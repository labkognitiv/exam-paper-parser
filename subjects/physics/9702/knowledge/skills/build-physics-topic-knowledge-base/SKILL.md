---
name: build-physics-topic-knowledge-base
description: Build and independently verify one canonical Cambridge Physics 9702 topic knowledge base before lesson authoring, including exact syllabus records, P2 evidence indexes, a prerequisite-safe course pathway, controlled lesson mappings, and lean module and lesson specifications; excludes learner lesson content and supports explicit P1 deferral.
---

# Build Physics Topic Knowledge Base

Build one topic under:

`subjects/physics/9702/study/topics/<topic_id>_<topic_slug>/`

This is pre-authoring work. Do not create learner-facing notes, questions, mark
schemes, enrichment, diagrams, prototype files or generated assets.

## Read first

From the repository root, read completely:

1. Repository `AGENTS.md`, then the nearest scoped `AGENTS.md` and context.
2. `subjects/physics/9702/AGENTS.md` and the current git status.
3. The finalized Kinematics and Dynamics topic folders as structural examples.
4. The AS taxonomy and learning outcomes for the requested syllabus version.
5. `knowledge/definitions.json`, `formulas.json`, `skills.json` and
   `question-patterns.json`.
6. Every in-scope P2 enrichment record.
7. Recent topic handoffs or approved architecture decisions when present.

Use the official syllabus as curriculum truth and P2 enrichment as assessment
evidence. Preserve unrelated dirty-worktree changes.

## Scope lock

Before writing, record:

- exact topic ID, official topic name and syllabus version;
- all official Cambridge module and outcome IDs;
- whether P1 mapping is included or deferred;
- the allowed output root; and
- explicit exclusions for learner content and official-source edits.

If P1 is deferred, write that state into the topic plan, lesson map, Cambridge
module records and every lesson specification. Do not create a P1 index.

## Two module layers

Keep these layers distinct:

- **Cambridge modules** reproduce the official syllabus headings exactly.
- **Course modules** are smaller prerequisite-safe teaching groups designed by
  Kognitiv.

Do not force the same course-module count across topics. Split only where a
meaningful prerequisite, representation, procedure or knowledge boundary would
otherwise overload a module. Preserve stable IDs:

- Cambridge module: `<topic_id>_mNN`
- Course module: `<topic_id>_cmNN`
- Lesson: `<course_module_id>_lNN`

## Evidence inventory

Reconstruct topic evidence from the real P2 enrichment files:

1. Select only answerable leaves whose
   `mapping.primary_topic_id == <topic_id>`.
2. Retain each whole question through `question_id` and
   `enrichment_path`.
3. Store only the selected topic `part_ids` in the topic index.
4. Build each Cambridge-module index from
   `mapping.primary_module_id`.
5. Allow one whole question to occur in more than one module index when its
   leaves span modules.
6. Preserve ordered part identity, mixed-question context and
   occurrence-aware reconciliation by reference.
7. Never copy an official question, mark scheme, diagram or canonical question
   package into the topic folder.

Report unique whole-question and answerable-part counts. Module question counts
may overlap; module part counts must sum to the topic part count because each
leaf has one primary module.

## Controlled knowledge audit

For each official outcome, identify only the definitions, formulas, skills and
question patterns needed by the topic.

- Reuse existing controlled IDs.
- Treat cross-topic IDs as prior or supplied context unless the current
  syllabus explicitly requires them.
- Do not import later-topic knowledge merely because a mixed P2 question uses
  it.
- If a genuinely required controlled formula is absent, add one narrowly
  scoped record to `knowledge/formulas.json` with a unique stable ID and valid
  P2 evidence. Do not add speculative convenience formulas.
- Record syllabus or P2 evidence gaps honestly instead of assigning unrelated
  evidence.

## Design the pathway

Create the smallest course pathway that teaches every official outcome without
premature knowledge.

For every lesson decide:

- stable lesson ID and title;
- exact outcome IDs;
- controlled definition, formula, skill and question-pattern IDs;
- representative P2 leaf evidence IDs;
- immediate previous lesson;
- all completed previous course modules;
- external prerequisite topics;
- prior knowledge;
- learning goals;
- genuinely new learning;
- not-yet-taught knowledge;
- explicit inside/outside boundary; and
- next-lesson handoff.

Order procedural dependencies explicitly. Examples include momentum before force
as momentum rate, drag before terminal velocity, and one-dimensional vector work
before two-dimensional applications. These examples are not universal lesson
templates.

Every selected evidence leaf must resolve, have the requested topic as its
primary topic and share at least one mapped outcome with its lesson. Use
whole-question evidence for integrated application only after its component
methods have been taught.

## Required output

Create:

```text
<topic-root>/
├── syllabus.json
├── p2-evidence-index.json
├── lesson-knowledge-map.json
├── module-lesson-structure.md
├── modules/
│   └── <cambridge-module>/
│       ├── module.json
│       └── p2-evidence-index.json
└── course-modules/
    └── <course-module>/
        ├── module.json
        └── lessons/
            └── <lesson>/
                └── lesson.json
```

`syllabus.json` must copy the controlled taxonomy and outcomes exactly.

Each Cambridge `module.json` must list its outcomes, all mapped lesson IDs,
P2 index and source records.

Each course-module `module.json` must aggregate its lesson IDs, outcomes,
definitions, formulas, taught concepts, usable skills, prerequisite course
modules and handoff.

Each lean `lesson.json` must contain mapping, prerequisites, prior knowledge,
learning goals, new learning, not-yet-taught, knowledge boundary, P2 evidence,
source records and downstream authoring status. Set notes, questions,
markscheme, enrichment and visual assets to `not_created`.

The Markdown plan must list the complete pathway and explicitly state structure
status, P1 status, downstream-content exclusion and official-source boundary.

## Deterministic verification

Treat every failure as blocking. Verify:

- every JSON parses;
- exact taxonomy and learning-outcome equality with controlled curriculum;
- Cambridge module, course module and lesson counts;
- stable-ID uniqueness and sequence continuity;
- full outcome coverage with no unknown outcomes;
- every definition, formula, skill and pattern ID resolves;
- lesson map and lesson specifications agree exactly;
- every selected P2 part exists, is primary to the topic and overlaps the
  lesson outcome mapping;
- topic P2 index exactly reconstructs from enrichment;
- question, part, enrichment-path and module identity;
- module evidence indexes exactly reconstruct from the topic index;
- course-module and Cambridge-module aggregation;
- immediate lesson and cumulative course-module prerequisites;
- all declared source paths;
- P1 absence when deferred; and
- absence of downstream lesson files, visual assets, symlinks or copied
  official packages.

Also run `jq empty` over every created or changed JSON file.

## Independent completion gate

Use an independent agent to inspect the real completed files read-only. Require
it to reconstruct the evidence indexes, resolve every controlled ID, audit the
pathway and boundaries, inspect scoped git status and return `PASS` or exact
actionable defects.

Repair every defect and rerun deterministic and independent verification. Do not
finish with a partial structure or a provisional pass.

## Completion report

Report:

- official Cambridge modules and outcomes;
- proposed course modules and lessons;
- exact files changed;
- P2 whole-question, part and module counts;
- controlled registry additions;
- deterministic validation result;
- independent verdict;
- P1 status;
- remaining evidence limitations; and
- confirmation that learner packages and official/canonical extraction were
  untouched.

Do not commit, push, merge or begin lesson authoring unless the user separately
requests it.
