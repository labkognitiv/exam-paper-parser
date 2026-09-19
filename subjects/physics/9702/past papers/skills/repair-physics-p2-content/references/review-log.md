# Physics P2 Review Log

## Controlled issue codes

Use one of these codes when applicable:

- `collapsed_printed_subparts`: one extracted leaf contains multiple separately numbered or marked printed prompts.
- `official_part_identity_conflict`: question and official mark scheme use incompatible stable IDs for the same printed prompt.
- `official_mark_conflict`: printed/question marks conflict with immutable official mark-scheme marks without a safe authorized reconciliation.
- `missing_response_scaffold_crop`: an assessed drawing or annotation scaffold lacks an approved standalone crop and figure record.
- `unsupported_response_pattern`: registered fields, table and canvas blocks cannot faithfully represent the printed interaction.

Use a more specific free-form code only when none applies. Do not combine distinct issues into one entry merely because they affect the same question.

Create or append to `review-log.txt` in the active question-paper output directory. Use one entry per issue:

```text
[OPEN] Question 06 | missing_response_scaffold_crop
Observed: Fig. 6.2 is visible in the complete question image but has no separate figure file.
Suggested action: create and verify figure_6_2.png.
Blocked work: figure linkage and final validation for Question 06.
```

Log and do not perform:

- opening an original PDF because extracted evidence is incomplete;
- creating, recropping or replacing an image;
- guessing missing or unreadable content;
- material question/mark-scheme hierarchy changes;
- registry or schema extensions;
- any change whose official interpretation is uncertain.

Routine image-supported transcription, Unicode/LaTeX normalization, response schemas using registered types, content flow, dependencies and unambiguous mark reconciliation may continue. Never mark a logged issue resolved without user approval or intervention.

A question with an open material issue must keep the relevant verification flag `false` or retain `proposed_type`. The strict validator must fail that question until the issue is resolved; report it as blocked, never as PASS.

An OPEN entry must account for the exact expected validator consequences. It does not excuse unrelated failures in the same question. Before accepting a blocked pair, repair all unaffected text, LaTeX, content flow, figure placement, dependencies and response schemas, then compare every remaining failure with the entry's `Blocked work` statement.

For `collapsed_printed_subparts`, include:

- the printed labels and marks;
- the collapsed question leaf ID and its current mark;
- the corresponding official mark-scheme IDs and marks;
- the precise leaf whose response schema remains blocked.

For `official_source_locked` work, log official duplicates or malformed official structure without editing the mark-scheme JSON.
