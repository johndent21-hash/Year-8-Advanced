"""Build a Summer Maths booklet (HTML -> PDF via Chromium)."""
import html, json, os, re, subprocess, sys, importlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
KATEX = ROOT / 'node_modules' / 'katex' / 'dist'


FONTDIR = ROOT / 'node_modules' / '@fontsource' / 'inter' / 'files'
FONTS = ''.join(
    f"@font-face {{ font-family: 'InterW'; font-weight: {w}; font-style: normal; "
    f"src: url('file://{FONTDIR}/inter-latin-{w}-normal.woff2') format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }}\n"
    f"@font-face {{ font-family: 'InterW'; font-weight: {w}; font-style: normal; "
    f"src: url('file://{FONTDIR}/inter-latin-ext-{w}-normal.woff2') format('woff2'); unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }}\n"
    for w in (400, 500, 600, 700, 800, 900))

NAME_COLS = {
    'Number': '#e8590c', 'Functions & graphs': '#e8590c',
    'Indices & roots': '#c2255c', 'Indices': '#c2255c', 'Indices & surds': '#c2255c', 'Indices, surds & logs': '#c2255c', 'Money': '#c2255c',
    'Algebra': '#1c7ed6', 'Equations': '#7048e8',
    'Measurement': '#0c9a73', 'Measurement & trig': '#0c9a73', 'Trigonometry': '#0c9a73',
    'Patterns & graphs': '#0b7285', 'Rates & graphs': '#0b7285', 'Coordinate geometry': '#0b7285', 'Linear': '#0b7285',
    'Angles & chance': '#5c940d', 'Angles, data & chance': '#5c940d', 'Data & chance': '#5c940d', 'Geometry & chance': '#5c940d',
    'Data & context': '#495057', 'In context': '#495057', 'Money & context': '#495057',
}
GROUP_COLS = ['#e8590c', '#c2255c', '#1c7ed6', '#7048e8', '#0c9a73', '#0b7285', '#5c940d', '#495057']


def esc(s):
    return s  # content is authored HTML


CSS = r"""
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { font-family: 'InterW', 'DejaVu Sans', sans-serif; color: #1f2a37; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width: 210mm; height: 297mm; position: relative; overflow: hidden; page-break-after: always; background: #fff; }
.page:last-child { page-break-after: auto; }
.katex { font-size: 1.04em; }
.footer { position: absolute; left: 38px; right: 38px; bottom: 16px; display: flex; justify-content: space-between; font-size: 8px; color: #6b7280; }
.footer b { font-size: 9.5px; font-weight: 800; }

/* ---------- cover ---------- */
.cover { background: var(--cream); }
.cover .art { position: absolute; left: 0; top: 0; width: 100%; height: 76%; background-size: cover; background-position: center top; }
.cover .art::after { content: ''; position: absolute; left: 0; right: 0; bottom: 0; height: 52%;
  background: linear-gradient(to bottom, rgba(255,255,255,0) 0%, var(--cream-a) 55%, var(--cream) 100%); }
.cover .pill1 { position: absolute; top: 34px; left: 50px; background: rgba(255,255,255,0.93); border-radius: 20px; padding: 6px 13px;
  font-size: 10.5px; font-weight: 800; letter-spacing: 1.6px; color: #1f2a37; }
.cover .pill2 { position: absolute; top: 34px; right: 50px; border: 1.5px solid var(--c3); background: rgba(255,255,255,0.75); color: var(--c3d);
  border-radius: 20px; padding: 5px 13px; font-size: 10.5px; font-weight: 800; letter-spacing: 1.6px; }
.cover .block { position: absolute; left: 52px; right: 52px; bottom: 54px; }
.cover .kicker { font-size: 12.5px; font-weight: 800; letter-spacing: 1.9px; color: var(--c3d); margin-bottom: 4px; }
.cover h1 { font-size: 72px; line-height: 1.02; margin: 0; font-weight: 900; letter-spacing: -2.2px; color: var(--c1); }
.cover h2 { font-size: 33px; margin: 2px 0 14px; font-weight: 800; letter-spacing: -0.6px; color: var(--c2); }
.cover .stripe { display: flex; width: 172px; height: 6px; border-radius: 3px; overflow: hidden; margin-bottom: 18px; }
.cover .stripe span { flex: 1; }
.cover .intro { font-size: 14px; line-height: 1.5; color: #374151; max-width: 540px; margin-bottom: 22px; }
.cover .chips { display: flex; gap: 9px; margin-bottom: 30px; }
.cover .chips span { flex: 1; text-align: center; border-radius: 7px; padding: 8px 0; font-size: 11.5px; font-weight: 800; color: #fff; }
.cover .namerow { display: flex; gap: 32px; }
.cover .namerow div { font-size: 10px; font-weight: 800; letter-spacing: 1.6px; color: #374151; border-bottom: 1.4px solid var(--c3); padding-bottom: 22px; }

/* ---------- banners ---------- */
.banner { position: absolute; left: 0; top: 0; width: 100%; height: 108px; background-size: cover; background-position: center; }
.banner svg.wave { position: absolute; left: 0; bottom: -1px; width: 100%; height: 30px; }
.ptitle { position: absolute; left: 38px; top: 26px; background: rgba(255,255,255,0.94); border-radius: 13px; padding: 9px 20px;
  font-size: 23px; font-weight: 900; letter-spacing: -0.4px; border: 1px solid rgba(0,0,0,0.06); }

/* ---------- how it works ---------- */
.hiw { position: absolute; top: 128px; left: 38px; right: 38px; display: flex; gap: 26px; }
.hiw .col { flex: 1; }
.hiw h3 { font-size: 15.5px; margin: 0 0 5px; font-weight: 800; color: var(--acc); }
.hiw p { margin: 0 0 13px; font-size: 12.6px; line-height: 1.5; color: #374151; }
.strands { display: grid; grid-template-columns: 1fr 1fr; column-gap: 12px; row-gap: 3px; margin: 4px 0 14px; }
.strands div { display: flex; align-items: center; border-left: 3px solid; padding: 3px 0 3px 7px; font-size: 11.2px; color: #374151; min-height: 21px; line-height: 1.2; }
.strands b { width: 22px; flex: none; font-size: 11.5px; }
.why { background: var(--peach); border-radius: 8px; padding: 11px 13px; font-size: 11.5px; line-height: 1.5; color: #374151; margin-bottom: 11px; }
.syl { border: 1px solid #e5e7eb; border-radius: 8px; padding: 9px 12px; font-size: 9.6px; line-height: 1.45; color: #4b5563; }
.syl b { color: #1f2a37; }
.rules { margin: 0 0 14px; padding-left: 16px; }
.rules li { font-size: 12.3px; line-height: 1.45; margin-bottom: 5px; color: #374151; }
.tracker { width: 100%; border-collapse: collapse; margin-bottom: 16px; }
.tracker th { font-size: 7.6px; letter-spacing: 0.7px; color: #6b7280; text-align: left; padding: 4px 3px; border-bottom: 1px solid #d1d5db; font-weight: 800; }
.tracker td { font-size: 11.5px; padding: 12px 3px; border-bottom: 1px solid #e5e7eb; color: #374151; }
.wk { display: inline-flex; width: 17px; height: 17px; border-radius: 50%; color: #fff; font-size: 9.5px; font-weight: 800; align-items: center; justify-content: center; margin-right: 6px; }
.firstup { background: #12263a; color: #e5edf5; border-radius: 9px; padding: 13px 15px; font-size: 12.3px; line-height: 1.5; }
.firstup b { color: var(--c2l); }

/* ---------- week page ---------- */
.wkcard { position: absolute; left: 38px; top: 16px; background: rgba(255,255,255,0.95); border-radius: 12px; padding: 7px 14px 7px 8px;
  display: flex; align-items: center; gap: 9px; border: 1px solid rgba(0,0,0,0.06); }
.wkcard .vw { writing-mode: vertical-rl; transform: rotate(180deg); font-size: 8.5px; font-weight: 800; letter-spacing: 2px; }
.wkcard .big { font-size: 46px; font-weight: 900; line-height: 1; letter-spacing: -1px; padding-right: 9px; border-right: 1px solid #d1d5db; }
.wkcard .tt { font-size: 11px; color: #374151; line-height: 1.35; }
.wkcard .tt b { display: block; font-size: 14px; color: #1f2a37; font-weight: 800; }
.scard { position: absolute; right: 38px; top: 12px; background: rgba(255,255,255,0.95); border-radius: 12px; padding: 8px 14px 8px 14px;
  font-size: 11px; font-weight: 600; color: #374151; border: 1px solid rgba(0,0,0,0.06); width: 210px; line-height: 2.05; }
.scard .ln { display: inline-block; border-bottom: 1px solid #6b7280; width: 92px; margin-left: 4px; }
.scard .bx { display: inline-block; width: 42px; height: 17px; border: 1.4px solid; border-radius: 6px; vertical-align: middle; margin: 0 3px; }
.scard .cb { display: inline-block; width: 12px; height: 12px; border: 1.4px solid; border-radius: 3px; vertical-align: middle; margin: 0 9px 0 4px; }
.legend { position: absolute; top: 114px; left: 38px; right: 38px; display: flex; align-items: center; font-size: 7.7px; color: #374151; gap: 8px; white-space: nowrap; }
.legend i { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 3px; vertical-align: -0.5px; }
.legend .r { margin-left: auto; font-weight: 700; }
.star { color: #d9480f; }
.grid { position: absolute; top: 128px; left: 38px; right: 38px; bottom: 100px; display: flex; gap: 10px; }
.qcol { flex: 1; display: flex; flex-direction: column; gap: 5px; min-width: 0; }
.card { flex: 1 1 auto; border: 1px solid #e3e7ec; border-radius: 7px; padding: 5px 9px 3px 11px; display: flex; flex-direction: column; background: #fff; min-height: 0; position: relative; overflow: hidden; }
.card .bar { position: absolute; left: 0; top: 0; bottom: 0; width: 4px; }
.qh { display: flex; align-items: center; gap: 6px; margin-bottom: 1px; }
.num { width: 17px; height: 17px; border-radius: 50%; color: #fff; font-size: 9.5px; font-weight: 800; display: inline-flex; align-items: center; justify-content: center; flex: none; }
.lab { font-size: 8px; font-weight: 800; letter-spacing: 1.1px; text-transform: uppercase; }
.qb { display: flex; align-items: flex-start; gap: 6px; }
.qt { flex: 1; font-size: 11.9px; line-height: 1.34; min-width: 0; }
.qb svg.dg, .qb .dgh { flex: none; margin-top: -12px; margin-bottom: -6px; }
.dots { flex: 1 1 auto; min-height: 19px; margin-top: 2px; position: relative; overflow: hidden; }
.dots { background-image: url('DOTSURL/dots.png'); background-size: 13px 12px; background-repeat: repeat; }
.bonus .bd { background-image: url('DOTSURL/dots_gold.png'); background-size: 13px 12px; background-repeat: repeat; }
table.xy { border-collapse: collapse; margin-top: 3px; font-size: 11px; }
table.xy td { border: 1px solid #9aa4b1; padding: 0 8px; text-align: center; min-width: 28px; height: 16px; }
table.xy td:first-child { background: #f1f4f7; }
table.sl { border-collapse: collapse; font-size: 10.5px; line-height: 1.25; }
table.sl td { padding: 0 6px; }
table.sl td:first-child { border-right: 1.2px solid #1f2a37; text-align: right; font-weight: 700; }
.bonus { position: absolute; left: 38px; right: 38px; bottom: 36px; height: 58px; border: 1.4px solid #f2c94c; background: #fffbea; border-radius: 9px;
  display: flex; align-items: center; padding: 0 14px; gap: 14px; }
.bonus .bt { flex: none; background: linear-gradient(90deg, #f59f00, #f08c00); color: #fff; font-weight: 900; font-size: 10.5px; letter-spacing: 1.6px; padding: 5px 13px; border-radius: 12px; }
.bonus .bq { flex: 2; font-size: 11.9px; line-height: 1.34; }
.bonus .bd { flex: 1; height: 38px; position: relative; overflow: hidden; }

/* ---------- hints ---------- */
.hgrid { position: absolute; top: 122px; left: 38px; right: 38px; bottom: 44px; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: repeat(4, 1fr); gap: 13px; }
.hbox { border-top: 3.5px solid; border-radius: 3px 3px 9px 9px; padding: 9px 13px; font-size: 11.2px; line-height: 1.5; color: #374151; overflow: hidden; }
.hbox h4 { margin: 0 0 4px; font-size: 14px; font-weight: 800; }
.hbox div { margin-bottom: 3px; }

/* ---------- answers ---------- */
.ans { position: absolute; top: 112px; left: 38px; right: 38px; bottom: 40px; display: flex; flex-direction: column; gap: 8px; }
.aweek h3 { font-size: 16px; font-weight: 800; margin: 0 0 4px; display: flex; align-items: center; gap: 6px; }
.agrid { display: grid; grid-template-columns: 1fr 1fr; column-gap: 26px; flex: 1; }
.agrid > div { display: flex; flex-direction: column; }
.agrid .arow { flex: 1 1 auto; }
.aweek { flex: 1; display: flex; flex-direction: column; }
.arow { display: flex; align-items: center; gap: 7px; border-bottom: 1px solid #e8ebef; padding: 3px 0; min-height: 36px; font-size: 11.6px; line-height: 1.3; }
.apill { flex: none; min-width: 22px; height: 15px; border-radius: 8px; color: #fff; font-size: 8.6px; font-weight: 800; display: inline-flex; align-items: center; justify-content: center; }
.aa { font-weight: 700; color: #111827; }
.aw { color: #6b7280; font-size: 10.4px; }
.aw .katex { font-size: 1em; }
.abonus { margin-top: 5px; border: 1.3px solid #f2c94c; background: #fffbea; border-radius: 8px; padding: 5px 9px; display: flex; align-items: center; gap: 8px; font-size: 11.6px; }
"""


def dots_svg(col='#b4bcc7', rows=14, width=420):
    """Rows of middle dots as text: tiny in the PDF (a vector path per dot is not)."""
    n = int(width // 13) + 1
    line = '·' * n
    body = '<br>'.join([line] * rows)
    return f'<div class="dt" style="color:{col}">{body}</div>'


DOTS = dots_svg()


def wave_svg(fill='#fff'):
    return ('<svg class="wave" viewBox="0 0 800 30" preserveAspectRatio="none">'
            f'<path d="M0,22 C120,6 230,4 360,14 C500,25 620,28 800,8 L800,30 L0,30 Z" fill="{fill}"/></svg>')


def footer(bk, page, col):
    return f'<div class="footer"><span>Kingscliff High School · Summer Maths: {bk["ready"]}</span><b style="color:{col}">{page}</b></div>'


def group_of(bk, n):
    for gi, (_, _, nums) in enumerate(bk['groups']):
        if n in nums:
            return gi
    raise KeyError(n)


def gcol(bk, n):
    return bk['gcols'][group_of(bk, n)]


def cover(bk, art):
    p = bk['pal']
    chips = ''.join(f'<span style="background:{c};{"color:#3b2f00" if bk.get("dark_chip") == i else ""}">Week {i + 1}</span>'
                    for i, c in enumerate(bk['chip_cols']))
    stripe = ''.join(f'<span style="background:{c}"></span>' for c in p['stripe'])
    return f"""<div class="page cover">
<div class="art" style="background-image:url('{art}/cover.jpg')"></div>
<div class="pill1">KINGSCLIFF HIGH SCHOOL · MATHEMATICS</div><div class="pill2">JULIA SERIES</div>
<div class="block">
<div class="kicker">{bk['kicker']}</div>
<h1>Summer Maths</h1><h2>{bk['ready']}</h2>
<div class="stripe">{stripe}</div>
<div class="intro">{bk['intro']}</div>
<div class="chips">{chips}</div>
<div class="namerow"><div style="flex:2.2">NAME</div><div style="flex:1">CLASS</div></div>
</div></div>"""


def how(bk, art):
    acc = bk['week_cols'][0]
    strands = ''
    order = list(range(1, 11)), list(range(11, 21))
    cells = []
    for i in range(10):
        for n in (order[0][i], order[1][i]):
            c = gcol(bk, n)
            cells.append(f'<div style="border-color:{c}"><b style="color:{c}">{n}</b>{bk["strands"][n]}</div>')
    strands = ''.join(cells)
    rows = ''.join(f'<tr><td><span class="wk" style="background:{c}">{i + 1}</span>Week {i + 1}</td><td></td><td>/ 20</td><td>☐</td><td>☐</td><td></td></tr>'
                   for i, c in enumerate(bk['week_cols']))
    rules = ''.join(f'<li>{r}</li>' for r in bk['rules'])
    return f"""<div class="page">
<div class="banner" style="background-image:url('{art}/w1.jpg')">{wave_svg()}</div>
<div class="ptitle" style="color:{acc}">How it works</div>
<div class="hiw" style="--acc:{acc}"><div class="col">
<h3>One page a week</h3>
<p>Each week has <b>20 questions</b> and a <b>bonus</b>. Set aside about <b>40 minutes</b> – one sitting or a few short ones. Questions start easier and get a little harder through the page.</p>
<h3>The same pattern every week</h3>
<p>{bk['pattern']}</p>
<div class="strands">{strands}</div>
<div class="why"><b>Why Julia?</b> Each banner is part of the same <i>Julia set</i>: pick a number $c$, then repeat $z \\to z^2 + c$ for every point. Points that stay small are coloured in. Every booklet in the series zooms into a different corner of the same set – {bk['julia_note']}</div>
<div class="syl"><b>NSW syllabus (NESA Mathematics K–10, 2022).</b> {re.sub(r'(MA[45]-[A-Z]+(?:-[A-Z])?-\d\d)', r'<span style="white-space:nowrap">\1</span>', bk['outcomes'])}</div>
</div><div class="col">
<h3>Rules of the game</h3>
<ul class="rules">{rules}</ul>
<h3>My summer tracker</h3>
<table class="tracker"><tr><th>WEEK</th><th>DATE</th><th>SCORE</th><th>DONE</th><th>BONUS</th><th>REVISE (Q NUMBERS)</th></tr>{rows}</table>
<div class="firstup">{bk['first_up']}</div>
</div></div>
{footer(bk, 2, acc)}</div>"""


def legend(bk):
    items = ''.join(f'<span><i style="background:{bk["gcols"][i]}"></i>{g[0]}</span>' for i, g in enumerate(bk['groups']))
    return f'<div class="legend">{items}<span class="r"><span class="star">★</span> {bk["star_text"]} · No calculator</span></div>'


def render_q(bk, n, q):
    c = gcol(bk, n)
    star = ' <span class="star" style="font-size:11px">★</span>' if q.get('s') else ''
    dg = q.get('d', '')
    extra = q.get('x', '')
    return (f'<div class="card"><div class="bar" style="background:{c}"></div><div class="qh"><span class="num" style="background:{c}">{n}</span>'
            f'<span class="lab" style="color:{c}">{bk["strands"][n]}</span>{star}</div>'
            f'<div class="qb"><div class="qt">{q["t"]}{extra}</div>{dg}</div><div class="dots"></div></div>')


def week_page(bk, art, w):
    col = bk['week_cols'][w]
    qs = bk['weeks'][w]
    left = ''.join(render_q(bk, i + 1, qs[i]) for i in range(10))
    right = ''.join(render_q(bk, i + 11, qs[i + 10]) for i in range(10))
    b = bk['bonus'][w]
    return f"""<div class="page">
<div class="banner" style="background-image:url('{art}/w{w + 1}.jpg')">{wave_svg()}</div>
<div class="wkcard"><span class="vw" style="color:{col}">WEEK</span><span class="big" style="color:{col}">{w + 1}</span><span class="tt">Summer Maths<b>{bk['ready']}</b></span></div>
<div class="scard">Date started<span class="ln"></span><br>Score<span class="bx" style="border-color:{col}"></span>/ 20<br>Done<span class="cb" style="border-color:{col}"></span>Bonus<span class="cb" style="border-color:{col}"></span></div>
{legend(bk)}
<div class="grid"><div class="qcol">{left}</div><div class="qcol">{right}</div></div>
<div class="bonus"><span class="bt">BONUS</span><span class="bq">{b['t']}</span><span class="bd"></span></div>
{footer(bk, w + 3, col)}</div>"""


def hints_page(bk, art):
    boxes = ''
    for gi, (title, lines) in enumerate(bk['hints']):
        c = bk['gcols'][gi]
        tint = bk['tints'][gi]
        body = ''.join(f'<div>{l}</div>' for l in lines)
        boxes += f'<div class="hbox" style="border-color:{c};background:{tint}"><h4 style="color:{c}">{title}</h4>{body}</div>'
    col = bk['week_cols'][4]
    return f"""<div class="page">
<div class="banner" style="background-image:url('{art}/w5.jpg')">{wave_svg()}</div>
<div class="ptitle" style="color:{col}">Hints &amp; formulas</div>
<div class="hgrid">{boxes}</div>
{footer(bk, 9, col)}</div>"""


def answer_rows(bk, w):
    qs = bk['weeks'][w]
    def row(n):
        q = qs[n - 1]
        c = gcol(bk, n)
        return f'<div class="arow"><span class="apill" style="background:{c}">{n}</span><span class="aa">{q["a"]}</span><span class="aw">{q.get("w", "")}</span></div>'
    left = ''.join(row(n) for n in range(1, 11))
    right = ''.join(row(n) for n in range(11, 21))
    b = bk['bonus'][w]
    col = bk['week_cols'][w]
    return f"""<div class="aweek"><h3 style="color:{col}"><span class="wk" style="background:{col};margin:0">{w + 1}</span>Week {w + 1} answers</h3>
<div class="agrid"><div>{left}</div><div>{right}</div></div>
<div class="abonus"><span class="apill" style="background:#f08c00">B</span><span class="aa">{b['a']}</span><span class="aw">{b.get('w', '')}</span></div></div>"""


def answers_page(bk, art, w0, page):
    col = bk['week_cols'][w0]
    return f"""<div class="page">
<div class="banner" style="background-image:url('{art}/w{w0 + 1}.jpg')">{wave_svg()}</div>
<div class="ptitle" style="color:{col}">Answers</div>
<div class="ans">{answer_rows(bk, w0)}{answer_rows(bk, w0 + 1)}</div>
{footer(bk, page, col)}</div>"""


def mathify(s):
    s = s.replace('\\$', '\x00')
    s = re.sub(r'\$(.+?)\$', lambda m: '\\(' + m.group(1) + '\\)', s, flags=re.S)
    assert '$' not in s, s[s.index('$') - 80: s.index('$') + 80]
    return s.replace('\x00', '$')


def build_html(bk, art):
    pages = [cover(bk, art), how(bk, art)] + [week_page(bk, art, w) for w in range(6)] + [hints_page(bk, art)]
    pages += [answers_page(bk, art, 0, 10), answers_page(bk, art, 2, 11), answers_page(bk, art, 4, 12)]
    p = bk['pal']
    vars_ = (f"--cream:{p['cream']};--cream-a:{p['cream_a']};--c1:{p['title']};--c2:{p['sub']};--c3:{p['kick']};"
             f"--c3d:{p['kick_d']};--peach:{p['peach']};--c2l:{p['firstup']};")
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>Summer Maths: {bk['ready']}</title>
<link rel="stylesheet" href="file://{KATEX}/katex.min.css">
<style>{FONTS}{CSS.replace('DOTSURL', 'file://' + str(ROOT / 'art'))}</style>
<script src="file://{KATEX}/katex.min.js"></script>
<script src="file://{KATEX}/contrib/auto-render.min.js"></script>
</head><body style="{vars_}">{mathify(''.join(pages))}
<script>renderMathInElement(document.body, {{delimiters:[{{left:'\\\\(',right:'\\\\)',display:false}}], throwOnError:true}}); document.body.setAttribute('data-done','1');</script>
</body></html>"""
