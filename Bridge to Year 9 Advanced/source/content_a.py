from dsl import *
from svg import *
import math

# ======================================================================
# LESSON 1  Algebra basics
# ======================================================================
L1 = dict(
    num=1, key='L1', title='Algebra basics',
    sub='Like terms · multiplying and dividing terms · substitution · simple algebraic fractions',
    outcomes='MA4-ALG-C-01', ext='Gold: MA5-ALG-C-01 (algebraic fractions with numerical denominators) · MA5-ALG-P-01/P-02 (indices, binomial numerators)',
    book='NCM 8 Adv 3.01–3.05 → NCM 9 Adv 1.01–1.04',
    ideas=[
        r'<b>Like terms</b> have exactly the same pronumerals with the same powers: $3x^2y$ and $-5x^2y$ are like terms; $3x^2$ and $3x$ are not.',
        r'<b>Add or subtract</b> only like terms: $5a + 2b + 3a = 8a + 2b$.',
        r'<b>Multiply</b> the numbers, then the pronumerals: $4a \times 3ab = 12a^2b$.',
        r'<b>Divide</b> by writing a fraction and cancelling: $12xy \div 4x = \dfrac{12xy}{4x} = 3y$.',
        r'<b>Substitute</b> using brackets: if $a=-3$, then $a^2 = (-3)^2 = 9$ but $-a^2 = -9$.',
    ],
    examples=[
        ('Simplify $5x + 3y - 2x + 7y$.', r'&= 5x - 2x + 3y + 7y \\ &= 3x + 10y'),
        (r'Evaluate $2a^2 - 3b$ when $a=-3,\ b=4$.', r'&= 2(-3)^2 - 3(4) \\ &= 18 - 12 = 6'),
        (r'Simplify $\dfrac{2x}{3} \times \dfrac{9}{4x}$.', r'&= \dfrac{18x}{12x} = \dfrac{3}{2}'),
    ],
)
L1['pages'] = [
    [('ideas',),
     ('round', 'B'),
     ('sub', 'Simplify.'),
     ('grid', 4, [
         S('7a+3a', '10a'), S('9m-4m', '5m'), S('5x+2y+3x', '8x+2y'), S('6p-p+2q', '5p+2q'),
         S('4*3k', '12k'), S('5a*2b', '10ab'), S('3m*m', '3m^2'), S('12y÷3', '4y'),
         S('20ab÷5b', '4a'), S('-7+12', '5', tag='Int', verb='Evaluate'), S('8x-3-2x+7', '6x+4'), S('-3*4n', '-12n'),
         S('[3|4]*36', '27', tag='Frac', verb='Evaluate'), S('2ab+5ab-ab', '6ab'),
     ]),
     ('sub', r'If $a = 4$, $b = -2$ and $c = 0.5$, evaluate:'),
     ('grid', 4, [
         V('3a+b', {'a': 4, 'b': -2}, '10'), V('ab', {'a': 4, 'b': -2}, '-8'),
         V('a^2+b^2', {'a': 4, 'b': -2}, '20'), V('10c', {'c': 0.5}, '5'),
         N(r'$25\%$ of $80$', '$20$', 0.25 * 80 == 20, tag='%'), V('b^2-a', {'a': 4, 'b': -2}, '0'),
     ]),
     ],
    [('round', 'S'),
     ('sub', 'Simplify.'),
     ('grid', 3, [
         S('3x^2+5x-x^2+2x', '2x^2+7x'), S('4ab-3ba+2a', 'ab+2a'), S('-6m*(-2mn)', '12m^2n'),
         S('2xy*3xy', '6x^2y^2'), S('-18pq÷6q', '-3p'), S('15a^2b÷5ab', '3a'),
         S('[8xy|12y]', '[2x|3]'), N(r'Simplify the ratio $18 : 24$', '$3 : 4$', math.gcd(18, 24) == 6, tag='Ratio'),
         S('5x-(-3x)', '8x'),
         S('[x|3]*6', '2x'), S('[2a|5]*[10|a]', '4'), S('[3m|4]÷[m|8]', '6'),
         N(r'If $y = 3x - 5$, find $y$ when $x = -2$', '$y = -11$', 3 * -2 - 5 == -11, tag='Lin'),
         N(r'Increase $\$60$ by $15\%$', r'$\$69$', close(60 * 1.15, 69), tag='%'),
         S('-2*(-3)*(-5)', '-30', tag='Int', verb='Evaluate'),
     ]),
     ('sub', r'If $p = -3$ and $q = 5$, evaluate:'),
     ('grid', 4, [
         V('p^2-2q', {'p': -3, 'q': 5}, '-1'), V('-p^2', {'p': -3}, '-9'),
         V('(p+q)^2', {'p': -3, 'q': 5}, '4'), V('[q-p|4]', {'p': -3, 'q': 5}, '2'),
     ]),
     ('long', 2, [
         L(r'Pizzas cost $\$14$ each, plus a $\$6$ delivery fee.<br>a) Write an expression for the cost, in dollars, of $n$ pizzas.<br>b) Find the cost of $3$ pizzas.',
           r'a) $14n + 6$ &nbsp; b) $\$48$', h=14, check=14 * 3 + 6 == 48),
         L(r'Mia says $3x + 2y = 5xy$. Choose values for $x$ and $y$ to show she is wrong, then explain her mistake.',
           r'e.g. $x=2,\ y=1$: $3x+2y = 8$ but $5xy = 10$. $3x$ and $2y$ are unlike terms, so they cannot be added. (Note: $x=y=1$ gives $5=5$, which does <i>not</i> disprove it.)',
           h=14, check=(3 * 2 + 2 * 1 == 8 and 5 * 2 * 1 == 10)),
     ]),
     ],
    [('round', 'G'),
     ('sub', 'Simplify.'),
     ('grid', 4, [
         S('[x|3]+[x|4]', '[7x|12]'), S('[2a|5]-[a|3]', '[a|15]'), S('[5m|6]-[m|4]', '[7m|12]'),
         S('[6x^2y|9xy^2]', '[2x|3y]'), S('[3x|4]-[x|6]', '[7x|12]'), S('[4ab|3]*[9|2b]', '6a'),
         S('[2m|3]÷[4m|9]', '[3|2]'), S('[x+1|2]+[x|3]', '[5x+3|6]'),
     ]),
     ('long', 2, [
         L(r'A rectangle has length $3x + 2$ and width $x - 1$.<br>a) Show that its perimeter is $8x + 2$.<br>b) Find the perimeter when $x = 4$.<br>c) Why must $x$ be greater than $1$?',
           r'a) $2(3x+2) + 2(x-1) = 6x + 4 + 2x - 2 = 8x + 2$ &nbsp; b) $34$ &nbsp; c) the width $x - 1$ must be positive',
           h=30, check=(8 * 4 + 2 == 34)),
         L(r'Without a calculator, evaluate $a^2 - 2ab + b^2$ when $a = 7.5$ and $b = 2.5$.<br><span class="hint">Hint: look for a shortcut.</span>',
           r'$56.25 - 37.5 + 6.25 = 25$; shortcut: it equals $(a-b)^2 = 5^2 = 25$', h=30,
           check=close(7.5 ** 2 - 2 * 7.5 * 2.5 + 2.5 ** 2, 25)),
         L(r'The $n$th term of a pattern is $3n^2 - n$.<br>a) Find the $10$th term.<br>b) Is $70$ a term of the pattern? Justify your answer.',
           r'a) $290$ &nbsp; b) Yes: $n = 5$ gives $75 - 5 = 70$ (the 5th term)', h=30,
           check=(3 * 100 - 10 == 290 and 3 * 25 - 5 == 70)),
         L(r'Two numbers $a$ and $b$ have $a + b = 10$ and $ab = 21$. Find the value of $a^2 + b^2$.',
           r'$58$ (the numbers are $3$ and $7$: $9 + 49 = 58$; or $(a+b)^2 - 2ab = 100 - 42$)', h=30,
           check=(3 + 7 == 10 and 3 * 7 == 21 and 9 + 49 == 58)),
     ]),
     ],
]

# ======================================================================
# LESSON 2  Expanding brackets
# ======================================================================
L2 = dict(
    num=2, key='L2', title='Expanding brackets',
    sub='The distributive law · expanding and simplifying · binomial products (Gold)',
    outcomes='MA4-ALG-C-01',
    ext='★ negative coefficients: MA5-ALG-C-01 · Gold: binomial products MA5-ALG-C-01; special products MA5-ALG-P-02',
    book='NCM 8 Adv 3.07, 3.11–3.13 → NCM 9 Adv 1.05, 1.07–1.10',
    ideas=[
        r'<b>Distributive law:</b> multiply <i>every</i> term inside the brackets by the term outside: $a(b + c) = ab + ac$.',
        r'An area model shows why: a rectangle $3$ by $(x + 5)$ has area $3x + 15$.',
        r'<b>Negative outside:</b> every sign inside changes: $-2(x - 5) = -2x + 10$.',
        r'<b>Expand, then collect like terms:</b> $3(x + 2) + 2(x - 1) = 3x + 6 + 2x - 2 = 5x + 4$.',
        r'<b>Gold</b> – binomial products: $(a + b)(c + d) = ac + ad + bc + bd$.',
    ],
    examples=[
        ('Expand $-3(2x - 4)$.', r'&= -3 \times 2x + (-3) \times (-4) \\ &= -6x + 12'),
        ('Expand and simplify $4(2a + 1) - 3(a - 2)$.', r'&= 8a + 4 - 3a + 6 \\ &= 5a + 10'),
        ('<span class="gold-t">Gold</span> Expand $(x + 3)(x + 5)$.', r'&= x^2 + 5x + 3x + 15 \\ &= x^2 + 8x + 15'),
    ],
)
L2['pages'] = [
    [('ideas',),
     ('round', 'B'),
     ('sub', 'Expand.'),
     ('grid', 4, [
         E('3(x+4)', '3x+12'), E('5(a-2)', '5a-10'), E('2(3m+1)', '6m+2'), E('4(2-y)', '8-4y'),
         E('x(x+6)', 'x^2+6x'), E('a(b-3)', 'ab-3a'), S('4x+3-x+2', '3x+5', tag='L1', verb='Simplify'), E('6(2p+3q)', '12p+18q'),
         S('(-4)*(-6)', '24', tag='Int', verb='Evaluate'), E('7(3-2k)', '21-14k'), E('10(0.3x+2)', '3x+20'),
         V('2a+b', {'a': 3, 'b': -4}, '2', tag='L1', verb='If $a=3,\\,b=-4$:'),
     ]),
     ('sub', 'Expand and simplify.'),
     ('grid', 4, [
         E('2(x+3)+5', '2x+11'), E('4(a+1)+3a', '7a+4'), S('[2|3]+[1|6]', '[5|6]', tag='Frac', verb='Evaluate'), E('y(4-y)', '4y-y^2'),
         E('3(x+2)+2(x+1)', '5x+8'), N(r'$10\%$ of $450$', '$45$', 0.1 * 450 == 45, tag='%'),
     ]),
     ],
    [('round', 'S'),
     ('sub', 'Expand and simplify. <span class="star">★</span> = beyond Stage 4 core (in your Year 8 textbook).'),
     ('grid', 3, [
         E('-2(x+5)', '-2x-10', star=True), E('-(m+4)', '-m-4', star=True), E('-4(3a-2)', '-12a+8', star=True),
         E('-x(x-7)', '-x^2+7x', star=True), E('2a(3a+5b)', '6a^2+10ab'), E('5m(2-m)', '10m-5m^2'),
         E('3(x+2)+4(x+1)', '7x+10'), E('5(2a-1)-3(a+2)', '7a-11', star=True), E('x(x+3)+2(x-4)', 'x^2+5x-8'),
         E('4(3-y)-(y+2)', '10-5y', star=True), S('15x^2y÷3xy', '5x', tag='L1', verb='Simplify'),
         E('-2(p-q)+3(2p+q)', '4p+5q', star=True),
         N(r'Share $\$120$ in the ratio $3 : 5$', r'$\$45$ and $\$75$', (45 + 75 == 120 and 45 * 5 == 75 * 3), tag='Ratio'),
         E('[1|2](4x+6)', '2x+3'), E('3x(2x-1)-x(x+4)', '5x^2-7x', star=True),
     ]),
     ('long', 3, [
         L('Write the area of the whole rectangle in two ways, one using brackets.' + area_model(),
           r'$7(x + 4) = 7x + 28$ (distributive law)', h=10, check=True),
         L(r'Jack wrote $-3(x - 5) = -3x - 15$. Find his error and correct it. <span class="star">★</span>',
           r'$-3 \times (-5) = +15$, so $-3(x-5) = -3x + 15$', h=22, check=(-3 * -5 == 15)),
         L(r'Adult cinema tickets cost $\$x$ and child tickets cost $\$(x - 8)$.<br>a) Write and simplify an expression for $3$ adults and $4$ children.<br>b) Find the total if an adult ticket is $\$20$.',
           r'a) $3x + 4(x - 8) = 7x - 32$ &nbsp; b) $\$108$', h=14, check=(7 * 20 - 32 == 108 and 3 * 20 + 4 * 12 == 108)),
     ]),
     ],
    [('round', 'G'),
     ('sub', 'Expand and simplify.'),
     ('grid', 3, [
         E('(x+2)(x+7)', 'x^2+9x+14'), E('(a-4)(a+6)', 'a^2+2a-24'), E('(2m+1)(m-3)', '2m^2-5m-3'),
         E('(x+5)^2', 'x^2+10x+25'), E('(y-3)(y+3)', 'y^2-9'), E('(3a-2)^2', '9a^2-12a+4'),
         E('(x+4)(x-4)', 'x^2-16'), E('(2x+3)(3x-1)', '6x^2+7x-3'), E('(x+1)(x+2)-x(x+3)', '2'),
     ]),
     ('long', 2, [
         L(r'a) Show that $(n + 1)^2 - n^2 = 2n + 1$.<br>b) Hence find $101^2 - 100^2$ without a calculator.',
           r'a) $n^2 + 2n + 1 - n^2 = 2n + 1$ &nbsp; b) $n = 100$: $201$', h=40, check=(101 ** 2 - 100 ** 2 == 201)),
         L(r'A square of side $x$ is cut from a rectangle measuring $(x + 4)$ by $(x + 1)$. Show that the area left is $5x + 4$.' + rect_minus_square(),
           r'$(x+4)(x+1) - x^2 = x^2 + 5x + 4 - x^2 = 5x + 4$', h=14,
           check=(sp.expand(to_sympy('(x+4)(x+1)-x^2') - to_sympy('5x+4')) == 0)),
     ]),
     ],
]

# ======================================================================
# LESSON 3  Factorising
# ======================================================================
def hcf_check(a, b, ans):
    return sp.simplify(sp.gcd(to_sympy(a), to_sympy(b)) - to_sympy(ans)) == 0


L3 = dict(
    num=3, key='L3', title='Factorising',
    sub='Highest common factor · taking out the HCF · negative common factors · checking by expanding',
    outcomes='MA4-ALG-C-01',
    ext='★ negative HCF: MA5-ALG-P-01 · Gold: binomial common factors, difference of squares, monic trinomials MA5-ALG-P-01, MA5-ALG-P-02',
    book='NCM 8 Adv 3.08–3.10 → NCM 9 Adv 1.06, 1.11–1.14',
    ideas=[
        r'<b>Factorising</b> is the reverse of expanding: $6x + 15 \;\rightleftarrows\; 3(2x + 5)$.',
        r'Find the <b>HCF</b> of the numbers <i>and</i> the pronumerals, write it outside, then divide each term by it.',
        r'<b>Fully</b> factorised means nothing more can come out: $2x(6x - 4)$ is not finished – use $4x(3x - 2)$.',
        r'If the first term is negative, you may take out a <b>negative</b> HCF: $-6x - 9 = -3(2x + 3)$.',
        r'<b>Always check</b> by expanding your answer.',
    ],
    examples=[
        ('Factorise $12x + 18$.', r'&\text{HCF} = 6 \\ &= 6(2x + 3)'),
        ('Factorise $8a^2b - 12ab^2$.', r'&\text{HCF} = 4ab \\ &= 4ab(2a - 3b)'),
        ('Factorise $-5m - 15$.', r'&\text{HCF} = -5 \\ &= -5(m + 3)'),
    ],
)
L3['pages'] = [
    [('ideas',),
     ('round', 'B'),
     ('sub', 'Find the highest common factor (HCF).'),
     ('grid', 4, [
         N('$12$ and $18$', '$6$', hcf_check('12', '18', '6')), N('$8x$ and $12$', '$4$', hcf_check('8x', '12', '4')),
         N('$6a$ and $9ab$', '$3a$', hcf_check('6a', '9ab', '3a')), N('$x^2$ and $5x$', '$x$', hcf_check('x^2', '5x', 'x')),
     ]),
     ('sub', 'Factorise.'),
     ('grid', 4, [
         F('3x+12', '3(x+4)'), F('5a-20', '5(a-4)'), F('4m+6', '2(2m+3)'), F('7y-14', '7(y-2)'),
         E('4(2x-3)', '8x-12', tag='L2', verb='Expand'), F('x^2+3x', 'x(x+3)'), F('ab+5a', 'a(b+5)'), F('10-15k', '5(2-3k)'),
         S('-15÷(-3)', '5', tag='Int', verb='Evaluate'), F('9p+9', '9(p+1)'), S('3a*4a', '12a^2', tag='L1', verb='Simplify'),
         F('6xy+8x', '2x(3y+4)'),
         Q('3x+5=20', ['5'], tag='Eq', verb='Solve'), F('12a-8b', '4(3a-2b)'),
     ]),
     ],
    [('round', 'S'),
     ('sub', 'Factorise fully. <span class="star">★</span> = beyond Stage 4 core (in your Year 8 textbook).'),
     ('grid', 3, [
         F('x^2-7x', 'x(x-7)'), F('4a^2+10a', '2a(2a+5)'), F('9mn-6m', '3m(3n-2)'),
         F('-4x-12', '-4(x+3)', star=True), F('-10a+15', '-5(2a-3)', star=True), F('-x^2-6x', '-x(x+6)', star=True),
         F('15p^2q+20pq^2', '5pq(3p+4q)'), F('3x^2+6x+9', '3(x^2+2x+3)'), F('2a^2-4ab+6a', '2a(a-2b+3)'),
         E('-3(2-5y)', '-6+15y', tag='L2', star=True, verb='Expand'),
         N(r'A $\$85$ shirt is reduced by $20\%$. Find the sale price.', r'$\$68$', close(85 * 0.8, 68), tag='%'),
         F('18x^2y-12xy', '6xy(3x-2)'),
         V('3x^2-x', {'x': -2}, '14', tag='L1', verb='If $x=-2$:'),
         N(r'Does the point $(2,\,7)$ lie on $y = 3x + 1$?', r'Yes: $3(2) + 1 = 7$', 3 * 2 + 1 == 7, tag='Lin'),
     ]),
     ('sub', 'Factorise the numerator, then simplify.'),
     ('grid', 3, [
         S('[5x+10|5]', 'x+2'), S('[6a-9|3]', '2a-3'), S('[4x^2+8x|4x]', 'x+2'),
     ]),
     ('long', 3, [
         L(r'Sam says $12x^2 - 8x = 2x(6x - 4)$.<br>a) Expand to show the two sides are equal.<br>b) Why is Sam\'s answer not fully factorised? Correct it.',
           r'a) $2x(6x-4) = 12x^2 - 8x$ ✓ &nbsp; b) $6x - 4$ still has a common factor of $2$; $4x(3x - 2)$', h=16,
           check=(sp.expand(to_sympy('2x(6x-4)') - to_sympy('4x(3x-2)')) == 0)),
         L(r'A rectangle has area $(6x + 15)\ \text{cm}^2$ and width $3$ cm. Find an expression for its length.',
           r'$(2x + 5)$ cm', h=16, check=(sp.expand(to_sympy('3(2x+5)') - to_sympy('6x+15')) == 0)),
         L(r'Use factorising to evaluate $17 \times 23 + 17 \times 77$ mentally.',
           r'$17(23 + 77) = 17 \times 100 = 1700$', h=16, check=(17 * 23 + 17 * 77 == 1700)),
     ]),
     ],
    [('round', 'G'),
     ('sub', 'Factorise fully.'),
     ('grid', 3, [
         F('a(x+3)+b(x+3)', '(x+3)(a+b)', full=True), F('x(y-2)-4(y-2)', '(y-2)(x-4)', full=True),
         F('x^2-25', '(x-5)(x+5)', full=True),
         F('4m^2-9', '(2m-3)(2m+3)', full=True), F('x^2+7x+12', '(x+3)(x+4)', full=True),
         F('x^2-2x-15', '(x-5)(x+3)', full=True),
         F('x^2+x-12', '(x+4)(x-3)', full=True), F('9a^2-1', '(3a-1)(3a+1)', full=True), F('2x^2-18', '2(x-3)(x+3)', full=True),
     ]),
     ('long', 2, [
         L(r'Use the difference of two squares to evaluate $53^2 - 47^2$ without a calculator.',
           r'$(53 - 47)(53 + 47) = 6 \times 100 = 600$', h=40, check=(53 ** 2 - 47 ** 2 == 600)),
         L(r'Factorise $n^2 + n$, then explain why $n^2 + n$ is always even for any whole number $n$.',
           r'$n(n + 1)$: the product of two consecutive whole numbers, one of which must be even', h=40,
           check=all((k * k + k) % 2 == 0 for k in range(100))),
     ]),
     ],
]

# ======================================================================
# LESSON 4  Indices
# ======================================================================
def prime_ok(n, factors):
    return math.prod(p ** e for p, e in factors) == n and all(sp.isprime(p) for p, _ in factors)


L4 = dict(
    num=4, key='L4', title='Indices',
    sub='Index notation · prime factors · square and cube roots · index laws · the zero index',
    outcomes='MA4-IND-C-01',
    ext='Gold: index laws with pronumerals and the negative index MA5-IND-C-01',
    book='NCM 8 Adv 2.08, 2.10–2.12, 3.06 → NCM 9 Adv 5.01–5.05',
    ideas=[
        r'In $2^5$, $2$ is the <b>base</b> and $5$ is the <b>index</b> (power): $2^5 = 2\times2\times2\times2\times2 = 32$.',
        r'<b>Multiply:</b> add indices $a^m \times a^n = a^{m+n}$. &nbsp; <b>Divide:</b> subtract $a^m \div a^n = a^{m-n}$.',
        r'<b>Power of a power:</b> multiply $(a^m)^n = a^{mn}$. &nbsp; <b>Products:</b> $(ab)^n = a^n b^n$.',
        r'<b>Zero index:</b> $a^0 = 1$ (for $a \ne 0$). The laws only work when the <b>bases are the same</b>.',
        r'<b>Prime factors:</b> use a factor tree, then write in index form: $72 = 2^3 \times 3^2$.',
    ],
    examples=[
        (r'Simplify, then evaluate $3^4 \times 3^5 \div 3^6$.', r'&= 3^{4+5-6} \\ &= 3^3 = 27'),
        (r'Write $360$ as a product of primes.', r'360 &= 2\times2\times2\times3\times3\times5 \\ &= 2^3 \times 3^2 \times 5'),
        (r'Evaluate $(2^3)^2 \times 5^0$.', r'&= 2^6 \times 1 \\ &= 64'),
    ],
)
L4['pages'] = [
    [('ideas',),
     ('round', 'B'),
     ('sub', 'Evaluate, or write as instructed.'),
     ('grid', 4, [
         N(r'Write $5\times5\times5\times5$ in index form', '$5^4$', 5 ** 4 == 625),
         S('2^5', '32'), N('$10^4$', r'$10\,000$', 10 ** 4 == 10000), S('3^2+4^2', '25'),
         S('7^0', '1'), S('4x*5y', '20xy', tag='L1', verb='Simplify'), S('sqrt(81)', '9'), S('cbrt(64)', '4'),
         F('8x-20', '4(2x-5)', tag='L3', verb='Factorise'), N(r'Which is larger: $2^5$ or $5^2$?', '$2^5$ ($32 > 25$)', 2 ** 5 > 5 ** 2),
         E('5(2a+3)', '10a+15', tag='L2', verb='Expand'), S('[3|5]*[10|9]', '[2|3]', tag='Frac'),
     ]),
     ('sub', 'Write as a single power.'),
     ('grid', 4, [
         S('2^3*2^4', '2^7'), S('5^9÷5^3', '5^6'), S('(3^2)^4', '3^8'), S('6^5÷6', '6^4'),
     ]),
     ('sub', 'Write each number as a product of its prime factors in index form.'),
     ('grid', 4, [
         N('$24$', r'$2^3 \times 3$', prime_ok(24, [(2, 3), (3, 1)])),
         N('$100$', r'$2^2 \times 5^2$', prime_ok(100, [(2, 2), (5, 2)])),
         N('$90$', r'$2 \times 3^2 \times 5$', prime_ok(90, [(2, 1), (3, 2), (5, 1)])),
         N('$56$', r'$2^3 \times 7$', prime_ok(56, [(2, 3), (7, 1)])),
     ]),
     ],
    [('round', 'S'),
     ('sub', 'Evaluate (use the index laws first).'),
     ('grid', 4, [
         S('7^4*7^6÷7^8', '49'), S('(2^4)^3÷2^10', '4'), S('[3^5*3^4|3^7]', '9'), S('(2*5)^3', '1000'),
         S('4^0+4^1+4^2', '21'), S('5*2^3-(3+1)^2', '24'), S('2^3*3^2', '72'),
         F('-6a-9', '-3(2a+3)', tag='L3', star=True, verb='Factorise'),
         N(r'$540$ as a product of primes', r'$2^2 \times 3^3 \times 5$', prime_ok(540, [(2, 2), (3, 3), (5, 1)])),
         N(r'$1260$ as a product of primes', r'$2^2 \times 3^2 \times 5 \times 7$', prime_ok(1260, [(2, 2), (3, 2), (5, 1), (7, 1)])),
         N(r'Use $1764 = 2^2 \times 3^2 \times 7^2$ to find $\sqrt{1764}$', '$42$', 42 ** 2 == 1764 and prime_ok(1764, [(2, 2), (3, 2), (7, 2)])),
         N(r'If $b = -4$, evaluate $5 - 2b$', '$13$', 5 - 2 * -4 == 13, tag='L1'),
         N(r'$40$ as a percentage of $160$', r'$25\%$', 40 / 160 == 0.25, tag='%'),
         N(r'$\sqrt{50}$ lies between which two whole numbers?', '$7$ and $8$', 49 < 50 < 64),
         Q('2^n=128', ['7'], verb='Find $n$:'), Q('3^n*3^2=3^9', ['7'], verb='Find $n$:'),
         E('x(x-4)+3x', 'x^2-x', tag='L2', verb='Expand'),
         N(r'Simplify $\dfrac{2^{10}}{2^7 \times 2^3}$', '$1$', 2 ** 10 == 2 ** 7 * 2 ** 3),
     ]),
     ('long', 3, [
         L(r'True or false: $2^3 \times 2^4 = 4^7$? Explain.',
           r'False: $2^3 \times 2^4 = 2^7 = 128$, but $4^7 = 16\,384$. Add the indices; do not multiply the bases.', h=16,
           check=(2 ** 7 == 128 and 4 ** 7 == 16384)),
         L(r'One bacterium doubles every hour.<br>a) How many are there after $10$ hours?<br>b) After how many hours are there first more than $1\,000\,000$?',
           r'a) $2^{10} = 1024$ &nbsp; b) $20$ hours ($2^{19} = 524\,288$, $2^{20} = 1\,048\,576$)', h=16,
           check=(2 ** 10 == 1024 and 2 ** 19 < 10 ** 6 < 2 ** 20)),
         L(r'Use $5^3 \div 5^3$ in two different ways to explain why $5^0 = 1$.',
           r'Index law: $5^{3-3} = 5^0$. Dividing a number by itself: $125 \div 125 = 1$. So $5^0 = 1$.', h=16, check=True),
     ]),
     ],
    [('round', 'G'),
     ('sub', 'Simplify. (Index laws with pronumerals.)'),
     ('grid', 4, [
         S('a^4*a^5', 'a^9'), S('x^7÷x^2', 'x^5'), S('(m^3)^4', 'm^12'), S('3x^2*4x^5', '12x^7'),
         S('(2a^3)^2', '4a^6'), S('[12p^5q^2|4p^2q]', '3p^3q'), S('5y^0+(5y)^0', '6'), S('2^(-3)', '[1|8]', verb='Evaluate'),
         S('(3x^2y)^3', '27x^6y^3'), S('[(2a^2)^3|4a^5]', '2a'), S('[x^3*x^4|(x^2)^3]', 'x'), S('10^(-2)', '[1|100]', verb='Evaluate'),
     ]),
     ('long', 2, [
         L(r'Which is larger, $2^{30}$ or $3^{20}$? Justify your answer without a calculator.',
           r'$2^{30} = (2^3)^{10} = 8^{10}$ and $3^{20} = (3^2)^{10} = 9^{10}$, so $3^{20}$ is larger.', h=34,
           check=(3 ** 20 > 2 ** 30)),
         L(r'Find the value of $n$ if $4^n = 2^{10}$.<br><span class="hint">Hint: write $4$ as a power of $2$.</span>',
           r'$4^n = 2^{2n}$, so $2n = 10$ and $n = 5$', h=34, check=(4 ** 5 == 2 ** 10)),
     ]),
     ],
]
