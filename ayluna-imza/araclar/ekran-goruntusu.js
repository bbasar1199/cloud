const { chromium } = require('playwright');
(async () => {
  const out = process.argv[2] || 'ekran'; require('fs').mkdirSync(out,{recursive:true}); const url = 'file://' + require('path').resolve(__dirname, '../onizleme/' + (process.argv[3] || 'index.html'));
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
  const errs=[]; pg.on('pageerror', e => errs.push(e.message)); pg.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
  await pg.goto(url); await pg.waitForTimeout(4200);
  const H = await pg.evaluate(() => document.documentElement.scrollHeight);
  let y = 0, i = 0;
  while (y < H) { await pg.evaluate(v => window.scrollTo(0, v), y); await pg.waitForTimeout(700); await pg.screenshot({ path: `${out}/s${String(i).padStart(2,'0')}.png` }); i++; y += 760; }
  console.log('height', H, 'shots', i, 'errors', JSON.stringify(errs));
  await b.close();
})();
