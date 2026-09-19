---
name: run-physics-mcq-paper-pipeline
description: Orchestrate and execute the complete Cambridge AS Physics 9702 Paper 1 (MCQ) enrichment pipeline. Spawns an Author Subagent to generate flat enrichment records question-by-question, monitors execution, and runs automated deterministic validation with concise caveman communication.
---

# Run Physics MCQ Paper Pipeline

Orchestrate the end-to-end authoring and validation for one full Cambridge AS Physics 9702 Paper 1 (40 MCQs).

## Operating Rules

- **Execution Model**: Active two-tier architecture.
  1. Spawn a dedicated **Author Subagent (Gemini Flash)** to author the 40 MCQs.
  2. The **Parent Agent** actively monitors and audits using `scripts/validate_p1_enrichment.py`.
- **Communication Style**: Caveman language only. On success, output concise status (`PASS: [PAPER_CODE] (40/40 MCQs valid)`). On failure, output explicit error details.
- **Source Immutability**: Question files in `subjects/physics/9702/papers/p1/[PAPER_CODE]_qp_*/` are strictly immutable.
- **Preflight SHA-256**: Hash all 40 question JSONs before work and verify invariance upon completion.

---

## Workflow

1. **Preflight**:
   - Compute SHA-256 hashes of all 40 `question_*.json` files.
   - Confirm `answer_key.json` exists with 40 answers.

2. **Authoring (via Subagent)**:
   - For each question:
     - Read `question_XX.json` (text-first).
     - If `has_visual_content: true` or diagram/graph/circuit referenced, view `question_XX.png`.
     - Output flat enrichment JSON to `subjects/physics/9702/enrichment/p1/[PAPER_CODE]_qXX.enrichment.json`.

3. **Deterministic Validation**:
   - Run `.venv/bin/python scripts/validate_p1_enrichment.py --paper [PAPER_CODE] --json`.
   - Ensure 40/40 questions pass with 0 deterministic errors.

4. **Independent Audit**:
   - Invoke `verify-physics-mcq-enrichment` to audit the paper.
