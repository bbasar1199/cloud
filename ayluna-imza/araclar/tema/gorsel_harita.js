/* Ayluna · JS ile çizilen görsellerin blok haritası (28 Eki, kullanıcı: "odası böyle görünecekteki görselleri değiştirmek istiyorum ama sabit").
   Tema benzetiminde (araclar/tema/benzetim.py) her özel ürün sayfasını açar; her bloktaki görselleri toplar, bloğun düğmelerine tek tek basıp
   (model, disk, sekme, kaydırma) yeni görünen görselleri de ekler. Çıktı: araclar/tema/gorsel-harita.json {pano: {blok: [[blob, etiket]]}}.
   Ürün kartı görselleri (Shopify'daki ürünün ana görseli) ve galeri (ürünün medyası) dışarıda kalır.
   Kullanım: benzetim BENZETIM_MEDYA=<dört ürün> ile çalışırken  NODE_PATH=/opt/node-tools/node_modules node araclar/tema/gorsel_harita.js [adres] */
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const K = process.argv[2] || 'http://localhost:8790';
const SAYFA = [['LunaDreamE', '/products/lunadream-gece-lambasi'], ['GalaxyUSB', '/products/galayx-usb-projektor'], ['AyFeneri', '/products/lamba'], ['GalaksiNight', '/products/ayluna-galaksi-night-projektor'], ['Ayluna-Anasayfa', '/']];
(async () => {
  const b = await chromium.launch(); const sonuc = {};
  for (const [pano, h] of SAYFA) {
    const p = await b.newPage({ viewport: { width: 440, height: 956 } });
    await p.route(/\/cart\//, r => r.abort());
    await p.goto(K + h); await p.waitForTimeout(2500);
    const harita = {};
    const topla = async () => {
      const r = await p.evaluate(() => {
        const kart = new Set(Object.keys((window.AYLUNA_VERI || {}).kart || {}));
        const etiket = (el) => {
          const a = el.getAttribute && el.getAttribute('alt'); if (a && a.trim() && !/\{\{/.test(a)) return [a.trim(), 3];
          const c = el.closest('figure,li,article,button,label,[class*=kart],[class*=kare],[class*=slayt]');
          const t = c ? (c.innerText || '').split('\n').map(x => x.trim()).filter(x => x.length > 1)[0] : '';
          if (t) return [t, 2];
          const al = el.closest('[aria-label],[title]'); const at = al && (al.getAttribute('aria-label') || al.getAttribute('title'));
          if (at && al.closest('.ay-tb') === el.closest('.ay-tb') && !/^Ayluna/.test(at)) return [at.trim().replace(/ diskini göster$/, ' diski'), 2];
          const sec = el.closest('section, .pg > div'); const h = sec && sec.querySelector('h2, h3, .bas-y');
          return [h ? h.innerText.replace(/\s+/g, ' ').trim() : '', 1];
        };
        const out = {};
        const ana = !document.querySelector('.ay-tb[data-blok]');
        (ana ? [...document.querySelectorAll('.shopify-section')].filter(x => /__b\d+$/.test(x.id)) : [...document.querySelectorAll('.ay-tb[data-blok]')]).forEach(tb => {
          const blok = ana ? tb.id.split('__').pop() : tb.getAttribute('data-blok'); out[blok] = out[blok] || [];
          tb.querySelectorAll('.ay-kok img, .ay-kok video[poster], .ay-kok [style*="url("]').forEach(el => {
            const u = (el.getAttribute('src') || '') + ' ' + (el.getAttribute('poster') || '') + ' ' + (el.getAttribute('style') || '');
            (u.match(/[0-9a-f]{32}/g) || []).forEach(x => { if (!kart.has(x)) out[blok].push([x].concat(etiket(el))); });
          });
        });
        return out;
      });
      for (const blok in r) { harita[blok] = harita[blok] || new Map(); r[blok].forEach(([x, e, p]) => { const o = harita[blok].get(x); if (!o || p > o[1]) harita[blok].set(x, [e, p]); }); }
    };
    await topla();
    const bloklar = await p.evaluate(() => document.querySelector('.ay-tb[data-blok]') ? [...document.querySelectorAll('.ay-tb[data-blok]')].map(x => x.getAttribute('data-blok'))
      : [...document.querySelectorAll('.shopify-section')].filter(x => /__b\d+$/.test(x.id)).map(x => x.id.split('__').pop()));
    for (const blok of bloklar) {
      const sec = /^b\d+$/.test(blok) ? `[id$="__${blok}"]` : `.ay-tb[data-blok="${blok}"]`;
      const n = await p.locator(`${sec} .ay-kok button`).count();
      for (let i = 0; i < Math.min(n, 40); i++) {
        const d = p.locator(`${sec} .ay-kok button`).nth(i);
        const t = (await d.innerText().catch(() => '')) + ' ' + (await d.getAttribute('aria-label').catch(() => '') || '');
        if (/ödeme|sepet|satın|kapıda|menü|ara\b/i.test(t)) continue;
        await d.click({ timeout: 1500, force: true }).catch(() => {}); await p.waitForTimeout(220);
        await topla(); await p.keyboard.press('Escape').catch(() => {});
      }
    }
    // Aynı görsel iki blokta: ilk blokta kalır
    const gor = new Set(); sonuc[pano] = {};
    for (const blok of bloklar) {
      const l = [...(harita[blok] || new Map()).entries()].filter(([x]) => !gor.has(x)).map(([x, e]) => [x, e[0]]);
      l.forEach(([x]) => gor.add(x)); if (l.length) sonuc[pano][blok] = l;
    }
    console.log(pano, Object.entries(sonuc[pano]).map(([k, v]) => k + ':' + v.length).join(' '));
    await p.close();
  }
  await b.close();
  fs.writeFileSync(path.join(__dirname, 'gorsel-harita.json'), JSON.stringify(sonuc, null, 1) + '\n');
})();
