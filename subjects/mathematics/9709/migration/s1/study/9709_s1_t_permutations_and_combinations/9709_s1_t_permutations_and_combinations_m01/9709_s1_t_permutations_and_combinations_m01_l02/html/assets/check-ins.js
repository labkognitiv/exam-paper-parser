document.querySelectorAll('.quick-check').forEach((check) => {
  check.querySelectorAll('button').forEach((button) => {
    button.addEventListener('click', () => {
      check.querySelectorAll('button').forEach((option) => {
        option.setAttribute('aria-pressed', String(option === button));
      });
      check.querySelector('.check-feedback').textContent = button.dataset.feedback;
    });
  });
});
