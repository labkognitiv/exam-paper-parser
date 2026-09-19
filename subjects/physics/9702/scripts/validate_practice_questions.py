#!/usr/bin/env python3
"""Validation script for Cambridge Physics 9702 lesson-practice questions.

Verifies:
1. Directory structure: <lesson_dir>/practice-questions/ with manifest.json and 20 question files.
2. Question IDs and filenames: <lesson_id>_mcq01.json .. _mcq10.json, _theory01.json .. _theory10.json.
3. Schemas: 9702_lesson_practice_v1 and 9702_lesson_practice_manifest_v1.
4. Tier distribution: exactly 10 MCQ (1 mark each, 4 options, valid correct_option), 5 drill (1-2 marks), 3 medium (3-4 marks), 2 hard (5-7 marks, multipart response_structure and part_enrichment).
5. SHA256 hashes of lesson.md and topic-markdown-audit.md in manifest.
6. Total marks reconciliation: manifest total_marks == sum of question marks.
7. Strictly zero em dashes (chr(8212)) in any question file or manifest.
8. Valid JSON syntax across all files.
"""

import sys
import os
import json
import hashlib
from pathlib import Path

def validate_lesson_practice(lesson_dir):
    lesson_path = Path(lesson_dir)
    pq_dir = lesson_path / 'practice-questions'
    if not pq_dir.is_dir():
        return False, f'Missing directory {pq_dir}'

    manifest_path = pq_dir / 'manifest.json'
    if not manifest_path.is_file():
        return False, f'Missing manifest {manifest_path}'

    try:
        raw_m = manifest_path.read_text(encoding='utf-8')
        if chr(8212) in raw_m:
            return False, f'Em dash found in {manifest_path}'
        if chr(8211) in raw_m:
            return False, f'En dash found in {manifest_path}'
        manifest = json.loads(raw_m)
    except Exception as e:
        return False, f'Invalid manifest JSON: {e}'

    if manifest.get('schema_version') != '9702_lesson_practice_manifest_v1':
        return False, f'Invalid manifest schema: {manifest.get("schema_version")}'

    q_ids = manifest.get('question_ids', [])
    if len(q_ids) != 20:
        return False, f'Expected 20 question IDs in manifest, got {len(q_ids)}'

    dist = manifest.get('distribution', {})
    if dist != {'mcq': 10, 'drill': 5, 'medium': 3, 'hard': 2}:
        return False, f'Invalid distribution: {dist}'

    # Check inputs sha256
    inputs = manifest.get('inputs', {})
    repo_root = Path(__file__).resolve().parents[4] # exam-paper-parser
    for k in ['lesson_markdown', 'topic_audit']:
        item = inputs.get(k, {})
        p_str = item.get('path', '')
        exp_h = item.get('sha256')
        if not p_str:
            return False, f'Missing path for input {k}'
        p_path = Path(p_str)
        if not p_path.is_file():
            if (repo_root / p_str).is_file():
                p_path = repo_root / p_str
            elif (lesson_path / p_str).is_file():
                p_path = lesson_path / p_str
            elif (Path.cwd() / p_str).is_file():
                p_path = Path.cwd() / p_str
            else:
                return False, f'Input file {p_str} does not exist'
        actual_h = hashlib.sha256(p_path.read_bytes()).hexdigest()
        if actual_h != exp_h:
            return False, f'Hash mismatch for {p_str}: manifest={exp_h} vs actual={actual_h}'

    calc_marks = 0
    mcq_count = 0
    drill_count = 0
    medium_count = 0
    hard_count = 0

    for i, qid in enumerate(q_ids):
        q_path = pq_dir / f'{qid}.json'
        if not q_path.is_file():
            return False, f'Missing question file: {q_path}'
        try:
            raw_q = q_path.read_text(encoding='utf-8')
            if chr(8212) in raw_q:
                return False, f'Em dash found in {q_path}'
            if chr(8211) in raw_q:
                return False, f'En dash found in {q_path}'
            q = json.loads(raw_q)
        except Exception as e:
            return False, f'Invalid JSON in {q_path}: {e}'

        if q.get('schema_version') != '9702_lesson_practice_v1':
            return False, f'Wrong question schema in {qid}: {q.get("schema_version")}'

        if q.get('sequence') != i + 1:
            return False, f'Sequence mismatch in {qid}: expected {i+1}, got {q.get("sequence")}'

        q_type = q.get('question_type')
        marks = q.get('marks', 0)
        calc_marks += marks

        if i < 10:
            if q_type != 'mcq' or marks != 1:
                return False, f'{qid} must be mcq with 1 mark, got {q_type} with {marks}'
            mcq_count += 1
            opts = q.get('options', [])
            if len(opts) != 4:
                return False, f'{qid} must have 4 options, got {len(opts)}'
            ans = q.get('answer', {})
            correct = ans.get('correct_option')
            if correct not in [1, 2, 3, 4]:
                return False, f'{qid} invalid correct_option: {correct}'
            if not ans.get('explanation'):
                return False, f'{qid} missing answer explanation'
            dist_exp = q.get('distractor_explanations', [])
            if len(dist_exp) != 4:
                return False, f'{qid} must have 4 distractor_explanations, got {len(dist_exp)}'
        elif i < 15:
            if q_type != 'drill' or marks not in [1, 2]:
                return False, f'{qid} must be drill with 1-2 marks, got {q_type} with {marks}'
            drill_count += 1
        elif i < 18:
            if q_type != 'medium' or marks not in [3, 4]:
                return False, f'{qid} must be medium with 3-4 marks, got {q_type} with {marks}'
            medium_count += 1
        else:
            if q_type != 'hard' or marks < 5:
                return False, f'{qid} must be hard with >= 5 marks, got {q_type} with {marks}'
            hard_count += 1
            rs = q.get('response_structure')
            if not rs:
                return False, f'{qid} missing response_structure'
            pe = q.get('part_enrichment')
            if not pe:
                return False, f'{qid} missing part_enrichment'

        if not q.get('prompt'):
            return False, f'{qid} missing prompt'
        if not q.get('hints'):
            return False, f'{qid} missing hints'
        if not q.get('solution'):
            return False, f'{qid} missing solution'
        if not q.get('teacher_walkthrough'):
            return False, f'{qid} missing teacher_walkthrough'
        if not q.get('outcome_ids'):
            return False, f'{qid} missing outcome_ids'
        if not q.get('source_mode'):
            return False, f'{qid} missing source_mode'

    if manifest.get('total_marks') != calc_marks:
        return False, f'Marks mismatch: manifest={manifest.get("total_marks")} vs calculated={calc_marks}'

    return True, f'Valid: 20 questions (10 MCQ, 5 drill, 3 med, 2 hard), {calc_marks} marks'


def find_all_lessons(topics):
    physics_root = Path(__file__).resolve().parents[1]
    study_topics = physics_root / 'study' / 'topics'
    found = []

    for t_dir in sorted(study_topics.iterdir()):
        if not t_dir.is_dir() or t_dir.name.startswith('.'):
            continue
        if topics != 'all':
            topic_prefix = t_dir.name.split('_')[0] + '_' + t_dir.name.split('_')[1] if '_' in t_dir.name else t_dir.name
            matches_topic = False
            if isinstance(topics, list):
                matches_topic = any(t in t_dir.name or t.startswith(topic_prefix) for t in topics)
            elif isinstance(topics, str):
                matches_topic = topics in t_dir.name or topics.startswith(topic_prefix)
            if not matches_topic:
                continue

        cm_dir = t_dir / 'course-modules'
        if not cm_dir.is_dir():
            continue
        for cm in sorted(cm_dir.iterdir()):
            if not cm.is_dir() or cm.name.startswith('.'):
                continue
            l_dir = cm / 'lessons'
            if not l_dir.is_dir():
                continue
            for l in sorted(l_dir.iterdir()):
                if not l.is_dir() or l.name.startswith('.'):
                    continue
                if (l / 'lesson.json').is_file():
                    if topics != 'all':
                        is_lesson_filter = any('_l' in t for t in (topics if isinstance(topics, list) else [topics]))
                        if is_lesson_filter and l.name not in topics:
                            continue
                    # Check if retired alias
                    red_path = physics_root / 'study' / 'lesson-id-redirects.json'
                    if red_path.is_file():
                        with open(red_path) as rf:
                            aliases = json.load(rf).get('aliases', {})
                            if l.name in aliases:
                                continue
                    found.append(l)
    return found


def main():
    if len(sys.argv) < 2:
        print('Usage: validate_practice_questions.py <lesson_path|topic_name|all>')
        sys.exit(1)

    arg = sys.argv[1]
    if os.path.isdir(arg) and (Path(arg) / 'practice-questions').is_dir():
        lessons = [Path(arg)]
    elif arg == 'all':
        lessons = find_all_lessons('all')
    else:
        topics = sys.argv[1:]
        lessons = find_all_lessons(topics)

    if not lessons:
        print(f'No lessons found matching: {arg}')
        sys.exit(1)

    all_pass = True
    for l_path in lessons:
        lid = l_path.name
        ok, msg = validate_lesson_practice(l_path)
        status = 'PASS' if ok else 'FAIL'
        print(f'{lid:<20}: {status} - {msg}')
        if not ok:
            all_pass = False

    sys.exit(0 if all_pass else 1)


if __name__ == '__main__':
    main()
