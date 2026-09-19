---
name: verify-physics-mcq-source-package
description: Independently verify the original source package for exactly one Cambridge Physics 9702 Paper 1 MCQ paper before extraction. Use after downloading the question paper and official mark scheme or answer key. Checks paper identity, component, session, variant, PDF integrity, completeness, official answer-key presence, hashes, and forbidden archive/cutout sources. Produces a read-only source QC manifest and never extracts questions or edits PDFs.
---

# Verify Physics MCQ Source Package

Verify one paper before extraction. Original PDFs are the only authority.

## Workflow

1. Resolve the expected paper code and exactly one original QP plus one official MS/answer-key PDF.
2. Reject files under `_archive`, cutout, crop, image, or derivative folders.
3. Inspect both PDFs. Confirm subject `9702`, Paper 1 MCQ, session/year, component variant, complete question pages, and an official 40-answer key.
4. Write `source_qc/source_review.json` using [references/source-qc-contract.md](references/source-qc-contract.md).
5. Run:

   ```bash
   python3 scripts/validate_source_package.py \
     --paper-code 9702_m16_12 \
     --qp /absolute/path/9702_m16_qp_12.pdf \
     --ms /absolute/path/9702_m16_ms_12.pdf \
     --review /absolute/path/source_qc/source_review.json \
     --output /absolute/path/source_qc/qc_manifest.json
   ```

Stop unless `final_status=passed`. Never create extraction rows, visuals, topics, skills, tiers, lessons, or solutions.

