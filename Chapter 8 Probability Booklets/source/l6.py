from engine import Q, R, LN_W, LN_A, LN_A2
from gfx import *
from pm import *
from layout import F
from l5 import VINH_SP, VINH, MATCH, MATCH_TAB, DIE80, DIE80_TAB, DECL, DECL_TAB, SUMS, SUMS_TAB, NS, VINH_TAB

SUB = 'Probability • MA4-PRO-C-01'


def show(fav, tot, form='frac', dp=None):
    p = Fr(fav, tot)
    base = frs(fav, tot) + (f' = {fr(p)}' if p.denominator != tot else '')
    if form == 'dec':
        return base + f' = {dec(p, dp)}'
    return base


def num(x, dp=1):
    x = Fr(x)
    return str(x.numerator) if x.denominator == 1 else dec(x, dp)


def E(p, n, dp=1):
    """expected frequency working: P x n = answer"""
    v = Fr(p) * n
    return f'{fr(p)} × {n} = {num(v, dp)}'


NOTES = f'''<div class="tnotes" style="grid-template-columns:1.05fr 1.05fr 1fr">
<div><h4>KEY TERMS</h4>
<p><b>expected frequency:</b> the number of times we expect an event to happen in a number of trials</p>
<p><b>observed frequency:</b> the number of times it actually happened</p>
<p><b>fair:</b> every outcome equally likely; <b>biased:</b> not fair</p>
<p>Observed and expected are rarely exactly equal. A big difference over many trials suggests bias.</p></div>
<div><h4>FORMULA</h4>
<div class="fbox">expected frequency = probability × number of trials</div>
<p>From data, use the observed probability: 15 twos in 60 rolls → {F(1, 4)} × 500 = 125 twos in 500 rolls.</p>
<p>It need not be a whole number: {F(1, 6)} × 80 ≈ 13.3</p></div>
<div><h4>EXAMPLE</h4>
<p>Declan rolls a die 60 times. Expected 5s or 6s:</p>
<p>P(5 or 6) = {frs(2, 6)} = {fr(Fr(1, 3))}</p>
<p>expected = {fr(Fr(1, 3))} × 60 = 20</p>
<p>observed = 8 + 11 = 19: close to 20, so the die seems fair.</p></div>
</div>'''

EX1 = dict(
    instr='Expected frequency = probability × number of trials.',
    parts=[
        ('Coin', coin('H', 10), 'A coin is tossed 50 times. Find the expected number of heads.'),
        ('Die', die3d(12, 4, 2, 6), 'A die is rolled 72 times. Find the expected number of 4s.'),
        ('Spinner', spinner(VINH_SP, 14), 'Vinh spins 80 times. Find the expected number of reds. He got 44: compare.'),
        ('Rain', weather('30%', 14), 'P(rain on an April day) = 30%. Find the expected number of rainy days in April.'),
    ], box=17,
    ans=[E(Fr(1, 2), 50), E(Fr(1, 6), 72), f'{E(Fr(1, 2), 80)}; 44 is 4 more than expected.', f'0.3 × 30 = {Fr(3, 10) * 30} days'])

EX2 = dict(
    instr='Use theoretical probability when the outcomes are equally likely; otherwise use the observed probability.',
    parts=[
        ('From data', die3d(11, 2, 2, 2), 'Harper’s die: 15 twos in 60 rolls. Using this, how many 2s are expected in 500 rolls?'),
        ('Matchboxes', '', '20 of 50 sample boxes held exactly 50 matches. How many of 1000 boxes would you expect to?'),
        ('Not whole', '', 'A die is rolled 80 times. Find the expected number of 6s. It came up 22 times: comment.'),
        ('Lollies', '', 'P(red) = 0.5, P(green) = 0.2, P(purple) = 0.3. How many of each colour would you expect in a bag of 100?'),
    ], box=17,
    ans=[E(Fr(15, 60), 500), E(Fr(20, 50), 1000), f'{fr(Fr(1, 6))} × 80 ≈ {dec(Fr(80, 6), 1)}. 22 is far more: the die may be biased.', 'red 50, green 20, purple 30'])

# ---------------------------------------------------------------- standard
EXP_LN = [('P(E)', ''), ('× trials', ''), ('Expected', '')]
std_p1 = [
    R('find each expected frequency: probability × number of trials.', 4, [
        Q('A coin is tossed 100 times. Expected number of heads?', coin('H', 8), E(Fr(1, 2), 100)),
        Q('A die is rolled 60 times. Expected number of 6s?', die3d(9, 6, 6, 6), E(Fr(1, 6), 60)),
        Q('This spinner is spun 40 times. Expected number of blues?', spinner([('blue', 1, None), ('red', 1, None), ('green', 1, None), ('yellow', 1, None)], 10), E(Fr(1, 4), 40)),
        Q('A die is rolled 30 times. Expected number of even numbers?', die3d(9, 2, 4, 6), E(Fr(1, 2), 30)),
    ], h=31, ln=EXP_LN),
    R('Vinh’s spinner (half red, a quarter green, a quarter yellow) was spun 80 times: red 44, green 25, yellow 11.', 4, [
        Q('Find the expected number of reds.', '', E(Fr(1, 2), 80)),
        Q('Find the expected number of yellows.', '', E(Fr(1, 4), 80)),
        Q(f'Red came up {VINH["red"]} times. Is that more or less than expected? By how many?', '', f'More, by {VINH["red"] - 40}'),
        Q(f'Yellow came up {VINH["yellow"]} times. Compare it with the expected number.', '', f'{20 - VINH["yellow"]} fewer than expected'),
    ], h=24, ln=[('Working', ''), ('Answer', '')]),
]
std_p2 = [
    R('a fair die is rolled 72 times. Find each expected frequency.', 3, [
        Q('Expected number of 4s', '', E(Fr(1, 6), 72)),
        Q('Expected number greater than 2', '', E(Fr(4, 6), 72)),
        Q('Expected number of even numbers', '', E(Fr(3, 6), 72)),
    ], h=22, ln=[('Working', ''), ('Answer', '')]),
    R('use the observed probability to predict.', 3, [
        Q('A basketballer scores 7 of every 10 shots. How many goals are expected from 50 shots?', '', E(Fr(7, 10), 50)),
        Q('A surfer catches a wave on 3 of every 4 attempts. How many waves are expected from 60 attempts?', '', E(Fr(3, 4), 60)),
        Q('20 of 50 sample matchboxes held exactly 50 matches. How many of 250 boxes would you expect to?', '', E(Fr(20, 50), 250)),
    ], h=26, ln=[('Working', ''), ('Answer', '')]),
    R('Kingscliff weather records show that P(a summer day is above 30 °C) = 0.2.', 3, [
        Q('How many days above 30 °C are expected in a 90-day summer?', '', f'0.2 × 90 = {Fr(1, 5) * 90}'),
        Q('How many are expected in two weeks (14 days)?', '', f'0.2 × 14 = {dec(Fr(1, 5) * 14)}'),
        Q('Give a reason why the real number of hot days might be different.', '', 'Chance: the weather varies from year to year; 0.2 is only an estimate.'),
    ], h=24, ln=[('Working', ''), ('Answer', '')]),
    R('a coin experiment: observed against expected.', 3, [
        Q('Toss a coin 50 times (or use RanInt#(1,2), 1 = heads). Tally the results.',
          vtab(['Outcome', 'Tally', 'Frequency'], [['Heads', '', ''], ['Tails', '', ''], ['Total', '', '50']], 8.6).replace('<td></td>', '<td class="blank" style="min-width:24mm"></td>'),
          'Answers vary.', ln=[], span=2, figtop=True),
        Q('What is the expected number of heads in 50 tosses? Compare it with your observed frequency.', '', f'{E(Fr(1, 2), 50)}; comparison varies.'),
    ], h=32, ln=LN_A2),
]
STD = dict(
    rem1=f'expected frequency = probability × number of trials, e.g. {F(1, 6)} × 60 = 10',
    p1=std_p1,
    rem2='expected frequency = P × trials · from data: use the observed probability · it might not be a whole number',
    p2=std_p2,
    rem3='expected = P × trials · compare observed and expected: close suggests fair; far off over many trials suggests biased',
    p3=[
        Q('A die was rolled 80 times. Find the expected number of 6s, to 1 decimal place. Compare it with the observed number.', DIE80_TAB,
          f'{fr(Fr(1, 6))} × 80 ≈ {dec(Fr(80, 6), 1)}; 22 is much higher.', span=2, figtop=True),
        Q('Use Question 1. Do you think the die is biased? Explain.', '', 'Probably: 6 came up far more often than expected (22 compared with 13.3).'),
        Q('A fair die is rolled 100 times. Find the expected number of 3s, to 1 decimal place.', '', f'{fr(Fr(1, 6))} × 100 ≈ {dec(Fr(100, 6), 1)}'),
        Q('Find 35% of 240.', '', f'{Fr(35, 100) * 240}', tag='Year 7'),
        Q('41 of 50 sample matchboxes held at least 50 matches. How many of 1000 boxes would you expect to?', '', E(Fr(41, 50), 1000)),
    ],
    word=[
        Q('Declan rolled a die 60 times: 1 (10), 2 (11), 3 (13), 4 (7), 5 (8), 6 (11). Find the expected and observed number of 5s or 6s, and comment.', '',
          f'Expected {E(Fr(1, 3), 60)}; observed 8 + 11 = 19. Close, so the die seems fair.'),
        Q('A spinner has 5 equal sectors: 2 red, 2 blue, 1 green. Mel says she will get exactly 40 reds in 100 spins. Explain why she might not.', '',
          f'40 is the expected number ({E(Fr(2, 5), 100)}), but results vary by chance.'),
        Q('8 students each toss a coin 100 times. How many heads are expected in total? The class got 389 heads. Comment.', '',
          f'{E(Fr(1, 2), 800)}. 389 is close (observed P = {dec(Fr(389, 800), 3)}…).'),
    ],
)

# ---------------------------------------------------------------- extension
ext_p1 = [
    R('find each expected frequency.', 4, [
        Q('A die is rolled 300 times. Expected number of 6s?', die3d(9, 6, 6, 6), E(Fr(1, 6), 300)),
        Q('An 8-sided die has 2 red faces. It is rolled 200 times. Expected reds?', poly_die(8, 'R', 9), E(Fr(2, 8), 200)),
        Q('A card is drawn from a deck and replaced, 260 times. Expected hearts?', card('7', 'H', 7), E(Fr(13, 52), 260)),
        Q('P(rain) = 0.35 each day. Expected rainy days in 20 days?', weather('35%', 11), f'0.35 × 20 = {Fr(35, 100) * 20}'),
    ], h=32, ln=EXP_LN),
    R('Vinh’s spinner (½ red, ¼ green, ¼ yellow), 80 spins: red 44, green 25, yellow 11. Compare.', 4, [
        Q('Red: expected and observed?', '', f'expected {E(Fr(1, 2), 80)}; observed 44 (+4)'),
        Q('Green: expected and observed?', '', f'expected {E(Fr(1, 4), 80)}; observed 25 (+5)'),
        Q('Yellow: expected and observed?', '', f'expected {E(Fr(1, 4), 80)}; observed 11 (−9)'),
        Q('Is the spinner fair? Explain.', '', 'Possibly not: yellow came up far less than expected. More spins would show whether it is biased.'),
    ], h=24, ln=[('Working', ''), ('Answer', '')]),
]
ext_p2 = [
    R('a fair die is rolled 72 times. Find each expected frequency.', 3, [
        Q('Expected number of 4s', '', E(Fr(1, 6), 72)),
        Q('Expected number greater than 2', '', E(Fr(4, 6), 72)),
        Q('Expected number of primes', '', E(Fr(3, 6), 72)),
    ], h=20, ln=[('Working', ''), ('Answer', '')]),
    R('use the matchbox sample of 50 boxes to predict for 1000 boxes.', 3, [
        Q('Exactly 50 matches?', '', E(Fr(MATCH[50], 50), 1000)),
        Q('At least 50 matches?', '', E(Fr(41, 50), 1000)),
        Q('Fewer than 49 matches?', '', E(Fr(MATCH[48], 50), 1000)),
    ], h=20, ln=[('Working', ''), ('Answer', '')], info=MATCH_TAB),
    R('in 72 rolls of a die, 4 came up 9 times. Predict the number of 4s in 1000 rolls.', 3, [
        Q('Using the theoretical probability (1 d.p.)', '', f'{fr(Fr(1, 6))} × 1000 ≈ {dec(Fr(1000, 6), 1)}'),
        Q('Using the observed probability', '', E(Fr(9, 72), 1000)),
        Q('Which prediction do you trust more? Why?', '', 'The theoretical one, if the die is fair: 72 rolls is a small sample.'),
    ], h=24, ln=[('Working', ''), ('Answer', '')]),
    R('a pair of dice was rolled 50 times and the sum recorded.', 3, [
        Q('Using the observed probability, how many sums of 8 are expected in 300 rolls?', '', E(Fr(SUMS[8], NS), 300)),
        Q('Using the observed probability, how many sums of 2 are expected? Why is this prediction unreliable?', '', '0; but a sum of 2 (1 + 1) is possible. 50 rolls is too few.'),
        Q(f'The theoretical P(sum of 7) = {F(1, 6)} (Stage 5 shows why). Find the expected number of 7s in 50 rolls and compare.', '',
          f'{fr(Fr(1, 6))} × 50 ≈ {dec(Fr(50, 6), 1)}; observed {SUMS[7]}: fewer'),
    ], h=28, ln=[('Working', ''), ('Answer', '')], info=SUMS_TAB),
]


def fair_check(obs):
    exp = sum(obs) / len(obs)
    return exp, max(abs(o - exp) for o in obs)


EXT = dict(
    rem1=STD['rem1'],
    p1=ext_p1,
    rem2='expected = P × trials · for data, use observed P · small samples make poor predictions',
    p2=ext_p2,
    rem3='work backwards: P = expected ÷ trials · trials = expected ÷ P',
    p3=[
        Q('The expected frequency of an event in 400 trials is 150. Find its probability.', '', show(150, 400)),
        Q('A spinner is spun 250 times. The expected number of blues is 100. What fraction of the spinner is blue?', '', show(100, 250)),
        Q('The expected number of white cars among 80 cars is 24. Find P(a car is not white).', '', f'P(white) = {show(24, 80, "dec")}, so P(not white) = 0.7'),
        Q('A die is rolled n times and the expected number of 6s is 35. Find n.', '', f'n = 35 ÷ {fr(Fr(1, 6))} = {35 * 6}'),
        Q('A 4-colour spinner (equal sectors) gave red 52, blue 49, green 47, yellow 52 in 200 spins. Is it fair? Use expected frequencies.', '',
          'Expected 50 each; every result is within 3 of 50, so it seems fair.'),
        Q('Lollies: P(red) = 0.5, P(green) = 0.2 and the rest are purple. A bag has 9 purple lollies. How many lollies would you expect in the bag?', '',
          f'P(purple) = 0.3; 9 ÷ 0.3 = {Fr(9) / Fr(3, 10)}'),
    ],
    word=[
        Q('A biased coin landed tails 248 times in 400 tosses. Predict the number of heads in 1500 tosses.', '',
          f'P(heads) = {show(152, 400, "dec")}; 0.38 × 1500 = {Fr(38, 100) * 1500}'),
        Q('70 of the canteen’s last 200 orders were wraps. Next week it expects 900 orders. How many wraps should it make? Why make a few extra?', '',
          f'{E(Fr(70, 200), 900)}; the real number varies, so a few extra avoids running out.'),
        Q('Roll a die: Dani wins on 1 or 2, Van on 3, 4 or 5, and Kai on 6. They play 60 games. Find the expected number of wins for each. Is the game fair?', '',
          f'Dani {E(Fr(2, 6), 60)}, Van {E(Fr(3, 6), 60)}, Kai {E(Fr(1, 6), 60)}: not fair.'),
    ],
)
assert fair_check([52, 49, 47, 52]) == (50, 3)
assert Fr(9) / Fr(3, 10) == 30 and Fr(38, 100) * 1500 == 570

LESSON = dict(key='L6', num='6', title='Expected frequency', sub=SUB, alt=True,
              li='calculate the expected frequency of an event, and compare it with the observed frequency.',
              sc=['find expected frequency = probability × number of trials.',
                  'compare observed and expected frequencies.',
                  'use an observed probability to make a prediction.'],
              notes=NOTES, ex1=EX1, ex2=EX2, std=STD, ext=EXT)
