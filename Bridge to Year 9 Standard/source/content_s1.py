from dsl import *
from svg import *
import math
from fractions import Fraction as Fr


def P(item, step):
    """partly worked: show the first step (LaTeX, ends with a blank)"""
    item.scaf = step
    return item


def pct(x):
    return round(x, 10)


GOLD_EXT = 'Gold: harder Stage 4 problems (no Stage 5 content)'

# ======================================================================
# LESSON 1  Number skills
# ======================================================================
L1 = dict(
    num=1, key='L1', title='Number skills',
    sub='Integers · order of operations · fractions · decimals · percentages · rounding',
    outcomes='MA4-INT-C-01 · MA4-FRC-C-01', ext=GOLD_EXT,
    book='NCM 8 Ch 2, Ch 6',
    vocab=[('integer', 'a whole number: positive, negative or zero'), ('numerator', 'the top number of a fraction'),
           ('denominator', 'the bottom number of a fraction'), ('percentage', 'a number out of 100'),
           ('round', 'give an approximate value, e.g. to 1 decimal place')],
    ideas=[
        r'<b>Integers:</b> $\times$ or $\div$ with the same signs gives a positive; different signs gives a negative. Subtracting a negative is the same as adding: $4 - (-2) = 6$.',
        r'<b>Order of operations:</b> brackets, then $\times$ and $\div$ (left to right), then $+$ and $-$ (left to right).',
        r'<b>Fractions:</b> to add or subtract, use a common denominator. To multiply, multiply tops and bottoms. To divide, flip the second fraction and multiply.',
        r'<b>Percentages:</b> $15\%$ of $60 = 0.15 \times 60 = 9$. Increase by $15\%$: $\times 1.15$. Decrease by $20\%$: $\times 0.8$.',
        r'<b>Rounding:</b> look at the next digit. $5$ or more rounds up: $3.476 \approx 3.5$.',
    ],
    examples=[
        (r'Evaluate $-6 + 4 \times (-3)$.', r'&= -6 + (-12) \\ &= -18'),
        (r'Evaluate $\tfrac{2}{3} + \tfrac{3}{4}$.', r'&= \tfrac{8}{12} + \tfrac{9}{12} \\ &= \tfrac{17}{12} = 1\tfrac{5}{12}'),
        (r'Increase $\$240$ by $15\%$.', r'&= 240 \times 1.15 \\ &= \$276'),
    ],
)
L1['pages'] = [
    [('ideas',),
     ('round', 'B'),
     ('sub', 'Evaluate.'),
     ('grid', 4, [
         S('-5+8', '3'), S('-3-6', '-9'), S('4-(-2)', '6'), S('-4*5', '-20'),
         S('-18÷(-3)', '6'), S('3+4*2', '11'), S('(3+4)*2', '14'), S('[1|4]+[2|4]', '[3|4]'),
         P(S('[1|3]+[1|4]', '[7|12]'), r'= \tfrac{4}{12} + \tfrac{3}{12} = \_\_\_'),
         S('[2|3]*[3|5]', '[2|5]'),
         P(N(r'$15\%$ of $60$', '$9$', close(0.15 * 60, 9)), r'= 0.15 \times 60 = \_\_\_'),
         N(r'$25\%$ of $80$', '$20$', 0.25 * 80 == 20),
         N(r'Round $3.476$ to $1$ decimal place', '$3.5$', r(3.476, 1) == 3.5),
         N(r'Write $0.6$ as a percentage', r'$60\%$', close(0.6 * 100, 60)),
         N(r'Simplify the ratio $6 : 9$', '$2 : 3$', math.gcd(6, 9) == 3, tag='Ratio'),
         N(r'Two angles on a straight line: one is $130°$. Find the other.', r'$50°$', 180 - 130 == 50, tag='Ang'),
     ]),
     ],
    [('round', 'S'),
     ('grid', 3, [
         S('-2*(-3)*(-4)', '-24', verb='Evaluate'), S('20-3*(-4)', '32', verb='Evaluate'), S('[3|4]-[1|3]', '[5|12]', verb='Evaluate'),
         N(r'Evaluate $1\tfrac{1}{2} + 2\tfrac{2}{3}$', r'$4\tfrac{1}{6}$', Fr(3, 2) + Fr(8, 3) == Fr(25, 6)),
         N(r'Evaluate $\tfrac{2}{5} \div \tfrac{4}{15}$', r'$\tfrac{3}{2} = 1\tfrac12$', Fr(2, 5) / Fr(4, 15) == Fr(3, 2)),
         N(r'Evaluate $2\tfrac{1}{4} \times 1\tfrac{1}{3}$', '$3$', Fr(9, 4) * Fr(4, 3) == 3),
         N(r'Increase $\$80$ by $15\%$', r'$\$92$', close(80 * 1.15, 92)),
         N(r'Decrease $\$120$ by $30\%$', r'$\$84$', close(120 * 0.7, 84)),
         N(r'Write $18$ as a percentage of $72$', r'$25\%$', 18 / 72 == 0.25),
         S('2.4*0.3', '0.72', verb='Evaluate'), S('7.2÷0.4', '18', verb='Evaluate'),
         N(r'Round $12.6849$ to $2$ decimal places', '$12.68$', r(12.6849, 2) == 12.68),
         N(r'Share $\$60$ in the ratio $1 : 2$', r'$\$20$ and $\$40$', 20 + 40 == 60 and 40 == 2 * 20, tag='Ratio'),
         N(r'Find the mean of $3$, $5$ and $10$', '$6$', (3 + 5 + 10) / 3 == 6, tag='Data'),
     ]),
     ('long', 2, [
         L(r'A $\$95$ pair of thongs is reduced by $20\%$. Find the sale price.', r'$95 \times 0.8 = \$76$', h=18, check=close(95 * 0.8, 76)),
         L(r'At 6 am the temperature at Thredbo is $-4°$C. By noon it has risen $11°$, then it falls $3°$ by evening. What is the evening temperature?',
           r'$-4 + 11 - 3 = 4°$C', h=18, check=(-4 + 11 - 3 == 4)),
     ]),
     ],
    [('round', 'G'),
     ('long', 2, [
         L(r'A shop increases a price by $10\%$, then reduces the new price by $10\%$. Is the final price the same as the original? Use $\$100$ to explain.',
           r'No: $100 \times 1.1 = 110$, then $110 \times 0.9 = \$99$', h=30, check=close(100 * 1.1 * 0.9, 99)),
         L(r'What fraction is exactly halfway between $\tfrac{1}{3}$ and $\tfrac{1}{2}$?', r'$\tfrac{5}{12}$ $\left(\tfrac{4}{12}\text{ and }\tfrac{6}{12}\right)$', h=30,
           check=(Fr(1, 3) + Fr(1, 2)) / 2 == Fr(5, 12)),
         L(r'After a $15\%$ discount a jacket costs $\$68$. What was the original price?', r'$68 \div 0.85 = \$80$', h=30, check=close(68 / 0.85, 80)),
         L(r'Evaluate $-3 \times (4 - 7)^2 \div 9$.', r'$-3 \times 9 \div 9 = -3$', h=30, check=(-3 * (4 - 7) ** 2 / 9 == -3)),
         L(r'Two integers add to $-2$ and multiply to $-15$. Find them.', r'$3$ and $-5$', h=30, check=(3 + -5 == -2 and 3 * -5 == -15)),
         L(r'Which is the better buy: $500$ g of coffee for $\$12.50$ or $750$ g for $\$17.40$? Show working.',
           r'$\$2.50$ per $100$ g vs $\$2.32$ per $100$ g: the $750$ g pack', h=30, check=(12.5 / 5 > 17.4 / 7.5)),
     ]),
     ],
]

# ======================================================================
# LESSON 2  Algebra basics
# ======================================================================
L2 = dict(
    num=2, key='L2', title='Algebra basics',
    sub='Writing expressions · like terms · multiplying and dividing terms · substitution',
    outcomes='MA4-ALG-C-01', ext=GOLD_EXT, book='NCM 8 Ch 3.01–3.05',
    vocab=[('pronumeral', 'a letter that stands for a number'), ('term', 'part of an expression, e.g. $5x$ or $-3y$'),
           ('like terms', 'same pronumerals with the same powers'), ('coefficient', 'the number in front of a pronumeral'),
           ('substitute', 'replace a pronumeral with a number')],
    ideas=[
        r'<b>Like terms</b> have exactly the same pronumerals: $3xy$ and $-5xy$ are like terms; $3x$ and $3x^2$ are not.',
        r'<b>Add or subtract</b> only like terms: $5a + 2b + 3a = 8a + 2b$.',
        r'<b>Multiply</b> the numbers, then the pronumerals: $4a \times 3b = 12ab$, &nbsp; $3m \times m = 3m^2$.',
        r'<b>Divide</b> by writing a fraction and cancelling: $12xy \div 4x = \dfrac{12xy}{4x} = 3y$.',
        r'<b>Substitute</b> using brackets: if $a = -3$, then $2a = 2 \times (-3) = -6$ and $a^2 = (-3)^2 = 9$.',
    ],
    examples=[
        (r'Simplify $5x + 3y - 2x + 7y$.', r'&= 5x - 2x + 3y + 7y \\ &= 3x + 10y'),
        (r'Simplify $4a \times 3ab$.', r'&= 4 \times 3 \times a \times a \times b \\ &= 12a^2b'),
        (r'Evaluate $2a^2 - 3b$ when $a = -3$ and $b = 4$.', r'&= 2(-3)^2 - 3(4) \\ &= 18 - 12 = 6'),
    ],
)
L2['pages'] = [
    [('ideas',),
     ('round', 'B'),
     ('sub', 'Simplify, or answer as instructed.'),
     ('grid', 4, [
         S('7a+3a', '10a'), S('9m-4m', '5m'), S('5x+2y+3x', '8x+2y'), S('4*3k', '12k'),
         S('5a*2b', '10ab'), S('12y÷3', '4y'), S('20ab÷5b', '4a'), S('6p-p+2q', '5p+2q'), S('3m*m', '3m^2'),
         P(S('3a+4b+2a+b', '5a+5b'), r'= (3a + 2a) + (4b + b) = \_\_\_'),
         P(V('3x+5', {'x': 4}, '17', verb='If $x=4$:'), r'= 3 \times 4 + 5 = \_\_\_'),
         N(r'Write an expression for “$5$ more than $n$”', '$n + 5$', True),
         N(r'Write an expression for “the product of $3$ and $y$”', '$3y$', True),
         S('-7+12', '5', tag='L1', verb='Evaluate'),
         N(r'$\tfrac{3}{4}$ of $36$', '$27$', Fr(3, 4) * 36 == 27, tag='L1'),
         V('2a+b', {'a': 3, 'b': -4}, '2', verb='If $a=3,\\,b=-4$:'),
     ]),
     ],
    [('round', 'S'),
     ('sub', 'Simplify.'),
     ('grid', 3, [
         S('3x^2+5x-x^2+2x', '2x^2+7x'), S('4ab-3ba+2a', 'ab+2a'), S('2xy*3x', '6x^2y'),
         S('15a^2b÷5ab', '3a'), S('[8xy|12y]', '[2x|3]'), S('-6m*(-2n)', '12mn'),
     ]),
     ('sub', r'If $p = -3$ and $q = 5$, evaluate:'),
     ('grid', 4, [
         V('p^2-2q', {'p': -3, 'q': 5}, '-1'), V('(p+q)^2', {'p': -3, 'q': 5}, '4'),
         V('[q-p|4]', {'p': -3, 'q': 5}, '2'), V('2pq', {'p': -3, 'q': 5}, '-30'),
     ]),
     ('grid', 2, [
         N(r'Increase $\$60$ by $15\%$', r'$\$69$', close(60 * 1.15, 69), tag='L1'),
         N(r'If $y = 3x - 5$, find $y$ when $x = -2$', '$-11$', 3 * -2 - 5 == -11, tag='Lin'),
     ]),
     ('long', 2, [
         L(r'Pizzas cost $\$14$ each, plus a $\$6$ delivery fee.<br>a) Write an expression for the cost of $n$ pizzas.<br>b) Find the cost of $3$ pizzas.',
           r'a) $14n + 6$ &nbsp; b) $\$48$', h=16, check=(14 * 3 + 6 == 48)),
         L(r'Mia says $3x + 2y = 5xy$. Choose values for $x$ and $y$ to show she is wrong.',
           r'e.g. $x = 2$, $y = 1$: $3x + 2y = 8$ but $5xy = 10$. They are unlike terms.', h=16, check=(3 * 2 + 2 == 8 and 5 * 2 * 1 == 10)),
     ]),
     ],
    [('round', 'G'),
     ('long', 2, [
         L(r'The $n$th term of a pattern is $3n + 2$.<br>a) Find the $50$th term. &nbsp; b) Is $100$ a term? Explain.',
           r'a) $152$ &nbsp; b) No: $3n + 2 = 100$ gives $n = 32\tfrac{2}{3}$, not a whole number', h=30, check=(3 * 50 + 2 == 152 and (100 - 2) % 3 != 0)),
         L(r'A rectangle is $2a$ cm long and $a$ cm wide. Write and simplify expressions for its perimeter and its area.',
           r'Perimeter $6a$ cm; area $2a^2\ \text{cm}^2$', h=30, check=True),
         L(r'Evaluate $a^2 - 2ab + b^2$ when $a = 7.5$ and $b = 2.5$.', r'$56.25 - 37.5 + 6.25 = 25$', h=30,
           check=close(7.5 ** 2 - 2 * 7.5 * 2.5 + 2.5 ** 2, 25)),
         L(r'A taxi charges $\$4$ plus $\$2.50$ per km. Write an expression for the fare for $k$ km, then find the fare for $12$ km.',
           r'$4 + 2.5k$; $\$34$', h=30, check=close(4 + 2.5 * 12, 34)),
         L(r'Find a value of $x$ that makes $x^2$ smaller than $x$.', r'any number between $0$ and $1$, e.g. $x = 0.5$: $0.25 < 0.5$', h=30, check=(0.25 < 0.5)),
         L(r'Simplify $\dfrac{6x}{5} \times \dfrac{10}{3x}$.', '$4$', h=30, check=bool(S('[6x|5]*[10|3x]', '4'))),
     ]),
     ],
]

# ======================================================================
# LESSON 3  Expanding and factorising
# ======================================================================
def hcf_check(a, b, ans):
    return sp.simplify(sp.gcd(to_sympy(a), to_sympy(b)) - to_sympy(ans)) == 0


L3 = dict(
    num=3, key='L3', title='Expanding & factorising',
    sub='The distributive law · expanding and simplifying · highest common factor · factorising',
    outcomes='MA4-ALG-C-01', ext=GOLD_EXT, book='NCM 8 Ch 3.07–3.09',
    vocab=[('expand', 'remove the brackets by multiplying'), ('distributive law', '$a(b + c) = ab + ac$'),
           ('factor', 'a number or term that divides exactly into another'), ('HCF', 'highest common factor'),
           ('factorise', 'write as a product using brackets, e.g. $3(x + 4)$')],
    ideas=[
        r'<b>Expand:</b> multiply <i>every</i> term inside the brackets by the term outside: $3(x + 5) = 3x + 15$.',
        r'<b>Expand, then collect like terms:</b> $2(x + 3) + 4x = 2x + 6 + 4x = 6x + 6$.',
        r'<b>Factorise</b> is the reverse of expand: $6x + 15 = 3(2x + 5)$.',
        r'Find the <b>HCF</b> of the numbers and the pronumerals, write it outside the bracket, then divide each term by it.',
        r'<b>Check</b> your factorising by expanding your answer.',
    ],
    examples=[
        (r'Expand $4(2a + 3)$.', r'&= 4 \times 2a + 4 \times 3 \\ &= 8a + 12'),
        (r'Expand and simplify $3(x + 2) + 2(x + 5)$.', r'&= 3x + 6 + 2x + 10 \\ &= 5x + 16'),
        (r'Factorise $12x + 18$.', r'&\text{HCF} = 6 \\ &= 6(2x + 3)'),
    ],
)
L3['pages'] = [
    [('ideas',),
     ('round', 'B'),
     ('sub', 'Expand.'),
     ('grid', 4, [
         E('3(x+4)', '3x+12'), E('5(a-2)', '5a-10'), E('2(3m+1)', '6m+2'),
         P(E('4(x+5)', '4x+20'), r'= 4 \times x + 4 \times 5 = \_\_\_'),
         E('x(x+6)', 'x^2+6x'), E('a(b-3)', 'ab-3a'), S('-15÷(-3)', '5', tag='L1', verb='Evaluate'), S('3a*4a', '12a^2', tag='L2', verb='Simplify'),
     ]),
     ('sub', 'Find the HCF, then factorise.'),
     ('grid', 4, [
         N('HCF of $12$ and $18$', '$6$', hcf_check('12', '18', '6')), F('3x+12', '3(x+4)'), F('5a-20', '5(a-4)'), F('7y-14', '7(y-2)'),
         P(F('6x+9', '3(2x+3)'), r'\text{HCF} = 3:\ 3(\_\_ + \_\_)'),
         F('x^2+3x', 'x(x+3)'),
     ]),
     ],
    [('round', 'S'),
     ('sub', 'Expand and simplify.'),
     ('grid', 3, [
         E('2a(3a+5b)', '6a^2+10ab'), E('5m(2-m)', '10m-5m^2'), E('3(x+2)+4(x+1)', '7x+10'),
         E('x(x+3)+2(x-4)', 'x^2+5x-8'), E('2(3y+4)+5y', '11y+8'), S('[2|3]+[1|6]', '[5|6]', tag='L1', verb='Evaluate'),
     ]),
     ('sub', 'Factorise fully.'),
     ('grid', 3, [
         F('4m+6', '2(2m+3)'), F('x^2-7x', 'x(x-7)'), F('4a^2+10a', '2a(2a+5)'),
         F('9mn-6m', '3m(3n-2)'), F('15p^2q+20pq^2', '5pq(3p+4q)'), F('3x^2+6x+9', '3(x^2+2x+3)'),
         N(r'$20\%$ of $\$85$', r'$\$17$', close(0.2 * 85, 17), tag='L1'),
         V('3x^2-x', {'x': -2}, '14', tag='L2', verb='If $x=-2$:'),
     ]),
     ('long', 3, [
         L(r'Jack wrote $2(x + 5) = 2x + 5$. Find his mistake and correct it.', r'He did not multiply the $5$ by $2$: $2x + 10$', h=16, check=True),
         L(r'A rectangle has area $(6x + 15)\ \text{cm}^2$ and width $3$ cm. Find an expression for its length.', r'$(2x + 5)$ cm', h=16,
           check=(sp.expand(to_sympy('3(2x+5)') - to_sympy('6x+15')) == 0)),
         L(r'Use factorising to work out $17 \times 23 + 17 \times 77$ in your head.', r'$17(23 + 77) = 17 \times 100 = 1700$', h=16,
           check=(17 * 23 + 17 * 77 == 1700)),
     ]),
     ],
    [('round', 'G'),
     ('long', 2, [
         L(r'Expand and simplify $2(3x + 1) + 3(x + 4) - 5$, then factorise your answer.', r'$9x + 9 = 9(x + 1)$', h=30,
           check=(sp.expand(to_sympy('2(3x+1)+3(x+4)-5') - to_sympy('9(x+1)')) == 0)),
         L(r'Factorise fully $12a^2b + 18ab^2 - 6ab$.', r'$6ab(2a + 3b - 1)$', h=30,
           check=(sp.expand(to_sympy('6ab(2a+3b-1)') - to_sympy('12a^2b+18ab^2-6ab')) == 0)),
         L(r'Write three different expressions, each with brackets, that expand to $12x + 8$.', r'e.g. $4(3x + 2)$, $2(6x + 4)$, $2(3x + 4) + 6x$ (any correct)', h=30,
           check=all(sp.expand(to_sympy(e) - to_sympy('12x+8')) == 0 for e in ('4(3x+2)', '2(6x+4)', '2(3x+4)+6x'))),
         L(r'Factorise $n^2 + n$. Use your answer to explain why $n^2 + n$ is always even for whole numbers $n$.',
           r'$n(n + 1)$: two consecutive whole numbers, so one of them is even', h=30, check=all((k * k + k) % 2 == 0 for k in range(100))),
         L(r'A garden is $(x + 4)$ m long and $3$ m wide. A path $1$ m wide runs along one long side. Write and expand an expression for the area of the garden <i>without</i> the path.',
           r'$2(x + 4) = 2x + 8\ \text{m}^2$', h=30, check=True),
         L(r'Sam factorised $8x^2 - 12x$ as $2x(4x - 6)$. Is this fully factorised? Explain and correct it.',
           r'No: $4x - 6$ still has a common factor of $2$; $4x(2x - 3)$', h=30,
           check=(sp.expand(to_sympy('4x(2x-3)') - to_sympy('8x^2-12x')) == 0)),
     ]),
     ],
]

# ======================================================================
# LESSON 4  Indices and square roots
# ======================================================================
def prime_ok(n, factors):
    return math.prod(p ** e for p, e in factors) == n and all(sp.isprime(p) for p, _ in factors)


L4 = dict(
    num=4, key='L4', title='Indices & square roots',
    sub='Index notation · index laws · the zero index · prime factors · square and cube roots',
    outcomes='MA4-IND-C-01', ext=GOLD_EXT, book='NCM 8 Ch 2.08, 2.10–2.12',
    vocab=[('base', 'the number being multiplied: $2$ in $2^5$'), ('index', 'how many times it is multiplied: $5$ in $2^5$'),
           ('prime', 'a number with exactly two factors, e.g. $2, 3, 5, 7$'), ('square root', '$\\sqrt{49} = 7$ because $7^2 = 49$'),
           ('cube root', '$\\sqrt[3]{8} = 2$ because $2^3 = 8$')],
    ideas=[
        r'$2^5 = 2 \times 2 \times 2 \times 2 \times 2 = 32$. The <b>base</b> is $2$ and the <b>index</b> is $5$.',
        r'<b>Multiply:</b> add indices, $a^m \times a^n = a^{m+n}$. <b>Divide:</b> subtract, $a^m \div a^n = a^{m-n}$.',
        r'<b>Power of a power:</b> multiply, $(a^m)^n = a^{mn}$. <b>Zero index:</b> $a^0 = 1$.',
        r'These laws only work when the <b>bases are the same</b>.',
        r'<b>Prime factors:</b> use a factor tree, then index form: $72 = 2^3 \times 3^2$.',
    ],
    examples=[
        (r'Evaluate $3^4$.', r'&= 3 \times 3 \times 3 \times 3 \\ &= 81'),
        (r'Write $2^3 \times 2^4$ as a single power.', r'&= 2^{3+4} \\ &= 2^7'),
        (r'Write $72$ as a product of prime factors.', r'72 &= 2 \times 2 \times 2 \times 3 \times 3 \\ &= 2^3 \times 3^2'),
    ],
)
L4['pages'] = [
    [('ideas',),
     ('round', 'B'),
     ('sub', 'Evaluate, or answer as instructed.'),
     ('grid', 4, [
         N(r'Write $5 \times 5 \times 5$ in index form', '$5^3$', 5 ** 3 == 125), S('2^5', '32'), S('10^3', '1000'), S('3^2+4^2', '25'),
         S('7^0', '1'), S('sqrt(81)', '9'), S('cbrt(64)', '4'),
         P(S('2^3*2^4', '2^7', verb='Single power:'), r'= 2^{3+4} = \_\_\_'),
         S('5^9÷5^3', '5^6', verb='Single power:'), S('(3^2)^4', '3^8', verb='Single power:'),
         S('4x*5y', '20xy', tag='L2', verb='Simplify'), F('8x-20', '4(2x-5)', tag='L3', verb='Factorise'),
         P(N(r'Write $36$ as a product of primes in index form', r'$2^2 \times 3^2$', prime_ok(36, [(2, 2), (3, 2)])), r'36 = 2 \times 2 \times 3 \times 3 = \_\_\_'),
         N('Write $24$ as a product of primes in index form', r'$2^3 \times 3$', prime_ok(24, [(2, 3), (3, 1)])),
         N(r'$\tfrac{1}{2} + \tfrac{1}{5}$', r'$\tfrac{7}{10}$', Fr(1, 2) + Fr(1, 5) == Fr(7, 10), tag='L1'),
     ]),
     ],
    [('round', 'S'),
     ('sub', 'Evaluate (use the index laws first).'),
     ('grid', 4, [
         S('7^4*7^6÷7^8', '49'), S('(2^4)^3÷2^10', '4'), S('[3^5*3^4|3^7]', '9'), S('4^0+4^1+4^2', '21'),
         S('5*2^3-(3+1)^2', '24'), S('2^3*3^2', '72'), Q('2^n=128', ['7'], verb='Find $n$:'), Q('3^n*3^2=3^9', ['7'], verb='Find $n$:'),
     ]),
     ('grid', 3, [
         N(r'$90$ as a product of primes', r'$2 \times 3^2 \times 5$', prime_ok(90, [(2, 1), (3, 2), (5, 1)])),
         N(r'$540$ as a product of primes', r'$2^2 \times 3^3 \times 5$', prime_ok(540, [(2, 2), (3, 3), (5, 1)])),
         N(r'$\sqrt{50}$ lies between which two whole numbers?', '$7$ and $8$', 49 < 50 < 64),
         N(r'$\sqrt{50}$ to $1$ decimal place', '$7.1$', r(math.sqrt(50), 1) == 7.1),
         N(r'Decrease $\$250$ by $20\%$', r'$\$200$', 250 * 0.8 == 200, tag='L1'),
         E('3(2x+5)', '6x+15', tag='L3', verb='Expand'),
     ]),
     ('long', 3, [
         L(r'True or false: $2^3 \times 2^4 = 4^7$? Explain.', r'False: $2^3 \times 2^4 = 2^7 = 128$, but $4^7 = 16\,384$. Keep the base; add the indices.', h=16,
           check=(2 ** 7 == 128 and 4 ** 7 == 16384)),
         L(r'One bacterium doubles every hour. How many are there after $10$ hours? Write your answer as a power and as a number.',
           r'$2^{10} = 1024$', h=16, check=(2 ** 10 == 1024)),
         L(r'Explain why $5^0 = 1$, using $5^3 \div 5^3$.', r'$5^3 \div 5^3 = 5^0$ by the index law, and any number divided by itself is $1$.', h=16, check=True),
     ]),
     ],
    [('round', 'G'),
     ('long', 2, [
         L(r'Which is larger, $2^{30}$ or $3^{20}$? Hint: $2^{30} = (2^3)^{10}$.', r'$2^{30} = 8^{10}$ and $3^{20} = 9^{10}$, so $3^{20}$ is larger', h=30, check=(3 ** 20 > 2 ** 30)),
         L(r'Find $n$ if $4^n = 2^{10}$. (Write $4$ as a power of $2$.)', r'$2^{2n} = 2^{10}$, so $n = 5$', h=30, check=(4 ** 5 == 2 ** 10)),
         L(r'Use $1764 = 2^2 \times 3^2 \times 7^2$ to find $\sqrt{1764}$ without a calculator.', r'$2 \times 3 \times 7 = 42$', h=30, check=(42 ** 2 == 1764)),
         L(r'What is the smallest whole number you can multiply $72$ by to make a perfect square?', r'$2$: $72 = 2^3 \times 3^2$, so $72 \times 2 = 144 = 12^2$', h=30,
           check=(72 * 2 == 144 and all(math.isqrt(72 * k) ** 2 != 72 * k for k in (1,)))),
         L(r'Evaluate $\dfrac{2^{10}}{2^7 \times 2^3} + 6^0$.', '$2$', h=30, check=(2 ** 10 // (2 ** 7 * 2 ** 3) + 1 == 2)),
         L(r'A square has area $200\ \text{cm}^2$. Find its side length correct to $1$ decimal place.', r'$\sqrt{200} \approx 14.1$ cm', h=30, check=(r(math.sqrt(200), 1) == 14.1)),
     ]),
     ],
]
