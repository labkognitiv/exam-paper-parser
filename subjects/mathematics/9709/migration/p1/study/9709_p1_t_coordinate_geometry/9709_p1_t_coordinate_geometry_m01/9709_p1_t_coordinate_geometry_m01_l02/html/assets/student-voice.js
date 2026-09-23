document.addEventListener('DOMContentLoaded', () => {
  const main = document.querySelector('main');
  if (!main) return;

  const math = (tex, display = false) =>
    `<span class="math${display ? ' math-block' : ''}" data-tex="${tex.replaceAll('&', '&amp;').replaceAll('"', '&quot;')}">${tex}</span>`;
  const arrow = '<span class="legend-arrow" aria-hidden="true"></span>';
  const legend = (symbol, meaning) => `<p><span class="legend-symbol">${symbol}</span>${arrow}<span>${meaning}</span></p>`;
  const figure = (src, alt, caption) => `<figure class="generated-figure"><img src="assets/${src}" alt="${alt}"><figcaption>${caption}</figcaption></figure>`;
  const mini = (number, title, body) => `<article class="mini-example"><span>Example ${number}</span><h3>${title}</h3><p>${body}</p></article>`;

  document.querySelector('.hero .kicker').textContent = 'Coordinate Geometry · Lesson 2';
  document.querySelector('.hero h1').textContent = 'Parallel lines, perpendicular lines and perpendicular bisectors';
  document.querySelector('.hero p').innerHTML = 'We will take this slowly. First we will understand parallel lines. Next we will turn a line through 90°. Only then will we build a perpendicular bisector.';
  document.querySelector('.skip-link').setAttribute('href', '#parallel');
  document.querySelector('.hero a').setAttribute('href', '#parallel');

  const nav = document.querySelector('.lesson-nav');
  nav.innerHTML = '<span>Coordinate Geometry · Module 1 · Lesson 2</span><a href="#parallel">Parallel</a><a href="#perpendicular">Perpendicular</a><a href="#bisector">Bisectors</a><a href="#worked">Worked examples</a>';
  const bottomNav = document.querySelector('main > nav:last-of-type');
  if (bottomNav && bottomNav !== nav) bottomNav.innerHTML = '<a href="#parallel">Back to parallel lines</a><a href="#perpendicular">Back to perpendicular lines</a><a href="#bisector">Back to bisectors</a>';

  const sections = [...main.querySelectorAll(':scope > section')];
  sections.slice(5).forEach(section => section.remove());
  const [parallel, perpendicular, bisector, worked, equalDistance] = sections;
  parallel.id = 'parallel';
  perpendicular.id = 'perpendicular';
  bisector.id = 'bisector';
  worked.id = 'worked';
  equalDistance.id = 'equal-distance';

  parallel.innerHTML = `
    <p class="lesson-step">Part 1</p>
    <h2>Parallel lines: same direction, same gradient</h2>
    <p class="section-intro">Parallel lines point in exactly the same direction. The gap between them stays the same, so they never meet. On a graph, this means they have the <strong>same gradient</strong>.</p>
    <div class="formula-visual">
      <div class="formula-box simple-formula">
        <h3>The parallel-lines rule</h3>
        ${math('m_1=m_2', true)}
        <div class="formula-legend">
          ${legend(math('m_1'), 'gradient of the first line')}
          ${legend(math('m_2'), 'gradient of the second line')}
          ${legend('=', 'the gradients are the same')}
        </div>
      </div>
      ${figure('parallel-positive-v2.png', 'Two rising parallel lines, each with gradient 2', 'Both lines rise 2 squares for every 1 square across. Their gradients match, so they are parallel.')}
    </div>
    <p class="friendly-note"><strong>Read the picture first:</strong> if both lines rise in the same way, fall in the same way, stay flat, or are both vertical, they may be parallel. Then check the gradients.</p>
    <h3 class="gallery-heading">Parallel lines can look different</h3>
    <div class="visual-grid three-up">
      ${figure('parallel-negative-v2.png', 'Two falling parallel lines with gradient negative one half', '<strong>Falling lines:</strong> both gradients are −½.')}
      ${figure('parallel-horizontal-v2.png', 'Two horizontal parallel lines with gradient zero', '<strong>Horizontal lines:</strong> both gradients are 0.')}
      ${figure('parallel-vertical-v2.png', 'Two vertical parallel lines', '<strong>Vertical lines:</strong> both go straight up and never meet.')}
      ${figure('parallel-equations-v2.png', 'The parallel lines y equals 2x plus 1 and y equals 2x minus 3', '<strong>Different positions:</strong> the constant changes, but both gradients are 2.')}
      ${figure('parallel-not-v2.png', 'Two rising lines with gradients 2 and one half that meet', '<strong>Not parallel:</strong> both rise, but not at the same rate, so they meet.')}
    </div>
    <h3>Five quick parallel-line examples</h3>
    <div class="mini-example-grid">
      ${mini(1, `${math('m_1=3')}, ${math('m_2=3')}`, 'The gradients are equal. The lines are parallel.')}
      ${mini(2, `${math('m_1=-\\frac12')}, ${math('m_2=-\\frac12')}`, 'Both lines fall at the same rate. They are parallel.')}
      ${mini(3, `${math('y=2x+1')} and ${math('y=2x-3')}`, 'The number multiplying x is 2 in both equations. They are parallel.')}
      ${mini(4, `${math('y=-3x+4')} and ${math('y=-3x-9')}`, 'Both gradients are −3. They are parallel.')}
      ${mini(5, `${math('x=2')} and ${math('x=-5')}`, 'Both lines are vertical. They are parallel even though a vertical line has no gradient value.')}
    </div>`;

  perpendicular.innerHTML = `
    <p class="lesson-step">Part 2</p>
    <h2>Perpendicular lines: a 90° turn</h2>
    <p class="section-intro">Perpendicular lines meet at a <strong>right angle</strong>. That means the angle between them is 90°. One line may be steep while the other is gentle, but their gradients always follow one rule.</p>
    <div class="formula-visual">
      <div class="formula-box simple-formula">
        <h3>The perpendicular-lines rule</h3>
        ${math('m_1m_2=-1', true)}
        <div class="formula-legend">
          ${legend(math('m_1'), 'gradient of the first line')}
          ${legend(math('m_2'), 'gradient of the second line')}
          ${legend(math('-1'), 'their product when the angle is 90°')}
        </div>
      </div>
      ${figure('perpendicular-2-v2.png', 'Perpendicular lines with gradients 2 and negative one half', `Here ${math('2\\times(-\\frac12)=-1')}. The small square marks the 90° angle.`)}
    </div>
    <div class="formula-visual reverse">
      ${figure('perpendicular-third-v2.png', 'Perpendicular lines with gradients one third and negative 3', 'A gentle positive line needs a steep negative line to make 90°.')}
      <div class="formula-box simple-formula">
        <h3>How to find the new gradient</h3>
        ${math('m_{\\perp}=-\\frac1m', true)}
        <div class="formula-legend">
          ${legend(math('m'), 'the gradient you start with')}
          ${legend(math('m_{\\perp}'), 'the perpendicular gradient you need')}
          ${legend('−', 'the direction changes: rising becomes falling, or falling becomes rising')}
        </div>
        <p class="formula-instruction"><strong>In simple words:</strong> write the gradient as a fraction, flip the fraction, then change the sign.</p>
      </div>
    </div>
    <h3 class="gallery-heading">Different perpendicular pairs</h3>
    <div class="visual-grid three-up">
      ${figure('perpendicular-fractions-v2.png', 'Perpendicular lines with gradients negative three quarters and four thirds', `${math('-\\frac34')} becomes ${math('\\frac43')}: flip the fraction and change the sign.`)}
      ${figure('perpendicular-axis-v2.png', 'A horizontal line and vertical line meeting at 90 degrees', '<strong>Special case:</strong> a horizontal line is perpendicular to a vertical line.')}
      ${figure('perpendicular-not-v2.png', 'Lines with gradients 2 and one half meeting at a non-right angle', `${math('2\\times\\frac12=1')}, not −1. These lines are not perpendicular.`)}
    </div>
    <h3>Five quick perpendicular-line examples</h3>
    <div class="mini-example-grid">
      ${mini(1, `Start with ${math('m=2')}`, `Write ${math('2=\\frac21')}, flip to ${math('\\frac12')}, then change the sign. New gradient: ${math('-\\frac12')}.`)}
      ${mini(2, `Start with ${math('m=\\frac13')}`, `Flip ${math('\\frac13')} to ${math('3')}, then change the sign. New gradient: ${math('-3')}.`)}
      ${mini(3, `Start with ${math('m=-\\frac34')}`, `Flip to ${math('-\\frac43')}, then change the sign. New gradient: ${math('\\frac43')}.`)}
      ${mini(4, `Gradients ${math('5')} and ${math('-\\frac15')}`, `${math('5\\times(-\\frac15)=-1')}. The lines are perpendicular.`)}
      ${mini(5, `${math('y=2x+4')} and ${math('y=-\\frac12x+7')}`, 'The gradients are 2 and −½. Their product is −1, so the lines are perpendicular.')}
    </div>`;

  bisector.innerHTML = `
    <p class="lesson-step">Part 3</p>
    <h2>What is a perpendicular bisector?</h2>
    <p class="section-intro">The name tells us exactly what the line does. <strong>Perpendicular</strong> means it meets a segment at 90°. <strong>Bisector</strong> means it cuts that segment into two equal halves. It must do both jobs.</p>
    <div class="build-sequence">
      <div><span>1</span>${figure('bisector-segment-v2.png', 'A line segment joining A one comma one to B five comma three', '<strong>Start with a segment:</strong> A and B are its endpoints.')}</div>
      <div><span>2</span>${figure('bisector-midpoint-v2.png', 'The midpoint M three comma two halfway between A and B', '<strong>Find the midpoint:</strong> M is exactly halfway from A to B.')}</div>
      <div><span>3</span>${figure('bisector-definition-v2.png', 'A perpendicular bisector passing through midpoint M at 90 degrees', '<strong>Turn through 90°:</strong> draw the new line through M. Now we have a perpendicular bisector.')}</div>
    </div>
    <div class="definition-callout"><strong>So remember:</strong> through the midpoint + a 90° angle = perpendicular bisector.</div>
    <div class="formula-visual">
      <div class="formula-box simple-formula">
        <h3>First formula: find the midpoint</h3>
        ${math('M=\\left(\\frac{x_1+x_2}{2},\\frac{y_1+y_2}{2}\\right)', true)}
        <div class="formula-legend">
          ${legend(math('M'), 'the point halfway between A and B')}
          ${legend(math('x_1,x_2'), 'add the two x-values and divide by 2')}
          ${legend(math('y_1,y_2'), 'add the two y-values and divide by 2')}
        </div>
      </div>
      ${figure('bisector-midpoint-v2.png', 'Midpoint M splitting line segment AB into equal halves', 'The matching marks show that AM and MB have the same length.')}
    </div>
    <div class="formula-visual reverse">
      ${figure('bisector-fence-v2.png', 'A fence crossing path AB at its halfway point and at a right angle', 'Think of a fence crossing a path exactly halfway along, at a right angle.')}
      <div class="formula-box simple-formula">
        <h3>Second formula: turn the gradient</h3>
        ${math('m_{\\perp}=-\\frac1{m_{AB}}', true)}
        <div class="formula-legend">
          ${legend(math('m_{AB}'), 'gradient of the original segment AB')}
          ${legend(math('m_{\\perp}'), 'gradient of the perpendicular bisector')}
        </div>
      </div>
    </div>
    <div class="formula-box simple-formula wide-formula">
      <h3>Third formula: write the new line</h3>
      ${math('y-y_M=m_{\\perp}(x-x_M)', true)}
      <div class="formula-legend">
        ${legend(math('(x_M,y_M)'), 'the midpoint that the new line passes through')}
        ${legend(math('m_{\\perp}'), 'the new perpendicular gradient')}
        ${legend(math('(x,y)'), 'any point on the perpendicular bisector')}
      </div>
    </div>`;

  worked.innerHTML = `
    <p class="lesson-step">Part 4</p>
    <h2>Now work through complete examples</h2>
    <p class="section-intro">We will keep the same order every time: midpoint, original gradient, perpendicular gradient, then equation.</p>
    <div class="example-pair">
      <div class="worked-example">
        <p class="example-label">Worked example 1</p>
        <h3>Write a perpendicular line through a point</h3>
        <p>A line has gradient ${math('\\frac13')}. Find the perpendicular line through ${math('P=(2,3)')}.</p>
        <ol class="steps">
          <li><strong>Turn the gradient.</strong> Flip ${math('\\frac13')} to 3, then change the sign.${math('m_{\\perp}=-3', true)}</li>
          <li><strong>Use point P in the line formula.</strong>${math('y-3=-3(x-2)', true)}</li>
          <li><strong>Simplify.</strong>${math('y=-3x+9', true)}</li>
        </ol>
        <p class="answer"><strong>Answer:</strong> ${math('y=-3x+9')}</p>
      </div>
      <div class="worked-example">
        <p class="example-label">Worked example 2</p>
        <h3>Find a perpendicular bisector</h3>
        <p>${math('A=(1,1)')} and ${math('B=(5,3)')}. Find the perpendicular bisector of AB.</p>
        <ol class="steps">
          <li><strong>Midpoint:</strong>${math('M=\\left(\\frac{1+5}{2},\\frac{1+3}{2}\\right)=(3,2)', true)}</li>
          <li><strong>Gradient of AB:</strong>${math('m_{AB}=\\frac{3-1}{5-1}=\\frac12', true)}</li>
          <li><strong>Perpendicular gradient:</strong> flip ${math('\\frac12')} and change the sign.${math('m_{\\perp}=-2', true)}</li>
          <li><strong>Line through M:</strong>${math('y-2=-2(x-3)', true)}${math('y=-2x+8', true)}</li>
        </ol>
        <p class="answer"><strong>Answer:</strong> ${math('y=-2x+8')}</p>
      </div>
    </div>
    <div class="worked-visual">
      ${figure('bisector-definition-v2.png', 'Perpendicular bisector through midpoint M of AB', 'The equation describes the teal line: it passes through M and meets AB at 90°.')}
      ${figure('bisector-equal-v2.png', 'Point C on the perpendicular bisector equally far from A and B', 'Any point C on this line has equal distances to A and B.')}
    </div>`;

  equalDistance.innerHTML = `
    <p class="lesson-step">Part 5</p>
    <h2>One final idea: equal distance</h2>
    <p class="section-intro">A point on the perpendicular bisector is always the same distance from A and B. In the diagram, C lies on the bisector, so ${math('CA=CB')}.</p>
    <div class="formula-visual">
      ${figure('bisector-equal-v2.png', 'Point C joined to A and B with equal-length marks', 'The matching orange marks show that CA and CB have equal length.')}
      <div class="worked-example">
        <p class="example-label">Worked example 3</p>
        <h3>Find the line of points equally far from A and B</h3>
        <p>${math('A=(1,1)')}, ${math('B=(5,3)')} and ${math('C=(x,y)')}. We want ${math('AC=BC')}.</p>
        <ol class="steps">
          <li><strong>Square both distances.</strong>${math('(x-1)^2+(y-1)^2=(x-5)^2+(y-3)^2', true)}</li>
          <li><strong>Expand.</strong> The ${math('x^2')} and ${math('y^2')} terms cancel.${math('-2x-2y+2=-10x-6y+34', true)}</li>
          <li><strong>Collect and simplify.</strong>${math('8x+4y=32', true)}${math('y=-2x+8', true)}</li>
        </ol>
        <p class="answer"><strong>Answer:</strong> every possible point C lies on ${math('y=-2x+8')}, the same perpendicular bisector found above.</p>
      </div>
    </div>
    <p class="friendly-note"><strong>Final check:</strong> the pictured point ${math('C=(2,4)')} works because ${math('4=-2(2)+8')}. It lies on the perpendicular bisector.</p>`;
});
