# Subject Paper Processing Steps

This is a living workflow for every subject. Update it as the pipeline develops,
and create or revise subject-specific skills only where the subject genuinely
requires different rules.

## 1. Build and test the parsers

1. Collect a small representative source sample for every paper component and
   its official mark scheme.
2. Identify the different question formats that the parser must preserve, such
   as text, equations, tables, graphs, diagrams, embedded answer choices and
   practical layouts.
3. Build a separate parser where a component has materially different structure.
4. Test each parser on several representative papers before running a full batch.
5. Verify that the parser preserves the original meaning and produces the
   required files without silently reconstructing missing or ambiguous content.
6. Record failures and unsupported layouts explicitly. Do not guess.

Minimum parser test checks:

- expected number of questions or answers detected
- complete question boundaries
- selectable text extracted where available
- equations, tables, graphs and diagrams retained
- separate visual assets extracted when appropriate
- valid JSON and consistent IDs
- matching official mark scheme or answer key
- no empty or corrupt output files
- representative visual inspection against the source PDF

## 2. Run the full corpus and parse the syllabus

1. Place every source question paper and official mark scheme in the appropriate
   component input folders.
2. Run the parser across the complete corpus.
3. Separate successful papers from failed or blocked papers.
4. Repair genuine parser problems, replace corrupt sources and rerun only the
   affected papers.
5. Keep a review log for material ambiguities or unsupported structures.
6. Convert the official syllabus PDF into page-delimited searchable text.
7. Use the syllabus to identify which paper components share content, topics,
   skills or learning pathways.
8. Record component relationships before designing the subject taxonomy.

### Physics component relationship

- Physics P1 and P2 are directly connected. Both assess the same AS Level
  syllabus topics and should use one shared topic and learning-pathway taxonomy.
- P1 assesses the content through multiple-choice questions.
- P2 assesses the same content through structured written questions.
- P3 assesses practical skills. It is related to the subject but is not required
  for the initial P1/P2 knowledge-base and lesson-pathway build.
- Other Physics components can be added later after their role in the product is
  defined.

## 3. Preserve raw outputs, then apply the AI normalisation layer

For every supported component, first retain source-faithful parser outputs:

- complete question images
- extracted text
- structured JSON
- separate figures, diagrams, graphs or tables where confidently detectable
- official mark-scheme or answer-key mappings
- source filenames, page references and stable IDs

The raw parser output is the evidence layer and must remain recoverable. Do not
overwrite it with AI-generated content.

After extraction and validation, apply an AI normalisation layer that converts
the raw text and JSON into the website's canonical display schema. This layer may:

- normalise question and subpart hierarchy
- convert mathematical expressions to the website's LaTeX convention
- identify answer-block and response types
- associate figures with the correct question parts
- classify display mode, such as text-only, text with a supporting visual, or a
  complete source-image question
- prepare accessible text and website-facing labels
- connect questions to the shared subject taxonomy
- add topic, module, lesson, skill, difficulty and revision metadata

The website may initially display the complete source question image while using
the normalised data for search, answer controls and taxonomy. Rebuilt questions
can replace source-image display later, after the relevant formats are reliable.

## Required documents and records

### Reusable for every subject

- **Source manifest:** every source PDF, component, session, year and variant
- **Parser contract:** accepted filenames, input/output folders and output schema
- **Parser test report:** representative papers and verified format coverage
- **Extraction schema:** canonical fields, IDs, file references and display modes
- **Validation report:** pass, failed and blocked papers with reasons
- **Review log:** unresolved hierarchy, crop, source or reconstruction issues
- **Syllabus text:** page-delimited text derived from the official syllabus
- **Component map:** which papers share topics, skills and learning pathways
- **Taxonomy contract:** subject topics, modules, lessons and controlled IDs
- **AI normalisation contract:** raw-to-canonical transformation rules
- **Website rendering contract:** how text, LaTeX, images, tables and answers render
- **Release manifest:** exact validated artifacts approved for downstream use

### Physics-specific documents and controls used so far

- P1 MCQ parser rules and the three provisional display modes:
  `text_options`, `text_diagram_options` and `image_question`
- P2 question and mark-scheme repair rules
- strict P2 question/mark-scheme pair validator
- P2 review logs for blocked structural or source ambiguities
- official mark-scheme preservation checks
- `numerical_values_checked: false` until an authorised numerical review stage
- Physics syllabus text for 2025–2027 and 2028–2030
- shared P1/P2 Physics topic and learning-pathway relationship
- source-faithful P1 full-question images plus optional separate visual assets

Physics did require specific controls because structured P2 hierarchy and
official mark-scheme alignment are materially different from P1 MCQ extraction.
These rules should remain in Physics-specific skills and validators. The general
workflow, document checklist and raw-to-normalised architecture can be reused for
other subjects.

## Current Physics progress

- P1 parser creates complete question PNG, text and JSON files.
- P1 parser validates matching 40-answer mark schemes.
- P1 parser retains diagrams and all visual content inside the authoritative
  complete question image and does not export separate diagram files.
- P2 question papers and mark schemes can be parsed into source-faithful files.
- The current P2 repair sweep is complete with zero canonical OPEN blockers.
- Both available Physics syllabus PDFs have been converted to text.
- Shared P1/P2 taxonomy and knowledge-base design is the current next stage.
