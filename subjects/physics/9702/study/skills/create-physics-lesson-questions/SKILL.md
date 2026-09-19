---
name: create-physics-lesson-questions
description: Create 20 Physics 9702 lesson-practice questions after inspecting every past-paper part cited in the lesson evidence, with per-question origins, complete answer support and faithful source crops or verified original figures.
---

# Create Physics Lesson Questions

Read [subject-system.md](../subject-system.md) for actual paths, source authority
and validator interface. In managed runs, tracker/session instructions mean return
proposed lines to the manager; only the manager writes shared files. Record actual
model and reasoning effort in this stage's evidence.

Follow the shared [lesson workflow](../lesson-workflow.md) for order and impact-based
refresh. Update the affected tracker Notes cells with work done and only the
specific items needing refresh; preserve unrelated stage approvals.

Build one complete practice set from approved `lesson.md`. Own practice only;
preserve lesson Markdown, canonical sources, mappings, definitions and lesson HTML.
Read workspace instructions, the study handoff, target Markdown, lesson scope,
build evidence, topic maps, syllabus and topic audit when present.
Require pre-audit Student/Science coverage and the manager's final audited inputs
under the shared workflow. Student-reference sync is inactive. Read
[practice-contract.md](references/practice-contract.md) and
[cambridge-physics-diagram-style.md](references/cambridge-physics-diagram-style.md).

## Updates to an existing set

For a previously completed set, repair only affected questions/parts/assets. Keep
20 questions and stable IDs. Reuse truthful prior inspection records for unchanged
sources; reread relevant source parts when their content or the assessed claim
changes. Re-solve edited questions and check affected totals/dependencies. Do not
regenerate all 20 or reinspect unrelated sources for a bounded repair. Reconcile
input hashes after the impact check, retain history and resolve matching Notes.
Initial builds still follow the complete inspection workflow below. If the old
set lacks evidence needed for the current release, report that actual gap.

## Inspect the lesson's evidence questions

Use `lesson-build-evidence.json` to enumerate every unique cited past-paper
question/answerable part, including `question_parts_inspected`, diagram entries
and other explicit question references. Inspect all, not a three-question minimum
or a new arbitrary sample. Shared parent files/assets may be read once, but cover
every cited part. Do not crawl the entire mapped corpus or unrelated sources.

For each part, read the actual prompt, options, shared context, required figures
and tables, then its official answer/mark scheme. A quick focused inspection is
fine; summaries, enrichment and historical read claims are not substitutes.
Record actual file paths read and a short demand/misconception or exclusion reason
in the practice manifest. Inspect rejected/context-only entries too, retaining
scope exclusions; inspection does not mean the part must influence a new question.

Resolve cited parts through the topic evidence index, lesson map and canonical
packages under [subject-system.md](../subject-system.md). Evidence selects this
inspection set, not current lesson ownership. Preserve existing mapping decisions.
Flag unresolved paths or scope conflicts honestly; never silently count an unread
part as inspected. An explicitly empty evidence question list permits Markdown-led
questions with that limitation recorded; missing evidence is not an empty list.

## Decide inclusion from the actual lesson

Read the complete current `lesson.md` before selecting questions. Use what it
actually explains, together with its explicit prerequisites, to decide what the
student can answer. Broad lesson titles, outcome IDs, corpus mappings and prior
inspection records identify candidates; none proves the whole question or image
belongs here. Preserve mapping decisions, but exclude unsuitable practice content.

For every candidate, compare its required knowledge and visual recognition with
the relevant Markdown passages. Check each MCQ statement and each theory subpart,
not just the overall theme or correct answer. Students must be able to distinguish
the options using taught knowledge or information supplied in the question, without
needing later lessons. Supply brief unfamiliar context when useful; do not smuggle
in a later lesson's core teaching to rescue an unsuitable question.

An image may span several lessons. Inspect the exact figure and ask whether the
features needed for this question were taught here. Unrelated detail may remain
only if no answer depends on understanding it. Keep an in-scope part or faithful
crop when it stands alone; otherwise choose another question/image. A forces question requiring electrical fields does not automatically belong
in a mechanics lesson. Do not assess untaught circuit or field conventions.

Recheck every finished question against Markdown after adaptation. Confirm that
its prompt, options, marking points, hints and walkthrough stay within the selected
learning, and that every claimed label, arrow or identifying feature actually
exists in the final asset. If it does not fit, revise or replace that question;
do not expand the lesson or silently waive scope. Record the relevant section and
brief inclusion/exclusion reason in the existing origin/inspection notes, without
creating another report. Set `verification.scope` true only after this check.

## Readiness

Require reviewed Markdown; production requires a PASS topic audit matching the
current Markdown hashes for all audited lessons. Missing hashes or changed Markdown need
impact assessment and audit reconciliation under the shared workflow, not automatic
full re-audit or rebuilding all questions. The Markdown audit certifies teaching continuity only; independently
check the practice content and sources. Block completion for unresolved relevant
content evidence or any unread required evidence source. For an explicitly requested preview/test before the audit, create a draft set with
`delivery_status: review_preview` and `production_status: incomplete`. Record the
missing audit as a release blocker; all content/source/asset checks still apply.
Apply the release gates honestly: an absent audit remains a release failure, not
a reason to fabricate audit evidence. There is no minimum canonical-part count. Never fill gaps with off-lesson content.

## Exact set

Create exactly 20 questions in display order (filenames follow the contract):

- 1-10: ten four-option MCQs, one mark each. Make 8-10 moderately harder through
  application or linked reasoning, not untaught physics.
- 11-15: five short drills, normally 1-2 marks: definitions, terminology,
  recognition, classification or one-step concepts.
- 16-18: three medium questions, normally 3-4 marks: explanation, comparison,
  interpretation or data reasoning.
- 19-20: two hard multipart questions integrating several lesson ideas through
  a reasoning chain. Supply unfamiliar context needed to answer within scope.

Cover owned outcomes and major relevant inspected demands. Vary reasoning rather
than repeatedly testing one fact or copying embedded lesson activities. Questions
may adapt inspected papers or arise directly from Markdown; neither has a quota.
Keep exam prompts clear and precise. Difficulty comes from reasoning, not obscure
language. Do not force a figure where none is needed.

## Declare every question's origin

For a useful past-paper question, adaptation including light paraphrase is allowed.
Preserve its required information and use its faithful figure when suitable.
Re-solve after any change; a source answer key does not automatically remain valid.
Declare `adapted_official`, cite exact source parts, describe the changes and label
it “Adapted from Cambridge ...”. Never call light paraphrase wholly original or
an adapted answer an official mark scheme. New sets do not use exact question copies.

Use `official_figure_new_question` for independently written questions using an
unchanged official figure. Attribute the figure separately. Use `original` for
independently authored questions with no official figure; record any inspected
assessment pattern that influenced them. For questions thought from the lesson
alone, explicitly record “Created from lesson Markdown”, with lesson anchors and
no invented past-paper influence. Separate question influence from figure provenance;
an original prompt with an official figure still needs a figure source.

For multipart questions, identify influences per answerable part as well as the
parent question. Follow the contract's compact origin fields for every question.

## Figures: faithful sources or appropriate original methods

When an MCQ or theory part requires a figure, include the real asset. Prefer the
same inspected past-paper figure for an adapted question; copy an existing extracted
figure or crop it losslessly from the question image. Preserve all necessary labels,
scale bars, axes and context. Never stretch, redraw or change the scientific content
of a reused figure. Exclude surrounding answers and irrelevant question text. If a
crop cannot retain required context, use the complete figure or choose another item.

When a suitable source crop is unavailable, choose a method for the required
precision: programmatic drawings/plots for exact circuits, geometry, counts or data;
ImageGen for realistic illustrative form. Read the saved Cambridge style guide.
For qualitative ImageGen context, use the installed skill/tool and inspect the three local subject style examples
before the first generated figure; pass relevant style references. For programmatic
figures retain the source script/SVG and any input data, export a lossless PNG for
question delivery, and record method/provenance under the practice contract.
Answer-critical structures, mechanisms, circuits, graphs and data stay deterministic.
Neither method substitutes for authentic observational evidence when needed.

Specify required labels, counts, bonds, arrows and values explicitly for either method.
Inspect every generated feature against the intended question, especially graphs,
circuit diagrams and measurement tasks. Reject or regenerate incorrect output;
use a suitable source crop if generation cannot meet accuracy. Never accept an
inaccurate image to finish the set. Generated laboratory/context illustrations are synthetic, not experimental observations. Do not invent scale bars or calibration.
Printed magnification alone becomes unreliable after resizing; measurement questions
need a valid scale reference or controlled physical size and checked working.

Save final assets under `practice-questions/assets/`. Record source/crop or generation
provenance, dimensions, hashes, alt text and visual verification.
Alt text must supply equivalent observable information without revealing answers.

## Answer support and verification

Every question needs a complete mark scheme, progressive hints, concise solution,
and patient teacher walkthrough in simple short steps. Separate the complete
mark-worthy answer from its explanation. Include plausible MCQ distractors and
explain each option. Provide proportionate support for every multipart subpart.
Map questions to lesson anchors/outcomes and relevant definition/formula references.
Reference entries are optional recall support, not evidence that a concept was taught.
Keep prompts/options answerable without consulting the registry. Do not embed active
lookups that disclose answers; relevant concept links may appear in revealed hints
or feedback. Preserve the existing answer/scoring semantics.

Solve each final prompt and figure without consulting the proposed answer first;
then reconcile the answer, alternatives, marks, units, calculations and distractors.
Check that there is one unambiguous MCQ answer, no leaked answers in figures, and
no requirement for later lessons. Update the solution after any prompt/asset edit.

## Finish

Preserve any existing practice files before replacement using the repository's
dated archive and hash manifest; preserve released IDs. Write practice files, any necessary lesson-owned generators under
`scripts/practice-figures/<lesson_id>/`, the preservation archive and required
tracker/session updates. Do not modify shared validators during question creation. Validate JSON,
IDs, exact distribution, marks, complete evidence inspection, origins, referenced
files, hashes, scope and visual accuracy against the contract.

Run `python3 scripts/validate_practice_questions.py <lesson-folder>` from the subject
workspace. This is the structural validator, with no strict mode. Perform and record
all additional manual release gates in the practice contract separately; structural
PASS cannot certify provenance, scientific accuracy or release readiness.

Record creator verification in Notes and hand off to Review Questions. Mark
`Lesson questions` ✅ in `study/LESSON-PRODUCTION-TRACKER.md` only after that review
covers the final set and all release gates pass. A creator self-check alone does
not complete the stage. Append a concise dated study handoff.

For a requested independent review of an existing set, use
[review-physics-lesson-questions](../review-physics-lesson-questions/SKILL.md).
