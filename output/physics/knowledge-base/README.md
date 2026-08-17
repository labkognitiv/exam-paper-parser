# Physics 9702 knowledge base

This directory contains structured, reusable knowledge derived from the official syllabus and canonical past-paper corpus.

```text
knowledge-base/
├── curriculum/                 Official topic, module and outcome IDs
├── enrichment/
│   ├── p1/                     One enrichment JSON per P1 question
│   └── p2/                     One enrichment JSON per complete P2 question
├── knowledge/
│   ├── definitions.json        Canonical definitions
│   ├── formulas.json           Major syllabus physics formulas only
│   ├── skills.json             Controlled skill library
│   └── question-patterns.json  Controlled searchable question patterns
├── contracts/                  JSON Schemas
└── templates/                  Valid starter records
```

## Boundaries

- Canonical question and mark-scheme files remain in their existing locations.
- Enrichment references canonical question, part, criterion, taxonomy and knowledge IDs; it does not duplicate source files.
- Definitions and major syllabus physics formulas are stored once. Later occurrences add evidence references instead of creating duplicates.
- Search patterns use the controlled `question_patterns` vocabulary at part level; each whole-question list is the union of its parts.
- Student attempts, marks and mastery state do not belong here.
- Lessons, revision notes and cheat sheets are generated products and are not canonical knowledge records.

## First pilot

Do not run a corpus batch yet. Populate and validate one representative question first, then revise the contracts only if that real question exposes a missing requirement.
