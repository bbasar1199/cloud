// Ayluna teması · Shopify benzetiminde uçtan uca deneme. Önce: BENZETIM_FIYAT='{"sunset-lamba":64900,"ask-saati":74900}' python3 araclar/tema/benzetim.py 8790
// Çalıştır: NODE_PATH=$(npm root -g) node araclar/tema/test-tema.js
const { chromium } = require('playwright');
const K = process.env.TEMA_URL || 'http://127.0.0.1:8790';
let hata = 0; const not = (ok, m) => { console.log((ok ? 'TAMAM ' : 'HATA  ') + m); if (!ok) hata++; };
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const pg = await ctx.newPage(); const log = [];
  pg.on('pageerror', e => log.push('pageerror: ' + e.message));
  pg.on('console', m => { if (m.type() === 'error' && !/fonts\.g|net::ERR|Failed to load resource/.test(m.text())) log.push(m.text()); });
  const sepet = () => pg.evaluate(() => fetch('/cart.js').then(r => r.json()));
  await pg.evaluate(() => 0).catch(() => {});
  await pg.goto(K + '/'); await pg.waitForTimeout(800);
  await pg.evaluate(() => fetch('/cart/clear.js', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: '{}' }));

  // 1) Bütün tasarım sayfaları açılıyor
  for (const y of ['/', '/collections/all', '/cart', '/search', '/products/lunadream-gece-lambasi', '/products/galayx-usb-projektor', '/products/lamba',
    '/products/ayluna-galaksi-night-projektor', '/products/sunset-lamba', '/products/egitici-akilli-cizim-tahtasi', '/pages/iletisim', '/pages/iade', '/pages/kvkk', '/olmayan']) {
    await pg.goto(K + y); await pg.waitForTimeout(500);
    const n = await pg.evaluate(() => document.querySelector('#kok') ? document.querySelector('#kok').childElementCount : -1);
    not(n > 0, 'açıldı ' + y + ' (' + n + ' öğe)');
  }

  // 2) Canlı fiyat: benzetimde Kum Saati 749 TL, Sunset 649 TL (tasarımda 799 ve 699) → ana sayfa ve koleksiyon kartı canlı fiyatı gösterir
  await pg.goto(K + '/'); await pg.waitForTimeout(700);
  not((await pg.locator('.uk[data-h="ask-saati"] .f strong').textContent().catch(() => '')).includes('749'), 'ana sayfa kartında canlı fiyat (Kum Saati ₺749)');
  await pg.goto(K + '/collections/all'); await pg.waitForTimeout(700);
  not((await pg.locator('.uk', { hasText: 'Sunset' }).first().textContent()).includes('649'), 'koleksiyonda canlı fiyat');

  // 3) Adresler: masaüstü/menü bağlantıları mağaza adresleri
  await pg.goto(K + '/'); await pg.waitForTimeout(500);
  await pg.locator('#kok [aria-label="Menü"]').first().click(); await pg.waitForTimeout(400);
  const menu = await pg.evaluate(() => [...document.querySelectorAll('.ay-menu a')].map(a => a.getAttribute('href')));
  not(menu.includes('/collections/all') && menu.includes('/products/lunadream-gece-lambasi') && menu.includes('/apps/track123'), 'menü adresleri: ' + menu.slice(0, 4).join(' '));
  await pg.keyboard.press('Escape');

  // 4) LunaDream: 2 Adet, 1. lamba Kız, 2. lamba Erkek → Güvenli Ödeme → Shopify sepetinde iki varyant, /cart
  await pg.goto(K + '/products/lunadream-gece-lambasi'); await pg.waitForTimeout(700);
  const kalem = await pg.evaluate(() => { window.__istek = []; const f = window.fetch; window.fetch = function (u, o) { if (o && o.body && /cart\/add/.test(u)) window.__istek.push(JSON.parse(o.body)); return f.apply(this, arguments); }; });
  await pg.locator('#siparis .pk button, #siparis .paket button, #siparis [class*="pk"] button').filter({ hasText: '2 Adet' }).first().click().catch(() => {});
  await pg.waitForTimeout(300);
  const l2 = pg.locator('#siparis button', { hasText: 'Erkek' }).last(); await l2.click().catch(() => {}); await pg.waitForTimeout(300);
  await pg.locator('#siparis .btn-on').first().click();
  await pg.waitForURL(/\/cart$/, { timeout: 6000 }).catch(() => {});
  let c = await sepet();
  not(pg.url().endsWith('/cart'), 'Güvenli Ödeme → /cart');
  const vt = c.items.map(i => i.variant_title + '×' + i.quantity).sort().join(', ');
  not(c.item_count === 2 && c.items.length === 2 && /Erkek/.test(vt) && /Kız/.test(vt), 'sepette Kız + Erkek (' + vt + ')');
  not(c.items.every(i => i.properties && i.properties._paket === '2'), 'satırlarda _paket özelliği');
  await pg.waitForTimeout(600);
  const satir = await pg.locator('#kok .urun').count();
  not(satir === 2, 'sepet sayfasında 2 satır (' + satir + ')');

  // 5) Sepet: adet arttır, teklif ekle (mağaza fiyatıyla), sil
  await pg.locator('#kok .adet button[aria-label="Arttır"]').first().click(); await pg.waitForTimeout(700);
  c = await sepet(); not(c.item_count === 3, 'adet arttı (toplam ' + c.item_count + ')');
  const tek = pg.locator('#kok .teklif').first();
  const tekMetin = await tek.textContent().catch(() => '');
  not(!/Mağazada/.test(tekMetin), 'teklifte "Mağazada" indirimi yazmıyor (indirim tanımlı değil)');
  await tek.click(); await pg.waitForTimeout(700);
  c = await sepet(); not(c.items.some(i => i.properties && i.properties._ek), 'teklif sepete eklendi (_ek)');
  not(await pg.locator('#kok .teklif.on').count() === 1, 'teklif seçili görünüyor');
  not(await pg.locator('#kok .tes').count() === 0, 'kargo seçimi gizli (ödeme adımında seçilir)');
  const rozet = await pg.evaluate(() => document.querySelector('[data-ay-adet]') && document.querySelector('[data-ay-adet]').getAttribute('data-ay-adet'));
  not(rozet === String(c.item_count), 'sepet rozeti Shopify adedi (' + rozet + ')');
  await pg.locator('#kok .sil').first().click(); await pg.waitForTimeout(700);
  c = await sepet(); not(c.items.filter(i => !(i.properties || {})._ek).length === 1, 'satır silindi');

  // 6) Ödeme: kart → /checkout
  const odeme = await pg.evaluate(() => { let git = null; const s = Object.getOwnPropertyDescriptor(window.Location.prototype, 'href'); return null; });
  await pg.route('**/checkout', r => r.fulfill({ status: 200, body: 'checkout' }));
  await pg.locator('#kok .s-sag .btn1, #kok .btn1').filter({ hasText: 'Güvenli Ödeme' }).first().click(); await pg.waitForTimeout(800);
  not(pg.url().endsWith('/checkout'), 'Güvenli Ödeme ile Öde → /checkout');

  // 7) Kapıda: EasySell yokken sepete düşer; EasySell varken sayfa kalır ve gizli form seçime eşit
  await pg.goto(K + '/products/galayx-usb-projektor'); await pg.waitForTimeout(700);
  not(await pg.locator('#siparis .btn2[data-ay-kapida]').count() === 1, 'Kapıda düğmesi EasySell seçicisiyle işaretli [data-ay-kapida]');
  await pg.evaluate(() => { window.EASYSELL_CONFIG = {}; window.__es = 0; document.addEventListener('click', e => { if (e.target.closest('[data-ay-kapida]')) window.__es++; }); });
  await pg.locator('#siparis .btn2').click(); await pg.waitForTimeout(500);
  const form = await pg.evaluate(() => { const f = document.querySelector('form[data-ay-urun-formu]'); return { id: f.querySelector('[name=id]').value, q: f.querySelector('[name=quantity]').value }; });
  not(pg.url().includes('/products/galayx-usb-projektor') && await pg.evaluate(() => window.__es) === 1, 'EasySell varken Kapıda formu EasySell açar (sayfa kalır)');
  not(/^\d+$/.test(form.id) && form.q === '2', 'gizli ürün formu seçime eşit (varyant ' + form.id + ', adet ' + form.q + ')');
  await pg.goto(K + '/products/lamba'); await pg.waitForTimeout(700);
  await pg.locator('#siparis .btn2').click(); await pg.waitForURL(/\/cart$/, { timeout: 5000 }).catch(() => {});
  not(pg.url().endsWith('/cart'), 'EasySell yokken Kapıda → sepet');

  // 8) Koleksiyonda Sepete ekle
  await pg.goto(K + '/collections/all'); await pg.waitForTimeout(600);
  const once = (await sepet()).item_count;
  await pg.locator('.uk', { hasText: 'Kum Saati' }).locator('button').click(); await pg.waitForTimeout(800);
  not((await sepet()).item_count === once + 1, 'koleksiyondan sepete eklendi');

  // 9) Formlar: iletişim ve bülten Shopify'a gider
  await pg.goto(K + '/pages/iletisim'); await pg.waitForTimeout(600);
  const f = pg.locator('#kok form').filter({ has: pg.locator('textarea') }).first();
  await f.locator('input').first().fill('Ayşe Yılmaz'); await f.locator('input[type=email]').fill('ayse@ornek.com');
  if (await f.locator('input[type=tel]').count()) await f.locator('input[type=tel]').fill('05321112233');
  await f.locator('textarea').fill('Siparişim nerede?');
  if (await f.locator('input[type=checkbox]').count()) await f.locator('input[type=checkbox]').check();
  await f.locator('button[type=submit], button').last().click(); await pg.waitForTimeout(800);
  const gonderilen = await pg.evaluate(() => fetch('/__gonderilen').then(r => r.json()));
  not(gonderilen.some(g => /form_type/.test(g) && /contact/.test(g) && /ayse%40ornek|ayse@ornek/.test(g)), 'iletişim formu /contact\'a gönderildi');

  // 10) Masaüstü: üst menü mağaza adresleri, satın alma çubuğu, fiyat uyarısı konsolda
  const m = await b.newPage({ viewport: { width: 1440, height: 900 } }); const uyari = [];
  m.on('console', x => { if (x.type() === 'warning') uyari.push(x.text()); }); m.on('pageerror', e => log.push('masaüstü pageerror: ' + e.message));
  await m.goto(K + '/products/sunset-lamba'); await m.waitForTimeout(800);
  const nav = await m.evaluate(() => [...document.querySelectorAll('.ay-masa nav a')].map(a => a.getAttribute('href')));
  not(nav[0] === '/collections/all' && nav.includes('/products/lamba'), 'masaüstü menü adresleri');
  not(uyari.some(u => /tasarımdaki fiyat/.test(u)), 'tasarım fiyatı ≠ mağaza fiyatı uyarısı (Sunset)');
  await m.goto(K + '/products/lunadream-gece-lambasi'); await m.waitForTimeout(800);
  await m.evaluate(() => window.scrollTo(0, 2400)); await m.waitForTimeout(800);
  not(await m.locator('.ay-al.on').count() === 1 && await m.locator('.ay-al [data-kp][data-ay-kapida]').count() === 1, 'masaüstü satın alma çubuğu (Kapıda EasySell seçicili)');

  console.log('\n' + (log.length ? log.join('\n') : 'konsol hatası yok'));
  console.log(hata ? `\n${hata} HATA` : '\nHEPSİ TAMAM');
  await b.close(); process.exit(hata || log.length ? 1 : 0);
})();
