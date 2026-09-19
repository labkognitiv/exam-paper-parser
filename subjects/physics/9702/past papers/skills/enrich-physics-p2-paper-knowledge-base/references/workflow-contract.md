# P2 enrichment contract

Create one enrichment JSON per whole structured question in `subjects/physics/9702/enrichment/p2/`. Include answerable leaves by immutable canonical `part_id`.

## Question fields

- schema, enrichment, question, and component IDs;
- intrinsic difficulty from 1 to 5;
- first-occurrence ordered union of leaf question patterns; and
- first-occurrence ordered unions of topic, module, and syllabus-outcome IDs.

## Leaf fields

- intrinsic difficulty and smallest truthful controlled pattern set;
- one primary topic, module, skill, and applicable outcomes;
- only necessary supporting skills, definitions, and major formulas;
- one to five progressive question-specific hints;
- a complete teacher-style walkthrough with recomputed arithmetic; and
- deterministic, AI, or hybrid checking with exact official-criterion bindings.

The AS syllabus controls mappings. Assessment evidence controls skills, patterns, and difficulty. Keep contextual questions whole. Search registries by ID, wording, and meaning before adding anything. Never create semantic duplicates.

Use deterministic checking only when structured values establish every mark. Use AI for meaning, reasoning, explanations, definitions, derivations, or drawings. Use hybrid when both are credited. Every official source criterion must be bound exactly once, including alternatives, and scoring must be capped by canonical marks.

Hints must progress from concept to method without early answers. Walkthroughs must show equations, substitutions, arithmetic, units, directions, and conclusions. Ban generic boilerplate. Empty definition or formula references on matching task patterns require a specific justification.

Final checks: schema validity; identical answerable part sets or explicit reconciliation; matching question totals and 60 paper marks; all IDs resolve; exact ordered unions; complete hints and walkthroughs; consistent checking; unchanged sources; `numerical_values_checked: false`; no duplicate registry meanings; and independent verifier PASS.
