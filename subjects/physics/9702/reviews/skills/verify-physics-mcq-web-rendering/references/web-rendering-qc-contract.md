# Physics P1 MCQ web-rendering QC contract

## Placement

Run after final enrichment QC and after `merge_paper_csv.py`, before `pipeline_release_manifest.json`. Early validators still own notation correctness at authoring time:

- extraction validator and independent extraction QC: `question_text`, `option_a`–`option_d`;
- skill/rubric validator and independent QC: every `ai_rubric` JSON value;
- difficulty/tier validator and independent QC: `reason`;
- this gate: final integration, CSV/JSON escaping and actual browser rendering across all fields together.

## Input

The input is the single complete 40-row, 36-column paper CSV. Web-facing fields are:

- `question_text`;
- `option_a`, `option_b`, `option_c`, `option_d`;
- every JSON value inside `ai_rubric` (keys are stable skill identifiers and are not rendered as mathematical content);
- `reason`.

## Required evidence

`web_render_qc/` must contain:

- `web_render_preview.html`;
- `web_render_preview.png`;
- one `rows/<question_id>.png` screenshot for every row containing `$...$`;
- `preview_build.json`;
- `qc_manifest.json` bound to the merged CSV SHA-256.

## Pass conditions

- Exactly 40 unique question IDs and the required web fields are present.
- `ai_rubric` parses to a non-empty JSON object whose values are strings.
- Every source `$...$` span creates one KaTeX node.
- No raw `$` remains in visible browser text.
- No `.katex-error`, browser page error, failed render, blank required field, or row-coverage mismatch exists.
- The manifest records `final_status=passed`, `renderer=KaTeX auto-render`, row count, rows with math, expected/rendered span counts, error counts and the exact merged hash.

This is rendering QC, not source-authority QC. Source fidelity remains established against the original QP by independent extraction verification.
