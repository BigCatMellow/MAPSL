"""Offline comparison against the normal lesson APIs on disposable state."""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import statistics
import tempfile
from time import perf_counter_ns
from unittest.mock import patch

from runtime.context_builder import build_context_plan
from runtime.outcome_lesson_candidate import (
    OutcomeLessonCandidateError,
    build_outcome_lesson_candidate,
)
from runtime.smoke import smoke_contract
from runtime.state import TaskStore
from runtime.state.common import iso_z


FIXTURE_DIR = Path(__file__).resolve().parent
CLOCK = datetime(2030, 1, 1, tzinfo=timezone.utc)
ORIGIN = "TASK-LESSON-ORIGIN"
CONSUMER = "TASK-LESSON-CONSUMER"
OPERATOR = "fixture-operator"


def checked(result):
    if not result.ok:
        raise RuntimeError(f"{result.code}: {result.message}")
    return result.task


def source_rejection(store, lesson):
    """Probe the existing canonical builder again and compare the exact proof."""
    if lesson["source_kind"] != "TASK_OUTCOME":
        return None
    outcome_refs = [ref[8:] for ref in lesson["source_refs"] if ref.startswith("outcome:")]
    if len(outcome_refs) != 1 or not outcome_refs[0].isascii() or not outcome_refs[0].isdigit():
        return "Missing exact outcome reference"
    try:
        rebuilt = build_outcome_lesson_candidate(
            store,
            int(outcome_refs[0]),
            claim=lesson["claim"],
            applicability=lesson["applicability"],
            created_by=lesson["created_by"],
            created_at=lesson["created_at"],
        )
    except OutcomeLessonCandidateError as exc:
        return str(exc)
    if rebuilt["source_refs"] != lesson["source_refs"]:
        return "Saved source references differ from canonical evidence"
    return None


class FixtureStore(TaskStore):
    """Read counter and optional filter for the normal Context Builder call."""

    def __init__(self, path):
        self.count_reads = False
        self.selects = 0
        self.check_sources = False
        self.admission_rejections = {}
        super().__init__(path)

    def _connect(self):
        conn = super()._connect()
        if self.count_reads:
            conn.set_trace_callback(self._count_select)
        return conn

    def _count_select(self, statement):
        if statement.lstrip().upper().startswith("SELECT"):
            self.selects += 1

    def list_active_operational_lessons(self):
        active = super().list_active_operational_lessons()
        if not self.check_sources:
            return active
        admitted = []
        for lesson in active:
            reason = source_rejection(self, lesson)
            if reason is None:
                admitted.append(lesson)
            else:
                self.admission_rejections[lesson["lesson_id"]] = reason
        return admitted

    def measure(self, action):
        self.selects = 0
        self.count_reads = True
        started = perf_counter_ns()
        try:
            result = action()
            return result, {"milliseconds": (perf_counter_ns() - started) / 1e6, "selects": self.selects}
        finally:
            self.count_reads = False


def plan_at(store, repo, at):
    with patch("runtime.context_builder.datetime") as clock:
        clock.now.return_value = at
        return build_context_plan(store, CONSUMER, repo_root=repo)


def record_outcome(store, run_id, day, *, supersedes=None, status="FAILURE"):
    with patch("runtime.state.outcomes.utc_now", return_value=CLOCK + timedelta(days=day)):
        result = checked(store.record_outcome(
            ORIGIN, status, source="fixture verification", run_id=run_id,
            actor_class="OPERATOR", actor_id=OPERATOR, supersedes_outcome_id=supersedes,
        ))
    return result["outcome_record"]["id"]


def seed(store, repo, case):
    contract = smoke_contract()
    owner = contract["owner"]
    for task_id in (ORIGIN, CONSUMER):
        checked(store.create_task(task_id=task_id, project_id=case["family"]))
        checked(store.update_contract(task_id, contract))
    checked(store.promote_ready(ORIGIN, actor="fixture-shaper"))
    checked(store.claim_task(ORIGIN, owner))
    kind = case.get("source", "outcome")
    run_id = None
    if kind != "outcome_without_run":
        run_id = checked(store.create_run_manifest(
            ORIGIN, owner, repo_root=repo, created_by=owner,
        ))["run_id"]
    checked(store.submit_task(ORIGIN, owner, "fixture evidence", run_id=run_id))
    checked(store.claim_review(ORIGIN, "fixture-reviewer"))
    checked(store.record_review(ORIGIN, "fixture-reviewer", "APPROVED", "verified fixture"))
    outcome_id = record_outcome(store, run_id, 0)

    scope = case.get("scope", "project")
    mismatch = case.get("mismatch", False)
    applicability = {
        "global": scope == "global",
        "project_ids": ["another-project" if mismatch else case["family"]] if scope == "project" else [],
        "task_types": ["RESEARCH" if mismatch else contract["task_type"]] if scope == "task_type" else [],
        "risk_levels": [],
        "path_prefixes": [],
    }
    record = build_outcome_lesson_candidate(
        store, outcome_id, claim=case["claim"], applicability=applicability,
        created_by="fixture-observer", created_at=iso_z(CLOCK),
    )
    if kind == "other":
        record.update(source_kind="OPERATOR_OBSERVATION", source_refs=["fixture:operator-observation"])
    elif kind == "missing_outcome":
        record["source_refs"] = ["outcome:99999"]
    elif kind == "missing_binding":
        record["source_refs"] = [f"outcome:{outcome_id}"]
    if kind in {"other", "missing_outcome", "missing_binding"}:
        record["lesson_id"] = f"LESSON-FIXTURE-{case['id']}"
    checked(store.record_operational_lesson_candidate(record, created_by=record["created_by"]))
    return run_id, outcome_id, record


def run_case(case, *, recheck):
    with tempfile.TemporaryDirectory(prefix="maps-lesson-eval-") as directory:
        repo = Path(directory)
        (repo / "AGENTS.md").write_text("Local fixture authority only.\n", encoding="utf-8")
        (repo / "README.md").write_text("Disposable learning fixture.\n", encoding="utf-8")
        store = FixtureStore(repo / "fixture.sqlite")
        run_id, outcome_id, lesson = seed(store, repo, case)
        lesson_id = lesson["lesson_id"]
        task_before = store.get_task(CONSUMER)
        origin_before = store.get_task(ORIGIN)
        at = CLOCK + timedelta(days=10)
        before = plan_at(store, repo, at)
        promotion = "SKIPPED"
        measurements = {}
        reasons = {}
        decisions = []
        for day, event in enumerate(case.get("events", ["promote"]), start=1):
            when = CLOCK + timedelta(days=day)
            decision_ref = f"fixture:{case['id']}:{event}"
            if event == "promote":
                def promote():
                    if recheck:
                        reason = source_rejection(store, store.get_operational_lesson(lesson_id))
                        if reason is not None:
                            return "REFUSED", reason
                    checked(store.promote_operational_lesson(
                        lesson_id, decision_ref=decision_ref, promoted_by=OPERATOR,
                        starts_at=iso_z(when), review_at=iso_z(CLOCK + timedelta(days=30)),
                        expires_at=iso_z(CLOCK + timedelta(days=9)) if case.get("window") == "expired" else None,
                        now=when,
                    ))
                    return "PROMOTED", "LESSON_PROMOTED"

                (promotion, reasons["promotion"]), measurements["promotion"] = store.measure(promote)
                if promotion == "PROMOTED":
                    decisions.append(("PROMOTE", decision_ref))
            elif event in {"correct_source", "unrelated_outcome"}:
                supersedes = outcome_id if event == "correct_source" else None
                record_outcome(store, run_id, day, supersedes=supersedes, status="SUCCESS")
            elif event == "retire":
                checked(store.retire_operational_lesson(
                    lesson_id, decision_ref=decision_ref, retired_by=OPERATOR,
                    retired_at=iso_z(when), now=when,
                ))
                decisions.append(("RETIRE", decision_ref))
            else:
                raise ValueError(f"Unknown fixture event: {event}")

        store.check_sources = recheck
        plan, measurements["admission"] = store.measure(lambda: plan_at(store, repo, at))
        guidance = plan["guidance"]
        stored = store.get_operational_lesson(lesson_id)
        history = store.list_operational_lesson_decisions(lesson_id)
        assert [(row["decision_kind"], row["decision_payload"]["decision_ref"]) for row in history] == decisions
        assert all(row["decided_by"] == OPERATOR for row in history)
        assert stored["source_refs"] == lesson["source_refs"]
        assert store.get_task(CONSUMER) == task_before and store.get_task(ORIGIN) == origin_before
        for key in ("authority", "boundaries", "task_revision"):
            assert before[key] == plan[key], (case["id"], key)
        if guidance:
            assert len(guidance) == 1 and guidance[0]["lesson_id"] == lesson_id
            assert guidance[0]["authority"] == "GUIDANCE_ONLY"
            assert guidance[0]["source_refs"] == lesson["source_refs"]
            assert guidance[0]["promotion_decision_ref"] == decisions[0][1]
        baseline_reasons = {item["lesson_id"]: item["reason"] for item in plan["withheld_guidance"]}
        reasons["admission"] = store.admission_rejections.get(
            lesson_id, baseline_reasons.get(lesson_id, "GUIDANCE_ONLY" if guidance else stored["status"]),
        )
        return {
            "decision": [promotion, "ADMITTED" if guidance else "WITHHELD"],
            "reasons": reasons,
            "measurements": measurements,
        }


def summarize(rows):
    summary = {}
    for phase in ("promotion", "admission"):
        pairs = [(row["baseline"]["measurements"], row["recheck"]["measurements"]) for row in rows]
        comparisons = [(base[phase], probe[phase]) for base, probe in pairs if phase in base]
        summary[phase] = {
            "pairs": len(comparisons),
            "baseline_median_ms": statistics.median(x["milliseconds"] for x, _ in comparisons),
            "recheck_median_ms": statistics.median(y["milliseconds"] for _, y in comparisons),
            "total_extra_selects": sum(y["selects"] - x["selects"] for x, y in comparisons),
            "max_extra_selects_per_pair": max(y["selects"] - x["selects"] for x, y in comparisons),
        }
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("split", choices=("dev", "holdout"))
    args = parser.parse_args()
    fixture = json.loads((FIXTURE_DIR / f"lesson-source-freshness-{args.split}-v1.json").read_text())
    cases = fixture["cases"]
    count = 8 if args.split == "dev" else 16
    assert fixture["version"] == 1 and len(cases) == count
    assert len({case["family"] for case in cases}) == len({case["id"] for case in cases}) == count
    assert sum(case["expected"][1] == "ADMITTED" for case in cases) == count // 2
    rows = []
    for idx, case in enumerate(cases):
        arms = (False, True) if idx % 2 == 0 else (True, False)
        results = {recheck: run_case(case, recheck=recheck) for recheck in arms}
        rows.append({
            "id": case["id"], "expected": case["expected"],
            "baseline": results[False], "recheck": results[True],
        })
    passed = sum(row["recheck"]["decision"] == row["expected"] for row in rows)
    print(json.dumps({
        "split": args.split, "baseline_correct": sum(row["baseline"]["decision"] == row["expected"] for row in rows),
        "recheck_correct": passed, "cases": rows, "costs": summarize(rows),
    }, indent=2))
    return 0 if passed == count else 1


if __name__ == "__main__":
    raise SystemExit(main())
