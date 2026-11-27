from __future__ import annotations

import argparse
from datetime import timedelta
import hashlib
import json
from pathlib import Path
import tempfile
from typing import Any

from runtime.decision import DecisionBroker, DecisionConfig
from runtime.flow_handoff import flow_handoff
from runtime.flow_review import flow_review_record, flow_review_start
from runtime.flow_start import flow_start
from runtime.state import TaskStore
from runtime.state.common import utc_now


def smoke_contract() -> dict[str, Any]:
    return {
        "title": "Smoke lifecycle",
        "outcome": "Disposable task reaches DONE through guarded lifecycle",
        "task_type": "IMPLEMENTATION",
        "owner": "smoke-owner",
        "risk": "MEDIUM",
        "decision_authority": "disposable smoke state only",
        "verification": "this smoke lifecycle",
        "evidence_expected": "smoke evidence string",
        "review_required": "INDEPENDENT_REVIEW",
        "escalation": "stop on any failed guarded transition",
        "inputs": ["README.md"],
        "sources": ["AGENTS.md"],
        "dependencies": [],
        "output_paths": ["scratch/smoke-output.txt"],
        "non_goals": ["no live project mutation"],
        "acceptance_criteria": ["task reaches DONE"],
        "stop_conditions": ["any guard rejects expected valid transition"],
        "policy": {
            "requires_operator_approval": False,
            "destructive_action": False,
            "external_side_effect": False,
            "security_sensitive": False,
            "broad_architecture": False,
            "paid_execution": False,
        },
    }


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def _run_operating_workflow(store: TaskStore, task_id: str, repo: Path) -> dict[str, str]:
    """Exercise guarded runtime paths with fixture identities and local evidence."""
    repo.mkdir()
    (repo / "AGENTS.md").write_text("Work only in this smoke workspace.\n", encoding="utf-8")
    context = repo / "README.md"
    context.write_text("Produce one local smoke artifact.\n", encoding="utf-8")

    previous = "smoke-previous"
    worker = "smoke-worker"
    claimed = store.claim_task(
        task_id, previous, lease_seconds=60, now=utc_now() - timedelta(minutes=2)
    )
    require(claimed.ok, claimed.message)
    handoff = flow_handoff(
        store, task_id, from_worker=previous, to_worker=worker, reason="expired smoke claim"
    )
    require(handoff["ok"], f"flow handoff failed: {handoff}")
    require(
        store.get_task(task_id)["claimed_by"] == previous,
        "handoff transferred the task before the replacement claimed it",
    )
    started = flow_start(store, task_id, worker_id=worker, repo_root=repo, context_paths=[context])
    require(started["ok"], f"flow start failed: {started}")
    require(started["claim"]["code"] == "RECOVERED", "flow start did not recover the expired claim")
    require(
        started["next_step"]["state"] == "STOPPED_BEFORE_PROVIDER_SESSION",
        "flow start missed the provider launch boundary",
    )
    require(
        started["context_plan"]["coverage"]["root_agents_authority"],
        "flow start did not load the workspace authority",
    )
    run = started["run_manifest"]
    expected_context = {
        "path": context.name,
        "sha256": hashlib.sha256(context.read_bytes()).hexdigest(),
    }
    require(run["context_refs"] == [expected_context], "manifest did not bind the actual context bytes")

    artifact = repo / "scratch" / "smoke-output.txt"
    artifact.parent.mkdir()
    artifact.write_text("Disposable operating workflow complete.\n", encoding="utf-8")
    artifact_ref = f"sha256:{hashlib.sha256(artifact.read_bytes()).hexdigest()}"
    submitted = store.submit_task(task_id, worker, artifact_ref, run_id=run["run_id"])
    require(submitted.ok, submitted.message)
    submission_count = submitted.task["submission"]["submission_count"]
    linkage = store.get_submission_run_link(task_id, submission_count)
    require(
        linkage is not None and linkage["run_id"] == run["run_id"],
        "submission lost its run binding",
    )

    # Fixture review does not use environment-selected providers.
    broker = DecisionBroker(DecisionConfig())
    denied = flow_review_start(store, task_id, reviewer_id=previous, decision_broker=broker)
    require(
        not denied["ok"] and denied["step_result"]["code"] == "CONTINUITY_REVIEW_FORBIDDEN",
        "continuation identity was not refused independent review",
    )
    reviewer = "smoke-reviewer"
    review = flow_review_start(
        store, task_id, reviewer_id=reviewer, run_id=run["run_id"],
        artifact_refs=[artifact_ref], decision_broker=broker,
    )
    require(review["ok"], f"flow review-start failed: {review}")
    subject = review["review_subject"]
    require(
        subject["freshness_mode"] == "REVISION_BOUND"
        and subject["run_id"] == run["run_id"]
        and subject["artifact_refs"] == [artifact_ref]
        and subject["task_revision"] == run["task_revision"],
        "review did not bind the submitted run and artifact",
    )
    recorded = flow_review_record(
        store, task_id, reviewer_id=reviewer, verdict="APPROVED",
        summary="independent smoke criteria verified",
    )
    require(recorded["ok"], f"flow review-record failed: {recorded}")
    return {
        "claim": started["claim"]["code"],
        "handoff": handoff["code"],
        "continuation_review": denied["step_result"]["code"],
        "review": recorded["code"],
        "artifact_ref": artifact_ref,
    }


def _checkpointed_route(store: TaskStore, root: Path) -> dict[str, Any]:
    from runtime.policy import WorkerProfile
    from runtime.routing.service import route_project

    return route_project(
        store,
        [WorkerProfile("smoke-worker", "core")],
        halt_path=root / "halt.json",
        checkpoint_path=root / "langgraph-checkpoints.db",
        thread_id="maps-smoke",
        decision_config=DecisionConfig(),
    )


def run_smoke(*, with_langgraph: bool = False, with_hcom: bool = False) -> dict[str, Any]:
    result: dict[str, Any] = {}
    with tempfile.TemporaryDirectory(prefix="maps-smoke-") as td:
        root = Path(td)
        task_db = root / "maps.db"
        store = TaskStore(task_db)
        settings = store.connection_settings()
        require(settings["foreign_keys"] == 1, "SQLite foreign keys are not enabled")
        require(str(settings["journal_mode"]).lower() == "wal", "SQLite WAL is not enabled")
        require(settings["busy_timeout"] == 5000, "SQLite busy timeout is not 5000ms")

        created = store.create_task(title="Smoke lifecycle")
        require(created.ok, created.message)
        require(created.task is not None, "create_task returned no task payload")
        task_id = created.task["task_id"]
        shaped = store.update_contract(task_id, smoke_contract())
        require(shaped.ok, shaped.message)
        validated = store.validate_ready(task_id)
        require(validated.ok, "; ".join(validated.reasons))
        promoted = store.promote_ready(task_id, actor="smoke-shaper")
        require(promoted.ok, promoted.message)
        if with_langgraph:
            task_before = store.get_task(task_id)
            events_before = store.list_events(task_id)
            ready_route = _checkpointed_route(store, root)
            require(
                ready_route["route"] == "claim_or_assign"
                and ready_route["task_id"] == task_id
                and ready_route["worker_id"] == "smoke-worker",
                "LangGraph did not propose the READY task",
            )
            require(
                store.get_task(task_id) == task_before and store.list_events(task_id) == events_before,
                "routing mutated canonical task state",
            )
            result["langgraph"] = {"ready_proposal": ready_route["route"]}
        result["operating_workflow"] = _run_operating_workflow(store, task_id, root / "workspace")
        final = store.get_task(task_id)
        require(final is not None and final["status"] == "DONE", "smoke task did not reach DONE")
        result["sqlite_task_lifecycle"] = {
            "ok": True,
            "task_id": task_id,
            "status": final["status"],
            "settings": settings,
        }

        if with_langgraph:
            checkpoint_db = root / "langgraph-checkpoints.db"
            route = _checkpointed_route(store, root)
            require(route["route"] == "wait_or_reconcile", "unexpected idle LangGraph route")
            require(checkpoint_db.exists(), "LangGraph checkpoint DB was not created")
            require(checkpoint_db.resolve() != task_db.resolve(), "checkpoint DB equals task DB")
            result["langgraph"].update(ok=True, route=route["route"])

        if with_hcom:
            from runtime.communication import HcomAdapter

            adapter = HcomAdapter(hcom_dir=root / ".hcom")
            version = adapter.version()
            require(version.ok, "hcom --version failed")
            result["hcom"] = {"ok": True, "version": version.stdout.strip()}

    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run disposable MAPS Lean smoke checks")
    parser.add_argument("--with-langgraph", action="store_true")
    parser.add_argument("--with-hcom", action="store_true")
    args = parser.parse_args(argv)
    try:
        result = run_smoke(with_langgraph=args.with_langgraph, with_hcom=args.with_hcom)
    except Exception as exc:
        print(json.dumps({"ok": False, "error": type(exc).__name__, "message": str(exc)}, indent=2))
        return 1
    print(json.dumps({"ok": True, "checks": result}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
