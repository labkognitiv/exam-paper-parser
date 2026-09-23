document.querySelectorAll('.math[data-tex]').forEach((node) => {
  if (!window.katex) return;
  try { window.katex.render(node.dataset.tex, node, {throwOnError:false, output:'htmlAndMathml'}); }
  catch (_) { /* Keep editable text fallback. */ }
});
