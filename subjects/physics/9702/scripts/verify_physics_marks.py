#!/usr/bin/env python3
"""Marks Reconciliation Auditor for Physics 9702 Past Papers.

Checks:
- Question part marks sum equals question total_marks.
- Mark scheme part marks sum equals markscheme total_marks.
- Question total_marks matches Mark Scheme total_marks.
- Paper total marks invariant for Cambridge Physics 9702:
  - P1 (Multiple Choice): exactly 40 marks.
  - P2 (AS Level Structured): exactly 60 marks.
  - P4 (A Level Structured): exactly 100 marks.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

REPO_ROOT = next((p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()), Path(__file__).resolve().parents[2])
PHYSICS_PAPERS_ROOT = REPO_ROOT / "subjects/physics/9702/past papers"

PHYSICS_PAPER_EXPECTED_TOTALS = {
    "p1": 40,
    "p2": 60,
    "p4": 100,
}


def preferred_markscheme_path(question_dir: Path) -> Path:
    """Use an explicitly approved additive review, otherwise the locked source."""
    reviewed = question_dir / "markscheme_reviewed.json"
    review_meta = question_dir / "markscheme_review_meta.json"
    if reviewed.is_file() and review_meta.is_file():
        try:
            meta = json.loads(review_meta.read_text(encoding="utf-8"))
            if (
                meta.get("status") == "PASS"
                and meta.get("review_kind") == "publisher_erratum_reconciliation"
                and meta.get("official_source_locked") is True
            ):
                return reviewed
        except (OSError, json.JSONDecodeError):
            pass
    return question_dir / "markscheme.json"


def verify_physics_marks_for_paper(paper_dir: Path, fix: bool = False) -> list[dict]:
    issues = []
    paper_code = paper_dir.name
    
    # Determine component (e.g. p1, p2, p4)
    component = None
    for p in paper_dir.parents:
        if p.name.lower() in PHYSICS_PAPER_EXPECTED_TOTALS:
            component = p.name.lower()
            break
            
    expected_paper_total = PHYSICS_PAPER_EXPECTED_TOTALS.get(component) if component else None

    # Support both question_* subdirectories and legacy questions/ folder
    q_dirs = sorted([d for d in paper_dir.glob("question_*") if d.is_dir()])
    if not q_dirs and (paper_dir / "questions").is_dir():
        q_dirs = sorted([paper_dir / "questions"])

    paper_q_marks_sum = 0
    paper_ms_marks_sum = 0

    for qd in q_dirs:
        q_num = qd.name

        # Load question.json or question_ocr.json
        q_path = qd / "question.json"
        if not q_path.is_file() and (qd / "question_ocr.json").is_file():
            q_path = qd / "question_ocr.json"
        q_parts_sum = None
        q_total = None
        q_data = None

        if q_path.is_file():
            try:
                with open(q_path, encoding="utf-8") as f:
                    q_data = json.load(f)
                q_total = q_data.get("total_marks")
                parts = q_data.get("parts", [])
                if parts:
                    part_marks = [p.get("marks") for p in parts if isinstance(p.get("marks"), (int, float))]
                    if len(part_marks) == len(parts):
                        q_parts_sum = sum(part_marks)
            except Exception as e:
                issues.append({
                    "paper": paper_code,
                    "question": q_num,
                    "category": "marks",
                    "level": "ERROR",
                    "message": f"Cannot parse question.json for marks: {e}",
                    "fixable": False,
                })

        # Load markscheme.json
        ms_path = preferred_markscheme_path(qd)
        if not ms_path.is_file() and (qd / "mark_scheme.json").is_file():
            ms_path = qd / "mark_scheme.json"

        ms_parts_sum = None
        ms_total = None
        ms_data = None

        if ms_path.is_file():
            try:
                with open(ms_path, encoding="utf-8") as f:
                    ms_data = json.load(f)
                ms_total = ms_data.get("total_marks")
                ms_parts = ms_data.get("parts", [])
                if ms_parts:
                    ms_part_marks = [p.get("marks") for p in ms_parts if isinstance(p.get("marks"), (int, float))]
                    if len(ms_part_marks) == len(ms_parts):
                        ms_parts_sum = sum(ms_part_marks)
            except Exception as e:
                issues.append({
                    "paper": paper_code,
                    "question": q_num,
                    "category": "marks",
                    "level": "ERROR",
                    "message": f"Cannot parse markscheme.json for marks: {e}",
                    "fixable": False,
                })

        # Check part marks sum vs total_marks in question.json
        if q_parts_sum is not None and q_total is not None:
            if q_parts_sum != q_total:
                can_fix = (ms_total is not None and q_parts_sum == ms_total)
                if fix and can_fix and q_data:
                    q_data["total_marks"] = q_parts_sum
                    with open(q_path, "w", encoding="utf-8") as f:
                        json.dump(q_data, f, indent=2, ensure_ascii=False)
                    q_total = q_parts_sum
                else:
                    issues.append({
                        "paper": paper_code,
                        "question": q_num,
                        "category": "marks",
                        "level": "ERROR",
                        "message": f"Question parts sum ({q_parts_sum}) != total_marks ({q_total})",
                        "fixable": can_fix,
                    })

        # Check part marks sum vs total_marks in markscheme.json
        if ms_parts_sum is not None and ms_total is not None:
            if ms_parts_sum != ms_total:
                can_fix = (q_total is not None and ms_parts_sum == q_total)
                if fix and can_fix and ms_data:
                    ms_data["total_marks"] = ms_parts_sum
                    with open(ms_path, "w", encoding="utf-8") as f:
                        json.dump(ms_data, f, indent=2, ensure_ascii=False)
                    ms_total = ms_parts_sum
                else:
                    issues.append({
                        "paper": paper_code,
                        "question": q_num,
                        "category": "marks",
                        "level": "ERROR",
                        "message": f"Markscheme parts sum ({ms_parts_sum}) != total_marks ({ms_total})",
                        "fixable": can_fix,
                    })

        # Check parity between Question and Mark Scheme
        effective_q_mark = q_total if q_total is not None else q_parts_sum
        effective_ms_mark = ms_total if ms_total is not None else ms_parts_sum

        if effective_q_mark is not None and effective_ms_mark is not None:
            if effective_q_mark != effective_ms_mark:
                issues.append({
                    "paper": paper_code,
                    "question": q_num,
                    "category": "marks",
                    "level": "ERROR",
                    "message": f"Mark mismatch: Question has {effective_q_mark} marks, MarkScheme has {effective_ms_mark} marks",
                    "fixable": False,
                })

        if effective_q_mark is not None:
            paper_q_marks_sum += effective_q_mark
        if effective_ms_mark is not None:
            paper_ms_marks_sum += effective_ms_mark

    # Check overall paper total invariant
    if expected_paper_total is not None and q_dirs:
        if paper_q_marks_sum != expected_paper_total:
            issues.append({
                "paper": paper_code,
                "question": None,
                "category": "marks",
                "level": "ERROR",
                "message": f"Physics {component.upper()} paper question marks sum is {paper_q_marks_sum}, expected {expected_paper_total}",
                "fixable": False,
            })
        if paper_ms_marks_sum != expected_paper_total:
            issues.append({
                "paper": paper_code,
                "question": None,
                "category": "marks",
                "level": "ERROR",
                "message": f"Physics {component.upper()} paper markscheme marks sum is {paper_ms_marks_sum}, expected {expected_paper_total}",
                "fixable": False,
            })

    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--component", choices=["p1", "p2", "p4", "all"], default="all")
    parser.add_argument("--paper", help="Specific paper code or folder")
    parser.add_argument("--fix", action="store_true", help="Auto-fix discrepancies where possible")
    args = parser.parse_args()

    components = ["p1", "p2", "p4"] if args.component == "all" else [args.component]
    total_papers = 0
    total_issues = []

    for comp in components:
        comp_dir = PHYSICS_PAPERS_ROOT / comp
        if not comp_dir.is_dir():
            continue
        paper_dirs = sorted([d for d in comp_dir.glob("*/*") if d.is_dir()])
        if args.paper:
            paper_dirs = [d for d in paper_dirs if args.paper in d.name]

        for p_dir in paper_dirs:
            total_papers += 1
            issues = verify_physics_marks_for_paper(p_dir, fix=args.fix)
            total_issues.extend(issues)

    errors = [i for i in total_issues if i["level"] == "ERROR"]
    warnings = [i for i in total_issues if i["level"] == "WARNING"]

    print(f"Verified marks for {total_papers} Physics papers: {len(errors)} errors, {len(warnings)} warnings.")
    if total_issues:
        for iss in total_issues[:30]:
            print(f"[{iss['level']}] [{iss['paper']}] {iss['question'] or ''} ({iss['category']}): {iss['message']}")
        if len(total_issues) > 30:
            print(f"... and {len(total_issues) - 30} more issues.")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
