# Mathematics 9709 sandbox upload baseline

Date: 2026-09-23. Scope: M1, S1, P3, P1. This records the source state before the sandbox copy; `manifest.json` records the current export. It is not a mathematical approval or a production release.

## Purpose and rule

The first upload is a **sandbox test** of the app and database import. A later final upload must replace every temporary duplicate or placeholder with its real content. Keep the canonical files under `study/` and `past papers/` unchanged; make test copies only inside this migration package. Every substituted file, its template and its replacement requirement appear in `manifest.json`.

## Current inventory

| Component | Papers | Past-paper questions | Paper enrichment present | Study lessons | Original practice questions | HTML lessons | Missing custom-question figures |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| M1 | 70 | 486 | 484 | 64 | 832 | 39 | 0 |
| S1 | 70 | 479 | 479 | 59 | 767 | 36 | 0 |
| P3 | 70 | 727 | 727 | 82 | 1,066 | 16 | 36 |
| P1 | 69 | 745 | 718 | 77 | 1,001 | 42 | 176 |
| **Total** | **279** | **2,437** | **2,408** | **282** | **3,666** | **133** | **212** |

Every past-paper question has `question.json`, `markscheme.json`, `question_printable.png`, `question_compact.png`, and `markscheme.png`. Question-specific diagrams vary; include only those referenced by `question.json`. Every Study lesson has `questions.json`, `markscheme.json`, and `enrichment.json`. These are file-presence counts, not content validation.

There are **149 Study lessons without HTML**. The 212 custom-question figures are distinct referenced figure IDs with planned assets absent from active Study packages. All 133 existing HTML lessons and 12 topic overview pages were restored into active Study folders; no archive restoration is needed for them.

## HTML coverage

- M1: Kinematics of motion in a straight line 18; Forces and equilibrium 14; Momentum 7.
- S1: Permutations and combinations 13; Representation of data 12; Probability 11.
- P3: Logarithmic and exponential functions 10; Algebra 6.
- P1: Quadratics 13; Coordinate Geometry 11; Functions 9; Trigonometry 9.

## Missing paper enrichment

**29 absent files:** M1 2, P1 27. Another **13 M1 enrichment files** exist but omit some question parts; their missing parts are listed individually in `manifest.json`. Format below is `paper_code/question_folder/enrichment.json` under `past papers/<component>/<year>/`.

M1: `9709_s16_41/question_07`, `9709_s21_42/question_05`.

P1: `9709_m16_12/question_07`, `9709_s16_11/question_10`, `9709_s16_12/question_03`, `9709_s16_13/question_09`, `9709_w16_11/question_09`, `9709_w16_12/question_09`, `9709_w16_13/question_07`, `9709_m17_12/question_06`, `9709_s17_11/question_02`, `9709_s17_12/question_08`, `9709_s17_13/question_04`, `9709_w17_11/question_08`, `9709_w17_12/question_09`, `9709_w17_13/question_09`, `9709_s18_11/question_07`, `9709_s18_12/question_05`, `9709_s18_13/question_09`, `9709_w18_11/question_08`, `9709_w18_12/question_07`, `9709_w18_13/question_06`, `9709_m19_12/question_05`, `9709_s19_11/question_07`, `9709_s19_12/question_08`, `9709_s19_13/question_06`, `9709_w19_11/question_10`, `9709_w19_12/question_07`, `9709_w19_13/question_10`.

## Sandbox substitutions

1. Copied existing HTML into the 149 missing lesson slots, preserving each target lesson ID and labeling the page as a test fixture.
2. Used one visibly labeled SVG for the 212 missing custom-question figures, with each target reference recorded.
3. Supplied test enrichment JSON for the 29 missing paper packages, preserving target question and part IDs. Copied skill and lesson mappings are test data, not real classifications.
4. Supplemented the 13 incomplete M1 enrichment files in the copied bundle with visibly labeled test entries for missing parts. The original enrichment entries remain in place.
5. Prepared four separate component curriculum JSON files from the four active lesson registries. No combined curriculum JSON is required.

For the final upload, replace all 149 copied HTML lessons, 212 placeholder figures, 29 test enrichment files and 13 supplemented enrichment files. Verify the replacement manifest has zero test fixtures before production use.

## Source locations

- Paper packages: `subjects/mathematics/9709/past papers/<component>/<year>/<paper_code>/question_NN/`.
- Study packages: `subjects/mathematics/9709/study/<component>/<topic_id>/<module_id>/<lesson_id>/`.
- Lesson inventory: `study/<component>/<COMPONENT>_LESSON_PDF_REGISTRY.json`.
- Review prototypes and their generated datasets are consumers, not upload sources. Exclude review state, logs, scripts, trackers, manifests and archives from learner-facing data.
