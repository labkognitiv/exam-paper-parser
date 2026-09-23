/* Two-option lesson checks; no persistence or additional interactions. */
document.querySelectorAll('.quick-check').forEach(check => {
  const options = check.querySelector('.check-options');
  if (options && options.querySelectorAll('button').length === 1 && options.textContent.includes('B · 1/2')) {
    options.appendChild(Object.assign(document.createElement('button'), {
      type: 'button', textContent: 'B · 1/2'
    }));
    options.lastElementChild.dataset.correct = 'false';
    options.lastElementChild.dataset.feedback = 'Two Heads is one complete path, so multiply the two 1/2 factors: 1/4.';
  }
  check.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', () => {
      check.querySelectorAll('button').forEach(option => option.setAttribute('aria-pressed', String(option === button)));
      check.dataset.result = button.dataset.correct === 'true' ? 'correct' : 'incorrect';
      check.querySelector('.check-feedback').textContent = button.dataset.feedback;
    });
  });
});
