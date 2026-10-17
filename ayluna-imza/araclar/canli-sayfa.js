const { chromium } = require('playwright');
const out = process.argv[2], url = process.argv[3];
(async () => {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY } });
  const pg = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1' });
  await pg.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await pg.waitForTimeout(8000);
  for (let y = 0; y < 3000; y += 400) { await pg.evaluate(v => window.scrollTo(0, v), y); await pg.waitForTimeout(400); }
  await pg.evaluate(() => window.scrollTo(0, 0)); await pg.waitForTimeout(1500);
  const H = await pg.evaluate(() => document.documentElement.scrollHeight);
  console.log('H', H);
  for (let i = 0; i < Math.min(8, Math.ceil(H / 1200)); i++) {
    await pg.screenshot({ path: `${out}/c${i}.png`, clip: { x: 0, y: i * 1200, width: 390, height: Math.min(1200, H - i * 1200) }, fullPage: true });
  }
  const txt = await pg.evaluate(() => {
    const pick = s => Array.from(document.querySelectorAll(s)).map(e => e.innerText.trim()).filter(Boolean).slice(0, 5);
    return { forms: pick('form'), bundleish: pick('[class*="bundle" i],[class*="offer" i],[class*="quantity-break" i],[id*="releasit" i],[class*="releasit" i],[class*="easysell" i],[class*="cod" i]') };
  });
  require('fs').writeFileSync(`${out}/metin.json`, JSON.stringify(txt, null, 2));
  await b.close();
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
