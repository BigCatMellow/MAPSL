"""Regression checks for migration ledger omissions and false acceptance."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("migration_checker", Path(__file__).resolve().parents[1] / "migration/check_inventory.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


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


if __name__ == "__main__":
    unittest.main()
