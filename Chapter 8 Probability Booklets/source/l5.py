from engine import Q, R, LN_W, LN_A, LN_A2
from gfx import *
from pm import *
from layout import F

SUB = 'Probability • MA4-PRO-C-01'


def show(fav, tot, form='frac', dp=None):
    p = Fr(fav, tot)
    base = frs(fav, tot) + (f' = {fr(p)}' if p.denominator != tot else '')
    if form == 'dec':
        return base + f' = {dec(p, dp)}'
    if form == 'pct':
        return base + f' = {pct(p, dp)}'
    return base


# ---------------------------------------------------------------- shared data sets
VINH_SP = [('red', 2, None), ('green', 1, None), ('yellow', 1, None)]
VINH = dict(red=44, green=25, yellow=11)
NV = sum(VINH.values())
MATCH = {48: 3, 49: 6, 50: 20, 51: 16, 52: 4, 53: 1}
NM = sum(MATCH.values())
DIE80 = [11, 13, 9, 13, 12, 22]
DECL = [10, 11, 13, 7, 8, 11]
SUMS = dict(zip(range(2, 13), [0, 2, 4, 6, 5, 5, 9, 6, 8, 3, 2]))
NS = sum(SUMS.values())
assert (NV, NM, sum(DIE80), sum(DECL), NS) == (80, 50, 80, 60, 50)

VINH_TAB = htab('Colour', ['Red', 'Green', 'Yellow'], [VINH['red'], VINH['green'], VINH['yellow']])
MATCH_TAB = htab('Matches', list(MATCH), list(MATCH.values()), 'Boxes')
DIE80_TAB = htab('Outcome', range(1, 7), DIE80)
DECL_TAB = htab('Outcome', range(1, 7), DECL)
SUMS_TAB = htab('Sum', list(SUMS), list(SUMS.values()), size=7.8)

NOTES = f'''<div class="tnotes" style="grid-template-columns:1.15fr 1fr .95fr">
<div><h4>KEY TERMS</h4>
<p><b>theoretical (expected) probability:</b> worked out from equally likely outcomes, e.g. P(6) = {F(1, 6)}</p>
<p><b>observed (experimental) probability</b> or <b>relative frequency:</b> worked out from the results of trials</p>
<p><b>frequency:</b> how many times something happened</p>
<p><b>biased:</b> unfair: some outcomes are more likely</p>
<p><b>simulation:</b> an experiment that copies a real one, e.g. a random number generator</p></div>
<div><h4>FORMULA</h4>
<div class="fbox">observed P(E) = {F('number of times E happened', 'total number of trials', True)}</div>
<p>More trials → the observed probability is usually closer to the theoretical probability.</p>
<p>Random numbers: calculator <b>RanInt#(1,6)</b>; spreadsheet <b>=RANDBETWEEN(1,6)</b></p></div>
<div><h4>EXAMPLE</h4>
<p>Harper rolls a die 60 times; a 2 comes up 15 times.</p>
<p>observed P(2) = {frs(15, 60)} = {fr(Fr(1, 4))}</p>
<p>theoretical P(2) = {fr(Fr(1, 6))}</p>
<p>{fr(Fr(1, 4))} &gt; {fr(Fr(1, 6))}: more 2s than expected. Biased? Roll many more times to check.</p></div>
</div>'''

EX1 = dict(
    instr='Observed P(E) = number of times E happened ÷ total trials.',
    parts=[
        ('Observed', die3d(12, 2, 2, 2), 'A die is rolled 60 times and 2 comes up 15 times. Find the observed P(2).'),
        ('Compare', '', 'Find the theoretical P(2) for a fair die. Is the observed P(2) higher or lower?'),
        ('Spinner', spinner(VINH_SP, 14), 'Vinh spins 80 times: red 44, green 25, yellow 11. Find the observed P(red).'),
        ('Percentage', coin('T', 10, 'silver'), 'Sefina tosses a coin: 135 heads and 115 tails. Find the observed P(tails), as a %.'),
    ], box=17,
    ans=[show(15, 60), f'{fr(Fr(1, 6))}. The observed P(2) = {fr(Fr(1, 4))} is higher.', show(44, 80), show(115, 250, 'pct')])

d80p6 = Fr(DIE80[5], 80)
EX2 = dict(
    instr='Read each table carefully: the total number of trials is the bottom of the fraction.',
    data=f'<div style="text-align:center"><div class="sans" style="font-size:7pt;color:#555">Matches in 50 boxes</div>{MATCH_TAB}</div>'
         f'<div style="text-align:center"><div class="sans" style="font-size:7pt;color:#555">A die rolled 80 times</div>{DIE80_TAB}</div>',
    parts=[
        ('Table', '', 'Matchboxes: find the observed P(exactly 51 matches).'),
        ('Fewer than', '', 'Matchboxes: find the observed P(fewer than 50 matches).'),
        ('Biased?', '', 'The die rolled 80 times: do you think it is biased? Give a reason.'),
        ('Simulate', calculator('RanInt#(1,6)', '4', 10), 'Use RanInt#(1,6) to roll a die 20 times. Find your observed P(an even number).'),
    ], box=17,
    ans=[show(MATCH[51], NM), show(MATCH[48] + MATCH[49], NM),
         f'Probably: 6 came up 22 times (observed P(6) = {dec(d80p6)}) but each other number about 9–13 times. A fair die gives about 13 of each. Roll more to be sure.',
         f'Answers vary; compare with the theoretical {fr(Fr(1, 2))}.'])

# ---------------------------------------------------------------- standard
std_p1 = [
    R('find each observed probability. Write it in simplest form.', 4, [
        Q('A coin is tossed 20 times and lands heads 12 times. Find the observed P(heads).', '', show(12, 20)),
        Q('A die is rolled 30 times and shows 6 four times. Find the observed P(6).', '', show(4, 30)),
        Q('A basketballer scores 35 of 50 shots. Find the observed P(scores).', '', show(35, 50)),
        Q('A spinner is spun 25 times and lands on blue 10 times. Find the observed P(blue).', '', show(10, 25)),
    ], h=30, ln=[('Working', ''), ('P =', '')]),
    R('is each probability theoretical (T) or observed (O)? Write T or O.', 4, [
        Q(f'P(heads) = {F(1, 2)}, because a coin has two equal sides.', coin('H', 7), 'T'),
        Q('Kingscliff won 14 of its 20 games, so P(win) = 0.7.', '', 'O'),
        Q(f'P(rolling a 3) = {F(1, 6)} for a fair die.', die3d(8, 3, 1, 2), 'T'),
        Q('120 of last year’s 365 days were rainy, so P(rain) ≈ 0.33.', '', 'O'),
    ], h=24, ln=[('T or O', '')]),
]
std_p2 = [
    R('Vinh spun this spinner 80 times. Use the results.', 3, [
        Q('Find the observed P(red).', '', show(VINH['red'], NV)),
        Q('Find the theoretical P(red).', '', f'{fr(spin_p(VINH_SP, "red"))} (red is half the spinner)'),
        Q('Find the observed P(yellow).', '', show(VINH['yellow'], NV)),
    ], h=22, ln=[('Working', ''), ('Answer', '')], info=spinner(VINH_SP, 16) + VINH_TAB),
    R('the matches in 50 matchboxes were counted.', 3, [
        Q('How many matchboxes were tested? Check by adding.', '', f'3 + 6 + 20 + 16 + 4 + 1 = {NM}'),
        Q('Find the observed P(exactly 51 matches).', '', show(MATCH[51], NM)),
        Q('Find the observed P(fewer than 50 matches).', '', show(MATCH[48] + MATCH[49], NM)),
    ], h=22, ln=[('Working', ''), ('Answer', '')], info=MATCH_TAB),
    R('Declan rolled a die 60 times.', 3, [
        Q('Find the observed P(3).', '', show(DECL[2], 60)),
        Q('Find the observed P(5 or 6).', '', show(DECL[4] + DECL[5], 60)),
        Q('Find the theoretical P(5 or 6).', '', show(2, 6)),
    ], h=22, ln=[('Working', ''), ('Answer', '')],
      info=DECL_TAB + bar_chart(range(1, 7), DECL, 54, 30, ymax=15, step=5, xlabel='Outcome')),
    R('run your own simulation with a random number generator.', 3, [
        Q('Use RanInt#(1,6) on your calculator (or =RANDBETWEEN(1,6) in a spreadsheet) to roll a die 30 times. Tally your results.',
          vtab(['Outcome', '1', '2', '3', '4', '5', '6'], [['Tally', '', '', '', '', '', ''], ['Frequency', '', '', '', '', '', '']], 8.6).replace('<td></td>', '<td class="blank" style="min-width:11mm"></td>'),
          'Answers vary (frequencies should add to 30).', ln=[], span=2, figtop=True),
        Q(f'Find your observed P(6). Compare it with the theoretical P(6) = {F(1, 6)}. Why might they differ?', calculator('RanInt#(1,6)', '6', 8),
          'Answers vary. With only 30 trials the observed probability can be quite far from ⅙.'),
    ], h=34, ln=LN_A2),
]
assert spin_p(VINH_SP, 'red') == Fr(1, 2)
odd_sums = sum(f for s, f in SUMS.items() if s % 2)
STD = dict(
    rem1=f'observed P(E) = {F("number of times E happened", "total number of trials")} · theoretical: from equally likely outcomes · observed: from results',
    p1=std_p1,
    rem2='the total number of trials goes on the bottom · add the frequencies to find the total · ‘5 or 6’: add their frequencies',
    p2=std_p2,
    rem3='observed P = frequency ÷ total trials · more trials give a better estimate',
    p3=[
        Q('Kai tosses a coin 200 times and gets 92 heads. Find the observed P(tails), as a decimal.', '', show(200 - 92, 200, 'dec')),
        Q('A pair of dice was rolled 50 times and the sum recorded. Find the observed P(a sum of 8), as a decimal.', SUMS_TAB,
          show(SUMS[8], NS, 'dec'), span=2, figtop=True),
        Q('Use the table in Question 2. Find the observed P(a sum of 5 or 6).', '', show(SUMS[5] + SUMS[6], NS)),
        Q('Use the table in Question 2. Which sum came up most often? Find its observed probability.', '', f'8: {show(SUMS[8], NS)}'),
        Q(f'Write {F(13, 50)} as a percentage.', '', pct(Fr(13, 50)), tag='Year 7'),
    ],
    word=[
        Q('Harper rolled a die 60 times and 2 came up 15 times. Harper says the die is biased. Is there enough evidence? What could Harper do to check?', '',
          'Observed P(2) = ¼, but a fair die gives about 10 twos in 60 rolls. 15 is suspicious but 60 rolls is not many: roll it hundreds more times.'),
        Q('The canteen’s last 200 lunch orders were 70 wraps, 50 sushi and 80 burgers. Find the observed P(the next order is a wrap). Why is this only an estimate?', '',
          f'{show(70, 200, "dec")}. It is based on past orders; tomorrow’s orders may be different.'),
        Q('To estimate P(a family of 4 children are all girls), Jo tosses 4 coins (heads = girl) 50 times. 4 heads came up 4 times. Find the observed probability. How could Jo improve the estimate?', coin('H', 6) + coin('H', 6) + coin('H', 6) + coin('H', 6),
          f'{show(4, 50, "dec")}. Run many more trials.'),
    ],
)
assert odd_sums == 22

# ---------------------------------------------------------------- extension
comp_sums = sum(f for s, f in SUMS.items() if s in (4, 6, 8, 9, 10, 12))
sums_3_25 = [s for s, f in SUMS.items() if Fr(f, NS) == Fr(3, 25)]
sums_16 = [s for s, f in SUMS.items() if Fr(f, NS) == Fr(16, 100)]
mean_m = Fr(sum(k * v for k, v in MATCH.items()), NM)
mean_s = Fr(sum(k * v for k, v in SUMS.items()), NS)
ext_p1 = [
    R('find each observed probability as a decimal.', 4, [
        Q('A coin is tossed 250 times: 135 heads. Find the observed P(tails).', '', show(115, 250, 'dec')),
        Q('A die is rolled 80 times: 1 or 6 comes up 25 times. Find the observed P(1 or 6).', '', show(25, 80, 'dec')),
        Q('A goalkeeper saves 18 of 24 penalties. Find the observed P(save).', '', show(18, 24, 'dec')),
        Q('73 of last year’s 365 days had rain. Find the observed P(rain).', '', show(73, 365, 'dec')),
    ], h=30, ln=[('Working', ''), ('P =', '')]),
    R('theoretical (T) or observed (O)? Write T or O and give a reason.', 4, [
        Q('40 of 100 Tweed residents surveyed own a dog, so P(owns a dog) = 0.4.', '', 'O: from survey results'),
        Q(f'P(drawing an ace from a deck) = {F(1, 13)}.', '', 'T: 4 equally likely aces in 52 cards'),
        Q('60 of 200 cars passing the school were white, so P(white) = 0.3.', '', 'O: from counting cars'),
        Q(f'P(a random month starts with J) = {F(1, 4)}.', '', 'T: 3 of 12 equally likely months'),
    ], h=28, ln=[('T or O', ''), ('Reason', '')]),
]
ext_p2 = [
    R('the matches in 50 matchboxes were counted.', 3, [
        Q('Find the observed P(at least 50 matches), as a decimal.', '', show(50 - 9, NM, 'dec')),
        Q('Find the observed P(not exactly 50 matches), as a decimal.', '', show(NM - MATCH[50], NM, 'dec')),
        Q('The label says ‘average contents 50’. Find the mean number of matches. Is the label fair?', '', f'mean = {frs(2515, 50)} = {dec(mean_m)}: yes, fair', tag='Ch 7'),
    ], h=24, ln=[('Working', ''), ('Answer', '')], info=MATCH_TAB),
    R('a die was rolled 80 times.', 3, [
        Q('Find the observed P(1), as a percentage.', '', show(DIE80[0], 80, 'pct')),
        Q('Find the observed P(an even number), as a decimal.', '', show(DIE80[1] + DIE80[3] + DIE80[5], 80, 'dec')),
        Q('Is this die biased? Explain with numbers.', '', '6 came up 22 times; a fair die gives about 13 of each in 80 rolls. It looks biased towards 6, but more rolls would make us surer.'),
    ], h=24, ln=[('Working', ''), ('Answer', '')], info=DIE80_TAB),
    R('a pair of dice was rolled 50 times and the sum recorded.', 3, [
        Q('Find the observed P(a composite sum), as a decimal.', '', f'sums 4, 6, 8, 9, 10, 12: {show(comp_sums, NS, "dec")}'),
        Q(f'Which sum(s) had an observed probability of {F(3, 25)}?', '', ' and '.join(map(str, sums_3_25)) + f' ({frs(6, 50)} each)'),
        Q('Which sum had an observed probability of 16%?', '', f'{sums_16[0]} ({frs(8, 50)})'),
    ], h=24, ln=[('Working', ''), ('Answer', '')], info=SUMS_TAB),
    R('run a simulation and watch the observed probability change.', 3, [
        Q('Use RanInt#(1,2) (1 = heads) to toss a coin 40 times, in blocks of 10. Record the heads so far and the observed P(heads) after each block.',
          vtab(['Tosses', '10', '20', '30', '40'], [['Heads so far', '', '', '', ''], ['Observed P(heads)', '', '', '', '']], 8.4).replace('<td></td>', '<td class="blank" style="min-width:13mm"></td>'),
          'Answers vary.', ln=[], span=2, figtop=True),
        Q('What happens to the observed P(heads) as the tosses increase? Combine your results with 4 classmates (200 tosses) and comment.', '',
          'Answers vary: it usually settles closer to 0.5.'),
    ], h=34, ln=LN_A2),
]
assert sums_3_25 == [5, 9] and sums_16 == [10] and comp_sums == 34 and mean_m == Fr(503, 10)
EXT = dict(
    rem1=STD['rem1'],
    p1=ext_p1,
    rem2='observed P = frequency ÷ total trials · ‘at least 50’ means 50 or more · a biased die has outcomes that are not equally likely',
    p2=ext_p2,
    rem3='frequency = observed P × number of trials · work backwards from a probability to a count',
    p3=[
        Q('After 50 tosses, the observed P(heads) = 0.58. After 30 more tosses, the observed P(heads) for all 80 = 0.55. How many heads were in the last 30 tosses?', '',
          f'{Fr(58, 100) * 50} heads, then {Fr(55, 100) * 80} heads: {Fr(55, 100) * 80 - Fr(58, 100) * 50} in the last 30'),
        Q('A spinner is spun 120 times and the observed P(red) = 0.35. How many times did it land on red?', '', f'0.35 × 120 = {Fr(35, 100) * 120}'),
        Q('A die is rolled 40 times: 1 five times, 2 eight times, 3 x times, 4 six times, 5 seven times and 6 nine times. Find x and the observed P(3).', '',
          f'x = 40 − 35 = 5; {show(5, 40, "dec")}'),
        Q('After 20 games, the observed P(Kingscliff wins) = 0.65. They win the next 5 games. Find the new observed P(win).', '',
          f'13 wins, then 18 of 25: {show(18, 25, "dec")}'),
        Q('Use the dice-sum table from Round 5. Find the mean sum.', '', f'{frs(380, 50)} = {dec(mean_s)}', tag='Ch 7'),
        Q('A biased coin lands tails 248 times in 400 tosses. Find the observed P(heads).', '', show(152, 400, 'dec')),
    ],
    word=[
        Q(f'Jo’s family simulation gave 4 girls 4 times in 50 trials. The theoretical P(4 girls) = {F(1, 16)} (you will see why in Stage 5). Jo runs 50 more trials and gets 4 girls twice. Find the observed probability for all 100 trials. Is it closer to {F(1, 16)}?', '',
          f'50 trials: 0.08. 100 trials: {show(6, 100, "dec")}. {F(1, 16)} = 0.0625, so yes, 0.06 is closer.'),
        Q('A spinner has 3 colours. In 200 spins: red 98, blue 52, green 50. Sketch what the spinner probably looks like, and explain.', '',
          'Red about half (98 ÷ 200 ≈ 0.5), blue and green about a quarter each.'),
        Q('Two classes test a coin. 8K gets 23 heads in 40 tosses; 8R gets 112 heads in 200 tosses. Find each observed P(heads). Which is the better estimate, and why?', '',
          f'8K {show(23, 40, "dec")}; 8R {show(112, 200, "dec")}. 8R: more trials.'),
    ],
)
assert Fr(58, 100) * 50 == 29 and Fr(55, 100) * 80 == 44
assert abs(Fr(6, 100) - Fr(1, 16)) < abs(Fr(8, 100) - Fr(1, 16))

LESSON = dict(key='L5', num='5', title='Observed probability', sub=SUB,
              li='find observed probabilities from experiments and data, and compare them with theoretical probabilities.',
              sc=['find an observed probability: frequency ÷ total trials.',
                  'tell theoretical and observed probability apart.',
                  'run a simulation with a random number generator.'],
              notes=NOTES, ex1=EX1, ex2=EX2, std=STD, ext=EXT)
assert sum(k * v for k, v in SUMS.items()) == 380 and sum(k * v for k, v in MATCH.items()) == 2515
