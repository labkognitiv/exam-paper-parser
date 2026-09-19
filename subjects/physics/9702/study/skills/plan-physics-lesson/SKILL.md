---
name: plan-physics-lesson
description: Research one Physics 9702 lesson and compile lesson-plan.json - the evidence, the concepts to teach with their depth grade, the dependency order, and the hook, visual and activity decisions. Produces no student prose and no Markdown.
---

# Plan Physics Lesson

Read [subject-system.md](../subject-system.md) for actual paths, source authority
and validator interface. In managed runs, tracker/session instructions mean return
proposed lines to the manager; only the manager writes shared files. Record actual
model and reasoning effort in this stage's evidence.

Decide what this lesson teaches, in what order, at what depth, and on what evidence.
Write `lesson-plan.json`. Write no student prose, no Markdown, no HTML, no questions.

Follow the shared [lesson workflow](../lesson-workflow.md). This skill is stage 1; the
author skill is stage 2 and consumes your plan. Update the affected tracker Notes cell.

## The division of labour

You decide. The author writes. Neither does the other's job.

| You own | The author owns |
| --- | --- |
| Which sources were read, and what they demand | Every sentence a student reads |
| Which concepts are taught, and at what depth | How each concept is explained |
| The order concepts must appear in | Headings, paragraphing, transitions |
| Which historical investigation opens the lesson | The hook prose and its four tests |
| What each activity must retrieve, and its interaction type | Prompts, options, answers, feedback wording |
| Each visual's purpose, method and source asset | What the visual shows and what to notice |
| Verified verbatim wording and its source path | Where to place it and how to explain it |

**Never write a sentence the author could paste.** A plan that says "explain that the
resultant points to the right" produces transcription, and transcribed prose is flat. Say
what must be true and what students get wrong; let the author find the words. If an
entry in your plan reads like lesson text, rewrite it as a requirement.

Your plan is a floor, not a ceiling. The author may add what you missed, and records it.

## Research

Read the workspace contract and nearest instructions. Use `lesson.json`, topic
`syllabus.json`, `lesson-knowledge-map.json` and `module-lesson-structure.md` for
outcomes, scope and prerequisites. Read the previous and next lessons' `lesson.json`
scope fields, not their Markdown: lessons are planned in parallel and earlier Markdown
may not exist. Planned boundaries are not proof that another lesson taught anything.

Resolve candidate parts through the topic `evidence-index.json` and the lesson's
`lesson-knowledge-map.json` entry, then canonical packages as specified in
[subject-system.md](../subject-system.md). Historical reads are not fresh verification.

Inspect answerable question parts by reading the **actual question wording first**,
including shared context, and opening every diagram, table or asset needed to answer the
part. Then read the mark scheme. There is no target count: keep going until three
consecutive parts reveal no demand or misconception you have not already seen, then
stop. Record how many you inspected and what the last three added. Count a part as
inspected only after those sources were actually read; record unreadable sources and
summary-only reads honestly rather than counting them.

For every figure you open, record `observed_features`: what is genuinely visible in that
asset, written after looking at it, in enough detail that someone else could check a
description against it. Shapes actually used, counts, labels present, what distinguishes
the items from each other. This is what stops a visual being specified from a paper code
rather than from the image.

Follow the subject system's definitions/formulas rules; do not infer a registry. Record verified
**Cambridge wording** verbatim with its exact source path. Registry presence alone is not
verification: if you cannot verify wording against a source, record the gap and do not
label it a Cambridge quotation.

## Decide what is taught, and how deeply

This is the core of the plan. List every concept the lesson touches and give each one a
depth grade. Getting a grade wrong is the most common cause of a lesson that jumps or
bloats, and it is cheap to fix here and expensive to fix later.

| Grade | Means | Gets |
| --- | --- | --- |
| `develop` | The lesson's real content. The student must be able to use it. | Full explanation built from its parts, a concrete example or comparison, and a retrieval opportunity. |
| `explain` | Needed and new, but not what the lesson is for. | A proper explanation, compact. No worked example required. |
| `mention` | The student should know it exists or connects, nothing more. | A sentence in passing. |
| `remind` | A prerequisite an earlier lesson owns. | One sentence of reminder; no automatic glossary. Never re-taught. |
| `exclude` | In range of the topic but owned elsewhere. | Named as out of scope, with the lesson that owns it. |

Grade against the shared workflow's **Three tiers of knowledge**: `develop` and
`explain` are tier 1, `mention` and much supporting vocabulary are tier 2, `remind` is
tier 3. A lesson that grades everything `develop` is bloated; one that grades its own
outcomes `mention` has a hole.

For each concept also record:

- **`why_this_depth`** - one line. "Two mapped parts require deriving it" or "used only
  to make the next idea readable" beats an assertion.
- **`misconceptions`** - what students actually get wrong, taken from mark-scheme
  guidance, rejected answers and MCQ distractors you inspected. Not invented.
- **`demands`** - what a student must be able to produce, from the inspected parts.
- **`depends_on`** - the concepts that must come first.

`depends_on` across all concepts forms the teaching order. Check it has no cycle and
that nothing is used before its dependencies. That order is binding on the author.

## Decide the hook, visuals and activities

**Hook.** Name the historical investigation this lesson should open with, and why it is
*this* lesson's spine rather than merely nearby. Supply verified facts with sources:
who, what was actually stuck, what they found, when. Verify dates and events against
real sources; invent no quotations, thoughts or events. If no investigation genuinely
fits, say so and specify a hypothetical scene instead. Write no hook prose: the author
writes it and applies the four hook tests.

**Visuals.** You decide how many there are. List one entry per visual and the list is
the count; the author writes descriptions for what you list and anchors each in the
prose, but does not decide the set. Each entry carries: what it must teach, the
assigned `method` from the
[required treatment table](../visualize-physics-lesson/references/physics-visual-design.md#method-by-teaching-need),
a one-line reason for that method, and for a paper-linked visual the exact
`asset_path`, `mode` and its `observed_features`. There is no target count and no
range: a visual earns
its place by showing what prose cannot state, and a visual that restates a sentence is
decoration you should not list. Derive the number from the teaching, then record it.
Assign `source_figure` when authentic examiner figures or observational/data evidence
are the teaching point. Assign `svg` or `python` for exact scientific diagrams,
structures, mechanisms, graphs, geometry, counts and data. Assign `imagegen` only
for qualitative context requiring no exact measurement or answer-critical geometry.
Follow the subject treatment table. Never present generated art as experimental
evidence or substitute it for exact symbols, structures or data. Required raster
labels must be generated inside the image; no overlays or hybrid assets.

**Activities.** You decide how many there are, on the same basis: every distinct
reasoning step the lesson teaches earns one retrieval opportunity, and a section that
teaches nothing new earns none. One entry per activity: which concept and which
reasoning step it retrieves, the interaction type, and the misconceptions its
distractors must address.
No two activities share an interaction type, and at least one must combine two concepts
taught in different sections. An activity that can be answered by keyword-matching the
preceding paragraph is a recall checkpoint, not a retrieval opportunity. Write no
prompts, options or feedback.

## Write lesson-plan.json

Schema `9702_physics_lesson_plan_v1`. Include: `lesson_id`; `generated_at`; `scope` with
owned outcomes and declared boundaries; `sources_inspected` with paths, part ids and what
each demanded; `figures_observed` with `asset_path` and `observed_features`;
`verified_wording` with verbatim text and source path; `concepts[]` with `id`, `name`,
`depth`, `why_this_depth`, `misconceptions`, `demands`, `depends_on`; `teaching_order`;
`hook`; `visuals[]`; `activities[]`; `unresolved[]`; `model`; `reasoning_effort`.

Validate that it parses. Use no em dashes or en dashes anywhere.

## Finish

Check before you stop:

- Every owned outcome maps to at least one `develop` or `explain` concept.
- `depends_on` has no cycle and nothing precedes its dependencies.
- Every `remind` concept names the lesson that owns it.
- Every misconception is traceable to an inspected source, not invented.
- Every paper-linked visual has an `asset_path` that exists and `observed_features`
  written from opening it.
- Nothing in the file reads as student prose.

Record honest `unresolved` items: missing planning boundaries, unreadable sources,
scope conflicts where a prerequisite is too heavy for a reminder. Do not resolve a
scope conflict by quietly teaching it; report it.

Update the lesson's tracker Notes cell with the plan and what remains. Append one
concise dated handoff to `study/SESSION-LOG.md`. Planning alone completes no stage.
