document.addEventListener('click',event=>{
  const button=event.target.closest('[data-choice]');
  if(!button)return;
  const card=button.closest('.check');
  card.querySelectorAll('[data-choice]').forEach(item=>item.setAttribute('aria-pressed','false'));
  button.setAttribute('aria-pressed','true');
  card.querySelector('.feedback').textContent=button.dataset.feedback;
});
