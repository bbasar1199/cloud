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

  // 4) LunaDream: açılışta paket seçili değil (19 Eki), seçimsiz alım 1 adet; 2 Adet seçilince 2 lamba sepete doğru gidiyor
  await pg.goto(KOK + 'lunadream-gece-lambasi.html'); await pg.evaluate(() => localStorage.clear()); await pg.reload(); await pg.waitForTimeout(500);
  not(await pg.locator('#siparis [aria-pressed="true"]').filter({ hasText: 'Adet' }).count() === 0, 'LunaDream: açılışta paket seçili değil');
  await pg.locator('.btn-on').first().click(); await pg.waitForTimeout(800);
  const sat1 = await pg.evaluate(() => AylunaSepet.oku().satirlar[0]);
  not(sat1 && sat1.birim === 1699.99 && /1 adet/.test(sat1.varyant), 'LunaDream seçimsiz alım 1 adet: ' + (sat1 && sat1.varyant));
  await pg.evaluate(() => { localStorage.clear(); Ayluna.cekmeceKapat(); }); await pg.reload(); await pg.waitForTimeout(500);
  await pg.locator('#siparis button', { hasText: '2 Adet' }).first().click(); await pg.waitForTimeout(300);
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
  await pg.locator('#kok [aria-label="Ara"]').click(); await pg.waitForTimeout(300);
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
    if (f.startsWith('lunadream')) { const src = await sp.evaluate(() => [...document.querySelectorAll('.yarim-iz img')].map(i => i.currentSrc || i.src));
      not(src.length === 2 && src.every(x => /\.webp$/.test(x)), f + ': model kartı görselleri saydam (WebP), siyah zemin yok'); }
    { await sp.locator('.al-on').scrollIntoViewIfNeeded(); await sp.clock.runFor(600); const kd = await sp.locator('.stok-kd.on').textContent();
      not(/^Son (18|23) adet$/.test(kd) && await sp.locator('#siparis .canli, #siparis p.stok').count() === 0, f + ': stok kurdelesi butonda "' + kd + '", eski stok satırı yok'); }
    await sp.clock.setSystemTime(new Date('2026-10-19T13:30:00Z')); await sp.clock.runFor(11000); // 16.30
    const geç = await sp.locator('.donen .dn-s').nth(1).textContent();
    not(geç.includes('yarın kargoda') && await sp.locator('.dn-sy').count() === 0, f + ': 16.00 sonrası "' + geç + '", sayaç yok');
    await sp.close();
  }

  // Galeriler Shopify'daki gibi (19 Eki): görsel sayısı ogrenme/galeri-canli.json ile aynı, kare
  const GC = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '..', 'ogrenme', 'galeri-canli.json'), 'utf8'));
  for (const [h, liste] of Object.entries(GC)) {
    await pg.goto(KOK + h + '.html'); await pg.waitForTimeout(400);
    const r = await pg.evaluate(() => { const s = [...document.querySelectorAll('.kare-foto .kf, .h-iz .hs, .g-iz .gs')]; const i = s[0] && s[0].querySelector('img').getBoundingClientRect(); return { n: s.length, oran: i && i.height ? Math.round(i.width / i.height * 100) / 100 : 0 }; });
    not(r.n === liste.length && Math.abs(r.oran - 1) < .02, `${h}: galeri ${r.n}/${liste.length} görsel, oran ${r.oran}`);
    // Gösterge fotoğrafın içinde (kullanıcı, 19 Eki: "gömülü olsun"), altında "Temsilî görseller" yok
    const g = await pg.evaluate(() => { const f = document.querySelector('.kare-foto, .h-iz, .g-iz').getBoundingClientRect(), z = document.querySelector('.ay-iz, .d-iz, .g-alt').getBoundingClientRect();
      return { ic: z.top >= f.top && z.bottom <= f.bottom + .5 && z.left >= f.left && z.right <= f.right, temsil: /temsil/i.test(document.querySelector('#kok').textContent) }; });
    not(g.ic && !g.temsil, `${h}: gösterge fotoğrafın içinde, "temsilî" yazısı yok`);
  }
  // Güvenli Ödeme düğmelerinde fiyat yok (kullanıcı, 19 Eki)
  { const fiyatli = [];
    for (const f of ['lunadream-gece-lambasi', 'galayx-usb-projektor', 'lamba', 'ayluna-galaksi-night-projektor', 'sunset-lamba']) {
      await pg.goto(KOK + f + '.html'); await pg.waitForTimeout(300);
      const t = await pg.evaluate(() => [...document.querySelectorAll('#kok .btn-on, #kok .btn1')].map(b => (b.querySelector('.b-ic>span') || b).textContent.trim()));
      if (t.some(x => /₺/.test(x))) fiyatli.push(f + ': ' + t.join(' | ')); }
    not(!fiyatli.length, 'Güvenli Ödeme düğmelerinde fiyat yok' + (fiyatli.length ? ': ' + fiyatli.join('; ') : '')); }
  // Müşteri kanıtı tek bölüm (19 Eki, B · Tek akış): önce 6 mesajlık şerit (kendi başlığıyla), öne çıkan yorum, 5 fotoğraflık şerit; çip yok;
  // dokununca büyür, Esc kapatır
  await pg.goto(KOK + 'lunadream-gece-lambasi.html'); await pg.waitForTimeout(500);
  { const k = await pg.evaluate(() => [...document.querySelectorAll('#yorumlar .karma button')].map(b => b.className));
    await pg.locator('#yorumlar .karma button').first().click(); await pg.waitForTimeout(300);
    const acik = await pg.locator('.buyuk img').count(); await pg.keyboard.press('Escape'); await pg.waitForTimeout(300);
    not(k.filter(c => c === 'k-msj').length === 6 && k.filter(c => c === 'k-foto').length === 5 && k[0] === 'k-msj' && await pg.locator('#yorumlar .yone').count() === 1
      && await pg.locator('#yorumlar .cip[aria-pressed]').count() === 0 && await pg.locator('#mesajlar').count() === 0 && acik === 1 && await pg.locator('.buyuk').count() === 0,
      `müşteri kanıtı tek bölüm: ${k.length} görsel (ilk ${k[0]}), büyük görünüm açılıp Esc ile kapandı`); }
  // Sizden gelen mesajlar diğer ürünlerde de (kullanıcı, 19 Eki): 6 kart, "LunaDream siparişlerinden" notu, dokununca büyür, Esc kapatır
  { const eksik = [];
    for (const f of ['galayx-usb-projektor', 'lamba', 'ayluna-galaksi-night-projektor', 'ask-saati', 'sunset-lamba']) {
      await pg.goto(KOK + f + '.html'); await pg.waitForTimeout(400);
      const n = await pg.locator('#mesajlar .mkarma button').count(), not_ = /LunaDream siparişlerinden/.test(await pg.locator('#mesajlar').textContent().catch(() => ''));
      let ok = n === 6 && not_;
      if (ok) { await pg.locator('#mesajlar .mkarma button').first().click(); await pg.waitForTimeout(300); ok = await pg.locator('.mbuyuk img').count() === 1;
        await pg.keyboard.press('Escape'); await pg.waitForTimeout(300); ok = ok && await pg.locator('.mbuyuk').count() === 0; }
      if (!ok) eksik.push(f + ' (' + n + ')'); }
    not(!eksik.length, 'mesajlar bölümü diğer ürünlerde' + (eksik.length ? ': ' + eksik.join(', ') : '')); }
  // Azaltılmış hareket (ör. Windows'ta animasyon efektleri kapalı) galeriyi durdurmaz; kaymadan geçer
  { const rm = await b.newContext({ viewport: { width: 390, height: 844 }, reducedMotion: 'reduce' }); const rp = await rm.newPage();
    for (const f of ['lunadream-gece-lambasi', 'galayx-usb-projektor', 'lamba', 'ask-saati']) {
      await rp.goto(KOK + f + '.html'); await rp.waitForTimeout(6300);
      const x = await rp.evaluate(() => { const e = document.querySelector('.kare-foto, .h-iz, .g-iz'); return Math.round(e.scrollLeft / e.clientWidth); });
      not(x === 1, `${f}: azaltılmış harekette galeri 5 sn'de geçti (${x})`);
    }
    await rm.close(); }
  // WhatsApp ve şirket bilgisi şimdilik yok (kullanıcı, 19 Eki: "sonra kendim ekleyeceğim")
  { const kalan = [];
    for (const f of SAYFALAR) { await pg.goto(KOK + f); await pg.waitForTimeout(250);
      const t = await pg.evaluate(() => document.body.textContent + [...document.querySelectorAll('a')].map(a => a.href).join(' '));
      if (/whatsapp|wa\.me|ticaret unvan|mersis|\bKEP\b/i.test(t)) kalan.push(f); }
    await pg.locator('#kok [aria-label="Menü"]').first().click(); await pg.waitForTimeout(300);
    if (/whatsapp/i.test(await pg.locator('.ay-menu').textContent())) kalan.push('menü');
    await pg.keyboard.press('Escape');
    not(!kalan.length, 'WhatsApp ve şirket bilgisi hiçbir sayfada yok' + (kalan.length ? ': ' + kalan.join(', ') : '')); }

  // Galaxy USB canlı kartlar (21 Eki): 5 özellik hücresinde ekran, disk şeridi, teslim kartında USB ikonu
  await pg.goto(KOK + 'galayx-usb-projektor.html'); await pg.waitForTimeout(500);
  not(await pg.locator('#siparis .ozler .uk-ek').count() === 5 && await pg.locator('#siparis .ozler .ui-serit .sd').count() === 5 && await pg.locator('#siparis .teslim .y-ik').count() === 1, 'Galaxy USB: 5 özellik ekranı, disk şeridi, teslim kartında ikon');
  // Satın alma butonları sepeti katlamaz (kartla dene → kapat → kapıda), paket satırında "2 × eski fiyat" üstü çizili yok (§7 kural 2)
  await pg.goto(KOK + 'galayx-usb-projektor.html'); await pg.evaluate(() => localStorage.clear()); await pg.reload(); await pg.waitForTimeout(400);
  await pg.evaluate(() => { AylunaSepet.koy({ h: 'galayx-usb-projektor', ad: 'Galaxy USB', varyant: '2 adet', paket: 2, birim: 2279.99, eski: null }); });
  await pg.locator('#siparis .btn2').click(); await pg.waitForTimeout(500);
  await pg.evaluate(() => Ayluna.kapidaKapat()); await pg.locator('#siparis .btn2').click(); await pg.waitForTimeout(500);
  { const s = await pg.evaluate(() => AylunaSepet.oku().satirlar.filter(x => x.h === 'galayx-usb-projektor'));
    not(s.length === 1 && s[0].adet === 1, `Galaxy USB: iki kez Kapıda → sepette tek satır (${s.length} satır, adet ${s[0] && s[0].adet})`);
    const p = await pg.evaluate(() => { const s = AylunaSepet.oku(); return s.satirlar.map(x => x.eski); });
    not(p.every(e => e === null || e === undefined) || (await pg.evaluate(() => AylunaSepet.oku().satirlar[0].paket)) === 1, 'paket satırında üstü çizili eski fiyat yok'); }
  await pg.evaluate(() => Ayluna.kapidaKapat());

  await pg.goto(KOK + 'lunadream-gece-lambasi.html'); await pg.waitForTimeout(500);
  not(await pg.locator('#siparis .sih').count() === 1 && await pg.locator('.sol-oz').count() === 0, 'telefon: Sihirli Özellikler satın alma kutusunda, masaüstü kopyası yok');
  // Odası böyle görünecek · Gece vitrini (21 Eki): Bir gece ve iki posterli eski Odası yok; 4 oda, aya dokununca oda ortaya kayar ve yazı değişir
  not(await pg.locator('#bir-gece').count() === 0 && await pg.locator('.poster').count() === 0 && await pg.locator('#odalar.vitrin .vt-kart').count() === 4 && await pg.locator('#odalar').count() === 1, 'telefon: Bir gece yok, tek Odası bölümü (Gece vitrini, 4 oda)');
  { const sira = await pg.evaluate(() => ['videolar', 'odalar', 'yorumlar', 'diskler'].map(id => document.getElementById(id)).every((e, i, a) => e && (!i || a[i - 1].compareDocumentPosition(e) & 4)));
    not(sira, 'telefon: Odası Videolar ile Aileler ne diyor arasında'); }
  await pg.locator('#odalar').scrollIntoViewIfNeeded(); await pg.locator('.vt-ay').nth(2).click(); await pg.waitForTimeout(900);
  { const r = await pg.evaluate(() => { const el = document.querySelector('.vt-serit'), c = el.children[2], on = document.querySelector('.vt-m.on');
      return { orta: Math.abs(c.offsetLeft + c.offsetWidth / 2 - el.scrollLeft - el.clientWidth / 2), yazi: on && on.textContent, gizli: document.querySelectorAll('.vt-m[aria-hidden=true]').length }; });
    not(r.orta < 4 && /Tavanda uzay/.test(r.yazi) && r.gizli === 3, `telefon vitrin: 3. ay → Tavanda uzay ortada (${Math.round(r.orta)} px), yazı değişti, öbür yazılar gizli`); }
  { const sw = await pg.evaluate(() => document.documentElement.scrollWidth); not(sw === 390, 'telefon LunaDream: yatay taşma yok (' + sw + ')'); }
  // Sihirli özellikler · Canlı kartlar ve teslim kartı (21 Eki): 4 kart, her birinde mini ekran; teslim kartında Kapında lambası; Erkek seçilince robot ikonu
  not(await pg.locator('#siparis .sih .a-kart').count() === 4 && await pg.locator('#siparis .sih .sh-ek').count() === 4 && await pg.locator('.teslim .yol-lamba').count() === 1 && await pg.locator('.sih .oz').count() === 0, 'telefon: Sihirli canlı kartlar (4 ekran), teslim kartında lamba');
  { const kiz = await pg.locator('.sih .lmb.rb').count(); await pg.locator('.yarim-iz button').nth(1).click(); await pg.waitForTimeout(300);
    const rb = await pg.locator('.sih .lmb.rb').count(), lk = await pg.locator('.sih .lmb:not(.rb)').count(); await pg.locator('.yarim-iz button').nth(0).click(); await pg.waitForTimeout(300);
    not(kiz === 0 && rb === 3 && lk === 0, `Sihirli ikonu modele bağlı: Kız'da robot ${kiz}, Erkek'te robot ${rb}, atlıkarınca ${lk}`); }

  // Masaüstü (19 Eki): ortak üst menü, yatay taşma yok, ürün sayfasında galeri yalnız üst kısımda yapışık
  const mctx = await b.newContext({ viewport: { width: 1440, height: 900 } });
  const mp = await mctx.newPage(); mp.on('pageerror', e => loglar.push('pageerror masaüstü: ' + e.message));
  for (const f of ['index', 'tum-urunler', 'sepet', 'iletisim', 'arama', 'iade', 'lunadream-gece-lambasi', 'galayx-usb-projektor', 'lamba', 'ayluna-galaksi-night-projektor', 'sunset-lamba']) {
    await mp.goto(KOK + f + '.html'); await mp.waitForTimeout(700);
    await mp.evaluate(() => window.scrollTo(0, document.body.scrollHeight)); await mp.waitForTimeout(500);
    const r = await mp.evaluate(() => {
      const g = e => e && getComputedStyle(e).display !== 'none' && e.getBoundingClientRect().height > 0;
      const tel = [...document.querySelectorAll('#kok header.ust, #kok .sahne>header, #kok .u-ust')].some(g);
      const yt = document.querySelector('.ay-masa'), ust = yt && yt.getBoundingClientRect();
      const gal = document.querySelector('.urun-ust>.urun-sol, .urun-ust>.ust-sol');
      const yap = gal ? gal.getBoundingClientRect().bottom <= gal.parentElement.getBoundingClientRect().bottom + 1 : true;
      return { sw: document.documentElement.scrollWidth, masa: g(yt) && ust.width === innerWidth, tel, yap };
    });
    not(r.sw === 1440 && r.masa && !r.tel && r.yap, `masaüstü ${f}: taşma ${r.sw}, üst menü ${r.masa}, telefon başlığı gizli ${!r.tel}, galeri üst kısımda ${r.yap}`);
  }
  // Masaüstü yapışkan satın alma çubuğu: üstte kapalı, satın alma butonu geçince açılır; Kapıda → form, sepette tek satır
  await mp.goto(KOK + 'lunadream-gece-lambasi.html'); await mp.evaluate(() => localStorage.clear()); await mp.reload(); await mp.waitForTimeout(900);
  const c0 = await mp.locator('.ay-al.on').count();
  await mp.evaluate(() => window.scrollTo(0, 2400)); await mp.waitForTimeout(800);
  const cl = await mp.locator('.ay-al.on [data-l]').textContent().catch(() => '');
  not(c0 === 0 && cl.trim() === 'Güvenli Ödeme ile Al', 'masaüstü çubuğu: üstte kapalı, aşağıda açık, düğmede fiyat yok (19 Eki) "' + cl + '"');
  not(!/₺/.test(await mp.locator('.ay-al [data-kp]').textContent()), 'çubukta Kapıda bağlantısında fiyat yok');
  await mp.locator('.ay-al [data-kp]').click(); await mp.waitForTimeout(600);
  not(await mp.locator('.ay-kf.on').count() === 1 && await mp.evaluate(() => AylunaSepet.oku().satirlar.length) === 1, 'çubuktan Kapıda → form açıldı, sepette tek satır');
  // Masaüstü: özellik kartları sol sütunda tek kopya; Gece vitrini kenardan kenara bant ve şerit, yazı altta; 4. ay → 4. oda ortada
  await mp.goto(KOK + 'lunadream-gece-lambasi.html'); await mp.waitForTimeout(800);
  not(await mp.locator('.sol-oz .sih').count() === 1 && await mp.locator('.sih').count() === 1, 'masaüstü: Sihirli Özellikler galerinin altında, tek kopya');
  await mp.locator('#odalar').scrollIntoViewIfNeeded(); await mp.locator('.vt-ay').nth(3).click(); await mp.waitForTimeout(900);
  { const r = await mp.evaluate(() => { const v = document.getElementById('odalar').getBoundingClientRect(), el = document.querySelector('.vt-serit'), c = el.children[3], m = document.querySelector('.vt-m.on').getBoundingClientRect(), sr = el.getBoundingClientRect();
      return { gen: Math.round(v.width), solda: m.top >= sr.bottom && Math.abs(sr.width - innerWidth) < 2, orta: Math.abs(c.offsetLeft + c.offsetWidth / 2 - el.scrollLeft - el.clientWidth / 2), yazi: document.querySelector('.vt-m.on').textContent }; });
    not(r.gen === 1440 && r.solda && r.orta < 4 && /Masalı o seçsin/.test(r.yazi), `masaüstü vitrin: bant ${r.gen}, şerit kenardan kenara ve yazı altta ${r.solda}, 4. oda ortada (${Math.round(r.orta)} px), yazı değişti`); }
  await mctx.close();

  console.log('\n' +(loglar.length ? loglar.join('\n') : 'konsol hatası yok'));
  console.log(hata ? `\n${hata} HATA` : '\nHEPSİ TAMAM');
  await b.close();
  process.exit(hata || loglar.length ? 1 : 0);
})();
