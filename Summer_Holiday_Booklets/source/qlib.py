"""Question helpers shared by all booklet content files."""


def Q(t, a, w='', s=False, d='', x='', c=None):
    """t: question HTML (KaTeX in $..$), a: answer, w: one line of working,
    s: star (preview), d: SVG diagram, x: extra HTML (tables), c: check spec."""
    return dict(t=t, a=a, w=w, s=s, d=d, x=x, c=c)


def B(t, a, w='', c=None):
    return dict(t=t, a=a, w=w, c=c)


def xy(xs, ys, xl='$x$', yl='$y$'):
    r1 = ''.join(f'<td>{v}</td>' for v in xs)
    r2 = ''.join(f'<td>{v}</td>' for v in ys)
    return f'<table class="xy"><tr><td>{xl}</td>{r1}</tr><tr><td>{yl}</td>{r2}</tr></table>'


def stemleaf(rows, key):
    body = ''.join(f'<tr><td>{s}</td><td>{" ".join(str(l) for l in leaves)}</td></tr>' for s, leaves in rows)
    return f'<div class="dgh"><table class="sl">{body}</table><div style="font-size:8.5px;color:#6b7280;margin-top:1px">Key: {key}</div></div>'
