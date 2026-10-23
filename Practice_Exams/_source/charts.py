"""SVG chart helpers styled to match the charts in the Year 8 Yearly Examination."""
import math

FONT = "font-family='DejaVu Sans, sans-serif'"
BAR = "#a6c8ec"
EDGE = "#333"
GRID = "#dddddd"
MINOR = "#efefef"


def _ticks(lo, hi, step):
    v, out = lo, []
    while v <= hi + 1e-9:
        out.append(round(v, 6))
        v += step
    return out


def _fmt(v):
    return str(int(v)) if float(v).is_integer() else str(v)


def _axes(x0, y0, x1, y1, ymin, ymax, ystep, minor, ylabel):
    """Return gridlines, y-axis labels and a y-mapping function."""
    def Y(v):
        return y1 - (v - ymin) / (ymax - ymin) * (y1 - y0)

    s = []
    if minor:
        for v in _ticks(ymin, ymax, minor):
            s.append(f"<line x1='{x0}' x2='{x1}' y1='{Y(v):.1f}' y2='{Y(v):.1f}' stroke='{MINOR}' stroke-width='0.6'/>")
    for v in _ticks(ymin, ymax, ystep):
        s.append(f"<line x1='{x0}' x2='{x1}' y1='{Y(v):.1f}' y2='{Y(v):.1f}' stroke='{GRID}' stroke-width='0.8'/>")
        s.append(f"<line x1='{x0-3}' x2='{x0}' y1='{Y(v):.1f}' y2='{Y(v):.1f}' stroke='{EDGE}' stroke-width='0.8'/>")
        s.append(f"<text x='{x0-6}' y='{Y(v)+3:.1f}' font-size='8' text-anchor='end' {FONT}>{_fmt(v).replace('-', '−')}</text>")
    s.append(f"<rect x='{x0}' y='{y0}' width='{x1-x0}' height='{y1-y0}' fill='none' stroke='{EDGE}' stroke-width='0.8'/>")
    cy = (y0 + y1) / 2
    s.append(f"<text x='14' y='{cy}' font-size='8.5' text-anchor='middle' transform='rotate(-90 14 {cy})' {FONT}>{ylabel}</text>")
    return s, Y


def column_chart(title, cats, vals, ymax, ystep, ylabel, xlabel, minor=None, ymin=0):
    W, H = 380, 215
    x0, y0, x1, y1 = 52, 24, 370, 170
    s, Y = _axes(x0, y0, x1, y1, ymin, ymax, ystep, minor, ylabel)
    n = len(cats)
    slot = (x1 - x0) / n
    bw = slot * 0.62
    for i, (c, v) in enumerate(zip(cats, vals)):
        cx = x0 + slot * (i + 0.5)
        s.append(f"<rect x='{cx-bw/2:.1f}' y='{Y(v):.1f}' width='{bw:.1f}' height='{Y(ymin)-Y(v):.1f}' fill='{BAR}' stroke='{EDGE}' stroke-width='0.8'/>")
        s.append(f"<text x='{cx:.1f}' y='{y1+12}' font-size='8' text-anchor='middle' {FONT}>{c}</text>")
    s.append(f"<text x='{(x0+x1)/2}' y='{y1+25}' font-size='8.5' text-anchor='middle' {FONT}>{xlabel}</text>")
    s.append(f"<text x='{(x0+x1)/2}' y='14' font-size='9' font-weight='bold' text-anchor='middle' {FONT}>{title}</text>")
    return f"<svg viewBox='0 0 {W} {H}' width='{W}' height='{H}'>{''.join(s)}</svg>"


def line_chart(title, xs, vals, ymin, ymax, ystep, ylabel, xlabel, minor=None):
    W, H = 380, 215
    x0, y0, x1, y1 = 52, 24, 370, 170
    s, Y = _axes(x0, y0, x1, y1, ymin, ymax, ystep, minor, ylabel)
    n = len(xs)
    pad = 14
    X = lambda i: x0 + pad + i * (x1 - x0 - 2 * pad) / (n - 1)
    for i in range(n):
        s.append(f"<line x1='{X(i):.1f}' x2='{X(i):.1f}' y1='{y0}' y2='{y1}' stroke='{MINOR}' stroke-width='0.6'/>")
        s.append(f"<text x='{X(i):.1f}' y='{y1+12}' font-size='8' text-anchor='middle' {FONT}>{xs[i]}</text>")
    if ymin < 0:
        s.append(f"<line x1='{x0}' x2='{x1}' y1='{Y(0):.1f}' y2='{Y(0):.1f}' stroke='#999' stroke-width='0.9'/>")
    pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(vals))
    s.append(f"<polyline points='{pts}' fill='none' stroke='#000' stroke-width='1.1'/>")
    for i, v in enumerate(vals):
        s.append(f"<circle cx='{X(i):.1f}' cy='{Y(v):.1f}' r='2.6' fill='#000'/>")
    s.append(f"<text x='{(x0+x1)/2}' y='{y1+25}' font-size='8.5' text-anchor='middle' {FONT}>{xlabel}</text>")
    s.append(f"<text x='{(x0+x1)/2}' y='14' font-size='9' font-weight='bold' text-anchor='middle' {FONT}>{title}</text>")
    return f"<svg viewBox='0 0 {W} {H}' width='{W}' height='{H}'>{''.join(s)}</svg>"


PIE_COLOURS = ["#a6c8ec", "#f6d58a", "#b9e0a5", "#efb6d3", "#c9b8e6", "#f4b39a"]


def pie_chart(title, items):
    """items: list of (label, percent). Drawn clockwise from 12 o'clock."""
    W, H = 330, 258
    cx, cy, r = 165, 136, 90
    s = [f"<text x='{cx}' y='14' font-size='9' font-weight='bold' text-anchor='middle' {FONT}>{title}</text>"]
    a = -90.0
    for i, (lab, p) in enumerate(items):
        sweep = p * 3.6
        a0, a1 = math.radians(a), math.radians(a + sweep)
        xa, ya = cx + r * math.cos(a0), cy + r * math.sin(a0)
        xb, yb = cx + r * math.cos(a1), cy + r * math.sin(a1)
        large = 1 if sweep > 180 else 0
        s.append(f"<path d='M{cx},{cy} L{xa:.2f},{ya:.2f} A{r},{r} 0 {large} 1 {xb:.2f},{yb:.2f} Z' fill='{PIE_COLOURS[i % 6]}' stroke='#444' stroke-width='0.8'/>")
        mid = math.radians(a + sweep / 2)
        if p >= 10:
            lx, ly = cx + 0.6 * r * math.cos(mid), cy + 0.6 * r * math.sin(mid)
            anchor = "middle"
        else:
            lx, ly = cx + 1.14 * r * math.cos(mid), cy + 1.14 * r * math.sin(mid)
            anchor = "start" if math.cos(mid) > 0.2 else ("end" if math.cos(mid) < -0.2 else "middle")
        s.append(f"<text x='{lx:.1f}' y='{ly-2:.1f}' font-size='8' text-anchor='{anchor}' {FONT}>{lab}</text>")
        s.append(f"<text x='{lx:.1f}' y='{ly+8:.1f}' font-size='8' text-anchor='{anchor}' {FONT}>{_fmt(p)}%</text>")
        a += sweep
    return f"<svg viewBox='0 0 {W} {H}' width='{W}' height='{H}'>{''.join(s)}</svg>"


def dot_plot(title, values, counts, xlabel):
    n = len(values)
    W = 340
    top = max(counts)
    H = 60 + top * 11
    x0, x1 = 30, W - 30
    base = H - 32
    X = lambda i: x0 + i * (x1 - x0) / (n - 1)
    s = [f"<text x='{W/2}' y='12' font-size='9' font-weight='bold' text-anchor='middle' {FONT}>{title}</text>"]
    s.append(f"<line x1='{x0-12}' x2='{x1+12}' y1='{base}' y2='{base}' stroke='#000' stroke-width='0.9'/>")
    for i, (v, c) in enumerate(zip(values, counts)):
        s.append(f"<line x1='{X(i):.1f}' x2='{X(i):.1f}' y1='{base}' y2='{base+4}' stroke='#000' stroke-width='0.9'/>")
        s.append(f"<text x='{X(i):.1f}' y='{base+14}' font-size='8' text-anchor='middle' {FONT}>{v}</text>")
        for k in range(c):
            s.append(f"<circle cx='{X(i):.1f}' cy='{base-9-k*11}' r='4.2' fill='#000'/>")
    s.append(f"<text x='{W/2}' y='{base+26}' font-size='8.5' text-anchor='middle' {FONT}>{xlabel}</text>")
    return f"<svg viewBox='0 0 {W} {H}' width='{W}' height='{H}'>{''.join(s)}</svg>"


def right_triangle(left, bottom, hyp="x cm"):
    """Right angle at bottom-left; vertical leg on the left, horizontal leg along the bottom."""
    W, H = 230, 120
    A, B, C = (60, 18), (60, 92), (200, 92)
    s = [
        f"<polygon points='{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}' fill='none' stroke='#000' stroke-width='1.1'/>",
        f"<rect x='{B[0]}' y='{B[1]-9}' width='9' height='9' fill='none' stroke='#000' stroke-width='0.9'/>",
        f"<text x='{A[0]-6}' y='{(A[1]+B[1])/2+3}' font-size='9' text-anchor='end' {FONT}>{left}</text>",
        f"<text x='{(B[0]+C[0])/2}' y='{B[1]+14}' font-size='9' text-anchor='middle' {FONT}>{bottom}</text>",
        f"<text x='{(A[0]+C[0])/2+10}' y='{(A[1]+C[1])/2-6}' font-size='9' text-anchor='start' {FONT}>{hyp}</text>",
    ]
    return f"<svg viewBox='0 0 {W} {H}' width='{W}' height='{H}'>{''.join(s)}</svg>"
