---
name: review-physics-lesson-science
description: Verify and correct the science in Physics lesson Markdown against actual authoritative sources, including definitions, mechanisms, figures, calculations and answers. Student teaching and language belong to Review Student.
---

# Review Physics Lesson Science

Read [subject-system.md](../subject-system.md) for actual paths, source authority
and validator interface. In managed runs, tracker/session instructions mean return
proposed lines to the manager; only the manager writes shared files. Record actual
model and reasoning effort in this stage's evidence.

Follow the [shared workflow](../lesson-workflow.md). Read workspace instructions,
the complete target Markdown, its specification, applicable syllabus scope and
build evidence. The manager's topic audit follows all completed lesson reviews.
Preserve originals before repairs. Do not change lesson/section order or ownership.

## Establish actual evidence

On the first full review, verify every scientific claim in teaching, definitions,
worked examples, activities, options, keys, feedback, captions and visual cues.
Include historical claims in the hook. Later checks may cover a bounded diff and
dependent claims only with a recorded verified baseline and preserved originals.
Do not reinterpret historical readability/language passes as new scientific reviews.

Read relevant actual source passages and assets. Use Cambridge syllabus, questions
and mark schemes for assessed scope, exact wording and answer conditions. Resolve
paper references through the topic evidence index and lesson map, then canonical
packages under `past papers/`; inspect full context and required assets. Follow
[subject-system.md](../subject-system.md) for definition/formula authority.
Stored wording, summaries and previous inspection counts are not verification.

Use authoritative physics sources for mechanisms and unresolved claims: inspected
textbooks, primary research or relevant university/scientific institution resources.
Browse when local sources are unavailable or uncertain. A shortened mark-scheme
answer does not establish a complete mechanism. Related claims may share one
inspected passage; record concise locators rather than a report per sentence.

## Check the unsourced claims separately

Source verification cannot reach a claim that cites nothing. Run a second, explicit
pass over exactly those claims, because a lesson can quote every mark scheme perfectly
and still teach something false. Nothing in this pass is settled by finding a citation;
each item is settled by subject knowledge, and by an authoritative source where any
doubt remains.

Cover at least:

- **Physical representations.** Distinguish force vectors, rays, field lines and
  current arrows; check origins, directions and conventions. Circuit connectivity
  is topological; a schematic does not establish a numerical scale.
- **Laws and assumptions.** Check system boundaries, conservation laws, resultant
  versus individual forces, scalar/vector distinctions and approximation limits.
- **Quantitative physics.** Check dimensions, SI units/prefixes, signs, components,
  gradients/areas, uncertainty and significant figures; recalculate from givens.
- **Analogies and comparisons:** whether the relationship mapped is the real one, and
  whether the stated limit is the limit that matters.
- **Absolute and exhaustive statements.** "Always", "never", "only", "nothing but", and
  bare lists offered as complete. These are the most common carriers of a false claim
  in otherwise well-sourced teaching; confirm the absolute is true rather than merely
  true of the examples in front of you.

Record this pass in the review entry as `first_principles_check` with the claims
examined and the result. A source-verification PASS alone does not satisfy it, and an
entry that omits it is incomplete coverage.

## Verify and repair

- Check structures, locations, direction, connections, sequences, cause and effect,
  conditions, exceptions and analogy limits. Simplification must remain accurate.
- Check claimed Cambridge definitions and quotations against their exact source.
  Preserve verified wording and explain it separately. Unverified paraphrases
  must not be labelled official; record missing evidence or conflicts explicitly.
- Independently recalculate answers before consulting proposed working. Check units,
  symbols, rounding, values, alternatives, distractors, keys and all feedback paths.
  Keep the complete mark-worthy Answer distinct from its student Explanation.
- Open every source figure a cue names and record `observed_features` in the review
  entry: what is actually visible in that asset, written after looking at it, covering
  the shapes actually used, counts, labels present and what distinguishes the items
  from one another. Verify the cue against those recorded features, never against the
  cue's own description or the paper code alone. A cue that names a real figure can
  still misdescribe it, and that is a defect to repair here. Check labels, counts,
  vectors, orientation and what the visible evidence does or does not establish. Where a
  cue teaches a recognition shortcut, confirm the named figure actually supports that
  shortcut; if the figure distinguishes its items some other way, correct the cue to
  the convention the source really uses. A valid cue does not certify an unseen
  rendered image; flag exact downstream checks needed.

Correct supported scientific errors in authored content and original answers.
Keep IDs, lesson order, source quotations, canonical papers, mark schemes, mappings
and controlled registry records intact. Do not rewrite a quoted source to resolve
a conflict. Flag conflicts and continue independent work. Do not revise fluent
language for style or expand the topic scope. Repair scientifically necessary teaching
support in this pass and record the change; do not start an automatic Student recheck.

## Finish

Append `review_history` in the existing build evidence: `reviewer: science`, date,
final `markdown_sha256`, full/impact-scoped coverage, actual inspected sources with
page/section/figure locators, `observed_features` per opened figure,
`first_principles_check`, corrections, affected outputs, remaining issues and
`scientific_accuracy: PASS|FAIL|BLOCKED`. Apply the shared baseline coverage rule.
Known unresolved errors fail; evidence unavailable for a necessary claim blocks.
Do not certify student readiness, unseen HTML or a production release.

Keep historical source-read records and verdicts unchanged. Refresh a hash only
after its impact check; unresolved affected claims block dependent release. A
structural validator cannot establish scientific truth. Update relevant tracker
Notes and append the concise study handoff. Do not change practice packages or HTML.

## Sidecar coverage and anchors

Read `lesson-visuals.json` and `lesson-activities.json` with Markdown; options, keys
and feedback live there. Review/repair them within this stage's remit. When prose
changes an anchor, update its exact quote and heading path without moving its teaching
position. Preserve IDs/methods; report method defects upstream. Record both sidecar
hashes and Markdown hash in review evidence. Never certify unread sidecars or stale
anchors. Preserve originals before repairs.
