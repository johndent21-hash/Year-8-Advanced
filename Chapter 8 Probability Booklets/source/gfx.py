"""SVG graphics for the Year 8 Probability booklets.

Every function returns an inline <svg> string. Sizes are in mm so that the
graphics print at a predictable size. Colours are taken from the Kingscliff
statistical-investigation booklet palette plus clear, nameable colours for
probability objects. Each coloured region also carries a letter so the
graphics still work when the booklet is photocopied in black and white.
"""
import math

INK = '#3d3d3d'
BLUE = '#3f7cc0'
MAROON = '#7a1f4e'
SAND = '#c8c2a8'
COL = dict(red='#d9534f', blue='#4f7fd0', green='#5da867', yellow='#f2c94c',
           white='#ffffff', black='#3d3d3d', purple='#8e63b8', orange='#ee9a3a',
           pink='#efa3bf', grey='#b9b9b9', brown='#9a6b4f')
LET = dict(red='R', blue='B', green='G', yellow='Y', white='W', black='K',
           purple='P', orange='O', pink='Pk', grey='', brown='Br')
DARK = {'red', 'blue', 'green', 'black', 'purple', 'brown'}
SANS = "Poppins, sans-serif"
SERIF = "PagellaTT, 'TeX Gyre Pagella', serif"
SYM = "'DejaVu Sans', sans-serif"


def _svg(w_mm, h_mm, vw, vh, body, extra=''):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" class="g" width="{w_mm:.2f}mm" '
            f'height="{h_mm:.2f}mm" viewBox="0 0 {vw} {vh}" {extra}>{body}</svg>')


def _txt(x, y, s, size=10, fill=INK, weight=400, anchor='middle', family=SANS, extra=''):
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" text-anchor="{anchor}" dominant-baseline="central" '
            f'font-family="{family}" {extra}>{s}</text>')


# ---------------------------------------------------------------- spinner
def spinner(sectors, size=22, letters=True, pointer=40, start=-90, show_pointer=True,
            text_size=None):
    """sectors: list of (colour, weight, label or None).
    Label None -> colour letter (if letters) ; a string -> that text."""
    R, c = 46, 50
    total = sum(s[1] for s in sectors)
    a = start
    body = []
    for col, w, lab in sectors:
        da = 360 * w / total
        fill = COL.get(col, col)
        if da >= 359.99:
            body.append(f'<circle cx="{c}" cy="{c}" r="{R}" fill="{fill}" stroke="{INK}" stroke-width="1.6"/>')
        else:
            x1, y1 = c + R * math.cos(math.radians(a)), c + R * math.sin(math.radians(a))
            x2, y2 = c + R * math.cos(math.radians(a + da)), c + R * math.sin(math.radians(a + da))
            large = 1 if da > 180 else 0
            body.append(f'<path d="M{c},{c} L{x1:.2f},{y1:.2f} A{R},{R} 0 {large} 1 {x2:.2f},{y2:.2f} Z" '
                        f'fill="{fill}" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"/>')
        mid = math.radians(a + da / 2)
        rr = R * (0.68 if da < 100 else 0.6)
        if lab is None and letters:
            lab = LET.get(col, '')
        if lab:
            tcol = '#ffffff' if col in DARK else INK
            ts = text_size or (15 if len(sectors) <= 6 else 12)
            body.append(_txt(c + rr * math.cos(mid), c + rr * math.sin(mid), lab, ts, tcol, 600))
        a += da
    if show_pointer:
        p = math.radians(pointer)
        tipx, tipy = c + 25 * math.cos(p), c + 25 * math.sin(p)
        bx, by = c - 8 * math.cos(p), c - 8 * math.sin(p)
        nx, ny = -math.sin(p), math.cos(p)
        body.append(f'<polygon points="{tipx:.2f},{tipy:.2f} {c + 5*nx:.2f},{c + 5*ny:.2f} {bx:.2f},{by:.2f} '
                    f'{c - 5*nx:.2f},{c - 5*ny:.2f}" fill="{INK}"/>')
        body.append(f'<circle cx="{c}" cy="{c}" r="3.5" fill="#fff" stroke="{INK}" stroke-width="1.5"/>')
    return _svg(size, size, 100, 100, ''.join(body))


# ---------------------------------------------------------------- dice
PIPS = {1: [(50, 50)], 2: [(28, 28), (72, 72)], 3: [(28, 28), (50, 50), (72, 72)],
        4: [(28, 28), (72, 28), (28, 72), (72, 72)],
        5: [(28, 28), (72, 28), (50, 50), (28, 72), (72, 72)],
        6: [(28, 26), (72, 26), (28, 50), (72, 50), (28, 74), (72, 74)]}


def die(n=5, size=11, fill='#ffffff', pip=INK):
    body = [f'<rect x="5" y="5" width="90" height="90" rx="16" fill="{fill}" stroke="{INK}" stroke-width="4"/>']
    for x, y in PIPS[n]:
        body.append(f'<circle cx="{x}" cy="{y}" r="8.5" fill="{pip}"/>')
    return _svg(size, size, 100, 100, ''.join(body))


def die3d(size=16, top=1, front=5, right=3):
    """A cube drawn in perspective with three visible faces."""
    def face(pts, n, fpts):
        s = f'<polygon points="{pts}" fill="#fff" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"/>'
        for (u, v) in PIPS[n]:
            x, y = fpts(u / 100, v / 100)
            s += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.3" fill="{INK}"/>'
        return s
    # front square (10,35)-(65,90); top parallelogram; right parallelogram
    fr = face('10,35 65,35 65,90 10,90', front, lambda u, v: (10 + 55 * u, 35 + 55 * v))
    tp = face('10,35 35,12 90,12 65,35', top, lambda u, v: (10 + 25 * (1 - v) + 55 * u, 35 - 23 * (1 - v)))
    rt = face('65,35 90,12 90,67 65,90', right, lambda u, v: (65 + 25 * u, 35 - 23 * u + 55 * v))
    return _svg(size, size, 100, 100, fr + tp + rt)


def poly_die(sides=8, n=3, size=13):
    """An octahedral / other polyhedral die drawn as a gem shape with a number."""
    if sides == 8:
        body = (f'<polygon points="50,4 94,50 50,96 6,50" fill="#fff" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>'
                f'<polyline points="6,50 50,62 94,50" fill="none" stroke="{INK}" stroke-width="2"/>'
                f'<line x1="50" y1="62" x2="50" y2="96" stroke="{INK}" stroke-width="2"/>')
        body += _txt(50, 38, str(n), 26, INK, 600)
    elif sides == 4:
        body = (f'<polygon points="50,6 95,88 5,88" fill="#fff" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>')
        body += _txt(50, 62, str(n), 26, INK, 600)
    else:  # 12 or 20: pentagon-ish
        pts = ' '.join(f'{50 + 45 * math.cos(math.radians(-90 + 72 * k)):.1f},{52 + 45 * math.sin(math.radians(-90 + 72 * k)):.1f}' for k in range(5))
        body = f'<polygon points="{pts}" fill="#fff" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>'
        body += _txt(50, 54, str(n), 26, INK, 600)
    return _svg(size, size, 100, 100, body)


# ---------------------------------------------------------------- coins
def coin(face='H', size=11, metal='gold'):
    fill = {'gold': '#e8c766', 'silver': '#d5d9de'}[metal]
    edge = {'gold': '#a8862c', 'silver': '#8b9199'}[metal]
    body = (f'<circle cx="50" cy="50" r="45" fill="{fill}" stroke="{edge}" stroke-width="4"/>'
            f'<circle cx="50" cy="50" r="36" fill="none" stroke="{edge}" stroke-width="2" stroke-dasharray="3 3"/>')
    body += _txt(50, 52, face, 34 if len(face) == 1 else 22, INK, 600)
    return _svg(size, size, 100, 100, body)


def aus_coin(value='$1', size=10):
    if value in ('$1', '$2'):
        fill, edge = '#e8c766', '#a8862c'
    else:
        fill, edge = '#d5d9de', '#8b9199'
    if value == '50c':
        pts = ' '.join(f'{50 + 46 * math.cos(math.radians(15 + 30 * k)):.1f},{50 + 46 * math.sin(math.radians(15 + 30 * k)):.1f}' for k in range(12))
        shape = f'<polygon points="{pts}" fill="{fill}" stroke="{edge}" stroke-width="4"/>'
    else:
        r = {'$2': 34, '$1': 45, '20c': 44, '10c': 36, '5c': 30}[value]
        shape = f'<circle cx="50" cy="50" r="{r}" fill="{fill}" stroke="{edge}" stroke-width="4"/>'
    return _svg(size, size, 100, 100, shape + _txt(50, 52, value, 24 if len(value) < 3 else 21, INK, 600))


# ---------------------------------------------------------------- cards
SUIT = {'H': ('♥', '#c8372d'), 'D': ('♦', '#c8372d'), 'C': ('♣', INK), 'S': ('♠', INK)}


def _card(x, y, rank, suit, w=56, h=80, rot=0):
    sym, col = SUIT[suit]
    g = f'<g transform="rotate({rot} {x + w / 2} {y + h})">'
    g += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#fff" stroke="{INK}" stroke-width="2"/>'
    g += _txt(x + 9, y + 11, rank, 13, col, 600)
    g += _txt(x + 9, y + 25, sym, 12, col, 400, family=SYM)
    g += _txt(x + w / 2, y + h / 2 + 6, sym, 30, col, 400, family=SYM)
    g += '</g>'
    return g


def cards(hand, size_w=30):
    """hand: list like ['AH','KS','7D']. Drawn as an overlapping row."""
    n = len(hand)
    w, h, step = 56, 80, 34
    vw = w + step * (n - 1) + 6
    body = ''.join(_card(3 + i * step, 3, c[:-1], c[-1]) for i, c in enumerate(hand))
    return _svg(size_w, size_w * (h + 6) / vw, vw, h + 6, body)


def card(rank='A', suit='S', size_w=9):
    return _svg(size_w, size_w * 86 / 62, 62, 86, _card(3, 3, rank, suit))


def deck(size_w=80):
    """Chart of a standard 52-card deck: 4 rows of 13."""
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cw, ch, gap = 22, 30, 3
    left = 26
    vw = left + 13 * (cw + gap)
    vh = 4 * (ch + gap) + 2
    body = ''
    for r, s in enumerate('HDCS'):
        sym, col = SUIT[s]
        y = 1 + r * (ch + gap)
        body += _txt(12, y + ch / 2, sym, 18, col, 400, family=SYM)
        for i, rk in enumerate(ranks):
            x = left + i * (cw + gap)
            pic = rk in 'JQK'
            body += (f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="3" '
                     f'fill="{"#f3efe2" if pic else "#fff"}" stroke="{INK}" stroke-width="1.2"/>')
            body += _txt(x + cw / 2, y + 10, rk, 10 if rk != '10' else 9, col, 600)
            body += _txt(x + cw / 2, y + 22, sym, 10, col, 400, family=SYM)
    return _svg(size_w, size_w * vh / vw, vw, vh, body)


# ---------------------------------------------------------------- counters in a bag or jar
def _counter_positions(n, x0, y0, w, h, r):
    """Rows of counters, bottom up, centred, alternating widths. No two counters
    overlap (checked), so every counter can be seen and counted."""
    import math as _m
    step = 2 * r + 2
    cols = max(1, int((w + 2) // step))
    vstep = 2 * r + 1.2
    pos, row, i = [], 0, 0
    while i < n:
        cap = cols - (1 if (row % 2 and cols > 1) else 0)
        k = min(cap, n - i)
        roww = k * step - 2
        start = x0 + (w - roww) / 2 + r
        y = y0 + h - r - row * vstep
        for j in range(k):
            pos.append((start + j * step, y))
        i += k
        row += 1
    for a in range(len(pos)):
        for b in range(a + 1, len(pos)):
            assert _m.dist(pos[a], pos[b]) >= 2 * r - 1e-6, 'counters overlap'
    return pos


def _expand(counts):
    seq = []
    for col, k in counts:
        seq += [col] * k
    # interleave colours so the bag looks mixed but stays countable
    import random
    rnd = random.Random(7 + len(seq))
    rnd.shuffle(seq)
    return seq


def bag(counts, size=24, letters=True, r=7.5):
    """counts: list of (colour, number)."""
    seq = _expand(counts)
    body = (f'<path d="M30,22 C18,30 8,52 8,74 C8,98 24,110 60,110 C96,110 112,98 112,74 '
            f'C112,52 102,30 90,22 Z" fill="#f4efe1" stroke="{INK}" stroke-width="2.5"/>'
            f'<path d="M30,22 C40,14 80,14 90,22" fill="none" stroke="{INK}" stroke-width="2.5"/>'
            f'<path d="M36,18 C48,4 72,4 84,18" fill="none" stroke="{MAROON}" stroke-width="3"/>')
    for (x, y), col in zip(_counter_positions(len(seq), 16, 34, 88, 72, r), seq):
        body += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{COL[col]}" stroke="{INK}" stroke-width="1.2"/>'
        if letters:
            body += _txt(x, y + 0.5, LET[col], 7.5, '#fff' if col in DARK else INK, 600)
    return _svg(size, size * 116 / 120, 120, 116, body)


def jar(counts, size=22, letters=True, r=6.5):
    seq = _expand(counts)
    body = (f'<rect x="30" y="4" width="50" height="12" rx="3" fill="{MAROON}"/>'
            f'<path d="M34,16 L34,24 C14,30 10,44 10,60 L10,104 C10,112 16,116 24,116 L86,116 '
            f'C94,116 100,112 100,104 L100,60 C100,44 96,30 76,24 L76,16 Z" fill="#eef4fb" '
            f'stroke="{INK}" stroke-width="2.5"/>')
    for (x, y), col in zip(_counter_positions(len(seq), 14, 40, 82, 72, r), seq):
        body += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{COL[col]}" stroke="{INK}" stroke-width="1.1"/>'
        if letters:
            body += _txt(x, y + 0.5, LET[col], 6.5, '#fff' if col in DARK else INK, 600)
    return _svg(size * 110 / 120, size, 110, 120, body)


# ---------------------------------------------------------------- letter tiles and number cards
def tiles(word, size_h=8, fill='#efe9d8', stroke='#a59e83'):
    n = len(word)
    s, gap = 40, 5
    vw = n * (s + gap) - gap + 4
    body = ''
    for i, ch in enumerate(word):
        x = 2 + i * (s + gap)
        body += f'<rect x="{x}" y="2" width="{s}" height="{s}" rx="5" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
        body += _txt(x + s / 2, 2 + s / 2 + 1, ch, 24, INK, 600)
    return _svg(size_h * vw / (s + 4), size_h, vw, s + 4, body)


def number_cards(nums, size_h=9):
    return tiles([str(n) for n in nums], size_h, '#ffffff', INK)


def raffle(num='0427', size_w=24):
    body = (f'<path d="M4,4 H136 V22 A8,8 0 0 0 136,38 V56 H4 V38 A8,8 0 0 0 4,22 Z" '
            f'fill="#fbe9ef" stroke="{MAROON}" stroke-width="2.5"/>'
            f'<line x1="100" y1="6" x2="100" y2="54" stroke="{MAROON}" stroke-width="2" stroke-dasharray="4 3"/>')
    body += _txt(52, 20, 'RAFFLE', 13, MAROON, 600)
    body += _txt(52, 40, f'No. {num}', 15, INK, 600)
    body += _txt(118, 30, num[-2:], 15, MAROON, 600)
    return _svg(size_w, size_w * 60 / 140, 140, 60, body)


def balls(nums, size_h=9, fill='#f2c94c'):
    n = len(nums)
    vw = n * 46 + 4
    body = ''
    for i, k in enumerate(nums):
        x = 25 + i * 46
        body += f'<circle cx="{x}" cy="25" r="21" fill="{fill}" stroke="{INK}" stroke-width="2.2"/>'
        body += f'<circle cx="{x}" cy="25" r="12" fill="#fff"/>'
        body += _txt(x, 26, str(k), 13, INK, 600)
    return _svg(size_h * vw / 50, size_h, vw, 50, body)


# ---------------------------------------------------------------- probability scale
def prob_scale(width=150, marks=None, words=True, numbers=('0', '1/2', '1')):
    """marks: list of (value 0..1, label). Fonts grow when the scale is drawn small."""
    W = 400
    k = 1.0 if width >= 90 else (1.45 if width >= 55 else 1.8)
    x0, x1, y = 24, 376, 60
    body = f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{INK}" stroke-width="{2.5*k}"/>'
    for v in [0, 0.25, 0.5, 0.75, 1]:
        x = x0 + (x1 - x0) * v
        big = v in (0, 0.5, 1)
        t = (9 if big else 6) * k
        body += f'<line x1="{x}" y1="{y - t}" x2="{x}" y2="{y + t}" stroke="{INK}" stroke-width="{2.5*k}"/>'
    labs = {0: numbers[0], 0.5: numbers[1], 1: numbers[2]}
    for v, s in labs.items():
        if not s:
            continue
        x = x0 + (x1 - x0) * v
        if s == '1/2':
            body += _txt(x, y + 13 * k + 4, '1', 11 * k, INK, 500, family=SERIF)
            body += f'<line x1="{x - 5*k}" y1="{y + 20*k + 4}" x2="{x + 5*k}" y2="{y + 20*k + 4}" stroke="{INK}" stroke-width="{1.3*k}"/>'
            body += _txt(x, y + 27 * k + 4, '2', 11 * k, INK, 500, family=SERIF)
        else:
            body += _txt(x, y + 17 * k + 4, s, 13 * k, INK, 500, family=SERIF)
    vh = 92 + (38 * k if words else 0) - (0 if words else 10)
    if words:
        for v, s in [(0, 'impossible'), (0.25, 'unlikely'), (0.5, 'even chance'), (0.75, 'likely'), (1, 'certain')]:
            x = x0 + (x1 - x0) * v
            anc = 'start' if v == 0 else ('end' if v == 1 else 'middle')
            xx = x - 14 if v == 0 else (x + 14 if v == 1 else x)
            body += _txt(xx, y + 34 * k + 14, s, 11 * k, BLUE, 500, anc)
    for v, s in (marks or []):
        x = x0 + (x1 - x0) * v
        body += f'<line x1="{x}" y1="{y - 32}" x2="{x}" y2="{y - 12}" stroke="{MAROON}" stroke-width="2.5"/>'
        body += f'<polygon points="{x - 5},{y - 16} {x + 5},{y - 16} {x},{y - 9}" fill="{MAROON}"/>'
        body += f'<circle cx="{x}" cy="{y - 42}" r="10" fill="{MAROON}"/>'
        body += _txt(x, y - 41.5, s, 12, '#fff', 600)
    top = 0 if marks else 34
    return _svg(width, width * (vh - top) / W, W, vh - top, body, f'style="overflow:visible"').replace(
        f'viewBox="0 0 {W} {vh - top}"', f'viewBox="0 {top} {W} {vh - top}"')


# ---------------------------------------------------------------- column graph of results
def bar_chart(labels, freqs, width=60, height=38, ymax=None, step=None, xlabel='', ylabel='Frequency',
              title='', colour=None):
    W, H = 300, 190
    ml, mr, mt, mb = 40, 10, 22 if title else 10, 40
    ymax = ymax or max(freqs)
    step = step or (5 if ymax > 12 else 2)
    ytop = math.ceil(ymax / step) * step
    pw, ph = W - ml - mr, H - mt - mb
    body = ''
    if title:
        body += _txt(W / 2, 10, title, 11, INK, 600)
    for k in range(0, ytop + 1, step):
        y = mt + ph - ph * k / ytop
        body += f'<line x1="{ml}" y1="{y:.1f}" x2="{W - mr}" y2="{y:.1f}" stroke="#d9dde6" stroke-width="1"/>'
        body += _txt(ml - 6, y, str(k), 10, INK, 400, 'end', SERIF)
    n = len(freqs)
    bw = pw / n
    for i, (lab, f) in enumerate(zip(labels, freqs)):
        x = ml + i * bw + bw * 0.15
        h = ph * f / ytop
        body += f'<rect x="{x:.1f}" y="{mt + ph - h:.1f}" width="{bw * 0.7:.1f}" height="{h:.1f}" fill="{colour or "#a9c1e6"}" stroke="{BLUE}" stroke-width="1.5"/>'
        body += _txt(ml + i * bw + bw / 2, mt + ph + 11, str(lab), 11, INK, 400, family=SERIF)
    body += f'<line x1="{ml}" y1="{mt}" x2="{ml}" y2="{mt + ph}" stroke="{INK}" stroke-width="1.6"/>'
    body += f'<line x1="{ml}" y1="{mt + ph}" x2="{W - mr}" y2="{mt + ph}" stroke="{INK}" stroke-width="1.6"/>'
    if xlabel:
        body += _txt(ml + pw / 2, H - 10, xlabel, 11, INK, 500)
    if ylabel:
        body += _txt(12, mt + ph / 2, ylabel, 11, INK, 500, extra=f'transform="rotate(-90 12 {mt + ph / 2})"')
    return _svg(width, height, W, H, body)


# ---------------------------------------------------------------- calculator / random number generator
def calculator(cmd='RanInt#(1,6)', result='4', size_w=24):
    body = (f'<rect x="3" y="3" width="94" height="134" rx="10" fill="#5a5f66" stroke="{INK}" stroke-width="2"/>'
            f'<rect x="12" y="12" width="76" height="34" rx="3" fill="#cfdccb" stroke="#2d332d" stroke-width="1.5"/>')
    body += _txt(16, 22, cmd, 9.5, '#1f2a1f', 500, 'start')
    body += _txt(84, 37, result, 15, '#1f2a1f', 600, 'end')
    for r in range(4):
        for c in range(4):
            x, y = 14 + c * 19, 58 + r * 19
            body += f'<rect x="{x}" y="{y}" width="14" height="13" rx="3" fill="{"#e8913a" if (r, c) == (3, 3) else "#e6e7ea"}"/>'
    return _svg(size_w, size_w * 140 / 100, 100, 140, body)


# ---------------------------------------------------------------- coin-toss grid game
def grid_game(rows=5, cols=5, yellow=((0, 0), (1, 3), (2, 2), (3, 1), (4, 4), (0, 4), (4, 0)), size=22):
    s = 18
    body = ''
    for r in range(rows):
        for c in range(cols):
            f = COL['yellow'] if (r, c) in yellow else '#ffffff'
            body += f'<rect x="{4 + c * s}" y="{4 + r * s}" width="{s}" height="{s}" fill="{f}" stroke="{INK}" stroke-width="1.6"/>'
            if (r, c) in yellow:
                body += _txt(4 + c * s + s / 2, 4 + r * s + s / 2, 'Y', 8, INK, 600)
    vw = cols * s + 8
    return _svg(size, size * (rows * s + 8) / vw, vw, rows * s + 8, body)


# ---------------------------------------------------------------- Venn diagrams
def venn(a='', both='', b='', out='', la='A', lb='B', width=48, mutually_exclusive=False,
         total=None, fill_a='#dbe6f6', fill_b='#f1dde7'):
    W, H = 240, 150
    body = f'<rect x="3" y="3" width="{W - 6}" height="{H - 6}" rx="6" fill="#fff" stroke="{INK}" stroke-width="2"/>'
    if total is not None:
        body += _txt(W - 12, 16, f'{total}', 13, INK, 600, 'end', SERIF)
    if mutually_exclusive:
        ca, cb, r = (70, 80), (170, 80), 46
    else:
        ca, cb, r = (95, 80), (145, 80), 52
    body += f'<circle cx="{ca[0]}" cy="{ca[1]}" r="{r}" fill="{fill_a}" fill-opacity="0.85" stroke="{BLUE}" stroke-width="2.5"/>'
    body += f'<circle cx="{cb[0]}" cy="{cb[1]}" r="{r}" fill="{fill_b}" fill-opacity="0.65" stroke="{MAROON}" stroke-width="2.5"/>'
    body += _txt(ca[0] - (30 if not mutually_exclusive else 0), 20, la, 12, BLUE, 600)
    body += _txt(cb[0] + (30 if not mutually_exclusive else 0), 20, lb, 12, MAROON, 600)
    if mutually_exclusive:
        body += _txt(ca[0], 82, a, 16, INK, 500, family=SERIF)
        body += _txt(cb[0], 82, b, 16, INK, 500, family=SERIF)
    else:
        body += _txt(68, 82, a, 16, INK, 500, family=SERIF)
        body += _txt(120, 82, both, 16, INK, 500, family=SERIF)
        body += _txt(172, 82, b, 16, INK, 500, family=SERIF)
    body += _txt(24, H - 20, out, 16, INK, 500, family=SERIF)
    return _svg(width, width * H / W, W, H, body)


def venn_one(inside='', outside='', label='E', width=40, out_label="not E"):
    W, H = 200, 130
    body = f'<rect x="3" y="3" width="{W - 6}" height="{H - 6}" rx="6" fill="#f5f3eb" stroke="{INK}" stroke-width="2"/>'
    body += f'<circle cx="85" cy="68" r="48" fill="#dbe6f6" stroke="{BLUE}" stroke-width="2.5"/>'
    body += _txt(85, 40, label, 13, BLUE, 600)
    body += _txt(85, 72, inside, 13, INK, 500, family=SERIF)
    body += _txt(165, 24, out_label, 12, MAROON, 600)
    body += _txt(165, 95, outside, 13, INK, 500, family=SERIF)
    return _svg(width, width * H / W, W, H, body)


# ---------------------------------------------------------------- two dice sample space
def dice_grid(op='+', width=55, highlight=None, blank=False):
    s = 24
    W = H = 7 * s + 4
    body = ''
    for i in range(7):
        for j in range(7):
            x, y = 2 + j * s, 2 + i * s
            if i == 0 and j == 0:
                body += f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{INK}"/>'
                body += _txt(x + s / 2, y + s / 2, '+' if op == '+' else '×', 14, '#fff', 600)
                continue
            head = i == 0 or j == 0
            val = j if i == 0 else i if j == 0 else (i + j if op == '+' else i * j)
            hl = highlight and not head and highlight(val)
            fill = '#eaf1fa' if head else ('#f6d7e4' if hl else '#fff')
            body += f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{fill}" stroke="{INK}" stroke-width="1.2"/>'
            if head or not blank:
                body += _txt(x + s / 2, y + s / 2 + 0.5, str(val), 11, BLUE if head else INK, 600 if head else 400,
                             family=SANS if head else SERIF)
    return _svg(width, width, W, H, body)


# ---------------------------------------------------------------- weather
def weather(pct='30%', size_w=22):
    body = (f'<circle cx="38" cy="38" r="18" fill="#fff" stroke="{INK}" stroke-width="2.5"/>'
            f'<circle cx="60" cy="30" r="22" fill="#fff" stroke="{INK}" stroke-width="2.5"/>'
            f'<circle cx="82" cy="40" r="16" fill="#fff" stroke="{INK}" stroke-width="2.5"/>'
            f'<rect x="36" y="38" width="48" height="18" fill="#fff"/>'
            f'<line x1="22" y1="56" x2="96" y2="56" stroke="{INK}" stroke-width="2.5"/>')
    for x in (40, 58, 76):
        body += f'<path d="M{x},66 q-5,9 0,12 q5,-3 0,-12 Z" fill="{COL["blue"]}"/>'
    body += _txt(60, 96, pct, 15, INK, 600)
    return _svg(size_w, size_w * 106 / 120, 120, 106, body)


def money_box(counts, size_w=60):
    """counts: list of (value, number) e.g. [('$2',4),('$1',3)]"""
    n = len(counts)
    W = n * 60
    body = ''
    for i, (v, k) in enumerate(counts):
        cx = 30 + i * 60
        inner = aus_coin(v, 10)
        body += f'<g transform="translate({cx - 22},2) scale(0.44)">{inner[inner.index(">") + 1:-6]}</g>'
        body += _txt(cx, 62, f'× {k}', 19, INK, 600)
    return _svg(size_w, size_w * 76 / W, W, 76, body)


def esky(cans, size_w=40):
    """cans: list of (colour, label, number)"""
    W = 60 * len(cans)
    body = ''
    for i, (col, lab, k) in enumerate(cans):
        x = 18 + i * 60
        body += (f'<rect x="{x}" y="6" width="24" height="40" rx="4" fill="{COL[col]}" stroke="{INK}" stroke-width="2"/>'
                 f'<rect x="{x + 3}" y="2" width="18" height="6" rx="2" fill="#d5d9de" stroke="{INK}" stroke-width="1.5"/>')
        body += _txt(x + 12, 27, lab[0].upper(), 13, '#fff' if col in DARK else INK, 600)
        body += _txt(x + 12, 57, lab, 10.5, INK, 500)
        body += _txt(x + 12, 71, f'× {k}', 11, INK, 600)
    return _svg(size_w, size_w * 78 / W, W, 78, body)


def books(spines, size_h=14):
    """spines: list of (letter, colour)."""
    body = ''
    x = 4
    for i, (lab, col) in enumerate(spines):
        w = 22 + (i % 3) * 3
        h = 78 - (i % 4) * 6
        body += f'<rect x="{x}" y="{90 - h}" width="{w}" height="{h}" rx="3" fill="{COL.get(col, col)}" stroke="{INK}" stroke-width="2"/>'
        body += _txt(x + w / 2, 90 - h / 2, lab, 16, '#fff' if col in DARK else INK, 600)
        x += w + 3
    body += f'<line x1="0" y1="91" x2="{x + 2}" y2="91" stroke="{INK}" stroke-width="3"/>'
    return _svg(size_h * (x + 3) / 95, size_h, x + 3, 95, body)
