from engine import Q, R, LN_W, LN_A, LN_A2
from gfx import *
from pm import *
from layout import F

SUB = 'Probability • MA4-PRO-C-01'
BR = '{ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }'


def S(*cols):
    return [(c, 1, None) for c in cols]


def show(fav, tot, form='frac', dp=None):
    p = Fr(fav, tot)
    base = frs(fav, tot) + (f' = {fr(p)}' if p.denominator != tot else '')
    if form == 'dec':
        return base + f' = {dec(p, dp)}'
    if form == 'pct':
        return base + f' = {pct(p, dp)}'
    return base


def comp(p):
    return 1 - Fr(p)


NOTES = f'''<div class="tnotes" style="grid-template-columns:1.1fr 1fr 1fr">
<div><h4>KEY TERMS</h4>
<p><b>complement of E</b> (‘not E’): every outcome in the sample space that is <i>not</i> in E</p>
<p><b>complementary events:</b> E and not E. Together they make the whole sample space, with no overlap.</p>
<p>Careful: the complement of ‘winning’ is ‘not winning’ (losing <i>or</i> drawing), not just ‘losing’.</p></div>
<div><h4>FORMULA</h4>
<div class="fbox">P(E) + P(not E) = 1</div>
<div class="fbox">P(not E) = 1 − P(E)</div>
<p>with percentages: P(not E) = 100% − P(E)</p>
<p>The probabilities of <b>all</b> the outcomes add to 1.</p></div>
<div><h4>DIAGRAM</h4>
<div style="display:flex;gap:2mm;align-items:center">{venn_one('{5, 6}', '{1, 2, 3, 4}', 'E', 25, 'not E')}
<p style="margin:0">die: E = {{5, 6}}<br>P(E) = {frs(2, 6)} = {fr(Fr(1, 3))}<br>P(not E) = 1 − {fr(Fr(1, 3))} = {fr(Fr(2, 3))}</p></div></div>
</div>'''

EX1 = dict(
    instr='Write the complement (the ‘not’ event), then find the probabilities.',
    parts=[
        ('Complement', die3d(11, 6, 6, 6), 'A die is rolled. Write the complement of ‘rolling a 6’ and list its outcomes.'),
        ('Cards', '', 'A pack has 10 red, 6 yellow and 4 green cards. One card is taken without looking. Find P(yellow) and P(not yellow).'),
        ('Decimal', weather('15%', 13), 'The probability of rain is 0.15. Find the probability of no rain.'),
        ('Diagram', venn_one('', '', 'E', 24, 'not E'), 'A die is rolled. E = ‘an even number’. Write the outcomes in the diagram, then find P(not E).'),
    ], box=16,
    ans=['Not rolling a 6: {1, 2, 3, 4, 5}.',
         f'P(yellow) = {show(6, 20)}; P(not yellow) = 1 − {fr(Fr(3, 10))} = {fr(comp(Fr(3, 10)))}',
         f'1 − 0.15 = {dec(comp(Fr(15, 100)))}',
         f'E: {{2, 4, 6}}; not E: {{1, 3, 5}}. P(not E) = {fr(Fr(1, 2))}'])

EX2 = dict(
    instr='Use P(not E) = 1 − P(E). Give each answer in the same form as the question.',
    parts=[
        ('Percentage', '', 'A golfer sinks 74% of putts. Find the probability that the golfer misses a putt.'),
        ('Missing value', '', 'A bag holds only red, blue and white toy cars. P(red) = 0.4 and P(white) = 0.25. Find P(blue).'),
        ('Choose', '', 'Which is the complement of ‘winning a race’? A coming last B coming second C not winning D coming 2nd or 3rd'),
        ('Raffle', raffle('0731', 18), '1000 raffle tickets are sold and Tahnee buys 5. Find the probability that Tahnee does not win.'),
    ], box=17,
    ans=['100% − 74% = 26%', f'1 − 0.4 − 0.25 = {dec(1 - Fr(4, 10) - Fr(25, 100))}', 'C (not winning)',
         f'1 − {frs(5, 1000)} = {frs(995, 1000)} = {fr(Fr(995, 1000))}'])


def spin_comp(secs):
    p = spin_p(secs, 'blue')
    return Q('Find P(blue) and P(not blue).', spinner(secs, 12), ans=f'P(blue) = {fr(p)}, P(not blue) = {fr(comp(p))}; {fr(p)} + {fr(comp(p))} = 1')


# ---------------------------------------------------------------- standard
BOOKS = [('M', 'blue'), ('M', 'blue'), ('M', 'blue'), ('H', 'red'), ('H', 'red'), ('S', 'yellow')]
std_p1 = [
    R('the complement of an event is everything else that could happen. Write the complement of each event.', 4, [
        Q('A coin is tossed. Write the complement of ‘tossing tails’.', '', 'Tossing heads'),
        Q('A die is rolled. Write the complement of ‘rolling a 6’.', '', 'Not rolling a 6 (rolling 1, 2, 3, 4 or 5)'),
        Q('Write the complement of ‘tomorrow is a cloudy day’.', '', 'Not a cloudy day tomorrow'),
        Q('A box has white and dark chocolates. Write the complement of ‘a white chocolate’.', '', 'Choosing a dark chocolate'),
    ], h=25, ln=[('Complement', ''), ('', '')]),
    R('each spinner is spun once. Find P(blue) and P(not blue). Then check that the two add to 1.', 4,
      [spin_comp(S('blue', 'red', 'yellow', 'green')), spin_comp(S('blue', 'red', 'blue')),
       spin_comp(S('blue', 'red', 'yellow', 'green', 'red')), spin_comp(S('blue', 'blue', 'red', 'yellow', 'green', 'blue'))],
      h=30, ln=[('P(blue) =', ''), ('P(not blue) =', ''), ('Check', '___ + ___ = 1')]),
]
mult3 = [x for x in range(1, 11) if x % 3 == 0]
std_p2 = [
    R('a fair die is rolled once. List the outcomes that are NOT the given number(s), then find the probability.', 3, [
        Q('Find the probability of not rolling a 3.', die3d(9, 3, 1, 2), f'{{1, 2, 4, 5, 6}}: {show(5, 6)}'),
        Q('Find the probability of not rolling an even number.', die3d(9, 2, 4, 6), f'{{1, 3, 5}}: {show(3, 6)}'),
        Q('Find the probability of not rolling a prime number.', die3d(9, 1, 4, 6), f'{{1, 4, 6}} (1 is not prime): {show(3, 6)}'),
    ], h=28, ln=[('Outcomes', BR), ('Probability', '')]),
    R('use P(not E) = 1 − P(E). Give your answer in the same form as the question (percentage, decimal or fraction).', 3, [
        Q('The probability of rain this weekend is 85%. Find the probability of no rain.', '', '100% − 85% = 15%'),
        Q('The probability that a carton has a broken egg is 0.1. Find the probability that it has no broken eggs.', '', f'1 − 0.1 = {dec(comp(Fr(1, 10)))}'),
        Q(f'The probability of choosing a jack from a deck is {F(1, 13)}. Find the probability of not choosing a jack.', '', f'1 − {fr(Fr(1, 13))} = {fr(comp(Fr(1, 13)))}'),
    ], h=25, ln=[('Working', ''), ('Answer', '')]),
    R('one book is taken from this shelf without looking. Find each probability as a fraction.', 3, [
        Q('Find the probability that it is a history book.', '', show(2, 6)),
        Q('Find the probability that it is not a history book.', '', f'1 − {fr(Fr(1, 3))} = {fr(Fr(2, 3))}'),
        Q('Find the probability that it is not a science book.', '', '1 (there are no science books, so it is certain)'),
    ], h=22, ln=[('Working', ''), ('Answer', '')],
      info=books(BOOKS, 15) + '<span class="cap">3 maths (M), 2 history (H) and 1 sport (S) book.</span>'),
    R('show an event and its complement in a diagram, and use the fact that all the probabilities add to 1.', 3, [
        Q('A number from 1 to 10 is chosen. E = ‘a multiple of 3’. Write the outcomes of E inside the circle and the outcomes of not E outside it.', venn_one('', '', 'E', 28, 'not E'),
          f'E: {setstr(mult3)}; not E: {setstr([x for x in range(1, 11) if x not in mult3])}', ln=[]),
        Q('Use your diagram from Question 18. Find P(E) and P(not E).', '', f'P(E) = {fr(Fr(3, 10))}, P(not E) = {fr(Fr(7, 10))}'),
        Q('Kingscliff’s netball team can win, draw or lose. P(win) = 0.6 and P(draw) = 0.1. Find P(lose).', '', f'1 − 0.6 − 0.1 = {dec(1 - Fr(6, 10) - Fr(1, 10))}'),
    ], h=30, ln=[('Working', ''), ('Answer', '')]),
]

JB = [('red', 40), ('blue', 25), ('black', 50), ('white', 15)]
NJB = sum(k for _, k in JB)
cnt = lambda *cs: sum(k for c, k in JB if c in cs)
STD = dict(
    rem1='The complement of E is ‘not E’: every other outcome. P(E) + P(not E) = 1, so P(not E) = 1 − P(E).',
    p1=std_p1,
    rem2=f'P(not E) = 1 − P(E). With percentages: 100% − P(E). Decimals: 1 − 0.15 = 0.85. Fractions: 1 − {F(1, 4)} = {F(3, 4)}.',
    p2=std_p2,
    rem3='P(not E) = 1 − P(E). ‘Not blue and not black’ means any colour except blue or black. All the probabilities add to 1.',
    p3=[
        Q('A car park has 450 cars, 100 motorbikes and 10 buses. One vehicle is picked at random. Find the probability that it is not a car.', '',
          f'1 − {frs(450, 560)} = {frs(110, 560)} = {fr(Fr(110, 560))}'),
        Q(f'Work out: 1 − {F(3, 8)}, then 1 − 0.37, then 100% − 64%.', '', f'{fr(comp(Fr(3, 8)))}, {dec(comp(Fr(37, 100)))}, 36%', tag='Year 7'),
        Q('A jar has 40 red, 25 blue, 50 black and 15 white jelly beans. One is taken without looking. Find the probability that it is not white.', '',
          f'1 − {frs(15, NJB)} = {show(NJB - cnt("white"), NJB)}'),
        Q('Use the jar in Question 3. Find the probability that the jelly bean is not blue and not black.', '',
          f'blue or black = 75, so not = {show(NJB - cnt("blue", "black"), NJB)}'),
        Q('A mobile phone number is picked at random. Find the probability that its last digit is not 0 or 1. Write it as a decimal.', '',
          show(8, 10, 'dec')),
        Q('One tile is picked without looking. Find the probability that it is not a vowel.', tiles('PROBABILITY', 3.6), f'7 consonants: {show(7, 11)}'),
    ],
    word=[
        Q('A bag holds only red, blue and white toy cars. P(red) = 0.4 and P(white) = 0.25. (a) Find P(blue). (b) The bag holds 40 cars. How many of each colour are there?', '',
          f'P(blue) = 0.35. Red {Fr(4, 10) * 40}, white {Fr(25, 100) * 40}, blue {Fr(35, 100) * 40}.'),
        Q('In this game, you win if your coin lands in a yellow square of the 5 × 5 grid. Throws that miss the grid are taken again. Find P(winning) and P(not winning).', grid_game(size=16),
          f'P(win) = {fr(Fr(7, 25))}, P(not win) = {fr(Fr(18, 25))}'),
        Q('Sue and Liam are in Year 8; Emily and Matt are in Year 9. One of the four is picked at random to be captain. Find P(not Emily), P(the captain is in Year 8) and P(the captain is the teacher).', '',
          f'{fr(Fr(3, 4))}, {fr(Fr(1, 2))}, 0'),
    ],
)
assert Fr(110, 560) == Fr(11, 56)

# ---------------------------------------------------------------- extension


def die_pair(text, pred):
    fav, p = die_p(pred)
    return Q(f'E is ‘rolling {text}’. Find P(E) and P(not E).', die3d(9, 1, 5, 3), f'P(E) = {fr(p)}, P(not E) = {fr(comp(p))}')


ext_p1 = [
    R('write the complement of each event. Make sure it includes every other possible outcome.', 4, [
        Q('Write the complement of ‘winning a hockey game’.', '', 'Not winning: losing or drawing'),
        Q('Write the complement of ‘being born in winter’.', '', 'Being born in spring, summer or autumn'),
        Q('Write the complement of ‘being under 15 years old’.', '', 'Being 15 years old or older'),
        Q('A card is drawn from a deck. Write the complement of ‘a heart’.', '', 'Choosing a diamond, club or spade'),
    ], h=24, ln=[('Complement', ''), ('', '')]),
    R('a fair die is rolled once. Find P(E) and P(not E) for each event E.', 4, [
        die_pair('a number greater than 1', lambda x: x > 1), die_pair('a number less than 5', lambda x: x < 5),
        die_pair('a multiple of 3', lambda x: x % 3 == 0), die_pair('a number greater than 6', lambda x: x > 6),
    ], h=28, ln=[('P(E) =', ''), ('P(not E) =', '')]),
]
pv = sum(1 for c in 'PROBABILITY' if c in 'AEIOU')
ext_p2 = [
    R('each probability is given. Write the probability that the event does NOT happen.', 3, [
        Q(f'P(choosing a jack from a deck) = {F(1, 13)}. Find P(not choosing a jack).', '', fr(comp(Fr(1, 13)))),
        Q('P(shooting a goal) = 61%. Find P(missing).', '', '39%'),
        Q('P(winning a prize) = 0.15. Find P(not winning a prize).', '', dec(comp(Fr(15, 100)))),
    ], h=20, ln=LN_A),
    R('a jar has 40 red, 25 blue, 50 black and 15 white jelly beans. One is taken without looking. Find each probability in simplest form.', 3, [
        Q('Find the probability that it is not yellow.', '', '1 (there are no yellow jelly beans)'),
        Q('Find the probability that it is not red.', '', f'1 − {frs(40, NJB)} = {show(NJB - 40, NJB)}'),
        Q('Find the probability that it is not black.', '', f'1 − {frs(50, NJB)} = {show(NJB - 50, NJB)}'),
    ], h=24, ln=[('Working', ''), ('Answer', '')]),
    R('the probabilities of all the outcomes add to 1. Find the missing probability.', 3, [
        Q('Tomorrow will be sunny, cloudy or rainy. P(sunny) = 0.45 and P(cloudy) = 0.3. Find P(rainy).', '', dec(1 - Fr(45, 100) - Fr(3, 10))),
        Q(f'A spinner is red, blue or green. P(red) = {F(1, 3)} and P(blue) = {F(1, 4)}. Find P(green).', '', f'1 − {fr(Fr(1, 3))} − {fr(Fr(1, 4))} = {fr(1 - Fr(1, 3) - Fr(1, 4))}'),
        Q('A netball team can win, draw or lose. P(win) = 55% and P(draw) = 5%. Find P(lose).', '', '40%'),
    ], h=24, ln=[('Working', ''), ('Answer', '')]),
    R('one tile is picked from P R O B A B I L I T Y without looking. Find each probability.', 3, [
        Q('Find the probability that it is not a P.', '', show(10, 11)),
        Q('Find the probability that it is not a vowel.', '', show(11 - pv, 11)),
        Q('Find the probability that it is not a B.', '', f'B is on 2 tiles, so {show(9, 11)}'),
    ], h=22, ln=[('Working', ''), ('Answer', '')], info=tiles('PROBABILITY', 7)),
]


def solve_red():
    # P(red) = 2 P(blue), P(green) = 0.1, total 1
    b = (1 - Fr(1, 10)) / 3
    return 2 * b


EXT = dict(
    rem1='The complement must include every other outcome. P(E) + P(not E) = 1.',
    p1=ext_p1,
    rem2='P(not E) = 1 − P(E). All the probabilities add to 1. ‘Not A and not B’ means every outcome except A and B.',
    p2=ext_p2,
    rem3='P(E) + P(not E) = 1. When one probability is a multiple of another, write an equation.',
    p3=[
        Q(f'A car park has 450 cars, 100 motorbikes and 10 buses. One vehicle is picked at random. Which is P(not a car)? <span class="opts"><span><b>A</b>{F(45, 56)}</span><span><b>B</b>{F(110, 450)}</span><span><b>C</b>{F(10, 560)}</span><span><b>D</b>{F(11, 56)}</span></span>', '',
          f'D ({frs(110, 560)} = {fr(Fr(110, 560))})'),
        Q('A spinner is only red, blue or green. P(red) is twice P(blue), and P(green) = 0.1. Find P(red).', '',
          f'3 × P(blue) = 0.9, so P(blue) = 0.3 and P(red) = {dec(solve_red())}'),
        Q('The probability that a train is on time is 0.83. Find the probability that it is not on time. Write it as a percentage.', '', '1 − 0.83 = 0.17 = 17%'),
        Q('A bag holds 50 counters. P(not red) = 0.64. How many red counters are in the bag?', '', f'P(red) = 0.36; 0.36 × 50 = {Fr(36, 100) * 50}'),
        Q('A 2-digit number (10 to 99) is picked at random. Find the probability that it is not a multiple of 10.', '',
          f'90 numbers, 9 multiples of 10: {show(81, 90)}'),
        Q('Can P(E) = 0.7 and P(not E) = 0.4 for the same event? Explain.', '', 'No. P(E) + P(not E) must be 1, but 0.7 + 0.4 = 1.1.'),
    ],
    word=[
        Q('A bag of 40 toy cars holds only red, blue and white cars. P(red) = 0.4 and P(white) = 0.25. How many cars of each colour are there? What is the probability of a pink car?', '',
          f'Red {Fr(4, 10) * 40}, white {Fr(25, 100) * 40}, blue {Fr(35, 100) * 40}. P(pink) = 0.'),
        Q('A raffle sells 800 tickets for one prize. Jai buys some tickets. The probability that Jai does not win is 0.985. How many tickets did Jai buy?', '',
          f'P(win) = 0.015; 0.015 × 800 = {Fr(15, 1000) * 800} tickets'),
        Q('The grid game has 7 yellow squares out of 25. How many more squares must be coloured yellow so that P(not winning) = 0.6?', grid_game(size=15),
          f'P(win) = 0.4 needs 0.4 × 25 = 10 yellow, so 3 more'),
    ],
)
assert solve_red() == Fr(3, 5)
assert sum(1 for x in range(10, 100) if x % 10) == 81

LESSON = dict(key='L3', num='3', title='Complementary events', sub=SUB,
              li='identify the complement of an event, and use P(not E) = 1 − P(E) to solve problems.',
              sc=['write the complement of an event.',
                  'show that P(E) + P(not E) = 1.',
                  'use P(not E) = 1 − P(E) with fractions, decimals and percentages.'],
              notes=NOTES, ex1=EX1, ex2=EX2, std=STD, ext=EXT)
