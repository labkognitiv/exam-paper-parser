---
name: repair-physics-p4-paper-knowledge-base
description: Repair an existing Physics 9702 Paper 4 knowledge-base paper from independent review findings without re-authoring or self-certifying the paper.
---

# Repair Physics P4 Paper Knowledge Base

Use this skill only after an existing P4 paper has concrete verifier, auditor, deterministic, rendering or human-review findings. Do not use it for first-pass paper creation and do not treat an author summary as a defect list.

## Canonical repository root

Run from the repository root resolved by `git rev-parse --show-toplevel`.
Before inspecting or editing artifacts, run `pwd` and require it to equal that
resolved root. Refuse a different checkout or worktree unless the user explicitly
names it.

Require `.venv/bin/python`, the paper's original question PDF and original mark-scheme PDF in the canonical root. Print the resolved root in the first progress update and final report.

## Separation of duties

The repair agent owns only the repair. It must not issue verifier, external-auditor or release PASS evidence for its own changes.

- Start from the independent review report and current executable audit output.
- Repair only affected canonical questions, enrichment leaves or controlled registry records.
- Preserve unrelated correct content and unrelated dirty-worktree changes.
- After repair, hand the changed units to fresh agents using `$verify-physics-p4-paper-knowledge-base` for question-verifier and external-auditor review.
- A deterministic PASS proves structural consistency, not semantic correctness.

## Immutable and controlled invariants

- Never edit official mark-scheme JSON. Verify it against the initial source ledger before and after repair.
- Keep `numerical_values_checked: false`.
- Preserve original-PDF identity, complete structured-question context, figures and dependency graph.
- Preserve exact official occurrences, dependencies, alternatives and `Any N from M` rules.
- Root topic, module and outcome lists use leaf-first-occurrence order.
- Automatic full credit remains forbidden for multi-mark calculations with method, working or explanation credit.
- Every deterministic `field_id` must character-match a canonical response field.

## Repair loop

1. Read the complete independent review and turn every finding into a checkable item grouped by question and leaf.
2. Run the current question audit before editing and retain its actual output as the baseline.
3. Open the original question PDF page, original mark-scheme PDF page, canonical question, figures, immutable official criteria, enrichment and every referenced registry record.
4. If the paper was previously closed or released, use `manage_p4_workflow.py reopen` for the earliest affected question or leaf. Never edit workflow state or gate events directly.
5. Repair one affected question and one leaf at a time. Do not rewrite unaffected leaves for style.
6. Reread the saved file from disk and compare it against the finding, source and official criteria. Do not approve from an edit summary.
7. Run the question audit with `--check-git`; repair every failure before continuing.
8. Re-run the review checklist. A finding closes only when its exact bad value, wording or structure is absent and the correct replacement is present.
9. After all affected units pass, run the full structured-paper audit and immutable-hash checks.
10. Require fresh independent question-verifier and external-auditor reports for every changed question before release.

## Mandatory corruption scan

After any JSON text repair, parse every changed enrichment file and recursively scan all string values for:

- tab, form-feed, carriage-return and backspace control characters;
- shell-expansion debris such as `/bin/zsh`, `/bin/bash`, `569X` or substituted environment values;
- damaged LaTeX commands where `\\times`, `\\text`, `\\frac`, `\\right`, `\\left` or variables disappeared;
- unbalanced `$` delimiters and mathematically incomplete fragments;
- dropped leading digits, signs, variables or units.

Write LaTeX in JSON with JSON-safe escaped backslashes. Never use shell interpolation to construct mathematical JSON strings. Use `apply_patch` for manual repairs.

The corruption scan is a hard gate even when `audit_structured_question.py` reports PASS.

## Required commands

For every changed question:

```bash
.venv/bin/python scripts/audit_structured_question.py \
  --component P4 --paper <paper> --question <n> --check-git
```

For the whole paper:

```bash
.venv/bin/python scripts/audit_structured_paper.py --component P4 --paper <paper>
.venv/bin/python scripts/manage_p4_workflow.py --paper <paper> status
```

The workflow status must reflect the new file hashes and fresh independent evidence. A stale `COMPLETE` state is not a valid release.

## Handoff

Report only:

- canonical repository root and paper code;
- exact review findings repaired and files changed;
- corruption-scan result;
- affected-question and whole-paper deterministic results;
- official hash and numerical-flag results;
- questions requiring fresh independent verification;
- remaining blockers.

Do not claim `RELEASE PASS` until the executable manager accepts fresh independent evidence for every changed question.
