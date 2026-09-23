/* Local two-choice feedback, without persistence. */
document.querySelectorAll('.quick-check, .check').forEach(check => {
 const buttons=check.querySelectorAll('button');
 buttons.forEach(button => {button.setAttribute('type','button');button.setAttribute('aria-pressed','false');
  button.addEventListener('click',()=>{
   buttons.forEach(option=>option.setAttribute('aria-pressed',String(option===button)));
   if(button.dataset.feedback!==undefined){const feedback=check.querySelector('.check-feedback');feedback.textContent=button.dataset.feedback;feedback.setAttribute('role','status');feedback.setAttribute('aria-live','polite');}
   else {check.querySelectorAll('.feedback').forEach(feedback=>{feedback.style.display=feedback.dataset.f===button.dataset.c?'block':'none';feedback.setAttribute('role','status');feedback.setAttribute('aria-live','polite');});}
  });
 });
});
