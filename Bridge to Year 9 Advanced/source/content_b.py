from dsl import *
from svg import *
import math


def hyp(a, b):
    return math.sqrt(a * a + b * b)


# ======================================================================
# LESSON 5  Square roots, surds and Pythagoras
# ======================================================================
L5 = dict(
    num=5, key='L5', title="Square roots & Pythagoras' theorem",
    sub='Exact and approximate roots · hypotenuse and shorter sides · the converse · triads · surds (Gold)',
    outcomes='MA4-IND-C-01 (roots) · MA4-PYT-C-01',
    ext='Gold: surds MA5-IND-P-02 · length of an interval MA5-LIN-C-01 · 3D Pythagoras MA5-TRG-P-01',
    book='NCM 8 Adv 1.01–1.08, 2.09 → NCM 9 Adv 2.01–2.09',
    ideas=[
        r'The <b>hypotenuse</b> is the longest side, opposite the right angle. <b>Pythagoras:</b> $c^2 = a^2 + b^2$.',
        r'<b>Shorter side:</b> subtract: $a^2 = c^2 - b^2$.',
        r'<b>Exact</b> answers keep the root: $\sqrt{74}$. <b>Estimate</b> a root using squares: $8^2 = 64,\ 9^2 = 81$, so $\sqrt{74}$ is between $8$ and $9$.',
        r'$\sqrt{ab} = \sqrt{a} \times \sqrt{b}$, e.g. $\sqrt{9 \times 16} = 3 \times 4 = 12$.',
        r'<b>Converse:</b> if $c^2 = a^2 + b^2$ (with $c$ the longest side), the triangle is right-angled. Whole-number solutions such as $3, 4, 5$ are <b>Pythagorean triads</b>.',
    ],
    examples=[
        (r'Find $c$ if the shorter sides are $5$ and $12$.', r'c^2 &= 5^2 + 12^2 = 169 \\ c &= \sqrt{169} = 13'),
        (r'Find $x$ if the hypotenuse is $9$ and one side is $5$.', r'x^2 &= 9^2 - 5^2 = 56 \\ x &= \sqrt{56}\ \text{(exact)}'),
        (r'Is a triangle with sides $7, 24, 25$ right-angled?', r'7^2 + 24^2 &= 49 + 576 = 625 \\ 25^2 &= 625 \;\checkmark\ \text{Yes}'),
    ],
)
L5['pages'] = [
    [('ideas',),
     ('round', 'B'),
     ('sub', 'Evaluate, or answer as instructed.'),
     ('grid', 5, [
         S('sqrt(49)', '7'), S('sqrt(144)', '12'), S('(sqrt(13))^2', '13'), S('sqrt(9*16)', '12'), S('cbrt(27)', '3'),
         S('2^3*2^2', '32', tag='L4', verb='Evaluate'), S('7x-2x+x', '6x', tag='L1', verb='Simplify'),
         F('5y+15', '5(y+3)', tag='L3', verb='Factorise'),
         N(r'$\sqrt{30}$ lies between which two whole numbers?', '$5$ and $6$', 25 < 30 < 36),
         N(r'Estimate $\sqrt{30}$ to $1$ d.p. (check by squaring)', r'$5.5$ ($5.4^2 = 29.16$, $5.5^2 = 30.25$)', r(math.sqrt(30), 1) == 5.5),
     ]),
     ('sub', 'Find the length of the hypotenuse, $c$. Leave answers that are not whole numbers in exact form. (Lengths in cm.)'),
     ('grid', 4, [
         N(right_tri(8, 6, '8', '6', 'c'), '$10$ cm', hyp(6, 8) == 10),
         N(right_tri(12, 9, '12', '9', 'c'), '$15$ cm', hyp(9, 12) == 15),
         N(right_tri(15, 8, '15', '8', 'c'), '$17$ cm', hyp(8, 15) == 17),
         N(right_tri(7, 5, '7', '5', 'c'), r'$\sqrt{74}$ cm', 25 + 49 == 74),
     ]),
     ('grid', 2, [
         N(r'Write $0.35$ as a percentage', r'$35\%$', close(0.35 * 100, 35), tag='%'),
         N(r'In $\triangle PQR$, $\angle Q = 90^\circ$. Name the hypotenuse.', r'$PR$', True),
     ]),
     ],
    [('round', 'S'),
     ('sub', 'Find the length of the side marked $x$. Leave answers that are not whole numbers in exact form. (Lengths in cm.)'),
     ('grid', 4, [
         N(right_tri(12, 5, 'x', '5', '13'), '$12$ cm', math.sqrt(13 ** 2 - 5 ** 2) == 12),
         N(right_tri(24, 7, 'x', '7', '25'), '$24$ cm', math.sqrt(25 ** 2 - 7 ** 2) == 24),
         N(right_tri(math.sqrt(84), 4, 'x', '4', '10'), r'$\sqrt{84}$ cm', 100 - 16 == 84),
         N(right_tri(10, 7.5, 'x', '7.5', '12.5'), '$10$ cm', close(math.sqrt(12.5 ** 2 - 7.5 ** 2), 10)),
     ]),
     ('sub', 'Answer each question.'),
     ('grid', 3, [
         N(r'Exact length of the hypotenuse if the shorter sides are $2$ and $3$', r'$\sqrt{13}$', 4 + 9 == 13),
         N(r'Is a triangle with sides $9, 40, 41$ right-angled?', r'Yes: $81 + 1600 = 1681 = 41^2$', 81 + 1600 == 41 ** 2),
         N(r'Is a triangle with sides $6, 9, 11$ right-angled?', r'No: $36 + 81 = 117 \ne 121$', 36 + 81 != 121),
         N(r'Is $20, 21, 29$ a Pythagorean triad?', r'Yes: $400 + 441 = 841 = 29^2$', 400 + 441 == 29 ** 2),
         E('-2(3x-1)', '-6x+2', tag='L2', star=True, verb='Expand'), S('5^0+2^4', '17', tag='L4', verb='Evaluate'),
         S('[3a|4]*[8|a]', '6', tag='L1', verb='Simplify'), F('x^2+4x', 'x(x+4)', tag='L3', verb='Factorise'),
         N(r'Estimate $\sqrt{90}$ to $1$ decimal place without a calculator', r'$9.5$ ($9.49$)', r(math.sqrt(90), 1) == 9.5),
         N(r'Simplify the ratio $2.5 : 1.5$', '$5 : 3$', close(2.5 / 1.5, 5 / 3), tag='Ratio'),
     ]),
     ('long', 2, [
         L(r'A $5$ m ladder leans against a wall with its foot $1.4$ m from the wall. How high up the wall does it reach? <span class="hint">($48^2 = 2304$)</span>',
           r'$\sqrt{25 - 1.96} = \sqrt{23.04} = 4.8$ m', h=14, check=close(math.sqrt(25 - 1.96), 4.8)),
         L(r'A farm gate is $2.4$ m wide and $1$ m high. Find the length of the diagonal brace across it.',
           r'$\sqrt{5.76 + 1} = \sqrt{6.76} = 2.6$ m', h=14, check=close(hyp(2.4, 1), 2.6)),
         L(r'Ava walks $600$ m east along Marine Parade, Kingscliff, then $250$ m north. How much shorter would the straight-line path back to her start have been?',
           r'Direct: $\sqrt{360\,000 + 62\,500} = 650$ m; she walked $850$ m, so $200$ m shorter.', h=14,
           check=(hyp(600, 250) == 650)),
         L(r'$3, 4, 5$ is a triad. Write two more triads that are multiples of it, and explain why multiples of a triad are always triads.',
           r'e.g. $6, 8, 10$ and $9, 12, 15$. $(3k)^2 + (4k)^2 = 9k^2 + 16k^2 = 25k^2 = (5k)^2$.', h=14,
           check=(36 + 64 == 100 and 81 + 144 == 225)),
     ]),
     ],
    [('round', 'G'),
     ('sub', 'Simplify. (Surds.)'),
     ('grid', 4, [
         S('sqrt(12)', '2sqrt(3)'), S('sqrt(50)', '5sqrt(2)'), S('sqrt(72)', '6sqrt(2)'), S('2sqrt(3)+5sqrt(3)', '7sqrt(3)'),
         S('3sqrt(2)*2sqrt(5)', '6sqrt(10)'), S('sqrt(45)-sqrt(20)', 'sqrt(5)'),
         N(r'Hypotenuse, shorter sides $4$ and $8$, in simplest surd form', r'$\sqrt{80} = 4\sqrt{5}$', sp.sqrt(80) == 4 * sp.sqrt(5)),
         S('(2sqrt(3))^2', '12'), S('sqrt(2)*sqrt(8)', '4'), S('sqrt(3)(sqrt(3)+1)', '3+sqrt(3)'),
         S('[sqrt(48)|sqrt(3)]', '4'), S('5sqrt(2)-sqrt(8)', '3sqrt(2)'),
     ]),
     ('long', 3, [
         L(r'Find the length of the interval joining $A(1,\,2)$ and $B(4,\,6)$.<br><span class="hint">Hint: draw a right-angled triangle.</span>',
           r'run $3$, rise $4$: $\sqrt{9 + 16} = 5$ units', h=34, check=(hyp(3, 4) == 5)),
         L(r'Show that a triangle with sides $\sqrt{5}$, $\sqrt{20}$ and $5$ is right-angled.',
           r'$(\sqrt5)^2 + (\sqrt{20})^2 = 5 + 20 = 25 = 5^2$ ✓', h=34, check=(5 + 20 == 25)),
         L(r'A box measures $12$ cm by $4$ cm by $3$ cm. Find the length of the longest straight rod that fits inside it.',
           r'Base diagonal $\sqrt{144 + 16} = \sqrt{160}$; rod $= \sqrt{160 + 9} = \sqrt{169} = 13$ cm', h=34,
           check=(math.sqrt(144 + 16 + 9) == 13)),
     ]),
     ],
]

# ======================================================================
# LESSON 6  Equations and formulas
# ======================================================================
def subject_ok(formula, var, answer):
    lhs, rhs = formula.split('=')
    sol = sp.solve(to_sympy(lhs) - to_sympy(rhs), sp.Symbol(var))
    return any(sp.simplify(s_ - to_sympy(answer)) == 0 for s_ in sol)


L6 = dict(
    num=6, key='L6', title='Equations & formulas',
    sub='Inverse operations · unknowns on both sides · $ax^2 = c$ · substituting into formulas · changing the subject (Gold)',
    outcomes='MA4-EQU-C-01',
    ext='Gold: 3-step equations and grouping symbols MA5-EQU-C-01 · two fractions, changing the subject MA5-EQU-P-02',
    book='NCM 8 Adv 9.01–9.08 → NCM 9 Adv 7.01–7.09',
    ideas=[
        r'Keep the equation balanced: do the <b>same inverse operation</b> to both sides.',
        r'<b>Unknowns on both sides:</b> first move the pronumeral terms to one side: $5x = 2x + 12 \Rightarrow 3x = 12$.',
        r'<b>Check</b> every solution by substituting it back into the original equation.',
        r'$x^2 = c$ (with $c > 0$) has <b>two</b> solutions: $x = \pm\sqrt{c}$, since $(-6)^2 = 6^2 = 36$.',
        r'<b>Formulas:</b> substitute the known values first, then solve for the unknown.',
    ],
    examples=[
        (r'Solve $5x - 7 = 18$.', r'5x &= 25 \\ x &= 5'),
        (r'Solve $7x - 3 = 4x + 9$.', r'3x - 3 &= 9 \\ 3x = 12, \ \ x &= 4'),
        (r'Solve $2x^2 = 50$.', r'x^2 &= 25 \\ x &= \pm 5'),
    ],
)
L6['pages'] = [
    [('ideas',),
     ('round', 'B'),
     ('sub', 'Solve.'),
     ('grid', 4, [
         Q('x+9=15', ['6']), Q('y-4=-3', ['1']), Q('6m=42', ['7']), Q('[k|5]=3', ['15']),
         Q('2x+3=11', ['4']), Q('3a-5=16', ['7']), Q('[n|4]+2=5', ['12']), E('6(x-2)', '6x-12', tag='L2', verb='Expand'),
         Q('10-x=4', ['6']), Q('4p+7=-5', ['-3']), S('3^2*3^3', '243', tag='L4', verb='Evaluate'), Q('x^2=36', ['6', '-6']),
         N(r'Hypotenuse if the shorter sides are $3$ and $4$', '$5$', hyp(3, 4) == 5, tag='L5'),
         Q('5x=2x+12', ['4']), F('6a+8', '2(3a+4)', tag='L3', verb='Factorise'), Q('2(x+3)=14', ['4']),
         Q('[x+1|3]=4', ['11']), N(r'$15\%$ of $200$', '$30$', 0.15 * 200 == 30, tag='%'),
     ]),
     ],
    [('round', 'S'),
     ('sub', 'Solve. Leave answers that are not whole numbers in exact form.'),
     ('grid', 4, [
         Q('6x-5=2x+11', ['4']), Q('5a+2=2a-10', ['-4']), Q('[3x|4]=9', ['12']), Q('8-3x=2x-7', ['3']),
         Q('6-2x=14', ['-4']), Q('[x|5]-3=-1', ['10']), Q('0.5x+4=7', ['6']), Q('[x-4|3]=5', ['19']),
         Q('3x^2=48', ['4', '-4']), Q('x^2+5=30', ['5', '-5']), Q('5x^2=40', ['sqrt(8)', '-sqrt(8)']),
         S('(5^2)^3÷5^4', '25', tag='L4', verb='Evaluate'),
         E('2(x+4)-(x-3)', 'x+11', tag='L2', star=True, verb='Expand'),
         N(r'Is $8, 15, 17$ a Pythagorean triad?', r'Yes: $64 + 225 = 289$', 64 + 225 == 17 ** 2, tag='L5'),
         N(r'Write $\dfrac{3}{8}$ as a percentage', r'$37.5\%$', close(3 / 8 * 100, 37.5), tag='%'),
         N(r'$\dfrac{5}{6} - \dfrac{1}{4}$', r'$\dfrac{7}{12}$', sp.Rational(5, 6) - sp.Rational(1, 4) == sp.Rational(7, 12), tag='Frac'),
     ]),
     ('sub', 'Substitute into the formula, then solve.'),
     ('grid', 2, [
         N(r'$v = u + at$. Find $t$ when $v = 25$, $u = 5$, $a = 4$.', '$t = 5$', 5 + 4 * 5 == 25),
         N(r'$A = \tfrac{1}{2}bh$. Find $h$ when $A = 30$ and $b = 8$.', '$h = 7.5$', 0.5 * 8 * 7.5 == 30),
         N(r'$E = \tfrac{1}{2}mv^2$. Find $v$ ($v > 0$) when $E = 100$, $m = 8$.', '$v = 5$', 0.5 * 8 * 25 == 100),
         N(r'$A = \pi r^2$. Find $r$ ($r > 0$) when $A = 49\pi$.', '$r = 7$', 7 ** 2 == 49),
     ]),
     ('long', 2, [
         L(r'I think of a number, multiply it by $4$ and subtract $7$. The answer is the same as doubling the number and adding $9$. Write an equation and find the number.',
           r'$4n - 7 = 2n + 9$, so $2n = 16$ and $n = 8$', h=16, check=(4 * 8 - 7 == 2 * 8 + 9)),
         L(r'A Tweed Heads taxi charges $\$4.50$ plus $\$2.20$ per km. A trip cost $\$37.50$. Write an equation and find the length of the trip.',
           r'$4.50 + 2.20d = 37.50$, so $2.20d = 33$ and $d = 15$ km', h=16, check=close(4.5 + 2.2 * 15, 37.5)),
     ]),
     ],
    [('round', 'G'),
     ('sub', 'Solve.'),
     ('grid', 3, [
         Q('3(2m-1)=21', ['4']), Q('4(x+2)=3(x-1)', ['-11']), Q('[2x-3|5]=3', ['9']),
         Q('[x|3]+[x|4]=7', ['12']), Q('[x+2|3]=[x-1|2]', ['7']), Q('2(3y+1)-y=27', ['5']),
         Q('[3x-1|4]=[x+3|2]', ['7']), Q('5(x-2)-2(x+1)=0', ['4']), Q('[2|x]=[8|12]', ['3']),
     ]),
     ('sub', 'Make the pronumeral in brackets the subject.'),
     ('grid', 3, [
         N(r'$y = 3x + 2 \quad [x]$', r'$x = \dfrac{y - 2}{3}$', subject_ok('y=3x+2', 'x', '[y-2|3]')),
         N(r'$C = 2\pi r \quad [r]$', r'$r = \dfrac{C}{2\pi}$', subject_ok('C=2pi*r', 'r', '[C|2pi]')),
         N(r'$v^2 = u^2 + 2as \quad [a]$', r'$a = \dfrac{v^2 - u^2}{2s}$', subject_ok('v^2=u^2+2a*s', 'a', '[v^2-u^2|2s]')),
     ]),
     ('long', 2, [
         L(r'The length of a rectangle is $3$ cm more than twice its width. Its perimeter is $42$ cm. Find its dimensions.',
           r'$2(2w + 3) + 2w = 42 \Rightarrow 6w + 6 = 42 \Rightarrow w = 6$; $6$ cm by $15$ cm', h=30,
           check=(2 * (2 * 6 + 3) + 2 * 6 == 42)),
         L(r'Three consecutive even numbers add to $138$. Find them.',
           r'$n + (n + 2) + (n + 4) = 138 \Rightarrow 3n = 132$; $44, 46, 48$', h=30, check=(44 + 46 + 48 == 138)),
     ]),
     ],
]

# ======================================================================
# LESSON 7  Area and volume
# ======================================================================
L7 = dict(
    num=7, key='L7', title='Area & volume',
    sub='Rectangles, triangles, parallelograms, trapeziums, kites and rhombuses · composite areas · prisms and cylinders',
    outcomes='MA4-ARE-C-01 · MA4-VOL-C-01',
    ext='Gold: composite solids and algebraic area/volume (Stage 4 content, harder problems)',
    book='NCM 8 Adv 5.05–5.06, 5.09–5.13 → NCM 9 Adv 10.04–10.09',
    ideas=[
        r'$A_{\text{rectangle}} = lb \quad A_{\text{triangle}} = \tfrac{1}{2}bh \quad A_{\text{parallelogram}} = bh$ &nbsp;($h$ is the <b>perpendicular</b> height).',
        r'$A_{\text{trapezium}} = \tfrac{h}{2}(a + b) \qquad A_{\text{kite/rhombus}} = \tfrac{1}{2}xy$ &nbsp;($x$, $y$ are the diagonals).',
        r'<b>Composite shapes:</b> split into simple shapes and add, or take a piece away and subtract.',
        r'<b>Prism:</b> $V = Ah$, where $A$ is the area of the cross-section. <b>Cylinder:</b> $V = \pi r^2 h$.',
        r'Leave answers in terms of $\pi$ (exact), e.g. $V = 90\pi\ \text{cm}^3$. Units: $\text{cm}^2$ for area, $\text{cm}^3$ for volume.',
    ],
    examples=[
        (r'Trapezium: $a = 6,\ b = 10,\ h = 5$ (cm).', r'A &= \tfrac{5}{2}(6 + 10) \\ &= 40\ \text{cm}^2'),
        (r'Triangular prism: triangle base $6$, height $4$; length $10$ (cm).', r'A &= \tfrac12 \times 6 \times 4 = 12 \\ V &= 12 \times 10 = 120\ \text{cm}^3'),
        (r'Cylinder: $r = 3$ cm, $h = 10$ cm.', r'V &= \pi \times 3^2 \times 10 \\ &= 90\pi\ \text{cm}^3'),
    ],
)
L7['pages'] = [
    [('ideas',),
     ('round', 'B'),
     ('sub', 'Find the area or volume. Include units.'),
     ('grid', 3, [
         N('Rectangle $9$ m by $4$ m', r'$36\ \text{m}^2$', 9 * 4 == 36),
         N('Square of side $7$ cm', r'$49\ \text{cm}^2$', 7 * 7 == 49),
         N('Triangle: base $10$ cm, height $6$ cm', r'$30\ \text{cm}^2$', 0.5 * 10 * 6 == 30),
         N('Parallelogram: base $12$ cm, height $5$ cm', r'$60\ \text{cm}^2$', 12 * 5 == 60),
         N('Trapezium: $a = 4$, $b = 8$, $h = 5$ (cm)', r'$30\ \text{cm}^2$', 5 / 2 * (4 + 8) == 30),
         N('Kite: diagonals $6$ cm and $10$ cm', r'$30\ \text{cm}^2$', 0.5 * 6 * 10 == 30),
         N('Rhombus: diagonals $12$ m and $7$ m', r'$42\ \text{m}^2$', 0.5 * 12 * 7 == 42),
         Q('3x+4=19', ['5'], tag='L6', verb='Solve'), S('4^3', '64', tag='L4', verb='Evaluate'),
         N(r'Rectangular prism $5 \times 4 \times 3$ (cm)', r'$60\ \text{cm}^3$', 5 * 4 * 3 == 60),
         N('Cube of side $6$ cm', r'$216\ \text{cm}^3$', 6 ** 3 == 216),
         N(r'Prism: cross-section $15\ \text{cm}^2$, height $8$ cm', r'$120\ \text{cm}^3$', 15 * 8 == 120),
         N(r'Hypotenuse: shorter sides $6$ and $8$', '$10$', hyp(6, 8) == 10, tag='L5'),
         E('x(x+5)', 'x^2+5x', tag='L2', verb='Expand'), F('9m-12', '3(3m-4)', tag='L3', verb='Factorise'),
         N(r'Cylinder: $r = 1$ cm, $h = 10$ cm (in terms of $\pi$)', r'$10\pi\ \text{cm}^3$', True),
         N(r'Triangular prism: triangle base $5$, height $4$; length $9$ (cm)', r'$90\ \text{cm}^3$', 0.5 * 5 * 4 * 9 == 90),
         N(r'$50\%$ of $3.6$', '$1.8$', close(0.5 * 3.6, 1.8), tag='%'),
     ]),
     ],
    [('round', 'S'),
     ('sub', 'Find the area of the first two shapes (drawn to scale) and the volume of the prism.'),
     ('grid', 3, [
         N(l_shape(), r'$80 - 18 = 62\ \text{cm}^2$', 10 * 8 - 6 * 3 == 62),
         N(house(), r'$60 + 24 = 84\ \text{cm}^2$', 12 * 5 + 0.5 * 12 * 4 == 84),
         N(trap_prism() + '<div class="cap">Volume? (not to scale)</div>', r'$A = \tfrac32(4+10) = 21$; $V = 420\ \text{cm}^3$', 1.5 * 14 * 20 == 420),
     ]),
     ('sub', 'Find the unknown. Leave volumes of cylinders in terms of $\\pi$.'),
     ('grid', 3, [
         N(r'Trapezium: $a = 7.5$, $b = 12.5$, $h = 6$ (cm). Area?', r'$60\ \text{cm}^2$', 3 * (7.5 + 12.5) == 60),
         N(r'Parallelogram: area $72\ \text{cm}^2$, base $9$ cm. Height?', '$8$ cm', 72 / 9 == 8, tag='L6'),
         N(r'Kite: area $54\ \text{cm}^2$, one diagonal $12$ cm. Other diagonal?', '$9$ cm', 0.5 * 12 * 9 == 54, tag='L6'),
         N(r'Cylinder: $r = 5$ cm, $h = 8$ cm. Volume?', r'$200\pi\ \text{cm}^3$', 25 * 8 == 200),
         N(r'Cylinder: diameter $10$ cm, $h = 12$ cm. Volume?', r'$300\pi\ \text{cm}^3$', 25 * 12 == 300),
         N(r'Prism with the L-shape above as cross-section, depth $5$ cm. Volume?', r'$310\ \text{cm}^3$', 62 * 5 == 310),
         N(r'Isosceles triangle: base $10$ cm, equal sides $13$ cm. Area?', r'$h = 12$; $60\ \text{cm}^2$', hyp(5, 12) == 13 and 0.5 * 10 * 12 == 60, tag='L5'),
         N(r'Rectangle $3x$ by $2x$. Area?', '$6x^2$', True, tag='L1'),
         N(r'Rectangular prism: $V = 240\ \text{cm}^3$, base $8 \times 6$ cm. Height?', '$5$ cm', 240 / 48 == 5),
         N(r'A pool $25$ m long, $10$ m wide, $1.5$ m deep. Volume?', r'$375\ \text{m}^3$', 25 * 10 * 1.5 == 375),
         N(r'Rectangle $4$ by $(x + 3)$. Area, expanded?', '$4x + 12$', True, tag='L2'),
         N(r'Cube with volume $343\ \text{cm}^3$. Side length?', '$7$ cm', 7 ** 3 == 343, tag='L4'),
     ]),
     ('long', 2, [
         L(r'Explain why the area of a triangle is half the area of a parallelogram with the same base and height.',
           r'Two identical copies of the triangle fit together to make a parallelogram with base $b$ and height $h$, so the triangle is $\tfrac12 bh$.', h=13, check=True),
         L(r'A garden bed is a trapezium with parallel sides $3.5$ m and $5.5$ m, $2$ m apart. It is filled with soil $0.3$ m deep. Find the volume of soil.',
           r'$A = \tfrac22(3.5 + 5.5) = 9\ \text{m}^2$; $V = 9 \times 0.3 = 2.7\ \text{m}^3$', h=13, check=close(1 * 9 * 0.3, 2.7)),
     ]),
     ],
    [('round', 'G'),
     ('long', 2, [
         L(r'A pipe is $100$ cm long, with outer radius $5$ cm and inner radius $4$ cm. Find the volume of material, in terms of $\pi$.',
           r'$\pi(5^2 - 4^2) \times 100 = 900\pi\ \text{cm}^3$', h=26, check=((25 - 16) * 100 == 900)),
         L(r'A cylinder has volume $360\pi\ \text{cm}^3$ and radius $6$ cm. Find its height.',
           r'$36\pi h = 360\pi$, so $h = 10$ cm', h=26, check=(36 * 10 == 360)),
         L(r'A prism has a square base of side $x$ cm and height $(x + 3)$ cm.<br>a) Show that $V = x^3 + 3x^2$. &nbsp; b) Find $V$ when $x = 4$.',
           r'a) $x^2(x + 3) = x^3 + 3x^2$ &nbsp; b) $64 + 48 = 112\ \text{cm}^3$', h=26, check=(4 ** 3 + 3 * 16 == 112)),
         L(r'A trapezium has parallel sides $x$ cm and $(x + 4)$ cm, height $5$ cm and area $45\ \text{cm}^2$. Find $x$.',
           r'$\tfrac52(2x + 4) = 45 \Rightarrow 2x + 4 = 18 \Rightarrow x = 7$', h=26, check=(2.5 * (7 + 11) == 45)),
         L(r'A $10$ cm cube has a cylindrical hole of radius $2$ cm drilled straight through it. Find the volume left, in terms of $\pi$.',
           r'$1000 - \pi \times 2^2 \times 10 = (1000 - 40\pi)\ \text{cm}^3$', h=26, check=(4 * 10 == 40)),
         L(r'What happens to the volume of a cylinder if a) its radius is doubled? b) both its radius and height are doubled? Explain.',
           r'a) $\pi(2r)^2h = 4\pi r^2h$: $\times 4$ &nbsp; b) $\pi(2r)^2(2h) = 8\pi r^2 h$: $\times 8$', h=26, check=True),
     ]),
     ],
]

# ======================================================================
# PRE-TEST and POST-TEST  (20 marks, 20 minutes, non-calculator)
# ======================================================================
def T_(label, html, marks, ans, h=9, check=True):
    ok = check() if callable(check) else check
    if not ok:
        ERRORS.append('Test check failed: ' + html[:50])
    return dict(label=label, html=html, marks=marks, ans=ans, h=h)


def make_test(v):
    """v = 'pre' or 'post'"""
    if v == 'pre':
        Q1 = [T_('a', r'Simplify $5x + 3y - 2x$', 1, r'$3x + 3y$', check=lambda: S('5x+3y-2x', '3x+3y')),
              T_('b', r'Simplify $4a \times 3ab$', 1, r'$12a^2b$', check=lambda: S('4a*3ab', '12a^2b')),
              T_('c', r'Evaluate $2p^2 - q$ when $p = -3$ and $q = 4$', 1, r'$14$', check=2 * 9 - 4 == 14)]
        Q2 = [T_('a', r'Expand $x(x - 4)$', 1, r'$x^2 - 4x$', check=lambda: E('x(x-4)', 'x^2-4x')),
              T_('b', r'Expand $-3(2x - 5)$', 1, r'$-6x + 15$', check=lambda: E('-3(2x-5)', '-6x+15')),
              T_('c', r'Expand and simplify $4(a + 2) - 2(a - 3)$', 1, r'$2a + 14$', check=lambda: E('4(a+2)-2(a-3)', '2a+14'))]
        Q3 = [T_('a', r'$12m + 18$', 1, r'$6(2m + 3)$', check=lambda: F('12m+18', '6(2m+3)')),
              T_('b', r'$6x^2 - 9xy$', 1, r'$3x(2x - 3y)$', check=lambda: F('6x^2-9xy', '3x(2x-3y)')),
              T_('c', r'$-4a - 10$', 1, r'$-2(2a + 5)$', check=lambda: F('-4a-10', '-2(2a+5)'))]
        Q4 = [T_('a', r'Write $5^7 \times 5^2 \div 5^6$ as a single power, then evaluate', 1, r'$5^3 = 125$', check=5 ** 3 == 125),
              T_('b', r'Evaluate $(2^3)^2 \div 2^4$', 1, r'$4$', check=2 ** 6 // 2 ** 4 == 4),
              T_('c', r'Write $180$ as a product of prime factors in index form', 1, r'$2^2 \times 3^2 \times 5$', check=4 * 9 * 5 == 180)]
        Q5 = [T_('a', 'Find $c$.' + right_tri(12, 9, '12 cm', '9 cm', 'c'), 1, r'$15$ cm', h=0, check=hyp(9, 12) == 15),
              T_('b', 'Find $x$ as an exact value.' + right_tri(math.sqrt(75), 5, 'x', '5 cm', '10 cm'), 1, r'$\sqrt{75}$ cm (accept $5\sqrt3$)', h=0, check=100 - 25 == 75),
              T_('c', r'Is a triangle with sides $5$, $11$ and $12$ right-angled? Show working.', 1, r'No: $25 + 121 = 146 \ne 144$', check=25 + 121 != 144)]
        Q6 = [T_('a', r'$4x - 7 = 13$', 1, r'$x = 5$', check=lambda: Q('4x-7=13', ['5'])),
              T_('b', r'$5a + 3 = 2a - 9$', 1, r'$a = -4$', check=lambda: Q('5a+3=2a-9', ['-4'])),
              T_('c', r'$2x^2 = 72$', 1, r'$x = \pm 6$', check=lambda: Q('2x^2=72', ['6', '-6']))]
        Q7 = [T_('a', r'Find the area of a trapezium with parallel sides $5$ cm and $9$ cm and perpendicular height $4$ cm.', 1, r'$28\ \text{cm}^2$', check=2 * 14 == 28),
              T_('b', r'Find the volume of a cylinder with radius $3$ cm and height $5$ cm, in terms of $\pi$.', 1, r'$45\pi\ \text{cm}^3$', check=9 * 5 == 45)]
    else:
        Q1 = [T_('a', r'Simplify $7m + 2n - 3m$', 1, r'$4m + 2n$', check=lambda: S('7m+2n-3m', '4m+2n')),
              T_('b', r'Simplify $5x \times 2xy$', 1, r'$10x^2y$', check=lambda: S('5x*2xy', '10x^2y')),
              T_('c', r'Evaluate $3a^2 - b$ when $a = -2$ and $b = 5$', 1, r'$7$', check=3 * 4 - 5 == 7)]
        Q2 = [T_('a', r'Expand $y(y + 5)$', 1, r'$y^2 + 5y$', check=lambda: E('y(y+5)', 'y^2+5y')),
              T_('b', r'Expand $-4(3x - 2)$', 1, r'$-12x + 8$', check=lambda: E('-4(3x-2)', '-12x+8')),
              T_('c', r'Expand and simplify $3(a + 4) - 2(a - 1)$', 1, r'$a + 14$', check=lambda: E('3(a+4)-2(a-1)', 'a+14'))]
        Q3 = [T_('a', r'$15k + 20$', 1, r'$5(3k + 4)$', check=lambda: F('15k+20', '5(3k+4)')),
              T_('b', r'$8a^2 - 12ab$', 1, r'$4a(2a - 3b)$', check=lambda: F('8a^2-12ab', '4a(2a-3b)')),
              T_('c', r'$-6x - 15$', 1, r'$-3(2x + 5)$', check=lambda: F('-6x-15', '-3(2x+5)'))]
        Q4 = [T_('a', r'Write $3^8 \times 3^2 \div 3^7$ as a single power, then evaluate', 1, r'$3^3 = 27$', check=3 ** 3 == 27),
              T_('b', r'Evaluate $(5^2)^3 \div 5^4$', 1, r'$25$', check=5 ** 6 // 5 ** 4 == 25),
              T_('c', r'Write $252$ as a product of prime factors in index form', 1, r'$2^2 \times 3^2 \times 7$', check=4 * 9 * 7 == 252)]
        Q5 = [T_('a', 'Find $c$.' + right_tri(20, 15, '20 cm', '15 cm', 'c'), 1, r'$25$ cm', h=0, check=hyp(15, 20) == 25),
              T_('b', 'Find $x$ as an exact value.' + right_tri(math.sqrt(48), 4, 'x', '4 cm', '8 cm'), 1, r'$\sqrt{48}$ cm (accept $4\sqrt3$)', h=0, check=64 - 16 == 48),
              T_('c', r'Is a triangle with sides $8$, $15$ and $17$ right-angled? Show working.', 1, r'Yes: $64 + 225 = 289 = 17^2$', check=64 + 225 == 289)]
        Q6 = [T_('a', r'$3x + 8 = 29$', 1, r'$x = 7$', check=lambda: Q('3x+8=29', ['7'])),
              T_('b', r'$7a - 5 = 3a + 11$', 1, r'$a = 4$', check=lambda: Q('7a-5=3a+11', ['4'])),
              T_('c', r'$3x^2 = 75$', 1, r'$x = \pm 5$', check=lambda: Q('3x^2=75', ['5', '-5']))]
        Q7 = [T_('a', r'Find the area of a trapezium with parallel sides $6$ cm and $10$ cm and perpendicular height $5$ cm.', 1, r'$40\ \text{cm}^2$', check=2.5 * 16 == 40),
              T_('b', r'Find the volume of a cylinder with radius $2$ cm and height $7$ cm, in terms of $\pi$.', 1, r'$28\pi\ \text{cm}^3$', check=4 * 7 == 28)]
    return [
        ('1', 'Algebra basics', 'L1', Q1),
        ('2', 'Expanding brackets', 'L2', Q2),
        ('3', 'Factorise fully', 'L3', Q3),
        ('4', 'Indices', 'L4', Q4),
        ('5', "Pythagoras' theorem", 'L5', Q5),
        ('6', 'Solve', 'L6', Q6),
        ('7', 'Area and volume', 'L7', Q7),
    ]


PRE = make_test('pre')
POST = make_test('post')
