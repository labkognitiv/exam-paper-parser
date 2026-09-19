#!/usr/bin/env python3
"""Multimodal P1 enrichment only - no slicing, OCR conversion, or answer-key edits.

Each call sends one already-sliced MCQ PNG plus its canonical text to Meta Muse
Spark.  The official answer key remains authoritative.  The model's returned
letter is recorded in a derived metadata sidecar; the published enrichment's
``accepted_answer`` is always the canonical answer-key letter.
"""

from __future__ import annotations

import argparse
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import re
import sys
import time
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
PHYSICS_ROOT = SCRIPT_DIR.parents[1]
REPO_ROOT = next(
    (parent for parent in Path(__file__).resolve().parents if (parent / "subjects").is_dir()),
    PHYSICS_ROOT.parents[1],
)
P1_ROOT = PHYSICS_ROOT / "9702" / "past papers" / "p1"
VALIDATOR_DIR = REPO_ROOT / "scripts"
P2_SCRIPT_DIR = PHYSICS_ROOT / "scripts" / "p2"

sys.path.insert(0, str(VALIDATOR_DIR))
sys.path.insert(0, str(P2_SCRIPT_DIR))

from validate_p1_enrichment import load_registries, validate_single_mcq  # noqa: E402
from enrich_physics_p2 import (  # noqa: E402
    DEFAULT_MODEL_ID,
    call_llm,
    get_api_key,
    sanitize_enrichment,
)


ANSWER_LETTERS = {"A", "B", "C", "D"}
QUESTION_FILE_RE = re.compile(r"question_(\d{2})\.json$")


P1_ENRICHMENT_PROMPT = """You are an expert Cambridge International AS & A Level
Physics (9702) teacher. Create student-facing enrichment for exactly one
Paper 1 multiple-choice question.

You receive the authentic question image, canonical extracted text, the
official answer-key letter, and the allowed curriculum registries. The answer
key is authoritative. Do not re-grade the item or substitute a different
letter.

Return strictly valid JSON and nothing else with this exact shape:
{
  "schema_version": "9702_p1_enrichment_v1",
  "question_id": "...",
  "component": "P1",
  "difficulty": 1,
  "question_patterns": ["allowed_pattern_id"],
  "topic_id": "allowed_topic_id",
  "module_id": "allowed_module_id",
  "skill_id": "allowed_skill_id",
  "accepted_answer": "A",
  "options_breakdown": {
    "A": {"status": "incorrect", "explanation": "One or two concise sentences."},
    "B": {"status": "correct", "explanation": "One or two concise sentences."},
    "C": {"status": "incorrect", "explanation": "One or two concise sentences."},
    "D": {"status": "incorrect", "explanation": "One or two concise sentences."}
  },
  "hints": ["...", "..."],
  "walkthrough": ["...", "..."]
}

Strict answer contract:
- `accepted_answer` must be exactly the official one-character uppercase letter
  supplied in the user message: `A`, `B`, `C`, or `D`.
- Return `"C"`, never `"Option C"`, `"(C)"`, or a sentence.
- Hints must be progressive and never reveal an answer letter or say which
  option is correct. Provide 2 or 3 useful hints.
- Every hint must be specific to this item: name the relevant quantity, unit,
  relationship, diagram feature, wording, or misconception actually present in
  the question. Do not write reusable advice such as "use the right formula",
  "read carefully", or "apply the relevant rule".
- Make the hints a real ladder: first identify what to notice, then connect it
  to the governing physics, then (where useful) direct the next calculation or
  comparison. Keep the answer letter hidden.
- The walkthrough may identify the final option only in its final step and
  must explain why it follows. Write `This is option C`, never `The answer is
  C`. Provide 3 to 7 explicit, question-specific teaching steps.
- The walkthrough must teach this exact question as a teacher beside a student:
  identify the useful given information or diagram, state the physical rule,
  set up the calculation or causal argument, substitute values with units when
  present, show intermediate algebra or comparisons, and connect the result to
  the option. Never skip from a formula directly to the final option.
- For conceptual items, replace numerical substitution with the complete
  physical cause-and-effect chain. For calculation items, show the equation,
  rearrangement, substitution, intermediate result, unit check, and sensible
  precision. Explain the tempting wrong interpretation when it is useful.
- `options_breakdown` is mandatory. Include all four option letters. Mark only
  the official-answer letter `correct` and each other letter `incorrect`.
  Explain each option in one or two item-specific, physics-based sentences.

Content and formatting:
- Select only IDs from the supplied registries and keep module under its stated
  topic and skill valid for that topic.
- Use simple teacher language. Explain the physics, not test-taking tricks.
- Use KaTeX `$...$` for maths. Use upright units, such as `$\\text{m s}^{-1}$`.
- Use ASCII hyphens only: no em dashes or en dashes.
- Do not add fields, Markdown fences, or commentary outside the JSON.
"""


def normalize_answer(value: Any) -> str | None:
    """Extract a lone A-D option without accepting arbitrary prose."""
    if not isinstance(value, str):
        return None
    candidate = value.strip().upper()
    if candidate in ANSWER_LETTERS:
        return candidate
    match = re.fullmatch(r"(?:OPTION\s*)?\(?([ABCD])\)?", candidate)
    return match.group(1) if match else None


def atomic_write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def load_question_files(question_package: Path) -> list[Path]:
    files = [path for path in question_package.glob("question_*.json") if QUESTION_FILE_RE.fullmatch(path.name)]
    return sorted(files, key=lambda path: int(QUESTION_FILE_RE.fullmatch(path.name).group(1)))


def paper_code_from_package(question_package: Path) -> str:
    question_files = load_question_files(question_package)
    if not question_files:
        raise ValueError(f"No canonical question_XX.json files in {question_package}")
    data = json.loads(question_files[0].read_text(encoding="utf-8"))
    code = data.get("paper_code")
    if not isinstance(code, str) or not re.fullmatch(r"9702_[msw]\d{2}_\d{2}", code):
        raise ValueError(f"Invalid paper_code in {question_files[0]}")
    return code


def find_p1_paper_dir(paper_query: str) -> tuple[str, Path]:
    direct = Path(paper_query).expanduser()
    if direct.is_dir():
        package = direct / "question-package" if (direct / "question-package").is_dir() else direct
        return paper_code_from_package(package), package

    matches: list[tuple[str, Path]] = []
    for package in P1_ROOT.rglob("question-package"):
        try:
            code = paper_code_from_package(package)
        except ValueError:
            continue
        if paper_query in {code, code.replace("_", "-")}:
            matches.append((code, package))
    if len(matches) != 1:
        raise ValueError(f"Expected one P1 paper matching {paper_query!r}; found {len(matches)}")
    return matches[0]


def registry_prompt_context(registries: dict) -> str:
    modules = [{"module_id": module_id, "topic_id": topic_id} for module_id, topic_id in registries["modules_to_topic"].items()]
    skills = [
        {"skill_id": skill_id, "topic_ids": skill.get("topic_ids", [])}
        for skill_id, skill in registries["skills"].items()
    ]
    return json.dumps(
        {
            "topics": registries["topics"],
            "modules": modules,
            "skills": skills,
            "question_pattern_ids": sorted(registries["patterns"]),
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )


def canonical_answer(question: dict, answer_key: dict) -> str:
    question_answer = normalize_answer(question.get("correct_answer"))
    key_answer = normalize_answer(answer_key.get(str(question.get("question_num"))))
    if question_answer not in ANSWER_LETTERS:
        raise ValueError(f"{question.get('question_id')}: missing canonical correct_answer")
    if key_answer not in ANSWER_LETTERS:
        raise ValueError(f"{question.get('question_id')}: missing answer_key answer")
    if question_answer != key_answer:
        raise ValueError(
            f"{question.get('question_id')}: question correct_answer {question_answer} "
            f"does not match answer_key {key_answer}"
        )
    return question_answer


def enrich_one(
    question_path: Path,
    answer_key: dict,
    enrich_dir: Path,
    registries: dict,
    registry_context: str,
    api_key: str,
    force: bool,
    preview: bool,
    model_id: str,
    max_tokens: int,
) -> dict:
    question = json.loads(question_path.read_text(encoding="utf-8"))
    question_id = question.get("question_id")
    question_num = question.get("question_num")
    if not isinstance(question_id, str) or not isinstance(question_num, int):
        raise ValueError(f"Invalid canonical identity in {question_path}")
    official_answer = canonical_answer(question, answer_key)
    image_path = question_path.parent / question.get("question_image", f"question_{question_num:02d}.png")
    if not image_path.is_file():
        raise FileNotFoundError(f"Missing MCQ image: {image_path}")

    output_path = enrich_dir / f"{question.get('paper_code')}_q{question_num:02d}.enrichment.json"
    metadata_path = enrich_dir / f"{question.get('paper_code')}_q{question_num:02d}.muse-meta.json"
    if not preview and not force and output_path.is_file():
        return {"question_id": question_id, "status": "skipped-existing", "output": str(output_path)}

    image_data = base64.b64encode(image_path.read_bytes()).decode("ascii")
    user_content = [
        {
            "type": "text",
            "text": (
                f"Question ID: {question_id}\n"
                f"Canonical question text:\n{question.get('question_text', '')}\n\n"
                f"Official answer-key letter: {official_answer}\n\n"
                f"Allowed curriculum registries:\n{registry_context}"
            ),
        },
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_data}"}},
    ]
    response = call_llm(api_key, P1_ENRICHMENT_PROMPT, user_content, model_id=model_id, max_tokens=max_tokens)
    candidate = response.get("parsed_json")
    if not isinstance(candidate, dict):
        rejected_metadata_path = metadata_path
        if output_path.is_file():
            rejected_metadata_path = (
                enrich_dir
                / "rejected-candidates"
                / f"{metadata_path.stem}.failed-{time.time_ns()}.json"
            )
        atomic_write_json(
            rejected_metadata_path,
            {
                "question_id": question_id,
                "model": response.get("model"),
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "official_answer": official_answer,
                "response_valid_json": response.get("valid_json"),
                "tokens": response.get("tokens"),
                "cost_usd": response.get("cost_usd"),
                "raw_response": response.get("raw_content", "No JSON response"),
                "promotion_errors": ["invalid-model-json"],
                "image_sha256": hashlib.sha256(image_path.read_bytes()).hexdigest(),
            },
        )
        return {
            "question_id": question_id,
            "status": "invalid-model-json",
            "error": response.get("raw_content", "No JSON response"),
        }

    returned_answer_raw = candidate.get("accepted_answer")
    returned_answer = normalize_answer(returned_answer_raw)
    model_option_statuses = {
        option: entry.get("status")
        for option, entry in candidate.get("options_breakdown", {}).items()
        if option in ANSWER_LETTERS and isinstance(entry, dict)
    }
    enrichment = sanitize_enrichment(candidate)
    enrichment.update(
        {
            "schema_version": "9702_p1_enrichment_v1",
            "question_id": question_id,
            "component": "P1",
            "accepted_answer": official_answer,
        }
    )
    breakdown = enrichment.get("options_breakdown")
    if not isinstance(breakdown, dict):
        breakdown = {}
        enrichment["options_breakdown"] = breakdown
    for option in ANSWER_LETTERS:
        entry = breakdown.get(option)
        if isinstance(entry, dict):
            entry["status"] = "correct" if option == official_answer else "incorrect"
    errors, _ = validate_single_mcq(enrichment, question, registries)
    metadata = {
        "question_id": question_id,
        "model": response.get("model"),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "official_answer": official_answer,
        "model_accepted_answer_raw": returned_answer_raw,
        "model_accepted_answer": returned_answer,
        "model_answer_matches_official": returned_answer == official_answer,
        "model_option_statuses": model_option_statuses,
        "response_valid_json": response.get("valid_json"),
        "tokens": response.get("tokens"),
        "cost_usd": response.get("cost_usd"),
        "image_sha256": hashlib.sha256(image_path.read_bytes()).hexdigest(),
    }
    if errors:
        metadata["promotion_errors"] = errors
        # A forced retry must never replace the metadata belonging to an already
        # promoted enrichment with data from a rejected model candidate. Keep
        # that candidate separately so the successful result remains resumable
        # and auditable.
        failed_metadata_path = metadata_path
        if output_path.is_file():
            failed_metadata_path = (
                enrich_dir
                / "rejected-candidates"
                / f"{metadata_path.stem}.failed-{time.time_ns()}.json"
            )
        atomic_write_json(failed_metadata_path, metadata)
        return {"question_id": question_id, "status": "validation-failed", "errors": errors}

    if preview:
        return {
            "question_id": question_id,
            "status": "preview",
            "official_answer": official_answer,
            "model_answer": returned_answer,
            "enrichment": enrichment,
        }

    atomic_write_json(output_path, enrichment)
    atomic_write_json(metadata_path, metadata)
    return {
        "question_id": question_id,
        "status": "written",
        "official_answer": official_answer,
        "model_answer": returned_answer,
        "output": str(output_path),
    }


def process_paper(
    paper_query: str,
    question_filter: int | None,
    force: bool,
    preview: bool,
    max_workers: int,
    model_id: str,
    max_tokens: int,
) -> dict:
    paper_code, package = find_p1_paper_dir(paper_query)
    answer_key_path = package / "answer_key.json"
    if not answer_key_path.is_file():
        raise FileNotFoundError(f"Missing answer key: {answer_key_path}")
    answer_key = json.loads(answer_key_path.read_text(encoding="utf-8")).get("answers", {})
    question_paths = load_question_files(package)
    if question_filter is not None:
        question_paths = [path for path in question_paths if int(QUESTION_FILE_RE.fullmatch(path.name).group(1)) == question_filter]
    if not question_paths:
        raise ValueError("No selected canonical P1 questions")

    enrich_dir = package.parent / "enrichment"
    registries = load_registries()
    registry_context = registry_prompt_context(registries)
    needs_model_call = preview or force or any(
        not (enrich_dir / f"{paper_code}_q{int(QUESTION_FILE_RE.fullmatch(path.name).group(1)):02d}.enrichment.json").is_file()
        for path in question_paths
    )
    api_key = get_api_key() if needs_model_call else ""
    started = time.time()
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {
            pool.submit(
                enrich_one,
                question_path,
                answer_key,
                enrich_dir,
                registries,
                registry_context,
                api_key,
                force,
                preview,
                model_id,
                max_tokens,
            ): question_path
            for question_path in question_paths
        }
        for future in as_completed(futures):
            results.append(future.result())

    results.sort(key=lambda item: item["question_id"])
    statuses: dict[str, int] = {}
    for result in results:
        statuses[result["status"]] = statuses.get(result["status"], 0) + 1
    return {
        "paper_code": paper_code,
        "questions_selected": len(question_paths),
        "elapsed_sec": round(time.time() - started, 2),
        "status_counts": statuses,
        "results": results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Enrich already-sliced Physics 9702 P1 MCQs with Meta Muse Spark.")
    parser.add_argument("paper", help="Paper code (for example 9702_s16_11) or question-package directory")
    parser.add_argument("--question", type=int, help="Only enrich this question number")
    parser.add_argument("--force", action="store_true", help="Replace existing derived enrichment for selected questions")
    parser.add_argument("--preview", action="store_true", help="Call Muse and return validated JSON without writing files")
    parser.add_argument("--max-workers", type=int, default=40, help="Concurrent Muse calls (default: all 40 MCQs)")
    parser.add_argument("--model", default=DEFAULT_MODEL_ID, help="OpenRouter model ID")
    parser.add_argument("--max-tokens", type=int, default=3500, help="Maximum Muse completion tokens per question")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable report")
    args = parser.parse_args()
    if args.max_workers < 1:
        parser.error("--max-workers must be at least 1")
    if args.max_tokens < 1:
        parser.error("--max-tokens must be at least 1")

    try:
        report = process_paper(args.paper, args.question, args.force, args.preview, args.max_workers, args.model, args.max_tokens)
    except Exception as exc:
        parser.exit(1, f"P1 enrichment failed: {exc}\n")

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(
            f"{report['paper_code']}: {report['questions_selected']} selected, "
            f"{report['status_counts']}, {report['elapsed_sec']}s"
        )
    if any(status in report["status_counts"] for status in ("invalid-model-json", "validation-failed")):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
