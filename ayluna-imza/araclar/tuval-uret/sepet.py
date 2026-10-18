# Ayluna · sepet çekmecesi (18 Eki). Çalıştır: python3 sepet.py
# Kullanıcı: "Bunların hepsi güzel bir şekilde sepette gelecek." Canlı sepetteki ek teklifler (ekran görüntüsü):
#   Astronot Hava Temizleyici 749.00TL · Siparişinize özel Kum Saati Lamba 699.99TL · Işıklı Nemlendirici 749.99TL ·
#   Hızlı Kargo 79.99TL ("Siparişiniz öncelikli olarak hazırlanır ve aynı gün kargoya teslim edilir").
# Mağaza karşılıkları: Astronot Oda Nemlendirici Aroma Difüzör (₺799), Ayluna Kum Saati Lamba (₺799), Yıldız Işığı Nemlendirici (₺849,99).
# "Hava temizleyici" yazılmaz: ürün nemlendirici (teyitsiz işlev iddiası). Özel fiyatın yanında mağaza fiyatı düz yazıyla durur (üstü çizili değil).
# Marka dili (sepet her ürün sayfasında ortak): lacivert #1A2142 + beyaz, Ayluna işareti; Young Serif başlık + Onest gövde.
# Ödeme: kartla %5 önce, kapıda ikinci; kapıda butonunda fiyat yok (₺80 kapıda ücreti formda ve SSS'de).
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL, TL_JS
import luna_e as E
OUT = os.path.join(HERE, '..', '..', 'canvas', 'Sepet.dc.html')
B = '/_blob/'
IMG = dict(ld='ec56ce61ebfa99daa425df6a99f3c7cc', astronot='ec1ada6af6ab5b345bc0a6c49e46d7be', kum='ceaf4cf66048150f068cf32120aa9eb1', nem='bf1b4c56f2b7c2d2e4b44ece808b0887')

CSS = r""".pg{background:#FFFFFF;font-family:"Onest",ui-sans-serif,system-ui,sans-serif;font-size:15px;--lac:#1A2142;--soluk:#5C6078;--cizgi:#E6E8EE;--zemin:#F4F5F7;--ease:cubic-bezier(.2,.7,.2,1)}
.pg button{font:inherit;color:inherit;cursor:pointer}
.pg button:focus-visible{outline:2px solid #1A2142;outline-offset:3px}
/* Üst: başlık + kapat */
.s-ust{display:flex;align-items:center;justify-content:space-between;height:64px;padding:0 6px 0 16px;border-bottom:1px solid var(--cizgi)}
.s-ust h2{display:flex;align-items:center;gap:10px;margin:0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:24px;letter-spacing:-.02em}
.s-ust h2 span{display:inline-grid;place-items:center;min-width:26px;height:26px;padding:0 7px;border-radius:999px;background:var(--lac);color:#fff;font-family:"Onest",sans-serif;font-size:13px;font-weight:700}
.kapat{width:48px;height:48px;display:grid;place-items:center;border:0;background:transparent}
.kapat svg,.ik svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.kargo-serit{display:flex;align-items:center;gap:8px;margin:12px 16px 0;padding:10px 12px;border-radius:12px;background:var(--zemin);font-size:13px;font-weight:600}
.kargo-serit svg{width:20px;height:20px;flex:none;fill:none;stroke:var(--lac);stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;animation:kamyon 2.6s ease-in-out infinite}
@keyframes kamyon{0%,100%{transform:translateX(-1px)}50%{transform:translateX(2px)}}
/* Ürün satırı */
.urun{display:grid;grid-template-columns:76px minmax(0,1fr);gap:12px;margin:14px 16px 0;padding-bottom:16px;border-bottom:1px solid var(--cizgi)}
.urun img{width:76px;height:76px;border-radius:12px;object-fit:cover;background:var(--zemin)}
.urun b{display:block;font-size:15px;line-height:1.3}
.urun small{display:block;margin-top:2px;font-size:13px;color:var(--soluk)}
.urun-alt{display:flex;align-items:center;justify-content:space-between;margin-top:10px}
.adet{display:inline-flex;align-items:center;height:40px;border-radius:999px;box-shadow:inset 0 0 0 1.5px var(--cizgi)}
.adet button{width:44px;height:40px;border:0;background:transparent;font-size:18px}
.adet span{min-width:22px;text-align:center;font-weight:700;font-variant-numeric:tabular-nums}
.urun-fiyat{text-align:right;font-variant-numeric:tabular-nums}
.urun-fiyat b{font-size:16px}
.sil{display:inline-flex;align-items:center;min-height:32px;margin-top:4px;padding:0;border:0;background:transparent;font-size:13px;color:var(--soluk);text-decoration:underline;text-underline-offset:3px}
/* Siparişine özel: dokununca eklenir, ay dolar */
.blok-bas{display:flex;align-items:baseline;justify-content:space-between;margin:22px 16px 10px}
.blok-bas b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:20px;letter-spacing:-.01em}
.blok-bas span{font-size:12px;color:var(--soluk)}
.teklif{display:grid;grid-template-columns:56px minmax(0,1fr) auto;gap:12px;align-items:center;width:calc(100% - 32px);margin:0 16px 10px;padding:10px 12px 10px 10px;border:0;border-radius:16px;background:#fff;text-align:left;box-shadow:inset 0 0 0 1.5px var(--cizgi);transition:transform .2s var(--ease)}
.teklif:active{transform:scale(.985)}
.teklif.on{box-shadow:inset 0 0 0 2px var(--lac);background:#F8F9FC}
.teklif img{width:56px;height:56px;border-radius:12px;object-fit:cover;background:var(--zemin)}
.teklif b{display:block;font-size:14px;line-height:1.3}
.teklif small{display:block;margin-top:2px;font-size:12px;color:var(--soluk)}
.teklif .tf{display:block;margin-top:3px;font-size:15px;font-weight:700;font-variant-numeric:tabular-nums}
.ekle{display:inline-flex;align-items:center;gap:6px;height:36px;padding:0 12px 0 8px;border-radius:999px;box-shadow:inset 0 0 0 1.5px var(--lac);font-size:13px;font-weight:700;white-space:nowrap}
.ekle svg{width:20px;height:20px}
.ekle svg circle{fill:none;stroke:var(--lac);stroke-width:1.6}
.ekle svg path{fill:var(--lac);opacity:0;transform-origin:12px 12px;transform:scale(.4) rotate(-30deg);transition:opacity .35s var(--ease),transform .45s var(--ease)}
.on .ekle{background:var(--lac);color:#fff}
.on .ekle svg circle{stroke:#fff}.on .ekle svg path{fill:#fff;opacity:1;transform:none}
/* Teslimat seçimi */
.tes{display:grid;grid-template-columns:22px minmax(0,1fr) auto;gap:12px;align-items:start;width:calc(100% - 32px);margin:0 16px 10px;padding:14px 14px 14px 12px;border:0;border-radius:16px;background:#fff;text-align:left;box-shadow:inset 0 0 0 1.5px var(--cizgi)}
.tes.on{box-shadow:inset 0 0 0 2px var(--lac)}
.tes b{display:block;font-size:15px}
.tes small{display:block;margin-top:2px;font-size:13px;color:var(--soluk);line-height:1.4}
.tes em{font-style:normal;font-weight:700;font-variant-numeric:tabular-nums;white-space:nowrap}
.nokta{width:22px;height:22px;border-radius:50%;box-shadow:inset 0 0 0 1.6px #B8C0D2}
.nokta i{display:block;width:12px;height:12px;margin:5px;border-radius:50%;background:var(--lac);opacity:0;transform:scale(.3);transition:opacity .25s var(--ease),transform .25s var(--ease)}
.on .nokta{box-shadow:inset 0 0 0 1.6px var(--lac)}.on .nokta i{opacity:1;transform:none}
/* Özet ve ödeme */
.ozet{margin:12px 16px 0;padding:14px 0 0;border-top:1px solid var(--cizgi);font-variant-numeric:tabular-nums}
.ozet p{display:flex;justify-content:space-between;margin:0 0 8px;font-size:14px;color:var(--soluk)}
.ozet p b{color:var(--lac);font-weight:600}
.ozet p.ind b{color:#2E6B4F}
.ozet .top{display:flex;justify-content:space-between;align-items:baseline;margin-top:12px;padding-top:12px;border-top:1px dashed var(--cizgi);color:var(--lac)}
.ozet .top span{font-size:15px;font-weight:600}
.ozet .top b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:28px;letter-spacing:-.02em}
.btn1{display:flex;align-items:center;justify-content:center;gap:12px;width:calc(100% - 32px);min-height:62px;margin:16px 16px 0;padding:8px 16px;border:0;border-radius:16px;background:var(--lac);box-shadow:0 3px 0 #0C1027;transition:transform .12s var(--ease)}
.pg .btn1{color:#fff}
.btn1:active{transform:translateY(3px)}
.btn1 .b-ic{display:flex;flex-direction:column;align-items:center;line-height:1.2}
.btn1 .b-ic>span{font-size:16px;font-weight:700}
.btn1 .b-ic small{margin-top:2px;font-size:12px;font-weight:600;color:#C9D2EC}
.btn1 svg{width:18px;height:18px;flex:none;fill:none;stroke:#fff;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;animation:durt 2.4s var(--ease) infinite}
@keyframes durt{0%,58%,100%{transform:none}68%{transform:translateX(5px)}78%{transform:none}86%{transform:translateX(3px)}94%{transform:none}}
.btn2{display:flex;align-items:center;justify-content:center;width:calc(100% - 32px);min-height:56px;margin:12px 16px 0;border-radius:16px;background:transparent;color:var(--lac);border:1.5px solid var(--lac);font-size:15px;font-weight:600}
.guven{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin:18px 16px 24px;text-align:center}
.guven span{display:flex;flex-direction:column;align-items:center;gap:4px;font-size:12px;color:var(--soluk);line-height:1.3}
.guven svg{width:22px;height:22px;fill:none;stroke:var(--lac);stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.s-not{margin:0 16px 20px;font-size:12px;color:var(--soluk)}
@media (prefers-reduced-motion:reduce){.pg *{animation:none!important;transition:none!important}}
"""

AY = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="%s"></path></svg>' % E.ay(.999)
OK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"></path></svg>'
KAMYON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7h11v8H3z"></path><path d="M14 10h4l3 3v2h-7"></path><circle cx="7" cy="17" r="1.8"></circle><circle cx="17" cy="17" r="1.8"></circle></svg>'

HTML = """<div class="pg" style="padding-bottom: 0">
  <div class="s-ust"><h2>Sepetin <span>{{adetToplam}}</span></h2><button class="kapat" type="button" aria-label="Sepeti kapat"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"></path></svg></button></div>
  <p class="kargo-serit">""" + KAMYON + """<span>{{kargoSerit}}</span></p>

  <div class="urun"><img src=\"""" + B + IMG['ld'] + """\" alt="LunaDream Gece Lambası">
    <div><b>LunaDream Gece Lambası</b><small>2 lamba · Kız + Erkek</small>
      <div class="urun-alt"><span class="adet"><button type="button" onClick="{{azalt}}" aria-label="Azalt">−</button><span aria-live="polite">{{adet}}</span><button type="button" onClick="{{arttir}}" aria-label="Arttır">+</button></span>
        <span class="urun-fiyat"><b>{{urunTutar}}</b><br><button class="sil" type="button">Kaldır</button></span></div></div></div>

  <!-- Siparişine özel: canlı sepetteki üç teklif. Dokununca eklenir; ay dolar. Mağaza fiyatı düz yazı (üstü çizili değil). -->
  <div class="blok-bas"><b>Siparişine özel</b><span>Yalnız bu siparişte</span></div>
  <sc-for list="{{teklif}}" as="t" hint-placeholder-count="3"><button class="{{t.cls}}" type="button" onClick="{{t.pick}}" aria-pressed="{{t.on}}"><img src="{{t.src}}" alt=""><span><b>{{t.n}}</b><small>{{t.alt}}</small><span class="tf">{{t.p}}</span></span><span class="ekle">""" + AY + """{{t.btn}}</span></button></sc-for>

  <div class="blok-bas" style="margin-top: 18px"><b>Teslimat</b></div>
  <sc-for list="{{teslimat}}" as="d" hint-placeholder-count="2"><button class="{{d.cls}}" type="button" onClick="{{d.pick}}" aria-pressed="{{d.on}}"><span class="nokta"><i></i></span><span><b>{{d.n}}</b><small>{{d.t}}</small></span><em>{{d.p}}</em></button></sc-for>

  <div class="ozet">
    <p><span>Ürünler</span><b>{{araUrun}}</b></p>
    <sc-if value="{{ekVar}}" hint-placeholder-val="{{true}}"><p><span>Siparişine özel</span><b>{{araEk}}</b></p></sc-if>
    <p><span>Kargo</span><b>{{kargoT}}</b></p>
    <p class="ind"><span>Kartla ödeme indirimi (%5)</span><b>−{{indirim}}</b></p>
    <div class="top"><span>Kartla toplam</span><b>{{toplam}}</b></div>
  </div>
  <button class="btn1" type="button"><span class="b-ic"><span>Güvenli Ödeme ile Öde · {{toplam}}</span><small>Kartla %5 indirim dahil</small></span>""" + OK + """</button>
  <button class="btn2" type="button">Kapıda Ödeme ile Sipariş Ver</button>
  <div class="guven">
    <span><svg viewBox="0 0 24 24"><path d="M4 12a8 8 0 1 0 2.3-5.6"></path><path d="M4 4v4h4"></path></svg>30 gün iade</span>
    <span><svg viewBox="0 0 24 24"><rect x="3" y="6" width="18" height="12" rx="2"></rect><path d="M3 10h18M7 15h4"></path></svg>Kart bilgin bize gelmez</span>
    <span><svg viewBox="0 0 24 24"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"></path></svg>WhatsApp destek</span>
  </div>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { adet: 1, ek: {}, hizli: false }; }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    """ + TL_JS + """
    var LD = 2749.99;  // LunaDream 2 lamba paketi
    var T = [
      { k: 'astronot', n: 'Astronot Nemlendirici', alt: 'Mağazada ₺799,00', p: 749.00, img: '""" + IMG['astronot'] + """' },
      { k: 'kum', n: 'Kum Saati Lamba', alt: 'Mağazada ₺799,00', p: 699.99, img: '""" + IMG['kum'] + """' },
      { k: 'nem', n: 'Yıldız Işığı Nemlendirici', alt: 'Mağazada ₺849,99', p: 749.99, img: '""" + IMG['nem'] + """' }
    ];
    var teklif = T.map(function (t) { var on = !!S.ek[t.k]; return { n: t.n, alt: t.alt, p: TL(t.p, true), src: B + t.img, on: on ? 'true' : 'false', cls: on ? 'teklif on' : 'teklif', btn: on ? 'Eklendi' : 'Ekle',
      pick: function () { var e = Object.assign({}, self.state.ek); e[t.k] = !e[t.k]; self.setState({ ek: e }); } }; });
    var AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
    var now = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kd = new Date(now); do { kd.setDate(kd.getDate() + 1); } while (kd.getDay() === 0 || kd.getDay() === 6);
    var t1 = new Date(kd); t1.setDate(t1.getDate() + 3); var t2 = new Date(kd); t2.setDate(t2.getDate() + 7);
    var teslim = t1.getMonth() === t2.getMonth() ? t1.getDate() + '–' + t2.getDate() + ' ' + AY[t2.getMonth()] : t1.getDate() + ' ' + AY[t1.getMonth()] + '–' + t2.getDate() + ' ' + AY[t2.getMonth()];
    var HIZLI = 79.99;
    var teslimat = [
      { n: 'Standart kargo', t: kd.getDate() + ' ' + AY[kd.getMonth()] + ' kargoda, ' + teslim + ' kapında', p: 'Ücretsiz', h: false },
      { n: 'Hızlı Kargo', t: 'Siparişin öncelikli hazırlanır, aynı gün kargoya verilir.', p: TL(HIZLI, true), h: true }
    ].map(function (d) { var on = S.hizli === d.h; return { n: d.n, t: d.t, p: d.p, on: on ? 'true' : 'false', cls: on ? 'tes on' : 'tes', pick: function () { self.setState({ hizli: d.h }); } }; });
    var urun = LD * S.adet, ek = 0, ekSay = 0;
    T.forEach(function (t) { if (S.ek[t.k]) { ek += t.p; ekSay++; } });
    var kargo = S.hizli ? HIZLI : 0;
    var indirim = Math.round((urun + ek) * 0.05 * 100) / 100;
    var toplam = Math.round((urun + ek - indirim + kargo) * 100) / 100;
    return {
      adet: S.adet, adetToplam: S.adet + ekSay, urunTutar: TL(urun, true),
      azalt: function () { if (self.state.adet > 1) self.setState({ adet: self.state.adet - 1 }); },
      arttir: function () { self.setState({ adet: self.state.adet + 1 }); },
      teklif: teklif, teslimat: teslimat, kargoSerit: S.hizli ? 'Hızlı Kargo · aynı gün kargoda' : 'Kargo ücretsiz · ' + kd.getDate() + ' ' + AY[kd.getMonth()] + ' kargoda',
      araUrun: TL(urun, true), ekVar: ekSay > 0, araEk: TL(ek, true), kargoT: kargo ? TL(kargo, true) : 'Ücretsiz',
      indirim: TL(indirim, true), toplam: TL(toplam, true)
    };
  }
}"""

if __name__ == '__main__':
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='Ayluna · Sepet', css=CSS) + HTML + TAIL.format(h=int(os.environ.get('S_H', 1290)), js=JS))
    print('yazıldı:', os.path.abspath(OUT))
