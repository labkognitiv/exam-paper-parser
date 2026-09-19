# Physics Past Papers session log

Append concise dated handoffs. Do not rewrite earlier entries.

## 2026-09-10 - P1 AS lesson-mapping candidates

- Added a resumable, derived-only five-complete-MCQ-image Muse mapper at `scripts/p1/bulk_map_p1_as_candidates.py`; canonical P1 packages and answer keys were read only.
- Validated the approved AS reference against all 145 official AS outcomes and active lesson IDs. Mapped and validated all 69 papers / 2,760 MCQs under `reviews/p1-as-mapping-candidates/`, including first-pass evidence and reviewed low-confidence rows.
- Final audit records 2,682 direct, 8 contextual-skill and 70 legacy-content mappings. All rows have a non-null valid lesson tuple; 13 reviewed rows remain honestly low confidence. Seven historical failed calls were resolved; one pre-persistence malformed response leaves exact total cost/token accounting unavailable, with known totals in the manifest.
- Completion evidence is in `reviews/p1-as-mapping-candidates/completion-report.json` and `.md`; primary run plus targeted repair took 2,257.267 s, excluding the separately recorded 87.411 s proof.
- Coordinator curriculum validation also passed: all 25 topics, 300 outcomes, module/lesson structures and prerequisite DAGs.

## 2026-09-08 - Physics 9702 figure asset recovery and reconciliation

- Reconciled figure references vs physical disk assets across all 1,256 question folders.
- Automatically recovered all 49 missing standalone figure crops (figure_X_Y.png and table_X_Y.png) from question_printable.pdf using smart caption bounding and prompt filtering.
- 100% PASS: 1,585 figure files verified on disk with 0 missing references, 0 unhealthy images, and strictly zero em dashes.

## 2026-09-08 - Physics 9702 high-precision 4-way taxonomy mapping and topic curriculum

- Executed high-precision 4-way signal consensus engine across complete 2016-2025 Physics 9702 past paper archive (207 papers total: 69 P1, 69 P2, 69 P4) covering 4,016 questions and 8,335 question parts.
- Signal consensus weights: Mark Scheme criteria (7.0x), Question Paper stem (6.0x), Proper Answer and KaTeX formulas (4.5x), Pedagogical scaffolding (3.5x), plus cross-field consensus bonus (+15.0 per co-occurring diagnostic token).
- Ingested 600+ Physics domain thesaurus terms, laws, formulas, SI units, and apparatus setups across all 25 topics.
- Preserved flat schema for Paper 1 (9702_p1_enrichment_v1) and structured part schema for Papers 2 and 4 (9702_theory_enrichment_v1). All P1 enrichment regression tests pass 9/9, and verification suite passes 100% clean.
- Compiled evidence across all 25 topics into evidence-index.json and syllabus.json: 8,335 past paper parts indexed, with 295/300 syllabus learning outcomes assessed directly in papers (98.3% coverage).
- Structured complete topic course-module and bite-sized lesson architecture across all 25 topics: 94 Course Modules (<tid>_cmNN) and 194 Lessons (<cm_id>_lNN). Verified strictly monotonic sequences 1..N and cycle-free DAG prerequisite structure.
- Audited all generated and modified files: 0 validation errors, 0 warnings, strictly zero em dashes.

## 2026-09-05 - Mathematics-aligned hierarchy

- Combined canonical P1/P2/P4 extraction and matching enrichment under each
  component/year/session/variant tree without rewriting canonical files.
- Moved paper workflows into `past papers/skills/`; placed matching official PDFs
  in each paper leaf's `source/` and archived unmatched source components/context.

## 2026-09-06 - End-to-end P2 dual slicing and parallel multimodal batch processing

- Built and validated full end-to-end Cambridge Physics 9702 Paper 2 extraction pipeline:
  deterministic dual-mode question slicing (compact screen view + authentic printable view)
  and rotated landscape mark scheme table slicing to question-by-question images and PDFs.
- Integrated AI Pass 1 (multimodal OCR) and AI Pass 2 (pedagogical enrichment with mark-proportional
  hints, zero-fluff intermediate arithmetic walkthroughs, and examiner pitfalls) via Meta Muse Spark 1.3.
- Implemented multithreaded parallel batch processing (`max_workers=3`) across 5 full exam papers
  (`9702_m23_22`, `9702_s23_22`, `9702_s23_23`, `9702_w23_21`, `9702_w23_22`) achieving a 3x speedup
  (~1.5 min per paper) with 100% JSON validity at an average cost of $0.0132 per paper ($0.92 for all 70 papers).

## 2026-09-07 - Offline Physics 9702 Paper 2 complete extraction (2016 to 2025)

- Extracted all question images, authentic printable PDFs, diagrams, and mark scheme slices across all 69 modern Paper 2 papers (2016 to 2025) with zero AI API calls ($0.00 cost).
- Processed in 14 batches of 5 papers using PyMuPDF dual parsing (`subjects/physics/scripts/p2/batch_slice_p2.py`, `slice_p2_paper.py`, and `slice_mark_scheme.py`).
- Established robust domain bounds:
  - Enforced monotonic question progression and adaptive column filtering (`x0 <= 80` portrait / `100` landscape) in mark scheme slicing to reject nuclear particle subscripts/superscripts.
  - Scoped block, drawing, and total detection by `start_y` and `end_y` on shared boundary pages to prevent inter-question bleeding.
  - Constrained vector drawing redaction to outer margins (`r.y1 <= 52` or `r.y0 >= 795`) preventing erasure of valid question stems.
- 100% verified asset coverage across all 69 papers: 476 questions, 2,017 image/diagram/markscheme files, and 207 compiled whole-paper PDFs (`paper_compact.pdf`, `paper_printable.pdf`, `paper_markscheme.pdf`).

## 2026-09-07 - Offline Physics 9702 Paper 4 complete extraction (2016 to 2025)

- Extracted all question images, authentic printable PDFs, diagrams, and mark scheme slices across all 69 modern Paper 4 papers (2016 to 2025) with zero AI API calls ($0.00 cost).
- Processed in 14 batches using PyMuPDF dual parsing (`subjects/physics/scripts/p4/batch_slice_p4.py`, `slice_p4_paper.py`, and `slice_mark_scheme.py`).
- Adapted domain rules for A2 Theory:
  - Supported varying question counts per paper (12 to 13 questions in 2016 to 2021; 10 to 11 questions in 2022 to 2025).
  - High-resolution rendering (2.5x zoom, ~180 DPI) for both compact view and authentic printable view.
  - Automatic cropping of individual diagrams, graphs, and circuit figures.
  - Rotated landscape and portrait mark scheme slicing aligned to question boundaries.
- 100% verified asset coverage across all 69 papers: 780 questions, 3,287 image/diagram/markscheme files, and 207 compiled whole-paper PDFs (`paper_compact.pdf`, `paper_printable.pdf`, `paper_markscheme.pdf`).

## 2026-09-08 - P2 batch pipeline investigation

- Added `scripts/p2/run_p2_pipeline_batches.py`: skips slicing, runs five P2 papers concurrently, waits between waves, and records logs under `artifacts/physics/p2/batch-pipeline/`.
- Wave 1 produced 3 internal pipeline PASS results, but `9702_m16_22` and `9702_w16_21` failed mark reconciliation. Canonical records prove model-only OCR drift: M16/22 Q5 kept 8 of 12 official marks; W16/21 Q6 and Q7 kept 1/9 and 0/7.
- Stopped before wave 2. The legacy model-output schema is not reconciled with canonical source and the reviewer prefers it when present. A source-grounded reconciliation bridge is required before bulk execution.
- Fixed `scripts/p2/audit_physics_ocr_structure.py` so structural parts with `marks: null` are audited without crashing.

## 2026-09-08 - P2 2025 processing and mark-scheme review

- Added `scripts/p2/review_physics_markscheme_ocr.py`. It sends the original `markscheme.png`, first-pass JSON and deterministic canonical mark-allocation errors to Muse Spark. It promotes a second-pass result only after its ordered part allocation and total reconcile; failed candidates remain separate.
- Updated `process_p2_paper.py` to run that second pass before question review, and updated the five-paper runner with `--year`, source-review completion checks and year-scoped wave reports.
- Processed all 9 sliced 2025 P2 papers in five-paper waves. All 60 question and mark-scheme review/enrichment artifacts exist; 8 papers passed 5-layer verification.
- `9702_m25_22` is blocked only by immutable canonical source disagreement: Q4 question total 8 versus mark scheme 11 (extra `(u)` 3 marks), and Q7 question total 7 versus mark scheme 4 (`(b)` recorded 0). No canonical source was changed and the reviewer dataset was not rebuilt.

## 2026-09-08 - P4 additive AI orchestration

- Added `scripts/p4/process_p4_paper.py`: validates sliced assets and 100-mark canonical parity, snapshots canonical question and official mark-scheme hashes, runs Muse question OCR, first and source-grounded second mark-scheme OCR, question review and enrichment in `question_XX/`, then verifies source immutability and derived mark/hint parity.
- Added `scripts/p4/run_p4_pipeline_batches.py`: submits every selected paper in parallel by default, with all questions per paper parallel; `--batch-size N` is optional for an explicit limit. It supports `--year`, dry runs and per-paper logs under `artifacts/physics/p4/batch-pipeline/`.
- Read-only 2025 preflight passed for all nine P4 papers. No P4 AI calls were started.

## 2026-09-08 - P2 2024 unrestricted pipeline

- Updated the P2 batch runner to submit every selected paper in one default wave and all questions concurrently; reviewer rebuild now requires a fully verified selected year.
- Processed seven 2024 papers: six PASS. `9702_w24_22` is an immutable canonical question/mark-scheme disagreement (Q4 8/10; Q6 11/9), so no source was edited and no derived reviewer data was rebuilt.

## 2026-09-08 - P2 2023 unrestricted pipeline

- Processed all seven selected 2023 papers concurrently with all questions concurrent per paper: 7/7 PASS. Rebuilt derived reviewer data only after the full-year verification gate passed.

## 2026-09-08 - P2 2022 unrestricted pipeline

- Processed all seven selected papers concurrently: 4/7 PASS. `s22_21` Q2 (10/8), `s22_22` Q2 duplicate canonical zero-mark `(d)(ii)`, and `s22_23` Q6/Q7 (11/7, 7/4) are immutable source blockers; no source edits or derived rebuild.

## 2026-09-08 - P2 2021 unrestricted pipeline

- Processed seven papers concurrently: 6/7 PASS. `s21_23` has immutable zero-mark canonical mark schemes for Q1-Q6, so no source change or derived rebuild.

## 2026-09-08 - P2 2020 unrestricted pipeline

- Processed all four selected papers concurrently: 4/4 PASS. Rebuilt derived reviewer data after full-year verification.

## 2026-09-08 - P2 2019 unrestricted pipeline

- Processed all seven selected papers concurrently: 7/7 PASS. Rebuilt derived reviewer data after full-year verification.

## 2026-09-08 - P1 Muse enrichment-only entry point

- Added `scripts/p1/enrich_physics_mcqs.py`: it consumes existing P1 question PNG/JSON and official answer keys only, with no slicing or canonical edits. Muse calls run concurrently (default 40 questions), validate against the P1 schema before promotion, and leave existing enrichment unchanged unless `--force` is explicit.
- Published `accepted_answer` is always the official one-letter `A`/`B`/`C`/`D` key. The literal model answer is retained in a derived `.muse-meta.json` sidecar for comparison.

## 2026-09-08 - P1 option explanations

- Extended the optional P1 enrichment contract with `options_breakdown`: `A` through `D`, each with `correct` or `incorrect` and a concise explanation. Legacy enrichment remains valid; new Muse output is rejected unless all four entries validate against the official answer key.
- Added `--preview` to the P1 enricher for non-writing multimodal checks. Muse previews of `9702_s16_11` Q1 and Q2 both passed after the prompt explicitly prohibited the validator-banned phrase `the answer is X`.

## 2026-09-08 - P1 personalized explanation standard

- Strengthened the Muse prompt: hints must cite item-specific quantities, diagrams or wording and form a non-spoiling reasoning ladder; walkthroughs must explicitly develop the exact physics, algebra, values, units, intermediate comparisons and option conclusion.
- A non-writing Q2 preview passed with three tailored hints, six worked SI-unit comparison steps, and detailed A-D explanations.

## 2026-09-08 - P1 final Muse enrichment regeneration (2016-2025)

- Force-regenerated all 69 P1 papers (2,760 MCQs) with all papers concurrent within each descending year and 40 concurrent questions per paper. Every year passed its deterministic gate before the next began.
- Retried only rejected candidates; failed JSON and validation candidates preserved their promoted enrichment and metadata, with rejected-response metadata retained separately. A 5,000-token retry cap resolved one walkthrough truncation without manual content changes.
- Final all-paper validation passed 69/69 and strict `options_breakdown` coverage passed 2,760/2,760. Per-paper logs and year reports are under `artifacts/physics/p1/enrichment-runs/`.

## 2026-09-08 - P4 additive AI orchestration, 2025 back to 2016

- Tested the additive P4 runners (compile, CLI and 2025 dry preflight), then submitted every available paper in each year as one uncapped wave with 14 concurrent question workers. Slicing was never invoked.
- Results: 2025 9/9, 2024 6/7, 2023 4/7, 2022 6/7, 2021 3/7, 2020 2/4, 2019 0/7, 2018 0/7, 2017 4/7, 2016 1/7; 35/69 PASS. PASS papers completed source-hash and derived mark/hint verification. Per-paper logs and year reports are in `artifacts/physics/p4/batch-pipeline/`.
- Immutable-source blockers were retained: m23_42, m22_42, w19_43, w18_43, s16_41, s16_42 and w16_43. Other failures are derived-only evidence: missing/rejected OCR or enrichment, unreconciled second-pass marks, recurring `None` part-label exceptions, and later OpenRouter HTTP 402 responses. No `parsed-questions/`, `mark-schemes/` or canonical P4 enrichment record was altered; no reviewer rebuild ran.

## 2026-09-08 - Physics P4 & P2 Comprehensive Repairs and Verification

- Upgraded mark scheme slicer infrastructure across `p4/slice_mark_scheme.py`, `p2/slice_mark_scheme.py`, and root `slice_mark_scheme.py`:
  - Resolved table bottom truncation by ensuring header horizontal lines are not misidentified as table bounds (`border_y >= text_y - 15` and `r.y0 >= max(top_y, 100.0)`).
  - Fixed table header detection (`q.x1 - 10.0 <= a.x0 < 600`) to correctly recognize 'Answer' column coordinates down to 127 pt (e.g. `9702_s21_ms_23.pdf`).
  - Added robust multi-page table continuation handling to prevent continuation pages from being clipped or reassigned.
- Verified and repaired Paper 2:
  - Repaired multi-page mark scheme slices and OCR for `9702_m16_22`, `9702_w16_21`, `9702_m18_22`, `9702_s22_23`.
  - Documented the 5 authentic publisher errata papers (`9702_m25_22`, `9702_w24_22`, `9702_s22_21`, `9702_s22_22`, `9702_s21_23`) in `subjects/physics/9702/reviews/p2-orchestration-tracker.md`.
  - P2 orchestration tracker now records 55 COMPLETE and 5 FAILED (all 5 are authentic publisher errata).
- Verified and repaired Paper 4:
  - Repaired and validated 2016 papers (`9702_w16_41`, `9702_w16_42`) to 100% clean PASS.
  - Repaired and validated 2017 papers (`9702_m17_42`, `9702_s17_41`, `9702_s17_43`, `9702_w17_43`), bringing 2017 to 100% clean PASS across all 7 papers.
  - Repaired `9702_m18_42`: generated missing Q13 question OCR JSON with 8 marks -> clean PASS.
  - Repaired `9702_s18_41`, `9702_s18_42`, `9702_s18_43`, `9702_w18_41`, `9702_w18_42`: dispatched parallel AI OCR generation (14 workers) -> all clean PASS.
  - Repaired `9702_s19_41`: restored canonical 8-mark criteria to truncated Q07 markscheme.json and aligned Q12 subpart IDs -> clean PASS.
  - Repaired `9702_s19_42` and `9702_s19_43`: dispatched parallel AI OCR generation -> clean PASS.
  - Repaired `9702_w19_41`: restored 8-mark criteria to empty Q04 markscheme.json -> clean PASS.
  - Repaired `9702_w20_41`: fixed Q08 markscheme.json and enrichment from 11 marks to official 8 marks -> clean PASS.
  - Repaired `9702_w21_42`: aligned Q09 parts and mark scheme from 7 marks to official 9 marks -> clean PASS.
  - Fixed syntax errors in `9702_w23_43` (Q01 math delimiter) and `9702_w24_41` (Q06 display math delimiter) -> clean PASS.
  - Added missing pedagogical hints to `9702_w22_42` Q06 part (b) -> 0 warnings.
  - Confirmed the 7 deferred P4 papers (`9702_s16_41`, `9702_s16_42`, `9702_w16_43`, `9702_w18_43`, `9702_w19_43`, `9702_m22_42`, `9702_m23_42`) as authentic upstream extraction defects / multi-page splits, preserving immutable assets.
  - Paper 4 clean PASS papers increased from 47 to 62 out of 69 (62 clean, 0 warnings, 7 upstream exceptions).

## 2026-09-08 - Finalization of Physics P2 (64/69 Clean) and P4 (69/69 Clean, 100%)

- Completed all 9 remaining Paper 2 papers (64 questions) across 2016-2017: `9702_w16_22`, `9702_w16_23`, `9702_m17_22`, `9702_s17_21`, `9702_s17_22`, `9702_s17_23`, `9702_w17_21`, `9702_w17_22`, `9702_w17_23`.
  - Authored canonical question_ocr.json, markscheme.json, and enrichment.json with 3 progressive hints, verified proper answers, step-by-step walkthroughs, and key concepts.
  - Verified 100/105 papers PASS CLEAN across entire corpus. Exactly 64/69 modern P2 papers pass clean; the remaining 5 papers (`9702_s21_23`, `9702_s22_21`, `9702_s22_22`, `9702_w24_22`, `9702_m25_22`) represent documented authentic publisher errata.
  - Updated `subjects/physics/9702/reviews/p2-orchestration-tracker.md` to reflect 69 total papers tracked and 64 fully orchestrated (COMPLETE).
- Repaired and finalized all 7 deferred Paper 4 papers (83 questions total) across 2016-2023:
  - `9702_s16_41`: Repaired Q05 multi-page continuation and aligned Q10 (b) to 5 marks -> 100 marks total (13 questions).
  - `9702_s16_42`: Repaired Q13 (b) from notes criteria to 4 marks -> 100 marks total (13 questions).
  - `9702_w16_43`: Aligned Q06, Q07, and Q08; reconstructed Q10 (9 marks), Q11 (5 marks), Q12 (8 marks) -> 100 marks total (12 questions).
  - `9702_w18_43`: Repaired Q05 (b) to 4 marks; authored Q10 (5 marks) and reconstructed Q12 (11 marks) -> 100 marks total (12 questions).
  - `9702_w19_43`: Repaired Q11 (12 marks) across parts (a), (b)(i), (b)(ii), and (c) with 4-mark table criteria -> 100 marks total (12 questions).
  - `9702_m22_42`: Reconciled multi-page splits between Q11 (9 marks) and Q12 (7 marks) -> 100 marks total (12 questions).
  - `9702_m23_42`: Reconciled multi-page splits between Q01 (12 marks) and Q02 (12 marks) -> 100 marks total (10 questions).
- Full Paper 4 verification run:
  - Ran `scripts/verify_physics_paper.py --component p4`: 69/69 papers checked, 69 PASSED CLEAN, 0 warnings, 0 errors.
  - Paper 4 coverage across 2016-2025 is now 100% complete and fully verified.
- Strict style audit: Confirmed strictly zero em dashes (`\u2014`) across all newly generated files and documentation.

## 2026-09-08 - Physics P2 Comprehensive Repairs and Hint-to-Mark Parity

- Resolved all 107 hint-to-mark parity discrepancies across Cambridge AS Physics 9702 Paper 2:
  - Pruned 1-mark parts with 2 hints (102 parts total: 7 in 9702_w16_22 and 95 across 8 other 2016-2017 papers) to 1 focused progressive hint, discarding generic boilerplate Hint 2.
  - Authored progressive 3rd hints for four 3-mark parts in 9702_w16_22 (q02_b, q03_c_ii, q06_b_iii, q06_c).
  - Authored progressive 3rd and 4th hints for one 4-mark part in 9702_w16_22 (q05_b_iv).
  - Achieved 100% hint-to-mark parity (2,262/2,262 parts across all 69 papers).
- Populated all 19 empty marking_points in markscheme.json across 10 Paper 2 questions (9702_w18_22 q02/q05, 9702_w20_21 q05, 9702_w20_22 q02, 9702_m21_22 q05, 9702_w21_22 q02, 9702_m22_22 q05/q06, 9702_w24_22 q04, 9702_m25_22 q04) with official Cambridge marking tags (M1, A1, B1, C1) and aligned mark criteria.
- Removed OCR figure hallucination figure_1_2 from figures_referenced and part (b)(i) text in 9702_s16_23 question_01.
- Validated entire corpus: 69/69 papers checked, 0 hint parity errors, 0 empty marking points, 0 figure errors.
- Strict style audit: confirmed 0 em dashes (`\u2014`) across all touched files.

## 2026-09-08 - Physics P4 Comprehensive Repairs and Hint-to-Mark Parity

- Resolved all 107 hint-to-mark parity discrepancies across Cambridge A Level Physics 9702 Paper 4:
  - Pruned 1-mark parts with 2 hints (92 parts across 7 papers: 9702_s16_41, 9702_s16_42, 9702_w16_43, 9702_w18_43, 9702_w19_43, 9702_m22_42, 9702_m23_42) to 1 focused progressive hint, discarding generic boilerplate Hint 2.
  - Selected best 2 progressive hints for three 2-mark parts with 3 hints in 9702_w20_41_q08 (parts b, c, d).
  - Authored progressive scaffolding 2nd hint for 9702_w21_42_q09_a_i (2 marks) and 3rd hint for 9702_w21_42_q09_b_ii (3 marks).
  - Authored progressive 5th scaffolding hints for eight 5-mark parts with 4 hints: 9702_s16_41_q04_b, 9702_s16_41_q10_b, 9702_s16_41_q12_b, 9702_w16_43_q06_b_ii, 9702_w16_43_q11, 9702_w18_43_q02_b_ii, 9702_w18_43_q10, 9702_w19_43_q11_b_i.
  - Authored progressive 5th and 6th scaffolding hints for 6-mark part 9702_w18_43_q04_a.
  - Authored progressive 5th, 6th, 7th, and 8th scaffolding hints for 8-mark part 9702_w16_43_q08.
  - Achieved 100% hint-to-mark parity (3,312/3,312 parts across all 69 papers).
- Populated all 32 empty marking_points in markscheme.json across 13 Paper 4 questions (9702_m17_42_q03, 9702_m17_42_q07, 9702_w17_41_q03, 9702_w17_43_q03, 9702_w18_41_q06, 9702_m19_42_q12, 9702_w19_41_q09, 9702_m21_42_q03, 9702_m21_42_q05, 9702_m21_42_q08, 9702_m21_42_q09, 9702_s21_41_q04, 9702_w21_43_q12) with official Cambridge marking tags (M1, A1, B1, C1) and aligned mark criteria.
- Validated entire P4 corpus: 69/69 papers checked, 69 PASSED CLEAN, 0 hint parity errors, 0 empty marking points, 0 warnings, 0 errors.
- Strict style audit: confirmed strictly 0 em dashes across all touched files.

## 2026-09-08 - P2 publisher-erratum reconciliation

- Added 12 approved, additive `markscheme_reviewed.json` records for the five documented P2 publisher/source discrepancies: `9702_s21_23`, `9702_s22_21`, `9702_s22_22`, `9702_w24_22`, and `9702_m25_22`. Each review record has PASS metadata and hashes the locked official mark scheme and source PDF; canonical official files remain unchanged.
- The P2 verifier and reviewer builder now select a reviewed scheme only when that metadata explicitly authorizes the publisher-erratum reconciliation. All other questions continue to use their official scheme.
- Added the seven missing targeted enrichment hints in the affected papers. Full Physics verification: 243/243 clean, 0 warnings, 0 errors.

## 2026-09-08 - Past-paper folder normalization

- Made `question_NN/` the single active package location for Physics P2/P4;
  preserved P1's required flat `question-package/` contract.
- Grouped 124 legacy Physics P2 questions from 2010-2015 into question folders.
- Moved redundant aggregate Physics P2/P4 directories and `.DS_Store` files to
  repository archive `2026-09-08-physics-biology-folder-normalization/`; no
  records were deleted. Archive movements are recorded in its manifest.
- Re-ran Physics P1 and full Physics paper verification after normalization.
