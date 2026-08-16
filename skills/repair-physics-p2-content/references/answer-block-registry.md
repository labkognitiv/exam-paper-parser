# Physics P2 Answer-Block Registry

Status: exploratory and incrementally controlled. This is not a finalized production schema.

## Structure

Each answerable leaf part may contain:

```json
{
  "response_schema": {
    "version": "0.1",
    "blocks": []
  }
}
```

`blocks` is ordered because one part may require working plus multiple final inputs. Store one student response payload for the part, keyed by the stable IDs below.

## Registered blocks

### `fields`

Use for written, numerical, mathematical or choice responses. Required keys:

- `block_id`: `<part_id>_block_NN`
- `type`: `fields`
- `fields`: ordered array of registered controls

Registered controls:

- `long_text`: explanation, derivation or unrestricted working
- `short_text`: word, phrase, definition or short statement
- `number`: dimensionless numerical value
- `quantity`: numerical value with a defined unit
- `math_expression`: equation or symbolic expression
- `single_choice`: exactly one option
- `multiple_choice`: zero or more options

Each field requires `field_id`, `control`, `role` and `required`. Add `label`, `unit`, `options`, `presentation` or deterministic format validation only when applicable. `role` is storage metadata and does not require the UI to show a redundant label.

When a field has a unit, store both forms:

```json
{
  "unit": "m s⁻¹",
  "unit_latex": "\\mathrm{m\\,s^{-1}}"
}
```

Use optional `label_latex` for a mathematical label such as `v_x` or `I_2/I_1`. Do not include `$` delimiters in `unit_latex` or `label_latex`; the renderer supplies them.

Allowed roles include `answer`, `working`, `value`, `uncertainty`, `definition`, `explanation`, `selection` and `equation`. Roles describe storage semantics; they do not create new renderer controls.

### `table`

Use when the student must answer inside a fixed row/column structure. Define stable `row_id` and `column_id` values, then define every cell explicitly. Static cells contain display content; editable cells contain one registered field control. Keep every cell response inside the parent part payload.

Do not use bare row and column IDs as an implicit editable-cell contract. A conforming table block has this shape:

```json
{
  "block_id": "<part_id>_block_01",
  "type": "table",
  "columns": [
    {"column_id": "quantity", "label": "quantity"},
    {"column_id": "scalar", "label": "scalar"},
    {"column_id": "vector", "label": "vector"}
  ],
  "rows": [
    {
      "row_id": "acceleration",
      "cells": [
        {"column_id": "quantity", "type": "static", "value": "acceleration"},
        {
          "column_id": "scalar",
          "type": "editable",
          "field": {
            "field_id": "<part_id>_field_01",
            "control": "single_choice",
            "role": "selection",
            "required": true,
            "options": ["scalar", "vector"],
            "presentation": "tick_grid"
          }
        },
        {
          "column_id": "vector",
          "type": "choice_option",
          "field_id": "<part_id>_field_01",
          "option": "vector"
        }
      ]
    }
  ]
}
```

Use one shared `single_choice` field across mutually exclusive cells in a row. Use separate fields when multiple cells may be selected or independently completed. `choice_option` cells reference the owning editable field rather than duplicating it. Use `value_latex` beside `value` when static mathematical content needs rendering.

### `canvas`

Use when the assessed response must be drawn on a blank area, supplied figure or graph scaffold. Required keys:

- `block_id`
- `type`: `canvas`
- `mode`: `blank_drawing`, `annotate_figure`, or `draw_on_scaffold`
- `background_figure_id`: required except for `blank_drawing`
- `tools`: allowed drawing or annotation tools

Do not create separate primary types for circuits, waveforms or graphs; represent them through `canvas.mode`, background and tools.

## Presentation rules

- Render radio buttons, dropdowns, circles or crosses as presentations of `single_choice`.
- Render tick grids as table cells containing `single_choice` or `multiple_choice` controls.
- Represent an inline equation blank with an ordered `fields` block and optional static `segments`; it is not a separate block type.
- Use `quantity` only when the unit is known from the question. Validation may enforce shape and unit storage, never correctness.
- A calculation normally uses `long_text` for working and `quantity`, `number` or `math_expression` for the final response.
- A printed form such as `v = ___ ± ___ m s⁻¹` uses two ordered `quantity` fields with roles `value` and `uncertainty`.
- Plain question and label text must remain readable without LaTeX. Full prose-and-maths display strings belong in `question_text_latex`, with mathematical spans delimited by `$...$`.

## Unsupported patterns

The registry should grow from real Paper 2 questions rather than anticipated patterns. For each new response pattern:

1. First try to represent it by combining existing blocks, controls, presentation metadata and static segments.
2. If that would lose or distort the printed response interaction, describe the unsupported pattern precisely.
3. Add `proposed_type` to the affected part and record the proposed reusable extension in the paper review log.
4. Wait for user approval before changing this registry or the validator.
5. After approval, add the smallest reusable extension. Do not create a question-specific type; update this registry and `scripts/validate_pair.py` together.

If the correct reusable abstraction is uncertain, do not guess. Add this temporary form to the affected part and request review:

```json
{
  "response_schema": {
    "version": "0.1",
    "blocks": [
      {
        "block_id": "<part_id>_block_01",
        "type": "proposed_type",
        "observed_pattern": "concise factual description",
        "reason_registered_types_fail": "concise explanation"
      }
    ],
    "registry_review_required": true
  }
}
```

Replace `proposed_type` only after the user approves a reusable registry decision and the validator supports it.
