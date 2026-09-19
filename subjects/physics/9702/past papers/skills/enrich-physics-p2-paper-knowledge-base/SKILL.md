---
name: enrich-physics-p2-paper-knowledge-base
description: Create or repair one Cambridge Physics 9702 P2 paper's enrichment JSON, mappings, controlled references, hints, walkthroughs, and checking rules leaf by leaf.
---

# Enrich Physics P2 leaf by leaf

Read repository instructions, the knowledge contracts and registries under `subjects/physics/9702/knowledge/`, and [the workflow contract](references/workflow-contract.md).

## Setup

1. Inventory the named paper's canonical questions, official mark schemes, answerable leaves, marks, reconciliation metadata, existing enrichment, and source hashes.
2. Snapshot definition, formula, skill, and question-pattern registries before editing.
3. When agents are authorized, use one persistent author for the whole paper and reserve a distinct agent for final verification.

## Leaf loop

Process one answerable leaf at a time in canonical order.

1. Read the full question context, canonical leaf, official criteria, syllabus taxonomy, and controlled registries.
2. Edit only the required `subjects/physics/9702/enrichment/p2/*.enrichment.json` record or narrowly required controlled record.
3. Check physics, arithmetic, mapping, difficulty, smallest truthful pattern set, one narrow primary skill, knowledge references, progressive hints, complete walkthrough, checking mode, official bindings, and unchanged source hashes.
4. Repair the same leaf until it passes before advancing.
5. After a question, derive question-level patterns and mappings as exact first-occurrence ordered unions of its leaves.

## Final gate

Run `python3 scripts/audit_p2_question.py --repo . --paper <paper> --question <number>` for every question, then run `python3 subjects/physics/9702/reviews/skills/verify-physics-p2-paper-knowledge-base/scripts/audit_paper.py --repo . --paper <paper>`. Hand raw artifacts to a fresh verifier using `$verify-physics-p2-paper-knowledge-base`. A paper is PASS only after independent verification passes, controlled-registry additions are proven non-duplicate, canonical hashes match, and all semantic notices are resolved.

Never modify canonical questions or official mark schemes in this workflow. Keep `numerical_values_checked: false`. Preserve unrelated work.
