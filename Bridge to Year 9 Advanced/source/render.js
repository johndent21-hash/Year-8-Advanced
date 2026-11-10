const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const which = process.argv[2] || 'student';
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(__dirname, which + '.html'));
  await page.waitForSelector('body[data-ready]');
  await page.evaluate(() => document.fonts.ready);
  if (which === 'student') {
    const rep = await page.evaluate(() => {
      document.body.classList.add('measure');
      const out = [];
      document.querySelectorAll('.page').forEach((pg, i) => {
        const inner = pg.querySelector('.inner'); if (!inner) return;
        const ib = inner.getBoundingClientRect();
        const last = inner.lastElementChild.getBoundingClientRect();
        out.push({ p: i + 1, over: inner.scrollHeight - inner.clientHeight, slack_mm: ((ib.bottom - last.bottom) / 96 * 25.4).toFixed(1) });
      });
      // horizontal overflow of cells
      const wide = [];
      document.querySelectorAll('.cell, .lcell, .tpart').forEach(c => { if (c.scrollWidth > c.clientWidth + 1) wide.push(c.innerText.slice(0, 40)); });
      document.body.classList.remove('measure');
      return { pages: out, wide };
    });
    console.log(JSON.stringify(rep));
  }
  await page.pdf({ path: path.resolve(__dirname, which + '.pdf'), preferCSSPageSize: true, printBackground: true,
    displayHeaderFooter: which === 'teacher',
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:7pt;font-family:InterW,Inter;color:#5b6475;width:100%;padding:0 11mm;display:flex;justify-content:space-between"><span>Bridge to Year 9 Advanced · Teacher answers</span><span class="pageNumber"></span></div>' });
  await browser.close();
})();
