import sys, os, re, html, json
sys.path.insert(0, os.path.dirname(__file__))
import content_a as A, content_b as B
from dsl import ERRORS
from svg import right_tri

HERE = os.path.dirname(os.path.abspath(__file__))
LESSONS = [A.L1, A.L2, A.L3, A.L4, B.L5, B.L6, B.L7]
COL = {'L1': '#2f5fd0', 'L2': '#0c8a7e', 'L3': '#7f34c4', 'L4': '#c8382e', 'L5': '#2b8a3e',
       'L6': '#d9480f', 'L7': '#c2255c', 'T': '#3d4a5c'}
TOPIC = {'Int': 'Integers', 'Frac': 'Fractions', '%': 'Percentages', 'Ratio': 'Ratios', 'Lin': 'Linear', 'Eq': 'Equations'}
ROUND = {'B': ('Bronze round', 'Support · everyone starts here'),
         'S': ('Silver round', 'Core · aim to finish this round'),
         'G': ('Gold round', 'Extension · stretch yourself')}
FOOT = 'Kingscliff High School · Year 8 Advanced · Bridge to Year 9 Advanced'


def chip(tag):
    if not tag:
        return ''
    if tag in COL:
        return f'<span class="chip" style="--c:{COL[tag]}">↺ {tag}</span>'
    return f'<span class="chip y8">↺ {TOPIC.get(tag, tag)}</span>'


def star(it):
    return '<span class="star">★</span>' if it.star else ''


# ---------------------------------------------------------------- student
def render_grid(cols, items):
    rows = -(-len(items) // cols)
    diag = any('<svg' in it.q for it in items)
    out = [f'<div class="grid" style="--cols:{cols};flex-grow:{rows * (0.5 if diag else 1)}">']
    for it in items:
        diag = '<svg' in it.q
        out.append(f'<div class="cell{" dcell" if diag else ""}"><div class="qline"><span class="qn">{it.n}</span>'
                   f'<span class="q">{it.q}</span>{star(it)}</div><div class="aline">{chip(it.tag)}</div></div>')
    out.append('</div>')
    return ''.join(out)


def render_long(cols, items):
    rows = -(-len(items) // cols)
    hh = max(it.h for it in items)
    out = [f'<div class="lgrid" style="--cols:{cols};flex-grow:{rows * hh / 9:.2f}">']
    for it in items:
        out.append(f'<div class="lcell"><div class="qline"><span class="qn">{it.n}</span><span class="q">{it.q}</span>'
                   f'{star(it)}</div><div class="work" style="--h:{it.h}mm"></div></div>')
    out.append('</div>')
    return ''.join(out)


def render_ideas(L):
    lis = ''.join(f'<li>{x}</li>' for x in L['ideas'])
    exs = ''.join(f'<div class="ex"><div class="exq"><b>Example {i+1}</b> {q}</div>'
                  f'<div class="exa">$\\begin{{aligned}}{a}\\end{{aligned}}$</div></div>'
                  for i, (q, a) in enumerate(L['examples']))
    return (f'<div class="ideas"><div class="ki"><h3>Key ideas</h3><ul>{lis}</ul></div>'
            f'<div class="we"><h3>Worked examples</h3>{exs}</div></div>')


def round_head(code):
    t, who = ROUND[code]
    return (f'<div class="round {code}"><span class="medal">{code}</span><span class="rt">{t}</span>'
            f'<span class="who">{who}</span></div>')


def number_items(L):
    n = 0
    for pg in L['pages']:
        for b in pg:
            if b[0] in ('grid', 'long'):
                for it in b[2]:
                    n += 1
                    it.n = n
    return n


def lesson_pages(L, start_page):
    col = COL[L['key']]
    pages = []
    for pi, pg in enumerate(L['pages']):
        body = []
        if pi == 0:
            body.append(
                f'<header class="banner" style="background-image:url(img/{L["key"]}.jpg)"><div class="shade"></div>'
                f'<div class="bn-l"><div class="kick">Lesson {L["num"]} of 7</div><h1>{L["title"]}</h1>'
                f'<div class="bsub">{L["sub"]}</div></div>'
                f'<div class="bn-r"><span>50 min</span><span>No calculator</span></div></header>'
                f'<div class="outc"><b>Outcomes:</b> {L["outcomes"]} · MAO-WM-01 &nbsp;|&nbsp; {L["ext"]}'
                f'<span class="book">{L["book"]}</span></div>')
        else:
            body.append(f'<header class="mini" style="background-image:url(img/{L["key"]}.jpg)"><div class="shade"></div>'
                        f'<span>Lesson {L["num"]} · {L["title"]}</span><span class="pg">page {pi+1} of 3</span></header>')
        for b in pg:
            k = b[0]
            if k == 'ideas':
                body.append(render_ideas(L))
            elif k == 'round':
                body.append(round_head(b[1]))
            elif k == 'sub':
                body.append(f'<div class="subh">{b[1]}</div>')
            elif k == 'grid':
                body.append(render_grid(b[1], b[2]))
            elif k == 'long':
                body.append(render_long(b[1], b[2]))
        pages.append(page(''.join(body), start_page + pi, col, cls='lesson'))
    return pages


def page(inner, num, col, cls=''):
    return (f'<section class="page {cls}" style="--acc:{col}"><div class="inner">{inner}</div>'
            f'<footer><span>{FOOT}</span><span class="pn">{num}</span></footer></section>')


def test_pages(kind, start):
    data = A_PRE if kind == 'pre' else A_POST
    title = 'Pre-test' if kind == 'pre' else 'Post-test'
    blurb = ('Do this before Lesson 1. It shows what you already know and which rounds to focus on.' if kind == 'pre'
             else 'Do this after Lesson 7. Compare your score with your pre-test.')
    pages, cur = [], []
    head = (f'<header class="banner test" style="background-image:url(img/T.jpg)"><div class="shade"></div>'
            f'<div class="bn-l"><div class="kick">Bridge to Year 9 Advanced</div><h1>{title}</h1>'
            f'<div class="bsub">{blurb}</div></div>'
            f'<div class="bn-r"><span>20 marks</span><span>20 minutes</span><span>No calculator</span></div></header>'
            f'<div class="namebar"><span>Name ____________________________</span><span>Date ______________</span>'
            f'<span class="score">Score &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 20</span></div>')
    blocks = []
    for qn, qt, lk, parts in data:
        tot = sum(p['marks'] for p in parts)
        ps = []
        for p in parts:
            diag = '<svg' in p['html']
            ps.append(f'<div class="tpart{" tdiag" if diag else ""}"><div class="tq"><b>{p["label"]})</b> {p["html"]}</div>'
                      f'<div class="tans"><span class="tline"></span><span class="mk">[{p["marks"]}]</span></div></div>')
        blocks.append(f'<div class="tqblock"><div class="tqh"><span class="tqn" style="--c:{COL[lk]}">{qn}</span>'
                      f'<span>{qt}</span><span class="tl">Lesson {lk[1]} · {tot} marks</span></div>'
                      f'<div class="tparts">{"".join(ps)}</div></div>')
    p1 = head + ''.join(blocks[:4])
    tracker = ''.join(f'<tr><td><span class="tqn" style="--c:{COL[lk]}">{qn}</span> {qt}</td><td>Lesson {lk[1]}</td>'
                      f'<td>&nbsp;&nbsp;&nbsp;&nbsp;/ {sum(p["marks"] for p in parts)}</td>'
                      f'<td class="tick">Bronze &nbsp;☐ &nbsp; Silver ☐ &nbsp; Gold ☐</td></tr>'
                      for qn, qt, lk, parts in data)
    p2 = (f'<header class="mini" style="background-image:url(img/T.jpg)"><div class="shade"></div><span>{title}</span>'
          f'<span class="pg">page 2 of 2</span></header>' + ''.join(blocks[4:]) +
          f'<div class="reflect"><h3>{"Where should I start each lesson?" if kind == "pre" else "How much did I grow?"}</h3>'
          f'<table><tr><th>Question</th><th>Lesson</th><th>My marks</th>'
          f'<th>{"Start at…" if kind == "pre" else "Rounds I completed"}</th></tr>{tracker}</table>'
          f'<p class="small">{"Full marks on a question? Move quickly through Bronze and spend your time on Silver and Gold. Lost marks? Do every Bronze question first." if kind == "pre" else "Pre-test score: ______ / 20 &nbsp;&nbsp;→&nbsp;&nbsp; Post-test score: ______ / 20"}</p></div>')
    return [page(p1, start, COL['T'], 'test'), page(p2, start + 1, COL['T'], 'test')]


A_PRE, A_POST = B.PRE, B.POST


def cover():
    return ('<section class="page cover"><div class="cimg" style="background-image:url(img/cover.jpg)"></div>'
            '<div class="cshade"></div><div class="ctext">'
            '<div class="ckick">Kingscliff High School · Mathematics</div>'
            '<div class="cseries">Mandelbrot series</div>'
            '<h1>Bridge to<br>Year 9 Advanced</h1>'
            '<p class="csub">Seven lessons of revision and consolidation of the Year 8 algebra, indices, Pythagoras and measurement skills that Year 9 Advanced is built on.</p>'
            '<div class="ctopics">' + ''.join(
                f'<span style="--c:{COL[L["key"]]}"><b>{L["num"]}</b>{L["title"]}</span>' for L in LESSONS) +
            '</div><div class="cname"><span>Name</span><span>Class</span><span>Teacher</span></div></div></section>')


def howto(num):
    rows = ''.join(f'<tr><td><span class="tqn" style="--c:{COL[L["key"]]}">{L["num"]}</span> {L["title"]}</td>'
                   f'<td>{L["outcomes"]}</td><td>☐</td><td>☐</td><td>☐</td><td class="conf">1 &nbsp;2 &nbsp;3 &nbsp;4</td></tr>' for L in LESSONS)
    inner = (
        '<header class="mini tall" style="background-image:url(img/L1.jpg)"><div class="shade"></div><span>How this booklet works</span></header>'
        '<div class="how">'
        '<div class="hcol"><h3>One lesson = three pages = three rounds</h3>'
        '<p>Each lesson starts with <b>key ideas</b> and <b>worked examples</b>, then three rounds of questions that get harder as you go.</p>'
        '<div class="rrow"><span class="medal B">B</span><div><b>Bronze – support.</b> Quick drill questions. Everyone starts here; most should be done without help.</div></div>'
        '<div class="rrow"><span class="medal S">S</span><div><b>Silver – core.</b> Multi-step drill and worded problems. This is the standard for Year 9 Advanced.</div></div>'
        '<div class="rrow"><span class="medal G">G</span><div><b>Gold – extension.</b> Harder problems and a preview of Year 9 ideas. Try them once Silver is done.</div></div>'
        '<h3>Mixed questions</h3>'
        f'<p>Questions with a chip like {chip("L2")} come from an <b>earlier lesson</b>; chips like {chip("%")} revisit <b>other Year 8 topics</b>. '
        'Mixing topics feels harder, but it makes what you learn last much longer.</p>'
        '<h3>Symbols</h3>'
        '<p><span class="star">★</span> marks a Silver question that goes beyond Stage 4 core (it is in your Year 8 textbook as starred or Stage 5 work). '
        'All Gold questions are extension.</p>'
        '<p><b>No calculators.</b> Leave answers exact (e.g. $\\sqrt{74}$ or $90\\pi$) unless a question asks you to round. '
        'Write your working in the spaces provided.</p></div>'
        '<div class="hcol"><h3>My progress</h3><table class="track"><tr><th>Lesson</th><th>Syllabus</th><th>B</th><th>S</th><th>G</th><th>Confidence (circle)</th></tr>'
        f'{rows}</table>'
        '<div class="scores"><div><span>Pre-test</span><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 20</b></div><div><span>Post-test</span><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 20</b></div></div>'
        '<h3>A 50-minute lesson</h3><div class="timeline">'
        '<div style="flex:5"><b>0–5</b>Key ideas &amp; examples</div><div class="B" style="flex:13"><b>5–18</b>Bronze round</div>'
        '<div class="S" style="flex:22"><b>18–40</b>Silver round</div><div class="G" style="flex:10"><b>40–50</b>Gold · check answers</div></div>'
        '<p class="small">Finished early? Go straight to Gold. Stuck? Re-read the worked examples, then ask.</p>'
        '<h3>Getting the most out of it</h3><ul class="tips">'
        '<li>Try every question before asking for help – a wrong attempt teaches more than a blank.</li>'
        '<li>Show your working: in Year 9 Advanced most marks are for method.</li>'
        '<li>Check answers with your teacher; circle any you got wrong and redo them a few days later.</li>'
        '<li>Mixed (↺) questions are meant to make you stop and think “which skill is this?”</li></ul>'
        '<h3>Why Mandelbrot?</h3><p class="small">Every banner in this booklet is a zoom into the Mandelbrot set, drawn by repeating one '
        'tiny rule, $z \\to z^2 + c$, over and over. Simple algebra, repeated carefully, builds something extraordinary – which is '
        'exactly what Year 9 Advanced will ask of you.</p></div></div>')
    return page(inner, num, COL['L1'], 'howto')


def backpage(num):
    inner = (
        '<header class="mini tall" style="background-image:url(img/L4.jpg)"><div class="shade"></div><span>Summary sheet</span></header>'
        '<div class="summ">'
        '<div class="sbox" style="--c:#2f5fd0"><h4>Algebra</h4><p>Like terms: same pronumerals, same powers.</p><p>$4a \\times 3ab = 12a^2b$, &nbsp; $\\dfrac{12xy}{4x} = 3y$</p><p>$a(b + c) = ab + ac$, &nbsp; $-(x - 5) = -x + 5$</p><p>Factorise: take out the HCF, check by expanding.</p></div>'
        '<div class="sbox" style="--c:#c8382e"><h4>Index laws</h4><p>$a^m \\times a^n = a^{m+n}$</p><p>$a^m \\div a^n = a^{m-n}$</p><p>$(a^m)^n = a^{mn}$, &nbsp; $(ab)^n = a^nb^n$</p><p>$a^0 = 1$</p></div>'
        '<div class="sbox" style="--c:#2b8a3e"><h4>Pythagoras</h4><p>$c^2 = a^2 + b^2$ ($c$ = hypotenuse)</p><p>Shorter side: $a^2 = c^2 - b^2$</p><p>Triads: $3,4,5$; $5,12,13$; $8,15,17$; $7,24,25$</p><p>$\\sqrt{ab} = \\sqrt a \\times \\sqrt b$</p></div>'
        '<div class="sbox" style="--c:#d9480f"><h4>Equations</h4><p>Do the same inverse operation to both sides.</p><p>Pronumerals on both sides: collect them on one side first.</p><p>$x^2 = c \\Rightarrow x = \\pm\\sqrt c$</p><p>Always check by substituting.</p></div>'
        '<div class="sbox wide" style="--c:#c2255c"><h4>Area and volume</h4>'
        '<p>$A = lb$ &nbsp;·&nbsp; $A = \\tfrac12 bh$ &nbsp;·&nbsp; $A = bh$ (parallelogram) &nbsp;·&nbsp; $A = \\tfrac h2 (a + b)$ (trapezium) &nbsp;·&nbsp; $A = \\tfrac12 xy$ (kite, rhombus)</p>'
        '<p>Prism: $V = Ah$ &nbsp;·&nbsp; Cylinder: $V = \\pi r^2 h$ &nbsp;·&nbsp; units: $\\text{cm}^2$ for area, $\\text{cm}^3$ for volume</p></div>'
        '</div>'
        '<div class="watch"><h4>Watch out! Common mistakes</h4><div class="wgrid">'
        '<p>✗ $3x + 2y = 5xy$ &nbsp;✓ unlike terms stay apart</p>'
        '<p>✗ $-3^2 = 9$ &nbsp;✓ $-3^2 = -9$, but $(-3)^2 = 9$</p>'
        '<p>✗ $-(x - 5) = -x - 5$ &nbsp;✓ $-x + 5$</p>'
        '<p>✗ $2^3 \\times 2^4 = 4^7$ &nbsp;✓ $2^7$ (add indices, keep the base)</p>'
        '<p>✗ $5^0 = 0$ &nbsp;✓ $5^0 = 1$</p>'
        '<p>✗ $x^2 = 36 \\Rightarrow x = 6$ &nbsp;✓ $x = \\pm 6$</p>'
        '<p>✗ $\\sqrt{a^2 + b^2} = a + b$ &nbsp;✓ $\\sqrt{9 + 16} = 5 \\ne 7$</p>'
        '<p>✗ adding to find a shorter side &nbsp;✓ $a^2 = c^2 - b^2$</p>'
        '<p>✗ $2x(6x - 4)$ is “factorised” &nbsp;✓ fully: $4x(3x - 2)$</p>'
        '<p>✗ using the slant side as height &nbsp;✓ use the perpendicular height</p>'
        '</div></div>'
        '<div class="vocab"><h4>Key vocabulary</h4><div class="vgrid">'
        '<p><b>pronumeral</b> a letter standing for a number</p><p><b>coefficient</b> the number in front of a pronumeral, e.g. $5$ in $5x$</p>'
        '<p><b>like terms</b> same pronumerals, same powers</p><p><b>expand</b> remove grouping symbols</p>'
        '<p><b>factorise</b> write as a product, e.g. $3(x + 4)$</p><p><b>HCF</b> highest common factor</p>'
        '<p><b>base, index</b> in $2^5$: base $2$, index $5$</p><p><b>surd</b> a root that is not a whole number, e.g. $\\sqrt{7}$</p>'
        '<p><b>hypotenuse</b> longest side, opposite the right angle</p><p><b>triad</b> three whole numbers with $a^2 + b^2 = c^2$</p>'
        '<p><b>perpendicular height</b> height at right angles to the base</p><p><b>cross-section</b> the uniform face of a prism</p>'
        '</div></div>'
        '<div class="next"><h3>Coming up in Year 9 Advanced</h3><p>Products and factors (binomial products, factorising quadratics) · surds · '
        'index laws with negative and fractional indices · equations and quadratic equations · coordinate geometry · '
        'trigonometry · surface area and volume. Every one of them uses the skills in this booklet.</p></div>')
    return page(inner, num, COL['L4'], 'back')


def student_html():
    for L in LESSONS:
        number_items(L)
    pages = [cover(), howto(2)]
    pages += test_pages('pre', 3)
    p = 5
    for L in LESSONS:
        pages += lesson_pages(L, p)
        p += 3
    pages += test_pages('post', p)
    p += 2
    pages.append(backpage(p))
    return wrap('Bridge to Year 9 Advanced', ''.join(pages))


# ---------------------------------------------------------------- teacher
def teacher_html():
    tot = mix = 0; per = []
    for L in LESSONS:
        t = m_ = 0
        for pg in L['pages']:
            for b in pg:
                if b[0] == 'grid':
                    for it in b[2]:
                        t += 1; m_ += bool(it.tag)
        per.append(m_ / t); tot += t; mix += m_
    nq = sum(1 for L in LESSONS for pg in L['pages'] for b in pg if b[0] in ('grid', 'long') for _ in b[2])
    global STATS
    STATS = (f'{mix} of the {tot} drill questions ({mix/tot:.0%}; {min(per):.0%}–{max(per):.0%} per lesson)')
    NQ = nq
    qs = [sum(len(b[2]) for pg in L['pages'] for b in pg if b[0] in ('grid', 'long')) for L in LESSONS]
    QMIN, QMAX = min(qs), max(qs)
    out = []
    intro = (
        '<header class="banner" style="background-image:url(img/cover.jpg);background-position:center 30%"><div class="shade"></div>'
        '<div class="bn-l"><div class="kick">Teacher copy · answers</div><h1>Bridge to Year 9 Advanced</h1>'
        '<div class="bsub">Year 8 Advanced · 7 × 50-minute lessons · Mandelbrot series</div></div></header>'
        '<div class="tnotes">'
        '<h3>Overview</h3><table class="ov"><tr><th>Booklet pages</th><th>Section</th><th>Core outcomes</th><th>Extension (Gold / ★)</th></tr>'
        '<tr><td>3–4</td><td>Pre-test (20 marks, 20 min)</td><td colspan="2">One question per lesson; use it to decide where each student starts.</td></tr>' +
        ''.join(f'<tr><td>{5 + 3*i}–{7 + 3*i}</td><td>Lesson {L["num"]}: {L["title"]}</td><td>{L["outcomes"]}</td><td>{L["ext"]}</td></tr>'
                for i, L in enumerate(LESSONS)) +
        '<tr><td>26–27</td><td>Post-test (20 marks, 20 min)</td><td colspan="2">Parallel form of the pre-test.</td></tr></table>'
        '<h3>Notes for the teacher</h3><ul>'
        '<li><b>Levels.</b> Bronze = support (nearly everyone unaided), Silver = core Stage 4, Gold = extension (Stage 5 core or Path content, labelled with codes above). MAO-WM-01 applies throughout.</li>'
        '<li><b>★ items.</b> The NCM 8 Advanced textbook teaches some content in Year 8 that the 2022 syllabus places in Stage 5: expanding with negative coefficients (MA5-ALG-C-01) and factorising with a negative HCF (MA5-ALG-P-01). These appear in Silver marked ★. Test Q2b and Q3c also use them.</li>'
        f'<li><b>Interleaving.</b> {STATS} come from an earlier lesson (chip ↺ L1–L6) or from Year 8 topics not taught in the booklet (integers, fractions, percentages, ratios, linear relationships, equations).</li>'
        f'<li><b>Timing.</b> {NQ} questions in total ({QMIN}–{QMAX} per lesson). In 50 minutes most students will finish Bronze and most of Silver; Gold and any leftovers suit early finishers or homework.</li>'
        '<li><b>No calculator.</b> Numbers are chosen so that every question can be done by hand; non-square roots are left exact (e.g. $\\sqrt{74}$) and estimated to 1 d.p. by squaring.</li>'
        '<li><b>Every answer below was checked by computer algebra</b> (expansions, factorisations, solutions, substitutions and all numerical values).</li></ul></div>')
    out.append(f'<div class="tintro">{intro}</div>')
    blocks = []
    for L in LESSONS:
        rows = []
        for pg in L['pages']:
            for b in pg:
                if b[0] == 'round':
                    rows.append(f'<div class="arh {b[1]}"><span class="medal {b[1]}">{b[1]}</span>{ROUND[b[1]][0]}</div>')
                if b[0] == 'grid':
                    rows.append('<div class="agrid">' + ''.join(
                        f'<div><span class="an">{it.n}</span> {it.a}{(" " + chip(it.tag)) if it.tag else ""}</div>' for it in b[2]) + '</div>')
                if b[0] == 'long':
                    rows.append('<div class="along">' + ''.join(
                        f'<div><span class="an">{it.n}</span> {it.a}</div>' for it in b[2]) + '</div>')
        blocks.append(f'<div class="ablock" style="--acc:{COL[L["key"]]}"><h2><span class="tqn" style="--c:{COL[L["key"]]}">{L["num"]}</span>'
                      f'{L["title"]}</h2>{"".join(rows)}</div>')
    rows = ''
    for (qn, qt, lk, parts), (_, _, _, parts2) in zip(A_PRE, A_POST):
        for p1, p2 in zip(parts, parts2):
            rows += f'<tr><td>{qn}{p1["label"]}</td><td>{p1["ans"]}</td><td>{p2["ans"]}</td><td>{p1["marks"]}</td></tr>'
    blocks.append(f'<div class="ablock mgb" style="--acc:{COL["T"]}"><h2>Pre-test and post-test – marking guide (20 marks each)</h2>'
                  f'<table class="mg"><tr><th>Q</th><th>Pre-test answer</th><th>Post-test answer</th><th>Mark</th></tr>{rows}</table>'
                  f'<p class="small">Award the mark for the correct final answer; accept equivalent forms (e.g. $5\\sqrt3$ for $\\sqrt{{75}}$). '
                  f'In Q3 a correct but not fully factorised answer scores 0, because "factorise fully" is the skill tested. '
                  f'Q2b and Q3c use negative coefficients (★, Stage 5 A in the syllabus but taught in NCM 8 Advanced).</p></div>')
    out.append(f'<section class="flow">{"".join(blocks)}</section>')
    return wrap('Bridge to Year 9 Advanced – Teacher answers', ''.join(out), teacher=True)


def wrap(title, body, teacher=False):
    css = open(os.path.join(HERE, 'style.css')).read()
    return (f'<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><title>{title}</title>'
            f'<link rel="stylesheet" href="node_modules/katex/dist/katex.min.css"><style>{css}</style></head>'
            f'<body class="{"teacher" if teacher else "student"}">{body}'
            + ('<style>@page{margin:11mm 11mm 13mm}</style>' if teacher else '') +
            '<script src="node_modules/katex/dist/katex.min.js"></script>'
            '<script src="node_modules/katex/dist/contrib/auto-render.min.js"></script>'
            '<script>renderMathInElement(document.body,{delimiters:[{left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false}],throwOnError:true});'
            'document.body.dataset.ready=1;</script></body></html>')


if __name__ == '__main__':
    if ERRORS:
        print('CONTENT ERRORS:')
        for e in ERRORS:
            print(' -', e)
        sys.exit(1)
    open(os.path.join(HERE, 'student.html'), 'w').write(student_html())
    open(os.path.join(HERE, 'teacher.html'), 'w').write(teacher_html())
    print('ok')
