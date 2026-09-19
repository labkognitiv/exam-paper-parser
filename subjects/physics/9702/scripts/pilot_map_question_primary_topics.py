#!/usr/bin/env python3
"""Pilot one P2 and one P4 paper for singular question-level topic ownership."""

from __future__ import annotations

import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
MODEL = "meta/muse-spark-1.3-contributor"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
OUT = ROOT / "reviews/question-primary-topic-pilot"
PAPERS = {
    "p2": ROOT / "past papers/p2/2022/february-march/variant-2",
    "p4": ROOT / "past papers/p4/2022/february-march/variant-2",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def atomic(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def key() -> str:
    return subprocess.check_output(
        ["security", "find-generic-password", "-s", "kognitiv-openrouter-api-key", "-w"], text=True
    ).strip()


def reference(level: str) -> tuple[str, dict[str, str]]:
    taxonomy = load(ROOT / f"knowledge/2025-2027/{level}/9702-2025-2027-{level}-taxonomy.json")
    outcomes = load(ROOT / f"knowledge/2025-2027/{level}/9702-2025-2027-{level}-learning-outcomes.json")
    by_module: dict[str, list[dict]] = {}
    for outcome in outcomes["outcomes"]:
        by_module.setdefault(outcome["module_id"], []).append(
            {"outcome_id": outcome["outcome_id"], "text": outcome["outcome_text"]}
        )
    topics = []
    titles = {}
    for topic in taxonomy["topics"]:
        titles[topic["topic_id"]] = topic["topic_name"]
        topics.append({
            "topic_id": topic["topic_id"],
            "topic_name": topic["topic_name"],
            "modules": [
                {
                    "module_id": module["module_id"],
                    "module_name": module["module_name"],
                    "outcomes": by_module.get(module["module_id"], []),
                }
                for module in topic["modules"]
            ],
        })
    return json.dumps({"level": level, "topics": topics}, ensure_ascii=False, separators=(",", ":")), titles


def image(path: Path) -> dict:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{encoded}", "detail": "high"}}


def evidence(question_dir: Path) -> dict:
    enrichment = load(question_dir / "enrichment.json")
    markscheme = load(question_dir / "markscheme.json")
    marks = {part["id"]: int(part.get("marks") or 0) for part in markscheme.get("parts", [])}
    parts = []
    unique_topics = []
    for part in enrichment.get("parts", []):
        mapping = part.get("mapping") or {}
        topic_id = part.get("primary_topic_id") or mapping.get("primary_topic_id")
        if not topic_id:
            raise ValueError(f"missing part topic: {question_dir}/{part.get('part_id')}")
        if topic_id not in unique_topics:
            unique_topics.append(topic_id)
        parts.append({
            "part_id": part["part_id"],
            "marks": marks.get(part["part_id"], int(part.get("marks") or 0)),
            "topic_id": topic_id,
            "module_id": part.get("primary_module_id") or mapping.get("primary_module_id"),
            "outcome_ids": mapping.get("outcome_ids", []),
        })
    return {"question_id": enrichment["question_id"], "parts": parts, "candidate_topics": unique_topics}


def clean(text: str | None) -> dict:
    if not text:
        raise ValueError("empty response")
    return json.loads(re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip()))


def call(question_dir: Path, component: str, curriculum: str, titles: dict[str, str], api_key: str) -> dict:
    item = evidence(question_dir)
    candidates = item["candidate_topics"]
    prompt = f"""Choose the ONE strongest question-level primary topic for this complete Cambridge Physics 9702 question.

Do not remap or change any part. The existing part mappings below are authoritative candidate topics. The primary MUST be exactly one of those candidate topic IDs. Judge ownership from the complete question, mark allocation and official mark scheme. Prefer the topic that owns the question's central physical situation and dominant assessed reasoning, not a minor setup or unit skill.

Return JSON only with question_id, primary_topic_id, confidence (high/medium/low), and one short reason. Return no part mappings and no secondary list; secondaries will be derived deterministically.

component: {component}
question_id: {item['question_id']}
existing_part_mappings: {json.dumps(item['parts'], ensure_ascii=False)}
allowed_candidate_topics: {json.dumps([{'topic_id': topic, 'topic_name': titles[topic]} for topic in candidates], ensure_ascii=False)}

CONTROLLED LEVEL CURRICULUM:
{curriculum}
"""
    content = [{"type": "text", "text": prompt}, {"type": "text", "text": "AUTHORITATIVE COMPLETE QUESTION"}, image(question_dir / "question_compact.png"), {"type": "text", "text": "AUTHORITATIVE OFFICIAL MARK SCHEME"}, image(question_dir / "markscheme.png")]
    payload = {"model": MODEL, "messages": [{"role": "system", "content": "You are a precise Cambridge Physics 9702 curriculum mapper. Return JSON only."}, {"role": "user", "content": content}], "temperature": 0, "reasoning": {"effort": "low"}, "max_tokens": 900}
    started = time.monotonic()
    errors = []
    for attempt in range(1, 6):
        try:
            request = Request(API_URL, data=json.dumps(payload).encode(), headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json", "HTTP-Referer": "https://kognitiv.edu", "X-Title": "Kognitiv Physics primary-topic pilot"}, method="POST")
            with urlopen(request, timeout=180) as response:
                raw = json.loads(response.read().decode())
            mapping = clean(raw["choices"][0]["message"].get("content"))
            issue = None
            if mapping.get("question_id") != item["question_id"]:
                issue = "question_id"
            elif mapping.get("primary_topic_id") not in candidates:
                issue = "primary_topic_id"
            elif mapping.get("confidence") not in {"high", "medium", "low"}:
                issue = "confidence"
            elif not str(mapping.get("reason") or "").strip():
                issue = "reason"
            if issue:
                errors.append(f"attempt {attempt}: {issue}")
                continue
            usage = raw.get("usage") or {}
            primary = mapping["primary_topic_id"]
            return {
                "status": "VALID",
                "component": component,
                "question_id": item["question_id"],
                "source": "muse",
                "primary_topic_id": primary,
                "secondary_topic_ids": [topic for topic in candidates if topic != primary],
                "part_mappings_unchanged": item["parts"],
                "candidate_topics": candidates,
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


def main() -> None:
    refs = {level: reference(level) for level in ("as", "a2")}
    api_key = key()
    jobs = []
    records = []
    for component, paper in PAPERS.items():
        level = "as" if component == "p2" else "a2"
        for question_dir in sorted(path for path in paper.glob("question_*") if path.is_dir()):
            item = evidence(question_dir)
            destination = OUT / component / f"{item['question_id']}.json"
            previous_attempts = 0
            if destination.exists():
                existing = load(destination)
                if existing.get("status") == "VALID":
                    records.append(existing)
                    continue
                previous_attempts = len(existing.get("errors") or [])
            if len(item["candidate_topics"]) == 1:
                records.append({
                    "status": "VALID",
                    "component": component,
                    "question_id": item["question_id"],
                    "source": "deterministic_single_topic",
                    "primary_topic_id": item["candidate_topics"][0],
                    "secondary_topic_ids": [],
                    "part_mappings_unchanged": item["parts"],
                    "candidate_topics": item["candidate_topics"],
                    "confidence": "high",
                    "reason": "Every mapped part already has the same topic.",
                    "attempt": 0,
                    "prompt_tokens": 0,
                    "completion_tokens": 0,
                    "cost_usd": 0,
                })
            else:
                jobs.append((question_dir, component, refs[level][0], refs[level][1], previous_attempts))
    with ThreadPoolExecutor(max_workers=min(13, len(jobs))) as executor:
        futures = {executor.submit(call, question_dir, component, curriculum, titles, api_key): previous_attempts for question_dir, component, curriculum, titles, previous_attempts in jobs}
        for index, future in enumerate(as_completed(futures), 1):
            result = future.result()
            result["prior_attempts"] = futures[future]
            records.append(result)
            print(f"{index}/{len(jobs)} {result['component']} {result['question_id']} {result['status']}", flush=True)
    for record in records:
        atomic(OUT / record["component"] / f"{record['question_id']}.json", record)
    manifest = {
        "schema_version": "9702_question_primary_topic_pilot_v1",
        "run_finished": datetime.now(timezone.utc).isoformat(),
        "model": MODEL,
        "papers": {component: str(path.relative_to(ROOT)) for component, path in PAPERS.items()},
        "totals": {
            "questions": len(records),
            "automatic": sum(record.get("source") == "deterministic_single_topic" for record in records),
            "api_calls": sum((int(record.get("attempt") or 0) + int(record.get("prior_attempts") or 0)) for record in records),
            "valid": sum(record.get("status") == "VALID" for record in records),
            "failed": sum(record.get("status") != "VALID" for record in records),
            "prompt_tokens": sum(int(record.get("prompt_tokens") or 0) for record in records),
            "completion_tokens": sum(int(record.get("completion_tokens") or 0) for record in records),
            "cost_usd": sum(float(record.get("cost_usd") or 0) for record in records),
        },
    }
    atomic(OUT / "manifest.json", manifest)
    print(json.dumps(manifest["totals"], indent=2))
    if manifest["totals"]["failed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
