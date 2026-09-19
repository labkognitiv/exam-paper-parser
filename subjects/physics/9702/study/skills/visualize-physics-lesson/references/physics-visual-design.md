# Physics visual design

Use a white reading surface, dark text, restrained colour, open sections, and
print-safe linework. Keep labels editable and readable on mobile. Avoid slide-like
card stacks, decorative gradients, dense posters, and visual effects that imply
unsupported precision.

## Method by teaching need

| Need | Required treatment |
|---|---|
| Circuits | Deterministic SVG with prescribed IEC/Cambridge symbols, explicit junction dots, unambiguous wire crossings, source polarity, current direction, switch state, and correct meter placement. Preserve topology at every breakpoint; never mirror a circuit if polarity or node identity changes. |
| Graphs | Deterministic SVG/canvas with quantity and unit on each axis, justified scale and origin, legible ticks, correct points/curve, and explicit tangent/area construction when assessed. Preserve sign, intercept, gradient and enclosed area; label schematic graphs as not to scale. |
| Ray diagrams | Deterministic SVG with arrowed rays, normals, interfaces, optical axis, focal points and angles measured from the normal. Distinguish real/virtual extensions by line style and verify convergence, refraction, reflection and image position geometrically. |
| Force diagrams | Isolate the chosen body. Start arrows at the body, use correct line of action and direction, label every force, and omit environmental scenery unless it prevents ambiguity. Arrow length represents magnitude only when an explicit scale is valid. |
| Apparatus | Clear orthographic schematic with physically possible connections, readable scales, correct zero/reference, measuring-device resolution, and only relevant supports, leads and controls. Show the measured quantity and viewpoint explicitly. |
| Fields, waves and vectors | Code-native geometry with correct direction, spacing, phase, nodes, vector components and conventions. Use labels/line styles in addition to colour. |
| Qualitative context | An original white-background raster may show the real-world situation, but code owns exact physics. |

## Cambridge-style original figures

Inspect mapped local Physics 9702 `figure_*.png` files before designing a new
question-like teaching diagram. Representative conventions can be seen in:

- apparatus/coil: `past papers/p4/2017/may-june/variant-1/question_02/figure_2_1.png`;
- force geometry: `past papers/p2/2023/may-june/variant-1/question_02/figure_2_1.png`;
- quantitative graph: `past papers/p2/2017/may-june/variant-2/question_03/figure_3_2.png`.

Use monochrome thin-to-medium strokes, generous whitespace, short sans-serif
labels, collision-free leaders, flat presentation, and minimal shading. Do not
copy source geometry, labels, data, or contexts into an original figure.

For a copied or cropped official figure in a separately authorized assessment
workflow, preserve the original pixels and record canonical package path, paper
code, component, year/session/variant, question/figure number, original dimensions,
crop rectangle, output checksum, and an explicit `official Cambridge figure`
label. Cropping must not delete scale, legend, label, axis, arrow, or context
needed to interpret the figure.

Generated raster assets need a pure white background, a named teaching purpose,
prompt and checksum. Retry at most once for a scientific, completeness, or
legibility failure. Never retry merely for cosmetic variation.

## Assigned method values

The planner assigns `source_figure`, `svg`, `python` or `imagegen` once per cue.
Use `source_figure` for authentic figures/data evidence, preserving context and credit;
use `svg`/`python` for the exact subject treatments above. `imagegen` is limited to
qualitative context, never answer-critical geometry, structures, data or measurements.
The author supplies anchors/descriptions; the visualizer follows the assigned method
or reports a plan defect. Required generated labels belong inside the accepted raster.
No label overlays or hybrid images. Inspect the accepted result.
