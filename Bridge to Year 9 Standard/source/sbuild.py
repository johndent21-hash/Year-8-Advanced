import sys, os, re, html, json
sys.path.insert(0, os.path.dirname(__file__))
import content_s1 as A, content_s2 as B
from dsl import ERRORS
from svg import right_tri

HERE = os.path.dirname(os.path.abspath(__file__))
LESSONS = [A.L1, A.L2, A.L3, A.L4, B.L5, B.L6, B.L7]
COL = {'L1': '#2f5fd0', 'L2': '#0c8a7e', 'L3': '#7f34c4', 'L4': '#c8382e', 'L5': '#2b8a3e',
       'L6': '#d9480f', 'L7': '#c2255c', 'T': '#3d4a5c'}
TOPIC = {'Int': 'Integers', 'Frac': 'Fractions', '%': 'Percentages', 'Ratio': 'Ratios', 'Lin': 'Linear', 'Eq': 'Equations', 'Ang': 'Angles', 'Data': 'Data'}
ROUND = {'B': ('Bronze round', 'Support · everyone starts here'),
         'S': ('Silver round', 'Core · aim to finish this round'),
         'G': ('Gold round', 'Challenge · stretch yourself')}
FOOT = 'Kingscliff High School · Year 8 Mathematics · Bridge to Year 9'


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
                   f'<span class="q">{it.q}</span>{star(it)}</div>'
                   + (f'<div class="scaf">$\\displaystyle {it.scaf}$</div>' if getattr(it, 'scaf', None) else '')
                   + f'<div class="aline">{chip(it.tag)}</div></div>')
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


def render_ideas(L, teacher=False):
    lis = ''.join(f'<li>{x}</li>' for x in L['ideas'])
    if teacher:
        exs = ''.join(f'<div class="ex"><div class="exq"><b>Example {i+1}</b> {q}</div>'
                      f'<div class="exa">$\\begin{{aligned}}{a}\\end{{aligned}}$</div></div>'
                      for i, (q, a) in enumerate(L['examples']))
        return exs
    exs = ''.join(f'<div class="ex tl"><div class="exq"><b>Example {i+1}</b> {q}</div><div class="exspace"></div></div>'
                  for i, (q, a) in enumerate(L['examples']))
    return (f'<div class="ideas"><div class="ki"><h3>Key ideas</h3><ul>{lis}</ul></div>'
            f'<div class="we"><h3>Examples <span class="tlnote">– your teacher will work these with you</span></h3>{exs}</div></div>')


def vocab_strip(L):
    return ('<div class="vstrip"><span class="vh">Key words</span>' +
            ''.join(f'<span class="vw"><b>{w}</b> {d}</span>' for w, d in L['vocab']) + '</div>')


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
                f'<div class="bn-r"><span>50 min</span><span>Calculator allowed</span></div></header>'
                f'<div class="outc"><b>Outcomes:</b> {L["outcomes"]} · MAO-WM-01 &nbsp;|&nbsp; {L["ext"]}'
                f'<span class="book">{L["book"]}</span></div>' + vocab_strip(L))
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
            f'<div class="bn-l"><div class="kick">Bridge to Year 9</div><h1>{title}</h1>'
            f'<div class="bsub">{blurb}</div></div>'
            f'<div class="bn-r"><span>20 marks</span><span>20 minutes</span><span>Calculator allowed</span></div></header>'
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
            '<h1>Bridge to<br>Year 9</h1>'
            '<p class="csub">Seven lessons to revise and strengthen the Year 8 number, algebra, Pythagoras and measurement skills that Year 9 is built on.</p>'
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
        '<p>Each lesson starts with <b>key words</b>, <b>key ideas</b> and <b>examples</b> that your teacher works through with you, then three rounds of questions that get harder as you go.</p>'
        '<div class="rrow"><span class="medal B">B</span><div><b>Bronze – support.</b> Quick drill questions. Everyone starts here; most should be done without help.</div></div>'
        '<div class="rrow"><span class="medal S">S</span><div><b>Silver – core.</b> Multi-step questions and worded problems. Aim to finish this round.</div></div>'
        '<div class="rrow"><span class="medal G">G</span><div><b>Gold – challenge.</b> Harder problems that make you think. Try them once Silver is done.</div></div>'
        '<h3>Mixed questions</h3>'
        f'<p>Questions with a chip like {chip("L2")} come from an <b>earlier lesson</b>; chips like {chip("%")} revisit <b>other Year 8 topics</b>. '
        'Mixing topics feels harder, but it makes what you learn last much longer.</p>'
        '<h3>Help along the way</h3>'
        '<p>Some Bronze questions have the <b>first step done for you</b> in grey – finish them off.</p>'
        '<p><b>Calculators are allowed.</b> Write down what you put into the calculator, and round only at the last step.</p>'
        '<p>Write your working in the spaces provided.</p>'
        '<div class="calc"><h4>Calculator tips</h4><ul>'
        '<li>Put negatives in brackets: $(-3)^2 = 9$ but $-3^2 = -9$.</li>'
        '<li>Use the fraction key for fractions and mixed numbers.</li>'
        '<li>Use the $\\pi$ key, not $3.14$.</li>'
        '<li>Use $x^2$ and $\\sqrt{\\phantom{x}}$ for Pythagoras: $\\sqrt{(6^2 + 8^2)}$.</li>'
        '<li>Round only at the end, and say how you rounded (e.g. 1 d.p.).</li>'
        '<li>Estimate first, so you can spot a wrong key press.</li></ul></div></div>'
        '<div class="hcol"><h3>My progress</h3><table class="track"><tr><th>Lesson</th><th>Syllabus</th><th>B</th><th>S</th><th>G</th><th>Confidence (circle)</th></tr>'
        f'{rows}</table>'
        '<div class="scores"><div><span>Pre-test</span><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 20</b></div><div><span>Post-test</span><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 20</b></div></div>'
        '<h3>A 50-minute lesson</h3><div class="timeline">'
        '<div style="flex:5"><b>0–5</b>Key ideas &amp; examples</div><div class="B" style="flex:13"><b>5–18</b>Bronze round</div>'
        '<div class="S" style="flex:22"><b>18–40</b>Silver round</div><div class="G" style="flex:10"><b>40–50</b>Gold · check answers</div></div>'
        '<p class="small">Finished early? Go straight to Gold. Stuck? Look back at the examples you did with your teacher, then ask.</p>'
        '<h3>Getting the most out of it</h3><ul class="tips">'
        '<li>Try every question before asking for help – a wrong attempt teaches more than a blank.</li>'
        '<li>Show your working: in Year 9 many marks are for method.</li>'
        '<li>Check answers with your teacher; circle any you got wrong and redo them a few days later.</li>'
        '<li>Mixed (↺) questions are meant to make you stop and think “which skill is this?”</li></ul>'
        '<h3>Why Mandelbrot?</h3><p class="small">Every banner in this booklet is a zoom into the Mandelbrot set, drawn by repeating one '
        'tiny rule, $z \\to z^2 + c$, over and over. Simple algebra, repeated carefully, builds something extraordinary – which is '
        'exactly what Year 9 will ask of you.</p></div></div>')
    return page(inner, num, COL['L1'], 'howto')


def backpage(num):
    inner = (
        '<header class="mini tall" style="background-image:url(img/L4.jpg)"><div class="shade"></div><span>Summary sheet</span></header>'
        '<div class="summ">'
        '<div class="sbox" style="--c:#2f5fd0"><h4>Number</h4><p>Same signs $\\to +$, different signs $\\to -$ (for $\\times$, $\\div$)</p><p>$\\tfrac{a}{b} + \\tfrac{c}{d}$: common denominator first</p><p>Increase by $15\\%$: $\\times 1.15$ · decrease by $20\\%$: $\\times 0.8$</p><p>Round: next digit $5$ or more rounds up</p></div>'
        '<div class="sbox" style="--c:#0c8a7e"><h4>Algebra</h4><p>Like terms: same pronumerals, same powers</p><p>$4a \\times 3b = 12ab$, &nbsp; $\\dfrac{12xy}{4x} = 3y$</p><p>Expand: $a(b + c) = ab + ac$</p><p>Factorise: take out the HCF, check by expanding</p></div>'
        '<div class="sbox" style="--c:#c8382e"><h4>Index laws</h4><p>$a^m \\times a^n = a^{m+n}$ &nbsp; $a^m \\div a^n = a^{m-n}$</p><p>$(a^m)^n = a^{mn}$ &nbsp; $a^0 = 1$</p><p>Square root: $\\sqrt{49} = 7$ because $7^2 = 49$</p></div>'
        '<div class="sbox" style="--c:#2b8a3e"><h4>Pythagoras</h4><p>$c^2 = a^2 + b^2$ ($c$ = hypotenuse)</p><p>Shorter side: $a^2 = c^2 - b^2$</p><p>Triads: $3,4,5$; $5,12,13$; $8,15,17$</p></div>'
        '<div class="sbox" style="--c:#d9480f"><h4>Equations</h4><p>Do the same inverse operation to both sides</p><p>Pronumerals on both sides: collect them on one side first</p><p>$x^2 = c \\Rightarrow x = \\pm\\sqrt c$ · always check</p></div>'
        '<div class="sbox" style="--c:#c2255c"><h4>Area and volume</h4><p>$A = lb$ · $A = \\tfrac12 bh$ · $A = bh$ · $A = \\tfrac h2 (a + b)$</p><p>Kite $A = \\tfrac12 xy$ · circle $A = \\pi r^2$</p><p>Prism $V = Ah$ · cylinder $V = \\pi r^2 h$</p></div>'
        '</div>'
        '<div class="watch"><h4>Watch out! Common mistakes</h4><div class="wgrid">'
        '<p>✗ $3x + 2y = 5xy$ &nbsp;✓ unlike terms stay apart</p>'
        '<p>✗ $-3 - 6 = -3$ &nbsp;✓ $-9$</p>'
        '<p>✗ $2(x + 5) = 2x + 5$ &nbsp;✓ $2x + 10$</p>'
        '<p>✗ $2^3 \\times 2^4 = 4^7$ &nbsp;✓ $2^7$ (keep the base)</p>'
        '<p>✗ $5^0 = 0$ &nbsp;✓ $5^0 = 1$</p>'
        '<p>✗ $x^2 = 36 \\Rightarrow x = 6$ only &nbsp;✓ $x = \\pm 6$</p>'
        '<p>✗ adding to find a shorter side &nbsp;✓ subtract</p>'
        '<p>✗ using the slant side as height &nbsp;✓ perpendicular height</p>'
        '</div></div>'
        '<div class="notes"><h4>My notes</h4></div>'
        '<div class="next"><h3>Coming up in Year 9</h3><p>Algebra (expanding and simplifying), indices, equations, '
        'Pythagoras and trigonometry, financial maths, surface area and volume, data and probability. '
        'Every one of them uses the skills in this booklet.</p></div>')
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
    return wrap('Bridge to Year 9', ''.join(pages))


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
        '<div class="bn-l"><div class="kick">Teacher copy · examples and answers</div><h1>Bridge to Year 9</h1>'
        '<div class="bsub">Year 8 mixed-ability class → Year 9 Standard (Stage 5 core) · 7 × 50-minute lessons · Mandelbrot series</div></div></header>'
        '<div class="tnotes">'
        '<h3>Overview</h3><table class="ov"><tr><th>Booklet pages</th><th>Section</th><th>Core outcomes</th><th>Gold round</th></tr>'
        '<tr><td>3–4</td><td>Pre-test (20 marks, 20 min)</td><td colspan="2">One question per lesson; use it to decide where each student starts.</td></tr>' +
        ''.join(f'<tr><td>{5 + 3*i}–{7 + 3*i}</td><td>Lesson {L["num"]}: {L["title"]}</td><td>{L["outcomes"]}</td><td>{L["ext"]}</td></tr>'
                for i, L in enumerate(LESSONS)) +
        '<tr><td>26–27</td><td>Post-test (20 marks, 20 min)</td><td colspan="2">Parallel form of the pre-test.</td></tr></table>'
        '<h3>Notes for the teacher</h3><ul>'
        '<li><b>Levels.</b> Bronze = support (nearly everyone unaided; some questions show the first step), Silver = core Stage 4, Gold = harder multi-step Stage 4 problems. No Stage 5 content is included. MAO-WM-01 applies throughout.</li>'
        '<li><b>Examples are teacher-led.</b> The student copy shows each example question with blank space so you can work it live; the full working is in the box for each lesson below.</li>'
        '<li><b>Stage 4 only.</b> Expanding and factorising use single brackets with a positive term outside; negative coefficients, binomial products, surds and changing the subject (all Stage 5) are left for Year 9.</li>'
        f'<li><b>Interleaving.</b> {STATS} come from an earlier lesson (chip ↺ L1–L6) or from Year 8 topics not taught in the booklet (integers, fractions, percentages, ratios, linear relationships, equations).</li>'
        f'<li><b>Timing.</b> {NQ} questions in total ({QMIN}–{QMAX} per lesson). In 50 minutes most students will finish Bronze and most of Silver; Gold and any leftovers suit early finishers or homework.</li>'
        '<li><b>Calculator allowed.</b> Answers that need rounding say how many decimal places; answers were rounded only at the last step.</li>'
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
                      f'{L["title"]}</h2><div class="twe"><div class="twh">Examples (worked)</div>{render_ideas(L, teacher=True)}</div>{"".join(rows)}</div>')
    rows = ''
    for (qn, qt, lk, parts), (_, _, _, parts2) in zip(A_PRE, A_POST):
        for p1, p2 in zip(parts, parts2):
            rows += f'<tr><td>{qn}{p1["label"]}</td><td>{p1["ans"]}</td><td>{p2["ans"]}</td><td>{p1["marks"]}</td></tr>'
    blocks.append(f'<div class="ablock mgb" style="--acc:{COL["T"]}"><h2>Pre-test and post-test – marking guide (20 marks each)</h2>'
                  f'<table class="mg"><tr><th>Q</th><th>Pre-test answer</th><th>Post-test answer</th><th>Mark</th></tr>{rows}</table>'
                  f'<p class="small">Award the mark for the correct final answer; accept equivalent forms and correct rounding of a correct method. '
                  f'In Q3c a correct but not fully factorised answer scores 0, because factorising fully is the skill tested.</p></div>')
    out.append(f'<section class="flow">{"".join(blocks)}</section>')
    return wrap('Bridge to Year 9 – Teacher copy', ''.join(out), teacher=True)


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
