const { chromium } = require('playwright');
(async () => {
  const [,, src, out] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + src, { waitUntil: 'load' });
  await page.waitForSelector('body[data-done="1"]', { timeout: 30000 });
  await page.evaluate(() => document.fonts.ready);
  // shrink question text a little in any column that is too full
  const fits = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('.qcol').forEach((col, i) => {
      let fs = 11.9;
      const bad = () => [...col.querySelectorAll('.card')].some(c => c.scrollHeight > c.clientHeight + 1) ||
                        [...col.querySelectorAll('.dots')].some(d => d.clientHeight < 22);
      while (bad() && fs > 10.6) { fs -= 0.15; col.querySelectorAll('.qt').forEach(q => q.style.fontSize = fs + 'px'); }
      if (fs < 11.9) out.push('col' + i + ' -> ' + fs.toFixed(2) + 'px');
    });
    return out;
  });
  if (fits.length) console.log('FIT: ' + fits.join(', '));
  // report any card whose content overflows
  const over = await page.evaluate(() => {
    const bad = [];
    document.querySelectorAll('.card, .hbox, .ans, .hiw, .grid').forEach((el, i) => {
      if (el.scrollHeight > el.clientHeight + 1) bad.push(el.className + ' #' + i + ' ' + el.scrollHeight + '>' + el.clientHeight + ' ' + el.innerText.slice(0, 50).replace(/\n/g, ' '));
    });
    document.querySelectorAll('.dots').forEach((el, i) => { if (el.clientHeight < 21) bad.push('dots#' + i + ' h=' + el.clientHeight + ' ' + el.parentElement.innerText.slice(0, 50).replace(/\n/g, ' ')); });
    return bad;
  });
  if (over.length) console.log('OVERFLOW:\n' + over.join('\n'));
  const raw = await page.evaluate(() => {
    const errs = document.querySelectorAll('.katex-error').length;
    const txt = document.body.innerText;
    const left = (txt.match(/\\\(|\\\)|\$/g) || []).length;
    return {errs, left, sample: (txt.match(/.{0,40}(\\\(|\\\)).{0,40}/) || [''])[0]};
  });
  console.log('KATEX errors=' + raw.errs + ' leftover-delims=' + raw.left + ' ' + raw.sample);
  await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true });
  await browser.close();
})();
