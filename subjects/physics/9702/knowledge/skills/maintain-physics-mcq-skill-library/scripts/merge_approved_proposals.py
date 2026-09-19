#!/usr/bin/env python3
import argparse,csv,hashlib,json,re
from pathlib import Path
REG=["skill_id","skill_name","skill_role","canonical_definition","first_topic_id","first_module_id","first_seen_paper","first_seen_question_id","status","library_version"]
CHANGE=["change_id","library_version","change_type","skill_id","skill_name","source_paper","source_question_id","notes"]
def read(p):
    with p.open(newline="",encoding="utf-8-sig") as f:return list(csv.DictReader(f))
def norm(s):return re.sub(r"[^a-z0-9]+","",s.casefold())
def write(p,h,rows):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("w",newline="",encoding="utf-8") as f:w=csv.DictWriter(f,fieldnames=h);w.writeheader();w.writerows(rows)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser();
    for n in ["library","change-log","proposals","output-library","output-change-log","output-manifest"]:p.add_argument("--"+n,type=Path,required=True)
    p.add_argument("--new-version",required=True);a=p.parse_args();rows=read(a.library);changes=read(a.change_log);known={norm(x["skill_name"]) for x in rows};approved=[x for x in read(a.proposals) if x["review_status"]=="approved"]
    for x in approved:
        if norm(x["proposed_skill_name"]) in known:raise SystemExit(f"duplicate proposed skill: {x['proposed_skill_name']}")
        sid=f"9702_mcq_skill_{len(rows)+1:03d}";known.add(norm(x["proposed_skill_name"]))
        rows.append(dict(zip(REG,[sid,x["proposed_skill_name"],x["proposed_role"],x["proposed_definition"],x["topic_id"],x["module_id"],x["source_paper"],x["source_question_id"],"approved",a.new_version])))
        changes.append(dict(zip(CHANGE,[f"chg_{len(changes)+1:04d}",a.new_version,"add",sid,x["proposed_skill_name"],x["source_paper"],x["source_question_id"],x["reason"]])))
    for x in rows:x["library_version"]=a.new_version
    write(a.output_library,REG,rows);write(a.output_change_log,CHANGE,changes)
    manifest={"schema_version":"physics_mcq_skill_library_manifest_v1","subject_code":"9702","component_profile":"P1_single_select_mcq","active_version":a.new_version,"registry_path":str(a.output_library),"registry_sha256":sha(a.output_library),"change_log_path":str(a.output_change_log),"change_log_sha256":sha(a.output_change_log),"skill_count":len(rows),"status":"active"}
    a.output_manifest.write_text(json.dumps(manifest,indent=2)+"\n");print(json.dumps({"status":"merged","added":len(approved),"skill_count":len(rows),"version":a.new_version},indent=2));return 0
if __name__=="__main__":raise SystemExit(main())

