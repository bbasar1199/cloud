// Ayluna teması · Shopify benzetiminde uçtan uca deneme. Önce: BENZETIM_FIYAT='{"sunset-lamba":64900,"ask-saati":74900}'
//   BENZETIM_ELLE='{"galayx-usb-projektor":{"dun":7,"kd":0}}' BENZETIM_LOOX=galayx-usb-projektor BENZETIM_VARSAYILAN=ayluna-galaksi-night-projektor
//   BENZETIM_MEDYA=sunset-lamba BENZETIM_VIDEO=lunadream-gece-lambasi python3 araclar/tema/benzetim.py 8790
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
    const n = await pg.evaluate(() => [...document.querySelectorAll('.ay-kok')].reduce((t, k) => t + k.childElementCount, 0) || -1);
    not(n > 0, 'açıldı ' + y + ' (' + n + ' öğe)');
  }

  // 2) Canlı fiyat: benzetimde Kum Saati 749 TL, Sunset 649 TL (tasarımda 799 ve 699) → ana sayfa ve koleksiyon kartı canlı fiyatı gösterir
  await pg.goto(K + '/'); await pg.waitForTimeout(700);
  not((await pg.locator('.uk[data-h="ask-saati"] .f strong').textContent().catch(() => '')).includes('749'), 'ana sayfa kartında canlı fiyat (Kum Saati ₺749)');
  await pg.goto(K + '/collections/all'); await pg.waitForTimeout(700);
  not((await pg.locator('.uk', { hasText: 'Sunset' }).first().textContent()).includes('649'), 'koleksiyonda canlı fiyat');

  // 3) Adresler: masaüstü/menü bağlantıları mağaza adresleri
  await pg.goto(K + '/'); await pg.waitForTimeout(500);
  await pg.locator('.ay-kok [aria-label="Menü"]').first().click(); await pg.waitForTimeout(400);
  const menu = await pg.evaluate(() => [...document.querySelectorAll('.ay-menu a')].map(a => a.getAttribute('href')));
  not(menu.includes('/collections/all') && menu.includes('/products/lunadream-gece-lambasi') && menu.includes('/apps/track123'), 'menü adresleri: ' + menu.slice(0, 4).join(' '));
  await pg.keyboard.press('Escape');

  // 4) LunaDream: açılışta paket seçili değil (19 Eki); 2 Adet, 1. lamba Kız, 2. lamba Erkek → Kaching'de 2'li seçilir →
  //    Güvenli Ödeme → sepette iki varyant, ikisinde de Kaching indirim özelliği, istek kaching_bundles=true ile
  await pg.goto(K + '/products/lunadream-gece-lambasi'); await pg.waitForTimeout(2200);
  not(await pg.locator('#siparis [aria-pressed="true"]').filter({ hasText: 'Adet' }).count() === 0, 'açılışta paket seçili değil');
  not(await pg.evaluate(() => !!document.querySelector('kaching-bundle kaching-bundles-block') && !document.querySelector('kaching-bundle input:checked')), 'Kaching kutusu kuruldu, paketi seçili değil');
  not(await pg.evaluate(() => document.querySelectorAll('#siparis .btn-kp, #siparis .btn2').length === 0 && !!document.querySelector('#siparis [data-ay-dis]')), 'Kapıda düğmesi yok (27 Eki), uygulama yuvası yerinde');
  const kalem = await pg.evaluate(() => { window.__istek = []; const f = window.fetch; window.fetch = function (u, o) { if (o && o.body && /cart\/add/.test(u)) window.__istek.push(JSON.parse(o.body)); return f.apply(this, arguments); }; });
  await pg.locator('#siparis .pk button, #siparis .paket button, #siparis [class*="pk"] button').filter({ hasText: '2 Adet' }).first().click().catch(() => {});
  await pg.waitForTimeout(300);
  const l2 = pg.locator('#siparis button', { hasText: 'Erkek' }).last(); await l2.click().catch(() => {}); await pg.waitForTimeout(1300);
  not(await pg.evaluate(() => { const r = document.querySelector('kaching-bundle input:checked'); return r && r.value; }) === 'bar-2', 'tasarımda 2 Adet seçilince Kaching\'de 2\'li seçildi');
  await pg.locator('#siparis .btn-on').first().click();
  await pg.waitForURL(/\/cart$/, { timeout: 6000 }).catch(() => {});
  let c = await sepet();
  not(pg.url().endsWith('/cart'), 'Güvenli Ödeme → /cart');
  const vt = c.items.map(i => i.variant_title + '×' + i.quantity).sort().join(', ');
  not(c.item_count === 2 && c.items.length === 2 && /Erkek/.test(vt) && /Kız/.test(vt), 'sepette Kız + Erkek (' + vt + ')');
  not(c.items.every(i => i.properties && i.properties._paket === '2'), 'satırlarda _paket özelliği');
  not(c.items.every(i => i.properties && /"bid":"bar-2"/.test(i.properties.__kaching_bundles || '')), 'iki satırda da Kaching indirim özelliği (__kaching_bundles)');
  not((await pg.evaluate(() => fetch('/__istek').then(r => r.json()))).some(u => /kaching_bundles=true/.test(u)), 'sepete ekleme Kaching\'in değiştirmesine kapalı (kaching_bundles=true)');
  await pg.waitForTimeout(600);
  const satir = await pg.locator('.ay-kok .urun').count();
  not(satir === 2, 'sepet sayfasında 2 satır (' + satir + ')');

  // 5) Sepet: adet arttır, teklif ekle (mağaza fiyatıyla), sil
  await pg.locator('.ay-kok .adet button[aria-label="Arttır"]').first().click(); await pg.waitForTimeout(700);
  c = await sepet(); not(c.item_count === 3, 'adet arttı (toplam ' + c.item_count + ')');
  const tek = pg.locator('.ay-kok .teklif').first();
  const tekMetin = await tek.textContent().catch(() => '');
  not(!/Mağazada/.test(tekMetin), 'teklifte "Mağazada" indirimi yazmıyor (indirim tanımlı değil)');
  await tek.click(); await pg.waitForTimeout(700);
  c = await sepet(); not(c.items.some(i => i.properties && i.properties._ek), 'teklif sepete eklendi (_ek)');
  not(await pg.locator('.ay-kok .teklif.on').count() === 1, 'teklif seçili görünüyor');
  not(await pg.locator('.ay-kok .tes').count() === 0, 'kargo seçimi gizli (ödeme adımında seçilir)');
  const rozet = await pg.evaluate(() => document.querySelector('[data-ay-adet]') && document.querySelector('[data-ay-adet]').getAttribute('data-ay-adet'));
  not(rozet === String(c.item_count), 'sepet rozeti Shopify adedi (' + rozet + ')');
  await pg.locator('.ay-kok .sil').first().click(); await pg.waitForTimeout(700);
  c = await sepet(); not(c.items.filter(i => !(i.properties || {})._ek).length === 1, 'satır silindi');

  // 6) Ödeme: kart → /checkout. Sepette kapıda düğmesi ve notu yok (kapıda ödeme kaldırıldı, 27 Eki)
  not(await pg.evaluate(() => !/kapıda/i.test(document.querySelector('.ay-kok').innerText)), 'sepette kapıda yok');
  const odeme = await pg.evaluate(() => { let git = null; const s = Object.getOwnPropertyDescriptor(window.Location.prototype, 'href'); return null; });
  await pg.route('**/checkout', r => r.fulfill({ status: 200, body: 'checkout' }));
  await pg.locator('.ay-kok .s-sag .btn1, .ay-kok .btn1').filter({ hasText: 'Güvenli Ödeme' }).first().click(); await pg.waitForTimeout(800);
  not(pg.url().endsWith('/checkout'), 'Güvenli Ödeme ile Öde → /checkout');

  // 7) Kapıda ödeme yok (27 Eki). Bölüme eklenen uygulama düğmesi sayfa yeniden çizilince yuvada kalır; gizli ürün formu seçime eşit
  await pg.goto(K + '/products/galayx-usb-projektor'); await pg.waitForTimeout(2200);
  not(await pg.evaluate(() => document.querySelectorAll('#siparis .btn2').length === 0), 'USB: Kapıda düğmesi yok');
  await pg.evaluate(() => { const b = document.createElement('button'); b.className = 'es-popup-button'; b.textContent = 'Kapıda Ödeme ile Sipariş Ver'; document.querySelector('easysell-form').after(b); });
  await pg.locator('#siparis button', { hasText: '2 Adet' }).first().click(); await pg.waitForTimeout(1300);
  const form = await pg.evaluate(() => { const f = document.querySelector('form[data-ay-urun-formu]'); return { id: f.querySelector('[name=id]').value, q: f.querySelector('[name=quantity]').value, es: !!document.querySelector('#siparis [data-ay-dis] .es-popup-button'), kb: (document.querySelector('kaching-bundle input:checked') || {}).value }; });
  not(form.es, 'uygulama düğmesi yeniden çizimden sonra yuvada');
  not(/^\d+$/.test(form.id) && form.q === '2' && form.kb === 'bar-2', 'gizli ürün formu ve Kaching seçime eşit (varyant ' + form.id + ', adet ' + form.q + ', Kaching ' + form.kb + ')');
  await pg.goto(K + '/products/lamba'); await pg.waitForTimeout(2200);
  not(await pg.evaluate(() => document.querySelectorAll('#siparis .btn2').length === 0 && !document.querySelector('#siparis [aria-pressed="true"]')), 'AyFeneri: Kapıda yok, paket seçili değil');

  // 7b) Ürün sayfası blok blok (28 Eki): bütün ürünler varsayılan şablonda, her özel ürünün kendi sayfa bölümü, parçalar blok.
  // Loox kendi kutusunda (#looxReviews) tasarımın yorum bölümünde, blok eklemeden; yer tutucu yazı yok; kutu yeniden çizimde silinmez.
  // Dün sayısı ürün alanından, 0 olan stok kurdelesi gizli.
  await pg.goto(K + '/products/galayx-usb-projektor'); await pg.waitForTimeout(2200);
  const yk = await pg.evaluate(() => { const l = document.querySelector('#looxReviews .loox-benzetim'), s = document.querySelector('.ay-kok .stok-kd');
    const b = [...document.querySelectorAll('.ay-kok h2')].find(h => /Alanlar ne diyor/.test(h.textContent));
    return { loox: !!l && l.getBoundingClientRect().height > 0, sira: !!(l && b && (b.compareDocumentPosition(l) & Node.DOCUMENT_POSITION_FOLLOWING)),
      yer: /\[Loox/.test(document.body.innerText), blok: document.querySelectorAll('.ay-blok').length, kok: [...document.querySelectorAll('.ay-kok')].filter(k => k.childElementCount).length,
      bolum: document.querySelectorAll('.shopify-section').length, dun: /Dün 7 kişi/.test(document.querySelector('.ay-kok .dun').textContent), kd: !!s && getComputedStyle(s).display === 'none' }; });
  await pg.waitForTimeout(1500);
  const yk2 = await pg.evaluate(() => !!document.querySelector('#looxReviews .loox-benzetim') && /Dün 7 kişi/.test(document.querySelector('.ay-kok .dun').textContent));
  not(yk.loox && yk.sira && !yk.yer && yk.blok === 16 && yk.kok === 16 && yk.bolum === 5 && yk.dun && yk.kd && yk2, 'USB: 16 blok, Loox yorum bölümünde kendiliğinden, yer tutucu yok, Dün ürün alanından, 0 stok gizli ' + JSON.stringify(yk) + ' ' + yk2);
  // Yapışkan çubuk: paketler ve ana düğme ekrandayken çekilir, sonra geri gelir; 60 px
  const yp = await pg.evaluate(async () => { const y = document.querySelector('.ay-kok .yapis'), d = () => y.hasAttribute('data-ay-cekil');
    scrollTo(0, 0); await new Promise(r => setTimeout(r, 300)); const ust = d();
    const p = document.querySelector('.ay-kok .urun-ust .pk'); scrollTo(0, p.getBoundingClientRect().top + scrollY - 200); await new Promise(r => setTimeout(r, 400)); const paket = d();
    scrollTo(0, document.documentElement.scrollHeight * .6); await new Promise(r => setTimeout(r, 400)); const asagi = d();
    return { ust, paket, asagi, h: Math.round(y.getBoundingClientRect().height) }; });
  not(!yp.ust && yp.paket && !yp.asagi && yp.h === 60, 'yapışkan çubuk 60 px, paket alanında çekilir ' + JSON.stringify(yp));
  // LunaDream: video bölümü ürünün Shopify videosuyla çıkar, dokununca sesli oynar; [video] etiketi yok; Loox "Aileler ne diyor?" altında
  await pg.goto(K + '/products/lunadream-gece-lambasi'); await pg.waitForTimeout(2200);
  not(await pg.evaluate(() => /Dün 62 kişi/.test(document.querySelector('.ay-kok .dun').textContent)), 'LunaDream: ürün alanı boşsa tasarımdaki Dün sayısı kalır');
  const vd = await pg.evaluate(() => { const s = document.getElementById('videolar'), b = [...document.querySelectorAll('.ay-kok h2')].find(h => /Aileler/.test(h.textContent)), l = document.getElementById('looxReviews');
    return { n: document.querySelectorAll('#videolar .ay-vid video').length, gor: !!s && getComputedStyle(s).display !== 'none', etiket: /\[video\]/.test(document.body.innerText),
      loox: !!(l && b && (b.compareDocumentPosition(l) & Node.DOCUMENT_POSITION_FOLLOWING)), blok: document.querySelectorAll('.ay-blok').length }; });
  await pg.locator('#videolar .ay-vid').first().click({ force: true }).catch(() => {}); await pg.waitForTimeout(300);
  const ses = await pg.evaluate(() => { const v = document.querySelector('#videolar .ay-vid video'); return !!v && v.muted === false && v.hasAttribute('data-ay-oynuyor'); });
  not(vd.n === 1 && vd.gor && !vd.etiket && ses && vd.loox && vd.blok === 12, 'LunaDream: 12 blok, ürün videosu oynar (sesli), [video] etiketi yok, Loox yorumlarda ' + JSON.stringify(vd) + ' ' + ses);
  // Videosu olmayan ürün: video bölümü yok (sahte kapak gösterilmez) — AyFeneri'de video bölümü tasarımda yok; LunaDream'i medyasız denemek için
  // Galaksi Night ve sade ürün de kendi bloklarıyla açılır
  await pg.goto(K + '/products/ayluna-galaksi-night-projektor'); await pg.waitForTimeout(1500);
  not(await pg.evaluate(() => document.querySelectorAll('.ay-blok').length === 15 && !!document.querySelector('.ay-kok .urun-ust .btn1') && !document.getElementById('kok')), 'Galaksi Night: varsayılan şablonda kendi 15 bloğu');
  // Tema düzenleyici taklidi: blok ayarı değişince Shopify bölümü yeniden gönderir (shopify:section:load); sayfa yeni yazıyı çizer,
  // diğer bloklar ve sayfanın durumu bozulmaz. Blok silinince kalanlar çizilmeye devam eder.
  await pg.goto(K + '/products/galayx-usb-projektor'); await pg.waitForTimeout(1500);
  const duz = await pg.evaluate(async () => {
    const s = [...document.querySelectorAll('.shopify-section')].find(x => x.querySelector('.ay-blok'));
    const t = document.createElement('div'); t.innerHTML = s.innerHTML;
    const tpl = [...t.querySelectorAll('template.ay-parca')].find(x => /İçin rahat olsun/.test(x.innerHTML));
    tpl.innerHTML = tpl.innerHTML.replace('İçin rahat olsun', 'Gönül rahatlığıyla al'); t.querySelectorAll('.ay-kok').forEach(k => { k.innerHTML = ''; });
    s.innerHTML = t.innerHTML; s.dispatchEvent(new CustomEvent('shopify:section:load', { bubbles: true, detail: { sectionId: s.id } }));
    await new Promise(r => setTimeout(r, 400));
    const h = [...s.querySelectorAll('.ay-kok h2')].find(x => /Gönül rahatlığıyla/.test(x.textContent));
    const b = [...document.querySelectorAll('.ay-blok')].find(x => /Bu gece tavanda/.test(x.textContent));
    b.remove(); document.dispatchEvent(new CustomEvent('shopify:section:load', { detail: {} })); await new Promise(r => setTimeout(r, 1300));
    return { yazi: !!h, dolu: [...document.querySelectorAll('.ay-kok')].every(k => k.childElementCount > 0), fiyat: !!document.querySelector('.ay-kok .fiyat-satir'), disk: !!document.querySelector('#diskler .dk-iz button') };
  });
  not(duz.yazi && duz.dolu && duz.fiyat && duz.disk, 'düzenleyici: değişen blok yeniden çizilir, kalanlar sağlam ' + JSON.stringify(duz));
  // Galeri Shopify ürün görsellerinden (Sunset: benzetimde #ay-medya)
  await pg.goto(K + '/products/sunset-lamba'); await pg.waitForTimeout(1200);
  not(await pg.evaluate(() => { const m = JSON.parse(document.getElementById('ay-medya').textContent).g; const i = [...document.querySelectorAll('.ay-kok img')].map(x => x.getAttribute('src')); return m.length > 0 && m.every(x => i.includes(x.src)) && document.querySelectorAll('.ay-blok').length === 6; }), 'Sunset: 6 blok, galeri ürünün Shopify görsellerinden');

  // 8) Koleksiyonda Sepete ekle
  await pg.goto(K + '/collections/all'); await pg.waitForTimeout(600);
  const once = (await sepet()).item_count;
  await pg.locator('.uk', { hasText: 'Kum Saati' }).locator('button').click(); await pg.waitForTimeout(800);
  not((await sepet()).item_count === once + 1, 'koleksiyondan sepete eklendi');

  // 9) Formlar: iletişim ve bülten Shopify'a gider
  await pg.goto(K + '/pages/iletisim'); await pg.waitForTimeout(600);
  const f = pg.locator('.ay-kok form').filter({ has: pg.locator('textarea') }).first();
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
  not(await m.locator('.ay-al.on').count() === 1 && await m.evaluate(() => { const k = document.querySelector('.ay-al [data-kp]'); return !k || getComputedStyle(k).display === 'none'; }), 'masaüstü satın alma çubuğu (kapıda bağlantısı yok)');

  console.log('\n' + (log.length ? log.join('\n') : 'konsol hatası yok'));
  console.log(hata ? `\n${hata} HATA` : '\nHEPSİ TAMAM');
  await b.close(); process.exit(hata || log.length ? 1 : 0);
})();
