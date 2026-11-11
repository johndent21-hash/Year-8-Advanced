import sys, os, math
from fractions import Fraction as Fr
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'build'))
from dsl import S, E, F, Q, V, N, L, Item, ERRORS, to_sympy, sp, tex, close, r
from svg import right_tri
from hsvg import straight_angle, crossing, parallel, l_shape, house, rect_diag, tri_angles

SLOTS = [  # (topic group, label)
    ('num', 'Fractions & integers'), ('num', 'Percentages & rounding'), ('ind', 'Indices'), ('ind', 'Roots & surds'),
    ('alg', 'Simplify & substitute'), ('alg', 'Expand'), ('alg', 'Factorise'), ('eq', 'Equations'),
    ('eq', 'Equations'), ('eq', 'Formulas'), ('meas', 'Pythagoras'), ('meas', 'Area'), ('meas', 'Volume'),
    ('lin', 'Number plane'), ('lin', 'Gradient'), ('lin', 'y = mx + c'), ('geo', 'Angles'), ('geo', 'Probability'),
    ('ctx', 'Algebra in context'), ('ctx', 'Measurement in context')]


def W(item, work, diag=None, h=None):
    """attach brief working (and optional diagram) to an item"""
    item.w = work
    item.diag = diag
    return item


def H(q, a, work, check, star=False, diag=None):
    return W(N(q, a, check, star=star), work, diag)


def grad(p, q):
    return Fr(q[1] - p[1], q[0] - p[0])


def mean(xs):
    return Fr(sum(xs), len(xs))


# =====================================================================
WEEKS = []

# ---------------------------------------------------------------- WEEK 1
WEEKS.append(dict(n=1, items=[
    W(S('[3|4]+[2|3]', '[17|12]', verb='Evaluate'), r'$\tfrac{9}{12} + \tfrac{8}{12} = \tfrac{17}{12} = 1\tfrac{5}{12}$'),
    H(r'Increase $\$80$ by $15\%$.', r'$\$92$', r'$15\%$ of $80 = 12$; $80 + 12 = 92$', close(80 * 1.15, 92)),
    W(S('2^5*2^3÷2^4', '2^4', verb='Write as a single power:'), r'$2^{5+3-4} = 2^4\ (=16)$'),
    W(S('sqrt(36)+cbrt(8)', '8', verb='Evaluate'), r'$6 + 2 = 8$'),
    W(S('7a+3b-2a+b', '5a+4b', verb='Simplify'), r'$7a - 2a = 5a$; $3b + b = 4b$'),
    W(E('4(3x-5)', '12x-20', verb='Expand'), r'$4 \times 3x - 4 \times 5$'),
    W(F('6x+9', '3(2x+3)', verb='Factorise'), r'HCF $= 3$'),
    W(Q('3x-7=11', ['6'], verb='Solve'), r'$3x = 18$, $x = 6$'),
    W(Q('5x+2=2x+17', ['5'], verb='Solve'), r'$3x + 2 = 17$, $3x = 15$'),
    H(r'$P = 2(l + w)$. Find $P$ when $l = 8$ and $w = 3.5$.', '$P = 23$', r'$2 \times 11.5 = 23$', 2 * (8 + 3.5) == 23),
    H(r'Find $c$. (cm)', '$10$ cm', r'$c^2 = 36 + 64 = 100$', math.hypot(6, 8) == 10, diag=right_tri(8, 6, '8', '6', 'c', maxw=18, maxh=11)),
    H(r'Find the area of a trapezium with parallel sides $6$ cm and $10$ cm and height $4$ cm.', r'$32\ \text{cm}^2$',
      r'$\tfrac{4}{2}(6 + 10) = 2 \times 16$', 2 * 16 == 32),
    H(r'Find the volume of a rectangular prism $6$ cm by $5$ cm by $4$ cm.', r'$120\ \text{cm}^3$', r'$6 \times 5 \times 4$', 6 * 5 * 4 == 120),
    H(r'Complete the table for $y = 2x - 1$.<table class="tv"><tr><td>$x$</td><td>$-1$</td><td>$0$</td><td>$1$</td><td>$2$</td></tr><tr><td>$y$</td><td></td><td></td><td></td><td></td></tr></table>',
      r'$-3,\ -1,\ 1,\ 3$', r'substitute each $x$: e.g. $2(-1) - 1 = -3$', [2 * x - 1 for x in (-1, 0, 1, 2)] == [-3, -1, 1, 3]),
    H(r'Find the gradient of the interval joining $(1,\,2)$ and $(3,\,8)$.', '$3$', r'$\dfrac{\text{rise}}{\text{run}} = \dfrac{8 - 2}{3 - 1} = \dfrac{6}{2}$',
      grad((1, 2), (3, 8)) == 3, star=True),
    H(r'State the gradient and $y$-intercept of $y = 3x - 4$.', r'$m = 3$, $c = -4$', r'compare with $y = mx + c$', True, star=True),
    H(r'Find $a$.', r'$a = 55$', r'angles on a straight line: $180 - 125$', 180 - 125 == 55, diag=straight_angle(125, '125°', 'a°')),
    H(r'A fair die is rolled. Find $P(\text{number greater than } 4)$.', r'$\tfrac{1}{3}$', r'$\{5, 6\}$: $\tfrac{2}{6}$', Fr(2, 6) == Fr(1, 3)),
    H(r'Mia has $\$40$ and saves $\$15$ each week of the holidays. Write a rule for her savings $S$ after $w$ weeks, then find $S$ after $6$ weeks.',
      r'$S = 40 + 15w$; $\$130$', r'$40 + 15 \times 6 = 130$', 40 + 15 * 6 == 130),
    H(r'A rectangular pool area, $12$ m by $7.5$ m, is fenced on all four sides. How much fencing is needed?', '$39$ m',
      r'$2(12 + 7.5) = 39$', 2 * (12 + 7.5) == 39),
], bonus=H(r'Find two consecutive whole numbers whose squares differ by $15$.', '$7$ and $8$',
           r'$(n+1)^2 - n^2 = 2n + 1 = 15$, so $n = 7$; check $64 - 49 = 15$', 64 - 49 == 15)))

# ---------------------------------------------------------------- WEEK 2
WEEKS.append(dict(n=2, items=[
    W(S('-8+(-5)*3', '-23', verb='Evaluate'), r'$-8 + (-15) = -23$ (multiply first)'),
    H(r'Round $12.6849$ to $2$ decimal places.', '$12.68$', r'third decimal is $4$, so round down', r(12.6849, 2) == 12.68),
    H(r'Write $72$ as a product of prime factors in index form.', r'$2^3 \times 3^2$', r'$72 = 8 \times 9$', 8 * 9 == 72),
    W(S('sqrt(50)', '5sqrt(2)', star=True, verb='Simplify'), r'$\sqrt{25 \times 2} = 5\sqrt2$'),
    W(V('a^2-3b', {'a': -2, 'b': 5}, '-11', verb='If $a=-2,\\ b=5$:'), r'$(-2)^2 - 15 = 4 - 15$'),
    W(E('3(x+4)+2(x-1)', '5x+10', verb='Expand and simplify'), r'$3x + 12 + 2x - 2$'),
    W(F('8a^2-12a', '4a(2a-3)', verb='Factorise'), r'HCF $= 4a$'),
    W(Q('[x|4]+3=8', ['20'], verb='Solve'), r'$\tfrac{x}{4} = 5$, $x = 20$'),
    W(Q('3(x-2)=15', ['7'], verb='Solve'), r'$x - 2 = 5$'),
    H(r'$v = u + at$. Find $a$ when $v = 30$, $u = 6$ and $t = 8$.', '$a = 3$', r'$30 = 6 + 8a$, $8a = 24$', 6 + 8 * 3 == 30),
    H(r'Find $x$. (cm)', '$12$ cm', r'$x^2 = 169 - 25 = 144$', math.sqrt(169 - 25) == 12, diag=right_tri(12, 5, 'x', '5', '13', maxw=18, maxh=11)),
    H(r'Find the area of a circle with radius $5$ cm, in terms of $\pi$.', r'$25\pi\ \text{cm}^2$', r'$\pi \times 5^2$', True),
    H(r'Find the volume of a cylinder with radius $2$ cm and height $10$ cm, in terms of $\pi$.', r'$40\pi\ \text{cm}^3$', r'$\pi \times 2^2 \times 10$', 4 * 10 == 40),
    H(r'Does the point $(3,\,7)$ lie on the line $y = 3x - 2$?', r'Yes', r'$3(3) - 2 = 7$ ✓', 3 * 3 - 2 == 7),
    H(r'Find the gradient of the interval joining $(0,\,5)$ and $(4,\,-3)$.', '$-2$', r'$\dfrac{-3 - 5}{4 - 0} = \dfrac{-8}{4}$', grad((0, 5), (4, -3)) == -2, star=True),
    H(r'Write the equation of the line with gradient $2$ and $y$-intercept $-5$.', '$y = 2x - 5$', r'$y = mx + c$ with $m = 2$, $c = -5$', True, star=True),
    H(r'Find $x$.', r'$x = 65$', r'angle sum: $180 - 48 - 67$', 180 - 48 - 67 == 65, diag=tri_angles(48, 67, '48°', '67°', 'x°')),
    H(r'A bag has $3$ red, $5$ blue and $2$ green marbles. Find $P(\text{not blue})$.', r'$\tfrac{1}{2}$', r'$\tfrac{5}{10}$ are not blue', Fr(5, 10) == Fr(1, 2)),
    H(r'Ella pays $\$x$ towards a beach umbrella, Jack pays $\$5$ more than Ella and Sam pays twice what Ella pays. The umbrella costs $\$45$. Find $x$.',
      r'$x = 10$', r'$x + (x + 5) + 2x = 45$, $4x = 40$', 10 + 15 + 20 == 45),
    H(r'A triangular sail has base $2.4$ m and perpendicular height $3$ m. Find its area.', r'$3.6\ \text{m}^2$', r'$\tfrac12 \times 2.4 \times 3$', close(0.5 * 2.4 * 3, 3.6)),
], bonus=H(r'Solve $x^2 = 2x$. (Careful – there are two answers.)', '$x = 0$ or $x = 2$',
           r'$x^2 - 2x = 0$, $x(x - 2) = 0$; dividing by $x$ loses $x = 0$', set(sp.solve(to_sympy('x^2-2x'))) == {0, 2})))

# ---------------------------------------------------------------- WEEK 3
WEEKS.append(dict(n=3, items=[
    H(r'Evaluate $2\tfrac{1}{2} \times 1\tfrac{3}{5}$.', '$4$', r'$\tfrac{5}{2} \times \tfrac{8}{5} = \tfrac{40}{10}$', Fr(5, 2) * Fr(8, 5) == 4),
    H(r'Write $\tfrac{3}{8}$ as a percentage.', r'$37.5\%$', r'$\tfrac{3}{8} = 0.375$', Fr(3, 8) * 100 == Fr(75, 2)),
    W(S('(3^2)^3÷3^4', '9', verb='Evaluate'), r'$3^6 \div 3^4 = 3^2$'),
    W(S('sqrt(3)*sqrt(12)', '6', verb='Evaluate'), r'$\sqrt{36} = 6$'),
    W(S('12x^2y÷4xy', '3x', verb='Simplify'), r'$\dfrac{12x^2y}{4xy}$'),
    W(E('(x+3)(x+5)', 'x^2+8x+15', star=True, verb='Expand'), r'$x^2 + 5x + 3x + 15$'),
    W(F('15xy-10x', '5x(3y-2)', verb='Factorise'), r'HCF $= 5x$'),
    W(Q('7-2x=1', ['3'], verb='Solve'), r'$-2x = -6$'),
    W(Q('6x-4=2x+10', ['[7|2]'], verb='Solve'), r'$4x = 14$, $x = 3.5$'),
    H(r'$A = \tfrac{1}{2}bh$. Find $b$ when $A = 24$ and $h = 6$.', '$b = 8$', r'$24 = 3b$', 0.5 * 8 * 6 == 24),
    H(r'Is a triangle with sides $7$, $24$ and $25$ right-angled?', 'Yes', r'$49 + 576 = 625 = 25^2$', 49 + 576 == 625),
    H(r'Find the area. (cm)', r'$51\ \text{cm}^2$', r'$9 \times 7 - 4 \times 3 = 63 - 12$', 9 * 7 - 4 * 3 == 51,
      diag=l_shape(9, 7, 4, 3, ['9', '4', '4', '7'])),
    H(r'A triangular prism has a triangle of base $6$ cm and height $4$ cm as its cross-section, and length $12$ cm. Find its volume.',
      r'$144\ \text{cm}^3$', r'$A = 12$; $V = 12 \times 12$', 0.5 * 6 * 4 * 12 == 144),
    H(r'For $y = -2x + 5$, find $y$ when $x = 3$.', '$y = -1$', r'$-6 + 5$', -2 * 3 + 5 == -1),
    H(r'Find the gradient of the interval joining $(-2,\,1)$ and $(4,\,4)$.', r'$\tfrac{1}{2}$', r'$\dfrac{4 - 1}{4 - (-2)} = \dfrac{3}{6}$', grad((-2, 1), (4, 4)) == Fr(1, 2), star=True),
    H(r'Which line is steeper: $y = 2x + 7$ or $y = 5x - 1$? Why?', r'$y = 5x - 1$', r'larger gradient: $5 > 2$', 5 > 2, star=True),
    H(r'The lines are parallel. Find $x$.', r'$x = 108$', r'co-interior angles: $180 - 72$', 180 - 72 == 108, diag=parallel(108, '72°', 'x°')),
    H(r'The probability that a spinner lands on red is $0.35$. Find $P(\text{not red})$.', '$0.65$', r'$1 - 0.35$', close(1 - 0.35, 0.65)),
    H(r'Kayak hire on the Tweed River costs $\$20$ plus $\$15$ per hour. Lily paid $\$95$. Write an equation and find how many hours she hired it for.',
      r'$5$ hours', r'$20 + 15h = 95$, $15h = 75$', 20 + 15 * 5 == 95),
    H(r'A sandpit $3$ m by $2$ m is filled with sand $0.25$ m deep. Find the volume of sand.', r'$1.5\ \text{m}^3$', r'$3 \times 2 \times 0.25$', close(3 * 2 * 0.25, 1.5)),
], bonus=H(r'Show that the sum of any three consecutive whole numbers is always divisible by $3$.', r'$n + (n+1) + (n+2) = 3n + 3 = 3(n + 1)$',
           r'a multiple of $3$ for every $n$', all((n + n + 1 + n + 2) % 3 == 0 for n in range(50)))))

# ---------------------------------------------------------------- WEEK 4
WEEKS.append(dict(n=4, items=[
    W(S('(-3)^2-4*(-2)', '17', verb='Evaluate'), r'$9 + 8$'),
    H(r'Decrease $\$250$ by $20\%$.', r'$\$200$', r'$20\%$ of $250 = 50$', 250 * 0.8 == 200),
    W(S('5^0+2^3*3', '25', verb='Evaluate'), r'$1 + 8 \times 3 = 1 + 24$'),
    H(r'Estimate $\sqrt{70}$ to $1$ decimal place. (Check by squaring.)', '$8.4$', r'$8.3^2 = 68.89$, $8.4^2 = 70.56$; $70$ is closer to $70.56$', r(math.sqrt(70), 1) == 8.4),
    H(r'Write an expression for “$5$ less than three times $n$”.', '$3n - 5$', r'three times $n$ is $3n$; then subtract $5$', True),
    W(E('x(2x+7)-3x', '2x^2+4x', verb='Expand and simplify'), r'$2x^2 + 7x - 3x$'),
    W(F('9p+12q', '3(3p+4q)', verb='Factorise'), r'HCF $= 3$'),
    W(Q('[2x|5]=6', ['15'], verb='Solve'), r'$2x = 30$'),
    W(Q('3x+8=5x-4', ['6'], verb='Solve'), r'$8 = 2x - 4$, $2x = 12$'),
    H(r'Make $x$ the subject of $y = 4x - 3$.', r'$x = \dfrac{y + 3}{4}$', r'$y + 3 = 4x$',
      sp.simplify(sp.solve(to_sympy('4x-3-y'), sp.Symbol('x'))[0] - to_sympy('[y+3|4]')) == 0, star=True),
    H(r'A $2.5$ m ladder leans against a wall with its foot $0.7$ m from the wall. How high does it reach?', '$2.4$ m',
      r'$h^2 = 6.25 - 0.49 = 5.76$', close(math.sqrt(6.25 - 0.49), 2.4)),
    H(r'Find the area of a kite with diagonals $8$ cm and $11$ cm.', r'$44\ \text{cm}^2$', r'$\tfrac12 \times 8 \times 11$', 0.5 * 8 * 11 == 44),
    H(r'Find the volume of a cylinder with diameter $6$ cm and height $5$ cm, in terms of $\pi$.', r'$45\pi\ \text{cm}^3$', r'$r = 3$: $\pi \times 9 \times 5$', 9 * 5 == 45),
    H(r'Which point is <b>not</b> on $y = x + 4$: &nbsp;$(0, 4)$, $(2, 6)$, $(-1, 5)$, $(-4, 0)$?', r'$(-1,\,5)$', r'$-1 + 4 = 3 \ne 5$',
      all(y == x + 4 for x, y in [(0, 4), (2, 6), (-4, 0)]) and 5 != -1 + 4),
    H(r'Find the gradient of the interval joining $(-3,\,5)$ and $(6,\,5)$. What kind of line is it?', r'$0$; horizontal', r'rise $= 0$', grad((-3, 5), (6, 5)) == 0, star=True),
    H(r'Write $2x + y = 7$ in the form $y = mx + c$ and state the gradient.', r'$y = -2x + 7$; $m = -2$', r'subtract $2x$ from both sides', True, star=True),
    H(r'Find $x$.', r'$x = 30$', r'vertically opposite: $2x + 10 = 70$', 2 * 30 + 10 == 70, diag=crossing(70, '70°', '(2x + 10)°')),
    H(r'A letter is chosen at random from the word KINGSCLIFF. Find $P(\text{F})$.', r'$\tfrac{1}{5}$', r'$2$ F’s out of $10$ letters',
      Fr('KINGSCLIFF'.count('F'), len('KINGSCLIFF')) == Fr(1, 5)),
    H(r'A triangle has sides $x$, $x + 3$ and $2x - 1$ cm. Its perimeter is $30$ cm. Find $x$.', '$x = 7$', r'$4x + 2 = 30$', 7 + 10 + 13 == 30),
    H(r'A circular garden bed has diameter $6$ m. Find its area in terms of $\pi$.', r'$9\pi\ \text{m}^2$', r'$r = 3$: $\pi \times 3^2$', True),
], bonus=H(r'A square has area $50\ \text{cm}^2$. Find its side length in simplest surd form, and the length of its diagonal.',
           r'$5\sqrt2$ cm; $10$ cm', r'$\sqrt{50} = 5\sqrt2$; diagonal$^2 = 50 + 50 = 100$', sp.sqrt(50) == 5 * sp.sqrt(2))))

# ---------------------------------------------------------------- WEEK 5
WEEKS.append(dict(n=5, items=[
    W(S('[5|6]-[1|4]', '[7|12]', verb='Evaluate'), r'$\tfrac{10}{12} - \tfrac{3}{12}$'),
    H(r'Round $0.04682$ to $2$ significant figures.', '$0.047$', r'first significant figure is $4$; next digit $8$ rounds up', float(f'{0.04682:.2g}') == 0.047, star=True),
    W(S('[7^5|7^3]', '49', verb='Evaluate'), r'$7^{5-3} = 7^2$'),
    W(S('sqrt(16*25)', '20', verb='Evaluate'), r'$4 \times 5$'),
    W(V('(p-q)^2', {'p': 3, 'q': -4}, '49', verb='If $p=3,\\ q=-4$:'), r'$(3 - (-4))^2 = 7^2$'),
    W(E('5(2a-1)-3a', '7a-5', verb='Expand and simplify'), r'$10a - 5 - 3a$'),
    W(F('12xy+18y^2', '6y(2x+3y)', verb='Factorise'), r'HCF $= 6y$'),
    W(Q('[x|3]-4=2', ['18'], verb='Solve'), r'$\tfrac{x}{3} = 6$'),
    W(Q('2(x+5)=18', ['4'], verb='Solve'), r'$x + 5 = 9$'),
    H(r'$C = 2\pi r$. Find $r$ when $C = 18\pi$.', '$r = 9$', r'$2\pi r = 18\pi$', 2 * 9 == 18),
    H(r'Find the exact length of the hypotenuse if the shorter sides are $3$ and $5$.', r'$\sqrt{34}$', r'$9 + 25 = 34$', 9 + 25 == 34),
    H(r'Find the area of a semicircle with diameter $8$ cm, in terms of $\pi$.', r'$8\pi\ \text{cm}^2$', r'$\tfrac12 \times \pi \times 4^2$', 0.5 * 16 == 8),
    H(r'A prism has volume $96\ \text{cm}^3$ and length $8$ cm. Find the area of its cross-section.', r'$12\ \text{cm}^2$', r'$96 \div 8$', 96 / 8 == 12),
    H(r'Find the point where $y = x + 1$ and $y = 7 - x$ meet.', r'$(3,\,4)$', r'$x + 1 = 7 - x$, $x = 3$', 3 + 1 == 7 - 3 == 4),
    H(r'Find the gradient of the interval joining $(2,\,-1)$ and $(5,\,11)$.', '$4$', r'$\dfrac{11 - (-1)}{5 - 2} = \dfrac{12}{3}$', grad((2, -1), (5, 11)) == 4, star=True),
    H(r'Write the equation of the line with gradient $-4$ that passes through $(0,\,3)$.', '$y = -4x + 3$', r'$(0, 3)$ is the $y$-intercept', True, star=True),
    H(r'Three angles of a quadrilateral are $95°$, $80°$ and $110°$. Find the fourth.', r'$75°$', r'$360 - 285$', 360 - 95 - 80 - 110 == 75),
    H(r'In a class of $28$, $12$ students have been to a Gold Coast theme park. A student is chosen at random. Find $P(\text{has not been})$.',
      r'$\tfrac{4}{7}$', r'$\tfrac{16}{28}$', Fr(16, 28) == Fr(4, 7)),
    H(r'Ava is $4$ years older than her brother. In $3$ years their ages will add to $30$. How old is Ava now?', '$14$',
      r'$b + 3 + b + 7 = 30$, $b = 10$', (10 + 3) + (14 + 3) == 30),
    H(r'An esky measures $50$ cm by $30$ cm by $30$ cm inside. Find its capacity in litres. ($1000\ \text{cm}^3 = 1$ L)', '$45$ L',
      r'$45\,000\ \text{cm}^3$', 50 * 30 * 30 == 45000),
], bonus=W(E('(x+2)^2-(x-2)^2', '8x', verb='Expand and simplify'), r'$(x^2 + 4x + 4) - (x^2 - 4x + 4)$')))

# ---------------------------------------------------------------- WEEK 6
WEEKS.append(dict(n=6, items=[
    H(r'Evaluate $-24 \div (-6) + 3 \times (-2)$', '$-2$', r'$4 + (-6)$', (-24) / (-6) + 3 * (-2) == -2),
    H(r'A $\$120$ cricket bat is on sale for $\$90$. What is the percentage discount?', r'$25\%$', r'$\tfrac{30}{120} = \tfrac14$', Fr(30, 120) == Fr(1, 4)),
    W(S('2^4*5^4', '10000', verb='Evaluate'), r'$(2 \times 5)^4 = 10^4 = 10\,000$'),
    H(r'Between which two consecutive whole numbers does $\sqrt{90}$ lie?', '$9$ and $10$', r'$81 < 90 < 100$', 81 < 90 < 100),
    W(S('4ab*3a÷6b', '2a^2', verb='Simplify'), r'$\dfrac{12a^2b}{6b}$'),
    W(E('(2x-1)(x+4)', '2x^2+7x-4', star=True, verb='Expand'), r'$2x^2 + 8x - x - 4$'),
    W(F('9m^2+6m', '3m(3m+2)', verb='Factorise'), r'HCF $= 3m$'),
    W(Q('5-3x=17', ['-4'], verb='Solve'), r'$-3x = 12$'),
    W(Q('[x+4|3]=5', ['11'], verb='Solve'), r'$x + 4 = 15$'),
    H(r'$E = \tfrac{1}{2}mv^2$. Find $E$ when $m = 4$ and $v = 6$.', '$E = 72$', r'$\tfrac12 \times 4 \times 36$', 0.5 * 4 * 36 == 72),
    H(r'Find the length of the diagonal $d$. (cm)', '$13$ cm', r'$d^2 = 144 + 25 = 169$', math.hypot(12, 5) == 13, diag=rect_diag(12, 5, '12', '5', 'd')),
    H(r'Find the area. (cm)', r'$52\ \text{cm}^2$', r'$8 \times 5 + \tfrac12 \times 8 \times 3$', 8 * 5 + 0.5 * 8 * 3 == 52, diag=house(8, 5, 3, ['8', '5', '3'])),
    H(r'A prism has a trapezium cross-section (parallel sides $3$ cm and $7$ cm, height $4$ cm) and length $10$ cm. Find its volume.',
      r'$200\ \text{cm}^3$', r'$A = \tfrac42(3 + 7) = 20$', 2 * 10 * 10 == 200),
    H(r'Find the rule linking $x$ and $y$.<table class="tv"><tr><td>$x$</td><td>$0$</td><td>$1$</td><td>$2$</td><td>$3$</td></tr><tr><td>$y$</td><td>$5$</td><td>$8$</td><td>$11$</td><td>$14$</td></tr></table>',
      '$y = 3x + 5$', r'$y$ goes up by $3$; starts at $5$', [3 * x + 5 for x in range(4)] == [5, 8, 11, 14]),
    H(r'Find the gradient of the interval joining $(-4,\,7)$ and $(2,\,-2)$.', r'$-\tfrac{3}{2}$', r'$\dfrac{-2 - 7}{2 - (-4)} = \dfrac{-9}{6}$', grad((-4, 7), (2, -2)) == Fr(-3, 2), star=True),
    H(r'A line passes through $(0,\,-2)$ and $(3,\,4)$. Find its equation.', '$y = 2x - 2$', r'$m = \tfrac{6}{3} = 2$, $c = -2$', grad((0, -2), (3, 4)) == 2, star=True),
    H(r'An isosceles triangle has an apex angle of $40°$. Find each base angle.', r'$70°$', r'$(180 - 40) \div 2$', (180 - 40) / 2 == 70),
    H(r'A whole number from $1$ to $20$ is chosen at random. Find $P(\text{multiple of } 3 \text{ or } 5)$.', r'$\tfrac{9}{20}$',
      r'$3, 5, 6, 9, 10, 12, 15, 18, 20$', len([k for k in range(1, 21) if k % 3 == 0 or k % 5 == 0]) == 9),
    H(r'A cricket team scored $x$ runs in its first innings and $45$ fewer in its second. The total was $215$. Find $x$.', '$x = 130$',
      r'$2x - 45 = 215$', 130 + 85 == 215),
    H(r'A circular trampoline has radius $2$ m. A safety net goes around its edge. Find the length of the net in terms of $\pi$.', r'$4\pi$ m',
      r'$C = 2\pi r = 2\pi \times 2$', True),
], bonus=H(r'A right-angled triangle has sides $x$, $x + 7$ and $x + 8$. Find $x$.', '$x = 5$ (sides $5, 12, 13$)',
           r'$x^2 + (x+7)^2 = (x+8)^2 \Rightarrow x^2 - 2x - 15 = 0$', 25 + 144 == 169 and set(sp.solve(to_sympy('x^2+(x+7)^2-(x+8)^2'))) == {5, -3})))

for wk in WEEKS:
    assert len(wk['items']) == 20, (wk['n'], len(wk['items']))
    for i, it in enumerate(wk['items']):
        it.n = i + 1
        it.slot = SLOTS[i]
        if not hasattr(it, 'diag'):
            it.diag = None
    wk['bonus'].n = 'B'
    if not hasattr(wk['bonus'], 'diag'):
        wk['bonus'].diag = None
