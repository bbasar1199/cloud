import sys
sys.path.insert(0,'.')
from ortak import HEAD, TAIL, TL_JS
import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'canvas') + '/'

# ---------- Ortak veri ve mantık (üç yönde aynı) ----------
DATA_JS = """
    var self = this, S = this.state, B = '/_blob/';
    // Galeri = Shopify ana ürün medyası. "Elif K." kartı ve yorum kolajı (mevzuat) hariç tutuldu.
    var G = [
      { id: '211acb76d908e8ed6d4f5fcddc987893', n: 'Masalsı gece ışığı' }, { id: 'ec0a99ef7b8839a12ab7e6aa4282f7da', n: 'Temalar' },
      { id: '652e1893a0ae33a24ee0e3d53edab757', n: 'Müşteri' }, { id: 'a08890007843d79d94bfffc397a3d0ac', n: 'Gece modu' },
      { id: 'd4efe7e83c74524ece75e962161f7fff', n: 'Deniz altı' }, { id: '3ddd8b8b95f040d436d5d0ea350924b8', n: 'Hediye' },
      { id: '98db755893dbcebe192c69e73ae5afff', n: 'Uzay Kaşifi' }
    ];
    var gal = G.map(function (g, i) { var on = i === S.g; return { src: B + g.id, n: g.n, on: on ? 'true' : 'false', op: on ? 1 : 0, cls: on ? 'kucuk on' : 'kucuk', pick: function () { self.setState({ g: i }); } }; });
    var kiz = S.model === 'kiz';
    var models = [
      { id: 'kiz', n: 'Kız', sub: 'Tavşanlı · ninnili', src: B + 'e02351b3be4a1c555c5d760d0bbda723' },
      { id: 'erkek', n: 'Erkek', sub: 'Robot · ninnisiz', src: B + '0033dfea6282c5bc479c385213661c00' }
    ].map(function (m) { var on = S.model === m.id; return { n: m.n, sub: m.sub, src: m.src, on: on ? 'true' : 'false', cls: on ? 'mkart on' : 'mkart', pick: function () { self.setState({ model: m.id }); } }; });
    // Paket: canlı sitedeki biçim. 1 Adet'te üstü çizili ₺1.999 (son 10 günde uygulandı, kullanıcı teyidi).
    // 2 Adet'te ₺3.998 gösterilmez (2'li paket bu fiyattan hiç satılmadıysa mevzuat riski); yerine birim fiyat.
    var P1 = 1699.99, P2 = 2749.99, C1 = 1999;
    var paket = [
      { n: 1, t: '1 Adet', p: TL(P1, true), old: TL(C1, true), sub: '%' + Math.round((1 - P1 / C1) * 100) + ' indirim', rib: false, imgs: 1 },
      { n: 2, t: '2 Adet', p: TL(P2, true), old: '', unit: 'tanesi ' + TL(P2 / 2), sub: '2 tekliden %' + Math.round((1 - P2 / (2 * P1)) * 100) + ' az', rib: true, imgs: 2 }
    ].map(function (b) { var on = S.adet === b.n; return { t: b.t, p: b.p, old: b.old, hasOld: !!b.old, unit: b.unit || '', hasUnit: !!b.unit, sub: b.sub, rib: b.rib, two: b.imgs === 2, on: on ? 'true' : 'false', cls: on ? 'pk on' : 'pk', pick: function () { self.setState({ adet: b.n }); } }; });
    var total = S.adet === 2 ? P2 : P1, ucret = 80, online = Math.round(total * 0.95 * 100) / 100, kapida = total + ucret;
    var AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
    var now = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kd = new Date(now); do { kd.setDate(kd.getDate() + 1); } while (kd.getDay() === 0 || kd.getDay() === 6);
    var t1 = new Date(kd); t1.setDate(t1.getDate() + 3); var t2 = new Date(kd); t2.setDate(t2.getDate() + 7);
    var teslim = t1.getMonth() === t2.getMonth() ? t1.getDate() + '–' + t2.getDate() + ' ' + AY[t2.getMonth()] : t1.getDate() + ' ' + AY[t1.getMonth()] + '–' + t2.getDate() + ' ' + AY[t2.getMonth()];
    var vals = {
      gal: gal, gNo: S.g + 1, gCount: G.length, models: models, paket: paket,
      modelName: kiz ? 'Kız · tavşanlı' : 'Erkek · Uzay Kaşifi',
      onLabel: 'Güvenli Ödeme İle Al · ' + TL(online, true),
      onNote: 'Kartla %5 indirim · kapıda ödemeye göre ' + TL(kapida - online, true) + ' az',
      kpNote: 'Kapıda ödeme ücreti ₺80 · toplam ' + TL(kapida, true),
      kargo: kd.getDate() + ' ' + AY[kd.getMonth()], teslim: teslim, kiz: kiz, erkek: !kiz,
      rating: '4,7', reviews: 62, starPct: 94
    };
"""
STATE = "{ g: 0, model: 'kiz', adet: 2 }"

def build(name, title, css, html, extra_js, h):
    js = "class Component extends DCLogic {\n  constructor(p) { super(p); this.state = " + STATE + "; }\n  renderVals() {\n    " + TL_JS + DATA_JS + extra_js + "\n    return vals;\n  }\n}"
    open(OUT+name,'w',encoding='utf-8').write(HEAD.format(title=title, css=css)+html+TAIL.format(h=h, js=js))

# Ortak parça şablonları (her yön kendi sınıflarıyla biçimlendirir)
MODEL_HTML = """<div class="etiket" style="margin-top: 22px"><span>Model</span><b>{{modelName}}</b></div>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-top: 8px">
        <sc-for list="{{models}}" as="m" hint-placeholder-count="2">
          <button class="{{m.cls}}" onClick="{{m.pick}}" aria-pressed="{{m.on}}"><span class="foto"><img src="{{m.src}}" alt=""></span><span style="display: flex; flex-direction: column; min-width: 0; line-height: 1.2"><b style="font-size: 14px; font-weight: 600">{{m.n}}</b><span class="msub">{{m.sub}}</span></span></button>
        </sc-for>
      </div>"""
PAKET_HTML = """<div style="display: flex; flex-direction: column; gap: 12px; margin-top: {top}">
        <sc-for list="{{paket}}" as="b" hint-placeholder-count="2">
          <button class="{{b.cls}}" onClick="{{b.pick}}" aria-pressed="{{b.on}}">
            <sc-if value="{{b.rib}}" hint-placeholder-val="{{false}}"><span class="kurdele">En Çok Tercih Edilen</span></sc-if>
            <span class="pk-ust">
              <span class="pk-foto"><img src="/_blob/e02351b3be4a1c555c5d760d0bbda723" alt=""><sc-if value="{{b.two}}" hint-placeholder-val="{{false}}"><img class="iki" src="/_blob/e02351b3be4a1c555c5d760d0bbda723" alt=""></sc-if></span>
              <span style="display: flex; flex-direction: column; min-width: 0; line-height: 1.2"><b class="pk-ad">{{b.t}}</b><span class="pk-sub">{{b.sub}}</span></span>
              <span style="display: flex; flex-direction: column; align-items: flex-end; line-height: 1.15; font-variant-numeric: tabular-nums"><b class="pk-fiyat">{{b.p}}</b><sc-if value="{{b.hasOld}}" hint-placeholder-val="{{true}}"><s class="pk-eski">{{b.old}}</s></sc-if><sc-if value="{{b.hasUnit}}" hint-placeholder-val="{{false}}"><span class="pk-eski" style="text-decoration: none">{{b.unit}}</span></sc-if></span>
            </span>
            <span class="pk-hediye">+ 6 Tane Ücretsiz Hediye Disk</span>
          </button>
        </sc-for>
      </div>"""
BTN_HTML = """<button class="btn-on" type="button">{{onLabel}}</button>
      <p class="bnot">{{onNote}}</p>
      <!-- Canlıda kapıda ödeme uygulamasının formunu açar (uygulama korunur). -->
      <button class="btn-kp" type="button">Kapıda Ödeme ile Sipariş Ver</button>
      <p class="bnot">{{kpNote}}</p>"""
YOL_HTML = """<ol class="yol" aria-label="Siparişten teslime">
        <li><b>Bugün</b><span>Siparişin alındı</span></li>
        <li><b>{{kargo}}</b><span>Kargoda</span></li>
        <li><b>{{teslim}}</b><span>Kapında</span></li>
      </ol>"""

# =========================================================
# A · MASAL KİTABI — yazı ağırlıklı, kâğıt, kemer pencere
# =========================================================
cssA = """.pg{background:#F4EDE2}
.kagit{background-image:radial-gradient(rgba(120,90,50,.07) 1px,transparent 1.2px);background-size:7px 7px}
.ust{display:flex;justify-content:space-between;align-items:center;height:56px}
.kemer{position:relative;margin:0 16px;height:430px;border-radius:200px 200px 18px 18px;overflow:hidden;background:#141A36;border:1.5px solid #1A2142}
.kemer img.ana{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .45s cubic-bezier(.2,.7,.2,1)}
.kucuk{flex:none;width:52px;height:64px;padding:0;border-radius:26px 26px 8px 8px;border:1.5px solid #D9CDB9;background:#EDE3D3;overflow:hidden;cursor:pointer;transition:transform .2s cubic-bezier(.2,.7,.2,1),border-color .2s}
.kucuk.on{border-color:#1A2142;transform:translateY(-4px)}
.kucuk img{width:100%;height:100%;object-fit:cover;display:block}
.baslik{font-family:"Young Serif",Georgia,serif;font-size:54px;line-height:.92;letter-spacing:-.035em;margin:18px 0 0}
.alt{font-family:"Young Serif",Georgia,serif;font-size:19px;line-height:1.3;color:#5C6078;margin:10px 0 0;font-style:italic}
.cizgi{height:1px;background:#1A2142;opacity:.18;margin:18px 0}
.mkart{display:grid;grid-template-columns:52px minmax(0,1fr);gap:10px;align-items:center;min-height:68px;padding:7px 10px 7px 8px;border-radius:14px;border:1.5px solid #D9CDB9;background:transparent;font:inherit;color:#1A2142;text-align:left;cursor:pointer;transition:border-color .25s,background .25s}
.mkart.on{border-color:#1A2142;background:#FFFDF9}
.mkart .foto{width:52px;height:52px;border-radius:26px 26px 8px 8px;overflow:hidden;background:#EFE6D8}
.mkart .foto img{width:100%;height:100%;object-fit:cover;transform:scale(1.5);transform-origin:50% 62%}
.msub{font-size:12px;color:#5C6078;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pk{position:relative;display:block;width:100%;padding:0;border:1.5px solid #D9CDB9;border-radius:16px;background:#FFFDF9;font:inherit;color:#1A2142;text-align:left;cursor:pointer;overflow:visible;transition:border-color .25s,transform .2s cubic-bezier(.2,.7,.2,1)}
.pk.on{border-color:#1A2142;box-shadow:0 0 0 3px rgba(26,33,66,.08)}
.pk:active{transform:scale(.985)}
.pk-ust{display:grid;grid-template-columns:62px minmax(0,1fr) auto;gap:12px;align-items:center;padding:14px}
.pk-foto{position:relative;width:62px;height:56px}
.pk-foto img{position:absolute;left:0;top:0;width:52px;height:52px;border-radius:26px 26px 8px 8px;object-fit:cover;background:#EFE6D8;border:1.5px solid #FFFDF9}
.pk-foto img.iki{left:16px;top:6px}
.pk-ad{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:22px;letter-spacing:-.01em}
.pk-sub{font-size:13px;color:#5C6078;margin-top:2px}
.pk-fiyat{font-size:19px;font-weight:700;letter-spacing:-.02em}
.pk-eski{font-size:13px;color:#5C6078;margin-top:3px}
.pk-hediye{display:block;padding:9px 14px;border-top:1.5px dashed #D9CDB9;font-size:13.5px;font-weight:600;color:#8A4A12;background:#F7EBD8;border-radius:0 0 14px 14px}
.pk.on .pk-hediye{border-top-color:#1A2142}
.kurdele{position:absolute;right:14px;top:-12px;padding:3px 10px;border-radius:6px;background:#1A2142;color:#F3E9DA;font-size:12px;font-weight:600;font-family:"Young Serif",Georgia,serif;letter-spacing:.01em}
.btn-on{display:flex;align-items:center;justify-content:center;width:100%;min-height:58px;margin-top:18px;border:0;border-radius:16px;background:#1A2142;color:#FFFDF9;font:inherit;font-size:17px;font-weight:600;cursor:pointer}
.btn-kp{display:flex;align-items:center;justify-content:center;width:100%;min-height:54px;margin-top:12px;border:1.5px solid #1A2142;border-radius:16px;background:transparent;color:#1A2142;font:inherit;font-size:16px;font-weight:600;cursor:pointer}
.bnot{margin:6px 0 0;text-align:center;font-size:13px;color:#5C6078}
.yol{list-style:none;padding:0;margin:20px 0 0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-top:1px solid rgba(26,33,66,.18);border-bottom:1px solid rgba(26,33,66,.18)}
.yol li{padding:12px 6px;text-align:center;display:flex;flex-direction:column;gap:2px}
.yol li+li{border-left:1px solid rgba(26,33,66,.12)}
.yol b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:18px}
.yol span{font-size:12.5px;color:#5C6078}
.masal{font-family:"Young Serif",Georgia,serif;font-size:27px;line-height:1.22;letter-spacing:-.015em;margin:0}
.masal u{text-decoration:none;background:linear-gradient(transparent 62%,rgba(242,166,90,.45) 62%)}
.masal .ilk{float:left;font-size:76px;line-height:.82;margin:6px 8px 0 0;color:#E59A4C}
.pencere{flex:0 0 180px;height:240px;border-radius:90px 90px 14px 14px;overflow:hidden;background:#EDE3D3;border:1.5px solid #1A2142}
.pencere img{width:100%;height:100%;object-fit:cover;display:block}
.noscroll{scrollbar-width:none}.noscroll::-webkit-scrollbar{display:none}"""
htmlA = """<div class="pg kagit" style="padding-bottom: 36px">
  <header class="px ust"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 8h16M4 16h11"></path></svg><span style="display: flex; align-items: center; gap: 6px"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M15.5 3.5a8.5 8.5 0 1 0 5 15.4A7 7 0 0 1 15.5 3.5z" fill="#E59A4C"></path></svg><span class="ser" style="font-size: 22px">Ayluna</span></span><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 8h12l-1 12H7z"></path><path d="M9 8a3 3 0 0 1 6 0"></path></svg></header>

  <!-- Galeri: kemer pencere, ana ürün fotoğrafları -->
  <section class="kemer" aria-label="LunaDream fotoğrafları">
    <sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><img class="ana" src="{{f.src}}" alt="{{f.n}}" style="opacity: {{f.op}}"></sc-for>
    <span style="position: absolute; right: 14px; bottom: 12px; font-size: 13px; font-weight: 600; color: #FFFDF9; background: rgba(12,16,39,.5); padding: 3px 9px; border-radius: 999px; font-variant-numeric: tabular-nums">{{gNo}} / {{gCount}}</span>
  </section>
  <div class="noscroll" style="display: flex; gap: 8px; overflow-x: auto; padding: 14px 16px 4px">
    <sc-for list="{{gal}}" as="f" hint-placeholder-count="7"><button class="{{f.cls}}" onClick="{{f.pick}}" aria-label="{{f.n}}" aria-pressed="{{f.on}}"><img src="{{f.src}}" alt=""></button></sc-for>
  </div>

  <div class="px">
    <a href="#yorumlar" style="display: inline-flex; align-items: center; gap: 6px; margin-top: 14px; font-size: 13.5px; text-decoration: none; color: #5C6078"><span style="color: #E59A4C">★★★★★</span><b style="color: #1A2142">{{rating}}</b> · {{reviews}} yorum</a>
    <h1 class="baslik">LunaDream</h1>
    <p class="alt">Işığı kapattığında tavanda masal başlar.</p>
    <div class="cizgi"></div>
    """ + MODEL_HTML + """
    <div class="etiket" style="margin-top: 22px"><span>Paket</span><span style="color: #5C6078; font-weight: 500">Sınırlı süreli teklif</span></div>
    """ + PAKET_HTML.replace('{top}','14px') + """
    """ + BTN_HTML + """
    """ + YOL_HTML + """
  </div>

  <!-- Fayda: ikon yok; masal gibi tek paragraf + iki pencere -->
  <section class="px" style="margin-top: 44px">
    <p class="masal"><span class="ilk">K</span>ubbeyi aç, <u>altı masal diskinden</u> birini tak. Işığı kapat; tavan bir anda <u>okyanusa, uzaya ya da şatoya</u> döner. Kız modelinde <u>ninni</u> telefondan çalar. Sabah <u>şarja</u> tak, akşam yine hazır.</p>
  </section>
  <div class="noscroll" style="display: flex; gap: 12px; overflow-x: auto; padding: 22px 16px 0">
    <div class="pencere"><img src="/_blob/a08890007843d79d94bfffc397a3d0ac" alt="Gece modu"></div>
    <div class="pencere"><img src="/_blob/d4efe7e83c74524ece75e962161f7fff" alt="Deniz altı teması"></div>
    <div class="pencere"><img src="/_blob/ec0a99ef7b8839a12ab7e6aa4282f7da" alt="Temalar"></div>
  </div>
</div>
"""
build('YonA-MasalKitabi.dc.html','Yön A · Masal Kitabı',cssA,htmlA,'',2050)

# =========================================================
# B · GECE POSTASI — cesur renk blokları, poster yazı
# =========================================================
cssB = """.pg{background:#F6F1E9}
.ust{display:flex;justify-content:space-between;align-items:center;height:56px;background:#1A2142;color:#FFFDF9}
.galeri{position:relative;height:410px;background:#1A2142;overflow:hidden}
.galeri img.ana{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .45s cubic-bezier(.2,.7,.2,1)}
.sayac{position:absolute;left:16px;bottom:14px;font-family:"Young Serif",Georgia,serif;font-size:44px;line-height:1;color:#F2A65A;font-variant-numeric:tabular-nums}
.sayac small{font-size:20px;color:#FFFDF9;opacity:.8}
.kucuk{flex:none;width:58px;height:58px;padding:0;border-radius:12px;border:3px solid transparent;background:#232B55;overflow:hidden;cursor:pointer;transition:border-color .2s,transform .2s cubic-bezier(.2,.7,.2,1)}
.kucuk.on{border-color:#F2A65A;transform:translateY(-3px)}
.kucuk img{width:100%;height:100%;object-fit:cover;display:block}
.bant{background:#1A2142;padding:12px 0 18px}
.dev{font-family:"Young Serif",Georgia,serif;font-size:62px;line-height:.86;letter-spacing:-.045em;margin:0;color:#1A2142}
.dev span{color:#E59A4C}
.etiket>span:first-child{color:#766B5B}
.mkart{display:grid;grid-template-columns:52px minmax(0,1fr);gap:10px;align-items:center;min-height:70px;padding:8px 10px 8px 8px;border-radius:18px;border:2px solid #1A2142;background:#FFFDF9;font:inherit;color:#1A2142;text-align:left;cursor:pointer;transition:background .25s,color .25s}
.mkart.on{background:#1A2142;color:#FFFDF9}
.mkart.on .msub{color:#B9BED6}
.mkart .foto{width:52px;height:52px;border-radius:12px;overflow:hidden;background:#F4C9B8}
.mkart .foto img{width:100%;height:100%;object-fit:cover;transform:scale(1.5);transform-origin:50% 62%}
.msub{font-size:12px;color:#5C6078;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pk{position:relative;display:block;width:100%;padding:0;border:2px solid #1A2142;border-radius:20px;background:#FFFDF9;font:inherit;color:#1A2142;text-align:left;cursor:pointer;overflow:visible;transition:background .25s,color .25s,transform .2s cubic-bezier(.2,.7,.2,1)}
.pk.on{background:#1A2142;color:#FFFDF9}
.pk:active{transform:scale(.985)}
.pk-ust{display:grid;grid-template-columns:70px minmax(0,1fr) auto;gap:12px;align-items:center;padding:16px 14px 14px}
.pk-foto{position:relative;width:70px;height:60px}
.pk-foto img{position:absolute;left:0;top:0;width:56px;height:56px;border-radius:50%;object-fit:cover;background:#F4C9B8;border:2px solid #FFFDF9}
.pk .pk-ust{border-radius:18px 18px 0 0}
.pk-foto img.iki{left:16px;top:4px}
.pk-ad{font-size:24px;font-weight:700;letter-spacing:-.02em}
.pk-sub{font-size:13px;opacity:.75;margin-top:2px}
.pk-fiyat{font-size:21px;font-weight:700;letter-spacing:-.02em}
.pk.on .pk-fiyat{color:#F2A65A}
.pk-eski{font-size:13px;opacity:.65;margin-top:3px}
.pk-hediye{display:block;padding:10px 14px;font-size:14px;font-weight:700;background:#F4C9B8;color:#1A2142;border-radius:0 0 18px 18px}
.pk.on .pk-hediye{background:#F2A65A}
.kurdele{position:absolute;right:14px;top:-14px;z-index:1;padding:4px 12px;border-radius:10px;background:#E59A4C;color:#1A2142;font-size:12px;font-weight:700;letter-spacing:.02em;border:2px solid #1A2142}
.btn-on{display:flex;align-items:center;justify-content:center;width:100%;min-height:62px;margin-top:18px;border:0;border-radius:20px;background:#F2A65A;color:#1A2142;font:inherit;font-size:18px;font-weight:700;cursor:pointer;box-shadow:0 6px 0 #C97F38}
.btn-on:active{transform:translateY(3px);box-shadow:0 3px 0 #C97F38}
.btn-kp{display:flex;align-items:center;justify-content:center;width:100%;min-height:58px;margin-top:14px;border:0;border-radius:20px;background:#1A2142;color:#FFFDF9;font:inherit;font-size:17px;font-weight:600;cursor:pointer}
.bnot{margin:8px 0 0;text-align:center;font-size:13px;color:#5C6078}
.yol{list-style:none;padding:0;margin:22px 0 0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}
.yol li{padding:12px 8px;border-radius:14px;background:#FFFDF9;border:2px solid #1A2142;display:flex;flex-direction:column;gap:2px}
.yol li:last-child{background:#F4C9B8}
.yol b{font-size:16px;font-weight:700}
.yol span{font-size:12.5px;color:#3A3F5A}
.poster{border-radius:24px;padding:20px 18px;display:flex;flex-direction:column;gap:6px}
.poster b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:46px;line-height:.9;letter-spacing:-.03em}
.poster span{font-size:15px;line-height:1.35}
.noscroll{scrollbar-width:none}.noscroll::-webkit-scrollbar{display:none}"""
htmlB = """<div class="pg" style="padding-bottom: 36px">
  <header class="px ust"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 8h16M4 16h11"></path></svg><span style="display: flex; align-items: center; gap: 6px"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M15.5 3.5a8.5 8.5 0 1 0 5 15.4A7 7 0 0 1 15.5 3.5z" fill="#F2A65A"></path></svg><span class="ser" style="font-size: 22px">Ayluna</span></span><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 8h12l-1 12H7z"></path><path d="M9 8a3 3 0 0 1 6 0"></path></svg></header>
  <section class="galeri" aria-label="LunaDream fotoğrafları">
    <sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><img class="ana" src="{{f.src}}" alt="{{f.n}}" style="opacity: {{f.op}}"></sc-for>
    <span class="sayac">{{gNo}}<small> / {{gCount}}</small></span>
  </section>
  <div class="bant">
    <div class="noscroll" style="display: flex; gap: 8px; overflow-x: auto; padding: 0 16px">
      <sc-for list="{{gal}}" as="f" hint-placeholder-count="7"><button class="{{f.cls}}" onClick="{{f.pick}}" aria-label="{{f.n}}" aria-pressed="{{f.on}}"><img src="{{f.src}}" alt=""></button></sc-for>
    </div>
  </div>

  <div class="px" style="padding-top: 22px">
    <a href="#yorumlar" style="display: inline-flex; align-items: center; gap: 6px; font-size: 13.5px; text-decoration: none; color: #5C6078"><span style="color: #E59A4C">★★★★★</span><b style="color: #1A2142">{{rating}}</b> · {{reviews}} yorum</a>
    <h1 class="dev" style="margin-top: 10px">Luna<br>Dream<span>.</span></h1>
    <p style="margin: 10px 0 0; font-size: 17px; font-weight: 600">Tavana masal yansıtan gece lambası.</p>
    """ + MODEL_HTML + """
    <div class="etiket" style="margin-top: 22px"><span>Paket</span><span style="font-weight: 700">Sınırlı süreli teklif</span></div>
    """ + PAKET_HTML.replace('{top}','10px') + """
    """ + BTN_HTML + """
    """ + YOL_HTML + """
  </div>

  <!-- Fayda: ikon yok; poster gibi büyük kelime + tek cümle, renk blokları -->
  <div class="noscroll" style="display: flex; gap: 10px; overflow-x: auto; padding: 40px 16px 0; scroll-snap-type: x mandatory">
    <div class="poster" style="flex: 0 0 250px; background: #1A2142; color: #FFFDF9; scroll-snap-align: start"><b style="color: #F2A65A">6 + 6</b><span>Altı masal diski kutuda, altısı hediye. Her disk tavana başka bir masal.</span></div>
    <div class="poster" style="flex: 0 0 250px; background: #F4C9B8; color: #1A2142; scroll-snap-align: start"><b>Ninni</b><span>Kız modelinde telefonundan bağlan, ninni lambadan çalsın.</span></div>
    <div class="poster" style="flex: 0 0 250px; background: #F2A65A; color: #1A2142; scroll-snap-align: start"><b>Şarjlı</b><span>Kablo yok. Komodinden yatağın yanına taşı, sabah şarja tak.</span></div>
  </div>
</div>
"""
build('YonB-GecePostasi.dc.html','Yön B · Gece Postası',cssB,htmlB,'',2000)

# =========================================================
# C · YÖRÜNGE — disk ve ay daireleri, ürüne özgü imza
# =========================================================
cssC = """.pg{background:#F6F1E9}
.ust{display:flex;justify-content:space-between;align-items:center;height:56px}
.sahne{position:relative;height:440px;overflow:hidden;background:radial-gradient(120% 80% at 50% 38%,#232B55 0%,#141A36 58%,#F6F1E9 58.2%)}
.daire{position:absolute;left:50%;top:26px;width:330px;height:330px;margin-left:-165px;border-radius:50%;overflow:hidden;box-shadow:0 0 0 10px rgba(242,166,90,.12),0 0 0 22px rgba(242,166,90,.06)}
.daire img.ana{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .5s cubic-bezier(.2,.7,.2,1),transform .5s cubic-bezier(.2,.7,.2,1)}
.yorunge{position:absolute;left:50%;top:-14px;width:410px;height:410px;margin-left:-205px;border-radius:50%;border:1px dashed rgba(255,253,249,.22)}
.kucuk{flex:none;width:54px;height:54px;padding:0;border-radius:50%;border:2px solid #D9CDB9;background:#EDE3D3;overflow:hidden;cursor:pointer;transition:transform .25s cubic-bezier(.2,.7,.2,1),border-color .2s}
.kucuk.on{border-color:#E59A4C;transform:scale(1.1)}
.kucuk img{width:100%;height:100%;object-fit:cover;display:block}
.baslik{font-family:"Young Serif",Georgia,serif;font-size:48px;line-height:.95;letter-spacing:-.03em;margin:8px 0 0;text-align:center}
.alt{margin:8px 0 0;text-align:center;font-size:16px;color:#5C6078}
.mkart{display:grid;grid-template-columns:54px minmax(0,1fr);gap:10px;align-items:center;min-height:70px;padding:7px 12px 7px 7px;border-radius:999px;border:1.5px solid #D9CDB9;background:transparent;font:inherit;color:#1A2142;text-align:left;cursor:pointer;transition:border-color .25s,background .25s}
.mkart.on{border-color:#1A2142;background:#FFFDF9}
.mkart .foto{width:54px;height:54px;border-radius:50%;overflow:hidden;background:#EFE6D8}
.mkart .foto img{width:100%;height:100%;object-fit:cover;transform:scale(1.5);transform-origin:50% 62%}
.msub{font-size:12px;color:#5C6078;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pk{position:relative;display:block;width:100%;padding:0;border:1.5px solid #D9CDB9;border-radius:22px;background:#FFFDF9;font:inherit;color:#1A2142;text-align:left;cursor:pointer;overflow:visible;transition:border-color .25s,transform .2s cubic-bezier(.2,.7,.2,1)}
.pk.on{border-color:#1A2142}
.pk:active{transform:scale(.985)}
.pk-ust{display:grid;grid-template-columns:72px minmax(0,1fr) auto;gap:12px;align-items:center;padding:14px}
.pk-foto{position:relative;width:72px;height:60px}
.pk-foto img{position:absolute;left:0;top:0;width:56px;height:56px;border-radius:50%;object-fit:cover;background:#EFE6D8;box-shadow:0 0 0 3px #FFFDF9,0 0 0 4px #E3D8C7}
.pk-foto img.iki{left:18px;top:4px}
.pk.on .pk-foto img{box-shadow:0 0 0 3px #FFFDF9,0 0 0 5px #E59A4C}
.pk-ad{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:23px}
.pk-sub{font-size:13px;color:#5C6078;margin-top:2px}
.pk-fiyat{font-size:19px;font-weight:700;letter-spacing:-.02em}
.pk-eski{font-size:13px;color:#5C6078;margin-top:3px}
.pk-hediye{display:flex;align-items:center;gap:8px;padding:9px 14px;font-size:13.5px;font-weight:600;background:#141A36;color:#F3E9DA;border-radius:0 0 20px 20px}
.pk-hediye::before{content:"";width:14px;height:14px;border-radius:50%;background:radial-gradient(circle,#F2A65A 0 3px,transparent 3.5px),conic-gradient(#E59A4C,#F3E9DA,#E59A4C);flex:none}
.kurdele{position:absolute;right:16px;top:-13px;z-index:1;padding:3px 12px;border-radius:999px;background:#F2A65A;color:#1A2142;font-size:12px;font-weight:700;box-shadow:0 0 0 3px #F6F1E9}
.btn-on{display:flex;align-items:center;justify-content:center;width:100%;min-height:60px;margin-top:18px;border:0;border-radius:999px;background:#1A2142;color:#FFFDF9;font:inherit;font-size:17px;font-weight:600;cursor:pointer}
.btn-kp{display:flex;align-items:center;justify-content:center;width:100%;min-height:56px;margin-top:12px;border:1.5px solid #1A2142;border-radius:999px;background:transparent;color:#1A2142;font:inherit;font-size:16px;font-weight:600;cursor:pointer}
.bnot{margin:6px 0 0;text-align:center;font-size:13px;color:#5C6078}
.yol{position:relative;list-style:none;padding:0;margin:22px 0 0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr))}
.yol::before{content:"";position:absolute;left:16.6%;right:16.6%;top:13px;border-top:1.5px dashed #C9BFAE}
.yol li{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;gap:2px}
.yol li::before{content:"";width:26px;height:26px;border-radius:50%;background:#F6F1E9;border:1.5px solid #1A2142;margin-bottom:6px;box-shadow:inset 0 0 0 5px #F6F1E9,inset 0 0 0 13px #E3D8C7}
.yol li:first-child::before{box-shadow:inset 0 0 0 5px #F6F1E9,inset 0 0 0 13px #F2A65A}
.yol b{font-size:15px;font-weight:600}
.yol span{font-size:12.5px;color:#5C6078}
.disk{flex:0 0 200px;display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center}
.disk .d{width:180px;height:180px;border-radius:50%;overflow:hidden;box-shadow:0 0 0 6px #FFFDF9,0 0 0 7px #E3D8C7}
.disk .d img{width:100%;height:100%;object-fit:cover;display:block}
.disk b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:20px;line-height:1.1}
.disk span{font-size:13.5px;color:#5C6078;line-height:1.35;max-width:180px}
.noscroll{scrollbar-width:none}.noscroll::-webkit-scrollbar{display:none}"""
htmlC = """<div class="pg" style="padding-bottom: 36px">
  <section class="sahne" aria-label="LunaDream fotoğrafları">
    <header class="px ust" style="position: relative; z-index: 2; color: #FFFDF9"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 8h16M4 16h11"></path></svg><span style="display: flex; align-items: center; gap: 6px"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M15.5 3.5a8.5 8.5 0 1 0 5 15.4A7 7 0 0 1 15.5 3.5z" fill="#F2A65A"></path></svg><span class="ser" style="font-size: 22px">Ayluna</span></span><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 8h12l-1 12H7z"></path><path d="M9 8a3 3 0 0 1 6 0"></path></svg></header>
    <span class="yorunge" aria-hidden="true"></span>
    <div class="daire" style="top: 64px">
      <sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><img class="ana" src="{{f.src}}" alt="{{f.n}}" style="opacity: {{f.op}}"></sc-for>
    </div>
  </section>
  <div class="noscroll" style="display: flex; gap: 10px; overflow-x: auto; padding: 0 16px 6px; margin-top: -22px; position: relative; justify-content: flex-start">
    <sc-for list="{{gal}}" as="f" hint-placeholder-count="7"><button class="{{f.cls}}" onClick="{{f.pick}}" aria-label="{{f.n}}" aria-pressed="{{f.on}}"><img src="{{f.src}}" alt=""></button></sc-for>
  </div>

  <div class="px">
    <p style="margin: 14px 0 0; text-align: center; font-size: 13.5px; color: #5C6078"><span style="color: #E59A4C">★★★★★</span> <b style="color: #1A2142">{{rating}}</b> · {{reviews}} yorum</p>
    <h1 class="baslik">LunaDream</h1>
    <p class="alt">Her disk tavana başka bir masal.</p>
    """ + MODEL_HTML + """
    <div class="etiket" style="margin-top: 22px"><span>Paket</span><span style="color: #5C6078; font-weight: 500">Sınırlı süreli teklif</span></div>
    """ + PAKET_HTML.replace('{top}','10px') + """
    """ + BTN_HTML + """
    """ + YOL_HTML + """
  </div>

  <!-- Fayda: ikon yok; her fayda bir disk gibi daire fotoğraf + tek cümle -->
  <div class="noscroll" style="display: flex; gap: 14px; overflow-x: auto; padding: 44px 16px 0; scroll-snap-type: x mandatory">
    <div class="disk" style="scroll-snap-align: start"><span class="d"><img src="/_blob/ec0a99ef7b8839a12ab7e6aa4282f7da" alt="Tema diskleri"></span><b>6 + 6 masal</b><span>Altısı kutuda, altısı hediye.</span></div>
    <div class="disk" style="scroll-snap-align: start"><span class="d"><img src="/_blob/a08890007843d79d94bfffc397a3d0ac" alt="Tavanda yıldızlar"></span><b>Tavanda masal</b><span>Işığı kapat, oda masala döner.</span></div>
    <div class="disk" style="scroll-snap-align: start"><span class="d"><img src="/_blob/3ddd8b8b95f040d436d5d0ea350924b8" alt="Elde iki lamba"></span><b>Şarjlı, avuç içi</b><span>Kablo yok, her odaya taşı.</span></div>
  </div>
</div>
"""
build('YonC-Yorunge.dc.html','Yön C · Yörünge',cssC,htmlC,'',2000)
print('ok')
