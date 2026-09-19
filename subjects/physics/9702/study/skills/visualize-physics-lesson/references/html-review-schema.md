# Physics lesson HTML review

Write `<lesson-folder>/lesson-html-review.json` and validate it as JSON.

```json
{
  "schema_version": "9702_lesson_html_review_v1",
  "lesson_id": "",
  "inputs": {
    "lesson_markdown": {"path": "", "sha256": ""},
    "lesson_evidence": {"path": "", "sha256": ""},
    "topic_audit": {"path": "", "sha256": "", "gate": "PASS"}
  },
  "content_fidelity": {
    "all_markdown_claims_preserved": false,
    "definitions_exact": false,
    "worked_examples_exact": false,
    "added_claims": []
  },
  "visual_plan": {
    "planned_teaching_moments": 0,
    "imagegen_required": false,
    "cue_coverage": [],
    "activity_coverage": []
  },
  "image_production": {
    "imagegen_calls": 0,
    "source_sheets": [],
    "planned_panels": 0,
    "accepted_crops": [],
    "rejected_crops": [{"path": "", "reason": ""}],
    "displayed_crops": []
  },
  "visuals": [
    {"selector_or_path": "", "method": "svg|html|css|canvas|raster|library", "teaching_purpose": "", "method_reason": "", "alt_or_equivalent": "", "source": "original|official_reuse", "cue_id": "", "source_reference": {"part_id": "", "figure_id": "", "path": "", "sha256": "", "pdf_page_1based": null, "crop_coordinates_and_units": null}, "source_credit": ""}
  ],
  "gates": {
    "scientific_accuracy": "pass|fail",
    "accessibility": "pass|fail",
    "viewport_390": "pass|fail",
    "viewport_768": "pass|fail",
    "viewport_1280": "pass|fail",
    "print": "pass|fail",
    "offline_assets": "pass|fail",
    "source_figure_use": "pass|fail",
    "visual_coverage": "pass|fail",
    "image_provenance_complete": "pass|fail"
  },
  "observed_evidence": [],
  "unresolved": []
}
```

Completion requires every gate to pass, no added claim, no unresolved item, and accepted/rejected/displayed counts that reconcile with the named asset paths. Completion also requires every approved sidecar cue/activity implemented and the chosen per-cue production methods. Record actual counts and the learning rationale; no fixed count establishes quality. Set `imagegen_required` from the actual cue plan; zero ImageGen calls is valid when none are needed. Hybrid assets are prohibited. Record that SVG/Python labels are deterministic and that every required ImageGen label and annotation is part of the accepted raster. Sheet/crop fields apply only when used; keep unused arrays empty and counts zero. Record cue-to-visual and activity-to-control selectors in the coverage arrays. Observed evidence must cover generated label spelling, placement and target accuracy, activity feedback branches, varied readable compositions, and absence of production language.

`source_figure_use` passes when recreated visuals are original equivalents and
reused figures match explicit `reuse_official` cues, retain necessary scientific
context and carry source credit. Check paper-linked cues against their evidence figure entries. Lesson-only cues,
including reviewer/auditor additions, require no paper entry: use
`source_reference: null`, `source: original`, their local sidecar cue ID and exact Markdown anchor in observed evidence. Verify every cue against its approved teaching.
Record recognition-feature checks under observed evidence. The former
`no_official_diagram_copy` gate applies to historical reviews only; leave them
unchanged and use `source_figure_use` for new reviews under this workflow.

Before production PASS, verify all topic Markdown hashes and membership under
[the shared workflow](../../lesson-workflow.md). Record this freshness check in
`observed_evidence`; hashing the audit file alone does not establish freshness.

Record the manager-owned topic audit and its final Markdown hash in observed evidence.
Do not add student-reference inputs, entries, gates, bundles or interface controls.

Use `delivery_status: review_preview` and `production_status: incomplete` while a
topic audit is absent/stale. Content/asset/interaction failures cannot be waived as
preview-only limitations. Print PASS requires inspection of the final rendered
print output, not merely successful PDF generation.

Record plan, visual-sidecar and activity-sidecar input hashes, assigned/used method
per cue, exact-anchor checks, and actual model/reasoning effort.
