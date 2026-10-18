// Tek dosya site (site-tek/index.html) testi. Kullanım: NODE_PATH=$(npm root -g) node araclar/site/test-tek.js <url ya da file:///…/index.html>
const { chromium } = require('playwright');
const URL = process.argv[2];
let hata = 0; const not = (ok, m) => { console.log((ok ? 'TAMAM ' : 'HATA  ') + m); if (!ok) hata++; };
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const log = []; pg.on('pageerror', e => log.push(e.message)); pg.on('console', m => { if (m.type() === 'error' && !/fonts\.g|net::/.test(m.text())) log.push(m.text()); });
  const git = async h => { await pg.evaluate(x => { location.hash = x; }, h); await pg.waitForTimeout(350); };
  await pg.goto(URL); await pg.waitForTimeout(1200); await pg.evaluate(() => localStorage.clear());
  // Bütün sayfalar
  const adlar = await pg.evaluate(() => Object.keys(AYLUNA_SAYFALAR));
  for (const a of adlar) {
    await git(a === 'index' ? '' : a);
    const r = await pg.evaluate(() => ({ n: document.querySelectorAll('#kok *').length, t: document.documentElement.scrollWidth - innerWidth, s: document.getElementById('kok').getAttribute('data-sayfa') }));
    not(r.n > 10 && r.t <= 1, `#${a}: ${r.n} öğe, tür ${r.s}, taşma ${r.t}`);
  }
  // Ana sayfa kart → LunaDream → sepet → ödeme → teşekkür
  await git(''); await pg.locator('a.uk').first().click(); await pg.waitForTimeout(500);
  const h1 = await pg.evaluate(() => location.hash);
  not(h1 === '#lunadream-gece-lambasi', 'kart → ' + h1);
  await pg.locator('.btn-on').first().click(); await pg.waitForTimeout(600);
  not(await pg.evaluate(() => location.hash) === '#sepet' && (await pg.locator('.urun b').first().textContent()).includes('LunaDream'), 'Güvenli Ödeme → #sepet, LunaDream satırı');
  await pg.locator('.teklif').nth(1).click(); await pg.waitForTimeout(200);
  await pg.locator('.btn1').click(); await pg.waitForTimeout(500);
  not(await pg.evaluate(() => location.hash) === '#odeme', 'sepet → #odeme');
  for (const [k, v] of [['eposta', 'a@b.co'], ['ad', 'Ayşe'], ['soyad', 'Y'], ['adres', 'Moda Mah. Bahariye Cad. No 10'], ['il', 'İstanbul'], ['ilce', 'Kadıköy'], ['tel', '05321112233']]) await pg.fill(`input[name=${k}]`, v);
  await pg.locator('.btn-l[type=submit]').click(); await pg.waitForTimeout(600);
  not(await pg.evaluate(() => location.hash) === '#siparis-alindi' && (await pg.locator('.tamam h1').textContent()).includes('alındı'), 'ödeme → #siparis-alindi');
  // Kapıda
  await git('galayx-usb-projektor'); await pg.locator('#siparis .btn2').click(); await pg.waitForTimeout(500);
  not(await pg.locator('.ay-kf.on').count() === 1, 'USB kapıda formu açıldı');
  await pg.fill('.ay-kf input[name=ad]', 'Mehmet'); await pg.fill('.ay-kf input[name=tel]', '05321112233'); await pg.selectOption('.ay-kf select[name=il]', 'Ankara');
  await pg.fill('.ay-kf input[name=ilce]', 'Çankaya'); await pg.fill('.ay-kf textarea[name=adres]', 'Kızılay Mah. Atatürk Bulv. No 5');
  await pg.locator('.ay-kf button[type=submit]').click(); await pg.waitForTimeout(600);
  not(await pg.evaluate(() => location.hash) === '#siparis-alindi' && (await pg.locator('.tamam').textContent()).includes('kapına gelince'), 'kapıda → teşekkür');
  // Menü, arama, sayfa içi çapa, sepet kapat
  await git(''); await pg.locator('[aria-label="Menü"]').first().click(); await pg.waitForTimeout(300);
  await pg.locator('.ay-menu a', { hasText: 'AyFeneri' }).click(); await pg.waitForTimeout(500);
  not(await pg.evaluate(() => location.hash) === '#lamba', 'menü → #lamba');
  await git('arama?q=Projektör'); not(await pg.locator('.izg a').count() === 3, 'arama Projektör 3 sonuç');
  await git('lunadream-gece-lambasi');
  const capa = pg.locator('a[href="#diskler"]').first();
  if (await capa.count()) { await capa.click(); await pg.waitForTimeout(500); not(await pg.evaluate(() => location.hash) === '#lunadream-gece-lambasi' && await pg.evaluate(() => scrollY) > 300, 'sayfa içi çapa kaydırır, sayfa değişmez'); }
  await git('lamba'); await pg.locator('#siparis .btn1').first().click(); await pg.waitForTimeout(500);
  await pg.locator('[aria-label="Sepeti kapat"]').click(); await pg.waitForTimeout(500);
  not(await pg.evaluate(() => location.hash) === '#lamba', 'sepet kapat → geri (#lamba)');
  not(await pg.locator('[data-ay-adet="1"]').count() >= 1, 'rozet 1');
  console.log(log.length ? 'KONSOL:\n' + log.join('\n') : 'konsol hatası yok');
  console.log(hata ? hata + ' HATA' : 'HEPSİ TAMAM');
  await b.close(); process.exit(hata || log.length ? 1 : 0);
})();
