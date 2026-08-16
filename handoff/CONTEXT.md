# Current Context

## Goal

Develop a reliable Cambridge AS Physics 9702 P1/P2 content and knowledge pipeline:

1. Deterministic parser extracts complete question images, text, figures and initial structured JSON.
2. AI repair layer compares the complete question image with parser output, repairs symbols/LaTeX/structure/figure links/answer controls, checks that no content is missing and reconciles marks.
3. Canonical question and mark-scheme files become stable sources for enrichment, taxonomy, curriculum mapping, recommendations and grading.
4. Build one syllabus-controlled, past-paper-grounded taxonomy and knowledge base shared by P1 and P2.

The current transition is from completed corpus repair into taxonomy and knowledge-base design. Downstream lesson, revision and generation products are not yet designed or production-gated.

## Three-file architecture

1. Question file: question content, hierarchy, stable IDs, figures, marks, response UI schema and input validation format.
2. Mark-scheme file: official Cambridge marking instructions and accepted answers.
3. Enrichment file: controlled concepts/skills, difficulty, progressive hints, connected worked solution/walkthrough, AI rubric, checking mode and deterministic evaluator configuration derived from the mark scheme.

Static canonical files must remain separate from student attempts, mastery, timing and planner state.

## Active source files

- Forward-tested paper: `output/physics/p2/questions/9702_s16_qp_21/` and `output/physics/p2/mark-schemes/9702_s16_ms_21/`
- Questions: `output/physics/p2/questions/9702_m16_qp_22/question_01.json` through `question_06.json`
- Mark schemes: `output/physics/p2/mark-schemes/9702_m16_ms_22/markscheme_01.json` through `markscheme_06.json`
- Question images and figure crops live beside the question JSON files.
- Q5 recovered graph: `output/physics/p2/questions/9702_m16_qp_22/figure_5_2.png`

## Prototype

Open: `prototypes/2016-paper-22-renderer/index.html`

Files:

- `index.html`: student-view shell
- `styles.css`: visual presentation
- `app.js`: question/part/figure/response rendering and placeholder actions
- `build_data.py`: bundles repaired question JSON into browser data
- `paper-data.js`: generated browser data

The complete question image is no longer shown to the student. It remains an internal AI/human verification source. The prototype renders the stem, figures, parts, marks and response controls from structured data.

The prototype now bundles KaTeX locally under `vendor/katex/`, works through `file://`, renders normalized LaTeX fields, and falls back to readable plain Unicode text.

## Known architecture issue

The current JSON is mostly flat. It has `question_stem`, flat `question_text`, parts and figures with `introduced_by`, but it does not always encode precise interleaving inside a parent context. Examples include prose → figure → more prose and multiple figures between prose segments. The final question schema probably needs ordered content blocks or a render flow. Do not finalize or implement this without discussing it first.

## User preferences and boundaries

- Keep chat responses extremely precise and brief unless detail is requested.
- Ask before broad or materially different work.
- Do not process additional papers/questions without approval.
- Do not consult original PDFs unless requested for the relevant task; complete extracted question images are the normal repair/QC reference.
- Treat mark-scheme alternatives as alternative routes, not extra marks.
- Do not claim exploratory artifacts are official or production-approved.
- Do not create formal PASS evidence without the required gates.
- For taxonomy brainstorming, respond in precise, strict bullets and develop the design interactively. Give long comprehensive responses only when requested.
