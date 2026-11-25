"""Project Markdown file links from docs/wiki into GitHub's separate wiki repository."""
import argparse
import re
from pathlib import Path
from urllib.parse import quote, urlsplit


def project_links(source: str, root: Path, repository: str, revision: str) -> str:
    wiki = root / "docs/wiki"
    base = f"https://github.com/{repository}"

    def rewrite(match: re.Match) -> str:
        link = urlsplit(match[1])
        if link.scheme or link.netloc or not link.path:
            return match[0]
        target = (wiki / link.path).resolve()
        if not target.is_relative_to(root) or not target.exists():
            raise ValueError(f"Unresolved wiki source link: {match[1]}")
        if target.parent == wiki and target.suffix == ".md":
            url = f"{base}/wiki/{quote(target.stem)}"
        else:
            kind = "tree" if target.is_dir() else "blob"
            url = f"{base}/{kind}/{revision}/{quote(target.relative_to(root).as_posix())}"
        if link.query:
            url += "?" + link.query
        if link.fragment:
            url += "#" + link.fragment
        return f"]({url})"

    return re.sub(r"\]\(([^()\s]+)\)", rewrite, source)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Directory of copied wiki pages")
    parser.add_argument("repository", help="GitHub owner/repository")
    parser.add_argument("revision", help="Commit checked out for publication")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    for source in sorted((root / "docs/wiki").glob("*.md")):
        page = project_links(source.read_text(encoding="utf-8"), root, args.repository, args.revision)
        (args.output / source.name).write_text(page, encoding="utf-8")


if __name__ == "__main__":
    main()
