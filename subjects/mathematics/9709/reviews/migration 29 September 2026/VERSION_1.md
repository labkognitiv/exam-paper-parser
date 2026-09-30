# Mathematics 9709 migration — version 1

**Recorded:** 30 September 2026  
**Version:** 1  
**Scope:** complete lean Mathematics 9709 past-paper copy: 279 papers, 2,437 questions, P1/P3/M1/S1.  
**Status:** version 1 transferred and checked on 30 September 2026. Canonical sources remain in place. Git branch `mathematics-9709-version-1` identifies this snapshot; later versions should use new numbered branches. `TRANSFER_MANIFEST.json` records the source/destination SHA-256 of every copied file.

## Transferred question-folder contents

Each paper has a `questions/` folder with a folder for every question. For example, `questions/question_01/` contains:

| Migrate | Why |
| --- | --- |
| `question.json` | Complete question text, paper/question identity, ordered parts, marks, dependencies, content flow and figure placement. |
| `markscheme.json` | Complete official marking scheme, criteria and accepted routes. |
| `enrichment.json` | Topic/lesson mapping, primary skill ID, difficulty, practice tier, hints and walkthroughs. |
| Referenced diagram/image files, when present | Preserve the exact figures needed by `question.json` and their relative references. |

Part (a), (b), etc. stays inside these question-level JSON files in its original order. `ai-rubric.json`, `enrichment-extras.json`, OCR files, text extracts and PDF/PNG previews remain in the current source package; they are **not in the agreed question-folder migration set**. Paper-level manifest, PDFs and the exact version-control mechanism are still to be decided.

## Lean migration hierarchy (transferred)

Confirmed mapping scope: the four current topic/lesson hierarchy files, one per component. Each component folder owns its own `knowledge/` and `past papers/` folders. Keep its `hierarchy.json` once in `knowledge/`; do not duplicate it in every question folder. Each file contains ordered topics and lessons with stable IDs and display titles. The `mapping.topic_id` and `mapping.lesson_id` values already in each `enrichment.json` resolve against that component's hierarchy. No active module ID is needed. Filesystem component names use the existing lowercase IDs (`m1`, `p1`, `p3`, `s1`).

```text
migration 29 September 2026/
  VERSION_1.md
  subjects/
    mathematics/
      9709/
        m1/
          knowledge/
            hierarchy.json
          past papers/
            <year>/
              <paper_code>/
                paper.json
                questions/
                  question_01/
                    question.json
                    markscheme.json
                    enrichment.json
                    <referenced diagram files, if any>
                  question_02/
                    ...
        p1/
          knowledge/hierarchy.json
          past papers/<year>/<paper_code>/questions/question_01/...
        p3/
          knowledge/hierarchy.json
          past papers/<year>/<paper_code>/questions/question_01/...
        s1/
          knowledge/hierarchy.json
          past papers/<year>/<paper_code>/questions/question_01/...
```

The M1 `part-lesson-overrides.json` is a separate import/provenance rule and is not among the four confirmed hierarchy files. Its migration treatment has not been decided.

All topic/lesson IDs resolve against the four transferred hierarchy files. Sixty-five historical P1 vector parts reference P3 topic/lesson IDs; they remain under their original P1 paper folders and resolve through the P3 hierarchy. Any reader of this migration must index all four hierarchies by ID instead of limiting lookup to the paper's component. No mapping values or question locations were rewritten.

## Current source structure (inventory, not transfer list)

The current canonical path is `subjects/mathematics/9709/past papers/<component>/<year>/<paper_code>/`. Each paper has `manifest.json`, `paper_compact.pdf`, `paper_printable.pdf`, `paper_markscheme.pdf`, and one folder for each question (`question_01/`, `question_02/`, etc.). The manifest records the paper inventory, source provenance, contracts and file hashes. There are no separate folders for parts (a), (b), etc.; each question's ordered parts live in its JSON files.

## What the current `question_01/` contains

Every one of the 279 `question_01/` folders currently contains these 15 files. Other question-number folders use the same common set.

| File | Contents |
| --- | --- |
| `question.json` | Official question text, paper/question identity, ordered parts, marks, dependencies, figures and content flow. |
| `markscheme.json` | Official answers, marking criteria and accepted routes. |
| `enrichment.json` | Difficulty, practice tier, topic/lesson mapping, primary skill ID, hints, walkthroughs and checking mode/source; joined to the question by `question_id`. |
| `ai-rubric.json` | AI checking rubric companion, keyed by question and part IDs. |
| `enrichment-extras.json` | Knowledge links, skill tags, pattern IDs and numerical review flag, keyed by question and part IDs. |
| `question.txt` | Extracted question text source. |
| `question_ocr.json`, `question_ocr_meta.json` | Question OCR and extraction metadata. |
| `question_compact.pdf`, `question_compact.png` | Compact question crop and preview. |
| `question_printable.pdf`, `question_printable.png` | Printable question crop and preview. |
| `markscheme_ocr.json`, `markscheme_meta.json` | Mark-scheme OCR and extraction metadata. |
| `markscheme.png` | Mark-scheme crop/preview. |

Question-specific diagram PNGs are additional files when the printed question needs them. Of the 279 `question_01/` folders, 37 have additional diagram PNGs (47 PNGs total); the other 242 contain exactly the 15 common files. Their names vary. `question.json` supplies the figure references and placement.

## Version boundary

Version 1 contains 7,904 copied files: 7,311 core JSON files, 589 referenced figure files and four hierarchies. The transfer manifest verifies every destination hash, all 2,437 question/scheme/enrichment ID and part-order joins, all 589 relative figure references and all topic/lesson links. It records 65 valid P1-to-P3 links. The canonical paper packages remain at their existing paths. Paper-level manifests/PDFs, AI-rubric and enrichment-extras companions, OCR files and previews were not transferred. This is structural/hash verification, not fresh mathematical approval.

## Paper metadata and full-question delivery (30 September 2026 addendum)

The internal version 1 copy has 279 additive paper.json files beside its question folders. PAPER_METADATA_MANIFEST.json pins those historical metadata files; the 7,904 transfer files match current canonical sources. A previous delivery that physically omitted vector-scope questions is preserved at repository archive/2026-09-30-vector-screened-delivery/ with its manifest and builder.

The active DELIVERY_2026_2027/subjects/mathematics/9709/ contains **all 2,437 original questions**, 589 referenced figures, all four complete hierarchies and 279 updated paper.json files (8,183 content files, plus DELIVERY_MANIFEST.json). Every question, scheme, enrichment, figure and hierarchy is byte-identical to the internal version 1 copy. The 17 false figure crops removed on 30 September are preserved in the repair archive and are absent from both copies.

Each delivery paper.json records original marks, a **standard** duration of 110 minutes for P1/P3 or 75 minutes for M1/S1, marks available to attempt, and a proportional suggested practice duration. The 110-minute rule is a product choice across years; some 2016–19 P1/P3 source PDFs print 105 minutes. question_availability lists only exceptions; unlisted questions default to available. A record with status unavailable disables the whole question. Status partially_available keeps the question and disables only its unavailable_part_ids. The website can show display_message when it grays out blocked content; reason_code remains a stable machine-readable value.

The vector screen flags 27 P1 vector questions (65 parts, 210 marks) as wholly unavailable. In P3 it flags 26 plane-containing questions: 15 wholly unavailable and 11 partially available. Across P3, 49 plane parts (205 marks) are unavailable; the 11 mixed questions retain 55 attemptable vector marks. current_total_marks excludes exactly those unavailable marks, and suggested_duration_minutes scales from the standard duration. No question text, official marking, enrichment or figure was edited. DELIVERY_MANIFEST.json pins all delivered files and verifies the availability arithmetic.

The screen covers **these vector topics only**. Other-topic syllabus review remains pending for every component, so current_total_marks is not yet a certified full current-syllabus total. The 2026–27 syllabus includes P3 2D/3D vectors but does not list P1 vectors or P3 plane equations/line-plane work. Source: [Cambridge Mathematics 9709 syllabus 2026–27](https://www.cambridgeinternational.org/Images/697427-2026-2027-syllabus.pdf).

## Figure-link repair (30 September 2026)

M1 9709_w25_42 Q7(b) had a figure_ids value that did not match its single figure, although that figure already listed part (b) in referenced_by. Corrected that one ID in the canonical question, internal version 1 and active delivery; no wording, marks, marking, enrichment, figure bytes or placement changed. Refreshed the canonical paper manifest, both migration manifests, the delivery manifest and the two paper.json provenance hashes. The nine superseded files and their original hashes are preserved at repository archive/2026-09-30-m1-w25-42-q7-figure-link/. At that repair stage, the 7,921-file transfer and 8,200-file delivery verified, and all 598 part-to-figure links resolved. The later diagram cleanup reduced the current counts to 7,904 and 8,183 content files.
