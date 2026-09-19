#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; STUDY=ROOT/'study'
d=json.loads((STUDY/'lesson-id-redirects.json').read_text()); a=d['aliases']; active=set()
for p in STUDY.glob('topics/*/lesson-knowledge-map.json'): active|={x['lesson_id'] for x in json.loads(p.read_text())['lessons']}
errors=[]
for old,new in a.items():
    if old in active: errors.append(f'retired active {old}')
    if new not in active: errors.append(f'inactive target {old}->{new}')
    if new in a: errors.append(f'chain {old}->{new}')
    if not list(STUDY.glob(f'topics/**/lessons/{old}/lesson-redirect.json')): errors.append(f'missing record {old}')
print(f'Active lessons: {len(active)}\nRedirects: {len(a)}\nErrors: {len(errors)}')
if errors: raise SystemExit('\n'.join(errors))
print('PASS')
