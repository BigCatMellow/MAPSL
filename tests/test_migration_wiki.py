from pathlib import Path
import re
import unittest

from tools.project_wiki_links import project_links


ROOT = Path(__file__).resolve().parents[1]
REPO = "BigCatMellow/MAPSL"
REVISION = "1" * 40


class WikiProjectionTests(unittest.TestCase):
    def test_all_source_links_resolve_and_leave_the_legacy_authority(self):
        for path in sorted((ROOT / "docs/wiki").glob("*.md")):
            with self.subTest(page=path.name):
                source = path.read_text(encoding="utf-8")
                self.assertNotIn("BigCatMellow/MAPS_Lean/blob/main/", source)
                projected = project_links(source, ROOT, REPO, REVISION)
                self.assertNotRegex(projected, r"\]\(\.\./")
                self.assertEqual(len(re.findall(r"\]\(", projected)), len(re.findall(r"\]\(", source)))

    def test_wiki_and_committed_source_have_distinct_targets(self):
        source = "[Help](Home.md) [Rules](../../AGENTS.md#navigation) [State](../../runtime/)"
        url = f"https://github.com/{REPO}"
        self.assertEqual(
            project_links(source, ROOT, REPO, REVISION),
            f"[Help]({url}/wiki/Home) [Rules]({url}/blob/{REVISION}/AGENTS.md#navigation) "
            f"[State]({url}/tree/{REVISION}/runtime)",
        )
