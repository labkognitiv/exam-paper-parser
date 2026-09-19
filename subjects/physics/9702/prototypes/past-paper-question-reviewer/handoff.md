# Past-paper question reviewer handoff

Updated: 2026-09-05. Scope: this prototype only.

## Current state

- Question-player visual system reused for full-corpus review.
- Derived snapshot contains 2,437 questions and 523 diagram assets.
- P1, P3, M1 and S1 paper browsing is lazy-loaded by question.
- Hints, official marking and walkthrough are inspectable in original player tabs.
- Bottom review panel stores note plus Pass/Flag in `review-state.json` through a
  local persistence server; browser localStorage is only a fallback.
- First paper `9709_m25_12` is complete: Q1, Q2, Q3, Q6, Q7 and Q10 flagged
  with screenshot-transcribed notes; Q4, Q5, Q8, Q9 and Q11 passed.
- The six reported defects are fixed: Q1 wording, Q2/Q6 diagrams and aligned
  KaTeX rendering affecting Q3/Q7/Q10. Flags remain for user re-review.
- Thirty source-package notices are exposed in the interface, not repaired.
- Canonical Mathematics content remains read-only.

## Verification

- Data build completed.
- TypeScript, lint and production build passed.

## Known limit

- This is local-only. Run `npm run dev`; do not publish it through Sites.

## Update: 2026-09-06 (Physics 9702 Paper 2 Pipeline & Reviewer Integration)

- Integrated end-to-end Physics P2 digitizer and enrichment pipeline (`batch_paper_processor.py`).
- Added standalone captioned diagram extraction (`extract_question_figures`) and inline `{{figure:fig_X_Y}}` rendering with click-to-zoom in `MathText.tsx`.
- Guaranteed 100% answer prompt (`mass =`, `T =`, `percentage uncertainty =`) and SI unit (`%`, `N`, `m^3`, `J`, `s`) capture by feeding unmasked printable scans into Pass 1 OCR.
- Enforced verbatim Cambridge mark scheme criteria with official criterion tags (`[B1]`, `[M1]`, `[A1]`, `[C1]`), purging artificial summaries.
- Implemented stepped progressive teacher walkthroughs (`Step 1: ...`, `Step 2: ...`) with line-by-line intermediate arithmetic and an interactive "Reveal next step" control.
- Successfully verified on `9702_s22_22` (7 questions, 60 marks): total runtime 90.2s, total cost $0.017456 (~1.7 cents).
- Linked to prototype at `http://localhost:3002/?paper=9702_s22_22`. TypeScript (`tsc --noEmit`) and `oxlint` pass with zero errors.
