# Physics MCQ skill and rubric contract

Exact header:

```text
question_id,primary_skill,skill_tags,ai_rubric,rubric_id
```

- `primary_skill`: one title-cased, teacher/student-readable action such as `Using SI Prefixes` or `Applying Kirchhoff’s Second Law`.
- `skill_tags`: JSON array containing the primary skill and optionally one supporting skill; one or two unique entries only.
- `ai_rubric`: JSON object whose keys exactly equal `skill_tags` in the same order.
- Each rubric value is one concise sentence explaining what a correct choice indicates. It must be specific to the assessed Physics action but must not infer unseen working.
- Rubric prose is Markdown. Every equation, symbolic expression, Greek variable, scientific value, subscript/superscript or powered unit must use balanced inline `$...$` LaTeX; do not use raw Unicode lookalikes. Rubric keys and human-readable skill names remain plain text.
- `rubric_id`: always `single_select_mcq_v1`.
- Correct selection earns 1; any other selection earns 0. This score rule is not duplicated in every diagnostic statement.
- Reuse exact approved wording for materially identical skills across papers.
- Every tag must exist as an `approved` row in the active central Physics MCQ skill registry.
- Never use raw syllabus headings alone when a clearer action label is possible.
- Never use vague labels such as `Physics Knowledge`, `Calculation`, `Problem Solving`, or `Understanding the Question`.
