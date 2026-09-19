---
name: tag-physics-mcq-skills-rubric
description: Assign concise, human-readable primary skills, at most one supporting skill, and compact diagnostic AI-rubric statements to every question in one verified Cambridge Physics single-select MCQ paper. Use after extraction and topic/module mapping QC and before difficulty/tiering. Reuses the universal single_select_mcq_v1 scoring rule and never creates lessons, solutions, detailed written-working rubrics, or new extraction columns.
---

# Tag Physics MCQ Skills and Rubric

Work on one QC-passed paper at a time. Keep extraction and mapping files immutable.

## Workflow

1. Read the extraction CSV, QC-passed topic/module map, active central Physics skill registry, and previously approved enrichment rows.
2. Read [references/physics-mcq-skill-rubric-contract.md](references/physics-mcq-skill-rubric-contract.md).
3. Reuse an exact approved registry name when the assessed action is materially the same. If no skill fits, stage it through `$maintain-physics-mcq-skill-library`; the assignment cannot pass until the approved registry contains it.
4. Assign exactly one `primary_skill`. Add at most one supporting skill when the correct choice genuinely requires a second distinguishable action.
5. Write one short `ai_rubric` statement per skill tag. Describe the evidence represented by choosing the correct option; do not claim to observe hidden working. Keep prose as UTF-8 and encode every mathematical expression in the rubric value as balanced inline `$...$` LaTeX under the Physics web-math contract.
6. Use `single_select_mcq_v1` unchanged: selected option equals `correct_option` earns 1, otherwise 0.
7. Validate with `scripts/validate_physics_mcq_skills_rubric.py`, supplying the active registry, and save the JSON report.

## Output

Create only `enrichment/<paper_code>_skills_rubric.csv` and its validation report. Do not add these fields to the extraction CSV.

Do not create lessons, lesson order, solutions, hints, written-solution guidance, topic compilations, or difficulty/tier values.
