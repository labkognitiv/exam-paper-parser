# Mathematics 9709 — developer handover

## Contents

- `m1`, `p1`, `p3`, `s1`: each contains `knowledge/hierarchy.json` and `past papers/<year>/<paper>/paper.json`.
- Each paper has `questions/question_NN/`: `question.json`, `markscheme.json`, `enrichment.json`, and only its registered diagram files.
- `TOPIC_HIERARCHY.md`: readable view of the same component/topic/lesson hierarchy.
- `VALIDATION_MANIFEST.json`: counts, hashes and canonical source paths; audit metadata, not an upload dataset.

## Import and rendering

Import all four hierarchies before questions. Match stable topic/lesson IDs; module-like text inside historical IDs does not create a module level. Preserve question/part IDs, ordering, dependencies, content flow and figure placement. The 65 P1 vector parts intentionally link to the P3 hierarchy.

Enrichment v8 contains question ID, difficulty and parts. Each part has ID, difficulty, topic/lesson mapping, hints and one `walkthrough`. M1/S1 use their teacher walkthrough where present; three M1 parts retain their existing walkthrough. Skills, checking and practice tiers are absent. Render only `walkthrough`.

Use each question's figure records and references to place diagrams; do not glob PNG files or render a figure twice. Respect existing visibility/placement metadata. Question and mark-scheme JSON remain byte-identical to canonical content.

Paper metadata retains original/current marks, standard/suggested minutes and attempt availability. Questions default to available. `unavailable` blocks the question; `partially_available` blocks only `unavailable_part_ids`. Show `display_message` for blocked content. All questions remain included: 27 P1 vector questions are unavailable; 15 P3 plane questions are unavailable and 11 P3 questions are partially available. Other-topic syllabus review remains pending.

OCR, text/PDF/page-image companions, AI rubric, knowledge extras and internal review files are excluded. Structural/hash checks do not certify fresh mathematical review.
