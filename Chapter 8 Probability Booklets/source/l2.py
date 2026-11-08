from engine import Q, R, LN_W, LN_A, LN_A2
from gfx import *
from pm import *
from layout import F

SUB = 'Probability • MA4-PRO-C-01'


def S(*cols):
    return [(c, 1, None) for c in cols]


def blue_q(secs, size=14):
    nb = sum(w for c, w, _ in secs if c == 'blue')
    tot = sum(w for _, w, _ in secs)
    return Q(fig=spinner(secs, size), ans=f'{frs(nb, tot)} = {fr(spin_p(secs, "blue"))}' if Fr(nb, tot).denominator != tot else fr(spin_p(secs, 'blue')))


def die_q(text, pred, size=10):
    fav, p = die_p(pred)
    return Q(f'Find P({text}).', die3d(size, 1, 5, 3), f'{setstr(fav)}: {frs(len(fav), 6)} = {fr(p)}' if p.denominator != 6 else f'{setstr(fav)}: {fr(p)}')


def show(fav, tot, form='frac', dp=None):
    p = Fr(fav, tot)
    base = frs(fav, tot) + (f' = {fr(p)}' if p.denominator != tot else '')
    if form == 'dec':
        return base + f' = {dec(p, dp)}'
    if form == 'pct':
        return base + f' = {pct(p, dp)}'
    if form == 'all':
        return base + f' = {dec(p, dp)} = {pct(p, None if dp is None else dp - 2)}'
    return base


DIE_ROW = ''.join(
    f'<span style="display:inline-block;border-radius:1.6mm;{"outline:.45mm solid #7a1f4e;outline-offset:.35mm" if k >= 4 else ""}">{die(k, 4.8)}</span>'
    for k in range(1, 7))

NOTES = f'''<div class="tnotes">
<div><h4>KEY TERMS</h4>
<p><b>event (E):</b> the outcome or outcomes we want</p>
<p><b>favourable outcome:</b> an outcome that is in the event</p>
<p><b>P(E):</b> ‘the probability of E’</p>
<p><b>simplest form:</b> divide top and bottom by their highest common factor</p>
<p><b>a standard deck:</b> 52 cards, 4 suits of 13 (♥ ♦ red, ♣ ♠ black); picture cards J, Q, K</p></div>
<div><h4>FORMULA</h4>
<div class="fbox">P(E) = {F('number of favourable outcomes', 'total number of outcomes', True)}</div>
<p>fraction → decimal: top ÷ bottom</p><p>decimal → percentage: × 100%</p>
<p>‘or’ (different groups): add the counts, e.g. P(red or blue)</p></div>
<div><h4>STEPS</h4>
<p><span class="step">1</span>list the sample space &nbsp;<span class="step">2</span>circle the favourable outcomes</p>
<p><span class="step">3</span>write the fraction, simplify &nbsp;<span class="step">4</span>convert if asked</p>
<div style="display:flex;gap:1mm;margin:.8mm 0 .6mm">{DIE_ROW}</div>
<p><b>at least 4</b> = 4 or more; <b>at most 4</b> = 4 or less <span class="maroon" style="font-size:7pt">(extension wording)</span></p>
<p>P(at least 4) = {frs(3, 6)} = {fr(Fr(1, 2))} = 0.5 = 50%</p></div>
</div>'''

MONEY = [('$2', 4), ('$1', 3), ('50c', 2), ('20c', 6), ('10c', 5)]
NCOINS = sum(k for _, k in MONEY)
assert NCOINS == 20

EX1 = dict(
    instr='Find each probability. Write the fraction in simplest form.',
    parts=[
        ('Spinner: P(red)', spinner(S('red', 'blue', 'yellow', 'green'), 15), ''),
        ('Die: P(an odd number)', die3d(13, 1, 5, 3), ''),
        ('Lollies: P(yellow or blue)', jar([('red', 5), ('green', 3), ('yellow', 6), ('blue', 2)], 17), ''),
        ('Tiles: P(a vowel)', '<div style="padding:3mm 0">' + tiles('KINGSCLIFF', 4.4) + '</div>', ''),
    ], box=18,
    ans=[f'{fr(spin_p(S("red", "blue", "yellow", "green"), "red"))}',
         show(3, 6), show(8, 16), show(sum(1 for c in "KINGSCLIFF" if c in "AEIOU"), 10)])

gold = sum(k for v, k in MONEY if v in ('$1', '$2'))
_, rpic = card_p(lambda c: c[1] in RED and c[0] in PICTURE)
EX2 = dict(
    instr='Give each answer in the form asked. Read each question twice.',
    parts=[
        ('As a decimal', money_box(MONEY, 36), 'One coin falls out of the money box. P(gold coin)'),
        ('Cards', cards(['KH', 'QD', 'JS'], 14), 'One card from a 52-card deck. P(a red picture card)'),
        ('As a percentage', die3d(11, 2, 6, 4), 'A die is rolled. P(a number greater than 4)'),
        ('Notes', '', 'Elena has two $5, four $10 and three $20 notes. She takes one at random. P($20 note)'),
    ], box=18,
    ans=[show(gold, NCOINS, 'dec'), show(6, 52), f'{show(2, 6)} = {pct_third(Fr(1, 3))} (about 33.3%)', show(3, 9)])
assert rpic == Fr(6, 52)

# ---------------------------------------------------------------- standard
BAG = [('red', 5), ('blue', 3), ('green', 4)]
NB = sum(k for _, k in BAG)
JAR = [('red', 6), ('green', 3), ('yellow', 9), ('blue', 2)]
NJ = sum(k for _, k in JAR)
assert NJ == 20
cnt = lambda lst, *cs: sum(k for c, k in lst if c in cs)

std_p1 = [
    R('count the blue sectors and the total sectors, then write P(blue) in simplest form.', 4,
      [blue_q(S('blue', 'red')), blue_q(S('blue', 'red', 'yellow')), blue_q(S('blue', 'red', 'blue', 'green', 'yellow')),
       blue_q(S('blue', 'red', 'blue', 'yellow', 'red', 'blue', 'yellow', 'red'))],
      h=34, ln=[('Blue', ''), ('Total', ''), ('P(blue)', '')]),
    R('a fair die is rolled once. List the favourable outcomes, then find the probability.', 4,
      [die_q('rolling a 5', lambda x: x == 5), die_q('an even number', lambda x: x % 2 == 0),
       die_q('a number less than 3', lambda x: x < 3), die_q('a factor of 6', lambda x: 6 % x == 0)],
      h=30, ln=[('Favourable', '{ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }'), ('P =', '')]),
]
std_p2 = [
    R('one counter is taken at random from this bag. Find each probability.', 3, [
        Q('Find P(red).', '', show(cnt(BAG, 'red'), NB)),
        Q('Find P(blue).', '', show(cnt(BAG, 'blue'), NB)),
        Q('Find P(red or green).', '', show(cnt(BAG, 'red', 'green'), NB)),
    ], h=24, ln=[('Favourable', ''), ('Total', ''), ('P =', '')],
      info=bag(BAG, 22) + '<span class="cap">5 red, 3 blue and 4 green counters. Count them!</span>'),
    R('write each probability as a fraction, a decimal and a percentage.', 3, [
        Q('A coin is tossed. P(tails)', coin('T', 8, 'silver'), f'{fr(Fr(1, 2))} = 0.5 = 50%'),
        Q('This spinner is spun. P(red)', spinner(S('red', 'blue', 'green', 'yellow'), 10), f'{fr(Fr(1, 4))} = 0.25 = 25%'),
        Q('One tile is chosen. P(an F)', tiles('KINGSCLIFF', 3.6), show('KINGSCLIFF'.count('F'), 10, 'all')),
    ], h=34, ln=[('Fraction', ''), ('Decimal', ''), ('Percentage', '')]),
    R('one card is taken at random from a standard deck. Find each probability.', 3, [
        Q('Find P(an ace).', '', show(4, 52)),
        Q('Find P(a heart).', '', show(13, 52)),
        Q('Find P(a red card).', '', show(26, 52)),
    ], h=22, ln=[('Favourable', ''), ('P =', '')],
      info=deck(66) + '<span class="cap">52 cards: 4 suits of 13. Hearts and diamonds are red. J, Q, K are picture cards (shaded).</span>'),
    R('one lolly is taken at random from this jar. Give each answer in the form asked.', 3, [
        Q('P(green), as a decimal', '', show(cnt(JAR, 'green'), NJ, 'dec')),
        Q('P(yellow), as a percentage', '', show(cnt(JAR, 'yellow'), NJ, 'pct')),
        Q('P(red or blue), as a fraction', '', show(cnt(JAR, 'red', 'blue'), NJ)),
    ], h=22, ln=[('Working', ''), ('Answer', '')],
      info=jar(JAR, 22) + '<span class="cap">6 red, 3 green, 9 yellow and 2 blue lollies: 20 in total.</span>'),
]

JB = [('yellow', 4), ('red', 3), ('green', 6), ('black', 3)]
primes15 = [x for x in range(1, 16) if x in PRIMES]
STD = dict(
    rem1=f'P(E) = {F("number of favourable outcomes", "total number of outcomes")} · simplify: divide the top and bottom by the same number · a die: {{1, 2, 3, 4, 5, 6}}',
    p1=std_p1,
    rem2='count every counter, lolly or card · ‘or’ means add the counts · decimal: top ÷ bottom · percentage: × 100%',
    p2=std_p2,
    rem3='P(E) = favourable ÷ total · picture cards: J, Q, K · answer in the form the question asks for',
    p3=[
        Q('One jelly bean is taken at random. Find P(green or black).', bag(JB, 15), show(cnt(JB, 'green', 'black'), sum(k for _, k in JB))),
        Q(f'Write {F(3, 8)} as a decimal and as a percentage.', '', f'{dec(Fr(3, 8))} and {pct(Fr(3, 8))}', tag='Year 7'),
        Q('A whole number from 1 to 15 is chosen at random. Find P(a prime number).', number_cards(range(1, 9), 3.8) + number_cards(range(9, 16), 3.8),
          f'{setstr(primes15)}: {show(len(primes15), 15)}'),
        Q('One tile is chosen at random. Find P(an S).', tiles('SUCCESS', 5), show('SUCCESS'.count('S'), 7)),
        Q('A die is rolled. Find P(rolling at least 3).', die3d(10, 3, 4, 2), f'{{3, 4, 5, 6}}: {show(4, 6)}', tag='Extension'),
        Q('500 raffle tickets are sold at the school fete. Mia buys 8. Find P(Mia wins first prize), as a percentage.', raffle('0427', 18), show(8, 500, 'pct')),
    ],
    word=[
        Q('An Esky has 8 lemonade, 5 orange and 2 lime cans. Find P(lemonade). How many cola cans must be added so that P(lemonade) = ' + F(1, 2) + '?', '',
          f'{show(8, 15)}. Add 1 cola: then 8 of the 16 cans are lemonade.'),
        Q('Malik has 20 cards: five 5s, four 6s, eight 7s and three 8s. Lara takes one at random. Write P(a 7) as a fraction, decimal and percentage. Then find P(an even number).', '',
          f'P(7) = {show(8, 20, "all")}. P(even) = {show(4 + 3, 20, "all")}.'),
        Q('The probability that a day in April is rainy is 30%. About how many rainy days are expected in April (30 days)?', weather('30%', 13),
          f'30% × 30 = {Fr(30, 100) * 30} days'),
    ],
)
assert Fr(8, 16) == Fr(1, 2)

# ---------------------------------------------------------------- extension
d10 = list(range(1, 11))
ext_p1 = [
    R('find P(blue) in simplest form. For unequal sectors, compare the sizes.', 4, [
        blue_q(S('blue', 'red', 'blue', 'yellow', 'red', 'blue')),
        blue_q(S('blue', 'red', 'green', 'blue', 'yellow', 'red', 'green', 'blue', 'red', 'yellow')),
        blue_q([('blue', 2, None), ('red', 1, None), ('green', 1, None)]),
        blue_q([('blue', 1, None), ('red', 3, None)]),
    ], h=32, ln=[('Working', ''), ('P(blue)', '')]),
    R('a 10-sided die numbered 1 to 10 is rolled. Find each probability as a decimal.', 4, [
        Q(f'P(a prime number)', poly_die(12, 7, 9), show(len([x for x in d10 if x in PRIMES]), 10, 'dec')),
        Q(f'P(a multiple of 3)', poly_die(12, 3, 9), show(len([x for x in d10 if x % 3 == 0]), 10, 'dec')),
        Q(f'P(a factor of 10)', poly_die(12, 5, 9), show(len([x for x in d10 if 10 % x == 0]), 10, 'dec')),
        Q(f'P(at least 8)', poly_die(12, 9, 9), show(len([x for x in d10 if x >= 8]), 10, 'dec')),
    ], h=30, ln=[('Favourable', '{ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }'), ('P =', '')]),
]
nb_pic = len(card_p(lambda c: c[1] not in RED and c[0] in PICTURE)[0])
n_even = len(card_p(lambda c: c[0] in {'2', '4', '6', '8', '10'})[0])
n_2to5 = len(card_p(lambda c: c[0] in {'2', '3', '4', '5'})[0])
mb = dict(MONEY)
ext_p2 = [
    R('one card is taken at random from a standard deck. Find each probability in simplest form.', 3, [
        Q('P(a black picture card)', '', show(nb_pic, 52)),
        Q('P(a card with an even number)', '', show(n_even, 52)),
        Q('P(a card from 2 to 5, inclusive)', '', show(n_2to5, 52)),
    ], h=22, ln=[('Working', ''), ('P =', '')],
      info=deck(66) + '<span class="cap">J, Q, K are picture cards (shaded). An ace is not a number card here.</span>'),
    R('one coin falls out of the money box from Example 2 at random. Give each answer in the form asked.', 3, [
        Q('P(a 10c or 20c coin), as a percentage', '', show(mb['10c'] + mb['20c'], NCOINS, 'pct')),
        Q('P(a coin worth less than $1), as a percentage', '', show(mb['50c'] + mb['20c'] + mb['10c'], NCOINS, 'pct')),
        Q('P(a coin worth at least 50c), as a decimal', '', show(mb['$2'] + mb['$1'] + mb['50c'], NCOINS, 'dec')),
    ], h=24, ln=[('Working', ''), ('Answer', '')], info=money_box(MONEY, 52) + '<span class="cap">20 coins in the money box.</span>'),
    R('find the missing number. Show your working.', 3, [
        Q(f'A bag has 6 red counters and some blue ones. P(red) = {F(1, 3)}. How many blue counters?', '', f'total = 6 ÷ {fr(Fr(1, 3))} = 18, so {18 - 6} blue'),
        Q('A spinner has 12 equal sectors. P(green) = 0.25. How many sectors are green?', '', f'0.25 × 12 = {Fr(1, 4) * 12}'),
        Q(f'8K has 25 students. For a student chosen at random, P(plays a sport) = {F(3, 5)}. How many play a sport?', '', f'{fr(Fr(3, 5))} × 25 = {Fr(3, 5) * 25}'),
    ], h=30, ln=LN_A2),
    R('write each probability as a fraction, a decimal and a percentage. Round decimals to 2 places if needed.', 3, [
        Q('One tile from P R O B A B I L I T Y: P(a vowel)', '', f'{show(4, 11)} ≈ {dec(Fr(4, 11), 2)} ≈ {pct(Fr(4, 11), 1)} (vowels O, A, I, I)'),
        Q('A whole number from 1 to 40: P(a multiple of 8)', '', show(len([x for x in range(1, 41) if x % 8 == 0]), 40, 'all')),
        Q('A month chosen at random: P(it starts with J)', '', show(3, 12, 'all')),
    ], h=26, ln=[('Fraction', ''), ('Decimal', ''), ('Percentage', '')]),
]
assert sum(1 for c in 'PROBABILITY' if c in 'AEIOU') == 4
assert Fr(6, 18) == Fr(1, 3)

heart_or_pic = len(card_p(lambda c: c[1] == 'H' or c[0] in PICTURE)[0])
murw = 'MURWILLUMBAH'
n_LM = sum(1 for c in murw if c in 'LM')
ANG = [('red', 180, None), ('blue', 90, None), ('green', 60, None), ('yellow', 30, None)]
digits = [1, 3, 5, 8]
import itertools
nums = [int(''.join(map(str, p))) for p in itertools.permutations(digits)]
P_odd = Fr(sum(1 for n in nums if n % 2), len(nums))
P_gt = Fr(sum(1 for n in nums if n > 5000), len(nums))
P_5 = Fr(sum(1 for n in nums if str(n)[0] == '5'), len(nums))
kai = [x for x in range(1, 21) if x % 3 == 0 or x % 4 == 0]


def add_for(target, have, others):
    # x extra cans of a NEW type so that have/(total+x) = target  (have is cola count = x)
    for x in range(0, 200):
        if Fr(x, others + x) == target:
            return x


def add_more(target, count, total):
    # add x cans of other kinds so that count/(total + x) = target
    for x in range(0, 200):
        if Fr(count, total + x) == target:
            return x


x_cola = add_for(Fr(2, 5), 0, 15)
x_orange = add_more(Fr(1, 4), 5, 15)
assert (x_cola, x_orange) == (10, 5)

EXT = dict(
    rem1=STD['rem1'],
    p1=ext_p1,
    rem2='‘or’ with no overlap: add the counts · decimal: top ÷ bottom · percentage: × 100% · missing total = count ÷ probability',
    p2=ext_p2,
    rem3='P(E) = favourable ÷ total · if the total changes, the probability changes · never count an outcome twice',
    p3=[
        Q('An Esky has 8 lemonade, 5 orange and 2 lime cans. How many cola cans must be added so that P(cola) = ' + F(2, 5) + '?', esky([('yellow', 'lemon', 8), ('orange', 'orange', 5), ('green', 'lime', 2)], 26),
          f'Add {x_cola} colas: {frs(x_cola, 15 + x_cola)} = {fr(Fr(2, 5))}'),
        Q('Start again with the Esky in Q1. How many cola cans must be added so that P(orange) = 0.25?', '',
          f'Add {x_orange}: {frs(5, 15 + x_orange)} = 0.25'),
        Q('One card from a standard deck. Find P(a heart or a picture card). Careful: don’t count any card twice.', cards(['KH', '7H', 'QS'], 13),
          f'13 hearts + 9 other picture cards = {heart_or_pic}: {show(heart_or_pic, 52)}'),
        Q('One tile is chosen at random. Find P(an L or an M).', tiles(murw, 3.4), show(n_LM, len(murw))),
        Q('The spinner’s angles are 180° red, 90° blue, 60° green and 30° yellow. Find P(green) and P(yellow).', spinner(ANG, 14),
          f'P(green) = {frs(60, 360)} = {fr(spin_p(ANG, "green"))}; P(yellow) = {frs(30, 360)} = {fr(spin_p(ANG, "yellow"))}'),
        Q('A bag holds 40 marbles and P(red) = 0.35. How many red marbles are there? How many are not red?', '',
          f'0.35 × 40 = {Fr(35, 100) * 40} red; {40 - Fr(35, 100) * 40} not red'),
    ],
    word=[
        Q('The digits 1, 3, 5 and 8 are each used once to make a 4-digit number at random. Find P(it starts with 5), P(it is odd) and P(it is more than 5000).', '',
          f'{fr(P_5)}, {fr(P_odd)}, {fr(P_gt)} (the first digit is 5 or 8; the last digit is 1, 3 or 5)'),
        Q(f'A jar holds 60 lollies. P(red) = {F(1, 4)} and P(green) = {F(1, 3)}; the rest are yellow. How many yellow lollies are there? Find P(yellow).', '',
          f'red 15, green 20, so yellow {60 - 15 - 20}: P(yellow) = {show(25, 60)}'),
        Q('Kai picks a whole number from 1 to 20 at random. Kai wins on a multiple of 3 or a multiple of 4. Find P(Kai wins).', '',
          f'{setstr(kai)}: {show(len(kai), 20)} (12 is counted once)'),
    ],
)
assert (P_5, P_odd, P_gt) == (Fr(1, 4), Fr(3, 4), Fr(1, 2))
assert heart_or_pic == 22

LESSON = dict(key='L2', num='2', title='Probability of an event', sub=SUB, alt=True,
              li='find the probability of an event when the outcomes are equally likely, and write it as a fraction, decimal and percentage.',
              sc=['count the favourable outcomes and the total outcomes.',
                  'use P(E) = favourable ÷ total, and simplify.',
                  'write a probability as a fraction, a decimal and a percentage.'],
              notes=NOTES, ex1=EX1, ex2=EX2, std=STD, ext=EXT)
