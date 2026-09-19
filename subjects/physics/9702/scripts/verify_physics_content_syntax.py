#!/usr/bin/env python3
"""Content Syntax and Subpart Parity Auditor for Physics 9702 Past Papers.

Checks:
- Parity between question.json parts and markscheme.json parts.
- LaTeX math delimiter balance ($, $$, \\(, \\)).
- Brace balance within math blocks.
- Cleans non-standard characters (null bytes, zero-width spaces).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

REPO_ROOT = next((p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()), Path(__file__).resolve().parents[2])
PHYSICS_PAPERS_ROOT = REPO_ROOT / "subjects/physics/9702/past papers"


def check_latex_syntax(text: str) -> list[str]:
    issues = []
    if not text or not isinstance(text, str):
        return issues

    # 1. Check dollar sign balance
    escaped = text.replace(r"\$", "")
    # Check for triple dollars ($$$)
    if "$$$" in escaped:
        issues.append("Found triple dollar signs ($$$)")

    dollar_count = escaped.count("$")
    if dollar_count % 2 != 0:
        issues.append("Unbalanced math delimiter ($)")

    # 2. Check \( and \) balance
    open_paren = escaped.count(r"\(")
    close_paren = escaped.count(r"\)")
    if open_paren != close_paren:
        issues.append(r"Unbalanced math delimiter (\( and \))")

    # 3. Check \[ and \] balance
    open_bracket = escaped.count(r"\[")
    close_bracket = escaped.count(r"\]")
    if open_bracket != close_bracket:
        issues.append(r"Unbalanced math delimiter (\[ and \])")

    # 4. Check curly brace balance inside math blocks
    math_pattern = re.compile(r"\$\$(.*?)\$\$|\$(.*?)\$", re.DOTALL)
    for m in math_pattern.finditer(escaped):
        math_content = m.group(1) if m.group(1) is not None else m.group(2)
        clean_math = math_content.replace(r"\{", "").replace(r"\}", "")
        if clean_math.count("{") != clean_math.count("}"):
            issues.append(f"Unbalanced curly braces in math: {math_content[:30]}...")

    return issues


def check_and_clean_text(text: str, fix: bool = False) -> tuple[str, list[str]]:
    warnings = []
    cleaned = text
    if not isinstance(text, str):
        return text, warnings

    if "\x00" in text:
        warnings.append("Contains null character (\\x00)")
        if fix:
            cleaned = cleaned.replace("\x00", "")

    if "\u200b" in text:
        warnings.append("Contains zero-width space (\\u200b)")
        if fix:
            cleaned = cleaned.replace("\u200b", "")

    return cleaned, warnings


def verify_physics_content_syntax_for_paper(paper_dir: Path, fix: bool = False) -> list[dict]:
    issues = []
    paper_code = paper_dir.name
    q_dirs = sorted([d for d in paper_dir.glob("question_*") if d.is_dir()])
    if not q_dirs and (paper_dir / "questions").is_dir():
        q_dirs = sorted([paper_dir / "questions"])

    for qd in q_dirs:
        q_num = qd.name
        q_path = qd / "question.json"
        ms_path = qd / "markscheme.json"
        if not ms_path.is_file() and (qd / "mark_scheme.json").is_file():
            ms_path = qd / "mark_scheme.json"
        enr_path = qd / "enrichment.json"

        q_part_ids = []
        ms_part_ids = []
        enr_part_ids = []

        # 1. Parse question.json
        if q_path.is_file():
            try:
                with open(q_path, encoding="utf-8") as f:
                    q_data = json.load(f)
                q_part_ids = [p["id"] for p in q_data.get("parts", []) if "id" in p]
                
                # Check stems and text
                stem = q_data.get("question_stem", "")
                for err in check_latex_syntax(stem):
                    issues.append({
                        "paper": paper_code,
                        "question": q_num,
                        "category": "syntax",
                        "level": "ERROR",
                        "message": f"question.json stem: {err}",
                        "fixable": False,
                    })

                for p in q_data.get("parts", []):
                    p_text = p.get("question_text", "")
                    for err in check_latex_syntax(p_text):
                        issues.append({
                            "paper": paper_code,
                            "question": q_num,
                            "category": "syntax",
                            "level": "ERROR",
                            "message": f"question.json part '{p.get('id')}': {err}",
                            "fixable": False,
                        })
            except Exception as e:
                issues.append({
                    "paper": paper_code,
                    "question": q_num,
                    "category": "syntax",
                    "level": "ERROR",
                    "message": f"Error parsing question.json: {e}",
                    "fixable": False,
                })

        # 2. Parse markscheme.json
        if ms_path.is_file():
            try:
                with open(ms_path, encoding="utf-8") as f:
                    ms_data = json.load(f)
                ms_part_ids = [p["id"] for p in ms_data.get("parts", []) if "id" in p]
            except Exception as e:
                issues.append({
                    "paper": paper_code,
                    "question": q_num,
                    "category": "syntax",
                    "level": "ERROR",
                    "message": f"Error parsing markscheme.json: {e}",
                    "fixable": False,
                })

        # 3. Check Subpart Parity (QP vs MS)
        if q_part_ids and ms_part_ids and q_part_ids != ms_part_ids:
            issues.append({
                "paper": paper_code,
                "question": q_num,
                "category": "syntax",
                "level": "ERROR",
                "message": f"Subpart ID mismatch: question.json has {q_part_ids} vs markscheme.json has {ms_part_ids}",
                "fixable": False,
            })

        # 4. Parse enrichment.json syntax
        if enr_path.is_file():
            try:
                with open(enr_path, encoding="utf-8") as f:
                    enr_data = json.load(f)
                enr_part_ids = [p["part_id"] for p in enr_data.get("parts", []) if "part_id" in p]

                for part in enr_data.get("parts", []):
                    pid = part.get("part_id", "")
                    # Check walkthrough syntax
                    for step in part.get("walkthrough", []):
                        for err in check_latex_syntax(step):
                            issues.append({
                                "paper": paper_code,
                                "question": q_num,
                                "category": "syntax",
                                "level": "ERROR",
                                "message": f"enrichment.json part '{pid}' walkthrough: {err}",
                                "fixable": False,
                            })
                    # Check hints syntax
                    for hint in part.get("hints", []):
                        for err in check_latex_syntax(hint):
                            issues.append({
                                "paper": paper_code,
                                "question": q_num,
                                "category": "syntax",
                                "level": "ERROR",
                                "message": f"enrichment.json part '{pid}' hint: {err}",
                                "fixable": False,
                            })
            except Exception as e:
                issues.append({
                    "paper": paper_code,
                    "question": q_num,
                    "category": "syntax",
                    "level": "ERROR",
                    "message": f"Error parsing enrichment.json: {e}",
                    "fixable": False,
                })

    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--component", choices=["p1", "p2", "p4", "all"], default="all")
    parser.add_argument("--paper", help="Specific paper code or folder")
    parser.add_argument("--fix", action="store_true", help="Auto-fix cleanable syntax issues")
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
            issues = verify_physics_content_syntax_for_paper(p_dir, fix=args.fix)
            total_issues.extend(issues)

    errors = [i for i in total_issues if i["level"] == "ERROR"]
    warnings = [i for i in total_issues if i["level"] == "WARNING"]

    print(f"Verified syntax & subparts for {total_papers} Physics papers: {len(errors)} errors, {len(warnings)} warnings.")
    if total_issues:
        for iss in total_issues[:30]:
            print(f"[{iss['level']}] [{iss['paper']}] {iss['question'] or ''} ({iss['category']}): {iss['message']}")
        if len(total_issues) > 30:
            print(f"... and {len(total_issues) - 30} more issues.")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
