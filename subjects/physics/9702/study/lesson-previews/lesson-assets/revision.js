(() => {
  'use strict';
  const key = 'kognitiv.revision-gems.v1';
  const drawer = document.getElementById('gem-sidebar');
  const list = document.getElementById('gem-list');
  const notice = document.getElementById('gem-notice');
  let saved = [], catalog = [], persistent = true;
  const valid = x => x && typeof x.id === 'string' && ['Definition','Formula'].includes(x.kind) && ['title','text','subject'].every(k => typeof x[k] === 'string');
  function read() {
    try { const data = JSON.parse(localStorage.getItem(key) || '[]'); return Array.isArray(data) ? data.filter(valid) : []; }
    catch (_) { persistent = false; return []; }
  }
  saved = read();
  function render() {
    saved = [...new Map(saved.map(g => [g.id,g])).values()];
    document.getElementById('gem-count').textContent = saved.length;
    document.querySelectorAll('[data-gem-id]').forEach(button => {
      const collected = saved.some(g => g.id === button.dataset.gemId);
      button.textContent = collected ? '✓ Collected' : '◇ Collect gem';
      button.disabled = collected || !catalog.some(g => g.id === button.dataset.gemId);
      button.setAttribute('aria-label', (collected ? 'Collected: ' : 'Collect: ') + ((catalog.find(g => g.id === button.dataset.gemId)?.kind || '') + ': ' + (catalog.find(g => g.id === button.dataset.gemId)?.title || 'gem')));
    });
    list.replaceChildren();
    if (!saved.length) { const p = document.createElement('li'); p.textContent = 'Your collection is empty. Collect gems beside new definitions and formulas as you work through the lessons.'; list.append(p); }
    saved.forEach(g => {
      const item = document.createElement('li');
      const title = document.createElement('h3'); title.textContent = g.title;
      const meta = document.createElement('p'); meta.className = 'gem-meta'; meta.textContent = g.subject + ' · ' + g.kind;
      const body = document.createElement('p'); body.textContent = g.text;
      if (g.kind === 'Formula' && window.katex) katex.render(g.text, body, {displayMode:true,throwOnError:false,trust:false});
      const remove = document.createElement('button'); remove.type = 'button'; remove.className = 'gem-remove'; remove.textContent = 'Remove'; remove.setAttribute('aria-label', 'Remove ' + g.kind.toLowerCase() + ': ' + g.title);
      remove.addEventListener('click', () => { saved = [...new Map([...read(),...saved].map(x=>[x.id,x])).values()].filter(x=>x.id !== g.id); try { localStorage.setItem(key, JSON.stringify(saved)); } catch (_) { persistent = false; } render(); });
      item.append(meta,title,body,remove); list.append(item);
    });
    notice.textContent = persistent ? '' : 'Browser storage is unavailable. New gems will stay only while this page is open.';
  }
  document.getElementById('open-gems').addEventListener('click', () => drawer.showModal());
  document.getElementById('close-gems').addEventListener('click', () => drawer.close());
  drawer.addEventListener('click', e => { if(e.target === drawer && e.clientX < drawer.getBoundingClientRect().left) drawer.close(); });
  document.querySelectorAll('[data-gem-id]').forEach(button => button.addEventListener('click', () => {
    const gem = catalog.find(g => g.id === button.dataset.gemId);
    if (!gem || saved.some(g => g.id === gem.id)) return;
    // Merge other lessons' saved gems before writing; never replace the collection with this lesson alone.
    const existing = read(); saved = [...new Map([...existing,...saved,gem].map(g=>[g.id,g])).values()];
    try { localStorage.setItem(key, JSON.stringify(saved)); } catch (_) { persistent = false; }
    render(); document.getElementById('gem-announcement').textContent = gem.title + ' collected.';
  }));
  window.addEventListener('storage', e => { if (e.key === key) { saved = read(); render(); } });
  document.querySelectorAll('.quick-check').forEach(check => {
    check.querySelectorAll('button').forEach(button => button.addEventListener('click', () => {
      check.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
      check.dataset.result = button.dataset.correct === 'true' ? 'correct' : 'incorrect';
      check.querySelector('.check-feedback').textContent = button.dataset.feedback;
    }));
  });
  render();
  fetch('assets/gems.json').then(r => { if (!r.ok) throw Error(); return r.json(); }).then(data => { catalog = data.filter(valid); render(); }).catch(() => { notice.textContent = 'Definition records could not load. Reload to collect new gems.'; });
})();
