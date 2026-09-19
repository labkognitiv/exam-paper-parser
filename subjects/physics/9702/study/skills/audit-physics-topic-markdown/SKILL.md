---
name: audit-physics-topic-markdown
description: Read all Physics topic lesson Markdown in sequence and directly fix missing basics, explanations, transitions, unnecessary repeated teaching and visual cues. Markdown-only teaching continuity audit, not a scientific evidence or past-paper review.
---

# Audit Physics Topic Markdown

Read [subject-system.md](../subject-system.md) for actual paths, source authority
and validator interface. In managed runs, tracker/session instructions mean return
proposed lines to the manager; only the manager writes shared files. Record actual
model and reasoning effort in this stage's evidence.

Follow the shared [lesson workflow](../lesson-workflow.md) for order and impact-based
refresh. Update the affected tracker Notes cells with work done and only the
specific items needing refresh; preserve unrelated stage approvals.

Make the topic one connected learning journey. Treat reviewed science as an input.
The manager checks its continuity repairs; no automatic reviewer loop follows.
Uncertain new scientific claims are upstream defects blocking affected production. Edit lesson Markdown directly as you read; do not merely
propose fixes. Preserve language level, teacher voice, presentation and requirements.

## Choose the check scope

For an initial audit, read the full sequence below. For changes after a valid PASS,
compare preserved originals with current Markdown and inspect affected sections,
lessons and transitions. Preserve unaffected approvals; do not repeat the whole
initial audit for one or two bounded changes. Expand only if dependencies cannot
be bounded. Recheck all edited teaching and its affected downstream uses. Keep
input content Markdown-only. Record targeted scope in the existing audit report.

## Read the whole sequence (initial or unbounded audit)

Read applicable workspace instructions and the study handoff. Discover lesson
order and planned membership from the Course Pathway in `module-lesson-structure.md`,
including planned lessons without `lesson.md`; use folder IDs to locate files.
Conflicting/duplicate planned IDs block the audit. Read every
`lesson.md` completely, including all worked examples and answers. Sidecars are covered by the per-lesson
reviews; this audit checks Markdown continuity. Never substitute headings or excerpts for full reading. If order or
a missing lesson cannot be resolved, report it and continue useful repairs, but
do not pass an incomplete topic.

Teaching-continuity content inputs are Markdown only; the mechanical
sidecar-anchor check below is the sole exception. Do not open lesson JSON, syllabus JSON,
registries, evidence records, mappings, past papers, mark schemes, PDFs, images
or web sources. Do not load authoring or visualizer workflows. Check completeness
of the teaching in the supplied Markdown, not official syllabus coverage,
scientific certification or source verification.

Before edits, preserve originals and any existing audit report in the repository's
dated archive with a path/hash manifest. Keep a small working note of where each
idea is explained and what later lessons assume. Look ahead in the topic Markdown
when needed before changing apparent gaps or duplication. Audit only after parallel
lesson writers have finished; never edit a lesson concurrently with its owner.

## Repair while reading

- Read as a 17-18-year-old beginner with weak prior knowledge. Before technical
  teaching, check that basic meanings, terms, parts and reasoning are established.
  Add missing foundations before the explanation, example or activity using them.
- Track what prior lessons actually explain. If a prerequisite was taught there,
  add only a short reminder when useful; otherwise proceed without repeating it.
  Never claim an earlier lesson taught something it only mentioned. Standalone
  means understandable with a small bridge, not a full retelling of earlier lessons.
- Check every lesson transition, including module boundaries. Supply the missing
  reasoning between what students know and what comes next. Teach generic ideas
  and parts before specialised names, mechanisms and applications.
- Add missing explanations within existing topic scope. Match nearby simple words,
  patient teacher voice and short bursts, following the shared paragraph rule. Explain
  essential terms before use. Essential teaching belongs in explanations, not only
  in activity answers or feedback. Do not rewrite prose merely to change its style.
- Give each concept a clear main teaching location. Preserve useful reminders,
  retrieval, different examples and deeper applications. Trim only unnecessary
  full reteaching, preserving every unique point and the explanation needed locally.
  Do not change learning goals or move whole lesson ownership.
- Preserve presentation patterns, hooks, closing connections, worked
  Answer/Explanation separation, activities and feedback. Make local edits
  needed for continuity without changing lesson or section order. Preserve exact definitions, formulas, values, answer
  conditions, stable IDs and source references. Do not change learning requirements.
- Preserve the teaching behind approved activities and visuals. Do not add production
  cue blocks or interaction specifications to student Markdown. Record new sidecar
  needs in the report for the lesson owner.
- Before freezing inputs, have each lesson owner reconcile exact sidecar anchors
  against repaired Markdown without changing its prose. Verify this mechanical check
  and record sidecar hashes. The audit may read sidecars for anchor checking only;
  it does not certify their science. Substantive sidecar needs return to their owning
  stage and block affected production until checked.

Fix gaps in place using accepted Markdown and straightforward foundational explanations.
Do not move sections, examples, activities or lesson ownership; parallel authoring
does not imply sequential dependencies on completed drafts.
Do not guess to reconcile scientific contradictions or introduce uncertain new
subject content. Record those cases for separate authoring review while completing
all independent repairs. Do not expand this audit into external research.

## Re-read and finish

For a full audit, reread the entire revised sequence; for a targeted audit, reread
the affected teaching and transitions. Check that ideas precede their use, explanations
support activities and cues, transitions work, and no unique teaching, exact wording
or references were lost. Fix remaining repairable gaps before finishing.

The manager owns every audit repair and must resolve all teaching and continuity
defects before recording PASS. Record substantive additions and their evidence in the
audit report. Do not dispatch automatic Student/Science rechecks or reference sync.
A PASS cannot coexist with an unresolved content defect.

Write one concise `<topic-folder>/topic-markdown-audit.md` with:

- `Result: PASS` or `Result: FAIL` for Markdown teaching continuity. Missing lessons or unresolved
  teaching defects mean `FAIL`.
- Scope: Markdown only; science, official coverage and evidence were not revalidated.
- Use the shared workflow table format: workspace-relative lesson path, final
  SHA-256 of `lesson.md`, and `keep` or actual changes.
  Give section locations for unresolved findings.
- Topic Markdown gate: passed or blocked. PASS satisfies only this gate; the
  visualizer must still apply its separate evidence and content checks. Later edits use the
  shared impact-based refresh rules; keep unchanged rows and approvals.

Change only lesson Markdown, this report, tracker Notes, the preservation archive
and the required concise dated study session handoff. Do not change canonical data, planning, evidence,
practice packages, images or HTML. Update tracker Notes with checks completed and
only affected outputs needing refresh. Report completion briefly.
