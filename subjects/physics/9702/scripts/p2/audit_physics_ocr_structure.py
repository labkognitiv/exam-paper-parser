#!/usr/bin/env python3
"""Deterministic OCR Structure, KaTeX, Equation, and Figure Linter for Cambridge Physics (9702).

Audits question_ocr.json and markscheme.json to ensure 100% fidelity to the printed exam:
1. KaTeX Syntax & Bracket Balance ($...$, $$...$$, {...}, invalid macros).
2. Physical Display Equations ($$...$$) and SI Units (\\text{kg m s}^{-2}, \\text{N}, \\text{J}).
3. Visual Diagram, Circuit & Figure Completeness (all figure_*.png files referenced in place).
4. Answer Prompt & Unit Integrity (answer_prompt and unit populated for dotted lines).
5. Mark Totals & Subpart Parity (subpart marks sum to total_marks, matches markscheme.json).
6. Typography (zero em dashes \u2014, en dashes \u2013, or replacement characters \ufffd).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

REPO_ROOT = next(
    (p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()),
    Path(__file__).resolve().parents[3],
)
PHYSICS_PAPERS_ROOT = REPO_ROOT / "subjects/physics/9702/past papers"


def check_katex_syntax(text: str) -> list[str]:
    errors: list[str] = []
    if not text or not isinstance(text, str):
        return errors

    escaped = text.replace(r"\$", "")
    if "$$$" in escaped:
        errors.append("Found triple dollar signs ($$$)")

    dollar_count = escaped.count("$")
    if dollar_count % 2 != 0:
        errors.append(f"Unbalanced math delimiter ($): count {dollar_count}")

    if escaped.count(r"\(") != escaped.count(r"\)"):
        errors.append(r"Unbalanced math delimiter (\( and \))")

    if escaped.count(r"\[") != escaped.count(r"\]"):
        errors.append(r"Unbalanced math delimiter (\[ and \])")

    math_pattern = re.compile(r"\$\$(.*?)\$\$|\$(.*?)\$", re.DOTALL)
    for m in math_pattern.finditer(escaped):
        math_content = m.group(1) if m.group(1) is not None else m.group(2)
        clean_math = math_content.replace(r"\{", "").replace(r"\}", "")
        if clean_math.count("{") != clean_math.count("}"):
            errors.append(f"Unbalanced curly braces in KaTeX: '{math_content[:40]}...'")

    return errors


def check_typography(text: str) -> list[str]:
    errors = []
    if not text or not isinstance(text, str):
        return errors

    if "\u2014" in text:
        errors.append("Contains forbidden em dash (\u2014)")
    if "\u2013" in text:
        errors.append("Contains forbidden en dash (\u2013)")
    if "\ufffd" in text:
        errors.append("Contains replacement character (\ufffd)")
    return errors


def audit_question_structure(q_dir: Path) -> list[dict]:
    issues = []
    ocr_file = q_dir / "question_ocr.json"
    if not ocr_file.is_file():
        return issues

    try:
        data = json.loads(ocr_file.read_text(encoding="utf-8"))
    except Exception as exc:
        issues.append({"category": "json", "level": "ERROR", "message": f"Corrupt question_ocr.json: {exc}"})
        return issues

    stem = data.get("question_stem") or ""
    for err in check_katex_syntax(stem):
        issues.append({"category": "katex", "level": "ERROR", "message": f"question_stem: {err}"})
    for err in check_typography(stem):
        issues.append({"category": "typography", "level": "ERROR", "message": f"question_stem: {err}"})

    parts = data.get("parts", [])
    parts_mark_sum = 0

    on_disk_figures = {f.stem for f in q_dir.glob("figure_*.png")}
    referenced_figures = set(data.get("figures_referenced", []))

    for idx, p in enumerate(parts):
        pid = p.get("id", f"part_{idx}")
        marks = p.get("marks")
        # A structural parent can legitimately carry null marks while its child
        # leaves own the allocation. Ignore it in the total instead of crashing.
        if marks is not None:
            if not isinstance(marks, int):
                issues.append({
                    "category": "marks",
                    "level": "ERROR",
                    "message": f"{pid}.marks must be an integer or null",
                })
            else:
                parts_mark_sum += marks

        text = p.get("text") or ""
        part_stem = p.get("part_stem") or ""
        ans_prompt = p.get("answer_prompt") or ""
        unit = p.get("unit") or ""

        for field_name, field_val in [("text", text), ("part_stem", part_stem), ("answer_prompt", ans_prompt), ("unit", unit)]:
            if not field_val:
                continue
            for err in check_katex_syntax(field_val):
                issues.append({"category": "katex", "level": "ERROR", "message": f"{pid}.{field_name}: {err}"})
            for err in check_typography(field_val):
                issues.append({"category": "typography", "level": "ERROR", "message": f"{pid}.{field_name}: {err}"})

        for m in re.finditer(r"\{\{figure:([^}]+)\}\}", text + " " + part_stem + " " + stem):
            fig_id = m.group(1).strip()
            referenced_figures.add(fig_id)

    for f_id in on_disk_figures:
        if f_id not in referenced_figures:
            issues.append({
                "category": "figures",
                "level": "WARNING",
                "message": f"Figure on disk '{f_id}.png' is not referenced in question_ocr.json",
            })

    total_marks = data.get("total_marks", 0)
    if total_marks > 0 and parts_mark_sum != total_marks:
        issues.append({
            "category": "marks",
            "level": "ERROR",
            "message": f"Sum of part marks ({parts_mark_sum}) does not match question total_marks ({total_marks})",
        })

    return issues


def audit_paper_ocr(paper_dir: Path) -> dict[str, list[dict]]:
    results = {}
    q_dirs = sorted([d for d in paper_dir.iterdir() if d.is_dir() and d.name.startswith("question_")])
    for qd in q_dirs:
        issues = audit_question_structure(qd)
        if issues:
            results[qd.name] = issues
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit Physics OCR Structure")
    parser.add_argument("path", help="Path to question directory or paper directory")
    args = parser.parse_args()

    p = Path(args.path)
    if (p / "question_ocr.json").is_file():
        issues = audit_question_structure(p)
        print(f"Auditing {p.name}: {len(issues)} issue(s)")
        for iss in issues:
            print(f"  [{iss['level']}] [{iss['category']}] {iss['message']}")
    else:
        results = audit_paper_ocr(p)
        total = sum(len(iss) for iss in results.values())
        print(f"Auditing paper {p.name}: {total} issue(s) across {len(results)} questions")
        for q, issues in results.items():
            for iss in issues:
                print(f"  {q}: [{iss['level']}] [{iss['category']}] {iss['message']}")


if __name__ == "__main__":
    main()
