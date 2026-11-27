"""Regression checks for migration ledger omissions and false acceptance."""
import importlib.util
from pathlib import Path
import re
import unittest

spec = importlib.util.spec_from_file_location("migration_checker", Path(__file__).resolve().parents[1] / "migration/check_inventory.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

ROADMAPS = checker.ROOT / "work" / "roadmaps"


class MigrationCoverageTests(unittest.TestCase):
    def setUp(self):
        self.row = dict(zip(checker.FIELDS, ["a.py", "a" * 40, "100644", "10", "PENDING", "", "", ""]))
        self.baseline = {"a.py": self.row.copy()}

    def test_missing_and_mutated_metadata_are_rejected(self):
        self.assertTrue(checker.verify(self.baseline, {}, {}))
        changed = dict(self.row, blob_sha="b" * 40)
        self.assertTrue(checker.verify(self.baseline, {"a.py": changed}, {}))

    def test_pending_is_valid_for_staging_but_not_cutover(self):
        self.assertEqual([], checker.verify(self.baseline, self.baseline, {}))
        self.assertTrue(checker.verify(self.baseline, self.baseline, {}, cutover=True))

    def test_exact_stage_requires_matching_blob_and_mode(self):
        row = dict(self.row, destination_or_source_pointer="a.py", evidence="staged-exact:" + "a" * 40)
        self.assertEqual([], checker.verify(self.baseline, {"a.py": row}, {"a.py": ("100644", "a" * 40)}))
        self.assertTrue(checker.verify(self.baseline, {"a.py": row}, {"a.py": ("100755", "a" * 40)}))

    def test_exact_migration_requires_destination_and_evidence(self):
        row = dict(self.row, disposition="MIGRATE", destination_or_source_pointer="a.py", rationale="unchanged", evidence="verified")
        self.assertEqual([], checker.verify(self.baseline, {"a.py": row}, {"a.py": ("100644", "a" * 40)}, cutover=True))
        self.assertTrue(checker.verify(self.baseline, {"a.py": row}, {}, cutover=True))

    def test_terminal_adaptation_requires_bound_content_and_mode(self):
        row = dict(self.row, disposition="IMPROVE", destination_or_source_pointer="a.py",
                   rationale="verified change", evidence="adapted:" + "b" * 40)
        current = {"a.py": row}
        self.assertEqual([], checker.verify(self.baseline, current, {"a.py": ("100644", "b" * 40)}))
        for mode, blob in [("100755", "b" * 40), ("100644", "c" * 40)]:
            self.assertTrue(checker.verify(self.baseline, current, {"a.py": (mode, blob)}))

    def test_reference_requires_exact_pinned_path(self):
        row = dict(self.row, disposition="REFERENCE", rationale="historical",
                   evidence="inspection", destination_or_source_pointer=checker.source_url("a.py"))
        self.assertEqual([], checker.verify(self.baseline, {"a.py": row}, {}))
        row["destination_or_source_pointer"] = checker.source_url("wrong.py")
        self.assertTrue(checker.verify(self.baseline, {"a.py": row}, {}))

    def test_duplicate_inventory_row_rejected(self):
        header = "\t".join(checker.FIELDS)
        line = "\t".join(self.row[k] for k in checker.FIELDS)
        with self.assertRaises(ValueError):
            checker.parse("\n".join([header, line, line]))


class CapabilityPlanCoverageTests(unittest.TestCase):
    def test_source_capabilities_have_one_owner_and_an_evidence_based_exit(self):
        text = (ROADMAPS / "CAPABILITY_CHECKLIST.md").read_text(encoding="utf-8")
        owners = {
            "Direction and continuity",
            "Execution and reliability",
            "Safety and evidence",
            "Reasoning and context",
            "Learning and evaluation",
            "Usability and portability",
        }
        baseline_ids = {
            f"{prefix}{index}"
            for prefix, count in (("H", 6), ("S", 7), ("E", 7), ("SEC", 7), ("L", 9), ("6.", 35))
            for index in range(1, count + 1)
        } | {"D0", "D1", "D2a", "D2b", "D2c", "D3", "D4", "D5", "D6"}
        dispositions = {"VERIFIED", "VERIFY", "FINISH", "CONDITIONAL", "RETIRED"}
        found = set()
        sections = set()
        owner = None
        for line in text.splitlines():
            if line.startswith("## "):
                owner = line[3:]
                if owner in owners:
                    self.assertNotIn(owner, sections)
                    sections.add(owner)
                continue
            if not line.startswith("| ["):
                continue
            cells = [cell.strip() for cell in line.split("|")[1:-1]]
            self.assertEqual(len(cells), 6, line)
            match = re.fullmatch(r"\[([^\]]+)\]\(([^)]+)\)", cells[0])
            self.assertIsNotNone(match, line)
            capability, source = match.groups()
            with self.subTest(capability=capability):
                self.assertNotIn(capability, found)
                self.assertIn(owner, owners)
                self.assertIn(cells[3], dispositions)
                self.assertTrue(all(cells), "missing capability, source, evidence or next step")
                if capability in baseline_ids:
                    self.assertIn(
                        "MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/",
                        source,
                    )
            found.add(capability)
        self.assertEqual(owners, sections)
        self.assertFalse(baseline_ids - found, "lost pinned source capability")


if __name__ == "__main__":
    unittest.main()
