# Physics lesson build evidence

Write `<lesson-folder>/lesson-build-evidence.json` during authoring from the
inspected plan, distinguishing planner inspection from new author inspection.
Record plan path/hash, writer_additions, model/reasoning_effort and sidecar hashes.

```json
{
  "schema_version": "9702_physics_lesson_build_evidence_v1",
  "lesson_id": "9702_topic_module_lesson",
  "generated_at": "YYYY-MM-DD",
  "scope": {
    "outcome_ids": [],
    "current_boundary": "",
    "topic_scope_map_path": "",
    "prior_scope_summaries_consulted": [],
    "immediate_previous": {"lesson_id": null, "boundary": "", "can_assume": []},
    "immediate_next": {"lesson_id": null, "boundary": "", "must_not_preteach": []}
  },
  "sources_visited": [
    {"path": "", "kind": "lesson_spec|topic_map|syllabus|knowledge_reference|question_typology|past_paper|mark_scheme", "purpose": ""}
  ],
  "candidate_sample": {
    "mapping_method": "record_actual_topic_index_provenance",
    "available_candidate_count": 0,
    "selection_dimensions": [],
    "shortage_reason": null
  },
  "question_parts_inspected": [
    {
      "part_id": "",
      "source_path": "",
      "question_files_read": [],
      "required_assets_read": [],
      "mark_scheme_files_read": [],
      "diagrams": [
        {
          "figure_id": "",
          "asset_path": "",
          "pdf_page_1based": null,
          "figure_label_or_location": "",
          "recognition_to_teach": "",
          "markdown_cue_id": "",
          "mode": "recreate_original|reuse_official",
          "source_credit": ""
        }
      ],
      "component": "p1|p2|p4",
      "year_session_variant": "",
      "mapped_outcome_ids": [],
      "semantic_decision": "used|rejected|context_only",
      "decision_reason": "",
      "lesson_relevant_demand": "",
      "archetype": "",
      "reasoning_or_distractor": "",
      "lesson_sections_informed": []
    }
  ],
  "definitions_considered": [
    {
      "definition_id": "",
      "term": "",
      "record_path": "",
      "evidence_question_ids": [],
      "verification": "verified|unverified|conflict",
      "decision": "used|not_applicable|deferred",
      "reason": "",
      "markdown_anchor": null
    }
  ],
  "formulas_considered": [
    {
      "formula_id": "",
      "name": "",
      "record_path": "",
      "evidence_question_ids": [],
      "verification": "verified|unverified|conflict",
      "decision": "used|not_applicable|deferred",
      "reason": "",
      "markdown_anchor": null
    }
  ],
  "coverage_checks": {
    "all_outcomes_taught_within_boundary": false,
    "topic_scope_separation_respected": false,
    "saturation_reached_or_shortage_explained": false,
    "every_opened_part_has_semantic_decision": false,
    "major_lesson_archetypes_covered": false,
    "all_knowledge_candidates_accounted_for": false,
    "unverified_knowledge_not_presented_as_controlled": false,
    "examples_are_original": false
  },
  "unresolved": []
}
```

Rules:

- Record only files and parts actually opened. Set `mapping_method` from the
  current mapping provenance; do not assume a legacy method.
- Count answerable parts, not parent questions, in the sample. Count only parts
  whose actual wording, shared context and required visual/table assets were read.
- Name the actual question files, required assets and any mark-scheme files read
  in each entry. Enrichment-only or prepared-answer reads are not full inspections;
  record these and missing/unreadable sources under `unresolved`, not in the
  completed inspection count. Never reconstruct read history from intended paths.
- Inspect until three consecutive parts reveal no demand or misconception already
  seen, then stop. There is no target count. Record how many were inspected and what
  the last three added. If too few readable candidates exist, inspect all and explain the shortage.
- Every inspected part needs a semantic decision and reason. A mapped ID alone
  is not evidence.
- `used` means it materially informed teaching. `context_only` means it helped
  understand integration but did not own lesson demand. `rejected` includes
  false positives and inseparable cross-topic demand.
- Record every topic/outcome-filtered definition and formula candidate.
- Never mark a record verified solely because it exists in a Physics registry.
- Set booleans true only when the preceding evidence supports them.


For relevant teaching figures only, populate `diagrams`; use `[]` when none.
Name an existing image asset or source PDF with one-based page and an unambiguous
figure label/location. Inspect it before recording recognition features. Link the
stable sidecar cue ID to this entry; part_id supplies the question/subpart.
Default to an original equivalent; explicitly select `reuse_official` when the
actual source figure should be preserved. Record a concise credit for reuse.
Do not copy official question wording into original activities. The existing
`examples_are_original` check concerns authored examples, not credited source
figures separately declared here. These are additive fields; do not rewrite older
evidence records to pretend those checks or reads occurred.

For new builds, record the topic evidence-index.json, lesson map and actual canonical
source paths. Preserve their mapping provenance; no other subject's mapping contract
or per-lesson retrieval file is required.

For new work, record `learning_design` with actual activity/cue counts and a brief
teaching rationale for actual counts; no numeric activity/visual quota applies.
Use `review_history` as specified in the shared workflow for separate Student and
Science coverage of pre-audit Markdown and both sidecars. The manager audit
records its final inputs separately; reference sync is inactive. These fields do not rewrite historical evidence or source inspections.
