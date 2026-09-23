# Mathematics 9709 sandbox import

**Development only. Do not use this bundle for production.**

Each of `m1/`, `s1/`, `p3/` and `p1/` contains:

- `curriculum.json`: topic → module → lesson IDs, names, order and relative paths to lesson HTML and original practice files.
- `past-papers/<year>/<paper_code>/question_NN/`: question, mark scheme, enrichment, three standard images and referenced diagrams.
- `study/<topic_id>/<module_id>/<lesson_id>/`: original practice JSON and lesson HTML with its local assets and figures.
- `knowledge/`: controlled labels referenced by enrichment IDs.

Import from these four component folders. Keep IDs unchanged. `manifest.json` lists every copied file, SHA-256 hash and all **403 test substitutions**: 149 HTML copies, 212 SVG figures, 29 missing enrichment files and 13 existing enrichments supplemented with placeholder parts. Every test item has `replace_before_final_upload: true`. The originals under `../study/`, `../past papers/` and `../knowledge/` remain untouched.

The four `curriculum.json` files hold only the lesson hierarchy. Paths in a component curriculum are relative to that component's folder. For past-paper classification, read each question's `enrichment.json` `parts[].mapping` (`topic_id`, `module_id`, `lesson_id`). Original practice questions belong to the lesson package that contains them. Do not infer or copy question mappings into the hierarchy files. Test enrichment classifications remain temporary and must be replaced before the final upload.

`BASELINE.md` records the pre-export source inventory. Reviewer data, review decisions, logs, scripts, source PDFs and lesson PDFs are outside the import package. The final upload requires all 403 test substitutions to be replaced, followed by a fresh manifest and verification.

The Git handoff also excludes 155 zero-byte macOS `Icon` metadata files found in copied HTML font directories; they are not website assets.
