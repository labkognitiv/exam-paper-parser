# Physics lesson workflow

Stage-to-model assignment, wave order and run rules for automated production live in
`study/orchestration.json`. This file defines what each stage does; that one defines
who runs it and in what order.

Updated 2026-09-17. Review Student replaces the former readability/language
teaching work; Review Science owns its scientific verification. There are two
lesson review skills, not a third language pass. Historical reviews remain history.

## Production order

1. **Plan the lesson:** research the sources and compile `lesson-plan.json` - concepts
   with a depth grade, teaching order, and the hook, visual and activity decisions.
   No prose. Other lessons may not exist yet.
2. **Author Markdown** from the approved plan, in its existing planned position, plus
   its visual and activity sidecars. The plan's scope, depth grades and teaching order
   are binding; report a defect rather than overruling one.
3. **Review Student:** repair understanding and language in the lesson.
4. **Review Science:** verify the lesson's facts, sources, examples and answers.
5. **Audit Topic Markdown:** once every lesson in the topic has passed both reviews.
   The manager performs and repairs this audit itself. Its recorded hashes become the
   final Markdown inputs; do not start an automatic post-audit review loop.
6. **Visualize Physics Lesson** and **Create Physics Lesson Questions:** run in
   parallel from the same audited version; verify HTML, assets, interactions and print.
7. **Review Physics Lesson Questions:** start after question creation and solve/check
   the final set. It may overlap visualization. Release only when all content,
   topic-audit, question-review and production QA gates pass.

The manager creates one local Codex task per lesson in the saved subject project, never
a worktree. Plan through Science happen sequentially inside that same persistent lesson
task. After the manager's audit, all later work returns to the same lesson task.
A request for one stage need not generate unrequested downstream artifacts.
Student-reference synchronization and reference UI are outside this workflow.

## Topic completion and review previews

Topic Audit precedes production visualization/questions. The manager pauses lesson
writers, repairs the topic in place, and owns the final audited Markdown hashes. Add
small local bridges instead of rearranging sections or ownership. There is no automatic
Student/Science recheck after the audit; the audit must not leave unresolved errors.

An explicitly requested preview/test may build review HTML and draft questions before
the topic audit, labelled review_preview/incomplete. Preserve all content and asset
checks; do not claim production completion or fabricate an audit. This exception
is not the default skill order. Existing subject preview history remains unchanged.

## Ownership and review coverage

- Planner: sources read, scope, which concepts are taught and at what depth, teaching
  order, and the hook, visual-method and activity decisions. No student prose.
- Author: every sentence a student reads, written from the plan. Explanations, hook
  prose, activity and visual wording. Adds what the plan missed and records it.
- Student: definitions at point of need, language, reasoning, practice/feedback,
  visual recognition support and synthesis. Science concerns go to Science.
- Science: factual claims, exact source wording, mechanisms, original calculations,
  keys and cue constraints in the lesson.
- Topic audit: cross-lesson continuity; existing Markdown is its content input.
- Visualizer: rendering, interactions and actual asset accuracy against approved
  teaching. No substantive prose rewriting; report content defects upstream.
- Question creator/reviewer: actual practice scope, source/figure fidelity, solving,
  answers and feedback. Reference availability does not expand assessable scope.

Preserve lesson/section order, IDs and ownership in all passes.
A missing earlier draft is not a blocker to independent authoring.

## Three tiers of knowledge

A lesson cannot teach everything it uses, and trying to produces either bloat or a
jump. Sort every idea a lesson touches into one of three tiers and treat it
accordingly. Getting the tier wrong is the most common cause of a lesson that feels
either padded or impossible to follow.

- **Tier 1, this lesson's own new learning.** Taught in full, visibly, in the prose,
  built up from its parts before it is named or used. Never delegated to a glossary
  entry, a reminder or another lesson. A clickable reference is recall support, not a
  place to hide the reasoning a student is meeting for the first time.
- **Tier 2, supporting vocabulary this lesson needs but does not own.** A term the
  student must understand to follow the sentence, where the term itself is not the
  learning. Give one plain sentence at the point of need, then move on.
- **Tier 3, prerequisites an earlier lesson owns.** A one-sentence reminder of what the
  student needs to have in mind.
  Do not re-teach it, and do not assume silent recall either: name it so a student who
  has forgotten knows what to look up. Where the reminder cannot be honestly written in
  a sentence, the dependency is too heavy for a reminder; report the scope conflict
  rather than quietly re-teaching it or assuming it.

Lessons are authored in parallel, so a tier 3 reminder is written from this lesson's
stated prerequisites, never from another lesson's Markdown, and it may not claim that
another lesson taught something. Report a scope conflict if a prerequisite appears to
be missing from the plan entirely.

Use short connected paragraphs with one main idea and enough space for reasoning.
Sentence and rendered-line counts are not requirements, and neither are counts of
activities, visual cues or hook length: each is earned by the teaching, and the
resulting number is recorded, not targeted. Implement every approved activity and cue;
preserve existing sets unless a relevant defect warrants change.
The separate 20-question practice distribution remains the current product contract.

Before the topic audit, both Student and Science must cover the same Markdown. Each
review_history entry records its reviewer, final `markdown_sha256`,
`coverage` (full or impact-scoped), observations and result. A scoped entry also
names its verified baseline hash, preserved comparison path and affected sections.
A full PASS plus a traceable sequence of scoped checks can cover the final version;
a scoped PASS alone cannot imply full coverage. Carry an unaffected verdict forward
only after checking the intervening diff and recording why it remains valid.
The later manager-owned topic audit records its own final hashes and does not inherit
or rewrite the reviewers' earlier exact-hash claims.

Keep the existing `scientific_accuracy`, `student_readiness`, `teaching_order`
fields. Student owns the latter two; Science owns the first. Do not fabricate
coverage for legacy lessons or overwrite old verdicts when renaming skills.
An unresolved affected review issue blocks release. Manual evidence and final-version
coverage checks remain required even when structural validation passes.

## Freshness and completion

A successful topic audit freezes the recorded Markdown versions for production;
no separate approval file is needed. Each audit uses `Result: PASS` or `Result: FAIL`
and a table `| Lesson | SHA-256 | Changes |`. Lesson cells contain backticked paths
from the Physics workspace to `lesson.md`; SHA-256 cells contain final hashes.
List every planned topic lesson, including missing ones with `missing` in the hash
cell and an overall FAIL. Read the ordered Course Pathway lesson bullets in
`module-lesson-structure.md` for planned membership, including lessons without Markdown. Folder IDs locate the
files; existing `lesson.md` files alone cannot establish topic completeness.
Duplicate, conflicting or unresolved planned IDs block the audit. Planning language
about possible sequence changes does not authorize changing the current order.

Before questions or production HTML, compare the audit's listed hashes with disk
and verify membership against current topic lessons. A mismatch calls for change
assessment, not automatic full rework. Keep the first full audit requirement;
missing baseline audits or untraceable changes cannot inherit a PASS. Review
previews and draft questions use the explicit preview/test allowance above; every
relevant content, asset and accessibility check still applies.

## Impact-based refresh

Compare changed content with its preserved prior version and record what depends
on it. Impact, not the number of edits or a “major/minor” label, sets the scope:

- Typo, punctuation or wording polish without changed meaning: check that diff
  locally. Keep reviewer/topic approvals; update matching HTML text if needed.
  Questions remain valid unless the edit touches their wording or references.
- Changed explanation, fact, answer, activity or visual cue: check that section and
  its dependent questions/visuals. Recheck teaching order only where affected.
- A separately authorized change to prerequisites, scope or lesson sequence: use a
  targeted topic audit of affected lessons/transitions, expanding only when dependencies spread. A full
  topic reread is for initial audits or changes whose impact cannot be bounded.
- HTML-only layout, image or interaction changes: rerun affected HTML checks.
  Do not invalidate Markdown, reviewer, topic audit or questions. If HTML exposes
  a source-content defect, report that actual dependency separately.
- Question-only edits: validate affected questions, assets and set totals as needed;
  preserve other stage approvals unless a source-content defect is discovered.

Hashes remain evidence of exact inputs, not instructions to regenerate everything.
For meaning-preserving editorial edits, the editing skill may read the existing
PASS audit and update the changed lesson's hash/Changes cell after verifying the
diff, noting “editorial change checked; continuity unaffected”. This narrow audit
metadata reconciliation is allowed for author/reviewer edits, without a topic
reread or scientific research. Do not renew other mismatched rows unchecked.
For substantive changes made before the topic audit, Student and Science check the
affected content. During the manager-owned topic audit, the auditor repairs and checks
the affected teaching directly and updates the audit with final hashes. An unresolved
relevant defect blocks dependent release; unaffected work remains approved.

Refresh output input hashes only after checking whether the diff affects that
output. Record the check in its existing evidence/manifest and tracker Notes;
no regeneration is needed for unaffected content. Do not rewrite historical
source inspection claims or merely change hashes to suppress a failed check.
If a skill does not own a dependent output, leave a specific Notes item for its
owner. Retain archived originals for comparison and recovery; no Git required.

## Tracker Notes

Keep existing Markdown, HTML and Lesson questions columns. In managed production, lesson tasks return proposed Notes and session-log lines.
Only the manager writes shared files after final verification. In an explicitly
standalone single-stage task, its owner may write those entries serially.
Use concise dated entries such as `2026-09-11: Reviewer done; clarified units and notation.
Needs refresh: HTML explanation and Q4 answer.` Escape table pipes; use `<br>` to
separate entries when necessary. Notes are the visible change/refresh record, not
a numeric version scheme. Do not reconstruct or invent missing historical checks.

For new work, Markdown completion means the manager's topic audit has passed against
the final lesson hashes. Lesson questions completion also
requires Review Questions and all release gates. Authored or self-checked work alone
does not complete these stages. Preserve historical completion cells and evidence.

Preserve existing completion cells unless completing that stage under its own rules.
A `Needs refresh: ...` note qualifies a historical tick for the named items only.
Never mark all later stages stale simply because one file changed. Record both
what was done and what remains; when an item is resolved, replace its pending note
with a short dated completion while preserving other pending items/history. Keep
long provenance in existing evidence/archive files, with a link if useful.

For parallel production, each worker owns one output directory. Topic Markdown is
read-only after audit. Apply shared tracker/session updates serially, preserving
other workers' entries. No simultaneous writers to the same lesson/output.

Question release uses the current subject structural validator plus explicit manual
release checks in [subject-system.md](subject-system.md) and the practice contract.
The current validator has no strict mode; preserve legacy schemas and scoring. Automated checks verify records and file integrity,
not actual reading, physical truth or teaching quality. Those checks remain
explicit human/agent verification duties inside the owning skill.

## Subject and execution adapters

Read [subject-system.md](subject-system.md) before source-dependent stages. Existing
student-reference skills/registries are preserved for explicitly requested historical
maintenance, outside production; do not invoke sync or add reference UI.
Existing lessons without plans/sidecars keep their historical approvals. When rebuilding
under this workflow, create a sourced plan and extract reviewed interaction/visual
specifications into sidecars without losing student teaching or claiming old reviews
covered new files. Do not bulk-migrate lessons merely to install these skills.

A persistent lesson task owns coordination and handoffs, not every reviewer identity.
Use a fresh independent reviewer within that task, with source artifacts but without
the creator's self-verdict. A model switch in the same conversation is not blindness.
Keep per-lesson writers sequential. If isolated reviewer execution is unavailable,
report the review gate blocked rather than self-certifying independence.

Student and Science cover sidecars as well as Markdown. Each prose editor repairs
any affected exact anchors within its owned sidecars and records hashes. The topic
auditor delegates mechanical anchor reconciliation to the lesson owner and verifies
it before production, preserving final Markdown. Known content defects return to
the responsible stage; there is no automatic post-audit reviewer loop.

Every stage records its actual model/reasoning effort and exact input/output hashes
in its existing evidence/report. Plan uses lesson-plan.json; author/reviews use
lesson-build-evidence.json; audit uses its report; visualization uses HTML evidence;
question creation uses the manifest; question review uses its report.
