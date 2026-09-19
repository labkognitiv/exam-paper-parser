---
name: repair-physics-p2-content
description: Repair and normalize one Cambridge Physics 9702 Paper 2 question package and its matching mark-scheme JSON after deterministic extraction. Use for checking extracted question images, text, LaTeX, part hierarchy, printed marks, figure and part dependencies, response blocks, official marking points, alternatives, stable IDs, and question/mark-scheme reconciliation before enrichment or course mapping.
---

# Repair Physics P2 Content

Repair exactly the question requested. Do not process other questions implicitly.

## Required inputs

Locate:

- `question_NN_with_figures.png`, falling back to `question_NN.png`
- `question_NN.txt`
- `question_NN.json`
- `markscheme_NN.txt`
- `markscheme_NN.json`
- separate figure files referenced by the question JSON, for existence/link checks

Read [answer-block-registry.md](references/answer-block-registry.md) before assigning a response schema, [question-content-flow.md](references/question-content-flow.md) before repairing content order, and [review-log.md](references/review-log.md) before making changes.
Read [official-reconciliation.md](references/official-reconciliation.md) before representing immutable official-source identity, duplication, alias, or cross-question placement defects.

## Operating mode

Use `official_source_locked` unless the user explicitly authorizes mark-scheme repair. In this mode:

- compute and retain SHA-256 hashes for every mark-scheme JSON before work;
- treat mark-scheme JSON as immutable official source material;
- diagnose duplicates, hierarchy conflicts and notation defects without editing them;
- verify the hashes again before reporting completion.

Never infer authorization to leave `official_source_locked` merely because the validator reports a mark-scheme defect.

## Workflow

1. Confirm the question and mark scheme share `question_id`, paper metadata and question number.
2. Inspect the complete question image with figures as the primary visual source. Account for every visible question number, part, subpart, printed mark, diagram, table, graph and answer area.
3. Compare the complete image with question text, plain JSON text, LaTeX JSON text and the JSON hierarchy. Confirm that nothing visible was lost or assigned to the wrong part, and encode the printed order in `content_flow` and figure `placement`.
4. Confirm every visible diagram has a figure record and an existing linked file. Log missing, uncertain or defective crops for user review; do not create, recrop or replace them.
5. Repair transcription only when supported by the image. Correct lost roots, fractions, scripts, symbols, units, line breaks and duplicated printed marks. Apply the dual plain-text/LaTeX rules below; never rely on frontend string substitutions to repair notation.
6. Preserve stable question and part IDs. For collapsed printed subparts, follow the blocked-leaf procedure below; do not restructure without user approval.
7. Add one `response_schema` to each answerable leaf part. Do not add a response to a structural parent. Prefer combinations of existing registered blocks and controls. When a source question proves that they cannot represent the printed response pattern, follow the registry's incremental-extension procedure rather than forcing an inaccurate type.
8. Record explicit figure dependencies and clear previous-part dependencies. Do not infer Physics concepts or enrichment.
9. Compare the mark-scheme text and JSON. In `official_source_locked` mode, report but do not edit notation defects, exact duplicates or hierarchy conflicts. Outside locked mode, preserve official meaning and order while applying only explicitly authorized repairs.
10. Reconcile each printed part mark against question JSON and mark-scheme JSON, then reconcile their sums against the printed question total. Do not accept total-only agreement when individual parts differ.
    When an immutable official mark-scheme part demonstrably combines multiple separately printed question leaves, preserve those printed leaves and record `official_part_mapping` with one `markscheme_part_id` and the ordered `question_part_ids`; their printed marks must sum exactly to the locked official part mark.
    When duplicate IDs, multiple official identities for one printed leaf, pseudo-parts, aliases, or cross-question placement make `official_part_mapping` insufficient, use the additive occurrence-aware `official_reconciliation` contract. Never combine the two mapping formats.
11. Treat parenthesized mark codes and explicit `OR` routes as alternatives, not additional available marks.
12. Run `scripts/validate_pair.py QUESTION_JSON MARKSCHEME_JSON`.
13. Report every changed file and review-log entry.

## Collapsed printed subparts

When one extracted leaf contains multiple separately numbered or separately marked printed prompts:

1. Record the printed hierarchy, extracted leaf ID and official mark-scheme IDs in an OPEN `collapsed_printed_subparts` entry.
2. Do not split, rename or remap parts without user approval.
3. Leave only the ambiguous collapsed leaf without `response_schema`; repair unaffected leaves normally.
4. Keep `content_structure_checked` and `marks_reconciled` false for the affected question.
5. Repair unrelated transcription, LaTeX, figure placement, dependencies and response-schema defects in the same question.
6. Require the remaining validator failures to be direct consequences of the logged collapse.

## Repair constraints

- Keep the official question and mark scheme separate.
- Never place correct answers or marking rules in the question JSON.
- Never invent missing official marking content.
- Never change the maximum mark merely to make validation pass.
- Keep source images unchanged.
- Do not open original PDFs, create or recrop figures, materially restructure question/mark-scheme data, or extend the registry without user approval. Record the issue in the paper review log and continue only with unaffected work.
- Do not use a combined question image as a `response_background`. An assessed drawing or annotation scaffold requires an approved standalone figure record and file. Follow [question-content-flow.md](references/question-content-flow.md) when that crop is absent.
- For unsupported response patterns, use `proposed_type` and log the proposed reusable extension.
- Mark uncertain content for review rather than guessing.

## Text and mathematical notation

- Every non-empty `question_stem` requires `question_stem_latex`; every non-empty part `question_text` requires `question_text_latex`.
- Plain fields must be readable without a math renderer. Use Unicode where needed, such as `vₓ`, `s⁻¹`, `x₀`, `β⁻`, `Ω`, `×` and `√`. Do not leave LaTeX control sequences, braces, carets or underscore scripts in plain text.
- LaTeX fields contain the complete prose and delimit only mathematical spans with `$...$`. Normalize scripts, fractions, roots, Greek letters and upright SI units.
- Preferred examples: `$v_x$`, `$I_2/I_1$`, `$\frac{1}{2}kx^2$`, `$8.5\,\mathrm{m\,s^{-1}}$`, `$\bar{\nu}$`.
- A response field with `unit` must also have `unit_latex`. Keep `unit` as readable plain text and store `unit_latex` without surrounding `$` delimiters.
- A mathematical response-field label may add `label_latex`, also without surrounding `$` delimiters. Storage roles are semantic and must not be used as mandatory visible labels.
- Preserve a plain-text fallback even when the final UI renders LaTeX.

## Completion gate

Require valid JSON, matching IDs, unique part and marking-point IDs, valid content flow and figure placement, explicit verification status, reconciled totals, valid response schemas on answerable leaves, no response schema on structural parents, and no unresolved exact duplicate marking points.

For an explicitly blocked pair, replace the ordinary PASS requirement with all of these conditions:

- every validator failure is a direct and necessary consequence of one or more OPEN review entries;
- no unrelated raw-LaTeX, figure-placement, dependency, content-flow or response-schema failure remains;
- only the ambiguous or unsupported leaf lacks a response schema;
- relevant verification flags remain false and `numerical_values_checked` remains false;
- the pair is reported as BLOCKED, never PASS.

## Paper-level closing sweep

After all requested questions in a paper are processed:

1. Run the strict validator again on every question/mark-scheme pair.
2. Confirm every `numerical_values_checked` value is false unless an independent numerical audit was explicitly performed.
3. Confirm each blocked failure is covered by an OPEN review entry and no unrelated failure remains.
4. In `official_source_locked` mode, compare all post-work mark-scheme hashes with the retained pre-work hashes.
5. Confirm temporary repair scripts and scratch artifacts were removed.
6. Report PASS/BLOCKED counts, review entries, changed canonical files and hash preservation.
