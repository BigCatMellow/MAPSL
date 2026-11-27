"""The reviewed revision must identify an immutable commit."""
import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts.check_review_evidence import check


class ReviewRevisionTests(unittest.TestCase):
    def test_only_full_commit_object_ids_are_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def git(*args):
                return subprocess.check_output(["git", "-C", directory, *args], text=True).strip()
            git("init", "-q")
            git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                "commit", "--allow-empty", "-qm", "base")
            commit, tree = git("rev-parse", "HEAD"), git("rev-parse", "HEAD^{tree}")
            record = root / "work/reviews/pr-1-review-evidence.md"
            record.parent.mkdir(parents=True)
            for revision, accepted in [(commit, True), (tree, False), ("HEAD", False)]:
                with self.subTest(revision=revision):
                    record.write_text(
                        f"reviewer: fixture\nhead_sha: {revision}\nindependent: true\nsummary: fixture\n",
                        encoding="utf-8",
                    )
                    self.assertEqual(check("1", root)[0], accepted)
