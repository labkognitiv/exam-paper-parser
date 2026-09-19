# Physics P2 Question Content Flow

Use one ordered `content_flow` at question level. It contains `stem` once when the question has a stem, followed by every part exactly once in printed order:

```json
"content_flow": [
  {"type": "stem"},
  {"type": "part", "part_id": "9702_m16_22_q01_a"}
]
```

Keep the canonical prose in `question_stem` and each part's `question_text`; do not duplicate it in the flow.

Each figure has one placement:

- `after_stem`: printed after the question stem.
- `after_stem_text`: printed within the stem immediately after the exact `anchor` substring.
- `after_text`: printed within a part immediately after the exact `anchor` substring.
- `response_background`: the figure is the supplied scaffold for a canvas response.

```json
"placement": {
  "scope": "part",
  "part_id": "9702_m16_22_q02_b",
  "position": "after_text",
  "anchor": "as shown in Fig. 2.1."
}
```

For `after_stem_text` and `after_text`, copy a short exact anchor from the corresponding plain field. The validator must confirm the anchor occurs exactly once. Figure references and response-schema background references remain separate semantic links.

## Missing response scaffolds

Use `response_background` only when the assessed scaffold has its own approved figure record and existing standalone file. A combined `question_NN_with_figures.png` image is visual evidence, not a substitute response background.

If a required graph, circuit, diagram or annotation scaffold appears only inside the combined question image:

1. Keep any available contextual figure placement accurate.
2. Do not create, extract or recrop the missing scaffold.
3. Do not assign a canvas block with a missing or substitute background.
4. Add an OPEN `missing_response_scaffold_crop` review entry naming the printed figure and affected leaf.
5. Keep content-structure verification false and leave the affected leaf without a response schema.
6. Continue repairing all unaffected content in the question.
