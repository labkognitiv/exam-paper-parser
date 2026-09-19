#!/usr/bin/env python3
"""Map one active primary lesson to each complete Physics P2/P4 question.

The default is the original two-paper pilot. ``--all`` scales the same bounded
workflow to every paper which has an approved contextual part-level resolution.
All output is evidence-only under reviews and can safely be resumed.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
from pathlib import Path
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from pilot_map_question_primary_topics import API_URL, MODEL, ROOT, atomic, clean, image, key, load


PILOT_OUT = ROOT / "reviews/question-primary-lesson-pilot"
FULL_OUT = ROOT / "reviews/question-primary-lesson-mapping"
PAPERS = {
    "p2": {
        "level": "as",
        "paper": ROOT / "past papers/p2/2022/february-march/variant-2",
        "resolved": ROOT / "reviews/p2-as-mapping-contextual-resolution/9702_m22_22/resolved_candidate.json",
    },
    "p4": {
        "level": "a2",
        "paper": ROOT / "past papers/p4/2022/february-march/variant-2",
        "resolved": ROOT / "reviews/p4-a2-mapping-contextual-resolution/9702_m22_42/resolved_candidate.json",
    },
}


def lesson_reference(level: str) -> dict[str, dict]:
    outcome_file = ROOT / f"knowledge/2025-2027/{level}/9702-2025-2027-{level}-learning-outcomes.json"
    outcomes = {item["outcome_id"]: item["outcome_text"] for item in load(outcome_file)["outcomes"]}
    lessons = {}
    for path in sorted((ROOT / "study/topics").glob("*/lesson-knowledge-map.json")):
        payload = load(path)
        for lesson in payload.get("lessons", []):
            outcome_ids = list(lesson.get("outcome_ids") or [])
            if not outcome_ids:
                continue
            first = outcome_ids[0]
            topic_number = int(first.split("_t", 1)[1].split("_", 1)[0])
            if (level == "as" and topic_number > 11) or (level == "a2" and topic_number < 12):
                continue
            lesson_id = lesson["lesson_id"]
            lessons[lesson_id] = {
                "lesson_id": lesson_id,
                "topic_id": payload["topic_id"],
                "title": lesson["title"],
                "outcomes": [{"outcome_id": oid, "text": outcomes[oid]} for oid in outcome_ids],
            }
    return lessons


def question_evidence(question_dir: Path, resolved: dict, lessons: dict[str, dict]) -> dict:
    markscheme = load(question_dir / "markscheme.json")
    mappings = {item["part_id"]: item for item in resolved["mappings"]}
    parts = []
    unmapped = []
    candidates = []
    used_zero_fallback = False
    for part in markscheme.get("parts", []):
        if int(part.get("marks") or 0) <= 0:
            continue
        part_id = part["id"]
        mapping = mappings.get(part_id)
        # Some immutable legacy packages differ only in separator spelling, e.g.
        # ``d_i`` vs ``di``. Resolve that evidence-only compatibility case without
        # touching either source. Ambiguous/missing parts remain explicitly logged.
        if mapping is None:
            normalized = part_id.replace("_", "")
            matches = [item for item in resolved["mappings"] if item["part_id"].replace("_", "") == normalized]
            if len(matches) == 1:
                mapping = matches[0]
        if not mapping:
            unmapped.append({"part_id": part_id, "marks": int(part["marks"]), "label": part.get("label")})
            continue
        primary = mapping["primary"]
        lesson_id = primary["lesson_id"]
        if lesson_id not in lessons:
            raise ValueError(f"inactive lesson {lesson_id} for {part_id}")
        if lesson_id not in candidates:
            candidates.append(lesson_id)
        parts.append({
            "part_id": part_id,
            "marks": int(part["marks"]),
            "lesson_id": lesson_id,
            "topic_id": primary["topic_id"],
            "module_id": primary["module_id"],
            "mapping_type": mapping.get("mapping_type"),
            "reason": mapping.get("reason"),
        })
    if not candidates:
        # A small immutable 2021 source subset exposes its complete question as a
        # zero-mark stem despite resolved positive parts. Use those already
        # verified resolved parts as candidate evidence; record the boundary.
        question_prefix = f"{markscheme['question_id']}_"
        fallback = [item for item in resolved["mappings"] if item["part_id"].startswith(question_prefix)]
        if not fallback:
            raise ValueError(f"no resolved candidate lessons for {markscheme['question_id']}")
        for mapping in fallback:
            primary = mapping["primary"]
            lesson_id = primary["lesson_id"]
            if lesson_id not in lessons:
                raise ValueError(f"inactive fallback lesson {lesson_id} for {mapping['part_id']}")
            if lesson_id not in candidates:
                candidates.append(lesson_id)
            parts.append({
                "part_id": mapping["part_id"],
                "marks": 0,
                "lesson_id": lesson_id,
                "topic_id": primary["topic_id"],
                "module_id": primary["module_id"],
                "mapping_type": mapping.get("mapping_type"),
                "reason": mapping.get("reason"),
            })
        used_zero_fallback = True
    return {
        "question_id": markscheme["question_id"],
        "parts": parts,
        "candidate_lessons": candidates,
        "unmapped_positive_markscheme_parts": unmapped,
        "evidence_mode": "resolved_part_fallback_for_zero_mark_canonical" if used_zero_fallback else "canonical_markscheme_parts",
    }


def call(question_dir: Path, component: str, item: dict, lessons: dict[str, dict], api_key: str) -> dict:
    candidates = [lessons[lesson_id] for lesson_id in item["candidate_lessons"]]
    prompt = f"""Choose exactly ONE strongest primary LESSON for this complete Cambridge Physics 9702 question.

Do not remap or change any part. The resolved part-level lesson mappings are supplied only as candidate evidence. The whole-question primary lesson MUST be exactly one of the candidate lesson IDs. Judge ownership from the complete question, mark allocation and official mark scheme. Select the lesson that owns the central physical reasoning and dominant assessed demand, not a minor setup, unit conversion or supporting calculation.

Return JSON only with question_id, primary_lesson_id, confidence (high/medium/low), and one concise reason. Return no secondary lessons and no part mappings.

component: {component}
question_id: {item['question_id']}
evidence_mode: {item['evidence_mode']}
resolved_part_lesson_evidence: {json.dumps(item['parts'], ensure_ascii=False)}
unmapped_positive_markscheme_parts: {json.dumps(item['unmapped_positive_markscheme_parts'], ensure_ascii=False)}
allowed_candidate_lessons: {json.dumps(candidates, ensure_ascii=False)}
"""
    image_content = [
        {"type": "text", "text": prompt},
        {"type": "text", "text": "AUTHORITATIVE COMPLETE QUESTION"},
        image(question_dir / "question_compact.png"),
        {"type": "text", "text": "AUTHORITATIVE OFFICIAL MARK SCHEME"},
        image(question_dir / "markscheme.png"),
    ]
    mark_totals = {
        lesson_id: sum(part["marks"] for part in item["parts"] if part["lesson_id"] == lesson_id)
        for lesson_id in item["candidate_lessons"]
    }
    fallback_prompt = f"""Return JSON only. Choose exactly one primary lesson for Cambridge Physics 9702 question {item['question_id']} from the candidates below. Use dominant mark allocation and central physical reasoning. Confidence must be exactly high, medium or low.

Candidates: {json.dumps([{'lesson_id': lesson['lesson_id'], 'title': lesson['title'], 'mapped_marks': mark_totals[lesson['lesson_id']]} for lesson in candidates], ensure_ascii=False)}
Output fields: question_id, primary_lesson_id, confidence, reason.
"""
    evidence_content = [
        {"type": "text", "text": fallback_prompt},
        {
            "type": "text",
            "text": (
                "The image provider returned no content. Decide from the verified candidate mark totals."
            ),
        },
    ]
    started = time.monotonic()
    errors = []
    for attempt in range(1, 6):
        try:
            payload = {
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": "You are a precise Cambridge Physics 9702 lesson mapper. Return JSON only."},
                    {"role": "user", "content": image_content if attempt <= 3 else evidence_content},
                ],
                "temperature": 0,
                "reasoning": {"effort": "low"},
                "max_tokens": 900,
            }
            request = Request(
                API_URL,
                data=json.dumps(payload).encode(),
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://kognitiv.edu",
                    "X-Title": "Kognitiv Physics primary-lesson pilot",
                },
                method="POST",
            )
            with urlopen(request, timeout=180) as response:
                raw = json.loads(response.read().decode())
            mapping = clean(raw["choices"][0]["message"].get("content"))
            issue = None
            if mapping.get("question_id") != item["question_id"]:
                issue = "question_id"
            elif mapping.get("primary_lesson_id") not in item["candidate_lessons"]:
                issue = "primary_lesson_id"
            elif mapping.get("confidence") not in {"high", "medium", "low"}:
                issue = "confidence"
            elif not str(mapping.get("reason") or "").strip():
                issue = "reason"
            if issue:
                errors.append(f"attempt {attempt}: {issue}")
                continue
            usage = raw.get("usage") or {}
            lesson_id = mapping["primary_lesson_id"]
            return {
                "status": "VALID",
                "component": component,
                "question_id": item["question_id"],
                "primary_lesson_id": lesson_id,
                "derived_topic_id": lessons[lesson_id]["topic_id"],
                "candidate_lesson_ids": item["candidate_lessons"],
                "part_lesson_mappings_unchanged": item["parts"],
                "unmapped_positive_markscheme_parts": item["unmapped_positive_markscheme_parts"],
                "evidence_mode": item["evidence_mode"],
                "confidence": mapping["confidence"],
                "reason": mapping["reason"],
                "attempt": attempt,
                "elapsed_sec": round(time.monotonic() - started, 3),
                "prompt_tokens": int(usage.get("prompt_tokens") or 0),
                "completion_tokens": int(usage.get("completion_tokens") or 0),
                "cost_usd": float(usage.get("cost") or usage.get("cost_usd") or 0),
                "raw_response": raw,
            }
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, KeyError, ValueError) as exc:
            errors.append(f"attempt {attempt}: {type(exc).__name__}: {exc}")
        if attempt < 5:
            time.sleep(min(15, 2**attempt))
    return {"status": "FAILED", "component": component, "question_id": item["question_id"], "errors": errors}


def full_papers() -> dict[str, dict]:
    """Discover only papers which have the validated contextual resolution."""
    configs = {}
    for component, level, review in (
        ("p2", "as", "p2-as-mapping-contextual-resolution"),
        ("p4", "a2", "p4-a2-mapping-contextual-resolution"),
    ):
        resolved_root = ROOT / "reviews" / review
        package_index: dict[str, Path] = {}
        for markscheme_path in (ROOT / "past papers" / component).rglob("question_*/markscheme.json"):
            question_id = load(markscheme_path)["question_id"]
            paper_id = question_id.rsplit("_q", 1)[0]
            package_index.setdefault(paper_id, markscheme_path.parents[1])
        for resolved_path in sorted(resolved_root.glob("*/resolved_candidate.json")):
            paper_id = resolved_path.parent.name
            paper = package_index.get(paper_id)
            if paper is None:
                raise ValueError(f"no canonical question package for {paper_id}")
            configs[f"{component}:{paper_id}"] = {
                "component": component,
                "level": level,
                "paper": paper,
                "resolved": resolved_path,
            }
    return configs


def source_from_pilot(component: str, question_id: str) -> dict | None:
    path = PILOT_OUT / component / f"{question_id}.json"
    if not path.exists():
        return None
    record = load(path)
    return record if record.get("status") == "VALID" else None


def verified_part_fallback(component: str, item: dict, lessons: dict[str, dict], prior: dict) -> dict:
    """Bounded fallback when Muse returned no usable JSON after five attempts.

    It is deliberately mechanical and low-confidence: the active lesson with
    the highest verified resolved-part mark total owns the question. Ties retain
    candidate order and are flagged for audit. This never edits part mappings.
    """
    totals = {
        lesson_id: sum(part["marks"] for part in item["parts"] if part["lesson_id"] == lesson_id)
        for lesson_id in item["candidate_lessons"]
    }
    top_mark = max(totals.values())
    tied = [lesson_id for lesson_id in item["candidate_lessons"] if totals[lesson_id] == top_mark]
    lesson_id = tied[0]
    return {
        "status": "VALID",
        "source": "verified_part_mark_fallback_after_provider_blank",
        "component": component,
        "question_id": item["question_id"],
        "paper_id": item["question_id"].rsplit("_q", 1)[0],
        "primary_lesson_id": lesson_id,
        "derived_topic_id": lessons[lesson_id]["topic_id"],
        "candidate_lesson_ids": item["candidate_lessons"],
        "part_lesson_mappings_unchanged": item["parts"],
        "unmapped_positive_markscheme_parts": item["unmapped_positive_markscheme_parts"],
        "evidence_mode": item["evidence_mode"],
        "confidence": "low",
        "reason": f"Muse returned no usable JSON after {len(prior.get('errors') or [])} attempts; selected highest verified resolved-part mark total ({top_mark}).",
        "candidate_mark_totals": totals,
        "tied_highest_mark_lesson_ids": tied,
        "provider_errors": prior.get("errors") or [],
        "attempt": int(prior.get("attempt") or len(prior.get("errors") or [])),
        "prompt_tokens": int(prior.get("prompt_tokens") or 0),
        "completion_tokens": int(prior.get("completion_tokens") or 0),
        "cost_usd": float(prior.get("cost_usd") or 0),
    }


def map_paper(
    paper_key: str,
    cfg: dict,
    out: Path,
    api_key: str,
    workers: int,
) -> list[dict]:
    """Map one paper. Paper concurrency is owned by main; questions stay bounded."""
    component = cfg["component"]
    lessons = lesson_reference(cfg["level"])
    resolved = load(cfg["resolved"])
    records: list[dict] = []
    jobs = []
    for question_dir in sorted(path for path in cfg["paper"].glob("question_*") if path.is_dir()):
        item = question_evidence(question_dir, resolved, lessons)
        destination = out / component / f"{item['question_id']}.json"
        if destination.exists():
            existing = load(destination)
            if existing.get("status") == "VALID":
                records.append(existing)
                continue
        pilot = source_from_pilot(component, item["question_id"])
        if pilot:
            # Preserve the approved pilot decision but re-derive facts from current evidence.
            lesson_id = pilot["primary_lesson_id"]
            if lesson_id not in item["candidate_lessons"] or lesson_id not in lessons:
                raise ValueError(f"pilot lesson no longer valid: {item['question_id']}")
            record = {
                **{key: value for key, value in pilot.items() if key not in {"raw_response", "part_lesson_mappings_unchanged"}},
                "source": "approved_pilot_reused",
                "component": component,
                "question_id": item["question_id"],
                "primary_lesson_id": lesson_id,
                "derived_topic_id": lessons[lesson_id]["topic_id"],
                "candidate_lesson_ids": item["candidate_lessons"],
                "part_lesson_mappings_unchanged": item["parts"],
                "unmapped_positive_markscheme_parts": item["unmapped_positive_markscheme_parts"],
                "evidence_mode": item["evidence_mode"],
            }
            atomic(destination, record)
            records.append(record)
            continue
        jobs.append((question_dir, item))
    # Paper concurrency is capped at ten; each paper maps its bounded question set together.
    with ThreadPoolExecutor(max_workers=min(workers, max(1, len(jobs)))) as executor:
        futures = {
            executor.submit(call, question_dir, component, item, lessons, api_key): (question_dir, item)
            for question_dir, item in jobs
        }
        for future in as_completed(futures):
            record = future.result()
            record["source"] = "muse"
            record["paper_id"] = resolved["paper_id"]
            atomic(out / component / f"{record['question_id']}.json", record)
            records.append(record)
            print(f"{paper_key} {record['question_id']} {record['status']}", flush=True)
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="map every resolved P2 and P4 paper")
    parser.add_argument("--finalize-provider-fallbacks", action="store_true", help="finalize only retained blank/malformed provider failures")
    parser.add_argument("--paper-workers", type=int, default=10, help="simultaneous papers (max 10)")
    parser.add_argument("--question-workers", type=int, default=12, help="requests within one paper (max 12)")
    args = parser.parse_args()
    if not 1 <= args.paper_workers <= 10:
        parser.error("--paper-workers must be 1..10")
    if not 1 <= args.question_workers <= 12:
        parser.error("--question-workers must be 1..12")
    out = FULL_OUT if args.all else PILOT_OUT
    configs = full_papers() if args.all else {
        component: {"component": component, **cfg} for component, cfg in PAPERS.items()
    }
    api_key = None if args.finalize_provider_fallbacks else key()
    records = []
    if args.finalize_provider_fallbacks:
        for paper_key, cfg in configs.items():
            component = cfg["component"]
            lessons = lesson_reference(cfg["level"])
            resolved = load(cfg["resolved"])
            for question_dir in sorted(path for path in cfg["paper"].glob("question_*") if path.is_dir()):
                item = question_evidence(question_dir, resolved, lessons)
                destination = out / component / f"{item['question_id']}.json"
                existing = load(destination) if destination.exists() else None
                if not existing or existing.get("status") == "VALID":
                    continue
                errors = existing.get("errors") or []
                if not errors or not all("ValueError: empty response" in error or "JSONDecodeError" in error for error in errors):
                    raise ValueError(f"non-provider failure requires investigation: {destination}")
                record = verified_part_fallback(component, item, lessons, existing)
                atomic(destination, record)
                records.append(record)
                print(f"fallback {paper_key} {item['question_id']} VALID", flush=True)
        # Include all current records in the manifest, not merely this pass.
        records = [load(path) for path in sorted(out.glob("*/*.json"))]
    else:
        with ThreadPoolExecutor(max_workers=args.paper_workers) as executor:
            futures = {
                executor.submit(map_paper, paper_key, cfg, out, api_key, args.question_workers): paper_key
                for paper_key, cfg in configs.items()
            }
            for index, future in enumerate(as_completed(futures), 1):
                paper_records = future.result()
                records.extend(paper_records)
                valid = sum(record.get("status") == "VALID" for record in paper_records)
                print(f"paper {index}/{len(configs)} {futures[future]} {valid}/{len(paper_records)} VALID", flush=True)
    manifest = {
        "schema_version": "9702_question_primary_lesson_mapping_v1" if args.all else "9702_question_primary_lesson_pilot_v1",
        "run_finished": datetime.now(timezone.utc).isoformat(),
        "model": MODEL,
        "mode": "full" if args.all else "pilot",
        "papers": {paper_key: str(cfg["paper"].relative_to(ROOT)) for paper_key, cfg in configs.items()},
        "totals": {
            "questions": len(records),
            "valid": sum(record.get("status") == "VALID" for record in records),
            "failed": sum(record.get("status") != "VALID" for record in records),
            "approved_pilot_reused": sum(record.get("source") == "approved_pilot_reused" for record in records),
            "verified_part_mark_fallback": sum(record.get("source") == "verified_part_mark_fallback_after_provider_blank" for record in records),
            "api_attempts": sum(int(record.get("attempt") or len(record.get("errors") or [])) for record in records),
            "prompt_tokens": sum(int(record.get("prompt_tokens") or 0) for record in records),
            "completion_tokens": sum(int(record.get("completion_tokens") or 0) for record in records),
            "cost_usd": sum(float(record.get("cost_usd") or 0) for record in records),
        },
    }
    atomic(out / "manifest.json", manifest)
    print(json.dumps(manifest["totals"], indent=2))
    if manifest["totals"]["failed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
