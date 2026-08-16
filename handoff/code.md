# Code and Commands

Repository:

```bash
cd "/Users/abdullahaftab/Kognitiv/exam-paper-parser"
```

Open the prototype:

```bash
open "prototypes/2016-paper-22-renderer/index.html"
```

Rebuild its bundled question data after question JSON changes:

```bash
python3 prototypes/2016-paper-22-renderer/build_data.py
```

Validate one repaired question/mark-scheme pair:

```bash
python3 skills/repair-physics-p2-content/scripts/validate_pair.py \
  output/physics/p2/questions/9702_m16_qp_22/question_01.json \
  output/physics/p2/mark-schemes/9702_m16_ms_22/markscheme_01.json
```

Validate all six pairs:

```bash
for n in 01 02 03 04 05 06; do
  python3 skills/repair-physics-p2-content/scripts/validate_pair.py \
    "output/physics/p2/questions/9702_m16_qp_22/question_${n}.json" \
    "output/physics/p2/mark-schemes/9702_m16_ms_22/markscheme_${n}.json"
done
```

Check prototype JavaScript and whitespace errors:

```bash
node --check prototypes/2016-paper-22-renderer/app.js
git diff --check -- prototypes/2016-paper-22-renderer
```

Inspect only the active work without printing the repository's very large unrelated dirty state:

```bash
git status --short -- \
  input/physics/p2 \
  output/physics/p2/questions/9702_m16_qp_22 \
  output/physics/p2/mark-schemes/9702_m16_ms_22 \
  prototypes/2016-paper-22-renderer \
  skills/repair-physics-p2-content \
  handoff
```

## Current prototype behavior

- Renders all six 2016 Paper 22 questions from `paper-data.js`.
- Renders question stem, figures, part hierarchy, marks and response blocks.
- Supports text, quantity/unit and drawing-canvas responses present in the repaired JSON.
- Shows placeholder Mark scheme, Hints, Walkthrough, AI help and Check answer controls on each answerable part.
- Does not yet connect those controls to mark-scheme or enrichment data.
- Uses bundled KaTeX for stems, part text, mathematical field labels and units; no internet connection is required.

## Do not do automatically

- Do not clean the entire Git working tree.
- Do not commit unrelated deletions.
- Do not finalize the schema without user review.
- Do not add official answers to question JSON.
