from importlib.util import find_spec
import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

from runtime.smoke import run_smoke


class SmokeInstallTests(unittest.TestCase):
    def test_disposable_state_smoke_reaches_done(self):
        with patch.dict(os.environ, {"MAPS_DECISION_PROVIDER": "not-a-provider"}):
            result = run_smoke()
        lifecycle = result["sqlite_task_lifecycle"]
        self.assertTrue(lifecycle["ok"])
        self.assertEqual(lifecycle["status"], "DONE")
        self.assertEqual(lifecycle["settings"]["foreign_keys"], 1)
        self.assertEqual(str(lifecycle["settings"]["journal_mode"]).lower(), "wal")
        workflow = result["operating_workflow"]
        self.assertEqual(workflow["claim"], "RECOVERED")
        self.assertEqual(workflow["handoff"], "FLOW_HANDOFF_RECORDED")
        self.assertEqual(workflow["continuation_review"], "CONTINUITY_REVIEW_FORBIDDEN")
        self.assertEqual(workflow["review"], "FLOW_REVIEW_RECORDED")

    @unittest.skipUnless(find_spec("langgraph"), "LangGraph is optional for this smoke")
    def test_smoke_routes_ready_work_without_mutating_task_state(self):
        with patch.dict(os.environ, {"MAPS_DECISION_PROVIDER": "not-a-provider"}):
            langgraph = run_smoke(with_langgraph=True)["langgraph"]
        self.assertEqual(
            langgraph, {"ok": True, "ready_proposal": "claim_or_assign", "route": "wait_or_reconcile"}
        )

    def test_learning_imports_without_loading_task_store_first(self):
        result = subprocess.run(
            [sys.executable, "-c", "import runtime.operational_learning"],
            cwd=Path(__file__).resolve().parents[1],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_smoke_has_no_legacy_or_migration_execution_dependency(self):
        source = Path(__file__).parents[1] / "runtime" / "smoke.py"
        text = source.read_text(encoding="utf-8")
        self.assertNotIn("legacy/", text)
        self.assertNotIn("migration/", text)
        self.assertNotIn("MAP_System", text)

    def test_installer_is_preview_first_and_non_system(self):
        source = Path(__file__).parents[1] / "scripts" / "install_maps.sh"
        text = source.read_text(encoding="utf-8")
        self.assertIn("APPLY=0", text)
        self.assertIn("--apply", text)
        self.assertIn("Mode: PREVIEW", text)
        self.assertNotIn("sudo ", text)
        self.assertNotIn("apt install", text)
        self.assertNotIn("wezterm", text.lower())
        self.assertNotIn("legacy/", text)
        self.assertNotIn("migration/", text)

    def test_installer_does_not_embed_credentials(self):
        source = Path(__file__).parents[1] / "scripts" / "install_maps.sh"
        text = source.read_text(encoding="utf-8").lower()
        for secret_assignment in (
            "openai_api_key=",
            "anthropic_api_key=",
            "api_key=",
            "token=",
        ):
            self.assertNotIn(secret_assignment, text)


if __name__ == "__main__":
    unittest.main()
