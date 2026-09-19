# Difficulty/tier QC contract

Exact ledger header:

```text
question_id,difficulty_fit,tier_fit,reason_fit,independent_difficulty,independent_practice_tier,verdict,notes
```

- Fit fields: `yes` or `no`.
- Independent difficulty: `easy`, `medium`, or `hard`.
- Independent tier: `mandatory` or `revision`.
- Verdict: `passed`, `failed`, or `needs_review`.
- Review every row. A passed row must agree exactly with both assigned values.
- The independent full-paper allocation must also be exactly 60% mandatory and 40% revision.

