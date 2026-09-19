---
name: assign-physics-mcq-difficulty-tier
description: Assign intrinsic easy/medium/hard difficulty and the approved 60% mandatory / 40% revision practice split to every question in one QC-passed Cambridge Physics single-select MCQ paper. Use after compact skills/rubrics are approved. Keeps difficulty separate from practice priority, gives evidence for every decision, and never creates lessons, solutions, optional tiers, or extraction-column changes.
---

# Assign Physics MCQ Difficulty and Tier

Work on one complete paper. Read [references/difficulty-tier-contract.md](references/difficulty-tier-contract.md).

## Workflow

1. Read the verified questions, topic/module map, and approved skills/rubrics.
2. Assign intrinsic difficulty independently of tier:
   - `easy`: direct recall or one transparent substitution.
   - `medium`: interpretation, two linked ideas, or a standard multi-step calculation.
   - `hard`: non-obvious representation, several linked decisions, or unusually demanding reasoning for a one-mark MCQ.
3. Rank practice priority across the paper. Mark core, diagnostic, representative questions `mandatory`; mark repetition, narrow variation, historical outside-current-component content, or consolidation `revision`.
4. Enforce exactly 60% `mandatory` and 40% `revision` using nearest whole-row counts. For 40 questions, require 24 and 16.
5. Give a concise reason for every row. Do not use difficulty alone to determine tier. Keep prose as UTF-8 and encode every mathematical expression in `reason` as balanced inline `$...$` LaTeX under the Physics web-math contract.
6. Validate with `scripts/validate_physics_mcq_difficulty_tier.py`.

Create only `enrichment/<paper_code>_difficulty_tier.csv` and its report. Do not create `optional`, solutions, lessons, or final topical ordering.
