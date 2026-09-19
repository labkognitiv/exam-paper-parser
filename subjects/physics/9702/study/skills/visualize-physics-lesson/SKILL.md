---
name: visualize-physics-lesson
description: Convert audited Physics 9702 lesson Markdown into accessible visual HTML using exact deterministic diagrams, authentic source figures and qualitative ImageGen context; do not use for authoring or repairing lesson content.
---

# Visualize Physics Lesson

Read [subject-system.md](../subject-system.md) for actual paths, source authority
and validator interface. In managed runs, tracker/session instructions mean return
proposed lines to the manager; only the manager writes shared files. Record actual
model and reasoning effort in this stage's evidence.

Follow the shared [lesson workflow](../lesson-workflow.md) for order and impact-based
refresh. Update the affected tracker Notes cells with work done and only the
specific items needing refresh; preserve unrelated stage approvals.

Render one approved Physics lesson as responsive HTML without changing its teaching claims, definitions, values, examples, or sequence. Study the whole lesson before composing it. Preserve its science and learning progression, not its Markdown syntax or authoring scaffolding; this is an editorial translation into a student experience, not a Markdown dump.

Resolve source figures through the topic evidence index and lesson map, then inspect
canonical packages using [subject-system.md](../subject-system.md). Build records
remain inspection history, not verification of current sources.

## Required inputs and stop gate

Read the nearest repository, subject, and study instructions, then the complete target
`lesson.md`, its `lesson-visuals.json` and `lesson-activities.json` sidecars,
`lesson.json`, topic `syllabus.json`, lesson evidence record, and topic Markdown audit.
Read [physics-visual-design.md](references/physics-visual-design.md) before planning and
[html-review-schema.md](references/html-review-schema.md) before QA.

Production HTML is blocked when any condition holds (the preview allowance below
waives only the topic-audit gate):

- the topic audit is absent, is not `PASS`, is stale under the shared workflow
  (compare every topic lesson hash and membership), or lists an unresolved issue
  affecting this lesson;
- the lesson evidence record is absent/invalid, inspected canonical references are not named, or its unresolved items affect a claim being visualized;
- `lesson.md` conflicts with its mapped syllabus outcomes or contains an undefined essential term;
- the topic audit does not record the final Markdown hash;
- the target HTML or shared asset is being modified concurrently.

Report the blocking evidence. Do not repair Markdown inside this workflow.
For an explicitly requested preview/test before the topic audit exists,
produce `preview.html` and record `delivery_status: review_preview` and the absent
or stale audit in review evidence. Preserve all content, asset and accessibility
checks; do not mark the HTML tracker complete or claim a production PASS. This
preview allowance does not override known unresolved scientific/content defects.

## Required visual reference

Before every build, read [brand-guidelines.md](references/brand-guidelines.md) and
the subject visual-design reference. Inspect its three local source-figure examples
for subject conventions. Reuse verified local presentation components where available;
use subject-local references for conventions. References supply style, never
unrelated teaching content.

## Build

1. Hash and record every input. Preserve teaching claims, verified wording, values,
   answers and sequence. Preserve the student-reviewed teaching order; do not
   merge sections or move images so that terminology or visual features appear
   before their explanation. Presentation may change; add no teaching claims.
2. Start with the Markdown hook and its assigned visual. Implement every entry in both
   sidecars, following each rather than inventing filler to reach a count.
   Visuals describe learning steps, not mandatory separate image files. Related cues
   may share a composition while retaining each teaching purpose and its order.
   Build progressive visuals: generic parts first, then names and detail when the
   prose introduces them. Keep the sequence understandable without interaction.
   Teach recognition through visible identifying features and distinctions, not
   merely decorative pictures. Preserve the Markdown's recognition explanations.
3. Read `lesson-visuals.json` and `lesson-activities.json` beside the Markdown. These
   carry the visual and activity specifications; `lesson.md` is student prose only and
   contains none. Locate each entry by its `anchor` (heading path plus the exact quoted
   sentence it follows). **An anchor whose quote no longer matches the Markdown is a
   hard error: report it and stop, never guess the position.**
   Each visual already carries a `method` assigned by the planner under the
   [required treatment table](references/physics-visual-design.md#method-by-teaching-need).
   Build it with that method. You may not substitute a different one; if a method looks
   wrong for the teaching, report it as a defect for the planner rather than silently
   changing it. Where `method` is `source_figure`, place the real past-paper asset
   unaltered with its visible credit. Record the method actually used and confirm it
   matches the assigned one in HTML review evidence.
4. For cues assigned to ImageGen, **read and use the available ImageGen skill**.
   Group compatible illustrations into composite sheets, normally six panels
   (2 × 3), where useful; use standalone images when detail or composition warrants.
   Follow the design reference for generation, inspection, cropping and retries.
   No ImageGen call or sheet is required when the cue plan does not need it.
5. Use deterministic SVG, Python or native tables for exact scientific diagrams,
   graphs, geometry, data and notation, following the subject treatment table.
   ImageGen is only qualitative context; required labels must be in the accepted
   raster. Do not overlay exact diagrams or labels onto generated art.
   Implement reviewer/auditor additions from approved sidecars, retaining IDs and
   exact anchors. Lesson-only cues need no paper ID or invented provenance.
   For each explicitly paper-linked cue, resolve the exact figure from lesson evidence
   and open the actual asset. Record an `observed_features` note for that cue in HTML
   review evidence: what is genuinely visible in the opened figure, written after
   looking at it, in enough detail to check the cue against (shapes actually used,
   counts, labels present, what distinguishes the items from each other). Then compare
   the cue's description against `observed_features`, not against the cue's own wording,
   and report a mismatch rather than drawing what the cue says. A cue that misdescribes
   its own source figure is a content defect for Review Science, not an illustration
   choice. `recreate_original` uses an original scientifically equivalent
   representation; `reuse_official` permits a faithful copy or crop with source
   credit. Preserve labels, scale and context; never accept misleading detail or
   present a copy as original.
6. Vary composition to suit teaching: image right/text left, the reverse, labelled
   multi-panel groups, matched comparisons, or paired image-and-text scenarios.
   Keep explanations in short teaching bursts beside the relevant visual. Preserve
   purposeful repetition; do not compress it away or build dense text panels.
   Size diagrams to their useful content; never leave a half-page empty column
   opposite a lone figure. Group related comparisons and keep captions attached.
   Preserve reading sequence and stack sensibly on mobile. Follow
   [physics-visual-design.md](references/physics-visual-design.md).
7. Give definitions and formulas consistent, distinct backgrounds or cards;
   preserve verified wording exactly and keep the simple explanation nearby.
   Keep each worked example in one shared container with internal question,
   **Answer**, and **Explanation** labels and its supporting diagram.
   Highlight important terms selectively with bold plus accessible accent colours
   from the approved palette, not only bold black. Use consistent colours for
   related terms and restrained emphasis from the brand guidelines. Keep answers
   and calculations readable.
8. Preserve each activity sidecar’s checking mode. Use selectable blocks/options for checked
   responses; never automatically grade typed answers. Optional writing uses only
   ungraded model-answer reveal.
   Implement every approved activity with simple student-facing actions,
   correct/incorrect feedback, keyboard and touch support, and restrained coloured
   backgrounds that make them easy to find. Keep written teaching complete without
   JavaScript. Meaning must not depend on colour alone.
9. The Markdown is already student prose, so nothing needs stripping from it. Your job
   is to keep it that way: never print a sidecar field on the page. Convert `action`
   and `prompt` into one natural student instruction with real controls; `answer` and
   `feedback` become hidden interaction data revealed only after an attempt or an
   explicit reveal. Visual `purpose`, `what_to_notice`, `method` and `source` are
   production metadata and never appear as text. No sentence written about the student
   ("the student should notice") may reach the page; address the student directly or
   say nothing. Keep concise source credits for `source_figure` visuals visible, and
   preserve reviewed student prose unchanged. If wording or reasoning needs repair,
   return that passage to Review Student/Science rather than editing it here.
10. Give meaningful visuals alt text and equivalent prose, including important
    text embedded in generated images. Write lesson-owned `index.html`, assets,
    styles and `lesson-html-review.json`; do not mutate Markdown or canonical data.

When several lessons in one approved topic are visualized in parallel, assign one lesson directory per worker. Treat topic files and shared assets as read-only. Merge only after each lesson passes independently.

## Updates to existing HTML

For a previously verified lesson, change only affected text, visuals or controls.
Do not introduce student-reference integration. Historical review evidence is not
silently rewritten.
Rerun checks covering that change and shared layout dependencies; retain prior
checks for unaffected content with an explicit scope note in HTML review evidence.
Use the full QA below for a new build or changes whose effect cannot be bounded.
HTML-only edits do not invalidate other stages. Resolve the matching tracker Notes
item after verification and preserve unrelated pending work.

## QA

Verify at 390, 768, and 1280 px plus print. Test keyboard order, focus, both feedback branches, reduced motion, image failures, overflow, text size, contrast, scientific labels, and absence of network requests. Compare every HTML claim to Markdown and record the result using [html-review-schema.md](references/html-review-schema.md). Inspect every displayed image, including labels, short descriptions, leader-line targets, counts and physical relationships. Test every activity and inspect initial, incorrect, correct and reveal states: no leaked answers, duplicated specs or production language. Review actual screenshots across the whole page for empty columns, oversized image padding, detached captions, clipped labels and paragraph walls; source checks alone cannot pass visual QA. A successful generation call does not prove an image is usable. Any failed content-fidelity, accessibility, asset, or viewport gate leaves the lesson incomplete.

After all production content, topic-audit and HTML QA gates pass, update that lesson's `HTML` cell to `✅` in
`study/LESSON-PRODUCTION-TRACKER.md`. This is a required final step. Never mark
incomplete or failed work complete. Append one concise dated handoff to
`study/SESSION-LOG.md` after updating the tracker.
