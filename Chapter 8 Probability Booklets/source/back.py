"""Back matter: chapter summary, if you were away, chapter review, exit tickets,
homework strips. Every answer is computed or checked here too."""
from pm import *
from gfx import *
from layout import F


def show(fav, tot, form='frac', dp=None):
    p = Fr(fav, tot)
    base = frs(fav, tot) + (f' = {fr(p)}' if p.denominator != tot else '')
    if form == 'dec':
        return base + f' = {dec(p, dp)}'
    if form == 'pct':
        return base + f' = {pct(p, dp)}'
    return base


# ---------------------------------------------------------------- key facts
FACTS_STD = [
    '<b>Sample space</b>: every possible outcome, each written once, in braces { } <span class="blue">(L1)</span>',
    f'<b>Probability scale</b>: 0 impossible · {F(1, 2)} even chance · 1 certain <span class="blue">(L1)</span>',
    f'<b>P(E)</b> = {F("number of favourable outcomes", "total number of outcomes")} when outcomes are equally likely <span class="blue">(L2)</span>',
    '<b>Converting</b>: fraction → decimal: top ÷ bottom; decimal → percentage: × 100% <span class="blue">(L2)</span>',
    '<b>‘or’</b> for different groups: add the counts, e.g. P(red or blue) <span class="blue">(L2)</span>',
    '<b>Complement</b>: P(not E) = 1 − P(E); all probabilities add to 1 <span class="blue">(L3)</span>',
    '<b>Checklist</b>: total → favourable → ‘not’? → form asked → check <span class="blue">(L4)</span>',
    f'<b>Observed P(E)</b> = {F("number of times E happened", "total number of trials")} <span class="blue">(L5)</span>',
    '<b>More trials</b>: the observed probability usually gets closer to the theoretical one <span class="blue">(L5)</span>',
    '<b>Expected frequency</b> = probability × number of trials <span class="blue">(L6)</span>',
    '<b>Fair or biased?</b> Close to expected: probably fair. Far off over many trials: probably biased <span class="blue">(L6)</span>',
]
FACTS_EXT = FACTS_STD + [
    '<b class="x">Venn diagram</b>: A and B = the overlap; A or B = inside either circle; not both = the outer parts; mutually exclusive = no overlap <span class="maroon">(E1)</span>',
    '<b class="x">Two-way table</b>: each cell is an ‘and’; missing cell = total − known cells; P = cell ÷ grand total <span class="maroon">(E2)</span>',
]

# ---------------------------------------------------------------- if you were away (two worked examples per lesson)
AWAY = {
    'L1': [('a sample space', 'List the sample space for a spinner with sectors red, blue, red, green.',
            '<p><b>Step 1</b> Write each colour once: {red, blue, green}.</p><p><b>Step 2</b> Count: 3 outcomes.</p><p><b>Step 3</b> Red has 2 of the 4 sectors, so the outcomes are <b>not equally likely</b>.</p>'),
           ('chance words', 'The forecast says a 30% chance of rain. Describe the chance.',
            '<p><b>Step 1</b> Compare with 50% (even chance): 30% is less.</p><p><b>Step 2</b> So rain is <b>unlikely</b>.</p><p><b>Step 3</b> It is not 0%, so it is still possible.</p>')],
    'L2': [('P(E) from counters', 'A bag has 5 red, 3 blue and 4 green counters. Find P(red).',
            f'<p><b>Step 1</b> Total = 5 + 3 + 4 = 12.</p><p><b>Step 2</b> Favourable: 5 red.</p><p><b>Step 3</b> P(red) = {fr(Fr(5, 12))}</p>'),
           ('a percentage', 'A die is rolled. Find P(a number greater than 4), as a percentage.',
            f'<p><b>Step 1</b> Favourable: {{5, 6}}, 2 of 6.</p><p><b>Step 2</b> {frs(2, 6)} = {fr(Fr(1, 3))}</p><p><b>Step 3</b> {fr(Fr(1, 3))} × 100% = {pct_third(Fr(1, 3))} ≈ 33.3%</p>')],
    'L3': [('P(not E) with decimals', 'P(rain) = 0.15. Find P(no rain).',
            '<p><b>Step 1</b> ‘No rain’ is the complement of ‘rain’.</p><p><b>Step 2</b> P(no rain) = 1 − 0.15 = <b>0.85</b></p>'),
           ('P(not E) with fractions', 'A pack has 10 red, 6 yellow and 4 green cards. Find P(not yellow).',
            f'<p><b>Step 1</b> P(yellow) = {frs(6, 20)} = {fr(Fr(3, 10))}</p><p><b>Step 2</b> P(not yellow) = 1 − {fr(Fr(3, 10))} = <b>{fr(Fr(7, 10))}</b></p>')],
    'L4': [('an ‘or’ problem', 'A number from 1 to 15 is chosen. Find P(a multiple of 3 or 5).',
            f'<p><b>Step 1</b> List: {{3, 5, 6, 9, 10, 12, 15}} (15 once).</p><p><b>Step 2</b> 7 of 15: P = <b>{fr(Fr(7, 15))}</b></p>'),
           ('no memory', 'A coin has shown tails 7 times in a row. Find P(tails next).',
            f'<p>Each toss is a fresh start: the coin does not remember.</p><p>P(tails) = <b>{fr(Fr(1, 2))}</b></p>')],
    'L5': [('observed probability', 'A die is rolled 60 times; 2 comes up 15 times. Find the observed P(2).',
            f'<p><b>Step 1</b> Observed P = times ÷ trials = {frs(15, 60)} = <b>{fr(Fr(1, 4))}</b></p><p><b>Step 2</b> Theoretical P(2) = {fr(Fr(1, 6))}, so 2 came up more than expected.</p>'),
           ('from a table', 'Matches in 50 boxes: 48 (3), 49 (6), 50 (20), 51 (16), 52 (4), 53 (1). Find the observed P(fewer than 50).',
            f'<p><b>Step 1</b> Fewer than 50: 48 or 49, 3 + 6 = 9 boxes.</p><p><b>Step 2</b> P = <b>{fr(Fr(9, 50))}</b></p>')],
    'L6': [('expected frequency', 'A die is rolled 72 times. Find the expected number of 4s.',
            f'<p>Expected = P × trials = {fr(Fr(1, 6))} × 72 = <b>12</b></p>'),
           ('predicting from data', 'Harper’s die gave 15 twos in 60 rolls. How many 2s in 500 rolls?',
            f'<p><b>Step 1</b> Observed P(2) = {frs(15, 60)} = {fr(Fr(1, 4))}</p><p><b>Step 2</b> {fr(Fr(1, 4))} × 500 = <b>125</b></p>')],
    'E1': [('drawing a Venn diagram', '30 students: 18 computer, 15 sport, 6 both.',
            '<p><b>Step 1</b> Overlap: 6.</p><p><b>Step 2</b> Computer only 18 − 6 = 12; sport only 15 − 6 = 9.</p><p><b>Step 3</b> Neither: 30 − 27 = 3.</p>'),
           ('exclusive or', 'Same diagram: find P(sport or computer, but not both).',
            f'<p>Not both = the two outer parts: 12 + 9 = 21.</p><p>P = {frs(21, 30)} = <b>{fr(Fr(7, 10))}</b></p>')],
    'E2': [('reading a two-way table', 'Year 7: 13 can swim, 2 cannot; Year 8: 9 can, 3 cannot. Find P(Year 8 and can swim).',
            f'<p><b>Step 1</b> Grand total 27.</p><p><b>Step 2</b> The Year 8 / can swim cell: 9.</p><p><b>Step 3</b> P = {frs(9, 27)} = <b>{fr(Fr(1, 3))}</b></p>'),
           ('a missing cell', 'Saturday: under 18 ?, 18 and over 142, total 198. Find the missing cell.',
            '<p>missing = total − known = 198 − 142 = <b>56</b></p>')],
}

# ---------------------------------------------------------------- chapter review
fam_np = Fr(3, 5)
REVIEW_STD = [
    ('L1', 'List the sample space for a spinner with sectors 1, 2, 2 and 3. How many outcomes are there?', '{1, 2, 3}: 3 outcomes'),
    ('L1', 'A drawing pin is dropped: it lands point up or point down. Are the outcomes equally likely? Explain.', 'No: the pin is not symmetrical, so one way is more likely.'),
    ('L2', 'A bag has 6 red, 4 blue and 2 white marbles. Find P(blue).', show(4, 12)),
    ('L2', 'A die is rolled. Find P(a number less than 5), as a percentage.', f'{show(4, 6)} = {pct_third(Fr(2, 3))} ≈ 66.7%'),
    ('L2', 'One card is taken from a standard deck. Find P(a black king).', show(2, 52)),
    ('L2', f'Write {F(7, 20)} as a decimal and as a percentage.', '0.35 and 35%'),
    ('L3', 'Write the complement of ‘Kingscliff wins the final’.', 'Kingscliff does not win (it loses or draws).'),
    ('L3', 'P(the bus is late) = 0.12. Find P(the bus is not late).', '0.88'),
    ('L3', 'A spinner: P(red) = 0.45, P(blue) = 0.3 and the rest is green. Find P(green).', '0.25'),
    ('L3', 'A family of 5 (2 parents, 3 children) take turns to wash up. Find P(the washer-up is not a parent).', fr(fam_np)),
    ('L4', 'One tile is chosen from T, W, E, E, D. Find P(an E), as a decimal.', show(2, 5, 'dec')),
    ('L4', 'The digits 1, 3, 5 and 8 make a 4-digit number at random, each used once. Find P(the number is odd).', f'{fr(Fr(3, 4))} (it ends in 1, 3 or 5)'),
    ('L5', 'A coin is tossed 80 times and lands heads 36 times. Find the observed P(heads), as a decimal.', show(36, 80, 'dec')),
    ('L5', 'Theoretical or observed? ‘P(a Year 8 student surfs) = 0.3, from a survey.’ Explain.', 'Observed: it comes from survey results.'),
    ('L6', 'A die is rolled 90 times. Find the expected number of 5s.', '15'),
    ('L6', 'A basketballer scored 30 of 50 shots. Predict the number scored in 120 shots.', f'{fr(Fr(3, 5))} × 120 = 72'),
]
mult5_3dig = sum(1 for x in range(100, 1000) if x % 5 == 0)
m35_30 = [x for x in range(1, 31) if x % 3 == 0 or x % 5 == 0]
REVIEW_EXT = [
    ('L1', 'A die is rolled. Order from least to most likely: A a 1, B an odd number, C at most 5.', 'A (1 outcome), B (3), C (5)'),
    ('L2', 'An Esky has 6 lemonade and 4 lime cans. How many colas must be added so that P(cola) = ' + F(1, 3) + '?', '5 (5 of 15)'),
    ('L2', 'One card from a deck. Find P(a red card or a king).', f'26 + 2 = 28: {show(28, 52)}'),
    ('L2', 'A spinner has angles 120° red, 150° blue and 90° green. Find P(blue).', show(150, 360)),
    ('L3', 'P(not E) = 0.62. Find P(E).', '0.38'),
    ('L3', 'A spinner is red, green or blue. P(red) = 2 × P(green) and P(blue) = 0.4. Find P(green).', '0.2'),
    ('L3', 'A 3-digit number (100 to 999) is chosen at random. Find P(not a multiple of 5).', f'{mult5_3dig} multiples of 5: {show(900 - mult5_3dig, 900)}'),
    ('L4', 'A whole number from 1 to 30 is chosen. Find P(a multiple of 3 or 5).', f'{len(m35_30)} numbers: {show(len(m35_30), 30)}'),
    ('L4', 'A die is weighted so P(6) = 0.4 and the other numbers are equally likely. Find P(2).', '0.6 ÷ 5 = 0.12'),
    ('L5', 'After 40 games, the observed P(win) = 0.6. The team then loses 10 games in a row. Find the new observed P(win).', f'24 of 50: {show(24, 50, "dec")}'),
    ('L5', 'A die is rolled 120 times: 1 (18), 2 (22), 3 (20), 4 (19), 5 (21), 6 (x). Find x and the observed P(6).', f'x = 20; {show(20, 120)}'),
    ('L6', 'The expected frequency of an event in 400 trials is 140. Find its probability.', show(140, 400)),
    ('L6', 'The observed P(a car is white) = 0.3. Predict the number of white cars among 450 cars.', '135'),
    ('L6', 'A 4-sector spinner (equal sectors) gave 160 reds in 400 spins. Is it fair? Use the expected frequency.', 'Expected 100 reds; 160 is far more, so it is probably biased.'),
    ('E1', '60 students: 35 play sport, 28 play an instrument and 12 do both. How many do neither? Find P(exactly one).', f'neither 9; exactly one 23 + 16 = 39: {show(39, 60)}'),
    ('E1', 'On a die, are ‘a prime number’ and ‘an even number’ mutually exclusive? Explain.', 'No: 2 is both prime and even.'),
    ('E1', 'P(A) = 0.45, P(B) = 0.3 and P(A and B) = 0.1. Find P(neither).', '1 − 0.65 = 0.35'),
    ('E2', 'Year 7: 40 like, total 70. Year 8: 25 dislike. Grand total 130. Find P(Year 8 and likes).', f'Year 8 total 60, so likes 35: {show(35, 130)}'),
    ('E2', 'A Venn diagram has A only 14, both 6, B only 10 and neither 20. Make a two-way table and find P(not A).', f'not A = 10 + 20 = 30: {show(30, 50)}'),
    ('E2', 'Use the previous question. Find P(A or B, but not both).', show(24, 50)),
]
assert mult5_3dig == 180 and len(m35_30) == 14

# ---------------------------------------------------------------- exit tickets: (easy, medium, hard) std ; (medium, hard, further) ext
TICKETS = {
    'L1': dict(std=[('List the sample space for a spinner with sectors red, blue, red.', '{red, blue}'),
                    ('Is each colour on that spinner equally likely? Explain.', 'No: red has 2 of the 3 sectors.'),
                    ('Describe, in words, the chance of rolling less than 3 on a die.', 'Unlikely (2 of 6 outcomes).')],
               ext=[('List the sample space for the number of heads when 2 coins are tossed.', '{0, 1, 2}'),
                    ('Are those outcomes equally likely? Explain.', 'No: 1 head can happen in 2 ways (HT or TH).'),
                    ('Design a 6-sector spinner where red is likely and blue is unlikely but possible.', 'e.g. 4 red, 1 blue, 1 yellow')]),
    'L2': dict(std=[('A die is rolled. Find P(a 4).', fr(Fr(1, 6))),
                    ('A bag has 3 red and 5 blue counters. Find P(blue), as a percentage.', show(5, 8, 'pct')),
                    ('One card from a deck. Find P(a red ace).', show(2, 52))],
               ext=[('One card from a deck. Find P(a picture card).', show(12, 52)),
                    ('A 10-sided die (1 to 10). Find P(a multiple of 4), as a decimal.', show(2, 10, 'dec')),
                    ('A bag has 4 red counters and some blue. P(red) = 0.2. How many blue?', '16')]),
    'L3': dict(std=[('Write the complement of ‘rolling an even number’.', 'rolling an odd number'),
                    ('P(win) = 0.35. Find P(not win).', '0.65'),
                    ('A jar has 7 red, 5 green and 8 yellow lollies. Find P(not yellow).', show(12, 20))],
               ext=[('Write the complement of ‘at least 3’ on a die, and its probability.', f'at most 2 (1 or 2): {fr(Fr(1, 3))}'),
                    ('P(red) = 0.3, P(blue) = 0.45, the rest green. Find P(not green).', '0.75'),
                    ('P(not E) is four times P(E). Find P(E).', '0.2')]),
    'L4': dict(std=[('A spinner has 5 equal sectors, 1 to 5. Find P(odd), as a percentage.', '60%'),
                    ('30 students: 12 bus, 10 walk, the rest are driven. Find P(driven).', show(8, 30)),
                    ('A coin lands heads 5 times in a row. Find P(heads next). Explain.', f'{fr(Fr(1, 2))}: the coin has no memory.')],
               ext=[('A number from 1 to 100 is chosen. Find P(a perfect square).', show(10, 100)),
                    ('A number from 1 to 20 is chosen. Find P(a multiple of 2 or 5).', show(12, 20)),
                    ('Roll a die: A wins on 1 or 2, B on 3 to 6. Is it fair? Explain.', 'No: A has 2 outcomes, B has 4.')]),
    'L5': dict(std=[('A coin is tossed 40 times: 18 heads. Find the observed P(heads).', show(18, 40)),
                    ('Theoretical or observed: ‘P(rolling a 6) = ⅙’?', 'Theoretical'),
                    ('Why might the observed P(6) after 12 rolls be far from ⅙?', 'Too few trials: chance has a big effect.')],
               ext=[('400 tosses gave 150 tails. Find the observed P(tails), as a decimal.', show(150, 400, 'dec')),
                    ('After 20 shots, observed P(goal) = 0.45. How many goals?', '9'),
                    ('The player then scores 5 of the next 5 shots. Find the new observed P(goal).', f'14 of 25: {show(14, 25, "dec")}')]),
    'L6': dict(std=[('Find the expected number of heads in 60 coin tosses.', '30'),
                    ('Find the expected number of 3s in 120 rolls of a die.', '20'),
                    ('120 rolls gave 34 threes. Is the die biased? Explain.', 'Probably: 34 is far more than the 20 expected.')],
               ext=[('A spinner is ¼ red. Find the expected number of reds in 200 spins.', '50'),
                    ('The expected frequency is 45 in 180 trials. Find the probability.', show(45, 180)),
                    ('Observed P = 0.35 after 60 trials. Predict the number in 500 trials.', '175')]),
    'E1': dict(ext=[('Venn: A only 8, both 3, B only 5, neither 4. Find P(A or B).', show(16, 20)),
                    ('Same diagram: find P(A or B, but not both).', show(13, 20)),
                    ('40 students: 22 surf, 15 skate and 7 do neither. How many do both?', '4')]),
    'E2': dict(ext=[('Year 7: 12 like, 8 dislike. Year 8: 15 like, 5 dislike. Find P(Year 7 and likes).', show(12, 40)),
                    ('Same table: find P(Year 8 or dislikes).', show(15 + 5 + 8, 40)),
                    ('Draw the Venn diagram for that table (circles: Year 7, likes).', 'Year 7 only 8, both 12, likes only 15, neither 5')]),
}

# ---------------------------------------------------------------- homework strips
HW_STD = [
    ('HW 1', 'L1 Chance', [('List the sample space for tossing a coin.', '{heads, tails}'),
                           ('Choose a chance word for a probability of 0.8.', 'likely'),
                           ('Are the outcomes of rolling a fair die equally likely?', 'Yes')]),
    ('HW 2', 'L2 P(E)', [('A die is rolled. Find P(a number greater than 2).', show(4, 6)),
                         ('A bag has 2 red and 6 blue counters. Find P(red), as a decimal.', show(2, 8, 'dec')),
                         ('One card from a deck. Find P(a spade).', show(13, 52))]),
    ('HW 3', 'L3 Complements', [('P(rain) = 0.4. Find P(no rain).', '0.6'),
                                ('Write the complement of ‘winning a raffle’.', 'not winning the raffle'),
                                ('One tile from N, I, P, P, E, R, S. Find P(not a vowel).', show(5, 7))]),
    ('HW 4', 'L4 Problems', [('A number from 1 to 10 is chosen. Find P(a prime).', show(4, 10)),
                             ('One tile from T, W, E, E, D. Find P(not an E).', show(3, 5)),
                             ('A bag of 20 lollies has P(red) = 0.5. How many are red?', '10')]),
    ('HW 5', 'L5 Observed', [('50 tosses gave 27 heads. Find the observed P(heads).', fr(Fr(27, 50))),
                             ('Theoretical or observed: ‘P(heads) = ½’?', 'Theoretical'),
                             ('Why is it better to do many trials?', 'The observed probability gets closer to the true one.')]),
    ('HW 6', 'L6 Expected', [('Find the expected number of 6s in 300 rolls of a die.', '50'),
                             ('Find the expected number of heads in 70 coin tosses.', '35'),
                             ('A spinner is half red. Find the expected number of reds in 40 spins.', '20')]),
    ('HW 7', 'Before the test 1', [('<b>L1</b> How many outcomes are in the sample space for the day of the week?', '7'),
                                   ('<b>L2</b> A 10-sided die (1 to 10). Find P(an even number).', show(5, 10)),
                                   ('<b>L3</b> A die is rolled. Find P(not a 3).', show(5, 6))]),
    ('HW 8', 'Before the test 2', [('<b>L4</b> A drawer has 3 black socks and 1 white sock. Find P(white).', fr(Fr(1, 4))),
                                   ('<b>L5</b> 12 of 40 spins were blue. Find the observed P(blue).', show(12, 40)),
                                   ('<b>L6</b> P(E) = 0.3. Find the expected number in 50 trials.', '15')]),
    ('HW 9', 'Before the test 3', [('<b>L2</b> One card from a deck. Find P(an ace).', show(4, 52)),
                                   ('<b>L3</b> P(win) = 65%. Find P(not win).', '35%'),
                                   ('<b>L6</b> 60 rolls gave 25 sixes. Is the die biased?', 'Probably: 10 sixes were expected.')]),
]
m7_50 = sum(1 for x in range(1, 51) if x % 7 == 0)
m46_30 = [x for x in range(1, 31) if x % 4 == 0 or x % 6 == 0]
HW_EXT = [
    ('HW 1', 'L1 Chance', [('List the sample space for the number of heads when 3 coins are tossed.', '{0, 1, 2, 3}'),
                           ('Are those outcomes equally likely?', 'No'),
                           (f'Order from least to most likely: 0.3, {F(2, 5)}, 35%.', f'0.3, 35%, {fr(Fr(2, 5))}')]),
    ('HW 2', 'L2 P(E)', [('One card from a deck. Find P(a red picture card).', show(6, 52)),
                         (f'An Esky has 6 lemonade and 4 lime. How many colas must be added so that P(lemonade) = {F(1, 2)}?', '2'),
                         ('A spinner has a 90° red sector. Find P(red).', show(90, 360))]),
    ('HW 3', 'L3 Complements', [('P(not E) = 0.35. Find P(E).', '0.65'),
                                ('P(red) = 0.25, P(blue) = 0.4; the rest is green. Find P(green).', '0.35'),
                                ('A number from 1 to 50. Find P(not a multiple of 7).', show(50 - m7_50, 50))]),
    ('HW 4', 'L4 Problems', [('A number from 1 to 30. Find P(a multiple of 4 or 6).', show(len(m46_30), 30)),
                             ('P(left-handed) = 0.12 and 6 students are left-handed. How many students?', '50'),
                             ('Roll a die: Ann wins on a prime, Bo on any other number. Is it fair?', 'Yes: 3 outcomes each')]),
    ('HW 5', 'L5 Observed', [('250 tosses gave 140 heads. Find the observed P(heads).', show(140, 250, 'dec')),
                             ('After 30 spins, observed P(red) = 0.4. The next 10 are all red. Find the new observed P(red).', show(22, 40, 'dec')),
                             ('Why do two classes get different observed probabilities?', 'Chance: results vary from trial to trial.')]),
    ('HW 6', 'L6 Expected', [('The expected frequency is 90 in 360 trials. Find P(E).', show(90, 360)),
                             ('A die is rolled n times; the expected number of 6s is 42. Find n.', '252'),
                             ('Observed P = 0.15. Predict the number in 2000 trials.', '300')]),
    ('HW 7', 'E1 Venn', [('Venn: A only 9, both 4, B only 7, neither 5. Find P(A).', show(13, 25)),
                         ('Same diagram: find P(A or B).', show(20, 25)),
                         ('Same diagram: find P(exactly one of A, B).', show(16, 25))]),
    ('HW 8', 'E2 Tables', [('Table: A and B 6, A not B 9, B not A 5, neither 10. Find P(B).', show(11, 30)),
                           ('Same table: find P(A or B).', show(20, 30)),
                           ('Same table: find P(not A and not B).', show(10, 30))]),
    ('HW 9', 'Before the test', [('<b>L3</b> One tile from KINGSCLIFF. Find P(not a vowel).', show(8, 10)),
                                 ('<b>L6</b> Find the expected number of 4s in 150 rolls.', '25'),
                                 ('<b>E1</b> On a die, are ‘a multiple of 3’ and ‘a 5’ mutually exclusive?', 'Yes')]),
]
assert len(m46_30) == 10 and m7_50 == 7
