"""Shrink a Chromium PDF: round content-stream coordinates (device units are
1/300 inch, so 0.1 unit is invisible), then rewrite with maximum compression."""
import re, sys, pikepdf

NUM = re.compile(rb'(?<![\w.<])(-?\d*\.\d{2,})(?![\w.])')


def _round(m):
    raw = m.group(1)
    v = float(raw)
    a = abs(v)
    if a < 10:
        return raw  # scale factors, line widths, small offsets: leave exact
    dp = 1 if a >= 100 else 2
    s = ('%.*f' % (dp, v)).rstrip('0').rstrip('.')
    return (s if s not in ('-0', '') else '0').encode()


def shrink(src, dst):
    pdf = pikepdf.open(src)
    seen = set()
    for page in pdf.pages:
        page.contents_coalesce()
        c = page.obj['/Contents']
        if c.objgen in seen:
            continue
        seen.add(c.objgen)
        data = c.read_bytes()
        c.write(NUM.sub(_round, data))
    for obj in pdf.objects:
        if isinstance(obj, pikepdf.Stream) and obj.get('/Subtype') == '/Form' and obj.objgen not in seen:
            seen.add(obj.objgen)
            try:
                obj.write(NUM.sub(_round, obj.read_bytes()))
            except Exception:
                pass
    pdf.remove_unreferenced_resources()
    pdf.save(dst, compress_streams=True, recompress_flate=True,
             object_stream_mode=pikepdf.ObjectStreamMode.generate)


if __name__ == '__main__':
    shrink(sys.argv[1], sys.argv[2])
