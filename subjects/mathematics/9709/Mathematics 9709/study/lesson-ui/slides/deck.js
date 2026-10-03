/* Slide-lesson runtime: navigation, worked steps, answer checks. Load after the lesson script. */
/* ============ slide navigation ============ */
const slides = [...document.querySelectorAll(".slide")];
const prev = document.getElementById("prev"), next = document.getElementById("next"), count = document.getElementById("count"), bar = document.getElementById("bar");
let cur = 0;
function play(slide, alt) {
  const id = ++run;
  slide.querySelectorAll(".ws").forEach(resetWs);
  const done = slide.dataset.board ? scenes[slide.dataset.board](slide, () => id === run, alt) : Promise.resolve();
  slide._scene = Promise.resolve(done).catch(() => {});   // steps, reveals and predicts wait for this instead of cancelling it
  // early worked examples open by themselves, one step after another
  const open = slide.querySelector(".ws[data-open]");
  if (open && !alt) Promise.resolve(done).then(async () => {
    const n = open.querySelectorAll("li").length;
    while (id === run && (open._i || 0) < n) { await stepWs(open); await wait(900); }
  });
}
function show(n) {
  cur = Math.max(0, Math.min(slides.length - 1, n));
  slides.forEach((s, k) => s.classList.toggle("active", k === cur));
  count.textContent = `${cur + 1} / ${slides.length}`;
  bar.style.width = `${(cur + 1) / slides.length * 100}%`;
  prev.disabled = cur === 0; next.disabled = cur === slides.length - 1;
  window.resetTurns && resetTurns(slides[cur]);     // questions start afresh on every visit (interact.js)
  play(slides[cur]);
}
prev.onclick = () => show(cur - 1);
next.onclick = () => show(cur + 1);
document.addEventListener("keydown", e => {
  if (e.target.tagName === "INPUT") return;
  if (e.key === "ArrowRight") show(cur + 1);
  if (e.key === "ArrowLeft") show(cur - 1);
});
slides.forEach(s => { const r = s.querySelector(".replay"); if (r) r.onclick = () => {
  // the board is redrawn, so a predict (which drew on it) can be tried again
  s.querySelectorAll(".predict").forEach(t => { t.querySelectorAll(".opts button").forEach(b => { b.disabled = false; b.classList.remove("right", "wrong"); }); t.querySelector(".verdict").textContent = ""; });
  play(s);
}; });

/* vertical working: each line "lhs = rhs"; a line starting "= " continues; "!" marks the answer.
   Powers and subscripts in plain text: x^{3/2}, x^(3/2), x^½, x^2 → superscript; m_{AB}, x_1 → subscript. */
const scripts = t => t
  .replace(/\^\{([^}]*)\}/g, "<sup>$1</sup>").replace(/\^\(([^()]*)\)/g, "<sup>$1</sup>")
  .replace(/\^([0-9½⅓¼¾⅔−\-]+|[A-Za-z])/g, "<sup>$1</sup>")
  .replace(/_\{([^}]*)\}/g, "<sub>$1</sub>").replace(/_([A-Za-z0-9]+)/g, "<sub>$1</sub>");
document.querySelectorAll(".calc").forEach(el => {
  el.innerHTML = el.textContent.split("\n").map(l => l.trim()).filter(Boolean).map(l => {
    const hl = l.startsWith("!") ? " hl" : ""; if (hl) l = l.slice(1).trim();
    let lhs, rhs;
    l = scripts(l);
    if (l.startsWith("= ")) { lhs = ""; rhs = l.slice(2); }
    else { const i = l.indexOf(" = "); if (i < 0) return `<span class="full${hl}">${l}</span>`; lhs = l.slice(0, i); rhs = l.slice(i + 3); }
    return `<span class="l${hl}">${lhs}</span><span class="e${hl}">=</span><span class="r${hl}">${rhs}</span>`;
  }).join("");
});

/* worked steps */
function resetWs(ws) {
  ws.querySelectorAll("li").forEach(li => li.classList.remove("on"));
  ws.querySelectorAll("button").forEach(b => b.disabled = false);
  const nb = ws.querySelector(".nxt"); if (nb) nb.textContent = "Show step 1";   // buttons are optional on data-open examples
  ws._i = 0; ws._busy = null;
}
async function stepWs(ws) {
  const lis = ws.querySelectorAll("li"), i = ws._i || 0;
  if (i >= lis.length) return;
  ws._i = i + 1;                                    // claim the step now, so double clicks can't repeat it
  await ws.closest(".slide")._scene;                // let the opening drawing finish; the step builds on it
  lis[i].classList.add("on");
  const nb = ws.querySelector(".nxt");
  if (nb) nb.textContent = ws._i < lis.length ? `Show step ${ws._i + 1}` : "Done";
  if (ws._i >= lis.length) ws.querySelectorAll("button").forEach(b => b.disabled = true);
  const f = (acts[ws.dataset.ws] || [])[i], b = ws.closest(".slide")._b;
  if (f && b) await f(b);
}
document.querySelectorAll(".ws").forEach(ws => {
  const nb = ws.querySelector(".nxt"), ab = ws.querySelector(".all");
  if (nb) nb.onclick = async () => { if (ws._busy) return; ws._busy = stepWs(ws); await ws._busy; ws._busy = null; };
  if (ab) ab.onclick = async () => {
    if (ws._busy) await ws._busy;
    const n = ws.querySelectorAll("li").length;
    while ((ws._i || 0) < n) { ws._busy = stepWs(ws); await ws._busy; ws._busy = null; }
  };
});

/* your turn: typed answers */
document.querySelectorAll(".turn[data-check]").forEach(t => {
  const form = t.querySelector("form"), fb = t.querySelector(".fb"), key = t.dataset.check;
  form.onsubmit = e => {
    e.preventDefault();
    const vals = [...form.querySelectorAll("input")].map(i => num(i.value));
    const [good, msg, alt] = checks[key](vals);
    fb.textContent = msg;
    fb.style.color = good ? "#08756f" : "#c2562b";
    if (good && alt) play(t.closest(".slide"), alt);
  };
});

/* your turn: choices */
document.querySelectorAll(".turn[data-mcq]").forEach(t => {
  const fb = t.querySelector(".fb");
  t.querySelectorAll(".opts button").forEach(btn => btn.onclick = () => {
    t.querySelectorAll(".opts button").forEach(x => x.classList.remove("right", "wrong"));
    const good = btn.hasAttribute("data-ok");
    btn.classList.add(good ? "right" : "wrong");
    fb.textContent = btn.dataset.fb; fb.style.color = good ? "#08756f" : "#c2562b";
  });
});

document.querySelectorAll(".reveal button").forEach(btn => btn.onclick = () => {
  const slide = btn.closest(".slide"), k = btn.dataset.r;
  document.getElementById("r-" + k).classList.add("on");
  btn.disabled = true;
  Promise.resolve(slide._scene).then(() => reveals[k](slide._b));
});

document.fonts.ready.then(() => show(0));
