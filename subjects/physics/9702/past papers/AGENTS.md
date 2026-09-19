# Physics Past Papers

Follow `../AGENTS.md`, then read `SESSION-LOG.md`.

This layer combines canonical extraction and additive enrichment by component,
year, examination session and variant.

- P1 paper leaves use one flat `question-package/` because each MCQ is already
  one complete PNG/TXT/JSON record plus its official answer.
- P2 and P4 paper leaves use one `question_NN/` directory per whole question.
  Store question OCR/text/images, official mark scheme, enrichment and their
  metadata as distinct files inside that directory.
- Do not recreate aggregate `parsed-questions/`, `questions/`, `mark-schemes/`
  or `enrichment/` siblings. Historical copies are preserved under repository
  archive `2026-09-08-physics-biology-folder-normalization/`.

- Preserve whole questions, stable IDs, dependencies and official mark schemes.
- Official mark-scheme JSON is immutable.
- P1 keeps one complete MCQ PNG, TXT and JSON plus the official answer.
- Keep `numerical_values_checked: false` unless separately authorized.
- Paper workflows live in `skills/`.

Record material changes in `SESSION-LOG.md`.
