"""Small SVG diagrams for question cards. Everything is drawn to scale from the
numbers in the question, so a diagram cannot contradict its data."""
import math

INK = '#1f2a37'
FILL = '#e8f4f6'
FS = 9.5


def _svg(w, h, body, pad=6):
    return (f'<svg class="dg" xmlns="http://www.w3.org/2000/svg" width="{w + 2 * pad:.0f}" '
            f'height="{h + 2 * pad:.0f}" viewBox="{-pad} {-pad} {w + 2 * pad:.1f} {h + 2 * pad:.1f}">'
            f'{body}</svg>')


def _t(x, y, s, anchor='middle', size=FS, italic=False, weight=500, col=INK):
    st = ' font-style="italic"' if italic else ''
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" '
            f'dominant-baseline="middle" font-family="InterW, DejaVu Sans" font-weight="{weight}" fill="{col}"{st}>{s}</text>')


def _poly(pts, fill=FILL, stroke=INK, sw=1.1, dash=None):
    d = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<polygon points="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da}/>'


def _line(a, b, sw=1.1, dash=None, col=INK):
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{col}" stroke-width="{sw}"{da}/>'


def _arc(c, r, a0, a1, sw=0.9):
    """Arc centred c from angle a0 to a1 (degrees, maths convention, y up)."""
    x0, y0 = c[0] + r * math.cos(math.radians(a0)), c[1] - r * math.sin(math.radians(a0))
    x1, y1 = c[0] + r * math.cos(math.radians(a1)), c[1] - r * math.sin(math.radians(a1))
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return (f'<path d="M{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 0 {x1:.1f},{y1:.1f}" fill="none" '
            f'stroke="{INK}" stroke-width="{sw}"/>')


def _ang(p, q):
    return math.degrees(math.atan2(-(q[1] - p[1]), q[0] - p[0]))


def _right_mark(p, u, v, s=6):
    """Right-angle square at p with unit vectors u, v along the two arms."""
    a = (p[0] + u[0] * s, p[1] + u[1] * s)
    b = (p[0] + u[0] * s + v[0] * s, p[1] + u[1] * s + v[1] * s)
    c = (p[0] + v[0] * s, p[1] + v[1] * s)
    return f'<polyline points="{a[0]:.1f},{a[1]:.1f} {b[0]:.1f},{b[1]:.1f} {c[0]:.1f},{c[1]:.1f}" fill="none" stroke="{INK}" stroke-width="0.9"/>'


def _unit(p, q):
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = math.hypot(dx, dy)
    return dx / L, dy / L


def _scale(w, h, maxw, maxh):
    return min(maxw / w, maxh / h)


def right_triangle(vert, horiz, lv='', lh='', lhyp='', theta=None, tlabel='θ',
                   maxw=80, maxh=44, flip=False):
    """Right angle at bottom-left (or bottom-right if flip). vert/horiz are true
    lengths (used only for scale). theta: 'top' or 'right' marks an acute angle."""
    k = _scale(horiz, vert, maxw, maxh)
    W, H = horiz * k, vert * k
    if not flip:
        R, T, B = (0, H), (0, 0), (W, H)
    else:
        R, T, B = (W, H), (W, 0), (0, H)
    body = _poly([R, T, B])
    body += _right_mark(R, _unit(R, B), _unit(R, T))
    off = 7
    sx = -1 if not flip else 1
    body += _t(R[0] + sx * off, H / 2, lv, anchor='end' if not flip else 'start')
    body += _t(W / 2, H + off + 1, lh)
    # hypotenuse label: outward normal
    mx, my = (T[0] + B[0]) / 2, (T[1] + B[1]) / 2
    ux, uy = _unit(T, B)
    nx, ny = (uy, -ux) if not flip else (-uy, ux)
    body += _t(mx + nx * 9, my + ny * 9, lhyp)
    if theta:
        P, Q1, Q2 = (B, R, T) if theta == 'base' else (T, R, B)
        a0, a1 = sorted([_ang(P, Q1), _ang(P, Q2)])
        if a1 - a0 > 180:
            a0, a1 = a1, a0 + 360
        r = 13
        body += _arc(P, r, a0, a1)
        mid = math.radians((a0 + a1) / 2)
        body += _t(P[0] + (r + 8) * math.cos(mid), P[1] - (r + 8) * math.sin(mid), tlabel, size=FS - 0.5)
    pad_l = 18 if not flip else 6
    return _svg(W + 24, H + 14, f'<g transform="translate({pad_l - 6},2)">{body}</g>')


def triangle(A, B, labels=('', '', ''), base=72, maxh=40):
    """Triangle with base angles A (left) and B (right) in degrees; apex angle C.
    labels: text placed inside the three corners (left, right, apex)."""
    C = 180 - A - B
    # base length 1; apex from left vertex via sine rule
    b_side = math.sin(math.radians(B)) / math.sin(math.radians(C))  # side from left vertex to apex
    ax, ay = b_side * math.cos(math.radians(A)), b_side * math.sin(math.radians(A))
    xs = [0, 1, ax]
    k = min(base / (max(xs) - min(xs)), maxh / ay)
    x0 = min(xs)
    L = ((0 - x0) * k, ay * k)
    Rt = ((1 - x0) * k, ay * k)
    Ap = ((ax - x0) * k, 0)
    W = (max(xs) - x0) * k
    body = _poly([L, Rt, Ap])
    for P, Q1, Q2, lab in [(L, Rt, Ap, labels[0]), (Rt, L, Ap, labels[1]), (Ap, L, Rt, labels[2])]:
        if not lab:
            continue
        u1, u2 = _unit(P, Q1), _unit(P, Q2)
        bx, by = u1[0] + u2[0], u1[1] + u2[1]
        bl = math.hypot(bx, by)
        half = math.acos(max(-1, min(1, u1[0] * u2[0] + u1[1] * u2[1]))) / 2
        d = max(13, 6.5 / math.sin(half))
        body += _t(P[0] + bx / bl * d, P[1] + by / bl * d, lab, size=FS - 1.5)
    return _svg(W, ay * k, body)


def straight_line(known, known_lab, unk_lab, length=96):
    """Ray from the middle of a horizontal line making `known` degrees with the right-hand side."""
    O = (length / 2, 34)
    r = 32
    P = (O[0] + r * math.cos(math.radians(known)), O[1] - r * math.sin(math.radians(known)))
    body = _line((0, O[1]), (length, O[1])) + _line(O, P)
    body += _arc(O, 10, 0, known) + _arc(O, 14, known, 180)
    m1, m2 = math.radians(known / 2), math.radians((known + 180) / 2)
    body += _t(O[0] + 27 * math.cos(m1), O[1] - 18 * math.sin(m1) - 3, known_lab, size=FS - 1)
    body += _t(O[0] + 27 * math.cos(m2), O[1] - 18 * math.sin(m2) - 3, unk_lab, size=FS - 1, italic=False)
    return _svg(length, 38, body)


def angles_at_point(rays, labels, r=27):
    """rays: directions in degrees (ascending); labels[i] sits between ray i and i+1."""
    O = (r + 6, r + 4)
    body = ''
    for a in rays:
        body += _line(O, (O[0] + r * math.cos(math.radians(a)), O[1] - r * math.sin(math.radians(a))))
    n = len(rays)
    for i in range(n):
        a0, a1 = rays[i], rays[(i + 1) % n]
        if a1 <= a0:
            a1 += 360
        body += _arc(O, 8 + 2 * (i % 2), a0, a1)
        m = math.radians((a0 + a1) / 2)
        body += _t(O[0] + 21 * math.cos(m), O[1] - 19 * math.sin(m), labels[i], size=FS - 1.5)
    return _svg(2 * r + 12, 2 * r + 8, body)


def crossing_lines(theta, lab_left, lab_right, length=100):
    """Two lines crossing at O making angle theta; label the left and right vertically opposite angles."""
    h = 36
    O = (length / 2, h / 2)
    dx = (h / 2) / math.tan(math.radians(theta / 2))
    body = _line((O[0] - dx, 0), (O[0] + dx, h)) + _line((O[0] - dx, h), (O[0] + dx, 0))
    body += _arc(O, 9, 180 - theta / 2, 180 + theta / 2) + _arc(O, 9, -theta / 2, theta / 2)
    body += _t(O[0] - 26, O[1], lab_left, anchor='end', size=FS - 1.5)
    body += _t(O[0] + 26, O[1], lab_right, anchor='start', size=FS - 1.5)
    return _svg(length, h, body)


def parallel(theta, pair, lab1, lab2, length=112):
    """Two horizontal parallel lines, transversal at theta (deg, measured from the
    positive x-direction). pair: 'corr', 'alt', 'coint'. lab1 at upper intersection, lab2 lower."""
    gap = 24
    y1, y2 = 8, 8 + gap
    t = math.radians(theta)
    cx = length / 2
    dx = (gap / 2 + 10) / math.tan(t)
    top = (cx + dx, y1 - 10)
    bot = (cx - dx, y2 + 10)
    body = _line((0, y1), (length, y1)) + _line((0, y2), (length, y2)) + _line(top, bot)
    for y in (y1, y2):  # arrows
        x = length - 14
        body += f'<polyline points="{x - 4},{y - 3} {x},{y} {x - 4},{y + 3}" fill="none" stroke="{INK}" stroke-width="1"/>'
    U = (cx + (gap / 2) / math.tan(t), y1)
    Lw = (cx - (gap / 2) / math.tan(t), y2)
    # angle positions: 'ur' = above line, right of transversal (between 0 and theta)
    def mark(P, where, lab, r=9):
        s = ''
        if where == 'ur':
            a0, a1 = 0, theta
        elif where == 'ul':
            a0, a1 = theta, 180
        elif where == 'll':
            a0, a1 = 180, 180 + theta
        else:  # 'lr'
            a0, a1 = 180 + theta, 360
        s += _arc(P, r, a0, a1)
        m = math.radians((a0 + a1) / 2)
        s += _t(P[0] + 19 * math.cos(m), P[1] - 11 * math.sin(m), lab, size=FS - 1.5)
        return s
    if pair == 'corr':
        body += mark(U, 'ur', lab1) + mark(Lw, 'ur', lab2)
    elif pair == 'alt':
        body += mark(U, 'll', lab1) + mark(Lw, 'ur', lab2)
    else:  # co-interior: both between the lines on the right side
        body += mark(U, 'lr', lab1) + mark(Lw, 'ur', lab2)
    return _svg(length, y2 + 10, body)


def lshape(W, H, cw, ch, labels, maxw=84, maxh=44):
    """L-shape: W x H rectangle with a cw x ch notch cut from the top-right corner.
    labels: dict edge->text for 'bottom','left','top','notch_v','notch_h','right'."""
    k = _scale(W, H, maxw, maxh)
    w, h, nw, nh = W * k, H * k, cw * k, ch * k
    pts = [(0, 0), (w - nw, 0), (w - nw, nh), (w, nh), (w, h), (0, h)]
    body = _poly(pts)
    o = 7
    if 'bottom' in labels: body += _t(w / 2, h + o + 1, labels['bottom'])
    if 'left' in labels: body += _t(-o, h / 2, labels['left'], anchor='end')
    if 'top' in labels: body += _t((w - nw) / 2, -o, labels['top'])
    if 'notch_v' in labels: body += _t(w - nw + 4, nh * 0.42, labels['notch_v'], anchor='start')
    if 'notch_h' in labels: body += _t(w - nw * 0.22, nh - o + 1, labels['notch_h'])
    if 'right' in labels: body += _t(w + o, (nh + h) / 2, labels['right'], anchor='start')
    return _svg(w + 30, h + 16, f'<g transform="translate(14,8)">{body}</g>')


def house(W, Hr, Ht, labels, maxw=72, maxh=46):
    """Rectangle W x Hr with an isosceles triangle of height Ht on top."""
    k = _scale(W, Hr + Ht, maxw, maxh)
    w, hr, ht = W * k, Hr * k, Ht * k
    pts = [(0, ht), (w / 2, 0), (w, ht), (w, ht + hr), (0, ht + hr)]
    body = _poly(pts) + _line((0, ht), (w, ht), sw=0.8, dash='3,2') + _line((w / 2, 0), (w / 2, ht), sw=0.8, dash='3,2')
    body += _t(w / 2 + 4, ht * 0.55, labels.get('roof', ''), anchor='start', size=FS - 1)
    body += _t(w + 6, ht + hr / 2, labels.get('side', ''), anchor='start')
    body += _t(w / 2, ht + hr + 8, labels.get('base', ''))
    return _svg(w + 22, ht + hr + 14, f'<g transform="translate(4,2)">{body}</g>')


def rect_diag(W, H, lw, lh, ld, maxw=84, maxh=40):
    k = _scale(W, H, maxw, maxh)
    w, h = W * k, H * k
    body = _poly([(0, 0), (w, 0), (w, h), (0, h)]) + _line((0, h), (w, 0), dash='4,2')
    body += _t(-6, h / 2, lh, anchor='end') + _t(w / 2, h + 8, lw) + _t(w / 2 + 6, h / 2 - 2, ld, italic=True)
    return _svg(w + 22, h + 14, f'<g transform="translate(14,2)">{body}</g>')


def network(nodes, edges, maxw=112, maxh=52):
    """nodes: {name: (x, y)} in arbitrary units (y down); edges: [(u, v, weight)]."""
    xs = [p[0] for p in nodes.values()]; ys = [p[1] for p in nodes.values()]
    k = min(maxw / (max(xs) - min(xs)), maxh / (max(ys) - min(ys)))
    P = {n: ((x - min(xs)) * k, (y - min(ys)) * k) for n, (x, y) in nodes.items()}
    body = ''
    for u, v, wt in edges:
        a, b = P[u], P[v]
        body += _line(a, b, sw=1)
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        body += (f'<rect x="{mx - 5.5:.1f}" y="{my - 5.5:.1f}" width="11" height="11" rx="2" fill="white"/>'
                 + _t(mx, my + 0.5, str(wt), size=FS - 1.5, weight=600))
    for n, (x, y) in P.items():
        body += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="white" stroke="{INK}" stroke-width="1.1"/>' + _t(x, y + 0.5, n, size=FS - 1.5, weight=700)
    W = max(p[0] for p in P.values()); H = max(p[1] for p in P.values())
    body += _t(W + 8, H + 15, 'Not to scale', anchor='end', size=7, weight=500, col='#6b7280')
    return _svg(W + 16, H + 24, f'<g transform="translate(8,8)">{body}</g>')


def oblique_triangle(a, b, C, lab_a, lab_b, lab_c, lab_C, maxw=90, maxh=46):
    """Triangle with sides a (CB) and b (CA) enclosing angle C at the bottom-left vertex."""
    Cp = (0, 0)
    Bp = (a, 0)
    Ap = (b * math.cos(math.radians(C)), b * math.sin(math.radians(C)))
    xs = [0, a, Ap[0]]; ys = [0, Ap[1]]
    k = min(maxw / (max(xs) - min(xs)), maxh / (max(ys) - min(ys)))
    x0 = min(xs)
    T = lambda p: ((p[0] - x0) * k, (Ap[1] - p[1]) * k)
    c_, b_, a_ = T(Cp), T(Bp), T(Ap)
    body = _poly([c_, b_, a_])
    body += _t((c_[0] + b_[0]) / 2, c_[1] + 8, lab_a)
    mx, my = (c_[0] + a_[0]) / 2, (c_[1] + a_[1]) / 2
    body += _t(mx - 8, my, lab_b, anchor='end')
    mx, my = (b_[0] + a_[0]) / 2, (b_[1] + a_[1]) / 2
    body += _t(mx + 7, my, lab_c, anchor='start', italic=True)
    body += _arc(c_, 10, 0, C)
    m = math.radians(C / 2)
    body += _t(c_[0] + 20 * math.cos(m), c_[1] - 17 * math.sin(m), lab_C, size=FS - 1.5)
    W = (max(xs) - x0) * k
    return _svg(W + 26, Ap[1] * k + 12, f'<g transform="translate(14,2)">{body}</g>')
