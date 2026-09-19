#!/usr/bin/env python3
"""Fail-closed manager for one Physics 9702 P4 knowledge-base paper.

The program owns progression.  Agents may edit artifacts, but a later unit is not
unlocked until deterministic checks and an explicit independent-manager review pass.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PAPER_RE = re.compile(r"(9702_[msw]\d{2})_(4[1-4])$")


class GateError(RuntimeError):
    pass


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise GateError(f"missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise GateError(f"invalid JSON: {path}: {exc}") from exc


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def value_digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def paper_paths(repo: Path, paper: str) -> dict[str, Path]:
    match = PAPER_RE.fullmatch(paper)
    if not match:
        raise GateError("paper must look like 9702_m18_42 and be a P4 variant")
    stem, variant = match.groups()
    sessions = {"m": "february-march", "s": "may-june", "w": "october-november"}
    session_char = stem.split("_")[1][0]
    year_digits = stem.split("_")[1][1:]
    year = f"20{year_digits}"
    session = sessions.get(session_char, "may-june")
    v_digit = variant[1] if len(variant) == 2 else variant
    variant_dir = f"variant-{v_digit}"

    structured_evidence = repo / "subjects/physics/9702/reviews/evidence/p4" / paper
    legacy_evidence = repo / "subjects/physics/9702/evidence/p4" / paper
    evidence = structured_evidence if (structured_evidence.exists() or not legacy_evidence.exists()) else legacy_evidence

    structured_qp = repo / "subjects/physics/9702/past papers/p4" / year / session / variant_dir / "parsed-questions"
    legacy_qp = repo / f"subjects/physics/9702/papers/p4/parsed-questions/{stem}_qp_{variant}"
    questions = structured_qp if (structured_qp.exists() or not legacy_qp.exists()) else legacy_qp

    structured_ms = repo / "subjects/physics/9702/past papers/p4" / year / session / variant_dir / "mark-schemes"
    legacy_ms = repo / f"subjects/physics/9702/papers/p4/mark-schemes/{stem}_ms_{variant}"
    official = structured_ms if (structured_ms.exists() or not legacy_ms.exists()) else legacy_ms

    structured_enrichment = repo / "subjects/physics/9702/past papers/p4" / year / session / variant_dir / "enrichment"
    legacy_enrichment = repo / "subjects/physics/9702/enrichment/p4"
    enrichment = structured_enrichment if (structured_enrichment.exists() or not legacy_enrichment.exists()) else legacy_enrichment

    return {
        "questions": questions,
        "official": official,
        "enrichment": enrichment,
        "state": evidence / "workflow-state.json",
        "ledger": evidence / "initial-source-ledger.json",
        "events": evidence / "gate-events.json",
        "verifier": evidence / "independent-verifier.json",
        "question_evidence": evidence / "questions",
    }



def question_files(paths: dict[str, Path]) -> list[Path]:
    files = sorted(paths["questions"].glob("question_*.json"))
    if not files:
        raise GateError(f"no canonical questions in {paths['questions']}")
    return files


def official_files(paths: dict[str, Path]) -> list[Path]:
    files = sorted(paths["official"].glob("markscheme_*.json"))
    if not files:
        raise GateError(f"no official mark schemes in {paths['official']}")
    return files


def answerable_leaves(question: dict[str, Any]) -> list[str]:
    return [
        part["id"]
        for part in question.get("parts", [])
        if isinstance(part, dict) and isinstance(part.get("marks"), int) and part["marks"] > 0
    ]


def enrichment_leaf_hashes(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    data = read_json(path)
    return {
        part["part_id"]: value_digest(part)
        for part in data.get("parts", [])
        if isinstance(part, dict) and part.get("part_id")
    }


def assert_edit_scope(
    paths: dict[str, Path],
    state: dict[str, Any],
    paper: str,
    allowed_question: int,
    allowed_leaf: str | None = None,
    allow_canonical: bool = False,
) -> None:
    """Reject edits to locked canonical questions or non-active enrichment leaves."""
    violations: list[str] = []
    for number_text, unit in state["questions"].items():
        number = int(number_text)
        qpath, _, epath = qpaths(paths, paper, number)
        baseline = unit.get("baseline", {})
        if not (allow_canonical and number == allowed_question):
            if digest(qpath) != baseline.get("canonical_sha256"):
                violations.append(f"Q{number} canonical changed while locked")
        current_leaves = enrichment_leaf_hashes(epath)
        expected_leaves = baseline.get("enrichment_leaves", {})
        all_leaf_ids = set(current_leaves) | set(expected_leaves)
        for leaf_id in all_leaf_ids:
            if number == allowed_question and (leaf_id == allowed_leaf or allow_canonical):
                continue
            if current_leaves.get(leaf_id) != expected_leaves.get(leaf_id):
                violations.append(f"{leaf_id} changed while locked")
    if violations:
        raise GateError("out-of-scope artifact edits detected:\n- " + "\n- ".join(violations))


def make_ledger(repo: Path, paths: dict[str, Path], paper: str) -> dict[str, Any]:
    def entries(files: list[Path]) -> list[dict[str, Any]]:
        return [
            {"path": f.relative_to(repo).as_posix(), "sha256": digest(f), "size": f.stat().st_size}
            for f in files
        ]

    return {
        "schema_version": 1,
        "paper": paper,
        "created_at": now(),
        "canonical_questions": entries(question_files(paths)),
        "official_mark_schemes": entries(official_files(paths)),
    }


def verify_official(repo: Path, paths: dict[str, Path]) -> None:
    ledger = read_json(paths["ledger"])
    expected = {entry["path"]: entry for entry in ledger.get("official_mark_schemes", [])}
    current = {f.relative_to(repo).as_posix(): f for f in official_files(paths)}
    if set(current) != set(expected):
        raise GateError("official mark-scheme inventory changed after preflight")
    changed = [rel for rel, file in current.items() if digest(file) != expected[rel].get("sha256")]
    if changed:
        raise GateError("official mark-scheme bytes changed: " + ", ".join(changed))


def load_state(repo: Path, paper: str) -> tuple[dict[str, Path], dict[str, Any]]:
    paths = paper_paths(repo, paper)
    state = read_json(paths["state"])
    if state.get("paper") != paper:
        raise GateError("workflow state belongs to another paper")
    verify_official(repo, paths)
    return paths, state


def save_state(paths: dict[str, Path], state: dict[str, Any]) -> None:
    state["updated_at"] = now()
    write_json(paths["state"], state)


def record(paths: dict[str, Path], event: dict[str, Any]) -> None:
    events = read_json(paths["events"]) if paths["events"].exists() else []
    events.append({"at": now(), **event})
    write_json(paths["events"], events)


def init(
    repo: Path,
    paper: str,
    expected_total: int = 100,
    only_question: int | None = None,
) -> None:
    paths = paper_paths(repo, paper)
    if paths["state"].exists():
        raise GateError(f"workflow already initialized; use status/resume: {paths['state']}")
    questions = question_files(paths)
    officials = official_files(paths)
    if only_question is None:
        if len(questions) != len(officials):
            raise GateError(f"inventory mismatch: {len(questions)} questions, {len(officials)} mark schemes")
        canonical_total = sum(read_json(path).get("total_marks", 0) for path in questions)
        official_total = sum(read_json(path).get("total_marks", 0) for path in officials)
        if canonical_total != expected_total or official_total != expected_total:
            raise GateError(
                f"paper total must be {expected_total} before initialization; "
                f"canonical={canonical_total}, official={official_total}"
            )
        selected_questions = questions
    else:
        selected_questions = [path for path in questions if path.name == f"question_{only_question:02d}.json"]
        selected_officials = [path for path in officials if path.name == f"markscheme_{only_question:02d}.json"]
        if len(selected_questions) != 1 or len(selected_officials) != 1:
            raise GateError(f"Q{only_question} canonical/official pair is missing")
        canonical_total = read_json(selected_questions[0]).get("total_marks", 0)
        official_total = read_json(selected_officials[0]).get("total_marks", 0)
        if canonical_total != official_total:
            raise GateError(
                f"Q{only_question} canonical/official marks disagree: "
                f"canonical={canonical_total}, official={official_total}"
            )
    ledger = make_ledger(repo, paths, paper)
    write_json(paths["ledger"], ledger)
    units: dict[str, Any] = {}
    for question_path in selected_questions:
        q = read_json(question_path)
        qnum = int(q.get("question_num"))
        units[str(qnum)] = {
            "canonical": "PENDING",
            "canonical_sha256": None,
            "leaves": {leaf: "LOCKED" for leaf in answerable_leaves(q)},
            "closeout": "LOCKED",
            "enrichment_sha256": None,
            "verifier": "LOCKED",
            "verifier_id": None,
            "external_auditor": "LOCKED",
            "external_auditor_id": None,
            "baseline": {
                "canonical_sha256": digest(question_path),
                "enrichment_leaves": enrichment_leaf_hashes(
                    paths["enrichment"] / f"{paper}_q{qnum:02d}.enrichment.json"
                ),
            },
        }
    state = {
        "schema_version": 2,
        "paper": paper,
        "scope": "paper" if only_question is None else "question",
        "only_question": only_question,
        "created_at": now(),
        "updated_at": now(),
        "current_question": min(int(n) for n in units),
        "phase": "CANONICAL",
        "questions": units,
        "independent_verification": "LOCKED",
        "release": "LOCKED",
    }
    write_json(paths["state"], state)
    write_json(paths["events"], [{"at": now(), "gate": "INIT", "verdict": "PASS"}])
    scope = "whole paper" if only_question is None else f"Q{only_question} only"
    print(f"PASS: initialized {paper} ({scope}); Q{state['current_question']} canonical is unlocked")


def ensure_current(state: dict[str, Any], question: int) -> dict[str, Any]:
    if question != state.get("current_question"):
        raise GateError(f"Q{question} is locked; current question is Q{state.get('current_question')}")
    try:
        return state["questions"][str(question)]
    except KeyError as exc:
        raise GateError(f"question {question} is not in workflow inventory") from exc


def qpaths(paths: dict[str, Path], paper: str, question: int) -> tuple[Path, Path, Path]:
    qn = f"{question:02d}"
    return (
        paths["questions"] / f"question_{qn}.json",
        paths["official"] / f"markscheme_{qn}.json",
        paths["enrichment"] / f"{paper}_q{qn}.enrichment.json",
    )


def canonical_errors(question: dict[str, Any], official: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    parts = question.get("parts", [])
    ids = [p.get("id") for p in parts if isinstance(p, dict)]
    if len(ids) != len(set(ids)):
        errors.append("duplicate canonical part IDs")
    leaf_ids = answerable_leaves(question)
    for part in parts:
        if not isinstance(part, dict):
            errors.append("non-object canonical part")
            continue
        pid = part.get("id", "unknown")
        parent = part.get("parent_id")
        if parent is not None and parent not in ids:
            errors.append(f"{pid}: missing parent {parent}")
        is_leaf = pid in leaf_ids
        schema = part.get("response_schema")
        if is_leaf and not isinstance(schema, dict):
            errors.append(f"{pid}: answerable leaf missing response_schema")
        if not is_leaf and schema is not None:
            errors.append(f"{pid}: structural parent has response_schema")
        if is_leaf and schema and schema.get("version") != "0.1":
            errors.append(f"{pid}: response_schema version must be 0.1")
    flow_ids = [item.get("part_id") for item in question.get("content_flow", []) if item.get("type") == "part"]
    if flow_ids != ids:
        errors.append("content_flow must list every part once in printed order")
    if sum(p.get("marks", 0) or 0 for p in parts) != question.get("total_marks"):
        errors.append("canonical leaf marks do not sum to total_marks")
    official_marks = sum(p.get("marks", 0) or 0 for p in official.get("parts", []))
    if question.get("official_reconciliation") is None:
        if official_marks != official.get("total_marks") or official_marks != question.get("total_marks"):
            errors.append("canonical and official total marks disagree")
    else:
        if official_marks != official.get("total_marks"):
            errors.append("official mark-scheme parts do not sum to total_marks")
    figures = question.get("figures", [])
    if any(not isinstance(fig, dict) for fig in figures):
        errors.append("every figure must be a structured placement object")
    return errors


def canonical_artifact_errors(question_path: Path, question: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    image = question_path.with_suffix(".png")
    if not image.is_file() or image.stat().st_size == 0:
        errors.append("canonical question image is missing or empty")
    part_ids = {part.get("id") for part in question.get("parts", []) if isinstance(part, dict)}
    figures = {fig.get("id"): fig for fig in question.get("figures", []) if isinstance(fig, dict)}
    for figure_id, figure in figures.items():
        file_name = figure.get("file")
        if not figure_id or not file_name:
            errors.append("figure placement requires id and file")
            continue
        file_path = question_path.parent / file_name
        if not file_path.is_file() or file_path.stat().st_size == 0:
            errors.append(f"{figure_id}: figure file is missing or empty")
        introduced = figure.get("introduced_by")
        referenced = figure.get("referenced_by")
        if introduced not in part_ids or not isinstance(referenced, list) or any(pid not in part_ids for pid in referenced):
            errors.append(f"{figure_id}: invalid introduced_by/referenced_by placement")
    known_figures = set(figures)
    for part in question.get("parts", []):
        if not isinstance(part, dict):
            continue
        unknown = set(part.get("figure_ids", [])) - known_figures
        if unknown:
            errors.append(f"{part.get('id')}: unknown figure IDs {sorted(unknown)}")
        latex = part.get("question_text_latex", "")
        if latex.count("$") % 2:
            errors.append(f"{part.get('id')}: unbalanced LaTeX dollar delimiters")
        text = f"{part.get('question_text', '')}\n{latex}".lower()
        if any(marker in text for marker in ("© ucles", "blank page", "turn over")):
            errors.append(f"{part.get('id')}: source footer or page furniture leaked into prompt")
    return errors


def registry_ids(repo: Path, rel: str, key: str, id_key: str) -> set[str]:
    primary = repo / "subjects/physics/9702" / rel
    if not primary.exists():
        primary = repo / "subjects/physics/9702/knowledge/knowledge-base" / Path(rel).name
    data = read_json(primary)
    return {item[id_key] for item in data.get(key, []) if isinstance(item, dict) and item.get(id_key)}


def registry_map(repo: Path, rel: str, key: str, id_key: str) -> dict[str, dict[str, Any]]:
    primary = repo / "subjects/physics/9702" / rel
    if not primary.exists():
        primary = repo / "subjects/physics/9702/knowledge/knowledge-base" / Path(rel).name
    data = read_json(primary)
    return {item[id_key]: item for item in data.get(key, []) if isinstance(item, dict) and item.get(id_key)}


def has_bad_control_text(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    return any(ord(char) < 32 and char not in "\n\r\t" for char in value)


def curriculum(repo: Path) -> tuple[dict[str, str], dict[str, tuple[str, str]]]:
    modules: dict[str, str] = {}
    outcomes: dict[str, tuple[str, str]] = {}
    base = repo / "subjects/physics/9702/knowledge/2025-2027"
    for level in ("as", "a2"):
        tax = read_json(base / level / f"9702-2025-2027-{level}-taxonomy.json")
        for topic in tax.get("topics", []):
            for module in topic.get("modules", []):
                modules[module["module_id"]] = topic["topic_id"]
        outs = read_json(base / level / f"9702-2025-2027-{level}-learning-outcomes.json")
        for outcome in outs.get("outcomes", []):
            outcomes[outcome["outcome_id"]] = (outcome["topic_id"], outcome["module_id"])
    return modules, outcomes


def leaf_errors(
    repo: Path,
    question: dict[str, Any],
    official: dict[str, Any],
    enrichment: dict[str, Any],
    leaf_id: str,
    official_path: Path | None = None,
) -> list[str]:
    errors: list[str] = []
    canonical = {p.get("id"): p for p in question.get("parts", [])}
    official_parts = {p.get("id"): p for p in official.get("parts", [])}
    enriched = {p.get("part_id"): p for p in enrichment.get("parts", [])}
    if leaf_id not in canonical or leaf_id not in answerable_leaves(question):
        return [f"{leaf_id}: not an answerable canonical leaf"]
    if leaf_id not in enriched:
        return [f"{leaf_id}: missing enrichment part"]
    part = enriched[leaf_id]
    mapping = part.get("mapping", {})
    modules, outcomes = curriculum(repo)
    module = mapping.get("primary_module_id")
    topic = mapping.get("primary_topic_id")
    if modules.get(module) != topic:
        errors.append(f"{leaf_id}: primary module is not a child of primary topic")
    for outcome in mapping.get("outcome_ids", []):
        if outcome not in outcomes:
            errors.append(f"{leaf_id}: unknown outcome {outcome}")
        elif outcomes[outcome] != (topic, module):
            errors.append(f"{leaf_id}: outcome {outcome} does not belong to primary module")
    for secondary in mapping.get("direct_secondary_mappings", []):
        secondary_module = secondary.get("module_id")
        if modules.get(secondary_module) != topic:
            errors.append(f"{leaf_id}: secondary module {secondary_module} is not a child of primary topic")
        for outcome in secondary.get("outcome_ids", []):
            if outcome not in outcomes:
                errors.append(f"{leaf_id}: unknown secondary outcome {outcome}")
            elif outcomes[outcome] != (topic, secondary_module):
                errors.append(f"{leaf_id}: secondary outcome {outcome} does not belong to declared secondary module")
    patterns = set(part.get("question_patterns", []))
    if part.get("knowledge_refs", {}).get("definition_ids") and "definition" not in patterns:
        errors.append(f"{leaf_id}: definition reference requires definition pattern")
    if len(part.get("hints", [])) < 2:
        errors.append(f"{leaf_id}: requires at least two progressive hints")
    if len(part.get("walkthrough", [])) < 2:
        errors.append(f"{leaf_id}: requires at least two walkthrough steps")
    checking = part.get("checking", {})
    mode = checking.get("mode")
    checks = checking.get("deterministic_checks", [])
    rubric = checking.get("ai_rubric", [])
    if mode not in {"ai", "hybrid", "deterministic"}:
        errors.append(f"{leaf_id}: invalid checking mode")
    if mode == "ai" and checks:
        errors.append(f"{leaf_id}: ai mode cannot contain deterministic checks")
    if mode == "hybrid" and (not checks or not rubric):
        errors.append(f"{leaf_id}: hybrid mode needs deterministic checks and AI rubric")
    if mode == "deterministic" and rubric:
        errors.append(f"{leaf_id}: deterministic mode cannot contain AI rubric")
    if checking.get("full_marks_if_all_deterministic_checks_pass") and canonical[leaf_id].get("marks", 0) > 1:
        errors.append(f"{leaf_id}: automatic full marks forbidden for multi-mark leaf")
    fields = {
        field.get("field_id")
        for block in canonical[leaf_id].get("response_schema", {}).get("blocks", [])
        for field in block.get("fields", [])
        if isinstance(field, dict)
    }
    for check in checks:
        if check.get("field_id") not in fields:
            errors.append(f"{leaf_id}: deterministic field_id {check.get('field_id')!r} is not canonical")

    target_points: list[tuple[dict[str, Any], int]] = []
    reconciliation = question.get("official_reconciliation")
    if reconciliation and reconciliation.get("part_bindings"):
        for binding in reconciliation.get("part_bindings", []):
            if leaf_id in binding.get("question_part_ids", []):
                for ref in binding.get("official_part_refs", []):
                    ref_id = ref.get("part_id")
                    ref_occ = ref.get("occurrence", 1)
                    src_name = ref.get("source")
                    allowed_mps = set(ref.get("marking_point_ids", []))
                    if src_name and official_path is not None:
                        src_path = official_path.parent / src_name
                        if src_path.is_file():
                            src_ms = read_json(src_path)
                            matches = [p for p in src_ms.get("parts", []) if p.get("id") == ref_id]
                            if ref_occ <= len(matches):
                                for mp in matches[ref_occ - 1].get("marking_points", []):
                                    if not allowed_mps or mp.get("id") in allowed_mps:
                                        target_points.append((mp, ref_occ))
                    else:
                        matches = [p for p in official.get("parts", []) if p.get("id") == ref_id]
                        if ref_occ <= len(matches):
                            for mp in matches[ref_occ - 1].get("marking_points", []):
                                if not allowed_mps or mp.get("id") in allowed_mps:
                                    target_points.append((mp, ref_occ))
    if not target_points:
        target_points = [(mp, 1) for mp in official_parts.get(leaf_id, {}).get("marking_points", [])]

    expected: list[tuple[str, int]] = []
    for point, occ in target_points:
        criterion_id = point.get("id")
        expected.append((criterion_id, occ))
    actual: list[tuple[str, int]] = []
    for item in rubric:
        occurrence = item.get("criterion_occurrence", 1)
        if item.get("criterion_id"):
            actual.append((item["criterion_id"], occurrence))
        actual.extend((criterion_id, occurrence) for criterion_id in item.get("alternative_criterion_ids", []))
    if Counter(actual) != Counter(expected):
        errors.append(f"{leaf_id}: official criterion coverage mismatch; expected {expected}, got {actual}")
    official_text = " ".join(
        str(point.get("text", ""))
        for point, _ in target_points
    )
    any_match = re.search(r"\bAny\s+(one|two|three|four|five|\d+)\s+from\b", official_text, re.I)
    if any_match:
        required_phrase = f"any {any_match.group(1).lower()}"
        observable_text = " ".join(str(item.get("observable", "")) for item in rubric).lower()
        if required_phrase not in observable_text:
            errors.append(f"{leaf_id}: rubric does not preserve official '{required_phrase} from' rule")
    if enrichment.get("numerical_values_checked") is not False:
        errors.append("numerical_values_checked must remain false")
    skills = registry_ids(repo, "knowledge/skills.json", "skills", "skill_id")
    definitions = registry_ids(repo, "knowledge/definitions.json", "definitions", "definition_id")
    formulas = registry_ids(repo, "knowledge/formulas.json", "formulas", "formula_id")
    known_patterns = registry_ids(repo, "knowledge/question-patterns.json", "patterns", "pattern_id")
    for skill in [part.get("skills", {}).get("primary_skill_id"), *part.get("skills", {}).get("supporting_skill_ids", [])]:
        if skill not in skills:
            errors.append(f"{leaf_id}: unknown skill {skill}")
    for value in part.get("knowledge_refs", {}).get("definition_ids", []):
        if value not in definitions:
            errors.append(f"{leaf_id}: unknown definition {value}")
    for value in part.get("knowledge_refs", {}).get("formula_ids", []):
        if value not in formulas:
            errors.append(f"{leaf_id}: unknown formula {value}")
    for value in patterns:
        if value not in known_patterns:
            errors.append(f"{leaf_id}: unknown question pattern {value}")
    definition_records = registry_map(repo, "knowledge/definitions.json", "definitions", "definition_id")
    formula_records = registry_map(repo, "knowledge/formulas.json", "formulas", "formula_id")
    for value in part.get("knowledge_refs", {}).get("definition_ids", []):
        record = definition_records.get(value, {})
        if any(has_bad_control_text(item) for item in record.values()):
            errors.append(f"{leaf_id}: definition {value} contains invalid control characters")
    for value in part.get("knowledge_refs", {}).get("formula_ids", []):
        record = formula_records.get(value, {})
        if has_bad_control_text(record.get("latex")):
            errors.append(f"{leaf_id}: formula {value} contains invalid LaTeX control characters")
    return errors


def ordered_union(parts: list[dict[str, Any]], extractor) -> list[str]:
    result: list[str] = []
    for part in parts:
        for value in extractor(part):
            if value not in result:
                result.append(value)
    return result


def question_errors(
    repo: Path,
    question: dict[str, Any],
    official: dict[str, Any],
    enrichment: dict[str, Any],
    question_path: Path | None = None,
    official_path: Path | None = None,
) -> list[str]:
    errors = canonical_errors(question, official)
    if question_path is not None:
        errors.extend(canonical_artifact_errors(question_path, question))
    leaves = answerable_leaves(question)
    parts_by_id = {p.get("part_id"): p for p in enrichment.get("parts", [])}
    parts = [parts_by_id[leaf] for leaf in leaves if leaf in parts_by_id]
    if len(parts) != len(leaves):
        errors.append("enrichment leaf inventory does not match canonical leaves")
        return errors
    for leaf in leaves:
        errors.extend(leaf_errors(repo, question, official, enrichment, leaf, official_path))
    expected_patterns = ordered_union(parts, lambda p: p.get("question_patterns", []))
    expected_topics = ordered_union(parts, lambda p: [p.get("mapping", {}).get("primary_topic_id")])
    expected_modules = ordered_union(
        parts,
        lambda p: [
            p.get("mapping", {}).get("primary_module_id"),
            *[item.get("module_id") for item in p.get("mapping", {}).get("direct_secondary_mappings", [])],
        ],
    )
    expected_outcomes = ordered_union(
        parts,
        lambda p: [
            *p.get("mapping", {}).get("outcome_ids", []),
            *[
                outcome
                for item in p.get("mapping", {}).get("direct_secondary_mappings", [])
                for outcome in item.get("outcome_ids", [])
            ],
        ],
    )
    comparisons = (
        ("question_patterns", enrichment.get("question_patterns", []), expected_patterns),
        ("mapping.topic_ids", enrichment.get("mapping", {}).get("topic_ids", []), expected_topics),
        ("mapping.module_ids", enrichment.get("mapping", {}).get("module_ids", []), expected_modules),
        ("mapping.outcome_ids", enrichment.get("mapping", {}).get("outcome_ids", []), expected_outcomes),
    )
    for field, actual, expected in comparisons:
        if actual != expected:
            errors.append(f"{field}: expected first-occurrence order {expected}; got {actual}")
    return errors


def require_review(note: str | None) -> str:
    if not note or len(note.strip()) < 20:
        raise GateError("manager must supply a concrete independent-review note (20+ characters)")
    return note.strip()


def approve_canonical(repo: Path, paper: str, question_number: int, note: str | None) -> None:
    paths, state = load_state(repo, paper)
    unit = ensure_current(state, question_number)
    if state.get("phase") != "CANONICAL" or unit.get("canonical") != "PENDING":
        raise GateError("canonical gate is not currently unlocked")
    qpath, mpath, epath = qpaths(paths, paper, question_number)
    assert_edit_scope(paths, state, paper, question_number, allow_canonical=True)
    question, official = read_json(qpath), read_json(mpath)
    errors = canonical_errors(question, official) + canonical_artifact_errors(qpath, question)
    if errors:
        raise GateError("canonical gate failed:\n- " + "\n- ".join(errors))
    review = require_review(note)
    unit["canonical"] = "PASS"
    unit["canonical_sha256"] = digest(qpath)
    unit["baseline"]["canonical_sha256"] = digest(qpath)
    unit["baseline"]["enrichment_leaves"] = enrichment_leaf_hashes(epath)
    unit["leaves"] = {leaf: "LOCKED" for leaf in answerable_leaves(question)}
    first_leaf = next(iter(unit["leaves"]), None)
    if first_leaf is None:
        raise GateError("question has no answerable leaves")
    unit["leaves"][first_leaf] = "PENDING"
    state["phase"] = "LEAF"
    save_state(paths, state)
    record(paths, {"gate": "QUESTION PASS", "question": question_number, "verdict": "PASS", "review": review})
    print(f"PASS: Q{question_number} canonical; unlocked {first_leaf}")


def approve_leaf(repo: Path, paper: str, question_number: int, leaf: str, note: str | None) -> None:
    paths, state = load_state(repo, paper)
    unit = ensure_current(state, question_number)
    if state.get("phase") != "LEAF" or unit.get("leaves", {}).get(leaf) != "PENDING":
        raise GateError(f"leaf is locked or not current: {leaf}")
    qpath, mpath, epath = qpaths(paths, paper, question_number)
    assert_edit_scope(paths, state, paper, question_number, allowed_leaf=leaf)
    if digest(qpath) != unit.get("canonical_sha256"):
        raise GateError("canonical question changed after QUESTION PASS")
    errors = leaf_errors(repo, read_json(qpath), read_json(mpath), read_json(epath), leaf, mpath)
    if errors:
        raise GateError("leaf gate failed:\n- " + "\n- ".join(errors))
    review = require_review(note)
    unit["leaves"][leaf] = "PASS"
    unit["baseline"]["enrichment_leaves"][leaf] = enrichment_leaf_hashes(epath)[leaf]
    leaves = list(unit["leaves"])
    index = leaves.index(leaf)
    if index + 1 < len(leaves):
        unit["leaves"][leaves[index + 1]] = "PENDING"
        unlocked = leaves[index + 1]
    else:
        unit["closeout"] = "PENDING"
        state["phase"] = "CLOSEOUT"
        unlocked = "QUESTION CLOSEOUT"
    save_state(paths, state)
    record(paths, {"gate": "LEAF PASS", "question": question_number, "leaf": leaf, "verdict": "PASS", "review": review})
    print(f"PASS: {leaf}; unlocked {unlocked}")


def close_question(repo: Path, paper: str, question_number: int, note: str | None) -> None:
    paths, state = load_state(repo, paper)
    unit = ensure_current(state, question_number)
    if state.get("phase") != "CLOSEOUT" or unit.get("closeout") != "PENDING":
        raise GateError("question closeout is locked")
    if any(value != "PASS" for value in unit.get("leaves", {}).values()):
        raise GateError("not every leaf has LEAF PASS")
    qpath, mpath, epath = qpaths(paths, paper, question_number)
    assert_edit_scope(paths, state, paper, question_number)
    if digest(qpath) != unit.get("canonical_sha256"):
        raise GateError("canonical question changed after QUESTION PASS")
    errors = question_errors(repo, read_json(qpath), read_json(mpath), read_json(epath), qpath, mpath)
    validator = repo / "scripts/validate_question_enrichment.py"
    if validator.exists():
        result = subprocess.run(
            [sys.executable, str(validator), "--enrichment", str(epath), "--question", str(qpath), "--mark-scheme", str(mpath)],
            capture_output=True,
            text=True,
        )
        if result.returncode:
            errors.append("validate_question_enrichment.py failed: " + (result.stdout + result.stderr).strip())
    if errors:
        raise GateError("question closeout failed:\n- " + "\n- ".join(errors))
    review = require_review(note)
    unit["closeout"] = "PASS"
    unit["enrichment_sha256"] = digest(epath)
    unit["verifier"] = "PENDING"
    unit["verifier_id"] = None
    unit["external_auditor"] = "LOCKED"
    unit["external_auditor_id"] = None
    state["current_question"] = question_number
    state["phase"] = "QUESTION_VERIFIER"
    state["independent_verification"] = "PENDING"
    state["release"] = "LOCKED"
    unlocked = f"Q{question_number} independent verifier"
    save_state(paths, state)
    record(paths, {"gate": "QUESTION CLOSEOUT PASS", "question": question_number, "verdict": "PASS", "review": review})
    print(f"PASS: Q{question_number} closeout; unlocked {unlocked}")


def referenced_registry_ids(enrichment: dict[str, Any]) -> set[str]:
    result: set[str] = set()
    for part in enrichment.get("parts", []):
        skills = part.get("skills", {})
        primary = skills.get("primary_skill_id")
        if primary:
            result.add(primary)
        result.update(skills.get("supporting_skill_ids", []))
        refs = part.get("knowledge_refs", {})
        result.update(refs.get("definition_ids", []))
        result.update(refs.get("formula_ids", []))
        mapping = part.get("mapping", {})
        for key in ("primary_topic_id", "primary_module_id"):
            if mapping.get(key):
                result.add(mapping[key])
        result.update(mapping.get("outcome_ids", []))
    return result


def validate_question_review_report(
    report: dict[str, Any],
    paper: str,
    question_number: int,
    expected_leaves: set[str],
    expected_registry_ids: set[str],
    role: str,
) -> str:
    if report.get("paper") != paper or report.get("question") != question_number:
        raise GateError(f"{role} report must name {paper} Q{question_number}")
    if report.get("role") != role or report.get("verdict") != "PASS":
        raise GateError(f"{role} report must declare role={role} and verdict=PASS")
    reviewer_id = report.get("reviewer_id")
    identities = {report.get("author_id"), report.get("manager_id"), reviewer_id}
    if None in identities or len(identities) != 3:
        raise GateError(f"{role} must be identified and independent from author and manager")
    if report.get("semantic_findings") or report.get("deterministic_findings"):
        raise GateError(f"a PASS {role} report must contain zero findings")
    for field in ("reviewed_leaves", "physics_reviewed_leaves", "hint_reviewed_leaves", "rubric_reviewed_leaves"):
        if set(report.get(field, [])) != expected_leaves:
            raise GateError(f"{role} report field {field} must enumerate every Q{question_number} leaf")
    if not expected_registry_ids.issubset(set(report.get("registry_ids_checked", []))):
        missing = sorted(expected_registry_ids - set(report.get("registry_ids_checked", [])))
        raise GateError(f"{role} did not inspect referenced registry IDs: {missing}")
    source = report.get("source_evidence", {})
    required_source = {
        "original_question_pdf",
        "question_pdf_page",
        "original_mark_scheme_pdf",
        "mark_scheme_pdf_page",
        "canonical_question",
        "official_mark_scheme",
    }
    if not required_source.issubset(source) or any(source.get(key) in (None, "") for key in required_source):
        raise GateError(f"{role} report lacks original-PDF and canonical source evidence")
    if len(str(report.get("review_summary", "")).strip()) < 80:
        raise GateError(f"{role} report needs a concrete 80+ character review summary")
    return str(reviewer_id)


def approve_question_verifier(repo: Path, paper: str, question_number: int, report_path: Path) -> None:
    paths, state = load_state(repo, paper)
    unit = ensure_current(state, question_number)
    if state.get("phase") != "QUESTION_VERIFIER" or unit.get("verifier") != "PENDING":
        raise GateError("question verifier gate is locked")
    qpath, mpath, epath = qpaths(paths, paper, question_number)
    if digest(qpath) != unit.get("canonical_sha256") or digest(epath) != unit.get("enrichment_sha256"):
        raise GateError("question changed after manager closeout")
    errors = question_errors(repo, read_json(qpath), read_json(mpath), read_json(epath), qpath, mpath)
    if errors:
        raise GateError("question verifier deterministic precheck failed:\n- " + "\n- ".join(errors))
    enrichment = read_json(epath)
    reviewer_id = validate_question_review_report(
        read_json(report_path),
        paper,
        question_number,
        set(unit["leaves"]),
        referenced_registry_ids(enrichment),
        "question_verifier",
    )
    stored = {**read_json(report_path), "accepted_at": now(), "report_sha256": digest(report_path)}
    target = paths["question_evidence"] / f"question-{question_number:02d}-verifier.json"
    write_json(target, stored)
    unit["verifier"] = "PASS"
    unit["verifier_id"] = reviewer_id
    unit["external_auditor"] = "PENDING"
    state["phase"] = "QUESTION_AUDITOR"
    save_state(paths, state)
    record(paths, {"gate": "QUESTION VERIFIER PASS", "question": question_number, "verdict": "PASS", "reviewer_id": reviewer_id})
    print(f"PASS: Q{question_number} verifier; unlocked external auditor")


def approve_question_auditor(repo: Path, paper: str, question_number: int, report_path: Path) -> None:
    paths, state = load_state(repo, paper)
    unit = ensure_current(state, question_number)
    if state.get("phase") != "QUESTION_AUDITOR" or unit.get("external_auditor") != "PENDING":
        raise GateError("external question auditor gate is locked")
    qpath, mpath, epath = qpaths(paths, paper, question_number)
    if digest(qpath) != unit.get("canonical_sha256") or digest(epath) != unit.get("enrichment_sha256"):
        raise GateError("question changed after manager closeout")
    errors = question_errors(repo, read_json(qpath), read_json(mpath), read_json(epath), qpath, mpath)
    if errors:
        raise GateError("external auditor deterministic precheck failed:\n- " + "\n- ".join(errors))
    report = read_json(report_path)
    reviewer_id = validate_question_review_report(
        report,
        paper,
        question_number,
        set(unit["leaves"]),
        referenced_registry_ids(read_json(epath)),
        "external_auditor",
    )
    if reviewer_id == unit.get("verifier_id"):
        raise GateError("external auditor must be a different agent from the question verifier")
    target = paths["question_evidence"] / f"question-{question_number:02d}-external-auditor.json"
    write_json(target, {**report, "accepted_at": now(), "report_sha256": digest(report_path)})
    unit["external_auditor"] = "PASS"
    unit["external_auditor_id"] = reviewer_id
    record(paths, {"gate": "QUESTION EXTERNAL AUDITOR PASS", "question": question_number, "verdict": "PASS", "reviewer_id": reviewer_id})
    remaining = [
        int(number)
        for number, candidate in state["questions"].items()
        if candidate.get("external_auditor") != "PASS" and int(number) != question_number
    ]
    if remaining:
        next_question = min(remaining)
        state["current_question"] = next_question
        state["phase"] = "CANONICAL"
        unlocked = f"Q{next_question} canonical"
    else:
        state["current_question"] = None
        state["phase"] = "RELEASE"
        state["independent_verification"] = "PASS"
        state["release"] = "PENDING"
        unlocked = "release"
    save_state(paths, state)
    print(f"PASS: Q{question_number} external auditor; unlocked {unlocked}")


def reopen(repo: Path, paper: str, question_number: int, leaf: str | None, note: str | None) -> None:
    paths, state = load_state(repo, paper)
    if state.get("phase") not in {"LEAF", "CLOSEOUT", "QUESTION_VERIFIER", "QUESTION_AUDITOR", "INDEPENDENT", "RELEASE", "COMPLETE"}:
        raise GateError("reopen is allowed only after canonical approval")
    review = require_review(note)
    try:
        unit = state["questions"][str(question_number)]
    except KeyError as exc:
        raise GateError(f"question {question_number} is not in workflow inventory") from exc
    if unit.get("canonical") != "PASS":
        raise GateError("only a question with approved canonical can be reopened")
    state["current_question"] = question_number
    state["independent_verification"] = "LOCKED"
    state["release"] = "LOCKED"
    unit["closeout"] = "LOCKED"
    unit["enrichment_sha256"] = None
    unit["verifier"] = "LOCKED"
    unit["verifier_id"] = None
    unit["external_auditor"] = "LOCKED"
    unit["external_auditor_id"] = None
    if leaf is None:
        unit["canonical"] = "PENDING"
        unit["canonical_sha256"] = None
        for leaf_id in unit["leaves"]:
            unit["leaves"][leaf_id] = "LOCKED"
        unit["baseline"]["enrichment_leaves"] = enrichment_leaf_hashes(qpaths(paths, paper, question_number)[2])
        state["phase"] = "CANONICAL"
        gate = "REOPEN QUESTION"
        target = f"Q{question_number} canonical"
    else:
        if leaf not in unit.get("leaves", {}):
            raise GateError(f"leaf is not in Q{question_number}: {leaf}")
        leaves = list(unit["leaves"])
        start = leaves.index(leaf)
        _, _, epath = qpaths(paths, paper, question_number)
        current_leaf_hashes = enrichment_leaf_hashes(epath)
        baseline_leaf_hashes = unit["baseline"].setdefault("enrichment_leaves", {})
        for leaf_id in leaves:
            if leaf_id not in baseline_leaf_hashes and leaf_id in current_leaf_hashes:
                baseline_leaf_hashes[leaf_id] = current_leaf_hashes[leaf_id]
        for index, leaf_id in enumerate(leaves):
            if index >= start:
                unit["leaves"][leaf_id] = "PENDING" if index == start else "LOCKED"
        state["phase"] = "LEAF"
        gate = "REOPEN LEAF"
        target = leaf
    save_state(paths, state)
    record(paths, {"gate": gate, "question": question_number, "leaf": leaf, "verdict": "REOPENED", "review": review})
    print(f"PASS: reopened {target}; later gates are locked")


def upgrade_verification(repo: Path, paper: str) -> None:
    """Invalidate legacy release and install per-question verifier/auditor gates."""
    paths, state = load_state(repo, paper)
    candidates = [
        int(number)
        for number, unit in state.get("questions", {}).items()
        if unit.get("closeout") == "PASS"
    ]
    if not candidates:
        raise GateError("no manager-closed question is available for verification upgrade")
    for number_text, unit in state["questions"].items():
        unit["verifier"] = "PENDING" if int(number_text) == min(candidates) else "LOCKED"
        unit["verifier_id"] = None
        unit["external_auditor"] = "LOCKED"
        unit["external_auditor_id"] = None
    state["schema_version"] = 2
    state["current_question"] = min(candidates)
    state["phase"] = "QUESTION_VERIFIER"
    state["independent_verification"] = "PENDING"
    state["release"] = "LOCKED"
    save_state(paths, state)
    record(paths, {"gate": "UPGRADE PER-QUESTION VERIFICATION", "verdict": "PASS", "question": min(candidates)})
    print(f"PASS: invalidated legacy release; Q{min(candidates)} question verifier unlocked")


def approve_verifier(repo: Path, paper: str, report_path: Path) -> None:
    paths, state = load_state(repo, paper)
    if state.get("phase") != "INDEPENDENT" or state.get("independent_verification") != "PENDING":
        raise GateError("independent verification is locked")
    report = read_json(report_path)
    if report.get("paper") != paper or report.get("verdict") != "PASS":
        raise GateError("verifier report must name this paper and return PASS")
    identities = [report.get("author_id"), report.get("manager_id"), report.get("verifier_id")]
    if any(not identity for identity in identities) or len(set(identities)) != 3:
        raise GateError("verifier must be identified and independent from author and manager")
    if report.get("semantic_findings") or report.get("deterministic_findings"):
        raise GateError("a PASS verifier report must contain zero findings")
    reviewed = set(report.get("reviewed_leaves", []))
    expected: set[str] = set()
    for number in sorted(int(n) for n in state["questions"]):
        unit = state["questions"][str(number)]
        if unit.get("closeout") != "PASS":
            raise GateError(f"Q{number} has no closeout PASS")
        qpath, mpath, epath = qpaths(paths, paper, number)
        if digest(qpath) != unit.get("canonical_sha256") or digest(epath) != unit.get("enrichment_sha256"):
            raise GateError(f"Q{number} changed after manager approval")
        errors = question_errors(repo, read_json(qpath), read_json(mpath), read_json(epath), qpath, mpath)
        if errors:
            raise GateError(f"Q{number} regressed:\n- " + "\n- ".join(errors))
        expected.update(unit.get("leaves", {}))
    assert_edit_scope(paths, state, paper, -1)
    if reviewed != expected:
        raise GateError("verifier report does not enumerate every answerable leaf")
    stored = {**report, "accepted_at": now(), "report_sha256": digest(report_path)}
    write_json(paths["verifier"], stored)
    state["independent_verification"] = "PASS"
    state["release"] = "PENDING"
    state["phase"] = "RELEASE"
    save_state(paths, state)
    record(paths, {"gate": "INDEPENDENT PASS", "verdict": "PASS", "verifier_id": report["verifier_id"]})
    print("PASS: independent verification; release gate unlocked")


def release(repo: Path, paper: str) -> None:
    paths, state = load_state(repo, paper)
    if state.get("phase") != "RELEASE" or state.get("release") != "PENDING":
        raise GateError("release is locked")
    if state.get("independent_verification") != "PASS":
        raise GateError("independent verification has not passed")
    for number, unit in state["questions"].items():
        if unit.get("verifier") != "PASS" or unit.get("external_auditor") != "PASS":
            raise GateError(f"Q{number} lacks verifier and external-auditor PASS")
        qpath, _, epath = qpaths(paths, paper, int(number))
        if digest(qpath) != unit.get("canonical_sha256") or digest(epath) != unit.get("enrichment_sha256"):
            raise GateError(f"Q{number} changed after approval")
    assert_edit_scope(paths, state, paper, -1)
    state["release"] = "PASS"
    state["phase"] = "COMPLETE"
    save_state(paths, state)
    record(paths, {"gate": "RELEASE PASS", "verdict": "PASS"})
    print(f"PASS: {paper} RELEASE PASS")


def context(repo: Path, paper: str) -> None:
    paths, state = load_state(repo, paper)
    current = state.get("current_question")
    print(json.dumps({"paper": paper, "phase": state.get("phase"), "current_question": current, "state": state}, indent=2))
    if current:
        qpath, mpath, epath = qpaths(paths, paper, current)
        print("OPEN PRIMARY CONTEXT:")
        print(qpath)
        print(paths["questions"] / f"question_{current:02d}.png")
        print(paths["questions"] / f"question_{current:02d}_with_figures.png")
        print(mpath)
        print(epath)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--paper", required=True)
    sub = parser.add_subparsers(dest="command", required=True)
    init_parser = sub.add_parser("init")
    init_parser.add_argument("--only-question", type=int)
    sub.add_parser("status")
    canonical = sub.add_parser("approve-canonical")
    canonical.add_argument("--question", type=int, required=True)
    canonical.add_argument("--manager-review", required=True)
    leaf = sub.add_parser("approve-leaf")
    leaf.add_argument("--question", type=int, required=True)
    leaf.add_argument("--leaf", required=True)
    leaf.add_argument("--manager-review", required=True)
    close = sub.add_parser("close-question")
    close.add_argument("--question", type=int, required=True)
    close.add_argument("--manager-review", required=True)
    verifier = sub.add_parser("approve-question-verifier")
    verifier.add_argument("--question", type=int, required=True)
    verifier.add_argument("--report", type=Path, required=True)
    auditor = sub.add_parser("approve-question-auditor")
    auditor.add_argument("--question", type=int, required=True)
    auditor.add_argument("--report", type=Path, required=True)
    legacy_verifier = sub.add_parser("approve-verifier")
    legacy_verifier.add_argument("--report", type=Path, required=True)
    reopen_parser = sub.add_parser("reopen")
    reopen_parser.add_argument("--question", type=int, required=True)
    reopen_parser.add_argument("--leaf")
    reopen_parser.add_argument("--manager-review", required=True)
    sub.add_parser("release")
    sub.add_parser("upgrade-verification")
    args = parser.parse_args()
    repo = args.repo.resolve()
    try:
        if args.command == "init":
            init(repo, args.paper, only_question=args.only_question)
        elif args.command == "status":
            context(repo, args.paper)
        elif args.command == "approve-canonical":
            approve_canonical(repo, args.paper, args.question, args.manager_review)
        elif args.command == "approve-leaf":
            approve_leaf(repo, args.paper, args.question, args.leaf, args.manager_review)
        elif args.command == "close-question":
            close_question(repo, args.paper, args.question, args.manager_review)
        elif args.command == "approve-question-verifier":
            approve_question_verifier(repo, args.paper, args.question, args.report)
        elif args.command == "approve-question-auditor":
            approve_question_auditor(repo, args.paper, args.question, args.report)
        elif args.command == "approve-verifier":
            approve_verifier(repo, args.paper, args.report)
        elif args.command == "reopen":
            reopen(repo, args.paper, args.question, args.leaf, args.manager_review)
        elif args.command == "release":
            release(repo, args.paper)
        elif args.command == "upgrade-verification":
            upgrade_verification(repo, args.paper)
        return 0
    except GateError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
