---
name: verify-physics-mcq-web-rendering
description: Independently browser-render and verify every web-facing Markdown/LaTeX field in one complete merged Cambridge Physics 9702 Paper 1 MCQ CSV. Use after enrichment QC and the deterministic 40×36 merge, but before the release manifest, to catch CSV/JSON escaping, malformed math, missing delimiters, raw delimiters, renderer errors, or incomplete field coverage without reopening a released paper.
---

# Verify Physics MCQ Web Rendering

Run this read-only browser gate on exactly one merged paper CSV. Read [references/web-rendering-qc-contract.md](references/web-rendering-qc-contract.md) before running it.

## Workflow

1. Require all extraction, taxonomy, skill/rubric, difficulty/tier and enrichment QC gates to have passed.
2. Build the deterministic preview from the merged 36-column CSV:

   ```bash
   python3 scripts/build_web_render_preview.py \
     --merged /absolute/path/<paper_code>_Physics_P1_MC_Complete.csv \
     --paper-code <paper_code> \
     --output-dir /absolute/path/paper-root/web_render_qc
   ```

3. Load the bundled workspace dependencies to resolve the Node executable and `node_modules` directory. Browser-render the preview:

   ```bash
   /absolute/path/node scripts/run_web_render_qc.mjs \
     --html /absolute/path/paper-root/web_render_qc/web_render_preview.html \
     --merged /absolute/path/<paper_code>_Physics_P1_MC_Complete.csv \
     --paper-code <paper_code> \
     --node-modules /absolute/path/node_modules \
     --output-dir /absolute/path/paper-root/web_render_qc
   ```

4. Inspect the full screenshot and focused screenshots for every row with mathematical notation. Compare representative complex notation with the original QP; retain extraction QC as the row-by-row source-fidelity authority.
5. Stop unless `qc_manifest.json` reports `final_status=passed`, the merged hash matches, all expected inline spans produced KaTeX nodes, and browser/raw-delimiter/error counts are zero.
6. Pass this manifest to the release validator. Never repair extraction or enrichment from this QC skill; route failures to the owning upstream skill and rerun its QC before repeating this gate.

## Boundary

- Do not edit the merged CSV, stage CSVs, source PDFs, visuals, mapping, skill registry, difficulty, or tier decisions.
- Do not create lessons, hints, solutions, uploads, or app/database changes.
- Keep the generated HTML, full screenshot, focused row screenshots and hash-bound manifest inside `web_render_qc/` as paper-local release evidence.
