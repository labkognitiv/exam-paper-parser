#!/usr/bin/env python3
import argparse,csv,json,re
from collections import Counter
from pathlib import Path
HEADER=["question_id","difficulty","practice_tier","reason"]
RAW_MATH_UNICODE=re.compile(r"[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎√×±∝½⅓⅔¼¾αβγδεζηθικλμνξοπρστυφχψωΔΘΛΞΠΣΦΨΩū]")
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
def rows(p):
    with p.open(newline="",encoding="utf-8-sig") as f:r=csv.DictReader(f);return list(r.fieldnames or []),list(r)
def main():
    p=argparse.ArgumentParser();p.add_argument("--questions",type=Path,required=True);p.add_argument("--skills",type=Path,required=True);p.add_argument("--assignments",type=Path,required=True);p.add_argument("--output",type=Path);a=p.parse_args()
    e=[];_,q=rows(a.questions);_,s=rows(a.skills);h,x=rows(a.assignments)
    if h!=HEADER:e.append("assignment header does not match contract")
    qids=[r.get("question_id","") for r in q];sids=[r.get("question_id","") for r in s];xids=[r.get("question_id","") for r in x]
    if set(qids)!=set(sids) or len(qids)!=len(sids):e.append("skills coverage does not match questions")
    if set(qids)!=set(xids) or len(qids)!=len(xids):e.append("tier coverage does not match questions")
    if any(v>1 for v in Counter(xids).values()):e.append("duplicate assignment question_id")
    for r in x:
        qid=r.get("question_id","")
        if r.get("difficulty") not in {"easy","medium","hard"}:e.append(f"{qid}: invalid difficulty")
        if r.get("practice_tier") not in {"mandatory","revision"}:e.append(f"{qid}: invalid practice_tier")
        if len(r.get("reason","").strip())<20:e.append(f"{qid}: reason is too short")
        for issue in web_math_errors(r.get("reason","")):e.append(f"{qid}: reason: {issue}")
    tiers=Counter(r.get("practice_tier") for r in x); expected=round(len(x)*0.60)
    if tiers["mandatory"]!=expected or tiers["revision"]!=len(x)-expected:e.append(f"tier split must be {expected} mandatory and {len(x)-expected} revision")
    out={"schema_version":"physics_mcq_difficulty_tier_v1.1","final_status":"passed" if not e else "failed","rows":len(x),"difficulty":dict(Counter(r.get("difficulty") for r in x)),"practice_tier":dict(tiers),"errors":e}
    text=json.dumps(out,indent=2)+"\n";
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(text)
    print(text,end="");return 0 if not e else 1
if __name__=="__main__":raise SystemExit(main())
