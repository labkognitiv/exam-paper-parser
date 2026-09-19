#!/usr/bin/env python3
"""Fast, deterministic audit for one Physics 9702 P2 question."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


@dataclass(frozen=True)
class Finding:
    code: str
    kind: str
    artifact: str
    field: str
    message: str


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ordered_unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def registry(path: Path, collection: str) -> dict[str, dict[str, Any]]:
    records = load_json(path)[collection]
    result: dict[str, dict[str, Any]] = {}
    for record in records:
        keys = [key for key in record if key.endswith("_id")]
        if len(keys) != 1:
            continue
        value = record[keys[0]]
        result[value] = record
    return result


def add(
    findings: list[Finding],
    code: str,
    kind: str,
    path: Path,
    field: str,
    message: str,
) -> None:
    findings.append(Finding(code, kind, str(path), field, message))


def git_head_has(repo: Path, path: Path, record_id: str) -> bool | None:
    relative = path.relative_to(repo)
    proc = subprocess.run(
        ["git", "show", f"HEAD:{relative.as_posix()}"],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        return None
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None
    for value in data.values():
        if not isinstance(value, list):
            continue
        for record in value:
            if isinstance(record, dict) and record_id in record.values():
                return True
    return False


def check_schema(
    findings: list[Finding], record: dict[str, Any], schema: dict[str, Any], path: Path
) -> None:
    for error in Draft202012Validator(schema).iter_errors(record):
        field = ".".join(str(piece) for piece in error.absolute_path) or "root"
        add(findings, "SCHEMA", "fail", path, field, error.message)


def check_presentation(findings: list[Finding], question: dict[str, Any], path: Path) -> None:
    wrap_hits: list[str] = []
    stray_hits: list[str] = []
    latex_hits: list[str] = []
    dangling_hits: list[str] = []
    latex_syntax_hits: list[str] = []
    footer_hits: list[str] = []
    diagram_dump_hits: list[str] = []
    prose_in_math_hits: list[str] = []

    dangling_endings = (
        r"\b(?:of|the|and|between|with|in|to|from|a|an|is|that|for|or)\s*$"
    )
    footer_pattern = re.compile(
        r"©\s*UCLES|\bUCLES\b|\[Turn over|9702/\d{2}/[A-Z0-9]/|Permission to reproduce",
        re.IGNORECASE,
    )
    diagram_dump_pattern = re.compile(r"\(not to scale\)", re.IGNORECASE)
    prose_math_pattern = re.compile(r"\$[^$]{30,}\$")

    for part in question.get("parts", []):
        part_id = part.get("id", "unknown")
        for field in ("question_text", "question_text_latex"):
            text = part.get(field, "")
            lines = [l.strip() for l in text.splitlines() if l.strip()]
            if any(re.fullmatch(r"[A-Za-z]{1,2}", line) for line in lines):
                stray_hits.append(f"{part_id}.{field}")
            for before, after in zip(lines, lines[1:]):
                if any(token in before or token in after for token in ("___", "\\text", "=", "[", "]", "|")):
                    continue
                if re.match(r"\d+[.)]\s", after):
                    continue
                if before[-1] not in ".:;?!)]}" and re.match(r"[a-z0-9$]", after):
                    wrap_hits.append(f"{part_id}.{field}")
                    break
            if lines:
                last_line = lines[-1]
                if not any(token in last_line for token in ("___", "=", "[Total")):
                    if re.search(dangling_endings, last_line, re.IGNORECASE):
                        dangling_hits.append(f"{part_id}.{field}")

            if footer_pattern.search(text):
                footer_hits.append(f"{part_id}.{field}")
            if diagram_dump_pattern.search(text):
                diagram_dump_hits.append(f"{part_id}.{field}")

        latex = part.get("question_text_latex", "")
        if re.search(r"\$\s*(?:angle|magnitude|resultant)\b[^$]*=", latex, re.I):
            latex_hits.append(f"{part_id}.question_text_latex")

        # Check odd-indexed chunks (inside $ ... $)
        dollar_chunks = latex.split("$")
        if len(dollar_chunks) % 2 == 1:
            for math_chunk in dollar_chunks[1::2]:
                words = [w for w in math_chunk.split() if not w.startswith("\\")]
                if len(words) >= 4 and not re.search(r"\\text\{[^}]+\}", math_chunk):
                    prose_in_math_hits.append(f"{part_id}.question_text_latex")
                    break

        # LaTeX syntax & delimiter balance
        dollar_count = latex.count("$")
        if dollar_count % 2 != 0:
            latex_syntax_hits.append(f"{part_id}.question_text_latex (unbalanced $)")
        if latex.count("{") != latex.count("}"):
            latex_syntax_hits.append(f"{part_id}.question_text_latex (unbalanced braces)")

    if wrap_hits:
        add(
            findings,
            "PRESENTATION_OCR_WRAP",
            "fail",
            path,
            ", ".join(ordered_unique(wrap_hits)),
            "sentence split by page-width newline",
        )
    if stray_hits:
        add(
            findings,
            "PRESENTATION_STRAY_TEXT",
            "fail",
            path,
            ", ".join(ordered_unique(stray_hits)),
            "isolated 1–2 letter line; likely OCR junk",
        )
    if footer_hits:
        add(
            findings,
            "PRESENTATION_FOOTER_LEAK",
            "fail",
            path,
            ", ".join(ordered_unique(footer_hits)),
            "page footer, copyright, or exam code trapped in question text",
        )
    if diagram_dump_hits:
        add(
            findings,
            "PRESENTATION_DIAGRAM_DUMP",
            "fail",
            path,
            ", ".join(ordered_unique(diagram_dump_hits)),
            "raw diagram labels or '(not to scale)' dumped into prose",
        )
    if prose_in_math_hits:
        add(
            findings,
            "PRESENTATION_PROSE_IN_MATH",
            "fail",
            path,
            ", ".join(ordered_unique(prose_in_math_hits)),
            "multi-word English prose wrapped inside math mode $ ... $",
        )
    if dangling_hits:
        add(
            findings,
            "PRESENTATION_DANGLING_CLAUSE",
            "fail",
            path,
            ", ".join(ordered_unique(dangling_hits)),
            "text ends abruptly in a dangling preposition/conjunction",
        )
    if latex_hits:
        add(
            findings,
            "PRESENTATION_LATEX_PROSE",
            "fail",
            path,
            ", ".join(ordered_unique(latex_hits)),
            "ordinary answer-label prose is inside math mode",
        )
    if latex_syntax_hits:
        add(
            findings,
            "PRESENTATION_LATEX_SYNTAX",
            "fail",
            path,
            ", ".join(ordered_unique(latex_syntax_hits)),
            "unbalanced LaTeX delimiters or brackets",
        )


def check_content_flow(findings: list[Finding], question: dict[str, Any], path: Path) -> None:
    flow = question.get("content_flow")
    if not isinstance(flow, list) or not flow:
        add(findings, "CONTENT_FLOW_MISSING", "fail", path, "content_flow", "content_flow array missing or empty")
        return

    part_ids = [part.get("id") for part in question.get("parts", [])]
    flow_part_ids = []
    for idx, item in enumerate(flow):
        if not isinstance(item, dict) or "type" not in item:
            add(findings, "CONTENT_FLOW_INVALID", "fail", path, f"content_flow[{idx}]", "missing type")
            continue
        item_type = item.get("type")
        if item_type not in ("stem", "part"):
            add(findings, "CONTENT_FLOW_INVALID", "fail", path, f"content_flow[{idx}]", f"invalid type: {item_type}")
        if item_type == "part":
            pid = item.get("part_id")
            if not pid or pid not in part_ids:
                add(findings, "CONTENT_FLOW_INVALID", "fail", path, f"content_flow[{idx}]", f"unknown part_id: {pid}")
            else:
                flow_part_ids.append(pid)

    if flow_part_ids != part_ids:
        add(
            findings,
            "CONTENT_FLOW_MISMATCH",
            "fail",
            path,
            "content_flow",
            f"parts in flow {flow_part_ids} do not match question parts {part_ids}",
        )


def check_figures(findings: list[Finding], question: dict[str, Any], path: Path) -> None:
    figure_map = {}
    part_ids = {part.get("id") for part in question.get("parts", [])}
    for figure in question.get("figures", []):
        fig_id = figure.get("id")
        if not fig_id:
            add(findings, "FIGURE_MISSING_ID", "fail", path, "figures", "figure missing id")
            continue
        figure_map[fig_id] = figure
        img_file = figure.get("file")
        if not img_file:
            add(findings, "FIGURE_MISSING_FILE", "fail", path, f"figures.{fig_id}", "missing image file field")
        else:
            img_path = path.parent / img_file
            if not img_path.is_file():
                add(findings, "FIGURE_FILE_NOT_FOUND", "fail", path, f"figures.{fig_id}", f"file not found: {img_file}")
            elif img_path.stat().st_size == 0:
                add(findings, "FIGURE_FILE_EMPTY", "fail", path, f"figures.{fig_id}", f"file is 0 bytes: {img_file}")

        placement = figure.get("placement")
        if not isinstance(placement, dict):
            add(findings, "FIGURE_PLACEMENT", "fail", path, f"figures.{fig_id}", "missing placement dictionary")
        else:
            scope = placement.get("scope")
            position = placement.get("position")
            part_id = placement.get("part_id")
            if scope not in ("part", "question"):
                add(findings, "FIGURE_PLACEMENT", "fail", path, f"figures.{fig_id}.placement", f"invalid scope: {scope}")
            if position not in ("after_text", "after_stem", "after_stem_text", "response_background", "standalone"):
                add(findings, "FIGURE_PLACEMENT", "fail", path, f"figures.{fig_id}.placement", f"invalid position: {position}")
            if scope == "part" and part_id not in part_ids:
                add(findings, "FIGURE_PLACEMENT", "fail", path, f"figures.{fig_id}.placement", f"unknown part_id: {part_id}")

    for part in question.get("parts", []):
        part_id = part.get("id", "unknown")
        for fid in part.get("figure_ids", []):
            if fid not in figure_map:
                add(findings, "FIGURE_UNKNOWN_REF", "fail", path, part_id, f"references undeclared figure {fid}")


def check_response_schemas(findings: list[Finding], question: dict[str, Any], path: Path) -> None:
    figure_ids = {fig.get("id") for fig in question.get("figures", [])}
    for part in question.get("parts", []):
        part_id = part.get("id", "unknown")
        marks = part.get("marks")
        schema = part.get("response_schema")
        if marks is not None:
            if schema is None:
                add(findings, "RESPONSE_SCHEMA_MISSING", "fail", path, part_id, "answerable leaf requires response_schema")
            elif not isinstance(schema, dict) or schema.get("version") != "0.1":
                add(findings, "RESPONSE_SCHEMA_INVALID", "fail", path, part_id, "response_schema must have version 0.1")
            else:
                blocks = schema.get("blocks", [])
                if not isinstance(blocks, list) or not blocks:
                    add(findings, "RESPONSE_SCHEMA_INVALID", "fail", path, part_id, "response_schema blocks cannot be empty")
                for block in blocks:
                    if block.get("type") == "canvas":
                        bg = block.get("background_figure_id")
                        if bg and bg not in figure_ids:
                            add(findings, "RESPONSE_SCHEMA_INVALID", "fail", path, part_id, f"canvas background_figure_id {bg} not found in figures")
        else:
            if schema is not None:
                add(findings, "RESPONSE_SCHEMA_UNEXPECTED", "fail", path, part_id, "structural parent part should not have response_schema")


def check_git_immutability(findings: list[Finding], repo: Path, path: Path, code: str) -> None:
    relative = path.relative_to(repo)
    tracked = subprocess.run(
        ["git", "ls-files", "--error-unmatch", relative.as_posix()],
        cwd=repo,
        capture_output=True,
        check=False,
    )
    if tracked.returncode != 0:
        add(findings, code, "review", path, "root", "source is not tracked; hash baseline unknown")
        return
    changed = subprocess.run(
        ["git", "diff", "--quiet", "--", relative.as_posix()],
        cwd=repo,
        check=False,
    )
    if changed.returncode == 1:
        add(findings, code, "fail", path, "root", "tracked source differs from HEAD")
    elif changed.returncode > 1:
        add(findings, code, "review", path, "root", "could not check source against HEAD")


def audit(repo: Path, paper: str, question_number: int, check_git: bool = False) -> dict[str, Any]:
    qnum = f"{question_number:02d}"
    match = re.fullmatch(r"(9702_[msw]\d{2})_(\d{2})", paper)
    if not match:
        raise ValueError("paper must look like 9702_s21_23")
    stem, variant = match.groups()
    session_code = paper.split("_")[1]
    sessions = {"m": "february-march", "s": "may-june", "w": "october-november"}
    year = f"20{session_code[1:]}"
    session = sessions[session_code[0]]
    variant_dir = f"variant-{variant[1]}"
    paper_root = repo / "subjects/physics/9702/past papers/p2" / year / session / variant_dir
    question_path = paper_root / f"questions/question_{qnum}.json"
    mark_scheme_path = paper_root / f"mark-schemes/markscheme_{qnum}.json"
    enrichment_path = repo / "subjects/physics/9702/past papers/p2" / year / session / variant_dir / "enrichment" / f"{paper}_q{qnum}.enrichment.json"
    schema_path = repo / "subjects/physics/9702/knowledge/knowledge-base/contracts/question-enrichment.schema.json"
    base = repo / "subjects/physics/9702"

    for path in (question_path, mark_scheme_path, enrichment_path, schema_path):
        if not path.is_file():
            return {
                "paper": paper,
                "question": question_number,
                "status": "FAIL",
                "findings": [
                    asdict(Finding("MISSING_FILE", "fail", str(path), "root", "file missing"))
                ],
                "counts": {"fail": 1, "review": 0},
            }

    question = load_json(question_path)
    mark_scheme = load_json(mark_scheme_path)
    enrichment = load_json(enrichment_path)
    schema = load_json(schema_path)
    findings: list[Finding] = []

    check_schema(findings, enrichment, schema, enrichment_path)
    expected_id = f"{paper}_q{qnum}"
    for label, record, path in (
        ("question", question, question_path),
        ("mark scheme", mark_scheme, mark_scheme_path),
        ("enrichment", enrichment, enrichment_path),
    ):
        if record.get("question_id") != expected_id:
            add(findings, "IDENTITY", "fail", path, "question_id", f"{label} ID mismatch")
    if enrichment.get("component") != "P2":
        add(findings, "IDENTITY", "fail", enrichment_path, "component", "must be P2")

    canonical_ids = [part.get("id") for part in question.get("parts", [])]
    if len(canonical_ids) != len(set(canonical_ids)):
        add(findings, "DUPLICATE_PART", "fail", question_path, "parts", "duplicate canonical part ID")
    by_id = {part.get("id"): part for part in question.get("parts", [])}
    for index, part in enumerate(question.get("parts", []), 1):
        part_id = part.get("id", "unknown")
        if part.get("display_order") != index:
            add(findings, "PART_ORDER", "fail", question_path, part_id, "bad display_order")
        parent_id = part.get("parent_id")
        if parent_id is not None:
            parent = by_id.get(parent_id)
            if parent is None or part.get("path", [])[:-1] != parent.get("path", []):
                add(findings, "PART_HIERARCHY", "fail", question_path, part_id, "bad parent/path")

    answerable = [part for part in question.get("parts", []) if part.get("marks") is not None]
    actual_parts = enrichment.get("parts", [])
    actual_ids = [part.get("part_id") for part in actual_parts]
    expected_ids = [part.get("id") for part in answerable]
    if actual_ids != expected_ids:
        add(
            findings,
            "LEAF_ORDER",
            "fail",
            enrichment_path,
            "parts",
            f"expected {expected_ids}; got {actual_ids}",
        )
    if sum(part.get("marks", 0) for part in answerable) != question.get("total_marks"):
        add(findings, "MARK_TOTAL", "fail", question_path, "total_marks", "leaf marks do not add up")

    if enrichment.get("numerical_values_checked") is not False:
        add(
            findings,
            "NUMERICAL_REVIEW_FLAG",
            "fail",
            enrichment_path,
            "numerical_values_checked",
            "must exist and be false",
        )

    definitions = registry(base / "knowledge/knowledge-base/definitions.json", "definitions")
    formulas = registry(base / "knowledge/knowledge-base/formulas.json", "formulas")
    skills = registry(base / "knowledge/knowledge-base/skills.json", "skills")
    patterns = registry(base / "knowledge/knowledge-base/question-patterns.json", "patterns")

    taxonomy = load_json(base / "knowledge/2025-2027/as/9702-2025-2027-as-taxonomy.json")
    outcomes_data = load_json(
        base / "knowledge/2025-2027/as/9702-2025-2027-as-learning-outcomes.json"
    )
    topic_map: dict[str, dict[str, Any]] = {}
    module_map: dict[str, tuple[str, dict[str, Any]]] = {}
    for topic in taxonomy.get("topics", []):
        topic_map[topic["topic_id"]] = topic
        for module in topic.get("modules", []):
            module_map[module["module_id"]] = (topic["topic_id"], module)
    outcome_map = {item["outcome_id"]: item for item in outcomes_data.get("outcomes", [])}

    part_patterns: list[str] = []
    topic_ids: list[str] = []
    module_ids: list[str] = []
    outcome_ids: list[str] = []
    skill_use: dict[str, list[tuple[str, tuple[str, ...]]]] = {}
    boilerplate_pattern = re.compile(
        r"the task concerns|decide which physical principle controls|carries the preceding calculation|apply the official route|state the final result clearly",
        re.IGNORECASE,
    )

    for part in actual_parts:
        part_id = part.get("part_id", "unknown")
        current_patterns = part.get("question_patterns", [])
        part_patterns.extend(current_patterns)
        for pattern_id in current_patterns:
            if pattern_id not in patterns:
                add(findings, "UNKNOWN_PATTERN", "fail", enrichment_path, part_id, pattern_id)
        mapping = part.get("mapping", {})
        topic_id = mapping.get("primary_topic_id")
        module_id = mapping.get("primary_module_id")
        topic_ids.append(topic_id)
        module_ids.append(module_id)
        if topic_id not in topic_map:
            add(findings, "UNKNOWN_TOPIC", "fail", enrichment_path, part_id, str(topic_id))
        if module_id not in module_map or module_map[module_id][0] != topic_id:
            add(findings, "BAD_MODULE", "fail", enrichment_path, part_id, str(module_id))
        for outcome_id in mapping.get("outcome_ids", []):
            outcome_ids.append(outcome_id)
            outcome = outcome_map.get(outcome_id)
            if outcome is None:
                add(findings, "UNKNOWN_OUTCOME", "fail", enrichment_path, part_id, outcome_id)
            elif outcome.get("topic_id") != topic_id or outcome.get("module_id") != module_id:
                add(findings, "BAD_OUTCOME", "fail", enrichment_path, part_id, outcome_id)

        skill_data = part.get("skills", {})
        all_skills = [skill_data.get("primary_skill_id"), *skill_data.get("supporting_skill_ids", [])]
        for skill_id in all_skills:
            if skill_id not in skills:
                add(findings, "UNKNOWN_SKILL", "fail", enrichment_path, part_id, str(skill_id))
        primary_skill = skill_data.get("primary_skill_id")
        if primary_skill in skills:
            if topic_id not in skills[primary_skill].get("topic_ids", []):
                add(findings, "SKILL_TOPIC", "fail", enrichment_path, part_id, str(primary_skill))
            skill_use.setdefault(primary_skill, []).append((part_id, tuple(current_patterns)))

        refs = part.get("knowledge_refs", {})
        for definition_id in refs.get("definition_ids", []):
            if definition_id not in definitions:
                add(findings, "UNKNOWN_DEFINITION", "fail", enrichment_path, part_id, definition_id)
            elif topic_id and topic_id not in definitions[definition_id].get("topic_ids", []):
                add(findings, "DEFINITION_TOPIC", "fail", enrichment_path, part_id, f"{definition_id} not in topic {topic_id}")
        for formula_id in refs.get("formula_ids", []):
            if formula_id not in formulas:
                add(findings, "UNKNOWN_FORMULA", "fail", enrichment_path, part_id, formula_id)
            elif topic_id and topic_id not in formulas[formula_id].get("topic_ids", []):
                add(findings, "FORMULA_TOPIC", "fail", enrichment_path, part_id, f"{formula_id} not in topic {topic_id}")

        if "definition" in current_patterns and not refs.get("definition_ids"):
            add(findings, "DEFINITION_PATTERN_MISSING_ID", "fail", enrichment_path, part_id, "pattern 'definition' requires definition_ids")
        if refs.get("definition_ids") and "definition" not in current_patterns:
            add(findings, "DEFINITION_PATTERN_UNDECLARED", "fail", enrichment_path, part_id, "definition_ids referenced but 'definition' pattern undeclared")

        if set(current_patterns) & {"direct_calculation", "multi_step_calculation"}:
            if not refs.get("formula_ids") and not refs.get("formula_empty_justification"):
                add(findings, "FORMULA_NOT_EXPLAINED", "fail", enrichment_path, part_id, "no formula or reason")
        hints = part.get("hints", [])
        if not 1 <= len(hints) <= 5:
            add(findings, "HINT_COUNT", "fail", enrichment_path, part_id, "need 1–5 hints")
        if not part.get("walkthrough") or any(not str(x).strip() for x in part.get("walkthrough", [])):
            add(findings, "WALKTHROUGH_EMPTY", "fail", enrichment_path, part_id, "walkthrough empty")

        part_text = " ".join(hints + part.get("walkthrough", []) + [r.get("observable", "") for r in part.get("checking", {}).get("ai_rubric", [])])
        if boilerplate_pattern.search(part_text):
            add(findings, "BOILERPLATE_DETECTED", "fail", enrichment_path, part_id, "boilerplate filler phrase detected")

    expected_unions = {
        "question_patterns": ordered_unique(part_patterns),
        "topic_ids": ordered_unique(topic_ids),
        "module_ids": ordered_unique(module_ids),
        "outcome_ids": ordered_unique(outcome_ids),
    }
    actual_unions = {
        "question_patterns": enrichment.get("question_patterns", []),
        "topic_ids": enrichment.get("mapping", {}).get("topic_ids", []),
        "module_ids": enrichment.get("mapping", {}).get("module_ids", []),
        "outcome_ids": enrichment.get("mapping", {}).get("outcome_ids", []),
    }
    for key in expected_unions:
        if actual_unions[key] != expected_unions[key]:
            add(
                findings,
                "ORDERED_UNION",
                "fail",
                enrichment_path,
                key,
                f"expected {expected_unions[key]}; got {actual_unions[key]}",
            )

    for skill_id, uses in skill_use.items():
        pattern_set = {pattern for _, used_patterns in uses for pattern in used_patterns}
        record = skills[skill_id]
        description = f"{record.get('name', '')} {record.get('description', '')}".lower()
        mismatch = False
        if pattern_set & {"classification", "property_identification"}:
            mismatch = not any(
                word in description
                for word in ("classif", "distinguish", "property", "define", "example")
            )
        broad = len(pattern_set) >= 3 and len(uses) >= 4
        new_in_worktree = git_head_has(repo, base / "knowledge/knowledge-base/skills.json", skill_id) is False
        if mismatch or broad or new_in_worktree:
            leaf_ids = ", ".join(part_id for part_id, _ in uses)
            reasons = []
            if mismatch:
                reasons.append("description does not support classification/property leaves")
            if broad:
                reasons.append("one skill spans many different task patterns")
            if new_in_worktree:
                reasons.append("skill is new relative to HEAD")
            add(
                findings,
                "SKILL_NEEDS_REVIEW",
                "review",
                enrichment_path,
                leaf_ids,
                f"{skill_id}: {'; '.join(reasons)}",
            )

    check_content_flow(findings, question, question_path)
    check_figures(findings, question, question_path)
    check_response_schemas(findings, question, question_path)
    check_presentation(findings, question, question_path)
    if check_git:
        check_git_immutability(findings, repo, question_path, "CANONICAL_CHANGED")
        check_git_immutability(findings, repo, mark_scheme_path, "OFFICIAL_CHANGED")

    # Reuse the occurrence-aware source/criterion validator. Keep its full message only on failure.
    validator = repo / "scripts/validate_question_enrichment.py"
    proc = subprocess.run(
        [
            sys.executable,
            str(validator),
            "--enrichment",
            enrichment_path.relative_to(repo).as_posix(),
            "--question",
            question_path.relative_to(repo).as_posix(),
            "--mark-scheme",
            mark_scheme_path.relative_to(repo).as_posix(),
            "--schema",
            schema_path.relative_to(repo).as_posix(),
        ],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        message = " ".join(line.strip() for line in proc.stdout.splitlines() if line.strip())
        add(findings, "OFFICIAL_CRITERIA", "fail", mark_scheme_path, "criteria", message)

    fail_count = sum(item.kind == "fail" for item in findings)
    review_count = sum(item.kind == "review" for item in findings)
    return {
        "paper": paper,
        "question": question_number,
        "status": "FAIL" if fail_count else ("REVIEW" if review_count else "PASS"),
        "findings": [asdict(item) for item in findings],
        "counts": {
            "fail": fail_count,
            "review": review_count,
            "answerable_leaves": len(answerable),
        },
    }


def print_text(result: dict[str, Any]) -> None:
    print(f"Q{result['question']:02d} {result['status']}")
    for finding in result["findings"]:
        marker = "FAIL" if finding["kind"] == "fail" else "AI_CHECK"
        print(
            f"- {marker} {finding['code']} | {finding['field']} | {finding['message']}"
        )
    counts = result["counts"]
    print(f"Counts: {counts['fail']} fail, {counts['review']} AI check")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--paper", required=True, help="Example: 9702_s21_23")
    parser.add_argument("--question", required=True, type=int)
    parser.add_argument("--json", action="store_true", help="Print JSON instead of terse text")
    parser.add_argument(
        "--check-git",
        action="store_true",
        help="Also compare tracked canonical and official JSON with HEAD",
    )
    args = parser.parse_args()
    try:
        result = audit(args.repo.resolve(), args.paper, args.question, check_git=args.check_git)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"AUDIT ERROR: {error}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_text(result)
    return 1 if result["status"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
