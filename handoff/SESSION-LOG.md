# Session Log — Physics 9702

## Update — 2026-08-16

### Corpus and parser status

- Physics P1 question papers and matching official answer keys for 2016-2025 are collected and processed.
- P1 produces a complete MCQ PNG, TXT and JSON per question plus `answer_key.json`; official A-D answers are written into question JSON.
- P1 intentionally does not export separate diagram files. Diagrams, tables, equations and options remain inside the authoritative complete MCQ image.
- The 2016 two-column answer-key format is supported and regression-tested.
- A corrupt local `9702_w21_ms_11.pdf` was replaced with a readable three-page copy and the affected batch was rerun.
- P1 verification totals: 69 papers and 2,760 MCQs across 2016-2025; all current paper sets passed their file-count and official-answer checks.
- The latest P2 blocker sweep completed 12/12 strict pair validations with zero canonical OPEN review-log entries.
- P2 canonical/parsed mirrors and review logs were synchronized; official mark-scheme content was preserved and `numerical_values_checked` remains false.
- The repair layer now includes the additive occurrence-aware `official_reconciliation` contract for duplicate IDs, aliases, pseudo-parts, cross-question placement and one-to-many official mappings.

### Next phase

- Design the shared AS Physics P1/P2 taxonomy and knowledge-base architecture before generating lessons, revision products or custom questions.
- Use the syllabus for controlled topic boundaries and past papers as the assessment-pattern evidence base.
- Reference canonical questions through stable IDs instead of duplicating files into topic folders.
- Preserve structured P2 context and inter-part dependencies while allowing topic/skill mappings at leaf-part grain.
- Define one reusable enrichment record per question/part so downstream products consume stored analysis rather than repeatedly rereading the corpus.
- Delay vector indexing until taxonomy IDs, enrichment schema, retrieval grain and metadata are stable.
- The next task should brainstorm these decisions interactively in short, precise bullets rather than deliver a complete architecture immediately.

Date: 2026-08-15
Repository: `/Users/abdullahaftab/Kognitiv/exam-paper-parser`

## Work completed

- Forward-tested `repair-physics-p2-content` on the complete May/June 2016 Paper 21 (Questions 1–7).
- Repaired its question text/LaTeX, content flow, figure placement, response schemas, dependencies and mark reconciliation.
- Recovered the missing Question 6 Fig. 6.2 crop from the complete question image.
- Consulted the original Question 7 PDF page because the extracted image omitted the hadron/lepton prompts.
- Repaired parser-created mark-scheme pseudo-parts without changing official marking meaning or order.
- Added the reusable `after_stem_text` figure placement discovered by the forward test.
- Audited the existing Paper 2 extraction approach and answer-block requirements.
- Archived the previous generated output and reorganized the active Physics P2 paths.
- Located and processed the February/March 2016 Physics 9702 Paper 22 question paper and mark scheme.
- Repaired Question 1 first, then checked/repaired Questions 2–6.
- Reconciled question-part marks against the corresponding mark-scheme parts.
- Recovered the missing Question 5 Fig. 5.2 scaffold.
- Created a local exploratory repair skill and validation script.
- Built a browser prototype for the complete 2016 Paper 22.
- Changed the prototype from a split image/answer view to a student-facing JSON-rendered view.
- Added placeholder controls to every answerable part: Mark scheme, Hints, Walkthrough, AI help and Check answer.
- Normalized the six 2016 question JSON files to use readable Unicode fallback text plus normalized LaTeX display text.
- Added `unit_latex` to response fields with units and `label_latex` to mathematical field labels where needed.
- Bundled KaTeX locally and changed the prototype to render `question_stem_latex`, `question_text_latex`, field labels and units through KaTeX while retaining plain-text fallback.
- Updated the local repair skill, answer-block registry and validator with dual-text/LaTeX requirements.

## Checks completed

- All seven 2016 Paper 21 question/mark-scheme pairs pass the strict validator.
- All six repaired question/mark-scheme pairs passed the local stricter validator.
- `prototypes/2016-paper-22-renderer/app.js` passes `node --check`.
- Prototype changes pass `git diff --check`.
- The updated local skill passes `quick_validate.py`.

## Important repository state

The repository has a very large dirty working tree, including many pre-existing deletions and modifications. Do not reset, restore, commit, delete or otherwise alter unrelated files. The active 2016 work, prototype and local skill are currently untracked.

## Last discussion

- Canonical question JSON should describe what students see and how they respond.
- Canonical mark-scheme JSON should hold official answers and marking instructions.
- Enrichment should hold hints, walkthroughs, AI rubric/checking guidance and executable deterministic rules derived from the official mark scheme.
- Proposed per-part checking modes: `deterministic`, `ai`, or `hybrid`.
- The student UI may later suppress visible figure captions and shorten nested labels, e.g. show `(b)(i)` and then `(ii)`. Canonical IDs/labels can remain complete.
- No changes were made for those two presentation refinements because the user explicitly said they can wait.

## Next starting point

Finalize the canonical question JSON architecture before progressing to final mark-scheme and enrichment schemas. In particular, decide how exact content ordering/interleaving is represented for stems, figures, tables, parent context, parts and response blocks.
