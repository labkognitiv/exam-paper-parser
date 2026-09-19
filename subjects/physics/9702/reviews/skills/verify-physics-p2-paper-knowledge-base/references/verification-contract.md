# P2 verification contract

## Manual five-gate review

For every answerable leaf, directly inspect prompt and parent context, official marking points, mapped outcome text, skill descriptions, hints, walkthrough, and checking object. Judge:

- `AI_PHYSICS_ERROR`: scientific and arithmetic truth;
- `AI_OUTCOME_MISMATCH`: precise syllabus target;
- `AI_HINT_SPOILER`: progressive help without early answers;
- `AI_SKILL_SCOPE`: bounded reusable primary competency; and
- `AI_CHECKING_MODE`: deterministic, AI, or hybrid matches every credited criterion.

Do not sample. Do not reuse an old conclusion as evidence.

## Deterministic gate

After the full manual paper pass, run `scripts/audit_p2_question.py` for every question. It checks identity, schema, hierarchy, marks, mappings, ordered unions, content flow, response schemas, figures, typography, controlled IDs, and official bindings.

## Logs

Clean question:

```text
Q01 PASS
Counts: 0 fail, 0 blocked
```

Failing question:

```text
Q01 FAIL
- FAIL <CODE> | <leaf.field> | <problem> | fix: <smallest fix> | recheck: <command>
Counts: <n> fail, 0 blocked
```

Use `subjects/physics/9702/reviews/p2/verification-progress.md`. `Fix check` passes only after a clean semantic recheck and deterministic rerun.
