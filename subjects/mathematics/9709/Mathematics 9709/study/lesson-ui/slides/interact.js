/* Slide-lesson interactions beyond typed answers. Load after deck.js.
   Every type is written as plain HTML in the lesson; only predict and tap need a few lines of lesson script.

   predict  <div class="turn predict" data-predict="key"> question + .opts buttons (one data-ok, each data-fb) + .verdict
            lesson script: predicts.key = async board => { ...animate what really happens... }
   sort     <div class="turn sort"> .chips > button.chip[data-g][data-why]  +  .bins > .bin[data-g] > h4 + .got
   order    <div class="turn order"> ol + .chips > button.chip[data-n="1..n"][data-why]
   tap      <section ... data-tap="key">   lesson script: taps.key = { target: [x, y], near: (x, y) => "message" }
   flip     .fcard buttons: tap to turn
   rows     table.big tr.hid + button[data-rows]: shows the next hidden row
   explore  a lab slide: the lesson's scene uses board.drag(...) and board.redraw(...)          */

window.predicts = window.predicts || {};
window.taps = window.taps || {};
const say = (el, msg, good) => { el.textContent = msg; el.style.color = good ? "#08756f" : "#c2562b"; };

/* coming back to a slide starts its questions afresh (like its worked steps); deck.js calls this from show() */
const resetters = [];
window.resetTurns = slide => resetters.forEach(([t, f]) => slide.contains(t) && f());

/* predict: commit to a guess, then watch what really happens */
document.querySelectorAll(".predict").forEach(t => {
  const fb = t.querySelector(".verdict");
  resetters.push([t, () => { t.querySelectorAll(".opts button").forEach(b => { b.disabled = false; b.classList.remove("right", "wrong"); }); fb.textContent = ""; }]);
  t.querySelectorAll(".opts button").forEach(btn => btn.onclick = async () => {
    t.querySelectorAll(".opts button").forEach(b => b.disabled = true);
    const good = btn.hasAttribute("data-ok");
    btn.classList.add(good ? "right" : "wrong");
    say(fb, "Watch the board…", true); fb.style.color = "#655f70";
    await t.closest(".slide")._scene;                // let the opening drawing finish first
    const f = predicts[t.dataset.predict], b = t.closest(".slide")._b;
    if (f && b) await f(b);
    t.querySelector(".opts [data-ok]").classList.add("right");
    say(fb, btn.dataset.fb, good);
  });
});

/* sort: tap a card, then tap the group it belongs to */
document.querySelectorAll(".sort").forEach(t => {
  const fb = t.querySelector(".fb"), box = t.querySelector(".chips"), all = [...box.querySelectorAll(".chip")]; let sel = null;
  const left = () => t.querySelectorAll(".chips .chip").length;
  resetters.push([t, () => { sel = null; all.forEach(c => { c.classList.remove("ok", "sel", "no"); box.appendChild(c); }); t.querySelectorAll(".bin").forEach(b => b.classList.remove("hot")); fb.textContent = ""; }]);
  all.forEach(c => c.onclick = () => {
    if (c.classList.contains("ok")) return;
    t.querySelectorAll(".chip.sel").forEach(x => x.classList.remove("sel"));
    sel = c; c.classList.add("sel");
    t.querySelectorAll(".bin").forEach(b => b.classList.add("hot"));
  });
  t.querySelectorAll(".bin").forEach(bin => bin.onclick = () => {
    if (!sel) return;
    t.querySelectorAll(".bin").forEach(b => b.classList.remove("hot"));
    if (sel.dataset.g === bin.dataset.g) {
      sel.classList.remove("sel"); sel.classList.add("ok");
      bin.querySelector(".got").appendChild(sel);
      say(fb, left() ? "Yes. " + (sel.dataset.yes || "") : "All sorted. " + (sel.dataset.yes || ""), true);
    } else {
      sel.classList.remove("no"); void sel.offsetWidth; sel.classList.add("no");
      say(fb, sel.dataset.why || "Not that group. Look again.", false);
    }
    sel = null;
  });
});

/* order: tap the steps in the order you would do them */
document.querySelectorAll(".order").forEach(t => {
  const fb = t.querySelector(".fb"), list = t.querySelector("ol"), box = t.querySelector(".chips"), all = [...box.querySelectorAll(".chip")];
  resetters.push([t, () => { list.replaceChildren(); all.forEach(c => { c.classList.remove("no"); box.appendChild(c); }); fb.textContent = ""; }]);
  all.forEach(c => c.onclick = () => {
    const next = list.children.length + 1;
    if (+c.dataset.n === next) {
      const li = document.createElement("li"); li.textContent = c.textContent; list.appendChild(li); c.remove();
      say(fb, t.querySelector(".chips .chip") ? "Yes. What comes next?" : "That's the whole method, in order.", true);
    } else {
      c.classList.remove("no"); void c.offsetWidth; c.classList.add("no");
      say(fb, c.dataset.why || "Not yet. What do you need first?", false);
    }
  });
});

/* tap: tap a place on the board; it snaps to the nearest grid point */
document.querySelectorAll("[data-tap]").forEach(slide => {
  const fb = slide.querySelector(".fb");
  resetters.push([slide, () => { slide._tap && slide._tap.remove(); slide._tap = null; if (fb) fb.textContent = ""; }]);
  slide.querySelector("svg").addEventListener("click", ev => {
    const b = slide._b, cfg = taps[slide.dataset.tap]; if (!b || !cfg) return;
    const [wx, wy] = b.toWorld(ev).map(v => Math.round(v));
    slide._tap && slide._tap.remove();
    const good = wx === cfg.target[0] && wy === cfg.target[1];
    slide._tap = b.el("circle", { cx: b.X(wx), cy: b.Y(wy), r: 9, fill: "none", stroke: good ? C.along : C.up, "stroke-width": 3 });
    say(fb, good ? cfg.yes : cfg.near(wx, wy), good);
    if (good && cfg.onYes) cfg.onYes(b);               // optional: draw something once the tap is right
  });
});

/* flip cards and one-row-at-a-time tables */
/* card faces are flex columns: keep runs of text, sup, sub, i… together on one line (b, small, br start new lines) */
document.querySelectorAll(".fcard .fa, .fcard .fb2").forEach(face => {
  let run = null;
  [...face.childNodes].forEach(n => {
    const brk = n.nodeType === 1 && ["B", "SMALL", "BR", "DIV", "P", "UL", "OL"].includes(n.tagName);
    if (brk) { run = null; return; }
    if (n.nodeType === 3 && !n.textContent.trim() && !run) return;
    if (!run) { run = document.createElement("span"); n.before(run); }
    run.appendChild(n);
  });
});
document.querySelectorAll(".fcard").forEach(c => { c.onclick = () => c.classList.toggle("on"); resetters.push([c, () => c.classList.remove("on")]); });
document.querySelectorAll("button[data-rows]").forEach(btn => btn.onclick = () => {
  const row = btn.closest(".slide").querySelector("tr.hid:not(.on)");
  if (row) row.classList.add("on");
  if (!btn.closest(".slide").querySelector("tr.hid:not(.on)")) btn.disabled = true;
});
document.querySelectorAll("button[data-rows]").forEach(btn => resetters.push([btn, () => { btn.closest(".slide").querySelectorAll("tr.hid.on").forEach(r => r.classList.remove("on")); btn.disabled = false; }]));

/* typed answers and choices live in deck.js; they start afresh too */
document.querySelectorAll(".turn[data-check]").forEach(t => resetters.push([t, () => { t.querySelectorAll("input").forEach(i => i.value = ""); t.querySelector(".fb").textContent = ""; }]));
document.querySelectorAll(".turn[data-mcq]").forEach(t => resetters.push([t, () => { t.querySelectorAll(".opts button").forEach(b => b.classList.remove("right", "wrong")); t.querySelector(".fb").textContent = ""; }]));
