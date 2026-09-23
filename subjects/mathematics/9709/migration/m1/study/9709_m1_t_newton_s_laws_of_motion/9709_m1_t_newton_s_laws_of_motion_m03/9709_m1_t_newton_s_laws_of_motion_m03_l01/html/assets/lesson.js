document.querySelectorAll('.tex').forEach(el => {
  try { katex.render(el.dataset.tex, el, {throwOnError:false, displayMode:el.classList.contains('math')}); }
  catch (_) { if (!el.textContent.trim()) el.textContent = el.dataset.tex; }
});

document.querySelectorAll('.check').forEach(card => card.querySelectorAll('button').forEach(btn => btn.addEventListener('click', () => {
  card.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed','false'));
  btn.setAttribute('aria-pressed','true');
  card.querySelector('.feedback').textContent = btn.dataset.feedback;
})));
