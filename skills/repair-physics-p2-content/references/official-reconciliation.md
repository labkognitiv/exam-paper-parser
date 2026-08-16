# Immutable Official Reconciliation

Use `official_reconciliation` only when ordinary identity matching or legacy `official_part_mapping` cannot faithfully reconcile immutable official JSON with the printed question. It is additive question-side metadata; official mark-scheme bytes remain unchanged.

## Contract

```json
{
  "official_reconciliation": {
    "version": "0.1",
    "part_bindings": [
      {
        "question_part_ids": ["printed_leaf_id"],
        "official_part_refs": [
          {"source": "markscheme_02.json", "part_id": "official_id", "occurrence": 1}
        ]
      }
    ],
    "part_aliases": [],
    "part_transfers": [],
    "marking_point_aliases": []
  }
}
```

`source` is a basename in the same locked mark-scheme directory and defaults to the validator's input file. `occurrence` is one-based among records with the same ID. Omit unambiguous one-to-one bindings: the validator binds a unique matching ID automatically.

Every answerable printed leaf must be bound exactly once. Every local official part occurrence must be bound, transferred, or declared an alias exactly once. Binding marks must agree exactly in both directions.

## Multiple identities and duplicate IDs

One binding may contain multiple question leaves, multiple official occurrences, or both. This supports aggregation, pseudo-parts, marks stored under another printed identity, and duplicate official IDs without discarding any occurrence.

## Alternative-only part aliases

Use `part_aliases` only for a duplicate zero-mark official occurrence whose marking points are all alternatives:

```json
{
  "official_part_ref": {"part_id": "id", "occurrence": 2},
  "alias_of": {"part_id": "id", "occurrence": 1},
  "reason": "alternative_route"
}
```

Aliases never contribute marks and cannot conceal a positive-mark occurrence.

## Cross-question transfers

When an official part is immutably stored in the wrong question file, the source question declares its disposition:

```json
{
  "official_part_ref": {"part_id": "misplaced_id", "occurrence": 1},
  "target_question_id": "target_question_id",
  "target_question_part_id": "target_leaf_id"
}
```

The target question binds the same occurrence using `source` to name the sibling mark-scheme JSON. This preserves both source custody and target mark accounting.

## Exact duplicate alternative marking points

Every repeated occurrence remains addressable. Declare only byte-semantic exact duplicate alternatives:

```json
{
  "official_marking_point_ref": {
    "part_ref": {"part_id": "part_id", "occurrence": 1},
    "marking_point_id": "duplicate_id",
    "occurrence": 1
  },
  "alias_of": {
    "part_ref": {"part_id": "part_id", "occurrence": 1},
    "marking_point_id": "original_id",
    "occurrence": 1
  },
  "reason": "exact_duplicate_alternative"
}
```

The validator requires identical complete point objects and `is_alternative: true`; aliases cannot suppress distinct or available marks.
