#!/usr/bin/env python3
import argparse, csv, json, re
from collections import Counter
from pathlib import Path

HEADER = ["question_id", "primary_skill", "skill_tags", "ai_rubric", "rubric_id"]
VAGUE = {"physics knowledge", "calculation", "problem solving", "understanding the question"}
RAW_MATH_UNICODE = re.compile(r"[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎√×±∝½⅓⅔¼¾αβγδεζηθικλμνξοπρστυφχψωΔΘΛΞΠΣΦΨΩū]")

def web_math_errors(value):
    errors=[]
    if RAW_MATH_UNICODE.search(value) or "\u0304" in value: errors.append("raw Unicode mathematical notation")
    if value.count("$")%2: return errors+["unbalanced inline $ delimiters"]
    for index,part in enumerate(value.split("$")):
        if index%2:
            if not part.strip(): errors.append("empty inline math span")
            if part.count("{")!=part.count("}"): errors.append("unbalanced braces")
        elif "\\" in part or re.search(r"[=<>^_]",part) or re.search(r"\b[A-Za-z]\s*/\s*[A-Za-z]\b",part):
            errors.append("un-delimited mathematical expression")
    return errors

def rows(path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f); return list(r.fieldnames or []), list(r)

def main():
    p=argparse.ArgumentParser(); p.add_argument("--questions",type=Path,required=True); p.add_argument("--mapping-qc",type=Path,required=True); p.add_argument("--skill-library",type=Path,required=True); p.add_argument("--assignments",type=Path,required=True); p.add_argument("--output",type=Path); a=p.parse_args()
    errors=[]; qh,qs=rows(a.questions); ah,aa=rows(a.assignments); _,library=rows(a.skill_library)
    approved={r.get("skill_name") for r in library if r.get("status")=="approved"}
    qc=json.loads(a.mapping_qc.read_text())
    if qc.get("final_status")!="passed": errors.append("taxonomy mapping QC is not passed")
    if ah!=HEADER: errors.append("assignment header does not match contract")
    qids=[r.get("question_id","") for r in qs]; aids=[r.get("question_id","") for r in aa]
    if set(qids)!=set(aids) or len(qids)!=len(aids): errors.append("assignment coverage does not exactly match questions")
    if any(v>1 for v in Counter(aids).values()): errors.append("duplicate assignment question_id")
    for r in aa:
        qid=r.get("question_id",""); primary=r.get("primary_skill","").strip()
        if not primary or primary.lower() in VAGUE: errors.append(f"{qid}: invalid primary_skill")
        if primary and (primary[0].islower() or "_" in primary): errors.append(f"{qid}: primary_skill is not human-readable title text")
        try: tags=json.loads(r.get("skill_tags","")); rubric=json.loads(r.get("ai_rubric",""))
        except Exception: errors.append(f"{qid}: invalid JSON"); continue
        if not isinstance(tags,list) or not 1<=len(tags)<=2 or len(tags)!=len(set(tags)): errors.append(f"{qid}: skill_tags must contain one or two unique entries")
        if primary not in tags: errors.append(f"{qid}: primary_skill missing from skill_tags")
        for tag in tags:
            if tag not in approved: errors.append(f"{qid}: unregistered skill {tag!r}")
        if not isinstance(rubric,dict) or list(rubric)!=tags: errors.append(f"{qid}: ai_rubric keys must exactly match skill_tags order")
        else:
            for key,value in rubric.items():
                if not isinstance(value,str) or len(value.strip())<35 or len(value)>260: errors.append(f"{qid}: rubric for {key!r} is not a concise meaningful statement")
                if re.search(r"\b(M1|DM1|A1|B1|FT|AG)\b",value): errors.append(f"{qid}: rubric contains mark-code language")
                for issue in web_math_errors(value): errors.append(f"{qid}: rubric for {key!r}: {issue}")
        if r.get("rubric_id")!="single_select_mcq_v1": errors.append(f"{qid}: wrong rubric_id")
    out={"schema_version":"physics_mcq_skills_rubric_v1.1","final_status":"passed" if not errors else "failed","rows":len(aa),"one_skill_rows":0,"two_skill_rows":0,"errors":errors}
    for r in aa:
        try: n=len(json.loads(r.get("skill_tags","[]")))
        except Exception: n=0
        if n==1: out["one_skill_rows"]+=1
        if n==2: out["two_skill_rows"]+=1
    text=json.dumps(out,indent=2)+"\n"
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text)
    print(text,end=""); return 0 if not errors else 1
if __name__=="__main__": raise SystemExit(main())
