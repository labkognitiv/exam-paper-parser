#!/usr/bin/env python3
"""AI Theory Pedagogical Enrichment Generator for Cambridge Physics (9702) Paper 2.

Uses Meta Muse Spark (meta/muse-spark-1.3-contributor) via OpenRouter to generate:
- Mark-scaled hints: exactly N progressive hints for an N-mark question part.
- Stepped teacher walkthroughs explaining physical principles, algebraic derivations, and substitutions.
- Model proper answers with significant figures and SI units.
- Question patterns and difficulty ratings (1 to 5).
- Clean typography: zero em dashes, zero en dashes, balanced KaTeX math.
"""

from __future__ import annotations

import argparse
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import re
import subprocess
import sys
import time
import urllib.request

REPO_ROOT = next(
    (p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()),
    Path(__file__).resolve().parents[3],
)
PHYSICS_PAPERS_ROOT = REPO_ROOT / "subjects/physics/9702/past papers"

DEFAULT_MODEL_ID = "meta/muse-spark-1.3-contributor"
MODEL_PRICING = {
    "meta/muse-spark-1.3-contributor": {"prompt": 0.10 / 1_000_000, "completion": 0.20 / 1_000_000},
}


def get_api_key() -> str:
    """Retrieve OpenRouter API key from macOS Keychain."""
    cmd = ["security", "find-generic-password", "-s", "kognitiv-openrouter-api-key", "-w"]
    try:
        return subprocess.check_output(cmd).decode("utf-8").strip()
    except Exception as exc:
        raise RuntimeError(f"Failed to retrieve OpenRouter API key from Keychain: {exc}")


PHYSICS_THEORY_ENRICHMENT_PROMPT = """You are an expert Cambridge International AS & A Level Physics (9702) master teacher.
Your task is to generate warm, supportive, student-friendly pedagogical enrichment for this structured theory question, using the provided authentic Question Paper page and the official digitized Mark Scheme.

OUTPUT JSON SCHEMA:
{
  "schema_version": "9702_theory_enrichment_v1",
  "question_id": "9702_s24_21_q01",
  "difficulty": 2, // Overall question difficulty (1 to 5)
  "question_patterns": ["direct_calculation", "explanation"], // Ordered union of patterns
  "parts": [
    {
      "part_id": "9702_s24_21_q01_a",
      "label": "(a)",
      "marks": 2,
      "difficulty": 1, // Subpart difficulty (1 to 5)
      "question_patterns": ["direct_calculation"], // e.g. direct_calculation, algebraic_derivation, graph_interpretation, explanation, definition, circuit_analysis
      "key_concepts": ["concept 1", "concept 2"],
      "hints": [
        "Hint 1: First progressive clue directing student attention to the given data, diagram, or governing physical law without giving away the formula or answer.",
        "Hint 2: Second progressive clue guiding toward algebraic rearrangement or unit alignment."
      ],
      "proper_answer": "Concise, examiner-standard model solution matching Cambridge marking criteria with significant figures and SI units.",
      "walkthrough": [
        "Step 1: **Clear Descriptive Heading**\\nDirect teacher-to-student explanation of the physical principle...",
        "Step 2: **Next Heading**\\nAlgebraic steps and calculation in KaTeX ($$...$$)."
      ]
    }
  ]
}

STRICT PEDAGOGICAL & ARCHITECTURAL STANDARDS:

1. HINT SCALING RULE (STRICT):
   - The number of hints for each subpart MUST EXACTLY EQUAL its mark allocation (N marks = N hints).
   - If a part has 1 mark: exactly 1 hint.
   - If a part has 2 marks: exactly 2 hints.
   - If a part has 3 marks: exactly 3 hints.
   - If a part has 4 or 5 marks: exactly 4 or 5 hints.
   - Anti-Spoiler Guard: Hint 1 must NEVER reveal the final numerical answer, formula, or product directly. It scaffolds how to approach the problem.

2. PROPER ANSWER:
   - Provide a concise, complete, examiner-standard model answer ('proper_answer') matching official Cambridge mark scheme criteria.
   - For calculations: include final numerical value with correct significant figures (usually 2 or 3 s.f.) and SI units (e.g. $4.8 \\times 10^3\\text{ N}$, $0.42\\text{ m s}^{-1}$).
   - For explanations: include key required physical principles clearly and compactly.

3. STEPPED TEACHER WALKTHROUGH (TEACHER'S PERSPECTIVE):
   - Structure into logical steps: 'Step N: **Descriptive Heading**'.
   - Voice and Tone: Write from the perspective of an experienced teacher explaining one-on-one to a student sitting beside them.
   - Demystify terms: Explain tricky physical terminology simply and address common misconceptions upfront.
   - NEVER use detached meta-language: Do NOT write 'The question asks you to...', 'Notice the command word...', 'The examiner wants...'.
   - Teach how to think: Guide the student through the mental model:
     * For calculations: What physical law governs this? What values are given and in what units? How do we rearrange algebraically before plugging in numbers? Display equations in KaTeX ($$...$$).
     * For derivations: Show the logical step-by-step mathematical path clearly.
     * For explanations: What physical mechanism causes this effect (e.g. Newton's 3rd law, wave interference, drift velocity)?

4. NO CHECKING ENGINE:
   - Do NOT include 'checking', 'checking_mode', or 'deterministic_checks'. Only pedagogical content.

5. FORMATTING RULES:
   - Math and physical units in KaTeX: $...$ for inline, $$...$$ for standalone display equations.
   - Variables in math font: $v$, $a$, $t$, $m$, $F$. Units in upright text: $\\text{m s}^{-1}$, $\\text{kg m s}^{-2}$, $\\text{N}$.
   - STRICT: Zero em dashes ('—') and zero en dashes ('–'). Use standard ASCII hyphens (-) instead.
   - Output strictly valid JSON matching the schema.
"""


def extract_json(raw_text: str) -> dict | None:
    if not raw_text:
        return None
    m = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", raw_text)
    candidate = m.group(1) if m else raw_text.strip()
    try:
        return json.loads(candidate)
    except Exception:
        start = candidate.find("{")
        end = candidate.rfind("}")
        if start != -1 and end != -1:
            try:
                return json.loads(candidate[start : end + 1])
            except Exception:
                return None
    return None


def sanitize_dashes(text: str) -> str:
    return text.replace("—", " - ").replace("–", "-")


def sanitize_enrichment(data: dict) -> dict:
    if isinstance(data, dict):
        return {k: sanitize_enrichment(v) for k, v in data.items()}
    if isinstance(data, list):
        return [sanitize_enrichment(x) for x in data]
    if isinstance(data, str):
        return sanitize_dashes(data)
    return data


def call_llm(
    api_key: str,
    system_prompt: str,
    user_content: list[dict],
    model_id: str = DEFAULT_MODEL_ID,
    max_tokens: int = 7000,
    max_retries: int = 3,
) -> dict:
    req_body = {
        "model": model_id,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        "reasoning": {"effort": "low"},
        "max_tokens": max_tokens,
        "temperature": 0.1,
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://kognitiv.io",
        "X-Title": "Kognitiv Physics Theory Enricher",
    }

    pricing = MODEL_PRICING.get(model_id, MODEL_PRICING[DEFAULT_MODEL_ID])

    for attempt in range(max_retries):
        try:
            start_time = time.time()
            req = urllib.request.Request(
                "https://openrouter.ai/api/v1/chat/completions",
                data=json.dumps(req_body).encode("utf-8"),
                headers=headers,
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                elapsed = time.time() - start_time
                data = json.loads(resp.read().decode("utf-8"))

                choice = data["choices"][0]
                raw_content = choice["message"].get("content") or ""
                usage = data.get("usage", {})

                prompt_tokens = usage.get("prompt_tokens", 0)
                completion_tokens = usage.get("completion_tokens", 0)
                reasoning_tokens = usage.get("completion_tokens_details", {}).get("reasoning_tokens", 0)

                cost = usage.get("cost")
                if cost is None:
                    cost = (prompt_tokens * pricing["prompt"]) + (completion_tokens * pricing["completion"])

                parsed_json = extract_json(raw_content)

                return {
                    "model": model_id,
                    "elapsed_sec": round(elapsed, 2),
                    "tokens": {
                        "prompt_tokens": prompt_tokens,
                        "completion_tokens": completion_tokens,
                        "reasoning_tokens": reasoning_tokens,
                        "total_tokens": prompt_tokens + completion_tokens,
                    },
                    "cost_usd": round(cost, 6),
                    "valid_json": parsed_json is not None,
                    "parsed_json": parsed_json,
                    "raw_content": raw_content,
                }
        except Exception as exc:
            if attempt < max_retries - 1:
                wait_sec = 3 * (attempt + 1)
                time.sleep(wait_sec)
            else:
                return {
                    "model": model_id,
                    "elapsed_sec": 0,
                    "tokens": {"prompt_tokens": 0, "completion_tokens": 0, "reasoning_tokens": 0, "total_tokens": 0},
                    "cost_usd": 0.0,
                    "valid_json": False,
                    "parsed_json": None,
                    "raw_content": f"Error: {exc}",
                }
    return {}


def enforce_hint_scaling(enrichment: dict, official_ms: dict) -> dict:
    ms_parts = [p for p in official_ms.get("parts", []) if isinstance(p, dict)]
    ms_parts_map = {p.get("id"): p for p in ms_parts}

    enr_parts = [p for p in enrichment.get("parts", []) if isinstance(p, dict)]

    # If counts match, align part_id and label deterministically
    if len(enr_parts) == len(ms_parts):
        for p, ms_p in zip(enr_parts, ms_parts):
            p["part_id"] = ms_p.get("id")
            if ms_p.get("label"):
                p["label"] = ms_p.get("label")

    for idx, p in enumerate(enr_parts):
        pid = p.get("part_id")
        ms_part = ms_parts_map.get(pid)
        if not ms_part and idx < len(ms_parts):
            ms_part = ms_parts[idx]
            p["part_id"] = ms_part.get("id")
            if ms_part.get("label"):
                p["label"] = ms_part.get("label")
        expected_marks = ms_part.get("marks", p.get("marks", 1)) if ms_part else p.get("marks", 1)
        p["marks"] = expected_marks

        hints = p.get("hints", [])
        if not isinstance(hints, list):
            hints = [str(hints)] if hints else []

        if len(hints) > expected_marks:
            p["hints"] = hints[:expected_marks]
        elif len(hints) < expected_marks:
            walk = p.get("walkthrough", [])
            while len(hints) < expected_marks:
                step_idx = len(hints)
                if step_idx < len(walk):
                    step_text = re.sub(r"^Step\s*\d+\s*:\s*\*\*.*?\*\*\s*", "", walk[step_idx]).strip()
                    first_sent = step_text.split(".")[0].strip() + "."
                    hints.append(f"Hint {len(hints) + 1}: Consider {first_sent.lower()}")
                else:
                    hints.append(f"Hint {len(hints) + 1}: Apply the governing physical formula to calculate your answer.")
            p["hints"] = hints

    return enrichment


def enrich_single_theory_question(
    q_dir: Path,
    api_key: str,
    model_id: str = DEFAULT_MODEL_ID,
    force: bool = False,
) -> tuple[str, dict | None, dict, bool]:
    ms_json_path = q_dir / "markscheme.json"
    qp_img_path = q_dir / "question_printable.png"
    enr_json_path = q_dir / "enrichment.json"
    enr_meta_path = q_dir / "enrichment_meta.json"

    if not ms_json_path.is_file():
        raise FileNotFoundError(f"Missing markscheme.json in {q_dir}")
    if not qp_img_path.is_file():
        qp_img_path = q_dir / "question_compact.png"
        if not qp_img_path.is_file():
            raise FileNotFoundError(f"Missing question image in {q_dir}")

    if not force and enr_json_path.is_file() and enr_meta_path.is_file():
        try:
            with open(enr_json_path, encoding="utf-8") as f:
                data = json.load(f)
            with open(enr_meta_path, encoding="utf-8") as f:
                meta = json.load(f)
            return q_dir.name, data, meta, True
        except Exception:
            pass

    with open(ms_json_path, encoding="utf-8") as f:
        ms_data = json.load(f)

    with open(qp_img_path, "rb") as f:
        b64_img = base64.b64encode(f.read()).decode("utf-8")

    q_id = ms_data.get("question_id", q_dir.name)
    total_marks = ms_data.get("total_marks", 0)
    parts_summary = [
        f"Part {p.get('label', '')} (ID: {p.get('id')}): {p.get('marks')} mark(s)"
        for p in ms_data.get("parts", [])
    ]
    parts_str = "\n".join(parts_summary)

    user_content = [
        {
            "type": "text",
            "text": (
                f"Question: {q_id}\nTotal Marks: {total_marks}\n\n"
                f"Parts List:\n{parts_str}\n\n"
                f"Official Mark Scheme JSON:\n{json.dumps(ms_data, indent=2, ensure_ascii=False)}\n\n"
                "Generate pedagogical enrichment for all parts. Remember the strict rule: exactly N progressive hints for an N-mark subpart."
            ),
        },
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_img}"}},
    ]

    res = call_llm(api_key, PHYSICS_THEORY_ENRICHMENT_PROMPT, user_content, model_id=model_id, max_tokens=7000)
    pj = res.get("parsed_json")

    if not pj:
        pj = {"error": "Invalid JSON returned", "raw": res.get("raw_content")}
    else:
        pj = sanitize_enrichment(pj)
        pj["schema_version"] = "9702_theory_enrichment_v1"
        pj["question_id"] = q_id
        pj["total_marks"] = total_marks
        pj = enforce_hint_scaling(pj, ms_data)

        all_patterns = []
        for p in pj.get("parts", []):
            for pat in p.get("question_patterns", []):
                if pat not in all_patterns:
                    all_patterns.append(pat)
        pj["question_patterns"] = all_patterns

        with open(enr_json_path, "w", encoding="utf-8") as f:
            json.dump(pj, f, indent=2, ensure_ascii=False)
            f.write("\n")

        with open(enr_meta_path, "w", encoding="utf-8") as f:
            meta = {
                "model": res.get("model"),
                "elapsed_sec": res.get("elapsed_sec"),
                "tokens": res.get("tokens"),
                "cost_usd": res.get("cost_usd"),
                "valid_json": res.get("valid_json"),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
            }
            json.dump(meta, f, indent=2)
            f.write("\n")

    return q_dir.name, pj, res, False


def process_paper_theory_enrichment(
    paper_query: str,
    question_filter: int | None = None,
    force: bool = False,
    max_workers: int = 6,
) -> dict:
    from check_p2_extraction import find_p2_paper_dir
    code, variant_dir = find_p2_paper_dir(paper_query)
    api_key = get_api_key()

    q_dirs = sorted([d for d in variant_dir.iterdir() if d.is_dir() and d.name.startswith("question_")])
    if question_filter is not None:
        q_dirs = [d for d in q_dirs if int(d.name.split("_")[-1]) == question_filter]

    results = []
    total_cost = 0.0
    total_tokens = 0
    t0 = time.time()

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        future_to_qd = {
            pool.submit(enrich_single_theory_question, qd, api_key, force=force): qd
            for qd in q_dirs
        }
        for future in as_completed(future_to_qd):
            q_name, data, meta, was_cached = future.result()
            results.append((q_name, data, meta))
            if not was_cached:
                total_cost += meta.get("cost_usd", 0.0)
                toks = meta.get("tokens", {})
                total_tokens += toks.get("total_tokens", 0)

    elapsed = round(time.time() - t0, 2)
    return {
        "paper_code": code,
        "questions_processed": len(results),
        "total_cost_usd": total_cost,
        "total_tokens": total_tokens,
        "total_elapsed_sec": elapsed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Enrich Physics P2 questions via Meta Muse Spark")
    parser.add_argument("paper", help="Paper query or directory")
    parser.add_argument("--question", type=int, help="Optional specific question")
    parser.add_argument("--force", action="store_true", help="Force re-enrichment")
    parser.add_argument("--max-workers", type=int, default=6, help="Worker threads")
    args = parser.parse_args()

    res = process_paper_theory_enrichment(args.paper, question_filter=args.question, force=args.force, max_workers=args.max_workers)
    print(f"Done: {res['questions_processed']} questions enriched | Cost: ${res['total_cost_usd']:.5f} | Time: {res['total_elapsed_sec']}s")


if __name__ == "__main__":
    main()
