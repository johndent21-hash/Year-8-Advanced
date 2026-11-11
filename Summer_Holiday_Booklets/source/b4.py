"""Year 9 Advanced -> Year 10 Advanced (Stage 5 core + Adv path revision)."""
import math
from qlib import Q, B, xy, stemleaf
import diagrams as D

BK = dict(
    key='b4',
    file='Yr9_Advanced_Summer_Holiday_Ready_for_Yr10_Advanced_Revision_Booklet',
    kicker='YEAR 9 ADVANCED → YEAR 10 ADVANCED',
    ready='Ready for Year 10',
    intro='Six weeks. Twenty questions a week. Every Year 9 skill that Year 10 Advanced builds on – mixed together so it sticks.',
    star_text='Year 10 preview (Stage 5 path)',
    pattern='Question 1 is always number and percentages, question 11 is always Pythagoras, and so on. If the same number keeps going wrong, that is the skill to revise before Year 10.',
    groups=[('Number', '', [1, 2]), ('Indices & surds', '', [3, 4]), ('Algebra', '', [5, 6, 7]),
            ('Equations', '', [8, 9, 10]), ('Measurement & trig', '', [11, 12, 13]), ('Coordinate geometry', '', [14, 15, 16]),
            ('Geometry & chance', '', [17, 18]), ('In context', '', [19, 20])],
    strands={1: 'Number & percentages', 2: 'Scientific notation', 3: 'Indices', 4: 'Surds',
             5: 'Algebraic fractions', 6: 'Expand', 7: 'Factorise', 8: 'Linear equations', 9: 'Quadratic equations',
             10: 'Formulas & inequalities', 11: 'Pythagoras', 12: 'Trigonometry', 13: 'Surface area & volume',
             14: 'Distance & midpoint', 15: 'Gradient', 16: 'Equation of a line', 17: 'Geometry', 18: 'Probability',
             19: 'Financial maths', 20: 'Problem solving'},
    rules=['<b>No calculator.</b> Leave answers exact (e.g. $3\\sqrt{5}$ or $96\\pi$) unless asked to round. Trig questions give you any value you need.',
           '<b>Show working</b> in the space under each question.',
           '<b>Mark it yourself</b> using the answers at the back (pages 10–12). Each answer has a line of working to help you find a mistake.',
           '<b>Fix it.</b> Redo anything you got wrong a day or two later, without looking.',
           '<span class="star">★</span> questions preview Year 10 Advanced work. Have a go – they are the ones that will help most in Term 1.',
           '<b>Stuck?</b> The hints page (page 9) has the key facts and formulas.'],
    first_up='<b>First up in Year 10 Advanced:</b> interest and depreciation, graphing lines, surface area and volume, products, factors and surds, and equations, inequalities and logarithms. Every one of them starts from the skills in these six pages.',
    outcomes='Revises MA5-ALG-C-01, MA5-ALG-P-01, MA5-ALG-P-02, MA5-IND-C-01, MA5-IND-P-01, MA5-IND-P-02, MA5-MAG-C-01, MA5-EQU-C-01, MA5-EQU-P-01, MA5-EQU-P-02, MA5-LIN-C-01, MA5-LIN-C-02, MA5-TRG-C-01, MA5-TRG-C-02, MA5-ARE-C-01, MA5-VOL-C-01, MA5-GEO-C-01, MA5-GEO-P-01, MA5-PRO-C-01, MA5-PRO-P-01, MA5-FIN-C-01, with MA4-PYT-C-01. <span class="star">★</span> Year 10 preview: MA5-FIN-C-02, MA5-LIN-P-01, MA5-TRG-P-01, MA5-TRG-P-02, MA5-VOL-P-01, MA5-POL-P-01, MA5-LOG-P-01, MA5-CIR-P-01.',
)

W, BON = [], []
s60 = math.sin(math.radians(60))

# ---------------- Week 1 ----------------
W.append([
    Q('Decrease \\$360 by $15\\%$.', '\\$306', '$360 \\times 0.85$', c=('eq', '360*Rational(85,100)', '306')),
    Q('Write $0.000\\,058$ in scientific notation.', '$5.8 \\times 10^{-5}$', 'move the decimal point 5 places right', c=('eq', 'Rational(58,10)*Rational(1,10**5)', 'Rational(58,1000000)')),
    Q('Simplify $(3x^2y)^3$', '$27x^6y^3$', 'cube each factor', c=('eq', '(3*x**2*y)**3', '27*x**6*y**3')),
    Q('Simplify $\\sqrt{48}$', '$4\\sqrt{3}$', '$\\sqrt{16 \\times 3}$', c=('eq', 'sqrt(48)', '4*sqrt(3)')),
    Q('Simplify $\\dfrac{x}{3} + \\dfrac{x}{4}$', '$\\frac{7x}{12}$', '$\\frac{4x}{12} + \\frac{3x}{12}$', c=('eq', 'x/3+x/4', '7*x/12')),
    Q('Expand $(x + 7)(x - 3)$', '$x^2 + 4x - 21$', '$x^2 - 3x + 7x - 21$', c=('eq', 'expand((x+7)*(x-3))', 'x**2+4*x-21')),
    Q('Factorise $x^2 + 9x + 20$', '$(x + 4)(x + 5)$', '$4 \\times 5 = 20$, $4 + 5 = 9$', c=('fac', 'x**2+9*x+20', '(x+4)*(x+5)')),
    Q('Solve $\\dfrac{x + 3}{4} = x - 3$', '$x = 5$', '$x + 3 = 4x - 12$, $3x = 15$', c=('solve', '(x+3)/4', 'x-3', 'x', ['5'])),
    Q('Solve $x^2 - 7x + 10 = 0$', '$x = 2$ or $x = 5$', '$(x - 2)(x - 5) = 0$', c=('solve', 'x**2-7*x+10', '0', 'x', ['2', '5'])),
    Q('Make $h$ the subject of $V = \\pi r^2 h$.', '$h = \\dfrac{V}{\\pi r^2}$', 'divide both sides by $\\pi r^2$', c=('solve', 'pi*r**2*h', 'P', 'h', ['P/(pi*r**2)'])),
    Q('Find $x$ as an exact value.', '$x = \\sqrt{13}$', '$x^2 = 4 + 9$', d=D.right_triangle(2, 3, '2', '3', 'x'), c=('eq', 'sqrt(2**2+3**2)', 'sqrt(13)')),
    Q('Use $\\cos 60^\\circ = \\frac{1}{2}$ to find $x$. (cm)', '$x = 9$ cm', '$\\cos 60^\\circ = \\frac{x}{18}$', d=D.right_triangle(18 * s60, 9, '', 'x', '18', theta='base', tlabel='60°'), c=('eq', '18*cos(rad(60))', '9')),
    Q('Find the volume of a cylinder with radius 5 cm and height 4 cm, in terms of $\\pi$.', '$100\\pi$ cm³', '$\\pi \\times 25 \\times 4$', c=('eq', 'pi*25*4', '100*pi')),
    Q('Find the distance between $(-1,\\ 3)$ and $(5,\\ 11)$.', '10 units', '$\\sqrt{6^2 + 8^2}$', c=('eq', 'sqrt(6**2+8**2)', '10')),
    Q('Find the gradient of the line through $(-2,\\ 7)$ and $(4,\\ -5)$.', '$-2$', '$\\frac{-5 - 7}{4 - (-2)} = \\frac{-12}{6}$', c=('eq', 'Rational(-5-7,4+2)', '-2')),
    Q('Find the equation of the line with gradient 2 that passes through $(1,\\ 5)$.', '$y = 2x + 3$', '$5 = 2(1) + c$, $c = 3$', c=('py', '2*1+3==5')),
    Q('Find the size of each interior angle of a regular hexagon.', '$120^\\circ$', 'angle sum $(6 - 2) \\times 180 = 720$; $720 \\div 6$', c=('eq', '(6-2)*180/6', '120')),
    Q('A die is rolled twice. Find $P(\\text{a double})$.', '$\\frac{1}{6}$', '6 doubles out of 36', c=('eq', 'Rational(6,36)', 'Rational(1,6)')),
    Q('Find the simple interest on \\$4000 at $3.5\\%$ p.a. for 4 years.', '\\$560', '$I = 4000 \\times 0.035 \\times 4$', c=('eq', '4000*Rational(35,1000)*4', '560')),
    Q('A 4 m ladder reaches 3.2 m up a wall. How far is its foot from the wall?', '2.4 m', '$\\sqrt{16 - 10.24} = \\sqrt{5.76}$', c=('eq', 'sqrt(Rational(16)-Rational(1024,100))', 'Rational(24,10)')),
])
BON.append(B('Show that the product of two consecutive whole numbers, plus the larger number, is always a perfect square.', '$n(n + 1) + (n + 1) = (n + 1)^2$', 'take out the common factor $(n + 1)$', c=('eq', 'expand(n*(n+1)+(n+1))', 'expand((n+1)**2)')))

# ---------------- Week 2 ----------------
W.append([
    Q('Write $0.\\dot{4}$ (that is, $0.444\\ldots$) as a fraction.', '$\\frac{4}{9}$', '$10x - x = 4$, so $9x = 4$', c=('eq', 'Rational(4,9)', 'nsimplify("0.444444444444",rational=True,tolerance=1e-10)')),
    Q('Evaluate $(6 \\times 10^5) \\times (4 \\times 10^{-2})$ in scientific notation.', '$2.4 \\times 10^4$', '$24 \\times 10^3$', c=('eq', '6*10**5*4*Rational(1,100)', '24000')),
    Q('Evaluate $27^{\\frac{2}{3}}$', '$9$', '$(\\sqrt[3]{27})^2 = 3^2$', c=('eq', '27**Rational(2,3)', '9')),
    Q('Simplify $3\\sqrt{2} + \\sqrt{8}$', '$5\\sqrt{2}$', '$\\sqrt{8} = 2\\sqrt{2}$', c=('eq', '3*sqrt(2)+sqrt(8)', '5*sqrt(2)')),
    Q('Simplify $\\dfrac{4x}{9} \\times \\dfrac{3}{2x}$', '$\\frac{2}{3}$', '$\\frac{12x}{18x}$', c=('eq', '4*x/9*3/(2*x)', 'Rational(2,3)')),
    Q('Expand $(2x - 3)^2$', '$4x^2 - 12x + 9$', '$(2x)^2 - 2(2x)(3) + 9$', c=('eq', 'expand((2*x-3)**2)', '4*x**2-12*x+9')),
    Q('Factorise $x^2 - 49$', '$(x - 7)(x + 7)$', 'difference of two squares', c=('fac', 'x**2-49', '(x-7)*(x+7)')),
    Q('Solve $5 - 2(x - 4) = 3x - 7$', '$x = 4$', '$13 - 2x = 3x - 7$, $20 = 5x$', c=('solve', '5-2*(x-4)', '3*x-7', 'x', ['4'])),
    Q('Solve $x^2 = 5x$', '$x = 0$ or $x = 5$', '$x(x - 5) = 0$ – don’t divide by $x$', c=('solve', 'x**2', '5*x', 'x', ['0', '5'])),
    Q('Solve $3x - 4 > 11$', '$x > 5$', '$3x > 15$', s=True, c=('py', 'sp.solve_univariate_inequality(3*x-4>11, x, relational=False)==sp.Interval.open(5, sp.oo)', {'sp': __import__('sympy')})),
    Q('Find the exact length of the diagonal of a square with sides 6 cm.', '$6\\sqrt{2}$ cm', '$\\sqrt{36 + 36} = \\sqrt{72}$', c=('eq', 'sqrt(6**2+6**2)', '6*sqrt(2)')),
    Q('A 50 m kite string makes an angle of $35^\\circ$ with the ground. Use $\\sin 35^\\circ \\approx 0.57$ to find the height of the kite.', '$\\approx 28.5$ m', '$h = 50 \\times 0.57$', c=('py', 'abs(50*0.57-28.5)<1e-9 and abs(50*sin(rad(35))-28.5)<0.3')),
    Q('Find the surface area of a closed cylinder with radius 2 cm and height 6 cm, in terms of $\\pi$.', '$32\\pi$ cm²', '$2\\pi(4) + 2\\pi(2)(6) = 8\\pi + 24\\pi$', c=('eq', '2*pi*4+2*pi*2*6', '32*pi')),
    Q('Find the midpoint of the interval joining $(-4,\\ 9)$ and $(6,\\ -3)$.', '$(1,\\ 3)$', '$\\left(\\frac{-4 + 6}{2},\\ \\frac{9 - 3}{2}\\right)$', c=('py', '((-4+6)/2,(9-3)/2)==(1,3)')),
    Q('Find the gradient of the line $3x + 2y = 12$.', '$-\\frac{3}{2}$', '$y = -\\frac{3}{2}x + 6$', c=('eq', 'sp.solve(3*x+2*y-12, y)[0].coeff(x)', '-Rational(3,2)')),
    Q('Find the equation of the line through $(1,\\ 2)$ and $(3,\\ 10)$.', '$y = 4x - 2$', '$m = \\frac{8}{2} = 4$; $2 = 4 + c$', c=('py', '4*1-2==2 and 4*3-2==10')),
    Q('Two similar triangles have matching sides 6 cm and 15 cm. A side of the smaller triangle is 4 cm. Find the matching side of the larger one.', '10 cm', 'scale factor $\\frac{15}{6} = 2.5$; $4 \\times 2.5$', c=('eq', '4*Rational(15,6)', '10')),
    Q('In a class of 30, 18 play sport, 12 play music and 5 do both. How many do neither?', '5', '$30 - (18 + 12 - 5)$', c=('eq', '30-(18+12-5)', '5')),
    Q('A surf shop buys a board for \\$250 and sells it for \\$340. Find the profit as a percentage of the cost price.', '$36\\%$', '$\\frac{90}{250} \\times 100\\%$', c=('eq', 'Rational(90,250)*100', '36')),
    Q('Two cyclists leave the same point. One rides north at 12 km/h and the other east at 16 km/h. How far apart are they after 2 hours?', '40 km', '24 km and 32 km: $\\sqrt{576 + 1024}$', c=('eq', 'sqrt(24**2+32**2)', '40')),
])
BON.append(B('Simplify $\\sqrt{50} + \\sqrt{18} - \\sqrt{32}$', '$4\\sqrt{2}$', '$5\\sqrt{2} + 3\\sqrt{2} - 4\\sqrt{2}$', c=('eq', 'sqrt(50)+sqrt(18)-sqrt(32)', '4*sqrt(2)')))

# ---------------- Week 3 ----------------
W.append([
    Q('A price rises by $20\\%$, then falls by $20\\%$. What is the overall percentage change?', 'a $4\\%$ decrease', '$1.2 \\times 0.8 = 0.96$', c=('eq', 'Rational(12,10)*Rational(8,10)', 'Rational(96,100)')),
    Q('Round $0.007\\,164\\,9$ to 3 significant figures.', '$0.007\\,16$', 'figures 7, 1, 6; the next digit is 4', c=('py', 'float("%.3g" % 0.0071649)==0.00716')),
    Q('Simplify $(2a^{-3})^2$, writing your answer with positive indices.', '$\\frac{4}{a^6}$', '$4a^{-6}$', c=('eq', '(2*a**-3)**2', '4/a**6')),
    Q('Expand and simplify $\\sqrt{3}(\\sqrt{12} + 2)$', '$6 + 2\\sqrt{3}$', '$\\sqrt{36} + 2\\sqrt{3}$', c=('eq', 'expand(sqrt(3)*(sqrt(12)+2))', '6+2*sqrt(3)')),
    Q('Simplify $\\dfrac{x + 1}{2} - \\dfrac{x - 3}{5}$', '$\\frac{3x + 11}{10}$', '$\\frac{5(x + 1) - 2(x - 3)}{10}$', s=True, c=('eq', '(x+1)/2-(x-3)/5', '(3*x+11)/10')),
    Q('Expand $(x + 5)(x - 5)$', '$x^2 - 25$', 'difference of two squares', c=('eq', 'expand((x+5)*(x-5))', 'x**2-25')),
    Q('Factorise $2x^2 + 7x + 3$', '$(2x + 1)(x + 3)$', 'check: $2x^2 + 6x + x + 3$', c=('fac', '2*x**2+7*x+3', '(2*x+1)*(x+3)')),
    Q('Solve $\\dfrac{x}{2} - \\dfrac{x}{5} = 3$', '$x = 10$', '$\\frac{3x}{10} = 3$', c=('solve', 'x/2-x/5', '3', 'x', ['10'])),
    Q('Solve $(x - 3)(2x + 1) = 0$', '$x = 3$ or $x = -\\frac{1}{2}$', 'one of the factors must be 0', c=('solve', '(x-3)*(2*x+1)', '0', 'x', ['3', '-Rational(1,2)'])),
    Q('Make $r$ the subject of $A = \\pi r^2$ (where $r > 0$).', '$r = \\sqrt{\\dfrac{A}{\\pi}}$', '$r^2 = \\frac{A}{\\pi}$', c=('py', 'sp.simplify(sp.pi*sp.sqrt(P/sp.pi)**2 - P)==0', {'sp': __import__('sympy')})),
    Q('A right-angled triangle has hypotenuse 10 cm and one side 5 cm. Find the other side in simplest surd form.', '$5\\sqrt{3}$ cm', '$\\sqrt{100 - 25} = \\sqrt{75}$', c=('eq', 'sqrt(100-25)', '5*sqrt(3)')),
    Q('In a right-angled triangle, the side opposite $\\theta$ is 7 cm and the hypotenuse is 14 cm. Find $\\theta$.', '$\\theta = 30^\\circ$', '$\\sin\\theta = \\frac{1}{2}$', s=True, c=('eq', 'sin(rad(30))', 'Rational(7,14)')),
    Q('A rectangular prism has volume 120 cm³, length 6 cm and width 4 cm. Find its surface area.', '148 cm²', 'height 5; $2(24 + 30 + 20)$', c=('eq', '2*(6*4+6*5+4*5)', '148')),
    Q('Find the exact distance between $(1,\\ -2)$ and $(4,\\ 4)$.', '$3\\sqrt{5}$', '$\\sqrt{9 + 36} = \\sqrt{45}$', c=('eq', 'sqrt(3**2+6**2)', '3*sqrt(5)')),
    Q('Find the gradient of a line perpendicular to the line joining $(0,\\ 0)$ and $(2,\\ 6)$.', '$-\\frac{1}{3}$', 'that line has gradient 3', c=('eq', '-1/Rational(6,2)', '-Rational(1,3)')),
    Q('Write $2x - 3y + 6 = 0$ in gradient–intercept form.', '$y = \\frac{2}{3}x + 2$', '$3y = 2x + 6$', s=True, c=('eq', 'sp.solve(2*x-3*y+6, y)[0]', '2*x/3+2')),
    Q('An exterior angle of a triangle is $125^\\circ$. One of the two interior opposite angles is $60^\\circ$. Find the other.', '$65^\\circ$', 'exterior angle = sum of interior opposite angles', c=('eq', '125-60', '65')),
    Q('A bag has 5 red and 3 green balls. Two are drawn without replacement. Find $P(\\text{one of each colour})$.', '$\\frac{15}{28}$', '$\\frac{5}{8} \\times \\frac{3}{7} + \\frac{3}{8} \\times \\frac{5}{7}$', c=('eq', '2*Rational(5,8)*Rational(3,7)', 'Rational(15,28)')),
    Q('\\$2000 is invested at $5\\%$ p.a. compound interest. Find the interest earned in 2 years.', '\\$205', '$2000 \\times 1.05^2 = 2205$', s=True, c=('eq', '2000*Rational(105,100)**2-2000', '205')),
    Q('A rectangular garden is 3 m longer than it is wide, and its area is 40 m². Find its dimensions.', '5 m by 8 m', '$x(x + 3) = 40$, $(x + 8)(x - 5) = 0$', c=('solve', 'x*(x+3)', '40', 'x', ['5', '-8'])),
])
BON.append(B('Find two consecutive positive odd numbers whose product is 143.', '11 and 13', '$n(n + 2) = 143$', c=('py', '[n for n in range(1,50,2) if n*(n+2)==143]==[11]')))

# ---------------- Week 4 ----------------
W.append([
    Q('After a $12\\%$ discount, a bike costs \\$440. Find the original price.', '\\$500', '$440 \\div 0.88$', c=('eq', '440/Rational(88,100)', '500')),
    Q('Evaluate $(9 \\times 10^{-3}) \\div (3 \\times 10^4)$ in scientific notation.', '$3 \\times 10^{-7}$', '$9 \\div 3$; $10^{-3 - 4}$', c=('eq', '9*Rational(1,1000)/(3*10**4)', '3*Rational(1,10**7)')),
    Q('Evaluate $16^{-\\frac{3}{4}}$', '$\\frac{1}{8}$', '$\\frac{1}{(\\sqrt[4]{16})^3} = \\frac{1}{2^3}$', c=('eq', '16**Rational(-3,4)', 'Rational(1,8)')),
    Q('Rationalise the denominator of $\\dfrac{6}{\\sqrt{3}}$', '$2\\sqrt{3}$', '$\\frac{6\\sqrt{3}}{3}$', s=True, c=('eq', '6/sqrt(3)', '2*sqrt(3)')),
    Q('Simplify $\\dfrac{x^2 - 9}{x + 3}$', '$x - 3$', '$\\frac{(x - 3)(x + 3)}{x + 3}$', s=True, c=('eq', 'sp.cancel((x**2-9)/(x+3))', 'x-3')),
    Q('Expand and simplify $(x + 3)^2 - (x - 1)^2$', '$8x + 8$', '$(x^2 + 6x + 9) - (x^2 - 2x + 1)$', c=('eq', 'expand((x+3)**2-(x-1)**2)', '8*x+8')),
    Q('Factorise $3x^2 - 27$', '$3(x - 3)(x + 3)$', 'HCF 3, then difference of squares', c=('fac', '3*x**2-27', '3*(x-3)*(x+3)')),
    Q('Solve $\\dfrac{2x - 1}{3} - \\dfrac{x + 2}{4} = 1$', '$x = \\frac{22}{5}$', '$4(2x - 1) - 3(x + 2) = 12$, $5x = 22$', c=('solve', '(2*x-1)/3-(x+2)/4', '1', 'x', ['Rational(22,5)'])),
    Q('Solve $x^2 + 6x + 4 = 0$ by completing the square.', '$x = -3 \\pm \\sqrt{5}$', '$(x + 3)^2 = 5$', s=True, c=('solve', 'x**2+6*x+4', '0', 'x', ['-3+sqrt(5)', '-3-sqrt(5)'])),
    Q('Solve $-2x + 5 \\le 11$', '$x \\ge -3$', '$-2x \\le 6$; dividing by $-2$ reverses the sign', s=True, c=('py', 'sp.solve_univariate_inequality(-2*x+5<=11, x, relational=False)==sp.Interval(-3, sp.oo)', {'sp': __import__('sympy')})),
    Q('A box is 3 cm by 4 cm by 12 cm. Find the length of the longest rod that fits inside it.', '13 cm', '$\\sqrt{9 + 16 + 144} = \\sqrt{169}$', s=True, c=('eq', 'sqrt(3**2+4**2+12**2)', '13')),
    Q('A ship sails 8 km on a bearing of $180^\\circ$T, then 6 km on a bearing of $270^\\circ$T. How far is it from its start?', '10 km', '8 km south then 6 km west: $\\sqrt{64 + 36}$', c=('eq', 'sqrt(8**2+6**2)', '10')),
    Q('Find the volume of a sphere with radius 3 cm, in terms of $\\pi$.', '$36\\pi$ cm³', '$\\frac{4}{3}\\pi \\times 27$', s=True, c=('eq', 'Rational(4,3)*pi*27', '36*pi')),
    Q('The midpoint of $AB$ is $(2,\\ -1)$ and $A$ is $(-3,\\ 4)$. Find $B$.', '$B(7,\\ -6)$', '$x$: $-3 \\to 2 \\to 7$; $y$: $4 \\to -1 \\to -6$', c=('py', '((-3+7)/2,(4-6)/2)==(2,-1)')),
    Q('The line through $(k,\\ 3)$ and $(5,\\ 9)$ has gradient 2. Find $k$.', '$k = 2$', '$\\frac{6}{5 - k} = 2$', c=('solve', '6/(5-k)', '2', 'k', ['2'])),
    Q('Find the equation of the line through $(2,\\ -1)$ that is parallel to $y = 3x + 5$.', '$y = 3x - 7$', '$-1 = 3(2) + c$', c=('py', '3*2-7==-1')),
    Q('An angle at the centre of a circle is $110^\\circ$. Find the angle at the circumference standing on the same arc.', '$55^\\circ$', 'half the angle at the centre', s=True, c=('eq', '110/2', '55')),
    Q('Of 50 students, 30 play netball, and 12 of the netballers also play touch. A netballer is chosen at random. Find $P(\\text{plays touch})$.', '$\\frac{2}{5}$', '$\\frac{12}{30}$', s=True, c=('eq', 'Rational(12,30)', 'Rational(2,5)')),
    Q('Kim earns \\$32 an hour with time-and-a-half for overtime. Find her pay for 38 normal hours and 6 overtime hours.', '\\$1504', '$38 \\times 32 + 6 \\times 48 = 1216 + 288$', c=('eq', '38*32+6*48', '1504')),
    Q('The sum of a number and its reciprocal is $\\frac{10}{3}$. Find the number.', '$3$ or $\\frac{1}{3}$', '$3x^2 - 10x + 3 = 0$, $(3x - 1)(x - 3) = 0$', c=('solve', 'x+1/x', 'Rational(10,3)', 'x', ['3', 'Rational(1,3)'])),
])
BON.append(B('Simplify $\\dfrac{1}{\\sqrt{3} - \\sqrt{2}}$', '$\\sqrt{3} + \\sqrt{2}$', 'multiply top and bottom by $\\sqrt{3} + \\sqrt{2}$; the bottom becomes $3 - 2 = 1$', c=('eq', '1/(sqrt(3)-sqrt(2))', 'sqrt(3)+sqrt(2)')))

# ---------------- Week 5 ----------------
W.append([
    Q('Convert 72 km/h to metres per second.', '20 m/s', '$72\\,000 \\text{ m} \\div 3600 \\text{ s}$', c=('eq', '72000/3600', '20')),
    Q('A dust particle has mass $7.5 \\times 10^{-10}$ kg. How many particles have a total mass of $1.5 \\times 10^{-6}$ kg?', '$2 \\times 10^3$', '$\\frac{1.5}{7.5} \\times 10^{4} = 0.2 \\times 10^4$', c=('eq', 'Rational(15,10)*Rational(1,10**6)/(Rational(75,10)*Rational(1,10**10))', '2000')),
    Q('Simplify $\\dfrac{x^3y^{-2}}{x^{-1}y^4}$, with positive indices.', '$\\frac{x^4}{y^6}$', '$x^{3 - (-1)}y^{-2 - 4}$', c=('eq', 'x**3*y**-2/(x**-1*y**4)', 'x**4/y**6')),
    Q('Expand and simplify $(\\sqrt{5} + 2)(\\sqrt{5} - 2)$', '$1$', '$5 - 4$', c=('eq', 'expand((sqrt(5)+2)*(sqrt(5)-2))', '1')),
    Q('Simplify $\\dfrac{3}{x} + \\dfrac{2}{3x}$', '$\\frac{11}{3x}$', '$\\frac{9}{3x} + \\frac{2}{3x}$', c=('eq', '3/x+2/(3*x)', '11/(3*x)')),
    Q('Expand and simplify $(x + 2)(x^2 - x + 3)$', '$x^3 + x^2 + x + 6$', '$x^3 - x^2 + 3x + 2x^2 - 2x + 6$', s=True, c=('eq', 'expand((x+2)*(x**2-x+3))', 'x**3+x**2+x+6')),
    Q('Factorise $ax + ay + 3x + 3y$', '$(x + y)(a + 3)$', '$a(x + y) + 3(x + y)$', c=('fac', 'a*x+a*y+3*x+3*y', '(x+y)*(a+3)')),
    Q('Solve $4(3 - x) = 2(x + 9)$', '$x = -1$', '$12 - 4x = 2x + 18$, $-6 = 6x$', c=('solve', '4*(3-x)', '2*(x+9)', 'x', ['-1'])),
    Q('Use the quadratic formula to solve $x^2 - 2x - 4 = 0$.', '$x = 1 \\pm \\sqrt{5}$', '$\\frac{2 \\pm \\sqrt{4 + 16}}{2} = \\frac{2 \\pm 2\\sqrt{5}}{2}$', s=True, c=('solve', 'x**2-2*x-4', '0', 'x', ['1+sqrt(5)', '1-sqrt(5)'])),
    Q('Make $u$ the subject of $v^2 = u^2 + 2as$.', '$u = \\pm\\sqrt{v^2 - 2as}$', '$u^2 = v^2 - 2as$', c=('solve', 'u**2+2*a*s', 'v**2', 'u', ['sqrt(v**2-2*a*s)', '-sqrt(v**2-2*a*s)'])),
    Q('Rectangle $ABCD$ has $AB = 8$ cm and diagonal $AC = 10$ cm. Find its area.', '48 cm²', '$BC = \\sqrt{100 - 64} = 6$; $8 \\times 6$', c=('eq', '8*sqrt(10**2-8**2)', '48')),
    Q('In $\\triangle ABC$, $a = 10$, $A = 30^\\circ$ and $B = 45^\\circ$. Use the sine rule to find $b$ exactly.', '$b = 10\\sqrt{2}$', '$b = \\frac{10\\sin 45^\\circ}{\\sin 30^\\circ} = \\frac{10 \\times \\frac{\\sqrt{2}}{2}}{\\frac{1}{2}}$', s=True,
      c=('eq', '10*sin(rad(45))/sin(rad(30))', '10*sqrt(2)')),
    Q('A cone has radius 6 cm and slant height 10 cm. Find its perpendicular height and its volume, in terms of $\\pi$.', '8 cm; $96\\pi$ cm³', '$h = \\sqrt{100 - 36}$; $V = \\frac{1}{3}\\pi(36)(8)$', s=True,
      c=('py', 'sqrt(100-36)==8 and Rational(1,3)*pi*36*8==96*pi')),
    Q('Find the side lengths of the triangle with vertices $A(0,\\ 0)$, $B(4,\\ 0)$ and $C(2,\\ 2\\sqrt{3})$. What type of triangle is it?', 'all 4 units: equilateral', '$AC = \\sqrt{4 + 12} = 4$, $BC = \\sqrt{4 + 12} = 4$',
      c=('py', 'sqrt(2**2+(2*sqrt(3))**2)==4 and sqrt((4-2)**2+(2*sqrt(3))**2)==4')),
    Q('Find the angle a line with gradient 1 makes with the positive $x$-axis.', '$45^\\circ$', '$\\tan\\theta = m = 1$', s=True, c=('eq', 'tan(rad(45))', '1')),
    Q('Find the equation of the perpendicular bisector of the interval joining $(1,\\ 1)$ and $(5,\\ 3)$.', '$y = -2x + 8$', 'midpoint $(3, 2)$; gradient $\\frac{1}{2}$, so use $-2$', s=True, c=('py', '-2*3+8==2 and Rational(3-1,5-1)*(-2)==-1')),
    Q('Each exterior angle of a regular polygon is $24^\\circ$. How many sides does it have?', '15', '$360 \\div 24$', c=('eq', '360/24', '15')),
    Q('Three coins are tossed. Find $P(\\text{exactly two heads})$.', '$\\frac{3}{8}$', 'HHT, HTH, THH out of 8', c=('eq', 'Rational(3,8)', 'Rational(len([1 for a in "HT" for b in "HT" for c in "HT" if (a+b+c).count("H")==2]),8)')),
    Q('A \\$50 000 machine depreciates by $10\\%$ p.a. Find its value after 2 years.', '\\$40 500', '$50\\,000 \\times 0.9^2$', s=True, c=('eq', '50000*Rational(9,10)**2', '40500')),
    Q('Lily walks to the beach at 5 km/h and jogs home at 10 km/h. The round trip takes 1.5 hours. How far away is the beach?', '5 km', '$\\frac{d}{5} + \\frac{d}{10} = 1.5$', c=('solve', 'd/5+d/10', 'Rational(3,2)', 'd', ['5'])),
])
BON.append(B('Show that $x^2 + 6x + 10$ is positive for every value of $x$.', '$x^2 + 6x + 10 = (x + 3)^2 + 1 \\ge 1$', 'a square is never negative', c=('eq', 'expand((x+3)**2+1)', 'x**2+6*x+10')))

# ---------------- Week 6 ----------------
W.append([
    Q('Write $0.\\dot{1}\\dot{2}$ (that is, $0.121212\\ldots$) as a fraction.', '$\\frac{4}{33}$', '$100x - x = 12$, $x = \\frac{12}{99}$', c=('eq', 'Rational(12,99)', 'Rational(4,33)')),
    Q('Light travels at $3 \\times 10^8$ m/s. How far does it travel in $5 \\times 10^2$ seconds?', '$1.5 \\times 10^{11}$ m', '$15 \\times 10^{10}$', c=('eq', '3*10**8*5*10**2', '15*10**10')),
    Q('Evaluate $\\log_2 32 + \\log_3 \\frac{1}{9}$', '$3$', '$5 + (-2)$', s=True, c=('eq', 'log(32,2)+log(Rational(1,9),3)', '3')),
    Q('Evaluate $(2\\sqrt{3})^2 + \\sqrt{27} \\times \\sqrt{3}$', '$21$', '$12 + \\sqrt{81}$', c=('eq', '(2*sqrt(3))**2+sqrt(27)*sqrt(3)', '21')),
    Q('Simplify $\\dfrac{x^2 + 5x + 6}{x^2 - 4}$', '$\\frac{x + 3}{x - 2}$', '$\\frac{(x + 2)(x + 3)}{(x - 2)(x + 2)}$', s=True, c=('eq', 'sp.cancel((x**2+5*x+6)/(x**2-4))', '(x+3)/(x-2)')),
    Q('Expand and simplify $(2x + 3)(2x - 3) - (2x - 1)^2$', '$4x - 10$', '$4x^2 - 9 - (4x^2 - 4x + 1)$', c=('eq', 'expand((2*x+3)*(2*x-3)-(2*x-1)**2)', '4*x-10')),
    Q('Factorise $6x^2 - x - 2$', '$(2x + 1)(3x - 2)$', 'check: $6x^2 - 4x + 3x - 2$', c=('fac', '6*x**2-x-2', '(2*x+1)*(3*x-2)')),
    Q('Solve simultaneously: $3x + 2y = 16$ and $x - y = 2$', '$x = 4$, $y = 2$', '$x = y + 2$: $3y + 6 + 2y = 16$', s=True, c=('py', 'sp.solve([3*x+2*y-16, x-y-2],[x,y])=={x:4,y:2}', {'sp': __import__('sympy')})),
    Q('Solve $2x^2 - 5x - 3 = 0$', '$x = 3$ or $x = -\\frac{1}{2}$', '$(2x + 1)(x - 3) = 0$', c=('solve', '2*x**2-5*x-3', '0', 'x', ['3', '-Rational(1,2)'])),
    Q('Solve $5 - 3x < 2x - 10$', '$x > 3$', '$15 < 5x$', s=True, c=('py', 'sp.solve_univariate_inequality(5-3*x<2*x-10, x, relational=False)==sp.Interval.open(3, sp.oo)', {'sp': __import__('sympy')})),
    Q('Find $x$. (cm)', '$x = 5$', '$x^2 + (x + 7)^2 = 169$, so $x^2 + 7x - 60 = 0$', d=D.right_triangle(5, 12, 'x', 'x + 7', '13'), c=('solve', 'x**2+(x+7)**2', '169', 'x', ['5', '-12'])),
    Q('Find $c$ using the cosine rule.', '$c = 7$', '$c^2 = 25 + 64 - 2(5)(8)\\cos 60^\\circ = 49$', s=True, d=D.oblique_triangle(8, 5, 60, '8', '5', 'c', '60°'),
      c=('eq', 'sqrt(5**2+8**2-2*5*8*cos(rad(60)))', '7')),
    Q('A hemisphere of radius 3 cm sits on top of a cylinder with radius 3 cm and height 10 cm. Find the total volume, in terms of $\\pi$.', '$108\\pi$ cm³', '$\\frac{2}{3}\\pi(27) + \\pi(9)(10) = 18\\pi + 90\\pi$', s=True, c=('eq', 'Rational(2,3)*pi*27+pi*9*10', '108*pi')),
    Q('Find the equation of the circle with centre $(0,\\ 0)$ that passes through $(3,\\ 4)$.', '$x^2 + y^2 = 25$', 'radius $= \\sqrt{9 + 16} = 5$', c=('eq', '3**2+4**2', '25')),
    Q('The points $(1,\\ 2)$, $(3,\\ 8)$ and $(k,\\ 14)$ lie on a straight line. Find $k$.', '$k = 5$', 'gradient 3: $\\frac{14 - 2}{k - 1} = 3$', c=('solve', '(14-2)/(k-1)', '3', 'k', ['5'])),
    Q('Find the equation, in general form, of the line through $(-1,\\ 4)$ with gradient $-\\frac{2}{3}$.', '$2x + 3y - 10 = 0$', '$y - 4 = -\\frac{2}{3}(x + 1)$, so $3y - 12 = -2x - 2$', s=True, c=('py', '2*(-1)+3*4-10==0 and Rational(-2,3)==-Rational(2,3)')),
    Q('$OT$ is a radius and $PT$ is a tangent to the circle at $T$. If $\\angle TOP = 50^\\circ$, find $\\angle OPT$.', '$40^\\circ$', 'the tangent is perpendicular to the radius: $180 - 90 - 50$', s=True, c=('eq', '180-90-50', '40')),
    Q('A spinner lands on red with probability $0.3$. It is spun twice. Find $P(\\text{at least one red})$.', '$0.51$', '$1 - 0.7^2 = 1 - 0.49$', c=('eq', '1-Rational(7,10)**2', 'Rational(51,100)')),
    Q('Ben earns \\$1100 a week. He takes 4 weeks’ annual leave with $17.5\\%$ leave loading. Find his total holiday pay.', '\\$5170', '$4400 \\times 1.175$', c=('eq', '4*1100*Rational(1175,1000)', '5170')),
    Q('A farmer uses 40 m of fencing for three sides of a rectangular pen against a wall. The area is 200 m². Find the dimensions.', '10 m by 20 m', '$x(40 - 2x) = 200$, $(x - 10)^2 = 0$', c=('solve', 'x*(40-2*x)', '200', 'x', ['10'])),
])
BON.append(B('Find all real solutions of $x^4 - 13x^2 + 36 = 0$.', '$x = \\pm 2$ or $x = \\pm 3$', '$(x^2 - 4)(x^2 - 9) = 0$', c=('solve', 'x**4-13*x**2+36', '0', 'x', ['2', '-2', '3', '-3'])))

BK['weeks'] = W
BK['bonus'] = BON

BK['hints'] = [
    ('Number', ['Increase by $20\\%$ then decrease by $20\\%$: $\\times 1.2 \\times 0.8$',
                'Original price $=$ sale price $\\div$ (decimal you paid)',
                'Recurring decimals: $0.\\dot{4} = \\frac{4}{9}$, $0.\\dot{1}\\dot{2} = \\frac{12}{99}$',
                'Scientific notation: $a \\times 10^n$, $1 \\le a < 10$']),
    ('Indices & surds', ['$a^{-n} = \\frac{1}{a^n}$ · $a^{\\frac{m}{n}} = (\\sqrt[n]{a})^m$',
                         '$\\sqrt{ab} = \\sqrt{a}\\sqrt{b}$, e.g. $\\sqrt{48} = 4\\sqrt{3}$',
                         '$(\\sqrt{a} + b)(\\sqrt{a} - b) = a - b^2$',
                         '<span class="star">★</span> $\\frac{6}{\\sqrt{3}} = \\frac{6\\sqrt{3}}{3}$ · $\\log_a x = n \\Leftrightarrow a^n = x$']),
    ('Algebra', ['Fractions: common denominator, brackets around numerators',
                 '$(a \\pm b)^2 = a^2 \\pm 2ab + b^2$ · $(a + b)(a - b) = a^2 - b^2$',
                 'Factorise: HCF first, then DOTS, trinomials or grouping',
                 'Cancel factors, never terms']),
    ('Equations', ['Fractions: multiply every term by the common denominator',
                   '$x^2 = 5x$: move everything to one side and factorise',
                   '<span class="star">★</span> $x = \\dfrac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$ · complete the square: add $(\\frac{b}{2})^2$',
                   '<span class="star">★</span> Inequalities: ×/÷ by a negative reverses the sign']),
    ('Measurement & trig', ['$\\sin\\theta = \\frac{O}{H}$ · $\\cos\\theta = \\frac{A}{H}$ · $\\tan\\theta = \\frac{O}{A}$',
                            '$\\sin 30^\\circ = \\cos 60^\\circ = \\frac{1}{2}$ · $\\sin 45^\\circ = \\frac{\\sqrt{2}}{2}$',
                            'Cylinder $SA = 2\\pi r^2 + 2\\pi rh$',
                            '<span class="star">★</span> $\\frac{a}{\\sin A} = \\frac{b}{\\sin B}$ · $c^2 = a^2 + b^2 - 2ab\\cos C$',
                            '<span class="star">★</span> Cone $V = \\frac{1}{3}\\pi r^2h$ · sphere $V = \\frac{4}{3}\\pi r^3$']),
    ('Coordinate geometry', ['$d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ · $M = \\left(\\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2}\\right)$',
                             '$m = \\frac{y_2 - y_1}{x_2 - x_1}$ · parallel: equal $m$ · perpendicular: $m_1m_2 = -1$',
                             '<span class="star">★</span> $y - y_1 = m(x - x_1)$ · general form $ax + by + c = 0$',
                             '<span class="star">★</span> $m = \\tan\\theta$ (angle with the $x$-axis)']),
    ('Geometry & chance', ['Polygon angle sum $(n - 2) \\times 180^\\circ$ · exterior angles add to $360^\\circ$',
                           'Similar figures: multiply by the scale factor',
                           'Venn: $n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$',
                           '<span class="star">★</span> Angle at the centre is twice the angle at the circumference; tangent ⊥ radius']),
    ('In context', ['$I = Prn$ · profit % $= \\frac{\\text{profit}}{\\text{cost}} \\times 100\\%$',
                    'Leave loading: $17.5\\%$ extra on holiday pay',
                    '<span class="star">★</span> $A = P(1 + r)^n$ · depreciation $S = V_0(1 - r)^n$',
                    'Worded problems: define the unknown, write an equation, check the answer makes sense']),
]
