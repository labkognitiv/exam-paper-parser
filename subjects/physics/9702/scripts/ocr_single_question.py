#!/usr/bin/env python3
"""Run Gemini 3 Flash OCR on a single Physics P2 printable question image."""

from __future__ import annotations

import argparse
import base64
import json
import subprocess
import time
import urllib.request
from pathlib import Path

MODEL = "google/gemini-3-flash-preview"

SYSTEM_PROMPT = """You are an expert Cambridge Physics (9702) past paper digitizer.
Your goal is to produce an exact, high-fidelity JSON transcription of the physics question from the provided uncompressed printable question image.

OUTPUT JSON FORMAT:
{
  "question_num": int,
  "total_marks": int,
  "main_stem": "Initial narrative text introducing the question before any parts or figures (null if question starts immediately with a part like (a)). Use \\n\\n between paragraphs.",
  "parts": [
    {
      "label": "(a)(i)",
      "part_stem": "Introductory narrative prose shared across child subparts (e.g. in Q2(b) before (i) and (ii)). If this part is standalone with no child subparts (e.g. (b) or (c)), keep its narrative inside 'text' and set 'part_stem' to null.",
      "text": "The question prompt text. Use \\n\\n for paragraph breaks. All math/formulas strictly enclosed in $...$ or $$...$$. Never output raw dotted answer lines (.....) or mark brackets [2]. If a diagram/figure appears here, place an anchor token {{figure:fig_X_Y}} exactly where the figure visually sits relative to the text.",
      "marks": int,
      "answer_prompt": "Prompt label preceding the answer line (e.g. 'SI base units', 'T =', 'resultant moment =', 'speed =') or null if none.",
      "unit": "SI unit printed at the end of the answer space (e.g. 'kg m^{-1} s^{-2}', 'N', 'N m', 'J', 'm s^{-1}', '%', 'e') formatted for KaTeX or null if none.",
      "figures": ["Fig. X.Y"]
    }
  ]
}

STRICT DIGITIZATION RULES:
1. FORMULAS & MATH: Every variable ($m$, $t$, $L$, $R$, $k$, $p_1$, $p_2$), exponent ($R^4$, $10^{-4}$), Greek letter ($\\rho$, $\\pi$), fraction ($\\frac{\\pi(p_2 - p_1)R^4 \\rho t}{8kL}$), and unit must be valid KaTeX math.
2. ANSWER PROMPTS & UNITS: Scrutinize the bottom-right of every sub-question. If there is an answer prompt like 'SI base units' or 'speed =', capture it in 'answer_prompt'. If there is a unit like 'N' or 'kg m^{-1} s^{-2}', capture it in 'unit'.
3. NO RAW DOTTED LINES: Omit dotted answer lines (......).
4. MARKS: Every subpart must have its exact integer mark from the right margin. Sum of all parts' marks must exactly equal 'total_marks'.
5. EXACT TEXT ACCURACY: Transcribe every word and condition verbatim (e.g. 'State and explain, quantitatively, which of these two quantities contributes more...').
"""


def get_api_key() -> str:
    return subprocess.check_output(
        ["security", "find-generic-password", "-s", "kognitiv-openrouter-api-key", "-a", "abdullahaftab", "-w"]
    ).decode().strip()


def digitize_question(image_path: Path, output_json_path: Path) -> dict[str, object]:
    api_key = get_api_key()
    img_b64 = base64.b64encode(image_path.read_bytes()).decode("utf-8")

    payload = {
        "model": MODEL,
        "temperature": 0.0,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Digitize this Cambridge Physics 9702 P2 question image with 100% fidelity: {image_path.name}"
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{img_b64}"}
                    }
                ]
            }
        ]
    }

    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://kognitiv.dev",
            "X-Title": "Kognitiv Physics Digitizer"
        }
    )

    start_time = time.time()
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    latency = time.time() - start_time

    raw_content = res["choices"][0]["message"]["content"].strip()
    if raw_content.startswith("```json"):
        raw_content = raw_content[7:]
    if raw_content.startswith("```"):
        raw_content = raw_content[3:]
    if raw_content.endswith("```"):
        raw_content = raw_content[:-3]

    data = json.loads(raw_content.strip())
    if isinstance(data, list) and len(data) > 0:
        data = data[0]

    usage = res.get("usage", {})
    prompt_tokens = usage.get("prompt_tokens", 0)
    completion_tokens = usage.get("completion_tokens", 0)
    cost = (prompt_tokens * 0.50 + completion_tokens * 3.00) / 1_000_000

    data["meta"] = {
        "model": MODEL,
        "latency_seconds": round(latency, 2),
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "cost_usd": round(cost, 5),
        "source_image": image_path.name
    }

    output_json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", type=Path, nargs="?", help="Printable question image")
    parser.add_argument("--output", type=Path, default=None, help="Output JSON path")
    args = parser.parse_args()

    default_image = Path(
        "/Users/abdullahaftab/Kognitiv/exam-paper-parser/subjects/physics/9702/testing/output_s23_22/question_01_printable.png"
    )
    image_path = args.image_path or default_image
    output_path = args.output or image_path.parent / (image_path.stem.replace("_printable", "") + "_ocr_gemini.json")

    print(f"Running Gemini 3 Flash OCR on {image_path.name}...")
    data = digitize_question(image_path, output_path)
    print(f"Done in {data['meta']['latency_seconds']}s (Cost: ${data['meta']['cost_usd']})")
    print(f"Wrote {output_path.name}")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
