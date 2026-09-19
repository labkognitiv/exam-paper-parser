#!/usr/bin/env python3
"""Run the repository P2 question auditor over every enrichment in one paper."""

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--paper", required=True)
    args = parser.parse_args()

    repo = args.repo.resolve()
    root = repo / "subjects/physics/9702/enrichment/p2"
    files = sorted(root.glob(f"{args.paper}_q*.enrichment.json"))
    if not files:
        print(json.dumps({"paper": args.paper, "status": "FAIL", "errors": ["no enrichment files found"]}, indent=2))
        return 1

    results = []
    failed = False
    for path in files:
        question = path.stem.split("_q")[-1].split(".")[0]
        command = [
            sys.executable,
            str(repo / "scripts/audit_p2_question.py"),
            "--repo",
            str(repo),
            "--paper",
            args.paper,
            "--question",
            question,
        ]
        run = subprocess.run(command, capture_output=True, text=True, check=False)
        first_line = run.stdout.strip().splitlines()[0] if run.stdout.strip() else ""
        question_passed = run.returncode == 0 and first_line.endswith(" PASS")
        failed = failed or not question_passed
        results.append({
            "question": question,
            "returncode": run.returncode,
            "status": "PASS" if question_passed else "REVIEW_OR_FAIL",
            "stdout": run.stdout.strip(),
            "stderr": run.stderr.strip(),
        })

    print(json.dumps({"paper": args.paper, "status": "FAIL" if failed else "PASS", "results": results}, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
