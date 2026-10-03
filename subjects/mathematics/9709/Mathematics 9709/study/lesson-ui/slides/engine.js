/* Slide-lesson engine: graph-paper boards drawn from real coordinates. Shared by every lesson deck. */
/* ============ board engine: grids drawn from real coordinates ============ */
const NS = "http://www.w3.org/2000/svg";
const C = { ink: "#302b40", muted: "#655f70", along: "#08756f", up: "#c2562b", plum: "#29213f", mid: "#5b3fa8", line: "#8a84a0", faint: "#b9b4c8" };
const D = ms => window.FAST ? 1 : ms;                 // FAST = skip animation (used by the layout check)
const wait = ms => new Promise(r => setTimeout(r, window.FAST ? 0 : ms));
const sg = n => n < 0 ? `−${-n}` : `${n}`;             // proper minus sign
let run = 0;                                         // bumping this cancels older animations

class Board {
  constructor(svg, xr, yr, opt = {}) {
    this.svg = svg; this.xr = xr; this.yr = yr; this.opt = opt;
    const vb = svg.viewBox.baseVal, W = vb.width, H = vb.height;
    const m = opt.margin || { l: 34, r: 26, t: 22, b: 34 };
    this.U = Math.min((W - m.l - m.r) / (xr[1] - xr[0]), (H - m.t - m.b) / (yr[1] - yr[0]));
    this.x0 = m.l - xr[0] * this.U; this.y0 = m.t + yr[1] * this.U;
    if (opt.center) this.x0 += (W - m.l - m.r - this.U * (xr[1] - xr[0])) / 2;   // wide boards: centre the grid
    this.id = svg.id || (svg.id = "sv" + Math.random().toString(36).slice(2, 7));
    this.draw();
  }
  X(x) { return this.x0 + this.U * x }
  Y(y) { return this.y0 - this.U * y }
  el(tag, a, text) {
    const n = document.createElementNS(NS, tag);
    for (const k in a) n.setAttribute(k, a[k]);
    if (text != null) n.textContent = text;
    (this._into || this.svg).appendChild(n); return n;
  }
  draw() {
    const { xr, yr } = this, small = this.opt.small;
    this.svg.innerHTML = `<defs><marker id="ah-${this.id}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1 1L9 5L1 9" fill="none" stroke="${C.ink}" stroke-width="1.6" stroke-linecap="round"/></marker></defs>`;
    const every = this.U < 20 ? 2 : 1;
    for (let i = Math.ceil(xr[0]); i <= xr[1]; i++) this.el("path", { d: `M${this.X(i)} ${this.Y(yr[1])}V${this.Y(yr[0])}`, stroke: "#e6e3ec" });
    for (let j = Math.ceil(yr[0]); j <= yr[1]; j++) this.el("path", { d: `M${this.X(xr[0])} ${this.Y(j)}H${this.X(xr[1])}`, stroke: "#e6e3ec" });
    this._under = this.el("g", { class: "under" });   // shaded areas sit here: above the grid, below axes and lines
    this.el("path", { d: `M${this.X(xr[0])} ${this.Y(0)}H${this.X(xr[1]) + 8}`, stroke: C.ink, "stroke-width": 1.8, class: "axis", "marker-end": `url(#ah-${this.id})` });
    this.el("path", { d: `M${this.X(0)} ${this.Y(yr[0])}V${this.Y(yr[1]) - 8}`, stroke: C.ink, "stroke-width": 1.8, class: "axis", "marker-end": `url(#ah-${this.id})` });
    if (!small) {
      const fs = this.U < 24 ? 13 : 15;
      for (let i = Math.ceil(xr[0]); i <= xr[1] - .5; i++) if (i && i !== xr[0] && i % every === 0) this.el("text", { x: this.X(i), y: this.Y(0) + 18, "text-anchor": "middle", "font-size": fs, fill: C.muted, class: "tick" }, sg(i));
      for (let j = Math.ceil(yr[0]); j <= yr[1] - .5; j++) if (j && j !== yr[0] && !(j === -1 && xr[0] < 0) && j % every === 0) this.el("text", { x: this.X(0) - 8, y: this.Y(j) + 5, "text-anchor": "end", "font-size": fs, fill: C.muted, class: "tick" }, sg(j));
      // the origin's 0: below the corner, or level with the t-axis when the graph also goes below it (so it can't hit −1)
      if (xr[0] >= 0) this.el("text", { x: this.X(0) - 8, y: this.Y(0) + (yr[0] < 0 ? 5 : 18), "text-anchor": "end", "font-size": fs, fill: C.muted, class: "tick" }, 0);
    }
    // axis names: "x"/"y" by default; any other name, e.g. { xName: "t (s)", yName: "v (m s⁻¹)" } for kinematics
    const xn = this.opt.xName || "x", yn = this.opt.yName || "y";
    const letter = { "font-size": 20, "font-style": "italic", "font-family": "Georgia,serif" }, word = { "font-size": 16, "font-weight": 600 };
    if (!small) this.el("text", xn.length === 1
      ? { x: this.X(xr[1]) + 4, y: this.Y(0) + (yr[1] <= 0 ? 22 : -8), fill: C.ink, class: "axisname", ...letter }
      : { x: this.X(xr[1]) + 8, y: this.Y(0) + (yr[1] <= 0 ? 24 : -10), "text-anchor": "end", fill: C.ink, class: "axisname", ...word }, xn);
    if (!small) this.el("text", yn.length === 1
      ? { x: this.X(0) - 10, y: this.Y(yr[1]) + 6, "text-anchor": "end", fill: C.ink, class: "axisname", ...letter }
      : { x: this.X(0) + 10, y: this.Y(yr[1]) + 4, fill: C.ink, class: "axisname", ...word }, yn);
  }
  // hide any axis number that something else now covers
  tidy() {
    if (this._quiet) return;
    const hit = (b, x, y) => x > b.x && x < b.x + b.width && y > b.y && y < b.y + b.height;
    const labels = [...this.svg.querySelectorAll("text:not(.tick)")].map(t => t.getBBox());
    const strokes = [...this.svg.querySelectorAll("path.ink, circle.pt")];
    this.svg.querySelectorAll("text.tick").forEach(t => {
      const b = t.getBBox(), pad = { x: b.x - 2, y: b.y - 1, width: b.width + 4, height: b.height + 2 };
      let covered = labels.some(o => Math.min(o.x + o.width, pad.x + pad.width) > Math.max(o.x, pad.x) && Math.min(o.y + o.height, pad.y + pad.height) > Math.max(o.y, pad.y));
      if (!covered) for (const p of strokes) {
        if (p.tagName === "circle") { if (hit({ x: pad.x - 7, y: pad.y - 7, width: pad.width + 14, height: pad.height + 14 }, +p.getAttribute("cx"), +p.getAttribute("cy"))) { covered = true; break; } continue; }
        if (!p.getAttribute("d")) continue;                // an empty path has no length
        const L = p.getTotalLength();
        for (let k = 0; k <= 60 && !covered; k++) { const q = p.getPointAtLength(L * k / 60); covered = hit(pad, q.x, q.y); }
        if (covered) break;
      }
      t.style.visibility = covered ? "hidden" : "visible";
    });
  }
  path(d, color, ms = 600, w = 4.5, dash) {
    const p = this.el("path", { d, stroke: color, "stroke-width": w, fill: "none", "stroke-linecap": "round", "stroke-linejoin": "round", class: "ink" });
    if (dash) p.setAttribute("stroke-dasharray", dash);
    if (this.instant) { this.tidy(); return Promise.resolve(); }   // live redraw while dragging: no animation
    if (dash) { p.animate([{ opacity: 0 }, { opacity: 1 }], { duration: D(ms), fill: "forwards" }); this.tidy(); return wait(ms); }
    const L = p.getTotalLength() || 1;
    p.style.strokeDasharray = L; p.style.strokeDashoffset = L;
    p.animate([{ strokeDashoffset: L }, { strokeDashoffset: 0 }], { duration: D(ms), easing: "ease-in-out", fill: "forwards" });
    return wait(ms).then(() => this.tidy());
  }
  seg(x1, y1, x2, y2, color, ms = 600, w = 4.5, dash) {
    return this.path(`M${this.X(x1)} ${this.Y(y1)}L${this.X(x2)} ${this.Y(y2)}`, color, ms, w, dash);
  }
  // y = f(x) across the board, broken where it leaves the grid
  fn(f, color, ms = 900, w = 3.5, dash, from = this.xr[0], to = this.xr[1]) {
    let d = "", pen = false;
    for (let i = 0; i <= 240; i++) {
      const x = from + (to - from) * i / 240, y = f(x);
      if (!Number.isFinite(y) || y < this.yr[0] || y > this.yr[1]) { pen = false; continue; }   // NaN/∞ (e.g. √ of a negative) breaks the line
      d += `${pen ? "L" : "M"}${this.X(x).toFixed(1)} ${this.Y(y).toFixed(1)}`; pen = true;
    }
    return this.path(d, color, ms, w, dash);
  }
  ring(cx, cy, r, color, ms = 900) {
    const R = r * this.U, X = this.X(cx), Y = this.Y(cy);
    return this.path(`M${X + R} ${Y}A${R} ${R} 0 1 0 ${X - R} ${Y}A${R} ${R} 0 1 0 ${X + R} ${Y}`, color, ms, 2, "7 6");
  }
  dot(x, y, label, dx = 10, dy = -12, color = C.plum, anchor = "start") {
    const c = this.el("circle", { cx: this.X(x), cy: this.Y(y), r: 6.5, fill: color, class: "pt" });
    if (!this.instant) c.animate([{ r: 0 }, { r: 6.5 }], { duration: D(250) });
    if (label) this.text(x, y, label, color, 20, anchor, dx, dy);
    else this.tidy();
    return c;
  }
  text(x, y, s, color, size = 19, anchor = "start", dx = 0, dy = 0, weight = 700) {
    const t = this.el("text", { x: this.X(x) + dx, y: this.Y(y) + dy, fill: color, "font-size": size, "text-anchor": anchor, "font-weight": weight }, s);
    if (!this.instant) t.animate([{ opacity: 0 }, { opacity: 1 }], { duration: D(350), fill: "forwards" });
    this.tidy();
    return t;
  }
  corner(x, y, sx, sy) {           // right-angle mark; sx/sy = direction of the two legs (±1)
    const k = 12, X = this.X(x), Y = this.Y(y);
    this.el("path", { d: `M${X + sx * k} ${Y}V${Y - sy * k}H${X}`, stroke: C.ink, "stroke-width": 1.5, fill: "none" });
  }
  // right-angle mark at (x, y) between two directions given in grid units
  square(x, y, u, v, color = C.ink) {
    const n = w => { const L = Math.hypot(...w); return [w[0] / L, -w[1] / L]; };
    const [ux, uy] = n(u), [vx, vy] = n(v), k = 13, X = this.X(x), Y = this.Y(y);
    this.el("path", { d: `M${X + ux * k} ${Y + uy * k}L${X + (ux + vx) * k} ${Y + (uy + vy) * k}L${X + vx * k} ${Y + vy * k}`, stroke: color, "stroke-width": 1.6, fill: "none" });
  }
  /* ---------- explore: draggable points and live redraws ---------- */
  // a group that is wiped and redrawn (without animation) every time something moves
  layer() { return this.el("g", { class: "live" }); }
  redraw(g, fn) {
    g.replaceChildren(); const into = this._into; this._into = g; this.instant = true; this._quiet = true;
    try { fn(this); } finally { this.instant = false; this._into = into; this._quiet = false; }
    clearTimeout(this._tidyLater); this._tidyLater = setTimeout(() => this.tidy(), 120);   // tidy once, after moving stops
  }
  // a shaded region (e.g. the area under a v-t graph). pts: [[x, y], ...] in grid units
  fillPoly(pts, color = C.along, opacity = 0.18, ms = 500) {
    const d = pts.map(([x, y], i) => `${i ? "L" : "M"}${this.X(x).toFixed(1)} ${this.Y(y).toFixed(1)}`).join("") + "Z";
    const p = document.createElementNS(NS, "path");
    p.setAttribute("d", d); p.setAttribute("fill", color); p.setAttribute("fill-opacity", opacity); p.setAttribute("class", "area");
    (this._into || this._under).appendChild(p);
    if (!this.instant) p.animate([{ opacity: 0 }, { opacity: 1 }], { duration: D(ms), fill: "forwards" });
    return this.instant ? Promise.resolve() : wait(ms);
  }
  // shade between y = f(x) and the x-axis from x1 to x2 (area above the axis and below it both shaded)
  fillUnder(f, x1, x2, color = C.along, opacity = 0.18, ms = 500) {
    const pts = [[x1, 0]];
    for (let i = 0; i <= 120; i++) { const x = x1 + (x2 - x1) * i / 120; pts.push([x, f(x)]); }
    pts.push([x2, 0]);
    return this.fillPoly(pts, color, opacity, ms);
  }
  // a solid circle (ring() draws a dashed one)
  circle(cx, cy, r, color = C.plum, ms = 900, w = 3.5) {
    const R = r * this.U, X = this.X(cx), Y = this.Y(cy);
    return this.path(`M${X + R} ${Y}A${R} ${R} 0 1 0 ${X - R} ${Y}A${R} ${R} 0 1 0 ${X + R} ${Y}`, color, ms, w);
  }
  // screen position of a pointer event -> grid coordinates
  toWorld(ev) {
    const pt = this.svg.createSVGPoint(); pt.x = ev.clientX; pt.y = ev.clientY;
    const q = pt.matrixTransform(this.svg.getScreenCTM().inverse());
    return [(q.x - this.x0) / this.U, (this.y0 - q.y) / this.U];
  }
  // a point the student can drag (mouse, touch or arrow keys). limit(x, y) can keep it on a line or curve.
  drag(x, y, { snap = 1, limit, color = C.mid, onMove } = {}) {
    const c = this.el("circle", { cx: this.X(x), cy: this.Y(y), r: 10, fill: color, class: "pt drag", tabindex: 0 });
    const halo = this.el("circle", { cx: this.X(x), cy: this.Y(y), r: 18, fill: color, opacity: 0.15, class: "drag-halo" });
    c.before(halo);
    const h = { x, y };
    const set = (wx, wy) => {
      if (limit) [wx, wy] = limit(wx, wy);
      if (snap) { wx = Math.round(wx / snap) * snap; wy = Math.round(wy / snap) * snap; }
      wx = Math.max(this.xr[0], Math.min(this.xr[1], wx)); wy = Math.max(this.yr[0], Math.min(this.yr[1], wy));
      if (limit) [wx, wy] = limit(wx, wy);
      if (Math.abs(wx - h.x) < 1e-9 && Math.abs(wy - h.y) < 1e-9) return;
      h.x = wx; h.y = wy;
      for (const n of [c, halo]) { n.setAttribute("cx", this.X(wx)); n.setAttribute("cy", this.Y(wy)); }
      onMove && onMove(wx, wy);
    };
    c.addEventListener("pointerdown", e => {
      e.preventDefault(); c.setPointerCapture(e.pointerId); c.classList.add("held");
      const mv = ev => set(...this.toWorld(ev));
      c.addEventListener("pointermove", mv);
      c.addEventListener("pointerup", () => { c.removeEventListener("pointermove", mv); c.classList.remove("held"); }, { once: true });
    });
    c.addEventListener("keydown", e => {
      const k = { ArrowLeft: [-1, 0], ArrowRight: [1, 0], ArrowUp: [0, 1], ArrowDown: [0, -1] }[e.key];
      if (!k) return;
      e.preventDefault(); e.stopPropagation();
      const st = snap || 0.5, x0 = h.x, y0 = h.y;
      // on a limited path one step can snap straight back, so keep stepping until the point really moves
      for (let i = 1; i <= 12 && h.x === x0 && h.y === y0; i++) set(x0 + k[0] * st * i, y0 + k[1] * st * i);
    });
    h.set = set; h.el = c;
    return h;
  }
  // draw into a group that can then be turned about a grid point
  group() { const g = this.el("g", {}); this._into = g; return g; }
  endGroup() { this._into = null; }
  turn(g, x, y, deg, ms = 1200) {
    g.style.transformBox = "view-box"; g.style.transformOrigin = `${this.X(x)}px ${this.Y(y)}px`;
    const from = g._deg || 0; g._deg = from + deg;    // a second turn carries on from the first
    g.animate([{ transform: `rotate(${-from}deg)` }, { transform: `rotate(${-g._deg}deg)` }], { duration: D(ms), easing: "ease-in-out", fill: "forwards" });
    return wait(ms);
  }
  async walk(pts, perUnit = 380, keep) {
    const w = this.el("circle", { cx: this.X(pts[0][0]), cy: this.Y(pts[0][1]), r: 7.5, fill: C.ink });
    for (let k = 1; k < pts.length; k++) {
      const [ax, ay] = pts[k - 1], [bx, by] = pts[k];
      const ms = Math.max(300, perUnit * Math.hypot(bx - ax, by - ay));
      w.animate([{ cx: this.X(ax), cy: this.Y(ay) }, { cx: this.X(bx), cy: this.Y(by) }], { duration: D(ms), easing: "ease-in-out", fill: "forwards" });
      await wait(ms);
    }
    if (keep) return w;
    w.remove();
  }
  async go(x1, y1, x2, y2, color, perUnit = 380) {
    const ms = Math.max(300, perUnit * Math.hypot(x2 - x1, y2 - y1));
    this.walk([[x1, y1], [x2, y2]], perUnit);
    await this.seg(x1, y1, x2, y2, color, ms);
  }
}

/* A board with its own scale on each axis, for graphs against time (a v–t graph with t to 20 and v to 60 is not
   squashed) and for number-line tracks. Same drawing tools as Board. Built from the M1 Kinematics decks' TB class.
   Options (all optional):
     xName / yName   axis names, default "t (s)" and "v (m s⁻¹)"
     tx / ty         step between axis numbers (default 1); gx / gy step between grid lines (default tx / ty)
     fs              axis-number size (default 14);  margin  { l, r, t, b }
     small           an icon: axes only, no numbers or names
     track           a number line only: a teal line with ticks every gx and numbers every tx (a particle's path)
   e.g. new TimeBoard(svg, [0, 20], [-10, 60], { tx: 5, ty: 10 })                                             */
class TimeBoard extends Board {
  X(x) { return this.x0 + this.Ux * x }
  Y(y) { return this.y0 - this.Uy * y }
  draw() {
    const o = this.opt, { xr, yr } = this, vb = this.svg.viewBox.baseVal, W = vb.width, H = vb.height;
    const m = o.margin || (o.small ? { l: 12, r: 14, t: 12, b: 12 } : o.track ? { l: 18, r: 22, t: 8, b: 26 } : { l: 46, r: 24, t: 30, b: 30 });
    this.Ux = (W - m.l - m.r) / (xr[1] - xr[0]); this.Uy = (H - m.t - m.b) / (yr[1] - yr[0]);
    this.U = Math.min(this.Ux, this.Uy);
    this.x0 = m.l - xr[0] * this.Ux; this.y0 = m.t + yr[1] * this.Uy;
    this.svg.innerHTML = `<defs><marker id="ah-${this.id}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1 1L9 5L1 9" fill="none" stroke="${C.ink}" stroke-width="1.6" stroke-linecap="round"/></marker></defs>`;
    const thin = (r, s) => { while (r / s > 24) s *= 2; return s; };   // a wide range with step 1 would draw a wall of lines
    const fs = o.fs || 14, tx = o.tx || 1, ty = o.ty || 1, gx = o.gx || thin(xr[1] - xr[0], tx), gy = o.gy || thin(yr[1] - yr[0], ty);
    // the axes sit at 0, or at the edge of the range when 0 is not in it
    const ax = xr[0] > 0 ? xr[0] : xr[1] < 0 ? xr[1] : 0, ay = yr[0] > 0 ? yr[0] : yr[1] < 0 ? yr[1] : 0, orig = ax === 0 && ay === 0;
    const steps = (a, b, s) => { const out = []; for (let k = Math.ceil(a / s - 1e-9); k * s <= b + 1e-9; k++) out.push(+(k * s).toFixed(6)); return out; };
    if (o.track) {
      this._under = this.el("g", { class: "under" });
      this.el("path", { d: `M${this.X(xr[0])} ${this.Y(ay)}H${this.X(xr[1])}`, stroke: C.along, "stroke-width": 3, class: "axis" });
      for (const i of steps(xr[0], xr[1], gx)) this.el("path", { d: `M${this.X(i)} ${this.Y(ay) - 5}V${this.Y(ay) + 5}`, stroke: C.along, "stroke-width": 1.5 });
      if (!o.small) for (const i of steps(xr[0], xr[1], tx)) this.el("text", { x: this.X(i), y: this.Y(ay) + 20, "text-anchor": "middle", "font-size": fs, fill: C.muted, class: "tick" }, sg(i));
      return;
    }
    for (const i of steps(xr[0], xr[1], gx)) this.el("path", { d: `M${this.X(i)} ${this.Y(yr[1])}V${this.Y(yr[0])}`, stroke: "#e6e3ec" });
    for (const j of steps(yr[0], yr[1], gy)) this.el("path", { d: `M${this.X(xr[0])} ${this.Y(j)}H${this.X(xr[1])}`, stroke: "#e6e3ec" });
    this._under = this.el("g", { class: "under" });
    this.el("path", { d: `M${this.X(xr[0])} ${this.Y(ay)}H${this.X(xr[1]) + 8}`, stroke: C.ink, "stroke-width": 1.8, class: "axis", "marker-end": `url(#ah-${this.id})` });
    this.el("path", { d: `M${this.X(ax)} ${this.Y(yr[0])}V${this.Y(yr[1]) - 8}`, stroke: C.ink, "stroke-width": 1.8, class: "axis", "marker-end": `url(#ah-${this.id})` });
    if (o.small) return;
    for (const i of steps(xr[0], xr[1] - tx / 2, tx)) if (i || !orig) this.el("text", { x: this.X(i), y: this.Y(ay) + 18, "text-anchor": "middle", "font-size": fs, fill: C.muted, class: "tick" }, sg(i));
    for (const j of steps(yr[0], yr[1] - ty / 2, ty)) if ((j || !orig) && !(!orig && j === ay && steps(xr[0], xr[1] - tx / 2, tx).includes(ax))) this.el("text", { x: this.X(ax) - 7, y: this.Y(j) + 5, "text-anchor": "end", "font-size": fs, fill: C.muted, class: "tick" }, sg(j));
    if (orig) this.el("text", { x: this.X(0) - 7, y: this.Y(0) + (yr[0] < 0 ? 5 : 18), "text-anchor": "end", "font-size": fs, fill: C.muted, class: "tick" }, 0);
    const word = { "font-size": 15, "font-weight": 600, fill: C.ink, class: "axisname" };
    this.el("text", { x: this.X(xr[1]) + 8, y: this.Y(ay) - 9, "text-anchor": "end", ...word }, o.xName || "t (s)");
    this.el("text", { x: this.X(ax) + 9, y: this.Y(yr[1]) + 4, ...word }, o.yName || "v (m s⁻¹)");
  }
  toWorld(ev) {
    const pt = this.svg.createSVGPoint(); pt.x = ev.clientX; pt.y = ev.clientY;
    const q = pt.matrixTransform(this.svg.getScreenCTM().inverse());
    return [(q.x - this.x0) / this.Ux, (this.y0 - q.y) / this.Uy];
  }
}

/* along-then-up between two points, with labels and the subtraction */
const fmt = n => n < 0 ? `(${sg(n)})` : `${n}`;
async function alongUp(b, p, q, ok = () => true, show = true) {
  const dx = q[0] - p[0], dy = q[1] - p[1];
  await b.go(p[0], p[1], q[0], p[1], C.along); if (!ok()) return;
  const lx = (p[0] + q[0]) / 2, below = dy >= 0;
  b.text(lx, p[1], `${Math.abs(dx)} ${dx >= 0 ? "along" : "left"}`, C.along, 19, "middle", 0, below ? 24 : -14);
  if (show) b.text(lx, p[1], `${sg(q[0])} − ${fmt(p[0])} = ${sg(dx)}`, C.ink, 17, "middle", 0, below ? 50 : -40, 600);
  await wait(350); if (!ok()) return;
  await b.go(q[0], p[1], q[0], q[1], C.up); if (!ok()) return;
  const my = (p[1] + q[1]) / 2, rightRoom = b.X(q[0]) + 100 < b.svg.viewBox.baseVal.width;
  const anchor = rightRoom ? "start" : "end", off = rightRoom ? 10 : -10;
  b.text(q[0], my, `${Math.abs(dy)} ${dy >= 0 ? "up" : "down"}`, C.up, 19, anchor, off, 0);
  if (show) b.text(q[0], my, `${sg(q[1])} − ${fmt(p[1])} = ${sg(dy)}`, C.ink, 17, anchor, off, 26, 600);
}
const B = (root, xr, yr, i = 0) => (root._b = new Board(root.querySelectorAll("svg")[i], xr, yr));

/* answer parsing */
const num = s => { s = String(s).trim().replace(/−/g, "-"); if (!s) return NaN; if (s.includes("/")) { const [a, b] = s.split("/"); return +a / +b; } return +s; };
const eq = (a, b) => Math.abs(a - b) < 0.01;

/* readouts: exact fractions and surds for live numbers */
const gcd = (a, b) => b ? gcd(b, a % b) : Math.abs(a);
function frac(n, d) {
  if (d === 0) return "undefined";
  if (d < 0) { n = -n; d = -d; }
  const g = gcd(Math.round(n), Math.round(d)) || 1; n = Math.round(n) / g; d = Math.round(d) / g;
  return d === 1 ? sg(n) : `${sg(n)}/${d}`;
}
function surd(n) {                      // √n in simplest form, n a whole number
  if (n === 0) return "0";
  let out = 1, inside = n;
  for (let f = Math.floor(Math.sqrt(n)); f > 1; f--) if (inside % (f * f) === 0) { out *= f; inside /= f * f; break; }
  return inside === 1 ? `${out}` : `${out === 1 ? "" : out}√${inside}`;
}

/* filled in by lesson scripts, used by interact.js */
window.predicts = {}; window.taps = {};
