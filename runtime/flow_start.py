from __future__ import annotations

from contextlib import closing
from dataclasses import asdict
from pathlib import Path
import sqlite3
from typing import Any, Mapping, Sequence

from runtime.context_builder import build_context_plan
from runtime.skills import SkillCatalogError, SkillParseError, build_project_skill_catalog
from runtime.state import MutationResult, TaskStore
from runtime.state.common import parse_time, utc_now


def _mutation_payload(result: MutationResult) -> dict[str, Any]:
    return asdict(result)


def _failed(step: str, result: MutationResult | Mapping[str, Any]) -> dict[str, Any]:
    payload = _mutation_payload(result) if isinstance(result, MutationResult) else dict(result)
    return {
        "ok": False,
        "code": "FLOW_STEP_FAILED",
        "failed_step": step,
        "step_result": payload,
    }


def _prepare_environment_evidence(
    contract: Mapping[str, Any],
    repo_root: str | Path,
) -> dict[str, Any] | MutationResult:
    """Inspect a contracted environment before taking the startup write lock.

    Uses ``runtime.environment.safety.inspect_local_environment`` -- the
    containment-checked wrapper that will not follow dependency inputs outside
    the repo -- NOT the raw ``runtime.environment.fingerprint`` inspector. This
    adds no new probing capability: it composes two functions that already ship.
    """

    from runtime.environment.safety import inspect_local_environment
    from runtime.environment.spec import EnvironmentSpecError, load_environment_spec

    spec_ref = str(contract["spec_ref"])
    root = Path(repo_root)
    try:
        spec = load_environment_spec(root / spec_ref)
        fingerprint = inspect_local_environment(spec, repo_root=root)
    except (EnvironmentSpecError, OSError, ValueError, RuntimeError) as exc:
        return MutationResult(False, "ENVIRONMENT_INSPECTION_FAILED", str(exc))
    return {
        "spec": spec,
        "fingerprint": fingerprint,
        "spec_ref": spec_ref,
        "recorded_by": "maps-flow-start",
    }


def _startup_changed() -> dict[str, Any]:
    return _failed("claim", MutationResult(
        False,
        "STARTUP_TASK_CHANGED",
        "task definition or claim attempt changed during preparation; retry from current task state",
    ))


def _parse_runtime_limits(items: Sequence[str]) -> dict[str, int] | MutationResult:
    limits: dict[str, int] = {}
    for item in items:
        if "=" not in item:
            return MutationResult(
                False,
                "INVALID_RUNTIME_LIMIT",
                "runtime limits must use KEY=INT",
            )
        key, raw_value = item.split("=", 1)
        key = key.strip()
        try:
            value = int(raw_value)
        except ValueError:
            return MutationResult(
                False,
                "INVALID_RUNTIME_LIMIT",
                f"{key} must be an integer",
            )
        limits[key] = value
    return limits


def flow_start(
    store: TaskStore,
    task_id: str,
    *,
    worker_id: str,
    repo_root: str | Path = ".",
    created_by: str = "maps-flow-start",
    lease_seconds: int = 900,
    context_paths: Sequence[str | Path] = (),
    readable_paths: Sequence[str | Path] = (".",),
    writable_paths: Sequence[str | Path] | None = None,
    forbidden_paths: Sequence[str | Path] = (),
    runtime_limits: Mapping[str, int] | None = None,
    base_revision: str | None = None,
    require_worktree_binding: bool = False,
    require_write_scope_binding: bool = False,
) -> dict[str, Any]:
    """Start a deterministic local execution flow without provider launch.

    Check declared paths and claim eligibility, then prepare the context plan
    and any required environment observation. Bundled Skill discovery can
    register content-addressed catalog metadata independently of startup.
    Recheck the claim and task revision, then commit the claim, manifest and
    contracted environment evidence in one transaction. A failed write discards
    the entire new attempt.

    Invalid declared paths surface before a claim attempt, including when the
    same request would also fail to claim the task.

    It intentionally stops before choosing or launching a provider session.
    Per roadmap 6.9 / S6, a matched Skill whose trust-gate decision is `LOAD`
    has its hash-verified SKILL.md body attached to the plan
    (`plan["skills"][i]["body"]`, slice 1) plus an `execution_resources`
    manifest -- path / kind / size of its scripts/references/examples/assets,
    NEVER content (slice 2). WITHHELD / ON_DEMAND / DENIED Skills get neither,
    and resource *content* is only ever pulled on demand by a downstream
    consumer via `runtime.skills.load_skill_resource`.
    """

    preflight = store.preflight_run_context(
        repo_root=repo_root,
        context_paths=context_paths,
        readable_paths=readable_paths,
        forbidden_paths=forbidden_paths,
    )
    if preflight is not None:
        step = "context" if preflight.code == "INVALID_REPO_ROOT" else "run_manifest"
        return _failed(step, preflight)

    preview = store.preview_start_claim(task_id, worker_id, lease_seconds=lease_seconds)
    if not preview.ok:
        return _failed("claim", preview)
    task = preview.task
    revision = task["task_revision"]

    try:
        skill_catalog = build_project_skill_catalog(repo_root, store)
    except (SkillCatalogError, SkillParseError) as exc:
        return _failed(
            "skills",
            MutationResult(False, "SKILL_CATALOG_FAILED", str(exc)),
        )

    try:
        context_plan = build_context_plan(
            store, task_id, repo_root=repo_root, skill_catalog=skill_catalog
        )
    except ValueError as exc:
        return _failed(
            "context",
            MutationResult(False, "INVALID_REPO_ROOT", str(exc)),
        )
    if context_plan is None:
        return _failed(
            "context",
            MutationResult(False, "NOT_FOUND", f"{task_id} does not exist"),
        )
    if context_plan["task_revision"] != revision:
        return _startup_changed()

    preparation = store._prepare_run_manifest(
        worker_id,
        repo_root=repo_root,
        created_by=created_by,
        readable_paths=readable_paths,
        forbidden_paths=forbidden_paths,
        runtime_limits=runtime_limits,
        base_revision=base_revision,
        require_worktree_binding=require_worktree_binding,
    )
    if isinstance(preparation, MutationResult):
        return _failed("run_manifest", preparation)

    environment = None
    if task["environment"] is not None:
        environment = _prepare_environment_evidence(task["environment"], repo_root)
        if isinstance(environment, MutationResult):
            return _failed("environment_evidence", environment)

    step = "claim"
    try:
        # Each writer uses this connection without committing. Closing the
        # connection rolls back every new task write on failed checks or errors.
        with closing(store._connect()) as conn:
            conn.execute("BEGIN IMMEDIATE")
            claim = store._claim_task_conn(
                conn, task_id, worker_id, lease_seconds=lease_seconds,
            )
            if not claim.ok:
                return _failed(step, claim)
            if (
                claim.task["attempt"] != task["attempt"] + 1
                or store._task_revision_conn(conn, task_id) != revision
            ):
                return _startup_changed()

            step = "run_manifest"
            run = store._create_run_manifest_conn(
                conn,
                task_id,
                worker_id,
                preparation,
                created_by=created_by,
                context_paths=context_paths,
                writable_paths=writable_paths,
                require_write_scope_binding=require_write_scope_binding,
            )
            if not run.ok:
                return _failed(step, run)
            if environment is not None:
                step = "environment_evidence"
                evidence = store._record_run_environment_evidence_conn(
                    conn, run.task["run_id"], **environment,
                )
                if not evidence.ok:
                    return _failed(step, evidence)
            step = "commit"
            expiry = parse_time(claim.task["lease_expires_at"])
            if expiry is None or expiry <= utc_now():
                return _failed(step, MutationResult(
                    False, "LEASE_EXPIRED", "startup exceeded the requested lease before commit",
                ))
            conn.commit()
    except sqlite3.Error:
        return _failed(step, MutationResult(
            False, "STARTUP_TRANSACTION_FAILED", "could not commit startup to the task database",
        ))

    return {
        "ok": True,
        "code": "FLOW_STARTED",
        "task_id": task_id,
        "worker_id": worker_id,
        "claim": _mutation_payload(claim),
        "context_plan": context_plan,
        "run_manifest": run.task,
        "next_step": {
            "state": "STOPPED_BEFORE_PROVIDER_SESSION",
            "reason": (
                "flow start does not select workers, launch providers, attach "
                "sessions, or send messages"
            ),
        },
    }


def flow_start_from_runtime_limit_args(
    store: TaskStore,
    task_id: str,
    *,
    worker_id: str,
    repo_root: str | Path = ".",
    created_by: str = "maps-flow-start",
    lease_seconds: int = 900,
    context_paths: Sequence[str | Path] = (),
    readable_paths: Sequence[str | Path] = (".",),
    writable_paths: Sequence[str | Path] | None = None,
    forbidden_paths: Sequence[str | Path] = (),
    runtime_limit_args: Sequence[str] = (),
    base_revision: str | None = None,
    require_worktree_binding: bool = False,
    require_write_scope_binding: bool = False,
) -> dict[str, Any]:
    limits = _parse_runtime_limits(runtime_limit_args)
    if isinstance(limits, MutationResult):
        return _failed("options", limits)
    return flow_start(
        store,
        task_id,
        worker_id=worker_id,
        repo_root=repo_root,
        created_by=created_by,
        lease_seconds=lease_seconds,
        context_paths=context_paths,
        readable_paths=readable_paths,
        writable_paths=writable_paths,
        forbidden_paths=forbidden_paths,
        runtime_limits=limits or None,
        base_revision=base_revision,
        require_worktree_binding=require_worktree_binding,
        require_write_scope_binding=require_write_scope_binding,
    )
