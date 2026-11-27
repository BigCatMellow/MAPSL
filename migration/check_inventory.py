#!/usr/bin/env python3
"""Read-only migration ledger coverage check; does not certify semantic parity."""
import argparse
import csv
from urllib.parse import quote
import subprocess
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
BASE = "9c7bd19a4579c8804428bf898ea5e24810ea8355"
LEDGER = "migration/source-inventory.tsv"
FIELDS = ("source_path", "blob_sha", "git_mode", "bytes", "disposition",
          "destination_or_source_pointer", "rationale", "evidence")
STATES = {"PENDING", "MIGRATE", "IMPROVE", "CONSOLIDATE", "REPLACE",
          "DEFER", "RETIRE", "REFERENCE"}


def git(*args, root=ROOT):
    return subprocess.check_output(["git", *args], cwd=root, text=True)


def parse(text):
    reader = csv.DictReader(text.splitlines(), delimiter="\t")
    if tuple(reader.fieldnames or ()) != FIELDS:
        raise ValueError("unexpected ledger columns")
    result = {}
    for row in reader:
        path = row["source_path"]
        if not path or path in result or None in row or any(v is None for v in row.values()):
            raise ValueError(f"malformed or duplicate row: {path!r}")
        result[path] = row
    return result


def local_path(value):
    path = PurePosixPath(value)
    return bool(value) and not path.is_absolute() and ".." not in path.parts


def source_url(path):
    return ("https://github.com/BigCatMellow/MAPS_Lean/blob/"
            "605ce610e0be3334d1da7af2a7c6f5912b6cc05f/" + quote(path))


def verify(baseline, current, tracked, cutover=False):
    errors = []
    if baseline.keys() != current.keys():
        errors.append("source path set changed")
    for path in baseline.keys() & current.keys():
        old, row = baseline[path], current[path]
        if any(old[k] != row[k] for k in FIELDS[:4]):
            errors.append(f"{path}: immutable source metadata changed")
        state = row["disposition"]
        pointer, rationale, evidence = (row[k] for k in FIELDS[5:])
        if state not in STATES:
            errors.append(f"{path}: unknown disposition")
            continue
        if state == "PENDING":
            if cutover:
                errors.append(f"{path}: still pending")
            if evidence.startswith(("staged-exact:", "staged-adapted:")):
                mode, blob = tracked.get(pointer, ("", ""))
                if not local_path(pointer) or blob != evidence.split(":", 1)[1]:
                    errors.append(f"{path}: staged destination hash absent/changed")
                if evidence.startswith("staged-exact:") and (blob, mode) != (row["blob_sha"], row["git_mode"]):
                    errors.append(f"{path}: exact staging differs from source")
            continue
        if not all((pointer.strip(), rationale.strip(), evidence.strip())):
            errors.append(f"{path}: terminal disposition needs pointer, rationale, evidence")
        if state in {"MIGRATE", "IMPROVE", "CONSOLIDATE", "REPLACE"}:
            if not local_path(pointer) or pointer not in tracked:
                errors.append(f"{path}: successor destination not tracked")
            if state == "MIGRATE" and tracked.get(pointer) != (row["git_mode"], row["blob_sha"]):
                errors.append(f"{path}: exact migration differs from source")
            if state == "IMPROVE":
                mode, blob = tracked.get(pointer, ("", ""))
                if mode != row["git_mode"] or evidence != "adapted:" + blob:
                    errors.append(f"{path}: adapted destination hash or mode changed")
        elif state in {"REFERENCE", "RETIRE", "DEFER"}:
            if pointer != source_url(path) and pointer not in tracked:
                errors.append(f"{path}: missing source or successor reference")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cutover", action="store_true", help="require all file dispositions")
    args = parser.parse_args()
    old = parse(git("show", f"{BASE}:{LEDGER}"))
    new = parse((ROOT / LEDGER).read_text(encoding="utf-8"))
    tracked = {}
    for entry in git("ls-tree", "-rz", "HEAD").split("\0"):
        if entry:
            meta, path = entry.split("\t", 1)
            mode, kind, blob = meta.split()
            if kind == "blob":
                tracked[path] = (mode, blob)
    errors = verify(old, new, tracked, args.cutover)
    if len(old) != 3515:
        errors.append("unexpected baseline size")
    for error in errors[:40]:
        print(error)
    print(f"{len(new)} rows; {sum(r['disposition'] == 'PENDING' for r in new.values())} pending; {len(errors)} errors")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
