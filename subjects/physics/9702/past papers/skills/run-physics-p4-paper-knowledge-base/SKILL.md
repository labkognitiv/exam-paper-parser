---
name: run-physics-p4-paper-knowledge-base
description: Fully orchestrate one Physics 9702 Paper 4 paper from a paper code through source-image verification, canonical repair, enrichment, deterministic audits, independent verification, repair loops and release.
---

# Run Physics P4 Paper Knowledge Base

The user supplies only a paper code such as `9702_m18_42`. Start automatically. Do not ask the user to restate paths, stages, checks or commands when repository evidence can resolve them.

## Canonical repository root

Run the workflow from the repository root resolved by
`git rev-parse --show-toplevel`.

Before reading or changing paper artifacts:

1. Run `pwd` and `git rev-parse --show-toplevel`.
2. Require `pwd` to equal the resolved Git root.
3. Run all relative commands with that directory as the working directory.
4. Print the resolved root in the first progress update and final report.
5. Refuse a different checkout or worktree unless the user explicitly names it for the run.
6. Before accepting existing or newly written artifacts, require `.venv/bin/python`, the paper's primary question PDF and primary mark-scheme PDF inside this canonical root.

Do not infer that files are missing or stale from another checkout. If an artifact appears absent, first restate the resolved root and check its absolute canonical-root path.

Invocation authorizes in-scope creation and repair of that paper's compact source package, canonical questions, enrichment, evidence and derived reviewer data. It never authorizes editing official mark-scheme JSON, unrelated papers or unrelated worktree files.

## Required reads

Read repository instructions and these skills completely:

- `$compact-cambridge-p4-question-paper`
- `$create-physics-p4-paper-knowledge-base`
- `$verify-physics-p4-paper-knowledge-base`

Resolve all paths from the paper code and repository conventions.

## Manager-author operation

The root agent is the manager. This skill explicitly authorizes exactly one persistent author agent for the paper. After each question closes, create one fresh question-verifier agent and then a different fresh external-auditor agent for that question.

- The author handles one question and one answerable leaf at a time. Do not split leaves or questions across parallel authors.
- Before work starts, both manager and author independently open the complete question context: source image, canonical question, all figures and placements, immutable official criteria, enrichment, taxonomy and referenced registries.
- The author makes the in-scope repair. The manager then reopens the primary context, inspects the actual diff and runs the relevant checks. Never approve from the author's summary alone.
- The manager returns a precise defect list to the same author until the unit passes. Do not advance while any defect remains.
- Required sequence is `QUESTION PASS`, `LEAF PASS` for every leaf, `QUESTION CLOSEOUT PASS`, `QUESTION VERIFIER PASS`, then `QUESTION EXTERNAL AUDITOR PASS`. The next question stays locked until the full sequence passes.
- If delegation is unavailable, perform the same author/manager phases sequentially with a clean reread between them; do not collapse creation and approval into one judgment.

## Executable progression gate

The repository program owns workflow state. Skills and agent-written PASS text never unlock work. After compact source preparation is complete, initialize once:

```bash
.venv/bin/python scripts/manage_p4_workflow.py --paper <paper> init
```

When the user explicitly requests one question only, use `init --only-question <n>`. Do not let defects in unrelated questions block a question-scoped run. The scoped run still hashes and protects the complete official-file inventory.

Run `status` before every assignment. Advance only with `approve-canonical`, `approve-leaf`, `close-question`, `approve-question-verifier`, `approve-question-auditor`, and `release`. A non-zero exit is a hard stop. Never edit workflow state or gate events by hand. Never run extraction, compacting, official conversion or bulk-paper author scripts after initialization.

## Automatic run

1. Inventory the question paper, canonical questions, figures, official mark schemes, enrichment, registries and existing evidence.
2. Verify total paper marks sum to exactly 100. If raw parsed JSONs sum to less than 100, inspect the primary PDF to recover missing marks/subparts during canonical repair before creating the initial source ledger.
3. If valid `IMAGE PASS` evidence is absent or stale, run the compact P4 source-image workflow first. Do not confuse image PASS with knowledge-base PASS.
4. Run `manage_p4_workflow.py --paper <paper> init`. It creates the immutable ledger and locked workflow state under `subjects/physics/9702/evidence/p4/<paper>/`.
5. Run `$create-physics-p4-paper-knowledge-base` through the executable manager-author loop. For each question, obtain `QUESTION PASS`, approve exactly one leaf at a time, and obtain `QUESTION CLOSEOUT PASS`.
6. At every leaf gate, run the applicable enrichment validator and question audit via `.venv/bin/python`. At every question closeout, rerun `.venv/bin/python scripts/validate_question_enrichment.py` and `.venv/bin/python scripts/audit_structured_question.py` for the complete question. Repair every failure through the owning layer.
7. Run `.venv/bin/python scripts/audit_structured_paper.py --component P4 --paper <paper>`. Resolve inventory, hierarchy, marks, figures, response schemas, taxonomy, ordered unions, checking modes, deterministic fields and occurrence-aware official bindings. This is the paper-level deterministic gate, not a substitute for manager approval.
8. The manager verifies official hashes at every command and locks each canonical question hash at `QUESTION PASS`. Official changes always fail; canonical changes after manager approval also fail.
9. For that question, run `$verify-physics-p4-paper-knowledge-base` as a fresh `question_verifier`, submit its detailed report with `approve-question-verifier`, then run it again as a different fresh `external_auditor` receiving no prior conclusions. Submit with `approve-question-auditor`.
10. Return either agent's failures with `reopen --question <n> [--leaf <part_id>] --manager-review '<finding>'`. Require author repair, manager reapproval and two new independent agents. Only after both pass may the next question unlock.
11. After every selected question has both independent passes, run `release`. Rebuild derived data only after `RELEASE PASS`.

Track these separately:

- `IMAGE PASS`
- `QUESTION PASS`
- `ENRICHMENT PASS`
- `QUESTION VERIFIER PASS`
- `QUESTION EXTERNAL AUDITOR PASS`
- `RELEASE PASS`

The verification layers are: original-PDF evidence, source ledger, canonical manager gate, per-leaf manager gate, question closeout, per-question verifier, per-question external auditor, whole-paper deterministic audit and release. Every layer is required.

## Hard rules

- Never edit official mark-scheme JSON.
- Keep `numerical_values_checked: false`.
- Preserve whole structured questions and their dependency graph.
- Root lists use leaf-first-occurrence order, never set or sorted equality.
- A script PASS never replaces the manual leaf-level physics review.
- Do not stop after reporting defects when an in-scope repair is possible.
- Preserve unrelated dirty-worktree changes.

Finish with a short report: paper code, question/leaf/mark counts, repairs, reconciliation exceptions, ledger result, and every per-question manager/verifier/auditor/release verdict.
