from engine import Q, R, LN_W, LN_A, LN_A2
from gfx import *
from pm import *
from layout import F

SUB = 'Extension • Stage 5 Path • MA5-PRO-P-01'


def show(fav, tot, form='frac', dp=None):
    p = Fr(fav, tot)
    base = frs(fav, tot) + (f' = {fr(p)}' if p.denominator != tot else '')
    if form == 'dec':
        return base + f' = {dec(p, dp)}'
    return base


def ttab(cols, rows, size=8.2, blank=''):
    """Two-way table. cols: column headings (without the corner); rows: list of (heading, [cells])."""
    h = f'<table class="t" style="font-size:{size}pt"><tr><th></th>' + ''.join(f'<th>{c}</th>' for c in cols) + '</tr>'
    for head, cells in rows:
        h += f'<tr><th>{head}</th>' + ''.join(
            (f'<td>{c}</td>' if c != '' else '<td class="blank"></td>') for c in cells) + '</tr>'
    return h + '</table>'


def complete(grid):
    """grid: 3x3 list with None for unknowns (last row/col are totals). Solve by repeated subtraction."""
    g = [row[:] for row in grid]
    for _ in range(10):
        for i in range(3):
            r = g[i]
            if r.count(None) == 1:
                k = r.index(None)
                r[k] = r[2] - r[1 - k] if k < 2 else r[0] + r[1]
        for j in range(3):
            c = [g[i][j] for i in range(3)]
            if c.count(None) == 1:
                k = c.index(None)
                g[k][j] = c[2] - c[1 - k] if k < 2 else c[0] + c[1]
    assert all(None not in r for r in g), g
    for i in range(3):
        assert g[i][0] + g[i][1] == g[i][2]
    for j in range(3):
        assert g[0][j] + g[1][j] == g[2][j]
    return g


def show_grid(grid):
    return [['' if v is None else v for v in r] for r in grid]


NOTES = f'''<div class="tnotes" style="grid-template-columns:1.05fr 1.05fr 1fr">
<div><h4>KEY TERMS</h4>
<p><b>two-way table:</b> rows for one attribute, columns for another</p>
<p>each <b>cell</b> is an ‘and’, e.g. Year 7 <i>and</i> can swim</p>
<p><b>totals:</b> row totals, column totals and the <b>grand total</b> (bottom right)</p>
<p>missing cell = total − the known cells</p></div>
<div><h4>VENN DIAGRAM ↔ TABLE</h4>
{ttab(['B', 'not B', 'Total'], [('A', ['both', 'A only', 'A total']), ('not A', ['B only', 'neither', '']), ('Total', ['B total', '', 'grand'])], 7.4)}
<p style="margin-top:.6mm">overlap → ‘A and B’ cell; outside both circles → ‘not A and not B’ cell</p></div>
<div><h4>STEPS</h4>
<p><span class="step">1</span>fill in every total you can</p>
<p><span class="step">2</span>find missing cells by subtracting</p>
<p><span class="step">3</span>check: rows and columns add up</p>
<p><span class="step">4</span>P = cell(s) ÷ grand total</p>
<p>‘or’: add the cells, but count each cell once</p></div>
</div>'''

SWIM = [[13, 2], [9, 3]]
NSW_ = sum(map(sum, SWIM))
CIN = complete([[None, 142, 198], [45, None, None], [None, None, 344]])
assert CIN == [[56, 142, 198], [45, 101, 146], [101, 243, 344]]
ART = (21, 9, 12, 8)  # Chinese only, both, Art only, neither
ART_T = [[ART[1], ART[2], ART[1] + ART[2]], [ART[0], ART[3], ART[0] + ART[3]], [ART[0] + ART[1], ART[2] + ART[3], sum(ART)]]

EX1 = dict(
    instr='The table shows which students can swim. Each cell is an ‘and’, e.g. Year 7 and can swim.',
    data=ttab(['Can swim', 'Cannot swim'], [('Year 7', SWIM[0]), ('Year 8', SWIM[1])], 8.6),
    parts=[
        ('Total', '', 'How many students are in the table?'),
        ('Or', '', 'How many are in Year 7 or cannot swim (or both)?'),
        ('And', '', 'How many are in Year 7 and cannot swim?'),
        ('Probability', '', 'One student is picked at random. Find P(Year 8 and can swim).'),
    ], box=19,
    ans=[str(NSW_), str(13 + 2 + 3), '2', show(9, NSW_)],
    worked=[
        f'<p>Add every cell:</p><p>13 + 2 + 9 + 3 = <b>{NSW_}</b></p>',
        '<p>All of Year 7 (13 + 2) plus Year 8 students who cannot swim (3):</p><p>15 + 3 = <b>18</b></p><p>Don’t count the 2 twice.</p>',
        '<p>The cell in the Year 7 row and the Cannot swim column: <b>2</b></p>',
        f'<p>Year 8 and can swim: 9 of 27.</p><p>P = {show(9, NSW_)}</p>',
    ])

EX2 = dict(
    instr='Complete the cinema table, use it to find probabilities, then turn the Venn diagram into a table.',
    data=ttab(['Under 18', '18 and over', 'Total'], [('Saturday', ['', 142, 198]), ('Sunday', [45, '', '']), ('Total', ['', '', 344])], 8.4)
         + '<span class="sans" style="font-size:7.4pt;color:#555;max-width:40mm">A cinema’s audience on two days</span>'
         + venn('21', '9', '12', '8', 'Chinese', 'Art', 28),
    parts=[
        ('Complete', '', 'Fill in the empty cells. Each row and column must add to its total.'),
        ('And', '', 'One person is picked at random. Find P(Sunday and 18 or over).'),
        ('Or', '', 'Find P(Sunday or 18 or over), counting each person once.'),
        ('Convert', '', 'Show the Venn diagram (50 students) as a two-way table: Art / not Art down the side.'),
    ], box=14,
    ans=[f'Saturday: {CIN[0][0]}, 142, 198. Sunday: 45, {CIN[1][1]}, {CIN[1][2]}. Total: {CIN[2][0]}, {CIN[2][1]}, 344.',
         show(CIN[1][1], 344), show(45 + CIN[1][1] + 142, 344),
         f'Art: 9, 12, 21. not Art: 21, 8, 29. Total: 30, 20, 50.'],
    worked=[
        '<p>198 − 142 = <b>56</b>; 344 − 198 = <b>146</b> (Sunday)</p><p>146 − 45 = <b>101</b></p><p>56 + 45 = <b>101</b>; 142 + 101 = <b>243</b></p>',
        f'<p>Sunday and 18+: 101 of 344.</p><p>P = {show(CIN[1][1], 344)}</p>',
        f'<p>All of Sunday (146) plus Saturday 18+ (142): 288.</p><p>P = {show(288, 344)}</p>',
        ttab(['Ch', 'not', 'Tot'], [('Art', [9, 12, 21]), ('not', [21, 8, 29]), ('Tot', [30, 20, 50])], 6.8),
    ])

# ---------------------------------------------------------------- extension questions
SOC = [[64, 96], [144, 32]]
NSOC = sum(map(sum, SOC))
GL = complete([[22, None, 82], [None, 85, 98], [None, 145, None]])
assert GL == [[22, 60, 82], [13, 85, 98], [35, 145, 180]]
p1 = [
    R('the players in a soccer club are grouped by age and weight. Use the table.', 2, [
        Q('How many players does the club have?', '', str(NSOC)),
        Q('How many players are juniors or light (or both)?', '', str(64 + 96 + 32)),
        Q('How many players are juniors or light, but not both?', '', str(64 + 32)),
        Q('One player is picked at random. Find the probability that they are a senior.', '', show(144 + 32, NSOC)),
    ], h=16, ln=LN_A, info=ttab(['Heavy', 'Light'], [('Junior', SOC[0]), ('Senior', SOC[1])], 8.4), side=44),
    R('the table shows which students need glasses. Fill in the empty cells first, then answer.', 2, [
        Q('How many Year 9 students do not need glasses?', '', str(GL[0][1])),
        Q('How many Year 10 students need glasses?', '', str(GL[1][0])),
        Q('How many students are there in total?', '', str(GL[2][2])),
        Q('One student is picked at random. Find the probability that they need glasses.', '', show(GL[2][0], GL[2][2])),
    ], h=16, ln=LN_A, info=ttab(['Needs<br>glasses', 'Does<br>not', 'Total'], [('Year 9', [22, '', 82]), ('Year 10', ['', 85, 98]), ('Total', ['', 145, ''])], 7.8), side=56),
]
BR = complete([[60, None, 150], [None, 40, None], [130, None, None]])
SB = (34, 11, 20, 5)  # swim only, both, bowl only, neither
TV = (15, 28, 20, 7)  # soccer only, both, cricket only, neither
HJ = complete([[128, None, 360], [100, 40, None], [None, None, None]])
assert BR == [[60, 90, 150], [70, 40, 110], [130, 130, 260]] and HJ[2][2] == 500
p2 = [
    R('the table shows who likes broccoli. Fill in the empty cells first, then answer.', 3, [
        Q('How many students dislike broccoli?', '', str(BR[2][1])),
        Q('One student is picked at random. Find the probability that they are in Year 7 or dislike broccoli.', '', show(BR[0][2] + BR[1][1], BR[2][2])),
        Q('Find the probability that the student is in Year 8 and likes broccoli.', '', show(BR[1][0], BR[2][2])),
    ], h=20, ln=LN_A2, info=ttab(['Likes', 'Dislikes', 'Total'], [('Year 7', [60, '', 150]), ('Year 8', ['', 40, '']), ('Total', [130, '', ''])], 7.8), side=56),
    R('turn the Venn diagram into a two-way table, then answer.', 3, [
        Q('Fill in the table from the Venn diagram (S = swims, B = bowls).', ttab(['S', 'not S', 'Tot'], [('B', ['', '', '']), ('not B', ['', '', '']), ('Tot', ['', '', ''])], 6.6).replace('class="blank"', 'class="blank" style="min-width:6mm"'),
          'S = swims, B = bowls. B: 11, 20, 31. not B: 34, 5, 39. Total: 45, 25, 70.', ln=[]),
        Q('One person is picked at random. Find the probability that they swim.', '', show(SB[0] + SB[1], sum(SB))),
        Q('Find the probability that the person bowls but does not swim.', '', show(SB[2], sum(SB))),
    ], h=30, ln=LN_A2, info=venn(*map(str, SB), 'Swimming', 'Bowling', 40), side=46),
    R('turn the two-way table into a Venn diagram, then answer.', 3, [
        Q('Write the four numbers from the table in the Venn diagram.', venn('', '', '', '', 'Soccer', 'Cricket', 30), f'soccer only {TV[0]}, both {TV[1]}, cricket only {TV[2]}, neither {TV[3]}', ln=[]),
        Q('One person is picked at random. Find the probability that they watch soccer or cricket, but not both.', '', show(TV[0] + TV[2], sum(TV))),
        Q('Find the probability that the person does not watch cricket.', '', show(TV[0] + TV[3], sum(TV))),
    ], h=28, ln=LN_A2, info=ttab(['Cricket', 'Not<br>cricket'], [('Soccer', [TV[1], TV[0]]), ('Not<br>soccer', [TV[2], TV[3]])], 7.8)
      + '<span class="cap">TV sports watched by 70 people</span>', side=46),
    R('a sports high school surveyed students about hockey and judo. Fill in the table first, then answer.', 3, [
        Q('One student is picked at random. Find the probability that they do judo.', '', show(HJ[2][0], 500)),
        Q('Find the probability that the student does judo but not hockey.', '', show(HJ[1][0], 500)),
        Q('Find the probability that the student does hockey or judo, but not both.', '', show(HJ[0][1] + HJ[1][0], 500)),
    ], h=20, ln=LN_A2, info=ttab(['Judo', 'Not<br>judo', 'Total'], [('Hockey', [128, '', 360]), ('Not<br>hockey', [100, 40, '']), ('Total', ['', '', ''])], 7.8), side=56),
]
RM = (42, 25, 3, 12)  # 4-doors only, both, GPS only, neither
NRM = sum(RM)
NEI = 80 - (30 + 45 - 12)
WALK = complete([[9, None, 18], [4, None, 12], [None, None, 30]])
CAN = complete([[50, 40, 90], [70, None, 110], [120, None, 200]])
assert CAN == [[50, 40, 90], [70, 40, 110], [120, 80, 200]]
p3 = [
    Q('The Venn diagram shows the cars at Rusty Motors. Draw it as a two-way table. Then find the probability that a car picked at random has GPS.', venn(*map(str, RM), '4 doors', 'GPS', 27),
      f'4-door: 25, 42, 67. Not: 3, 12, 15. Total: 28, 54, 82. P(GPS) = {show(RM[1] + RM[2], NRM)}'),
    Q('Use your table from Question 1. Find P(4 doors and GPS) and P(no GPS).', '', f'{show(RM[1], NRM)}; {show(RM[0] + RM[3], NRM)}'),
    Q('A two-way table has a grand total of 80. The A total is 30, the B total is 45 and the ‘A and B’ cell is 12. Find the ‘not A and not B’ cell.', '',
      f'80 − (30 + 45 − 12) = {NEI}'),
    Q('8K has 30 students: 18 walk to school, and 9 of the walkers are in the band. 4 students who don’t walk are in the band. Make a two-way table. Find the probability that a student picked at random is in the band.', '',
      f'band: walk 9, not walk 4, total 13: {show(13, 30)}'),
    Q('In Year 8, 40% surf, 25% skate and 10% do both. Find the probability that a student does neither, as a percentage.', '', '100% − (40% + 25% − 10%) = 45%'),
    Q('P(A) = 0.5, P(B) = 0.4 and P(A and B) = 0.2. Make a two-way table of probabilities (the grand total is 1) and find P(neither).', '',
      'A only 0.3, B only 0.2, neither 1 − 0.7 = 0.3'),
]
assert NEI == 17
word = [
    Q('The canteen had 200 orders: 120 included a drink, 90 were hot food, and 50 were hot food with a drink. Make a two-way table. Find the probability that an order was hot food or included a drink, but not both.', '',
      f'hot+drink 50, hot only 40, drink only 70, neither 40: {show(40 + 70, 200)}'),
    Q('Of 150 Tweed residents, 40 own a boat, 55 live on the river and 18 do both. Find P(owns a boat but does not live on the river) and P(neither).', '',
      f'{show(40 - 18, 150)}; neither {150 - (40 + 55 - 18)}: {show(150 - 77, 150)}'),
    Q('Explain why a two-way table can show Years 7, 8 and 9 (down the side) more easily than a Venn diagram.', '',
      'Each year is just another row; a Venn diagram would need a circle for every group and gets crowded.'),
]

EXT = dict(
    rem1='Each cell is an ‘and’. For ‘or’, add the cells, counting each cell once. Probability = cell ÷ grand total.',
    p1=p1,
    rem2='Missing cell = total − the known cells. The Venn overlap goes in the ‘A and B’ cell; outside both circles goes in the ‘not A and not B’ cell.',
    p2=p2,
    p3h=33,
    rem3='Draw the table or the diagram first. Every row and column must add to its total.',
    p3=p3, word=word,
)

LESSON = dict(key='E2', num='E2', title='Two-way tables', sub=SUB, ext_only=True, alt=True,
              li='read, complete and draw two-way tables, convert between Venn diagrams and two-way tables, and find probabilities.',
              sc=['complete a two-way table using the totals.',
                  'convert between a Venn diagram and a two-way table.',
                  'find probabilities with ‘and’, ‘or’ and ‘not’ from a table.'],
              notes=NOTES, notes_h=37, ex1=EX1, ex2=EX2, ext=EXT)
