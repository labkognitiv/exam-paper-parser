# Difficulty and tier contract

Exact header:

```text
question_id,difficulty,practice_tier,reason
```

- Difficulty values: `easy`, `medium`, `hard`.
- Tier values: `mandatory`, `revision` only.
- `mandatory`: core or especially diagnostic practice that should appear in the first-pass set.
- `revision`: consolidation, repetition, narrow variation, historical scope, or lower-priority fluency.
- Exact allocation: nearest whole row to 60% mandatory; all remaining rows revision.
- A hard question may be mandatory and an easy question may be revision. Tier is instructional priority, not difficulty.
- Reasons must cite the actual demand or priority in plain language.
- Reasons are Markdown. Every equation, symbolic expression, Greek variable, scientific value, subscript/superscript or powered unit must use balanced inline `$...$` LaTeX; raw Unicode mathematical lookalikes are forbidden.
