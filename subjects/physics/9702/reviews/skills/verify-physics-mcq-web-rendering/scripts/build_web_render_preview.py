#!/usr/bin/env python3
import argparse, csv, hashlib, html, json
from pathlib import Path

FIELDS = ["question_text", "option_a", "option_b", "option_c", "option_d"]

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--merged", type=Path, required=True)
    p.add_argument("--paper-code", required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    a = p.parse_args()
    with a.merged.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f); header = list(reader.fieldnames or []); rows = list(reader)
    required = {"question_id", "paper_code", "question_num", "display_mode", "ai_rubric", "reason", *FIELDS}
    errors = []
    if not required.issubset(header): errors.append(f"missing fields: {sorted(required-set(header))}")
    ids = [r.get("question_id", "") for r in rows]
    if len(rows) != 40 or len(set(ids)) != 40 or "" in ids: errors.append("merged CSV must contain 40 unique question IDs")
    if any(r.get("paper_code") != a.paper_code for r in rows): errors.append("paper_code mismatch")
    cards, math_ids, span_count = [], [], 0
    for row in rows:
        qid = row.get("question_id", "")
        try:
            rubric = json.loads(row.get("ai_rubric", ""))
            if not isinstance(rubric, dict) or not rubric or not all(isinstance(v, str) for v in rubric.values()): raise ValueError
            rubric_values = list(rubric.values())
        except Exception:
            errors.append(f"{qid}: ai_rubric is not a non-empty string-valued JSON object"); rubric_values = []
        values = [row.get(field, "") for field in FIELDS] + rubric_values + [row.get("reason", "")]
        spans = sum(v.count("$") // 2 for v in values)
        if spans: math_ids.append(qid)
        span_count += spans
        options = "".join(f'<li><strong>{letter.upper()}</strong> {html.escape(row.get(f"option_{letter}", ""))}</li>' for letter in "abcd" if row.get(f"option_{letter}"))
        rubrics = "".join(f"<p>{html.escape(value)}</p>" for value in rubric_values)
        cards.append(f'<section data-question-id="{html.escape(qid)}"><h2>{html.escape(qid)} · {html.escape(row.get("display_mode", ""))}</h2><p>{html.escape(row.get("question_text", ""))}</p><ol>{options}</ol><h3>Rubric</h3>{rubrics}<h3>Difficulty reason</h3><p>{html.escape(row.get("reason", ""))}</p></section>')
    if errors:
        raise SystemExit("\n".join(errors))
    skill_root = Path(__file__).resolve().parents[1]
    katex = skill_root / "assets" / "katex"
    a.output_dir.mkdir(parents=True, exist_ok=True)
    doc = f'''<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(a.paper_code)} web rendering QC</title><link rel="stylesheet" href="{(katex/'katex.min.css').as_uri()}"><style>body{{font:16px/1.55 Arial,sans-serif;max-width:980px;margin:24px auto;color:#172033}}section{{border:1px solid #d7deea;border-radius:10px;padding:14px 18px;margin:12px 0;break-inside:avoid}}h1{{font-size:24px}}h2{{font-size:15px;color:#45546f}}h3{{font-size:14px;margin-top:18px}}ol{{list-style:none;padding:0}}li{{margin:5px 0}}strong{{display:inline-block;width:24px}}</style><script defer src="{(katex/'katex.min.js').as_uri()}"></script><script defer src="{(katex/'auto-render.min.js').as_uri()}"></script></head><body data-expected-spans="{span_count}" data-math-ids="{html.escape(json.dumps(math_ids))}"><h1>{html.escape(a.paper_code)} — web rendering QC</h1>{''.join(cards)}<script>window.addEventListener('load',()=>{{try{{renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}],throwOnError:true}});window.mathRenderError='';}}catch(e){{window.mathRenderError=String(e);}}window.mathReady=true;}});</script></body></html>'''
    preview = a.output_dir / "web_render_preview.html"
    preview.write_text(doc, encoding="utf-8")
    report = {"schema_version":"physics_p1_mcq_web_render_preview_v1","paper_code":a.paper_code,"rows":len(rows),"rows_with_math":len(math_ids),"math_question_ids":math_ids,"expected_inline_math_spans":span_count,"merged_csv_sha256":sha(a.merged),"preview":str(preview)}
    (a.output_dir / "preview_build.json").write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(report, indent=2))

if __name__ == "__main__": main()
