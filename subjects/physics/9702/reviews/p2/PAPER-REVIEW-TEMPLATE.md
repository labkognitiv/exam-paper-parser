# P2 check

Paper: `9702_<session>_<variant>`
Status: `IN_PROGRESS`

## Rules

- Script checks first.
- AI checks only `AI_CHECK` lines.
- Write fails only.
- No fail means one line: `Q01 PASS`.
- Do not change source files during review.
- Keep `numerical_values_checked: false`.
- No PDF/image check unless data is missing or fights itself. Then write `BLOCKED`.

## Questions

```text
Q01 FAIL
- FAIL <code> | <leaf.field> | <what is wrong> | fix: <small fix> | recheck: <command>
- BLOCKED <code> | <leaf.field> | <what is missing>
Counts: <n> fail, <n> blocked
```

Clean question:

```text
Q02 PASS
```

## End

```text
Paper: PASS|FAIL|BLOCKED
Fail: <n>
Blocked: <n>
```
