import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import content as C
from dsl import ERRORS

WEEKCOL = {1: '#0a8a99', 2: '#c2416b', 3: '#2f9e44', 4: '#e8590c', 5: '#1c64d6', 6: '#e8505b'}
GROUP = {'num': ('#e8590c', 'Number'), 'ind': ('#c2255c', 'Indices & roots'), 'alg': ('#1971c2', 'Algebra'),
         'eq': ('#6741d9', 'Equations'), 'meas': ('#099268', 'Measurement'), 'lin': ('#0b7285', 'Linear'),
         'geo': ('#5c940d', 'Angles & chance'), 'ctx': ('#495057', 'In context')}
FOOT = 'Kingscliff High School · Summer Maths: Ready for Year 9'
KATEX = 'node_modules/katex/dist/'


def page(inner, num, col, cls=''):
    return (f'<section class="page {cls}" style="--acc:{col}">{inner}'
            f'<footer><span>{FOOT}</span><span class="pn">{num}</span></footer></section>')


def wave(col='#fff'):
    return (f'<svg class="wave" viewBox="0 0 210 8" preserveAspectRatio="none"><path d="M0 5 C 25 0, 45 9, 70 4 S 115 0, 140 4 '
            f'S 185 9, 210 3 L210 8 L0 8 Z" fill="{col}"/></svg>')


def cell(it):
    gcol, _ = GROUP[it.slot[0]]
    star = '<span class="star">★</span>' if it.star else ''
    diag = f'<div class="dg">{it.diag}</div>' if it.diag else ''
    cls = ' hasdg' if it.diag else ''
    return (f'<div class="qc{cls}" style="--g:{gcol}"><div class="qh"><span class="qn">{it.n}</span>'
            f'<span class="tp">{it.slot[1]}</span>{star}</div>'
            f'<div class="qb"><div class="qt">{it.q}</div>{diag}</div><div class="wk"></div></div>')


def week_page(wk, num):
    n = wk['n']
    col = WEEKCOL[n]
    head = (f'<header class="wband" style="background-image:url(img/W{n}.jpg)">'
            f'<div class="wlabel"><span class="wk-k">Week</span><span class="wk-n">{n}</span>'
            f'<span class="wk-t">Summer Maths<br><b>Ready for Year 9</b></span></div>'
            f'<div class="wcard"><div>Date started <span class="ln"></span></div>'
            f'<div>Score <span class="sc"></span> / 20</div><div>Done <span class="box"></span> &nbsp; Bonus <span class="box"></span></div></div>'
            f'{wave()}</header>')
    legend = ('<div class="legend">' + ''.join(f'<span style="--g:{c}">{t}</span>' for c, t in GROUP.values()) +
              '<span class="lg-r"><span class="star">★</span> Year 9 preview (Stage 5) · No calculator</span></div>')
    its = wk['items']
    grid = ('<div class="qgrid"><div class="qcol">' + ''.join(cell(it) for it in its[:10]) + '</div>'
            '<div class="qcol">' + ''.join(cell(it) for it in its[10:]) + '</div></div>')
    b = wk['bonus']
    bonus = (f'<div class="bonus"><span class="bt">Bonus</span><div class="bq">{b.q}</div><div class="wk"></div></div>')
    return page(head + '<div class="inner">' + legend + grid + bonus + '</div>', num, col, 'week')


def cover():
    chips = ''.join(f'<span style="--c:{WEEKCOL[n]}">Week {n}</span>' for n in range(1, 7))
    return ('<section class="page cover"><div class="cimg"></div><div class="cshade"></div>'
            '<div class="ctop"><span>Kingscliff High School · Mathematics</span><span class="ser">Julia series</span></div>'
            '<div class="ctext"><div class="csm">Year 8 Advanced → Year 9 Advanced</div>'
            '<h1>Summer Maths</h1><div class="csub">Ready for Year 9</div>'
            '<p>Six weeks. Twenty questions a week. Every Year 8 skill that Year 9 Advanced builds on – mixed together so it sticks.</p>'
            f'<div class="cchips">{chips}</div>'
            '<div class="cname"><span>Name</span><span>Class</span></div></div></section>')


def howto(num):
    slots = ''.join(f'<li style="--g:{GROUP[g][0]}"><b>{i+1}</b>{t}</li>' for i, (g, t) in enumerate(C.SLOTS))
    rows = ''.join(f'<tr><td><span class="wdot" style="--c:{WEEKCOL[n]}">{n}</span> Week {n}</td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ 20</td>'
                   f'<td>☐</td><td>☐</td><td></td></tr>' for n in range(1, 7))
    inner = (
        f'<header class="hband" style="background-image:url(img/W1.jpg)"><h2>How it works</h2>{wave()}</header><div class="inner how">'
        '<div class="hgrid"><div>'
        '<h3>One page a week</h3><p>Each week has <b>20 questions</b> and a <b>bonus</b>. Set aside about <b>40 minutes</b> – one sitting or a few short ones. '
        'Questions start easier and get a little harder through the page.</p>'
        '<h3>The same pattern every week</h3><p>Question 1 is always fractions and integers, question 11 is always Pythagoras, and so on. '
        'If the same number keeps going wrong, that is the skill to revise before Year 9.</p>'
        f'<ol class="slots">{slots}</ol>'
        '<div class="julia"><b>Why Julia?</b> Each banner is a <i>Julia set</i>: pick a number $c$, then repeat $z \\to z^2 + c$ '
        'for every point. Points that stay small are coloured in. Change $c$ and you get a completely different shape – the same rule as the '
        'Mandelbrot set, seen from a different angle.</div>'
        '</div><div>'
        '<h3>Rules of the game</h3><ul class="rules">'
        '<li><b>No calculator.</b> Leave answers exact (e.g. $\\sqrt{34}$ or $9\\pi$) unless asked to round.</li>'
        '<li><b>Show working</b> in the box under each question.</li>'
        '<li><b>Mark it yourself</b> using the answers at the back (pages 10–12). Each answer has a line of working to help you find a mistake.</li>'
        '<li><b>Fix it.</b> Redo anything you got wrong a day or two later, without looking.</li>'
        '<li><span class="star">★</span> questions preview Year 9 (Stage 5) work. Have a go – they are the ones that will help most in Term 1.</li>'
        '<li><b>Stuck?</b> The hints page (page 9) has the key facts and formulas.</li></ul>'
        '<h3>My summer tracker</h3><table class="trk"><tr><th>Week</th><th>Date</th><th>Score</th><th>Done</th><th>Bonus</th><th>Revise (Q numbers)</th></tr>'
        f'{rows}</table>'
        '<div class="y9"><b>First up in Year 9 Advanced:</b> products and factors (expanding and factorising), surds and Pythagoras, '
        'indices, equations, trigonometry and coordinate geometry. Every one of them starts from the skills in these six pages.</div>'
        '</div></div></div>')
    return page(inner, num, WEEKCOL[1], 'howto')


def hints(num):
    def box(col, title, lines):
        return f'<div class="hb" style="--c:{col}"><h4>{title}</h4>' + ''.join(f'<p>{l}</p>' for l in lines) + '</div>'
    inner = (f'<header class="hband" style="background-image:url(img/W5.jpg)"><h2>Hints &amp; formulas</h2>{wave()}</header><div class="inner"><div class="hints">'
             + box(GROUP['num'][0], 'Number', [r'$\tfrac{a}{b} + \tfrac{c}{d}$: use a common denominator', r'$\times$: multiply tops and bottoms; $\div$: flip the second, then multiply',
                                              r'Increase by $15\%$: $\times 1.15$ &nbsp; Decrease by $20\%$: $\times 0.8$', r'$\%$ change $= \dfrac{\text{change}}{\text{original}} \times 100\%$',
                                              r'<span class="star">★</span> Significant figures start at the first non-zero digit'])
             + box(GROUP['ind'][0], 'Indices &amp; roots', [r'$a^m \times a^n = a^{m+n}$ &nbsp; $a^m \div a^n = a^{m-n}$', r'$(a^m)^n = a^{mn}$ &nbsp; $(ab)^n = a^nb^n$ &nbsp; $a^0 = 1$',
                                                          r'$\sqrt{ab} = \sqrt a \times \sqrt b$', r'<span class="star">★</span> $\sqrt{50} = \sqrt{25 \times 2} = 5\sqrt2$'])
             + box(GROUP['alg'][0], 'Algebra', [r'Like terms: same letters, same powers', r'$a(b + c) = ab + ac$, &nbsp; $-(x - 5) = -x + 5$',
                                                r'Factorise: take out the HCF, then check by expanding', r'<span class="star">★</span> $(a + b)(c + d) = ac + ad + bc + bd$'])
             + box(GROUP['eq'][0], 'Equations &amp; formulas', [r'Do the same to both sides', r'Unknowns on both sides: collect them on one side first',
                                                               r'$x^2 = c \Rightarrow x = \pm\sqrt c$', r'Formulas: substitute, then solve',
                                                               r'<span class="star">★</span> Change the subject: undo operations in reverse order'])
             + box(GROUP['meas'][0], 'Measurement', [r'Pythagoras: $c^2 = a^2 + b^2$ ($c$ = hypotenuse)',
                                                     r'$A = \tfrac12 bh$ · $A = bh$ · $A = \tfrac h2(a + b)$ · $A = \tfrac12 xy$',
                                                     r'Circle: $C = 2\pi r = \pi d$, &nbsp; $A = \pi r^2$', r'Prism: $V = Ah$ &nbsp; Cylinder: $V = \pi r^2 h$',
                                                     r'$1\ \text{cm}^3 = 1$ mL, &nbsp; $1000\ \text{cm}^3 = 1$ L'])
             + box(GROUP['lin'][0], 'Linear relationships', [r'A point lies on a line if its coordinates satisfy the equation',
                                                            r'<span class="star">★</span> Gradient $m = \dfrac{\text{rise}}{\text{run}} = \dfrac{y_2 - y_1}{x_2 - x_1}$',
                                                            r'<span class="star">★</span> $y = mx + c$: $m$ = gradient, $c$ = $y$-intercept',
                                                            r'Horizontal lines have gradient $0$; uphill (left to right) is positive'])
             + box(GROUP['geo'][0], 'Angles &amp; probability', [r'Straight line $180°$ · point $360°$ · vertically opposite angles are equal',
                                                                r'Parallel lines: corresponding and alternate angles are equal; co-interior add to $180°$',
                                                                r'Triangle $180°$ · quadrilateral $360°$',
                                                                r'$P(E) = \dfrac{\text{favourable outcomes}}{\text{total outcomes}}$, &nbsp; $P(\text{not } E) = 1 - P(E)$'])
             + box(GROUP['ctx'][0], 'Worded problems', ['1. Choose a letter for the unknown and say what it means.', '2. Write an equation from the words.',
                                                       '3. Solve it.', '4. Answer the question in a sentence, with units.'])
             + '</div></div>')
    return page(inner, num, WEEKCOL[5], 'hintsp')


def answers(weeks, num):
    blocks = ''
    for wk in weeks:
        rows = ''.join(f'<div class="ar"><span class="an" style="--g:{GROUP[it.slot[0]][0]}">{it.n}</span>'
                       f'<span class="aa">{it.a}</span><span class="aw">{getattr(it, "w", "")}</span></div>' for it in wk['items'])
        b = wk['bonus']
        brow = (f'<div class="ar bonusr"><span class="an bon">B</span><span class="aa">{b.a}</span><span class="aw">{getattr(b, "w", "")}</span></div>')
        blocks += (f'<div class="ablk" style="--acc:{WEEKCOL[wk["n"]]}"><h3><span class="wdot" style="--c:{WEEKCOL[wk["n"]]}">{wk["n"]}</span>'
                   f'Week {wk["n"]} answers</h3><div class="alist">{rows}</div>{brow}</div>')
    inner = (f'<header class="hband short" style="background-image:url(img/W{weeks[0]["n"]}.jpg)"><h2>Answers</h2>{wave()}</header>'
             f'<div class="inner">{blocks}</div>')
    return page(inner, num, WEEKCOL[weeks[0]['n']], 'ans')


def html():
    pages = [cover(), howto(2)]
    for i, wk in enumerate(C.WEEKS):
        pages.append(week_page(wk, 3 + i))
    pages.append(hints(9))
    pages.append(answers(C.WEEKS[0:2], 10))
    pages.append(answers(C.WEEKS[2:4], 11))
    pages.append(answers(C.WEEKS[4:6], 12))
    css = open(os.path.join(HERE, 'hstyle.css')).read()
    return (f'<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><title>Summer Maths: Ready for Year 9</title>'
            f'<link rel="stylesheet" href="{KATEX}katex.min.css"><style>{css}</style></head><body>{"".join(pages)}'
            f'<script src="{KATEX}katex.min.js"></script><script src="{KATEX}contrib/auto-render.min.js"></script>'
            '<script>renderMathInElement(document.body,{delimiters:[{left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false}],throwOnError:true});'
            'document.body.dataset.ready=1;</script></body></html>')


if __name__ == '__main__':
    if ERRORS:
        print('CONTENT ERRORS:'); [print(' -', e) for e in ERRORS]; sys.exit(1)
    open(os.path.join(HERE, 'holiday.html'), 'w').write(html())
    print('ok')
