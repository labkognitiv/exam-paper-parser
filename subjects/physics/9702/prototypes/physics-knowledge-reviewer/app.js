// Physics 9702 (2016) Interactive Question & Knowledge Platform Engine

const state = {
  paperIndex: 0,
  questionIndex: 0,
  activePartId: null,
  activeTab: 'learning',
  revealedHints: 0,
};

const $ = (id) => document.getElementById(id);

function escapeHtml(value = '') {
  return String(value).replace(/[&<>'"]/g, (c) => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    "'": '&#39;',
    '"': '&quot;',
  }[c]));
}

/**
 * Render mixed text containing $...$ or $$...$$ math spans using KaTeX
 */
function renderMath(text = '') {
  if (!text) return '';
  const str = String(text);
  if (!window.katex) return escapeHtml(str);

  // First handle display math $$...$$
  let parts = str.split(/(\$\$[\s\S]+?\$\$)/g);
  let html = '';

  for (let i = 0; i < parts.length; i++) {
    const segment = parts[i];
    if (segment.startsWith('$$') && segment.endsWith('$$')) {
      const math = segment.slice(2, -2).trim();
      try {
        html += `<div class="katex-display-wrap">${window.katex.renderToString(math, { displayMode: true, throwOnError: false })}</div>`;
      } catch (_) {
        html += `<code>${escapeHtml(math)}</code>`;
      }
    } else {
      // Handle inline math $...$
      const inlineParts = segment.split(/(\$[^\$\n]+?\$)/g);
      for (let j = 0; j < inlineParts.length; j++) {
        const item = inlineParts[j];
        if (item.startsWith('$') && item.endsWith('$')) {
          const math = item.slice(1, -1).trim();
          try {
            html += window.katex.renderToString(math, { displayMode: false, throwOnError: false });
          } catch (_) {
            html += `<code>${escapeHtml(math)}</code>`;
          }
        } else {
          // Regular text: preserve newlines
          const lines = escapeHtml(item).split('\n');
          html += lines.join('<br>');
        }
      }
    }
  }
  return html;
}

/**
 * Render a formula string directly with KaTeX display mode
 */
function renderFormula(latex = '') {
  if (!latex) return '';
  if (!window.katex) return `<code>${escapeHtml(latex)}</code>`;
  try {
    return window.katex.renderToString(latex, { displayMode: true, throwOnError: false });
  } catch (_) {
    return `<code>${escapeHtml(latex)}</code>`;
  }
}

function getPapers() {
  return window.REVIEW_DATA?.papers || [];
}

function currentData() {
  const papers = getPapers();
  const paper = papers[state.paperIndex] || papers[0];
  const question = paper?.questions[state.questionIndex] || paper?.questions[0];
  const leafParts = question?.parts.filter((p) => p.isLeaf) || [];
  let activePart = question?.parts.find((p) => p.id === state.activePartId);
  if (!activePart || !activePart.isLeaf) {
    activePart = leafParts[0] || question?.parts[0];
    if (activePart) state.activePartId = activePart.id;
  }
  return { paper, question, activePart, leafParts };
}

function renderFieldInput(field, index) {
  const id = escapeHtml(field.field_id || `answer-${index}`);
  const label = escapeHtml((field.label || field.role || 'answer').replaceAll('_', ' '));
  const choices = field.options || [];

  if (['single_choice', 'multiple_choice'].includes(field.control) && choices.length) {
    const type = field.control === 'multiple_choice' ? 'checkbox' : 'radio';
    return `
      <div class="field-control-group">
        <label class="field-label">${label}</label>
        <div class="choice-grid">
          ${choices.map((option) => `
            <label class="choice-card">
              <input type="${type}" name="${id}" value="${escapeHtml(option)}">
              <span>${renderMath(option)}</span>
            </label>
          `).join('')}
        </div>
      </div>`;
  }

  if (field.control === 'long_text') {
    return `
      <div class="field-control-group">
        <label class="field-label" for="${id}">${label}</label>
        <textarea id="${id}" class="answer-textarea" placeholder="Explain your physical reasoning, write out equations, and show working..."></textarea>
      </div>`;
  }

  const inputType = ['quantity', 'number'].includes(field.control) ? 'number' : 'text';
  const unitHtml = field.unit ? `<span class="unit-badge">${renderMath(field.unit_latex ? `$${field.unit_latex}$` : field.unit)}</span>` : '';

  return `
    <div class="field-control-group">
      <div class="input-with-label">
        <label class="field-label" for="${id}">${label}</label>
        <div class="input-unit-wrap">
          <input class="answer-input" id="${id}" type="${inputType}" placeholder="${field.control === 'math_expression' ? 'Enter formula / expression' : 'Enter value'}">
          ${unitHtml}
        </div>
      </div>
    </div>`;
}

function renderTableBlock(block) {
  const columns = block.columns || [];
  const header = columns.map((c) => `<th>${renderMath(c.label || c.column_id)}</th>`).join('');
  const body = (block.rows || []).map((row, rowIndex) => {
    if (row.cells?.length) {
      return `<tr>${columns.map((column, colIndex) => {
        const cell = row.cells.find((c) => c.column_id === column.column_id);
        if (!cell) return '<td></td>';
        if (cell.type === 'static') return `<td>${renderMath(cell.value)}</td>`;
        return `<td>${renderFieldInput(cell.field || {}, `${rowIndex}-${colIndex}`)}</td>`;
      }).join('')}</tr>`;
    }
    return `<tr>${columns.map((column, colIndex) => {
      if (colIndex === 0) return `<td class="row-label">${renderMath(row.row_id.replaceAll('_', ' '))}</td>`;
      const group = escapeHtml(`${block.block_id}-${row.row_id}`);
      return `<td><input type="radio" name="${group}" value="${escapeHtml(column.column_id)}"></td>`;
    }).join('')}</tr>`;
  }).join('');

  return `<table class="response-table"><thead><tr>${header}</tr></thead><tbody>${body}</tbody></table>`;
}

function renderResponseSchema(schema) {
  const blocks = schema?.blocks || [];
  if (!blocks.length) {
    return `<div class="response-box"><textarea class="answer-textarea" placeholder="Work through your calculation or explanation here..."></textarea></div>`;
  }
  return blocks.map((block) => {
    if (block.type === 'table') return `<div class="response-box">${renderTableBlock(block)}</div>`;
    if (block.type === 'canvas') {
      return `
        <div class="response-box canvas-box">
          <div class="canvas-header">
            <strong>Graph / Drawing Response</strong>
            <span class="canvas-tag">Assessed Drawing</span>
          </div>
          <p class="canvas-desc">Use the diagram canvas below to sketch or plot the required curve / diagram.</p>
          <div class="canvas-tools-placeholder">
            <span class="tool-pill">✏️ Pencil / Curve</span>
            <span class="tool-pill">📏 Line Tool</span>
            <span class="tool-pill">🧹 Eraser</span>
          </div>
        </div>`;
    }
    return `<div class="response-box">${(block.fields || []).map(renderFieldInput).join('')}</div>`;
  }).join('');
}

function renderFigureBlock(fig) {
  if (!fig || !fig.url) return '';
  return `
    <figure class="question-figure" id="${escapeHtml(fig.id)}">
      <img src="${escapeHtml(fig.url)}" alt="${escapeHtml(fig.label || 'Figure')}">
      ${fig.label ? `<figcaption>${renderMath(fig.label)}</figcaption>` : ''}
    </figure>`;
}

function populateSelectors() {
  const papers = getPapers();
  $('paper-select').innerHTML = papers.map((p, i) => `<option value="${i}">${escapeHtml(p.label)}</option>`).join('');
  populateQuestions();
}

function populateQuestions() {
  const { paper } = currentData();
  $('question-select').innerHTML = paper.questions.map((q, i) => `
    <option value="${i}">Question ${q.number} (${q.totalMarks} marks)</option>
  `).join('');
  state.questionIndex = 0;
  state.activePartId = null;
  state.revealedHints = 0;
  renderAll();
}

function renderAll() {
  const { paper, question, activePart, leafParts } = currentData();

  // Top badges & titles
  $('q-paper-badge').textContent = paper.label;
  $('q-marks-badge').textContent = `${question.totalMarks} Marks`;
  $('q-main-title').textContent = `Question ${question.number}`;
  $('modal-title').textContent = `${paper.label} · Question ${question.number} (Original Scan)`;
  $('modal-scan-img').src = question.image;
  $('modal-scan-img').alt = `Scanned question ${question.number}`;

  // 1. Render Left Column (Complete Question)
  const stemBlock = $('question-stem-block');
  const stemText = question.stemLatex || question.stem;
  if (stemText) {
    stemBlock.hidden = false;
    stemBlock.innerHTML = `<div class="stem-content">${renderMath(stemText)}</div>`;
  } else {
    stemBlock.hidden = true;
    stemBlock.innerHTML = '';
  }

  // Build figures map
  const figureMap = Object.fromEntries((question.figures || []).map((f) => [f.id, f]));

  // Render parts in flow
  const container = $('parts-flow-container');
  let partsHtml = '';

  // Render question-level figures placed after stem
  question.figures?.forEach((fig) => {
    if (fig.placement?.scope === 'question' || fig.placement?.position === 'after_stem') {
      partsHtml += renderFigureBlock(fig);
    }
  });

  question.parts.forEach((part) => {
    const isLeaf = part.isLeaf;
    const isActive = activePart && activePart.id === part.id;
    const partText = part.latex || part.text || '';

    // Attached figures for this part
    let partFiguresHtml = '';
    (part.figureIds || []).forEach((fid) => {
      const fig = figureMap[fid];
      if (fig) partFiguresHtml += renderFigureBlock(fig);
    });

    if (!isLeaf) {
      // Structural parent part (e.g. part (b) with introductory narrative & diagram)
      partsHtml += `
        <div class="part-parent-card" id="${escapeHtml(part.id)}">
          <div class="parent-label-row">
            <span class="parent-label">${escapeHtml(part.label)}</span>
            <div class="parent-text">${renderMath(partText)}</div>
          </div>
          ${partFiguresHtml}
        </div>`;
    } else {
      // Answerable leaf part
      partsHtml += `
        <article class="part-leaf-card ${isActive ? 'active-focused' : ''}" id="${escapeHtml(part.id)}" data-part-id="${escapeHtml(part.id)}">
          <div class="leaf-header">
            <div class="leaf-heading">
              <span class="leaf-label">${escapeHtml(part.label)}</span>
              <div class="leaf-text">${renderMath(partText)}</div>
            </div>
            <div class="leaf-meta">
              <span class="part-marks-chip">${part.marks} mark${part.marks === 1 ? '' : 's'}</span>
              <button class="btn-inspect-part ${isActive ? 'active' : ''}" type="button" data-part-id="${escapeHtml(part.id)}">
                ${isActive ? 'Active Part' : 'Inspect Part →'}
              </button>
            </div>
          </div>
          ${partFiguresHtml}
          <div class="leaf-answer-section">
            ${renderResponseSchema(part.responseSchema)}
          </div>
        </article>`;
    }
  });

  container.innerHTML = partsHtml;

  // Add click listeners to leaf cards and inspect buttons
  document.querySelectorAll('.part-leaf-card, .btn-inspect-part').forEach((elem) => {
    elem.addEventListener('click', (e) => {
      const pid = elem.dataset.partId || elem.closest('.part-leaf-card')?.dataset.partId;
      if (pid && pid !== state.activePartId) {
        state.activePartId = pid;
        state.revealedHints = 0;
        renderAll();
      }
    });
  });

  // 2. Render Right Column (Inspector)
  renderInspector(activePart, leafParts);
}

function renderInspector(activePart, leafParts) {
  if (!activePart) return;

  const enrich = activePart.enrichment;
  $('active-part-pill').textContent = `${activePart.label} · ${activePart.marks} Marks`;

  // Quick jump tabs for parts
  $('part-quick-nav').innerHTML = leafParts.map((p) => `
    <button class="nav-pill ${p.id === activePart.id ? 'active' : ''}" data-part-id="${p.id}" type="button">
      ${escapeHtml(p.label)}
    </button>
  `).join('');

  document.querySelectorAll('.part-quick-nav .nav-pill').forEach((btn) => {
    btn.addEventListener('click', () => {
      state.activePartId = btn.dataset.partId;
      state.revealedHints = 0;
      renderAll();
    });
  });

  if (!enrich) {
    $('insp-topic').textContent = 'No enrichment linked';
    return;
  }

  // 1. Classification & Syllabus
  $('insp-topic').textContent = enrich.mapping.topic || '-';
  $('insp-module').textContent = enrich.mapping.module || '-';
  $('insp-difficulty').innerHTML = [1, 2, 3, 4, 5].map((n) => `
    <span class="diff-bar ${n <= (enrich.difficulty || 2) ? 'on' : ''}"></span>
  `).join('');

  $('insp-patterns').innerHTML = (enrich.patterns || []).map((pat) => `
    <span class="pattern-pill">${escapeHtml(pat.replaceAll('_', ' '))}</span>
  `).join('');

  $('insp-outcomes').innerHTML = (enrich.mapping.outcomes || []).map((o) => `
    <div class="outcome-item">
      <span class="bullet">▸</span>
      <span>${renderMath(o)}</span>
    </div>
  `).join('');

  // Skills
  const skillsList = enrich.skills || [];
  $('insp-skills').innerHTML = skillsList.length ? skillsList.map((s, idx) => `
    <div class="skill-card ${idx === 0 ? 'primary-skill' : ''}">
      <div class="skill-header">
        <span class="skill-tag">${idx === 0 ? 'Primary Skill' : 'Supporting Skill'}</span>
        <strong class="skill-name">${escapeHtml(s.name)}</strong>
      </div>
      <p class="skill-desc">${renderMath(s.description)}</p>
    </div>
  `).join('') : '<p class="empty-text">No specialized skills tagged.</p>';

  // Formulas
  const formulasList = enrich.formulas || [];
  $('insp-formulas').innerHTML = formulasList.length ? formulasList.map((f) => `
    <div class="formula-card">
      <div class="formula-header">
        <strong class="formula-name">${escapeHtml(f.name)}</strong>
        <span class="formula-id">${escapeHtml(f.id)}</span>
      </div>
      <div class="formula-math">${renderFormula(f.latex)}</div>
    </div>
  `).join('') : '<p class="empty-text">No major mathematical formula registered.</p>';

  // Definitions
  const defList = enrich.definitions || [];
  const defSection = $('insp-def-section');
  if (defList.length) {
    defSection.hidden = false;
    $('insp-definitions').innerHTML = defList.map((d) => `
      <div class="definition-card">
        <strong class="def-term">${escapeHtml(d.term)}</strong>
        <p class="def-desc">${renderMath(d.description)}</p>
      </div>
    `).join('');
  } else {
    defSection.hidden = true;
  }

  // 2. Hint Ladder
  const hints = enrich.hints || [];
  $('hint-tab-counter').textContent = `${hints.length}`;
  $('hint-progress-badge').textContent = `${state.revealedHints} / ${hints.length} Revealed`;

  const hintContainer = $('hint-ladder-container');
  if (!hints.length) {
    hintContainer.innerHTML = '<p class="empty-text">No hints registered for this part.</p>';
    $('reveal-hint-btn').hidden = true;
  } else {
    $('reveal-hint-btn').hidden = false;
    $('reveal-hint-btn').textContent = state.revealedHints >= hints.length ? 'All Hints Revealed' : `Reveal Hint ${state.revealedHints + 1} of ${hints.length}`;
    $('reveal-hint-btn').disabled = state.revealedHints >= hints.length;

    let hintsHtml = '';
    for (let i = 0; i < hints.length; i++) {
      const isRevealed = i < state.revealedHints;
      hintsHtml += `
        <div class="hint-step ${isRevealed ? 'revealed' : 'locked'}">
          <div class="hint-step-header">
            <span class="hint-num">Hint ${i + 1}</span>
            <span class="hint-status">${isRevealed ? 'Revealed' : 'Locked'}</span>
          </div>
          <div class="hint-step-content">${isRevealed ? renderMath(hints[i]) : '<em>Click "Reveal Next Hint" to unlock step-by-step guidance.</em>'}</div>
        </div>`;
    }
    hintContainer.innerHTML = hintsHtml;
  }

  // 3. Walkthrough
  const walkthrough = enrich.walkthrough || [];
  $('walkthrough-steps').innerHTML = walkthrough.length ? walkthrough.map((step, idx) => `
    <li class="walkthrough-step-item">
      <div class="step-badge">Step ${idx + 1}</div>
      <div class="step-text">${renderMath(step)}</div>
    </li>
  `).join('') : '<p class="empty-text">No teacher walkthrough available.</p>';

  // 4. Mark Scheme
  const criteria = enrich.criteria || [];
  $('markscheme-criteria-list').innerHTML = criteria.length ? criteria.map((c) => `
    <div class="criterion-card">
      <div class="crit-top">
        <code class="crit-id">${escapeHtml(c.id)}${c.occurrence ? ` (Occur ${c.occurrence})` : ''}</code>
        ${c.alternatives?.length ? `<span class="alt-badge">Alt: ${escapeHtml(c.alternatives.join(', '))}</span>` : ''}
      </div>
      <div class="crit-official">
        <span class="crit-label">Official Mark Scheme:</span>
        <div class="crit-content">${renderMath(c.official)}</div>
      </div>
      <div class="crit-ai">
        <span class="crit-label">AI Marking Observable:</span>
        <div class="crit-content">${renderMath(c.observable)}</div>
      </div>
    </div>
  `).join('') : '<p class="empty-text">No criteria linked.</p>';

  // Checking mode card
  const checking = enrich.checking || {};
  $('checking-meta-card').innerHTML = `
    <div class="checking-grid">
      <div><span class="chk-label">Evaluation Mode:</span> <strong>${escapeHtml(checking.mode || 'hybrid')}</strong></div>
      <div><span class="chk-label">Full Marks on Deterministic:</span> <strong>${checking.fullMarks ? 'Yes' : 'No'}</strong></div>
      <div><span class="chk-label">Deterministic Checks:</span> <strong>${checking.deterministicCount || 0}</strong></div>
      <div><span class="chk-label">Rubric Items:</span> <strong>${criteria.length}</strong></div>
    </div>`;
}

// Event Listeners
$('paper-select').addEventListener('change', (e) => {
  state.paperIndex = Number(e.target.value);
  populateQuestions();
});

$('question-select').addEventListener('change', (e) => {
  state.questionIndex = Number(e.target.value);
  state.activePartId = null;
  state.revealedHints = 0;
  renderAll();
});

$('reveal-hint-btn').addEventListener('click', () => {
  const { activePart } = currentData();
  const hints = activePart?.enrichment?.hints || [];
  if (state.revealedHints < hints.length) {
    state.revealedHints++;
    renderInspector(activePart, currentData().leafParts);
  }
});

// Inspector Tab Switching
document.querySelectorAll('.inspector-tabs .tab-btn').forEach((btn) => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.inspector-tabs .tab-btn').forEach((b) => b.classList.remove('active'));
    document.querySelectorAll('.inspector-body .tab-pane').forEach((p) => p.classList.remove('active'));
    btn.classList.add('active');
    const tabName = btn.dataset.tab;
    state.activeTab = tabName;
    const pane = $(`tab-${tabName}`);
    if (pane) pane.classList.add('active');
  });
});

// Modal scan toggle
$('view-scan-btn').addEventListener('click', () => {
  $('scan-modal').hidden = false;
});
$('modal-close-btn').addEventListener('click', () => {
  $('scan-modal').hidden = true;
});
$('scan-modal').addEventListener('click', (e) => {
  if (e.target === $('scan-modal')) $('scan-modal').hidden = true;
});

// Init
populateSelectors();

