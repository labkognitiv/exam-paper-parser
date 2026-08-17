# Question enrichment

- `p1/`: one JSON file per MCQ, named `<question_id>.enrichment.json`.
- `p2/`: one JSON file per complete structured question, named `<question_id>.enrichment.json`.

Each file contains question-level taxonomy and difficulty plus one record per answerable question/part. P1 uses the question ID as its single part ID.

Checking modes:

- `deterministic`: the submitted answer can be checked without AI.
- `ai`: the response requires semantic marking against criterion observables.
- `hybrid`: check the final answer deterministically first; a correct final answer receives full block marks. If it is incorrect and working is present, AI may award partial marks from the rubric.
