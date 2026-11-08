from engine import Q, R, LN_W, LN_A, LN_A2
from gfx import *
from pm import *
from layout import F

SUB = 'Probability • MA4-PRO-C-01'


def word(p):
    p = Fr(p)
    if p == 0:
        return 'impossible'
    if p == 1:
        return 'certain'
    if p == Fr(1, 2):
        return 'even chance'
    return 'unlikely' if p < Fr(1, 2) else 'likely'


def S(*cols):
    return [(c, 1, None) for c in cols]


def blue_q(secs, size=13, text='What is the chance of landing on blue?'):
    p = spin_p(secs, 'blue')
    nb = sum(1 for c, _, _ in secs if c == 'blue')
    return Q(text, spinner(secs, size), ans=f'{nb} of {len(secs)} sectors: {word(p)}')


def uniq(seq):
    out = []
    for x in seq:
        if x not in out:
            out.append(x)
    return out


BR = '{ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }'

NOTES = f'''<div class="tnotes" style="grid-template-columns:1.1fr 1.05fr .95fr">
<div><h4>KEY TERMS</h4>
<p><b>chance experiment:</b> an activity with an uncertain result, e.g. a spin</p>
<p><b>trial:</b> one go · <b>outcome:</b> one possible result</p>
<p><b>sample space:</b> all possible outcomes, each written once, in braces {{ }}</p>
<p><b>equally likely:</b> every outcome has the same chance</p>
<p><b>at random:</b> no outcome is favoured</p></div>
<div><h4>THE PROBABILITY SCALE</h4>
{prob_scale(56, words=True)}
<p style="margin-top:.6mm">A probability is a number from 0 to 1. It can be a fraction, a decimal or a percentage: {F(1, 2)} = 0.5 = 50%.</p></div>
<div><h4>STEPS: THE SAMPLE SPACE</h4>
<p><span class="step">1</span>write each outcome once</p><p><span class="step">2</span>put them in braces {{ }}</p>
<p><span class="step">3</span>count the outcomes</p><p><span class="step">4</span>equally likely? check sizes, fairness</p>
<div style="display:flex;gap:2mm;align-items:center;margin-top:.8mm">{spinner(S('red', 'red', 'blue'), 11)}
<p style="margin:0">{{red, blue}}: 2 outcomes,<br>not equally likely<br>(red has 2 sectors)</p></div></div>
</div>'''

EX1 = dict(
    instr='Answer each part. Where it says explain, give a reason.',
    parts=[
        ('The scale', prob_scale(44, words=False),
         'Write each letter where its event belongs on the scale. A: the sun rises tomorrow. B: rolling a 7 on a die. C: a coin lands heads.'),
        ('Sample space', spinner(S('red', 'blue', 'green', 'yellow', 'red'), 15),
         'The spinner is spun once. List the sample space, then count the outcomes.'),
        ('Equally likely?', spinner([('red', 2, None), ('blue', 1, None), ('green', 1, None)], 15),
         'The spinner is spun once. Is each colour equally likely? Explain.'),
        ('Sample space', '',
         'List the sample space for the day of the week a person was born on. How many outcomes are there?'),
    ], box=16,
    ans=['A at 1 (certain), B at 0 (impossible), C at ½ (even chance).',
         '{red, blue, green, yellow}: 4 outcomes (red is listed once).',
         'No. Red covers half of the spinner; blue and green cover a quarter each.',
         '{Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday}: 7 outcomes.'])

EX2 = dict(
    instr='Answer each part in a full sentence, and give the reason.',
    parts=[
        ('Equally likely?', bag([('red', 3), ('blue', 1)], 14),
         'One counter is taken from the bag without looking. List the sample space. Are the outcomes equally likely?'),
        ('A match', '',
         'Kingscliff plays Cabarita in a final. List the sample space of results. Are the outcomes equally likely?'),
        ('Order', die3d(11, 1, 5, 3),
         'A die is rolled. Put these in order from least likely to most likely: A an even number, B a 6, C a number less than 6, D a 9.'),
        ('Forecast', weather('30%', 14),
         'The forecast is a 30% chance of rain. Is rain likely or unlikely? Could it still rain?'),
    ], box=19,
    ans=['{red, blue}. No: there are 3 red counters and 1 blue, so red is more likely.',
         '{Kingscliff wins, Cabarita wins, draw}. Not equally likely: it depends on the teams, and draws are rare.',
         'D (0 outcomes), B (1), A (3), C (5).',
         'Unlikely, because 30% is less than 50%. Yes, it could still rain: 30% is not 0%.'])

# ---------------------------------------------------------------- standard
SP_LN = [('Blue sectors', '___ out of ___'), ('Chance word', '')]
SS_LN = [('Sample space', BR), ('Number of outcomes', '')]

std_r1 = R('each spinner is spun once. Count the blue sectors and all the sectors. Then write the chance word for landing on blue.', 4,
           [blue_q(S('red', 'yellow', 'green')), blue_q(S('blue', 'red', 'yellow', 'green', 'red')),
            blue_q(S('blue', 'red', 'blue', 'yellow')), blue_q(S('blue', 'blue', 'red', 'blue', 'yellow', 'blue'))],
           h=31, ln=SP_LN)
assert [q.ans.split(': ')[1] for q in std_r1.qs] == ['impossible', 'unlikely', 'even chance', 'likely']

std_r2 = R('write every possible outcome once, inside braces { }. Then count how many outcomes there are.', 4, [
    Q('A coin is tossed. List the sample space.', coin('H', 8) + coin('T', 8, 'silver'), '{heads, tails}: 2 outcomes'),
    Q('A die is rolled. List the sample space.', die3d(10, 1, 5, 3), '{1, 2, 3, 4, 5, 6}: 6 outcomes'),
    Q('This spinner is spun. List the sample space.', spinner([('white', 1, '2'), ('yellow', 1, '4'), ('white', 1, '6'), ('yellow', 1, '8')], 11, letters=False), '{2, 4, 6, 8}: 4 outcomes'),
    Q('One tile is picked. List the sample space.', tiles('TWEED', 5.5), f'{setstr(uniq("TWEED"))}: {len(uniq("TWEED"))} outcomes (E is written once)'),
], h=29, ln=SS_LN)
assert len(uniq('TWEED')) == 4

std_r3 = R('list the sample space. If an outcome appears more than once, write it only once.', 3, [
    Q('This spinner is spun once. List the sample space and count the outcomes.', spinner(S('red', 'blue', 'red', 'green', 'blue'), 14), '{red, blue, green}: 3 outcomes'),
    Q('A person is asked the month they were born in. List the possible first letters of that month.', '', '{J, F, M, A, S, O, N, D}: 8 outcomes'),
    Q('Kingscliff plays a netball game. List the possible results for Kingscliff.', '', '{win, lose, draw}: 3 outcomes'),
], h=40, ln=[('Sample space', BR), ('', ''), ('Number of outcomes', '')])
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
assert uniq([m[0] for m in months]) == list('JFMASOND')

std_r4 = R('an event is the outcomes you want. List the outcomes in each event, inside braces { }.', 3, [
    Q('A die is rolled. List the outcomes in the event ‘an odd number’.', die3d(10, 3, 1, 5), setstr(die_p(lambda x: x % 2)[0])),
    Q('One tile is picked. List the outcomes in the event ‘a vowel’.', tiles('CUDGEN', 5.5), setstr([c for c in 'CUDGEN' if c in 'AEIOU'])),
    Q('List the house numbers that are greater than 4 but less than 10.', '', setstr([x for x in range(1, 20) if 4 < x < 10])),
], h=34, ln=[('Outcomes', BR), ('', '')])

std_r5 = R('decide if the outcomes are equally likely. Write <i>yes</i> or <i>no</i>, then give a reason.', 3, [
    Q('This spinner is spun. Are red, blue and green equally likely?', spinner([('red', 2, None), ('blue', 1, None), ('green', 1, None)], 13), 'No. Red covers half the spinner; blue and green cover a quarter each.'),
    Q('A fair die is rolled. Are 1, 2, 3, 4, 5 and 6 equally likely?', die3d(10, 2, 6, 4), 'Yes. Each face of a fair die has the same chance.'),
    Q('Someone sits a driving test. Are ‘pass’ and ‘fail’ equally likely?', '', 'No. It depends on how well the person drives.'),
], h=40, ln=[('Yes or no', ''), ('Reason', ''), ('', '')])

std_r6 = R('write the chance word that matches each probability: <i>impossible, unlikely, even chance, likely</i> or <i>certain</i>.', 3, [
    Q('An event has a probability of <b>0.9</b>. Which chance word fits?', '', word(Fr(9, 10))),
    Q(f'An event has a probability of <b>{F(1, 2)}</b>. Which chance word fits?', '', word(Fr(1, 2))),
    Q('An event has a <b>2%</b> chance. Which chance word fits?', '', word(Fr(2, 100)) + ' (almost impossible)'),
], h=22, ln=[('Chance word', '')])

STD = dict(
    rem1=f'Chance words: impossible (0) · unlikely (below {F(1, 2)}) · even chance ({F(1, 2)}) · likely (above {F(1, 2)}) · certain (1)',
    p1=[std_r1, std_r2],
    rem2='The sample space lists every possible outcome once, inside braces { }. An event is the outcomes you want. Equally likely means every outcome has the same chance.',
    p2=[std_r3, std_r4, std_r5, std_r6],
    rem3=f'0 means impossible, {F(1, 2)} means even chance, 1 means certain. List each outcome once. Equally likely means the same chance.',
    p3=[
        Q('A die is rolled and a coin is tossed. Write each letter on the scale where its event belongs. A: rolling a 6. B: rolling a number less than 7. C: the coin lands heads.',
          prob_scale(46, words=False), 'A between 0 and ½ (near 0), B at 1, C at ½.', ln=[]),
        Q(f'Write {F(3, 4)} as a decimal and as a percentage.', '', f'{dec(Fr(3, 4))} and {pct(Fr(3, 4))}', tag='Year 7'),
        Q('One tile is picked without looking. List the sample space, writing each letter once.', tiles('KINGSCLIFF', 4.4), f'{setstr(uniq("KINGSCLIFF"))}: {len(uniq("KINGSCLIFF"))} outcomes'),
        Q('This spinner is spun once. Which colour is more likely, red or blue? Explain how you know.', spinner(S('red', 'blue', 'red', 'green', 'red', 'blue'), 14), 'Red: it has 3 sectors and blue has only 2.'),
        Q('Sam says, ‘On a die, a 6 is less likely than a 1 because 6 is a bigger number.’ Is Sam right? Explain.', '', 'No. On a fair die every number is equally likely.'),
        Q('A coin lands tails 7 times in a row. Is heads more likely on the next toss? Explain your answer.', coin('T', 9, 'silver'), 'No. It is still an even chance: the coin does not remember earlier tosses.'),
    ],
    word=[
        Q('The forecast for the Tweed says ‘a 70% chance of rain’. Write the chance word for rain. Is rain certain? Explain.', '', 'Likely. It is not certain, because 70% is less than 100%.'),
        Q('Colour the 4 equal sectors of this spinner so that landing on blue is <i>likely</i> but not <i>certain</i>. Then explain why your spinner works.', spinner(S('white', 'white', 'white', 'white'), 14, letters=False), '3 blue sectors and 1 other colour: 3 of 4 is more than half but less than all.'),
        Q('Amy and Cara are in 8K; Ben and Dev are in 8R. One of the four is picked at random to be captain. List the sample space. Is the captain more likely to come from 8K? Explain.', '', '{Amy, Ben, Cara, Dev}. No: 2 are from each class, so it is an even chance.'),
    ],
)

# ---------------------------------------------------------------- extension
ext_r1 = R('each spinner is spun once. Count the blue sectors out of all the sectors, then write the chance word for landing on blue.', 4,
           [blue_q(S('blue', 'red', 'yellow', 'green', 'red', 'blue')), blue_q(S('blue', 'blue', 'red')),
            blue_q(S('blue', 'blue', 'red', 'yellow')), blue_q(S('red', 'green', 'yellow'))],
           h=30, ln=SP_LN)
coins3 = coin('H', 6.5) + coin('T', 6.5, 'silver') + coin('H', 6.5)
ext_r2 = R('list the sample space inside braces { } and count the outcomes. Write repeated outcomes only once.', 4, [
    Q('This spinner is spun once. List the sample space.', spinner([('white', 1, '1'), ('yellow', 1, '2'), ('yellow', 1, '2'), ('green', 1, '3'), ('green', 1, '3'), ('green', 1, '3')], 12, letters=False), '{1, 2, 3}: 3 outcomes'),
    Q('One tile is picked. List the sample space.', tiles('TWEEDHEADS', 3.4), f'{setstr(uniq("TWEEDHEADS"))}: {len(uniq("TWEEDHEADS"))} outcomes'),
    Q('List the possible last digits of a car number plate.', '', '{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}: 10 outcomes'),
    Q('3 coins are tossed together. List the possible numbers of heads.', coins3, '{0, 1, 2, 3}: 4 outcomes'),
], h=29, ln=SS_LN)

ext_r3 = R('list the outcomes in each event, inside braces { }.', 3, [
    Q('A 10-sided die numbered 1 to 10 is rolled. List the outcomes in the event ‘a prime number’.', poly_die(12, 7, 10), setstr([x for x in range(1, 11) if x in PRIMES])),
    Q('A month is picked. List the outcomes in the event ‘the month has exactly 30 days’.', '', '{April, June, September, November}'),
    Q('A normal die is rolled. List the outcomes in the event ‘a factor of 12’.', die3d(10, 4, 6, 2), setstr(die_p(lambda x: 12 % x == 0)[0])),
], h=36, ln=[('Outcomes', BR), ('', '')])

ext_r4 = R('decide if the outcomes are equally likely. Write <i>yes</i> or <i>no</i>, then give a reason.', 3, [
    Q('3 coins are tossed. Are 0, 1, 2 and 3 heads equally likely?', coins3, 'No. 1 head or 2 heads can happen in more ways than 0 or 3 heads.'),
    Q('A person is picked. Is every letter equally likely to be the first letter of their first name?', '', 'No. Some letters (like J or S) start far more names than others (like Q or X).'),
    Q('A random number generator makes a whole number from 1 to 20. Is each number equally likely?', calculator('RanInt#(1,20)', '13', 8), 'Yes. A random number generator makes each number equally likely.'),
], h=42, ln=[('Yes or no', ''), ('Reason', ''), ('', '')])

prob_tiles = 'PROBABILITY'
ext_r5 = R('put the events in order from least likely to most likely. Explain using the number of outcomes in each event.', 3, [
    Q('A die is rolled. Order these events: A an even number, B 5 or more, C less than 2.', die3d(9, 1, 5, 3),
      f'C ({len(die_p(lambda x: x < 2)[0])} outcome), B ({len(die_p(lambda x: x >= 5)[0])}), A ({len(die_p(lambda x: x % 2 == 0)[0])}).'),
    Q('One tile is picked. Order these events: (i) a B, (ii) an I, (iii) a vowel.', tiles(prob_tiles, 3.3),
      f'(i) and (ii) are equally likely ({prob_tiles.count("B")} tiles each), then (iii) ({sum(1 for c in prob_tiles if c in "AEIOU")} tiles: O, A, I, I).'),
    Q('The spinner is spun once. Order these events: A red, B blue, C yellow.', spinner(S('red', 'red', 'blue', 'green', 'red', 'yellow', 'blue', 'red'), 13),
      'C (1 sector), B (2), A (4).'),
], h=44, ln=[('Order', ''), ('Reason', ''), ('', '')])
assert prob_tiles.count('B') == prob_tiles.count('I') == 2

ext_r6 = R('use probabilities as numbers from 0 to 1. Show how you know.', 3, [
    Q('Write a decimal that could be the probability of an event that is unlikely but not impossible.', '', 'Any decimal between 0 and 0.5, e.g. 0.2.'),
    Q(f'One event has probability 0.45 and another has probability {F(4, 9)}. Which event is more likely? Show your working.', '', f'{F(4, 9)} = {dec(Fr(4, 9), 3)}…, so the event with probability 0.45 is more likely.'),
    Q('Explain why a probability can never be 1.2 or −0.3.', '', 'Probabilities go from 0 (impossible) to 1 (certain), so nothing is above 1 or below 0.'),
], h=28, ln=LN_A2)
assert Fr(4, 9) < Fr(45, 100)


def eight_designs():
    out = []
    for b in range(1, 8):
        r = 8 - 2 * b
        if r > 4:  # likely means more than half of 8
            out.append((r, b, b))
    return out


assert eight_designs() == [(6, 1, 1)]

EXT = dict(
    rem1=STD['rem1'],
    p1=[ext_r1, ext_r2],
    rem2='List each outcome once. An event is the outcomes you want. Compare events by counting their outcomes. A probability is never below 0 or above 1.',
    p2=[ext_r3, ext_r4, ext_r5, ext_r6],
    rem3='Equally likely means the same chance, not just the same number of names. Likely means more than half; unlikely means less than half, but more than 0.',
    p3=[
        Q('Colour these 5 equal sectors so that red is twice as likely as blue, and green is impossible. Label each sector with its colour.', spinner(S(*['white'] * 5), 15, letters=False),
          '2 red, 1 blue and 2 of another colour (not green), e.g. R, R, B, Y, Y.', ln=LN_A),
        Q('Spinner A has 3 equal sectors, 1 of them blue. Spinner B has 8 equal sectors, 3 of them blue. Which spinner gives the better chance of blue? Explain.', '',
          f'B: {F(3, 8)} = {dec(Fr(3, 8))}, but {F(1, 3)} = {dec(Fr(1, 3), 3)}…'),
        Q('A bag holds 10 counters, all red or blue. Red is likely. Blue is unlikely but possible. How many red counters could there be? List every possibility.', '',
          ', '.join(str(r) for r in range(11) if Fr(r, 10) > Fr(1, 2) and 0 < Fr(10 - r, 10) < Fr(1, 2))),
        Q('Jo writes the sample space for this spinner as {red, red, blue}. What is wrong? Write the sample space correctly.', spinner(S('red', 'red', 'blue'), 13),
          'Each outcome is listed once: {red, blue}. (The outcomes are not equally likely.)'),
        Q(f'Put these probabilities in order from least likely to most likely: A 0.6, B {F(3, 5)}, C 62%, D {F(5, 8)}.', '',
          f'A and B (both 0.6) are equally likely, then C (0.62), then D ({dec(Fr(5, 8))}).', tag='Year 7'),
        Q('A die is weighted so that a 6 comes up half the time. Are the six outcomes equally likely? Write the chance word for rolling a 6.', die3d(10, 6, 6, 6),
          'No. Rolling a 6 is an even chance; each other number is unlikely.'),
    ],
    word=[
        Q('The surf club picks 1 of its 12 members at random: 5 are in Year 8, 4 in Year 9 and 3 in Year 10. Write the chance word for ‘the person is in Year 8’ and for ‘the person is in Year 11’. Give reasons.', '',
          'Year 8: unlikely, because 5 of 12 is less than half. Year 11: impossible, because no members are in Year 11.'),
        Q('A spinner has 8 equal sectors coloured red, blue and yellow. Red is likely. Blue and yellow are equally likely, and yellow is possible. Find every possible design (how many sectors of each colour).', '',
          'Only one: 6 red, 1 blue, 1 yellow. (4 red, 2 blue, 2 yellow gives red an even chance, not likely.)'),
        Q('In a game a die is rolled: Ava wins on 1 or 2, Ben on 3, 4 or 5, and Cal on 6. Is the game fair? Explain, then change the rules to make it fair.', '',
          'Not fair: Ava has 2 outcomes, Ben 3 and Cal 1. Fair: give each player 2 numbers, e.g. Ava 1–2, Ben 3–4, Cal 5–6.'),
    ],
)

LESSON = dict(key='L1', num='1', title='Chance and the sample space', sub=SUB,
              li='describe chance with words and with numbers from 0 to 1, list a sample space, and decide whether outcomes are equally likely.',
              sc=['place an event on the probability scale from 0 to 1.',
                  'list the sample space of a chance experiment.',
                  'decide, with a reason, whether outcomes are equally likely.'],
              notes=NOTES, ex1=EX1, ex2=EX2, std=STD, ext=EXT)
