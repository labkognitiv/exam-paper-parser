document.querySelectorAll('[data-check-choice]').forEach(button => {
  button.addEventListener('click', () => {
    document.querySelectorAll('[data-check-choice]').forEach(option => {
      if (option.dataset.checkGroup === button.dataset.checkGroup) option.setAttribute('aria-pressed', String(option === button));
    });
    document.getElementById(button.dataset.feedbackTarget).textContent = button.dataset.feedback;
  });
});
