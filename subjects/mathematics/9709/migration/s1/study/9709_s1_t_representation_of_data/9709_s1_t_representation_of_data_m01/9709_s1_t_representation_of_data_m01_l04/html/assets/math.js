document.querySelectorAll('[data-tex]').forEach(node=>{
  try{katex.render(node.dataset.tex,node,{throwOnError:false,displayMode:node.classList.contains('math-display')});}
  catch(error){node.textContent=node.dataset.tex;}
});
