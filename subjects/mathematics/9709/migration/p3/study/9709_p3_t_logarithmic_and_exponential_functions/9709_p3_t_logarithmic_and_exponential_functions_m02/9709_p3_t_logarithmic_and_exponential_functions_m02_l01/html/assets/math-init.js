document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-math]').forEach(node => {
    const tex = node.getAttribute('data-math');
    katex.render(tex, node, {
      displayMode: node.matches('.math-display'),
      throwOnError: false,
      strict: 'ignore',
      output: 'htmlAndMathml'
    });
  });
});
