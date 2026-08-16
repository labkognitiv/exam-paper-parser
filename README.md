# Question Compactor

Question Compactor turns a born-digital exam paper into one compact PNG,
plain-text file, and structured JSON mapping per numbered question. It runs
locally and does not call an AI or OCR service.

The program preserves the original PDF content (including equations, tables,
graphs, and diagrams), masks dotted response fields, removes page furniture and
large working-space gaps, and vertically stacks the remaining content. Captioned
figures are also exported automatically as separate PNG files using PDF drawing
coordinates; no AI is used. After a figure is exported, both the diagram and its
standalone caption are removed from the question PNG. References within the
question text, such as "shown in Fig. 2.1", remain.

## Install

```bash
cd question_compactor
python3 -m venv .venv
.venv/bin/python -m pip install -e .
```

## Run

Put one or more PDFs in any directory, open Terminal in that directory, and run:

```bash
paperscript
```

The standard project layout is:

```text
input/
  physics/
    paper/
    markscheme/
    mcq/
    syllabus/
output/
  physics/
    paper/
    markscheme/
    mcq/
    syllabus/
```

Place Physics question-paper PDFs in `input/physics/paper` and run:

```bash
cd /Users/usman.zafar/PaperScript
paperscript paper
```

These are written to `output/physics/paper/<paper-code>/` automatically. For example,
`input/physics/paper/9702_s25_qp_22.pdf` produces
`output/physics/paper/9702_s25_qp_22/question_01.png`, and so on.

For a file named `9702_s25_qp_22.pdf`, the program automatically creates:

```text
9702_s25_qp_22/
  question_01.png
  question_01.txt
  question_01.json
  question_02.png
  question_02.txt
  question_02.json
  figure_2_1.png
figure_2_2.png
  ...
```

When a question contains a detected figure, the output also includes two
question-image variants: `question_02.png` with the figure removed and
`question_02_with_figures.png` with the figure retained. The separately cropped
`figure_2_1.png` file is still produced.

You can also pass a PDF or directory from anywhere:

```bash
paperscript /path/to/paper.pdf
paperscript /path/to/folder
```

Useful options:

```bash
# Inspect detected questions without writing files
paperscript paper.pdf --dry-run

# Keep answer lines while still removing empty vertical gaps
paperscript paper.pdf --keep-answer-lines

# Render higher-resolution PNGs
paperscript paper.pdf --dpi 200

# Skip separate figure extraction
paperscript paper.pdf --no-figures
```

The defaults are tuned for Cambridge-style structured papers, but rely on
ordinary PDF coordinates rather than a paper-specific page list. Numbered
questions are detected near the top of a page, and `[Total: ...]` closes a
question.

## Current scope

- Best results: PDFs containing selectable text and vector graphics.
- Scanned PDFs: not yet supported; add OCRmyPDF/Tesseract before this step.
- The output uses variable-height pages so long questions remain readable.
- Diagram regions are retained. Blank response graphs are intentionally retained
  because removing them can change the meaning of a question.

This is an MVP. Always review output before publishing or using it in assessment.

## Mark schemes

Mark schemes use a separate converter, so the question-paper extraction logic is
not changed. Put Physics mark-scheme PDFs in `input/physics/markscheme` and run:

```bash
cd /Users/usman.zafar/PaperScript
paperscript markscheme
```

For example, `9702_s25_ms_22.pdf` creates matching `.txt` and `.json` files in
`output/physics/markscheme/9702_s25_ms_22/`. Each answer line retains its marking tag,
such as `B1`, `C1`, `M1`, or `A1`, in a separate aligned column. The JSON groups
continued rows under the latest question-part label, records alternative marks,
and uses IDs compatible with the question JSON.

## Multiple-choice papers

Put Physics Paper 1 multiple-choice PDFs in `input/physics/mcq` and run:

```bash
paperscript mcq
```

The command writes one complete question crop and one JSON mapping per question
to `output/physics/mcq/<paper-code>/`. Diagrams, tables, equations, and the A-D choices
remain inside the question image. Each JSON record has `answer_type` set to
`multiple-choice`, one mark, and options A-D. A matching `_ms_` PDF may be put
in the same `input/physics/mcq` folder. The command validates its complete 40-answer
table, writes `answer_key.json`, and fills `correct_answer` in every question
JSON automatically.

The complete question PNG remains the authoritative display asset. When vector,
raster, table, graph, circuit, or other visual content is detected, the converter
also writes `figure_<question>_01.png` with a 64-pixel white safety border. The
question JSON lists these files, records whether the provisional display mode is
`text_options`, `text_diagram_options`, or `image_question`, and keeps
`rebuild_status` as `not_rebuilt` until a later reconstruction pass.

## Syllabuses

Physics syllabuses use a separate text converter because their long-form sections,
learning-objective lists, and tables differ from exam papers. Put born-digital
syllabus PDFs in `input/physics/syllabus` and run:

```bash
paperscript syllabus
```

Each PDF produces one UTF-8 text file under
`output/physics/syllabus/<syllabus-filename>/`. The text includes explicit page
markers, preserves line and block boundaries, and removes repeating Cambridge
page headers, page numbers, and “Back to contents” footer links. You can also
parse a file or folder from anywhere:

```bash
syllabus-converter /path/to/syllabus.pdf
syllabus-converter /path/to/syllabus-folder --output /path/to/text-output
```
