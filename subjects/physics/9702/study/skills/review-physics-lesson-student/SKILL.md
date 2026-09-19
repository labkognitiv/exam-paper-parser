---
name: review-physics-lesson-student
description: Review and repair Physics lesson Markdown from a student's perspective, including language, definitions, reasoning, practice support and synthesis. Scientific verification belongs to Review Science.
---

# Review Physics Lesson Student

Read [subject-system.md](../subject-system.md) for actual paths, source authority
and validator interface. In managed runs, tracker/session instructions mean return
proposed lines to the manager; only the manager writes shared files. Record actual
model and reasoning effort in this stage's evidence.

Read the [shared workflow](../lesson-workflow.md), complete target `lesson.md`,
lesson scope/prerequisites and current build evidence. Read the
[teacher guidelines](references/teacher-guidelines.md) for difficult passages.

Own the student's understanding and language together. Preserve lesson ownership,
section order, activity/cue IDs, verified quotations, values and answer meaning.
Lessons may be authored in parallel: do not wait for earlier lesson Markdown,
assume earlier teaching from a plan, or move content between lessons. Fix locally
with a brief explanation at the point of need. Flag a boundary conflict rather
than changing curriculum order. Preserve originals using the dated manifest rule.

## Read as a student

Read the whole lesson in order, with weak recall of its stated prerequisites.

Run four named checks and record each in `review_history`:

- **`first_lost_line`.** Reading in order, name the first line where a student with the
  stated prerequisites would be lost, and repair it. If there is none, say so
  explicitly. This is the single most useful thing this review produces.
- **`terms_before_use`.** Every technical term, symbol and diagram convention has its
  explanation earlier in the document than its first working use, including terms that
  first appear inside an activity option, a feedback branch or a worked answer. Check
  the tier too: a tier 1 idea written as a one-line reminder is the usual cause of a
  jump, and a tier 3 prerequisite re-taught at length is the usual cause of bloat.
- **`reasoning_not_listed`.** No mechanism or structure-function relationship is
  presented as a bulleted list of properties with no prose saying why one thing follows
  from another. A section that could be read in any order without loss is explaining
  nothing.
- **`hook_check`.** Apply the author skill's four hook tests: generality, vocabulary,
  ownership, return. A hook that breezes past its own question, or is never returned to
  at the close, fails and is repaired. Nobody else checks this.

For each difficult passage, determine whether the supplied teaching lets a learner:

- understand what the important words, symbols and diagram conventions mean;
- connect the new idea to the preceding explanation and follow why it happens;
- recognise the relevant features in the specified visual, including unfamiliar
  representations, without treating an arbitrary diagram shape as a universal rule;
- attempt the next activity using taught or explicitly supplied knowledge;
- understand the mistake and repair it from the feedback;
- connect the main ideas at the end and answer the opening question.

Fix missing explanations directly using supported lesson content. Essential new
teaching remains visible before its use; a clickable reference is recall support,
not a place to hide the lesson's reasoning. Where material is missing or uncertain,
name the precise claim/support needed for Review Science rather than guessing.
Do not inspect scientific sources or claim scientific certification in this pass.

## Repair teaching and language together

- Explain unfamiliar terms when first needed, including supporting vocabulary
  such as resultant or potential difference. Keep precise physical terms and simplify surrounding
  language. Explain terms without circular definitions or chains of new jargon.
- Follow the shared paragraph rule: short connected paragraphs, one main idea;
  give reasoning the space it needs. Use lists for parallel facts, steps for a
  sequence and tables for comparisons. Do not count sentences or displayed lines.
- Make causal steps explicit and keep useful reminders, varied examples and
  retrieval. Do not pad a lesson to satisfy an activity, image or opening-length quota.
- Check analogies explain the relationship and make their limits clear. Keep
  source codes, outcome IDs and production instructions out of student prose.
- Check visual cues specify what the student should look at and notice. A label saying “parallel branches” cannot replace actual circuit connections. Record asset changes
  for the visualizer; this review cannot certify unseen images or interactions.
- Keep each worked example together: question, complete **Answer**, then simple
  **Explanation**, with its related diagram. Preserve the approved definition style.
- Ensure activity directions are clear, distractor vocabulary is taught or supplied,
  and feedback addresses the selected misconception. Checked responses use supplied
  choices; optional writing uses ungraded model-answer reveal and comparison guidance.
- Strengthen the closing connection or an existing supported self-check when needed.
  Do not add a standard glossary, extra topic content or extra exercises by default.

## Finish

Reread revised teaching and inspect the diff. Append a concise entry in the existing
`lesson-build-evidence.json` `review_history` with `reviewer: student`, date, final
`markdown_sha256`, full or impact-scoped coverage, the four named checks above,
findings with section/cue/activity locators, corrections, remaining issues, and
separate `student_readiness` and `teaching_order` results. Use PASS, FAIL or BLOCKED. Missing learning support fails
readiness; unavailable material needed to judge it blocks the affected check.
Record scientific questions under existing `unresolved`; never write a science PASS.

Follow shared review coverage and impact rules. Send new or altered factual claims,
keys and examples to Review Science. Review Science is the final per-lesson review;
do not schedule an automatic Student recheck after it.
Update relevant tracker Notes and append the concise study handoff. Leave HTML,
practice packages, canonical definitions, mappings and historical approvals untouched.

## Sidecar coverage and anchors

Read `lesson-visuals.json` and `lesson-activities.json` with Markdown; options, keys
and feedback live there. Review/repair them within this stage's remit. When prose
changes an anchor, update its exact quote and heading path without moving its teaching
position. Preserve IDs/methods; report method defects upstream. Record both sidecar
hashes and Markdown hash in review evidence. Never certify unread sidecars or stale
anchors. Preserve originals before repairs.
