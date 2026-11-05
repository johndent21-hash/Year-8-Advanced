// Helpers for the Year 8 mixed revision booklet: maths markup, diagrams, layout blocks
// and an answer register, so every answer is stored next to the question that asks it.

// ---------------------------------------------------------------- numbers
const gcd = (a, b) => (b ? gcd(b, a % b) : Math.abs(a));
class Fr {
  constructor(n, d = 1) {
    if (d < 0) { n = -n; d = -d; }
    const g = gcd(n, d) || 1;
    this.n = n / g; this.d = d / g;
  }
  add(o) { return new Fr(this.n * o.d + o.n * this.d, this.d * o.d); }
  sub(o) { return new Fr(this.n * o.d - o.n * this.d, this.d * o.d); }
  mul(o) { return new Fr(this.n * o.n, this.d * o.d); }
  div(o) { return new Fr(this.n * o.d, this.d * o.n); }
  val() { return this.n / this.d; }
}
const fr = (n, d = 1) => new Fr(n, d);
const mx = (w, n, d) => new Fr(w * d + n, d);

// Plain text of a fraction as a mixed numeral: '3 11/12', '5/6', '2'
const fPlain = (f) => {
  const neg = f.n < 0, n = Math.abs(f.n), d = f.d;
  if (d === 1) return (neg ? '−' : '') + n;
  const w = Math.floor(n / d), r = n % d;
  return (neg ? '−' : '') + (w ? `${w} ${r}/${d}` : `${r}/${d}`);
};
// Plain text of an improper fraction (no mixed numeral)
const fImp = (f) => (f.d === 1 ? `${f.n}` : `${f.n}/${f.d}`).replace('-', '−');

// Decimal with no floating-point noise and no trailing zeros
const dec = (x, dp = 6) => {
  let s = (+x).toFixed(dp);
  if (s.includes('.')) s = s.replace(/\.?0+$/, '');
  return s.replace('-', '−');
};
// Round to a number of decimal places, keeping the zeros (e.g. 12.40)
const rnd = (x, dp) => (Math.round(x * 10 ** dp + 1e-9) / 10 ** dp).toFixed(dp);
const isSq = (n) => Number.isInteger(Math.sqrt(n));

// Long division to find a recurring decimal: {int, pre, rep}
const recurring = (n, d) => {
  const int = Math.floor(n / d); let r = n % d; const seen = new Map(); let digits = '';
  while (r !== 0 && !seen.has(r)) { seen.set(r, digits.length); r *= 10; digits += Math.floor(r / d); r %= d; }
  if (r === 0) return { int, pre: digits, rep: '' };
  const k = seen.get(r);
  return { int, pre: digits.slice(0, k), rep: digits.slice(k) };
};

// ---------------------------------------------------------------- maths markup
// M('3x^2 - 4y') → italic pronumerals, true minus, × for *, superscripts. Skips HTML tags.
const M = (s) => String(s).split(/(<[^>]+>)/).map((seg) => (seg.startsWith('<') ? seg : seg
  .replace(/[a-zA-Z]/g, (c) => `<i class="v">${c}</i>`)
  .replace(/\^(\d)/g, '<sup>$1</sup>')
  .replace(/-/g, '−')
  .replace(/\*/g, '×')
)).join('');
// stacked fraction; w = whole number part for a mixed numeral
const F = (n, d, w = '') => `${w}<span class="fr"><span class="nu">${n}</span><span class="de">${d}</span></span>`;
const FH = (f) => {
  if (f.d === 1) return dec(f.n);
  const neg = f.n < 0, n = Math.abs(f.n), w = Math.floor(n / f.d), r = n % f.d;
  return (neg ? '−' : '') + (w ? F(r, f.d, w) : F(r, f.d));
};
const FI = (f) => (f.d === 1 ? dec(f.n) : (f.n < 0 ? '−' : '') + F(Math.abs(f.n), f.d));
const SQ = (r) => `<span class="sq"><span class="sqs">√</span><span class="rad">${r}</span></span>`;
const REC = ({ int, pre, rep }) => {
  if (!rep) return `${int}.${pre}`;
  const r = rep.length === 1 ? `<span class="rec">${rep}</span>`
    : `<span class="rec">${rep[0]}</span>${rep.slice(1, -1)}<span class="rec">${rep.slice(-1)}</span>`;
  return `${int}.${pre}${r}`;
};
const RECP = ({ int, pre, rep }) => (rep ? `${int}.${pre}(${rep})` : `${int}.${pre}`);
const B = (w = 12) => `<span class="bl" style="min-width:${w}mm"></span>`;          // blank to fill in
const H = (s) => `<span class="hint">${s}</span>`;                                  // given step (grey)
const money = (x) => '$' + (+x).toFixed(2);

// ---------------------------------------------------------------- answer register
const ANS = [];
let group = null;
const setGroup = (g) => { group = g; };
const reg = (key, label, h, p) => { ANS.push({ group, key, label, h, p }); };

// ---------------------------------------------------------------- layout blocks
const chip = (cls, t) => `<span class="chip ${cls}">${t}</span>`;
const LEVEL = {
  easy: chip('lv', 'EASY · support &amp; core'),
  easyc: chip('lv', 'EASY · core'),
  med: chip('lv', 'MEDIUM · core'),
  hard: chip('lv', 'CHALLENGING · core, exam style'),
  ext: chip('lv ext', 'EXTENSION · Stage 5 Path'),
};
const sec = (code, title, level, exam = '') => `<div class="sec"><span class="code">${code}</span><span class="st">${title}</span>${LEVEL[level] || ''}${exam ? chip('ex', 'EXAM ' + exam) : ''}</div>`;
const learn = (html, style = '') => `<div class="learn" style="${style}"><div class="tag">LEARN IT</div>${html}</div>`;
const we = (html, title = 'WORKED EXAMPLE', style = '') => `<div class="we" style="${style}"><div class="tag">${title}</div>${html}</div>`;
const you = (n, text, html, style = '') => `<div class="you" style="${style}"><div class="tag">YOUR TURN ${n}</div>${text ? `<div class="yt">${text}</div>` : ''}${html}</div>`;
const grid = (cols, items, style = '') => `<div class="g" style="grid-template-columns:${typeof cols === 'number' ? `repeat(${cols},1fr)` : cols};${style}">${items.join('')}</div>`;
const row = (cols, items, style = '') => `<div class="row" style="grid-template-columns:${cols};${style}">${items.map((x) => `<div>${x}</div>`).join('')}</div>`;

// A question item. ans = [html, plain]. o: work (mm box), line (answer line prefix), unit, fig, sc (scaffold html)
const Q = (key, label, q, ans, o = {}) => {
  reg(key, label, ans[0], ans[1]);
  return `<div class="it${o.cls ? ' ' + o.cls : ''}">`
    + `<div class="q"><b class="lb">${label}</b><span>${q}${o.inl !== undefined || o.inlpos ? ` ${o.inl || ''}${B(o.lw || 12)}${o.unit ? ' ' + o.unit : ''}` : ''}</span>${o.marks ? `<span class="mk">${o.marks}</span>` : ''}</div>`
    + (o.fig ? `<div class="fig">${o.fig}</div>` : '')
    + (o.sc ? `<div class="sc">${o.sc}</div>` : '')
    + (o.work ? `<div class="wk" style="height:${o.work}mm"></div>` : '')
    + (o.line !== undefined ? `<div class="al">${o.line}${B(o.lw || 16)}${o.unit ? ' ' + o.unit : ''}</div>` : '')
    + '</div>';
};

// ---------------------------------------------------------------- diagrams (all drawn to scale)
const r2 = (n) => +n.toFixed(2);
const FS = 3.1; // label font size in mm
const tw = (s) => String(s).replace(/^\$/, '').replace(/_/g, '').length * FS * 0.56; // estimated text width
const label = (x, y, s, o = {}) => {
  const it = String(s).startsWith('$');
  const t = (it ? s.slice(1) : String(s)).replace(/_([a-z])_/g, '<tspan class="svi">$1</tspan>');
  return `<text x="${r2(x)}" y="${r2(y)}" font-size="${o.size || FS}" text-anchor="middle" dominant-baseline="central"`
    + `${it ? ' class="sv"' : ''}${o.fill ? ` fill="${o.fill}"` : ''}${o.weight ? ` font-weight="${o.weight}"` : ''}>${t}</text>`;
};
const svgWrap = (inner, box, extra = '') => {
  const [x0, y0, x1, y1] = box; const w = x1 - x0, h = y1 - y0;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${r2(x0)} ${r2(y0)} ${r2(w)} ${r2(h)}" width="${r2(w)}mm" height="${r2(h)}mm" ${extra}>${inner}</svg>`;
};
// bounding-box tracker
const bb = () => { const b = [Infinity, Infinity, -Infinity, -Infinity]; const add = (x, y) => { b[0] = Math.min(b[0], x); b[1] = Math.min(b[1], y); b[2] = Math.max(b[2], x); b[3] = Math.max(b[3], y); }; return { b, add }; };

// Right-angled triangle. Legs a (along x) and b (along y) meet at the right angle.
// la, lb, lc label leg a, leg b and the hypotenuse ('$x' = italic pronumeral). vl = [R, A, B] vertex names.
const tri = ({ a, b, la = '', lb = '', lc = '', rot = 0, flip = false, w = 34, h = 24, vl = null, hl = false }) => {
  let P = [[0, 0], [a, 0], [0, b]];
  if (flip) P = P.map(([x, y]) => [-x, y]);
  const t = (rot * Math.PI) / 180;
  P = P.map(([x, y]) => [x * Math.cos(t) - y * Math.sin(t), -(x * Math.sin(t) + y * Math.cos(t))]);
  const xs = P.map((p) => p[0]), ys = P.map((p) => p[1]);
  const s = Math.min(w / (Math.max(...xs) - Math.min(...xs)), h / (Math.max(...ys) - Math.min(...ys)));
  P = P.map(([x, y]) => [(x - Math.min(...xs)) * s, (y - Math.min(...ys)) * s]);
  const [R, A, Bv] = P;
  const C = [(R[0] + A[0] + Bv[0]) / 3, (R[1] + A[1] + Bv[1]) / 3];
  const box = bb(); P.forEach(([x, y]) => box.add(x, y));
  let out = `<polygon points="${P.map((p) => p.map(r2).join(',')).join(' ')}" fill="#fff" stroke="#222" stroke-width="0.45" stroke-linejoin="round"/>`;
  if (hl) out += `<line x1="${r2(A[0])}" y1="${r2(A[1])}" x2="${r2(Bv[0])}" y2="${r2(Bv[1])}" stroke="${hl}" stroke-width="1.1" stroke-linecap="round"/>`;
  const unit = (p, q) => { const dx = q[0] - p[0], dy = q[1] - p[1], L = Math.hypot(dx, dy); return [dx / L, dy / L]; };
  const u = unit(R, A), v = unit(R, Bv), k = 2.2;
  out += `<polyline points="${r2(R[0] + k * u[0])},${r2(R[1] + k * u[1])} ${r2(R[0] + k * u[0] + k * v[0])},${r2(R[1] + k * u[1] + k * v[1])} ${r2(R[0] + k * v[0])},${r2(R[1] + k * v[1])}" fill="none" stroke="#222" stroke-width="0.35"/>`;
  const side = (p, q, s) => {
    if (!s) return;
    const m = [(p[0] + q[0]) / 2, (p[1] + q[1]) / 2];
    let n = [-(q[1] - p[1]), q[0] - p[0]]; const L = Math.hypot(...n); n = [n[0] / L, n[1] / L];
    if ((m[0] - C[0]) * n[0] + (m[1] - C[1]) * n[1] < 0) n = [-n[0], -n[1]];
    const W = tw(s), off = 1.3 + Math.abs(n[0]) * W / 2 + Math.abs(n[1]) * FS / 2;
    const x = m[0] + n[0] * off, y = m[1] + n[1] * off;
    box.add(x - W / 2, y - FS / 2); box.add(x + W / 2, y + FS / 2);
    out += label(x, y, s);
  };
  side(R, A, la); side(R, Bv, lb); side(A, Bv, lc);
  if (vl) P.forEach((p, i) => {
    const d = unit(C, p); const x = p[0] + d[0] * 2.8, y = p[1] + d[1] * 2.8;
    box.add(x - 2, y - 2); box.add(x + 2, y + 2);
    out += label(x, y, vl[i], { weight: 600 });
  });
  const [x0, y0, x1, y1] = box.b;
  return svgWrap(out, [x0 - 0.6, y0 - 0.6, x1 + 0.6, y1 + 0.6]);
};

// 3-4-5 triangle with a square drawn on each side (unit grid), areas 9 + 16 = 25
const squaresFig = (u = 3.1) => {
  const T = ([x, y]) => [r2(x * u), r2(-y * u)];
  const poly = (pts, fill) => `<polygon points="${pts.map((p) => T(p).join(',')).join(' ')}" fill="${fill}" stroke="#222" stroke-width="0.35"/>`;
  const lines = (o, e1, e2, n) => { let s = ''; for (let i = 1; i < n; i++) { const a = [o[0] + (e1[0] * i) / n, o[1] + (e1[1] * i) / n], b = [a[0] + e2[0], a[1] + e2[1]]; const c = [o[0] + (e2[0] * i) / n, o[1] + (e2[1] * i) / n], d = [c[0] + e1[0], c[1] + e1[1]]; s += `<line x1="${T(a)[0]}" y1="${T(a)[1]}" x2="${T(b)[0]}" y2="${T(b)[1]}"/><line x1="${T(c)[0]}" y1="${T(c)[1]}" x2="${T(d)[0]}" y2="${T(d)[1]}"/>`; } return `<g stroke="#555" stroke-width="0.15">${s}</g>`; };
  let s = '';
  s += poly([[0, 0], [4, 0], [4, -4], [0, -4]], '#fde7c7') + lines([0, 0], [4, 0], [0, -4], 4);
  s += poly([[0, 0], [0, 3], [-3, 3], [-3, 0]], '#d7ecf7') + lines([0, 0], [0, 3], [-3, 0], 3);
  s += poly([[4, 0], [0, 3], [3, 7], [7, 4]], '#e3dcf5') + lines([4, 0], [-4, 3], [3, 4], 5);
  s += poly([[0, 0], [4, 0], [0, 3]], '#fff');
  s += `<polyline points="${T([0.55, 0]).join(',')} ${T([0.55, 0.55]).join(',')} ${T([0, 0.55]).join(',')}" fill="none" stroke="#222" stroke-width="0.3"/>`;
  const L = (p, t, o) => { const [x, y] = T(p); return label(x, y, t, o); };
  s += L([2, -2], '16', { weight: 700, size: 3.6 }) + L([-1.5, 1.5], '9', { weight: 700, size: 3.6 }) + L([3.5, 3.5], '25', { weight: 700, size: 3.6 });
  return svgWrap(s, [-3.3 * u, -7.3 * u, 7.3 * u, 4.3 * u]);
};

// Rectangle with a diagonal (to scale)
const rectDiag = ({ L, W, lL, lW, lD, w = 38 }) => {
  const s = w / L, x1 = L * s, y1 = W * s;
  let o = `<rect x="0" y="0" width="${r2(x1)}" height="${r2(y1)}" fill="#f4f8ec" stroke="#222" stroke-width="0.45"/>`;
  o += `<line x1="0" y1="${r2(y1)}" x2="${r2(x1)}" y2="0" stroke="#222" stroke-width="0.45" stroke-dasharray="1.4 0.9"/>`;
  o += label(x1 / 2, y1 + 2.6, lL) + label(x1 + tw(lW) / 2 + 1.4, y1 / 2, lW) + label(x1 / 2 - 2.6, y1 / 2 - 2.2, lD);
  return svgWrap(o, [-1, -1, x1 + tw(lW) + 2.5, y1 + 4.6]);
};

// Isosceles triangle with its perpendicular height (to scale)
const isoFig = ({ base, side, s = 2.2 }) => {
  const hgt = Math.sqrt(side * side - (base / 2) ** 2);
  const A = [0, hgt * s], Bp = [base * s, hgt * s], Cp = [(base * s) / 2, 0], Fp = [(base * s) / 2, hgt * s];
  let o = `<polygon points="${[A, Bp, Cp].map((p) => p.map(r2).join(',')).join(' ')}" fill="#fff" stroke="#222" stroke-width="0.45"/>`;
  o += `<line x1="${r2(Cp[0])}" y1="0" x2="${r2(Fp[0])}" y2="${r2(Fp[1])}" stroke="#222" stroke-width="0.4" stroke-dasharray="1.2 0.8"/>`;
  o += `<polyline points="${r2(Fp[0] + 2)},${r2(Fp[1])} ${r2(Fp[0] + 2)},${r2(Fp[1] - 2)} ${r2(Fp[0])},${r2(Fp[1] - 2)}" fill="none" stroke="#222" stroke-width="0.3"/>`;
  o += label(Fp[0], Fp[1] + 2.6, `${base} cm`) + label(A[0] + (Cp[0] - A[0]) / 2 - 6, hgt * s / 2, `${side} cm`) + label(Cp[0] + (Bp[0] - Cp[0]) / 2 + 6, hgt * s / 2, `${side} cm`) + label(Fp[0] - 2.2, hgt * s / 2 + 2, '$h');
  return svgWrap(o, [-9, -1, base * s + 9, hgt * s + 4.6]);
};

// Fraction bar: n equal parts, k shaded
const bar = ({ n, k, w = 46, h = 6, col = '#f6b26b', lab = '' }) => {
  let o = '';
  for (let i = 0; i < n; i++) o += `<rect x="${r2((i * w) / n)}" y="0" width="${r2(w / n)}" height="${h}" fill="${i < k ? col : '#fff'}" stroke="#333" stroke-width="0.3"/>`;
  if (lab) o += `<text x="${w + 2}" y="${h / 2}" font-size="3.2" dominant-baseline="central">${lab}</text>`;
  return svgWrap(o, [-0.3, -0.3, w + (lab ? 10 : 0.6), h + 0.6]);
};

// Sector (pie) graph with percentage labels; drawn accurately
const pie = ({ data, r = 15 }) => {
  const cols = ['#9fc5e8', '#f9cb9c', '#b6d7a8', '#d5a6bd', '#ffe599', '#cfe2f3'];
  let a0 = -90, o = '', leg = '';
  data.forEach((d, i) => {
    const a1 = a0 + (d.p * 360) / 100, la = (a1 - a0) > 180 ? 1 : 0;
    const p0 = [r * Math.cos((a0 * Math.PI) / 180), r * Math.sin((a0 * Math.PI) / 180)];
    const p1 = [r * Math.cos((a1 * Math.PI) / 180), r * Math.sin((a1 * Math.PI) / 180)];
    o += `<path d="M0,0 L${r2(p0[0])},${r2(p0[1])} A${r},${r} 0 ${la} 1 ${r2(p1[0])},${r2(p1[1])} Z" fill="${cols[i]}" stroke="#333" stroke-width="0.3"/>`;
    const m = ((a0 + a1) / 2) * Math.PI / 180, rr = d.p < 8 ? r + 3.4 : r * 0.62;
    o += label(rr * Math.cos(m), rr * Math.sin(m), `${d.p}%`, { size: 2.8, weight: 600 });
    leg += `<rect x="${r + 7}" y="${-r + 1 + i * 5.2}" width="3.4" height="3.4" fill="${cols[i]}" stroke="#333" stroke-width="0.25"/><text x="${r + 11.6}" y="${-r + 2.7 + i * 5.2}" font-size="3" dominant-baseline="central">${d.l}</text>`;
    a0 = a1;
  });
  return svgWrap(o + leg, [-r - 4.5, -r - 1, r + 27, Math.max(r + 1, -r + 1 + data.length * 5.2)]);
};

// Area model for a(b + c): rectangle split into two parts (not to scale)
const areaModel = ({ out, p1, p2, a1, a2, w = 52, h = 14 }) => {
  const w1 = w * 0.6;
  let o = `<rect x="0" y="0" width="${w1}" height="${h}" fill="#e3dcf5" stroke="#222" stroke-width="0.4"/><rect x="${w1}" y="0" width="${w - w1}" height="${h}" fill="#fde7c7" stroke="#222" stroke-width="0.4"/>`;
  o += label(w1 / 2, -2.6, p1) + label(w1 + (w - w1) / 2, -2.6, p2) + label(-3.2, h / 2, out);
  o += label(w1 / 2, h / 2, a1, { weight: 700, size: 3.4 }) + label(w1 + (w - w1) / 2, h / 2, a2, { weight: 700, size: 3.4 });
  return svgWrap(o, [-6.5, -5.2, w + 0.6, h + 0.6]);
};

// Rectangle with algebraic side labels (not to scale)
const rectAlg = ({ lL, lW, w = 30, h = 13 }) => {
  let o = `<rect x="0" y="0" width="${w}" height="${h}" fill="#f4f0fb" stroke="#222" stroke-width="0.45"/>`;
  o += label(w / 2, h + 2.6, lL) + label(w + 1.4 + tw(lW) / 2, h / 2, lW);
  return svgWrap(o, [-0.6, -0.6, w + tw(lW) + 3, h + 4.6]);
};

module.exports = { gcd, Fr, fr, mx, fPlain, fImp, dec, rnd, isSq, recurring, M, F, FH, FI, SQ, REC, RECP, B, H, money,
  ANS, setGroup, reg, chip, sec, learn, we, you, grid, row, Q, tri, squaresFig, rectDiag, isoFig, bar, pie, areaModel, rectAlg, label, svgWrap };
