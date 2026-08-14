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
  paper/
  markscheme/
output/
  paper/
  markscheme/
```

Place question-paper PDFs in `input/paper` and run:

```bash
cd /Users/usman.zafar/PaperScript
paperscript paper
```

These are written to `output/paper/<paper-code>/` automatically. For example,
`input/paper/9702_s25_qp_22.pdf` produces
`output/paper/9702_s25_qp_22/question_01.png`, and so on.

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
not changed. Put mark-scheme PDFs in `input/markscheme` and run:

```bash
cd /Users/usman.zafar/PaperScript
paperscript markscheme
```

For example, `9702_s25_ms_22.pdf` creates matching `.txt` and `.json` files in
`output/markscheme/9702_s25_ms_22/`. Each answer line retains its marking tag,
such as `B1`, `C1`, `M1`, or `A1`, in a separate aligned column. The JSON groups
continued rows under the latest question-part label, records alternative marks,
and uses IDs compatible with the question JSON.
