// Year 8 catch-up revision booklet: Pythagoras' theorem · Fractions, decimals & percentages · Algebraic techniques
// Usage: node build.js [outDir]   → writes the 9-page booklet, the answer booklet and answers.json
// Every answer is calculated here from the numbers in its question (see lib.js → Q and reg).

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const L = require('./lib');
const { fr, mx, fPlain, fImp, dec, rnd, recurring, M, F, FH, FI, SQ, REC, RECP, B, H, money,
  ANS, setGroup, sec, learn, we, you, grid, row, Q, tri, squaresFig, rectDiag, isoFig, bar, pie, areaModel, rectAlg } = L;

const OUT = path.resolve(process.argv[2] || path.join(__dirname, '..'));
const BASE = 'Yr8_Mixed_Pythagoras_FDP_Algebra_Revision_Booklet';

const TOPIC = {
  1: { name: 'Pythagoras’ theorem', cls: 't1' },
  2: { name: 'Fractions, decimals and percentages', cls: 't2' },
  3: { name: 'Algebraic techniques', cls: 't3' },
};
const page = (n, t, tp, body) => `<section class="page ${TOPIC[t].cls}">
<div class="hd"><span>Kingscliff High School · Year 8 Mathematics · Catch-up revision booklet</span><span><b>Topic ${t} · ${TOPIC[t].name}</b> · page ${tp} of 3</span></div>
<div class="inner">${body}</div>
<div class="ft"><span>Check your answers in the answer booklet. Diagrams are drawn to scale unless marked “not to scale”.</span><span>Page ${n} of 9</span></div>
</section>`;
const band = (t, title, outcomes, right) => `<div class="band"><div class="num">${t}</div><div><div class="ttl">${title}</div><div class="out">${outcomes}</div></div><div class="pg">${right}</div></div>`;
const check = (items) => `<div class="check"><b style="white-space:nowrap">I can do this on my own:</b>${items.map((s) => `<span style="white-space:nowrap"><span class="box"></span>${s}</span>`).join('')}</div>`;
const g = (k) => setGroup(k);

// ---------------------------------------------------------------- Pythagoras helpers (answers worked out in code)
const sqr = (x) => +(x * x).toFixed(6);
const root = (s) => { const r = Math.sqrt(s); return { r, exact: Math.abs(r - Math.round(r * 1e6) / 1e6) < 1e-9 && Number.isInteger(+(r * 100).toFixed(6)) }; };
const hypA = (a, b, u, v = 'x') => {
  const s = +(sqr(a) + sqr(b)).toFixed(6), { r, exact } = root(s);
  return [`${M(`${v}^2 = ${dec(a)}^2 + ${dec(b)}^2 = ${dec(sqr(a))} + ${dec(sqr(b))} = ${dec(s)}`)}, ${M(v)} = ${SQ(dec(s))} ${exact ? '= ' + dec(r) : '≈ ' + rnd(r, 1)} ${u}`,
    exact ? `${dec(r)} ${u}` : `√${dec(s)} ≈ ${rnd(r, 1)} ${u}`];
};
const legA = (c, b, u, v = 'y') => {
  const s = +(sqr(c) - sqr(b)).toFixed(6), { r, exact } = root(s);
  return [`${M(`${v}^2 = ${dec(c)}^2 - ${dec(b)}^2 = ${dec(sqr(c))} - ${dec(sqr(b))} = ${dec(s)}`)}, ${M(v)} = ${SQ(dec(s))} ${exact ? '= ' + dec(r) : '≈ ' + rnd(r, 1)} ${u}`,
    exact ? `${dec(r)} ${u}` : `√${dec(s)} ≈ ${rnd(r, 1)} ${u}`];
};
const converse = (x, y, z) => {
  const [a, b, c] = [x, y, z].sort((p, q) => p - q);
  const L2 = sqr(c), S = +(sqr(a) + sqr(b)).toFixed(6), yes = Math.abs(L2 - S) < 1e-9;
  return { L2, S, yes, a, b, c,
    h: `${dec(c)}² = ${dec(L2)}; ${dec(a)}² + ${dec(b)}² = ${dec(sqr(a))} + ${dec(sqr(b))} = ${dec(S)}. ${yes ? '<span class="ok">Equal, so it is right-angled.</span>' : `<span class="no">${dec(L2)} ≠ ${dec(S)}, so it is not right-angled.</span>`}`,
    p: yes ? 'yes' : 'no' };
};

// ================================================================= PAGE 1
g('Topic 1 · Your turn 1 — Squares, powers and square roots (page 1)');
const yt1 = [
  ['a', M('6^2'), '6 × 6 = 36', 6 ** 2], ['b', M('11^2'), '11 × 11 = 121', 11 ** 2], ['c', M('0.3^2'), '0.3 × 0.3 = 0.09', sqr(0.3)],
  ['d', M('3^4'), '3 × 3 × 3 × 3 = 81', 3 ** 4], ['e', M('10^3'), '10 × 10 × 10 = 1000', 10 ** 3],
  ['f', SQ(81), '9, because 9² = 81', Math.sqrt(81)], ['g', SQ(196), '14, because 14² = 196', Math.sqrt(196)],
  ['h', M('5^2 + 12^2'), '25 + 144 = 169', 5 ** 2 + 12 ** 2], ['i', SQ(M('5^2 + 12^2')), '√169 = 13', Math.sqrt(5 ** 2 + 12 ** 2)],
].map(([l, q, h, v]) => Q(`1.1${l}`, l, q, [h, dec(v)], { inl: '=', lw: 9 }));

g('Topic 1 · Your turn 2 — The hypotenuse (page 1)');
const yt2 = [
  Q('1.2a', 'a', 'Hypotenuse:', ['<i>PR</i> (opposite the right angle at <i>Q</i>)', 'PR'], { fig: tri({ a: 4, b: 3, vl: ['Q', 'R', 'P'], w: 22, h: 13 }), inlpos: 1, lw: 12 }),
  Q('1.2b', 'b', 'Hypotenuse:', ['<i>XY</i> (opposite the right angle at <i>Z</i>)', 'XY'], { fig: tri({ a: 5, b: 3, rot: 160, vl: ['Z', 'X', 'Y'], w: 24, h: 13 }), inlpos: 1, lw: 12 }),
  Q('1.2c', 'c', 'Hypotenuse:', ['<i>MN</i> (opposite the right angle at <i>L</i>)', 'MN'], { fig: tri({ a: 3, b: 4.5, rot: 60, flip: true, vl: ['L', 'M', 'N'], w: 22, h: 13 }), inlpos: 1, lw: 12 }),
  Q('1.2d', 'd', 'Rule:', [M('r^2 = p^2 + q^2') + ' (<i class="v">r</i> is opposite the right angle)', 'r² = p² + q²'], { fig: tri({ a: 4, b: 3, rot: 180, la: '$p', lb: '$q', lc: '$r', w: 22, h: 13 }), inlpos: 1, lw: 26 }),
];

g('Topic 1 · Your turn 3 — Finding the hypotenuse (page 1)');
const yt3 = [
  Q('1.3a', 'a', 'Fill in the blanks.', hypA(6, 8, 'cm'), { fig: tri({ a: 8, b: 6, la: '8 cm', lb: '6 cm', lc: '$x', w: 24, h: 13 }),
    sc: `${H(M('x^2 = 6^2 + 8^2'))}<br>${M('x^2')} = ${B(8)} + ${B(8)}<br>${M('x^2')} = ${B(10)}<br>${M('x')} = ${SQ(B(9))} = ${B(8)} cm` }),
  Q('1.3b', 'b', 'Fill in the blanks.', hypA(20, 21, 'm'), { fig: tri({ a: 21, b: 20, la: '21 m', lb: '20 m', lc: '$x', rot: 180, w: 24, h: 13 }),
    sc: `${M('x^2')} = ${B(6)}² + ${B(6)}²<br>${M('x^2')} = ${B(8)} + ${B(8)} = ${B(8)}<br>${M('x')} = ${B(12)} m` }),
  Q('1.3c', 'c', 'Round to 1 decimal place.', hypA(7, 10, 'cm'), { fig: tri({ a: 10, b: 7, la: '10 cm', lb: '7 cm', lc: '$x', flip: true, w: 24, h: 13 }), work: 15, line: M('x') + ' ≈ ', unit: 'cm', lw: 12 }),
  Q('1.3d', 'd', 'Show your working.', hypA(2.4, 1.8, 'm'), { fig: tri({ a: 2.4, b: 1.8, la: '2.4 m', lb: '1.8 m', lc: '$x', rot: 90, w: 22, h: 13 }), work: 15, line: M('x') + ' = ', unit: 'm', lw: 12 }),
];

const p1 = page(1, 1, 1, `
<div class="title"><div><div class="kick">YEAR 8 MATHEMATICS · GETTING READY FOR THE YEARLY EXAM</div><div class="big">Catch-up revision booklet</div>
<div class="sub">Pythagoras’ theorem · Fractions, decimals and percentages · Algebraic techniques</div></div>
<div class="name">Name: ${B(44)}<br>Date started: ${B(30)}</div></div>
<div class="legend"><span><span class="sw" style="background:var(--acc)"></span><b>1 LEARN IT</b> read it</span><span><span class="sw" style="background:var(--we)"></span><b>2 WORKED EXAMPLE</b> follow each line</span><span><span class="sw" style="background:var(--you)"></span><b>3 YOUR TURN</b> fill the blanks</span><span><b>4 CHECK</b> with the answer booklet</span></div>
${band(1, 'Pythagoras’ theorem', 'NSW syllabus: <b>MA4-PYT-C-01</b> applies Pythagoras’ theorem to solve problems in various contexts · <b>MA4-IND-C-01</b> squares and square roots · <b>MAO-WM-01</b> working mathematically', 'Yearly exam<br>Section C · Q15, Q17, Q18')}
${sec('1A', 'Squares, powers and square roots', 'easy', 'Q17')}
${learn(row('1fr', [`<ul class="k"><li><b>Squaring</b> multiplies a number by itself: ${M('7^2')} = 7 × 7 = 49 <span class="mut">(not 7 × 2)</span>.</li>
<li>A <b>power</b> says how many times to multiply: ${M('2^5')} = 2 × 2 × 2 × 2 × 2 = 32.</li>
<li>The <b>square root</b> undoes squaring: ${SQ(49)} = 7, because ${M('7^2')} = 49.</li></ul>`,
`<div style="display:flex;align-items:center;gap:2mm"><table class="sqt" style="margin:0"><tr><td class="h">${M('n')}</td>${[...Array(15)].map((_, i) => `<td>${i + 1}</td>`).join('')}</tr><tr><td class="h">${M('n^2')}</td>${[...Array(15)].map((_, i) => `<td>${(i + 1) ** 2}</td>`).join('')}</tr></table><span class="small mut">← perfect squares:<br>learn these by heart</span></div>`], 'gap:1mm'))}
${you(1, 'Evaluate.', grid(5, yt1, 'gap:1.3mm 2mm'))}
${sec('1B', 'The hypotenuse and Pythagoras’ theorem', 'easyc')}
${learn(row('1fr 34mm', [`<ul class="k"><li>A <b>right-angled triangle</b> has one 90° angle, marked with a small square.</li>
<li>The <b>hypotenuse</b> is the <b>longest side</b>. It is <b>opposite</b> (across from) the right angle.</li>
<li><b>Pythagoras’ theorem:</b> in a right-angled triangle, the square of the hypotenuse equals the sum of the squares of the two shorter sides.</li></ul>
<div style="margin:1.2mm 0 0 3.6mm" class="big2"><b>${M('c^2 = a^2 + b^2')}</b> &nbsp;<span class="small mut">where ${M('c')} is the hypotenuse and ${M('a')} and ${M('b')} are the two shorter sides.</span></div>
<div style="margin:0.6mm 0 0 3.6mm" class="small">See it: in a 3, 4, 5 triangle, the squares on the shorter sides (9 + 16) match the square on the hypotenuse (25).</div>`,
`<div class="figc">${squaresFig(2.45)}</div>`]))}
${you(2, 'Name the hypotenuse in a, b and c. In d, write Pythagoras’ theorem for the triangle.', grid(4, yt2))}
${sec('1C', 'Finding the hypotenuse', 'med', 'Q15a')}
${we(grid(2, [row('auto 1fr', [`<div class="figc">${tri({ a: 12, b: 9, la: '12 cm', lb: '9 cm', lc: '$x', w: 24, h: 15 })}</div>`,
  `<div class="ln">${M('c^2 = a^2 + b^2')} <span class="small mut">← write the rule</span><br>${M('x^2 = 9^2 + 12^2')} <span class="small mut">← substitute</span><br>${M('x^2 = 81 + 144 = 225')}<br>${M('x')} = ${SQ(225)} = <b>15 cm</b> <span class="small mut">← square root</span></div>`]),
row('auto 1fr', [`<div class="figc">${tri({ a: 8, b: 5, la: '8 cm', lb: '5 cm', lc: '$x', w: 24, h: 15 })}</div>`,
  `<div class="ln">${M('x^2 = 5^2 + 8^2 = 25 + 64 = 89')}<br>${M('x')} = ${SQ(89)} <span class="small mut">← exact answer (a surd)</span><br>${M('x')} ≈ 9.433 98… ≈ <b>9.4 cm</b> <span class="small mut">(1 d.p.)</span><br><span class="small mut">≈ means “is approximately equal to”.</span></div>`])], 'grid-template-columns:0.9fr 1.1fr'))}
${you(3, 'Find the length of the hypotenuse, ' + M('x') + '. <span class="mut" style="font-weight:400">Grey steps are done for you.</span>', grid(4, yt3))}
`);

// ================================================================= PAGE 2
g('Topic 1 · Your turn 4 — Finding a shorter side (page 2)');
const yt4 = [
  Q('1.4a', 'a', 'Fill in the blanks.', legA(10, 8, 'cm'), { fig: tri({ a: 8, b: 6, la: '8 cm', lb: '$y', lc: '10 cm', w: 26, h: 16 }),
    sc: `${H(M('y^2 = 10^2 - 8^2'))}<br>${M('y^2')} = ${B(8)} − ${B(8)}<br>${M('y^2')} = ${B(10)}<br>${M('y')} = ${SQ(B(9))} = ${B(8)} cm` }),
  Q('1.4b', 'b', 'Fill in the blanks.', legA(25, 15, 'm'), { fig: tri({ a: 15, b: 20, la: '15 m', lb: '$y', lc: '25 m', flip: true, w: 26, h: 18 }),
    sc: `${M('y^2')} = ${B(6)}² − ${B(6)}²<br>${M('y^2')} = ${B(8)} − ${B(8)} = ${B(8)}<br>${M('y')} = ${B(12)} m` }),
  Q('1.4c', 'c', 'Round to 1 decimal place.', legA(9, 5, 'cm'), { fig: tri({ a: 5, b: Math.sqrt(56), la: '5 cm', lb: '$y', lc: '9 cm', rot: 90, w: 24, h: 16 }), work: 14, line: M('y') + ' ≈ ', unit: 'cm', lw: 12 }),
  Q('1.4d', 'd', '<b>Add or subtract?</b> Find ' + M('x') + '.', hypA(6, 2.5, 'm'), { fig: tri({ a: 6, b: 2.5, la: '6 m', lb: '2.5 m', lc: '$x', rot: 180, w: 26, h: 14 }), work: 14, line: M('x') + ' = ', unit: 'm', lw: 12 }),
];

g('Topic 1 · Your turn 5 — Surds (page 2)');
const surdList = [1, 8, 30, 49, 45, 100, 2, 144];
const yt5 = [
  Q('1.5a', 'a', `Circle the surds: &nbsp;${surdList.map((n) => SQ(n)).join(' &nbsp; ')}`, [`${surdList.filter((n) => !Number.isInteger(Math.sqrt(n))).map((n) => SQ(n)).join(', ')} <span class="mut">(the others are 1, 7, 10 and 12)</span>`, surdList.filter((n) => !Number.isInteger(Math.sqrt(n))).map((n) => '√' + n).join(', ')]),
  Q('1.5b', 'b', `${SQ(30)} lies between which two whole numbers? Explain.`, ['5 and 6, because 5² = 25 and 6² = 36, and 30 is between 25 and 36.', '5 and 6'], { line: '', lw: 58 }),
  Q('1.5c', 'c', 'A right-angled triangle has shorter sides 3 cm and 5 cm. Find the hypotenuse.', [hypA(3, 5, 'cm')[0].replace('≈', '(exact) ≈'), '√34 cm ≈ 5.8 cm'], { line: 'Exact: ' + M('x') + ' = ', unit: 'cm &nbsp;&nbsp; Rounded: ' + M('x') + ' ≈ ' + B(12) + ' cm', lw: 14 }),
];

g('Topic 1 · Your turn 6 — Pythagoras in real life (page 2)');
const yt6 = [
  Q('1.6a', 'a', 'A rectangular paddock is 40 m long and 30 m wide. How long is the diagonal path across it?', [hypA(40, 30, 'm', 'd')[0] + '. The path is 50 m long.', '50 m'],
    { fig: rectDiag({ L: 40, W: 30, lL: '40 m', lW: '30 m', lD: '$d', w: 26 }), work: 8, line: 'The path is ', unit: 'm long.', lw: 12 }),
  Q('1.6b', 'b', 'A phone screen is 7 cm wide and 15 cm tall. Find the length of its diagonal, to 1 decimal place. <span class="mut">Draw a diagram first.</span>', [hypA(7, 15, 'cm', 'd')[0], '√274 ≈ 16.6 cm'], { work: 21 }),
  Q('1.6c', 'c', 'Ava flies a kite on a 30 m string pulled tight. The kite is directly above a point 18 m from Ava’s hand. How high is the kite above her hand?', [legA(30, 18, 'm', 'h')[0] + '. The kite is 24 m above her hand.', '24 m'], { work: 21 }),
];

const p2 = page(2, 1, 2, `
${sec('1D', 'Finding a shorter side', 'med')}
${learn(row('1fr 1fr 1fr', [`<b>Which side is missing?</b><br>Find the right angle. The side opposite it is the hypotenuse.`,
  `<b>Missing the hypotenuse → ADD</b><br>${M('c^2 = a^2 + b^2')}`,
  `<b>Missing a shorter side → SUBTRACT</b><br>${M('a^2 = c^2 - b^2')} <span class="small">(hypotenuse² − the other side²)</span>`], 'gap:4mm') + '<div class="small" style="margin-top:0.8mm">Check: a shorter side must come out <b>smaller</b> than the hypotenuse.</div>')}
${we(grid(2, [row('auto 1fr', [`<div class="figc">${tri({ a: 5, b: 12, la: '5 cm', lb: '$y', lc: '13 cm', w: 22, h: 20 })}</div>`,
  `<div class="ln">${M('y^2 = 13^2 - 5^2')} <span class="small mut">← subtract</span><br>${M('y^2 = 169 - 25 = 144')}<br>${M('y')} = ${SQ(144)} = <b>12 cm</b><br><span class="small mut">Check: 12 is less than 13 ✓</span></div>`]),
  row('auto 1fr', [`<div class="figc">${tri({ a: 7, b: Math.sqrt(95), la: '7 cm', lb: '$y', lc: '12 cm', flip: true, w: 22, h: 20 })}</div>`,
  `<div class="ln">${M('y^2 = 12^2 - 7^2')}<br>${M('y^2 = 144 - 49 = 95')}<br>${M('y')} = ${SQ(95)} ≈ 9.746… ≈ <b>9.7 cm</b><br><span class="small mut">Check: 9.7 is less than 12 ✓</span></div>`])]))}
${you(4, 'Find the length of the unknown side. Round to 1 decimal place where needed.', grid(4, yt4))}
${sec('1E', 'Surds: exact answers', 'med', 'Q18a')}
${row('1fr 1.35fr', [learn(`<ul class="k"><li>${SQ(81)} = 9 is a whole number, so ${SQ(81)} is <b>not</b> a surd.</li>
<li>${SQ(89)} = 9.433 981 1… goes on forever and never repeats, so ${SQ(89)} <b>is</b> a surd.</li>
<li>The square root of a whole number is a <b>surd</b> when the number is <b>not</b> a perfect square.</li>
<li><b>Exact</b> answer: ${SQ(89)}. <b>Rounded</b> answer: ≈ 9.4</li></ul>`, 'margin:0'),
you(5, '', `<div class="g" style="gap:1.6mm">${yt5.join('')}</div>`, 'margin:0')])}
${sec('1F', 'Pythagoras in real life', 'hard')}
${row('1fr 1.15fr', [learn(`<b>Four steps for worded problems</b><ol style="margin:0.3mm 0 0;padding-left:4mm"><li>Draw a diagram. Mark the right angle.</li><li>Label the sides you know; use a pronumeral for the unknown.</li><li>Unknown hypotenuse → add. Shorter side → subtract.</li><li>Answer in a sentence, with units.</li></ol>`, 'margin:0'),
we(row('auto 1fr', [`<div class="figc">${tri({ a: 0.9, b: 4, la: '0.9 m', lb: '$h', lc: '4.1 m', flip: true, w: 10, h: 21 })}</div>`,
  `<div class="small" style="line-height:1.45">A 4.1 m ladder leans against a wall. Its foot is 0.9 m from the wall. How high up the wall does it reach?<br>The ladder is the hypotenuse, so subtract:<br>${M('h^2 = 4.1^2 - 0.9^2 = 16.81 - 0.81 = 16')}<br>${M('h')} = ${SQ(16)} = 4. <b>The ladder reaches 4 m up the wall.</b></div>`]), 'WORKED EXAMPLE', 'margin:0')])}
${you(6, '', grid('1fr 1fr 1fr', yt6))}
`);

// ================================================================= PAGE 3
g('Topic 1 · Your turn 7 — Is it right-angled? (page 3)');
const yt7rows = [[6, 8, 10], [4, 5, 6], [9, 40, 41], [10, 11, 15], [1.5, 2, 2.5], [11, 60, 61]];
const yt7 = yt7rows.map((s, i) => {
  const c = converse(...s), l = 'abcdef'[i];
  L.reg(`1.7${l}`, l, `${c.h}`, c.p);
  const sides = s.map((x) => dec(x)).join(', ');
  return i === 0
    ? `<tr><td><b>${l}</b>&nbsp; ${sides}</td><td>${H('10² =')} ${B(8)}</td><td>${H('6² + 8² =')} ${B(6)} + ${B(6)} = ${B(7)}</td><td>${H('Yes / No')}</td><td>${H('Yes / No')}</td></tr>`
    : `<tr><td><b>${l}</b>&nbsp; ${sides}</td><td></td><td></td><td></td><td></td></tr>`;
});
g('Topic 1 · Your turn 8 — Pythagorean triads (page 3)');
const yt8 = [
  Q('1.8a', 'a', 'Show that 5, 12, 13 is a Pythagorean triad.', ['5² + 12² = 25 + 144 = 169 = 13² ✓', 'yes'], { work: 7 }),
  Q('1.8b', 'b', 'Multiply 3, 4, 5 by 5. Check that the new numbers make a triad.', ['15, 20, 25: 15² + 20² = 225 + 400 = 625 = 25² ✓', '15, 20, 25'], { work: 7 }),
  Q('1.8c', 'c', 'Complete each triad.', ['9, 12, 15 (81 + 144 = 225 = 15²); 10, 24, 26 (676 − 100 = 576 = 24²)', '15; 24'], { sc: '9, 12, ' + B(9) + '<br>10, ' + B(9) + ', 26' }),
];
g('Topic 1 · Your turn 9 — Exam-style practice (page 3)');
const c92 = converse(8, 10, 13), c93 = converse(60, 80, 100);
const yt9 = [
  Q('1.9a', '1', 'Find the length of the hypotenuse, ' + M('x') + '.', hypA(12, 35, 'cm'), { marks: '2 marks', fig: tri({ a: 35, b: 12, la: '35 cm', lb: '12 cm', lc: '$x', w: 34, h: 12 }), work: 10, line: M('x') + ' = ', unit: 'cm', lw: 12 }),
  Q('1.9b', '2', 'A triangle has sides 8 cm, 10 cm and 13 cm. Is it a right-angled triangle? Show working.', [c92.h, c92.p], { marks: '2 marks', work: 19 }),
  Q('1.9c', '3', 'A builder checks that a corner is square. She marks 60 cm along one wall and 80 cm along the other. The distance between the marks is 1 m. Is the corner a right angle?', [`1 m = 100 cm. ${c93.h}`, c93.p], { marks: '2 marks', work: 16 }),
  Q('1.9d', '4', 'An isosceles triangle has two sides of 10 cm and a base of 12 cm. Find its perpendicular height, ' + M('h') + '.', ['Half the base is 6 cm. ' + legA(10, 6, 'cm', 'h')[0], '8 cm'], { marks: '2 marks', fig: isoFig({ base: 12, side: 10, s: 1.6 }), work: 6, line: M('h') + ' = ', unit: 'cm', lw: 12 }),
];
g('Topic 1 · Extension — Simplifying surds (page 3)');
const simpSurd = (n) => { let k = 1; for (let i = 2; i * i <= n; i++) if (n % (i * i) === 0) k = i; return { k, r: n / (k * k) }; };
const ext = [8, 20, 27, 75].map((n, i) => { const { k, r } = simpSurd(n); return Q(`1.10${'abcd'[i]}`, 'abcd'[i], SQ(n), [`${SQ(n)} = ${SQ(`${k * k} × ${r}`)} = ${k}${SQ(r)}`, `${k}√${r}`], { line: '= ', lw: 14 }); });

const p3 = page(3, 1, 3, `
${sec('1G', 'Is it a right-angled triangle? (the converse of Pythagoras’ theorem)', 'med', 'Q15b')}
${row('1fr 1.3fr', [learn(`<ol style="margin:0;padding-left:4mm"><li>Square the <b>longest</b> side.</li><li>Square the two shorter sides and <b>add</b>.</li><li>If the answers are <b>equal</b>, the triangle <b>is</b> right-angled. The right angle is opposite the longest side. If they are not equal, it is <b>not</b> right-angled.</li></ol><div class="small" style="margin-top:0.6mm">Always finish with a sentence that answers the question.</div>`, 'margin:0'),
we(`<div class="ln"><b>(a)</b> 12 cm, 16 cm, 20 cm: &nbsp;${M('20^2')} = 400 &nbsp;and&nbsp; ${M('12^2 + 16^2')} = 144 + 256 = 400<br>400 = 400, so <b>the triangle is right-angled</b>.<br><b>(b)</b> 5 cm, 7 cm, 9 cm: &nbsp;${M('9^2')} = 81 &nbsp;and&nbsp; ${M('5^2 + 7^2')} = 25 + 49 = 74<br>81 ≠ 74, so <b>the triangle is not right-angled</b>.</div>`, 'WORKED EXAMPLE', 'margin:0')])}
${you(7, 'Is each triangle right-angled? The sides are in centimetres.', `<table class="t"><tr><th style="width:24%">Sides</th><th style="width:17%">Longest side²</th><th>Sum of the squares of the other two sides</th><th style="width:12%">Equal?</th><th style="width:15%">Right-angled?</th></tr>${yt7.join('')}</table>`)}
${sec('1H', 'Pythagorean triads', 'med')}
${row('1.15fr 2fr', [learn(`A <b>Pythagorean triad</b> is three whole numbers that fit ${M('a^2 + b^2 = c^2')}, such as 3, 4, 5 &nbsp;(9 + 16 = 25).<br>Multiply a triad by any whole number to get another: 3, 4, 5 → 6, 8, 10 → 9, 12, 15.`, 'margin:0'),
you(8, '', grid(3, yt8), 'margin:0')])}
${sec('1I', 'Exam-style practice', 'hard', 'Q15')}
${you(9, 'Show all working.', grid(2, yt9, 'gap:2mm 5mm'))}
<div class="ext-box" style="line-height:1.5">${row('1.5fr 1fr', [`<div class="tag">EXTENSION · STAGE 5 PATH CONTENT · <span style="color:var(--exam)">YOUR EXAM ASKS THIS IN Q18b</span></div><b>Simplifying a surd:</b> find the <b>largest square factor</b> (4, 9, 16, 25, 36, …) and take its square root out.<br>
${SQ(18)} = ${SQ('9 × 2')} = ${SQ(9)} × ${SQ(2)} = <b>3${SQ(2)}</b> &nbsp;&nbsp; ${SQ(48)} = ${SQ('16 × 3')} = <b>4${SQ(3)}</b> <span class="small mut">(not ${SQ('4 × 12')}: 4 is not the largest square factor)</span>`,
`<div class="yt">Simplify.</div>${grid(4, ext, 'gap:1mm 2mm')}`])}</div>
${check(['hypotenuse', 'shorter side', 'right angle test', 'surds'])}
`);

// ================================================================= PAGE 4 — fractions
g('Topic 2 · Your turn 1 — Equivalent fractions and mixed numerals (page 4)');
const ord = [fr(2, 3), fr(3, 4), fr(5, 8)];
const ordSorted = [...ord].sort((a, b) => a.val() - b.val());
const yt21 = [
  Q('2.1a', 'a', `Complete: ${F(2, 3)} = ${F(B(5), 12)}`, [`${F(8, 12)} (multiply top and bottom by 4)`, '8']),
  Q('2.1b', 'b', `Simplify ${F(15, 25)}`, [`${FI(fr(15, 25))} (÷ 5)`, fImp(fr(15, 25))], { inl: '=', lw: 10 }),
  Q('2.1c', 'c', `Simplify ${F(24, 32)}`, [`${FI(fr(24, 32))} (÷ 8)`, fImp(fr(24, 32))], { inl: '=', lw: 10 }),
  Q('2.1d', 'd', `Improper fraction: ${F(2, 7, 3)} =`, [`${F('3 × 7 + 2', 7)} = ${FI(mx(3, 2, 7))}`, fImp(mx(3, 2, 7))], { inl: '', lw: 10 }),
  Q('2.1e', 'e', `Mixed numeral: ${F(29, 6)} =`, [`29 ÷ 6 = 4 remainder 5, so ${FH(fr(29, 6))}`, fPlain(fr(29, 6))], { inl: '', lw: 10 }),
  Q('2.1f', 'f', `Order from smallest to largest: &nbsp;${ord.map(FI).join(' &nbsp; ')}`, [`${F(16, 24)}, ${F(18, 24)}, ${F(15, 24)} → ${ordSorted.map(FI).join(', ')}`, ordSorted.map(fImp).join(', ')], { line: '', lw: 36, cls: 'span2' }),
];
g('Topic 2 · Your turn 2 — Adding and subtracting fractions (page 4)');
const addQ = (key, l, a, op, b, aH, bH, o = {}) => {
  const r = op === '+' ? a.add(b) : a.sub(b);
  return Q(key, l, `${aH} ${op === '+' ? '+' : '−'} ${bH}`, [`${o.work || ''}= ${FH(r)}`, fPlain(r)], o.q || {});
};
const yt22 = [
  addQ('2.2a', 'a', fr(1, 2), '+', fr(1, 3), F(1, 2), F(1, 3), { q: { sc: `= ${F(B(5), 6)} + ${F(B(5), 6)} = ${F(B(5), 6)}` }, work: `${F(3, 6)} + ${F(2, 6)} ` }),
  addQ('2.2b', 'b', fr(4, 5), '−', fr(1, 2), F(4, 5), F(1, 2), { q: { sc: `= ${F(B(5), 10)} − ${F(B(5), 10)} = ${F(B(5), 10)}` }, work: `${F(8, 10)} − ${F(5, 10)} ` }),
  addQ('2.2c', 'c', fr(3, 4), '+', fr(5, 6), F(3, 4), F(5, 6), { q: { sc: `= ${F(B(5), 12)} + ${F(B(5), 12)} = ${B(10)}` }, work: `${F(9, 12)} + ${F(10, 12)} = ${F(19, 12)} ` }),
  addQ('2.2d', 'd', mx(2, 1, 4), '+', mx(1, 2, 3), F(1, 4, 2), F(2, 3, 1), { q: { work: 14, line: '= ', lw: 12 }, work: `${F(9, 4)} + ${F(5, 3)} = ${F(27, 12)} + ${F(20, 12)} = ${F(47, 12)} ` }),
  addQ('2.2e', 'e', fr(5), '−', mx(2, 3, 8), '5', F(3, 8, 2), { q: { work: 14, line: '= ', lw: 12 }, work: `${F(40, 8)} − ${F(19, 8)} = ${F(21, 8)} ` }),
];
g('Topic 2 · Your turn 3 — Multiplying and dividing fractions (page 4)');
const mq = (key, l, a, op, b, aH, bH, work, o = {}) => {
  const r = op === '×' ? a.mul(b) : a.div(b);
  return Q(key, l, `${aH} ${op} ${bH}`, [`${work}= ${FH(r)}`, fPlain(r)], o);
};
const yt23 = [
  mq('2.3a', 'a', fr(2, 5), '×', fr(3, 7), F(2, 5), F(3, 7), '', { line: '= ', lw: 10 }),
  mq('2.3b', 'b', fr(5, 6), '×', fr(3, 10), F(5, 6), F(3, 10), `${F(1, 2)} × ${F(1, 2)} (cancel 5 and 10, 3 and 6) `, { line: '= ', lw: 10 }),
  mq('2.3c', 'c', mx(1, 1, 3), '×', fr(3, 8), F(1, 3, 1), F(3, 8), `${F(4, 3)} × ${F(3, 8)} `, { work: 11, line: '= ', lw: 10 }),
  mq('2.3d', 'd', fr(3, 4), '÷', fr(1, 2), F(3, 4), F(1, 2), `${F(3, 4)} × ${F(2, 1)} = ${F(6, 4)} `, { sc: `= ${F(3, 4)} × ${F(B(6), B(6))} = ${B(10)}` }),
  mq('2.3e', 'e', fr(2, 3), '÷', fr(4), F(2, 3), '4', `${F(2, 3)} × ${F(1, 4)} `, { work: 11, line: '= ', lw: 10 }),
  mq('2.3f', 'f', mx(3, 1, 2), '÷', mx(1, 3, 4), F(1, 2, 3), F(3, 4, 1), `${F(7, 2)} × ${F(4, 7)} `, { work: 11, line: '= ', lw: 10 }),
];
const sheepB = fr(1, 3).mul(fr(36)).val(), sheepBr = fr(1, 4).mul(fr(36)).val();
const cups = mx(2, 1, 4).mul(fr(3));
yt23.push(Q('2.3g', 'g', 'A farmer has 36 sheep. One-third are black, one-quarter are brown and the rest are white. How many are white?', [`black ${F(1, 3)} × 36 = ${sheepB}, brown ${F(1, 4)} × 36 = ${sheepBr}, white 36 − ${sheepB} − ${sheepBr} = ${36 - sheepB - sheepBr}`, `${36 - sheepB - sheepBr}`], { work: 12, cls: 'span3' }));
yt23.push(Q('2.3h', 'h', `A cake needs ${F(1, 4, 2)} cups of flour. How much flour is needed for 3 cakes?`, [`${F(9, 4)} × 3 = ${F(27, 4)} = ${FH(cups)} cups`, fPlain(cups) + ' cups'], { work: 12, cls: 'span3' }));

const p4 = page(4, 2, 1, `
${band(2, 'Fractions, decimals and percentages', 'NSW syllabus: <b>MA4-FRC-C-01</b> represents and operates with fractions, decimals and percentages to solve problems · <b>MAO-WM-01</b> working mathematically', 'Yearly exam<br>Section C · Q16 · Section B · Q9')}
${sec('2A', 'Equivalent fractions, simplifying and mixed numerals', 'easy')}
${row('1.55fr 1fr', [learn(`<div style="display:grid;grid-template-columns:auto 1fr;gap:0.9mm 3mm;align-items:center">
<b>Equivalent fractions</b><span>Multiply or divide the <b>numerator</b> (top) and <b>denominator</b> (bottom) by the same number.</span>
<b>Simplify</b><span>Divide the top and bottom by their <b>highest common factor</b> (HCF): ${F(18, 30)} = ${F('18 ÷ 6', '30 ÷ 6')} = ${F(3, 5)}</span>
<b>Mixed → improper</b><span>${F(3, 5, 2)} = ${F('2 × 5 + 3', 5)} = ${F(13, 5)}</span>
<b>Improper → mixed</b><span>${F(17, 4)}: 17 ÷ 4 = 4 remainder 1, so ${F(17, 4)} = ${F(1, 4, 4)}</span></div>`, 'margin:0'),
`<div class="learn" style="margin:0"><div class="tag">SEE IT</div><div style="display:grid;grid-template-columns:auto 1fr;gap:1mm 2mm;align-items:center">${bar({ n: 4, k: 3, w: 40 })}<span>${F(3, 4)}</span>${bar({ n: 8, k: 6, w: 40 })}<span>${F(6, 8)}</span></div><div class="small" style="margin-top:0.8mm">Same amount shaded, so ${F(3, 4)} = ${F(6, 8)}. Cutting each quarter in half doubles the top <b>and</b> the bottom.</div></div>`])}
${you(1, '', grid(3, [...yt21.slice(0, 3), yt21[5], ...yt21.slice(3, 5)], 'gap:2.4mm 3mm'))}
${sec('2B', 'Adding and subtracting fractions', 'med')}
${row('1.1fr 1fr', [learn(`Fractions need the <b>same denominator</b> before you add or subtract.<ol style="margin:0.3mm 0 0;padding-left:4mm"><li>Find the <b>lowest common denominator</b> (LCD) and rewrite each fraction.</li><li>Add or subtract the numerators. Keep the denominator.</li><li>Mixed numerals: change to improper fractions first.</li></ol>`, 'margin:0'),
we(`<div class="ln">${F(2, 3)} + ${F(1, 4)} = ${F(8, 12)} + ${F(3, 12)} = <b>${F(11, 12)}</b> <span class="small mut">(LCD of 3 and 4 is 12)</span><br>${F(1, 2, 3)} − ${F(2, 3, 1)} = ${F(7, 2)} − ${F(5, 3)} = ${F(21, 6)} − ${F(10, 6)} = ${F(11, 6)} = <b>${F(5, 6, 1)}</b></div>`, 'WORKED EXAMPLE', 'margin:0')])}
${you(2, 'Evaluate. Write answers in simplest form.', grid(5, yt22, 'gap:1.5mm 2.5mm'))}
${sec('2C', 'Multiplying and dividing fractions', 'med')}
${row('1.1fr 1fr', [learn(`<b>×</b> &nbsp;Multiply the tops, multiply the bottoms. Cancel first to keep numbers small.<br><b>÷</b> &nbsp;<b>Keep</b> the first fraction, <b>change</b> ÷ to ×, <b>flip</b> the second.<br>Mixed numerals → improper fractions first. “<b>of</b>” means ×: ${F(2, 3)} of 45 = 45 ÷ 3 × 2 = 30.`, 'margin:0'),
we(`<div class="ln">${F(4, 9)} × ${F(3, 8)} = ${F('<s>4</s>¹', '<s>9</s>₃')} × ${F('<s>3</s>¹', '<s>8</s>₂')} = <b>${F(1, 6)}</b> <span class="small mut">(4 and 8 share 4; 3 and 9 share 3)</span><br>${F(1, 2, 2)} ÷ ${F(3, 4)} = ${F(5, 2)} × ${F(4, 3)} = ${F(20, 6)} = ${F(10, 3)} = <b>${F(1, 3, 3)}</b></div>`, 'WORKED EXAMPLE', 'margin:0')])}
${you(3, 'Evaluate. Write answers in simplest form.', grid(6, yt23, 'gap:1.5mm 2.5mm'))}
`);

// ================================================================= PAGE 5 — decimals
g('Topic 2 · Your turn 4 — Fractions and decimals, rounding (page 5)');
const d2f = (s) => { const dp = s.split('.')[1].length; const f = fr(Math.round(+s * 10 ** dp), 10 ** dp); return [`${F(Math.round(+s * 10 ** dp), 10 ** dp)} = ${FI(f)}`, fImp(f)]; };
const f2d = (n, d) => { const r = recurring(n, d); return [`${n} ÷ ${d} = ${REC(r)}`, RECP(r)]; };
const yt24 = [
  ...['0.8', '0.45', '0.125'].map((s, i) => Q(`2.4${'abc'[i]}`, 'abc'[i], `${s} as a fraction`, d2f(s), { line: '= ', lw: 10 })),
  ...[[3, 5], [7, 20], [5, 6], [4, 9], [3, 11]].map(([n, d], i) => Q(`2.4${'defgh'[i]}`, 'defgh'[i], `${F(n, d)} as a decimal`, f2d(n, d), { line: '= ', lw: 13 })),
  Q('2.4i', 'i', 'Round 5.4271 to 1 decimal place.', [`${rnd(5.4271, 1)} (next digit 2 → round down)`, rnd(5.4271, 1)], { line: '', lw: 13 }),
  Q('2.4j', 'j', 'Round 12.3958 to 2 decimal places.', [`${rnd(12.3958, 2)} (next digit 5 → round up; keep the 0)`, rnd(12.3958, 2)], { line: '', lw: 13 }),
];
g('Topic 2 · Your turn 5 — Multiplying decimals (page 5)');
const dp = (s) => (String(s).split('.')[1] || '').length;
const mulD = (a, b) => { const ia = Math.round(a * 10 ** dp(a)), ib = Math.round(b * 10 ** dp(b)), n = dp(a) + dp(b); return { ia, ib, n, r: (ia * ib) / 10 ** n }; };
const yt25 = [[0.4, 0.3], [0.9, 0.06], [2.5, 0.8], [1.6, 0.45], [3.2, 0.15], [7.5, 0.12]].map(([a, b], i) => {
  const m = mulD(a, b), l = 'abcdef'[i];
  const ans = [`${m.ia} × ${m.ib} = ${m.ia * m.ib}; ${m.n} decimal places → ${dec(m.r)}`, dec(m.r)];
  return i === 0
    ? Q(`2.5${l}`, l, `${a} × ${b}`, ans, { sc: `${H(`${m.ia} × ${m.ib} =`)} ${B(7)}<br>${H('decimal places =')} ${B(5)}<br>${H('answer =')} ${B(9)}` })
    : Q(`2.5${l}`, l, `${a} × ${b}`, ans, { work: 10, line: '= ', lw: 12 });
});
g('Topic 2 · Your turn 6 — Dividing decimals (page 5)');
const divD = (a, b) => { const k = dp(b); const A = +(a * 10 ** k).toFixed(6), Bb = +(b * 10 ** k).toFixed(6); return { k, A, Bb, r: +(A / Bb).toFixed(6) }; };
const yt26 = [[3.6, 0.4], [1.44, 0.12], [8.1, 0.09], [0.56, 0.08], [15, 0.5], [9.45, 0.3]].map(([a, b], i) => {
  const d = divD(a, b), l = 'abcdef'[i];
  const ans = [`× ${10 ** d.k}: ${dec(d.A)} ÷ ${dec(d.Bb)} = ${dec(d.r)}`, dec(d.r)];
  return i === 0
    ? Q(`2.6${l}`, l, `${a} ÷ ${b}`, ans, { sc: `= ${B(7)} ÷ ${B(5)}<br>= ${B(9)}` })
    : Q(`2.6${l}`, l, `${a} ÷ ${b}`, ans, { work: 10, line: '= ', lw: 12 });
});
g('Topic 2 · Your turn 7 — Decimals in real life (page 5)');
const pizzas = 12 * 14.9 + 8 * 4.75, rice = 4.2 / 1.5, change = 50 - (3 * 2.85 + 8.4);
const yt27 = [
  Q('2.7a', 'a', 'A netball club orders 12 pizzas at $14.90 each and 8 garlic breads at $4.75 each. What is the total cost?', [`12 × $14.90 = ${money(12 * 14.9)}; 8 × $4.75 = ${money(8 * 4.75)}; total ${money(pizzas)}`, money(pizzas)], { work: 18 }),
  Q('2.7b', 'b', 'A 1.5 kg bag of rice costs $4.20. What is the cost per kilogram?', [`$4.20 ÷ 1.5 = 42 ÷ 15 = ${money(rice)} per kg`, money(rice)], { work: 18 }),
  Q('2.7c', 'c', 'Ella has $50. She buys 3 drinks at $2.85 each and a sandwich for $8.40. How much change does she get?', [`3 × $2.85 = ${money(3 * 2.85)}; ${money(3 * 2.85)} + $8.40 = ${money(3 * 2.85 + 8.4)}; $50 − ${money(3 * 2.85 + 8.4)} = ${money(change)}`, money(change)], { work: 18 }),
];

const p5 = page(5, 2, 2, `
${sec('2D', 'Fractions ↔ decimals, and rounding', 'easy')}
${row('1fr 1fr', [learn(`<ul class="k"><li><b>Decimal → fraction:</b> use place value, then simplify: 0.35 = ${F(35, 100)} = ${F(7, 20)}</li>
<li><b>Fraction → decimal:</b> divide the top by the bottom: ${F(3, 8)} = 3 ÷ 8 = 0.375 <span class="mut">(it stops: <b>terminating</b>)</span></li>
<li>Some decimals repeat forever (<b>recurring</b>). Dots go over the first and last digits that repeat: ${F(2, 3)} = 0.666… = ${REC(recurring(2, 3))} &nbsp; ${F(5, 11)} = 0.4545… = ${REC(recurring(5, 11))}</li></ul>`, 'margin:0'),
learn(`<b>Rounding</b> to 2 decimal places: look at the <b>3rd</b> decimal place.<br>5 or more → round up. 4 or less → keep the digit.<br>2.73<u>6</u>8 → <b>2.74</b> &nbsp;&nbsp; 2.73<u>2</u>8 → <b>2.73</b><br><span class="small">“Nearest tenth” means 1 decimal place.</span>`, 'margin:0')])}
${you(4, '', grid(5, yt24, 'gap:1.6mm 2.5mm'))}
${sec('2E', 'Multiplying decimals', 'med', 'Q16a')}
${row('1fr 1.1fr', [learn(`<ol style="margin:0;padding-left:4mm"><li>Ignore the decimal points and multiply the whole numbers.</li><li>Count the decimal places in the question (add them up).</li><li>Put that many decimal places in the answer.</li><li>Estimate to check it makes sense.</li></ol>`, 'margin:0'),
we(`<div class="ln">0.6 × 0.07: &nbsp; 6 × 7 = 42; &nbsp;1 + 2 = 3 decimal places → <b>0.042</b><br>2.3 × 1.4: &nbsp; 23 × 14 = 322; &nbsp;2 decimal places → <b>3.22</b> <span class="small mut">(estimate 2 × 1.5 = 3 ✓)</span></div>`, 'WORKED EXAMPLE', 'margin:0')])}
${you(5, '', grid('1.5fr 1fr 1fr 1fr 1fr 1fr', yt25, 'gap:1.5mm 2.5mm'))}
${sec('2F', 'Dividing by a decimal', 'med', 'Q16b')}
${row('1fr 1.1fr', [learn(`Move the decimal point in <b>both</b> numbers the same number of places to the right, until you are dividing by a <b>whole number</b>. (This multiplies both by 10, 100, … so the answer does not change.)`, 'margin:0'),
we(`<div class="ln">4.2 ÷ 0.07 → × 100 → 420 ÷ 7 = <b>60</b><br>2.88 ÷ 0.4 → × 10 → 28.8 ÷ 4 = <b>7.2</b> <span class="small mut">(check: 7.2 × 0.4 = 2.88 ✓)</span></div>`, 'WORKED EXAMPLE', 'margin:0')])}
${you(6, '', grid(6, yt26, 'gap:1.5mm 2.5mm'))}
${sec('2G', 'Decimals in real life', 'hard')}
${you(7, 'Show your working and answer in a sentence.', grid(3, yt27))}
`);

// ================================================================= PAGE 6 — percentages
g('Topic 2 · Your turn 8 — Fractions, decimals and percentages (page 6)');
const fdpRows = [
  { f: fr(1, 4), give: 'f' }, { f: fr(3, 5), give: 'd' }, { f: fr(12, 100), give: 'p' }, { f: fr(7, 8), give: 'f' }, { f: fr(25, 1000), give: 'p' },
];
const fdp = fdpRows.map(({ f, give }, i) => {
  const d = dec(f.val()), p = dec(f.val() * 100) + '%', l = 'abcde'[i];
  L.reg(`2.8${l}`, l, `${FI(f)} = ${d} = ${p}`, `${fImp(f)} = ${d} = ${p}`);
  return `<tr><td><b>${l}</b>&nbsp; ${give === 'f' ? FI(f) : ''}</td><td>${give === 'd' ? d : ''}</td><td>${give === 'p' ? p : ''}</td></tr>`;
});
g('Topic 2 · Your turn 9 — Percentage of a quantity (page 6)');
const pc = (p, q) => +(p / 100 * q).toFixed(6);
const yt29 = [
  Q('2.9a', 'a', '10% of 70', [`70 ÷ 10 = ${dec(pc(10, 70))}`, dec(pc(10, 70))], { inl: '=', lw: 9 }),
  Q('2.9b', 'b', '25% of 36', [`36 ÷ 4 = ${dec(pc(25, 36))}`, dec(pc(25, 36))], { inl: '=', lw: 9 }),
  Q('2.9c', 'c', '40% of 85', [`0.4 × 85 = ${dec(pc(40, 85))}`, dec(pc(40, 85))], { inl: '=', lw: 9 }),
  Q('2.9d', 'd', '12% of $250', [`0.12 × 250 = ${money(pc(12, 250))}`, money(pc(12, 250))], { inl: '=', lw: 9 }),
  Q('2.9e', 'e', `${F(3, 8)} of 64`, [`64 ÷ 8 × 3 = ${dec(fr(3, 8).mul(fr(64)).val())}`, dec(fr(3, 8).mul(fr(64)).val())], { inl: '=', lw: 9 }),
];
const travel = [{ l: 'Bus', p: 35 }, { l: 'Car', p: 30 }, { l: 'Walk', p: 20 }, { l: 'Bike', p: 10 }, { l: 'Other', p: 5 }];
const tot = 160;
const yt29b = [
  Q('2.9f', 'f', 'How many students travel by bus?', [`35% of 160 = 0.35 × 160 = ${dec(pc(35, tot))} students`, dec(pc(35, tot))], { work: 7, line: '', unit: 'students', lw: 10 }),
  Q('2.9g', 'g', 'How many more students walk than ride a bike?', [`Walk 20% of 160 = ${dec(pc(20, tot))}; bike 10% of 160 = ${dec(pc(10, tot))}; ${dec(pc(20, tot))} − ${dec(pc(10, tot))} = ${dec(pc(20, tot) - pc(10, tot))} more`, dec(pc(20, tot) - pc(10, tot))], { work: 7, line: '', unit: 'more students', lw: 10 }),
];
g('Topic 2 · Your turn 10 — One quantity as a percentage of another (page 6)');
const yt210 = [
  Q('2.10a', 'a', 'Chloe scored 34 out of 40 in a quiz. What percentage is this?', [`${F(34, 40)} × 100% = ${dec(34 / 40 * 100)}%`, dec(34 / 40 * 100) + '%'], { sc: `${F(B(8), B(8))} × 100% = ${B(10)}` }),
  Q('2.10b', 'b', 'A netballer had 30 shots at goal and scored 12. What percentage of her shots went in?', [`${F(12, 30)} × 100% = ${dec(12 / 30 * 100)}%`, dec(12 / 30 * 100) + '%'], { work: 6, line: '', lw: 12 }),
  Q('2.10c', 'c', 'What percentage of 2 hours is 30 minutes? <span class="mut">Make the units the same first.</span>', [`2 h = 120 min; ${F(30, 120)} × 100% = ${dec(30 / 120 * 100)}%`, dec(30 / 120 * 100) + '%'], { work: 6, line: '', lw: 12 }),
];
g('Topic 2 · Your turn 11 — Percentage increase and decrease (page 6)');
const yt211 = [
  Q('2.11a', 'a', 'Increase $60 by 10%.', [`10% of 60 = 6; 60 + 6 = ${money(60 * 1.1)}`, money(60 * 1.1)], { sc: `10% of 60 = ${B(7)}<br>60 + ${B(6)} = ${B(10)}` }),
  Q('2.11b', 'b', 'Decrease 250 kg by 20%.', [`20% of 250 = 50; 250 − 50 = ${dec(250 * 0.8)} kg`, dec(250 * 0.8) + ' kg'], { work: 7, line: '', unit: 'kg', lw: 10 }),
  Q('2.11c', 'c', 'A $45 T-shirt is on sale at 30% off. What is the sale price?', [`30% of 45 = 13.50; 45 − 13.50 = ${money(45 * 0.7)}`, money(45 * 0.7)], { work: 7, line: '', lw: 12 }),
  Q('2.11d', 'd', '30% of the students in Year 8 is 54 students. How many students are in Year 8? <span class="mut">Hint: find 1% first.</span>', [`1% = 54 ÷ 30 = 1.8; 100% = 1.8 × 100 = ${dec(54 / 30 * 100)} students`, dec(54 / 30 * 100)], { work: 7, line: '', unit: 'students', lw: 10 }),
];

const p6 = page(6, 2, 3, `
${sec('2H', 'Converting between fractions, decimals and percentages', 'easy')}
${row('1.1fr 1fr', [learn(`<b>Per cent</b> means “out of 100”.<ul class="k" style="margin-top:0.3mm"><li><b>% → fraction:</b> write it over 100, then simplify: 35% = ${F(35, 100)} = ${F(7, 20)}</li><li><b>% → decimal:</b> divide by 100: 35% = 0.35 &nbsp;·&nbsp; 4% = 0.04</li><li><b>Decimal → %:</b> multiply by 100: 0.6 = 60%</li><li><b>Fraction → %:</b> multiply by 100%: ${F(3, 8)} × 100% = 37.5%</li></ul>`, 'margin:0'),
you(8, 'Complete the table.', `<table class="t"><tr><th>Fraction (simplest form)</th><th>Decimal</th><th>Percentage</th></tr>${fdp.join('')}</table>`, 'margin:0')])}
${sec('2I', 'Percentage of a quantity', 'med', 'Q9a')}
${row('1fr 1.1fr', [learn(`“<b>of</b>” means ×. Change the percentage to a decimal and multiply: 15% of 80 = 0.15 × 80 = 12.<br><b>Without a calculator:</b> 10% → ÷ 10 &nbsp;·&nbsp; 5% → half of 10% &nbsp;·&nbsp; 1% → ÷ 100 &nbsp;·&nbsp; 25% → ÷ 4 &nbsp;·&nbsp; 50% → ÷ 2`, 'margin:0'),
we(`<div class="ln">35% of 240: &nbsp;10% = 24, so 30% = 3 × 24 = 72<br>5% = half of 24 = 12, so 35% = 72 + 12 = <b>84</b><br><span class="small mut">Calculator: 0.35 × 240 = 84 ✓</span></div>`, 'WORKED EXAMPLE', 'margin:0')])}
${you(9, '', grid(5, yt29, 'gap:1.5mm 2.5mm') + `<div style="margin-top:1.6mm">${row('auto 1fr', [`<div><div class="yt" style="margin-bottom:0.4mm">${tot} Year 8 students were asked how they travel to school.</div><div class="figc">${pie({ data: travel, r: 11 })}</div></div>`, grid(2, yt29b)], 'gap:4mm')}</div>`)}
${sec('2J', 'One quantity as a percentage of another', 'med')}
${row('1fr 1.1fr', [learn(`Write the amounts as a fraction, <b>part over whole</b>, then multiply by 100%. Make sure both amounts are in the <b>same units</b> first.`, 'margin:0'),
we(`<div class="ln">18 out of 24 = ${F(18, 24)} × 100% = <b>75%</b><br>450 m out of 2 km = ${F(450, 2000)} × 100% = <b>22.5%</b> <span class="small mut">(2 km = 2000 m)</span></div>`, 'WORKED EXAMPLE', 'margin:0')])}
${you(10, '', grid(3, yt210))}
${sec('2K', 'Percentage increase and decrease', 'hard')}
${row('1fr 1.1fr', [learn(`<b>Increase:</b> find the percentage of the amount, then <b>add</b> it on.<br><b>Decrease</b> (or discount): find the percentage, then <b>subtract</b> it.`, 'margin:0'),
we(`<div class="ln">Increase $80 by 15%: 15% of 80 = 12 → 80 + 12 = <b>$92</b><br>$120 shoes, 25% off: 25% of 120 = 30 → 120 − 30 = <b>$90</b></div>`, 'WORKED EXAMPLE', 'margin:0')])}
${you(11, '', grid(4, yt211))}
${check(['fractions', 'F ↔ D ↔ %', '× and ÷ decimals', '% of an amount', '% increase and decrease'])}
`);

// ================================================================= PAGE 7 — algebra: language and substitution
g('Topic 3 · Your turn 1 — The language of algebra (page 7)');
const yt31 = [
  Q('3.1a', 'a', `For ${M('6k - p + 4')}, write: &nbsp;(i) the coefficient of ${M('k')} ${B(8)} &nbsp;(ii) the coefficient of ${M('p')} ${B(8)} &nbsp;(iii) the constant term ${B(8)} &nbsp;(iv) the number of terms ${B(8)}`, ['(i) 6 (ii) −1 (iii) 4 (iv) 3', '6; −1; 4; 3'], { cls: 'span5' }),
  ...[['5 * y', '5y'], ['a * 3 * b', '3ab'], ['m * m', 'm^2'], ['2 * p * p', '2p^2']].map(([q, a], i) => Q(`3.1${'bcde'[i]}`, 'bcde'[i], `${M(q)} =`, [M(a), a.replace('^2', '²')], { inl: '', lw: 10 })),
  Q('3.1f', 'f', `${M('k')} ÷ 6 =`, [F(M('k'), 6), 'k/6'], { inl: '', lw: 10 }),
  Q('3.1g', 'g', `${M('4mn')} =`, [M('4 * m * n'), '4 × m × n'], { inl: '', lw: 22, cls: 'span2' }),
  Q('3.1h', 'h', `${M('3c^2')} =`, [M('3 * c * c'), '3 × c × c'], { inl: '', lw: 22, cls: 'span2' }),
];
g('Topic 3 · Your turn 2 — Words to algebra (page 7)');
const yt32 = [['7 more than <i>n</i>', 'n + 7'], ['the product of 4 and <i>n</i>', '4n'], ['3 less than <i>n</i>', 'n - 3'], ['<i>n</i> divided by 5', null], ['twice <i>n</i>, then add 1', '2n + 1'], ['the next whole number after <i>n</i>', 'n + 1'], ['the sum of <i>x</i> and <i>y</i>, all multiplied by 3', '3(x + y)']]
  .map(([q, a], i) => Q(`3.2${'abcdefg'[i]}`, 'abcdefg'[i], q.replace(/<i>(\w)<\/i>/g, (_, c) => M(c)), a ? [M(a), a.replace('-', '−')] : [F(M('n'), 5), 'n/5'], { line: '', lw: 20, cls: i === 6 ? 'span2' : '' }));
g('Topic 3 · Your turn 3 — Substitution (page 7)');
const X = 5, Y = 2, Z = -3;
const sub = [
  ['a', '3x + y', 3 * X + Y, `3 × (5) + (2) = 15 + 2 = ${3 * X + Y}`, `${H('3 × (5) + (2)')}<br>= ${B(6)} + ${B(6)} = ${B(8)}`],
  ['b', 'xy - 4', X * Y - 4, `(5) × (2) − 4 = 10 − 4 = ${X * Y - 4}`, `= (5) × (${B(5)}) − 4<br>= ${B(8)}`],
  ['c', 'x^2 + y^2', X ** 2 + Y ** 2, `(5)² + (2)² = 25 + 4 = ${X ** 2 + Y ** 2}`],
  ['d', '2y^2', 2 * Y ** 2, `2 × (2)² = 2 × 4 = ${2 * Y ** 2} (square first)`, `${H('2 × (2)²')}<br>= 2 × ${B(6)} = ${B(8)}`],
  ['e', '3x^2 - 4y', 3 * X ** 2 - 4 * Y, `3 × 25 − 4 × 2 = 75 − 8 = ${3 * X ** 2 - 4 * Y}`],
  ['f', 'x + z', X + Z, `(5) + (−3) = ${X + Z}`],
  ['g', 'z^2', Z ** 2, `(−3)² = (−3) × (−3) = ${Z ** 2}`],
  ['h', '4z - y', 4 * Z - Y, `4 × (−3) − (2) = −12 − 2 = ${dec(4 * Z - Y)}`],
  ['i', '(x + y)^2', (X + Y) ** 2, `(5 + 2)² = 7² = ${(X + Y) ** 2}`],
];
const yt33 = sub.map(([l, e, v, h, sc]) => Q(`3.3${l}`, l, M(e), [h, dec(v)], sc ? { sc } : { work: 11, line: '= ', lw: 10 }));
const C = (h) => 45 * h + 60;
yt33.push(Q('3.3j', 'j', `An electrician charges ${M('C = 45h + 60')} dollars for a job that takes ${M('h')} hours. Find ${M('C')} when (i) ${M('h = 3')} &nbsp;(ii) ${M('h = 2.5')}`, [`(i) 45 × 3 + 60 = ${money(C(3))} (ii) 45 × 2.5 + 60 = ${money(C(2.5))}`, `${money(C(3))}; ${money(C(2.5))}`], { work: 13, cls: 'span5' }));

const p7 = page(7, 3, 1, `
${band(3, 'Algebraic techniques', 'NSW syllabus: <b>MA4-ALG-C-01</b> generalises number properties to operate with algebraic expressions including expansion and factorisation · <b>MAO-WM-01</b> working mathematically', 'Yearly exam<br>Section C · Q19')}
${sec('3A', 'The language of algebra', 'easy')}
${row('1.1fr 1fr', [learn(`<div class="big2" style="margin-bottom:0.6mm">${M('5x - 3y + 7')}</div><ul class="k"><li>${M('x')} and ${M('y')} are <b>pronumerals</b>: letters that stand for numbers.</li><li>There are 3 <b>terms</b>: ${M('5x')}, ${M('-3y')} and 7. The sign in front belongs to the term.</li><li>5 is the <b>coefficient</b> of ${M('x')} (the number in front). The coefficient of ${M('y')} is −3.</li><li>7 is the <b>constant term</b> (a number on its own).</li></ul>`, 'margin:0'),
learn(`<b>How we write algebra</b><br>${M('3 * a')} = ${M('3a')} &nbsp;·&nbsp; ${M('a * b')} = ${M('ab')} &nbsp;·&nbsp; ${M('b * a')} = ${M('ab')} <span class="small mut">(alphabetical)</span><br>${M('a * a')} = ${M('a^2')} &nbsp;·&nbsp; ${M('1 * x')} = ${M('x')} &nbsp;·&nbsp; ${M('a')} ÷ 4 = ${F(M('a'), 4)}<br><b>Expanded form</b> shows every ×: ${M('5ab')} = ${M('5 * a * b')}`, 'margin:0')])}
${you(1, '', grid(5, yt31.slice(0, 1), 'margin-bottom:1.6mm') + '<div class="yt" style="font-weight:400"><b>Write simply</b> (b–f), then <b>write in expanded form</b> (g–h).</div>' + grid(5, yt31.slice(1), 'gap:1.6mm 3mm'))}
${sec('3B', 'Turning words into algebra', 'easyc')}
${row('1fr 1.5fr', [learn(`<table style="border-collapse:collapse;font-size:8pt"><tr><td style="padding:0.3mm 2mm 0.3mm 0"><b>+</b></td><td>sum, more than, increased by, plus</td></tr><tr><td><b>−</b></td><td>difference, less than, decreased by</td></tr><tr><td><b>×</b></td><td>product, times, twice (× 2), double</td></tr><tr><td><b>÷</b></td><td>quotient, divided by, shared, half (÷ 2)</td></tr></table><div class="small" style="margin-top:0.6mm">Careful: “3 less than ${M('n')}” is ${M('n - 3')}, not ${M('3 - n')}.</div>`, 'margin:0'),
you(2, 'Write an expression for each. Use the pronumerals given.', grid(2, yt32, 'gap:1.3mm 3mm'), 'margin:0')])}
${sec('3C', 'Substitution', 'med', 'Q19c')}
${row('1fr 1.1fr', [learn(`Replace each pronumeral with its number <b>in brackets</b>, then use the order of operations:<br><b>brackets → powers → × and ÷ → + and −</b><br>${M('3a^2')} means ${M('3 * a^2')}: square first, then multiply. It is <b>not</b> ${M('(3a)^2')}.`, 'margin:0'),
we(`<div class="ln">When ${M('a = 4')} and ${M('b = -2')}:<br>${M('5a - 3')} = 5 × (4) − 3 = 20 − 3 = <b>17</b><br>${M('3a^2 + b')} = 3 × (4)² + (−2) = 3 × 16 − 2 = 48 − 2 = <b>46</b><br>${M('b^2')} = (−2)² = (−2) × (−2) = <b>4</b></div>`, 'WORKED EXAMPLE', 'margin:0')])}
${you(3, `Evaluate each expression when ${M('x = 5')}, ${M('y = 2')} and ${M('z = -3')}.`, grid(5, yt33, 'gap:1.6mm 2.5mm'))}
`);

// ================================================================= PAGE 8 — like terms, × and ÷ terms
g('Topic 3 · Your turn 4 — Collecting like terms (page 8)');
const yt34 = [
  ['a', '6a + 2a', '8a'], ['b', '9k - k', '8k'], ['c', '3p + 4 + 2p', '5p + 4'], ['d', '5x + 3y + 2x - y', '7x + 2y'],
  ['e', '8p - 3q - 5p + 6q', '3p + 3q'], ['f', '3ab + 2ba - ab', '4ab'], ['g'],
  ['h', '6y^2 - 2y + y^2 + 5y', '7y^2 + 3y'], ['i', '2m - 7 - 5m + 4', '-3m - 3'], ['j'],
].map(([l, q, a]) => {
  if (l === 'g') return Q('3.4g', 'g', `Circle the terms that are like ${M('5x')}: &nbsp; ${['2y', '-x', 'x^2', '7x', '5'].map(M).join(' &nbsp;&nbsp; ')}`, [`${M('-x')} and ${M('7x')}`, '−x, 7x'], { cls: 'span2' });
  if (l === 'j') return Q('3.4j', 'j', `Simplify the perimeter, ${M('P')}, of this rectangle. <span class="mut">(not to scale)</span>`, [`${M('(3x + 2) + x + (3x + 2) + x')} = ${M('8x + 4')}`, '8x + 4'], { fig: `<div style="display:flex;align-items:center;gap:6mm">${rectAlg({ lL: '3_x_ + 2', lW: '_x_', w: 26, h: 8 })}<span>${M('P')} = ${B(24)}</span></div>`, cls: 'span2' });
  return Q(`3.4${l}`, l, M(q), [M(a), a.replace(/\^2/g, '²').replace(/-/g, '−')], l === 'a' ? { sc: `= (${B(4)} + ${B(4)})${M('a')} = ${B(9)}` } : { line: '= ', lw: 15 });
});
g('Topic 3 · Your turn 5 — Multiplying terms (page 8)');
const yt35 = [['a', '5 * 3k', '15k'], ['b', '2p * 7q', '14pq'], ['c', '4y * 3y', '12y^2'], ['d', '-2a * 6b', '-12ab'], ['e', '3m * 2n * 5', '30mn'], ['f', '-4x * (-3x)', '12x^2']]
  .map(([l, q, a]) => Q(`3.5${l}`, l, M(q), [M(a), a.replace(/\^2/g, '²').replace(/-/g, '−')], l === 'a' ? { sc: `= ${B(5)} × ${B(5)} × ${M('k')}<br>= ${B(10)}` } : { line: '= ', lw: 13 }));
g('Topic 3 · Your turn 6 — Dividing terms (page 8)');
const yt36 = [['a', '18m', '6', '3m'], ['b', '15xy', '5y', '3x'], ['c', '24ab', '8a', '3b'], ['d', '14k^2', '7k', '2k'], ['e', '30mn', '-6n', '-5m']]
  .map(([l, n, d, a]) => Q(`3.6${l}`, l, l === 'a' || l === 'b' ? `${M(n)} ÷ ${M(d)}` : F(M(n), M(d)), [M(a), a.replace(/-/g, '−')], l === 'a' ? { sc: `= ${F(M('18m'), 6)} = ${B(10)}` } : { line: '= ', lw: 12 }));

g('Topic 3 · Your turn 7 — Reasoning with algebra (page 8)');
const yt37r = [
  Q('3.7a', 'a', `Sam says ${M('3x + 2y = 5xy')}. Test this with ${M('x = 2')} and ${M('y = 1')}. Then explain Sam’s mistake.`, [`${M('3x + 2y')} = 6 + 2 = ${3 * 2 + 2 * 1}, but ${M('5xy')} = 5 × 2 × 1 = ${5 * 2 * 1}. ${3 * 2 + 2 * 1} ≠ ${5 * 2 * 1}, so Sam is wrong: ${M('3x')} and ${M('2y')} are not like terms, so they cannot be added.`, 'no'], { work: 15, cls: 'span2' }),
  Q('3.7b', 'b', `Find the missing term: ${M('7m')} − ${B(9)} = ${M('3m')}`, [M('4m'), '4m'], {}),
  Q('3.7c', 'c', `Find the missing term: ${M('6ab')} ÷ ${B(9)} = ${M('2b')}`, [M('3a'), '3a'], {}),
  Q('3.7d', 'd', `Simplify the area of a rectangle ${M('5x')} long and ${M('3x')} wide:`, [`${M('5x * 3x')} = ${M('15x^2')}`, '15x²'], { inl: 'Area =', lw: 16, cls: 'span2' }),
  Q('3.7e', 'e', `Is ${M('4a^2')} the same as ${M('(4a)^2')}? Test with ${M('a = 3')}.`, [`${M('4a^2')} = 4 × 9 = ${4 * 9}; ${M('(4a)^2')} = 12² = ${12 ** 2}. Not the same: in ${M('4a^2')} only ${M('a')} is squared.`, 'no'], { work: 10, cls: 'span2' }),
];

const p8 = page(8, 3, 2, `
${sec('3D', 'Collecting like terms', 'easy', 'Q19a')}
${row('1fr 1.1fr', [learn(`<b>Like terms</b> have exactly the same pronumerals, with the same powers.<br><span class="ok">Like:</span> ${M('3x')} and ${M('-5x')} &nbsp;·&nbsp; ${M('4ab')} and ${M('2ba')} <span class="small mut">(ab = ba)</span><br><span class="no">Not like:</span> ${M('2x')} and ${M('2x^2')} &nbsp;·&nbsp; ${M('3x')} and ${M('3y')}<br>To simplify, <b>add or subtract the coefficients</b> of like terms. Keep the pronumeral the same. The sign <b>in front</b> of a term moves with it.`, 'margin:0'),
we(`<div class="ln">${M('7m + 3n - 2m + n')}<br>= ${M('7m - 2m + 3n + n')} <span class="small mut">← group like terms</span><br>= <b>${M('5m + 4n')}</b> <span class="small mut">(${M('n')} means ${M('1n')})</span><br>${M('4x^2 + 3x - x^2 + 5x')} = <b>${M('3x^2 + 8x')}</b><br>${M('2k - 7 - 5k + 4')} = <b>${M('-3k - 3')}</b></div>`, 'WORKED EXAMPLE', 'margin:0')])}
${you(4, 'Simplify by collecting like terms.', grid(4, yt34, 'gap:2mm 3mm'))}
${sec('3E', 'Multiplying terms', 'med')}
${row('1fr 1.1fr', [learn(`Multiply the <b>numbers</b>, then the <b>pronumerals</b> (in alphabetical order). The same letter twice is squared.<br><b>Signs:</b> + × + = + &nbsp;·&nbsp; + × − = − &nbsp;·&nbsp; − × − = +`, 'margin:0'),
we(`<div class="ln">${M('3a * 4b')} = 3 × 4 × ${M('a * b')} = <b>${M('12ab')}</b> &nbsp;&nbsp; ${M('2x * 5x')} = <b>${M('10x^2')}</b><br>${M('-3m * 4n')} = <b>${M('-12mn')}</b> &nbsp;&nbsp; ${M('-2p * (-6q)')} = <b>${M('12pq')}</b></div>`, 'WORKED EXAMPLE', 'margin:0')])}
${you(5, 'Simplify.', grid(6, yt35, 'gap:1.5mm 2.5mm'))}
${sec('3F', 'Dividing terms', 'med')}
${row('1fr 1.1fr', [learn(`Write the division as a <b>fraction</b>. Then cancel factors that are on the top <b>and</b> the bottom: numbers first, then pronumerals.`, 'margin:0'),
we(`<div class="ln">${M('12xy')} ÷ ${M('4x')} = ${F(M('12xy'), M('4x'))} = <b>${M('3y')}</b> <span class="small mut">(12 ÷ 4 = 3 and ${M('x')} ÷ ${M('x')} = 1)</span><br>${F(M('20a^2'), M('5a'))} = ${F('20 × ' + M('a * a'), '5 × ' + M('a'))} = <b>${M('4a')}</b></div>`, 'WORKED EXAMPLE', 'margin:0')])}
${you(6, 'Simplify.', grid(5, yt36, 'gap:1.5mm 2.5mm'))}
${sec('3G', 'Reasoning with algebra', 'hard')}
${you(7, 'To test whether two expressions are equal, substitute the same numbers into both. <span style="font-weight:400">If the answers differ even once, they are not equal. Explain using words such as <i>like terms</i> and <i>square first</i>.</span>', grid(4, yt37r, 'gap:1.6mm 4mm'))}
`);

// ================================================================= PAGE 9 — expanding, factorising, mixed exam check
g('Topic 3 · Your turn 8 — Expanding brackets (page 9)');
const yt37 = [['a', '6(m + 2)', '6m + 12'], ['b', '3(4k - 5)', '12k - 15'], ['c', '-2(y + 8)', '-2y - 16'], ['d', 'a(a - 9)', 'a^2 - 9a'], ['e', '4(2x + 1) + 3', '8x + 7'], ['f', '5(p + 2) + 2(p - 3)', '7p + 4']]
  .map(([l, q, a]) => Q(`3.8${l}`, l, M(q), [M(a) + (l === 'e' ? ` <span class="mut">(${M('8x + 4 + 3')})</span>` : l === 'f' ? ` <span class="mut">(${M('5p + 10 + 2p - 6')})</span>` : ''), a.replace(/\^2/g, '²').replace(/-/g, '−')],
    l === 'a' ? { sc: `= 6 × ${M('m')} + 6 × 2<br>= ${B(14)}` } : l === 'b' ? { sc: `= ${B(5)} − ${B(5)}` } : { work: l > 'd' ? 11 : 0, line: '= ', lw: 15 }));
g('Topic 3 · Your turn 9 — Factorising (page 9)');
const yt38 = [['a', '4x + 8', '4(x + 2)'], ['b', '9m - 6', '3(3m - 2)'], ['c', '12y + 18', '6(2y + 3)'], ['d', 'k^2 - 7k', 'k(k - 7)'], ['e', '14pq + 21p', '7p(2q + 3)']]
  .map(([l, q, a]) => Q(`3.9${l}`, l, M(q), [M(a), a.replace(/\^2/g, '²').replace(/-/g, '−')], l === 'a' ? { sc: `HCF = ${B(5)}<br>= ${B(5)}(${B(5)} + ${B(5)})` } : { line: '= ', lw: 17 }));
g('Mixed exam check — all three topics (page 9)');
const mix = [
  Q('3.10a', '1', `Simplify ${M('9a + 2b - 4a - 6b')} =`, [M('5a - 4b'), '5a − 4b'], { marks: '1 mark', inl: '', lw: 22 }),
  Q('3.10b', '2', `Expand ${M('4(3m - 2)')} =`, [M('12m - 8'), '12m − 8'], { marks: '1 mark', inl: '', lw: 22 }),
  Q('3.10c', '3', `Evaluate ${M('3p^2 - 2q')} when ${M('p = 2')} and ${M('q = -5')}.`, [`3 × (2)² − 2 × (−5) = 12 + 10 = ${3 * 2 ** 2 - 2 * -5}`, `${3 * 2 ** 2 - 2 * -5}`], { marks: '1 mark', work: 11, line: '', lw: 14 }),
  Q('3.10d', '4', 'Find the hypotenuse of a right-angled triangle with shorter sides 16 cm and 30 cm.', hypA(16, 30, 'cm'), { marks: '2 marks', work: 11, line: '', unit: 'cm', lw: 12 }),
  Q('3.10e', '5', 'Calculate 0.7 × 0.08 =', [`7 × 8 = 56; 3 decimal places → ${dec(mulD(0.7, 0.08).r)}`, dec(mulD(0.7, 0.08).r)], { marks: '1 mark', inl: '', lw: 18 }),
  Q('3.10f', '6', 'Calculate 2.4 ÷ 0.03 =', [`× 100: 240 ÷ 3 = ${dec(divD(2.4, 0.03).r)}`, dec(divD(2.4, 0.03).r)], { marks: '1 mark', inl: '', lw: 18 }),
  Q('3.10g', '7', 'A sector graph shows that 45% of 360 students play sport. How many students is that?', [`0.45 × 360 = ${dec(pc(45, 360))}`, dec(pc(45, 360))], { marks: '1 mark', work: 11, line: '', unit: 'students', lw: 12 }),
  Q('3.10h', '8', `Evaluate ${F(1, 2, 2)} + ${F(3, 4)}`, [`${F(5, 2)} + ${F(3, 4)} = ${F(10, 4)} + ${F(3, 4)} = ${F(13, 4)} = ${FH(mx(2, 1, 2).add(fr(3, 4)))}`, fPlain(mx(2, 1, 2).add(fr(3, 4)))], { marks: '1 mark', work: 11, line: '', lw: 14 }),
  Q('3.10i', '9', 'Is a triangle with sides 7 cm, 9 cm and 12 cm right-angled? Show working.', [converse(7, 9, 12).h, converse(7, 9, 12).p], { marks: '2 marks', work: 15 }),
  Q('3.10j', '10', 'Increase $150 by 8%.', [`8% of 150 = ${dec(pc(8, 150))}; 150 + ${dec(pc(8, 150))} = ${money(150 + pc(8, 150))}`, money(150 + pc(8, 150))], { marks: '1 mark', work: 11, line: '', lw: 14 }),
];

const p9 = page(9, 3, 3, `
${sec('3H', 'Expanding brackets (the distributive law)', 'med', 'Q19b')}
${row('1fr 1.1fr', [learn(row('1fr auto', [`Multiply the term outside by <b>every</b> term inside:<div class="big2" style="margin:0.6mm 0"><b>${M('a(b + c) = ab + ac')}</b></div>A negative outside changes the sign of <b>every</b> term inside.`, `<div class="figc">${areaModel({ out: '4', p1: '_x_', p2: '3', a1: '4_x_', a2: '12', w: 34, h: 11 })}</div><div class="small mut" style="text-align:center">${M('4(x + 3) = 4x + 12')} (not to scale)</div>`]), 'margin:0'),
we(`<div class="ln">${M('5(2y - 3)')} = 5 × ${M('2y')} − 5 × 3 = <b>${M('10y - 15')}</b><br>${M('-3(a + 4)')} = <b>${M('-3a - 12')}</b> &nbsp;&nbsp; ${M('x(x + 7)')} = <b>${M('x^2 + 7x')}</b><br>Expand, then simplify: ${M('2(x + 5) + 3x')} = ${M('2x + 10 + 3x')} = <b>${M('5x + 10')}</b></div>`, 'WORKED EXAMPLE', 'margin:0')])}
${you(8, 'Expand. Simplify where you can.', grid('1fr 1fr 1fr 1fr 1.25fr 1.5fr', yt37, 'gap:1.5mm 2.5mm'))}
${sec('3I', 'Factorising', 'hard')}
${row('1fr 1.1fr', [learn(`Factorising is the <b>reverse</b> of expanding.<ol style="margin:0.3mm 0 0;padding-left:4mm"><li>Find the <b>HCF</b> of all the terms (number and pronumeral).</li><li>Write the HCF outside the brackets.</li><li>Divide each term by the HCF. Write what is left inside.</li><li>Check by expanding.</li></ol>`, 'margin:0'),
we(`<div class="ln">${M('6x + 15')}: HCF = 3 → <b>${M('3(2x + 5)')}</b> <span class="small mut">check: ${M('3 * 2x + 3 * 5')} ✓</span><br>${M('8a - 12')} = <b>${M('4(2a - 3)')}</b> &nbsp;&nbsp; ${M('x^2 + 5x')} = <b>${M('x(x + 5)')}</b><br>${M('10ab + 15a')}: HCF = ${M('5a')} → <b>${M('5a(2b + 3)')}</b></div>`, 'WORKED EXAMPLE', 'margin:0')])}
${you(9, 'Factorise fully.', grid(5, yt38, 'gap:1.5mm 2.5mm'))}
<div class="sec" style="--acc:#3a3f44"><span class="code">MIX</span><span class="st">Mixed exam check: all three topics <span style="font-weight:400;font-size:8pt;color:#5b6168">· 12 marks · about 12 minutes</span></span>${L.chip('lv', 'CHALLENGING · core, exam style')}${L.chip('ex', 'EXAM SECTION C')}</div>
${you('★', 'Try these without looking back. Then check, and revise any you got wrong.', grid(2, mix, 'gap:2.2mm 6mm'))}
${check(['substitute', 'like terms', '× and ÷ terms', 'expand', 'factorise'])}
`);

// ================================================================= answer booklet
const groups = [];
ANS.forEach((a) => { let gp = groups.find((x) => x.name === a.group); if (!gp) { gp = { name: a.group, items: [] }; groups.push(gp); } gp.items.push(a); });
const plainLen = (h) => h.replace(/<[^>]+>/g, '').length;
const cols = (gp) => { if (gp.name.startsWith('Mixed')) return 'w2'; const m = Math.max(...gp.items.map((a) => plainLen(a.h))); return m > 70 ? 'w1' : m > 30 ? 'w2' : ''; };
const topicOf = (name) => (name.startsWith('Topic 1') ? 't1' : name.startsWith('Topic 2') ? 't2' : name.startsWith('Topic 3') ? 't3' : 'ta');
const ansHtml = groups.map((gp) => `<div class="grp ${topicOf(gp.name)}"><h3>${gp.name}</h3><div class="ag ${cols(gp)}">${gp.items.map((a) => `<div class="a"><b>${a.label}</b>&nbsp; ${a.h}</div>`).join('')}</div></div>`).join('');

const css = fs.readFileSync(path.join(__dirname, 'style.css'), 'utf8');
const doc = (title, body) => `<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><title>${title}</title><style>${css}</style></head><body>${body}</body></html>`;
const booklet = doc('Year 8 catch-up revision booklet', [p1, p2, p3, p4, p5, p6, p7, p8, p9].join('\n'));
const answers = doc('Year 8 catch-up revision booklet – answers', `<style>@page { size: A4; margin: 9mm 11mm 13mm; }</style><div class="ans ta">
<div class="hd"><span>Kingscliff High School · Year 8 Mathematics · Catch-up revision booklet</span><span><b>Answers and working</b></span></div>
<div class="title" style="margin-bottom:1mm"><div><div class="big" style="font-size:15pt">Answers and working</div><div class="sub">Mark your work, then fix each mistake in a different colour. Rounded answers are to 1 decimal place unless the question says otherwise.</div></div></div>
${ansHtml}</div>`);

(async () => {
  fs.writeFileSync(path.join(__dirname, 'booklet.html'), booklet);
  fs.writeFileSync(path.join(__dirname, 'answers.html'), answers);
  fs.writeFileSync(path.join(__dirname, 'answers.json'), JSON.stringify(ANS.map(({ group: gname, key, p }) => ({ group: gname, key, p })), null, 1));
  const browser = await chromium.launch();
  const pg = await browser.newPage();
  // layout check: anything spilling out of a page?
  await pg.goto('file://' + path.join(__dirname, 'booklet.html'));
  await pg.evaluate(() => document.fonts.ready);
  const over = await pg.evaluate(() => [...document.querySelectorAll('.page')].map((p, i) => {
    const inner = p.querySelector('.inner'); const ft = p.querySelector('.ft').getBoundingClientRect();
    const kids = [...inner.children]; const last = kids.length ? kids[kids.length - 1].getBoundingClientRect().bottom : 0;
    return { page: i + 1, spare_mm: +((ft.top - last) / 3.7795).toFixed(1), overflow: inner.scrollHeight > inner.clientHeight + 1 };
  }));
  console.table(over);
  const wideItems = await pg.evaluate(() => [...document.querySelectorAll('.it, .g > *')].filter((e) => e.scrollWidth > e.clientWidth + 2).length);
  console.log('items wider than their cell:', wideItems);
  await pg.pdf({ path: path.join(OUT, BASE + '.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true });
  await pg.goto('file://' + path.join(__dirname, 'answers.html'));
  await pg.evaluate(() => document.fonts.ready);
  await pg.pdf({ path: path.join(OUT, BASE + '_Answers.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true, displayHeaderFooter: true, headerTemplate: '<span></span>', footerTemplate: '<div style="font-size:7px;width:100%;text-align:center;color:#888;font-family:sans-serif">Answers · page <span class="pageNumber"></span> of <span class="totalPages"></span></div>' });
  await browser.close();
  console.log('answers registered:', ANS.length);
})();
