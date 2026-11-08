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
FACTS_EXT = FACTS_STD
_OLD_EXT_FACTS = [
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
    'L4': [('an ‘or’ problem', 'A number from 1 to 20 is chosen. Find P(a number less than 3 or greater than 17).',
            f'<p><b>Step 1</b> List: {{1, 2, 18, 19, 20}}.</p><p><b>Step 2</b> 5 of 20: P = {frs(5, 20)} = <b>{fr(Fr(1, 4))}</b></p>'),
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
    ('L2', 'A bag has 6 red, 4 blue and 2 white marbles. One is taken without looking. Find the probability of blue.', show(4, 12)),
    ('L2', 'A die is rolled. Find the probability of a number less than 5, as a percentage.', f'{show(4, 6)} = {pct_third(Fr(2, 3))} ≈ 66.7%'),
    ('L2', 'One card is taken from a standard deck. Find the probability of a black king.', show(2, 52)),
    ('L2', f'Write {F(7, 20)} as a decimal and as a percentage.', '0.35 and 35%'),
    ('L3', 'Write the complement of ‘Kingscliff wins the final’.', 'Kingscliff does not win (it loses or draws).'),
    ('L3', 'The probability that the bus is late is 0.12. Find the probability that it is not late.', '0.88'),
    ('L3', 'A spinner is red, blue or green. P(red) = 0.45 and P(blue) = 0.3. Find P(green).', '0.25'),
    ('L3', 'A family of 5 (2 parents, 3 children) take turns to wash up. Find P(the washer-up is not a parent).', fr(fam_np)),
    ('L4', 'One tile is picked from T, W, E, E, D. Find the probability of an E, as a decimal.', show(2, 5, 'dec')),
    ('L4', 'The digits 1, 3, 5 and 8 make a 4-digit number at random, each used once. Find P(the number is odd).', f'{fr(Fr(3, 4))} (it ends in 1, 3 or 5)'),
    ('L5', 'A coin is tossed 80 times and lands heads 36 times. Find the observed probability of heads, as a decimal.', show(36, 80, 'dec')),
    ('L5', 'Theoretical or observed? ‘P(a Year 8 student surfs) = 0.3, from a survey.’ Explain.', 'Observed: it comes from survey results.'),
    ('L6', 'A die is rolled 90 times. How many 5s would you expect?', '15'),
    ('L6', 'A basketballer scored 30 of 50 shots. Predict the number scored in 120 shots.', f'{fr(Fr(3, 5))} × 120 = 72'),
]
mult5_3dig = sum(1 for x in range(100, 1000) if x % 5 == 0)
m35_30 = [x for x in range(1, 31) if x % 3 == 0 or x % 5 == 0]
REVIEW_EXT = [
    ('L1', 'A die is rolled. Put these in order from least to most likely: A a 1, B an odd number, C a number less than 6.', 'A (1 outcome), B (3), C (5)'),
    ('L1', 'A spinner has 10 equal sectors: 5 red, 3 blue and 2 green. Write the chance word for landing on red, and for landing on green.', 'Red: even chance (5 of 10). Green: unlikely (2 of 10).'),
    ('L2', 'An Esky has 6 lemonade and 4 lime cans. How many colas must be added so that P(cola) = ' + F(1, 3) + '?', '5 (5 of 15)'),
    ('L2', 'One card is taken from a deck. Find the probability of a red number card (2 to 10).', f'9 hearts + 9 diamonds = 18: {show(18, 52)}'),
    ('L2', 'A whole number from 1 to 60 is chosen at random. Find the probability of a multiple of 12, as a decimal correct to 2 decimal places.', f'{{12, 24, 36, 48, 60}}: {show(5, 60)} ≈ 0.08'),
    ('L2', 'A spinner has sector angles 120° red, 150° blue and 90° green. Find P(blue).', show(150, 360)),
    ('L3', 'The probability that E does not happen is 0.62. Find P(E).', '0.38'),
    ('L3', 'A spinner is red, green or blue. P(red) = 2 × P(green) and P(blue) = 0.4. Find P(green).', '0.2'),
    ('L3', 'A bag has only red, blue and green marbles. P(red) = 0.35 and P(not blue) = 0.6. Find P(blue) and P(green).', 'P(blue) = 0.4; P(green) = 1 − 0.35 − 0.4 = 0.25'),
    ('L3', 'A 3-digit number (100 to 999) is chosen at random. Find P(not a multiple of 5).', f'{mult5_3dig} multiples of 5: {show(900 - mult5_3dig, 900)}'),
    ('L4', 'A whole number from 1 to 30 is chosen at random. Find the probability that it is not a multiple of 3.', f'10 multiples of 3: {show(20, 30)}'),
    ('L4', 'One letter is picked at random from the 11 letters of MISSISSIPPI. Find P(an S) and P(not an I).', f'P(S) = {show(4, 11)}; P(not I) = {show(7, 11)}'),
    ('L4', 'A die is weighted so P(6) = 0.4 and the other numbers are equally likely. Find P(2).', '0.6 ÷ 5 = 0.12'),
    ('L5', 'After 40 games, the observed P(win) = 0.6. The team then loses 10 games in a row. Find the new observed P(win).', f'24 of 50: {show(24, 50, "dec")}'),
    ('L5', 'A die is rolled 120 times: 1 (18), 2 (22), 3 (20), 4 (19), 5 (21), 6 (x). Find x and the observed P(6).', f'x = 20; {show(20, 120)}'),
    ('L5', 'A die is rolled 50 times and a 6 comes up 14 times. Find the observed probability of a 6, as a percentage. Is it close to the theoretical probability?', f'{show(14, 50, "pct")}; theoretical {fr(Fr(1, 6))} ≈ 16.7%, so it is not close (more rolls are needed, or the die may be biased).'),
    ('L6', 'The expected frequency of an event in 400 trials is 140. Find its probability.', show(140, 400)),
    ('L6', 'The observed probability that a car is white is 0.3. How many white cars would you expect among 450 cars?', '135'),
    ('L6', 'A spinner is spun 300 times and lands on blue 75 times. Use the observed probability to predict the number of blues in 1000 spins.', f'{frs(75, 300)} = {fr(Fr(1, 4))}; {fr(Fr(1, 4))} × 1000 = 250'),
    ('L6', 'A 4-sector spinner (equal sectors) gave 160 reds in 400 spins. Is it fair? Use the expected frequency.', 'Expected 100 reds; 160 is far more, so it is probably biased.'),
]
assert mult5_3dig == 180 and len(m35_30) == 14 and len([x for x in range(1, 61) if x % 12 == 0]) == 5 and 'MISSISSIPPI'.count('S') == 4 and 'MISSISSIPPI'.count('I') == 4

# ---------------------------------------------------------------- exit tickets: (easy, medium, hard) std ; (medium, hard, further) ext
TICKETS = {
    'L1': dict(std=[('A spinner has 3 equal sectors: red, blue, red. List the sample space.', '{red, blue}'),
                    ('On that spinner, are red and blue equally likely? Explain.', 'No: red has 2 of the 3 sectors.'),
                    ('A die is rolled. Write the chance word for rolling a number less than 3.', 'Unlikely (2 of 6 outcomes).')],
               ext=[('One tile is picked from B, A, N, A, N, A. List the sample space.', '{B, A, N}'),
                    ('Are those letters equally likely? Explain.', 'No: A is on 3 tiles, N on 2 and B on 1.'),
                    ('Design a spinner with 6 equal sectors where red is likely and blue is unlikely but possible.', 'e.g. 4 red, 1 blue, 1 yellow')]),
    'L2': dict(std=[('A die is rolled. Find the probability of a 4.', fr(Fr(1, 6))),
                    ('A bag has 3 red and 5 blue counters. Find the probability of blue, as a percentage.', show(5, 8, 'pct')),
                    ('One card is taken from a deck. Find the probability of a red ace.', show(2, 52))],
               ext=[('One card is taken from a deck. Find the probability of a picture card (J, Q or K).', show(12, 52)),
                    ('A 10-sided die (1 to 10) is rolled. Find the probability of a multiple of 4, as a decimal.', show(2, 10, 'dec')),
                    ('A bag has 4 red counters and some blue ones. P(red) = 0.2. How many blue counters are there?', '16')]),
    'L3': dict(std=[('Write the complement of ‘rolling an even number’.', 'rolling an odd number'),
                    ('The probability of winning is 0.35. Find the probability of not winning.', '0.65'),
                    ('A jar has 7 red, 5 green and 8 yellow lollies. One is taken. Find the probability it is not yellow.', show(12, 20))],
               ext=[('A die is rolled. Write the complement of ‘a number greater than 2’, then find its probability.', f'rolling a 1 or 2: {fr(Fr(1, 3))}'),
                    ('A spinner is red, blue or green. P(red) = 0.3 and P(blue) = 0.45. Find P(not green).', '0.75'),
                    ('The probability that E does not happen is four times P(E). Find P(E).', '0.2')]),
    'L4': dict(std=[('A spinner has 5 equal sectors numbered 1 to 5. Find the probability of an odd number, as a percentage.', '60%'),
                    ('Of 30 students, 12 catch the bus, 10 walk and the rest are driven. Find P(driven).', show(8, 30)),
                    ('A coin lands heads 5 times in a row. Find the probability of heads on the next toss. Explain.', f'{fr(Fr(1, 2))}: the coin has no memory.')],
               ext=[('A whole number from 1 to 100 is chosen at random. Find the probability of a square number.', show(10, 100)),
                    ('A whole number from 1 to 20 is chosen at random. Find the probability of a number less than 5 or greater than 16.', f'{{1, 2, 3, 4, 17, 18, 19, 20}}: {show(8, 20)}'),
                    ('A die is rolled: Amy wins on 1 or 2, Bo wins on 3 to 6. Is the game fair? Explain.', 'No: A has 2 outcomes, B has 4.')]),
    'L5': dict(std=[('A coin is tossed 40 times and lands heads 18 times. Find the observed probability of heads.', show(18, 40)),
                    ('Is ‘P(rolling a 6) = ⅙’ a theoretical or an observed probability?', 'Theoretical'),
                    ('After 12 rolls, the observed probability of a 6 is far from ⅙. Why might this happen?', 'Too few trials: chance has a big effect.')],
               ext=[('A coin is tossed 400 times and lands tails 150 times. Find the observed probability of tails, as a decimal.', show(150, 400, 'dec')),
                    ('After 20 shots, a player’s observed probability of a goal is 0.45. How many goals has the player scored?', '9'),
                    ('The player then scores with all of the next 5 shots. Find the new observed probability of a goal.', f'14 of 25: {show(14, 25, "dec")}')]),
    'L6': dict(std=[('A coin is tossed 60 times. How many heads would you expect?', '30'),
                    ('A die is rolled 120 times. How many 3s would you expect?', '20'),
                    ('Those 120 rolls actually gave 34 threes. Do you think the die is biased? Explain.', 'Probably: 34 is far more than the 20 expected.')],
               ext=[('A spinner is ¼ red. It is spun 200 times. How many reds would you expect?', '50'),
                    ('An event is expected 45 times in 180 trials. Find its probability.', show(45, 180)),
                    ('An event has an observed probability of 0.35. How many times would you expect it in 500 trials?', '175')]),
    'E1': dict(ext=[('A Venn diagram has A only 8, both 3, B only 5 and neither 4. Find P(A or B).', show(16, 20)),
                    ('Use the same Venn diagram. Find P(A or B, but not both).', show(13, 20)),
                    ('Of 40 students, 22 surf, 15 skate and 7 do neither. How many students do both?', '4')]),
    'E2': dict(ext=[('A two-way table: Year 7 has 12 like, 8 dislike; Year 8 has 15 like, 5 dislike. Find P(Year 7 and likes).', show(12, 40)),
                    ('Use the same table. Find P(Year 8 or dislikes).', show(15 + 5 + 8, 40)),
                    ('Draw a Venn diagram for that table, with one circle for Year 7 and one for likes.', 'Year 7 only 8, both 12, likes only 15, neither 5')]),
}

# ---------------------------------------------------------------- homework strips
HW_STD = [
    ('HW 1', 'L1 Chance', [('A coin is tossed. List the sample space.', '{heads, tails}'),
                           ('An event has a probability of 0.8. Write its chance word.', 'likely'),
                           ('A fair die is rolled. Are the outcomes 1 to 6 equally likely?', 'Yes')]),
    ('HW 2', 'L2 P(E)', [('A die is rolled. Find the probability of a number greater than 2.', show(4, 6)),
                         ('A bag has 2 red and 6 blue counters. Find the probability of red, as a decimal.', show(2, 8, 'dec')),
                         ('One card is taken from a deck. Find the probability of a spade.', show(13, 52))]),
    ('HW 3', 'L3 Complements', [('The probability of rain is 0.4. Find the probability of no rain.', '0.6'),
                                ('Write the complement of ‘winning a raffle’.', 'not winning the raffle'),
                                ('One tile is picked from N, I, P, P, E, R, S. Find the probability that it is not a vowel.', show(5, 7))]),
    ('HW 4', 'L4 Problems', [('A whole number from 1 to 10 is chosen at random. Find the probability of a prime number.', show(4, 10)),
                             ('One tile is picked from T, W, E, E, D. Find the probability that it is not an E.', show(3, 5)),
                             ('A bag of 20 lollies has P(red) = 0.5. How many lollies are red?', '10')]),
    ('HW 5', 'L5 Observed', [('A coin is tossed 50 times and lands heads 27 times. Find the observed probability of heads.', fr(Fr(27, 50))),
                             ('Is ‘P(heads) = ½’ a theoretical or an observed probability?', 'Theoretical'),
                             ('Why is it better to do many trials?', 'The observed probability gets closer to the true one.')]),
    ('HW 6', 'L6 Expected', [('A die is rolled 300 times. How many 6s would you expect?', '50'),
                             ('A coin is tossed 70 times. How many heads would you expect?', '35'),
                             ('A spinner is half red. It is spun 40 times. How many reds would you expect?', '20')]),
    ('HW 7', 'Before the test 1', [('<b>L1</b> How many outcomes are in the sample space for the day of the week?', '7'),
                                   ('<b>L2</b> A 10-sided die (1 to 10) is rolled. Find the probability of an even number.', show(5, 10)),
                                   ('<b>L3</b> A die is rolled. Find the probability of not rolling a 3.', show(5, 6))]),
    ('HW 8', 'Before the test 2', [('<b>L4</b> A drawer has 3 black socks and 1 white sock. One sock is taken. Find P(white).', fr(Fr(1, 4))),
                                   ('<b>L5</b> A spinner landed on blue in 12 of 40 spins. Find the observed probability of blue.', show(12, 40)),
                                   ('<b>L6</b> P(E) = 0.3. How many times would you expect E in 50 trials?', '15')]),
    ('HW 9', 'Before the test 3', [('<b>L2</b> One card is taken from a deck. Find the probability of an ace.', show(4, 52)),
                                   ('<b>L3</b> The probability of winning is 65%. Find the probability of not winning.', '35%'),
                                   ('<b>L6</b> A die rolled 60 times gave 25 sixes. Do you think it is biased? Explain.', 'Probably: 10 sixes were expected.')]),
]
m7_50 = sum(1 for x in range(1, 51) if x % 7 == 0)
m46_30 = [x for x in range(1, 31) if x % 4 == 0 or x % 6 == 0]
HW_EXT = [
    ('HW 1', 'L1 Chance', [('A spinner has 8 equal sectors: 3 red, 3 blue and 2 green. List the sample space.', '{red, blue, green}'),
                           ('Are those colours equally likely? Explain.', 'No: green has only 2 sectors.'),
                           (f'Put these probabilities in order from least to most likely: 0.3, {F(2, 5)}, 35%.', f'0.3, 35%, {fr(Fr(2, 5))}')]),
    ('HW 2', 'L2 P(E)', [('One card is taken from a deck. Find the probability of a red picture card.', show(6, 52)),
                         (f'An Esky has 6 lemonade and 4 lime cans. How many cola cans must be added so that P(lemonade) = {F(1, 2)}?', '2'),
                         ('A spinner has a red sector with an angle of 90°. Find the probability of red.', show(90, 360))]),
    ('HW 3', 'L3 Complements', [('The probability that E does not happen is 0.35. Find P(E).', '0.65'),
                                ('A spinner is red, blue or green. P(red) = 0.25 and P(blue) = 0.4. Find P(green).', '0.35'),
                                ('A whole number from 1 to 50 is chosen at random. Find the probability that it is not a multiple of 7.', show(50 - m7_50, 50))]),
    ('HW 4', 'L4 Problems', [('A whole number from 1 to 30 is chosen at random. Find the probability of a multiple of 4.', f'{{4, 8, …, 28}}: {show(7, 30)}'),
                             ('In a group, P(left-handed) = 0.12 and 6 students are left-handed. How many students are in the group?', '50'),
                             ('A die is rolled: Ann wins on a prime number, Bo on any other number. Is the game fair? Explain.', 'Yes: 3 outcomes each')]),
    ('HW 5', 'L5 Observed', [('A coin is tossed 250 times and lands heads 140 times. Find the observed probability of heads.', show(140, 250, 'dec')),
                             ('After 30 spins, the observed probability of red is 0.4. The next 10 spins are all red. Find the new observed probability of red.', show(22, 40, 'dec')),
                             ('Why do two classes get different observed probabilities?', 'Chance: results vary from trial to trial.')]),
    ('HW 6', 'L6 Expected', [('An event E is expected 90 times in 360 trials. Find P(E).', show(90, 360)),
                             ('A die is rolled n times. The expected number of 6s is 42. Find n.', '252'),
                             ('An event has an observed probability of 0.15. How many times would you expect it in 2000 trials?', '300')]),
    ('HW 7', 'Before the test 1', [('<b>L1</b> A bag has 4 red, 4 blue and 2 green counters. Are the three colours equally likely? Explain.', 'No: green has only 2 counters.'),
                                   ('<b>L2</b> A spinner has sector angles 180° red, 120° blue and 60° green. Find P(green).', show(60, 360)),
                                   ('<b>L3</b> The probability of rain is 0.27. Find the probability of no rain, as a percentage.', '73%')]),
    ('HW 8', 'Before the test 2', [('<b>L4</b> A whole number from 1 to 40 is chosen at random. Find the probability of a square number.', f'{{1, 4, 9, 16, 25, 36}}: {show(6, 40)}'),
                                   ('<b>L5</b> A spinner landed on red 27 times in 60 spins. Find the observed probability of red, as a decimal.', show(27, 60, 'dec')),
                                   ('<b>L6</b> A die is rolled 240 times. How many numbers greater than 4 would you expect?', f'{fr(Fr(1, 3))} × 240 = 80')]),
    ('HW 9', 'Before the test 3', [('<b>L3</b> One tile is picked from KINGSCLIFF. Find the probability that it is not a vowel.', show(8, 10)),
                                   ('<b>L5</b> A coin lands heads 33 times in 60 tosses. Find the observed probability of heads, as a decimal.', show(33, 60, 'dec')),
                                   ('<b>L6</b> A die is rolled 150 times. How many 4s would you expect?', '25')]),
]
assert len(m46_30) == 10 and m7_50 == 7
