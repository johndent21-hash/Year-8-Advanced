// usage: node render.js in.html out.pdf
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(process.argv[2]), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  // report any page whose content overflows its box (layout check)
  const over = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('.page').forEach((p, i) => {
      const pr = p.getBoundingClientRect();
      const foot = p.querySelector('.footer');
      const limit = foot ? foot.getBoundingClientRect().top - 2 : pr.bottom;
      let maxb = 0;
      p.querySelectorAll(':scope > *:not(.footer):not(.art):not(.credit):not(.lower)').forEach(e => { maxb = Math.max(maxb, e.getBoundingClientRect().bottom); });
      if (maxb > limit) out.push(`page ${i + 1}: content bottom ${(maxb - pr.top).toFixed(0)}px > limit ${(limit - pr.top).toFixed(0)}px`);
      p.querySelectorAll('.card').forEach(c => { if (c.scrollHeight > c.clientHeight + 2) out.push(`page ${i + 1}: card overflow ${c.innerText.slice(0, 40).replace(/\n/g, ' ')}`); });
    });
    return out;
  });
  if (over.length) console.log('LAYOUT WARNINGS:\n' + over.join('\n'));
  await page.pdf({ path: process.argv[3], preferCSSPageSize: true, printBackground: true });
  await browser.close();
  console.log('wrote ' + process.argv[3]);
})();
