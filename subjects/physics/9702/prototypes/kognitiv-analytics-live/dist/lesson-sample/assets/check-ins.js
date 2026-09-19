document.querySelectorAll('.check').forEach(check => {
  const feedback = check.querySelector('.feedback');
  check.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', () => {
      check.querySelectorAll('button').forEach(option => option.setAttribute('aria-pressed', String(option === button)));
      feedback.textContent = button.dataset.feedback;
      feedback.className = `feedback show ${button.dataset.correct === 'true' ? 'correct' : 'incorrect'}`;
    });
  });
});
