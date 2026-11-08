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


def blue_q(secs, size=14):
    p = spin_p(secs, 'blue')
    nb = sum(1 for c, _, _ in secs if c == 'blue')
    return Q(fig=spinner(secs, size), ans=f'{nb} of {len(secs)} sectors: {word(p)}')


def uniq(seq):
    out = []
    for x in seq:
        if x not in out:
            out.append(x)
    return out


NOTES = f'''<div class="tnotes" style="grid-template-columns:1.1fr 1.05fr .95fr">
<div><h4>KEY TERMS</h4>
<p><b>chance experiment:</b> an activity with an uncertain result, e.g. spinning a spinner</p>
<p><b>trial:</b> one go of the experiment</p>
<p><b>outcome:</b> one possible result</p>
<p><b>sample space:</b> the list of all possible outcomes, each written once, in braces {{ }}</p>
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
    instr='Answer each part. Give a reason where you are asked to.',
    parts=[
        ('The scale', prob_scale(44, words=False), 'Mark: A the sun rises tomorrow; B rolling a 7 on a die; C a coin lands heads.'),
        ('Sample space', spinner(S('red', 'blue', 'green', 'yellow', 'red'), 15), 'List the sample space. How many outcomes are there?'),
        ('Equally likely?', spinner([('red', 2, None), ('blue', 1, None), ('green', 1, None)], 15), 'Is each colour equally likely? Explain.'),
        ('Sample space', '', 'List the sample space for the day of the week a person was born on. How many outcomes?'),
    ], box=19,
    ans=['A at 1 (certain), B at 0 (impossible), C at ½ (even chance).',
         '{red, blue, green, yellow}: 4 outcomes (red is listed once).',
         'No. Red covers half of the spinner; blue and green cover a quarter each.',
         '{Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday}: 7 outcomes.'])

EX2 = dict(
    instr='Answer in a full sentence, and give the reason.',
    parts=[
        ('Equally likely?', bag([('red', 3), ('blue', 1)], 14), 'One counter is taken. List the sample space. Are the outcomes equally likely?'),
        ('A match', '', 'Kingscliff plays Cabarita in a final. List the sample space. Are the outcomes equally likely?'),
        ('Order', die3d(11, 1, 5, 3), 'Least to most likely: A an even number, B a 6, C less than 6, D a 9.'),
        ('Forecast', weather('30%', 15), 'A 30% chance of rain: is rain likely or unlikely? Could it still rain?'),
    ], box=19,
    ans=['{red, blue}. No: there are 3 red counters and 1 blue, so red is more likely.',
         '{Kingscliff wins, Cabarita wins, draw}. Not equally likely: it depends on the teams, and draws are rare.',
         'D (0 outcomes), B (1), A (3), C (5).',
         'Unlikely, because 30% is less than 50%. Yes, it could still rain: 30% is not 0%.'])

# ---------------------------------------------------------------- standard
SP_LN = [('Blue', ''), ('Total', ''), ('Word', '')]
SS_LN = [('Sample space', '{ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }'), ('Outcomes', '')]

std_r1 = R('count the blue sectors and the total sectors, then choose a chance word for landing on blue.', 4,
           [blue_q(S('red', 'yellow', 'green')), blue_q(S('blue', 'red', 'yellow', 'green', 'red')),
            blue_q(S('blue', 'red', 'blue', 'yellow')), blue_q(S('blue', 'blue', 'red', 'blue', 'yellow', 'blue'))],
           h=34, ln=SP_LN)
assert [q.ans.split(': ')[1] for q in std_r1.qs] == ['impossible', 'unlikely', 'even chance', 'likely']

std_r2 = R('list the sample space in braces { }, then count the outcomes.', 4, [
    Q('Tossing a coin', coin('H', 9) + coin('T', 9, 'silver'), '{heads, tails}: 2 outcomes'),
    Q('Rolling a die', die3d(11, 1, 5, 3), '{1, 2, 3, 4, 5, 6}: 6 outcomes'),
    Q('Spinning this spinner', spinner([('white', 1, '2'), ('yellow', 1, '4'), ('white', 1, '6'), ('yellow', 1, '8')], 12, letters=False), '{2, 4, 6, 8}: 4 outcomes'),
    Q('Choosing one tile', tiles('TWEED', 6), f'{setstr(uniq("TWEED"))}: {len(uniq("TWEED"))} outcomes (E is written once)'),
], h=30, ln=SS_LN)
assert len(uniq('TWEED')) == 4

std_r3 = R('list the sample space. Write each outcome only once, even if it repeats.', 3, [
    Q('This spinner is spun once.', spinner(S('red', 'blue', 'red', 'green', 'blue'), 15), '{red, blue, green}: 3 outcomes'),
    Q('The first letter of the month a person was born in.', '', '{J, F, M, A, S, O, N, D}: 8 outcomes'),
    Q('The result of a netball game for Kingscliff.', '', '{win, lose, draw}: 3 outcomes'),
], h=40, ln=[('Sample space', '{ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }'), ('', ''), ('Outcomes', '')])
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
assert uniq([m[0] for m in months]) == list('JFMASOND')

std_r4 = R('list the outcomes in each event, in braces { }.', 3, [
    Q('Rolling an odd number on a die.', die3d(11, 3, 1, 5), setstr(die_p(lambda x: x % 2)[0])),
    Q('Choosing a vowel from these tiles.', tiles('CUDGEN', 6), setstr([c for c in 'CUDGEN' if c in 'AEIOU'])),
    Q('A house number greater than 4 but less than 10.', '', setstr([x for x in range(1, 20) if 4 < x < 10])),
], h=34, ln=[('Event', '{ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }'), ('', '')])

std_r5 = R('are the outcomes equally likely? Write <i>yes</i> or <i>no</i>, then give a reason.', 3, [
    Q('Spinning this spinner.', spinner([('red', 2, None), ('blue', 1, None), ('green', 1, None)], 14), 'No. Red covers half the spinner; blue and green cover a quarter each.'),
    Q('Rolling a fair die.', die3d(11, 2, 6, 4), 'Yes. Each face of a fair die has the same chance.'),
    Q('Passing or failing a driving test.', '', 'No. It depends on how well the person drives.'),
], h=40, ln=[('Yes / no', ''), ('Reason', ''), ('', '')])

std_r6 = R('write the chance word for each probability: <i>impossible, unlikely, even chance, likely</i> or <i>certain</i>.', 3, [
    Q('A probability of <b>0.9</b>', '', word(Fr(9, 10))),
    Q(f'A probability of <b>{F(1, 2)}</b>', '', word(Fr(1, 2))),
    Q('A <b>2%</b> chance', '', word(Fr(2, 100)) + ' (almost impossible)'),
], h=20, ln=[('Word', '')])

STD = dict(
    rem1=f'impossible = 0 · unlikely: between 0 and {F(1, 2)} · even chance = {F(1, 2)} · likely: between {F(1, 2)} and 1 · certain = 1',
    p1=[std_r1, std_r2],
    rem2='sample space: every possible outcome, each written once, in braces { } · event: the outcomes we want · equally likely: the same chance (equal sectors, a fair die, chosen at random)',
    p2=[std_r3, std_r4, std_r5, std_r6],
    rem3=f'0 = impossible · {F(1, 2)} = even chance · 1 = certain · list each outcome once · equally likely means the same chance',
    p3=[
        Q('Mark on the scale: A rolling a 6 on a die, B rolling a number less than 7, C a coin landing heads.', prob_scale(46, words=False), 'A between 0 and ½ (near 0), B at 1, C at ½.', ln=[]),
        Q(f'Write {F(3, 4)} as a decimal and as a percentage.', '', f'{dec(Fr(3, 4))} and {pct(Fr(3, 4))}', tag='Year 7'),
        Q('One tile is chosen at random. List the sample space.', tiles('KINGSCLIFF', 4.4), f'{setstr(uniq("KINGSCLIFF"))}: {len(uniq("KINGSCLIFF"))} outcomes'),
        Q('Are the outcomes of ‘tomorrow’s weather: sunny, cloudy or rainy’ equally likely? Explain.', '', 'No. The weather depends on the season and the conditions, so the three are not equally likely.'),
        Q('This spinner is spun. Which is more likely: red or blue? Explain.', spinner(S('red', 'blue', 'red', 'green', 'red', 'blue'), 15), 'Red: it has 3 sectors and blue has only 2.'),
        Q('Sam says, ‘On a die, a 6 is less likely than a 1 because 6 is a bigger number.’ Is Sam right? Explain.', '', 'No. On a fair die every number is equally likely.'),
        Q('Describe the chance of choosing a green counter, in words.', bag([('green', 4), ('yellow', 4)], 15), f'Even chance ({word(Fr(4, 8))}): 4 of the 8 counters are green.'),
        Q('Write 0.35 as a percentage, and as a fraction in simplest form.', '', f'35% and {fr(Fr(35, 100))}', tag='Year 7'),
        Q('A coin lands tails 7 times in a row. Is heads more likely on the next toss? Explain.', coin('T', 9, 'silver'), 'No. It is still an even chance: the coin does not remember earlier tosses.'),
    ],
    word=[
        Q('The forecast for the Tweed is ‘a 70% chance of rain’. Describe the chance in words. Is rain certain? Explain.', '', 'Likely. It is not certain, because 70% is less than 100%.'),
        Q('Colour this spinner’s 4 equal sectors so that landing on blue is <i>likely</i> but not <i>certain</i>. Explain why your spinner works.', spinner(S('white', 'white', 'white', 'white'), 14, letters=False), '3 blue sectors and 1 other colour: 3 of 4 is more than half but less than all.'),
        Q('Amy and Cara are in 8K; Ben and Dev are in 8R. One of the four is chosen at random as captain. List the sample space. Is the captain more likely to come from 8K?', '', '{Amy, Ben, Cara, Dev}. No: 2 are from each class, so it is an even chance.'),
    ],
)

# ---------------------------------------------------------------- extension
ext_r1 = R('count the blue sectors, then describe the chance of landing on blue in words.', 4,
           [blue_q(S('blue', 'red', 'yellow', 'green', 'red', 'blue')), blue_q(S('blue', 'blue', 'red')),
            blue_q(S('blue', 'blue', 'red', 'yellow')), blue_q(S('red', 'green', 'yellow'))],
           h=32, ln=[('Blue / total', ''), ('Word', '')])
coins3 = coin('H', 7) + coin('T', 7, 'silver') + coin('H', 7)
ext_r2 = R('list the sample space and count the outcomes. Watch out for repeats.', 4, [
    Q('Spinning this spinner', spinner([('white', 1, '1'), ('yellow', 1, '2'), ('yellow', 1, '2'), ('green', 1, '3'), ('green', 1, '3'), ('green', 1, '3')], 13, letters=False), '{1, 2, 3}: 3 outcomes'),
    Q('Choosing one tile', tiles('TWEEDHEADS', 3.6), f'{setstr(uniq("TWEEDHEADS"))}: {len(uniq("TWEEDHEADS"))} outcomes'),
    Q('The last digit of a car number plate', '', '{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}: 10 outcomes'),
    Q('The number of heads when 3 coins are tossed together', coins3, '{0, 1, 2, 3}: 4 outcomes'),
], h=30, ln=SS_LN)

ext_r3 = R('list the outcomes in each event, in braces { }.', 3, [
    Q('A 10-sided die numbered 1 to 10 shows a prime number.', poly_die(12, 7, 11), setstr([x for x in range(1, 11) if x in PRIMES])),
    Q('A month with exactly 30 days is chosen.', '', '{April, June, September, November}'),
    Q('A normal die shows a factor of 12.', die3d(11, 4, 6, 2), setstr(die_p(lambda x: 12 % x == 0)[0])),
], h=36, ln=[('Event', '{ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }'), ('', '')])

ext_r4 = R('are the outcomes equally likely? Write <i>yes</i> or <i>no</i>, then give a reason.', 3, [
    Q('The number of heads when 3 coins are tossed.', coins3, 'No. 1 head or 2 heads can happen in more ways than 0 or 3 heads.'),
    Q('The first letter of a person’s first name.', '', 'No. Some letters (like J or S) start far more names than others (like Q or X).'),
    Q('A whole number from 1 to 20 made by a random number generator.', calculator('RanInt#(1,20)', '13', 8), 'Yes. A random number generator makes each number equally likely.'),
], h=42, ln=[('Yes / no', ''), ('Reason', ''), ('', '')])

prob_tiles = 'PROBABILITY'
ext_r5 = R('order the events from least to most likely. Explain using the number of outcomes.', 3, [
    Q('A die is rolled. A: an even number. B: 5 or more. C: less than 2.', die3d(10, 1, 5, 3),
      f'C ({len(die_p(lambda x: x < 2)[0])} outcome), B ({len(die_p(lambda x: x >= 5)[0])}), A ({len(die_p(lambda x: x % 2 == 0)[0])}).'),
    Q('One tile is chosen. Event (i): a B. Event (ii): an I. Event (iii): a vowel.', tiles(prob_tiles, 3.4),
      f'(i) and (ii) are equally likely ({prob_tiles.count("B")} tiles each), then (iii) ({sum(1 for c in prob_tiles if c in "AEIOU")} tiles: O, A, I, I).'),
    Q('The spinner is spun. A: red. B: blue. C: yellow.', spinner(S('red', 'red', 'blue', 'green', 'red', 'yellow', 'blue', 'red'), 14),
      'C (1 sector), B (2), A (4).'),
], h=44, ln=[('Order', ''), ('Reason', ''), ('', '')])
assert prob_tiles.count('B') == prob_tiles.count('I') == 2

ext_r6 = R('probabilities as numbers. Answer each one and show how you know.', 3, [
    Q('Write a probability, as a decimal, for an event that is unlikely but not impossible.', '', 'Any decimal between 0 and 0.5, e.g. 0.2.'),
    Q(f'Which is more likely: an event with probability 0.45, or one with probability {F(4, 9)}?', '', f'{F(4, 9)} = {dec(Fr(4, 9), 3)}…, so the event with probability 0.45 is more likely.'),
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
    rem2='sample space: each outcome once · event: the outcomes we want · compare events by counting their outcomes · a probability is never below 0 or above 1',
    p2=[ext_r3, ext_r4, ext_r5, ext_r6],
    rem3='equally likely means the same chance, not just the same number of names · likely: more than half · unlikely: less than half, but not 0',
    p3=[
        Q('Colour these 5 equal sectors so that red is twice as likely as blue, and green is impossible.', spinner(S(*['white'] * 5), 15, letters=False),
          '2 red, 1 blue and 2 of another colour (not green), e.g. R, R, B, Y, Y.', ln=LN_A),
        Q(f'Write {F(7, 8)} as a decimal and as a percentage.', '', f'{dec(Fr(7, 8))} and {pct(Fr(7, 8))}', tag='Year 7'),
        Q('Spinner A has 3 equal sectors, 1 blue. Spinner B has 8 equal sectors, 3 blue. Which gives the better chance of blue? Explain.', '',
          f'B: {F(3, 8)} = {dec(Fr(3, 8))}, but {F(1, 3)} = {dec(Fr(1, 3), 3)}…'),
        Q('A bag holds 10 red and blue counters. Red is likely; blue is unlikely but possible. How many red counters could there be? List every possibility.', '',
          ', '.join(str(r) for r in range(11) if Fr(r, 10) > Fr(1, 2) and 0 < Fr(10 - r, 10) < Fr(1, 2))),
        Q('Jo writes the sample space for this spinner as {red, red, blue}. What is wrong? Write it correctly.', spinner(S('red', 'red', 'blue'), 13),
          'Each outcome is listed once: {red, blue}. (The outcomes are not equally likely.)'),
        Q(f'Order from least to most likely: A 0.6, B {F(3, 5)}, C 62%, D {F(5, 8)}.', '',
          f'A and B (both 0.6) are equally likely, then C (0.62), then D ({dec(Fr(5, 8))}).', tag='Year 7'),
        Q('Kingscliff’s soccer team has won 18 of its last 20 games. Is winning the next game certain? Are a win and a loss equally likely? Explain.', '',
          'Likely, but not certain. Not equally likely: wins have been far more common.'),
        Q('A die is weighted so that a 6 comes up half the time. Are the six outcomes equally likely? Describe the chance of a 6.', die3d(10, 6, 6, 6),
          'No. Rolling a 6 is an even chance; each other number is unlikely.'),
        Q('A fair die is rolled. Describe an event with each probability: (a) 0 (b) 1 (c) ½.', '',
          'e.g. (a) rolling a 7 (b) rolling less than 7 (c) rolling an even number.'),
    ],
    word=[
        Q('The surf-club roster picks 1 of its 12 members at random: 5 are in Year 8, 4 in Year 9 and 3 in Year 10. Describe the chance that the person is in Year 8, and that they are in Year 11.', '',
          'Year 8: unlikely, because 5 of 12 is less than half. Year 11: impossible, because no members are in Year 11.'),
        Q('A spinner has 8 equal sectors coloured red, blue and yellow. Red is likely, blue and yellow are equally likely, and yellow is possible. Find every possible design.', '',
          'Only one: 6 red, 1 blue, 1 yellow. (4 red, 2 blue, 2 yellow gives red an even chance, not likely.)'),
        Q('Roll a die: Ava wins on 1 or 2, Ben on 3, 4 or 5, and Cal on 6. Is the game fair? Change the rules to make it fair.', '',
          'Not fair: Ava has 2 outcomes, Ben 3 and Cal 1. Fair: give each player 2 numbers, e.g. Ava 1–2, Ben 3–4, Cal 5–6.'),
    ],
)

LESSON = dict(key='L1', num='1', title='Chance and the sample space', sub=SUB,
              li='describe chance with words and with numbers from 0 to 1, list a sample space, and decide whether outcomes are equally likely.',
              sc=['place an event on the probability scale from 0 to 1.',
                  'list the sample space of a chance experiment.',
                  'decide, with a reason, whether outcomes are equally likely.'],
              notes=NOTES, ex1=EX1, ex2=EX2, std=STD, ext=EXT)

# page 3 keeps 6 mixed questions (2 rows of 3) so there is room to work
STD['p3'] = [STD['p3'][i] for i in (0, 1, 2, 4, 5, 8)]
EXT['p3'] = [EXT['p3'][i] for i in (0, 2, 3, 4, 5, 7)]
