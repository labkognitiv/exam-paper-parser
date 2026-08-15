#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def main() -> None:
    source = Path(sys.argv[1]).resolve()
    destination = Path(sys.argv[2]).resolve()
    data = json.loads(source.read_text(encoding="utf-8"))
    embedded = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    source_dir = json.dumps(str(source.parent), ensure_ascii=False)
    title = str(data.get("question_num", ""))
    page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
  <style>
    :root {{ color-scheme: light dark; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background: Canvas; color: CanvasText; font: 17px/1.55 Arial, sans-serif; }}
    main {{ width: min(920px, calc(100% - 32px)); margin: 32px auto 80px; }}
    .number {{ font-weight: 700; margin-bottom: 24px; }}
    .part {{ display: grid; grid-template-columns: 70px minmax(0, 1fr) 48px; gap: 10px; margin: 26px 0; }}
    .label {{ font-weight: 700; }}
    .text {{ white-space: pre-wrap; }}
    .marks {{ text-align: right; align-self: end; }}
    .figure {{ display: block; width: 100%; height: auto; margin-top: 18px; }}
    @media (max-width: 560px) {{
      main {{ width: min(100% - 20px, 920px); margin-top: 18px; }}
      .part {{ grid-template-columns: 62px minmax(0, 1fr); }}
      .marks {{ grid-column: 2; }}
    }}
  </style>
</head>
<body>
  <main id="question"></main>
  <script id="question-data" type="application/json">{embedded}</script>
  <script>
    (() => {{
      const data = JSON.parse(document.getElementById('question-data').textContent);
      const sourceDir = {source_dir};
      const root = document.getElementById('question');
      const number = document.createElement('div');
      number.className = 'number';
      number.textContent = data.question_num;
      root.appendChild(number);

      if (data.question_stem_latex) {{
        const stem = document.createElement('div');
        stem.className = 'text';
        stem.textContent = data.question_stem_latex;
        root.appendChild(stem);
      }}

      (data.parts || []).forEach((part) => {{
        const section = document.createElement('section');
        section.className = 'part';

        const label = document.createElement('div');
        label.className = 'label';
        label.textContent = part.label;
        section.appendChild(label);

        const body = document.createElement('div');
        body.className = 'text';
        body.textContent = part.question_text_latex ?? part.question_text ?? '';

        (part.figure_ids || []).forEach((figureId) => {{
          const figure = (data.figures || []).find((item) => item.id === figureId);
          if (!figure?.file) return;
          const image = document.createElement('img');
          image.className = 'figure';
          image.src = sourceDir + '/' + figure.file;
          image.alt = figure.label || figure.id;
          body.appendChild(image);
        }});
        section.appendChild(body);

        const marks = document.createElement('div');
        marks.className = 'marks';
        marks.textContent = part.marks == null ? '' : '[' + part.marks + ']';
        section.appendChild(marks);
        root.appendChild(section);
      }});

      const render = () => {{
        if (typeof renderMathInElement !== 'function') {{
          window.setTimeout(render, 50);
          return;
        }}
        renderMathInElement(root, {{
          delimiters: [
            {{ left: '$$', right: '$$', display: true }},
            {{ left: '$', right: '$', display: false }}
          ],
          throwOnError: false
        }});
      }};
      render();
    }})();
  </script>
</body>
</html>'''
    destination.write_text(page, encoding="utf-8")


if __name__ == "__main__":
    main()
