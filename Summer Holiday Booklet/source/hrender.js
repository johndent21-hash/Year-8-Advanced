const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + path.resolve(__dirname, 'holiday.html'));
  await p.waitForSelector('body[data-ready]'); await p.evaluate(() => document.fonts.ready);
  const rep = await p.evaluate(() => {
    const out = [];
    document.querySelectorAll('.page').forEach((pg, i) => {
      const inn = pg.querySelector('.inner'); if (inn && inn.scrollHeight > inn.clientHeight + 1) out.push(['page', i + 1, inn.scrollHeight - inn.clientHeight]);
      pg.querySelectorAll('.qc').forEach(q => {
        const wk = q.querySelector('.wk'); const h = wk.getBoundingClientRect().height / 96 * 25.4;
        if (q.scrollHeight > q.clientHeight + 1 || h < 6) out.push(['cell', i + 1, q.querySelector('.qn').innerText, 'work_mm', h.toFixed(1), 'over', q.scrollHeight - q.clientHeight]);
      });
      const ab = pg.querySelectorAll('.ablk'); ab.forEach(a => { if (a.scrollHeight > a.clientHeight + 1) out.push(['ans', i + 1]); });
    });
    // min working height per week page
    const mins = [];
    document.querySelectorAll('.week').forEach(pg => { let m = 999; pg.querySelectorAll('.qc .wk').forEach(w => m = Math.min(m, w.getBoundingClientRect().height / 96 * 25.4)); mins.push(m.toFixed(1)); });
    return { out, mins };
  });
  console.log(JSON.stringify(rep));
  await p.pdf({ path: path.resolve(__dirname, 'holiday.pdf'), preferCSSPageSize: true, printBackground: true });
  await b.close();
})();
