---
name: maintain-physics-mcq-skill-library
description: Govern the central Cambridge Physics 9702 MCQ skill registry while papers are enriched. Use before and during per-paper skill/rubric tagging to reuse exact approved human-readable skills, automatically stage genuinely missing skill proposals, validate the registry, and merge only reviewed proposals with versioned provenance. Prevents duplicate wording and never changes question extraction, taxonomy, lessons, solutions, or rubrics already stored per question.
---

# Maintain Physics MCQ Skill Library

Use the active registry recorded in `Physics A Level/governance/active_skill_library.json`.

## Workflow

1. Read [references/skill-library-contract.md](references/skill-library-contract.md).
2. Before tagging a paper, load all approved registry names and definitions.
3. Reuse an exact skill name when it represents the same measurable action.
4. If no approved skill fits, use `scripts/stage_skill_proposals.py` after drafting the paper assignments. It writes only missing skills with `review_status=pending`.
5. Review every proposal for human readability, distinct meaning, correct role and topic/module provenance. Change only genuinely approved rows to `approved`.
6. Run `scripts/merge_approved_proposals.py` to produce a new staged registry, change log and manifest. Never overwrite the active registry directly.
7. Validate the staged package with `scripts/validate_skill_library.py`.
8. Activate the new version only after validation and paper enrichment QC both pass.

Do not centralise question-specific `ai_rubric` sentences. The registry controls skill identity and canonical definitions; each paper retains its own diagnostic wording.

