"""Assemble the five booklets.

python3 build.py            -> writes out/*.html
"""
import sys, re, os
sys.path.insert(0, '.')
from layout import *
from engine import lesson_pages, answer_block
import l1, l2, l3, l4, l5, l6
import back
from pm import fr, Fr

STD_L = [l1.LESSON, l2.LESSON, l3.LESSON, l4.LESSON, l5.LESSON, l6.LESSON]
EXT_L = STD_L  # v3: no Stage 5 lessons (E1 Venn, E2 two-way tables removed)

VARIANTS = {
    'std_student': dict(book='std', mode='student', file='Yr8_Ch8_Probability_Lesson_Booklet'),
    'std_teacher': dict(book='std', mode='teacher', file='Yr8_Ch8_Probability_Lesson_Booklet_Teacher_Copy'),
    'ext_student': dict(book='ext', mode='student', file='Yr8_Ch8_Probability_Extension_Lesson_Booklet'),
    'ext_teacher': dict(book='ext', mode='teacher', file='Yr8_Ch8_Probability_Extension_Lesson_Booklet_Teacher_Copy'),
}


def footer_text(book, mode):
    s = 'Kingscliff High School • Year 8 Mathematics • Probability • ' + ('Extension workbook' if book == 'ext' else 'Workbook')
    if mode == 'teacher':
        s += ' • Teacher copy'
    if mode == 'selfstudy':
        s += ' • E1–E2 self-study'
    return s


# ---------------------------------------------------------------- cover
def cover(book, mode, toc_rows, back_rows):
    pill = '<span class="pillw x">EXTENSION WORKBOOK</span>' if book == 'ext' else '<span class="pillw">WORKBOOK</span>'
    if mode == 'teacher':
        pill += '<span class="pillw t">TEACHER COPY</span>'
    if mode == 'selfstudy':
        pill += '<span class="pillw t">E1–E2 SELF-STUDY</span>'
    toc = ''.join(f'<span class="n{" x" if n.startswith("E") else ""}">{n}</span><span>{t}</span><span class="p">{p}</span>' for n, t, p in toc_rows)
    toc += f'<span class="n">+</span><span>At the back: {back_rows}</span><span></span>'
    if book == 'std':
        levels = '<p>Page 1 of each lesson is <b>Easy ●</b>, page 2 is <b>Medium ●●</b> and page 3 is <b>Hard ●●●</b>: a harder example, mixed questions (a tag shows an earlier lesson or year) and worded problems.</p>'
    else:
        levels = '<p>Your notes and examples match the main workbook, so you follow the class lesson, then do these harder questions: page 1 <b>Medium ●●</b>, page 2 <b>Hard ●●●</b>, page 3 <b>Going further</b>. Everything is Stage 4 content.</p>'
    how = ('<p>Each lesson is <b>three pages</b>. Copy your teacher’s <b>notes</b>, then work through <b>We do</b> (dark boxes: we solve these together; copy every step) '
           'and <b>You do</b> (your turn, one round at a time). Rate each success criterion at the end.</p>' + levels
           + '<p class="small"><i>NSW Mathematics K–10 Syllabus</i> (2022), Stage 4: MA4-PRO-C-01'
           + '. We acknowledge the Bundjalung people, the Traditional Custodians of the land on which we learn.</p>')
    inner = (f'<div class="art"></div><div class="ccard"><img class="logo" src="img/logo.jpg">'
             f'<div class="meta">Mathematics<br>Year 8<br>{pill}</div>'
             f'<h1>Probability</h1><div class="subt">Year 8 Mathematics • {"Extension workbook" if book == "ext" else "Workbook"}</div>'
             f'<div class="fields"><div>Name</div><div>Class</div><div>Teacher</div></div></div>'
             f'<div class="lower"><div class="ibox"><div class="hd">How this workbook works</div><div class="bd">{how}</div></div>'
             f'<div class="ibox"><div class="hd">Contents</div><div class="bd"><div class="toc">{toc}</div></div></div></div>'
             f'<div class="credit">Cover and banner artwork: <i>Kingscliff High School Vision Statement</i> by local Indigenous artist Marni Tuala.</div>')
    return f'<div class="page cover">{inner}</div>'


# ---------------------------------------------------------------- back matter pages
def summary_pages(lessons, book, footer, pno, lesson_pages_map):
    facts = back.FACTS_EXT if book == 'ext' else back.FACTS_STD
    conf = ''.join(f'<div class="r"><span><span class="n">{L["num"]}</span>{L["title"]}</span><span class="tl"><i></i><i></i><i></i></span></div>' for L in lessons)
    head = (f'<div class="bar dark"><span>CHAPTER SUMMARY</span><span class="r">the key facts from every lesson, and how confident you are with each</span></div>'
            f'<div class="conf"><div class="hh"><span>HOW CONFIDENT AM I?</span><span style="font-weight:300;font-size:7.4pt;color:#555"><span class="tl"><i></i><i></i><i></i></span> not yet · getting there · got it</span></div>{conf}</div>'
            f'<div class="box"><div class="hd">Key facts</div><div class="facts">{"".join(f"<div>{x}</div>" for x in facts)}</div></div>')
    away_head = '<div class="bar sand"><span>IF YOU WERE AWAY</span><span class="r">two examples from each lesson, fully worked: read them, then try the lesson’s first round</span></div>'

    def away_block(L):
        ex = back.AWAY[L['key']]
        cells = ''.join(f'<div class="ex"><h5>Example {i + 1}: {t}</h5><p><i>{q}</i></p>{w}</div>' for i, (t, q, w) in enumerate(ex))
        return (f'<div class="away-h"><span>Lesson {L["num"]} • {L["title"]}</span><span>the lesson is on p. {lesson_pages_map[L["key"]]}</span></div>'
                f'<div class="away">{cells}</div>')

    pages = []
    # page A: summary + first two lessons; then 3 lessons per page
    first = lessons[:2]
    rest = lessons[2:]
    pages.append(page(head + away_head + ''.join(away_block(L) for L in first), footer, pno))
    pno += 1
    while rest:
        chunk, rest = rest[:4], rest[4:]
        pages.append(page(away_head.replace('IF YOU WERE AWAY', 'IF YOU WERE AWAY (CONTINUED)') + ''.join(away_block(L) for L in chunk), footer, pno))
        pno += 1
    return pages, pno


def review_pages(book, footer, pno):
    items = back.REVIEW_EXT if book == 'ext' else back.REVIEW_STD
    per_page = 10
    pages = []
    for k in range(0, len(items), per_page):
        chunk = items[k:k + per_page]
        cells = ''
        for i, (tag, q, a) in enumerate(chunk):
            n = k + i + 1
            cells += f'<div class="rq"><div><span class="n">R{n}</span><span class="tag{" x" if tag.startswith("E") else ""}" style="margin-right:1.4mm">{tag}</span>{q}</div><div class="ab" style="height:{30 if book == "std" else 27}mm"></div></div>'
        head = f'<div class="bar dark"><span>CHAPTER REVIEW{" (CONTINUED)" if k else ""}</span><span class="r">questions on every lesson: set out every answer in full • the tag shows the lesson</span></div>'
        pages.append(page(head + f'<div class="review">{cells}</div>', footer, pno))
        pno += 1
    return pages, pno


def ticket_pages(lessons, book, footer, pno):
    lv = ('Easy ●', 'Medium ●●', 'Hard ●●●') if book == 'std' else ('Medium ●●', 'Hard ●●●', 'Going further')
    col = ('#3f7cc0', '#34529a', '#7a1f4e') if book == 'std' else ('#34529a', '#7a1f4e', '#681a42')
    pages = []
    for k in range(0, len(lessons), 4):
        chunk = lessons[k:k + 4]
        fr_html = '<div class="bar dark"><span>EXIT TICKETS</span><span class="r">cut along the dashed lines • write your summary on the back • hand it to your teacher</span></div><div class="cut"></div>'
        bk_html = '<div class="bar dark"><span>SUMMARIES</span><span class="r">the back of your exit tickets: summarise each lesson in your own words</span></div><div class="cut" style="border-color:transparent"></div>'
        for L in chunk:
            qs = back.TICKETS[L['key']][book]
            cols = ''.join(f'<div><span><span class="lv" style="color:{col[i]}">{lv[i]}</span> {q}</span><div class="lines"></div></div>' for i, (q, a) in enumerate(qs))
            fr_html += (f'<div class="ticket"><div class="th"><b>EXIT TICKET</b><span>Lesson {L["num"]}: {L["title"]}</span>'
                        f'<span class="nm">Name ____________________ &nbsp; Class ________</span></div><div class="cols">{cols}</div></div><div class="cut"></div>')
            bk_html += (f'<div class="summ"><div class="th"><span>SUMMARISE LESSON {L["num"]} IN YOUR OWN WORDS</span><span>{L["title"]} • the back of your exit ticket</span></div>'
                        f'<div class="lines"></div></div><div class="cut" style="border-color:transparent"></div>')
        pages.append(page(fr_html, footer, pno))
        pages.append(page(bk_html, footer, pno + 1))
        pno += 2
    return pages, pno


def hw_pages(book, footer, pno):
    hw = back.HW_EXT if book == 'ext' else back.HW_STD
    # front: columns right-to-left so each cell's back lines up when printed double-sided
    order_front = [2, 1, 0]
    rows = [hw[0:3], hw[3:6], hw[6:9]]
    front, backside = '', ''
    for c in range(3):  # 3 rows on the page; each row holds hw[i], hw[i+3], hw[i+6] read top-right first
        pass
    # layout like the stats booklet: column j holds HW j*3+1..j*3+3; front shows columns reversed
    cols = [hw[0:3], hw[3:6], hw[6:9]]
    for r in range(3):
        for j in order_front:
            code, title, qs = cols[j][r]
            body = ''.join(f'<div class="hq"><span class="n">{i + 1}</span><span>{q}</span></div><div class="hl"></div>' for i, (q, a) in enumerate(qs))
            front += f'<div class="hwcell"><div class="hh"><span>{code} &nbsp;{title}</span><span>✂</span></div>{body}</div>'
        for j in [0, 1, 2]:
            code, title, qs = cols[j][r]
            backside += (f'<div class="hwcell"><div class="hh"><span>{code} &nbsp;Name and working</span></div>'
                         '<div class="fld">Name <span class="l"></span></div><div class="fld">Class <span class="l"></span> Due <span class="l"></span></div>'
                         '<div class="fld" style="margin-top:2mm">How did it go? &nbsp;<span class="tl"><i></i><i></i><i></i></span> easy · okay · stuck</div>'
                         '<div style="margin-top:1.4mm">More working:</div><div class="hl" style="flex:1"></div></div>')
    head = '<div class="bar"><span>HOMEWORK STRIPS</span><span class="r">after each lesson, cut out its strip (start at the top right), do it at home, and hand it in next lesson</span></div>'
    p1 = page(head + f'<div class="hwgrid">{front}</div>', footer, pno)
    p2 = page('<div class="bar"><span>HOMEWORK STRIPS: THE BACK</span><span class="r">name, how it went, and more working</span></div>' + f'<div class="hwgrid">{backside}</div>', footer, pno + 1)
    return [p1, p2], pno + 2


def working_page(footer, pno):
    return page('<div class="bar sand"><span>WORKING SPACE</span><span class="r">extra working for any lesson</span></div>'
                '<div class="dots" style="height:262mm;margin-top:3mm;border:.3mm solid #ddd;border-radius:1.8mm"></div>', footer, pno)


# ---------------------------------------------------------------- answers (teacher copies)
def strip_tags(s):
    return re.sub(r'<[^>]+>', '', s)


def est_h(text):
    t = strip_tags(text)
    lines = max(1, -(-len(t) // 52))
    return lines * 3.9 + (1.4 if 'class="fr' in text else 0) + 0.5


def answer_items(lessons, all_answers, book):
    """Flat list of (html, height_mm) items."""
    items = []
    lv = ('Easy', 'Medium', 'Hard') if book == 'std' else ('Medium', 'Hard', 'Going further')
    for L in lessons:
        a = all_answers[L['key']]
        items.append((f'<h3>Lesson {L["num"]} · {L["title"]}</h3>', 7))
        items.append((f'<h4>PAGES 1–2 · {lv[0].upper()} AND {lv[1].upper()} ROUNDS</h4>', 5))
        items += [(f'<p><b>{n}</b>{x}</p>', est_h(x)) for n, x in a['rounds']]
        items.append((f'<h4>PAGE 3 · {lv[2].upper()}</h4>', 5))
        items += [(f'<p><b>{n}</b>{x}</p>', est_h(x)) for n, x in a['p3']]
        items.append(('<h4>WORDED PROBLEMS</h4>', 5))
        items += [(f'<p><b>W{n}</b>{x}</p>', est_h(x)) for n, x in a['word']]
    rev = back.REVIEW_EXT if book == 'ext' else back.REVIEW_STD
    items.append(('<h3>Chapter review</h3>', 7))
    items += [(f'<p><b>R{i + 1}</b>{a}</p>', est_h(a)) for i, (t, q, a) in enumerate(rev)]
    items.append(('<h3>Exit tickets</h3>', 7))
    lvs = ('E', 'M', 'H') if book == 'std' else ('M', 'H', 'F')
    for L in lessons:
        qs = back.TICKETS[L['key']][book]
        txt = ' · '.join(f'<b>{lvs[i]}</b>{a}' for i, (q, a) in enumerate(qs))
        items.append((f'<p><b>L{L["num"]}</b>{txt}</p>', est_h(txt) + 1))
    items.append(('<h3>Homework strips</h3>', 7))
    hw = back.HW_EXT if book == 'ext' else back.HW_STD
    for code, title, qs in hw:
        txt = ' · '.join(f'<b>{i + 1}</b>{a}' for i, (q, a) in enumerate(qs))
        items.append((f'<p><b>{code}</b>{txt}</p>', est_h(txt) + 1))
    return items


def answer_pages(items, footer, pno, cap=478):
    pages, cur, h = [], [], 0
    for it in items:
        if h + it[1] > cap and cur:
            pages.append(cur)
            cur, h = [], 0
        cur.append(it[0])
        h += it[1]
    if cur:
        pages.append(cur)
    out = []
    for k, chunk in enumerate(pages):
        head = f'<div class="bar maroon"><span>ANSWERS{" (CONTINUED)" if k else ""}</span><span class="r">teacher copy • working shown where it helps • Example answers are left for you to work live</span></div>'
        out.append(page(head + f'<div class="ans" style="height:262mm;column-fill:auto">{"".join(chunk)}</div>', footer, pno))
        pno += 1
    return out, pno


COVERAGE = [
    ('8.01 Probability', 'Q1 spinners', 'L1 Ex 1b, Round 1; L2 Round 1'),
    ('', 'Q2 count outcomes, equally likely', 'L1 Rounds 2, 5 (std); L1 Rounds 2, 4 (ext)'),
    ('', 'Q3 list outcomes in events', 'L1 Round 4 (std), Round 3 (ext)'),
    ('', 'Q4 money box', 'L2 Ex 2a; L2 Round 4 (ext)'),
    ('', 'Q5 jar of lollies', 'L2 Ex 1c, Round 6 (std)'),
    ('', 'Q6, Q8, Q10 multiple choice', 'L2 Round 6 Q20 (ext); L2 page 3 Q1; L2 Ex 2d'),
    ('', 'Q7 match sample space', 'L1 Ex 2b'),
    ('', 'Q9 Malik’s cards', 'L2 worded W2 (std)'),
    ('', 'Q11 values ↔ chance words', 'L1 Round 6 (std), Round 6 (ext)'),
    ('', 'Q12 deck of cards', 'L2 Ex 2b, Round 5 (std), Round 3 (ext)'),
    ('', 'Q13 rain in April', 'L2 W3 (std); L6 Ex 1d'),
    ('', 'Q14 name from the roll', 'L1 W3 (std); L3 W3 (std)'),
    ('', 'Q15 Esky', 'L2 W1 (std); L2 page 3 Q1–2 (ext)'),
    ('', 'Investigation: complementary events', 'L3 notes and Ex 1'),
    ('8.02 Complementary events', 'Q1 write complements', 'L3 Round 1 (std and ext)'),
    ('', 'Q2–Q4 not red, die, books', 'L3 Ex 1b, Rounds 3 and 5 (std), Round 2 (ext)'),
    ('', 'Q5 car park', 'L3 page 3 Q1 (std and ext)'),
    ('', 'Q6 teacher’s birth month', 'L1 Round 3 Q10 (months); L2 Round 6 (ext)'),
    ('', 'Q7 phone number; Q8 raffle', 'L3 page 3 Q5 (std); L3 Ex 2d'),
    ('', 'Q9 jelly beans; Q10 complement values', 'L3 page 3 Q3–4 (std), Rounds 3–4 (ext); L3 Round 4 (std)'),
    ('', 'Q11 toy cars', 'L3 Ex 2b, W1 (std and ext)'),
    ('', 'Q12 captain; Q13 rain 85%; Q14 complement of winning', 'L3 W3 (std); L3 Round 4; L3 Ex 2c'),
    ('', 'Q15 coin grid game', 'L3 W2 (std), W3 (ext)'),
    ('', 'Q16 PROBABILITY; Q17 washing up; Q18 4-digit numbers', 'L3 page 3 Q6 (std), Round 6 (ext); Review R10 (std); L2 W1 (ext), Review R12 (std)'),
    ('8.03 Venn diagrams*', 'Q1–Q8', 'Not included (Stage 5 Path)'),
    ('8.04 Two-way tables*', 'Q1–Q7', 'Not included (Stage 5 Path)'),
    ('8.05 Probability problems', 'Q1–Q9, Q13', 'L4 Ex 1–2, Rounds 1–6 (std and ext); L3 Round 4 (eggs)'),
    ('', 'Q10* tennis', 'L4 page 3 Q1–2 (std); L4 Round 3 (ext), rewritten as single-event questions'),
    ('', 'Q11* camp Venn; Q12* hockey/judo', 'Not included (Stage 5 Path)'),
    ('8.06 Observed and expected', 'Q1 Harper’s die', 'L5 Ex 1a–b; L6 Ex 2a'),
    ('', 'Q2, Q5 coin and die experiments', 'L5 Round 6; L6 Ex 1b, Rounds 3 and 6'),
    ('', 'Q3 Vinh’s spinner', 'L5 Ex 1c, Round 3; L6 Ex 1c, Round 2'),
    ('', 'Q4 matchboxes', 'L5 Ex 2a–b, Round 4; L6 Ex 2b, Round 4'),
    ('', 'Q6 Sefina; Q7 die 80 rolls', 'L5 Ex 1d; L5 Ex 2c, L6 page 3 Q1–2'),
    ('', 'Q8 dice sums', 'L5 page 3 Q2–4 (std), Round 5 (ext); L6 Round 6 (ext)'),
    ('Technology and investigations', 'rolling a die, tossing a coin, family of 4', 'L5 Round 6, W3 (std), W1 (ext); L6 Round 6'),
    ('Test yourself 8', 'Q1–Q6, Q10–Q11; Q7–Q9*', 'L1–L6 and review; Q7–Q9 not included (Stage 5 Path)'),
]


def coverage_page(footer, pno):
    rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in COVERAGE)
    note = ('<div class="callout"><b class="k">Not included</b> Two-up (Did you know?) and lotto contexts (left out by choice), Power plus (not selected), '
            'Mental skills 8 (whole-number skills, not probability). * marks textbook Year 9 path content. The 2022 syllabus places Venn diagrams, two-way tables, ‘at least / at most’, ‘and’, inclusive and exclusive ‘or’ (MA5-PRO-P-01) and multistage experiments (MA5-PRO-C-01) in Stage 5, so neither booklet includes them. '
            'Where the textbook uses ‘at least’ in 8.01–8.02, the questions are reworded (e.g. ‘a number greater than 7’).</div>')
    return page('<div class="bar maroon"><span>TEXTBOOK COVERAGE</span><span class="r">New Century Maths 8, Chapter 8: where each exercise’s skills appear (questions are rewritten, not copied)</span></div>'
                f'<table class="cov"><tr><th>Section</th><th>Textbook questions</th><th>Where in this booklet</th></tr>{rows}</table>{note}', footer, pno)


# ---------------------------------------------------------------- assemble
def build(variant):
    v = VARIANTS[variant]
    book, mode = v['book'], v['mode']
    lessons = EXT_L if book == 'ext' else STD_L
    footer = footer_text(book, mode)
    pages, answers, start = [], {}, {}
    pno = 2
    for L in lessons:
        lmode = mode
        if mode == 'selfstudy' and not L.get('ext_only'):
            lmode = 'student'
        ps, a = lesson_pages(L, book, lmode, footer, pno)
        start[L['key']] = pno
        pages += ps
        answers[L['key']] = a
        pno += 3
    back_start = pno
    sp, pno = summary_pages(lessons, book, footer, pno, start)
    rp, pno = review_pages(book, footer, pno)
    pages += sp + rp
    # exit tickets and homework strips must start on a front (odd) page
    if pno % 2 == 0:
        pages.append(working_page(footer, pno))
        pno += 1
    tick_start = pno
    tp, pno = ticket_pages(lessons, book, footer, pno)
    hw_start = pno
    hp, pno = hw_pages(book, footer, pno)
    pages += tp + hp
    if mode == 'teacher':
        ans_start = pno
        ap, pno = answer_pages(answer_items(lessons, answers, book), footer, pno)
        pages += ap
        pages.append(coverage_page(footer, pno))
        pno += 1
    toc_rows = [(L['num'], L['title'] + (' <span class="maroon" style="font-size:7.6pt">(Stage 5 Path)</span>' if L.get('ext_only') else ''), start[L['key']]) for L in lessons]
    back_rows = (f'chapter summary and if you were away {back_start}, review {back_start + len(sp)}, exit tickets {tick_start}, homework strips {hw_start}'
                 + (f', answers {ans_start}' if mode == 'teacher' else ''))
    pages.insert(0, cover(book, mode, toc_rows, back_rows))
    title = v['file'].replace('_', ' ')
    os.makedirs('out', exist_ok=True)
    open(f'out/{v["file"]}.html', 'w').write(html_doc(pages, title))
    return v['file'], len(pages)


if __name__ == '__main__':
    which = sys.argv[1:] or list(VARIANTS)
    for w in which:
        print(build(w))
