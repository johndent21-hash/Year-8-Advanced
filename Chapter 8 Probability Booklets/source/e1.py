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
    if form == 'pct':
        return base + f' = {pct(p, dp)}'
    return base


def regions(total, a, b, both):
    """Return (A only, both, B only, neither) from totals."""
    return a - both, both, b - both, total - (a + b - both)


NOTES = f'''<div class="tnotes" style="grid-template-columns:1.12fr .95fr 1fr">
<div><h4>KEY TERMS</h4>
<p><b>Venn diagram:</b> a rectangle (everyone) with a circle for each group</p>
<p><b>A and B:</b> in both groups: the overlap</p>
<p><b>A or B</b> (inclusive or): in A, in B, or in both</p>
<p><b>A or B but not both</b> (exclusive or): A only or B only</p>
<p><b>neither:</b> outside both circles</p>
<p><b>mutually exclusive:</b> cannot happen together, so the circles do not overlap</p></div>
<div><h4>DIAGRAM</h4>
{venn('12', '6', '9', '3', 'Computer', 'Sport', 33, total='30')}
<p style="margin-top:.6mm">12 computer only, 6 both, 9 sport only, 3 neither</p></div>
<div><h4>STEPS</h4>
<p><span class="step">1</span>start with the overlap (both)</p>
<p><span class="step">2</span>A only = A total − both</p>
<p><span class="step">3</span>B only = B total − both</p>
<p><span class="step">4</span>neither = total − the other three</p>
<p><span class="step">5</span>P = number in the region(s) ÷ total</p>
<p>30 students: 18 computer, 15 sport, 6 both</p></div>
</div>'''

MS = (21, 9, 12, 8)
CS = regions(30, 18, 15, 6)
NQ = regions(130, 44, 66, 20)
assert CS == (12, 6, 9, 3) and NQ == (24, 20, 46, 40)

EX1 = dict(
    instr='Read and draw Venn diagrams. Start with the overlap.',
    parts=[
        ('Read', venn(*map(str, MS), 'Maths', 'Science', 27), 'How many students were surveyed? How many like both subjects?'),
        ('Or', '', 'Same diagram. How many like Maths or Science? How many like Maths or Science, but not both?'),
        ('Mutually exclusive', venn('21', '', '19', '6', 'Netball', 'Hockey', 27, mutually_exclusive=True), 'Are netball and hockey mutually exclusive? How many play netball or hockey?'),
        ('Draw', venn('', '', '', '', 'Computer', 'Sport', 27), '30 students: 18 play computer games, 15 play sport, 6 do both. Complete the diagram.'),
    ], box=17,
    ans=[f'{sum(MS)} students; {MS[1]} like both', f'{MS[0] + MS[1] + MS[2]}; not both {MS[0] + MS[2]}', 'Yes (the circles do not overlap); 40',
         f'computer only {CS[0]}, both {CS[1]}, sport only {CS[2]}, neither {CS[3]}'],
    worked=[
        f'<p>Add all four regions:</p><p>21 + 9 + 12 + 8 = <b>{sum(MS)}</b> students</p><p>Both = the overlap = <b>9</b></p>',
        f'<p>Or = everything inside the circles:</p><p>21 + 9 + 12 = <b>42</b></p><p>Not both = only the outer parts: 21 + 12 = <b>33</b></p>',
        '<p>The circles do not overlap: no-one plays both, so <b>yes</b>, they are mutually exclusive.</p><p>Netball or hockey: 21 + 19 = <b>40</b></p>',
        '<p>Overlap: <b>6</b>. Computer only: 18 − 6 = <b>12</b>. Sport only: 15 − 6 = <b>9</b>. Neither: 30 − 27 = <b>3</b>.</p>',
    ])

EX2 = dict(
    instr='Find probabilities from Venn diagrams: the total of everyone goes on the bottom.',
    parts=[
        ('And / not', '', 'Use Example 1d. Find P(plays sport but not computer games).'),
        ('Exclusive or', '', 'Use Example 1d. Find P(plays sport or computer games, but not both).'),
        ('Draw', venn('', '', '', '', 'NSW', 'Qld', 27), '130 people: 44 like NSW holidays, 66 like Queensland, 20 like both. Complete the diagram.'),
        ('Probability', '', 'Use part c. Find P(likes NSW only) and P(likes neither).'),
    ], box=17,
    ans=[show(CS[2], 30), show(CS[0] + CS[2], 30), f'NSW only {NQ[0]}, both {NQ[1]}, Qld only {NQ[2]}, neither {NQ[3]}',
         f'{show(NQ[0], 130)}; {show(NQ[3], 130)}'],
    worked=[
        f'<p>Sport but not computer = sport only = 9.</p><p>P = {show(9, 30)}</p>',
        f'<p>Not both = computer only + sport only = 12 + 9 = 21.</p><p>P = {show(21, 30)}</p>',
        '<p>Overlap <b>20</b>. NSW only 44 − 20 = <b>24</b>. Qld only 66 − 20 = <b>46</b>. Neither 130 − 90 = <b>40</b>.</p>',
        f'<p>P(NSW only) = {show(24, 130)}</p><p>P(neither) = {show(40, 130)}</p>',
    ])

# ---------------------------------------------------------------- extension questions
IC = (120, 57, 248, 15)
NIC = sum(IC)
SL = (38, 4, 10, 48)
NSL = sum(SL)
MB = regions(30, 20, 13, 4)
assert NSL == 100 and MB == (16, 4, 9, 1) and 20 + 13 - 4 + 1 == 30

p1 = [
    R('use this Venn diagram of an ice-cream survey.', 2, [
        Q('How many people were surveyed?', '', str(NIC)),
        Q('How many liked strawberry or chocolate, but not both?', '', str(IC[0] + IC[2])),
        Q('How many liked neither flavour?', '', str(IC[3])),
        Q('Find P(a person likes both flavours).', '', show(IC[1], NIC)),
    ], h=20, ln=LN_A2, info=venn(*map(str, IC), 'Strawberry', 'Chocolate', 44) + '<span class="cap">Each number is a count of people.</span>', side=50),
    R('are the two events mutually exclusive or overlapping? Explain.', 4, [
        Q('‘surfs’ and ‘is left-handed’', '', 'Overlapping: a surfer can be left-handed.'),
        Q('‘born in Australia’ and ‘born in Japan’', '', 'Mutually exclusive: you are born in only one country.'),
        Q('Die: ‘an even number’ and ‘a 3’', '', 'Mutually exclusive: 3 is not even.'),
        Q('Die: ‘an even number’ and ‘greater than 3’', '', 'Overlapping: 4 and 6 are in both.'),
    ], h=24, ln=[('ME / overlap', ''), ('Reason', '')]),
]
eyes = dict(blue=32, brown=38, neither=10)
p2 = [
    R('this Venn diagram shows the sports some students play.', 3, [
        Q('How many students are in the diagram?', '', str(21 + 19 + 6)),
        Q('How many play netball or hockey?', '', str(21 + 19)),
        Q('How many play netball and hockey?', '', '0 (mutually exclusive)'),
    ], h=19, ln=LN_A, info=venn('21', '', '19', '6', 'Netball', 'Hockey', 40, mutually_exclusive=True), side=46),
    R('one person from this diagram is chosen at random. Give each probability as a decimal.', 3, [
        Q('Find P(surfs).', '', show(SL[0] + SL[1], NSL, 'dec')),
        Q('Find P(surfs or is left-handed).', '', show(SL[0] + SL[1] + SL[2], NSL, 'dec')),
        Q('Find P(left-handed and does not surf).', '', show(SL[2], NSL, 'dec')),
    ], h=19, ln=LN_A2, info=venn(*map(str, SL), 'Surfs', 'Left-handed', 40), side=46),
    R('30 customers: 20 bought milk, 13 bought bread and 1 bought neither. Draw a Venn diagram first.', 3, [
        Q('How many bought both milk and bread?', venn('', '', '', '', 'Milk', 'Bread', 26), f'20 + 13 + 1 − 30 = {MB[1]}'),
        Q('How many bought milk only?', '', str(MB[0])),
        Q('Find P(bread only).', '', show(MB[2], 30)),
    ], h=28, ln=LN_A2),
    R('a group has 32 students with blue eyes, 38 with brown eyes and 10 with neither.', 3, [
        Q('Are ‘blue eyes’ and ‘brown eyes’ mutually exclusive here? Why?', '', 'Yes: no-one has both blue and brown eyes.'),
        Q('How many students are in the group?', '', str(sum(eyes.values()))),
        Q('Find P(not brown eyes), as a percentage.', '', show(32 + 10, 80, 'pct')),
    ], h=22, ln=LN_A2),
]
ITC = regions(30, 20, 30 - 20 + 7, 7)
CAMP_BOTH = 35 + 20 - 40
MED = (22, 28, 16, 7)
NMED = sum(MED)
x_val = (39 - 9) // 3
p3 = [
    Q('All 30 students in a class study IT or Chemistry (or both). 7 study both and 20 study IT. How many study Chemistry? Find P(Chemistry).', '',
      f'IT only 13, so Chemistry only 30 − 20 = 10; Chemistry = 17: {show(17, 30)}'),
    Q('40 students at camp: 35 chose kayaking, 20 chose bushwalking, and everyone chose at least one. How many chose both? Find P(both) and P(not bushwalking).', '',
      f'{CAMP_BOTH} both; {show(CAMP_BOTH, 40)}; {show(20, 40)}'),
    Q('The diagram shows children who have had measles or mumps. Find P(measles), P(measles or mumps) and P(neither).', venn(*map(str, MED), 'Measles', 'Mumps', 28),
      f'{fr(Fr(MED[0] + MED[1], NMED))}, {fr(Fr(MED[0] + MED[1] + MED[2], NMED))}, {fr(Fr(MED[3], NMED))} (total {NMED})'),
    Q('P(A) = 0.6, P(B) = 0.5 and P(A and B) = 0.3. Draw a Venn diagram for 100 people and find P(A or B).', '',
      'A only 30, both 30, B only 20, neither 20: P(A or B) = 0.8'),
    Q('A Venn diagram has A only = x, both = 5, B only = 2x and neither = 4. The total is 39. Find x and P(A).', '',
      f'3x + 9 = 39, x = {x_val}; P(A) = {show(x_val + 5, 39)}'),
    Q('Can A and B be mutually exclusive if P(A) = 0.7 and P(B) = 0.5? Explain.', '', 'No: then P(A or B) = 1.2, which is more than 1.'),
]
assert x_val == 10 and CAMP_BOTH == 15
DC = regions(120, 70, 45, 70 + 45 - (120 - 25))
NB = regions(48, 30, 26, 30 + 26 - (48 - 5))
evens = {x for x in range(1, 21) if x % 2 == 0}
m3 = {x for x in range(1, 21) if x % 3 == 0}
assert DC == (50, 20, 25, 25) and NB == (17, 13, 13, 5)
word = [
    Q('120 Year 8 students: 70 have a dog, 45 have a cat and 25 have neither. Draw a Venn diagram. Find P(dog and cat) and P(exactly one of the two).', '',
      f'both {DC[1]}: {show(DC[1], 120)}; exactly one {DC[0] + DC[2]}: {show(DC[0] + DC[2], 120)}'),
    Q('Kingscliff Nippers has 48 members: 30 swim, 26 do board and 5 do neither. Find P(swims but does not do board).', '',
      f'both = 30 + 26 − 43 = {NB[1]}; swim only {NB[0]}: {show(NB[0], 48)}'),
    Q('A number from 1 to 20 is chosen. A = even, B = a multiple of 3. Put the numbers in a Venn diagram. Find P(A or B) and P(A or B but not both).', '',
      f'{show(len(evens | m3), 20)}; {show(len(evens ^ m3), 20)}'),
]

EXT = dict(
    rem1='A and B: the overlap · A or B: inside either circle · not both: the two outer parts only · neither: outside the circles · Venn diagrams are not drawn to scale',
    p1=p1,
    rem2='start with the overlap · A only = A − both · neither = total − (A only + both + B only) · P = region ÷ total',
    p2=p2,
    rem3='P(A or B) = P(A) + P(B) − P(A and B), or draw the diagram and add the regions',
    p3=p3, word=word,
)

LESSON = dict(key='E1', num='E1', title='Venn diagrams', sub=SUB, ext_only=True,
              li='read and draw Venn diagrams, and use them to find probabilities with ‘and’, ‘or’ and ‘not’.',
              sc=['read the four regions of a two-circle Venn diagram.',
                  'draw a Venn diagram, starting with the overlap.',
                  'tell inclusive ‘or’ from exclusive ‘or’ and find probabilities.'],
              notes=NOTES, notes_h=38, ex1=EX1, ex2=EX2, ext=EXT)
