/* global INTERNAL_QUESTION_DATA */
const data = window.INTERNAL_QUESTION_DATA;
const state = {
  moduleId: data.modules[0]?.id || '',
  lessonId: data.modules[0]?.lessons[0]?.id || '',
  questionId: data.modules[0]?.lessons[0]?.questions[0]?.question_id || '',
  partId: '',
  filter: 'all',
  tab: 'scheme',
  reviews: {},
};

const $ = (selector) => document.querySelector(selector);
const moduleSelect = $('#module-select');
const lessonSelect = $('#lesson-select');
const questionList = $('#question-list');
const questionContent = $('#question-content');
const questionMeta = $('#question-meta');
const supportContent = $('#support-content');
const reviewNote = $('#review-note');

function escapeHtml(value) {
  return String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

function currentModule() {
  return data.modules.find((item) => item.id === state.moduleId) || data.modules[0];
}

function currentLesson() {
  const module = currentModule();
  return module?.lessons.find((item) => item.id === state.lessonId) || module?.lessons[0];
}

function currentQuestion() {
  return currentLesson()?.questions.find((item) => item.question_id === state.questionId) || currentLesson()?.questions[0];
}

function currentSupportRecord() {
  const question = currentQuestion();
  if (!question?.question?.parts?.length) return question;
  return question.question.parts.find((part) => part.part_id === state.partId) || question.question.parts[0];
}

function visibleQuestions() {
  const questions = currentLesson()?.questions || [];
  if (state.filter === 'all') return questions;
  if (state.filter === 'flag') return questions.filter((question) => state.reviews[question.question_id]?.decision === 'flag');
  return questions.filter((question) => question.question_type === state.filter);
}

function renderSelectors() {
  moduleSelect.innerHTML = data.modules.map((module) => `<option value="${escapeHtml(module.id)}">${escapeHtml(module.title)}</option>`).join('');
  moduleSelect.value = state.moduleId;
  const module = currentModule();
  lessonSelect.innerHTML = (module?.lessons || []).map((lesson) => `<option value="${escapeHtml(lesson.id)}">${escapeHtml(lesson.title)}</option>`).join('');
  lessonSelect.value = state.lessonId;
}

function renderList() {
  const questions = visibleQuestions();
  if (!questions.some((question) => question.question_id === state.questionId)) state.questionId = questions[0]?.question_id || '';
  questionList.innerHTML = questions.length ? questions.map((question, index) => {
    const review = state.reviews[question.question_id];
    const detail = question.question_type === 'mcq' ? 'MCQ' : `${question.difficulty} theory`;
    return `<button class="question-link ${question.question_id === state.questionId ? 'active' : ''}" data-id="${escapeHtml(question.question_id)}" type="button">
      <span class="question-number">${index + 1}</span>
      <span class="question-label"><strong>${escapeHtml(question.short_label)}</strong><span>${escapeHtml(detail)}</span></span>
      <span class="decision-dot ${escapeHtml(review?.decision || '')}" aria-label="${escapeHtml(review?.decision || 'not reviewed')}"></span>
    </button>`;
  }).join('') : '<div class="empty">No questions match this filter.</div>';
  questionList.querySelectorAll('[data-id]').forEach((button) => button.addEventListener('click', () => {
    state.questionId = button.dataset.id;
    state.partId = '';
    render();
  }));
}

function renderQuestion() {
  const question = currentQuestion();
  if (!question) {
    questionMeta.innerHTML = '';
    questionContent.innerHTML = '<div class="empty">No question selected.</div>';
    supportContent.innerHTML = '';
    return;
  }
  const lesson = currentLesson();
  $('#crumb').textContent = `${currentModule().title} / ${lesson.title}`;
  questionMeta.innerHTML = `<span class="badge blue">${escapeHtml(question.question_type === 'mcq' ? 'MCQ' : `${question.difficulty} theory`)}</span><span class="badge">${question.marks} ${question.marks === 1 ? 'mark' : 'marks'}</span><span class="badge">${escapeHtml(question.question_id)}</span>`;
  const prompt = question.question;
  let body = `<p class="stem">${escapeHtml(prompt.stem)}</p>`;
  if (prompt.options) {
    body += `<div class="options">${Object.entries(prompt.options).map(([key, value]) => `<div class="option"><span class="option-key">${escapeHtml(key)}</span><span>${escapeHtml(value)}</span></div>`).join('')}</div>`;
  }
  if (prompt.parts) {
    if (!prompt.parts.some((part) => part.part_id === state.partId)) state.partId = prompt.parts[0].part_id;
    body += `<p class="part-cue">Select a part to inspect its support.</p>`;
    body += prompt.parts.map((part) => `<button class="part part-selector ${part.part_id === state.partId ? 'active' : ''}" data-part-id="${escapeHtml(part.part_id)}" type="button"><span class="part-heading"><span class="part-label">${escapeHtml(part.label)}</span><span>${escapeHtml(part.prompt)}</span><span class="marks">[${part.marks}]</span></span></button>`).join('');
  }
  questionContent.innerHTML = body;
  questionContent.querySelectorAll('[data-part-id]').forEach((button) => button.addEventListener('click', () => {
    state.partId = button.dataset.partId;
    renderQuestion();
  }));
  const review = state.reviews[question.question_id] || {};
  reviewNote.value = review.note || '';
  $('#pass').classList.toggle('selected', review.decision === 'pass');
  $('#flag').classList.toggle('selected', review.decision === 'flag');
  $('#save-status').textContent = review.updated_at ? `Saved ${new Date(review.updated_at).toLocaleString()}` : 'Not reviewed';
  renderSupport();
}

function renderSupport() {
  const question = currentQuestion();
  if (!question) return;
  const support = currentSupportRecord();
  const partLabel = support?.part_id ? `<p class="support-part">Support for ${escapeHtml(support.label)} · ${support.marks} ${support.marks === 1 ? 'mark' : 'marks'}</p>` : '';
  const item = (content, prefix = '') => `<div class="support-item">${prefix}${escapeHtml(content)}</div>`;
  if (state.tab === 'scheme') {
    const answer = question.correct_answer ? `<p class="correct-answer">Correct answer: ${escapeHtml(question.correct_answer)}</p>` : '';
    supportContent.innerHTML = partLabel + answer + (support.mark_scheme || []).map((point) => item(point.criterion, `<span class="mark-code">${escapeHtml(point.mark || 'M')}</span>`)).join('');
  } else if (state.tab === 'hints') {
    supportContent.innerHTML = partLabel + (support.hints || []).map((hint, index) => item(hint, `<strong>Hint ${index + 1}. </strong>`)).join('');
  } else if (state.tab === 'solution') {
    supportContent.innerHTML = partLabel + `<div class="support-item"><p>${escapeHtml(support.solution || '')}</p></div>`;
  } else if (state.tab === 'walkthrough') {
    supportContent.innerHTML = partLabel + (support.walkthrough || []).map((step, index) => item(step, `<strong>Step ${index + 1}. </strong>`)).join('');
  } else {
    const evidence = support.past_paper_inspiration || question.past_paper_inspiration || [];
    supportContent.innerHTML = partLabel + evidence.map((source) => item(source.testing_demand, `<strong>${escapeHtml(source.question_id)}. </strong>`)).join('');
  }
}

function renderProgress() {
  const all = data.modules.flatMap((module) => module.lessons.flatMap((lesson) => lesson.questions));
  const reviewed = all.filter((question) => ['pass', 'flag'].includes(state.reviews[question.question_id]?.decision)).length;
  $('#progress').textContent = `${reviewed} of ${all.length} reviewed`;
}

async function saveReview(decision) {
  const question = currentQuestion();
  if (!question) return;
  const review = { decision, note: reviewNote.value.trim(), updated_at: new Date().toISOString() };
  state.reviews[question.question_id] = review;
  localStorage.setItem('physics-internal-question-reviews-v1', JSON.stringify(state.reviews));
  try {
    const response = await fetch('/api/reviews', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({question_id: question.question_id, review}) });
    if (!response.ok) throw new Error('save failed');
  } catch {
    $('#save-status').textContent = 'Saved in this browser';
  }
  render();
}

function move(offset) {
  const questions = visibleQuestions();
  const index = questions.findIndex((question) => question.question_id === state.questionId);
  if (!questions.length) return;
  state.questionId = questions[Math.max(0, Math.min(questions.length - 1, index + offset))].question_id;
  state.partId = '';
  render();
}

function render() {
  renderSelectors();
  renderList();
  renderQuestion();
  renderProgress();
}

moduleSelect.addEventListener('change', () => {
  state.moduleId = moduleSelect.value;
  state.lessonId = currentModule().lessons[0]?.id || '';
  state.questionId = currentLesson()?.questions[0]?.question_id || '';
  state.partId = '';
  render();
});
lessonSelect.addEventListener('change', () => {
  state.lessonId = lessonSelect.value;
  state.questionId = currentLesson()?.questions[0]?.question_id || '';
  state.partId = '';
  render();
});
document.querySelectorAll('.filter').forEach((button) => button.addEventListener('click', () => {
  state.filter = button.dataset.filter;
  document.querySelectorAll('.filter').forEach((item) => item.classList.toggle('active', item === button));
  render();
}));
document.querySelectorAll('.tab').forEach((button) => button.addEventListener('click', () => {
  state.tab = button.dataset.tab;
  document.querySelectorAll('.tab').forEach((item) => item.classList.toggle('active', item === button));
  renderSupport();
}));
$('#previous').addEventListener('click', () => move(-1));
$('#next').addEventListener('click', () => move(1));
$('#pass').addEventListener('click', () => saveReview('pass'));
$('#flag').addEventListener('click', () => saveReview('flag'));
$('#open-library').addEventListener('click', () => $('.library').classList.add('open'));
$('#close-library').addEventListener('click', () => $('.library').classList.remove('open'));

async function start() {
  try {
    const response = await fetch('/api/reviews');
    if (response.ok) state.reviews = await response.json();
    else throw new Error('load failed');
  } catch {
    try { state.reviews = JSON.parse(localStorage.getItem('physics-internal-question-reviews-v1') || '{}'); } catch { state.reviews = {}; }
  }
  render();
}

start();
