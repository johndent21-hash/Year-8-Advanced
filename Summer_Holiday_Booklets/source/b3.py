"""Year 9 Standard -> Year 10 Standard (Stage 5 core revision, Year 10 preview)."""
import math
from qlib import Q, B, xy, stemleaf
import diagrams as D

BK = dict(
    key='b3',
    file='Yr9_Standard_Summer_Holiday_Ready_for_Yr10_Standard_Revision_Booklet',
    kicker='YEAR 9 STANDARD → YEAR 10 STANDARD',
    ready='Ready for Year 10',
    intro='Six weeks. Twenty questions a week. Every Year 9 skill that Year 10 Standard builds on – mixed together so it sticks.',
    star_text='Year 10 preview (Stage 5)',
    pattern='Question 1 is always fractions and integers, question 11 is always Pythagoras, and so on. If the same number keeps going wrong, that is the skill to revise before Year 10.',
    groups=[('Number', '', [1, 2, 3]), ('Indices', '', [4, 5]), ('Algebra', '', [6, 7, 8]),
            ('Equations', '', [9, 10]), ('Measurement & trig', '', [11, 12, 13, 14]), ('Coordinate geometry', '', [15, 16]),
            ('Data & chance', '', [17, 18]), ('Money & context', '', [19, 20])],
    strands={1: 'Fractions & integers', 2: 'Percentages', 3: 'Sig. figs & sci. notation', 4: 'Index laws', 5: 'Zero & negative indices',
             6: 'Simplify & substitute', 7: 'Expand', 8: 'Factorise', 9: 'Equations', 10: 'Formulas & word problems',
             11: 'Pythagoras', 12: 'Trigonometry', 13: 'Area & surface area', 14: 'Volume', 15: 'Gradient & midpoint',
             16: 'Straight lines', 17: 'Data', 18: 'Probability', 19: 'Earning money', 20: 'Problem solving'},
    rules=['<b>No calculator.</b> Leave answers exact (e.g. $48\\pi$) unless asked to round. Trig questions give you the value you need.',
           '<b>Show working</b> in the space under each question.',
           '<b>Mark it yourself</b> using the answers at the back (pages 10–12). Each answer has a line of working to help you find a mistake.',
           '<b>Fix it.</b> Redo anything you got wrong a day or two later, without looking.',
           '<span class="star">★</span> questions preview Year 10 Standard work. Have a go – they are the ones that will help most in Term 1.',
           '<b>Stuck?</b> The hints page (page 9) has the key facts and formulas.'],
    first_up='<b>First up in Year 10 Standard:</b> interest and depreciation, graphing lines, surface area and volume, algebra and equations. Every one of them starts from the skills in these six pages.',
    outcomes='Revises MA5-FIN-C-01, MA5-ALG-C-01, MA5-IND-C-01, MA5-EQU-C-01, MA5-LIN-C-01, MA5-LIN-C-02, MA5-MAG-C-01, MA5-TRG-C-01, MA5-ARE-C-01, MA5-VOL-C-01, MA5-GEO-C-01, MA5-DAT-C-01, MA5-PRO-C-01, with MA4-PYT-C-01. <span class="star">★</span> Year 10 preview: MA5-FIN-C-02, MA5-TRG-C-02, MA5-ARE-P-01, MA5-VOL-P-01, MA5-ALG-P-02, MA5-EQU-P-01, MA5-EQU-P-02, MA5-LIN-C-02 (perpendicular lines).',
)

W, BON = [], []
t35, s40, t40 = math.tan(math.radians(35)), math.sin(math.radians(40)), math.tan(math.radians(40))

# ---------------- Week 1 ----------------
W.append([
    Q('Evaluate $-12 + 3 \\times (-4)$', '$-24$', '$-12 + (-12)$', c=('eq', '-12+3*(-4)', '-24')),
    Q('Increase \\$250 by $12\\%$.', '\\$280', '$12\\%$ of 250 = 30', c=('eq', '250*Rational(112,100)', '280')),
    Q('Round $0.05348$ to 2 significant figures.', '$0.053$', 'first significant figure is 5; next digit 3 rounds down', c=('py', 'float("%.2g" % 0.05348)==0.053')),
    Q('Simplify $a^5 \\times a^3$', '$a^8$', 'add the indices', c=('eq', 'a**5*a**3', 'a**8')),
    Q('Evaluate $5^0 + 3^{-1}$', '$1\\tfrac{1}{3}$', '$1 + \\frac{1}{3}$', c=('eq', 'Rational(5)**0+Rational(3)**-1', 'Rational(4,3)')),
    Q('Simplify $4x - 7y - 2x + 3y$', '$2x - 4y$', '$4x - 2x$ and $-7y + 3y$', c=('eq', '4*x-7*y-2*x+3*y', '2*x-4*y')),
    Q('Expand and simplify $3(2x - 5) + 4x$', '$10x - 15$', '$6x - 15 + 4x$', c=('eq', 'expand(3*(2*x-5)+4*x)', '10*x-15')),
    Q('Factorise $9a^2 - 6a$', '$3a(3a - 2)$', 'HCF = $3a$', c=('fac', '9*a**2-6*a', '3*a*(3*a-2)')),
    Q('Solve $4x - 9 = 2x + 5$', '$x = 7$', '$2x = 14$', c=('solve', '4*x-9', '2*x+5', 'x', ['7'])),
    Q('$s = ut + \\frac{1}{2}at^2$. Find $s$ when $u = 3$, $t = 4$ and $a = 2$.', '$s = 28$', '$12 + \\frac{1}{2} \\times 2 \\times 16 = 12 + 16$', c=('eq', '3*4+Rational(1,2)*2*4**2', '28')),
    Q('Find $c$. (cm)', '25 cm', '$c^2 = 49 + 576 = 625$', d=D.right_triangle(7, 24, '7', '24', 'c'), c=('eq', 'sqrt(7**2+24**2)', '25')),
    Q('Write $\\sin\\theta$ as a fraction in simplest form.', '$\\sin\\theta = \\frac{3}{5}$', '$\\frac{\\text{opposite}}{\\text{hypotenuse}} = \\frac{6}{10}$',
      d=D.right_triangle(6, 8, '6', '8', '10', theta='base'), c=('eq', 'Rational(6,10)', 'Rational(3,5)')),
    Q('Find the surface area of a cube with edges 5 cm long.', '150 cm²', '6 faces: $6 \\times 25$', c=('eq', '6*5**2', '150')),
    Q('Find the volume of a cylinder with radius 4 cm and height 5 cm, in terms of $\\pi$.', '$80\\pi$ cm³', '$\\pi \\times 16 \\times 5$', c=('eq', 'pi*4**2*5', '80*pi')),
    Q('Find the midpoint of the interval joining $(2,\\ 7)$ and $(8,\\ -1)$.', '$(5,\\ 3)$', '$\\left(\\frac{2 + 8}{2},\\ \\frac{7 + (-1)}{2}\\right)$', c=('py', '((2+8)/2,(7-1)/2)==(5,3)')),
    Q('State the gradient and $y$-intercept of $y = -2x + 5$.', '$m = -2$, $c = 5$', 'compare with $y = mx + c$', c=('man', 'read off y=mx+c')),
    Q('Find the mean of $12,\\ 15,\\ 9,\\ 18,\\ 16$.', '$14$', '$70 \\div 5$', c=('eq', 'Rational(12+15+9+18+16,5)', '14')),
    Q('Two coins are tossed. Find $P(\\text{at least one head})$.', '$\\frac{3}{4}$', 'HH, HT, TH out of 4', c=('eq', '1-Rational(1,4)', 'Rational(3,4)')),
    Q('Liam earns \\$28 an hour. Find his pay for a 35-hour week.', '\\$980', '$35 \\times 28$', c=('eq', '35*28', '980')),
    Q('A phone plan costs \\$45 a month plus 10 cents per text. Find the cost of a month with 120 texts.', '\\$57', '$45 + 120 \\times 0.10$', c=('eq', '45+120*Rational(1,10)', '57')),
])
BON.append(B('The sum of three consecutive even numbers is 78. Find them.', '24, 26 and 28', '$n + (n + 2) + (n + 4) = 78$, $3n = 72$', c=('solve', 'n+(n+2)+(n+4)', '78', 'n', ['24'])))

# ---------------- Week 2 ----------------
W.append([
    Q('Evaluate $\\dfrac{2}{3} \\times \\dfrac{9}{10} - \\dfrac{1}{5}$', '$\\frac{2}{5}$', '$\\frac{18}{30} - \\frac{1}{5} = \\frac{3}{5} - \\frac{1}{5}$', c=('eq', 'Rational(2,3)*Rational(9,10)-Rational(1,5)', 'Rational(2,5)')),
    Q('A jacket marked \\$120 is reduced by $35\\%$. Find the sale price.', '\\$78', '$35\\%$ of 120 = 42', c=('eq', '120*Rational(65,100)', '78')),
    Q('Write $4\\,720\\,000$ in scientific notation.', '$4.72 \\times 10^6$', 'move the decimal point 6 places', c=('eq', 'Rational(472,100)*10**6', '4720000')),
    Q('Simplify $(2m^3)^2$', '$4m^6$', '$2^2 \\times m^{3 \\times 2}$', c=('eq', '(2*m**3)**2', '4*m**6')),
    Q('Write $10^{-3}$ as a decimal.', '$0.001$', '$\\frac{1}{1000}$', c=('eq', 'Rational(10)**-3', 'Rational(1,1000)')),
    Q('If $p = -2$ and $q = 3$, find the value of $p^2 - 4pq$.', '$28$', '$4 - 4(-2)(3) = 4 + 24$', c=('eq', '(-2)**2-4*(-2)*3', '28')),
    Q('Expand $(x + 6)(x - 2)$', '$x^2 + 4x - 12$', '$x^2 - 2x + 6x - 12$', c=('eq', 'expand((x+6)*(x-2))', 'x**2+4*x-12')),
    Q('Factorise $14xy + 21y$', '$7y(2x + 3)$', 'HCF = $7y$', c=('fac', '14*x*y+21*y', '7*y*(2*x+3)')),
    Q('Solve $5(x + 2) = 3x + 18$', '$x = 4$', '$5x + 10 = 3x + 18$, $2x = 8$', c=('solve', '5*(x+2)', '3*x+18', 'x', ['4'])),
    Q('Rachel is 3 times as old as her brother. In 4 years their ages will add to 36. How old is her brother now?', '7', '$b + 4 + 3b + 4 = 36$, $4b = 28$', c=('solve', '(n+4)+(3*n+4)', '36', 'n', ['7'])),
    Q('Find $x$. (cm)', '15 cm', '$x^2 = 289 - 64 = 225$', d=D.right_triangle(8, 15, '8', 'x', '17'), c=('eq', 'sqrt(17**2-8**2)', '15')),
    Q('Use $\\tan 35^\\circ \\approx 0.70$ to find $x$. (cm)', '$x \\approx 14$ cm', '$\\tan 35^\\circ = \\frac{x}{20}$, $x = 20 \\times 0.70$',
      d=D.right_triangle(20 * t35, 20, 'x', '20', '', theta='base', tlabel='35°'), c=('py', 'abs(20*0.70-14)<1e-9 and abs(20*tan(rad(35))-14)<0.1')),
    Q('Find the area of a quadrant (quarter circle) with radius 6 cm, in terms of $\\pi$.', '$9\\pi$ cm²', '$\\frac{1}{4} \\times \\pi \\times 36$', c=('eq', 'Rational(1,4)*pi*36', '9*pi')),
    Q('A triangular prism has a triangle with base 8 cm and height 6 cm as its cross-section, and length 15 cm. Find its volume.', '360 cm³', '$A = 24$; $V = 24 \\times 15$', c=('eq', 'Rational(1,2)*8*6*15', '360')),
    Q('Find the gradient of the line through $(-1,\\ 4)$ and $(3,\\ -8)$.', '$-3$', '$\\frac{-8 - 4}{3 - (-1)} = \\frac{-12}{4}$', c=('eq', 'Rational(-8-4,3-(-1))', '-3')),
    Q('Find the equation of the line with gradient 3 that passes through $(0,\\ -4)$.', '$y = 3x - 4$', '$y$-intercept is $-4$', c=('man', 'y = mx + c, c = -4')),
    Q('Find the median of the data in the stem-and-leaf plot.', '$32$', '10 values; middle two are 32 and 32', d=stemleaf([(2, [3, 5, 8]), (3, [0, 2, 2, 6]), (4, [1, 4, 9])], '3 | 2 means 32'),
      c=('py', 'sorted(L)[4]==32 and sorted(L)[5]==32', {'L': [23, 25, 28, 30, 32, 32, 36, 41, 44, 49]})),
    Q('A card is drawn at random from cards numbered 1 to 12. Find $P(\\text{factor of } 12)$.', '$\\frac{1}{2}$', '1, 2, 3, 4, 6, 12: $\\frac{6}{12}$', c=('eq', 'Rational(len([n for n in range(1,13) if 12%n==0]),12)', 'Rational(1,2)')),
    Q('Sam’s normal rate is \\$30 an hour. He works 38 hours at the normal rate and 4 hours at time-and-a-half. Find his pay.', '\\$1320', '$38 \\times 30 + 4 \\times 45 = 1140 + 180$', c=('eq', '38*30+4*45', '1320')),
    Q('A map has a scale of $1 : 25\\,000$. A walking track is 14 cm long on the map. Find its real length in km.', '3.5 km', '$14 \\times 25\\,000 = 350\\,000$ cm', c=('eq', '14*25000/100000', '3.5')),
])
BON.append(B('Show that $(n + 1)^2 - (n - 1)^2 = 4n$ for every number $n$.', '$n^2 + 2n + 1 - (n^2 - 2n + 1) = 4n$', 'the $n^2$ and 1 terms cancel', c=('eq', 'expand((n+1)**2-(n-1)**2)', '4*n')))

# ---------------- Week 3 ----------------
W.append([
    Q('Evaluate $3\\tfrac{3}{4} - 1\\tfrac{5}{6}$', '$1\\tfrac{11}{12}$', '$\\frac{45}{12} - \\frac{22}{12} = \\frac{23}{12}$', c=('eq', 'Rational(15,4)-Rational(11,6)', 'Rational(23,12)')),
    Q('Write \\$45 as a percentage of \\$360.', '$12.5\\%$', '$\\frac{45}{360} = \\frac{1}{8}$', c=('eq', 'Rational(45,360)*100', 'Rational(25,2)')),
    Q('Write $3.06 \\times 10^{-4}$ as a decimal.', '$0.000\\,306$', 'move the decimal point 4 places left', c=('eq', 'Rational(306,100)*Rational(1,10**4)', 'Rational(306,1000000)')),
    Q('Simplify $12x^7 \\div 4x^2$', '$3x^5$', '$12 \\div 4$; subtract the indices', c=('eq', '12*x**7/(4*x**2)', '3*x**5')),
    Q('Evaluate $2^{-2} \\times 8$', '$2$', '$\\frac{1}{4} \\times 8$', c=('eq', 'Rational(2)**-2*8', '2')),
    Q('Simplify $\\dfrac{2a}{3} + \\dfrac{a}{6}$', '$\\frac{5a}{6}$', '$\\frac{4a}{6} + \\frac{a}{6}$', c=('eq', '2*a/3+a/6', '5*a/6')),
    Q('Expand $(2x + 1)(x + 4)$', '$2x^2 + 9x + 4$', '$2x^2 + 8x + x + 4$', c=('eq', 'expand((2*x+1)*(x+4))', '2*x**2+9*x+4')),
    Q('Factorise $x^2 + 7x + 12$', '$(x + 3)(x + 4)$', '$3 \\times 4 = 12$, $3 + 4 = 7$', s=True, c=('fac', 'x**2+7*x+12', '(x+3)*(x+4)')),
    Q('Solve $\\dfrac{2x - 1}{3} = 5$', '$x = 8$', '$2x - 1 = 15$', c=('solve', '(2*x-1)/3', '5', 'x', ['8'])),
    Q('Use $F = \\frac{9C}{5} + 32$ to find $C$ when $F = 59$.', '$C = 15$', '$27 = \\frac{9C}{5}$, $9C = 135$', c=('solve', '9*n/5+32', '59', 'n', ['15'])),
    Q('A rectangle is 9 cm by 12 cm. Find the length of its diagonal.', '15 cm', '$d^2 = 81 + 144 = 225$', d=D.rect_diag(12, 9, '12', '9', 'd'), c=('eq', 'sqrt(9**2+12**2)', '15')),
    Q('Use $\\sin 40^\\circ \\approx 0.64$ to find $x$. (cm)', '$x \\approx 9.6$ cm', '$\\sin 40^\\circ = \\frac{x}{15}$, $x = 15 \\times 0.64$',
      d=D.right_triangle(15 * s40, 15 * math.cos(math.radians(40)), 'x', '', '15', theta='base', tlabel='40°'), c=('py', 'abs(15*0.64-9.6)<1e-9 and abs(15*sin(rad(40))-9.6)<0.1')),
    Q('Find the surface area of a rectangular prism 6 cm by 4 cm by 3 cm.', '108 cm²', '$2(24 + 18 + 12)$', c=('eq', '2*(6*4+6*3+4*3)', '108')),
    Q('A tank is 2 m long, 1.5 m wide and 1 m high. How many litres does it hold? ($1 \\text{ m}^3 = 1000$ L)', '3000 L', '$2 \\times 1.5 \\times 1 = 3 \\text{ m}^3$', c=('eq', '2*1.5*1*1000', '3000')),
    Q('Find the length of the interval joining $(1,\\ 2)$ and $(7,\\ 10)$.', '10 units', '$\\sqrt{6^2 + 8^2} = \\sqrt{100}$', c=('eq', 'sqrt((7-1)**2+(10-2)**2)', '10')),
    Q('Does the point $(-2,\\ 7)$ lie on the line $y = -3x + 1$?', 'Yes', '$-3(-2) + 1 = 7$ ✓', c=('py', '-3*(-2)+1==7')),
    Q('Which of these is categorical data: shoe size, favourite beach, height, number of siblings?', 'favourite beach', 'the others are numerical', c=('man', 'only favourite beach is categorical')),
    Q('A bag has 3 red and 2 blue marbles. One is drawn and replaced, then a second is drawn. Find $P(\\text{both red})$.', '$\\frac{9}{25}$', '$\\frac{3}{5} \\times \\frac{3}{5}$', c=('eq', 'Rational(3,5)**2', 'Rational(9,25)')),
    Q('A real estate agent earns $2\\%$ commission on a \\$650 000 sale. How much is the commission?', '\\$13 000', '$1\\% = 6500$', c=('eq', '650000*Rational(2,100)', '13000')),
    Q('A hose delivers 12 L per minute. How long does it take to fill a 1500 L pool? Answer in hours and minutes.', '2 h 5 min', '$1500 \\div 12 = 125$ min', c=('eq', '1500/12', '125')),
])
BON.append(B('A rectangle has an area of 48 cm² and a perimeter of 28 cm. Find its length and width.', '8 cm by 6 cm', '$l + w = 14$ and $lw = 48$', c=('py', '[(l,14-l) for l in range(1,14) if l*(14-l)==48 and l>=14-l]==[(8,6)]')))

# ---------------- Week 4 ----------------
W.append([
    Q('Evaluate $(-3)^3 - (-2)^2$', '$-31$', '$-27 - 4$', c=('eq', '(-3)**3-(-2)**2', '-31')),
    Q('\\$1000 is invested at $10\\%$ p.a. compound interest. Find its value after 2 years.', '\\$1210', '$1000 \\times 1.1 = 1100$; $1100 \\times 1.1$', s=True, c=('eq', '1000*Rational(11,10)**2', '1210')),
    Q('Evaluate $(3 \\times 10^4) \\times (2 \\times 10^3)$ in scientific notation.', '$6 \\times 10^7$', '$3 \\times 2$; $10^{4+3}$', c=('eq', '3*10**4*2*10**3', '6*10**7')),
    Q('Simplify $(3a^2b)^3$', '$27a^6b^3$', 'cube each factor', c=('eq', '(3*a**2*b)**3', '27*a**6*b**3')),
    Q('Write $\\dfrac{1}{49}$ as a power of 7.', '$7^{-2}$', '$\\frac{1}{7^2}$', c=('eq', 'Rational(7)**-2', 'Rational(1,49)')),
    Q('Simplify $\\dfrac{3x}{4} - \\dfrac{x}{2}$', '$\\frac{x}{4}$', '$\\frac{3x}{4} - \\frac{2x}{4}$', c=('eq', '3*x/4-x/2', 'x/4')),
    Q('Expand $(x - 5)^2$', '$x^2 - 10x + 25$', '$(x - 5)(x - 5)$', s=True, c=('eq', 'expand((x-5)**2)', 'x**2-10*x+25')),
    Q('Factorise $20m - 5m^2$', '$5m(4 - m)$', 'HCF = $5m$', c=('fac', '20*m-5*m**2', '5*m*(4-m)')),
    Q('Solve $x^2 = 64$', '$x = 8$ or $x = -8$', '$\\pm\\sqrt{64}$', c=('solve', 'x**2', '64', 'x', ['8', '-8'])),
    Q('A taxi charges \\$3.60 plus \\$2.20 per km. A trip cost \\$47.60. How long was it?', '20 km', '$2.2d = 44$', c=('solve', 'Rational(18,5)+Rational(11,5)*d', 'Rational(238,5)', 'd', ['20'])),
    Q('A 13 m rope runs from the top of a vertical pole to a peg 5 m from its base. How tall is the pole?', '12 m', '$h^2 = 169 - 25 = 144$', c=('eq', 'sqrt(13**2-5**2)', '12')),
    Q('From 30 m away, the angle of elevation of the top of a tree is $40^\\circ$. Use $\\tan 40^\\circ \\approx 0.84$ to find its height.', '25.2 m', '$h = 30 \\times 0.84$', s=True,
      d=D.right_triangle(30 * t40, 30, 'h', '30 m', '', theta='base', tlabel='40°'), c=('py', 'abs(30*0.84-25.2)<1e-9 and abs(30*tan(rad(40))-25.2)<0.1')),
    Q('Find the surface area of a closed cylinder with radius 3 cm and height 5 cm, in terms of $\\pi$.', '$48\\pi$ cm²', '$2\\pi(9) + 2\\pi(3)(5) = 18\\pi + 30\\pi$', c=('eq', '2*pi*3**2+2*pi*3*5', '48*pi')),
    Q('Find the volume of a cone with radius 3 cm and height 10 cm, in terms of $\\pi$.', '$30\\pi$ cm³', '$\\frac{1}{3} \\times \\pi \\times 9 \\times 10$', s=True, c=('eq', 'Rational(1,3)*pi*9*10', '30*pi')),
    Q('$M(4,\\ 1)$ is the midpoint of $AB$, and $A$ is $(1,\\ -3)$. Find $B$.', '$B(7,\\ 5)$', '$x$: $1 \\to 4 \\to 7$; $y$: $-3 \\to 1 \\to 5$', c=('py', '((1+7)/2,(-3+5)/2)==(4,1)')),
    Q('Find the equation of the line through $(0,\\ 2)$ and $(3,\\ 11)$.', '$y = 3x + 2$', '$m = \\frac{11 - 2}{3 - 0} = 3$, $c = 2$', c=('py', '3*3+2==11 and 3*0+2==2')),
    Q('Find the range and the mode of $15,\\ 18,\\ 12,\\ 18,\\ 21,\\ 14,\\ 18$.', 'range 9, mode 18', 'range $21 - 12$', c=('py', 'max(L)-min(L)==9 and max(set(L),key=L.count)==18', {'L': [15, 18, 12, 18, 21, 14, 18]})),
    Q('A coin is tossed and a die is rolled. Find $P(\\text{head and a } 6)$.', '$\\frac{1}{12}$', '$\\frac{1}{2} \\times \\frac{1}{6}$', c=('eq', 'Rational(1,2)*Rational(1,6)', 'Rational(1,12)')),
    Q('Ella’s salary is \\$78 000 a year. Find her fortnightly pay. (1 year = 26 fortnights)', '\\$3000', '$78\\,000 \\div 26$', c=('eq', '78000/26', '3000')),
    Q('A car travels 150 km in 1 hour 40 minutes. Find its average speed in km/h.', '90 km/h', '$150 \\div 1\\frac{2}{3} = 150 \\times \\frac{3}{5}$', c=('eq', '150/Rational(5,3)', '90')),
])
BON.append(B('$2^x = 32$ and $3^y = \\frac{1}{9}$. Find $x + y$.', '$3$', '$x = 5$, $y = -2$', c=('py', '2**5==32 and Rational(3)**-2==Rational(1,9) and 5+(-2)==3')))

# ---------------- Week 5 ----------------
W.append([
    Q('Evaluate $\\dfrac{4}{5} \\div \\dfrac{8}{15}$', '$1\\tfrac{1}{2}$', '$\\frac{4}{5} \\times \\frac{15}{8} = \\frac{60}{40}$', c=('eq', 'Rational(4,5)/Rational(8,15)', 'Rational(3,2)')),
    Q('A price rises from \\$80 to \\$92. Find the percentage increase.', '$15\\%$', '$\\frac{12}{80} \\times 100\\%$', c=('eq', 'Rational(12,80)*100', '15')),
    Q('Round $7.0496$ to 3 significant figures.', '$7.05$', 'the 4th figure is 9, so round up', c=('py', 'float("%.3g" % 7.0496)==7.05')),
    Q('Simplify $\\dfrac{6x^5y^2}{2x^3y}$', '$3x^2y$', '$\\frac{6}{2}$; subtract the indices', c=('eq', '6*x**5*y**2/(2*x**3*y)', '3*x**2*y')),
    Q('Evaluate $4^{-1} + 2^{-2}$', '$\\frac{1}{2}$', '$\\frac{1}{4} + \\frac{1}{4}$', c=('eq', 'Rational(4)**-1+Rational(2)**-2', 'Rational(1,2)')),
    Q('If $m = \\frac{1}{2}$ and $n = -4$, find the value of $6m - n^2$.', '$-13$', '$3 - 16$', c=('eq', '6*Rational(1,2)-(-4)**2', '-13')),
    Q('Expand and simplify $(x + 4)(x + 1) - 3x$', '$x^2 + 2x + 4$', '$x^2 + 5x + 4 - 3x$', c=('eq', 'expand((x+4)*(x+1)-3*x)', 'x**2+2*x+4')),
    Q('Factorise $-8a - 12ab$', '$-4a(2 + 3b)$', 'take out $-4a$', c=('fac', '-8*a-12*a*b', '-4*a*(2+3*b)')),
    Q('Solve $3(x - 4) - 2(x + 1) = 5$', '$x = 19$', '$3x - 12 - 2x - 2 = 5$, $x - 14 = 5$', c=('solve', '3*(x-4)-2*(x+1)', '5', 'x', ['19'])),
    Q('Make $r$ the subject of $C = 2\\pi r$.', '$r = \\dfrac{C}{2\\pi}$', 'divide both sides by $2\\pi$', s=True, c=('solve', '2*pi*r', 'P', 'r', ['P/(2*pi)'])),
    Q('Is a triangle with sides 9 cm, 40 cm and 41 cm right-angled? Explain.', 'Yes', '$81 + 1600 = 1681 = 41^2$', c=('py', '9**2+40**2==41**2')),
    Q('In a right-angled triangle, $\\tan\\theta = \\frac{5}{12}$. Find $\\sin\\theta$.', '$\\frac{5}{13}$', 'opposite 5, adjacent 12, so hypotenuse 13', c=('eq', 'Rational(5,sqrt(5**2+12**2))', 'Rational(5,13)')),
    Q('A triangular prism has right-angled triangle ends with sides 3 cm, 4 cm and 5 cm, and length 10 cm. Find its surface area.', '132 cm²', '$2 \\times 6 + (3 + 4 + 5) \\times 10 = 12 + 120$', c=('eq', '2*Rational(1,2)*3*4+(3+4+5)*10', '132')),
    Q('A cylinder has a volume of $72\\pi$ cm³ and a height of 8 cm. Find its radius.', '3 cm', '$\\pi r^2 \\times 8 = 72\\pi$, $r^2 = 9$', c=('py', 'sp.solve(sp.pi*r**2*8-72*sp.pi, r)==[-3,3]', {'sp': __import__('sympy')})),
    Q('Are $(0,\\ 1)$, $(2,\\ 5)$ and $(4,\\ 9)$ on the same straight line? Explain.', 'Yes', 'both gradients are $\\frac{4}{2} = 2$', c=('py', 'Rational(5-1,2-0)==Rational(9-5,4-2)==2')),
    Q('Find the gradient of a line perpendicular to $y = 4x - 7$.', '$-\\frac{1}{4}$', 'product of the gradients is $-1$', s=True, c=('eq', '-1/Rational(4)', '-Rational(1,4)')),
    Q('Find the five-number summary of $3,\\ 5,\\ 6,\\ 8,\\ 9,\\ 11,\\ 14$.', '3, 5, 8, 11, 14', 'min, $Q_1$, median, $Q_3$, max', s=True,
      c=('py', '(min(L), median(L[:3]), median(L), median(L[4:]), max(L))==(3,5,8,11,14)', {'L': [3, 5, 6, 8, 9, 11, 14], 'median': __import__('statistics').median})),
    Q('Two dice are rolled. Find $P(\\text{the sum is } 7)$.', '$\\frac{1}{6}$', '6 of the 36 outcomes', c=('eq', 'Rational(len([1 for i in range(1,7) for j in range(1,7) if i+j==7]),36)', 'Rational(1,6)')),
    Q('Kai is paid \\$1.20 for each box he packs. How many boxes must he pack to earn \\$480?', '400', '$480 \\div 1.20$', c=('eq', '480/Rational(6,5)', '400')),
    Q('A \\$30 000 car loses $20\\%$ of its value each year. Find its value after 2 years.', '\\$19 200', '$30\\,000 \\times 0.8 \\times 0.8$', s=True, c=('eq', '30000*Rational(8,10)**2', '19200')),
])
BON.append(B('The diagonal of a square is 10 cm long. Find the area of the square.', '50 cm²', '$s^2 + s^2 = 100$, so $s^2 = 50$', c=('solve', '2*s', '100', 's', ['50'])))

# ---------------- Week 6 ----------------
W.append([
    Q('Evaluate $-2\\tfrac{1}{3} + 4\\tfrac{1}{2}$', '$2\\tfrac{1}{6}$', '$-\\frac{14}{6} + \\frac{27}{6} = \\frac{13}{6}$', c=('eq', '-Rational(7,3)+Rational(9,2)', 'Rational(13,6)')),
    Q('After a $15\\%$ increase, the rent is \\$460 a week. What was it before?', '\\$400', '$460 \\div 1.15$', c=('eq', '460/Rational(115,100)', '400')),
    Q('Evaluate $(8 \\times 10^9) \\div (4 \\times 10^{-2})$ in scientific notation.', '$2 \\times 10^{11}$', '$8 \\div 4$; $10^{9 - (-2)}$', c=('eq', '8*Rational(10)**9/(4*Rational(10)**-2)', '2*10**11')),
    Q('Simplify $(2x^3)^4 \\div 8x^5$', '$2x^7$', '$16x^{12} \\div 8x^5$', c=('eq', '(2*x**3)**4/(8*x**5)', '2*x**7')),
    Q('Write $0.0001$ as a power of 10.', '$10^{-4}$', '$\\frac{1}{10\\,000}$', c=('eq', 'Rational(10)**-4', 'Rational(1,10000)')),
    Q('If $x = -\\frac{1}{2}$, find the value of $4x^2 - 2x + 1$.', '$3$', '$1 + 1 + 1$', c=('eq', '4*Rational(-1,2)**2-2*Rational(-1,2)+1', '3')),
    Q('Expand $(3x - 2)^2$', '$9x^2 - 12x + 4$', '$(3x)^2 - 2(3x)(2) + 2^2$', s=True, c=('eq', 'expand((3*x-2)**2)', '9*x**2-12*x+4')),
    Q('Factorise $x^2 - 2x - 15$', '$(x - 5)(x + 3)$', '$-5 \\times 3 = -15$, $-5 + 3 = -2$', s=True, c=('fac', 'x**2-2*x-15', '(x-5)*(x+3)')),
    Q('Solve $x^2 - 5x + 6 = 0$', '$x = 2$ or $x = 3$', '$(x - 2)(x - 3) = 0$', s=True, c=('solve', 'x**2-5*x+6', '0', 'x', ['2', '3'])),
    Q('Hiring a hall costs $C = 200 + 15n$ dollars for $n$ guests. How many guests can come for \\$1100?', '60', '$15n = 900$', c=('solve', '200+15*n', '1100', 'n', ['60'])),
    Q('An isosceles triangle has equal sides 13 cm and a base of 10 cm. Find its perpendicular height.', '12 cm', 'half the base is 5: $h^2 = 169 - 25$', c=('eq', 'sqrt(13**2-5**2)', '12')),
    Q('A boat sails 10 km due east, then 10 km due south. Find the true bearing of the boat from its start.', '$135^\\circ$T', 'south-east: halfway between $090^\\circ$ and $180^\\circ$', s=True, c=('py', 'abs((90 - __import__("math").degrees(__import__("math").atan2(-10,10))) % 360 - 135)<1e-9')),
    Q('Find the surface area of a sphere with radius 3 cm, in terms of $\\pi$.', '$36\\pi$ cm²', '$4\\pi r^2 = 4\\pi \\times 9$', s=True, c=('eq', '4*pi*9', '36*pi')),
    Q('A cylindrical hole of radius 1 cm is drilled right through a cube with edges 4 cm long. Find the volume left, in terms of $\\pi$.', '$(64 - 4\\pi)$ cm³', '$4^3 - \\pi \\times 1^2 \\times 4$', c=('eq', '4**3-pi*1**2*4', '64-4*pi')),
    Q('The interval from $(-3,\\ k)$ to $(5,\\ 7)$ has gradient $\\frac{1}{2}$. Find $k$.', '$k = 3$', '$\\frac{7 - k}{8} = \\frac{1}{2}$', c=('solve', '(7-k)/8', 'Rational(1,2)', 'k', ['3'])),
    Q('Find the point where the lines $2x + y = 10$ and $y = x + 1$ meet.', '$(3,\\ 4)$', '$2x + x + 1 = 10$, $x = 3$', s=True, c=('py', '2*3+4==10 and 4==3+1')),
    Q('The mean of 6 scores is 15. A seventh score is added and the mean becomes 16. Find the seventh score.', '22', '$7 \\times 16 - 6 \\times 15 = 112 - 90$', c=('eq', '7*16-6*15', '22')),
    Q('A box holds 4 red and 6 blue pens. Two are taken without replacement. Find $P(\\text{both red})$.', '$\\frac{2}{15}$', '$\\frac{4}{10} \\times \\frac{3}{9} = \\frac{12}{90}$', c=('eq', 'Rational(4,10)*Rational(3,9)', 'Rational(2,15)')),
    Q('Zoe earns \\$1200 a week and pays \\$180 tax. What percentage of her pay is tax?', '$15\\%$', '$\\frac{180}{1200} \\times 100\\%$', c=('eq', 'Rational(180,1200)*100', '15')),
    Q('A tank 2 m long, 1 m wide and 1.2 m high is filled at 40 L per minute. How long does it take to fill?', '1 hour', '$2.4 \\text{ m}^3 = 2400$ L; $2400 \\div 40 = 60$ min', c=('eq', '2*1*1.2*1000/40', '60')),
])
BON.append(B('The product of two consecutive whole numbers is 132. Find them.', '11 and 12', '$n(n + 1) = 132$', c=('py', '[n for n in range(1,100) if n*(n+1)==132]==[11]')))

BK['weeks'] = W
BK['bonus'] = BON

BK['hints'] = [
    ('Number', ['Increase by $12\\%$: $\\times 1.12$ · decrease by $35\\%$: $\\times 0.65$',
                'Percentage change $= \\dfrac{\\text{change}}{\\text{original}} \\times 100\\%$',
                'Significant figures start at the first non-zero digit',
                'Scientific notation: $a \\times 10^n$ with $1 \\le a < 10$']),
    ('Indices', ['$a^m \\times a^n = a^{m+n}$ · $a^m \\div a^n = a^{m-n}$',
                 '$(a^m)^n = a^{mn}$ · $(ab)^n = a^n b^n$ · $a^0 = 1$',
                 '$a^{-n} = \\dfrac{1}{a^n}$, e.g. $2^{-3} = \\frac{1}{8}$']),
    ('Algebra', ['Fractions: use a common denominator, e.g. $\\frac{2a}{3} = \\frac{4a}{6}$',
                 '$(a + b)(c + d) = ac + ad + bc + bd$',
                 '<span class="star">★</span> $(a - b)^2 = a^2 - 2ab + b^2$',
                 '<span class="star">★</span> $x^2 + bx + c = (x + p)(x + q)$ where $pq = c$, $p + q = b$']),
    ('Equations & formulas', ['Expand brackets, collect the unknowns on one side, then solve',
                              '$x^2 = 64 \\Rightarrow x = \\pm 8$',
                              '<span class="star">★</span> Change the subject: undo operations in reverse order',
                              '<span class="star">★</span> $(x - 2)(x - 3) = 0 \\Rightarrow x = 2$ or $x = 3$']),
    ('Measurement & trig', ['$c^2 = a^2 + b^2$ · $\\sin\\theta = \\frac{O}{H}$, $\\cos\\theta = \\frac{A}{H}$, $\\tan\\theta = \\frac{O}{A}$',
                            'Surface area: add the areas of all faces',
                            'Closed cylinder $SA = 2\\pi r^2 + 2\\pi rh$ · $V = \\pi r^2 h$',
                            '<span class="star">★</span> Cone $V = \\frac{1}{3}\\pi r^2 h$ · sphere $SA = 4\\pi r^2$',
                            '<span class="star">★</span> Elevation: measured up from the horizontal; bearings clockwise from north']),
    ('Coordinate geometry', ['$m = \\dfrac{y_2 - y_1}{x_2 - x_1}$ · midpoint $\\left(\\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2}\\right)$',
                             'Length: $d^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2$',
                             '$y = mx + c$: $m$ = gradient, $c$ = $y$-intercept',
                             '<span class="star">★</span> Perpendicular lines: $m_1 \\times m_2 = -1$']),
    ('Data & chance', ['Mean = total ÷ count · median: middle value in order',
                       'Range = highest − lowest',
                       'Independent events: $P(A \\text{ and } B) = P(A) \\times P(B)$',
                       'Without replacement: the second fraction changes',
                       '<span class="star">★</span> Five-number summary: min, $Q_1$, median, $Q_3$, max']),
    ('Money & context', ['Weekly pay = salary ÷ 52 · fortnightly = ÷ 26',
                         'Overtime: time-and-a-half $= 1.5 \\times$ rate',
                         'Commission: a percentage of sales',
                         '<span class="star">★</span> Compound interest: $\\times (1 + r)$ each year; depreciation: $\\times (1 - r)$']),
]
