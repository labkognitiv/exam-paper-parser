---
name: verify-physics-mcq-enrichment
description: Independently audit and verify Cambridge AS Physics 9702 Paper 1 (MCQ) enrichment records. Performs read-only deterministic checks on answer keys, taxonomy hierarchy, LaTeX formatting, and source hash invariance without relying on author conclusions.
---

# Verify Physics MCQ Enrichment

Perform an independent, read-only audit on one or more Cambridge AS Physics 9702 Paper 1 enrichment packages.

## Audit Criteria

1. **Exact Question Count**: Exactly 40 questions present, 0 missing, 0 duplicates.
2. **Answer Parity**: 100% agreement between `accepted_answer` and official `correct_answer` in `question_*.json` and `answer_key.json`.
3. **Taxonomy & Hierarchy**:
   - `topic_id` exists in `9702-2025-2027-as-taxonomy.json`.
   - `module_id` exists and is a valid child of the assigned `topic_id`.
4. **Controlled Skills & Patterns**:
   - `skill_id` resolves in `skills.json`.
   - `question_patterns` resolve in `question-patterns.json`.
5. **Instructional Quality**:
   - $\ge 2$ progressive, non-generic hints per MCQ without direct answer giveaways.
   - $\ge 2$ structured walkthrough steps explaining the physical basis and distractor diagnosis.
6. **Text & LaTeX Integrity**:
   - 0 corrupt unicode characters (`�`).
   - 0 unescaped control characters.
   - Balanced math delimiters (`$ ... $`).
   - 0 shell PID expansion artifacts (`2053612345`).
7. **Source File Invariance**: Preflight SHA-256 hashes match byte-for-byte.

---

## Verification Command

```bash
.venv/bin/python scripts/validate_p1_enrichment.py --paper [PAPER_CODE] --json
```

## Output Format (Caveman)

- On PASS:
```
PASS: [PAPER_CODE] (40/40 MCQs valid)
```
- On FAIL:
```
FAIL: [PAPER_CODE]
  - [filename]: [error description]
```
