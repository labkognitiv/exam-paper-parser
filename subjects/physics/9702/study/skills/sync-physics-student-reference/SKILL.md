---
name: sync-physics-student-reference
description: After Physics lesson Student and Science reviews, find important terms needing clarification, reuse shared registry entries or write brief explanations, and save stable IDs with lesson links in one run.
---

# Sync Physics Student Reference

Run once after Review Student and Review Science cover the target lesson. Read the
[shared workflow](../lesson-workflow.md), complete final `lesson.md`, its review/source
evidence and the [reference contract](references/reference-contract.md). Preserve
lesson Markdown, controlled definition/formula registries and canonical sources.
There is no separate reference-draft pass or routine return through lesson reviews.

## Find and explain

Scan teaching, examples, activities, feedback and learner-facing visual descriptions
for anything needing a brief clarification. Include supporting vocabulary such as
resultant, gradient, phase, field, potential and equilibrium. Selection
is based on student need here, not membership in an official definitions list.
Exclude production metadata, irrelevant nouns and unrelated source-question content.

Look up each term with `python3 scripts/student_reference.py "resultant"` from the
Physics workspace. The read-only helper matches normalized names and saved aliases,
returning candidate IDs, meanings and explanations. Check the meaning in context:
“potential” can have different physical senses. Add useful aliases to
new entries; do not guess that similar spelling proves identical meaning.

If a suitable entry exists, reuse its ID and explanation. Add this lesson's links;
do not rewrite or expand the explanation just because the term appears again.
For a new concept, write a brief, standalone teacher explanation and a short example
when it helps. Explain supporting vocabulary directly, avoid circular definitions,
and include necessary qualifications. No images or advanced concept expansion yet.

Check each new explanation for clarity, accuracy and fit against the reviewed lesson
and actual source passages. A paraphrase must preserve the supported meaning; new
facts/examples need source checking in this run. Earlier lesson reviews do not
certify text written afterwards: record these as the sync skill's own checks, not
invented Student/Science approvals. If evidence is missing or meanings conflict,
record the specific unresolved entry; do not publish it as checked. This exception
is not an extra routine workflow stage. Essential teaching still belongs visibly
in the lesson; report any lesson defect for its owner rather than editing it here.

## Save once

Prepare changes in memory, then acquire the shared lock and reload the registry.
Repeat lookup under the lock: a parallel lesson may just have added the same term.
Reuse that entry when its meaning fits; never create duplicates from an earlier
lookup or overwrite another lesson's update. Check any different saved wording
against intended occurrences before choosing it. Follow the contract's reversible
write procedure and preserve all existing IDs, explanations and other lesson links.

Save new checked entries with stable concept IDs, explanations and source evidence.
Write the final lesson occurrence map using the contract; this is an output of the
same run, not a user-facing second step. Each link names the lesson, concept ID,
current payload hash and exact locations. Rescanning replaces this lesson's old
occurrences, preserving history; it does not delete unused shared concepts.

## Verify and stop

Check duplicate IDs/meanings, alias matches, payload hashes, final Markdown hash,
source/clarity checks and all intended occurrence locations. An unresolved candidate
keeps its lesson map pending; do not mark an incomplete map complete. Reuse unchanged
valid entries without re-research. Record changed-entry corrections explicitly and
flag their existing consumers for targeted refresh; never silently rewrite them.

Update relevant tracker Notes and append the concise study handoff with added/reused
IDs and any unresolved items. Do not create a reference-draft artifact, require two
sync invocations, populate unrelated lessons, build panels or mark production complete.
