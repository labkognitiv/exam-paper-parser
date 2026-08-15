#!/usr/bin/env python3
import html
import json
import sys
from pathlib import Path


def main() -> None:
    source_dir = Path(sys.argv[1]).resolve()
    destination = Path(sys.argv[2]).resolve()
    documents = []
    for path in sorted(source_dir.glob("*.json")):
        with path.open(encoding="utf-8") as handle:
            documents.append(json.load(handle))

    embedded = json.dumps(documents, ensure_ascii=False).replace("</", "<\\/")
    document = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(documents[0]["source_filename"] if documents else source_dir.name)}</title>
  <style>
    :root {{ color-scheme: light dark; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background: Canvas; color: CanvasText; font: 16px/1.5 Arial, sans-serif; }}
    main {{ width: min(1100px, calc(100% - 28px)); margin: 24px auto 72px; }}
    .controls {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px; }}
    button, select {{ color: inherit; background: ButtonFace; border: 1px solid ButtonBorder; border-radius: 6px; padding: 8px 12px; }}
    button[aria-pressed="true"] {{ outline: 2px solid Highlight; outline-offset: 1px; }}
    .part {{ margin: 24px 0; }}
    .part-head {{ display: flex; justify-content: space-between; gap: 16px; font-weight: 700; margin-bottom: 8px; }}
    .point {{ display: grid; grid-template-columns: minmax(0, 1fr) 64px 54px; gap: 12px; padding: 8px 0; border-bottom: 1px solid GrayText; }}
    .alternative {{ padding-left: 24px; }}
    .notes {{ white-space: pre-wrap; margin-top: 8px; }}
    table {{ width: 100%; border-collapse: collapse; }}
    th, td {{ border: 1px solid GrayText; padding: 8px; text-align: left; vertical-align: top; }}
    th:nth-child(1), td:nth-child(1) {{ width: 100px; }}
    th:nth-child(3), td:nth-child(3), th:nth-child(4), td:nth-child(4) {{ width: 75px; }}
    th:nth-child(5), td:nth-child(5) {{ width: 100px; }}
    @media (max-width: 620px) {{
      .point {{ grid-template-columns: minmax(0, 1fr) 54px; }}
      .point .point-marks {{ grid-column: 2; }}
      .table-wrap {{ overflow-x: auto; }}
      table {{ min-width: 720px; }}
    }}
  </style>
</head>
<body>
  <main>
    <div class="controls">
      <select id="question" aria-label="Question"></select>
      <button type="button" data-view="paragraph" aria-pressed="true">Paragraph</button>
      <button type="button" data-view="table" aria-pressed="false">Table</button>
    </div>
    <div id="content"></div>
  </main>
  <script id="documents" type="application/json">{embedded}</script>
  <script>
    (() => {{
      const documents = JSON.parse(document.getElementById('documents').textContent);
      const select = document.getElementById('question');
      const content = document.getElementById('content');
      const buttons = document.querySelectorAll('[data-view]');
      let view = 'paragraph';

      const escapeHtml = (value) => String(value ?? '')
        .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;').replaceAll("'", '&#039;');

      documents.forEach((document, index) => {{
        const option = window.document.createElement('option');
        option.value = index;
        option.textContent = document.question_num;
        select.appendChild(option);
      }});

      function paragraph(document) {{
        return document.parts.map((part) => {{
          const points = (part.marking_points || []).map((point) => `
            <div class="point ${{point.is_alternative ? 'alternative' : ''}}">
              <div>${{escapeHtml(point.text)}}</div>
              <div>${{escapeHtml(point.tag)}}</div>
              <div class="point-marks">${{escapeHtml(point.marks)}}</div>
            </div>`).join('');
          const notes = (part.notes || []).map((note) => `<div class="notes">${{escapeHtml(note)}}</div>`).join('');
          return `<section class="part">
            <div class="part-head"><span>${{escapeHtml(part.label)}}</span><span>${{escapeHtml(part.marks)}}</span></div>
            ${{points}}${{notes}}
          </section>`;
        }}).join('');
      }}

      function table(document) {{
        const rows = document.parts.flatMap((part) => {{
          const points = part.marking_points || [];
          if (!points.length) {{
            return [`<tr><td>${{escapeHtml(part.label)}}</td><td>${{escapeHtml((part.notes || []).join('\\n'))}}</td><td></td><td>${{escapeHtml(part.marks)}}</td><td></td></tr>`];
          }}
          return points.map((point) => `<tr>
            <td>${{escapeHtml(part.label)}}</td><td>${{escapeHtml(point.text)}}</td>
            <td>${{escapeHtml(point.tag)}}</td><td>${{escapeHtml(point.marks)}}</td>
            <td>${{escapeHtml(point.is_alternative)}}</td>
          </tr>`);
        }}).join('');
        return `<div class="table-wrap"><table><thead><tr>
          <th>label</th><th>text</th><th>tag</th><th>marks</th><th>is_alternative</th>
        </tr></thead><tbody>${{rows}}</tbody></table></div>`;
      }}

      function render() {{
        const document = documents[Number(select.value) || 0];
        content.innerHTML = view === 'table' ? table(document) : paragraph(document);
      }}

      buttons.forEach((button) => button.addEventListener('click', () => {{
        view = button.dataset.view;
        buttons.forEach((item) => item.setAttribute('aria-pressed', String(item === button)));
        render();
      }}));
      select.addEventListener('change', render);
      render();
    }})();
  </script>
</body>
</html>'''
    destination.write_text(document, encoding="utf-8")


if __name__ == "__main__":
    main()
