#!/usr/bin/env python3
"""
Model Comparison Test for Pedagogical Enrichment
Compares 3 multimodal vision models on Cambridge Physics 9702 (May/June 2023 Paper 22 Question 4):
1. Meta Muse Spark 1.3 Contributor (meta/muse-spark-1.3-contributor)
2. Qwen 3.8 Flash (qwen/qwen3.8-flash)
3. Gemini 3.8 Flash (google/gemini-3.8-flash)

Measures:
- Latency (seconds)
- Cost (USD)
- Token breakdown (prompt, completion, reasoning)
- Mark-proportional hint adherence (1 mark = 1 hint, 2 marks = 2 hints)
- Graph coordinate reading accuracy (L0 = 8.0 cm, extension calculations)
- Teacher walkthrough pedagogical tone and step-by-step intermediate calculations
- Zero em/en dashes adherence
"""

import json
import base64
import time
import re
import urllib.request
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
IMG_PATH = ROOT_DIR / "9702/prototypes/past-paper-question-reviewer/public/data/assets/9702_s23_22_q04/figure_4_1.png"
OUTPUT_FILE = ROOT_DIR / "testing/q04_enrichment_comparison.json"

def get_api_key():
    cmd = ["security", "find-generic-password", "-s", "kognitiv-openrouter-api-key", "-w"]
    return subprocess.check_output(cmd).decode("utf-8").strip()

MODELS = [
    {
        "id": "meta/muse-spark-1.3-contributor",
        "name": "Meta Muse Spark 1.3 Contributor",
        "pricing_prompt_per_m": 0.10,
        "pricing_compl_per_m": 0.20
    },
    {
        "id": "qwen/qwen3.8-flash",
        "name": "Qwen 3.8 Flash",
        "pricing_prompt_per_m": 0.15,
        "pricing_compl_per_m": 0.47
    },
    {
        "id": "google/gemini-3.8-flash",
        "name": "Google Gemini 3.8 Flash",
        "pricing_prompt_per_m": 0.75,
        "pricing_compl_per_m": 3.75
    }
]

SYSTEM_PROMPT = """You are an expert Cambridge International AS-Level Physics (9702) teacher and curriculum author.
Your task is to generate high-quality pedagogical learning content and student enrichment for a past exam question.

You are provided with:
1. Question Stem and Parts text.
2. Official Cambridge Mark Scheme text and marks.
3. Cropped diagram / graph image (Fig. 4.1).

You must output a single, strictly valid JSON object. Do not include markdown codeblocks around the JSON if possible, or use standard ```json ... ```.

### Pedagogical Requirements:

1. **Mark-Proportional Tiered Progressive Hints**:
   - The number of hints for each part MUST strictly equal its mark count:
     * 1 mark = exactly 1 conceptual hint.
     * 2 marks = exactly 2 tiered progressive hints.
     * 3 marks = exactly 3 tiered progressive hints.
   - Hints must be progressive:
     * Hint 1 directs student attention to the core physics concept, definition, or initial graph observation.
     * Hint 2 directs the student to the required formula setup, variable relationship, or necessary unit conversion.
     * Subsequent hints guide the algebraic rearrangement.
   - NEVER give away the final numerical answer or final calculated value in hints.

2. **Humane Teacher Walkthrough (`teacher_walkthrough`)**:
   - Written in a warm, encouraging, student-friendly teacher-to-student tone (like Cambridge M1/S1 mechanics walkthroughs).
   - Explains the intuitive "why" behind each step.
   - Shows EVERY intermediate algebraic and numerical step explicitly without skipping steps (e.g. show the substitution line, clearing fractions, and arithmetic).
   - Formats math with LaTeX: display formulas in `$$...$$` on their own lines, inline variables in `$x$`.
   - STRICT RULE: NO em dashes ("—") and NO en dashes ("–") in the prose. Use commas, parentheses, colons, or clean sentences instead.

3. **Technical Mark Scheme Walkthrough (`walkthrough`)**:
   - A concise, precise step-by-step derivation matching official Cambridge examiner marking points (e.g. C1 formula, A1 answer).

4. **Common Student Pitfalls (`common_pitfalls`)**:
   - 2 to 3 real, examiner-identified traps students fall into (e.g. reading total length instead of extension from the graph, forgetting unstretched length at F=0, forgetting cm to m unit conversions, omitting 1/2 in energy formula).

5. **Difficulty & Question Patterns**:
   - `difficulty`: integer 1 to 5 (1 = very easy, 5 = extremely challenging).
   - `question_patterns`: array of standard pattern strings, e.g.:
     ["property_identification"], ["graph_interpretation", "direct_calculation"], ["algebraic_derivation"].

### Schema:
{
  "question_difficulty": 2,
  "question_patterns": ["property_identification", "graph_interpretation", "direct_calculation"],
  "parts": [
    {
      "part_id": "9702_s23_22_q04_a",
      "difficulty": 1,
      "question_patterns": ["property_identification"],
      "hints": [
        "..."
      ],
      "walkthrough": [
        "..."
      ],
      "teacher_walkthrough": [
        "..."
      ],
      "common_pitfalls": [
        "..."
      ]
    },
    {
      "part_id": "9702_s23_22_q04_b",
      "difficulty": 2,
      "question_patterns": ["graph_interpretation", "direct_calculation"],
      "hints": [
        "Hint 1...",
        "Hint 2..."
      ],
      "walkthrough": [
        "..."
      ],
      "teacher_walkthrough": [
        "..."
      ],
      "common_pitfalls": [
        "..."
      ]
    },
    {
      "part_id": "9702_s23_22_q04_c",
      "difficulty": 2,
      "question_patterns": ["graph_interpretation", "direct_calculation"],
      "hints": [
        "Hint 1...",
        "Hint 2..."
      ],
      "walkthrough": [
        "..."
      ],
      "teacher_walkthrough": [
        "..."
      ],
      "common_pitfalls": [
        "..."
      ]
    }
  ]
}
"""

QUESTION_CONTENT = """### Question Information
**Paper**: Cambridge AS-Level Physics 9702/22/M/J/23 Question 4
**Total Marks**: 5

**Stem**:
A spring is suspended from a fixed point at one end. The spring is extended by a vertical force applied to the other end. The variation of the applied force $F$ with the length $L$ of the spring is shown in Fig. 4.1.
For the spring:

**Part (a)** [1 mark]:
state the name of the law that gives the relationship between the force and the extension

**Part (b)** [2 marks]:
determine the spring constant, in $\\text{N m}^{-1}$
$$\\text{spring constant} = \\text{...................................................}\\text{ N m}^{-1}$$

**Part (c)** [2 marks]:
determine the elastic potential energy when $F = 6.0\\text{ N}$.
$$\\text{elastic potential energy} = \\text{...................................................}\\text{ J}$$

---
### Official Mark Scheme
**Part (a)** [1 mark]:
- B1: Hooke’s (law)

**Part (b)** [2 marks]:
- C1: $k = F / x$ or $k = \\text{gradient}$
- A1: $= \\text{e.g. } 12.0 / (0.240 - 0.08) = 75\\text{ N m}^{-1}$

**Part (c)** [2 marks]:
- C1: $E = \\frac{1}{2} F x$ or $E = \\frac{1}{2} k x^2$ or $E = \\text{area under graph}$
- A1: $E = \\frac{1}{2} \\times 6.0 \\times 0.080$ or $\\frac{1}{2} \\times 75 \\times 0.08^2 = 0.24\\text{ J}$

---
Refer to the attached image (Fig. 4.1) showing Force $F$ vs Length $L$ in cm. Note carefully the unstretched length when $F = 0$.
Now generate the complete JSON enrichment following the specified pedagogical standards and schema.
"""

def extract_json(raw_text):
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
                return json.loads(candidate[start:end+1])
            except Exception:
                return None
    return None

def analyze_output(parsed_json, raw_text):
    metrics = {
        "valid_json": parsed_json is not None,
        "dash_violations": [],
        "hint_counts": {},
        "hint_proportionality_pass": False,
        "graph_l0_recognized": False,
        "part_b_extension_correct": False,
        "part_c_extension_correct": False,
    }
    
    em_dashes = len(re.findall(r"—", raw_text))
    en_dashes = len(re.findall(r"–", raw_text))
    if em_dashes > 0 or en_dashes > 0:
        metrics["dash_violations"].append(f"Found {em_dashes} em-dashes and {en_dashes} en-dashes.")
    
    text_lower = raw_text.lower()
    if "8" in text_lower and ("unstretched" in text_lower or "zero" in text_lower or "l_0" in text_lower or "initial length" in text_lower or "intercept" in text_lower or "0.08" in text_lower):
        metrics["graph_l0_recognized"] = True
    
    if "0.16" in raw_text or "16 cm" in raw_text or "24 - 8" in raw_text or "0.24 - 0.08" in raw_text or "0.240 - 0.08" in raw_text:
        metrics["part_b_extension_correct"] = True
        
    if "0.08" in raw_text or "8 cm" in raw_text or "16 - 8" in raw_text or "0.16 - 0.08" in raw_text or "0.24" in raw_text:
        metrics["part_c_extension_correct"] = True

    if parsed_json and "parts" in parsed_json:
        parts = parsed_json["parts"]
        counts = {}
        for p in parts:
            pid = p.get("part_id", "unknown")
            hints = p.get("hints", [])
            counts[pid] = len(hints)
        metrics["hint_counts"] = counts
        p_a = next((p for p in parts if "q04_a" in p.get("part_id", "")), None)
        p_b = next((p for p in parts if "q04_b" in p.get("part_id", "")), None)
        p_c = next((p for p in parts if "q04_c" in p.get("part_id", "")), None)
        
        if (p_a and len(p_a.get("hints", [])) == 1 and
            p_b and len(p_b.get("hints", [])) == 2 and
            p_c and len(p_c.get("hints", [])) == 2):
            metrics["hint_proportionality_pass"] = True
            
    return metrics

def run_model(model_info, api_key, b64_img):
    model_id = model_info["id"]
    print(f"\n========================================================")
    print(f"Calling: {model_info['name']} ({model_id})")
    print(f"========================================================")
    
    req_body = {
        "model": model_id,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": QUESTION_CONTENT},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{b64_img}"
                        }
                    }
                ]
            }
        ],
        "reasoning": {"effort": "low"},
        "max_tokens": 6000,
        "temperature": 0.2
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://kognitiv.io",
        "X-Title": "Kognitiv Exam Parser"
    }
    
    max_retries = 4
    for attempt in range(max_retries):
        try:
            start_time = time.time()
            req = urllib.request.Request(
                "https://openrouter.ai/api/v1/chat/completions",
                data=json.dumps(req_body).encode("utf-8"),
                headers=headers
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                elapsed = time.time() - start_time
                resp_data = json.loads(resp.read().decode("utf-8"))
                
                choice = resp_data["choices"][0]
                message = choice["message"]
                raw_content = message.get("content") or ""
                reasoning = message.get("reasoning") or ""
                usage = resp_data.get("usage", {})
                
                prompt_tokens = usage.get("prompt_tokens", 0)
                completion_tokens = usage.get("completion_tokens", 0)
                reasoning_tokens = usage.get("completion_tokens_details", {}).get("reasoning_tokens", 0)
                
                prompt_cost = (prompt_tokens / 1_000_000) * model_info["pricing_prompt_per_m"]
                compl_cost = (completion_tokens / 1_000_000) * model_info["pricing_compl_per_m"]
                total_cost = prompt_cost + compl_cost
                
                if "cost" in usage and usage["cost"] is not None:
                    total_cost = usage["cost"]
                    
                parsed_json = extract_json(raw_content)
                metrics = analyze_output(parsed_json, raw_content)
                
                print(f"SUCCESS in {elapsed:.2f}s | Tokens: {prompt_tokens} in, {completion_tokens} out (Reasoning: {reasoning_tokens}) | Cost: ${total_cost:.6f}")
                print(f"Valid JSON: {metrics['valid_json']} | Hint Proportionality Pass: {metrics['hint_proportionality_pass']}")
                print(f"Dash Violations: {metrics['dash_violations']}")
                
                return {
                    "model_id": model_id,
                    "model_name": model_info["name"],
                    "elapsed_sec": round(elapsed, 2),
                    "tokens": {
                        "prompt_tokens": prompt_tokens,
                        "completion_tokens": completion_tokens,
                        "reasoning_tokens": reasoning_tokens,
                        "total_tokens": prompt_tokens + completion_tokens
                    },
                    "cost_usd": round(total_cost, 6),
                    "metrics": metrics,
                    "parsed_json": parsed_json,
                    "raw_content": raw_content,
                    "reasoning": reasoning
                }
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            if hasattr(e, "read"):
                try:
                    err_json = json.loads(e.read().decode("utf-8"))
                    print(f"Error details: {err_json}")
                except Exception:
                    pass
            if attempt < max_retries - 1:
                sleep_sec = 4 * (attempt + 1)
                print(f"Waiting {sleep_sec}s before retry...")
                time.sleep(sleep_sec)
            else:
                return {
                    "model_id": model_id,
                    "model_name": model_info["name"],
                    "error": str(e),
                    "parsed_json": None
                }

def main():
    api_key = get_api_key()
    print(f"Loading diagram image: {IMG_PATH}")
    with open(IMG_PATH, "rb") as f:
        b64_img = base64.b64encode(f.read()).decode("utf-8")
        
    results = {}
    for model_info in MODELS:
        res = run_model(model_info, api_key, b64_img)
        results[model_info["id"]] = res
        time.sleep(3)
        
    print(f"\nWriting comparison results to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print("Done!")

if __name__ == "__main__":
    main()
