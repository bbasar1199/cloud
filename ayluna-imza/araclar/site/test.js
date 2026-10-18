// Ayluna site önizlemesi · uçtan uca test (390×844). Kullanım:
//   (cd ayluna-imza/site && python3 -m http.server 8765 &) ; NODE_PATH=$(npm root -g) node ayluna-imza/araclar/site/test.js [çıktı-klasörü]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const KOK = 'http://127.0.0.1:8765/';
const OUT = process.argv[2] || '/tmp/ayluna-test';
fs.mkdirSync(OUT, { recursive: true });
const SAYFALAR = fs.readdirSync(path.join(__dirname, '..', '..', 'site')).filter(f => f.endsWith('.html'));
let hata = 0;
const not = (ok, m) => { console.log((ok ? 'TAMAM ' : 'HATA  ') + m); if (!ok) hata++; };

(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true });
  const pg = await ctx.newPage();
  const loglar = [];
  pg.on('pageerror', e => loglar.push('pageerror ' + pg.url().split('/').pop() + ': ' + e.message));
  pg.on('console', m => { if (m.type() === 'error' && !/fonts\.g|ERR_INTERNET|net::/.test(m.text())) loglar.push('console ' + pg.url().split('/').pop() + ': ' + m.text()); });

  // 1) Her sayfa açılıyor, çiziliyor, yatay taşma yok
  for (const f of SAYFALAR) {
    await pg.goto(KOK + f, { waitUntil: 'load' }); await pg.waitForTimeout(500);
    const r = await pg.evaluate(() => ({ n: document.querySelectorAll('#kok *').length, tasma: document.documentElement.scrollWidth - innerWidth, h: document.documentElement.scrollHeight }));
    not(r.n > 10 && r.tasma <= 1, `${f}: ${r.n} öğe, taşma ${r.tasma}px, boy ${r.h}`);
    await pg.screenshot({ path: path.join(OUT, f.replace('.html', '') + '.png') });
  }
  // 320px'te taşma
  await pg.setViewportSize({ width: 320, height: 700 });
  for (const f of ['index.html', 'lamba.html', 'lunadream-gece-lambasi.html', 'sepet.html', 'odeme.html', 'tum-urunler.html']) {
    await pg.goto(KOK + f); await pg.waitForTimeout(400);
    const t = await pg.evaluate(() => document.documentElement.scrollWidth - innerWidth);
    not(t <= 1, `320px ${f}: taşma ${t}px`);
  }
  await pg.setViewportSize({ width: 390, height: 844 });

  // 2) Kartla akış: AyFeneri → sepete → çekmece → ödeme → sipariş alındı
  await pg.goto(KOK + 'lamba.html'); await pg.evaluate(() => localStorage.clear()); await pg.reload(); await pg.waitForTimeout(400);
  await pg.locator('#siparis .btn1').first().click();
  await pg.waitForTimeout(900);
  not(await pg.locator('.ay-cek.on').count() === 1, 'AyFeneri: Güvenli Ödeme → sepet çekmecesi açıldı');
  const fr = pg.frameLocator('.ay-cek iframe');
  not((await fr.locator('.urun b').first().textContent()).includes('AyFeneri'), 'çekmecede AyFeneri satırı');
  await fr.locator('.teklif').first().click(); await pg.waitForTimeout(300);
  not((await fr.locator('.teklif.on').count()) === 1, 'çekmecede ek teklif eklendi');
  await fr.locator('.adet button[aria-label="Arttır"]').first().click(); await pg.waitForTimeout(300);
  not((await fr.locator('.adet span').first().textContent()).trim() === '2', 'adet 2 oldu');
  await pg.screenshot({ path: path.join(OUT, 'akis-cekmece.png') });
  await fr.locator('.btn1').click(); await pg.waitForURL(/odeme\.html/, { timeout: 5000 }).catch(() => {});
  not(pg.url().endsWith('odeme.html'), 'Güvenli Ödeme ile Öde → odeme.html');
  await pg.waitForTimeout(400);
  await pg.screenshot({ path: path.join(OUT, 'akis-odeme.png'), fullPage: true });
  await pg.locator('.btn-l[type=submit]').click(); await pg.waitForTimeout(300);
  not((await pg.locator('.o-hata').textContent()).length > 3, 'boş formda hata mesajı');
  await pg.fill('input[name=eposta]', 'deneme@ornek.com'); await pg.fill('input[name=ad]', 'Ayşe'); await pg.fill('input[name=soyad]', 'Yılmaz');
  await pg.fill('input[name=adres]', 'Moda Mah. Bahariye Cad. No 10 D 3'); await pg.fill('input[name=il]', 'İstanbul'); await pg.fill('input[name=ilce]', 'Kadıköy'); await pg.fill('input[name=tel]', '0532 111 22 33');
  await pg.locator('.btn-l[type=submit]').click(); await pg.waitForURL(/siparis-alindi/, { timeout: 5000 }).catch(() => {});
  await pg.waitForTimeout(500);
  not(pg.url().includes('siparis-alindi') && (await pg.locator('.tamam h1').textContent()).includes('alındı'), 'Şimdi öde → Siparişin alındı');
  not(await pg.evaluate(() => AylunaSepet.sayi()) === 0, 'sipariş sonrası sepet boş');
  await pg.screenshot({ path: path.join(OUT, 'akis-tamam.png'), fullPage: true });

  // 3) Kapıda ödeme: Galaxy USB → kapıda formu → sipariş
  await pg.goto(KOK + 'galayx-usb-projektor.html'); await pg.waitForTimeout(400);
  await pg.locator('#siparis .btn2').click(); await pg.waitForTimeout(600);
  not(await pg.locator('.ay-kf.on').count() === 1, 'Galaxy USB: Kapıda Ödeme → form açıldı');
  not((await pg.locator('.kf-top').textContent()).includes('80,00'), 'formda ₺80 kapıda ücreti');
  await pg.screenshot({ path: path.join(OUT, 'akis-kapida.png') });
  await pg.locator('.ay-kf [data-vazgec]').click(); await pg.waitForTimeout(200);
  not(await pg.locator('.kf-bekle:not([hidden])').count() === 1, 'kapatınca "Bekle!" teklifi');
  await pg.locator('[data-devam]').click();
  await pg.fill('.ay-kf input[name=ad]', 'Mehmet Can'); await pg.fill('.ay-kf input[name=tel]', '05321112233'); await pg.selectOption('.ay-kf select[name=il]', 'Ankara');
  await pg.fill('.ay-kf input[name=ilce]', 'Çankaya'); await pg.fill('.ay-kf textarea[name=adres]', 'Kızılay Mah. Atatürk Bulv. No 5');
  await pg.locator('.ay-kf button[type=submit]').click(); await pg.waitForURL(/siparis-alindi/, { timeout: 5000 }).catch(() => {});
  await pg.waitForTimeout(400);
  not(pg.url().includes('siparis-alindi') && (await pg.locator('.tamam').textContent()).includes('kapına gelince'), 'kapıda sipariş → teşekkür (kapıda yazısı)');

  // 4) LunaDream: model + 2 lamba sepete doğru gidiyor
  await pg.goto(KOK + 'lunadream-gece-lambasi.html'); await pg.waitForTimeout(500);
  await pg.locator('.btn-on').first().click(); await pg.waitForTimeout(800);
  const sat = await pg.evaluate(() => AylunaSepet.oku().satirlar[0]);
  not(sat && sat.birim === 2749.99 && /2 adet/.test(sat.varyant), 'LunaDream 2 lamba sepette: ' + (sat && sat.varyant));

  // 5) Menü, koleksiyon "Sepete ekle", rozet, arama, alt bilgi bağlantıları
  await pg.goto(KOK + 'index.html'); await pg.waitForTimeout(400);
  const rozet = await pg.locator('[data-ay-adet]').first().getAttribute('data-ay-adet');
  not(rozet === '1', 'ana sayfa sepet rozeti: ' + rozet);
  await pg.locator('[aria-label="Menü"]').first().click(); await pg.waitForTimeout(400);
  not(await pg.locator('.ay-menu.on').count() === 1, 'menü açıldı');
  await pg.locator('.ay-menu a', { hasText: 'Tüm ürünler' }).click(); await pg.waitForURL(/tum-urunler/).catch(() => {});
  not(pg.url().includes('tum-urunler'), 'menü → Tüm ürünler');
  await pg.waitForTimeout(400);
  await pg.locator('.uk:not(.yok) .ekle-b').first().click(); await pg.waitForTimeout(800);
  not(await pg.evaluate(() => AylunaSepet.sayi()) === 2, 'koleksiyondan sepete ekle (2 ürün)');
  await pg.goto(KOK + 'arama.html?q=Projektör'); await pg.waitForTimeout(400);
  const n = await pg.locator('.izg a').count();
  not(n === 3, 'arama "Projektör": ' + n + ' sonuç');
  await pg.locator('.izg a').first().click(); await pg.waitForTimeout(400);
  not(/projektor|galaksi/.test(pg.url()), 'arama sonucu → ürün sayfası: ' + pg.url().split('/').pop());
  for (const [metin, hedef] of [['KVKK', 'kvkk.html'], ['Mesafeli Satış Sözleşmesi', 'mesafeli-satis.html'], ['Kargo takip', 'kargo-takip.html'], ['İade politikası', 'iade.html']]) {
    await pg.goto(KOK + 'index.html'); await pg.waitForTimeout(300);
    await pg.locator('footer a', { hasText: metin }).first().click(); await pg.waitForTimeout(400);
    not(pg.url().endsWith(hedef), `alt bilgi "${metin}" → ${pg.url().split('/').pop()}`);
  }
  // Ana sayfa ürün kartı → ürün
  await pg.goto(KOK + 'index.html'); await pg.waitForTimeout(300);
  await pg.locator('a.uk').first().click(); await pg.waitForTimeout(400);
  not(!pg.url().endsWith('index.html'), 'ana sayfa ürün kartı → ' + pg.url().split('/').pop());
  // Sepet sayfası: kaldır → boş hâl
  await pg.goto(KOK + 'sepet.html'); await pg.waitForTimeout(400);
  while (await pg.locator('.sil').count()) { await pg.locator('.sil').first().click(); await pg.waitForTimeout(250); }
  not(await pg.locator('.bos-s').count() === 1, 'hepsini kaldırınca boş sepet');
  await pg.screenshot({ path: path.join(OUT, 'sepet-bos.png') });

  // 6) Seçenekli ürün, tükendi ürün, çekmeceden kapıda, formlar, rozet çekmecede yok
  await pg.goto(KOK + 'egitici-akilli-cizim-tahtasi.html'); await pg.waitForTimeout(400);
  const secB = pg.locator('[aria-pressed]', { hasText: /Mavi|Pembe|Yeşil|Sarı|Turuncu|Mor/ });
  if (await secB.count() > 1) { await secB.nth(1).click(); await pg.waitForTimeout(200); }
  await pg.locator('.btn1').first().click(); await pg.waitForTimeout(800);
  const s2 = await pg.evaluate(() => AylunaSepet.oku().satirlar.slice(-1)[0]);
  not(s2 && s2.h === 'egitici-akilli-cizim-tahtasi' && s2.varyant.split('·').length >= 2, 'seçenekli ürün sepette: ' + (s2 && s2.varyant));
  const xRozet = await pg.frameLocator('.ay-cek iframe').locator('[aria-label="Sepeti kapat"][data-ay-adet]').count();
  not(xRozet === 0, 'çekmecedeki kapat düğmesinde rozet yok');
  await pg.frameLocator('.ay-cek iframe').locator('.btn2').click(); await pg.waitForTimeout(600);
  not(await pg.locator('.ay-kf.on').count() === 1 && await pg.locator('.ay-cek.on').count() === 0, 'çekmeceden Kapıda Ödeme → form (çekmece kapandı)');
  await pg.goto(KOK + 'aroma-terapi-nemlendirici.html'); await pg.waitForTimeout(400);
  not(await pg.locator('.btn1[disabled]').count() === 1, 'tükendi ürün: buton kapalı');
  await pg.locator('.btn2').click(); await pg.waitForTimeout(300);
  not((await pg.locator('.ay-tost').textContent()).includes('haber'), 'tükendi: Gelince haber ver bildirimi');
  for (const [f, sec, beklenen] of [['iletisim.html', '.form', 'Mesajın alındı'], ['kargo-takip.html', '.form', 'Track123'], ['index.html', '.bulten form', 'Kaydın alındı'], ['hesap.html', '.form', 'Giriş kodu']]) {
    await pg.goto(KOK + f); await pg.waitForTimeout(300);
    const frm = pg.locator(sec).first();
    for (const i of await frm.locator('input[type=email],input[type=text],input[type=tel],textarea').all()) await i.fill(/email/.test(await i.getAttribute('type') || '') ? 'a@b.co' : '05321112233');
    await frm.locator('button[type=submit]').click(); await pg.waitForTimeout(300);
    not((await pg.locator('.ay-tost').textContent()).includes(beklenen), `${f} formu → "${beklenen}"`);
  }
  await pg.goto(KOK + '404.html'); await pg.waitForTimeout(300);
  await pg.fill('input[type=search]', 'nemlendirici'); await pg.press('input[type=search]', 'Enter'); await pg.waitForTimeout(500);
  not(pg.url().includes('arama.html?q=nemlendirici') && (await pg.locator('.izg a').count()) === 3, '404 arama → 3 nemlendirici');
  await pg.goto(KOK + 'index.html'); await pg.waitForTimeout(300);
  await pg.locator('[aria-label="Ara"]').click(); await pg.waitForTimeout(300);
  not(pg.url().endsWith('arama.html'), 'başlık Ara → arama.html');

  // Baskı satırları (18 Eki): fiyatta "Stokta" yok, altında "Dün [X]"; dönen satır hediye → aynı gün kargo + 16.00 sayacı (İstanbul saati)
  for (const [f, ilk] of [['lunadream-gece-lambasi.html', 'hediye'], ['galayx-usb-projektor.html', 'film diski']]) {
    const sp = await ctx.newPage(); sp.on('pageerror', e => loglar.push('pageerror ' + f + ': ' + e.message));
    await sp.clock.install({ time: new Date('2026-10-19T09:47:15Z') }); // Pazartesi 12:47:15 İstanbul
    await sp.goto(KOK + f); await sp.clock.runFor(1500);
    const on = () => sp.locator('.donen .dn-s.on').textContent();
    not(!/Stokta/.test(await sp.locator('#siparis .fiyat-satir, #siparis .fiyat').first().textContent()) && /Dün .+ kişi satın aldı/.test(await sp.locator('.dun').textContent()), f + ': fiyatta Stokta yok, altında Dün satırı');
    not((await on()).includes(ilk), f + ': dönen satır önce "' + ilk + '"');
    await sp.clock.runFor(3500); const k = await on(), s1 = await sp.locator('.dn-sy').textContent();
    not(k.includes('16.00’ya kadar') && /^03:12:\d\d$/.test(s1), f + ': sonra aynı gün kargo + sayaç ' + s1);
    await sp.clock.runFor(2000); const s2 = await sp.locator('.dn-sy').textContent(), fark = +s1.slice(-2) - +s2.slice(-2);
    not(fark >= 2 && fark <= 3, f + ': sayaç akıyor ' + s1 + ' → ' + s2);
    await sp.clock.runFor(4500); not((await on()).includes(ilk), f + ': başa döndü');
    not((await sp.locator('.yol li').nth(1).textContent()).includes('Bugün'), f + ': yolda kargo tarihi Bugün');
    { await sp.locator('.al-on').scrollIntoViewIfNeeded(); await sp.clock.runFor(600); const kd = await sp.locator('.stok-kd.on').textContent();
      not(/^Son (18|\[N\]) adet$/.test(kd) && await sp.locator('#siparis .canli, #siparis p.stok').count() === 0, f + ': stok kurdelesi butonda "' + kd + '", eski stok satırı yok'); }
    await sp.clock.setSystemTime(new Date('2026-10-19T13:30:00Z')); await sp.clock.runFor(11000); // 16.30
    const geç = await sp.locator('.donen .dn-s').nth(1).textContent();
    not(geç.includes('yarın kargoda') && await sp.locator('.dn-sy').count() === 0, f + ': 16.00 sonrası "' + geç + '", sayaç yok');
    await sp.close();
  }

  console.log('\n' +(loglar.length ? loglar.join('\n') : 'konsol hatası yok'));
  console.log(hata ? `\n${hata} HATA` : '\nHEPSİ TAMAM');
  await b.close();
  process.exit(hata || loglar.length ? 1 : 0);
})();
