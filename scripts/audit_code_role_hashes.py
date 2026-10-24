"""Audit code-file role headers and SHA-256 hashes against the canonical inventory.

Run at repository root:
    python scripts/audit_code_role_hashes.py
    python scripts/audit_code_role_hashes.py --write

Default checks role/provenance metadata and reports outdated hashes without modifying files.
--write refreshes only the sha256 column after all metadata checks pass.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "SOURCE_ROLE_AND_RELEASE_GATE.csv"
ROLES = {
    "SECTION_EXECUTABLE_STUDY": "EXECUTABLE",
    "ORIGINAL_PACKAGE_CANDIDATE": "EXECUTABLE",
    "AUTOMATED_TEST": "TEST",
    "ALTERNATIVE_QA_COPY": "INTERNAL_QA",
    "RECOVERED_EXAMPLE_OR_DEPENDENCY": "REFERENCE",
    "VERIFIED_REPRESENTATIVE_EXAMPLE": "REFERENCE",
    "INTENTIONAL_FAILURE_EDUCATIONAL": "INTENTIONAL_BUG",
    "PACKAGE_INITIALIZER": "REFERENCE",
    "EXECUTABLE_ENTRYPOINT_RECONSTRUCTED": "EXECUTABLE",
    "RECONSTRUCTED_SOURCE": "REFERENCE",
}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="Update SHA-256 inventory after validating metadata")
    args = ap.parse_args()
    with MANIFEST.open(newline="", encoding="utf-8-sig") as fp:
        reader = csv.DictReader(fp)
        fields = reader.fieldnames
        rows = list(reader)
    if not fields or len(rows) != 81:
        print("ERROR: expected 81 inventoried Python files", file=sys.stderr)
        return 2
    problems = []
    changed = 0
    for row in rows:
        path = ROOT / row["path"]
        if not path.is_file():
            problems.append(f"missing: {row['path']}")
            continue
        raw = path.read_bytes()
        decoded = raw.decode("utf-8-sig")
        for key, value in (
            ("CODE_COMPANION_ROLE", ROLES[row["role"]]),
            ("CODE_COMPANION_PROVENANCE", row["provenance"]),
        ):
            if f"# {key}: {value}" not in decoded[:1200]:
                problems.append(f"{row['path']}: incorrect {key}")
        calculated = hashlib.sha256(raw).hexdigest()
        if row["sha256"].lower() != calculated:
            changed += 1
        row["sha256"] = calculated
    if problems:
        for problem in problems:
            print("ERROR:", problem, file=sys.stderr)
        return 2
    print(f"Verified {len(rows)} role/provenance headers; {changed} SHA-256 values differ.")
    if args.write:
        with MANIFEST.open("w", newline="", encoding="utf-8-sig") as fp:
            writer = csv.DictWriter(fp, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        print("Updated SHA-256 inventory (no source files changed).")
    return 0 if args.write or changed == 0 else 1

if __name__ == "__main__":
    raise SystemExit(main())
