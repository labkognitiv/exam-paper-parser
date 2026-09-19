# Physics production system

Read `workspace-contract.json` and the nearest instructions before source work.
Paths below resolve from `subjects/physics/9702/`.

## Curriculum and question evidence

- Discover topic membership/order from `study/topics/<topic>/module-lesson-structure.md`.
  Use topic `syllabus.json`, `lesson-knowledge-map.json`, and each `lesson.json`
  for scope, prerequisites and lesson-owned evidence IDs. Resolve retired IDs through
  `study/lesson-id-redirects.json`; do not author retired aliases or alter redirects.
- Retrieve candidates through the topic `evidence-index.json`, filtered against
  the lesson map and outcomes. An index hit is a candidate, not proof of lesson fit.
  Preserve existing mapping decisions and provenance; do not impose another subject's
  mapping method, per-lesson retrieval index, or mapping-contract file.
- Resolve canonical packages under `past papers/<component>/<year>/<session>/variant-N/`.
  P1 retains complete MCQ assets and official answers; P2/P4 retain whole `question_NN`
  packages, shared context and dependencies. Inspect actual prompts, figures and mark schemes.
  Missing paths are evidence gaps, never a reason to invent a source or use an archive fallback.
- Official PDF binaries live at repository-root `pdfs/physics/9702/`;
  existing package `source/` links remain compatible. Do not modify official sources,
  mappings, reconciliation exceptions, scoring semantics or `numerical_values_checked`.

## Definitions and formulas

Formal definitions must exactly match `knowledge/knowledge-base/definitions.json`.
Read `knowledge/knowledge-base/formulas.json` for controlled formulas; preserve IDs,
notation, units and conditions. Stored records do not prove Cambridge provenance:
inspect cited sources before claiming it. Report conflicts without changing registries
or substituting paraphrases for controlled definitions. Check dimensions, SI prefixes,
scalar/vector distinctions, signs, significant figures, uncertainty and assumptions.

## Existing practice validator

From the subject workspace run:

```sh
python3 scripts/validate_practice_questions.py <lesson-folder>
```

Pass the actual lesson directory, not a guessed alias. The current script has no
`--strict` mode. Its PASS is structural only: separately verify topic PASS and complete
planned membership, current hashes, review coverage, origins, every cited source read,
asset provenance/pixels, independent solutions and all manual release checks in the
practice contract. Record structural and manual results separately. Missing evidence
blocks production; never claim unimplemented strict checks ran. Preserve existing v1
schemas, question IDs, fields and scoring semantics. Do not modify validators as part
of lesson production.
