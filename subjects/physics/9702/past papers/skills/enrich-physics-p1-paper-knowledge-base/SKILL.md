---
name: enrich-physics-p1-paper-knowledge-base
description: Author, validate, and audit Cambridge International AS Physics 9702 Paper 1 (MCQ) knowledge-base enrichment records using the flat P1 schema, text-first visual inspection, deterministic grading, and concise caveman communication.
---

# Enrich Physics P1 Paper Knowledge-Base

Complete one full Cambridge AS Physics 9702 Paper 1 (40 MCQs).

## Operating Mode & Strict Rules

- **Communication**: Strict caveman language only. No verbose markdown tables, no filler text. Report concise status (PASS, FAIL, key counts).
- **Source immutability**: Canonical question files (subjects/physics/9702/papers/p1/[PAPER_CODE]_qp_*/question_*.json) are strictly immutable.
- **Preflight SHA-256**: Hash all question JSONs before authoring and verify byte-for-byte invariance after completion.
- **Flat Schema**: Use 9702_p1_enrichment_v1 (no nested parts array, no top-level duplication).

---

## Inspection Strategy: Text-First with Image Fallback

For each question question_XX:
1. **Read Text/JSON First**: Read question_XX.json. Obtain question_text, correct_answer, has_visual_content, and options.
2. **Check Image only if Visual**: If has_visual_content: true or the prompt refers to a diagram/graph/circuit, view question_XX.png. If pure text/conceptual, skip PNG to save tokens and speed up generation.

---

## Flat P1 Schema Contract (9702_p1_enrichment_v1)

Target path: subjects/physics/9702/enrichment/p1/[PAPER_CODE]_qXX.enrichment.json

```json
{
  "schema_version": "9702_p1_enrichment_v1",
  "question_id": "9702_s16_11_q01",
  "component": "P1",
  "difficulty": 2,
  "question_patterns": [
    "vector_diagram_construction",
    "comparison"
  ],
  "topic_id": "9702_t01",
  "module_id": "9702_t01_m04",
  "skill_id": "9702_skill_add_vectors",
  "accepted_answer": "B",
  "hints": [
    "Progressive conceptual hint 1",
    "Progressive calculation / deduction hint 2"
  ],
  "walkthrough": [
    "1. Key physical relationship or direct step to the correct answer.",
    "2. Calculation or reasoning showing why the accepted option follows.",
    "3. Diagnostic explanation of why the main distractors are incorrect."
  ]
}
```

---

## Controlled Registries & Log Sheet

- **Paper Log Sheet**: subjects/physics/9702/past papers/skills/enrich-physics-p1-paper-knowledge-base/references/paper-log.md (master progress log across all 69 papers)
- **Taxonomy**: subjects/physics/9702/knowledge/2025-2027/as/9702-2025-2027-as-taxonomy.json (topic_id, module_id)
- **Skills**: subjects/physics/9702/knowledge/skills.json (skill_id)
- **Question Patterns**: subjects/physics/9702/knowledge/question-patterns.json (question_patterns)

---

## Parallel Execution & Agent Claiming Protocol

When running multiple authoring agents in parallel across papers:
1. **Pre-flight Check**: Check `references/paper-log.md`. Only select papers with status `NOT_STARTED`.
2. **Claiming**: Before starting, ensure no other agent is working on the same paper code. Optionally mark `IN_PROGRESS` in `references/paper-log.md`.
3. **Execution**: Perform preflight SHA-256, author all 40 questions, validate each MCQ.
4. **Post-flight Sync**: After 40/40 PASS and SHA-256 invariance verification, run:
```bash
.venv/bin/python scripts/update_p1_paper_log.py
```
This automatically updates `references/paper-log.md` with the new completion status and summary statistics.

---

## Validation & Verification Gate

1. Validate every MCQ individually:
```bash
.venv/bin/python scripts/validate_p1_enrichment.py \
  --enrichment subjects/physics/9702/enrichment/p1/[PAPER_CODE]_qXX.enrichment.json \
  --question subjects/physics/9702/papers/p1/[PAPER_CODE]_qp_*/question_XX.json
```

2. Independent whole-paper audit:
- 40 / 40 questions present.
- 100% match with official answer_key.json / correct_answer.
- Preflight SHA-256 byte-for-byte verified.
- Schema valid, valid topic/module/skill IDs.
- >= 2 progressive hints and >= 2 walkthrough steps per MCQ.

3. Final report in caveman style:
```
PASS
[PAPER_CODE] (40 MCQs) Complete & Validated.
- Validation: 40/40 PASS
- Preflight SHA-256: PASS
- Answer Key Match: 100%
- Log Sheet: UPDATED
```

