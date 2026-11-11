s = open('build.py').read()

def rep(old, new, count=1):
    global s
    assert s.count(old) >= 1, 'NOT FOUND: ' + old[:70]
    s = s.replace(old, new) if count == 0 else s.replace(old, new, count)

def between(start, end, new):
    global s
    i = s.index(start); j = s.index(end, i)
    s = s[:i] + new + s[j:]

rep("import content_a as A, content_b as B", "import content_s1 as A, content_s2 as B")
rep("TOPIC = {'Int': 'Integers', 'Frac': 'Fractions', '%': 'Percentages', 'Ratio': 'Ratios', 'Lin': 'Linear', 'Eq': 'Equations'}",
    "TOPIC = {'Int': 'Integers', 'Frac': 'Fractions', '%': 'Percentages', 'Ratio': 'Ratios', 'Lin': 'Linear', 'Eq': 'Equations', 'Ang': 'Angles', 'Data': 'Data'}")
rep("FOOT = 'Kingscliff High School · Year 8 Advanced · Bridge to Year 9 Advanced'", "FOOT = 'Kingscliff High School · Year 8 Mathematics · Bridge to Year 9'")
rep("'S': ('Silver round', 'Core · aim to finish this round'),", "'S': ('Silver round', 'Core · aim to finish this round'),")
rep("'G': ('Gold round', 'Extension · stretch yourself')}", "'G': ('Gold round', 'Challenge · stretch yourself')}")

# partly worked step in grid cells
rep("""f'<span class="q">{it.q}</span>{star(it)}</div><div class="aline">{chip(it.tag)}</div></div>')""",
    """f'<span class="q">{it.q}</span>{star(it)}</div>'
                   + (f'<div class="scaf">$\\\\displaystyle {it.scaf}$</div>' if getattr(it, 'scaf', None) else '')
                   + f'<div class="aline">{chip(it.tag)}</div></div>')""")

# teacher-led examples + vocab strip
between("def render_ideas(L):", "def round_head(code):", '''def render_ideas(L, teacher=False):
    lis = ''.join(f'<li>{x}</li>' for x in L['ideas'])
    if teacher:
        exs = ''.join(f'<div class="ex"><div class="exq"><b>Example {i+1}</b> {q}</div>'
                      f'<div class="exa">$\\\\begin{{aligned}}{a}\\\\end{{aligned}}$</div></div>'
                      for i, (q, a) in enumerate(L['examples']))
        return exs
    exs = ''.join(f'<div class="ex tl"><div class="exq"><b>Example {i+1}</b> {q}</div><div class="exspace"></div></div>'
                  for i, (q, a) in enumerate(L['examples']))
    return (f'<div class="ideas"><div class="ki"><h3>Key ideas</h3><ul>{lis}</ul></div>'
            f'<div class="we"><h3>Examples <span class="tlnote">– your teacher will work these with you</span></h3>{exs}</div></div>')


def vocab_strip(L):
    return ('<div class="vstrip"><span class="vh">Key words</span>' +
            ''.join(f'<span class="vw"><b>{w}</b> {d}</span>' for w, d in L['vocab']) + '</div>')


''')
rep("""f'<div class="bn-r"><span>50 min</span><span>No calculator</span></div></header>'""",
    """f'<div class="bn-r"><span>50 min</span><span>Calculator allowed</span></div></header>'""")
rep("""                f'<span class="book">{L["book"]}</span></div>')""",
    """                f'<span class="book">{L["book"]}</span></div>' + vocab_strip(L))""")
rep("""f'<div class="bn-l"><div class="kick">Bridge to Year 9 Advanced</div><h1>{title}</h1>'""",
    """f'<div class="bn-l"><div class="kick">Bridge to Year 9</div><h1>{title}</h1>'""")
rep("""f'<div class="bn-r"><span>20 marks</span><span>20 minutes</span><span>No calculator</span></div></header>'""",
    """f'<div class="bn-r"><span>20 marks</span><span>20 minutes</span><span>Calculator allowed</span></div></header>'""")

between("def cover():", "def howto(num):", '''def cover():
    return ('<section class="page cover"><div class="cimg" style="background-image:url(img/cover.jpg)"></div>'
            '<div class="cshade"></div><div class="ctext">'
            '<div class="ckick">Kingscliff High School · Mathematics</div>'
            '<div class="cseries">Mandelbrot series</div>'
            '<h1>Bridge to<br>Year 9</h1>'
            '<p class="csub">Seven lessons to revise and strengthen the Year 8 number, algebra, Pythagoras and measurement skills that Year 9 is built on.</p>'
            '<div class="ctopics">' + ''.join(
                f'<span style="--c:{COL[L["key"]]}"><b>{L["num"]}</b>{L["title"]}</span>' for L in LESSONS) +
            '</div><div class="cname"><span>Name</span><span>Class</span><span>Teacher</span></div></div></section>')


''')
# how-to edits
rep("'<p>Each lesson starts with <b>key ideas</b> and <b>worked examples</b>, then three rounds of questions that get harder as you go.</p>'",
    "'<p>Each lesson starts with <b>key words</b>, <b>key ideas</b> and <b>examples</b> that your teacher works through with you, then three rounds of questions that get harder as you go.</p>'")
rep("'<div class=\"rrow\"><span class=\"medal S\">S</span><div><b>Silver – core.</b> Multi-step drill and worded problems. This is the standard for Year 9 Advanced.</div></div>'",
    "'<div class=\"rrow\"><span class=\"medal S\">S</span><div><b>Silver – core.</b> Multi-step questions and worded problems. Aim to finish this round.</div></div>'")
rep("'<div class=\"rrow\"><span class=\"medal G\">G</span><div><b>Gold – extension.</b> Harder problems and a preview of Year 9 ideas. Try them once Silver is done.</div></div>'",
    "'<div class=\"rrow\"><span class=\"medal G\">G</span><div><b>Gold – challenge.</b> Harder problems that make you think. Try them once Silver is done.</div></div>'")
between("        '<h3>Symbols</h3>'", "        '<div class=\"hcol\"><h3>My progress</h3>", '''        '<h3>Help along the way</h3>'
        '<p>Some Bronze questions have the <b>first step done for you</b> in grey – finish them off.</p>'
        '<p><b>Calculators are allowed.</b> Write down what you put into the calculator, and round only at the last step.</p>'
        '<p>Write your working in the spaces provided.</p></div>'
''')
rep("'<li>Show your working: in Year 9 Advanced most marks are for method.</li>'", "'<li>Show your working: in Year 9 many marks are for method.</li>'")
rep("'exactly what Year 9 Advanced will ask of you.</p></div></div>')", "'exactly what Year 9 will ask of you.</p></div></div>')")
rep("'<p class=\"small\">Finished early? Go straight to Gold. Stuck? Re-read the worked examples, then ask.</p>'",
    "'<p class=\"small\">Finished early? Go straight to Gold. Stuck? Look back at the examples you did with your teacher, then ask.</p>'")

between("def backpage(num):", "def student_html():", '''def backpage(num):
    inner = (
        '<header class="mini tall" style="background-image:url(img/L4.jpg)"><div class="shade"></div><span>Summary sheet</span></header>'
        '<div class="summ">'
        '<div class="sbox" style="--c:#2f5fd0"><h4>Number</h4><p>Same signs $\\\\to +$, different signs $\\\\to -$ (for $\\\\times$, $\\\\div$)</p><p>$\\\\tfrac{a}{b} + \\\\tfrac{c}{d}$: common denominator first</p><p>Increase by $15\\\\%$: $\\\\times 1.15$ · decrease by $20\\\\%$: $\\\\times 0.8$</p><p>Round: next digit $5$ or more rounds up</p></div>'
        '<div class="sbox" style="--c:#0c8a7e"><h4>Algebra</h4><p>Like terms: same pronumerals, same powers</p><p>$4a \\\\times 3b = 12ab$, &nbsp; $\\\\dfrac{12xy}{4x} = 3y$</p><p>Expand: $a(b + c) = ab + ac$</p><p>Factorise: take out the HCF, check by expanding</p></div>'
        '<div class="sbox" style="--c:#c8382e"><h4>Index laws</h4><p>$a^m \\\\times a^n = a^{m+n}$ &nbsp; $a^m \\\\div a^n = a^{m-n}$</p><p>$(a^m)^n = a^{mn}$ &nbsp; $a^0 = 1$</p><p>Square root: $\\\\sqrt{49} = 7$ because $7^2 = 49$</p></div>'
        '<div class="sbox" style="--c:#2b8a3e"><h4>Pythagoras</h4><p>$c^2 = a^2 + b^2$ ($c$ = hypotenuse)</p><p>Shorter side: $a^2 = c^2 - b^2$</p><p>Triads: $3,4,5$; $5,12,13$; $8,15,17$</p></div>'
        '<div class="sbox" style="--c:#d9480f"><h4>Equations</h4><p>Do the same inverse operation to both sides</p><p>Pronumerals on both sides: collect them on one side first</p><p>$x^2 = c \\\\Rightarrow x = \\\\pm\\\\sqrt c$ · always check</p></div>'
        '<div class="sbox" style="--c:#c2255c"><h4>Area and volume</h4><p>$A = lb$ · $A = \\\\tfrac12 bh$ · $A = bh$ · $A = \\\\tfrac h2 (a + b)$</p><p>Kite $A = \\\\tfrac12 xy$ · circle $A = \\\\pi r^2$</p><p>Prism $V = Ah$ · cylinder $V = \\\\pi r^2 h$</p></div>'
        '</div>'
        '<div class="watch"><h4>Watch out! Common mistakes</h4><div class="wgrid">'
        '<p>✗ $3x + 2y = 5xy$ &nbsp;✓ unlike terms stay apart</p>'
        '<p>✗ $-3 - 6 = -3$ &nbsp;✓ $-9$</p>'
        '<p>✗ $2(x + 5) = 2x + 5$ &nbsp;✓ $2x + 10$</p>'
        '<p>✗ $2^3 \\\\times 2^4 = 4^7$ &nbsp;✓ $2^7$ (keep the base)</p>'
        '<p>✗ $5^0 = 0$ &nbsp;✓ $5^0 = 1$</p>'
        '<p>✗ $x^2 = 36 \\\\Rightarrow x = 6$ only &nbsp;✓ $x = \\\\pm 6$</p>'
        '<p>✗ adding to find a shorter side &nbsp;✓ subtract</p>'
        '<p>✗ using the slant side as height &nbsp;✓ perpendicular height</p>'
        '</div></div>'
        '<div class="next"><h3>Coming up in Year 9</h3><p>Algebra (expanding and simplifying), indices, equations, '
        'Pythagoras and trigonometry, financial maths, surface area and volume, data and probability. '
        'Every one of them uses the skills in this booklet.</p></div>')
    return page(inner, num, COL['L4'], 'back')


''')
rep("return wrap('Bridge to Year 9 Advanced', ''.join(pages))", "return wrap('Bridge to Year 9', ''.join(pages))")

# teacher copy
rep("'<div class=\"bn-l\"><div class=\"kick\">Teacher copy · answers</div><h1>Bridge to Year 9 Advanced</h1>'",
    "'<div class=\"bn-l\"><div class=\"kick\">Teacher copy · examples and answers</div><h1>Bridge to Year 9</h1>'")
rep("'<div class=\"bsub\">Year 8 Advanced · 7 × 50-minute lessons · Mandelbrot series</div></div></header>'",
    "'<div class=\"bsub\">Year 8 mixed-ability class → Year 9 Standard (Stage 5 core) · 7 × 50-minute lessons · Mandelbrot series</div></div></header>'")
rep("<th>Extension (Gold / ★)</th>", "<th>Gold round</th>")
between("        '<li><b>Levels.</b>", "        f'<li><b>Interleaving.</b>", '''        '<li><b>Levels.</b> Bronze = support (nearly everyone unaided; some questions show the first step), Silver = core Stage 4, Gold = harder multi-step Stage 4 problems. No Stage 5 content is included. MAO-WM-01 applies throughout.</li>'
        '<li><b>Examples are teacher-led.</b> The student copy shows each example question with blank space so you can work it live; the full working is in the box for each lesson below.</li>'
        '<li><b>Stage 4 only.</b> Expanding and factorising use single brackets with a positive term outside; negative coefficients, binomial products, surds and changing the subject (all Stage 5) are left for Year 9.</li>'
''')
rep("'<li><b>No calculator.</b> Numbers are chosen so that every question can be done by hand; non-square roots are left exact (e.g. $\\\\sqrt{74}$) and estimated to 1 d.p. by squaring.</li>'",
    "'<li><b>Calculator allowed.</b> Answers that need rounding say how many decimal places; answers were rounded only at the last step.</li>'")
rep("""        blocks.append(f'<div class="ablock" style="--acc:{COL[L["key"]]}"><h2><span class="tqn" style="--c:{COL[L["key"]]}">{L["num"]}</span>'
                      f'{L["title"]}</h2>{"".join(rows)}</div>')""",
    """        blocks.append(f'<div class="ablock" style="--acc:{COL[L["key"]]}"><h2><span class="tqn" style="--c:{COL[L["key"]]}">{L["num"]}</span>'
                      f'{L["title"]}</h2><div class="twe"><div class="twh">Examples (worked)</div>{render_ideas(L, teacher=True)}</div>{"".join(rows)}</div>')""")
rep("""                  f'<p class="small">Award the mark for the correct final answer; accept equivalent forms (e.g. $5\\\\sqrt3$ for $\\\\sqrt{{75}}$). '
                  f'In Q3 a correct but not fully factorised answer scores 0, because "factorise fully" is the skill tested. '
                  f'Q2b and Q3c use negative coefficients (★, Stage 5 A in the syllabus but taught in NCM 8 Advanced).</p></div>')""",
    """                  f'<p class="small">Award the mark for the correct final answer; accept equivalent forms and correct rounding of a correct method. '
                  f'In Q3c a correct but not fully factorised answer scores 0, because factorising fully is the skill tested.</p></div>')""")
rep("return wrap('Bridge to Year 9 Advanced – Teacher answers', ''.join(out), teacher=True)", "return wrap('Bridge to Year 9 – Teacher copy', ''.join(out), teacher=True)")
open('sbuild.py', 'w').write(s)
print('patched')
