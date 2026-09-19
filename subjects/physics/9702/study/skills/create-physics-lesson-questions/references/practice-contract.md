# Physics 20-question practice contract

Create `<lesson-folder>/practice-questions/manifest.json`, exactly 20 question JSON
files, and `assets/` only when needed. Paths in provenance resolve from the Physics
workspace unless explicitly marked as practice-relative.

## Stable IDs

MCQs: `<lesson_id>_mcq01.json` through `_mcq10.json`.
Theory: `<lesson_id>_theory01.json` through `_theory10.json`.
Theory 01-05 are drill, 06-08 medium, 09-10 hard. Display sequences are 1-20.
Multipart IDs append `_a`, `_b`, then lowercase Roman numerals where needed.
Never renumber released IDs.

## Question records

Keep schema `9702_lesson_practice_v1` and existing fields: question/lesson IDs,
sequence, type, difficulty, marks, prompt, options or response structure, answer,
complete mark scheme, hints, solution, teacher walkthrough, outcome IDs, lesson
anchors, definition/formula references, exclusions, assets and verification fields.
Hard questions require per-part enrichment; MCQs require four option explanations.

For new builds, add `origin` to every question and answerable multipart part:

```json
{
  "basis": "past_paper_adapted",
  "source_part_ids": ["<exact inspected canonical part ID>"],
  "lesson_anchors": ["<existing lesson anchor>"],
  "note": "Adapted from Cambridge <paper/part>; describe the actual changes."
}
```

Allowed `basis` values:

- `past_paper_adapted`: source question adapted, including light paraphrase.
- `past_paper_inspired`: independently written, influenced by an inspected demand.
- `lesson_markdown`: no particular question influenced it; `source_part_ids: []`
  and note “Created from lesson Markdown”, with the relevant anchors.

Parent multipart source IDs are the union of part influences. Mixed parts retain
their individual basis; the parent uses adapted if any part is adapted, otherwise
inspired if any part is inspired, otherwise lesson_markdown. Figure provenance is
separate: a Markdown-led prompt may still use an attributed official figure.

`source_mode` for new builds:

- `adapted_official`: adapted source prompt, with or without an official crop.
- `official_figure_new_question`: independent prompt using an official figure.
- `original`: independent prompt with no official figure.

Preserve legacy `official_reuse` records as history; do not produce exact copies
in new sets or relabel old packages. These provenance fields are additive to v1;
existing question IDs and scoring semantics stay unchanged.

Full provenance gives canonical part IDs, package paths, paper/session/variant,
changes or independence explanation, and all figure sources. For each crop record
source path/hash, original dimensions, pixel rectangle `[left, top, right, bottom]`
(right/bottom exclusive), final dimensions/hash and credit. For an unchanged
extracted figure use its full bounds. For each generated image record its actual
method, final dimensions/hash and inspected scientific constraints. ImageGen also records its prompt/style references;
programmatic figures record their drawing/generator sources and inputs as below.
Copied figures remain credited even in adapted questions.

## Manifest

Keep schema `9702_lesson_practice_manifest_v1`: ordered question IDs, distribution,
total marks, input paths/hashes, asset ledger, validation results and unresolved.
Hash Markdown, audit, build evidence, topic evidence index and lesson map.
Record workspace-contract.json as source-system authority; no separate mapping
contract or per-lesson retrieval index is required. Retain an empty exact-reuse ledger for new sets if present.

Add `evidence_inspection` with:

- `cited_part_ids`: every distinct question/part reference in lesson build evidence;
- `parts`: one record per ID with actual question/context files, assets and mark
  schemes read, `status` (`complete` or `unread`), and concise demand/exclusion note;
- `unresolved`: unread files, ambiguous references or relevant scope conflicts.

Deduplicate references, not answerable parts. Shared files can be read once.
Completion requires every cited part inspected, including excluded/context parts.
An explicitly empty source set is recorded honestly, not padded with invented IDs.
Keep the inspection ledger concise; no separate question-by-question research report.

Add `question_origins`: 20 rows with question ID, basis, influencing IDs and a short
origin note, consistent with the question records. This makes each origin reviewable
without reading all enrichment. Record manual content/figure checks separately
from automated record/integrity checks; do not invent successful checks.

## Release checks

- Exactly 10 MCQs, 5 drills, 3 medium and 2 hard questions; sequences 1-20, unique IDs.
- Current topic audit PASS with matching lesson hashes; all cited evidence inspected.
- Every prompt answerable from lesson-owned or supplied information.
- All question and part origins recorded; source IDs resolve to inspected parts.
- Every question independently solved; marks and multipart sums reconcile.
- Four plausible MCQ options, one unambiguous answer, complete answer support.
- All answer-critical assets present, inspected and accurate; delivery assets are raster.
- Faithful source crops credited; original figures use verified ImageGen or programmatic provenance.
- No copied/adapted wording mislabelled as original; no exact-copy questions in new sets.
- All referenced files and hashes valid; `unresolved` empty.

## Release evidence and existing validator

New manifests may record `release_contract: physics_practice_release_v3` as the
manual evidence contract. It does not activate strict validation: the current local
script has no such mode. Preserve v1 schemas, IDs, scoring fields and legacy packages.
Run `python3 scripts/validate_practice_questions.py <lesson-folder>` from the subject
workspace; record its structural outcome separately from all manual release gates.

- `inputs.lesson_markdown`, `topic_audit`, `lesson_evidence`, `retrieval_index`,
  `lesson_map` and `workspace_contract` use path/hash records. `retrieval_index` points
  to the actual topic evidence-index.json; lesson_map to lesson-knowledge-map.json.
  No fabricated `mapping_contract` path is required.
- Audit result/table follows [the shared workflow](../../lesson-workflow.md). V3
  additionally requires the ordered Course Pathway lesson bullets in the topic’s
  `module-lesson-structure.md` to match the audit rows. Missing/unwritten planned
  lessons, duplicate IDs or an unreadable plan block release; existing files alone
  cannot prove completeness. Preserve older evidence as history; do not infer
  that its recorded checks ran on current files.
- Each `evidence_inspection.parts` record uses `part_id`, `status`, `note`,
  `question_files_read`, `required_assets_read`, `mark_scheme_files_read`.
  Read-file lists contain path/hash records. Include previously required assets;
  inspect any additional dependencies discovered in the actual source too.
- Every question has `assets: []` or `assets: [{ "asset_id": "..." }]` pointing to
  `manifest.asset_ledger`, and `verification.independent_solve: true` only after
  the final independent solve. Existing semantic verification fields still apply.
- Each asset ledger row has `asset_id`, workspace-relative `path`, `sha256`,
  `dimensions: [width, height]`, `alt_text`, `visual_verified: true` and `method`.
  `official_crop` additionally requires `source` (path/hash), `source_dimensions`,
  `crop_xyxy`, and `credit`. Its decoded pixels must equal the declared source crop.
  `imagegen` additionally requires `prompt`, `style_references` (path/hash records
  for the saved examples) and a nonempty `verified_constraints` list.
- In v3, `programmatic` requires lossless PNG delivery, a nonempty `method_reason` string,
  `verified_constraints` (a nonempty list of nonblank strings), and `source_files`
  path/hash records for the generator or drawing source and any data inputs. At least one source is `.py`, `.js` or `.svg`;
  the output cannot be its own source. Save subject-owned generator scripts under
  `scripts/practice-figures/<lesson_id>/`; source SVGs may live with practice assets.
  Inspect scientific constraints and independently solve from the delivered PNG.
  Record all actual generator inputs; matching hashes alone cannot prove fidelity.
- Every answerable theory part appears in `response_structure` with `part_id` and
  positive integer `marks`; nested containers use `parts`. Each leaf has matching
  `part_enrichment[part_id]` with `origin`, `answer`, `mark_scheme`, `hints`,
  `solution` and `teacher_walkthrough`. Parent marks reconcile with leaves.
- Each `question_origins` row uses `question_id`, `basis`, `source_part_ids`, `note`,
  matching the question's origin exactly. Parent source IDs unite all leaf sources.

The existing validator checks v1 structure, distribution, required support fields,
Markdown/audit input hashes and mark totals. It does not enforce all release records
above. Manually verify origins, inspected-source coverage, crop pixels, generator
provenance, part marks, input hashes, complete planned topic membership and audit PASS.
Separately verify actual source reading, scientific truth and solving. Record checks
honestly; structural PASS alone is not production PASS.

## Independent lesson drafts

New draft sets use the v1 question schema plus v3 manual evidence fields and checks, with
`delivery_status: review_preview`, `production_status: incomplete` and an explicit
unresolved topic-audit blocker when absent. Do not invent the missing audit's path
or hash. Production release remains blocked until actual release inputs exist and all
blockers are resolved, regardless of any structural validator result. Question review may still record its
separate content result. After the topic audit, inspect impacts, refresh affected
inputs and rerun structural validation and all manual release gates before any tracker completion.

New work requires pre-audit Student/Science coverage and the manager's final audited
Markdown/sidecars. Student-reference sync and new reference integration are outside
production; preserve historical reference records without silently migrating them.
Taught/supplied scope determines assessability.
