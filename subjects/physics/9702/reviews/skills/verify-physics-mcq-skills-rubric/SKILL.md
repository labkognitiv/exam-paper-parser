---
name: verify-physics-mcq-skills-rubric
description: Independently QC the primary skill, optional supporting skill, and compact diagnostic AI rubric for every row of one Cambridge Physics 9702 Paper 1 MCQ paper. Use immediately after tag-physics-mcq-skills-rubric and before assigning difficulty or practice tier. Reassesses all rows from verified CSV data, enforces the approved central registry and MCQ evidence boundary, writes a read-only ledger, and never edits assignments or creates lessons or solutions.
---

# Verify Physics MCQ Skills and Rubric

Review one complete paper from CSV alone. Treat assignments as untrusted and immutable.

## Workflow

1. Confirm taxonomy QC and the tagging validator passed.
2. Read each question, choices, visual description, approved topic/module map, active skill registry, and assigned skills/rubric.
3. Independently check every row for primary-skill fit, supporting-skill necessity, registry fit, and rubric fit. A rubric may describe only what a correct option demonstrates.
4. Write `enrichment/skills_qc/<paper_code>_skills_rubric_qc.csv` using [references/skills-qc-contract.md](references/skills-qc-contract.md).
5. Run `scripts/validate_skills_rubric_qc.py` and save `enrichment/skills_qc/qc_manifest.json`.

Stop unless every row and the manifest pass. Record disagreements; never repair upstream files during QC.

