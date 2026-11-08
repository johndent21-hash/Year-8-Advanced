"""Fonts used by the booklets (not stored in the repo):
- Poppins (SIL OFL): `npm pack @fontsource/poppins`, then copy
  files/poppins-latin-{300,400,500,600,700}-normal.woff2 and
  poppins-latin-300-italic.woff2 into source/fonts/.
- TeX Gyre Pagella (GUST licence): `apt-get install fonts-texgyre`, then run this
  script to convert the CFF outlines to TrueType (Chromium embeds CFF fonts as
  large Type 3 fonts, TrueType keeps the PDFs small).
"""
import os
from fontTools.ttLib import TTFont, newTable
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen

SRC = '/usr/share/texmf/fonts/opentype/public/tex-gyre/'
os.makedirs('fonts', exist_ok=True)
for style in ['regular', 'bold', 'italic', 'bolditalic']:
    f = TTFont(SRC + f'texgyrepagella-{style}.otf')
    gs = f.getGlyphSet()
    glyf = newTable('glyf'); glyf.glyphs = {}; glyf.glyphOrder = f.getGlyphOrder()
    for name in f.getGlyphOrder():
        pen = TTGlyphPen(gs)
        gs[name].draw(Cu2QuPen(pen, 1.0, reverse_direction=True))
        glyf[name] = pen.glyph()
    f['glyf'] = glyf; f['loca'] = newTable('loca'); del f['CFF ']
    f['maxp'].tableVersion = 0x00010000
    for a in ['maxZones', 'maxTwilightPoints', 'maxStorage', 'maxFunctionDefs', 'maxInstructionDefs', 'maxStackElements',
              'maxSizeOfInstructions', 'maxComponentElements', 'maxPoints', 'maxContours', 'maxCompositePoints',
              'maxCompositeContours', 'maxComponentDepth']:
        setattr(f['maxp'], a, 0)
    f['maxp'].maxZones = 1
    f['head'].glyphDataFormat = 0
    f['post'].formatType = 2.0; f['post'].extraNames = []; f['post'].mapping = {}
    f.sfntVersion = '\x00\x01\x00\x00'
    f.save(f'fonts/pagella-{style}.ttf')
