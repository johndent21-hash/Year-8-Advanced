"""HTML/CSS building blocks: Kingscliff statistical-investigation look,
Year 9 booklet structure (Notes / We do / You do rounds / Worded problems)."""

CSS = r"""
@font-face{font-family:Poppins;font-weight:300;src:url(fonts/poppins-latin-300-normal.woff2)}
@font-face{font-family:Poppins;font-weight:300;font-style:italic;src:url(fonts/poppins-latin-300-italic.woff2)}
@font-face{font-family:Poppins;font-weight:400;src:url(fonts/poppins-latin-400-normal.woff2)}
@font-face{font-family:Poppins;font-weight:500;src:url(fonts/poppins-latin-500-normal.woff2)}
@font-face{font-family:Poppins;font-weight:600;src:url(fonts/poppins-latin-600-normal.woff2)}
@font-face{font-family:Poppins;font-weight:700;src:url(fonts/poppins-latin-700-normal.woff2)}
@font-face{font-family:PagellaTT;font-weight:400;font-style:normal;src:url(fonts/pagella-regular.ttf)}
@font-face{font-family:PagellaTT;font-weight:700;font-style:normal;src:url(fonts/pagella-bold.ttf)}
@font-face{font-family:PagellaTT;font-weight:400;font-style:italic;src:url(fonts/pagella-italic.ttf)}
@font-face{font-family:PagellaTT;font-weight:700;font-style:italic;src:url(fonts/pagella-bolditalic.ttf)}
@page{size:A4;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{font-family:PagellaTT,'TeX Gyre Pagella',serif;font-size:10.5pt;color:#262626;line-height:1.25}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;padding:9mm 14mm 0 14mm;background:#fff}
.page:last-child{page-break-after:auto}
.page.fill{display:flex;flex-direction:column;padding-bottom:15.5mm}
.page.fill>*{flex:none}
.page.fill>.yd.grow{flex:1 1 auto;display:flex;flex-direction:column}
.yd.grow>.rw{flex:1 1 auto;display:flex;flex-direction:column}
.yd.grow>.rw>.cards{flex:1 1 auto;grid-auto-rows:1fr}
.rside{display:grid;gap:2.6mm}
.yd.grow>.rw>.rside{flex:1 1 auto}
.rside>.cards{grid-auto-rows:1fr}
.infobox.side{margin-top:0;flex-direction:column;gap:2mm;padding:2mm}
.sans{font-family:Poppins,sans-serif}
.blue{color:#3f7cc0}.maroon{color:#7a1f4e}
svg.g{display:block;flex:none}
b,strong{font-weight:700}
/* ---------- footer */
.footer{position:absolute;left:14mm;right:14mm;bottom:6.5mm;display:flex;justify-content:space-between;align-items:center;font-family:Poppins;font-weight:300;font-size:7.3pt;color:#8a8a8a}
.pno{width:6.6mm;height:6.6mm;border-radius:50%;background:#3f7cc0;color:#fff;font-weight:500;display:flex;align-items:center;justify-content:center;font-size:7.6pt}
/* ---------- lesson banner */
.banner{height:13mm;background:#3f3f3f url(img/banner_full.jpg) center/100% 100% no-repeat;border-radius:1mm;display:flex;align-items:center;padding:0 4mm 0 5mm;color:#fff;font-family:Poppins}
.banner.b2{background:#3f3f3f url(img/banner2_full.jpg) center/100% 100% no-repeat}
.banner .num{font-weight:300;font-size:19pt;margin-right:3.5mm;line-height:1}
.banner .title{font-weight:500;font-size:13pt;white-space:nowrap}
.banner .sub{font-weight:300;font-size:7.6pt;color:#d4d4d4;margin-left:4mm;white-space:nowrap}
.banner .lvl{margin-left:auto;background:#fff;font-weight:600;font-size:7.2pt;letter-spacing:.09em;padding:.9mm 2.8mm;border-radius:1.2mm;white-space:nowrap}
.lvl.easy{color:#3f7cc0}.lvl.medium{color:#34529a}.lvl.hard{color:#7a1f4e}.lvl.further{background:#7a1f4e!important;color:#fff}
.banner .lvl .d{letter-spacing:0;margin-left:1.2mm}
/* ---------- learning intention + success criteria (compact strip) */
.li2{display:grid;grid-template-columns:.86fr 1.3fr;gap:4mm;background:#eaf1fa;border-left:1.1mm solid #3f7cc0;border-radius:0 1.5mm 1.5mm 0;padding:1.7mm 3mm;margin-top:3mm;font-size:8.9pt;line-height:1.2}
.li2 .h{display:block;font-family:Poppins;font-weight:500;color:#3f7cc0;font-size:7.6pt;letter-spacing:.05em;margin-bottom:.5mm}
.li2 .sch{display:flex;justify-content:space-between;align-items:baseline}
.li2 .rate{font-family:Poppins;font-weight:300;font-size:6.4pt;color:#555}
.li2 .row{display:flex;justify-content:space-between;gap:2mm;font-size:8.6pt;line-height:1.2;margin-top:.25mm}
.li2 .row span:first-child:before{content:"\25BA\00a0";color:#3f7cc0;font-size:7pt}
.tl{display:inline-flex;gap:.5mm;flex:none;margin-top:.3mm;vertical-align:-.3mm}
.tl i{display:inline-block;width:2.5mm;height:2.5mm;border-radius:50%;border:.3mm solid}
.tl i:nth-child(1){border-color:#d9534f}.tl i:nth-child(2){border-color:#ee9a3a}.tl i:nth-child(3){border-color:#4caf50}
/* ---------- generic boxes */
.box{border:.35mm solid #3f7cc0;border-radius:1.8mm;margin-top:3mm;overflow:hidden;background:#fff}
.box>.hd{background:#3f7cc0;color:#fff;font-family:Poppins;font-size:9.2pt;font-weight:500;padding:.9mm 3mm;display:flex;align-items:center;gap:3mm;letter-spacing:.02em}
.hd .note{font-weight:300;font-size:7.4pt;color:#e6eef8;letter-spacing:0}
.hd .right{margin-left:auto;font-weight:300;font-size:7.6pt;display:flex;align-items:center;gap:2mm}
.hd .dateln{display:inline-block;width:30mm;border-bottom:.3mm solid #fff;height:3.4mm}
.hd .tc{background:#fff;color:#3f7cc0;font-weight:600;font-size:7pt;letter-spacing:.1em;padding:.4mm 2mm;border-radius:1mm}
.dots{background-image:url(img/dot.png);background-size:4.5mm 4.5mm;background-position:0 0}
/* teacher notes */
.tnotes{display:grid;grid-template-columns:1.12fr 1fr .98fr;gap:4mm;padding:1.6mm 3mm;font-size:8.3pt;line-height:1.18;height:100%}
.tnotes h4{margin:0 0 .5mm;font-family:Poppins;font-weight:600;font-size:6.9pt;letter-spacing:.1em;color:#7a1f4e}
.tnotes p{margin:0 0 .4mm}
.tnotes .fbox{border:.3mm solid #3f7cc0;border-radius:1.2mm;padding:.8mm 2mm;margin:.4mm 0 1mm;background:#eaf1fa;display:flex;align-items:center;justify-content:center;gap:1mm;font-size:8.8pt;text-align:center}
.step{display:inline-flex;width:3.5mm;height:3.5mm;border-radius:50%;background:#3d3d3d;color:#fff;font-family:Poppins;font-weight:600;font-size:6.2pt;align-items:center;justify-content:center;margin-right:1mm;vertical-align:.1mm;flex:none}
/* ---------- WE DO */
.wedo{border:.35mm solid #3d3d3d;border-radius:1.8mm;margin-top:3mm;overflow:hidden;background:#fff}
.wedo>.hd{background:#3d3d3d;color:#fff;font-family:Poppins;font-size:9.2pt;font-weight:600;letter-spacing:.08em;padding:.9mm 3mm;display:flex;align-items:center;gap:3mm}
.wedo .ex{display:flex;align-items:center;gap:2.5mm;padding:1.8mm 3mm 0;font-family:Poppins;font-weight:500;font-size:9.2pt;color:#262626}
.exdata{display:flex;gap:6mm;justify-content:center;align-items:center;padding:1.6mm 3mm 0}
.expill{background:#3d3d3d;color:#fff;font-weight:600;font-size:7.4pt;padding:.5mm 2.2mm;border-radius:1mm;letter-spacing:.04em;white-space:nowrap}
.parts{display:grid;gap:3mm;padding:1.6mm 3mm 2.6mm}
.part{display:flex;flex-direction:column}
.part .lab{display:flex;align-items:center;gap:1.6mm;font-family:Poppins;font-size:8.5pt;font-weight:500;min-height:5mm}
.letter{display:inline-flex;width:4.6mm;height:4.6mm;border-radius:50%;background:#3d3d3d;color:#fff;font-family:Poppins;font-weight:600;font-size:7.4pt;align-items:center;justify-content:center;flex:none}
.part .fig{display:flex;align-items:center;justify-content:center;gap:1.5mm;margin-top:.8mm}
.part .txt{font-size:8.5pt;line-height:1.16;margin:.5mm 0 0}
.wbox{border:.3mm solid #b8b8b8;border-radius:1.5mm;margin-top:1.6mm;flex:1}
.wbox.worked{background:#fbfaf6;border-color:#c8c2a8;padding:1mm 1.6mm;font-size:8pt;line-height:1.22}
.wbox.worked p{margin:0 0 .5mm}
/* ---------- YOU DO */
.yd{position:relative;margin-top:4.6mm;border:.4mm solid #3f7cc0;border-radius:2.4mm;background:#f5f6fa;padding:4mm 3mm 2.8mm}
.yd .tab{position:absolute;top:-2.5mm;left:4mm;display:flex;align-items:center;font-family:Poppins;font-size:7.6pt;line-height:1}
.yd .tab .lb{background:#3f7cc0;color:#fff;font-weight:500;padding:.9mm 2.6mm;border-radius:1.2mm;letter-spacing:.06em}
.yd .tab .t{background:#fff;color:#3f7cc0;font-weight:300;padding:.8mm 2mm;margin-left:1mm}
.yd .cnt{position:absolute;top:-1.9mm;right:4mm;background:#fff;color:#3f7cc0;font-family:Poppins;font-weight:600;font-size:7pt;letter-spacing:.1em;padding:0 2mm;line-height:1.2}
.yd.medium{border-color:#34529a}
.yd.medium .tab .lb{background:#34529a}.yd.medium .tab .t,.yd.medium .cnt{color:#34529a}
.yd.hard{border-color:#7a1f4e;background:#f8f4f6}
.yd.hard .tab .lb{background:#7a1f4e}.yd.hard .tab .t,.yd.hard .cnt{color:#7a1f4e}
.yd.further{border-color:#681a42;background:#f7f2f4}
.yd.further .tab .lb{background:#681a42}.yd.further .tab .t,.yd.further .cnt{color:#681a42}
.rem{background:#fff;border-left:1mm solid #3f7cc0;border-radius:.8mm;padding:1mm 2.5mm;font-size:8.7pt;line-height:1.28;flex:none}
.rem b.k{font-family:Poppins;font-weight:600;color:#3f7cc0;font-size:7pt;letter-spacing:.12em;margin-right:2mm}
.medium .rem{border-left-color:#34529a}.medium .rem b.k{color:#34529a}
.hard .rem,.further .rem{border-left-color:#7a1f4e}.hard .rem b.k,.further .rem b.k{color:#7a1f4e}
.round{display:flex;align-items:center;gap:2mm;margin:2mm 0 1.4mm;font-family:Poppins;font-weight:500;color:#3f7cc0;font-size:8.4pt;line-height:1.18}
.medium .round{color:#34529a}.hard .round,.further .round{color:#7a1f4e}
.round .pill{background:#3d3d3d;color:#fff;font-weight:600;font-size:7pt;letter-spacing:.1em;padding:.55mm 2.2mm;border-radius:1mm;white-space:nowrap;flex:none}
.sep{border-top:.3mm dashed #b9c4da;margin-top:2.4mm;flex:none}
.hard .sep,.further .sep{border-top-color:#dcc3cf}
.cards{display:grid;gap:2.6mm}
.c4{grid-template-columns:repeat(4,minmax(0,1fr))}.c3{grid-template-columns:repeat(3,minmax(0,1fr))}.c2{grid-template-columns:repeat(2,minmax(0,1fr))}.c1{grid-template-columns:minmax(0,1fr)}
.card{background:#fff;border:.3mm solid #c9d3e6;border-radius:1.8mm;padding:1.6mm 2.2mm 1.4mm;display:flex;flex-direction:column;position:relative;min-width:0}
.hard .card,.further .card{border-color:#e2cfd9}
.card .top{display:flex;gap:1.8mm;align-items:flex-start}
.qn{width:5.2mm;height:5.2mm;border-radius:50%;border:.35mm solid #3f7cc0;color:#3f7cc0;font:600 7.4pt Poppins;display:flex;align-items:center;justify-content:center;flex:none;background:#fff}
.medium .qn{border-color:#34529a;color:#34529a}
.hard .qn,.further .qn{border-color:#7a1f4e;color:#7a1f4e}
.card .q{font-size:8.8pt;line-height:1.16;flex:1;padding-top:.3mm}
.card .fig{flex:1;display:flex;align-items:center;justify-content:center;gap:1.5mm;min-height:0;padding:.6mm 0}
.card .figt{display:flex;align-items:center;justify-content:center;gap:1.5mm;padding:1.2mm 0 .4mm}
.tag{font-family:Poppins;font-size:6.2pt;font-weight:500;color:#555;border:.25mm solid #aaa;border-radius:1mm;padding:.1mm 1.2mm;white-space:nowrap;background:#fff;margin-left:auto;flex:none}
.tag.x{color:#7a1f4e;border-color:#7a1f4e}
.ln{display:flex;align-items:flex-end;gap:1.6mm;height:5.4mm;flex:none}
.ln .k{font:500 6.3pt Poppins;color:#666;min-width:13mm;flex:none;padding-bottom:.4mm;white-space:nowrap}
.ln .v{flex:1;border-bottom:.25mm solid #9aa3b5;font-family:Poppins;font-weight:600;font-size:7.8pt;color:#3f7cc0;padding-bottom:.3mm;white-space:nowrap;overflow:hidden}
.space{flex:1}
.opts{display:flex;flex-wrap:wrap;gap:1mm 3mm;font-size:9pt;margin-top:1mm}
.opts span b{font-family:Poppins;font-weight:600;font-size:7.4pt;color:#7a1f4e;margin-right:.8mm}
/* math */
.fr{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;font-size:.84em;line-height:1.02;margin:0 .1em}
.fr>span:first-child{border-bottom:.22mm solid currentColor;padding:0 .18em}
.fr.big{font-size:1em}
.it{font-style:italic}
/* tables */
table.t{border-collapse:collapse;font-size:8.8pt;margin:0 auto}
table.t td,table.t th{border:.3mm solid #8d97a8;padding:.5mm 1.8mm;text-align:center;line-height:1.15}
table.t th{background:#eaf1fa;font-family:Poppins;font-weight:500;font-size:7.2pt;color:#3d3d3d}
table.t td.blank{min-width:9mm;height:5.4mm}
table.t td.l{text-align:left}
.infobox{background:#fff;border:.3mm solid #c9d3e6;border-radius:1.8mm;padding:1.8mm 3mm;display:flex;align-items:center;gap:5mm;justify-content:center;margin-top:2mm}
.hard .infobox,.further .infobox{border-color:#e2cfd9}
.infobox .cap{font-family:Poppins;font-weight:500;font-size:7.6pt;color:#3d3d3d;max-width:55mm;line-height:1.3}
/* ---------- section bars */
.bar{display:flex;justify-content:space-between;align-items:center;background:#3f7cc0;color:#fff;font-family:Poppins;font-weight:500;font-size:9pt;padding:.9mm 3mm;border-radius:1mm;margin-top:2.4mm}
.bar:first-child{margin-top:0}
.bar .r{font-weight:300;font-size:7.6pt}
.bar.dark{background:#3d3d3d}.bar.maroon{background:#7a1f4e}.bar.sand{background:#aaa58f}
/* ---------- cover */
.cover{padding:0}
.cover .art{position:absolute;left:0;top:0;width:210mm;height:172mm;background:url(img/cover.jpg) center top/cover no-repeat}
.cover .ccard{position:absolute;left:18mm;right:18mm;top:100mm;height:94mm;border-radius:2.5mm;background:#fff;box-shadow:1.2mm 1.2mm 0 #e3e3e3;padding:9mm 10mm 0 10mm}
.cover .logo{width:48mm}
.cover .meta{position:absolute;right:10mm;top:10mm;text-align:right;font-family:Poppins;font-size:9.2pt;color:#3d3d3d;line-height:1.35}
.cover .pillw{display:inline-block;margin-top:2.6mm;background:#3f7cc0;color:#fff;font-weight:500;font-size:8.4pt;padding:.8mm 3mm;border-radius:1mm;letter-spacing:.02em}
.cover .pillw.x{background:#7a1f4e}
.cover .pillw.t{background:#3d3d3d;margin-left:1.5mm}
.cover h1{font-family:Poppins;font-weight:500;font-size:37pt;color:#3d3d3d;margin:7mm 0 0;letter-spacing:-.01em;line-height:1.05}
.cover .subt{font-family:Poppins;font-weight:300;color:#3f7cc0;font-size:12pt;margin-top:3mm}
.cover .fields{display:grid;grid-template-columns:2.6fr 1fr 1.1fr;gap:6mm;margin-top:6mm;font-family:Poppins;font-weight:300;font-size:7.4pt;color:#777}
.cover .fields div{border-bottom:.3mm solid #999;height:12mm}
.cover .lower{position:absolute;left:14mm;right:14mm;top:201mm;display:grid;grid-template-columns:1.05fr 1fr;gap:5mm}
.ibox{border:.35mm solid #3f7cc0;border-radius:1.8mm;overflow:hidden;font-size:9.1pt;line-height:1.26;background:#fff}
.ibox .hd{background:#3f7cc0;color:#fff;font-family:Poppins;font-weight:500;font-size:9pt;padding:1mm 3mm}
.ibox .bd{padding:2.2mm 3.2mm}
.ibox p{margin:0 0 1.4mm}
.ibox .small{font-size:7.9pt;color:#666;line-height:1.25}
.toc{display:grid;grid-template-columns:7mm 1fr 8mm;row-gap:.4mm;font-size:9.1pt}
.toc .n{font-family:Poppins;color:#3f7cc0;font-weight:500;text-align:right;padding-right:2mm}
.toc .n.x{color:#7a1f4e}
.toc .p{text-align:right}
.credit{position:absolute;left:0;right:0;bottom:7mm;text-align:center;font-family:Poppins;font-weight:300;font-size:7.4pt;color:#888}
/* ---------- back matter */
.conf{background:#eaf1fa;border-radius:1.5mm;padding:2mm 3mm;margin-top:2.4mm;display:grid;grid-template-columns:1fr 1fr;column-gap:8mm;row-gap:.8mm;font-size:9.2pt}
.conf .hh{grid-column:span 2;display:flex;justify-content:space-between;font-family:Poppins;font-weight:500;color:#3f7cc0;font-size:8.6pt}
.conf .r{display:flex;justify-content:space-between;align-items:center}
.conf .r .n{font-family:Poppins;color:#3f7cc0;font-weight:500;width:6mm;display:inline-block}
.facts{display:grid;grid-template-columns:1fr 1fr;column-gap:7mm;row-gap:1.6mm;padding:2.4mm 3.2mm;font-size:9pt;line-height:1.25}
.facts .x{color:#7a1f4e}
.away-h{display:flex;justify-content:space-between;align-items:baseline;margin-top:2.6mm;font-family:Poppins;font-size:9.4pt;color:#3d3d3d}
.away-h span:last-child{font-weight:300;font-size:7.4pt;color:#777}
.away{display:grid;grid-template-columns:1fr 1fr;gap:3mm;margin-top:1.2mm}
.away .ex{background:#f5f3eb;border-left:1.1mm solid #aaa58f;border-radius:0 1.5mm 1.5mm 0;padding:1.8mm 2.6mm;font-size:8.8pt;line-height:1.28}
.away .ex h5{margin:0 0 .6mm;font-family:Poppins;font-weight:500;font-size:8.8pt;color:#3d3d3d}
.away .ex p{margin:0 0 .5mm}
.review{display:grid;grid-template-columns:1fr 1fr;column-gap:6mm;row-gap:2.4mm;margin-top:2.6mm}
.rq{font-size:9.3pt;line-height:1.25;display:flex;flex-direction:column}
.rq .n{font-family:Poppins;font-weight:500;color:#3f7cc0;margin-right:1.4mm}
.rq .ab{border:.3mm solid #cfd5e0;border-radius:1.5mm;margin-top:1.2mm;background-image:repeating-linear-gradient(#fff 0,#fff 6.2mm,#d6dbe4 6.2mm,#d6dbe4 6.5mm);background-position:0 1mm}
.cut{border-top:.35mm dashed #999;margin:3mm 0;position:relative;height:0}
.cut:before{content:"\2702";position:absolute;left:6mm;top:-2.6mm;background:#fff;padding:0 1mm;color:#666;font-size:9pt;font-family:'DejaVu Sans'}
.ticket{border:.35mm solid #888;border-left:1.6mm solid #3d3d3d;border-radius:1.8mm;padding:2mm 3mm;height:52mm;display:flex;flex-direction:column}
.ticket .th{display:flex;align-items:baseline;gap:3mm;font-family:Poppins;font-size:8.8pt;color:#3d3d3d}
.ticket .th b{font-weight:600}
.ticket .th .nm{margin-left:auto;font-weight:300}
.ticket .cols{display:grid;grid-template-columns:repeat(3,1fr);flex:1;margin-top:1.6mm}
.ticket .cols>div{padding:0 2.4mm;border-left:.3mm solid #bbb;font-size:8.9pt;line-height:1.22;display:flex;flex-direction:column}
.ticket .cols>div:first-child{border-left:none;padding-left:0}
.ticket .lv{font-family:Poppins;font-weight:500;font-size:8.2pt}
.ticket .lines{flex:1;background-image:repeating-linear-gradient(#fff 0,#fff 5.6mm,#d6dbe4 5.6mm,#d6dbe4 5.9mm);margin-top:1mm}
.summ{border:.35mm solid #888;border-radius:1.8mm;padding:2mm 3mm;height:52mm;display:flex;flex-direction:column}
.summ .th{display:flex;justify-content:space-between;font-family:Poppins;font-size:8.8pt;color:#3d3d3d}
.summ .th span:last-child{font-weight:300;font-size:7.4pt;color:#777}
.summ .lines{flex:1;background-image:repeating-linear-gradient(#fff 0,#fff 7mm,#d6dbe4 7mm,#d6dbe4 7.3mm);margin-top:1mm}
.hwgrid{display:grid;grid-template-columns:repeat(3,1fr);border:.3mm solid #ccc;margin-top:2mm}
.hwcell{height:84mm;padding:2.2mm 3mm;border-right:.35mm dashed #999;border-bottom:.35mm dashed #999;display:flex;flex-direction:column;font-size:8.8pt;line-height:1.22}
.hwcell:nth-child(3n){border-right:none}
.hwcell .hh{background:#3f7cc0;color:#fff;font-family:Poppins;font-size:8pt;padding:.7mm 2mm;display:flex;justify-content:space-between}
.hwcell .hq{display:flex;gap:1.6mm;margin-top:1.6mm}
.hwcell .hq .n{font-family:Poppins;color:#3f7cc0;font-weight:500}
.hwcell .hl{height:9mm;background-image:repeating-linear-gradient(#fff 0,#fff 4.2mm,#d6dbe4 4.2mm,#d6dbe4 4.5mm)}
.hwcell .fld{display:flex;gap:2mm;margin-top:1.4mm;font-size:8.6pt}
.hwcell .fld span.l{flex:1;border-bottom:.25mm solid #aaa}
/* answers */
.ans{column-count:2;column-gap:7mm;font-size:8.4pt;line-height:1.28;margin-top:2.4mm}
.ans h3{font-family:Poppins;font-weight:500;font-size:9pt;color:#fff;background:#3d3d3d;padding:.6mm 2mm;margin:0 0 1mm;border-radius:.8mm;break-after:avoid}
.ans h4{font-family:Poppins;font-weight:500;font-size:7.6pt;color:#3f7cc0;margin:1.2mm 0 .3mm;letter-spacing:.04em;break-after:avoid}
.ans .blk{break-inside:avoid-column;margin-bottom:2mm}
.ans p{margin:0 0 .35mm;break-inside:avoid}
.ans p b{font-family:Poppins;font-weight:600;font-size:7.4pt;color:#7a1f4e;margin-right:1mm}
.cov{font-size:8.2pt;border-collapse:collapse;width:100%;margin-top:2mm}
.cov td,.cov th{border:.25mm solid #c0c6d2;padding:.6mm 1.6mm;text-align:left;vertical-align:top;line-height:1.22}
.cov th{background:#eaf1fa;font-family:Poppins;font-weight:500;font-size:7.4pt}
.callout{background:#f5f3eb;border-left:1.1mm solid #7a1f4e;padding:1.6mm 3mm;font-size:9pt;margin-top:2.6mm;border-radius:0 1.5mm 1.5mm 0;line-height:1.28}
.callout b.k{font-family:Poppins;font-weight:500;color:#7a1f4e;font-size:8.4pt;margin-right:1.5mm}
"""

LEVEL = {'EASY': ('easy', '●'), 'MEDIUM': ('medium', '●●'), 'HARD': ('hard', '●●●'),
         'GOING FURTHER': ('further', '')}


def F(a, b, big=False):
    return f'<span class="fr{" big" if big else ""}"><span>{a}</span><span>{b}</span></span>'


def page(inner, footer_text, pno, cls=''):
    return (f'<div class="page {cls}">{inner}'
            f'<div class="footer"><span>{footer_text}</span><span class="pno">{pno}</span></div></div>')


def banner(num, title, sub, level=None, alt=False):
    lv = ''
    if level:
        cls, dots = LEVEL[level]
        lv = f'<span class="lvl {cls}">{level}' + (f'<span class="d">{dots}</span>' if dots else '') + '</span>'
    return (f'<div class="banner{" b2" if alt else ""}"><span class="num">{num}</span><span class="title">{title}</span>'
            f'<span class="sub">{sub}</span>{lv}</div>')


def li_box(intention, criteria):
    sc = ''.join(f'<div class="row"><span><i>I can</i> {c}</span><span class="tl"><i></i><i></i><i></i></span></div>' for c in criteria)
    return (f'<div class="li2"><div><span class="h">LEARNING INTENTION</span><i>We are learning to</i> {intention}</div>'
            f'<div><div class="sch"><span class="h">SUCCESS CRITERIA</span><span class="rate">rate yourself at the end: '
            f'<span class="tl"><i></i><i></i><i></i></span> not yet · getting there · got it</span></div>{sc}</div></div>')


def notes_box(content=None, height=42, mode='student'):
    """mode: student (blank dotted), teacher (filled + TEACHER COPY), selfstudy (filled, KEY IDEAS)."""
    if mode == 'student' or content is None:
        return (f'<div class="box notes"><div class="hd">NOTES <span class="note">copy what your teacher writes on the board</span>'
                f'<span class="right">Date <span class="dateln"></span></span></div>'
                f'<div class="body" style="height:{height}mm"></div></div>')
    if mode == 'teacher':
        return (f'<div class="box notes"><div class="hd">NOTES <span class="note">key ideas: students copy these into their booklet</span>'
                f'<span class="right"><span class="tc">TEACHER COPY</span></span></div>'
                f'<div class="body" style="height:{height}mm">{content}</div></div>')
    return (f'<div class="box notes"><div class="hd">KEY IDEAS <span class="note">read these carefully, then highlight the key words</span>'
            f'<span class="right"><span class="tc">SELF-STUDY</span></span></div>'
            f'<div class="body" style="height:{height}mm">{content}</div></div>')


def wedo(ex_label, instruction, parts, box_h=22, cols=4, worked=None,
         note='with your teacher: copy every step into the space', data=None):
    ps = ''
    for i, (cap, fig, txt) in enumerate(parts):
        letter = 'abcdefgh'[i]
        if worked:
            wb = f'<div class="wbox worked" style="min-height:{box_h}mm">{worked[i]}</div>'
        else:
            wb = f'<div class="wbox" style="min-height:{box_h}mm"></div>'
        ps += (f'<div class="part"><div class="lab"><span class="letter">{letter}</span>{cap}</div>'
               + (f'<div class="txt">{txt}</div>' if txt else '')
               + (f'<div class="fig">{fig}</div>' if fig else '')
               + wb + '</div>')
    if worked:
        note = 'worked examples: read each step, then cover it and try it yourself'
    return (f'<div class="wedo"><div class="hd">{"WORKED" if worked else "WE DO"} <span class="note" style="font-weight:300;letter-spacing:0">{note}</span></div>'
            f'<div class="ex"><span class="expill">{ex_label}</span>{instruction}</div>'
            + (f'<div class="exdata">{data}</div>' if data else '') +
            f'<div class="parts" style="grid-template-columns:repeat({cols},minmax(0,1fr))">{ps}</div></div>')


def lines(spec):
    return ''.join(f'<div class="ln"><span class="k">{k}</span><span class="v">{v}</span></div>' for k, v in spec)


def qcard(n, fig='', q='', ln=None, tag='', h=None, span=1, figtop=False):
    style = []
    if h:
        style.append(f'min-height:{h}mm')
    if span > 1:
        style.append(f'grid-column:span {span}')
    st = f' style="{";".join(style)}"' if style else ''
    if tag:
        cls = ' x' if tag.lower().startswith('ext') else ''
        tg = f'<span class="tag{cls}">{tag}</span>'
    else:
        tg = ''
    figcls = 'figt' if figtop else 'fig'
    body = (f'<div class="card"{st}><div class="top"><span class="qn">{n}</span>'
            + (f'<div class="q">{q}</div>' if q else '<div class="space"></div>') + tg + '</div>')
    if fig:
        body += f'<div class="{figcls}">{fig}</div>'
        if figtop:
            body += '<div class="space"></div>'
    else:
        body += '<div class="space"></div>'
    body += (lines(ln) if ln else '') + '</div>'
    return body


def round_hdr(n, text):
    return f'<div class="round"><span class="pill">ROUND {n}</span><span>{text}</span></div>'


def youdo(title, count, inner, kind='', label='YOU DO', grow=False):
    return (f'<div class="yd {kind}{" grow" if grow else ""}"><div class="tab"><span class="lb">✎&nbsp; {label}</span><span class="t">{title}</span></div>'
            f'<div class="cnt">{count}</div>{inner}</div>')


def remember(text):
    return f'<div class="rem"><b class="k">REMEMBER</b>{text}</div>'


def html_doc(pages, title='Booklet'):
    return (f'<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
