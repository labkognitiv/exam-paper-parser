---
name: author-physics-lesson-markdown
description: Write one Physics 9702 lesson from its approved lesson-plan.json - the student prose in lesson.md plus the visual and activity sidecars. Consumes the researched plan and verifies quoted sources without repeating candidate selection.
---

# Author Physics Lesson Markdown

Read [subject-system.md](../subject-system.md) for actual paths, source authority
and validator interface. In managed runs, tracker/session instructions mean return
proposed lines to the manager; only the manager writes shared files. Record actual
model and reasoning effort in this stage's evidence.

Write the lesson the plan describes. Follow the shared
[lesson workflow](../lesson-workflow.md) for order and impact-based refresh, and update
the affected tracker Notes cell.

You are stage 2. [plan-physics-lesson](../plan-physics-lesson/SKILL.md) is stage 1 and
has already read the sources, chosen the concepts, graded their depth, fixed the
teaching order and assigned each visual its method. Read `lesson-plan.json` first and
in full. Do not redo that work, and do not overrule it: the scope, depth grades and
teaching order are binding. If a decision looks wrong, report it as a defect for the
planner rather than quietly changing it.

Create `lesson.md`, `lesson-visuals.json`, `lesson-activities.json`, and
`lesson-build-evidence.json` recording the plan hash you consumed, anything you added,
and the review history that follows. Use the
[build evidence schema](references/lesson-build-evidence-schema.md).

**Read the real sources for anything you quote or explain.** The plan names them and
records what it found; it does not replace reading them. Verified wording is copied from
its recorded source path, not retyped from the plan. Nuance a student needs often lives
in the raw mark-scheme text and survives no summary.

**The plan is a floor, not a ceiling.** If you find a misconception, a demand or a
necessary explanation the plan missed, add it and record it under `writer_additions`
with its source. The same applies to a visual or an activity the teaching clearly needs
and the plan lacks: add it, assign its method from the required treatment table, and
record it as an addition. Do not remove one the plan specified; report it instead. A plan that caps quality has failed; silently dropping something it
missed is worse.

Turn depth grades into prose:

- `develop`: build it from its parts, work a concrete example, give it a retrieval
  opportunity. This is where the lesson spends its length.
- `explain`: explain it properly and compactly. No worked example needed.
- `mention`: one sentence in passing.
- `remind`: one sentence of reminder, then move on. Never re-teach it.
- `exclude`: name it as out of scope where a student would expect it, and move on.

Follow `teaching_order`. Preserve the plan's concept set, section ownership and lesson
position. Create every example, activity and explanation fresh; the plan supplies
findings, never wording.

## Write the hook

The plan names the historical investigation and supplies its verified facts. You write
the prose. Do not pick a different investigation; if the one you were given is not
genuinely this lesson's spine, report it to the planner rather than substituting one.

Open with a nontechnical story, observation or mini-mystery. There is no length rule. A
hook is as long as it needs to be and no longer: some lessons turn on a single startling
observation, others on a problem that took years to crack. Judge it by the tests, never
by line count.

A hook carries four things: a **specific unsolved problem** stated so a beginner feels
it, not "a discovery that helped us understand life" but what was actually stuck; **why
it resisted**, briefly, which is what makes the answer feel earned; a **concrete
finding** in everyday words, or two where the lesson has two halves; and a **closing
question the lesson will answer**.

Apply four tests to what you wrote. Each is pass or fail and a failure is rewritten:

- **Generality.** Would the closing question fit three other lessons in this subject? If
  yes it is too generic. "What would you need to know to describe its structure?" fits
  any molecule ever studied and fails. A question that restates this lesson's own spine
  in plain words passes.
- **Vocabulary.** Does any technical term, molecule name or unexplained scientific
  vocabulary appear before the story ends? If yes, cut it. The hook runs on everyday
  words; terminology arrives afterwards.
- **Ownership.** Does the hook centre on this lesson's owned learning, without
  requiring a later lesson to answer it? If not, report a plan defect.
- **Return.** Does the close answer every part of the question the hook asked, under a
  heading that names the story? A hook never returned to is incomplete, and a bullet
  recap does not satisfy this.

Use only the facts the plan verified, or verify a new one against a real source and
record it. Invent no quotations, thoughts or events about real people. Keep biography to
what the lesson needs.

This skill supplies no specimen hook. A sample gets copied instead of thought about,
which has already happened once in this corpus.

After the close, give a compact recap and handoff to the next lesson.

## Write like a teacher

Assume the student is new to the topic and may have weak prior knowledge. Be
patient and respectful, never condescending. Explain the very basics rather than
assuming technical names, symbols or diagram conventions are obvious. Start with
the generic idea and its parts before named examples: for forces, define the body, interaction and direction before resolving components.

Keep official syllabus outcomes, outcome IDs and curriculum instructions out of
student-facing Markdown. Translate goals into a brief natural-language introduction
only when useful. This does not remove verified verbatim definitions, formulas or
official answers where they support learning; retain their simple explanations.

Write for a **17- or 18-year-old student**, using “you”, familiar examples and
guided reasoning. Keep sentences clear, vocabulary simple and paragraphs easy to
follow. Detail is welcome; dense language is not. Follow the shared paragraph rule: short connected paragraphs, one main idea,
with enough space for the reasoning; no sentence or displayed-line quota. Break up a long
explanation with a useful subheading, visual cue, example, comparison or brief
list. Use lists for components or steps, not as a replacement for explaining why.
Keep the teacher's conversational flow and purposeful repetition; spread depth
across small connected chunks rather than large blocks of prose. Markdown itself
must be easy to scan; do not leave this work to the visualizer. Avoid unnecessary jargon and
explain essential physical terms when first introduced. Move from observation
to plain meaning, then precise terminology and application.
Explain how and why; build connected teaching rather than compressed textbook
notes. **The explanation is the backbone of the lesson.** Develop each concept
through connected prose, a concrete example or comparison, and the reasoning a
student needs before asking them to practise. Activities, answers and feedback
must not carry essential teaching missing from the explanation. Do not rush from
a short fact list straight into an activity.

Repeat important ideas deliberately: explain them simply, revisit them through a
different example or visual, retrieve them in an activity, and connect them again
later. Repetition helps learning; vary the context or reasoning while keeping the
core terminology consistent. Preserve helpful reminders and recaps rather than
removing them as duplication. Add depth within scope, not unrelated extra facts. Use another lens or analogy when helpful, and explain its limits.

### Two rules that stop the jumping

Both are pass or fail, and both are checkable against the finished file.

**Nothing is used before it is explained.** Every technical term, symbol and diagram
convention must have its explanation earlier in the document than its first working
use. "Explained earlier" means the student could state what it is from what they have
already read, not that the word has appeared before. A term introduced inside an
activity option, a feedback branch or a worked answer, with no prose behind it, fails
this rule. Read the lesson once in order and find the first line where a student with
the stated prerequisites would be lost; if such a line exists, repair it before
finishing. Sort each idea into its tier first: tier 1 is taught in full, tier 2 gets one
plain sentence at the point of need, tier 3 gets a one-sentence reminder. Most jumping
is a tier 1 idea that was written as though it were tier 3.

**A list never replaces the reasoning.** No mechanism, process or structure-function
relationship may be presented as a bulleted list of properties without prose saying why
one thing follows from another. Lists are for genuinely parallel items and ordered
steps. A stack of definitions is a glossary, not teaching: if a section could be read in
any order without loss, it is not explaining anything.

Cover every owned outcome and introduce prerequisites before using them. Connect
structure to function and mechanism to outcome. Work through original examples,
showing reasoning, units and conditions for calculations or data interpretation.

For each worked example, separate **Answer** from **Explanation**. First give a
complete, precise exam-style answer, including required reasoning, working, units
and conditions. Then explain separately in easy language how to reach it and why
it works. The explanation must not substitute for the proper answer. Original
worked answers are not official Cambridge answers. Keep verified official answers
and definition wording verbatim when used; place plain-language explanations
alongside them rather than rewriting the quoted wording. Never label unverified
wording as official.

## Teach through activities

The plan lists the activities: which concept and reasoning step each retrieves, its
interaction type, and the misconceptions its distractors must address. You write them.
Record justified additions under `writer_additions`. Report removals, changed
interaction types or changed requirements as plan defects before proceeding.

Teach, invite an action, explain the feedback, then build on it. Place each activity
after the teaching it retrieves, never before.
### Answer controls

For automatically checked activities, always provide selectable blocks/options:
single-choice MCQs, multiple selection, label selection, matching, ordering,
classification or formula assembly from supplied blocks. Vary the reasoning and
interaction, not just the number of choices. State whether to select one or all
that apply. Blanks and error correction must use supplied choices, not typed text.

Never require students to type an answer for automatic checking, including short
labels, numbers, explanations or subjective responses. Do not specify exact-text,
keyword or AI grading of written answers: a student entering “speed” when the
model says “velocity” must not encounter a brittle text-matching checker.
Instead, offer complete terms as options and explain the scientific distinction.

Optional written reflection is allowed only as **ungraded self-check**: let the
student think or write, then reveal a model answer and explanation for comparison.
Specify **Reveal model answer**, with no Check/Submit-for-grading control, score,
correct/incorrect verdict or conditional feedback based on their writing. Prefer
selectable activities; use this exception only when writing supports the learning.

Specify each activity in the activity sidecar (see Sidecars below) with: stable id,
anchor, title, checking mode (`selection` or `ungraded self-check`), action, prompt,
the supplied options or items, the correct selection, and one feedback branch per
selectable option. For self-check, supply the model answer and comparison guidance
instead of correct/incorrect feedback.

Every selectable option gets its own feedback naming the specific misconception that
choice represents. A single blob of feedback covering several wrong options fails this.
Every distractor's vocabulary must already be taught in the prose before the student
meets it as an option.

The Markdown owns the learning; the sidecar owns the interaction; the visualizer builds
the controls. A student reading only the Markdown must still be able to follow the
lesson to its end.

## Write the visuals

The plan lists the visuals: what each must teach, its assigned `method`, and for a
paper-linked visual its `asset_path`, `mode` and `observed_features`. You write
`what_to_show` and `what_to_notice` for each.

**You may not change an assigned method.** If one looks wrong for the teaching, report
it as a plan defect. The method is assigned once, by the planner, from the
[required treatment table](../visualize-physics-lesson/references/physics-visual-design.md#method-by-teaching-need);
that is what stops the same lesson family coming out as generated art in one build and
hand-drawn vector in another.

Write each description against the plan's `observed_features`, not against a paper code
or your memory of the figure. A description that contradicts what was actually observed
in the asset is a defect: report it rather than writing what you assume is there.

You decide where each visual sits, by writing its `anchor`. The plan fixes what the
visuals are and the order of the concepts; placement within the prose is yours. Sequence
them with the explanation: a visual must never require terminology or a
recognition feature taught later. Show generic structure before specialised forms.
Qualify a recognition shortcut to the diagram or context where it actually works, and
distinguish what a visible clue establishes from what it cannot prove.

## Sidecars

`lesson.md` is the student's document. It contains teaching prose and nothing else: no
visual cue blocks, no activity specifications, no checking modes, no paper codes, no
figure references, no rendering modes, no instructions addressed to an illustrator, and
no sentence written about the student rather than to them. Most lessons are read as
Markdown before any page is built, so anything left in this file is shipped.

Production detail moves to two sidecar files beside it:

- **`lesson-visuals.json`**: one entry per visual: `id`, `anchor`, `purpose`,
  `method`, `what_to_show`, `what_to_notice`, and for a paper-linked visual
  `source: {paper, part, figure, asset_path, mode}`.
- **`lesson-activities.json`**: one entry per activity: `id`, `anchor`, `title`,
  `checking_mode`, `action`, `prompt`, `options`, `answer`, and `feedback` keyed by
  option.

An `anchor` locates the entry without putting a marker in the prose: the full heading
path plus a short exact quote of the sentence it follows. A quote that no longer matches
the Markdown is a hard error for the visualizer, not something to guess around.

Write the prose so it reads completely without either sidecar. A student who never sees
a diagram or attempts an activity must still be able to follow the lesson to its end.

## Hand off to the two reviews

Use [Review Student](../review-physics-lesson-student/SKILL.md) for understanding
and language, then [Review Science](../review-physics-lesson-science/SKILL.md) for
factual verification. The manager runs the topic audit after every lesson in the topic
passes both reviews. Earlier lessons need not exist; preserve the planned order.

## Finish

Read once as a beginner: is every essential term explained before use, does each
visual follow what has been taught, and do identification claims stay within the
available evidence? Check nearby lesson boundaries and remove official outcome
quotations from learner prose. Check scope, teacher voice, opening and closing connection, verified wording,
complete purposeful activities and visuals. Check that every
automatically checked response uses supplied selectable options and any written
response is explicitly ungraded with model-answer reveal only. Validate the evidence
JSON and keep its sources, decisions and unresolved items truthful.
After the manager's topic audit passes on the final hashes, mark its `Markdown` cell ✅
in `study/LESSON-PRODUCTION-TRACKER.md` and append a concise dated handoff to
`study/SESSION-LOG.md`. If only authoring was requested, record “authored; reviews and
topic audit pending” in Notes and leave completion pending. Never mark incomplete work
complete. Production release waits for the complete topic audit.
Single-lesson HTML previews and draft questions may proceed under the shared workflow. The topic-audit skill repairs Markdown directly and
records remaining defects for revision and re-audit.
