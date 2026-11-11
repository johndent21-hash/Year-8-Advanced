from dsl import *
from svg import *
import math
from fractions import Fraction as Fr
from content_s1 import P, GOLD_EXT

PI = math.pi


def hyp(a, b):
    return math.hypot(a, b)


# ======================================================================
# LESSON 5  Pythagoras' theorem
# ======================================================================
L5 = dict(
    num=5, key='L5', title="Pythagoras' theorem",
    sub='The hypotenuse · finding the hypotenuse · finding a shorter side · testing for a right angle · triads',
    outcomes='MA4-PYT-C-01', ext=GOLD_EXT, book='NCM 8 Ch 1',
    vocab=[('hypotenuse', 'the longest side, opposite the right angle'), ('right angle', 'an angle of $90°$, marked with a small square'),
           ('exact answer', 'leaves the square root, e.g. $\\sqrt{74}$'), ('approximate', 'a rounded decimal, e.g. $8.60$'),
           ('triad', 'three whole numbers with $a^2 + b^2 = c^2$')],
    ideas=[
        r'The <b>hypotenuse</b> $c$ is the longest side, opposite the right angle. <b>Pythagoras:</b> $c^2 = a^2 + b^2$.',
        r'<b>Finding the hypotenuse:</b> square, <b>add</b>, then take the square root.',
        r'<b>Finding a shorter side:</b> square, <b>subtract</b>, then take the square root: $a^2 = c^2 - b^2$.',
        r'Round only at the <b>last step</b>, e.g. $c = \sqrt{74} \approx 8.60$.',
        r'<b>Testing:</b> if $a^2 + b^2 = c^2$ (with $c$ the longest side), the triangle is right-angled.',
    ],
    examples=[
        (r'Find $c$ if the shorter sides are $5$ cm and $12$ cm.', r'c^2 &= 5^2 + 12^2 = 169 \\ c &= \sqrt{169} = 13\text{ cm}'),
        (r'Find $x$ if the hypotenuse is $9$ cm and one side is $5$ cm (1 d.p.).', r'x^2 &= 9^2 - 5^2 = 56 \\ x &= \sqrt{56} \approx 7.5\text{ cm}'),
        (r'Is a triangle with sides $7, 24, 25$ right-angled?', r'7^2 + 24^2 &= 625 \\ 25^2 &= 625 \;\checkmark\ \text{Yes}'),
    ],
)
L5['pages'] = [
    [('ideas',),
     ('round', 'B'),
     ('sub', 'Find the hypotenuse $c$. Round to $1$ decimal place where needed. (Lengths in cm.)'),
     ('grid', 4, [
         N(right_tri(8, 6, '8', '6', 'c'), '$10$ cm', hyp(6, 8) == 10),
         N(right_tri(12, 9, '12', '9', 'c'), '$15$ cm', hyp(9, 12) == 15),
         P(N(right_tri(4, 3, '4', '3', 'c'), '$5$ cm', hyp(3, 4) == 5), r'c^2 = 9 + 16 = \_\_\_'),
         N(right_tri(7, 5, '7', '5', 'c'), r'$\sqrt{74} \approx 8.6$ cm', r(hyp(5, 7), 1) == 8.6),
     ]),
     ('grid', 4, [
         N(r'In $\triangle PQR$, $\angle Q = 90°$. Name the hypotenuse.', '$PR$', True),
         S('sqrt(49)', '7', tag='L4', verb='Evaluate'),
         N(r'Round $8.6023$ to $2$ decimal places', '$8.60$', r(8.6023, 2) == 8.6, tag='L1'),
         S('6^2+8^2', '100', verb='Evaluate'),
     ]),
     ('grid', 4, [
         N(r'Hypotenuse: shorter sides $5$ cm and $12$ cm', '$13$ cm', hyp(5, 12) == 13),
         N(r'Hypotenuse: shorter sides $2$ cm and $3$ cm (1 d.p.)', r'$\sqrt{13} \approx 3.6$ cm', r(hyp(2, 3), 1) == 3.6),
         P(N(r'Find $x$: hypotenuse $10$ cm, one side $6$ cm', '$8$ cm', math.sqrt(100 - 36) == 8), r'x^2 = 100 - 36 = \_\_\_'),
         S('sqrt(7^2+24^2)', '25', verb='Evaluate'),
     ]),
     ],
    [('round', 'S'),
     ('sub', 'Find $x$. Round to $1$ decimal place where needed. (Lengths in cm.)'),
     ('grid', 4, [
         N(right_tri(12, 5, 'x', '5', '13'), '$12$ cm', math.sqrt(13 ** 2 - 5 ** 2) == 12),
         N(right_tri(24, 7, 'x', '7', '25'), '$24$ cm', math.sqrt(25 ** 2 - 7 ** 2) == 24),
         N(right_tri(math.sqrt(84), 4, 'x', '4', '10'), r'$\sqrt{84} \approx 9.2$ cm', r(math.sqrt(84), 1) == 9.2),
         N(right_tri(10, 7.5, 'x', '7.5', '12.5'), '$10$ cm', close(math.sqrt(12.5 ** 2 - 7.5 ** 2), 10)),
     ]),
     ('grid', 3, [
         N(r'Is a triangle with sides $9, 40, 41$ right-angled?', r'Yes: $81 + 1600 = 1681 = 41^2$', 81 + 1600 == 41 ** 2),
         N(r'Is a triangle with sides $6, 9, 11$ right-angled?', r'No: $36 + 81 = 117 \ne 121$', 36 + 81 != 121),
         N(r'Is $20, 21, 29$ a Pythagorean triad?', r'Yes: $400 + 441 = 841$', 400 + 441 == 29 ** 2),
         F('x^2+4x', 'x(x+4)', tag='L3', verb='Factorise'), S('5^0+2^4', '17', tag='L4', verb='Evaluate'),
         V('a^2+b^2', {'a': -3, 'b': 4}, '25', tag='L2', verb='If $a=-3,\\,b=4$:'),
         N(r'Shorter side: hypotenuse $15$ cm, one side $9$ cm', '$12$ cm', math.sqrt(225 - 81) == 12),
         N(r'Diagonal of a rectangle $30$ cm by $40$ cm', '$50$ cm', hyp(30, 40) == 50),
         N(r'$20\%$ discount on $\$45$: sale price?', r'$\$36$', close(45 * 0.8, 36), tag='L1'),
     ]),
     ('long', 3, [
         L(r'A $5$ m ladder leans against a wall with its foot $1.4$ m from the wall. How high up the wall does it reach?', r'$\sqrt{25 - 1.96} = 4.8$ m', h=16,
           check=close(math.sqrt(25 - 1.96), 4.8)),
         L(r'A TV screen is $80$ cm wide and $45$ cm high. Find the length of its diagonal to $1$ decimal place.', r'$\sqrt{8425} \approx 91.8$ cm', h=16,
           check=(r(hyp(80, 45), 1) == 91.8)),
         L(r'Ava walks $600$ m east along Marine Parade, Kingscliff, then $250$ m north. How far is she in a straight line from where she started?', r'$650$ m', h=16,
           check=(hyp(600, 250) == 650)),
     ]),
     ],
    [('round', 'G'),
     ('long', 2, [
         L(r'A $3$ m ladder must reach $2.8$ m up a wall. How far from the wall should its foot be? (1 d.p.)', r'$\sqrt{9 - 7.84} = \sqrt{1.16} \approx 1.1$ m', h=30,
           check=(r(math.sqrt(9 - 7.84), 1) == 1.1)),
         L(r'Find the perimeter of a right-angled triangle whose shorter sides are $6$ cm and $8$ cm.', r'hypotenuse $10$; perimeter $24$ cm', h=30, check=(6 + 8 + hyp(6, 8) == 24)),
         L(r'An isosceles triangle has equal sides of $13$ cm and a base of $10$ cm. Find its height and its area.', r'height $\sqrt{169 - 25} = 12$ cm; area $60\ \text{cm}^2$', h=30,
           check=(math.sqrt(169 - 25) == 12 and 0.5 * 10 * 12 == 60)),
         L(r'A rectangular paddock is $120$ m by $50$ m. How much shorter is it to walk across the diagonal than around two sides?', r'diagonal $130$ m; $170 - 130 = 40$ m shorter', h=30,
           check=(hyp(120, 50) == 130)),
         L(r'$3, 4, 5$ is a triad. Write two more triads that are multiples of it and show they work.', r'e.g. $6, 8, 10$: $36 + 64 = 100$; $9, 12, 15$: $81 + 144 = 225$', h=30,
           check=(36 + 64 == 100 and 81 + 144 == 225)),
         L(r'A kite string is $50$ m long. The kite is directly above a point $30$ m from where Leo stands. How high is the kite? (Ignore Leo’s height.)', r'$\sqrt{2500 - 900} = 40$ m', h=30,
           check=(math.sqrt(2500 - 900) == 40)),
     ]),
     ],
]

# ======================================================================
# LESSON 6  Equations and formulas
# ======================================================================
L6 = dict(
    num=6, key='L6', title='Equations & formulas',
    sub='Inverse operations · one- and two-step equations · unknowns on both sides · $x^2 = c$ · formulas',
    outcomes='MA4-EQU-C-01', ext=GOLD_EXT, book='NCM 8 Ch 9',
    vocab=[('equation', 'a number sentence with an equals sign, e.g. $2x + 3 = 11$'), ('solution', 'the value that makes the equation true'),
           ('inverse operation', 'the opposite operation, e.g. $+$ and $-$'), ('formula', 'a rule linking quantities, e.g. $A = lb$'),
           ('check', 'substitute your answer back into the equation')],
    ideas=[
        r'Keep the equation <b>balanced</b>: do the same inverse operation to both sides.',
        r'<b>Two steps:</b> undo $+$ or $-$ first, then $\times$ or $\div$: &nbsp; $2x + 3 = 11 \Rightarrow 2x = 8 \Rightarrow x = 4$.',
        r'<b>Unknowns on both sides:</b> first move the pronumeral terms to one side.',
        r'$x^2 = c$ has <b>two</b> solutions: $x = \pm\sqrt{c}$, because $(-6)^2 = 6^2 = 36$.',
        r'<b>Formulas:</b> substitute the values you know, then solve. Always <b>check</b> by substituting back.',
    ],
    examples=[
        (r'Solve $5x - 7 = 18$.', r'5x &= 25 \\ x &= 5'),
        (r'Solve $7x - 3 = 4x + 9$.', r'3x - 3 &= 9 \\ 3x = 12,\ \ x &= 4'),
        (r'Solve $2x^2 = 50$.', r'x^2 &= 25 \\ x &= \pm 5'),
    ],
)
L6['pages'] = [
    [('ideas',),
     ('round', 'B'),
     ('sub', 'Solve.'),
     ('grid', 4, [
         Q('x+9=15', ['6']), Q('y-4=-3', ['1']), Q('6m=42', ['7']), Q('[k|5]=3', ['15']),
         Q('2x+3=11', ['4']), Q('3a-5=16', ['7']),
         P(Q('4x+7=31', ['6']), r'4x = \_\_\_,\ \ x = \_\_\_'),
         Q('[n|4]+2=5', ['12']), Q('x^2=36', ['6', '-6']), Q('10-x=4', ['6']),
         E('6(x-2)', '6x-12', tag='L3', verb='Expand'), S('3^2*3^3', '243', tag='L4', verb='Evaluate'),
         N(r'Hypotenuse if the shorter sides are $3$ and $4$', '$5$', hyp(3, 4) == 5, tag='L5'),
         P(Q('5x=2x+12', ['4']), r'3x = 12,\ \ x = \_\_\_'),
     ]),
     ],
    [('round', 'S'),
     ('sub', 'Solve. Round to $2$ decimal places where needed.'),
     ('grid', 4, [
         Q('6x-5=2x+11', ['4']), Q('5a+2=2a-10', ['-4']), Q('[3x|4]=9', ['12']), Q('8-3x=2x-7', ['3']),
         Q('0.5x+4=7', ['6']), Q('[x-4|3]=5', ['19']), Q('3x^2=48', ['4', '-4']), Q('5x^2=40', ['sqrt(8)', '-sqrt(8)'], approx=r'\pm 2.83'),
         N(r'$30\%$ of $\$45$', r'$\$13.50$', close(0.3 * 45, 13.5), tag='L1'), S('[5|6]-[1|4]', '[7|12]', tag='L1', verb='Evaluate'),
     ]),
     ('sub', 'Substitute into the formula, then solve.'),
     ('grid', 2, [
         N(r'$v = u + at$. Find $t$ when $v = 25$, $u = 5$, $a = 4$.', '$t = 5$', 5 + 4 * 5 == 25),
         N(r'$A = \tfrac{1}{2}bh$. Find $h$ when $A = 30$ and $b = 8$.', '$h = 7.5$', 0.5 * 8 * 7.5 == 30),
         N(r'$A = \pi r^2$. Find $r$ ($r > 0$) when $A = 50$. (2 d.p.)', r'$r \approx 3.99$', r(math.sqrt(50 / PI), 2) == 3.99),
         N(r'$F = 1.8C + 32$. Find $C$ when $F = 95$.', '$C = 35$', close(1.8 * 35 + 32, 95)),
     ]),
     ('long', 2, [
         L(r'I think of a number, multiply it by $4$ and subtract $7$. The answer is $2$ times the number plus $9$. Find the number.', r'$4n - 7 = 2n + 9$, so $n = 8$', h=14,
           check=(4 * 8 - 7 == 2 * 8 + 9)),
         L(r'A Tweed Heads taxi charges $\$4.50$ plus $\$2.20$ per km. A trip cost $\$37.50$. How long was the trip?', r'$4.50 + 2.20d = 37.50$, $d = 15$ km', h=14,
           check=close(4.5 + 2.2 * 15, 37.5)),
     ]),
     ],
    [('round', 'G'),
     ('long', 2, [
         L(r'A plumber charges $\$80$ to come out plus $\$65$ per hour. A bill is $\$307.50$. How many hours did the plumber work?', r'$80 + 65h = 307.50$, $h = 3.5$ hours', h=30,
           check=close(80 + 65 * 3.5, 307.5)),
         L(r'The length of a rectangle is $3$ cm more than its width. Its perimeter is $42$ cm. Find its length and width.', r'$4w + 6 = 42$, $w = 9$; $9$ cm by $12$ cm', h=30,
           check=(2 * (9 + 12) == 42)),
         L(r'Solve $x^2 + 5 = 86$.', r'$x^2 = 81$, $x = \pm 9$', h=30, check=(81 + 5 == 86)),
         L(r'Three consecutive whole numbers add to $138$. Find them.', r'$3n + 3 = 138$; $45, 46, 47$', h=30, check=(45 + 46 + 47 == 138)),
         L(r'A circle has area $200\ \text{cm}^2$. Find its radius to $1$ decimal place.', r'$r = \sqrt{200 \div \pi} \approx 8.0$ cm', h=30,
           check=(r(math.sqrt(200 / PI), 1) == 8.0)),
         L(r'Two phone plans: Plan A costs $\$20$ plus $\$0.50$ per GB; Plan B costs $\$12$ plus $\$1$ per GB. For how many GB do they cost the same?', r'$20 + 0.5g = 12 + g$, $g = 16$ GB', h=30,
           check=close(20 + 0.5 * 16, 12 + 16)),
     ]),
     ],
]

# ======================================================================
# LESSON 7  Area and volume
# ======================================================================
L7 = dict(
    num=7, key='L7', title='Area & volume',
    sub='Rectangles, triangles, parallelograms, trapeziums, kites · circles · composite areas · prisms and cylinders',
    outcomes='MA4-ARE-C-01 · MA4-VOL-C-01', ext=GOLD_EXT, book='NCM 8 Ch 5',
    vocab=[('perpendicular height', 'the height at right angles to the base'), ('composite shape', 'a shape made of simpler shapes'),
           ('cross-section', 'the face that is the same all the way through a prism'), ('prism', 'a solid with a uniform cross-section'),
           ('capacity', 'how much a container holds: $1000\\ \\text{cm}^3 = 1$ L')],
    ideas=[
        r'$A_{\text{rectangle}} = lb \quad A_{\text{triangle}} = \tfrac12 bh \quad A_{\text{parallelogram}} = bh$ &nbsp;($h$ is the <b>perpendicular</b> height).',
        r'$A_{\text{trapezium}} = \tfrac{h}{2}(a + b) \qquad A_{\text{kite}} = \tfrac12 xy \qquad A_{\text{circle}} = \pi r^2$.',
        r'<b>Composite shapes:</b> split into simple shapes and add, or take a piece away and subtract.',
        r'<b>Prism:</b> $V = Ah$ ($A$ = area of the cross-section). <b>Cylinder:</b> $V = \pi r^2 h$.',
        r'Units: $\text{cm}^2$ for area, $\text{cm}^3$ for volume; $1\ \text{cm}^3 = 1$ mL and $1\ \text{m}^3 = 1000$ L.',
    ],
    examples=[
        (r'Trapezium: $a = 6$, $b = 10$, $h = 5$ (cm). Find the area.', r'A &= \tfrac{5}{2}(6 + 10) \\ &= 40\ \text{cm}^2'),
        (r'Circle: radius $3$ cm. Find the area (1 d.p.).', r'A &= \pi \times 3^2 \\ &\approx 28.3\ \text{cm}^2'),
        (r'Cylinder: $r = 3$ cm, $h = 10$ cm. Find the volume (1 d.p.).', r'V &= \pi \times 3^2 \times 10 \\ &\approx 282.7\ \text{cm}^3'),
    ],
)
L7['pages'] = [
    [('ideas',),
     ('round', 'B'),
     ('sub', 'Find the area or volume. Include units. Round to $1$ decimal place where needed.'),
     ('grid', 3, [
         N('Rectangle $9$ m by $4$ m', r'$36\ \text{m}^2$', 9 * 4 == 36),
         N('Triangle: base $10$ cm, height $6$ cm', r'$30\ \text{cm}^2$', 0.5 * 10 * 6 == 30),
         N('Parallelogram: base $12$ cm, height $5$ cm', r'$60\ \text{cm}^2$', 12 * 5 == 60),
         N('Trapezium: $a = 4$, $b = 8$, $h = 5$ (cm)', r'$30\ \text{cm}^2$', 5 / 2 * 12 == 30),
         N('Kite: diagonals $6$ cm and $10$ cm', r'$30\ \text{cm}^2$', 0.5 * 60 == 30),
         N('Circle: radius $5$ cm', r'$78.5\ \text{cm}^2$', r(PI * 25, 1) == 78.5),
         P(N(r'Prism: cross-section $15\ \text{cm}^2$, height $8$ cm', r'$120\ \text{cm}^3$', 15 * 8 == 120), r'V = 15 \times 8 = \_\_\_'),
         N(r'Rectangular prism $5 \times 4 \times 3$ (cm)', r'$60\ \text{cm}^3$', 60 == 5 * 4 * 3),
         N('Cube of side $6$ cm', r'$216\ \text{cm}^3$', 6 ** 3 == 216),
         Q('3x+4=19', ['5'], tag='L6', verb='Solve'),
         N(r'Hypotenuse: shorter sides $6$ and $8$', '$10$', hyp(6, 8) == 10, tag='L5'),
         S('4^3', '64', tag='L4', verb='Evaluate'),
         N('Square of side $7$ cm', r'$49\ \text{cm}^2$', 49 == 7 * 7),
         N('Circle: diameter $8$ cm', r'$50.3\ \text{cm}^2$', r(PI * 16, 1) == 50.3),
         N(r'Cylinder: $r = 1$ cm, $h = 10$ cm', r'$31.4\ \text{cm}^3$', r(PI * 10, 1) == 31.4),
     ]),
     ],
    [('round', 'S'),
     ('sub', 'Find the area of the first two shapes (drawn to scale) and the volume of the prism.'),
     ('grid', 3, [
         N(l_shape(), r'$80 - 18 = 62\ \text{cm}^2$', 10 * 8 - 6 * 3 == 62),
         N(house(), r'$60 + 24 = 84\ \text{cm}^2$', 12 * 5 + 0.5 * 12 * 4 == 84),
         N(trap_prism() + '<div class="cap">Volume? (not to scale)</div>', r'$A = 21$; $V = 420\ \text{cm}^3$', 1.5 * 14 * 20 == 420),
     ]),
     ('sub', 'Round to $1$ decimal place where needed.'),
     ('grid', 3, [
         N(r'Semicircle: diameter $10$ cm. Area?', r'$39.3\ \text{cm}^2$', r(0.5 * PI * 25, 1) == 39.3),
         N(r'Cylinder: $r = 5$ cm, $h = 8$ cm. Volume?', r'$628.3\ \text{cm}^3$', r(PI * 25 * 8, 1) == 628.3),
         N(r'Cylinder: diameter $10$ cm, $h = 12$ cm. Volume?', r'$942.5\ \text{cm}^3$', r(PI * 25 * 12, 1) == 942.5),
         N(r'Parallelogram: area $72\ \text{cm}^2$, base $9$ cm. Height?', '$8$ cm', 72 / 9 == 8, tag='L6'),
         N(r'A pool is $25$ m by $10$ m by $1.5$ m deep. Volume, and capacity in litres?', r'$375\ \text{m}^3 = 375\,000$ L', 25 * 10 * 1.5 == 375),
         N(r'Rectangle $4$ by $(x + 3)$. Area, expanded?', '$4x + 12$', True, tag='L3'),
         N(r'Rhombus: diagonals $12$ m and $7$ m. Area?', r'$42\ \text{m}^2$', 0.5 * 12 * 7 == 42),
         N(r'Triangular prism: triangle base $6$ cm, height $4$ cm; length $10$ cm. Volume?', r'$120\ \text{cm}^3$', 0.5 * 6 * 4 * 10 == 120),
         N(r'Cube with volume $343\ \text{cm}^3$. Side length?', '$7$ cm', 7 ** 3 == 343, tag='L4'),
     ]),
     ('long', 2, [
         L(r'A garden bed is a trapezium with parallel sides $3.5$ m and $5.5$ m, $2$ m apart. It is filled with soil $0.3$ m deep. Find the volume of soil.',
           r'$A = 9\ \text{m}^2$; $V = 2.7\ \text{m}^3$', h=14, check=close(1 * 9 * 0.3, 2.7)),
         L(r'Explain why the area of a triangle is half the area of a rectangle with the same base and height.',
           r'Two identical triangles fit together to make a rectangle (or parallelogram) $b$ by $h$, so the triangle is $\tfrac12 bh$.', h=14, check=True),
     ]),
     ],
    [('round', 'G'),
     ('long', 2, [
         L(r'A pipe is $100$ cm long, with outer radius $5$ cm and inner radius $4$ cm. Find the volume of material (1 d.p.).', r'$\pi(25 - 16) \times 100 \approx 2827.4\ \text{cm}^3$', h=30,
           check=(r(PI * 9 * 100, 1) == 2827.4)),
         L(r'A cylinder has volume $1000\ \text{cm}^3$ and radius $5$ cm. Find its height (1 d.p.).', r'$h = 1000 \div (25\pi) \approx 12.7$ cm', h=30, check=(r(1000 / (25 * PI), 1) == 12.7)),
         L(r'A $10$ cm cube has a cylindrical hole of radius $2$ cm drilled straight through it. Find the volume left (1 d.p.).', r'$1000 - 40\pi \approx 874.3\ \text{cm}^3$', h=30,
           check=(r(1000 - 40 * PI, 1) == 874.3)),
         L(r'A cylindrical rainwater tank has radius $1.2$ m and height $2$ m. How many litres does it hold? (nearest litre)', r'$\pi \times 1.44 \times 2 \approx 9.048\ \text{m}^3 \approx 9048$ L', h=30,
           check=(round(PI * 1.44 * 2 * 1000) == 9048)),
         L(r'A trapezium has parallel sides $x$ cm and $(x + 4)$ cm, height $5$ cm and area $45\ \text{cm}^2$. Find $x$.', r'$\tfrac52(2x + 4) = 45$, $x = 7$', h=30,
           check=(2.5 * (7 + 11) == 45)),
         L(r'What happens to the area of a circle when its radius is doubled? Explain.', r'It is multiplied by $4$: $\pi(2r)^2 = 4\pi r^2$', h=30, check=True),
     ]),
     ],
]


# ======================================================================
# PRE- and POST-TEST (20 marks, 20 min, calculator allowed)
# ======================================================================
def T_(label, html, marks, ans, check=True):
    ok = check() if callable(check) else check
    if not ok:
        ERRORS.append('Test check failed: ' + html[:50])
    return dict(label=label, html=html, marks=marks, ans=ans, h=9)


def make_test(v):
    if v == 'pre':
        Q1 = [T_('a', r'Evaluate $-8 + 3 \times (-2)$', 1, '$-14$', -8 + 3 * -2 == -14),
              T_('b', r'Evaluate $\tfrac{2}{3} + \tfrac{1}{4}$', 1, r'$\tfrac{11}{12}$', Fr(2, 3) + Fr(1, 4) == Fr(11, 12)),
              T_('c', r'Increase $\$80$ by $15\%$', 1, r'$\$92$', close(80 * 1.15, 92))]
        Q2 = [T_('a', r'Simplify $5x + 3y - 2x$', 1, '$3x + 3y$', lambda: S('5x+3y-2x', '3x+3y')),
              T_('b', r'Simplify $4a \times 3b$', 1, '$12ab$', lambda: S('4a*3b', '12ab')),
              T_('c', r'Evaluate $2p + q$ when $p = -3$ and $q = 4$', 1, '$-2$', 2 * -3 + 4 == -2)]
        Q3 = [T_('a', r'Expand $3(x + 4)$', 1, '$3x + 12$', lambda: E('3(x+4)', '3x+12')),
              T_('b', r'Expand and simplify $2(a + 3) + 4a$', 1, '$6a + 6$', lambda: E('2(a+3)+4a', '6a+6')),
              T_('c', r'Factorise $12m + 18$', 1, '$6(2m + 3)$', lambda: F('12m+18', '6(2m+3)'))]
        Q4 = [T_('a', r'Write $5^7 \times 5^2 \div 5^6$ as a single power', 1, '$5^3$', 7 + 2 - 6 == 3),
              T_('b', r'Evaluate $2^3 \times 3^2$', 1, '$72$', 8 * 9 == 72),
              T_('c', r'Write $180$ as a product of prime factors', 1, r'$2^2 \times 3^2 \times 5$', 4 * 9 * 5 == 180)]
        Q5 = [T_('a', 'Find $c$.' + right_tri(12, 9, '12 cm', '9 cm', 'c'), 1, '$15$ cm', hyp(9, 12) == 15),
              T_('b', 'Find $x$.' + right_tri(8, 6, 'x', '6 cm', '10 cm'), 1, '$8$ cm', math.sqrt(100 - 36) == 8),
              T_('c', r'Find the hypotenuse if the shorter sides are $4$ cm and $7$ cm (1 d.p.)', 1, r'$\sqrt{65} \approx 8.1$ cm', r(hyp(4, 7), 1) == 8.1)]
        Q6 = [T_('a', r'Solve $4x - 7 = 13$', 1, '$x = 5$', lambda: Q('4x-7=13', ['5'])),
              T_('b', r'Solve $5a + 3 = 2a + 9$', 1, '$a = 2$', lambda: Q('5a+3=2a+9', ['2'])),
              T_('c', r'Solve $2x^2 = 72$', 1, r'$x = \pm 6$', lambda: Q('2x^2=72', ['6', '-6']))]
        Q7 = [T_('a', r'Find the area of a trapezium with parallel sides $5$ cm and $9$ cm and height $4$ cm.', 1, r'$28\ \text{cm}^2$', 2 * 14 == 28),
              T_('b', r'Find the volume of a cylinder with radius $3$ cm and height $5$ cm (1 d.p.).', 1, r'$141.4\ \text{cm}^3$', r(PI * 45, 1) == 141.4)]
    else:
        Q1 = [T_('a', r'Evaluate $-10 + 2 \times (-4)$', 1, '$-18$', -10 + 2 * -4 == -18),
              T_('b', r'Evaluate $\tfrac{3}{5} + \tfrac{1}{2}$', 1, r'$\tfrac{11}{10} = 1\tfrac{1}{10}$', Fr(3, 5) + Fr(1, 2) == Fr(11, 10)),
              T_('c', r'Decrease $\$90$ by $20\%$', 1, r'$\$72$', close(90 * 0.8, 72))]
        Q2 = [T_('a', r'Simplify $7m + 2n - 3m$', 1, '$4m + 2n$', lambda: S('7m+2n-3m', '4m+2n')),
              T_('b', r'Simplify $5x \times 2y$', 1, '$10xy$', lambda: S('5x*2y', '10xy')),
              T_('c', r'Evaluate $3a - b$ when $a = -2$ and $b = 5$', 1, '$-11$', 3 * -2 - 5 == -11)]
        Q3 = [T_('a', r'Expand $5(y - 2)$', 1, '$5y - 10$', lambda: E('5(y-2)', '5y-10')),
              T_('b', r'Expand and simplify $3(m + 2) + 2m$', 1, '$5m + 6$', lambda: E('3(m+2)+2m', '5m+6')),
              T_('c', r'Factorise $15k + 20$', 1, '$5(3k + 4)$', lambda: F('15k+20', '5(3k+4)'))]
        Q4 = [T_('a', r'Write $3^8 \times 3^2 \div 3^7$ as a single power', 1, '$3^3$', 8 + 2 - 7 == 3),
              T_('b', r'Evaluate $2^4 \times 5$', 1, '$80$', 16 * 5 == 80),
              T_('c', r'Write $252$ as a product of prime factors', 1, r'$2^2 \times 3^2 \times 7$', 4 * 9 * 7 == 252)]
        Q5 = [T_('a', 'Find $c$.' + right_tri(20, 15, '20 cm', '15 cm', 'c'), 1, '$25$ cm', hyp(15, 20) == 25),
              T_('b', 'Find $x$.' + right_tri(12, 5, 'x', '5 cm', '13 cm'), 1, '$12$ cm', math.sqrt(169 - 25) == 12),
              T_('c', r'Find the hypotenuse if the shorter sides are $5$ cm and $9$ cm (1 d.p.)', 1, r'$\sqrt{106} \approx 10.3$ cm', r(hyp(5, 9), 1) == 10.3)]
        Q6 = [T_('a', r'Solve $3x + 8 = 29$', 1, '$x = 7$', lambda: Q('3x+8=29', ['7'])),
              T_('b', r'Solve $7a - 5 = 3a + 11$', 1, '$a = 4$', lambda: Q('7a-5=3a+11', ['4'])),
              T_('c', r'Solve $3x^2 = 75$', 1, r'$x = \pm 5$', lambda: Q('3x^2=75', ['5', '-5']))]
        Q7 = [T_('a', r'Find the area of a trapezium with parallel sides $6$ cm and $10$ cm and height $5$ cm.', 1, r'$40\ \text{cm}^2$', 2.5 * 16 == 40),
              T_('b', r'Find the volume of a cylinder with radius $2$ cm and height $7$ cm (1 d.p.).', 1, r'$88.0\ \text{cm}^3$', r(PI * 28, 1) == 88.0)]
    return [('1', 'Number skills', 'L1', Q1), ('2', 'Algebra basics', 'L2', Q2), ('3', 'Expanding & factorising', 'L3', Q3),
            ('4', 'Indices', 'L4', Q4), ('5', "Pythagoras' theorem", 'L5', Q5), ('6', 'Solve', 'L6', Q6), ('7', 'Area and volume', 'L7', Q7)]


PRE = make_test('pre')
POST = make_test('post')
