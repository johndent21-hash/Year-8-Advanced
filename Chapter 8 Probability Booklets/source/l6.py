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
<p><b>expected frequency:</b> how many times we expect an event in a number of trials</p>
<p><b>observed frequency:</b> how many times it actually happened</p>
<p><b>fair:</b> every outcome equally likely; <b>biased:</b> not fair</p>
<p>Observed is rarely exactly expected. A big gap over many trials suggests bias.</p></div>
<div><h4>FORMULA</h4>
<div class="fbox">expected frequency = probability × number of trials</div>
<p>From data, use the observed P: 15 twos in 60 rolls, so {F(1, 4)} × 500 = 125.</p>
<p>Not always whole: {F(1, 6)} × 80 ≈ 13.3</p></div>
<div><h4>EXAMPLE</h4>
<p>Declan rolls a die 60 times. Expected 5s or 6s:</p>
<p>P(5 or 6) = {frs(2, 6)} = {fr(Fr(1, 3))}</p>
<p>expected = {fr(Fr(1, 3))} × 60 = 20</p>
<p>observed = 8 + 11 = 19: close to 20, so the die seems fair.</p></div>
</div>'''

EX1 = dict(
    instr='Find each expected frequency: the probability × the number of trials.',
    parts=[
        ('Coin', coin('H', 10), 'A coin is tossed 50 times. Find the expected number of heads.'),
        ('Die', die3d(12, 4, 2, 6), 'A die is rolled 72 times. Find the expected number of 4s.'),
        ('Spinner', spinner(VINH_SP, 14), 'Vinh spins the spinner 80 times. Find the expected number of reds. He actually got 44 reds: compare.'),
        ('Rain', weather('30%', 14), 'The probability of rain on an April day is 30%. April has 30 days. Find the expected number of rainy days.'),
    ], box=17,
    ans=[E(Fr(1, 2), 50), E(Fr(1, 6), 72), f'{E(Fr(1, 2), 80)}; 44 is 4 more than expected.', f'0.3 × 30 = {Fr(3, 10) * 30} days'])

EX2 = dict(
    instr='Expected = probability × trials. If the outcomes are not equally likely, use the observed probability from the data.',
    parts=[
        ('From data', die3d(11, 2, 2, 2), 'Harper’s die gave 15 twos in 60 rolls. Use this observed probability to find how many 2s to expect in 500 rolls.'),
        ('Matchboxes', '', 'In a sample, 20 of 50 matchboxes held exactly 50 matches. How many of 1000 boxes would you expect to hold exactly 50?'),
        ('Not whole', '', 'A die is rolled 80 times. Find the expected number of 6s (to 1 decimal place). A 6 actually came up 22 times. What does this suggest?'),
        ('Lollies', '', 'For a bag of lollies, P(red) = 0.5, P(green) = 0.2 and P(purple) = 0.3. How many of each colour would you expect in a bag of 100 lollies?'),
    ], box=17,
    ans=[E(Fr(15, 60), 500), E(Fr(20, 50), 1000), f'{fr(Fr(1, 6))} × 80 ≈ {dec(Fr(80, 6), 1)}. 22 is far more: the die may be biased.', 'red 50, green 20, purple 30'])

# ---------------------------------------------------------------- standard
EXP_LN = [('Probability', ''), ('× number of trials', ''), ('Expected', '')]
std_p1 = [
    R('find each expected frequency. Write the probability, multiply by the number of trials, then write the expected number.', 4, [
        Q('A coin is tossed 100 times. How many heads would you expect?', coin('H', 8), E(Fr(1, 2), 100)),
        Q('A die is rolled 60 times. How many 6s would you expect?', die3d(9, 6, 6, 6), E(Fr(1, 6), 60)),
        Q('This spinner is spun 40 times. How many blues would you expect?', spinner([('blue', 1, None), ('red', 1, None), ('green', 1, None), ('yellow', 1, None)], 10), E(Fr(1, 4), 40)),
        Q('A die is rolled 30 times. How many even numbers would you expect?', die3d(9, 2, 4, 6), E(Fr(1, 2), 30)),
    ], h=31, ln=EXP_LN),
    R('Vinh’s spinner (half red, a quarter green, a quarter yellow) was spun 80 times: red 44, green 25, yellow 11.', 4, [
        Q('How many reds would you expect in 80 spins?', '', E(Fr(1, 2), 80)),
        Q('How many yellows would you expect in 80 spins?', '', E(Fr(1, 4), 80)),
        Q(f'Red actually came up {VINH["red"]} times. Is that more or less than expected? By how many?', '', f'More, by {VINH["red"] - 40}'),
        Q(f'Yellow actually came up {VINH["yellow"]} times. Is that more or less than expected? By how many?', '', f'{20 - VINH["yellow"]} fewer than expected'),
    ], h=24, ln=[('Working', ''), ('Answer', '')]),
]
std_p2 = [
    R('a fair die is rolled 72 times. Find each expected frequency: probability × 72.', 3, [
        Q('How many 4s would you expect?', '', E(Fr(1, 6), 72)),
        Q('How many numbers greater than 2 would you expect?', '', E(Fr(4, 6), 72)),
        Q('How many even numbers would you expect?', '', E(Fr(3, 6), 72)),
    ], h=22, ln=[('Working', ''), ('Answer', '')]),
    R('use the observed probability (from what happened before) to predict what will happen.', 3, [
        Q('A basketballer scores 7 of every 10 shots. How many goals would you expect from 50 shots?', '', E(Fr(7, 10), 50)),
        Q('A surfer catches a wave on 3 of every 4 attempts. How many waves would you expect from 60 attempts?', '', E(Fr(3, 4), 60)),
        Q('In a sample, 20 of 50 matchboxes held exactly 50 matches. How many of 250 boxes would you expect to hold exactly 50?', '', E(Fr(20, 50), 250)),
    ], h=26, ln=[('Working', ''), ('Answer', '')]),
    R('Kingscliff weather records show that the probability of a summer day above 30 °C is 0.2.', 3, [
        Q('How many days above 30 °C would you expect in a 90-day summer?', '', f'0.2 × 90 = {Fr(1, 5) * 90}'),
        Q('How many days above 30 °C would you expect in two weeks (14 days)?', '', f'0.2 × 14 = {dec(Fr(1, 5) * 14)}'),
        Q('Give a reason why the real number of hot days might be different.', '', 'Chance: the weather varies from year to year; 0.2 is only an estimate.'),
    ], h=24, ln=[('Working', ''), ('Answer', '')]),
    R('do a coin experiment, then compare what you observed with what you expected.', 3, [
        Q('Toss a coin 50 times (or use RanInt#(1,2), 1 = heads). Tally the results.',
          vtab(['Outcome', 'Tally', 'Frequency'], [['Heads', '', ''], ['Tails', '', ''], ['Total', '', '50']], 8.6).replace('<td></td>', '<td class="blank" style="min-width:24mm"></td>'),
          'Answers vary.', ln=[], span=2, figtop=True),
        Q('How many heads would you expect in 50 tosses? Compare this with the number of heads you actually got.', '', f'{E(Fr(1, 2), 50)}; comparison varies.'),
    ], h=32, ln=LN_A2),
]
STD = dict(
    rem1=f'Expected frequency = probability × number of trials. For example, 6s in 60 rolls: {F(1, 6)} × 60 = 10.',
    p1=std_p1,
    rem2='Expected frequency = probability × number of trials. From data, use the observed probability. The answer might not be a whole number.',
    p2=std_p2,
    rem3='Expected = probability × trials. If observed is close to expected, the die or spinner seems fair; if it is far off over many trials, it may be biased.',
    p3=[
        Q('A die was rolled 80 times (see the table). Find the expected number of 6s, to 1 decimal place. Compare it with the number of 6s that actually came up.', DIE80_TAB,
          f'{fr(Fr(1, 6))} × 80 ≈ {dec(Fr(80, 6), 1)}; 22 is much higher.', span=2, figtop=True),
        Q('Use Question 1. Do you think the die is biased? Explain.', '', 'Probably: 6 came up far more often than expected (22 compared with 13.3).'),
        Q('A fair die is rolled 100 times. Find the expected number of 3s, to 1 decimal place.', '', f'{fr(Fr(1, 6))} × 100 ≈ {dec(Fr(100, 6), 1)}'),
        Q('Find 35% of 240.', '', f'{Fr(35, 100) * 240}', tag='Year 7'),
        Q('In a sample, 41 of 50 matchboxes held at least 50 matches. How many of 1000 boxes would you expect to hold at least 50?', '', E(Fr(41, 50), 1000)),
    ],
    word=[
        Q('Declan rolled a die 60 times: 1 (10), 2 (11), 3 (13), 4 (7), 5 (8), 6 (11). Find the expected number of 5s or 6s and the observed number of 5s or 6s. Is the die fair? Explain.', '',
          f'Expected {E(Fr(1, 3), 60)}; observed 8 + 11 = 19. Close, so the die seems fair.'),
        Q('A spinner has 5 equal sectors: 2 red, 2 blue, 1 green. Mel says she will get exactly 40 reds in 100 spins. Explain why she might not.', '',
          f'40 is the expected number ({E(Fr(2, 5), 100)}), but results vary by chance.'),
        Q('8 students each toss a coin 100 times. How many heads would you expect altogether? The class got 389 heads. Is that close? Explain.', '',
          f'{E(Fr(1, 2), 800)}. 389 is close (observed P = {dec(Fr(389, 800), 3)}…).'),
    ],
)

# ---------------------------------------------------------------- extension
ext_p1 = [
    R('find each expected frequency: probability × number of trials.', 4, [
        Q('A die is rolled 300 times. How many 6s would you expect?', die3d(9, 6, 6, 6), E(Fr(1, 6), 300)),
        Q('An 8-sided die has 2 red faces. It is rolled 200 times. How many reds would you expect?', poly_die(8, 'R', 9), E(Fr(2, 8), 200)),
        Q('A card is drawn from a deck and put back, 260 times. How many hearts would you expect?', card('7', 'H', 7), E(Fr(13, 52), 260)),
        Q('The probability of rain each day is 0.35. How many rainy days would you expect in 20 days?', weather('35%', 11), f'0.35 × 20 = {Fr(35, 100) * 20}'),
    ], h=32, ln=EXP_LN),
    R('Vinh’s spinner (½ red, ¼ green, ¼ yellow) was spun 80 times: red 44, green 25, yellow 11. Compare expected with observed.', 4, [
        Q('How many reds were expected? How many more or fewer were observed?', '', f'expected {E(Fr(1, 2), 80)}; observed 44 (+4)'),
        Q('How many greens were expected? How many more or fewer were observed?', '', f'expected {E(Fr(1, 4), 80)}; observed 25 (+5)'),
        Q('How many yellows were expected? How many more or fewer were observed?', '', f'expected {E(Fr(1, 4), 80)}; observed 11 (−9)'),
        Q('Do you think the spinner is fair? Explain using your answers.', '', 'Possibly not: yellow came up far less than expected. More spins would show whether it is biased.'),
    ], h=24, ln=[('Working', ''), ('Answer', '')]),
]
ext_p2 = [
    R('a fair die is rolled 72 times. Find each expected frequency: probability × 72.', 3, [
        Q('How many 4s would you expect?', '', E(Fr(1, 6), 72)),
        Q('How many numbers greater than 2 would you expect?', '', E(Fr(4, 6), 72)),
        Q('How many prime numbers would you expect?', '', E(Fr(3, 6), 72)),
    ], h=20, ln=[('Working', ''), ('Answer', '')]),
    R('use the matchbox sample of 50 boxes (table) to predict how many of 1000 boxes would hold each number of matches.', 3, [
        Q('How many of 1000 boxes would hold exactly 50 matches?', '', E(Fr(MATCH[50], 50), 1000)),
        Q('How many would hold at least 50 matches (50 or more)?', '', E(Fr(41, 50), 1000)),
        Q('How many would hold fewer than 49 matches?', '', E(Fr(MATCH[48], 50), 1000)),
    ], h=20, ln=[('Working', ''), ('Answer', '')], info=MATCH_TAB),
    R('in 72 rolls of a die, a 4 came up 9 times. Predict the number of 4s in 1000 rolls.', 3, [
        Q('Predict using the theoretical probability (to 1 decimal place).', '', f'{fr(Fr(1, 6))} × 1000 ≈ {dec(Fr(1000, 6), 1)}'),
        Q('Predict using the observed probability.', '', E(Fr(9, 72), 1000)),
        Q('Which prediction do you trust more? Why?', '', 'The theoretical one, if the die is fair: 72 rolls is a small sample.'),
    ], h=24, ln=[('Working', ''), ('Answer', '')]),
    R('two dice were rolled 50 times and the sum was recorded each time. Use the table.', 3, [
        Q('Using the observed probability, how many sums of 8 would you expect in 300 rolls?', '', E(Fr(SUMS[8], NS), 300)),
        Q('Using the observed probability, how many sums of 2 would you expect in 300 rolls? Why is this prediction unreliable?', '', '0; but a sum of 2 (1 + 1) is possible. 50 rolls is too few.'),
        Q(f'The theoretical probability of a sum of 7 is {F(1, 6)} (Stage 5 shows why). How many 7s would you expect in 50 rolls? Compare with the table.', '',
          f'{fr(Fr(1, 6))} × 50 ≈ {dec(Fr(50, 6), 1)}; observed {SUMS[7]}: fewer'),
    ], h=28, ln=[('Working', ''), ('Answer', '')], info=SUMS_TAB),
]


def fair_check(obs):
    exp = sum(obs) / len(obs)
    return exp, max(abs(o - exp) for o in obs)


EXT = dict(
    rem1=STD['rem1'],
    p1=ext_p1,
    rem2='Expected = probability × trials. From data, use the observed probability. Small samples make poor predictions.',
    p2=ext_p2,
    rem3='Work backwards: probability = expected ÷ trials, and trials = expected ÷ probability.',
    p3=[
        Q('The expected frequency of an event in 400 trials is 150. Find its probability.', '', show(150, 400)),
        Q('A spinner is spun 250 times. The expected number of blues is 100. What fraction of the spinner is blue?', '', show(100, 250)),
        Q('Among 80 cars, the expected number of white cars is 24. Find the probability that a car is not white.', '', f'P(white) = {show(24, 80, "dec")}, so P(not white) = 0.7'),
        Q('A die is rolled n times. The expected number of 6s is 35. Find n, the number of rolls.', '', f'n = 35 ÷ {fr(Fr(1, 6))} = {35 * 6}'),
        Q('A spinner with 4 equal colour sectors was spun 200 times: red 52, blue 49, green 47, yellow 52. Find the expected number for each colour. Does the spinner seem fair?', '',
          'Expected 50 each; every result is within 3 of 50, so it seems fair.'),
        Q('In a bag of lollies, P(red) = 0.5 and P(green) = 0.2, and the rest are purple. The bag has 9 purple lollies. How many lollies would you expect in the whole bag?', '',
          f'P(purple) = 0.3; 9 ÷ 0.3 = {Fr(9) / Fr(3, 10)}'),
    ],
    word=[
        Q('A biased coin landed tails 248 times in 400 tosses. Use the observed probability to predict the number of heads in 1500 tosses.', '',
          f'P(heads) = {show(152, 400, "dec")}; 0.38 × 1500 = {Fr(38, 100) * 1500}'),
        Q('70 of the canteen’s last 200 orders were wraps. Next week it expects 900 orders. How many wraps should it make? Why make a few extra?', '',
          f'{E(Fr(70, 200), 900)}; the real number varies, so a few extra avoids running out.'),
        Q('In a game a die is rolled: Dani wins on 1 or 2, Van on 3, 4 or 5, and Kai on 6. They play 60 games. Find the expected number of wins for each player. Is the game fair?', '',
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
