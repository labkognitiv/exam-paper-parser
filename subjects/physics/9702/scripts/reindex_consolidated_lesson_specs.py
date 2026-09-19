#!/usr/bin/env python3
"""Set active Physics lesson sequence/prerequisite fields after consolidation."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
for mp in ROOT.glob('study/topics/*/lesson-knowledge-map.json'):
    active=json.loads(mp.read_text())['lessons']; ids=[x['lesson_id'] for x in active]
    for i,lid in enumerate(ids,1):
        matches=list(mp.parent.glob(f'course-modules/*/lessons/{lid}/lesson.json'))
        if len(matches)!=1: raise SystemExit(f'{lid}: expected 1 spec, got {len(matches)}')
        p=matches[0]; d=json.loads(p.read_text())
        d['sequence']=i
        prereq=d.setdefault('prerequisites',{})
        prereq['previous_lesson_ids']=ids[:i-1]
        if 'immediate_previous_lesson_id' in prereq: prereq['immediate_previous_lesson_id']=ids[i-2] if i>1 else None
        if 'next_lesson_handoff' in d and isinstance(d['next_lesson_handoff'],dict): d['next_lesson_handoff']['next_lesson_id']=ids[i] if i<len(ids) else None
        tmp=p.with_suffix('.json.tmp'); tmp.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n'); tmp.replace(p)
print('Reindexed active lesson specifications')
