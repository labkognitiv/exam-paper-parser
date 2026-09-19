# Physics student-reference contract

Authored study support, separate from the controlled knowledge definitions/formulas.
One sync invocation runs after lesson Student and Science reviews. It finds needed
clarifications, checks existing entries, writes new brief explanations and saves IDs
and lesson links. No separate draft file or reference-review stage is required.

## Storage

- `study/student-reference/registry.json`: schema `9702_student_reference_v1`,
  `entries` array. Entries are shared across lessons.
- `<lesson-folder>/student-reference-links.json`: schema
  `9702_student_reference_links_v1`; the final occurrence map produced by sync.
  Derive reverse lesson-ID lists from these maps rather than maintaining two lists.

No entries or maps were populated under the former draft contract. Historical
instructions and evidence stay archived; do not invent prior approvals.

## Shared entry

Each entry contains a stable `concept_id` (`9702_ref_<meaningful_slug>`), `payload`,
`payload_sha256`, `checks` and `sources`.

`payload` contains `term`, `sense` (brief disambiguation), `aliases` (including useful
plural/abbreviation forms), `explanation`, optional `example`, and optional existing
`definition_id`/`formula_id`. Cover all important clarifications needed by the
lesson, whether or not a formal definition exists. Keep explanations short and
self-contained, including qualifications needed for accuracy. Images come later.

Hash payload UTF-8 JSON with
`json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(',', ':'))`.
`checks` contains `checked_by: sync-physics-student-reference`, exact `payload_sha256`,
date, `clarity: PASS|FAIL|BLOCKED`, `scientific_accuracy: PASS|FAIL|BLOCKED`, and a
brief note. Sources name actual inspected passages (path/URL and section/page),
including the reviewed lesson location when its explanation is reused.
Only publish entries with both checks PASS for the current payload. These are
sync-time checks, not claims of an independent Student/Science review of new text.
Stored wording is student explanation unless an official quotation was verified
and attributed. Controlled registry presence alone is not verification.

Exact names/aliases are lookup candidates, not semantic proof. Same meaning reuses
one ID; distinct meanings can share spelling. Do not create an extra entry or extend
an existing explanation for each lesson. A correction preserves the old payload
and names affected consumers; mismatched hashes require targeted refresh.

## Lesson links

The final map records `lesson_id`, `markdown: {path, sha256}`, `links`, `sync_id` and
`unresolved: []`. Each link has `concept_id`, `payload_sha256`, `occurrences`,
`context_sha256` and `context_check` (checked_by, date, result, concise note).

An occurrence has exact `section` heading/anchor, `text` span, one-based
`occurrence_index` among exact matches in that section, `role` (taught, reminder,
mentioned or practised), and `availability` (teaching or after_reveal). Use full
heading paths to disambiguate repeated headings. Only mark taught when the passage
explains it; a mention is not proof of teaching or student recall. Cue metadata
cannot serve as a learner-facing text location. Visible diagram/caption terms need
an identifiable rendered target.

Compute `context_sha256` from canonical JSON of `markdown_sha256`, `payload_sha256`
and `occurrences`. Sync records a PASS context check for the exact hash after
checking sense, location and availability. Reused entries still need this local
fit check. If Markdown or payload changes, inspect the impact before updating hashes.
Consumers verify current payload checks, context check, hashes and actual locations.
An empty checked map is valid when no terms need support. Unresolved intended links
keep the map pending; never publish a partial map as complete. Record unresolved
items in existing lesson evidence/Notes and preserve the previous map until resolved.

## Shared writes and snapshots

Parallel lessons may read/prepare independently. Before mutation, acquire exclusive
ownership with atomic directory creation at `study/student-reference/.merge-lock`.
Reload and repeat semantic matching while holding it; save only once per sync run.
An occupied lock means retry later; do not remove another writer's lock. Release
only this invocation's lock in finally cleanup. Read-only lookup is advisory; the
locked reload decides what can be added.

Archive original registry/map files and their path/hash manifest under
`study/archive/<date>-student-reference-<sync_id>/`. Stage proposed complete files
there; record destinations/hashes with status pending, atomically replace each
file from a same-filesystem temporary file, verify final hashes/links, then mark
complete. This is an internal save operation, not a second skill invocation.
Recover interrupted saves by comparing current, staged and original hashes; never
overwrite unexplained edits. An incomplete transaction blocks affected consumers.

Consumers snapshot registry/map together under the same lock and recheck pinned
hashes before completion. Release the lock while rendering. Unrelated registry
additions do not invalidate a lesson. Preserve other lessons' maps and unused entries.
The lookup helper reads one atomically replaced registry file; it never mutates it.

## Rendering

Bundle the lesson's checked entries locally for offline HTML. Record entry IDs,
payload hashes and map hash in HTML evidence. Render the saved wording unchanged.
Understated underline triggers open a right-side panel on desktop and a suitable
mobile panel. Support keyboard use, explicit close/Escape, focus return and preserved
reading position. Avoid hover-only controls and underlining every repeated word.
Keep the approved definition cards. Essential new teaching remains visible inline.

Do not enable reference controls or revealing tooltips/accessible names inside
assessment prompts/options before an attempt/reveal. Links may appear in revealed
feedback. Test no-JavaScript support separately: assessment-only references belong
behind native reveal controls; print answer support follows the questions. Normal
taught reference material remains accessible; this is a learning page. Check final
mobile/print/fallback rendering rather than treating valid JSON as UI verification.
