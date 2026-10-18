// Kaydırmaya bağlı bölümü iki durumda sınar (Tur 25: "kaydırdıkça değişmiyor").
//   1) Telefon / Oynat: sayfa kendi kayar (390×844).
//   2) Tuval: pano 390×<h> boyunda başka kökenli bir çerçevede durur, kaymaz; tuval dışarıdan kaydırılır ve ölçeklenir.
// Önce yerel önizlemeyi üret (dc-onizle.js sayfayı os.tmpdir()/ayluna-dc-onizle.html'e yazar):
//   NODE_PATH=$(npm root -g) ONIZLE_H=844 node ayluna-imza/araclar/dc-onizle.js <pano.dc.html> /tmp/x.png '{}' 0 100
// Sonra: NODE_PATH=$(npm root -g) node ayluna-imza/araclar/kaydirma-testi.js [pano yüksekliği=5700] [bölüm=.gece-bolum] [durum=gece]
// Önizleme her durumda DOM'u baştan kurar; gerçek çalışma zamanı gibi davranması için her kurulumdan sonra componentDidUpdate çağrılır.
const http = require('http'), fs = require('fs'), path = require('path'), os = require('os');
const { chromium } = require('playwright');
const H = Number(process.argv[2] || 5700), BOLUM = process.argv[3] || '.gece-bolum', ALAN = process.argv[4] || 'gece';
const SAYFA = fs.readFileSync(path.join(os.tmpdir(), 'ayluna-dc-onizle.html'));
const HOST = (p) => `<!doctype html><body style="margin:0"><div id="kap" style="position:relative;width:500px;height:900px;overflow:hidden"><iframe id="f" src="http://127.0.0.1:${p}/e.html" style="position:absolute;left:0;top:0;width:390px;height:${H}px;border:0;transform-origin:0 0"></iframe></div></body>`;
function sun(icerik) { return new Promise(r => { const s = http.createServer((q, w) => { w.setHeader('content-type', 'text/html; charset=utf-8'); w.end(typeof icerik === 'function' ? icerik() : icerik); }).listen(0, '127.0.0.1', () => r(s)); }); }
const KUR = `(() => { const oR = R; window.R = function () { oR(); C.componentDidUpdate && C.componentDidUpdate(); }; C.componentDidMount(); clearInterval(C.iv); })()`;
(async () => {
  const sE = await sun(SAYFA), pE = sE.address().port, sH = await sun(() => HOST(pE));
  const b = await chromium.launch();
  let pg = await b.newPage({ viewport: { width: 390, height: 844 } });
  await pg.goto(`http://127.0.0.1:${pE}/e.html`); await pg.waitForTimeout(500); await pg.evaluate(KUR);
  const ust = await pg.evaluate(s => document.querySelector(s).getBoundingClientRect().top + scrollY, BOLUM);
  let out = [];
  for (const d of [-400, 0, 300, 700, 1100, 1500, 1900, 2300]) { await pg.evaluate(y => scrollTo(0, y), ust + d); await pg.waitForTimeout(150); out.push(d + ':' + await pg.evaluate(a => C.state[a], ALAN)); }
  console.log('telefon  (bölüm üstünden kaydırma px : durum)', out.join(' '));
  await pg.close();
  pg = await b.newPage({ viewport: { width: 500, height: 900 } });
  await pg.goto(`http://127.0.0.1:${sH.address().port}/`); await pg.waitForTimeout(800);
  const fr = pg.frames().find(f => f.url().includes(':' + pE + '/'));
  await fr.evaluate(KUR); await pg.waitForTimeout(400);
  const st = await fr.evaluate(s => document.querySelector(s).getBoundingClientRect().top, BOLUM);
  for (const sc of [1, .6]) {
    out = [];
    for (const d of [700, 300, 0, -150, -300, -500, -700]) { // bölüm üstünün ekran ortasına uzaklığı (ekran px); azaldıkça kullanıcı aşağı kaydırıyor
      await pg.evaluate(([y, sc]) => { document.getElementById('f').style.transform = `translateY(${-y}px) scale(${sc})`; }, [st * sc - 450 - d, sc]);
      await pg.waitForTimeout(400); out.push(d + ':' + await fr.evaluate(a => C.state[a], ALAN));
    }
    console.log('tuval x' + sc + ' (bölüm üstü − ekran ortası : durum)', out.join(' '));
  }
  await b.close(); sE.close(); sH.close();
})();
