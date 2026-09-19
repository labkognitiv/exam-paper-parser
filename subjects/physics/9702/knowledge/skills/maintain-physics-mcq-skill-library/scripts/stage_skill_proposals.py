#!/usr/bin/env python3
import argparse,csv,json,re
from pathlib import Path
HEADER=["proposed_skill_name","proposed_role","topic_id","module_id","proposed_definition","source_paper","source_question_id","reason","review_status"]
def read(p):
    with p.open(newline="",encoding="utf-8-sig") as f:return list(csv.DictReader(f))
def norm(s):return re.sub(r"[^a-z0-9]+","",s.casefold())
def main():
    p=argparse.ArgumentParser();p.add_argument("--library",type=Path,required=True);p.add_argument("--assignments",type=Path,required=True);p.add_argument("--mapping",type=Path,required=True);p.add_argument("--output",type=Path,required=True);a=p.parse_args()
    known={norm(x["skill_name"]) for x in read(a.library) if x["status"]=="approved"};mapping={x["question_id"]:x for x in read(a.mapping)};out=[];seen=set()
    for row in read(a.assignments):
        tags=json.loads(row["skill_tags"]);rub=json.loads(row["ai_rubric"]);m=mapping[row["question_id"]]
        for i,name in enumerate(tags):
            n=norm(name)
            if n in known or n in seen:continue
            seen.add(n);out.append([name,"primary" if i==0 else "supporting",m["topic_id"],m["module_id"],rub[name],m["paper_code"],row["question_id"],"No approved canonical skill matched this assessed action.","pending"])
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open("w",newline="",encoding="utf-8") as f:w=csv.writer(f);w.writerow(HEADER);w.writerows(out)
    print(json.dumps({"status":"staged","proposals":len(out),"output":str(a.output)},indent=2));return 0
if __name__=="__main__":raise SystemExit(main())

