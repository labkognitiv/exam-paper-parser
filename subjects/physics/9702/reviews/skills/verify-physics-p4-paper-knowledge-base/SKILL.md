---
name: verify-physics-p4-paper-knowledge-base
description: Independently verify one Physics 9702 Paper 4 knowledge-base paper leaf by leaf against canonical prompts, figures, immutable official criteria, taxonomy, skills, hints, walkthroughs and checking rules.
---

# Verify Physics P4 Paper Knowledge Base

Act as one fresh read-only per-question agent in the role assigned by the manager: `question_verifier` or `external_auditor`. Do not trust author summaries or earlier PASS results.

The question verifier is the third judgment layer. The external auditor is a fourth, different agent and receives no question-verifier conclusions. Neither agent may have authored or managed the question. Give only paper code, question number and repository paths.

Write the result using `subjects/physics/9702/knowledge/contracts/p4-question-review-report.schema.json`. Enumerate every leaf separately for general, physics, hint and rubric review; enumerate every referenced registry ID; cite original question and mark-scheme PDF pages. A PASS report contains zero findings. The manager submits it through the command matching the assigned role.

## Manual pass first

Review every answerable leaf in the assigned question. Open its original question-paper PDF page, original mark-scheme PDF page, parent context, figures, official marking points, full outcome/skill/definition/formula records, hints, walkthrough and checking object.

Make explicit judgments for:

- prompt and figure context understood correctly;
- physics, calculation, sign, unit and explanation truth;
- topic, module and outcome precision;
- narrow reusable skill scope;
- hint progression without giveaway;
- complete teacher-style walkthrough;
- safe `ai`, `hybrid` or `deterministic` checking mode; `full_marks_if_all_deterministic_checks_pass` is allowed only when deterministic checks cover 100% of official credit (forbidden on multi-mark calculations with intermediate method marks);
- character-exact `field_id` matches between `deterministic_checks` and the canonical question's `response_schema.blocks`;
- exact official criteria, full coverage of all alternative (`OR`) branches, dependencies and occurrences.

`deterministic` is allowed only when structured checks cover the complete credited answer. `hybrid` requires both machine-checkable and semantic credit.

## Deterministic pass second

After the complete manual pass, run:

```bash
.venv/bin/python scripts/audit_structured_question.py --component P4 --paper <paper> --question <n> --check-git
```

Deterministic failures cannot be waived. Confirm `numerical_values_checked: false`, exact first-occurrence ordered unions, AS+A2 registry resolution, canonical hashes and official hashes.

Run `.venv/bin/python scripts/manage_p4_workflow.py --paper <paper> status`. The command verifies official hashes against the initial ledger before returning state. A missing or stale ledger is a failure.

## Verdict

Return `PASS` only with zero deterministic failures and zero open semantic findings. Return a short leaf/field defect list otherwise. Do not edit files. Official mark-scheme JSON is immutable.

On failure, hand findings back through `reopen`. Every affected gate must be regained, and both independent per-question agents must restart from primary artifacts. The next question remains locked.
