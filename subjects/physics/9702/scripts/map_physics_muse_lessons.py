#!/usr/bin/env python3
"""Derived Muse Spark mapping for Physics 9702 structured papers.

This intentionally reads only canonical packages and writes only reviews/. It
is resumable at a question file boundary and resolves legacy lesson aliases
before accepting a model answer.
"""
from __future__ import annotations
import argparse, concurrent.futures, hashlib, json, os, random, re, subprocess, tempfile, time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT=Path(__file__).resolve().parents[1]
MODEL="meta/muse-spark-1.3-contributor"
TYPES={"direct","contextual_skill","legacy_content"}
LEGACY_FALLBACK={
    # 2016-19 electric-field content is absent from the current syllabus. The
    # model correctly identifies that gap but must still receive an explicit
    # pedagogical retrieval home, never a fabricated direct lesson.
    ("9702_s16_22",("9702_s16_22_q06_a","9702_s16_22_q06_b")):[
        ("9702_s16_22_q06_a","9702_t03","9702_t03_m01","9702_t03_cm01_l03","legacy electric-field-line representation; closest current force concept"),
        ("9702_s16_22_q06_b","9702_t05","9702_t05_m01","9702_t05_cm01_l01","legacy electric-field-strength calculation; closest current work-and-energy concept"),],
    ("9702_s19_22",("9702_s19_22_q06_a","9702_s19_22_q06_b")):[
        ("9702_s19_22_q06_a","9702_t03","9702_t03_m01","9702_t03_cm01_l03","legacy electric-field-line definition; closest current force concept"),
        ("9702_s19_22_q06_b","9702_t03","9702_t03_m01","9702_t03_cm01_l03","legacy field-line-density interpretation; closest current force concept"),],
}

def atomic(p, x):
    p.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(dir=p.parent,prefix=p.name+".",suffix=".tmp")
    try:
        with os.fdopen(fd,"w",encoding="utf8") as f: json.dump(x,f,indent=2,ensure_ascii=False);f.write("\n")
        os.replace(tmp,p)
    except Exception:
        try: os.unlink(tmp)
        except FileNotFoundError: pass
        raise
def load(p): return json.loads(p.read_text(encoding="utf8"))
def api_key(): return subprocess.check_output(["security","find-generic-password","-s","kognitiv-openrouter-api-key","-w"],text=True).strip()
def clean_json(s):
    s=re.sub(r"^```(?:json)?\s*|\s*```$","",s.strip()); return json.loads(s)

def curriculum(level):
    """Canonical lesson JSON is authoritative; redirects are compatibility only."""
    aliases=load(ROOT/"study/lesson-id-redirects.json").get("aliases",{})
    active={}; full=[]
    for p in sorted((ROOT/"study/topics").glob("**/lessons/*/lesson.json")):
        d=load(p)
        if d.get("level"," ").lower()!=level: continue
        lid=d["lesson_id"]; topic=d["topic_id"]
        for mod in d.get("cambridge_module_ids",[]): active[(topic,mod,lid)]=d
        full.append({"topic_id":topic,"module_ids":d.get("cambridge_module_ids",[]),"lesson_id":lid,"title":d.get("title"),"learning_goals":d.get("learning_goals",[]),"new_learning":d.get("new_learning",[]),"outcome_ids":d.get("knowledge_mapping",{}).get("outcome_ids",[])})
    if not active: raise RuntimeError("no active lesson JSON")
    return active,aliases,full
def normalize(obj, active, aliases):
    if not isinstance(obj,dict): return None
    lid=aliases.get(obj.get("lesson_id"),obj.get("lesson_id")); tup=(obj.get("topic_id"),obj.get("module_id"),lid)
    return {"topic_id":tup[0],"module_id":tup[1],"lesson_id":tup[2]} if tup in active else None
def qtext(q):
    out=[q.get("question_stem") or ""]
    for p in q.get("parts",[]): out.append("\n".join(str(x) for x in [p.get("id"),p.get("label"),p.get("part_stem"),p.get("text"),p.get("answer_prompt"),p.get("unit")] if x))
    return "\n\n".join(out)
def preferred(q,names):
    for n in names:
        p=q/n
        if p.exists():
            try:return load(p),n
            except json.JSONDecodeError: pass
    raise ValueError("missing "+"/".join(names))
def inventory(component):
    ans=[]
    for paper in sorted((ROOT/"past papers"/component).glob("*/*/variant-*")):
        qs=[]
        for qd in sorted(paper.glob("question_*")):
            try:
                ms,msrc=preferred(qd,["markscheme_reviewed.json","markscheme.json"])
                q,qsrc=preferred(qd,["question_ocr_review_2.json","question_ocr.json"])
                # Derived target identity is one unique positive-mark mark-scheme ID.
                seen=set(); positive=[]; zero=[]; duplicate=[]
                for p in ms.get("parts",[]):
                    pid=p.get("id"); marks=int(p.get("marks") or 0)
                    if not pid: continue
                    if pid in seen:
                        duplicate.append(pid); continue
                    seen.add(pid)
                    (positive if marks>0 else zero).append(pid)
                qs.append({"dir":qd,"question":q,"marks":ms,"positive":positive,"zero":zero,"duplicates":duplicate,"qsource":qsrc,"msource":msrc})
            except Exception as e: qs.append({"dir":qd,"error":str(e)})
        if qs:
            code=next((x["marks"].get("paper_code") for x in qs if "marks" in x),paper.name)
            ans.append({"paper_id":code,"path":paper,"questions":qs})
    return ans
def validate(data,pid,expected,active,aliases,require_type=False):
    if not isinstance(data,dict) or data.get("paper_id")!=pid or not isinstance(data.get("mappings"),list): return "schema_or_paper"
    got=[x.get("part_id") for x in data["mappings"] if isinstance(x,dict)]
    if len(got)!=len(set(got)) or set(got)!=set(expected): return "part_ids"
    for x in data["mappings"]:
        # Normalise explicit confidence scores/phrases into the controlled
        # three-value schema. A genuinely null first-pass home is necessarily
        # low-confidence and is deliberately sent to contextual resolution.
        c=x.get("confidence")
        if isinstance(c,(int,float)): x["confidence"]="high" if c>=.8 else "medium" if c>=.5 else "low"
        elif isinstance(c,str) and c.lower() not in {"high","medium","low"}:
            c=c.lower(); x["confidence"]="high" if "high" in c else "medium" if "med" in c else "low" if "low" in c else None
        if x.get("confidence") not in {"high","medium","low"}: return "confidence"
        pri=x.get("primary"); n=normalize(pri,active,aliases)
        if n is None:
            if pri and any(pri.get(k) is not None for k in ("topic_id","module_id","lesson_id")): return "primary_curriculum"
            if require_type:return "null_primary"
            x["confidence"]="low"
        else:x["primary"]=n
        if not isinstance(x.get("secondary",[]),list):return "secondary"
        secs=[]
        for s in x.get("secondary",[]):
            n=normalize(s,active,aliases)
            if not n:return "secondary_curriculum"
            if n!=x.get("primary") and n not in secs:secs.append(n)
        x["secondary"]=secs
        if require_type and x.get("mapping_type") not in TYPES:return "mapping_type"
    return None
def call(prompt, system, pid, expected, active, aliases, require_type, dry, key):
    if dry:return {"status":"DRY_RUN","prompt_chars":len(prompt),"prompt_tokens":0,"completion_tokens":0,"cost_usd":0}
    fallback=LEGACY_FALLBACK.get((pid,tuple(expected))) if require_type else None
    if fallback:
        data={"paper_id":pid,"mappings":[{"part_id":part,"primary":{"topic_id":topic,"module_id":module,"lesson_id":lesson},"secondary":[],"confidence":"low","mapping_type":"legacy_content","reason":reason} for part,topic,module,lesson,reason in fallback]}
        if not validate(data,pid,expected,active,aliases,True): return {"status":"VALID","data":data,"attempt":0,"elapsed_sec":0,"prompt_tokens":0,"completion_tokens":0,"cost_usd":0,"fallback":"controlled_legacy_gap"}
    payload={"model":MODEL,"messages":[{"role":"system","content":system},{"role":"user","content":prompt}],"temperature":0,"reasoning":{"effort":"low"},"max_tokens":3500}
    start=time.monotonic();pt=ct=0;cost=0.;err=None
    for attempt in range(5):
        try:
            req=Request("https://openrouter.ai/api/v1/chat/completions",data=json.dumps(payload).encode(),headers={"Authorization":"Bearer "+key,"Content-Type":"application/json","HTTP-Referer":"https://kognitiv.edu","X-Title":"Kognitiv Physics lesson mapper"},method="POST")
            with urlopen(req,timeout=180) as r:raw=json.loads(r.read().decode())
            u=raw.get("usage",{});pt+=int(u.get("prompt_tokens") or 0);ct+=int(u.get("completion_tokens") or 0);cost+=float(u.get("cost") or u.get("cost_usd") or 0)
            data=clean_json(raw["choices"][0]["message"].get("content","") or "")
            issue=validate(data,pid,expected,active,aliases,require_type)
            if not issue:return {"status":"VALID","data":data,"attempt":attempt+1,"elapsed_sec":round(time.monotonic()-start,3),"prompt_tokens":pt,"completion_tokens":ct,"cost_usd":cost}
            err="model validation: "+issue
        except HTTPError as e:
            err="HTTP "+str(e.code)
            # OpenRouter can briefly return 402 while the shared account
            # refreshes. Treat it as bounded retryable infrastructure state;
            # the five-attempt cap and exponential backoff still prevent a
            # runaway spend/retry loop.
            if e.code not in {402,429} and not 500<=e.code<600:break
        except (URLError,TimeoutError,json.JSONDecodeError,KeyError) as e:err=type(e).__name__+": "+str(e)
        if attempt<4:time.sleep(min(30,2**attempt)+random.random())
    if fallback:
        data={"paper_id":pid,"mappings":[{"part_id":part,"primary":{"topic_id":topic,"module_id":module,"lesson_id":lesson},"secondary":[],"confidence":"low","mapping_type":"legacy_content","reason":reason} for part,topic,module,lesson,reason in fallback]}
        if not validate(data,pid,expected,active,aliases,True):
            return {"status":"VALID","data":data,"attempt":attempt+1,"elapsed_sec":round(time.monotonic()-start,3),"prompt_tokens":pt,"completion_tokens":ct,"cost_usd":cost,"fallback":"controlled_legacy_gap"}
    return {"status":"FAILED","error":err,"attempt":attempt+1,"elapsed_sec":round(time.monotonic()-start,3),"prompt_tokens":pt,"completion_tokens":ct,"cost_usd":cost}
def reference(full):return json.dumps(full,ensure_ascii=False,separators=(",",":"))
def mappings_prompt(item,pid,expected,ref):
    return "CONTROLLED PHYSICS 9702 LESSON JSON REFERENCE:\n"+ref+"\n\nMAP EACH POSITIVE-MARK PART EXACTLY ONCE. paper_id="+pid+" expected="+json.dumps(expected)+"\n\nWHOLE QUESTION:\n"+qtext(item["question"])+"\n\nREVIEWED/CANONICAL MARK SCHEME:\n"+json.dumps(item["marks"],ensure_ascii=False)+"\nReturn JSON {paper_id,mappings:[{part_id,primary:{topic_id,module_id,lesson_id},secondary:[],confidence,reason}]}. Use only IDs supplied. primary module_id is a Cambridge module ID, not course module ID. Null primary only when no direct current lesson covers the awarded knowledge."
def phase(component,level,phase,args):
    active,aliases,full=curriculum(level); papers=inventory(component); base=ROOT/"reviews"/f"{component}-{level}-mapping-{phase}"
    if phase=="candidates":
        ref=reference(full); system="Map Cambridge Physics 9702 marked question parts to supplied controlled lessons. Return JSON only. Never invent IDs; mark only awarded knowledge."
        jobs=[]
        for p in papers:
            for i in p["questions"]:
                if "error" not in i:jobs.append((p,i,i["positive"],mappings_prompt(i,p["paper_id"],i["positive"],ref),False))
    else:
        cand=ROOT/"reviews"/f"{component}-{level}-mapping-candidates"; jobs=[]; ref=reference(full)
        second_dir=ROOT/"reviews"/f"{component}-{level}-mapping-second-pass"
        for p in papers:
            cp=cand/p["paper_id"]/'candidate.json'
            if not cp.exists():continue
            old={x.get("part_id"):x for x in load(cp).get("mappings",[])}
            for i in p["questions"]:
                if "error" in i:continue
                # Contextual resolution follows the review result, not a stale
                # first-pass null. This avoids paying twice for a review that
                # has already supplied an active pedagogical home.
                if phase=="contextual-resolution":
                    sp=second_dir/p["paper_id"]/((i["marks"].get("question_id") or i["question"].get("question_id"))+".json")
                    if sp.exists():
                        sd=load(sp)
                        if sd.get("status")=="VALID": old.update({x["part_id"]:x for x in sd.get("data",{}).get("mappings",[])})
                targets=[x for x in i["positive"] if (old.get(x,{}).get("confidence")=="low" if phase=="second-pass" else (old.get(x,{}).get("primary") or {}).get("lesson_id") is None)]
                if not targets:continue
                first=[old[x] for x in i["positive"] if x in old]
                if phase=="second-pass":
                    prompt="Review only low-confidence part IDs "+json.dumps(targets)+". Whole question:\n"+qtext(i["question"])+"\nMARK SCHEME:\n"+json.dumps(i["marks"],ensure_ascii=False)+"\nFIRST PASS FOR THIS QUESTION:\n"+json.dumps(first,ensure_ascii=False)+"\nLESSON REFERENCE:\n"+ref+"\nReturn {paper_id,mappings:[{part_id,primary:{topic_id,module_id,lesson_id},secondary:[],confidence,reason}]} JSON only."
                else:
                    plausible={((x.get("primary") or {}).get("topic_id")) for x in first if (x.get("primary") or {}).get("topic_id")}
                    scoped_ref=reference([x for x in full if x["topic_id"] in plausible]) if plausible else ref
                    prompt="FINAL RESOLUTION: every requested marked part MUST receive one non-null active primary lesson. Resolve using the whole question, neighbouring mappings and mark scheme. Use direct only where the current lesson explicitly teaches the awarded knowledge; otherwise use contextual_skill for a transferable skill under the question's active home, or legacy_content for absent older-syllabus content and choose its closest active pedagogical home.\nResolve these marked null part IDs "+json.dumps(targets)+".\nWHOLE QUESTION:\n"+qtext(i["question"])+"\nMARK SCHEME:\n"+json.dumps(i["marks"],ensure_ascii=False)+"\nCURRENT MAPPINGS:\n"+json.dumps(first,ensure_ascii=False)+"\nACTIVE LESSON REFERENCE (redirects already resolved):\n"+scoped_ref+"\nReturn {paper_id,mappings:[{part_id,primary:{topic_id,module_id,lesson_id},secondary:[],confidence,mapping_type,reason}]} JSON only. primary must never be null. mapping_type is direct, contextual_skill, or legacy_content."
                jobs.append((p,i,targets,prompt,phase=="contextual-resolution"))
        system=("You are the final Cambridge Physics 9702 retrieval resolver. Return only valid JSON and never invent IDs. Every requested marked part MUST have an active non-null primary lesson. If direct coverage is absent, select the closest active pedagogical home and label contextual_skill or legacy_content honestly; null is forbidden." if phase=="contextual-resolution" else "Return only valid JSON for controlled Cambridge Physics 9702 lesson mapping. Never invent IDs.")
    start=time.monotonic();records=[]
    def dest(p,i):return base/p["paper_id"]/((i["marks"].get("question_id") or i["question"].get("question_id"))+".json")
    pending=[]
    for j in jobs:
        d=dest(j[0],j[1])
        try:
            x=load(d); ok=x.get("status")=="VALID" and not validate(x["data"],j[0]["paper_id"],j[2],active,aliases,j[4])
        except Exception:ok=False
        if not ok:pending.append(j)
    key="" if args.dry_run else api_key()
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(args.workers, max(1,len(pending)))) as ex:
        fs={ex.submit(call,j[3],system,j[0]["paper_id"],j[2],active,aliases,j[4],args.dry_run,key):j for j in pending}
        for n,f in enumerate(concurrent.futures.as_completed(fs),1):
            j=fs[f]
            try:r=f.result()
            except Exception as e:r={"status":"FAILED","error":repr(e),"prompt_tokens":0,"completion_tokens":0,"cost_usd":0}
            r.update({"paper_id":j[0]["paper_id"],"question_id":j[1]["marks"].get("question_id"),"part_ids":j[2]});atomic(dest(j[0],j[1]),r);print(f"{phase} {n}/{len(pending)} {r['paper_id']} {r['question_id']} {r['status']}",flush=True)
    # durable reports include resumed records
    for j in jobs:
        p=dest(j[0],j[1])
        if p.exists():records.append(load(p))
    # A paper-level durable candidate is the stage contract consumed by later
    # stages. It is rebuilt from independently durable question responses.
    if phase=="candidates":
        by_question={(r.get("paper_id"),r.get("question_id")):r for r in records}
        for p in papers:
            expected=[]; mapped=[]
            for i in p["questions"]:
                if "error" in i: continue
                expected += i["positive"]
                r=by_question.get((p["paper_id"],i["marks"].get("question_id")))
                if r and r.get("status")=="VALID": mapped += r["data"]["mappings"]
            issue=validate({"paper_id":p["paper_id"],"mappings":mapped},p["paper_id"],expected,active,aliases)
            atomic(base/p["paper_id"]/'candidate.json',{"paper_id":p["paper_id"],"mappings":mapped,"candidate_status":"COMPLETE" if not issue else "INCOMPLETE","zero_mark_stems_excluded":sum(len(i.get("zero",[])) for i in p["questions"]),"duplicate_mark_scheme_part_records_normalized":sum(len(i.get("duplicates",[])) for i in p["questions"])})
    # contextual stage materializes complete per-paper resolved candidates.
    paper_status=[]
    if phase=="contextual-resolution":
        second=ROOT/"reviews"/f"{component}-{level}-mapping-second-pass"; cand=ROOT/"reviews"/f"{component}-{level}-mapping-candidates"
        overrides={x["part_id"]:x for r in records if r.get("status")=="VALID" for x in r["data"]["mappings"]}
        second_over={x["part_id"]:x for p in second.glob("*/*.json") if p.name!="manifest.json" for x in (load(p).get("data",{}).get("mappings",[]) if load(p).get("status")=="VALID" else [])}
        for p in papers:
            first={x["part_id"]:x for x in load(cand/p["paper_id"]/'candidate.json').get("mappings",[])}; combined=[]; expected=[]
            for i in p["questions"]:
                if "error" in i:continue
                expected+=i["positive"]
                for pid in i["positive"]:
                    x=dict(overrides.get(pid) or second_over.get(pid) or first.get(pid) or {}); x.setdefault("mapping_type","direct");combined.append(x)
            issue=validate({"paper_id":p["paper_id"],"mappings":combined},p["paper_id"],expected,active,aliases,True)
            atomic(base/p["paper_id"]/'resolved_candidate.json',{"paper_id":p["paper_id"],"mappings":combined,"candidate_status":"RESOLVED" if not issue else "INCOMPLETE","zero_mark_stems_excluded":sum(len(i.get("zero",[])) for i in p["questions"]),"duplicate_mark_scheme_part_records_normalized":sum(len(i.get("duplicates",[])) for i in p["questions"])})
            paper_status.append({"paper_id":p["paper_id"],"status":"VALID" if not issue else issue,"marked_parts":len(expected)})
    totals={"papers":len(papers),"questions":sum(len([i for i in p["questions"] if "error" not in i]) for p in papers),"unique_positive_mark_parts":sum(len(i.get("positive",[])) for p in papers for i in p["questions"]),"excluded_zero_mark_stems":sum(len(i.get("zero",[])) for p in papers for i in p["questions"]),"duplicate_part_records_normalized":sum(len(i.get("duplicates",[])) for p in papers for i in p["questions"]),"jobs":len(jobs),"valid_jobs":sum(r.get("status")=="VALID" for r in records),"failed_jobs":sum(r.get("status")!="VALID" for r in records),"low_confidence_parts":sum(x.get("confidence")=="low" for r in records if r.get("status")=="VALID" for x in r.get("data",{}).get("mappings",[])),"mapping_types":Counter(x.get("mapping_type","direct") for p in (paper_status and [load(base/x["paper_id"]/'resolved_candidate.json') for x in paper_status] or []) for x in p.get("mappings",[])),"prompt_tokens":sum(int(r.get("prompt_tokens") or 0) for r in records),"completion_tokens":sum(int(r.get("completion_tokens") or 0) for r in records),"cost_usd":sum(float(r.get("cost_usd") or 0) for r in records),"elapsed_sec":round(time.monotonic()-start,3)}
    totals["mapping_types"]=dict(totals["mapping_types"])
    manifest={"schema_version":f"9702_{component}_{level}_{phase}_v1","model":MODEL,"run_finished":datetime.now(timezone.utc).isoformat(),"lesson_json_reference_sha256":hashlib.sha256(ref.encode()).hexdigest(),"totals":totals,"papers":paper_status,"records":[{k:r.get(k) for k in ("paper_id","question_id","part_ids","status","error","prompt_tokens","completion_tokens","cost_usd")} for r in records]}
    atomic(base/'manifest.json',manifest);print(json.dumps(totals,indent=2))
    if phase=="contextual-resolution" and any(x["status"]!="VALID" for x in paper_status):raise SystemExit(1)
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--component",choices=("p2","p4"),required=True);ap.add_argument("--level",choices=("as","a2"),required=True);ap.add_argument("--phase",choices=("candidates","second-pass","contextual-resolution"),required=True);ap.add_argument("--workers",type=int,default=16);ap.add_argument("--dry-run",action="store_true");a=ap.parse_args();phase(a.component,a.level,a.phase,a)
if __name__=="__main__":main()
