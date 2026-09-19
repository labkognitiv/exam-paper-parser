#!/usr/bin/env python3
"""Audit the minimal Physics website selection and mapping joins.

This is read-only. It prints one JSON report and never copies source data.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


QUESTION_SUFFIX = re.compile(r"^(?P<prefix>9702_[msw]\d{2}_\d{2}_q\d{2})_(?P<suffix>.+)$")

_VERIFY_SPEC = importlib.util.spec_from_file_location(
    "verify_physics_marks_for_migration",
    Path(__file__).with_name("verify_physics_marks.py"),
)
assert _VERIFY_SPEC and _VERIFY_SPEC.loader
_VERIFY_MODULE = importlib.util.module_from_spec(_VERIFY_SPEC)
_VERIFY_SPEC.loader.exec_module(_VERIFY_MODULE)
preferred_markscheme_path = _VERIFY_MODULE.preferred_markscheme_path


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def normalized_part_id(part_id: str) -> str:
    """Normalize only the part suffix; preserve the complete question identity."""
    match = QUESTION_SUFFIX.match(part_id)
    if not match:
        return part_id
    return f"{match.group('prefix')}_{match.group('suffix').replace('_', '')}"


def question_part_ids(question: dict[str, Any]) -> set[str]:
    result: set[str] = set()
    for part in question.get("parts", []):
        part_id = part.get("id")
        if isinstance(part_id, str):
            result.add(part_id)
    return result


def resolve_part_ids(
    source_id: str,
    question_ids: set[str],
    explicit_translations: dict[str, list[str]] | None = None,
) -> tuple[str, list[str]]:
    explicit_targets = (explicit_translations or {}).get(source_id)
    if explicit_targets is not None:
        source_question = source_id.split("_q", 1)[0] + "_q" + source_id.split("_q", 1)[1][:2]
        if (
            explicit_targets
            and all(target in question_ids for target in explicit_targets)
            and all(target == source_question or target.startswith(source_question + "_") for target in explicit_targets)
        ):
            return "explicit", explicit_targets
        return "invalid_explicit", []
    match = QUESTION_SUFFIX.match(source_id)
    if match is None and any(part_id.startswith(source_id + "_") for part_id in question_ids):
        return "whole_question", [source_id]
    if source_id in question_ids:
        return "exact", [source_id]
    wanted = normalized_part_id(source_id)
    candidates = sorted(part_id for part_id in question_ids if normalized_part_id(part_id) == wanted)
    if len(candidates) == 1:
        return "translated", candidates
    if not candidates:
        return "unresolved", []
    return "ambiguous", []


def collect_active_lessons(subject_root: Path) -> tuple[set[str], list[str]]:
    active: set[str] = set()
    duplicates: list[str] = []
    maps = sorted((subject_root / "study" / "topics").glob("*/lesson-knowledge-map.json"))
    for path in maps:
        for lesson in load_json(path).get("lessons", []):
            lesson_id = lesson["lesson_id"]
            if lesson_id in active:
                duplicates.append(lesson_id)
            active.add(lesson_id)
    return active, duplicates


def audit_redirects(subject_root: Path, active_lessons: set[str]) -> dict[str, Any]:
    path = subject_root / "study" / "lesson-id-redirects.json"
    aliases = load_json(path).get("aliases", {})
    cycles: list[list[str]] = []
    missing_targets: list[str] = []
    for alias, target in aliases.items():
        seen = [alias]
        cursor = target
        while cursor in aliases:
            if cursor in seen:
                cycles.append(seen + [cursor])
                break
            seen.append(cursor)
            cursor = aliases[cursor]
        if cursor not in active_lessons:
            missing_targets.append(f"{alias}->{cursor}")
    return {
        "aliases": len(aliases),
        "cycles": cycles,
        "missing_active_targets": missing_targets,
    }


def audit_modules(subject_root: Path, active_lessons: set[str]) -> dict[str, Any]:
    paths = sorted((subject_root / "study" / "topics").glob("*/course-modules/*/module.json"))
    empty: list[str] = []
    invalid: list[str] = []
    missing_lessons: list[str] = []
    ids: list[str] = []
    for path in paths:
        if path.stat().st_size == 0:
            empty.append(str(path.relative_to(subject_root)))
            continue
        try:
            data = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            invalid.append(f"{path.relative_to(subject_root)}: {exc}")
            continue
        module_id = data.get("course_module_id")
        if isinstance(module_id, str):
            ids.append(module_id)
        for lesson_id in data.get("lesson_ids", []):
            if lesson_id not in active_lessons:
                missing_lessons.append(f"{module_id}:{lesson_id}")
            elif isinstance(module_id, str) and not lesson_id.startswith(module_id + "_"):
                missing_lessons.append(f"{module_id}:{lesson_id}:wrong_course_module")
    duplicate_ids = sorted(item for item, count in Counter(ids).items() if count > 1)
    return {
        "files": len(paths),
        "parsed": len(paths) - len(empty) - len(invalid),
        "empty": empty,
        "invalid": invalid,
        "duplicate_ids": duplicate_ids,
        "lesson_ids_not_active": sorted(missing_lessons),
    }


def canonical_question_paths(subject_root: Path) -> dict[str, list[Path]]:
    papers = subject_root / "past papers"
    return {
        "p1": sorted(papers.glob("p1/*/*/variant-*/question-package/question_*.json")),
        "p2": sorted(papers.glob("p2/*/*/variant-*/question_*/question_ocr.json")),
        "p4": sorted(papers.glob("p4/*/*/variant-*/question_*/question_ocr.json")),
    }


def audit_questions_and_mappings(subject_root: Path, active_lessons: set[str]) -> dict[str, Any]:
    paths_by_component = canonical_question_paths(subject_root)
    unreadable: list[str] = []
    duplicate_question_ids: list[str] = []
    questions: dict[str, tuple[str, Path, dict[str, Any]]] = {}
    for component, paths in paths_by_component.items():
        for path in paths:
            try:
                data = load_json(path)
            except (OSError, json.JSONDecodeError) as exc:
                unreadable.append(f"{path.relative_to(subject_root)}: {exc}")
                continue
            question_id = data.get("question_id")
            if not isinstance(question_id, str):
                unreadable.append(f"{path.relative_to(subject_root)}: missing question_id")
                continue
            if question_id in questions:
                duplicate_question_ids.append(question_id)
            questions[question_id] = (component, path, data)

    review_root = subject_root / "reviews" / "question-primary-lesson-mapping"
    translations_record = load_json(subject_root / "migration" / "part-id-translations.json")
    explicit_translations = translations_record.get("translations", {})
    excluded_enrichment_parts = translations_record.get("excluded_enrichment_parts", {})
    unavailable_enrichment_question_parts = translations_record.get("unavailable_enrichment_question_parts", {})
    source_reconciliation_required = translations_record.get("unresolved", {})
    aliases = load_json(subject_root / "study" / "lesson-id-redirects.json").get("aliases", {})

    def resolve_lesson(lesson_id: Any) -> Any:
        seen: set[str] = set()
        while isinstance(lesson_id, str) and lesson_id in aliases and lesson_id not in seen:
            seen.add(lesson_id)
            lesson_id = aliases[lesson_id]
        return lesson_id

    valid_topics: set[str] = set()
    valid_modules: set[str] = set()
    outcome_lessons: dict[str, set[str]] = {}
    lesson_topics: dict[str, str] = {}
    lesson_modules: dict[str, set[str]] = {}
    for syllabus_path in sorted((subject_root / "study" / "topics").glob("*/syllabus.json")):
        syllabus = load_json(syllabus_path)
        valid_topics.add(syllabus["topic"]["topic_id"])
        valid_modules.update(module["module_id"] for module in syllabus["topic"]["modules"])
    for map_path in sorted((subject_root / "study" / "topics").glob("*/lesson-knowledge-map.json")):
        lesson_map = load_json(map_path)
        for lesson in lesson_map.get("lessons", []):
            lesson_topics[lesson["lesson_id"]] = lesson_map["topic_id"]
            lesson_modules[lesson["lesson_id"]] = {
                outcome_id.rsplit("_o", 1)[0] for outcome_id in lesson.get("outcome_ids", [])
            }
            for outcome_id in lesson.get("outcome_ids", []):
                outcome_lessons.setdefault(outcome_id, set()).add(lesson["lesson_id"])

    p1_missing_enrichment: list[str] = []
    p1_invalid_targets: list[str] = []
    p1_lesson_candidate_counts: Counter[int] = Counter()
    for question_id, (component, path, _) in questions.items():
        if component != "p1":
            continue
        enrichment_path = path.parent.parent / "enrichment" / f"{question_id}.enrichment.json"
        if not enrichment_path.is_file():
            p1_missing_enrichment.append(question_id)
            continue
        try:
            enrichment = load_json(enrichment_path)
        except (OSError, json.JSONDecodeError) as exc:
            p1_invalid_targets.append(f"{question_id}: invalid enrichment: {exc}")
            continue
        mapping = enrichment.get("mapping", {})
        topic_id = mapping.get("primary_topic_id", enrichment.get("topic_id"))
        module_id = mapping.get("primary_module_id", enrichment.get("module_id"))
        if topic_id not in valid_topics:
            p1_invalid_targets.append(f"{question_id}: topic {topic_id}")
        if module_id not in valid_modules:
            p1_invalid_targets.append(f"{question_id}: module {module_id}")
        candidates: set[str] = set()
        for outcome_id in mapping.get("outcome_ids", []):
            candidates.update(outcome_lessons.get(outcome_id, set()))
        p1_lesson_candidate_counts[len(candidates)] += 1
        if not candidates or not candidates.issubset(active_lessons):
            p1_invalid_targets.append(f"{question_id}: active lesson candidates {sorted(candidates)}")

    enrichment_joins: Counter[str] = Counter()
    enrichment_join_issues: list[dict[str, str]] = []
    for question_id, (component, path, question) in questions.items():
        if component not in {"p2", "p4"}:
            continue
        enrichment_path = path.with_name("enrichment.json")
        if not enrichment_path.is_file():
            enrichment_join_issues.append(
                {"question_id": question_id, "part_id": "*", "status": "missing_enrichment"}
            )
            continue
        enrichment = load_json(enrichment_path)
        question_ids = question_part_ids(question)
        for part in enrichment.get("parts", []):
            source_id = part.get("part_id")
            if not isinstance(source_id, str):
                continue
            if source_id in excluded_enrichment_parts:
                enrichment_joins["explicit_exclusion"] += 1
                continue
            resolution, _ = resolve_part_ids(source_id, question_ids, explicit_translations)
            enrichment_joins[resolution] += 1
            if resolution in {"unresolved", "ambiguous", "invalid_explicit"}:
                enrichment_join_issues.append(
                    {"question_id": question_id, "part_id": source_id, "status": resolution}
                )

    effective_markscheme_joins: Counter[str] = Counter()
    effective_markscheme_join_issues: list[dict[str, str]] = []
    selected_ocr_reconciliations: list[str] = []
    for question_id, (component, path, question) in questions.items():
        if component not in {"p2", "p4"}:
            continue
        effective_path = preferred_markscheme_path(path.parent)
        if effective_path.name == "markscheme_ocr_reviewed.json":
            selected_ocr_reconciliations.append(question_id)
        try:
            marks = load_json(effective_path)
        except (OSError, json.JSONDecodeError) as exc:
            effective_markscheme_join_issues.append(
                {"question_id": question_id, "part_id": "*", "status": f"invalid_effective_markscheme: {exc}"}
            )
            continue
        question_ids = question_part_ids(question)
        for part in marks.get("parts", []):
            source_id = part.get("id")
            if not isinstance(source_id, str):
                continue
            resolution, _ = resolve_part_ids(source_id, question_ids, explicit_translations)
            effective_markscheme_joins[resolution] += 1
            if resolution in {"unresolved", "ambiguous", "invalid_explicit"}:
                effective_markscheme_join_issues.append(
                    {"question_id": question_id, "part_id": source_id, "status": resolution}
                )

    statuses: Counter[str] = Counter()
    confidences: Counter[str] = Counter()
    failed_reviews: list[str] = []
    missing_reviews: list[str] = []
    missing_active_lessons: list[str] = []
    inconsistent_mapping_targets: list[str] = []
    joins: Counter[str] = Counter()
    redirected_mapping_lessons = 0
    join_issues: list[dict[str, str]] = []
    reviewed_ids: set[str] = set()
    low_confidence_ids: set[str] = set()
    overrides_path = subject_root / "migration" / "mapping-overrides.json"
    overrides = load_json(overrides_path).get("records", []) if overrides_path.is_file() else []
    override_by_id = {record["question_id"]: record for record in overrides}

    for component in ("p2", "p4"):
        for review_path in sorted((review_root / component).glob("*.json")):
            review = load_json(review_path)
            question_id = review.get("question_id")
            if not isinstance(question_id, str):
                failed_reviews.append(review_path.stem)
                continue
            reviewed_ids.add(question_id)
            status = str(review.get("status", "MISSING"))
            statuses[status] += 1
            override = override_by_id.get(question_id)
            if status != "VALID":
                failed_reviews.append(question_id)
                if override is None:
                    continue
            else:
                confidence = str(review.get("confidence", "missing"))
                confidences[confidence] += 1
                if confidence == "low":
                    low_confidence_ids.add(question_id)
            original_lesson_id = (override or review).get("primary_lesson_id")
            lesson_id = resolve_lesson(original_lesson_id)
            if lesson_id != original_lesson_id:
                redirected_mapping_lessons += 1
            if lesson_id not in active_lessons:
                missing_active_lessons.append(f"{question_id}:{lesson_id}")
            elif override is None and review.get("derived_topic_id") != lesson_topics.get(lesson_id):
                inconsistent_mapping_targets.append(
                    f"{question_id}: derived topic {review.get('derived_topic_id')} != {lesson_topics.get(lesson_id)}"
                )
            question_record = questions.get(question_id)
            if question_record is None:
                join_issues.append({"question_id": question_id, "part_id": "*", "status": "missing_question"})
                continue
            question_ids = question_part_ids(question_record[2])
            if override is not None:
                mappings = [
                    {"part_id": part_id, "lesson_id": mapped_lesson_id}
                    for part_id, mapped_lesson_id in override.get("part_lesson_ids", {}).items()
                ]
            else:
                mappings = review.get("part_lesson_mappings_unchanged", [])
            for mapping in mappings:
                source_id = mapping.get("part_id")
                if not isinstance(source_id, str):
                    continue
                resolution, target_ids = resolve_part_ids(source_id, question_ids, explicit_translations)
                joins[resolution] += 1
                if resolution in {"unresolved", "ambiguous", "invalid_explicit"}:
                    join_issues.append({
                        "question_id": question_id,
                        "part_id": source_id,
                        "status": resolution,
                    })
                original_mapped_lesson = mapping.get("lesson_id")
                mapped_lesson = resolve_lesson(original_mapped_lesson)
                if mapped_lesson != original_mapped_lesson:
                    redirected_mapping_lessons += 1
                if mapped_lesson not in active_lessons:
                    missing_active_lessons.append(f"{question_id}:{source_id}:{mapped_lesson}")
                else:
                    if override is None and mapping.get("topic_id") != lesson_topics.get(mapped_lesson):
                        inconsistent_mapping_targets.append(
                            f"{question_id}:{source_id}: topic {mapping.get('topic_id')} != {lesson_topics.get(mapped_lesson)}"
                        )
                    if override is None and mapping.get("module_id") not in lesson_modules.get(mapped_lesson, set()):
                        inconsistent_mapping_targets.append(
                            f"{question_id}:{source_id}: module {mapping.get('module_id')} not in {sorted(lesson_modules.get(mapped_lesson, set()))}"
                        )
                if any(target_id != question_id and not target_id.startswith(question_id + "_") for target_id in target_ids):
                    join_issues.append({"question_id": question_id, "part_id": source_id, "status": "cross_question"})

    structured_ids = {qid for qid, value in questions.items() if value[0] in {"p2", "p4"}}
    missing_reviews = sorted(structured_ids - reviewed_ids)
    extra_reviews = sorted(reviewed_ids - structured_ids)
    component_counts = {component: len(paths) for component, paths in paths_by_component.items()}
    readable_counts = Counter(component for component, _, _ in questions.values())
    override_issues: list[str] = []
    overridden_ids: set[str] = set()
    for override in overrides:
        question_id = override.get("question_id")
        overridden_ids.add(question_id)
        review_status = "VALID" if question_id in reviewed_ids and question_id not in failed_reviews else "FAILED"
        replacement = str(override.get("replaces_review_status", ""))
        if not replacement.startswith(review_status):
            override_issues.append(f"{question_id}: override says {replacement}, source review is {review_status}")
        for lesson_id in [override.get("primary_lesson_id"), *override.get("part_lesson_ids", {}).values()]:
            if resolve_lesson(lesson_id) not in active_lessons:
                override_issues.append(f"{question_id}: inactive override lesson {lesson_id}")
    failed_without_override = sorted(set(failed_reviews) - overridden_ids)
    return {
        "selected_files": component_counts,
        "selected_total": sum(component_counts.values()),
        "readable": dict(sorted(readable_counts.items())),
        "readable_total": len(questions),
        "unreadable": unreadable,
        "duplicate_question_ids": sorted(set(duplicate_question_ids)),
        "p1_mapping": {
            "enrichment_records": component_counts["p1"] - len(p1_missing_enrichment),
            "missing_enrichment_question_ids": sorted(p1_missing_enrichment),
            "invalid_curriculum_targets": sorted(p1_invalid_targets),
            "active_lesson_candidate_counts": {
                str(count): questions for count, questions in sorted(p1_lesson_candidate_counts.items())
            },
            "note": "P1 canonical mappings select topic/module/outcomes; active lesson candidates are derived for validation and are not asserted as approved primary lessons."
        },
        "review_status": dict(sorted(statuses.items())),
        "review_confidence": dict(sorted(confidences.items())),
        "failed_review_question_ids": sorted(failed_reviews),
        "development_overrides": len(overrides),
        "override_issues": override_issues,
        "failed_reviews_without_override": failed_without_override,
        "review_required_records": len(low_confidence_ids | overridden_ids),
        "missing_review_question_ids": missing_reviews,
        "extra_review_question_ids": extra_reviews,
        "part_id_joins": dict(sorted(joins.items())),
        "part_id_join_issues": join_issues,
        "enrichment_part_id_joins": dict(sorted(enrichment_joins.items())),
        "enrichment_part_id_join_issues": enrichment_join_issues,
        "excluded_enrichment_parts": excluded_enrichment_parts,
        "unavailable_enrichment_question_parts": unavailable_enrichment_question_parts,
        "effective_markscheme_part_id_joins": dict(sorted(effective_markscheme_joins.items())),
        "effective_markscheme_part_id_join_issues": effective_markscheme_join_issues,
        "selected_ocr_reconciliations": sorted(selected_ocr_reconciliations),
        "source_reconciliation_required": source_reconciliation_required,
        "mapping_lesson_ids_not_active": sorted(set(missing_active_lessons)),
        "inconsistent_mapping_targets": sorted(set(inconsistent_mapping_targets)),
        "redirected_mapping_lesson_references": redirected_mapping_lessons,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--subject-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    args = parser.parse_args()
    subject_root = args.subject_root.resolve()

    active_lessons, duplicate_lessons = collect_active_lessons(subject_root)
    redirects = audit_redirects(subject_root, active_lessons)
    modules = audit_modules(subject_root, active_lessons)
    papers = audit_questions_and_mappings(subject_root, active_lessons)
    structural_errors = (
        duplicate_lessons
        or redirects["cycles"]
        or redirects["missing_active_targets"]
        or modules["empty"]
        or modules["invalid"]
        or modules["duplicate_ids"]
        or modules["lesson_ids_not_active"]
        or papers["unreadable"]
        or papers["duplicate_question_ids"]
        or papers["p1_mapping"]["missing_enrichment_question_ids"]
        or papers["p1_mapping"]["invalid_curriculum_targets"]
        or papers["missing_review_question_ids"]
        or papers["extra_review_question_ids"]
        or papers["mapping_lesson_ids_not_active"]
        or papers["inconsistent_mapping_targets"]
        or papers["override_issues"]
        or papers["failed_reviews_without_override"]
        or papers["enrichment_part_id_join_issues"]
        or papers["effective_markscheme_part_id_join_issues"]
    )
    report = {
        "schema_version": "9702_migration_selection_audit_v1",
        "subject_code": "9702",
        "active_lessons": len(active_lessons),
        "duplicate_active_lesson_ids": sorted(duplicate_lessons),
        "redirects": redirects,
        "course_modules": modules,
        "past_papers": papers,
        "selection_structure_ready": not bool(structural_errors),
        "part_id_join_ready": not bool(papers["part_id_join_issues"]),
        "note": "Readiness covers source selection and mapping structure only; database-schema compatibility and upload are outside this audit.",
    }
    json.dump(report, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0 if not structural_errors and not papers["part_id_join_issues"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
