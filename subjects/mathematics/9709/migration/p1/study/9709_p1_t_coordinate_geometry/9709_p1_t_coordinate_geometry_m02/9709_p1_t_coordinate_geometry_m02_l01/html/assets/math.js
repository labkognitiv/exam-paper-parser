document.querySelectorAll('[data-tex]').forEach((node) => {
  if (!window.katex) return;
  window.katex.render(node.dataset.tex, node, {
    throwOnError: false,
    displayMode: node.dataset.display === 'true',
    output: 'htmlAndMathml'
  });
});
