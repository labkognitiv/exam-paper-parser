/* Two-option lesson checks; no persistence or additional interactions. */
document.querySelectorAll('.quick-check').forEach(check => {
  check.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', () => {
      check.querySelectorAll('button').forEach(option => option.setAttribute('aria-pressed', String(option === button)));
      check.dataset.result = button.dataset.correct === 'true' ? 'correct' : 'incorrect';
      check.querySelector('.check-feedback').textContent = button.dataset.feedback;
    });
  });
});
