"""Year 10 Standard -> Year 11 Mathematics Standard (Stage 5 revision, Stage 6 preview)."""
import math
from qlib import Q, B, xy, stemleaf
import diagrams as D

BK = dict(
    key='b5',
    file='Yr10_Standard_Summer_Holiday_Ready_for_Yr11_Standard_Revision_Booklet',
    kicker='YEAR 10 STANDARD → YEAR 11 MATHEMATICS STANDARD',
    ready='Ready for Year 11',
    intro='Six weeks. Twenty questions a week. Every Year 10 skill that Year 11 Mathematics Standard builds on – mixed together so it sticks.',
    star_text='Year 11 preview (Stage 6 Standard)',
    pattern='Question 1 is always number and rounding, question 11 is always Pythagoras, and so on. If the same number keeps going wrong, that is the skill to revise before Year 11.',
    groups=[('Number', '', [1, 2, 3]), ('Algebra', '', [4, 5, 6]), ('Equations', '', [7, 8]),
            ('Linear', '', [9, 10]), ('Measurement', '', [11, 12, 13, 14, 15]), ('Money', '', [16, 17]),
            ('Data & chance', '', [18, 19]), ('In context', '', [20])],
    strands={1: 'Number & rounding', 2: 'Percentages', 3: 'Rates & ratios', 4: 'Expand & factorise', 5: 'Substitute into formulas',
             6: 'Change the subject', 7: 'Equations', 8: 'Equations from words', 9: 'Gradient & lines', 10: 'Linear models',
             11: 'Pythagoras', 12: 'Trigonometry', 13: 'Area & surface area', 14: 'Volume & capacity', 15: 'Units & error',
             16: 'Earning money', 17: 'Interest & depreciation', 18: 'Data', 19: 'Probability', 20: 'Problem solving'},
    rules=['<b>No calculator.</b> Leave answers exact (e.g. $24\\pi$) unless asked to round. Trig questions give you any value you need.',
           '<b>Show working</b> in the space under each question.',
           '<b>Mark it yourself</b> using the answers at the back (pages 10–12). Each answer has a line of working to help you find a mistake.',
           '<b>Fix it.</b> Redo anything you got wrong a day or two later, without looking.',
           '<span class="star">★</span> questions preview Year 11 Mathematics Standard (Stage 6). Have a go – they are the ones that will help most in Term 1.',
           '<b>Stuck?</b> The hints page (page 9) has the key facts and formulas.'],
    first_up='<b>First up in Year 11 Mathematics Standard:</b> formulas and equations, linear relationships, earning and managing money, applications of measurement, time and location, networks, and data analysis. Every one of them starts from the skills in these six pages.',
    outcomes='Revises MA5-FIN-C-01, MA5-FIN-C-02, MA5-ALG-C-01, MA5-ALG-P-01, MA5-EQU-C-01, MA5-EQU-P-02, MA5-LIN-C-01, MA5-LIN-C-02, MA5-RAT-P-01, MA5-MAG-C-01, MA5-TRG-C-01, MA5-TRG-C-02, MA5-TRG-P-01, MA5-ARE-C-01, MA5-ARE-P-01, MA5-VOL-C-01, MA5-VOL-P-01, MA5-DAT-C-01, MA5-DAT-C-02, MA5-PRO-C-01, with MA4-PYT-C-01. <span class="star">★</span> Year 11 preview: Mathematics Standard 11–12 (2024) focus areas Time and location; Networks, paths and trees; Earning money; Managing money.',
)

W, BON = [], []
r = math.radians

# ---------------- Week 1 ----------------
W.append([
    Q('Round $3.4786$ to 2 decimal places.', '$3.48$', 'third decimal is 8, so round up', c=('eq', 'round(3.4786,2)', '3.48')),
    Q('Find $12.5\\%$ of \\$640.', '\\$80', '$12.5\\% = \\frac{1}{8}$', c=('eq', '640*Rational(125,1000)', '80')),
    Q('Simplify the ratio $45 : 60$', '$3 : 4$', 'divide both parts by 15', c=('py', '__import__("math").gcd(45,60)==15')),
    Q('Expand and simplify $4(x - 3) - 2(x - 5)$', '$2x - 2$', '$4x - 12 - 2x + 10$', c=('eq', 'expand(4*(x-3)-2*(x-5))', '2*x-2')),
    Q('$v = u + at$. Find $v$ when $u = 5$, $a = -2$ and $t = 3$.', '$v = -1$', '$5 + (-6)$', c=('eq', '5+(-2)*3', '-1')),
    Q('Make $x$ the subject of $y = 3x - 6$.', '$x = \\dfrac{y + 6}{3}$', 'add 6, then divide by 3', c=('solve', '3*x-6', 'y', 'x', ['(y+6)/3'])),
    Q('Solve $6x - 7 = 2x + 9$', '$x = 4$', '$4x = 16$', c=('solve', '6*x-7', '2*x+9', 'x', ['4'])),
    Q('Three times a number, decreased by 4, is 17. Find the number.', '7', '$3n - 4 = 17$', c=('solve', '3*n-4', '17', 'n', ['7'])),
    Q('State the gradient and $y$-intercept of $y = 5 - 2x$.', '$m = -2$, $c = 5$', 'rewrite as $y = -2x + 5$', c=('man', 'y=-2x+5')),
    Q('A plumber charges \\$90 call-out plus \\$70 an hour. Write a formula for the cost $C$ of an $h$-hour job, and find the cost of a 3-hour job.', '$C = 90 + 70h$; \\$300', '$90 + 210$', c=('eq', '90+70*3', '300')),
    Q('Find $c$. (cm)', '17 cm', '$c^2 = 64 + 225 = 289$', d=D.right_triangle(8, 15, '8', '15', 'c'), c=('eq', 'sqrt(8**2+15**2)', '17')),
    Q('Write $\\cos\\theta$ as a fraction in simplest form.', '$\\cos\\theta = \\frac{4}{5}$', '$\\frac{\\text{adjacent}}{\\text{hypotenuse}} = \\frac{12}{15}$', d=D.right_triangle(9, 12, '9', '12', '15', theta='base'), c=('eq', 'Rational(12,15)', 'Rational(4,5)')),
    Q('Find the area of a trapezium with parallel sides 8 m and 12 m and perpendicular height 5 m.', '50 m²', '$\\frac{5}{2}(8 + 12)$', c=('eq', 'Rational(5,2)*(8+12)', '50')),
    Q('A tank is 3 m by 2 m by 1.5 m. Find its capacity in kilolitres. ($1 \\text{ m}^3 = 1$ kL)', '9 kL', '$3 \\times 2 \\times 1.5 = 9 \\text{ m}^3$', c=('eq', '3*2*1.5', '9')),
    Q('Convert 3.6 m² to cm².', '36 000 cm²', '$1 \\text{ m}^2 = 10\\,000 \\text{ cm}^2$', c=('eq', '3.6*10000', '36000')),
    Q('Mai earns \\$26.50 an hour. Find her pay for 20 hours.', '\\$530', '$20 \\times 26.50$', c=('eq', '20*26.5', '530')),
    Q('Find the simple interest on \\$3000 at $4\\%$ p.a. for 5 years.', '\\$600', '$I = 3000 \\times 0.04 \\times 5$', c=('eq', '3000*Rational(4,100)*5', '600')),
    Q('Find the mean of $23,\\ 27,\\ 31,\\ 25,\\ 29,\\ 33$.', '$28$', '$168 \\div 6$', c=('eq', 'Rational(23+27+31+25+29+33,6)', '28')),
    Q('A card is drawn at random from cards numbered 1 to 20. Find $P(\\text{multiple of 5})$.', '$\\frac{1}{5}$', '5, 10, 15, 20: $\\frac{4}{20}$', c=('eq', 'Rational(4,20)', 'Rational(1,5)')),
    Q('In winter, Sydney time is 2 hours ahead of Perth time. A flight leaves Perth at 11:30 am (Perth time) and takes 4 h 15 min. What is the time in Sydney when it lands?', '5:45 pm', 'lands 3:45 pm Perth time; add 2 hours', s=True, c=('py', '(11*60+30+4*60+15+120)==17*60+45')),
])
BON.append(B('A number is doubled, then 5 is added, then the result is tripled. The answer is 51. Find the number.', '6', '$3(2n + 5) = 51$, $2n + 5 = 17$', c=('solve', '3*(2*n+5)', '51', 'n', ['6'])))

# ---------------- Week 2 ----------------
W.append([
    Q('Round $0.006\\,82$ to 2 significant figures.', '$0.0068$', 'first significant figure is 6; next digit 2 rounds down', c=('py', 'float("%.2g" % 0.00682)==0.0068')),
    Q('A \\$1200 TV is reduced by $15\\%$. Find the sale price.', '\\$1020', '$15\\%$ of 1200 = 180', c=('eq', '1200*Rational(85,100)', '1020')),
    Q('A car uses 24 L of fuel to travel 300 km. Find its fuel consumption in L/100 km.', '8 L/100 km', '$\\frac{24}{300} \\times 100$', c=('eq', 'Rational(24,300)*100', '8')),
    Q('Expand $(x + 4)(x - 6)$', '$x^2 - 2x - 24$', '$x^2 - 6x + 4x - 24$', c=('eq', 'expand((x+4)*(x-6))', 'x**2-2*x-24')),
    Q('Use $d = st$ to find the distance travelled at 85 km/h for 2.5 hours.', '212.5 km', '$85 \\times 2.5$', c=('eq', '85*2.5', '212.5')),
    Q('Make $t$ the subject of $v = u + at$.', '$t = \\dfrac{v - u}{a}$', 'subtract $u$, then divide by $a$', c=('solve', 'u+a*t', 'v', 't', ['(v-u)/a'])),
    Q('Solve $\\dfrac{x - 4}{3} = 5$', '$x = 19$', '$x - 4 = 15$', c=('solve', '(x-4)/3', '5', 'x', ['19'])),
    Q('Tom is 5 years older than Ana. Their ages add to 39. How old is Ana?', '17', '$a + (a + 5) = 39$', c=('solve', 'a+(a+5)', '39', 'a', ['17'])),
    Q('Find the gradient of the line through $(1,\\ 3)$ and $(5,\\ 11)$.', '$2$', '$\\frac{11 - 3}{5 - 1} = \\frac{8}{4}$', c=('eq', 'Rational(11-3,5-1)', '2')),
    Q('A \\$900 phone loses \\$150 of value each year. Write a rule for its value $V$ after $n$ years. When is it worth nothing?', '$V = 900 - 150n$; after 6 years', '$150n = 900$', c=('solve', '900-150*n', '0', 'n', ['6'])),
    Q('Find $x$. (cm)', '24 cm', '$x^2 = 625 - 49 = 576$', d=D.right_triangle(7, 24, '7', 'x', '25'), c=('eq', 'sqrt(25**2-7**2)', '24')),
    Q('Use $\\sin 30^\\circ = 0.5$ to find $x$. (cm)', '$x = 8$ cm', '$x = 16 \\times 0.5$', d=D.right_triangle(16 * math.sin(r(30)), 16 * math.cos(r(30)), 'x', '', '16', theta='base', tlabel='30°'), c=('eq', '16*sin(rad(30))', '8')),
    Q('Find the area of a circle with diameter 12 cm, in terms of $\\pi$.', '$36\\pi$ cm²', '$r = 6$: $\\pi \\times 36$', c=('eq', 'pi*6**2', '36*pi')),
    Q('Find the volume of a cylinder with radius 5 cm and height 8 cm, in terms of $\\pi$.', '$200\\pi$ cm³', '$\\pi \\times 25 \\times 8$', c=('eq', 'pi*25*8', '200*pi')),
    Q('A length is measured as 24 cm, to the nearest centimetre. What is the absolute error?', '$\\pm 0.5$ cm', 'half the precision of 1 cm', c=('eq', 'Rational(1,2)*1', 'Rational(1,2)')),
    Q('Raj’s normal rate is \\$32 an hour. Find his pay for 38 normal hours and 5 hours at time-and-a-half.', '\\$1456', '$38 \\times 32 + 5 \\times 48 = 1216 + 240$', c=('eq', '38*32+5*48', '1456')),
    Q('\\$5000 is invested at $6\\%$ p.a. compound interest. Find its value after 2 years.', '\\$5618', '$5000 \\times 1.06 = 5300$; $5300 \\times 1.06$', c=('eq', '5000*Rational(106,100)**2', '5618')),
    Q('Find the median of $14,\\ 9,\\ 21,\\ 17,\\ 12,\\ 16,\\ 19,\\ 11$.', '$15$', '9, 11, 12, <b>14, 16</b>, 17, 19, 21', c=('py', 'median(L)==15', {'L': [14, 9, 21, 17, 12, 16, 19, 11], 'median': __import__('statistics').median})),
    Q('Two dice are rolled. Find $P(\\text{the sum is } 10)$.', '$\\frac{1}{12}$', '(4, 6), (5, 5), (6, 4): $\\frac{3}{36}$', c=('eq', 'Rational(len([1 for i in range(1,7) for j in range(1,7) if i+j==10]),36)', 'Rational(1,12)')),
    Q('The numbers show travel times in minutes. Find the shortest path from A to E and its length.', 'A–C–B–D–E, 10 min', '$2 + 1 + 5 + 2$; A–B–D–E takes 11', s=True,
      d=D.network({'A': (0, 1), 'B': (1.3, 0), 'C': (1.3, 2), 'D': (2.6, 0.5), 'E': (3.7, 1.5)},
                  [('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 1), ('B', 'D', 5), ('C', 'D', 8), ('C', 'E', 10), ('D', 'E', 2)]),
      c=('py', 'shortest()==10', {'shortest': lambda: __import__('qcheck').dijkstra({('A', 'B'): 4, ('A', 'C'): 2, ('B', 'C'): 1, ('B', 'D'): 5, ('C', 'D'): 8, ('C', 'E'): 10, ('D', 'E'): 2}, 'A', 'E')})),
])
BON.append(B('A rectangle has a perimeter of 34 cm and a diagonal of 13 cm. Find its length and width.', '12 cm by 5 cm', '$l + w = 17$ and $l^2 + w^2 = 169$', c=('py', '[(l,17-l) for l in range(1,17) if l*l+(17-l)**2==169 and l>17-l]==[(12,5)]')))

# ---------------- Week 3 ----------------
W.append([
    Q('Write $0.000\\,032$ in scientific notation.', '$3.2 \\times 10^{-5}$', 'move the decimal point 5 places right', c=('eq', 'Rational(32,10)*Rational(1,10**5)', 'Rational(32,1000000)')),
    Q('A house bought for \\$640 000 sells for \\$720 000. Find the profit as a percentage of the cost.', '$12.5\\%$', '$\\frac{80\\,000}{640\\,000} = \\frac{1}{8}$', c=('eq', 'Rational(80000,640000)*100', 'Rational(25,2)')),
    Q('Share \\$900 in the ratio $2 : 3 : 4$.', '\\$200, \\$300, \\$400', '9 parts: \\$100 each', c=('py', '[900*k//9 for k in (2,3,4)]==[200,300,400]')),
    Q('Factorise $6x^2 - 9x$', '$3x(2x - 3)$', 'HCF = $3x$', c=('fac', '6*x**2-9*x', '3*x*(2*x-3)')),
    Q('$S = \\frac{n}{2}(a + l)$. Find $S$ when $n = 20$, $a = 3$ and $l = 41$.', '$S = 440$', '$10 \\times 44$', c=('eq', 'Rational(20,2)*(3+41)', '440')),
    Q('Make $r$ the subject of $A = \\pi r^2$ (where $r > 0$).', '$r = \\sqrt{\\dfrac{A}{\\pi}}$', 'divide by $\\pi$, then take the square root', c=('py', 'sp.simplify(sp.pi*sp.sqrt(P/sp.pi)**2-P)==0')),
    Q('Solve $3(2x + 1) = 4(x + 5)$', '$x = 8.5$', '$6x + 3 = 4x + 20$, $2x = 17$', c=('solve', '3*(2*x+1)', '4*(x+5)', 'x', ['Rational(17,2)'])),
    Q('Adult tickets cost \\$25 and child tickets \\$15. 40 tickets were sold for \\$800. How many were adult tickets?', '20', '$25a + 15(40 - a) = 800$, $10a = 200$', c=('solve', '25*a+15*(40-a)', '800', 'a', ['20'])),
    Q('Find the equation of the line with gradient 3 that passes through $(2,\\ 1)$.', '$y = 3x - 5$', '$1 = 3(2) + c$', c=('py', '3*2-5==1')),
    Q('A café’s weekly costs are $C = 200 + 4n$ and its income is $R = 9n$, where $n$ is the number of coffees. How many coffees must it sell to break even?', '40', '$9n = 200 + 4n$, $5n = 200$', c=('solve', '9*n', '200+4*n', 'n', ['40'])),
    Q('A ramp rises 1.2 m over a horizontal distance of 3.5 m. How long is the ramp?', '3.7 m', '$\\sqrt{1.44 + 12.25} = \\sqrt{13.69}$', c=('eq', 'sqrt(Rational(144,100)+Rational(1225,100))', 'Rational(37,10)')),
    Q('From 50 m away, the angle of elevation of the top of a building is $32^\\circ$. Use $\\tan 32^\\circ \\approx 0.62$ to find its height.', '$\\approx 31$ m', '$h = 50 \\times 0.62$', d=D.right_triangle(50 * math.tan(r(32)), 50, 'h', '50 m', '', theta='base', tlabel='32°'),
      c=('py', 'abs(50*0.62-31)<1e-9 and abs(50*tan(rad(32))-31)<0.3')),
    Q('Find the surface area of a closed cylinder with radius 4 cm and height 6 cm, in terms of $\\pi$.', '$80\\pi$ cm²', '$2\\pi(16) + 2\\pi(4)(6) = 32\\pi + 48\\pi$', c=('eq', '2*pi*16+2*pi*4*6', '80*pi')),
    Q('Find the volume of a cone with radius 3 cm and height 8 cm, in terms of $\\pi$.', '$24\\pi$ cm³', '$\\frac{1}{3} \\times \\pi \\times 9 \\times 8$', c=('eq', 'Rational(1,3)*pi*9*8', '24*pi')),
    Q('A 50 m length has an absolute error of 0.5 m. Find the percentage error.', '$1\\%$', '$\\frac{0.5}{50} \\times 100\\%$', c=('eq', 'Rational(1,2)/50*100', '1')),
    Q('Ali earns \\$450 a week plus $3\\%$ commission on sales. Find his pay in a week with \\$12 000 of sales.', '\\$810', '$450 + 360$', c=('eq', '450+12000*Rational(3,100)', '810')),
    Q('A \\$24 000 car depreciates by $25\\%$ a year. Find its value after 2 years.', '\\$13 500', '$24\\,000 \\times 0.75 = 18\\,000$; $\\times 0.75$', c=('eq', '24000*Rational(3,4)**2', '13500')),
    Q('Find the interquartile range of $4,\\ 7,\\ 8,\\ 10,\\ 12,\\ 15,\\ 18,\\ 20,\\ 21$.', '$11.5$', '$Q_1 = 7.5$, $Q_3 = 19$', c=('py', 'median(L[4+1:])-median(L[:4])==11.5', {'L': [4, 7, 8, 10, 12, 15, 18, 20, 21], 'median': __import__('statistics').median})),
    Q('A bag holds 4 red and 6 blue balls. Two are drawn without replacement. Find $P(\\text{both blue})$.', '$\\frac{1}{3}$', '$\\frac{6}{10} \\times \\frac{5}{9} = \\frac{30}{90}$', c=('eq', 'Rational(6,10)*Rational(5,9)', 'Rational(1,3)')),
    Q('Melbourne is at about $145^\\circ$E and London at $0^\\circ$. Using $15^\\circ$ of longitude = 1 hour, find the time difference.', '9 h 40 min', '$145 \\div 15 = 9\\frac{2}{3}$ h', s=True, c=('eq', 'Rational(145,15)*60', '580')),
])
BON.append(B('Find the whole number $n$ for which $n^2 + (n + 1)^2 = 145$.', '$n = 8$', '$64 + 81 = 145$', c=('py', '[k for k in range(0,20) if k**2+(k+1)**2==145]==[8]')))

# ---------------- Week 4 ----------------
W.append([
    Q('Evaluate $(4.8 \\times 10^6) \\div (1.2 \\times 10^2)$ in scientific notation.', '$4 \\times 10^4$', '$4.8 \\div 1.2 = 4$; $10^{6 - 2}$', c=('eq', 'Rational(48,10)*10**6/(Rational(12,10)*10**2)', '4*10**4')),
    Q('A price including $10\\%$ GST is \\$660. Find the price before GST.', '\\$600', '$660 \\div 1.1$', c=('eq', '660/Rational(11,10)', '600')),
    Q('Convert 90 km/h to metres per second.', '25 m/s', '$90\\,000 \\div 3600$', c=('eq', '90000/3600', '25')),
    Q('Expand $(2x - 3)^2$', '$4x^2 - 12x + 9$', '$(2x)^2 - 2(2x)(3) + 3^2$', c=('eq', 'expand((2*x-3)**2)', '4*x**2-12*x+9')),
    Q('Use $A = P(1 + r)^n$ to find $A$ when $P = 2000$, $r = 0.05$ and $n = 2$.', '$A = 2205$', '$2000 \\times 1.1025$', c=('eq', '2000*Rational(105,100)**2', '2205')),
    Q('Make $h$ the subject of $V = \\frac{1}{3}\\pi r^2 h$.', '$h = \\dfrac{3V}{\\pi r^2}$', 'multiply by 3, then divide by $\\pi r^2$', c=('solve', 'Rational(1,3)*pi*r**2*h', 'P', 'h', ['3*P/(pi*r**2)'])),
    Q('Solve $5 - 2x = 3(x - 5)$', '$x = 4$', '$5 - 2x = 3x - 15$, $20 = 5x$', c=('solve', '5-2*x', '3*(x-5)', 'x', ['4'])),
    Q('Two numbers add to 50 and differ by 12. Find them.', '31 and 19', '$2x = 62$', c=('py', '31+19==50 and 31-19==12')),
    Q('Are the lines $y = 2x + 1$ and $y = -\\frac{1}{2}x + 4$ perpendicular? Explain.', 'Yes', '$2 \\times (-\\frac{1}{2}) = -1$', c=('eq', '2*(-Rational(1,2))', '-1')),
    Q('A 30 cm candle burns down 2.5 cm each hour. Write a formula for its height $h$ after $t$ hours. When will it be 10 cm tall?', '$h = 30 - 2.5t$; after 8 hours', '$2.5t = 20$', c=('solve', '30-Rational(5,2)*t', '10', 't', ['8'])),
    Q('A TV screen is 120 cm wide and 50 cm high. Find the length of its diagonal.', '130 cm', '$\\sqrt{14\\,400 + 2500} = \\sqrt{16\\,900}$', d=D.rect_diag(120, 50, '120', '50', 'd'), c=('eq', 'sqrt(120**2+50**2)', '130')),
    Q('Use the cosine rule to find $c$. ($\\cos 60^\\circ = 0.5$)', '$c = 7$', '$c^2 = 9 + 64 - 2(3)(8)(0.5) = 49$', d=D.oblique_triangle(8, 3, 60, '8', '3', 'c', '60°'), c=('eq', 'sqrt(3**2+8**2-2*3*8*cos(rad(60)))', '7')),
    Q('Find the area of a sector with radius 6 cm and angle $60^\\circ$, in terms of $\\pi$.', '$6\\pi$ cm²', '$\\frac{60}{360} \\times \\pi \\times 36$', c=('eq', 'Rational(60,360)*pi*36', '6*pi')),
    Q('Find the volume of a sphere with radius 3 cm, in terms of $\\pi$.', '$36\\pi$ cm³', '$\\frac{4}{3} \\times \\pi \\times 27$', c=('eq', 'Rational(4,3)*pi*27', '36*pi')),
    Q('A length is 7.4 cm, measured to the nearest millimetre. Between what two values does the true length lie?', '7.35 cm and 7.45 cm', 'absolute error $= 0.05$ cm', c=('py', 'abs(7.4-0.05-7.35)<1e-9 and abs(7.4+0.05-7.45)<1e-9')),
    Q('Raj earns \\$68 000 a year and has \\$2500 of allowable tax deductions. Find his taxable income.', '\\$65 500', '$68\\,000 - 2500$', c=('eq', '68000-2500', '65500')),
    Q('On \\$10 000 for 2 years, which earns more interest: $10\\%$ p.a. simple or $9\\%$ p.a. compound?', '10% simple (\\$2000 vs \\$1881)', '$10\\,000 \\times 1.09^2 = 11\\,881$', c=('py', '10000*0.10*2 > 10000*1.09**2-10000')),
    Q('For $3,\\ 5,\\ 5,\\ 6,\\ 8,\\ 40$, which measure of centre best describes the data? Explain.', 'the median (5.5)', 'the outlier 40 pulls the mean up to about 11', c=('py', 'median(L)==5.5 and sum(L)/6>11', {'L': [3, 5, 5, 6, 8, 40], 'median': __import__('statistics').median})),
    Q('Events $A$ and $B$ are independent, with $P(A) = 0.6$ and $P(B) = 0.5$. Find $P(A \\text{ and } B)$.', '$0.3$', '$0.6 \\times 0.5$', c=('eq', 'Rational(6,10)*Rational(1,2)', 'Rational(3,10)')),
    Q('The numbers are cable lengths in km. Find the length of the minimum spanning tree that connects every town.', '13 km', 'choose CD 2, AB 3, BC 4, DE 4', s=True,
      d=D.network({'A': (0, 0), 'B': (1.4, 0), 'C': (0.7, 1.4), 'D': (2.2, 1.6), 'E': (3.2, 0.5)},
                  [('A', 'B', 3), ('A', 'C', 5), ('B', 'C', 4), ('B', 'D', 6), ('C', 'D', 2), ('C', 'E', 7), ('D', 'E', 4)]),
      c=('py', 'mst()==13', {'mst': lambda: __import__('qcheck').mst({('A', 'B'): 3, ('A', 'C'): 5, ('B', 'C'): 4, ('B', 'D'): 6, ('C', 'D'): 2, ('C', 'E'): 7, ('D', 'E'): 4})})),
])
BON.append(B('A rectangle is $(x + 5)$ cm long and $(x - 2)$ cm wide. Its area is 30 cm². Find $x$.', '$x = 5$', '$x^2 + 3x - 40 = 0$, $(x + 8)(x - 5) = 0$; $x = -8$ gives a negative width', c=('solve', '(x+5)*(x-2)', '30', 'x', ['5', '-8'])))

# ---------------- Week 5 ----------------
W.append([
    Q('Round $26\\,849$ to 3 significant figures.', '$26\\,800$', 'the 4th figure is 4, so round down', c=('py', 'round(26849,-2)==26800')),
    Q('A salary of \\$70 000 rises by $3\\%$. Find the new salary.', '\\$72 100', '$70\\,000 \\times 1.03$', c=('eq', '70000*Rational(103,100)', '72100')),
    Q('A 1.25 L drink costs \\$2.50 and a 2 L drink costs \\$3.60. Which is the better buy?', 'the 2 L drink', '\\$2.00 per L vs \\$1.80 per L', c=('py', '3.60/2 < 2.50/1.25')),
    Q('Expand and simplify $(x + 5)(x - 5) - x(x - 2)$', '$2x - 25$', '$x^2 - 25 - x^2 + 2x$', c=('eq', 'expand((x+5)*(x-5)-x*(x-2))', '2*x-25')),
    Q('Use $F = 1.8C + 32$ to find $C$ when $F = 50$.', '$C = 10$', '$1.8C = 18$', c=('solve', 'Rational(18,10)*n+32', '50', 'n', ['10'])),
    Q('Make $b$ the subject of $P = 2(a + b)$.', '$b = \\dfrac{P}{2} - a$', 'divide by 2, then subtract $a$', c=('solve', '2*(a+b)', 'P', 'b', ['P/2-a'])),
    Q('Solve $2(3x - 1) - (x + 4) = 9$', '$x = 3$', '$6x - 2 - x - 4 = 9$, $5x = 15$', c=('solve', '2*(3*x-1)-(x+4)', '9', 'x', ['3'])),
    Q('A rectangle is 4 m longer than it is wide, and its perimeter is 48 m. Find its area.', '140 m²', 'width 10, length 14', c=('py', '[(w,w+4) for w in range(1,24) if 2*(2*w+4)==48]==[(10,14)] and 10*14==140')),
    Q('Find the $x$- and $y$-intercepts of $3x + 4y = 12$.', '$(4,\\ 0)$ and $(0,\\ 3)$', 'put $y = 0$, then $x = 0$', c=('py', '3*4+4*0==12 and 3*0+4*3==12')),
    Q('Use 1 AUD = 0.65 USD. How many US dollars is 400 AUD? How many Australian dollars is 130 USD?', '260 USD; 200 AUD', '$400 \\times 0.65$; $130 \\div 0.65$', c=('py', 'abs(400*0.65-260)<1e-9 and abs(130/0.65-200)<1e-9')),
    Q('A box is 6 cm by 8 cm by 24 cm. Find the diagonal of its 6 × 8 base, then the longest rod that fits in the box.', '10 cm; 26 cm', '$\\sqrt{36 + 64} = 10$; $\\sqrt{100 + 576} = 26$', c=('py', 'sqrt(6**2+8**2)==10 and sqrt(10**2+24**2)==26')),
    Q('In a right-angled triangle, the adjacent side is 12 and the hypotenuse is 13. Write $\\cos\\theta$ and find $\\tan\\theta$.', '$\\cos\\theta = \\frac{12}{13}$, $\\tan\\theta = \\frac{5}{12}$', 'opposite $= \\sqrt{169 - 144} = 5$', c=('eq', 'sqrt(13**2-12**2)/12', 'Rational(5,12)')),
    Q('Find the area. (m)', '88 m²', '$12 \\times 9 - 5 \\times 4 = 108 - 20$', d=D.lshape(12, 9, 5, 4, {'bottom': '12', 'left': '9', 'notch_h': '5', 'notch_v': '4'}), c=('eq', '12*9-5*4', '88')),
    Q('A pool is 25 m long, 10 m wide and 1.2 m deep. How many kilolitres does it hold?', '300 kL', '$25 \\times 10 \\times 1.2 = 300 \\text{ m}^3$', c=('eq', '25*10*1.2', '300')),
    Q('A 2 kg bag is weighed to the nearest 10 g. Find the percentage error.', '$0.25\\%$', 'absolute error 5 g; $\\frac{5}{2000} \\times 100\\%$', c=('eq', 'Rational(5,2000)*100', 'Rational(1,4)')),
    Q('Sophie earns \\$1500 a week. She takes 4 weeks’ leave with $17.5\\%$ leave loading. How much is the loading?', '\\$1050', '$17.5\\%$ of \\$6000', c=('eq', '4*1500*Rational(175,1000)', '1050')),
    Q('A \\$9000 machine loses \\$1200 of value each year (straight-line depreciation). Find its value after 4 years.', '\\$4200', '$9000 - 4 \\times 1200$', c=('eq', '9000-4*1200', '4200')),
    Q('A scatterplot of hours studied against test mark has points rising from left to right, close to a straight line. Describe the association.', 'strong, positive, linear', 'direction, strength, form', c=('man', 'description of a scatterplot')),
    Q('A coin is tossed 200 times and lands heads 92 times. Find the relative frequency of heads.', '$0.46$', '$\\frac{92}{200}$', c=('eq', 'Rational(92,200)', 'Rational(46,100)')),
    Q('Ava earns \\$860 a week. She spends $30\\%$ on rent, \\$160 on food and \\$120 on transport. How much is left?', '\\$322', '$258 + 160 + 120 = 538$', s=True, c=('eq', '860-860*Rational(3,10)-160-120', '322')),
])
BON.append(B('A \\$20 000 car loses $20\\%$ of its value each year. After how many whole years is it first worth less than \\$10 000?', '4 years', 'values: 16 000, 12 800, 10 240, 8192', c=('py', 'min(n for n in range(1,20) if 20000*0.8**n<10000)==4')))

# ---------------- Week 6 ----------------
W.append([
    Q('Evaluate $(2.4 \\times 10^{-3}) \\times (5 \\times 10^5)$ in scientific notation.', '$1.2 \\times 10^3$', '$12 \\times 10^2$', c=('eq', 'Rational(24,10)*Rational(1,1000)*5*10**5', '1200')),
    Q('After a $25\\%$ increase, a price is \\$150. Find the original price.', '\\$120', '$150 \\div 1.25$', c=('eq', '150/Rational(125,100)', '120')),
    Q('A tap fills a 2.4 kL tank at 15 L per minute. How long does it take? Answer in hours and minutes.', '2 h 40 min', '$2400 \\div 15 = 160$ min', c=('eq', '2400/15', '160')),
    Q('Factorise $x^2 - x - 20$', '$(x - 5)(x + 4)$', '$-5 \\times 4 = -20$, $-5 + 4 = -1$', c=('fac', 'x**2-x-20', '(x-5)*(x+4)')),
    Q('$A = \\frac{h}{2}(a + b)$. Find $a$ when $A = 60$, $h = 6$ and $b = 12$.', '$a = 8$', '$60 = 3(a + 12)$', c=('solve', 'Rational(6,2)*(a+12)', '60', 'a', ['8'])),
    Q('Make $r$ the subject of $V = \\frac{4}{3}\\pi r^3$.', '$r = \\sqrt[3]{\\dfrac{3V}{4\\pi}}$', 'multiply by 3, divide by $4\\pi$, then cube root', c=('py', 'sp.simplify(Rational(4,3)*sp.pi*((3*P/(4*sp.pi))**Rational(1,3))**3-P)==0')),
    Q('Solve simultaneously: $4x + 3y = 18$ and $y = 2x - 4$', '$x = 3$, $y = 2$', '$4x + 6x - 12 = 18$', c=('py', 'sp.solve([4*x+3*y-18, y-2*x+4],[x,y])=={x:3,y:2}')),
    Q('Pens cost \\$2 and notebooks \\$5. Mia buys 12 items for \\$39. How many notebooks did she buy?', '5', '$2(12 - n) + 5n = 39$, $3n = 15$', c=('solve', '2*(12-n)+5*n', '39', 'n', ['5'])),
    Q('Find the equation of the line through $(1,\\ 4)$ that is perpendicular to $y = 2x + 3$.', '$y = -\\frac{1}{2}x + \\frac{9}{2}$', 'gradient $-\\frac{1}{2}$: $4 = -\\frac{1}{2} + c$', c=('eq', '-Rational(1,2)*1+Rational(9,2)', '4')),
    Q('Electricity costs \\$1.10 a day plus 30 cents per kWh. Find the bill for 90 days in which 1200 kWh were used.', '\\$459', '$99 + 360$', c=('eq', '90*Rational(11,10)+1200*Rational(3,10)', '459')),
    Q('A cone has radius 5 cm and perpendicular height 12 cm. Find its slant height.', '13 cm', '$\\sqrt{25 + 144}$', c=('eq', 'sqrt(5**2+12**2)', '13')),
    Q('In $\\triangle ABC$, $a = 10$, $A = 30^\\circ$ and $B = 50^\\circ$. Use $\\sin 30^\\circ = 0.5$ and $\\sin 50^\\circ \\approx 0.77$ to find $b$.', '$b \\approx 15.4$', '$b = \\frac{10 \\times 0.77}{0.5}$', c=('py', 'abs(10*0.77/0.5-15.4)<1e-9 and abs(10*sin(rad(50))/sin(rad(30))-15.4)<0.1')),
    Q('A square pyramid has a base of side 10 cm, and each triangular face has a perpendicular height of 13 cm. Find its surface area.', '360 cm²', '$100 + 4 \\times \\frac{1}{2} \\times 10 \\times 13$', c=('eq', '10**2+4*Rational(1,2)*10*13', '360')),
    Q('Find the volume of a hemispherical bowl with radius 6 cm, in terms of $\\pi$.', '$144\\pi$ cm³', '$\\frac{2}{3} \\times \\pi \\times 216$', c=('eq', 'Rational(2,3)*pi*216', '144*pi')),
    Q('A field is 120 m by 80 m, each measured to the nearest metre. Find the largest possible area.', '9700.25 m²', '$120.5 \\times 80.5$', c=('eq', 'Rational(1205,10)*Rational(805,10)', 'Rational(970025,100)')),
    Q('An employer pays $12\\%$ superannuation on a \\$75 000 salary. How much super is paid in the year?', '\\$9000', '$0.12 \\times 75\\,000$', s=True, c=('eq', '75000*Rational(12,100)', '9000')),
    Q('\\$8000 is invested at $5\\%$ p.a. compound interest for 3 years. Find the interest earned.', '\\$1261', '$8400 \\to 8820 \\to 9261$', c=('eq', '8000*Rational(105,100)**3-8000', '1261')),
    Q('The mean of 8 scores is 15. A score of 29 is removed. Find the new mean.', '$13$', '$(120 - 29) \\div 7 = 91 \\div 7$', c=('eq', '(8*15-29)/7', '13')),
    Q('A die is rolled three times. Find $P(\\text{no sixes})$.', '$\\frac{125}{216}$', '$\\left(\\frac{5}{6}\\right)^3$', c=('eq', 'Rational(5,6)**3', 'Rational(125,216)')),
    Q('It is 9:00 pm Friday in Sydney (UTC+10). What time and day is it in Los Angeles (UTC−7)?', '4:00 am Friday', 'difference 17 hours: $9 \\text{ pm} - 17 \\text{ h}$', s=True, c=('py', '(21-17)==4')),
])
BON.append(B('\\$10 000 is invested for 3 years at $10\\%$ p.a. compounded yearly. How much more is this than $10\\%$ p.a. simple interest?', '\\$310 more', '$13\\,310$ vs $13\\,000$', c=('eq', '10000*Rational(11,10)**3-(10000+3*1000)', '310')))

BK['weeks'] = W
BK['bonus'] = BON

BK['hints'] = [
    ('Number', ['Sig. figs start at the first non-zero digit', 'Increase by $3\\%$: $\\times 1.03$ · price before GST $=$ price $\\div 1.1$', 'Best buy: compare the cost per unit', 'km/h to m/s: ÷ 3.6 · fuel use (L/100 km) $= \\frac{\\text{litres}}{\\text{km}} \\times 100$']),
    ('Algebra', ['Expand: multiply every term inside by the term outside', '$(a - b)^2 = a^2 - 2ab + b^2$', 'Factorise: HCF first, then $x^2 + bx + c = (x + p)(x + q)$', 'Change the subject: undo operations in reverse order']),
    ('Equations', ['Expand, collect like terms, then solve', 'Simultaneous: substitute one equation into the other', 'Worded problems: let the unknown be a letter; write an equation; check']),
    ('Linear', ['$m = \\frac{\\text{rise}}{\\text{run}}$ · $y = mx + c$', 'Parallel: equal gradients · perpendicular: $m_1 m_2 = -1$', 'Intercepts: put $x = 0$ (for $y$) and $y = 0$ (for $x$)', 'Linear model: starting value + rate × time']),
    ('Measurement', ['$c^2 = a^2 + b^2$ · $\\sin\\theta = \\frac{O}{H}$, $\\cos\\theta = \\frac{A}{H}$, $\\tan\\theta = \\frac{O}{A}$', '$\\frac{a}{\\sin A} = \\frac{b}{\\sin B}$ · $c^2 = a^2 + b^2 - 2ab\\cos C$', 'Sector $A = \\frac{\\theta}{360} \\pi r^2$ · cylinder $SA = 2\\pi r^2 + 2\\pi rh$', 'Cone $V = \\frac{1}{3}\\pi r^2 h$ · sphere $V = \\frac{4}{3}\\pi r^3$', 'Absolute error $= \\frac{1}{2}$ precision · % error $= \\frac{\\text{abs. error}}{\\text{measurement}} \\times 100\\%$']),
    ('Money', ['Overtime: time-and-a-half $= 1.5 \\times$ rate', 'Leave loading: $17.5\\%$ of holiday pay', 'Simple interest $I = Prn$ · compound $A = P(1 + r)^n$', 'Declining balance $S = V_0(1 - r)^n$ · straight line $S = V_0 - Dn$', '<span class="star">★</span> Superannuation: a percentage of salary paid by the employer']),
    ('Data & chance', ['IQR $= Q_3 - Q_1$ · outliers affect the mean most', 'Relative frequency $= \\frac{\\text{frequency}}{\\text{total}}$', 'Independent: $P(A \\text{ and } B) = P(A)P(B)$', 'Scatterplots: describe direction, strength and form']),
    ('In context', ['<span class="star">★</span> 15° of longitude = 1 hour of time', '<span class="star">★</span> Time zones: east is ahead (UTC+10 is 17 h ahead of UTC−7)', '<span class="star">★</span> Shortest path: try every route and keep the best', '<span class="star">★</span> Spanning tree: add the shortest edges, never making a loop']),
]
