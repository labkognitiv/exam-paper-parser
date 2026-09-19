#!/usr/bin/env python3
"""Reversible 2026-09-10 Physics 9702 lesson consolidation.

Only local, coherent lessons in the same course module are combined.  The
canonical past-paper corpus is outcome-based and intentionally is not changed.
"""
from __future__ import annotations

import hashlib, json, re, shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = next(p for p in ROOT.parents if (p / "subjects").is_dir())
STUDY = ROOT / "study"
ARCHIVE = REPO / "archive" / "2026-09-10-physics-lesson-consolidation"
REDIRECTS = STUDY / "lesson-id-redirects.json"

# Merge only adjacent, tightly coupled teaching steps. Practical, definition,
# core and distinct calculation lessons remain active even when low-frequency.
ALIASES = {
 "9702_t01_cm02_l04":"9702_t01_cm02_l03", "9702_t01_cm05_l10":"9702_t01_cm05_l11",
 "9702_t02_cm02_l04":"9702_t02_cm02_l03", "9702_t02_cm03_l07":"9702_t02_cm03_l06", "9702_t02_cm03_l08":"9702_t02_cm03_l06", "9702_t02_cm04_l10":"9702_t02_cm04_l09", "9702_t02_cm05_l12":"9702_t02_cm05_l11", "9702_t02_cm06_l15":"9702_t02_cm06_l14",
 "9702_t04_cm03_l09":"9702_t04_cm03_l08", "9702_t04_cm04_l11":"9702_t04_cm04_l10",
 "9702_t06_cm04_l09":"9702_t06_cm04_l08",
 "9702_t07_cm02_l04":"9702_t07_cm02_l03", "9702_t07_cm03_l06":"9702_t07_cm03_l05", "9702_t07_cm04_l08":"9702_t07_cm04_l07", "9702_t07_cm05_l10":"9702_t07_cm05_l09", "9702_t07_cm06_l12":"9702_t07_cm06_l11", "9702_t07_cm07_l14":"9702_t07_cm07_l13",
 "9702_t08_cm02_l03":"9702_t08_cm02_l02", "9702_t08_cm04_l06":"9702_t08_cm04_l05", "9702_t08_cm05_l08":"9702_t08_cm05_l07", "9702_t08_cm07_l11":"9702_t08_cm07_l10",
 "9702_t09_cm01_l02":"9702_t09_cm01_l01", "9702_t09_cm02_l05":"9702_t09_cm02_l04",
 "9702_t10_cm03_l07":"9702_t10_cm03_l06",
 "9702_t11_cm01_l02":"9702_t11_cm01_l01", "9702_t11_cm02_l04":"9702_t11_cm02_l03",
 "9702_t12_cm01_l01":"9702_t12_cm01_l02", "9702_t14_cm02_l03":"9702_t14_cm02_l02", "9702_t15_cm02_l03":"9702_t15_cm02_l02", "9702_t17_cm03_l06":"9702_t17_cm03_l05", "9702_t18_cm01_l02":"9702_t18_cm01_l01", "9702_t19_cm01_l02":"9702_t19_cm01_l01",
 "9702_t20_cm02_l03":"9702_t20_cm02_l02", "9702_t20_cm04_l08":"9702_t20_cm04_l07", "9702_t20_cm05_l10":"9702_t20_cm05_l09", "9702_t21_cm01_l02":"9702_t21_cm01_l01", "9702_t21_cm02_l04":"9702_t21_cm02_l03",
 "9702_t22_cm01_l02":"9702_t22_cm01_l01", "9702_t22_cm02_l06":"9702_t22_cm02_l05", "9702_t22_cm04_l10":"9702_t22_cm04_l09",
 "9702_t23_cm01_l03":"9702_t23_cm01_l04", "9702_t24_cm01_l03":"9702_t24_cm01_l02", "9702_t24_cm02_l05":"9702_t24_cm02_l04", "9702_t24_cm03_l08":"9702_t24_cm03_l07",
 "9702_t25_cm01_l02":"9702_t25_cm01_l01", "9702_t25_cm02_l04":"9702_t25_cm02_l03", "9702_t25_cm03_l06":"9702_t25_cm03_l05",
}
RETAINED = ["9702_t06_cm03_l06", "9702_t12_cm02_l03", "9702_t18_cm02_l03", "9702_t22_cm03_l08", "9702_t23_cm02_l06", "9702_t24_cm03_l06"]

def atomic(path, value):
    text = json.dumps(value, indent=2, ensure_ascii=False) + "\n" if not isinstance(value, str) else value
    tmp = path.with_suffix(path.suffix + ".tmp"); tmp.write_text(text, encoding="utf-8"); tmp.replace(path)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def cm_of(lesson): return lesson["lesson_id"].rsplit("_l", 1)[0]

def render_docs():
    outcomes = {}
    for level in ("as", "a2"):
        p = next((ROOT / "knowledge/2025-2027" / level).glob("*learning-outcomes.json"))
        outcomes[level] = {x["outcome_id"]: x["outcome_text"] for x in json.loads(p.read_text())["outcomes"]}
    grouped = {"as": [], "a2": []}
    for topic in sorted(STUDY.glob("topics/*")):
        mp = topic / "lesson-knowledge-map.json"
        if not mp.exists(): continue
        data = json.loads(mp.read_text()); level = "as" if data["topic_id"] <= "9702_t11" else "a2"
        grouped[level].append((topic, data))
        lines=[f"# {data['topic_id']} Active Module and Lesson Structure", "", "Retired IDs resolve through `study/lesson-id-redirects.json`.", ""]
        for x in data["lessons"]: lines.append(f"- `{x['lesson_id']}` {x['title']} (outcomes: {', '.join(x['outcome_ids'])})")
        atomic(topic / "module-lesson-structure.md", "\n".join(lines)+"\n")
    for level,label in (("as","AS"),("a2","A2")):
        lessons=[x for _,m in grouped[level] for x in m["lessons"]]
        lines=[f"# Cambridge Physics 9702 {label}: Topic, Module and Lesson Mapping Reference","",f"Official outcomes: {len(outcomes[level])}; active lessons: {len(lessons)}.","Retired IDs resolve through `study/lesson-id-redirects.json`.",""]
        for _,m in grouped[level]:
            lines += [f"## `{m['topic_id']}`",""]
            for x in m['lessons']:
                lines += [f"### `{x['lesson_id']}`: {x['title']}",""]
                lines += [f"- `{oid}`: {outcomes[level][oid]}" for oid in x['outcome_ids']]
                lines.append("")
        atomic(STUDY / f"{label}-TOPIC-MODULE-LESSON-MAPPING.md", "\n".join(lines))
    lines=["# Physics 9702 Lesson Production Tracker","","Updated: 2026-09-10","","| Lesson | Specification |","| --- | :---: |"]
    for _,m in grouped['as']+grouped['a2']:
        for x in m['lessons']: lines.append(f"| `{x['lesson_id']}` | active |")
    lines += ["", "Retired IDs: `study/lesson-id-redirects.json`.", ""]
    atomic(STUDY / "LESSON-PRODUCTION-TRACKER.md", "\n".join(lines))

def main():
    if REDIRECTS.exists():
        if json.loads(REDIRECTS.read_text()).get("aliases") == ALIASES: print("Already migrated"); return
        raise SystemExit("existing redirect manifest differs")
    maps=sorted(STUDY.glob("topics/*/lesson-knowledge-map.json")); byid={}; paths={}
    for mp in maps:
        for x in json.loads(mp.read_text())["lessons"]: byid[x['lesson_id']]=x; paths[x['lesson_id']]=mp
    assert not (set(ALIASES)|set(ALIASES.values()))-set(byid)
    assert not set(ALIASES)&set(ALIASES.values())
    for old,new in ALIASES.items(): assert paths[old]==paths[new] and cm_of(byid[old])==cm_of(byid[new])
    # Archive every file whose text will be changed, plus affected maps/modules.
    candidates=[]
    for p in STUDY.rglob('*'):
        if p.is_file() and p.suffix in {'.json','.md','.js','.py'} and (p.name in {'lesson-knowledge-map.json','module.json'} or any(old in p.read_text(encoding='utf-8',errors='ignore') for old in ALIASES)): candidates.append(p)
    candidates += [STUDY/'AS-TOPIC-MODULE-LESSON-MAPPING.md', STUDY/'A2-TOPIC-MODULE-LESSON-MAPPING.md', STUDY/'LESSON-PRODUCTION-TRACKER.md', STUDY/'skills/author-lesson-markdown/references/source-index.json', REPO/'tracker/physics/physics-paper-verification-tracker.xlsx']
    ARCHIVE.mkdir(parents=True,exist_ok=True); manifest=[]
    for p in sorted(set(candidates)):
        if not p.exists(): continue
        dst=ARCHIVE/p.relative_to(REPO); dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,dst)
        manifest.append({'path':str(p.relative_to(REPO)),'sha256':sha(p),'bytes':p.stat().st_size})
    atomic(ARCHIVE/'manifest.json',{'date':str(date.today()),'purpose':'Physics 9702 lesson consolidation pre-change state','files':manifest})
    # Update all editable study consumers. Preserve old paths and add redirect records.
    for p in candidates:
        if not p.exists() or p.suffix not in {'.json','.md','.js','.py'} or p.name in {'lesson-knowledge-map.json','module.json','source-index.json'}: continue
        s=p.read_text(encoding='utf-8')
        for old,new in ALIASES.items(): s=s.replace(old,new)
        atomic(p,s)
    # Canonical map merge needs unioned outcomes/evidence, not simple replacement.
    for mp in maps:
        data=json.loads(mp.read_text()); original=json.loads((ARCHIVE/mp.relative_to(REPO)).read_text())
        old={x['lesson_id']:x for x in original['lessons']}; active=[]
        for x in original['lessons']:
            if x['lesson_id'] in ALIASES: continue
            active.append(dict(x))
        active_by={x['lesson_id']:x for x in active}
        for src,tgt in ALIASES.items():
            if src in old:
                target=active_by[tgt]; source=old[src]
                target['outcome_ids']=list(dict.fromkeys(target['outcome_ids']+source['outcome_ids']))
                target['evidence_ids']=sorted(set(target.get('evidence_ids',[])+source.get('evidence_ids',[])))
                target['title']=f"{target['title']} and {source['title']}"
        data['lessons']=active; atomic(mp,data)
    # Keep canonical module lesson lists active-only.
    for p in STUDY.rglob('module.json'):
        if not p.read_text(encoding='utf-8').strip():
            continue
        d=json.loads(p.read_text());
        if 'lesson_ids' in d: d['lesson_ids']=[x for x in d['lesson_ids'] if x not in ALIASES]
        atomic(p,d)
    # Source index is a reader-facing lesson-ID consumer: collapse retired
    # entries into the surviving record and retarget predecessor pointers.
    source_index=STUDY/'skills/author-lesson-markdown/references/source-index.json'
    if source_index.exists():
        d=json.loads(source_index.read_text())
        for topic in d.get('topics',{}).values():
            lessons=topic.get('lessons',{})
            for old,new in ALIASES.items():
                if old in lessons:
                    retired=lessons.pop(old)
                    if new in lessons and not lessons[new].get('content'):
                        lessons[new]['content']=retired.get('content')
            for x in lessons.values():
                if x.get('previous_lesson_id') in ALIASES: x['previous_lesson_id']=ALIASES[x['previous_lesson_id']]
                if x.get('mapping_record_id') in ALIASES: x['mapping_record_id']=ALIASES[x['mapping_record_id']]
        atomic(source_index,d)
    # Compatibility records remain at all former lesson folders.
    for old,new in ALIASES.items():
        matches=list(STUDY.glob(f'topics/**/lessons/{old}'))
        for folder in matches: atomic(folder/'lesson-redirect.json',{'deprecated_lesson_id':old,'redirect_to_lesson_id':new,'effective_date':'2026-09-10'})
    atomic(REDIRECTS,{'schema_version':'9702_lesson_id_redirects_v1','effective_date':'2026-09-10','compatibility_window':'indefinite until separately retired','aliases':ALIASES,'retained_sub_20_exceptions':RETAINED,'resolution_policy':'Resolve before lookup; aliases are unique and acyclic.'})
    render_docs()
    print(f'Migrated {len(ALIASES)} lessons')
if __name__ == '__main__': main()
