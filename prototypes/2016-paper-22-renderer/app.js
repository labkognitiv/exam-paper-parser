const questions = window.PAPER_DATA || [];
const state = Object.create(null);
let activeIndex = 0;

const nav = document.querySelector('#question-nav');
const content = document.querySelector('#question-content');
const questionLabel = document.querySelector('#question-label');
const questionMarks = document.querySelector('#question-marks');
const sourceImage = document.querySelector('#source-image');

function figureMap(question) {
  return Object.fromEntries((question.figures || []).map((figure) => [figure.id, figure]));
}

function saveValue(id, value) {
  state[id] = value;
  document.querySelector('#save-state').textContent = 'Saved in this tab';
}

function renderMixedText(element, latexValue, plainValue = '') {
  const source = latexValue || plainValue;
  if (!latexValue || !window.katex) {
    element.append(document.createTextNode(plainValue || source));
    return;
  }
  source.split(/(\$[^$]+\$)/g).forEach((segment) => {
    if (!segment) return;
    if (segment.startsWith('$') && segment.endsWith('$')) {
      const math = document.createElement('span');
      try {
        window.katex.render(segment.slice(1, -1), math, { throwOnError: false, strict: 'warn', trust: false });
      } catch (_) {
        math.textContent = segment.slice(1, -1);
      }
      element.append(math);
      return;
    }
    segment.split('\n').forEach((line, index) => {
      if (index) element.append(document.createElement('br'));
      element.append(document.createTextNode(line));
    });
  });
}

function textElement(tag, className, value, latexValue = '') {
  const element = document.createElement(tag);
  element.className = className;
  renderMixedText(element, latexValue, value);
  return element;
}

function textWithPlacedFigures(tag, className, plainValue, latexValue, placements, renderedFigures, warnings) {
  const element = document.createElement(tag);
  element.className = className;
  let plainCursor = 0;
  let latexCursor = 0;

  const ordered = placements.map((figure) => {
    const anchor = figure.placement?.anchor || '';
    return { figure, anchor, index: plainValue.indexOf(anchor) };
  }).sort((a, b) => a.index - b.index);

  ordered.forEach(({ figure, anchor, index }) => {
    if (!anchor || index < plainCursor || index < 0 || plainValue.indexOf(anchor, index + 1) >= 0) {
      warnings.push(`${figure.id}: placement anchor was not found exactly once`);
      return;
    }
    const anchorEnd = index + anchor.length;
    const latexIndex = latexValue ? latexValue.indexOf(anchor, latexCursor) : -1;
    if (latexValue && latexIndex >= 0) {
      renderMixedText(element, latexValue.slice(latexCursor, latexIndex + anchor.length), plainValue.slice(plainCursor, anchorEnd));
      latexCursor = latexIndex + anchor.length;
    } else {
      renderMixedText(element, '', plainValue.slice(plainCursor, anchorEnd));
    }
    element.append(figureElement(figure));
    renderedFigures.add(figure.id);
    plainCursor = anchorEnd;
  });

  if (latexValue && latexCursor > 0) renderMixedText(element, latexValue.slice(latexCursor), plainValue.slice(plainCursor));
  else renderMixedText(element, '', plainValue.slice(plainCursor));
  return element;
}

function fieldControl(field, showLabel = true) {
  const wrapper = document.createElement('div');
  wrapper.className = 'field';
  if (showLabel) {
    const label = document.createElement('label');
    label.htmlFor = field.field_id;
    renderMixedText(label, field.label_latex, field.label || field.role.replaceAll('_', ' '));
    wrapper.append(label);
  }

  let control;
  if (field.control === 'math_expression') {
    const bar = document.createElement('div');
    bar.className = 'symbol-bar';
    control = document.createElement('textarea');
    ['→', '+', '−', 'β⁻', 'ν̄', '¹', '₀', '₋₁'].forEach((symbol) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'symbol-button';
      button.textContent = symbol;
      button.addEventListener('click', () => {
        control.setRangeText(symbol, control.selectionStart, control.selectionEnd, 'end');
        control.dispatchEvent(new Event('input'));
      });
      bar.append(button);
    });
    wrapper.append(bar);
  } else {
    control = field.control === 'long_text' ? document.createElement('textarea') : document.createElement('input');
  }

  const row = document.createElement('div');
  row.className = 'field-row';
  control.id = field.field_id;
  control.value = state[field.field_id] || '';
  control.placeholder = field.control === 'math_expression' ? 'Enter the completed equation' : 'Enter answer';
  if (field.control === 'number' || field.control === 'quantity') control.inputMode = 'decimal';
  control.addEventListener('input', () => saveValue(field.field_id, control.value));
  row.append(control);
  if (field.unit) row.append(textElement('span', 'unit', field.unit, field.unit_latex ? `$${field.unit_latex}$` : ''));
  wrapper.append(row);
  return wrapper;
}

function fieldsBlock(block) {
  const element = document.createElement('div');
  element.className = 'answer-block';
  (block.segments || []).filter((segment) => segment.type === 'static_latex').forEach((segment) => {
    const value = segment.value.includes('\\rightarrow')
      ? '¹₀n →'
      : segment.value.replaceAll('\\mathrm', '').replaceAll('{', '').replaceAll('}', '');
    element.append(textElement('div', 'segment', value, `$${segment.value}$`));
  });
  const fields = block.fields || [];
  fields.forEach((field) => element.append(fieldControl(field, fields.length > 1)));
  return element;
}

function humanizeId(value = '') {
  return value.replaceAll('_', ' ').replace(/\b\w/g, (letter) => letter.toUpperCase());
}

function tableBlock(block, part) {
  const element = document.createElement('div');
  element.className = 'answer-block table-answer-block';
  const scroller = document.createElement('div');
  scroller.className = 'response-table-wrap';
  const table = document.createElement('table');
  table.className = 'response-table';
  const head = document.createElement('thead');
  const headRow = document.createElement('tr');

  (block.columns || []).forEach((column) => {
    const cell = document.createElement('th');
    cell.scope = 'col';
    cell.textContent = column.label || humanizeId(column.column_id);
    headRow.append(cell);
  });
  head.append(headRow);
  table.append(head);

  const body = document.createElement('tbody');
  const columns = block.columns || [];
  (block.rows || []).forEach((row) => {
    const tableRow = document.createElement('tr');
    const rowHeading = document.createElement('th');
    rowHeading.scope = 'row';
    rowHeading.textContent = row.label || humanizeId(row.row_id);
    tableRow.append(rowHeading);

    columns.slice(1).forEach((column) => {
      const cell = document.createElement('td');
      const inputId = `${block.block_id}_${row.row_id}_${column.column_id}`;
      if (part.answer_type === 'selection') {
        const label = document.createElement('label');
        label.className = 'table-choice';
        const input = document.createElement('input');
        input.type = 'radio';
        input.name = `${block.block_id}_${row.row_id}`;
        input.id = inputId;
        input.checked = state[`${block.block_id}_${row.row_id}`] === column.column_id;
        input.setAttribute('aria-label', `${rowHeading.textContent}: ${column.label || humanizeId(column.column_id)}`);
        input.addEventListener('change', () => saveValue(`${block.block_id}_${row.row_id}`, column.column_id));
        const tick = document.createElement('span');
        tick.className = 'table-tick';
        tick.textContent = '✓';
        label.append(input, tick);
        cell.append(label);
      } else {
        const input = document.createElement('input');
        input.type = 'text';
        input.id = inputId;
        input.value = state[inputId] || '';
        input.setAttribute('aria-label', `${rowHeading.textContent}: ${column.label || humanizeId(column.column_id)}`);
        input.addEventListener('input', () => saveValue(inputId, input.value));
        cell.append(input);
      }
      tableRow.append(cell);
    });
    body.append(tableRow);
  });
  table.append(body);
  scroller.append(table);
  element.append(scroller);
  return element;
}

function canvasBlock(block, figures) {
  const element = document.createElement('div');
  element.className = 'answer-block';
  const wrap = document.createElement('div');
  wrap.className = 'canvas-wrap';
  const background = document.createElement('img');
  background.className = 'canvas-background';
  background.alt = 'Question drawing area';
  background.src = figures[block.background_figure_id]?.prototype_file || '';
  const canvas = document.createElement('canvas');
  canvas.className = 'drawing-canvas';
  wrap.append(background, canvas);
  element.append(wrap);
  const clear = document.createElement('button');
  clear.type = 'button';
  clear.className = 'drawing-clear';
  clear.textContent = 'Clear drawing';
  element.append(clear);

  let drawing = false;
  const context = canvas.getContext('2d');
  function sizeCanvas() {
    canvas.width = background.naturalWidth || 900;
    canvas.height = background.naturalHeight || 500;
    context.lineWidth = Math.max(2, canvas.width / 350);
    context.lineCap = 'round';
    context.strokeStyle = '#b74328';
  }
  background.addEventListener('load', sizeCanvas);
  function point(event) {
    const rect = canvas.getBoundingClientRect();
    return [(event.clientX - rect.left) * canvas.width / rect.width, (event.clientY - rect.top) * canvas.height / rect.height];
  }
  canvas.addEventListener('pointerdown', (event) => {
    drawing = true;
    const [x, y] = point(event);
    context.beginPath();
    context.moveTo(x, y);
    canvas.setPointerCapture(event.pointerId);
  });
  canvas.addEventListener('pointermove', (event) => {
    if (!drawing) return;
    const [x, y] = point(event);
    context.lineTo(x, y);
    context.stroke();
  });
  canvas.addEventListener('pointerup', () => { drawing = false; });
  clear.addEventListener('click', () => context.clearRect(0, 0, canvas.width, canvas.height));
  return element;
}

function figureElement(figure) {
  const container = document.createElement('figure');
  container.className = 'question-figure';
  const image = document.createElement('img');
  image.src = figure.prototype_file;
  image.alt = figure.label || 'Question diagram';
  container.append(image);
  if (figure.label && !figure.label.toLowerCase().includes('scaffold')) {
    container.append(textElement('figcaption', '', figure.label));
  }
  return container;
}

function markSchemePart(question, partId) {
  return question.prototype_mark_scheme?.parts?.find((part) => part.id === partId) || null;
}

function markSchemePanel(markSchemePartData, part) {
  const panel = document.createElement('section');
  panel.className = 'mark-scheme-panel';
  panel.id = `${part.id}_mark_scheme`;
  panel.hidden = true;

  const header = document.createElement('header');
  header.className = 'mark-scheme-heading';
  const titleWrap = document.createElement('div');
  const eyebrow = document.createElement('span');
  eyebrow.className = 'mark-scheme-eyebrow';
  eyebrow.textContent = 'Official mark scheme';
  const title = document.createElement('h3');
  title.textContent = `${markSchemePartData.label || part.label} · ${markSchemePartData.marks} ${markSchemePartData.marks === 1 ? 'mark' : 'marks'}`;
  titleWrap.append(eyebrow, title);
  const seal = document.createElement('span');
  seal.className = 'examiner-seal';
  seal.textContent = 'MS';
  seal.setAttribute('aria-hidden', 'true');
  header.append(titleWrap, seal);
  panel.append(header);

  const list = document.createElement('ol');
  list.className = 'marking-points';
  (markSchemePartData.marking_points || []).forEach((point) => {
    const item = document.createElement('li');
    item.className = point.is_alternative ? 'marking-point alternative' : 'marking-point';
    const code = document.createElement('span');
    code.className = 'mark-code';
    code.textContent = point.tag || '•';
    const copy = document.createElement('div');
    copy.className = 'mark-copy';
    if (point.is_alternative) {
      const route = document.createElement('span');
      route.className = 'alternative-label';
      route.textContent = 'Alternative route';
      copy.append(route);
    }
    copy.append(textElement('p', '', point.text || '', point.text_latex || ''));
    const marks = document.createElement('span');
    marks.className = 'point-marks';
    marks.textContent = `+${point.marks}`;
    marks.setAttribute('aria-label', `${point.marks} mark${point.marks === 1 ? '' : 's'}`);
    item.append(code, copy, marks);
    list.append(item);
  });
  panel.append(list);
  return panel;
}

function partActions(part, question, panel) {
  const actions = document.createElement('div');
  actions.className = 'part-actions';
  const support = document.createElement('div');
  support.className = 'support-actions';
  const markScheme = markSchemePart(question, part.id);
  const controls = [
    ['MS', 'Mark scheme', Boolean(markScheme)],
    ['?', 'Hints', false],
    ['▶', 'Walkthrough', false],
    ['AI', 'AI help', false]
  ];
  controls.forEach(([icon, label, available]) => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'action-button';
    button.title = available ? label : `${label} (placeholder)`;
    button.setAttribute('aria-label', label);
    button.innerHTML = `<span class="action-icon">${icon}</span><span>${label}</span>`;
    if (label === 'Mark scheme') {
      button.classList.add('mark-scheme-button');
      button.disabled = !available;
      if (available && panel) {
        button.setAttribute('aria-controls', panel.id);
        button.setAttribute('aria-expanded', 'false');
        button.addEventListener('click', () => {
          const opening = panel.hidden;
          panel.hidden = !opening;
          button.setAttribute('aria-expanded', String(opening));
          button.classList.toggle('revealed', opening);
          button.querySelector('span:last-child').textContent = opening ? 'Hide mark scheme' : 'Mark scheme';
          if (opening) panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        });
      }
    }
    support.append(button);
  });
  const check = document.createElement('button');
  check.type = 'button';
  check.className = 'check-button';
  check.title = 'Check answer (placeholder)';
  check.innerHTML = '<span class="check-icon">✓</span><span>Check answer</span>';
  actions.append(support, check);
  return actions;
}

function renderQuestion(index) {
  activeIndex = index;
  const question = questions[index];
  const figures = figureMap(question);
  const parentIds = new Set(question.parts.map((part) => part.parent_id).filter(Boolean));
  const renderedFigures = new Set();
  const seenChildGroups = new Set();
  const warnings = [];
  content.replaceChildren();

  document.querySelectorAll('.question-tab').forEach((tab, tabIndex) => tab.classList.toggle('active', tabIndex === index));
  questionLabel.textContent = `${question.paper_code} · Question ${question.question_num}`;
  questionMarks.textContent = `${question.total_marks} marks`;
  sourceImage.src = question.prototype_image || '';
  sourceImage.alt = `Original ${question.paper_code}, Question ${question.question_num}`;

  const questionFigures = (question.figures || []).filter((figure) => figure.placement?.scope === 'question');
  const stemAnchoredFigures = questionFigures.filter((figure) => figure.placement?.position === 'after_stem_text');
  const afterStemFigures = questionFigures.filter((figure) => figure.placement?.position === 'after_stem');
  const partById = Object.fromEntries(question.parts.map((part) => [part.id, part]));

  function renderStem() {
    if (question.question_stem) {
      content.append(textWithPlacedFigures(
        'section', 'question-stem', question.question_stem, question.question_stem_latex || '',
        stemAnchoredFigures, renderedFigures, warnings
      ));
    }
    afterStemFigures.forEach((figure) => {
      content.append(figureElement(figure));
      renderedFigures.add(figure.id);
    });
  }

  function renderPart(part) {
    const isParent = parentIds.has(part.id) || part.marks === null;
    const section = document.createElement('section');
    section.className = isParent ? 'context-section' : 'part-section';

    if (part.question_text || !isParent) {
      const promptRow = document.createElement('div');
      promptRow.className = 'prompt-row';
      let displayLabel = part.label;
      if (part.parent_id) {
        if (seenChildGroups.has(part.parent_id)) displayLabel = `(${part.path.at(-1)})`;
        seenChildGroups.add(part.parent_id);
      }
      promptRow.append(textElement('span', 'part-label', displayLabel));
      const anchoredFigures = (question.figures || []).filter((figure) =>
        figure.placement?.scope === 'part' &&
        figure.placement?.part_id === part.id &&
        figure.placement?.position === 'after_text'
      );
      const prompt = textWithPlacedFigures(
        'div', 'part-prompt', part.question_text || '', part.question_text_latex || '',
        anchoredFigures, renderedFigures, warnings
      );
      promptRow.append(prompt);
      if (part.marks !== null) promptRow.append(textElement('span', 'part-marks', `[${part.marks}]`));
      section.append(promptRow);
    }

    (part.response_schema?.blocks || []).forEach((block) => {
      if (block.type === 'fields') section.append(fieldsBlock(block));
      if (block.type === 'table') section.append(tableBlock(block, part));
      if (block.type === 'canvas') {
        section.append(canvasBlock(block, figures));
        renderedFigures.add(block.background_figure_id);
      }
    });
    if (!isParent) {
      const officialPart = markSchemePart(question, part.id);
      const panel = officialPart ? markSchemePanel(officialPart, part) : null;
      section.append(partActions(part, question, panel));
      if (panel) section.append(panel);
    }
    if (section.childElementCount) content.append(section);
  }

  const flow = question.content_flow?.length
    ? question.content_flow
    : [{ type: 'stem' }, ...question.parts.map((part) => ({ type: 'part', part_id: part.id }))];
  flow.forEach((item) => {
    if (item.type === 'stem') renderStem();
    if (item.type === 'part' && partById[item.part_id]) renderPart(partById[item.part_id]);
  });

  (question.figures || []).filter((figure) => !renderedFigures.has(figure.id)).forEach((figure) => {
    warnings.push(`${figure.id}: figure was not placed by content_flow/placement metadata`);
  });
  if (warnings.length) {
    const warning = document.createElement('aside');
    warning.className = 'qa-warning';
    warning.innerHTML = '<strong>Placement metadata needs review</strong>';
    const list = document.createElement('ul');
    warnings.forEach((message) => {
      const item = document.createElement('li');
      item.textContent = message;
      list.append(item);
    });
    warning.append(list);
    content.prepend(warning);
  }
  document.querySelector('#previous').disabled = index === 0;
  document.querySelector('#next').disabled = index === questions.length - 1;
  window.scrollTo({ top: 0, behavior: 'instant' });
}

questions.forEach((question, index) => {
  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'question-tab';
  const [, session, variant] = question.paper_code.match(/^9702_([msw]\d{2})_(\d+)$/) || [];
  button.textContent = `${session || question.paper_code}/${variant || ''} Q${question.question_num}`;
  button.addEventListener('click', () => renderQuestion(index));
  nav.append(button);
});

document.querySelector('#previous').addEventListener('click', () => renderQuestion(activeIndex - 1));
document.querySelector('#next').addEventListener('click', () => renderQuestion(activeIndex + 1));
document.querySelector('#clear').addEventListener('click', () => {
  questions[activeIndex].parts.forEach((part) => {
    (part.response_schema?.blocks || []).forEach((block) => {
      (block.fields || []).forEach((field) => delete state[field.field_id]);
      (block.rows || []).forEach((row) => {
        delete state[`${block.block_id}_${row.row_id}`];
        (block.columns || []).slice(1).forEach((column) => delete state[`${block.block_id}_${row.row_id}_${column.column_id}`]);
      });
    });
  });
  renderQuestion(activeIndex);
  document.querySelector('#save-state').textContent = 'Responses stay in this tab';
});

if (questions.length) renderQuestion(0);
