"""Year 10 Advanced -> Year 11 Mathematics Advanced (Stage 5 path revision, Stage 6 preview)."""
import math
from qlib import Q, B, xy, stemleaf
import diagrams as D

BK = dict(
    key='b6',
    file='Yr10_Advanced_Summer_Holiday_Ready_for_Yr11_Advanced_Revision_Booklet',
    kicker='YEAR 10 ADVANCED → YEAR 11 MATHEMATICS ADVANCED',
    ready='Ready for Year 11',
    intro='Six weeks. Twenty questions a week. Every Year 10 skill that Year 11 Mathematics Advanced builds on – mixed together so it sticks.',
    star_text='Year 11 preview (Stage 6 Advanced)',
    pattern='Question 1 is always indices, question 10 is always functions, and so on. If the same number keeps going wrong, that is the skill to revise before Year 11.',
    groups=[('Indices, surds & logs', '', [1, 2, 3]), ('Algebra', '', [4, 5, 6]), ('Equations', '', [7, 8, 9]),
            ('Functions & graphs', '', [10, 11, 12]), ('Coordinate geometry', '', [13, 14]), ('Trigonometry', '', [15, 16]),
            ('Geometry & chance', '', [17, 18]), ('In context', '', [19, 20])],
    strands={1: 'Indices', 2: 'Surds', 3: 'Logarithms', 4: 'Expand', 5: 'Factorise', 6: 'Algebraic fractions',
             7: 'Linear equations & inequalities', 8: 'Quadratic equations', 9: 'Simultaneous equations',
             10: 'Functions', 11: 'Graphs', 12: 'Polynomials', 13: 'Lines', 14: 'Coordinate geometry',
             15: 'Trig ratios & exact values', 16: 'Sine & cosine rules', 17: 'Geometry', 18: 'Probability',
             19: 'Financial maths', 20: 'Problem solving'},
    rules=['<b>No calculator.</b> Leave answers exact (e.g. $2 \\pm \\sqrt{5}$ or $\\frac{3\\pi}{4}$) unless asked to round.',
           '<b>Show working</b> in the space under each question.',
           '<b>Mark it yourself</b> using the answers at the back (pages 10–12). Each answer has a line of working to help you find a mistake.',
           '<b>Fix it.</b> Redo anything you got wrong a day or two later, without looking.',
           '<span class="star">★</span> questions preview Year 11 Mathematics Advanced (Stage 6). Have a go – they are the ones that will help most in Term 1.',
           '<b>Stuck?</b> The hints page (page 9) has the key facts and formulas.'],
    first_up='<b>First up in Year 11 Mathematics Advanced:</b> working with functions, graph transformations, trigonometry and measure of angles, exponential and logarithmic functions, and an introduction to differentiation. Every one of them starts from the skills in these six pages.',
    outcomes='Revises MA5-IND-P-01, MA5-IND-P-02, MA5-LOG-P-01, MA5-ALG-P-01, MA5-ALG-P-02, MA5-EQU-P-01, MA5-EQU-P-02, MA5-FNC-P-01, MA5-NLI-P-01, MA5-POL-P-01, MA5-LIN-P-01, MA5-TRG-P-01, MA5-TRG-P-02, MA5-CIR-P-01, MA5-GEO-P-01, MA5-PRO-C-01, MA5-PRO-P-01, MA5-FIN-C-02. <span class="star">★</span> Year 11 preview: Mathematics Advanced 11–12 (2024) focus areas Working with functions; Trigonometry and measure of angles; Trigonometric identities and equations; Introduction to differentiation.',
)

W, BON = [], []

# ---------------- Week 1 ----------------
W.append([
    Q('Evaluate $8^{\\frac{2}{3}} + 4^{-\\frac{1}{2}}$', '$4\\tfrac{1}{2}$', '$2^2 + \\frac{1}{2}$', c=('eq', '8**Rational(2,3)+4**Rational(-1,2)', 'Rational(9,2)')),
    Q('Simplify $\\sqrt{75} - \\sqrt{12}$', '$3\\sqrt{3}$', '$5\\sqrt{3} - 2\\sqrt{3}$', c=('eq', 'sqrt(75)-sqrt(12)', '3*sqrt(3)')),
    Q('Evaluate $\\log_3 81$', '$4$', '$3^4 = 81$', c=('eq', 'log(81,3)', '4')),
    Q('Expand $(2x - 5)(x + 3)$', '$2x^2 + x - 15$', '$2x^2 + 6x - 5x - 15$', c=('eq', 'expand((2*x-5)*(x+3))', '2*x**2+x-15')),
    Q('Factorise $x^2 - 3x - 28$', '$(x - 7)(x + 4)$', '$-7 \\times 4 = -28$, $-7 + 4 = -3$', c=('fac', 'x**2-3*x-28', '(x-7)*(x+4)')),
    Q('Simplify $\\dfrac{x + 2}{3} + \\dfrac{x - 1}{4}$', '$\\frac{7x + 5}{12}$', '$\\frac{4(x + 2) + 3(x - 1)}{12}$', c=('eq', '(x+2)/3+(x-1)/4', '(7*x+5)/12')),
    Q('Solve $7 - 3x \\ge 19$', '$x \\le -4$', '$-3x \\ge 12$; divide by $-3$ and reverse', c=('py', 'sp.solve_univariate_inequality(7-3*x>=19, x, relational=False)==sp.Interval(-sp.oo,-4)')),
    Q('Solve $x^2 + 2x - 15 = 0$', '$x = 3$ or $x = -5$', '$(x + 5)(x - 3) = 0$', c=('solve', 'x**2+2*x-15', '0', 'x', ['3', '-5'])),
    Q('Solve simultaneously: $y = 2x - 1$ and $x + y = 8$', '$x = 3$, $y = 5$', '$x + 2x - 1 = 8$', c=('py', 'sp.solve([y-2*x+1, x+y-8],[x,y])=={x:3,y:5}')),
    Q('$f(x) = x^2 - 3x$. Find $f(-2)$.', '$10$', '$4 + 6$', c=('eq', '(-2)**2-3*(-2)', '10')),
    Q('State the vertex and axis of symmetry of $y = (x - 2)^2 + 3$.', '$(2,\\ 3)$; $x = 2$', 'vertex form $y = (x - h)^2 + k$', c=('man', 'vertex form')),
    Q('$P(x) = x^3 - 2x^2 + 4$. Find $P(2)$.', '$4$', '$8 - 8 + 4$', c=('eq', '2**3-2*2**2+4', '4')),
    Q('Find the gradient and $y$-intercept of $4x - 2y + 6 = 0$.', '$m = 2$, $c = 3$', '$2y = 4x + 6$', c=('eq', 'sp.solve(4*x-2*y+6, y)[0]', '2*x+3')),
    Q('$A$ is $(-2,\\ 1)$ and $B$ is $(4,\\ 9)$. Find the midpoint and the length of $AB$.', '$(1,\\ 5)$; 10 units', '$\\sqrt{36 + 64}$', c=('py', '((-2+4)/2,(1+9)/2)==(1,5) and sqrt(6**2+8**2)==10')),
    Q('Find the exact value of $\\sin 60^\\circ \\times \\tan 30^\\circ$', '$\\frac{1}{2}$', '$\\frac{\\sqrt{3}}{2} \\times \\frac{1}{\\sqrt{3}}$', c=('eq', 'sin(rad(60))*tan(rad(30))', 'Rational(1,2)')),
    Q('Find $c$.', '$c = 7$', '$c^2 = 9 + 25 - 2(3)(5)\\cos 120^\\circ = 34 + 15$', d=D.oblique_triangle(5, 3, 120, '5', '3', 'c', '120°'), c=('eq', 'sqrt(3**2+5**2-2*3*5*cos(rad(120)))', '7')),
    Q('$ABCD$ is a cyclic quadrilateral with $\\angle A = 75^\\circ$. Find $\\angle C$.', '$105^\\circ$', 'opposite angles of a cyclic quadrilateral are supplementary', c=('eq', '180-75', '105')),
    Q('Two dice are rolled. Find $P(\\text{the sum is at least } 10)$.', '$\\frac{1}{6}$', '3 + 2 + 1 = 6 outcomes out of 36', c=('eq', 'Rational(len([1 for i in range(1,7) for j in range(1,7) if i+j>=10]),36)', 'Rational(1,6)')),
    Q('\\$5000 is invested at $4\\%$ p.a., compounded annually. Find its value after 2 years.', '\\$5408', '$5000 \\times 1.04^2 = 5000 \\times 1.0816$', c=('eq', '5000*Rational(104,100)**2', '5408')),
    Q('The product of two consecutive positive even numbers is 168. Find them.', '12 and 14', '$n(n + 2) = 168$', c=('py', '[n for n in range(2,40,2) if n*(n+2)==168]==[12]')),
])
BON.append(B('If $x + \\dfrac{1}{x} = 3$, find $x^2 + \\dfrac{1}{x^2}$.', '$7$', 'square both sides: $x^2 + 2 + \\frac{1}{x^2} = 9$', c=('py', 'all(sp.simplify(v**2+1/v**2-7)==0 for v in sp.solve(x+1/x-3, x))')))

# ---------------- Week 2 ----------------
W.append([
    Q('Simplify $(27x^6)^{\\frac{1}{3}}$', '$3x^2$', '$\\sqrt[3]{27} \\times x^{6 \\times \\frac{1}{3}}$', c=('py', 'sp.simplify((27*z**6)**Rational(1,3) - 3*z**2)==0', {'z': __import__('sympy').Symbol('z', positive=True)})),
    Q('Rationalise the denominator of $\\dfrac{10}{\\sqrt{5}}$', '$2\\sqrt{5}$', '$\\frac{10\\sqrt{5}}{5}$', c=('eq', '10/sqrt(5)', '2*sqrt(5)')),
    Q('Evaluate $\\log_{10} 0.001$', '$-3$', '$10^{-3} = 0.001$', c=('eq', 'log(Rational(1,1000),10)', '-3')),
    Q('Expand and simplify $(x + 1)(x^2 - x + 1)$', '$x^3 + 1$', '$x^3 - x^2 + x + x^2 - x + 1$', c=('eq', 'expand((x+1)*(x**2-x+1))', 'x**3+1')),
    Q('Factorise $2x^2 - 8$', '$2(x - 2)(x + 2)$', 'HCF 2, then difference of squares', c=('fac', '2*x**2-8', '2*(x-2)*(x+2)')),
    Q('Simplify $\\dfrac{x^2 - 4x}{x^2 - 16}$', '$\\frac{x}{x + 4}$', '$\\frac{x(x - 4)}{(x - 4)(x + 4)}$', c=('eq', 'sp.cancel((x**2-4*x)/(x**2-16))', 'x/(x+4)')),
    Q('Solve $\\dfrac{2x - 1}{5} < 3$', '$x < 8$', '$2x - 1 < 15$', c=('py', 'sp.solve_univariate_inequality((2*x-1)/5<3, x, relational=False)==sp.Interval.open(-sp.oo,8)')),
    Q('Solve $x^2 - 4x - 1 = 0$, giving exact answers.', '$x = 2 \\pm \\sqrt{5}$', '$\\frac{4 \\pm \\sqrt{16 + 4}}{2}$', c=('solve', 'x**2-4*x-1', '0', 'x', ['2+sqrt(5)', '2-sqrt(5)'])),
    Q('Solve simultaneously: $2x + 3y = 13$ and $5x - 3y = 1$', '$x = 2$, $y = 3$', 'add: $7x = 14$', c=('py', 'sp.solve([2*x+3*y-13, 5*x-3*y-1],[x,y])=={x:2,y:3}')),
    Q('State the domain of $f(x) = \\sqrt{x - 3}$.', '$x \\ge 3$', 'need $x - 3 \\ge 0$', c=('man', 'square root needs non-negative')),
    Q('Find the $x$- and $y$-intercepts of $y = x^2 - x - 6$.', '$x = 3$, $x = -2$; $y = -6$', '$(x - 3)(x + 2) = 0$', c=('solve', 'x**2-x-6', '0', 'x', ['3', '-2'])),
    Q('Find the remainder when $P(x) = x^3 + 2x - 5$ is divided by $(x - 1)$.', '$-2$', 'remainder theorem: $P(1) = 1 + 2 - 5$', c=('eq', 'sp.rem(x**3+2*x-5, x-1, x)', '-2')),
    Q('Find the equation of the line through $(3,\\ -1)$ with gradient $-2$.', '$y = -2x + 5$', '$y + 1 = -2(x - 3)$', c=('py', '-2*3+5==-1')),
    Q('Find the centre and radius of $(x - 1)^2 + (y + 2)^2 = 16$.', 'centre $(1,\\ -2)$, radius 4', 'compare with $(x - a)^2 + (y - b)^2 = r^2$', c=('man', 'read off circle form')),
    Q('Solve $\\sin\\theta = \\dfrac{\\sqrt{3}}{2}$ for $0^\\circ \\le \\theta \\le 180^\\circ$.', '$\\theta = 60^\\circ$ or $120^\\circ$', '$\\sin(180^\\circ - 60^\\circ) = \\sin 60^\\circ$', c=('py', 'sin(rad(60))==sqrt(3)/2 and sin(rad(120))==sqrt(3)/2')),
    Q('In $\\triangle ABC$, $a = 6$, $A = 45^\\circ$ and $B = 30^\\circ$. Find $b$ exactly.', '$b = 3\\sqrt{2}$', '$b = \\frac{6\\sin 30^\\circ}{\\sin 45^\\circ} = \\frac{3}{\\frac{\\sqrt{2}}{2}}$', c=('eq', '6*sin(rad(30))/sin(rad(45))', '3*sqrt(2)')),
    Q('Two similar solids have matching lengths in the ratio $2 : 3$. The smaller has volume 40 cm³. Find the volume of the larger.', '135 cm³', 'volumes in the ratio $8 : 27$', c=('eq', '40*Rational(27,8)', '135')),
    Q('A bag has 3 red and 2 white balls. Two are drawn without replacement. Find $P(\\text{same colour})$.', '$\\frac{2}{5}$', '$\\frac{3}{5} \\cdot \\frac{2}{4} + \\frac{2}{5} \\cdot \\frac{1}{4} = \\frac{8}{20}$', c=('eq', 'Rational(3,5)*Rational(2,4)+Rational(2,5)*Rational(1,4)', 'Rational(2,5)')),
    Q('A \\$30 000 car depreciates by $15\\%$ p.a. Find its value after 2 years.', '\\$21 675', '$30\\,000 \\times 0.85^2 = 30\\,000 \\times 0.7225$', c=('eq', '30000*Rational(85,100)**2', '21675')),
    Q('A rectangle has a perimeter of 26 cm and an area of 40 cm². Find its dimensions.', '8 cm by 5 cm', '$x(13 - x) = 40$, $(x - 5)(x - 8) = 0$', c=('solve', 'x*(13-x)', '40', 'x', ['5', '8'])),
])
BON.append(B('Show that $\\dfrac{\\sqrt{5} + \\sqrt{3}}{\\sqrt{5} - \\sqrt{3}} = 4 + \\sqrt{15}$.', 'multiply by $\\frac{\\sqrt{5} + \\sqrt{3}}{\\sqrt{5} + \\sqrt{3}}$', '$\\frac{5 + 2\\sqrt{15} + 3}{5 - 3} = \\frac{8 + 2\\sqrt{15}}{2}$', c=('eq', 'sp.radsimp((sqrt(5)+sqrt(3))/(sqrt(5)-sqrt(3)))', '4+sqrt(15)')))

# ---------------- Week 3 ----------------
W.append([
    Q('Solve $9^x = 27$', '$x = \\frac{3}{2}$', '$3^{2x} = 3^3$', c=('py', '9**Rational(3,2)==27 and [v for v in sp.solve(9**x-27, x) if v.is_real]==[Rational(3,2)]')),
    Q('Expand and simplify $(2\\sqrt{3} - 1)^2$', '$13 - 4\\sqrt{3}$', '$12 - 4\\sqrt{3} + 1$', c=('eq', 'expand((2*sqrt(3)-1)**2)', '13-4*sqrt(3)')),
    Q('Simplify $\\log_6 4 + \\log_6 9$', '$2$', '$\\log_6 36$', c=('eq', 'sp.simplify(log(4,6)+log(9,6))', '2')),
    Q('Expand and simplify $(x - 2)(x + 2)(x^2 + 4)$', '$x^4 - 16$', '$(x^2 - 4)(x^2 + 4)$', c=('eq', 'expand((x-2)*(x+2)*(x**2+4))', 'x**4-16')),
    Q('Factorise $3x^2 + 10x - 8$', '$(3x - 2)(x + 4)$', 'check: $3x^2 + 12x - 2x - 8$', c=('fac', '3*x**2+10*x-8', '(3*x-2)*(x+4)')),
    Q('Simplify $\\dfrac{2}{x - 1} - \\dfrac{1}{x + 1}$', '$\\frac{x + 3}{x^2 - 1}$', '$\\frac{2(x + 1) - (x - 1)}{(x - 1)(x + 1)}$', c=('eq', '2/(x-1)-1/(x+1)', '(x+3)/(x**2-1)')),
    Q('Solve $\\dfrac{x}{3} - \\dfrac{x - 2}{4} = 1$', '$x = 6$', '$4x - 3(x - 2) = 12$', c=('solve', 'x/3-(x-2)/4', '1', 'x', ['6'])),
    Q('Solve $3x^2 - 5x - 2 = 0$', '$x = 2$ or $x = -\\frac{1}{3}$', '$(3x + 1)(x - 2) = 0$', c=('solve', '3*x**2-5*x-2', '0', 'x', ['2', '-Rational(1,3)'])),
    Q('Find where $y = x^2$ and $y = x + 2$ meet.', '$(2,\\ 4)$ and $(-1,\\ 1)$', '$x^2 - x - 2 = 0$', c=('solve', 'x**2', 'x+2', 'x', ['2', '-1'])),
    Q('$f(x) = 2x + 1$ and $g(x) = x^2$. Find $f(g(3))$.', '$19$', '$g(3) = 9$; $f(9) = 19$', s=True, c=('eq', '2*3**2+1', '19')),
    Q('State the equations of the asymptotes of $y = \\dfrac{2}{x} + 1$.', '$x = 0$ and $y = 1$', '$y = \\frac{2}{x}$ moved up 1', c=('man', 'hyperbola asymptotes')),
    Q('Show that $(x + 2)$ is a factor of $x^3 + x^2 - 4x - 4$, then factorise fully.', '$(x + 1)(x - 2)(x + 2)$', '$P(-2) = -8 + 4 + 8 - 4 = 0$', c=('py', 'sp.factor(x**3+x**2-4*x-4)==(x+1)*(x-2)*(x+2)')),
    Q('Find the equation of the line through $(0,\\ 4)$ perpendicular to $3x - y + 2 = 0$.', '$y = -\\frac{1}{3}x + 4$', 'that line has $m = 3$', c=('eq', '-1/Rational(3)', '-Rational(1,3)')),
    Q('Show that $A(1,\\ 1)$, $B(4,\\ 5)$ and $C(8,\\ 2)$ form a right-angled triangle.', '$m_{AB} \\times m_{BC} = -1$', '$\\frac{4}{3} \\times (-\\frac{3}{4}) = -1$: right angle at $B$', c=('eq', 'Rational(5-1,4-1)*Rational(2-5,8-4)', '-1')),
    Q('Convert $135^\\circ$ to radians, as an exact value.', '$\\frac{3\\pi}{4}$', '$135 \\times \\frac{\\pi}{180}$', s=True, c=('eq', 'rad(135)', '3*pi/4')),
    Q('Find the area of a triangle with sides 8 cm and 10 cm and an included angle of $30^\\circ$.', '20 cm²', '$\\frac{1}{2} \\times 8 \\times 10 \\times \\sin 30^\\circ$', c=('eq', 'Rational(1,2)*8*10*sin(rad(30))', '20')),
    Q('Chords $AB$ and $CD$ cross at $P$. $AP = 4$, $PB = 6$ and $CP = 3$. Find $PD$.', '$8$', '$AP \\times PB = CP \\times PD$', c=('solve', '3*d', '4*6', 'd', ['8'])),
    Q('$P(A) = 0.5$, $P(B) = 0.4$ and $P(A \\cap B) = 0.2$. Find $P(A \\cup B)$ and $P(A \\mid B)$.', '$0.7$; $0.5$', '$0.5 + 0.4 - 0.2$; $\\frac{0.2}{0.4}$', c=('py', 'Rational(5,10)+Rational(4,10)-Rational(2,10)==Rational(7,10) and Rational(2,10)/Rational(4,10)==Rational(1,2)')),
    Q('\\$10 000 is invested at $6\\%$ p.a., compounded monthly. Write an expression for its value after 3 years.', '$10\\,000 \\times 1.005^{36}$', '$0.5\\%$ per month for 36 months', c=('py', 'Rational(6,100)/12==Rational(5,1000) and 3*12==36')),
    Q('A ball’s height is $h = 20t - 5t^2$ metres after $t$ seconds. When does it land, and what is its greatest height?', '$t = 4$ s; 20 m', '$5t(4 - t) = 0$; max halfway, at $t = 2$', c=('py', 'sp.solve(20*t-5*t**2, t)==[0,4] and (20*2-5*4)==20')),
])
BON.append(B('Solve $2^{2x} - 6 \\times 2^x + 8 = 0$', '$x = 1$ or $x = 2$', 'let $u = 2^x$: $u^2 - 6u + 8 = 0$, $u = 2$ or $4$', c=('py', 'sorted(sp.solve(2**(2*x)-6*2**x+8, x))==[1,2]')))

# ---------------- Week 4 ----------------
W.append([
    Q('Simplify $(a^{\\frac{1}{2}}b^{-1})^2 \\times ab^3$', '$a^2b$', '$ab^{-2} \\times ab^3$', c=('py', 'sp.simplify((A**Rational(1,2)*b**-1)**2*A*b**3 - A**2*b)==0', {'A': __import__('sympy').Symbol('A', positive=True)})),
    Q('Rationalise the denominator of $\\dfrac{4}{\\sqrt{7} - \\sqrt{3}}$', '$\\sqrt{7} + \\sqrt{3}$', '$\\frac{4(\\sqrt{7} + \\sqrt{3})}{7 - 3}$', c=('eq', 'sp.radsimp(4/(sqrt(7)-sqrt(3)))', 'sqrt(7)+sqrt(3)')),
    Q('Solve $\\log_2 x = 5$', '$x = 32$', '$x = 2^5$', c=('eq', '2**5', '32')),
    Q('Expand $(x + 2)^3$', '$x^3 + 6x^2 + 12x + 8$', '$(x^2 + 4x + 4)(x + 2)$', c=('eq', 'expand((x+2)**3)', 'x**3+6*x**2+12*x+8')),
    Q('Factorise $x^3 - 9x$', '$x(x - 3)(x + 3)$', 'HCF $x$, then difference of squares', c=('fac', 'x**3-9*x', 'x*(x-3)*(x+3)')),
    Q('Simplify $\\dfrac{x^2 - 9}{2x + 6} \\times \\dfrac{4}{x - 3}$', '$2$', '$\\frac{(x - 3)(x + 3)}{2(x + 3)} \\times \\frac{4}{x - 3}$', c=('eq', 'sp.cancel((x**2-9)/(2*x+6)*4/(x-3))', '2')),
    Q('Solve $-3 < 2x + 1 \\le 7$', '$-2 < x \\le 3$', 'subtract 1, then divide by 2', c=('py', 'sp.solve_univariate_inequality(-3<2*x+1, x, relational=False).intersect(sp.solve_univariate_inequality(2*x+1<=7, x, relational=False))==sp.Interval.Lopen(-2,3)')),
    Q('Find the discriminant of $2x^2 - 3x + 5 = 0$. How many real roots are there?', '$\\Delta = -31$; none', '$9 - 40$', c=('eq', '(-3)**2-4*2*5', '-31')),
    Q('Solve simultaneously: $x + y = 7$ and $xy = 12$', '$(3,\\ 4)$ or $(4,\\ 3)$', '$x(7 - x) = 12$, $x^2 - 7x + 12 = 0$', c=('py', 'sorted(sp.solve([x+y-7, x*y-12],[x,y]))==[(3,4),(4,3)]')),
    Q('Is the relation $y^2 = x$ a function? Explain.', 'No', '$x = 4$ gives $y = 2$ and $y = -2$', c=('man', 'fails vertical line test')),
    Q('Describe how to get the graph of $y = (x - 3)^2 - 1$ from $y = x^2$.', '3 right, 1 down', 'vertex moves from $(0, 0)$ to $(3, -1)$', c=('man', 'translation')),
    Q('$P(x) = x^3 - 6x^2 + 11x - 6$ and $P(1) = 0$. Factorise $P(x)$ fully and solve $P(x) = 0$.', '$(x - 1)(x - 2)(x - 3)$; $x = 1, 2, 3$', 'divide by $(x - 1)$: $x^2 - 5x + 6$', c=('py', 'sp.factor(x**3-6*x**2+11*x-6)==(x-1)*(x-2)*(x-3)')),
    Q('Find where $2x + 5y = 20$ cuts the axes, and the area of the triangle it makes with the axes.', '$(10,\\ 0)$, $(0,\\ 4)$; 20 units²', '$\\frac{1}{2} \\times 10 \\times 4$', c=('eq', 'Rational(1,2)*10*4', '20')),
    Q('Write the equation of the circle with centre $(2,\\ -3)$ and radius 5.', '$(x - 2)^2 + (y + 3)^2 = 25$', '$(x - a)^2 + (y - b)^2 = r^2$', c=('man', 'circle form')),
    Q('Find the exact value of $\\cos 150^\\circ$', '$-\\frac{\\sqrt{3}}{2}$', '$\\cos 150^\\circ = -\\cos 30^\\circ$', c=('eq', 'cos(rad(150))', '-sqrt(3)/2')),
    Q('Find the largest angle of a triangle with sides 3, 5 and 7.', '$120^\\circ$', '$\\cos C = \\frac{9 + 25 - 49}{30} = -\\frac{1}{2}$', c=('eq', 'Rational(9+25-49,30)', 'cos(rad(120))')),
    Q('Find the sum of the interior angles of a decagon.', '$1440^\\circ$', '$(10 - 2) \\times 180^\\circ$', c=('eq', '(10-2)*180', '1440')),
    Q('Two cards are drawn without replacement from ten cards numbered 1 to 10. Find $P(\\text{both even})$.', '$\\frac{2}{9}$', '$\\frac{5}{10} \\times \\frac{4}{9}$', c=('eq', 'Rational(5,10)*Rational(4,9)', 'Rational(2,9)')),
    Q('Which earns more on \\$1000 over 3 years: $12\\%$ p.a. simple interest or $10\\%$ p.a. compound interest?', '12% simple (\\$360 vs \\$331)', '$1000 \\times 1.1^3 = 1331$', c=('py', '1000*Rational(12,100)*3 > 1000*Rational(11,10)**3-1000')),
    Q('The sum of the first $n$ positive integers is $\\frac{n(n + 1)}{2}$. How many must be added to make 210?', '20', '$n(n + 1) = 420 = 20 \\times 21$', c=('solve', 'n*(n+1)/2', '210', 'n', ['20', '-21'])),
])
BON.append(B('Find $k$ if $x^2 + kx + 9 = 0$ has exactly one real solution.', '$k = 6$ or $k = -6$', '$\\Delta = k^2 - 36 = 0$', c=('solve', 'k**2-36', '0', 'k', ['6', '-6'])))

# ---------------- Week 5 ----------------
W.append([
    Q('Write $\\dfrac{\\sqrt{x}}{x^2}$ as a single power of $x$.', '$x^{-\\frac{3}{2}}$', '$x^{\\frac{1}{2} - 2}$', c=('eq', 'Rational(1,2)-2', '-Rational(3,2)')),
    Q('Find $a$ and $b$ if $(3 + \\sqrt{2})^2 = a + b\\sqrt{2}$.', '$a = 11$, $b = 6$', '$9 + 6\\sqrt{2} + 2$', c=('eq', 'expand((3+sqrt(2))**2)', '11+6*sqrt(2)')),
    Q('Simplify $2\\log_{10} 5 + \\log_{10} 4$', '$2$', '$\\log_{10} 25 + \\log_{10} 4 = \\log_{10} 100$', c=('eq', 'sp.simplify(2*log(5,10)+log(4,10))', '2')),
    Q('Expand $\\left(x + \\dfrac{1}{x}\\right)^2$', '$x^2 + 2 + \\frac{1}{x^2}$', 'the middle term is $2 \\times x \\times \\frac{1}{x}$', c=('eq', 'expand((x+1/x)**2)', 'x**2+2+1/x**2')),
    Q('Factorise $x^3 - 8$', '$(x - 2)(x^2 + 2x + 4)$', '$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$', s=True, c=('fac', 'x**3-8', '(x-2)*(x**2+2*x+4)')),
    Q('Simplify $\\dfrac{1 - \\frac{1}{x}}{1 - \\frac{1}{x^2}}$', '$\\frac{x}{x + 1}$', 'multiply top and bottom by $x^2$: $\\frac{x(x - 1)}{(x - 1)(x + 1)}$', c=('eq', 'sp.cancel((1-1/x)/(1-1/x**2))', 'x/(x+1)')),
    Q('Solve $3(x - 2) - 4(1 - x) > 4$', '$x > 2$', '$7x - 10 > 4$', c=('py', 'sp.solve_univariate_inequality(3*(x-2)-4*(1-x)>4, x, relational=False)==sp.Interval.open(2,sp.oo)')),
    Q('Solve $(x - 3)^2 = 7$', '$x = 3 \\pm \\sqrt{7}$', '$x - 3 = \\pm\\sqrt{7}$', c=('solve', '(x-3)**2', '7', 'x', ['3+sqrt(7)', '3-sqrt(7)'])),
    Q('Find where the circle $x^2 + y^2 = 25$ meets the line $y = x + 1$.', '$(3,\\ 4)$ and $(-4,\\ -3)$', '$2x^2 + 2x - 24 = 0$', c=('py', 'sorted(sp.solve([x**2+y**2-25, y-x-1],[x,y]))==[(-4,-3),(3,4)]')),
    Q('$f(x) = 3x - 2$. Find $f(a + 1) - f(a)$.', '$3$', '$3a + 1 - (3a - 2)$', c=('eq', '(3*(a+1)-2)-(3*a-2)', '3')),
    Q('Find the vertex of $y = x^2 - 6x + 5$ by completing the square.', '$(3,\\ -4)$', '$y = (x - 3)^2 - 4$', c=('eq', 'expand((x-3)**2-4)', 'x**2-6*x+5')),
    Q('Divide $x^3 - 4x^2 + x + 6$ by $(x - 2)$. State the quotient and remainder.', '$x^2 - 2x - 3$, remainder 0', 'check: $(x - 2)(x^2 - 2x - 3) = x^3 - 4x^2 + x + 6$', c=('py', 'sp.div(x**3-4*x**2+x+6, x-2, x)==(x**2-2*x-3, 0)')),
    Q('Find the angle the line $y = \\sqrt{3}x + 1$ makes with the positive $x$-axis.', '$60^\\circ$', '$\\tan\\theta = \\sqrt{3}$', c=('eq', 'tan(rad(60))', 'sqrt(3)')),
    Q('Find the centre and radius of $x^2 + y^2 - 6x + 4y - 12 = 0$.', 'centre $(3,\\ -2)$, radius 5', '$(x - 3)^2 + (y + 2)^2 = 12 + 9 + 4$', c=('eq', 'expand((x-3)**2+(y+2)**2-25)', 'x**2+y**2-6*x+4*y-12')),
    Q('$\\theta$ is acute and $\\sin\\theta = \\frac{3}{5}$. Use $\\sin^2\\theta + \\cos^2\\theta = 1$ to find $\\cos\\theta$.', '$\\frac{4}{5}$', '$\\cos^2\\theta = 1 - \\frac{9}{25} = \\frac{16}{25}$', s=True, c=('eq', 'sqrt(1-Rational(9,25))', 'Rational(4,5)')),
    Q('How many triangles have $a = 6$, $b = 10$ and $A = 30^\\circ$? Explain.', 'two', '$\\sin B = \\frac{10 \\times 0.5}{6} = \\frac{5}{6} < 1$, and $B$ can be acute or obtuse', c=('py', 'Rational(10,6)*sin(rad(30))==Rational(5,6) and 30+(180-sp.deg(sp.asin(Rational(5,6))).evalf())<180')),
    Q('$PA$ and $PB$ are tangents from $P$ to a circle with centre $O$. If $\\angle APB = 50^\\circ$, find $\\angle AOB$.', '$130^\\circ$', 'tangents ⊥ radii: $360 - 90 - 90 - 50$', c=('eq', '360-90-90-50', '130')),
    Q('In a class of 28, 15 study French, 12 study Japanese and 5 study both. A Japanese student is chosen at random. Find $P(\\text{also studies French})$.', '$\\frac{5}{12}$', 'conditional: 5 of the 12 Japanese students', c=('eq', 'Rational(5,12)', 'Rational(5,12)')),
    Q('An investment grows to \\$4840 after 2 years at $10\\%$ p.a., compounded annually. Find the amount invested.', '\\$4000', '$P = 4840 \\div 1.21$', c=('eq', '4840/Rational(121,100)', '4000')),
    Q('For $y = x^2$, find the gradient of the line through $(2,\\ 4)$ and $(2 + h,\\ (2 + h)^2)$. What happens as $h \\to 0$?', '$4 + h$; it approaches 4', '$\\frac{(2 + h)^2 - 4}{h} = \\frac{4h + h^2}{h}$', s=True, c=('eq', 'sp.cancel(((2+h)**2-4)/h)', '4+h')),
])
BON.append(B('Solve $x - 5\\sqrt{x} + 6 = 0$', '$x = 4$ or $x = 9$', 'let $u = \\sqrt{x}$: $u^2 - 5u + 6 = 0$, $u = 2$ or 3', c=('py', 'all(v - 5*sqrt(v) + 6 == 0 for v in (4, 9))')))

# ---------------- Week 6 ----------------
W.append([
    Q('Solve $4^{x + 1} = 8^x$', '$x = 2$', '$2^{2x + 2} = 2^{3x}$', c=('solve', '2*x+2', '3*x', 'x', ['2'])),
    Q('Simplify $\\dfrac{(\\sqrt{6} + \\sqrt{2})(\\sqrt{6} - \\sqrt{2})}{\\sqrt{2}}$', '$2\\sqrt{2}$', '$\\frac{6 - 2}{\\sqrt{2}} = \\frac{4}{\\sqrt{2}}$', c=('eq', '(sqrt(6)+sqrt(2))*(sqrt(6)-sqrt(2))/sqrt(2)', '2*sqrt(2)')),
    Q('Solve $2^x = 7$, giving an exact answer.', '$x = \\log_2 7$', 'definition of a logarithm', c=('eq', '2**log(7,2)', '7')),
    Q('Expand $(2x - 1)^3$', '$8x^3 - 12x^2 + 6x - 1$', '$(4x^2 - 4x + 1)(2x - 1)$', c=('eq', 'expand((2*x-1)**3)', '8*x**3-12*x**2+6*x-1')),
    Q('Factorise $2x^3 + 3x^2 - 8x - 12$', '$(2x + 3)(x - 2)(x + 2)$', '$x^2(2x + 3) - 4(2x + 3)$', c=('fac', '2*x**3+3*x**2-8*x-12', '(2*x+3)*(x-2)*(x+2)')),
    Q('Solve $\\dfrac{3}{x - 2} = \\dfrac{2}{x + 1}$', '$x = -7$', '$3(x + 1) = 2(x - 2)$', c=('solve', '3/(x-2)', '2/(x+1)', 'x', ['-7'])),
    Q('For which values of $x$ is $5 - 2x$ positive?', '$x < \\frac{5}{2}$', '$5 - 2x > 0$', c=('py', 'sp.solve_univariate_inequality(5-2*x>0, x, relational=False)==sp.Interval.open(-sp.oo,Rational(5,2))')),
    Q('For which values of $k$ does $x^2 - 4x + k = 0$ have two distinct real roots?', '$k < 4$', '$\\Delta = 16 - 4k > 0$', c=('py', 'sp.solve_univariate_inequality(16-4*k>0, k, relational=False)==sp.Interval.open(-sp.oo,4)')),
    Q('The line $y = 2x + c$ touches the parabola $y = x^2$ at exactly one point. Find $c$.', '$c = -1$', '$x^2 - 2x - c = 0$; $\\Delta = 4 + 4c = 0$', c=('solve', '4+4*c', '0', 'c', ['-1'])),
    Q('Is $f(x) = x^3 - x$ odd, even or neither? Show why.', 'odd', '$f(-x) = -x^3 + x = -f(x)$', s=True, c=('eq', '((-x)**3-(-x))', '-(x**3-x)')),
    Q('For $y = 2^x - 4$, find the $y$-intercept, the $x$-intercept and the asymptote.', '$y = -3$; $x = 2$; $y = -4$', '$2^0 - 4 = -3$; $2^x = 4$', c=('py', '2**0-4==-3 and 2**2-4==0')),
    Q('$P(x) = x^3 + ax + 2$ leaves a remainder of 5 when divided by $(x - 1)$. Find $a$.', '$a = 2$', '$P(1) = 1 + a + 2 = 5$', c=('solve', '1+a+2', '5', 'a', ['2'])),
    Q('Find the point of intersection of $3x - 2y = 4$ and $x + 4y = 6$.', '$(2,\\ 1)$', '$x = 6 - 4y$: $18 - 14y = 4$', c=('py', 'sp.solve([3*x-2*y-4, x+4*y-6],[x,y])=={x:2,y:1}')),
    Q('Find the equation of the tangent to the circle $x^2 + y^2 = 25$ at $(3,\\ 4)$.', '$3x + 4y = 25$', 'radius gradient $\\frac{4}{3}$, so tangent gradient $-\\frac{3}{4}$', c=('py', '3*3+4*4==25 and Rational(4,3)*Rational(-3,4)==-1')),
    Q('Solve $2\\cos\\theta + 1 = 0$ for $0^\\circ \\le \\theta \\le 360^\\circ$.', '$\\theta = 120^\\circ$ or $240^\\circ$', '$\\cos\\theta = -\\frac{1}{2}$: 2nd and 3rd quadrants', s=True, c=('py', 'cos(rad(120))==-Rational(1,2) and cos(rad(240))==-Rational(1,2)')),
    Q('A ship sails 5 km on a bearing of $060^\\circ$T, then 8 km on a bearing of $180^\\circ$T. How far is it from its start?', '7 km', 'angle between the legs is $60^\\circ$: $c^2 = 25 + 64 - 40$', c=('eq', 'sqrt(5**2+8**2-2*5*8*cos(rad(60)))', '7')),
    Q('Prove that the angle in a semicircle is a right angle.', 'it is half the angle at the centre', 'the angle at the centre is a straight angle, $180^\\circ$; half of it is $90^\\circ$', c=('man', 'circle theorem proof')),
    Q('$A$ and $B$ are independent, with $P(A) = 0.3$ and $P(B) = 0.4$. Find $P(A \\cup B)$.', '$0.58$', '$0.3 + 0.4 - 0.3 \\times 0.4$', c=('eq', 'Rational(3,10)+Rational(4,10)-Rational(3,10)*Rational(4,10)', 'Rational(58,100)')),
    Q('An account pays $4.8\\%$ p.a., compounded monthly. Find the monthly interest rate and the number of compounding periods in 5 years.', '$0.4\\%$; 60', '$4.8 \\div 12$; $5 \\times 12$', c=('py', 'Rational(48,10)/12==Rational(4,10) and 5*12==60')),
    Q('The tangent to $y = x^2$ at $x = a$ has gradient $2a$. Find the point where the tangent is parallel to $y = 6x - 1$.', '$(3,\\ 9)$', '$2a = 6$', s=True, c=('solve', '2*a', '6', 'a', ['3'])),
])
BON.append(B('Solve $\\log_2 x + \\log_2(x - 2) = 3$', '$x = 4$', '$x(x - 2) = 8$, so $x = 4$ or $-2$; reject $-2$', c=('solve', 'x*(x-2)', '8', 'x', ['4', '-2'])))

BK['weeks'] = W
BK['bonus'] = BON

BK['hints'] = [
    ('Indices, surds & logs', ['$a^{-n} = \\frac{1}{a^n}$ · $a^{\\frac{m}{n}} = (\\sqrt[n]{a})^m$',
                               '$\\frac{a}{\\sqrt{b}} = \\frac{a\\sqrt{b}}{b}$; use the conjugate for $\\sqrt{a} - \\sqrt{b}$',
                               '$\\log_a x = n \\Leftrightarrow a^n = x$',
                               '$\\log_a xy = \\log_a x + \\log_a y$ · $\\log_a x^n = n\\log_a x$']),
    ('Algebra', ['$(a \\pm b)^2 = a^2 \\pm 2ab + b^2$ · $(a + b)(a - b) = a^2 - b^2$',
                 'Factorise: HCF, DOTS, trinomial, grouping',
                 '<span class="star">★</span> $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$',
                 'Algebraic fractions: factorise first, then cancel factors']),
    ('Equations', ['$x = \\dfrac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$ · $\\Delta = b^2 - 4ac$',
                   '$\\Delta > 0$: two roots · $\\Delta = 0$: one · $\\Delta < 0$: none',
                   'Inequalities: ×/÷ by a negative reverses the sign',
                   'Simultaneous: substitute or eliminate; a line and a curve can meet twice']),
    ('Functions & graphs', ['$f(a)$: replace $x$ with $a$ · domain: the $x$-values allowed',
                            'Vertical line test: one $y$ for each $x$',
                            '$y = (x - h)^2 + k$: vertex $(h, k)$ · $y = \\frac{k}{x}$: asymptotes $x = 0$, $y = 0$',
                            'Remainder theorem: remainder $= P(a)$ when dividing by $(x - a)$',
                            '<span class="star">★</span> Odd: $f(-x) = -f(x)$ · even: $f(-x) = f(x)$']),
    ('Coordinate geometry', ['$y - y_1 = m(x - x_1)$ · perpendicular: $m_1m_2 = -1$',
                             '$m = \\tan\\theta$ · general form $ax + by + c = 0$',
                             'Circle: $(x - a)^2 + (y - b)^2 = r^2$; complete the square to find the centre']),
    ('Trigonometry', ['$\\sin 30^\\circ = \\frac{1}{2}$, $\\cos 30^\\circ = \\frac{\\sqrt{3}}{2}$, $\\tan 45^\\circ = 1$',
                      '$\\sin(180^\\circ - \\theta) = \\sin\\theta$ · $\\cos(180^\\circ - \\theta) = -\\cos\\theta$',
                      '$\\frac{a}{\\sin A} = \\frac{b}{\\sin B}$ · $c^2 = a^2 + b^2 - 2ab\\cos C$ · $A = \\frac{1}{2}ab\\sin C$',
                      '<span class="star">★</span> $180^\\circ = \\pi$ radians · $\\sin^2\\theta + \\cos^2\\theta = 1$']),
    ('Geometry & chance', ['Cyclic quadrilateral: opposite angles add to $180^\\circ$',
                           'Tangent ⊥ radius · intersecting chords: $AP \\cdot PB = CP \\cdot PD$',
                           '$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$',
                           '$P(A \\mid B) = \\dfrac{P(A \\cap B)}{P(B)}$']),
    ('In context', ['$A = P(1 + r)^n$, with $r$ and $n$ per compounding period',
                    'Depreciation $S = V_0(1 - r)^n$',
                    '<span class="star">★</span> Gradient of a secant $= \\dfrac{f(x + h) - f(x)}{h}$; let $h \\to 0$ for the tangent']),
]
