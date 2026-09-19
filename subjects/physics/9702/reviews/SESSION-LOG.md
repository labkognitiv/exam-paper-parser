# Physics reviews session log

Append concise dated handoffs. Do not rewrite previous entries.

Each entry should state the bounded task, material changes, verification, and the next unresolved action.

## 2026-09-19 — Whole-question primary-lesson pilot

- Added an evidence-only Muse Spark pilot for one AS P2 paper (`9702_m22_22`) and one A2 P4 paper (`9702_m22_42`): all 19 questions received exactly one active primary lesson, no secondary lessons, and unchanged resolved part evidence.
- Manual source and mark-scheme review accepted P2 7/7 and P4 12/12; each selected lesson derives its parent topic correctly. One P2 image request required a candidate-mark fallback after blank provider responses. Canonical papers and enrichment were unchanged.
- Pilot evidence and review live in `question-primary-lesson-pilot/`; scaling to the remaining papers is not yet authorised.

## 2026-09-19 — Full P2/P4 whole-question primary-lesson mapping

- Added resumable evidence-only mappings under `question-primary-lesson-mapping/` for all 476 P2/AS and 780 P4/A2 questions. Each has one active primary lesson, an automatically derived parent topic, no secondary lessons and unchanged contextual part-level evidence.
- Muse Spark produced 1,177 mappings; 19 accepted pilot records were reused. Sixty persistent blank/malformed provider responses were finalized using the recorded, low-confidence highest-resolved-part-mark fallback. Active lesson, candidate-membership and derived-topic checks pass for all 1,256 records.
- Canonical questions, enrichment, stable IDs, mark schemes and numerical checks were unchanged. See `question-primary-lesson-mapping/manual-review.md` for audit and provider-cost evidence.

## 2026-09-10 — Muse lesson-mapping evidence

- Added derived, resumable P2/AS and P4/A2 Muse mapping evidence only under the six `*-mapping-{candidates,second-pass,contextual-resolution}` review directories; canonical packages and official mark schemes were unchanged.
- P2 resolved 2,260 unique positive-mark parts across 69 papers. P4 resolved 3,313 across 69 papers after excluding one zero-mark stem and normalising three duplicate mark-scheme records in the derived loader.
- Strict active-lesson/redirect/schema/per-paper validation passed for all 138 resolved candidates; no remaining marked nulls. No unresolved action.

## 2026-08-31 — Complete P2 manual review inventory

- Added `p2/P2_QUESTION_REVIEW_TRACKER.md` with 600 canonical P2 paper rows and
  539 topical lesson-question rows.
- Defined PASS as a completed human review of source, marking, mapping, hints,
  walkthrough, checks, rubric, alternatives and dependencies.
- All 1,139 rows begin `NOT REVIEWED`; 3,169 linked files resolve.

## 2026-08-31 — P2 tracker split

- Separated the 600 past-paper rows into `p2/P2_PAST_PAPER_TRACKER.md` and the
  539 topical rows into `p2/P2_TOPICAL_TRACKER.md`.
- Kept the old combined filename as a pointer only, preventing duplicate status
  ownership. All statuses, notes and working links were preserved.

## 2026-09-05 — Mathematics-aligned hierarchy

- Renamed the active quality boundary to `reviews/`, retaining reviews, evidence,
  benchmarks and unresolved states.
- Moved verification workflows into `reviews/skills/`.

## 2026-09-08 — P2 2024 unrestricted verification

- Ran all seven 2024 P2 papers concurrently, with all questions concurrent per paper: six PASS, one immutable-source blocker.
- `9702_w24_22` remains blocked: Q4 canonical question total 8 versus official mark-scheme total 10 (extra `(u)` 2); Q6 question total 11 versus mark-scheme total 9 (`(c)(i)` 3 versus 1). No canonical or official record changed; reviewer data was not rebuilt.

## 2026-09-08 — P2 2023 unrestricted verification

- All seven 2023 P2 papers passed source-grounded review and deterministic verification; derived reviewer data was rebuilt only after that complete pass.

## 2026-09-08 — P2 2022 unrestricted verification

- Seven papers ran concurrently: four PASS; three immutable canonical-source blockers. `s22_21` Q2 is 10/8; `s22_22` Q2 has a duplicate canonical `(d)(ii)` zero-mark record where the source-derived artifact exposes `(d)(iii)`; `s22_23` Q6 is 11/7 and Q7 7/4. No canonical or official file changed; no reviewer rebuild.

## 2026-09-08 — P2 2021 unrestricted verification

- Six of seven papers passed. `9702_s21_23` is blocked by immutable zero-mark canonical mark schemes for Q1-Q6 against question totals 11, 11, 10, 8, 11 and 9; no source edit or rebuild.

## 2026-09-08 — P2 2020 unrestricted verification

- All four selected 2020 papers passed source-grounded review and deterministic verification; derived reviewer data rebuilt after the full-year pass.

## 2026-09-08 — P2 2019 unrestricted verification

- All seven selected 2019 papers passed source-grounded review and deterministic verification; derived reviewer data rebuilt after the full-year pass.
