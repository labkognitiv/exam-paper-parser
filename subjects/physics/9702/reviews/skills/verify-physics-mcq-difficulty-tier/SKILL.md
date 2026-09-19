---
name: verify-physics-mcq-difficulty-tier
description: Independently QC intrinsic difficulty and the exact 60% mandatory / 40% revision practice allocation for every row of one Cambridge Physics 9702 Paper 1 MCQ paper. Use immediately after assign-physics-mcq-difficulty-tier and before final enrichment QC. Reassesses every question from verified CSV data, keeps difficulty separate from practice priority, writes a read-only ledger, and never edits tiers or creates lessons or solutions.
---

# Verify Physics MCQ Difficulty and Tier

Review one paper from verified CSV artifacts. Treat assigned values as untrusted and immutable.

## Workflow

1. Confirm the skills/rubric QC and difficulty/tier assignment validator passed.
2. Independently reassess intrinsic `easy`, `medium`, or `hard` difficulty for every row.
3. Independently reassess `mandatory` versus `revision` using conceptual importance, diagnostic value, representativeness, repetition, and historical scope. Do not infer tier from difficulty.
4. Write `enrichment/difficulty_tier_qc/<paper_code>_difficulty_tier_qc.csv` using [references/difficulty-tier-qc-contract.md](references/difficulty-tier-qc-contract.md).
5. Run `scripts/validate_difficulty_tier_qc.py` and save `enrichment/difficulty_tier_qc/qc_manifest.json`.

Stop unless every independent value agrees, every row passes, and the allocation is exactly 60/40.

