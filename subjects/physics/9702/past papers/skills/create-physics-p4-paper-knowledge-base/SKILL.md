---
name: create-physics-p4-paper-knowledge-base
description: Create or repair one Physics 9702 Paper 4 canonical-question and enrichment paper after verified compact source images exist, while preserving official mark schemes and source identity.
---

# Create Physics P4 Paper Knowledge Base

Build one paper in two owned stages. Enrichment authoring continuously checks the canonical question and immutable official criteria; it is not an enrichment-only review. Source images are evidence. Official mark-scheme JSON is immutable.

## Preflight

1. Read repository instructions, the knowledge-base contracts and controlled AS+A2 registries.
2. Require a verified compact P4 question-image package and matching canonical/official paper identity.
3. Verify that the sum of canonical question marks equals exactly 100. If raw parsed JSONs sum to less than 100, inspect the primary PDF to recover missing marks/subparts during canonical repair before creating the initial source ledger.
4. Require an initialized repository manager state created by `.venv/bin/python scripts/manage_p4_workflow.py --paper <paper> init`. It binds every canonical question and official mark-scheme file before authoring.
5. Inventory top-level questions, complete part hierarchy, answerable leaves, marks, figures and official occurrences.

## Agent-manager execution contract

Use one persistent author agent for the whole paper and keep the root agent as manager. This skill explicitly authorizes that delegation. Do not create one agent per leaf and do not author multiple questions or leaves concurrently.

For every unit:

1. Manager and author independently open the original question image at readable resolution, the whole canonical question, parent/child context, every referenced figure and placement, immutable official criteria, current enrichment, taxonomy and referenced registries.
2. Author changes only the active question or active leaf and any narrowly required controlled registry entry.
3. Manager reopens the evidence, reads the actual changed files and diff, and runs the applicable deterministic checks via `.venv/bin/python`. An author report is never approval evidence.
4. Manager either records the exact PASS token or returns a field-specific defect list to the same author. Repeat until no defect remains.
5. Do not open the next leaf or question before approval. If a later audit invalidates an earlier unit, reopen that unit and repeat its gate.

The manager is an independent approver, not a second author. If delegation is unavailable, separate the phases with a clean context reread and apply the same gates sequentially.

Before every assignment run `.venv/bin/python scripts/manage_p4_workflow.py --paper <paper> status`. Work only on the unit it reports. Only the manager invokes the corresponding `approve-canonical`, `approve-leaf`, or `close-question` command. A non-zero exit returns the unit to the same author; it never permits progression.

## Stage 1: canonical questions

Create or repair only the canonical P4 question layer. For every question require:

- source-faithful complete wording, symbols, values, units, captions, labels and marks;
- structural parents and answerable leaves in printed order, with valid parent paths;
- a complete `content_flow` sequence;
- a structured placement dictionary and non-empty file for every figure;
- response schema version `0.1` on every answerable leaf and none on structural parents;
- strict math vs prose separation: no multi-word English prose wrapped inside math mode (`$...$`) without `\text{...}`; balanced `$` delimiters; KaTeX compatibility;
- natural prose wrapping, supported LaTeX and no footer, OCR or neighbouring-question leakage.

Run `.venv/bin/python scripts/audit_structured_question.py --component P4 --paper <paper> --question <n>`. Repair canonical defects before enrichment. A canonical repair invalidates downstream enrichment review.

The manager records `QUESTION PASS` only after independently checking every printed part, mark, figure, placement, response field and `content_flow` item against the primary source.

## Stage 2: enrichment

Process answerable leaves in canonical order, exactly one active leaf at a time. For each leaf both author and manager read the full question context, figures and immutable official criteria. Require:

- precise primary topic and module; every outcome belongs to that module;
- one narrow reusable primary skill and only relevant supporting skills;
- smallest truthful pattern set and controlled knowledge references;
- progressive question-specific hints that do not reveal the result early;
- a complete, independently checked physics walkthrough;
- checking mode chosen from the full credited answer, not from answer appearance;
- exact official criterion, alternative (`OR` branches) and occurrence bindings; write distinct rubric criteria for all listed alternative routes or 'Any N from M' choices to guarantee 100% official marking-point parity;
- character-exact `field_id` match: every `field_id` referenced in `deterministic_checks` must have an identical, character-exact counterpart in the leaf's Stage 1 `response_schema.blocks`;
- `full_marks_if_all_deterministic_checks_pass: false` on any multi-mark calculation leaf where method/working marks (`C1`, `M1`) are required;
- `numerical_values_checked: false`.

Every outcome must belong to the leaf's primary module. Do not represent a prerequisite by attaching a foreign-module outcome; use a relevant supporting skill. Automatic full credit is forbidden for every multi-mark leaf.

After the author finishes a leaf, the manager checks prompt interpretation, physics, taxonomy/outcomes, reusable skill scope, hints, walkthrough, checking mode, response-field coverage and exact official occurrence bindings. Record `LEAF PASS` only when both semantic review and applicable scripts pass. No later leaf may compensate for an earlier leaf defect.

After each question, derive root patterns/topics/modules/outcomes from leaf-first occurrence order. Never sort or compare them as sets.

Run `.venv/bin/python scripts/validate_question_enrichment.py` for the question, then run `.venv/bin/python scripts/audit_structured_question.py` again.

The audit must also prove checking-mode invariants, unique criterion occurrences, and that every deterministic `field_id` exists in the canonical response schema.

After the last leaf, the author derives ordered root unions and the manager rereads the complete question and all leaves. Record `QUESTION CLOSEOUT PASS` only after full-question validators pass. This unlocks the fresh question verifier—not the next question. The next question unlocks only after both the question verifier and external auditor pass.

## Finish

Run `.venv/bin/python scripts/audit_structured_paper.py --component P4 --paper <paper>`. Handoff only after the manager has issued every `QUESTION CLOSEOUT PASS`. This authoring skill does not certify semantic release; use `$verify-physics-p4-paper-knowledge-base` independently.

Never edit official mark-scheme JSON. Preserve unrelated changes. Do not rebuild derived browser/search data before final verification.
