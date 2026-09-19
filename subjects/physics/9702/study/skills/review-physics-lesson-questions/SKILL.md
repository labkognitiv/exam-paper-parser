---
name: review-physics-lesson-questions
description: Audit and directly fix an existing Physics lesson's 20 practice questions against its Markdown, answers and actual figures. Preserve sound questions; report meaningful fixes or explicitly say no defects found.
---

# Review Physics Lesson Questions

Read [subject-system.md](../subject-system.md) for actual paths, source authority
and validator interface. In managed runs, tracker/session instructions mean return
proposed lines to the manager; only the manager writes shared files. Record actual
model and reasoning effort in this stage's evidence.

Follow the shared [lesson workflow](../lesson-workflow.md). Review for dependable
student practice, not perfection. Fix meaningful errors directly; do not regenerate
a sound set, polish every sentence, manufacture findings or force a difficulty score.

## Read and solve

Read local instructions, complete current `lesson.md`, lesson scope, all 20 question
records including every answer, hint, walkthrough and subpart, the manifest and
any existing review. Read the [practice contract](../create-physics-lesson-questions/references/practice-contract.md).
Open every distinct final question image. Check existing topic-audit/release status;
a missing topic audit does not prevent this review, but must not become a release PASS.

For each question, solve its prompt and figure before comparing with the proposed
answer. Use the actual Markdown to check what students know. Mappings and source
inspection history only identify candidates, not guaranteed lesson fit. Check every
MCQ statement and answerable theory part, including knowledge needed to reject
options. Brief supplied context is fine; later-lesson teaching must not be required.

Check the following, fixing only genuine defects:

- Correct science, one unambiguous MCQ key, fair distractors, correct calculations,
  units and marks; multipart marking totals and accepted answers must agree.
- Prompts and required recognition fit the lesson. Figure labels, arrows, counts,
  directions and features cited in prompts/answers must exist in the actual image.
  Do not assume a source figure has the labels needed by the adapted question.
- Mark schemes, progressive hints and simple teacher walkthroughs are complete
  and agree with each other; explanations must not introduce scientific errors.
- Sources/origins, per-part origins, manifest summaries, asset credits and hashes
  match the finished questions. Adaptation is not exact official wording.
- Reference support does not introduce untaught assessable content or disclose an
  answer in a prompt/option before reveal. Preserve historical reference records; new sets have no reference integration.
  Rendered behaviour remains HTML QA.
- Overall coverage is useful. Purposeful repetition and modest difficulty are not
  defects; intervene only when duplication displaces essential learning or a
  supposedly answerable question requires untaught knowledge.

Inspect canonical question/mark-scheme sources where a disputed answer, source
claim or adaptation needs verification. Do not repeat the creator's entire corpus
inspection merely to review unchanged sources, and do not claim it was repeated.
If figure repair is necessary, follow the creator's source-crop/original-method
workflow. Preserve source pixels for official crops. New original precise figures
may use programmatic PNGs under the v3 contract; do not relabel redrawn official
figures as faithful crops or silently migrate existing packages.

## Repair and verify

Archive files before changing them with the repository's dated path/hash manifest.
Keep stable IDs, 20-question distribution and valid surrounding work. For each
repair update all affected answer/support fields, part origins and manifest notes;
re-solve the changed item. Do not change lesson Markdown, mappings, canonical
sources, production HTML or validator code. Report source-content or tooling issues
separately and continue independent question repairs.

Run `python3 scripts/validate_practice_questions.py <lesson-folder>` from the subject
workspace. It has no strict mode. Record the structural outcome and first blocker,
then separately record manual release gates from the practice contract. Fail-fast
results cannot prove later checks passed. Diagnostic bypasses cannot become production
PASS; never rewrite input hashes to hide failures.

Write one concise `practice-questions/question-review.md`: content verdict, whether
anything was found, exact question IDs/fixes (or “No question-content defects found”),
checks performed, input/final artifact hashes or a compact file-hash ledger, and
remaining release/tooling blockers. Correct inaccurate existing validation summaries
without inventing source-read history. Keep reporting proportionate to the findings.

Update only relevant tracker Notes with review completed, fixes and specific pending
items. Preserve unrelated stage approvals. Mark Lesson questions complete only if
all current release gates pass; a content PASS during an unaudited test run keeps
release pending. Append the required concise dated study session handoff, report
what was found/fixed, then stop. Do not add another refinement pass after acceptance.
