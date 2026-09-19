#!/usr/bin/env python3
import argparse,csv,hashlib,json,re
from pathlib import Path
HEADER=["skill_id","skill_name","skill_role","canonical_definition","first_topic_id","first_module_id","first_seen_paper","first_seen_question_id","status","library_version"]
CHANGE_HEADER=["change_id","library_version","change_type","skill_id","skill_name","source_paper","source_question_id","notes"]
def read(p):
    with p.open(newline="",encoding="utf-8-sig") as f:r=csv.DictReader(f);return list(r.fieldnames or []),list(r)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub(r"[^a-z0-9]+","",s.casefold())
def main():
    p=argparse.ArgumentParser();p.add_argument("--library",type=Path,required=True);p.add_argument("--taxonomy",type=Path,required=True);p.add_argument("--change-log",type=Path,required=True);p.add_argument("--manifest",type=Path,required=True);p.add_argument("--output",type=Path);a=p.parse_args();e=[]
    h,rows=read(a.library);th,tax=read(a.taxonomy);ch,changes=read(a.change_log);m=json.loads(a.manifest.read_text())
    if h!=HEADER:e.append("registry header does not match contract")
    if ch!=CHANGE_HEADER:e.append("change-log header does not match contract")
    ids=[];names=[];pairs={(x["topic_id"],x["module_id"]) for x in tax}
    for i,x in enumerate(rows,1):
        sid=x.get("skill_id","");ids.append(sid);names.append(norm(x.get("skill_name","")))
        if sid!=f"9702_mcq_skill_{i:03d}":e.append(f"row {i}: skill_id sequence mismatch")
        if x.get("skill_role") not in {"primary","supporting","both"}:e.append(f"{sid}: invalid role")
        if len(x.get("skill_name","").strip())<5 or "_" in x.get("skill_name",""):e.append(f"{sid}: skill_name is not human-readable")
        if len(x.get("canonical_definition","").strip())<35:e.append(f"{sid}: canonical definition too short")
        if (x.get("first_topic_id"),x.get("first_module_id")) not in pairs:e.append(f"{sid}: invalid first topic/module pair")
        if x.get("status") not in {"approved","deprecated"}:e.append(f"{sid}: invalid status")
        if x.get("library_version")!=m.get("active_version"):e.append(f"{sid}: library_version differs from manifest")
    if len(names)!=len(set(names)):e.append("normalised duplicate skill names")
    if m.get("skill_count")!=len(rows):e.append("manifest skill_count mismatch")
    if m.get("registry_sha256")!=sha(a.library):e.append("manifest registry hash mismatch")
    if m.get("change_log_sha256")!=sha(a.change_log):e.append("manifest change-log hash mismatch")
    if m.get("status")!="active":e.append("manifest status is not active")
    out={"schema_version":"physics_mcq_skill_library_validation_v1","final_status":"passed" if not e else "failed","active_version":m.get("active_version"),"skill_count":len(rows),"approved":sum(x.get("status")=="approved" for x in rows),"deprecated":sum(x.get("status")=="deprecated" for x in rows),"change_rows":len(changes),"errors":e}
    text=json.dumps(out,indent=2)+"\n";
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(text)
    print(text,end="");return 0 if not e else 1
if __name__=="__main__":raise SystemExit(main())

