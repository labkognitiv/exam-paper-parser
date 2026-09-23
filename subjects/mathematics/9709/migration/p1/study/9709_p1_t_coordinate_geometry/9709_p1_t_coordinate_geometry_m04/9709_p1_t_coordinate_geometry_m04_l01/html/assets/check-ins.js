/* Two-option lesson checks; no persistence or additional interactions. */
document.querySelectorAll('.quick-check').forEach(check => {
  const feedback = check.querySelector('.check-feedback');
  check.querySelectorAll('button[data-choice]').forEach(button => {
    button.addEventListener('click', () => {
      check.querySelectorAll('button[data-choice]').forEach(option => {
        option.setAttribute('aria-pressed', String(option === button));
      });
      const correct = button.dataset.choice === 'correct';
      check.dataset.result = correct ? 'correct' : 'incorrect';
      feedback.textContent = correct ? feedback.dataset.correct : feedback.dataset.incorrect;
    });
  });
});
