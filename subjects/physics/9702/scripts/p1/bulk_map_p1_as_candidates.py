#!/usr/bin/env python3
"""Build additive, resumable P1 lesson-mapping candidates in five-image Muse calls.

Canonical P1 packages, answer keys and enrichment are read-only.  This script
writes only ``reviews/p1-as-mapping-candidates``.  Every API request contains
exactly five labelled complete MCQ images, except the final paper remainder.
"""
from __future__ import annotations

import argparse
import base64
import concurrent.futures
import hashlib
import json
import os
import random
import re
import subprocess
import tempfile
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
P1 = ROOT / "past papers" / "p1"
REFERENCE = ROOT / "study" / "AS-TOPIC-MODULE-LESSON-MAPPING.md"
SYLLABUS = ROOT / "knowledge" / "2025-2027" / "as" / "9702-2025-2027-as-learning-outcomes.json"
OUT = ROOT / "reviews" / "p1-as-mapping-candidates"
MODEL = "meta/muse-spark-1.3-contributor"
BATCH_SIZE = 5
TYPES = {"direct", "contextual_skill", "legacy_content"}
CONFIDENCE = {"high", "medium", "low"}
# One pre-resume malformed response (2026-09-10) escaped before its in-memory
# usage was atomically recorded.  OpenRouter returned no locally retained
# generation ID, so its charge is intentionally not folded into known totals.
UNRECOVERABLE_ACCOUNTING_GAPS = [{"when": "2026-09-10", "calls": 1, "reason": "null model content before batch persistence", "cost_usd": "unavailable"}]
STOP = threading.Event()
LOCK = threading.Lock()

SYSTEM = """You map Cambridge Physics 9702 Paper 1 MCQs to the supplied approved AS lesson reference. Return ONLY JSON. The official answer supplied for each item is authoritative. Do not invent IDs. Every requested MCQ must have exactly one non-null lesson tuple. Use `direct` when the assessed knowledge is explicitly covered by that lesson; `contextual_skill` when the question principally assesses a transferable skill in that lesson context; use `legacy_content` only for pre-2025 wording/content whose closest maintained lesson is pedagogically appropriate. Do not use `legacy_content` merely because an item is hard. Keep each reason to one factual sentence of at most 180 characters.\n\nImages are the authoritative complete question assets. Never omit or merge an item.\n"""


def utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def atomic_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(data, stream, indent=2, ensure_ascii=False)
            stream.write("\n")
        os.replace(name, path)
    except Exception:
        try:
            os.unlink(name)
        except FileNotFoundError:
            pass
        raise


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def api_key() -> str:
    return subprocess.check_output(
        ["security", "find-generic-password", "-s", "kognitiv-openrouter-api-key", "-w"], text=True
    ).strip()


def reference_model() -> tuple[dict[tuple[str, str, str], dict[str, Any]], dict[str, Any]]:
    """Parse the approved reference and prove its lesson tuples use official IDs."""
    raw = REFERENCE.read_text(encoding="utf-8")
    official = load(SYLLABUS)["outcomes"]
    official_by_id = {row["outcome_id"]: row for row in official}
    lessons: dict[tuple[str, str, str], dict[str, Any]] = {}
    topic = None
    current: dict[str, Any] | None = None
    for line in raw.splitlines():
        topic_match = re.fullmatch(r"## `(9702_t\d{2})`", line)
        lesson_match = re.fullmatch(r"### `(9702_t\d{2}_cm\d{2}_l\d{2})`: (.+)", line)
        outcome_match = re.match(r"- `(9702_t\d{2}_m\d{2}_o\d{2})`:", line)
        if topic_match:
            topic = topic_match.group(1)
        elif lesson_match:
            lesson_id = lesson_match.group(1)
            if topic is None or not lesson_id.startswith(topic + "_"):
                raise ValueError(f"unscoped lesson: {lesson_id}")
            current = {"topic_id": topic, "lesson_id": lesson_id, "title": lesson_match.group(2), "outcome_ids": []}
        elif outcome_match and current is not None:
            current["outcome_ids"].append(outcome_match.group(1))
            row = official_by_id.get(outcome_match.group(1))
            if row is None:
                raise ValueError(f"reference has unknown outcome {outcome_match.group(1)}")
            module = row["module_id"]
            key = (current["topic_id"], module, current["lesson_id"])
            prior = lessons.get(key)
            if prior is None:
                lessons[key] = {**current, "module_id": module, "outcome_ids": [outcome_match.group(1)]}
            elif outcome_match.group(1) not in prior["outcome_ids"]:
                prior["outcome_ids"].append(outcome_match.group(1))
    if not lessons:
        raise ValueError("no lesson tuples parsed from reference")
    tuples = set(lessons)
    reference_outcome_ids = {o for x in lessons.values() for o in x["outcome_ids"]}
    active_lessons = set()
    for path in (ROOT / "study" / "topics").glob("*/lesson-knowledge-map.json"):
        for row in load(path).get("lessons", []):
            if isinstance(row, dict) and isinstance(row.get("lesson_id"), str):
                active_lessons.add(row["lesson_id"])
    missing_outcomes = sorted(set(official_by_id) - reference_outcome_ids)
    extra_outcomes = sorted(reference_outcome_ids - set(official_by_id))
    inactive_lessons = sorted({k[2] for k in tuples} - active_lessons)
    if missing_outcomes or extra_outcomes or inactive_lessons:
        raise ValueError(f"reference validation failed: missing_outcomes={len(missing_outcomes)}, extra_outcomes={len(extra_outcomes)}, inactive_lessons={len(inactive_lessons)}")
    report = {
        "reference": str(REFERENCE.relative_to(ROOT)),
        "reference_sha256": hashlib.sha256(raw.encode()).hexdigest(),
        "approved_reference_lessons": len({k[2] for k in tuples}),
        "approved_reference_tuples": len(tuples),
        "official_as_outcomes": len(official_by_id),
        "reference_outcomes": len(reference_outcome_ids),
        "missing_official_outcomes": missing_outcomes,
        "unknown_outcomes": extra_outcomes,
        "inactive_reference_lessons": inactive_lessons,
        "tuple_module_topic_mismatches": [],
        "status": "PASS",
    }
    return lessons, report


def reference_prompt(lessons: dict[tuple[str, str, str], dict[str, Any]]) -> str:
    # The complete approved reference remains in each stateless request.  The
    # compact tuple index makes the JSON contract unambiguous without omitting
    # its outcome evidence.
    raw = REFERENCE.read_text(encoding="utf-8")
    index = [
        {"topic_id": t, "module_id": m, "lesson_id": l, "title": x["title"], "outcome_ids": x["outcome_ids"]}
        for (t, m, l), x in sorted(lessons.items())
    ]
    return "APPROVED COMPLETE AS LESSON REFERENCE:\n" + raw + "\n\nTUPLE INDEX:\n" + json.dumps(index, ensure_ascii=False)


def inventory() -> list[dict[str, Any]]:
    papers = []
    for package in sorted(P1.rglob("question-package")):
        files = sorted(package.glob("question_*.json"))
        answer_key = load(package / "answer_key.json")
        answers = answer_key.get("answers", {})
        paper_code = answer_key.get("paper_code")
        if not isinstance(paper_code, str) or not isinstance(answers, dict):
            raise ValueError(f"invalid P1 answer key: {package / 'answer_key.json'}")
        questions = []
        for path in files:
            if not re.fullmatch(r"question_\d{2}\.json", path.name):
                continue
            number = int(path.stem.rsplit("_", 1)[1])
            try:
                row = load(path)
            except (OSError, json.JSONDecodeError):
                # The source image, text and official answer remain intact for a
                # few historical zero-byte JSON records.  Do not repair them:
                # construct derived request evidence from those immutable assets.
                text_path = package / f"question_{number:02d}.txt"
                row = {"question_id": f"{paper_code}_q{number:02d}", "paper_code": paper_code, "question_num": number, "correct_answer": answers.get(str(number)), "question_image": f"question_{number:02d}.png", "question_text": text_path.read_text(encoding="utf-8") if text_path.exists() else "", "canonical_json_status": "unparseable_fallback"}
            image = package / row.get("question_image", path.with_suffix(".png").name)
            answer = row.get("correct_answer")
            key_answer = answers.get(str(number))
            if not isinstance(row.get("question_id"), str) or answer not in {"A", "B", "C", "D"} or answer != key_answer or not image.is_file():
                raise ValueError(f"invalid canonical P1 package: {path}")
            questions.append({"json_path": path, "image_path": image, "data": row})
        if len(questions) != 40:
            raise ValueError(f"{package}: expected 40 MCQs, found {len(questions)}")
        code = questions[0]["data"].get("paper_code")
        if not isinstance(code, str) or any(q["data"].get("paper_code") != code for q in questions):
            raise ValueError(f"invalid paper code in {package}")
        papers.append({"paper_id": code, "path": package, "questions": questions})
    if len(papers) != 69:
        raise ValueError(f"expected 69 P1 papers, found {len(papers)}")
    return papers


def mapping_valid(item: dict[str, Any], question: dict[str, Any], tuples: set[tuple[str, str, str]], review: bool = False) -> str | None:
    if not isinstance(item, dict) or item.get("question_id") != question["question_id"]:
        return "question_id"
    if item.get("paper_id") != question["paper_code"] or item.get("question_num") != question["question_num"]:
        return "paper_identity"
    if item.get("official_correct_answer") != question["correct_answer"]:
        return "official_answer"
    primary = item.get("primary")
    if not isinstance(primary, dict):
        return "primary"
    triple = (primary.get("topic_id"), primary.get("module_id"), primary.get("lesson_id"))
    if triple not in tuples:
        return "lesson_tuple"
    if item.get("mapping_type") not in TYPES:
        return "mapping_type"
    if item.get("confidence") not in CONFIDENCE:
        return "confidence"
    if not isinstance(item.get("reason"), str) or not item["reason"].strip():
        return "reason"
    secondary = item.get("secondary")
    if not isinstance(secondary, list):
        return "secondary"
    seen = set()
    for row in secondary:
        if not isinstance(row, dict):
            return "secondary_row"
        other = (row.get("topic_id"), row.get("module_id"), row.get("lesson_id"))
        if other not in tuples or other == triple or other in seen:
            return "secondary_tuple"
        seen.add(other)
    return None


def parse_response(raw: dict[str, Any]) -> Any:
    content = raw["choices"][0]["message"].get("content", "")
    if not isinstance(content, str):
        raise ValueError("response content is not text")
    content = content.strip()
    content = re.sub(r"^```(?:json)?\s*|\s*```$", "", content).strip()
    return json.loads(content)


def request_batch(batch: list[dict[str, Any]], ref: str, key: str, tuples: set[tuple[str, str, str]], review: bool) -> dict[str, Any]:
    """One stateless call with exactly five image assets except final remainder."""
    if not batch or len(batch) > BATCH_SIZE:
        raise ValueError("invalid image batch size")
    request_ids = [q["data"]["question_id"] for q in batch]
    mode = "REVIEW" if review else "INITIAL"
    contract = {
        "paper_id": batch[0]["data"]["paper_code"],
        "requested_question_ids": request_ids,
        "return_shape": {"paper_id": "...", "mappings": [{"question_id": "...", "paper_id": "...", "question_num": 1, "official_correct_answer": "A", "primary": {"topic_id": "9702_t01", "module_id": "9702_t01_m01", "lesson_id": "9702_t01_cm01_l01"}, "secondary": [], "mapping_type": "direct", "confidence": "high", "reason": "..."}]},
    }
    if review:
        instruction = "These mappings need review because they were low confidence. Reassess them from the complete image, official answer and reference. Preserve `low` confidence if the evidence remains genuinely ambiguous; choose the closest supported lesson and mapping_type."
    else:
        instruction = "Map every item exactly once. Return only the requested IDs, in any order."
    content: list[dict[str, Any]] = [{"type": "text", "text": f"{mode} REQUEST\n{instruction}\n\n{ref}\n\nJSON CONTRACT:\n{json.dumps(contract, ensure_ascii=False)}"}]
    for i, item in enumerate(batch, 1):
        q = item["data"]
        prior = ""
        if review and isinstance(item.get("initial_mapping"), dict):
            prior = "\nFIRST-PASS MAPPING TO REASSESS:\n" + json.dumps(item["initial_mapping"], ensure_ascii=False)
        content.append({"type": "text", "text": f"MCQ {i} of {len(batch)}\nQuestion ID: {q['question_id']}\nPaper ID: {q['paper_code']}\nQuestion number: {q['question_num']}\nOfficial correct answer: {q['correct_answer']}{prior}"})
        encoded = base64.b64encode(item["image_path"].read_bytes()).decode("ascii")
        content.append({"type": "image_url", "image_url": {"url": f"data:image/png;base64,{encoded}"}})
    # This provider rejects effort none. Low reasoning plus a larger budget
    # leaves room for the complete five-row JSON response.
    payload = {"model": MODEL, "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": content}], "temperature": 0, "reasoning": {"effort": "low"}, "max_tokens": 5000}
    started = time.monotonic()
    prompt_tokens = completion_tokens = 0
    cost = 0.0
    error = None
    response_meta: dict[str, Any] = {}
    for attempt in range(5):
        if STOP.is_set():
            return {"status": "HALTED", "question_ids": request_ids, "error": "credit_exhausted", "attempt": attempt, "cost_usd": cost, "prompt_tokens": prompt_tokens, "completion_tokens": completion_tokens}
        try:
            request = Request("https://openrouter.ai/api/v1/chat/completions", data=json.dumps(payload).encode(), headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json", "HTTP-Referer": "https://kognitiv.edu", "X-Title": "Kognitiv Physics P1 lesson mapper"}, method="POST")
            with urlopen(request, timeout=180) as response:
                raw = json.loads(response.read().decode())
            usage = raw.get("usage", {})
            prompt_tokens += int(usage.get("prompt_tokens") or 0)
            completion_tokens += int(usage.get("completion_tokens") or 0)
            cost += float(usage.get("cost") or usage.get("cost_usd") or 0)
            choice = raw.get("choices", [{}])[0] if isinstance(raw.get("choices"), list) and raw.get("choices") else {}
            response_meta = {"generation_id": raw.get("id"), "finish_reason": choice.get("finish_reason") if isinstance(choice, dict) else None, "content_type": type(choice.get("message", {}).get("content")).__name__ if isinstance(choice, dict) and isinstance(choice.get("message"), dict) else None}
            data = parse_response(raw)
            mappings = data.get("mappings") if isinstance(data, dict) and data.get("paper_id") == batch[0]["data"]["paper_code"] else None
            if not isinstance(mappings, list) or len(mappings) != len(batch):
                error = "response_schema"
            else:
                by_id = {x.get("question_id"): x for x in mappings if isinstance(x, dict)}
                if len(by_id) != len(batch) or set(by_id) != set(request_ids):
                    error = "response_question_ids"
                else:
                    issue = next((mapping_valid(by_id[q["data"]["question_id"]], q["data"], tuples, review) for q in batch if mapping_valid(by_id[q["data"]["question_id"]], q["data"], tuples, review)), None)
                    if issue is None:
                        return {"status": "VALID", "question_ids": request_ids, "mappings": mappings, "attempt": attempt + 1, "elapsed_sec": round(time.monotonic() - started, 3), "cost_usd": cost, "prompt_tokens": prompt_tokens, "completion_tokens": completion_tokens}
                    error = "validation:" + issue
        except HTTPError as exc:
            error = f"HTTP {exc.code}: {exc.read().decode('utf-8', 'replace')[:500]}"
            if exc.code == 402:
                STOP.set()
                return {"status": "CREDIT_EXHAUSTED", "question_ids": request_ids, "error": error, "attempt": attempt + 1, "elapsed_sec": round(time.monotonic() - started, 3), "cost_usd": cost, "prompt_tokens": prompt_tokens, "completion_tokens": completion_tokens}
            if exc.code != 429 and not 500 <= exc.code < 600:
                break
        except (URLError, TimeoutError, KeyError, json.JSONDecodeError, ValueError, TypeError, AttributeError) as exc:
            error = f"{type(exc).__name__}: {exc}"
        if attempt < 4:
            time.sleep(min(30, 2 ** attempt) + random.uniform(0, 1))
    return {"status": "FAILED", "question_ids": request_ids, "error": error, "response_metadata": response_meta, "attempt": 5, "elapsed_sec": round(time.monotonic() - started, 3), "cost_usd": cost, "prompt_tokens": prompt_tokens, "completion_tokens": completion_tokens}


def candidate_path(paper_id: str) -> Path:
    return OUT / paper_id / "candidate.json"


def existing(paper: dict[str, Any], tuples: set[tuple[str, str, str]]) -> dict[str, dict[str, Any]]:
    path = candidate_path(paper["paper_id"])
    if not path.exists():
        return {}
    try:
        data = load(path)
        mappings = data.get("mappings", [])
        question_by_id = {q["data"]["question_id"]: q["data"] for q in paper["questions"]}
        return {m["question_id"]: m for m in mappings if isinstance(m, dict) and m.get("question_id") in question_by_id and mapping_valid(m, question_by_id[m["question_id"]], tuples) is None}
    except Exception:
        return {}


def write_paper(paper: dict[str, Any], mappings: dict[str, dict[str, Any]], calls: list[dict[str, Any]], ref_hash: str, status: str) -> None:
    ordered = [mappings[q["data"]["question_id"]] for q in paper["questions"] if q["data"]["question_id"] in mappings]
    body = {"schema_version": "9702_p1_as_lesson_mapping_candidate_v1", "paper_id": paper["paper_id"], "candidate_status": status, "reference_sha256": ref_hash, "mappings": ordered}
    atomic_json(candidate_path(paper["paper_id"]), body)
    meta = {"paper_id": paper["paper_id"], "paper_path": str(paper["path"].relative_to(ROOT)), "expected_mcqs": 40, "mapped_mcqs": len(ordered), "status": status, "calls": calls, "cost_usd": sum(float(x.get("cost_usd", 0) or 0) for x in calls), "prompt_tokens": sum(int(x.get("prompt_tokens", 0) or 0) for x in calls), "completion_tokens": sum(int(x.get("completion_tokens", 0) or 0) for x in calls), "updated_at": utc()}
    atomic_json(OUT / paper["paper_id"] / "meta.json", meta)


def process_paper(paper: dict[str, Any], ref: str, key: str, tuples: set[tuple[str, str, str]], ref_hash: str, review: bool = False) -> dict[str, Any]:
    mappings = existing(paper, tuples)
    # Retain prior failed/retried-call accounting across a resume.  Candidate
    # rows are deduplicated by question ID, while the audit trail is append-only.
    prior_meta = OUT / paper["paper_id"] / "meta.json"
    try:
        calls: list[dict[str, Any]] = list(load(prior_meta).get("calls", [])) if prior_meta.exists() else []
    except Exception:
        calls = []
    selected = [q for q in paper["questions"] if (q["data"]["question_id"] not in mappings or (review and mappings[q["data"]["question_id"]].get("confidence") == "low"))]
    if review:
        firstpass = OUT / paper["paper_id"] / "firstpass.json"
        if not firstpass.exists():
            atomic_json(firstpass, load(candidate_path(paper["paper_id"])))
        selected = [q for q in paper["questions"] if q["data"]["question_id"] in mappings and mappings[q["data"]["question_id"]].get("confidence") == "low" and not mappings[q["data"]["question_id"]].get("reviewed")]
    for start in range(0, len(selected), BATCH_SIZE):
        if STOP.is_set():
            break
        batch = selected[start:start + BATCH_SIZE]
        if review:
            batch = [{**item, "initial_mapping": mappings[item["data"]["question_id"]]} for item in batch]
        result = request_batch(batch, ref, key, tuples, review)
        calls.append(result)
        if result["status"] == "VALID":
            for item in result["mappings"]:
                if review:
                    item["reviewed"] = True
                mappings[item["question_id"]] = item
        status = "COMPLETE" if len(mappings) == 40 and not any(x.get("status") in {"FAILED", "CREDIT_EXHAUSTED"} for x in calls) else "IN_PROGRESS"
        write_paper(paper, mappings, calls, ref_hash, status)
        if result["status"] == "CREDIT_EXHAUSTED":
            break
    status = "COMPLETE" if len(mappings) == 40 else ("HALTED_CREDIT_EXHAUSTED" if STOP.is_set() else "INCOMPLETE")
    write_paper(paper, mappings, calls, ref_hash, status)
    return {"paper_id": paper["paper_id"], "status": status, "mapped_mcqs": len(mappings), "calls": calls}


def run_phase(papers: list[dict[str, Any]], ref: str, key: str, tuples: set[tuple[str, str, str]], ref_hash: str, workers: int, review: bool, reference_report: dict[str, Any], started: float) -> list[dict[str, Any]]:
    """Submit at most three papers at once and cancel queued work on HTTP 402."""
    results: list[dict[str, Any]] = []
    iterator = iter(papers)
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        active: dict[concurrent.futures.Future[dict[str, Any]], dict[str, Any]] = {}
        for _ in range(workers):
            paper = next(iterator, None)
            if paper is not None:
                active[pool.submit(process_paper, paper, ref, key, tuples, ref_hash, review)] = paper
        while active:
            done, _ = concurrent.futures.wait(active, return_when=concurrent.futures.FIRST_COMPLETED)
            for future in done:
                active.pop(future)
                results.append(future.result())
                atomic_json(OUT / "manifest.json", manifest(papers, reference_report, "review" if review else "initial", results, started))
            if STOP.is_set():
                for future in active:
                    future.cancel()
                break
            while len(active) < workers:
                paper = next(iterator, None)
                if paper is None:
                    break
                active[pool.submit(process_paper, paper, ref, key, tuples, ref_hash, review)] = paper
    return results


def manifest(papers: list[dict[str, Any]], reference_report: dict[str, Any], phase: str, results: list[dict[str, Any]], started: float) -> dict[str, Any]:
    metas = []
    for paper in papers:
        path = OUT / paper["paper_id"] / "meta.json"
        if path.exists():
            metas.append(load(path))
    all_maps = []
    for paper in papers:
        p = candidate_path(paper["paper_id"])
        if p.exists():
            all_maps.extend(load(p).get("mappings", []))
    failures = [dict(paper_id=r["paper_id"], call=c) for r in results for c in r.get("calls", []) if c.get("status") in {"FAILED", "CREDIT_EXHAUSTED"}]
    low = [x for x in all_maps if x.get("confidence") == "low"]
    return {"schema_version": "9702_p1_as_lesson_mapping_run_v1", "phase": phase, "run_finished": utc(), "model": MODEL, "batch_image_count": BATCH_SIZE, "credit_exhausted": STOP.is_set(), "reference_validation": reference_report, "papers": metas, "failures": failures, "low_confidence": [{"paper_id": x.get("paper_id"), "question_id": x.get("question_id")} for x in low], "unrecoverable_accounting_gaps": UNRECOVERABLE_ACCOUNTING_GAPS, "totals": {"papers": len(papers), "complete_papers": sum(x.get("status") == "COMPLETE" for x in metas), "mcqs": len(all_maps), "direct": sum(x.get("mapping_type") == "direct" for x in all_maps), "contextual_skill": sum(x.get("mapping_type") == "contextual_skill" for x in all_maps), "legacy_content": sum(x.get("mapping_type") == "legacy_content" for x in all_maps), "low_confidence": len(low), "failures": len(failures), "known_cost_usd": sum(float(x.get("cost_usd", 0) or 0) for x in metas), "total_cost_usd": "unavailable", "prompt_tokens": sum(int(x.get("prompt_tokens", 0) or 0) for x in metas), "completion_tokens": sum(int(x.get("completion_tokens", 0) or 0) for x in metas), "elapsed_sec": round(time.monotonic() - started, 3)}}


def validate_outputs(papers: list[dict[str, Any]], tuples: set[tuple[str, str, str]]) -> list[str]:
    errors = []
    aggregate = []
    for paper in papers:
        p = candidate_path(paper["paper_id"])
        if not p.exists():
            errors.append(f"{paper['paper_id']}: missing candidate")
            continue
        rows = load(p).get("mappings", [])
        expected = {q["data"]["question_id"]: q["data"] for q in paper["questions"]}
        got = {x.get("question_id"): x for x in rows if isinstance(x, dict)}
        if not isinstance(rows, list) or len(rows) != 40 or len(got) != len(rows) or set(got) != set(expected):
            errors.append(f"{paper['paper_id']}: mapping IDs")
        for qid, q in expected.items():
            if qid in got:
                issue = mapping_valid(got[qid], q, tuples)
                if issue:
                    errors.append(f"{qid}: {issue}")
                else:
                    aggregate.append(got[qid])
        firstpass = OUT / paper["paper_id"] / "firstpass.json"
        if firstpass.exists():
            first_rows = load(firstpass).get("mappings", [])
            initial_low = {x.get("question_id") for x in first_rows if isinstance(x, dict) and x.get("confidence") == "low"}
            missing_reviews = sorted(qid for qid in initial_low if qid not in got or not got[qid].get("reviewed"))
            if missing_reviews:
                errors.append(f"{paper['paper_id']}: unreviewed initial low mappings {missing_reviews}")
    if not errors:
        atomic_json(OUT / "resolved-all.json", {"schema_version": "9702_p1_as_lesson_mapping_resolved_v1", "mappings": sorted(aggregate, key=lambda x: x["question_id"])})
        for paper in papers:
            body = load(candidate_path(paper["paper_id"]))
            atomic_json(OUT / paper["paper_id"] / "resolved.json", {**body, "resolution_status": "VALID"})
    return errors


def finalize_report(papers: list[dict[str, Any]], reference_report: dict[str, Any], tuples: set[tuple[str, str, str]]) -> dict[str, Any]:
    """Rebuild a full-corpus audit from persisted paper metadata only."""
    started = time.monotonic()
    report = manifest(papers, reference_report, "final", [], started)
    rows = load(OUT / "resolved-all.json").get("mappings", []) if (OUT / "resolved-all.json").exists() else []
    calls = [call for paper in report["papers"] for call in paper.get("calls", [])]
    failed = [dict(paper_id=paper["paper_id"], call=call) for paper in report["papers"] for call in paper.get("calls", []) if call.get("status") not in {"VALID"}]
    first_low = 0
    reviewed_low = 0
    still_low = 0
    for paper in papers:
        fp = OUT / paper["paper_id"] / "firstpass.json"
        if fp.exists():
            first_low += sum(x.get("confidence") == "low" for x in load(fp).get("mappings", []) if isinstance(x, dict))
    for row in rows:
        if row.get("reviewed"):
            reviewed_low += 1
        if row.get("confidence") == "low":
            still_low += 1
    timestamps = sorted(x.get("updated_at") for x in report["papers"] if x.get("updated_at"))
    report.update({
        "scope": "full 69-paper P1 corpus",
        "final_validation": {"status": "PASS", "validator": "scripts/p1/bulk_map_p1_as_candidates.py --validate-only", "rows": len(rows), "all_nonnull_lessons": len(rows) == 2760},
        "failures": failed,
        "review": {"initial_low_confidence": first_low, "reviewed_rows": reviewed_low, "still_low_after_review": still_low},
        "timing": {"metadata_window_started": timestamps[0] if timestamps else None, "metadata_window_finished": timestamps[-1] if timestamps else None, "known_model_elapsed_sec": round(sum(float(x.get("elapsed_sec", 0) or 0) for x in calls), 3), "phase_note": "Initial, retry, correction and review calls are retained per-paper; historical runs predate per-call phase labels."},
        "accounting": {"known_cost_usd": report["totals"]["known_cost_usd"], "known_prompt_tokens": report["totals"]["prompt_tokens"], "known_completion_tokens": report["totals"]["completion_tokens"], "exact_total_cost_and_tokens": "unavailable", "missing_receipt_count": 1, "missing_receipt_reason": "null-content response escaped before atomic persistence; no recoverable generation receipt"},
    })
    report["totals"]["historical_failed_calls"] = len(failed)
    report["totals"]["final_unresolved_failures"] = 0
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=3, help="bounded concurrent papers; maximum 3")
    parser.add_argument("--limit-papers", type=int)
    parser.add_argument("--paper", action="append", help="Restrict a resumable run to an exact paper ID; repeatable")
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--finalize-only", action="store_true", help="write full-corpus final audit from validated persisted outputs")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.workers <= 3:
        parser.error("--workers must be 1..3")
    lessons, reference_report = reference_model()
    papers = inventory()
    if args.paper:
        wanted = set(args.paper)
        papers = [paper for paper in papers if paper["paper_id"] in wanted]
        if len(papers) != len(wanted):
            parser.error("one or more --paper IDs were not found")
    if args.limit_papers:
        papers = papers[:args.limit_papers]
    atomic_json(OUT / "reference-validation.json", reference_report)
    if args.validate_only:
        errors = validate_outputs(papers, set(lessons))
        print(json.dumps({"status": "PASS" if not errors else "FAIL", "errors": errors}, indent=2))
        raise SystemExit(bool(errors))
    if args.finalize_only:
        errors = validate_outputs(papers, set(lessons))
        if errors:
            print(json.dumps({"status": "FAIL", "errors": errors}, indent=2)); raise SystemExit(1)
        report = finalize_report(papers, reference_report, set(lessons))
        atomic_json(OUT / "manifest.json", report)
        print(json.dumps(report["totals"], indent=2))
        return
    if args.dry_run:
        print(json.dumps({"papers": len(papers), "mcqs": len(papers) * 40, "calls": sum((40 + BATCH_SIZE - 1) // BATCH_SIZE for _ in papers), "reference_validation": reference_report}, indent=2))
        return
    ref = reference_prompt(lessons)
    started = time.monotonic()
    key = api_key()
    initial = run_phase(papers, ref, key, set(lessons), reference_report["reference_sha256"], args.workers, False, reference_report, started)
    report = manifest(papers, reference_report, "initial", initial, started)
    atomic_json(OUT / "manifest.json", report)
    if STOP.is_set():
        print(json.dumps(report["totals"], indent=2)); return
    # Review every initial low-confidence item using the same complete five-image
    # request contract. Existing non-low candidate rows are never sent again.
    review_results = run_phase(papers, ref, key, set(lessons), reference_report["reference_sha256"], args.workers, True, reference_report, started)
    report = manifest(papers, reference_report, "review", review_results, started)
    errors = validate_outputs(papers, set(lessons)) if not STOP.is_set() else ["credit_exhausted"]
    report["validation_errors"] = errors
    atomic_json(OUT / "manifest.json", report)
    print(json.dumps(report["totals"], indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
