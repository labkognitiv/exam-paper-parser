# Physics 9702 controlled syllabus spine (2025-2027)

## Scope

This directory separates the official curriculum spine from later question mappings, enrichment and generated learning products.

```text
2025-2027/
├── as/
│   ├── 9702-2025-2027-as-taxonomy.json
│   └── 9702-2025-2027-as-learning-outcomes.json
└── a2/
    ├── 9702-2025-2027-a2-taxonomy.json
    └── 9702-2025-2027-a2-learning-outcomes.json
```

## Stable IDs

- Topic: `9702_tNN`
- Module: `9702_tNN_mNN`
- Learning outcome: `9702_tNN_mNN_oNN`

Examples:

- Topic 7 Waves: `9702_t07`
- Module 7.1 Progressive waves: `9702_t07_m01`
- Its fourth official learning outcome: `9702_t07_m01_o04`

The files are versioned by directory and carry `syllabus_years`, so a later syllabus version must be stored separately and compared explicitly.

## Counts

| Level | Topics | Modules | Learning outcomes |
|---|---:|---:|---:|
| AS | 11 | 32 | 145 |
| A2-only extension | 14 | 44 | 155 |

Cambridge labels topics 12-25 as **A Level subject content**. `a2` is used here only to distinguish that extension from the AS topics.

## Source and status

- Official PDF: `output/physics/syllabus/664565-2025-2027-syllabus/664565-2025-2027-syllabus.pdf`
- Official PDF SHA-256: `1cba1cdca33c51a39dd6dfdc69d612f48967abcd89b6ceacdf9ffd6fa2e2b195`
- AS source pages: 16-25
- A2 source pages: 26-39
- JSON is the canonical format for structured curriculum data. CSV may be generated temporarily for external review or compatibility, but is not stored as a source of truth.
- Both taxonomy JSON files are deterministically checked for unique topics/modules and complete hierarchy references.
- Learning-outcome IDs and numbering are deterministically checked for complete sequential numbering within every module.
- Outcome wording is extracted from the official PDF with page provenance. Mathematical typography remains plain extracted text and must be normalised into a separate LaTeX-bearing knowledge layer before formulas are used for generation or automated checking.

## Boundary

These files contain no lessons, micro-skills, question mappings, difficulty, solutions, rubrics or generated learning content.
