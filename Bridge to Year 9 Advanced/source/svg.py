"""Small inline-SVG diagrams, drawn to scale. Units: 1 user unit = 1 mm when width given in mm."""
import math

STROKE = '#1d2433'
FILL = 'rgba(80,110,200,0.08)'


def _svg(w, h, body, vb=None):
    vb = vb or f'0 0 {w} {h}'
    return (f'<svg class="dia" viewBox="{vb}" width="{w}mm" height="{h}mm" '
            f'xmlns="http://www.w3.org/2000/svg" font-family="InterW, Inter" font-size="3.1">{body}</svg>')


def _txt(x, y, s, anchor='middle', size=3.1, weight=500, col=STROKE, italic=False):
    st = ' font-style="italic"' if italic else ''
    return (f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" font-size="{size}" '
            f'font-weight="{weight}" fill="{col}"{st}>{s}</text>')


def right_tri(a, b, la, lb, lc, maxw=24, maxh=17, flip=False):
    """legs a (horizontal) and b (vertical); hypotenuse label lc. Drawn to scale."""
    k = min(maxw / a, maxh / b)
    W, H = a * k, b * k
    pad = 6
    w, h = W + 2 * pad + 4, H + 2 * pad
    if not flip:
        P = [(pad, pad), (pad, pad + H), (pad + W, pad + H)]  # right angle at bottom-left
        sq = 2.2
        mark = f'<path d="M{pad} {pad+H-sq} h{sq} v{sq}" fill="none" stroke="{STROKE}" stroke-width="0.3"/>'
        t_a = _txt(pad + W / 2, pad + H + 4.2, la)
        t_b = _txt(pad - 1.2, pad + H / 2 + 1, lb, anchor='end')
        # hypotenuse label offset outward (up-right)
        mx, my = pad + W / 2, pad + H / 2
        nx, ny = H, W
        nl = math.hypot(nx, ny)
        t_c = _txt(mx + nx / nl * 3.2 + 1, my - ny / nl * 3.2 + 1, lc)
    else:
        P = [(pad + W, pad), (pad + W, pad + H), (pad, pad + H)]
        sq = 2.2
        mark = f'<path d="M{pad+W} {pad+H-sq} h{-sq} v{sq}" fill="none" stroke="{STROKE}" stroke-width="0.3"/>'
        t_a = _txt(pad + W / 2, pad + H + 4.2, la)
        t_b = _txt(pad + W + 1.2, pad + H / 2 + 1, lb, anchor='start')
        mx, my = pad + W / 2, pad + H / 2
        nx, ny = -H, W
        nl = math.hypot(nx, ny)
        t_c = _txt(mx + nx / nl * 3.2 - 1, my - ny / nl * 3.2 + 1, lc)
    pts = ' '.join(f'{x:.2f},{y:.2f}' for x, y in P)
    body = (f'<polygon points="{pts}" fill="{FILL}" stroke="{STROKE}" stroke-width="0.35"/>'
            + mark + t_a + t_b + t_c)
    return _svg(round(w, 1), round(h, 1), body)


def poly(points, labels, scale, w, h, extra=''):
    """points in real units; labels list of (x, y, text, anchor) in real units (y up)."""
    pad = 5
    pts = ' '.join(f'{pad + x*scale:.2f},{h - pad - y*scale:.2f}' for x, y in points)
    body = f'<polygon points="{pts}" fill="{FILL}" stroke="{STROKE}" stroke-width="0.35"/>'
    for x, y, t, anc in labels:
        body += _txt(pad + x * scale, h - pad - y * scale, t, anchor=anc)
    body += extra
    return _svg(w, h, body)


def area_model():
    """rectangle 7 high, split into widths x and 4"""
    s = 3.2
    X, F_, H = 9, 4, 7   # drawn widths
    pad = 7
    w, h = pad + (X + F_) * s + 4, pad + H * s + 4
    x0, y0 = pad, 3
    body = (f'<rect x="{x0}" y="{y0}" width="{X*s}" height="{H*s}" fill="rgba(15,155,142,0.12)" stroke="{STROKE}" stroke-width="0.35"/>'
            f'<rect x="{x0+X*s}" y="{y0}" width="{F_*s}" height="{H*s}" fill="rgba(15,155,142,0.28)" stroke="{STROKE}" stroke-width="0.35"/>'
            + _txt(x0 + X * s / 2, y0 + H * s + 4, 'x', italic=True)
            + _txt(x0 + X * s + F_ * s / 2, y0 + H * s + 4, '4')
            + _txt(x0 - 1.5, y0 + H * s / 2 + 1, '7', anchor='end'))
    return _svg(round(w, 1), round(h, 1), body)


def rect_minus_square():
    """(x+4) by (x+1) rectangle with x by x square shaded"""
    s = 3.0
    xs, a, b = 6, 4, 1
    pad = 8
    W, H = (xs + a) * s, (xs + b) * s
    w, h = W + pad + 4, H + 10
    x0, y0 = pad, 3
    body = (f'<rect x="{x0}" y="{y0}" width="{W}" height="{H}" fill="rgba(15,155,142,0.22)" stroke="{STROKE}" stroke-width="0.35"/>'
            f'<rect x="{x0}" y="{y0 + b*s}" width="{xs*s}" height="{xs*s}" fill="#fff" stroke="{STROKE}" stroke-width="0.35" stroke-dasharray="1 0.8"/>'
            + _txt(x0 + xs * s / 2, y0 + b * s + xs * s / 2 + 1, 'cut out', size=2.6, col='#667085')
            + _txt(x0 + W / 2, y0 + H + 4.5, 'x + 4', italic=True)
            + _txt(x0 - 1.5, y0 + H / 2 + 1, 'x + 1', anchor='end', italic=True)
            + _txt(x0 + xs * s / 2, y0 + b * s + xs * s - 1.5, 'x', italic=True, size=2.8))
    return _svg(round(w, 1), round(h, 1), body)


def l_shape():
    """10 x 8 rectangle with 6 x 3 notch from top-right: area 62"""
    pts = [(0, 0), (10, 0), (10, 5), (4, 5), (4, 8), (0, 8)]
    lab = [(5, -1.0, '10 cm', 'middle'), (10.4, 2.3, '5 cm', 'start'), (7, 5.4, '6 cm', 'middle'),
           (-0.5, 4, '8 cm', 'end'), (2, 8.4, '4 cm', 'middle')]
    return poly(pts, lab, 3.2, 52, 36)


def house():
    """rectangle 12 x 5 with triangle on top, height 4"""
    pts = [(0, 0), (12, 0), (12, 5), (6, 9), (0, 5)]
    extra = ''
    s, pad, h = 2.6, 5, 33
    # dashed height of triangle
    X, Y1, Y2 = pad + 6 * s, h - pad - 5 * s, h - pad - 9 * s
    extra += f'<line x1="{X}" y1="{Y1}" x2="{X}" y2="{Y2}" stroke="{STROKE}" stroke-width="0.3" stroke-dasharray="1 0.7"/>'
    extra += f'<line x1="{pad}" y1="{Y1}" x2="{pad+12*s}" y2="{Y1}" stroke="{STROKE}" stroke-width="0.25" stroke-dasharray="1 0.7"/>'
    lab = [(6, -1.1, '12 cm', 'middle'), (12.4, 2.2, '5 cm', 'start'), (6.4, 6.1, '4 cm', 'start')]
    return poly(pts, lab, s, 48, h, extra)


def trap_prism():
    """trapezoidal prism: front face trapezium a=4 (top), b=10 (bottom), h=3; length 20"""
    s = 3.0
    pad = 3
    a, b, hh, L = 4, 10, 3, 20
    dx, dy = 9, -6  # depth offset (oblique)
    bx = pad
    by = 28
    P = [(bx, by), (bx + b * s, by), (bx + (b + a) / 2 * s, by - hh * s), (bx + (b - a) / 2 * s, by - hh * s)]
    Q = [(x + dx, y + dy) for x, y in P]
    def pl(pts):
        return ' '.join(f'{x:.2f},{y:.2f}' for x, y in pts)
    body = f'<polygon points="{pl(P)}" fill="rgba(214,51,108,0.12)" stroke="{STROKE}" stroke-width="0.35"/>'
    for i in (1, 2, 3):
        body += f'<line x1="{P[i][0]:.2f}" y1="{P[i][1]:.2f}" x2="{Q[i][0]:.2f}" y2="{Q[i][1]:.2f}" stroke="{STROKE}" stroke-width="0.35"/>'
    body += f'<polyline points="{pl([Q[1], Q[2], Q[3]])}" fill="none" stroke="{STROKE}" stroke-width="0.35"/>'
    body += _txt(bx + b * s / 2, by + 4, '10 cm')
    body += _txt(bx + b / 2 * s, by - hh * s + 3.6, '4 cm', size=2.8)
    body += f'<line x1="{P[3][0]:.2f}" y1="{P[3][1]:.2f}" x2="{P[3][0]:.2f}" y2="{by}" stroke="{STROKE}" stroke-width="0.25" stroke-dasharray="0.8 0.6"/>'
    body += _txt(P[3][0] + 0.8, by - 1.2, '3 cm', anchor='start', size=2.8)
    body += _txt((P[1][0] + Q[1][0]) / 2 + 2.5, (P[1][1] + Q[1][1]) / 2 + 2, '20 cm', anchor='start')
    return _svg(48, 34, body)
