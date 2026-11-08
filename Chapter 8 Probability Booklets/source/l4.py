from engine import Q, R, LN_W, LN_A, LN_A2
from gfx import *
from pm import *
from layout import F

SUB = 'Probability • MA4-PRO-C-01'


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


TRIP = [('Australia', 17), ('Italy', 3), ('Vietnam', 4), ('Japan', 1), ('China', 3)]
NT = sum(k for _, k in TRIP)
assert NT == 28
tc = dict(TRIP)
TRIP_TAB = ('<table class="t"><tr><th>Born in</th>' + ''.join(f'<td>{c}</td>' for c, _ in TRIP)
            + '</tr><tr><th>Students</th>' + ''.join(f'<td>{k}</td>' for _, k in TRIP) + '</tr></table>')

TRIP_V = ('<table class="t" style="font-size:7.6pt">' + ''.join(f'<tr><td class="l">{c}</td><td>{k}</td></tr>' for c, k in TRIP) + '</table>')

NOTES = f'''<div class="tnotes" style="grid-template-columns:1.05fr 1.05fr 1fr">
<div><h4>PROBLEM-SOLVING CHECKLIST</h4>
<p><span class="step">1</span>What is the experiment? Count the <b>total</b>.</p>
<p><span class="step">2</span>Which outcomes are <b>favourable</b>?</p>
<p><span class="step">3</span>Is it ‘not’? Use 1 − P(E).</p>
<p><span class="step">4</span>Answer in the <b>form asked</b>: fraction, decimal or %.</p>
<p><span class="step">5</span><b>Check</b>: between 0 and 1? Sensible?</p></div>
<div><h4>KEY IDEAS</h4>
<p><b>‘or’</b> (different groups): add the counts</p>
<p><b>equally likely?</b> Count each object, not each name: SUCCESS has 3 S tiles.</p>
<p><b>no memory:</b> a coin or die does not remember earlier results</p>
<p><b>how many?</b> number ≈ P × total, e.g. P(red) = 0.5 in a bag of 10: about 5 red</p></div>
<div><h4>EXAMPLE</h4>
{balls([5, 10, 15, 20], 6)}
<p style="margin-top:1mm">Balls numbered 1 to 20. P(a multiple of 5):</p>
<p>{{5, 10, 15, 20}}: {frs(4, 20)} = {fr(Fr(1, 5))} = 0.2 = 20%</p></div>
</div>'''

LOL = [('red', Fr(1, 2)), ('green', Fr(1, 5))]
p_purple = 1 - sum(p for _, p in LOL)
m15 = [x for x in range(1, 16) if x < 4 or x > 12]
EX1 = dict(
    instr='Use the checklist in your notes. Write each probability as a fraction in simplest form, unless the question asks for a percentage.',
    parts=[
        ('A table', TRIP_V, '28 students on a trip were born in these countries. One is picked at random. Find P(born in Asia).'),
        ('Letters', tiles('SUCCESS', 5), 'One tile is picked without looking. List the sample space. Is each letter equally likely? Explain.'),
        ('Percentage', spinner([('white', 1, str(k)) if k % 2 else ('yellow', 1, str(k)) for k in range(1, 6)], 14, letters=False), 'The spinner is spun once. Find the probability of an even number. Write it as a percentage.'),
        ('Not', bag([('black', 2), ('blue', 2), ('red', 2)], 14), 'Alex takes one sock without looking from 2 black, 2 blue and 2 red socks. Find the probability that it is not red.'),
    ], box=15,
    ans=[f'Asia: Vietnam, Japan, China = 8 students: {show(8, 28)}',
         '{S, U, C, E}. No: S has 3 tiles, C has 2, U and E have 1 each.',
         f'{{2, 4}}: {show(2, 5, "pct")}',
         f'{show(4, 6)}'])

EX2 = dict(
    instr='Harder problems: read each one twice, decide what you need to find, then solve.',
    parts=[
        ('Small chances', raffle('0042', 18), 'A charity raffle sells 100 000 tickets and Sophia buys 4. Find the probability that Sophia wins. Write it as a decimal.'),
        ('Or', number_cards(range(1, 9), 3.2) + number_cards(range(9, 16), 3.2), 'A whole number from 1 to 15 is chosen at random. Find the probability of a number less than 4 or greater than 12.'),
        ('How many?', '', 'A bag of lollies has P(red) = 0.5 and P(green) = 0.2. The rest are purple. Find P(purple). Then find how many of each colour are in a bag of 10 lollies.'),
        ('No memory', coin('T', 9, 'silver'), 'A coin lands tails 7 times in a row. Find the probability of tails on the next toss.'),
    ], box=17,
    ans=[f'{frs(4, "100 000")} = {dec(Fr(4, 100000))}',
         f'{setstr(m15)}: {show(len(m15), 15)}',
         f'P(purple) = 1 − 0.5 − 0.2 = {dec(p_purple)}; red 5, green 2, purple 3',
         f'{fr(Fr(1, 2))}: each toss is a fresh start.'])
assert len(m15) == 6

# ---------------------------------------------------------------- standard
SPIN5 = [('white', 1, str(k)) if k % 2 else ('yellow', 1, str(k)) for k in range(1, 6)]
std_p1 = [
    R('one ball is picked at random from a barrel of 100 balls numbered 1 to 100. Find each probability as a fraction in simplest form.', 4, [
        Q('Find the probability of the ball numbered 12.', '', show(1, 100)),
        Q('Find the probability of a number greater than 40.', '', show(60, 100)),
        Q('Find the probability of an even number.', '', show(50, 100)),
        Q('Find the probability of a number from 1 to 25.', '', show(25, 100)),
    ], h=26, ln=[('Favourable outcomes', ''), ('Probability', '')]),
    R('the spinner has 5 equal sectors numbered 1 to 5 and is spun once. Write each probability as a fraction, then as a percentage.', 4, [
        Q('Find the probability of a 2.', spinner(SPIN5, 10, letters=False), show(1, 5, 'pct')),
        Q('Find the probability of an even number.', spinner(SPIN5, 10, letters=False), show(2, 5, 'pct')),
        Q('Find the probability of a number less than 5.', spinner(SPIN5, 10, letters=False), show(4, 5, 'pct')),
        Q('Find the probability of a number from 1 to 5.', spinner(SPIN5, 10, letters=False), show(5, 5, 'pct') + ' (certain)'),
    ], h=27, ln=[('Fraction', ''), ('Percentage', '')]),
]
odd15 = [x for x in range(1, 16) if x % 2]
np15 = [x for x in range(1, 16) if x not in PRIMES]
f12 = [x for x in range(1, 16) if 12 % x == 0]
std_p2 = [
    R('one student from the trip is picked at random. Use the table. Find each probability as a fraction in simplest form.', 3, [
        Q('Find the probability that the student was born in Australia.', '', show(tc['Australia'], NT)),
        Q('Find the probability that the student was not born in Vietnam.', '', show(NT - tc['Vietnam'], NT)),
        Q('Find the probability that the student was born in Italy or China.', '', show(tc['Italy'] + tc['China'], NT)),
    ], h=22, ln=[('Working', ''), ('Answer', '')], info=TRIP_TAB + '<span class="cap">28 students went on the school trip to Japan.</span>'),
    R('Alex takes one sock without looking from a drawer with 2 black, 2 blue and 2 red socks.', 3, [
        Q('List the sample space (the possible colours).', '', '{black, blue, red}'),
        Q('Find the probability of a blue sock.', '', show(2, 6)),
        Q('Find the probability of a pink sock.', '', '0 (impossible)'),
    ], h=20, ln=LN_A),
    R('a whole number from 1 to 15 is chosen at random. List the favourable outcomes, then find the probability.', 3, [
        Q('Find the probability of an odd number.', '', f'{setstr(odd15)}: {show(len(odd15), 15)}'),
        Q('Find the probability of a number that is not prime. (1 is not prime.)', '', f'{setstr(np15)}: {show(len(np15), 15)}'),
        Q('Find the probability of a factor of 12.', '', f'{setstr(f12)}: {show(len(f12), 15)}'),
    ], h=26, ln=[('Favourable outcomes', '{ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }'), ('Probability', '')]),
    R('the 7 letters of SUCCESS are written on 7 cards. One card is picked without looking. Find each probability.', 3, [
        Q('Find the probability of a vowel.', '', show(2, 7)),
        Q('Find the probability that the letter is not a C.', '', show(5, 7)),
        Q('Find the probability that the letter is also in the word FAIL.', '', '0: no letter of SUCCESS is in FAIL'),
    ], h=22, ln=[('Working', ''), ('Answer', '')], info=tiles('SUCCESS', 8)),
]
assert set('SUCCESS') & set('FAIL') == set()
TEN = [('NSW', 34), ('Victoria', 20), ('Queensland', 6)]
STD = dict(
    rem1='Probability = favourable outcomes ÷ total outcomes. To change a fraction to a percentage, multiply by 100%. Simplify fractions.',
    p1=std_p1,
    rem2='Checklist: count the total, count the favourable outcomes, use 1 − P(E) for ‘not’, answer in the form asked, then check. ‘Or’ means add the counts.',
    p2=std_p2,
    rem3='P(not E) = 1 − P(E). Each toss or roll is a fresh start. Give the answer in the form the question asks for.',
    p3=[
        Q('A tennis tournament has 34 players from NSW, 20 from Victoria and 6 from Queensland. One player is picked at random. Find the probability that the player is from NSW.', '', show(34, 60)),
        Q('Use the tournament in Question 1. Find the probability that the player is not from Victoria.', '', show(40, 60)),
        Q('A raffle sells 5000 tickets and Ben buys 2. Find the probability that Ben wins. Write it as a decimal.', '', show(2, 5000, 'dec')),
        Q(f'Write {F(7, 15)} as a decimal, correct to 2 decimal places.', '', dec(Fr(7, 15), 2), tag='Year 7'),
        Q('The spinner is spun once. Find the probability of not landing on yellow. Write it as a percentage.', spinner(S('red', 'blue', 'yellow', 'red', 'blue', 'yellow', 'red', 'blue'), 13), show(6, 8, 'pct')),
        Q('A fair die shows a 6 five times in a row. Mai says a 6 is now more likely. Rani says a 6 is now less likely. Who is right? Explain.', die3d(9, 6, 6, 6),
          f'Neither: P(6) = {fr(Fr(1, 6))} on every roll of a fair die.'),
    ],
    word=[
        Q('8K has 28 students: 12 catch the bus, 9 walk and the rest are driven to school. One student is picked at random. Find (a) P(driven) (b) P(does not walk).', '',
          f'Driven 7: {show(7, 28)}. Not walk: {show(19, 28)}.'),
        Q('The letters of TWEED HEADS are written on 10 cards. One card is picked without looking. Find (a) P(an E) (b) P(a vowel).', '',
          f'P(E) = {show("TWEEDHEADS".count("E"), 10)}; P(vowel) = {show(sum(1 for c in "TWEEDHEADS" if c in "AEIOU"), 10)}'),
        Q('A charity raffle sells 2500 tickets at $2 each, with one prize. Lucy spends $20 on tickets. How many tickets does Lucy have? Find the probability that Lucy wins, as a percentage.', '',
          f'10 tickets: {show(10, 2500, "pct")}'),
    ],
)

# ---------------------------------------------------------------- extension
digit5 = [x for x in range(1, 101) if '5' in str(x)]
FACES = [('red', 2), ('white', 3), ('blue', 1), ('yellow', 2)]
fc = dict(FACES)
ext_p1 = [
    R('one ball is picked at random from a barrel of 100 balls numbered 1 to 100. Find each probability as a fraction in simplest form.', 4, [
        Q('Find the probability of a number from 1 to 85.', '', show(85, 100)),
        Q('Find the probability of a multiple of 7.', '', show(len([x for x in range(1, 101) if x % 7 == 0]), 100)),
        Q('Find the probability of a two-digit number.', '', show(90, 100)),
        Q('Find the probability that the number has a 5 as one of its digits.', '', show(len(digit5), 100)),
    ], h=28, ln=[('Working', ''), ('Probability', '')]),
    R('an 8-sided die has 2 red, 3 white, 1 blue and 2 yellow faces. It is rolled once. Find each probability as a decimal.', 4, [
        Q('Find the probability of blue.', poly_die(8, 'B', 9), show(fc['blue'], 8, 'dec')),
        Q('Find the probability of yellow.', poly_die(8, 'Y', 9), show(fc['yellow'], 8, 'dec')),
        Q('Find the probability of not red.', poly_die(8, 'R', 9), show(8 - fc['red'], 8, 'dec')),
        Q('Find the probability of white or yellow.', poly_die(8, 'W', 9), show(fc['white'] + fc['yellow'], 8, 'dec')),
    ], h=28, ln=[('Working', ''), ('Probability', '')]),
]
assert len(digit5) == 19
e5 = [x for x in range(1, 16) if x % 4 == 0]
nf12 = [x for x in range(1, 16) if 12 % x]
po = [x for x in range(1, 16) if x in PRIMES]
KC = 'KINGSCLIFF'
TRUCK = [('hand sanitiser', 240), ('soap', 305), ('paper', 335), ('pens', 120)]
trk = dict(TRUCK)
NTR = sum(trk.values())
assert NTR == 1000
ext_p2 = [
    R('a tennis tournament has 34 players from NSW, 20 from Victoria and 6 from Queensland. One player is picked at random. Find each probability.', 3, [
        Q('Find the probability that the player is from Queensland.', '', show(6, 60)),
        Q('Find the probability that the player is not from Victoria.', '', show(40, 60)),
        Q('Find the probability that the player is from Queensland or Victoria.', '', show(26, 60)),
    ], h=22, ln=[('Working', ''), ('Answer', '')]),
    R('a whole number from 1 to 15 is chosen at random. List the favourable outcomes, then find the probability.', 3, [
        Q('Find the probability of a multiple of 4.', '', f'{setstr(e5)}: {show(len(e5), 15)}'),
        Q('Find the probability of a number that is not a factor of 12.', '', f'{setstr(nf12)}: {show(len(nf12), 15)}'),
        Q('Find the probability of a prime number.', '', f'{setstr(po)}: {show(len(po), 15)}'),
    ], h=26, ln=[('Favourable outcomes', '{ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }'), ('Probability', '')]),
    R('the 10 letters of KINGSCLIFF are written on 10 cards. One card is picked without looking.', 3, [
        Q('Is each different letter equally likely to be picked? Explain.', '', 'No: I and F are on 2 cards each; every other letter is on 1 card.'),
        Q('Find the probability that the letter is also in the word FISH.', '', f'F, F, I, I, S: {show(sum(1 for c in KC if c in "FISH"), 10)}'),
        Q('Find the probability that the letter is not a vowel.', '', show(sum(1 for c in KC if c not in "AEIOU"), 10)),
    ], h=24, ln=[('Working', ''), ('Answer', '')], info=tiles(KC, 7)),
    R('a truck carries 240 boxes of hand sanitiser, 305 of soap, 335 of paper and 120 of pens. One box is picked at random. Find each probability in simplest form.', 3, [
        Q('Find the probability that it is a box of hand sanitiser.', '', show(trk['hand sanitiser'], NTR)),
        Q('Find the probability that it is a box of pens or soap.', '', show(trk['pens'] + trk['soap'], NTR)),
        Q('Find the probability that it is not a box of paper.', '', show(NTR - trk['paper'], NTR)),
    ], h=22, ln=[('Working', ''), ('Answer', '')]),
]
m46 = [x for x in range(1, 51) if x % 6 == 0]
same3 = [x for x in range(100, 1000) if len(set(str(x))) == 1]
EXT = dict(
    rem1='Probability = favourable outcomes ÷ total outcomes. Write fractions in simplest form. For a decimal, divide the top by the bottom.',
    p1=ext_p1,
    rem2='List the outcomes carefully. Count each object, not each name. ‘Or’ for different groups: add the counts.',
    p2=ext_p2,
    rem3='Plan before you calculate. A game is fair when every player has the same probability of winning.',
    p3=[
        Q('Bag A has 10 lollies and bag B has 100 lollies. In both bags, P(red) = 0.5. Which bag gives the better chance of taking a red lolly? Explain.', '',
          'Neither: P(red) = 0.5 in both bags. Bag B just has more lollies.'),
        Q('A whole number from 1 to 50 is chosen at random. List the multiples of 6, then find the probability of a multiple of 6.', '',
          f'{setstr(m46)}: {show(len(m46), 50)}'),
        Q('A 3-digit number from 100 to 999 is chosen at random. Find the probability that all three digits are the same.', '',
          f'{len(same3)} numbers (111, …, 999): {show(len(same3), 900)}'),
        Q('A die is weighted so that P(6) = 0.25. The other five numbers are equally likely. Find P(1).', '',
          f'0.75 ÷ 5 = {dec(Fr(3, 4) / 5)}'),
        Q('In a class, the probability that a student picked at random is left-handed is 0.15. There are 3 left-handed students. How many students are in the class?', '',
          f'3 ÷ 0.15 = {Fr(3) / Fr(15, 100)}'),
        Q(f'Ali says: ‘A game has two outcomes, win or lose, so P(win) = {F(1, 2)}.’ Explain what is wrong with Ali’s thinking.', '',
          'Win and lose are not always equally likely (and there might be a draw), so P(win) need not be ½.'),
    ],
    word=[
        Q('The canteen sold 120 lunches: 45 wraps, 30 sushi and the rest burgers. One receipt is picked at random. (a) Find P(burger). (b) 20 more burgers are sold. Find the new P(burger).', '',
          f'{show(45, 120)}; new: {show(65, 140)}'),
        Q('One card is picked from cards numbered 1 to 20. Ash wins on a multiple of 4, Bo wins on a prime number, and Cy wins on any other number. Is the game fair? Who is most likely to win?', '',
          'Ash 5 cards, Bo 8, Cy 7: not fair. Bo is most likely to win.'),
        Q('A bag holds 20 marbles and P(red) = 0.35. How many red marbles are there? How many blue marbles must be added to make P(red) = 0.25?', '',
          'Red = 7. Need 7 ÷ 0.25 = 28 marbles, so add 8 blue.'),
    ],
)
assert len(m46) == 8 and len([x for x in range(1, 21) if x % 4 == 0]) == 5 and len([x for x in range(1, 21) if x in PRIMES]) == 8
assert Fr(7, 28) == Fr(1, 4)

LESSON = dict(key='L4', num='4', title='Probability problems', sub=SUB, alt=True,
              li='choose and use the right probability skill to solve problems from lists, tables and words.',
              sc=['decide which skill a problem needs.',
                  'set out working with P(E) = favourable ÷ total.',
                  'explain my answer in a sentence.'],
              notes=NOTES, ex1=EX1, ex2=EX2, std=STD, ext=EXT)
