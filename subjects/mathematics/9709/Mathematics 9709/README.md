# Mathematics 9709 — developer handover

## Contents

- `m1`, `p1`, `p3`, `s1`: each contains `knowledge/hierarchy.json` and `past papers/<year>/<paper>/paper.json`.
- Each paper has `questions/question_NN/`: `question.json`, `markscheme.json`, `enrichment.json`, and only its registered diagram files.
- `TOPIC_HIERARCHY.md`: readable view of the same component/topic/lesson hierarchy.
- `VALIDATION_MANIFEST.json`: counts, hashes and canonical source paths; audit metadata, not an upload dataset.
- `schemas/`: JSON Schemas (Draft 2020-12) for `question.json`, `markscheme.json` and `enrichment.json`. One set covers past-paper and lesson questions; every question file in this folder validates against it.

## Import and rendering

Import all four hierarchies before questions. Match stable topic/lesson IDs; module-like text inside historical IDs does not create a module level. Preserve question/part IDs, ordering, dependencies, content flow and figure placement. The 65 P1 vector parts intentionally link to the P3 hierarchy.

Enrichment v8 contains question ID, difficulty and parts. Each part has ID, difficulty, topic/lesson mapping, hints and one `walkthrough`. M1/S1 use their teacher walkthrough where present; three M1 parts retain their existing walkthrough. Skills, checking and practice tiers are absent. Render only `walkthrough`.

Use each question's figure records and references to place diagrams; do not glob PNG files or render a figure twice. Respect existing visibility/placement metadata. Question and mark-scheme JSON remain byte-identical to canonical content.

Paper metadata retains original/current marks, standard/suggested minutes and attempt availability. Questions default to available. `unavailable` blocks the question; `partially_available` blocks only `unavailable_part_ids`. Show `display_message` for blocked content. All questions remain included: 27 P1 vector questions are unavailable; 15 P3 plane questions are unavailable and 11 P3 questions are partially available. Other-topic syllabus review remains pending.

OCR, text/PDF/page-image companions, AI rubric, knowledge extras and internal review files are excluded. Structural/hash checks do not certify fresh mathematical review.

## Study

- `study/<component>/<topic>/<mNN_lNN>/`: one folder per lesson. So far P1 Coordinate Geometry (11 lessons, 143 practice questions). The lesson ID is `9709_<component>_t_<topic>_<mNN_lNN>` (e.g. `9709_p1_t_coordinate_geometry_m01_l01`), and every JSON carries the full ID; `mNN_lNN` is an opaque ID segment, not a module.
- `lesson.json` is the lesson's equivalent of `paper.json`: lesson and topic IDs, title and order (as in `p1/knowledge/hierarchy.json`), total marks and the ordered question list.
- `slides/index.html` is the lesson deck. Decks load the shared kit from `study/lesson-ui/slides/` (`deck.css`, `engine.js`, `deck.js`, `interact.js`) and link to the previous/next lesson.
- `questions/question_NN/` uses the same structure as past-paper questions (`question.json`, `markscheme.json`, `enrichment.json` v8, registered figure PNGs), with `lesson_id`/`topic_id` in place of the paper fields (`paper_code`, `year`, `session`, `variant`; mark schemes have no `source`). Mark-scheme parts may also carry `accepted_alternatives` and `tolerance`.
- Difficulty is 1–5 for each part; the question's difficulty is its highest part. Every part maps to its own lesson.
- Figures are registered in `question.json` `figures` with `sha256` and placed after the stem; parts list them in `figure_ids`. Render from those records only.
