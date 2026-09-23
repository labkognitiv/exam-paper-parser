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
document.querySelectorAll('.check-in').forEach(check => {
  const feedback = check.querySelector('.feedback');
  check.querySelectorAll('button').forEach(button => button.addEventListener('click', () => {
    check.querySelectorAll('button').forEach(option => option.setAttribute('aria-pressed', String(option === button)));
    check.dataset.result = button.dataset.correct === 'true' ? 'correct' : 'incorrect';
    feedback.textContent = button.dataset.correct === 'true' ? 'Correct. Gravity acts downwards, so acceleration is negative when upwards is positive.' : 'Check the direction: gravity acts downwards, so acceleration is negative when upwards is positive.';
  }));
});
