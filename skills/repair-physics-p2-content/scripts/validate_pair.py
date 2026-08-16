#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


BLOCK_TYPES = {"fields", "table", "canvas", "proposed_type"}
CONTROLS = {
    "long_text", "short_text", "number", "quantity", "math_expression",
    "single_choice", "multiple_choice",
}
CANVAS_MODES = {"blank_drawing", "annotate_figure", "draw_on_scaffold"}
PLACEMENT_POSITIONS = {"after_stem", "after_stem_text", "after_text", "response_background"}
RAW_LATEX_IN_PLAIN = re.compile(r"\\[A-Za-z]+|[{}]|\^[{(]?[-+0-9]|[A-Za-z]_[A-Za-z0-9{]")


def unique(values: list[str], label: str, errors: list[str]) -> None:
    duplicates = sorted({value for value in values if values.count(value) > 1})
    if duplicates:
        errors.append(f"duplicate {label}: {', '.join(duplicates)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("question_json", type=Path)
    parser.add_argument("markscheme_json", type=Path)
    args = parser.parse_args()
    question = json.loads(args.question_json.read_text())
    markscheme = json.loads(args.markscheme_json.read_text())
    errors: list[str] = []

    if not isinstance(question.get("schema_version"), str) or not question.get("schema_version"):
        errors.append("missing question schema_version")
    if not isinstance(markscheme.get("schema_version"), str) or not markscheme.get("schema_version"):
        errors.append("missing mark-scheme schema_version")
    if question.get("question_id") != markscheme.get("question_id"):
        errors.append("question_id mismatch")
    if question.get("total_marks") != markscheme.get("total_marks") and question.get("official_reconciliation") is None:
        errors.append("total_marks mismatch")

    stem = question.get("question_stem", "")
    stem_latex = question.get("question_stem_latex", "")
    if stem and not stem_latex:
        errors.append("question_stem has no question_stem_latex")
    if RAW_LATEX_IN_PLAIN.search(stem):
        errors.append("raw LaTeX-like notation in question_stem")
    if stem_latex.count("$") % 2:
        errors.append("unbalanced math delimiters in question_stem_latex")

    parts = question.get("parts", [])
    part_ids = [part.get("id", "") for part in parts]
    unique(part_ids, "question part IDs", errors)
    part_map = {part.get("id"): part for part in parts}
    display_orders = [part.get("display_order") for part in parts]
    if display_orders != list(range(1, len(parts) + 1)):
        errors.append("part display_order must be unique, sequential and match array order")
    for part in parts:
        parent_id = part.get("parent_id")
        if parent_id and parent_id not in part_map:
            errors.append(f"unknown parent_id in {part.get('id')}: {parent_id}")
        elif parent_id and part_ids.index(parent_id) >= part_ids.index(part.get("id")):
            errors.append(f"parent must precede child: {part.get('id')}")

    flow = question.get("content_flow")
    if not isinstance(flow, list):
        errors.append("missing content_flow")
        flow = []
    flow_part_ids: list[str] = []
    stem_entries = 0
    for entry in flow:
        if not isinstance(entry, dict) or entry.get("type") not in {"stem", "part"}:
            errors.append("invalid content_flow entry")
            continue
        if entry.get("type") == "stem":
            stem_entries += 1
        else:
            flow_part_ids.append(entry.get("part_id", ""))
    if flow_part_ids != part_ids:
        errors.append("content_flow parts must match parts array order exactly")
    expected_stems = 1 if stem else 0
    if stem_entries != expected_stems:
        errors.append(f"content_flow stem count {stem_entries} != {expected_stems}")

    verification = question.get("verification")
    verification_keys = {"content_structure_checked", "marks_reconciled", "numerical_values_checked"}
    if not isinstance(verification, dict) or set(verification) != verification_keys:
        errors.append("verification must contain exactly the registered status fields")
    elif any(not isinstance(verification[key], bool) for key in verification_keys):
        errors.append("verification status values must be boolean")
    else:
        if not verification["content_structure_checked"]:
            errors.append("content structure is not verified")
        if not verification["marks_reconciled"]:
            errors.append("marks are not reconciled")

    children = {part.get("parent_id") for part in parts if part.get("parent_id")}
    answerable = {part.get("id") for part in parts if part.get("marks") is not None and part.get("id") not in children}
    for part in parts:
        plain = part.get("question_text", "")
        latex = part.get("question_text_latex", "")
        if plain and not latex:
            errors.append(f"question_text has no question_text_latex: {part.get('id')}")
        if RAW_LATEX_IN_PLAIN.search(plain):
            errors.append(f"raw LaTeX-like notation in question_text: {part.get('id')}")
        if latex.count("$") % 2:
            errors.append(f"unbalanced math delimiters in question_text_latex: {part.get('id')}")
        schema = part.get("response_schema")
        if part.get("id") in answerable and not schema:
            errors.append(f"missing response_schema: {part.get('id')}")
        if part.get("id") in children and schema:
            errors.append(f"structural parent has response_schema: {part.get('id')}")
        if not schema:
            continue
        if schema.get("version") != "0.1":
            errors.append(f"unsupported response_schema version in {part.get('id')}")
        if not isinstance(schema.get("blocks"), list) or not schema.get("blocks"):
            errors.append(f"response_schema has no blocks: {part.get('id')}")
            continue
        block_ids: list[str] = []
        field_ids: list[str] = []
        for block in schema.get("blocks", []):
            block_ids.append(block.get("block_id", ""))
            if not block.get("block_id"):
                errors.append(f"missing block_id in {part.get('id')}")
            if block.get("type") not in BLOCK_TYPES:
                errors.append(f"unknown block type in {part.get('id')}")
            block_type = block.get("type")
            if block_type == "fields" and (not isinstance(block.get("fields"), list) or not block.get("fields")):
                errors.append(f"fields block has no fields in {part.get('id')}")
            if block_type == "canvas":
                if block.get("mode") not in CANVAS_MODES:
                    errors.append(f"invalid canvas mode in {part.get('id')}")
                if not isinstance(block.get("tools"), list) or not block.get("tools"):
                    errors.append(f"canvas has no tools in {part.get('id')}")
                if block.get("mode") != "blank_drawing" and not block.get("background_figure_id"):
                    errors.append(f"canvas has no background figure in {part.get('id')}")
            if block_type == "table":
                if not isinstance(block.get("rows"), list) or not block.get("rows"):
                    errors.append(f"table has no rows in {part.get('id')}")
                if not isinstance(block.get("columns"), list) or not block.get("columns"):
                    errors.append(f"table has no columns in {part.get('id')}")
            if block_type == "proposed_type":
                if not block.get("observed_pattern") or not block.get("reason_registered_types_fail"):
                    errors.append(f"incomplete proposed_type in {part.get('id')}")
                if schema.get("registry_review_required") is not True:
                    errors.append(f"proposed_type requires registry review in {part.get('id')}")
                errors.append(f"unresolved proposed_type in {part.get('id')}")
            for field in block.get("fields", []):
                field_ids.append(field.get("field_id", ""))
                if not field.get("field_id"):
                    errors.append(f"missing field_id in {part.get('id')}")
                if field.get("control") not in CONTROLS:
                    errors.append(f"unknown control in {part.get('id')}")
                if not isinstance(field.get("role"), str) or not field.get("role"):
                    errors.append(f"missing field role: {field.get('field_id')}")
                if not isinstance(field.get("required"), bool):
                    errors.append(f"field required must be boolean: {field.get('field_id')}")
                if field.get("unit") and not field.get("unit_latex"):
                    errors.append(f"unit has no unit_latex: {field.get('field_id')}")
                if "$" in field.get("unit_latex", "") or "$" in field.get("label_latex", ""):
                    errors.append(f"field LaTeX must not contain delimiters: {field.get('field_id')}")
                if field.get("control") in {"single_choice", "multiple_choice"}:
                    if not isinstance(field.get("options"), list) or not field.get("options"):
                        errors.append(f"choice field has no options: {field.get('field_id')}")
        unique(block_ids, f"block IDs in {part.get('id')}", errors)
        unique(field_ids, f"field IDs in {part.get('id')}", errors)

    figure_ids = {figure.get("id") for figure in question.get("figures", [])}
    for figure in question.get("figures", []):
        figure_file = args.question_json.parent / figure.get("file", "")
        if not figure_file.is_file():
            errors.append(f"missing figure file: {figure.get('file')}")
        placement = figure.get("placement")
        if not isinstance(placement, dict) or placement.get("position") not in PLACEMENT_POSITIONS:
            errors.append(f"invalid figure placement: {figure.get('id')}")
            continue
        position = placement.get("position")
        if position == "after_stem" and (placement.get("scope") != "question" or not stem):
            errors.append(f"invalid after_stem placement: {figure.get('id')}")
        if position == "after_stem_text":
            anchor = placement.get("anchor", "")
            if placement.get("scope") != "question" or not anchor or stem.count(anchor) != 1:
                errors.append(f"invalid after_stem_text placement: {figure.get('id')}")
        if position in {"after_text", "response_background"}:
            part_id = placement.get("part_id")
            if placement.get("scope") != "part" or part_id not in part_map:
                errors.append(f"invalid part figure placement: {figure.get('id')}")
            elif position == "after_text":
                anchor = placement.get("anchor", "")
                if not anchor or part_map[part_id].get("question_text", "").count(anchor) != 1:
                    errors.append(f"figure placement anchor must occur once: {figure.get('id')}")
            else:
                canvas_ids = {
                    block.get("background_figure_id")
                    for block in part_map[part_id].get("response_schema", {}).get("blocks", [])
                    if block.get("type") == "canvas"
                }
                if figure.get("id") not in canvas_ids:
                    errors.append(f"response background is not used by canvas: {figure.get('id')}")
    for part in parts:
        for figure_id in part.get("figure_ids", []):
            if figure_id not in figure_ids:
                errors.append(f"unknown figure reference in {part.get('id')}: {figure_id}")
        for dependency in part.get("dependencies", []):
            if dependency.get("type") == "figure" and dependency.get("id") not in figure_ids:
                errors.append(f"unknown figure dependency in {part.get('id')}")
            if dependency.get("type") == "previous_response":
                dependency_id = dependency.get("part_id")
                if dependency_id not in part_map or part_ids.index(dependency_id) >= part_ids.index(part.get("id")):
                    errors.append(f"invalid previous_response dependency in {part.get('id')}")
        for block in part.get("response_schema", {}).get("blocks", []):
            background_id = block.get("background_figure_id")
            if background_id and background_id not in figure_ids:
                errors.append(f"unknown canvas background in {part.get('id')}: {background_id}")

    reconciliation = question.get("official_reconciliation")
    if reconciliation is not None:
        if question.get("official_part_mapping"):
            errors.append("official_reconciliation cannot be combined with official_part_mapping")
        validate_official_reconciliation(
            question, markscheme, reconciliation, args.markscheme_json, answerable, errors
        )
        if errors:
            for error in errors:
                print(f"FAIL: {error}")
            return 1
        print("PASS")
        return 0

    ms_parts = markscheme.get("parts", [])
    ms_part_ids = [part.get("id", "") for part in ms_parts]
    unique(ms_part_ids, "mark-scheme part IDs", errors)
    mappings = question.get("official_part_mapping", [])
    mapped_ms_ids: set[str] = set()
    mapped_question_ids: set[str] = set()
    for mapping in mappings:
        ms_id = mapping.get("markscheme_part_id")
        question_ids = mapping.get("question_part_ids")
        if ms_id not in ms_part_ids or not isinstance(question_ids, list) or len(question_ids) < 2:
            errors.append("invalid official_part_mapping")
            continue
        if ms_id in mapped_ms_ids or any(qid in mapped_question_ids for qid in question_ids):
            errors.append("overlapping official_part_mapping")
            continue
        if any(qid not in part_ids for qid in question_ids):
            errors.append(f"unknown question part in official_part_mapping: {ms_id}")
            continue
        mapped_ms_ids.add(ms_id)
        mapped_question_ids.update(question_ids)
    for part_id in ms_part_ids:
        if part_id not in part_ids and part_id not in mapped_ms_ids:
            errors.append(f"mark-scheme part has no matching question part: {part_id}")
    question_marks = {part.get("id"): part.get("marks") for part in parts if part.get("marks") is not None}
    markscheme_marks = {part.get("id"): part.get("marks") for part in ms_parts}
    for part_id, marks in question_marks.items():
        if part_id in mapped_question_ids:
            continue
        if markscheme_marks.get(part_id) != marks:
            errors.append(f"part-mark mismatch for {part_id}: question={marks}, markscheme={markscheme_marks.get(part_id)}")
    for mapping in mappings:
        ms_id = mapping.get("markscheme_part_id")
        question_ids = mapping.get("question_part_ids", [])
        if ms_id in mapped_ms_ids:
            mapped_total = sum(question_marks.get(qid, 0) for qid in question_ids)
            if mapped_total != markscheme_marks.get(ms_id):
                errors.append(f"mapped part-mark mismatch for {ms_id}: question={mapped_total}, markscheme={markscheme_marks.get(ms_id)}")
    point_ids = [point.get("id", "") for part in ms_parts for point in part.get("marking_points", [])]
    unique(point_ids, "marking-point IDs", errors)
    available = sum(part.get("marks", 0) for part in ms_parts)
    if available != markscheme.get("total_marks"):
        errors.append(f"mark-scheme part total {available} != {markscheme.get('total_marks')}")
    seen_points: set[tuple[str, str, str, bool]] = set()
    for part in ms_parts:
        point_total = 0
        for point in part.get("marking_points", []):
            if not point.get("id") or not isinstance(point.get("text"), str) or not point.get("text"):
                errors.append(f"incomplete marking point in {part.get('id')}")
            if not isinstance(point.get("tag"), str) or not point.get("tag"):
                errors.append(f"missing marking tag: {point.get('id')}")
            if not isinstance(point.get("marks"), int) or point.get("marks", 0) < 1:
                errors.append(f"invalid marking-point marks: {point.get('id')}")
            if not isinstance(point.get("is_alternative"), bool):
                errors.append(f"is_alternative must be boolean: {point.get('id')}")
            if not point.get("is_alternative", False):
                point_total += point.get("marks", 0)
            key = (part.get("id", ""), point.get("text", ""), point.get("tag", ""), point.get("is_alternative", False))
            if key in seen_points:
                errors.append(f"exact duplicate marking point: {point.get('id')}")
            seen_points.add(key)
        if point_total != part.get("marks"):
            errors.append(f"marking-point total {point_total} != part marks {part.get('marks')} for {part.get('id')}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS")
    return 0


def validate_official_reconciliation(
    question: dict,
    local_markscheme: dict,
    reconciliation: object,
    local_path: Path,
    answerable: set[str],
    errors: list[str],
) -> None:
    """Validate occurrence-aware, question-side bindings to immutable official JSON."""
    if not isinstance(reconciliation, dict) or reconciliation.get("version") != "0.1":
        errors.append("invalid official_reconciliation version")
        return
    allowed = {"version", "part_bindings", "part_aliases", "part_transfers", "marking_point_aliases"}
    if set(reconciliation) - allowed:
        errors.append("unknown official_reconciliation field")

    source_cache: dict[str, dict] = {local_path.name: local_markscheme}

    def load_source(name: object) -> dict | None:
        if not isinstance(name, str) or not name or Path(name).name != name:
            errors.append("invalid official source filename")
            return None
        if name not in source_cache:
            path = local_path.parent / name
            if not path.is_file():
                errors.append(f"missing official source: {name}")
                return None
            try:
                source_cache[name] = json.loads(path.read_text())
            except (OSError, json.JSONDecodeError):
                errors.append(f"invalid official source: {name}")
                return None
        return source_cache[name]

    def part_key(ref: object) -> tuple[str, str, int] | None:
        if not isinstance(ref, dict):
            errors.append("invalid official part reference")
            return None
        source = ref.get("source", local_path.name)
        part_id = ref.get("part_id")
        occurrence = ref.get("occurrence", 1)
        ms = load_source(source)
        if ms is None or not isinstance(part_id, str) or not isinstance(occurrence, int) or occurrence < 1:
            errors.append("invalid official part reference")
            return None
        matches = [p for p in ms.get("parts", []) if p.get("id") == part_id]
        if occurrence > len(matches):
            errors.append(f"unknown official part occurrence: {source}:{part_id}#{occurrence}")
            return None
        return source, part_id, occurrence

    def part_for(key: tuple[str, str, int]) -> dict:
        source, part_id, occurrence = key
        matches = [p for p in source_cache[source].get("parts", []) if p.get("id") == part_id]
        return matches[occurrence - 1]

    local_keys: list[tuple[str, str, int]] = []
    counts: dict[str, int] = {}
    for part in local_markscheme.get("parts", []):
        pid = part.get("id", "")
        counts[pid] = counts.get(pid, 0) + 1
        local_keys.append((local_path.name, pid, counts[pid]))

    consumed_parts: set[tuple[str, str, int]] = set()
    bound_questions: set[str] = set()

    def consume(key: tuple[str, str, int], kind: str) -> None:
        if key in consumed_parts:
            errors.append(f"official part occurrence used more than once: {key[0]}:{key[1]}#{key[2]}")
        consumed_parts.add(key)

    for binding in reconciliation.get("part_bindings", []):
        if not isinstance(binding, dict):
            errors.append("invalid official part binding")
            continue
        qids = binding.get("question_part_ids")
        refs = binding.get("official_part_refs")
        if not isinstance(qids, list) or not qids or not isinstance(refs, list) or not refs:
            errors.append("invalid official part binding")
            continue
        if any(qid not in answerable for qid in qids):
            errors.append("official binding references non-answerable question part")
            continue
        if any(qid in bound_questions for qid in qids):
            errors.append("question part is bound more than once")
            continue
        keys = [part_key(ref) for ref in refs]
        if any(key is None for key in keys):
            continue
        resolved = [key for key in keys if key is not None]
        for key in resolved:
            consume(key, "binding")
        qmarks = sum(next(p["marks"] for p in question["parts"] if p.get("id") == qid) for qid in qids)
        omarks = sum(part_for(key).get("marks", 0) for key in resolved)
        if qmarks != omarks:
            errors.append(f"official binding mark mismatch: question={qmarks}, official={omarks}")
        bound_questions.update(qids)

    alias_keys: set[tuple[str, str, int]] = set()
    for alias in reconciliation.get("part_aliases", []):
        if not isinstance(alias, dict) or not alias.get("reason"):
            errors.append("invalid official part alias")
            continue
        key = part_key(alias.get("official_part_ref"))
        target = part_key(alias.get("alias_of"))
        if key is None or target is None:
            continue
        if key[0] != local_path.name:
            errors.append("only local official parts may be declared aliases")
        part = part_for(key)
        if part.get("marks") != 0 or any(not p.get("is_alternative", False) for p in part.get("marking_points", [])):
            errors.append("official part alias must be a zero-mark alternative-only occurrence")
        consume(key, "alias")
        alias_keys.add(key)

    for transfer in reconciliation.get("part_transfers", []):
        if not isinstance(transfer, dict) or not transfer.get("target_question_id") or not transfer.get("target_question_part_id"):
            errors.append("invalid official part transfer")
            continue
        key = part_key(transfer.get("official_part_ref"))
        if key is None:
            continue
        if key[0] != local_path.name:
            errors.append("only local official parts may be transferred")
        consume(key, "transfer")

    # Unambiguous one-to-one IDs remain implicit, keeping additive metadata small.
    for qid in sorted(answerable - bound_questions):
        matches = [key for key in local_keys if key[1] == qid and key not in consumed_parts]
        if len(matches) != 1:
            errors.append(f"question part has no unique official binding: {qid}")
            continue
        key = matches[0]
        qmark = next(p["marks"] for p in question["parts"] if p.get("id") == qid)
        if qmark != part_for(key).get("marks"):
            errors.append(f"part-mark mismatch for {qid}: question={qmark}, official={part_for(key).get('marks')}")
            continue
        consume(key, "implicit binding")
        bound_questions.add(qid)

    for key in local_keys:
        if key not in consumed_parts:
            errors.append(f"unconsumed official part occurrence: {key[0]}:{key[1]}#{key[2]}")
    if bound_questions != answerable:
        for qid in sorted(answerable - bound_questions):
            errors.append(f"unbound question part: {qid}")

    point_aliases: dict[tuple[str, str, int, str, int], tuple[str, str, int, str, int]] = {}

    def point_key(ref: object) -> tuple[str, str, int, str, int] | None:
        if not isinstance(ref, dict):
            errors.append("invalid official marking-point reference")
            return None
        pk = part_key(ref.get("part_ref"))
        point_id = ref.get("marking_point_id")
        occurrence = ref.get("occurrence", 1)
        if pk is None or not isinstance(point_id, str) or not isinstance(occurrence, int) or occurrence < 1:
            errors.append("invalid official marking-point reference")
            return None
        matches = [p for p in part_for(pk).get("marking_points", []) if p.get("id") == point_id]
        if occurrence > len(matches):
            errors.append(f"unknown official marking-point occurrence: {point_id}#{occurrence}")
            return None
        return (*pk, point_id, occurrence)

    def point_for(key: tuple[str, str, int, str, int]) -> dict:
        pk = key[:3]
        matches = [p for p in part_for(pk).get("marking_points", []) if p.get("id") == key[3]]
        return matches[key[4] - 1]

    for alias in reconciliation.get("marking_point_aliases", []):
        if not isinstance(alias, dict) or alias.get("reason") != "exact_duplicate_alternative":
            errors.append("invalid official marking-point alias")
            continue
        key = point_key(alias.get("official_marking_point_ref"))
        target = point_key(alias.get("alias_of"))
        if key is None or target is None:
            continue
        point = point_for(key)
        target_point = point_for(target)
        semantic_point = lambda value: {k: v for k, v in value.items() if k != "id"}
        if key == target or semantic_point(point) != semantic_point(target_point) or not point.get("is_alternative", False):
            errors.append("marking-point alias is not an exact duplicate alternative")
            continue
        if key in point_aliases:
            errors.append("official marking-point occurrence aliased more than once")
        point_aliases[key] = target

    for source, ms in source_cache.items():
        available = sum(part.get("marks", 0) for part in ms.get("parts", []))
        if available != ms.get("total_marks"):
            errors.append(f"official source part total {available} != total_marks in {source}")
        part_counts: dict[str, int] = {}
        for part in ms.get("parts", []):
            pid = part.get("id", "")
            part_counts[pid] = part_counts.get(pid, 0) + 1
            pk = (source, pid, part_counts[pid])
            point_total = 0
            seen: dict[tuple[str, str, bool, int], tuple[str, str, int, str, int]] = {}
            point_counts: dict[str, int] = {}
            for point in part.get("marking_points", []):
                mpid = point.get("id", "")
                point_counts[mpid] = point_counts.get(mpid, 0) + 1
                key = (*pk, mpid, point_counts[mpid])
                if not mpid or not isinstance(point.get("text"), str) or not point.get("text"):
                    errors.append(f"incomplete marking point in {pid}")
                if not isinstance(point.get("tag"), str) or not point.get("tag"):
                    errors.append(f"missing marking tag: {mpid}")
                if not isinstance(point.get("marks"), int) or point.get("marks", 0) < 1:
                    errors.append(f"invalid marking-point marks: {mpid}")
                if not isinstance(point.get("is_alternative"), bool):
                    errors.append(f"is_alternative must be boolean: {mpid}")
                if not point.get("is_alternative", False):
                    point_total += point.get("marks", 0)
                signature = (point.get("text", ""), point.get("tag", ""), point.get("is_alternative", False), point.get("marks", 0))
                if signature in seen and pk not in alias_keys and key not in point_aliases:
                    errors.append(f"undeclared exact duplicate marking point: {source}:{pid}#{pk[2]}:{mpid}#{key[4]}")
                seen[signature] = key
            if point_total != part.get("marks"):
                errors.append(f"marking-point total {point_total} != part marks {part.get('marks')} for {source}:{pid}#{pk[2]}")


if __name__ == "__main__":
    raise SystemExit(main())
