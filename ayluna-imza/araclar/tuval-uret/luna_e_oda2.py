# LunaDream · E için "Odası böyle görünecek" 4 kart, premium arayüz seçenekleri (21 Eki). Çalıştır: python3 luna_e_oda2.py
# Kullanıcı: "Bir gece, beş an bir şey hissettirmiyor" → benzer marka araştırması → eleştirmen Fikir 3'ü seçti
# (çocuk + lamba + tavandaki ışık aynı karede, kaydırmalı 4 kart, Bir gece'nin yerine). Kullanıcı: "1 mantıklı ama ona biraz
# UI ekleyelim, premium bir his versin müşterilere."
# Dört kart: Tavanda masal (Kız) · Birlikte dinleyin (ninni) · Tavanda uzay (Erkek) · Masalı o seçsin (disk).
# Görseller bu panoda yer tutucu (tuvaldeki oda fotoğrafları); çocuklu kareler Google Flow'dan gelecek, "müşteri" etiketi yok.
# B+ dili korunur: Young Serif + Onest, krem/lacivert/tek amber, ay evresi işareti, tek eğri, yalnız transform/opacity.
#   A · Gece vitrini: koyu bant, ortadaki kart odakta (öbürleri küçülür, söner), yazı şeridin altında değişir, ay evresi gezgini
#   B · Kemerli pencere: krem zemin, fotoğraf kemer pencerede ve iç çerçevede, çizgi üstünde kayan ay
#   C · Deste: kartlar üst üste, dokununca öndeki kenara kayar, arkadaki öne gelir
#   D · Hikâye: Instagram hikâyesi gibi tek büyük kart, üstte 4 parça çubuk, sağa/sola dokununca geçer (yazı fotoğrafın altında, ürüne binmez)
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE-Oda2.dc.html')


def ay(f, r=9, c=12):
    rx = abs(1 - 2 * f) * r
    return 'M%d %dA%d %d 0 0 1 %d %dA%.2f %d 0 0 %d %d %dZ' % (c, c - r, r, r, c, c + r, rx, r, 0 if f < .5 else 1, c, c - r)


EVRE = [.25, .5, .75, 1]
OK = '<svg class="ok-ik" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"></path></svg>'
GERI = '<svg class="ok-ik" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 12H6M11 6l-6 6 6 6"></path></svg>'
EV_SVG = '<svg class="evre" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="{{%s}}"></path></svg>'

CSS = r""".pg{background:#F6F1E9;font-size:15px}
.noscroll{scrollbar-width:none}.noscroll::-webkit-scrollbar{display:none}
.sec{padding:0 0 40px}
.oneri{display:flex;align-items:center;gap:8px;margin:0 16px 6px;padding-top:16px;border-top:1px dashed #D6CAB6;font-size:12px;font-weight:700;color:#A05A1C}
.oneri .evre{width:14px;height:14px}
.oneri-alt{margin:0 16px 18px;font-size:13px;color:#5C6078;text-wrap:balance}
.evre circle{fill:none;stroke:#1A2142;stroke-width:1.6}
.evre path{fill:#F2A65A}
.h2{font-size:26px;line-height:1.08}
.h2 span.n{color:#F2A65A}
.pg button{font:inherit;cursor:pointer;-webkit-tap-highlight-color:transparent}
.pg button:focus-visible{outline:2px solid #F2A65A;outline-offset:3px}
.ok-ik{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;flex:none}
.cip{display:inline-flex;align-items:center;gap:6px;padding:5px 11px 5px 7px;border-radius:999px;background:rgba(255,253,249,.94);color:#1A2142;font-size:12px;font-weight:700;line-height:1.2}
.cip .evre{width:14px;height:14px}
img{display:block}

/* A · Gece vitrini: koyu bant; kart 280, yanlarda 55px pay, ortadaki odakta */
.a-bol{background:#141A36;color:#FFFDF9;padding:28px 0 26px}
.a-ust{display:flex;align-items:flex-end;justify-content:space-between;padding:0 16px}
.a-ust .h2{color:#FFFDF9}
.a-say{font-family:"Young Serif",Georgia,serif;font-size:15px;color:#B9BED6;font-variant-numeric:tabular-nums}
.a-say b{font-weight:400;font-size:26px;color:#FFFDF9}
.a-serit{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;padding:22px 55px 0}
.a-kart{position:relative;flex:0 0 280px;height:380px;border-radius:22px;overflow:hidden;background:#0C1027;scroll-snap-align:center;transform:scale(.9);opacity:.45;transition:transform .5s cubic-bezier(.2,.7,.2,1),opacity .5s cubic-bezier(.2,.7,.2,1)}
.a-kart.on{transform:none;opacity:1}
.a-kart img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.a-kart .cip{position:absolute;left:12px;top:12px}
.a-kart::after{content:"";position:absolute;inset:0;border-radius:22px;box-shadow:inset 0 0 0 1px rgba(255,253,249,.14);pointer-events:none}
.a-metin{min-height:132px;padding:20px 24px 0;text-align:center}
.a-bas{margin:0;font-family:"Young Serif",Georgia,serif;font-size:26px;line-height:1.1;letter-spacing:-.015em}
.a-bas span{color:#F2A65A}
.a-yazi{margin:8px auto 0;max-width:300px;font-size:15px;line-height:1.45;color:#B9BED6;text-wrap:balance}
.a-sec{display:inline-flex;align-items:center;gap:6px;min-height:48px;margin-top:6px;padding:0 4px;border:0;background:none;color:#F2A65A;font-size:14px;font-weight:700}
.a-aylar{position:relative;display:flex;justify-content:center;gap:28px;margin-top:10px}
.a-aylar::before{content:"";position:absolute;left:50%;top:50%;width:204px;height:1px;margin-left:-102px;background:rgba(255,253,249,.18)}
.a-ay{position:relative;display:grid;place-items:center;width:48px;height:48px;border:0;border-radius:50%;background:#141A36;padding:0}
.a-ay .evre{width:22px;height:22px;transition:transform .4s cubic-bezier(.2,.7,.2,1)}
.a-ay .evre circle{stroke:rgba(255,253,249,.5)}
.a-ay .evre path{fill:rgba(255,253,249,.28)}
.a-ay.on .evre{transform:scale(1.18)}
.a-ay.on .evre circle{stroke:#F2A65A}
.a-ay.on .evre path{fill:#F2A65A}

/* B · Kemerli pencere: krem; kemer fotoğraf + 8px içeriden ince çerçeve (paspartu) */
.b-ust{display:flex;align-items:flex-end;justify-content:space-between;gap:12px;padding:0 16px}
.b-cizgi{position:relative;flex:none;width:112px;height:24px;margin-bottom:4px}
.b-cizgi::before{content:"";position:absolute;left:0;right:0;top:50%;height:1px;background:#D6CAB6}
.b-ay{position:absolute;left:0;top:0;width:24px;height:24px;display:grid;place-items:center;background:#F6F1E9;transition:transform .5s cubic-bezier(.2,.7,.2,1)}
.b-ay .evre{width:20px;height:20px}
.b-serit{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:16px;padding:20px 16px 4px}
.b-kart{flex:0 0 272px;scroll-snap-align:start}
.b-foto{position:relative;height:360px;border-radius:136px 136px 18px 18px;overflow:hidden;background:#0C1027}
.b-foto img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.b-foto::after{content:"";position:absolute;inset:8px;border-radius:128px 128px 12px 12px;box-shadow:inset 0 0 0 1px rgba(255,253,249,.55);pointer-events:none}
.b-etiket{display:flex;align-items:center;gap:6px;margin:14px 0 0;font-size:12px;font-weight:600;color:#766B5B}
.b-etiket .evre{width:14px;height:14px}
.b-bas{margin:4px 0 0;font-family:"Young Serif",Georgia,serif;font-size:24px;line-height:1.1;letter-spacing:-.015em;color:#1A2142}
.b-bas span{color:#F2A65A}
.b-yazi{margin:6px 0 0;font-size:14px;line-height:1.45;color:#5C6078}
.b-sec{display:inline-flex;align-items:center;gap:6px;min-height:48px;padding:0;border:0;background:none;color:#1A2142;font-size:14px;font-weight:700;text-decoration:underline;text-decoration-color:#D6CAB6;text-underline-offset:5px}

/* C · Deste: kartlar üst üste; arkadakiler alttan 16px'er taşar ve daralır; geçen kart sola kayar */
.c-deste{position:relative;height:536px;margin:18px 16px 0}
.c-kart{position:absolute;left:0;right:0;top:0;height:500px;display:flex;flex-direction:column;border:0;padding:0;border-radius:24px;overflow:hidden;background:#1A2142;color:#FFFDF9;text-align:left;transform-origin:50% 100%;transition:transform .55s cubic-bezier(.2,.7,.2,1),opacity .45s cubic-bezier(.2,.7,.2,1)}
.c-foto{position:relative;flex:1;overflow:hidden;background:#0C1027}
.c-foto img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.c-foto .cip{position:absolute;left:14px;top:14px}
.c-alt{flex:none;padding:16px 18px 18px}
.c-bas{display:block;font-family:"Young Serif",Georgia,serif;font-size:24px;line-height:1.1;letter-spacing:-.015em}
.c-bas span{color:#F2A65A}
.c-yazi{display:block;margin-top:6px;font-size:14px;line-height:1.45;color:#B9BED6}
.c-alt-sira{display:flex;align-items:center;justify-content:space-between;gap:10px;margin:14px 16px 0}
.c-oklar{display:flex;gap:8px}
.c-ok{display:grid;place-items:center;width:48px;height:48px;border:1.5px solid #D6CAB6;border-radius:50%;background:#FFFDF9;color:#1A2142;padding:0}
.c-ok[disabled]{opacity:.35}
.c-sec{display:inline-flex;align-items:center;gap:6px;min-height:48px;padding:0 16px;border:0;border-radius:16px;background:#1A2142;color:#FFFDF9;font-size:14px;font-weight:600}
.c-aylar{display:flex;gap:6px;align-items:center}
.c-aylar .evre{width:16px;height:16px}
.c-aylar .evre path{fill:#D6CAB6}
.c-aylar .on .evre path{fill:#F2A65A}

/* D · Hikâye: tek büyük kart; üstte 4 parça çubuk ve marka satırı; altta lacivert levha (fotoğrafın içinde, gradyan yok) */
.d-kart{position:relative;height:580px;margin:18px 16px 0;border-radius:24px;overflow:hidden;background:#1A2142;color:#FFFDF9}
.d-foto{position:absolute;left:0;right:0;top:0;bottom:164px;background:#0C1027}
.d-foto img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .6s cubic-bezier(.2,.7,.2,1)}
.d-foto img.on{opacity:1}
.d-cubuk{position:absolute;left:12px;right:12px;top:12px;z-index:2;display:flex;gap:4px}
.d-cubuk i{flex:1;height:3px;border-radius:2px;background:rgba(255,253,249,.35);overflow:hidden}
.d-cubuk i.bitti,.d-cubuk i.on{background:#FFFDF9}
.d-marka{position:absolute;left:12px;top:24px;z-index:2;display:flex;align-items:center;gap:8px;font-size:13px;font-weight:600}
.d-marka .d-av{display:grid;place-items:center;width:30px;height:30px;border-radius:50%;background:#FFFDF9}
.d-marka .evre{width:18px;height:18px}
.d-marka span{color:rgba(255,253,249,.8);font-weight:500}
.d-dokun{position:absolute;top:0;bottom:164px;z-index:1;width:50%;border:0;background:none;padding:0}
.d-dokun.sol{left:0}.d-dokun.sag{right:0}
.d-levha{position:absolute;left:0;right:0;bottom:0;z-index:2;height:164px;padding:18px 20px 10px;background:#1A2142}
.d-bas{margin:0;font-family:"Young Serif",Georgia,serif;font-size:26px;line-height:1.08;letter-spacing:-.015em}
.d-bas span{color:#F2A65A}
.d-yazi{margin:6px 0 0;font-size:14px;line-height:1.45;color:#B9BED6}
.d-sira{display:flex;align-items:center;justify-content:space-between;margin-top:4px}
.d-sec{display:inline-flex;align-items:center;gap:6px;min-height:48px;padding:0;border:0;background:none;color:#F2A65A;font-size:14px;font-weight:700}
.d-no{font-family:"Young Serif",Georgia,serif;font-size:14px;color:#B9BED6;font-variant-numeric:tabular-nums}
"""

BASLIK = '<h2 class="h2">Odası böyle<br>görünecek<span class="n">.</span></h2>'

HTML = """<div class="pg">
  <div style="padding: 18px 16px 10px">
    <h1 class="h2" style="font-size: 22px">Odası böyle görünecek · dört kart, dört arayüz</h1>
    <p style="margin: 6px 0 0; font-size: 13px; color: #5C6078">"Bir gece, beş an"ın yerine. Görseller yer tutucu: çocuk, lamba ve tavandaki ışık aynı karede olan kareler Flow'dan gelecek.</p>
  </div>

  <section class="sec" style="padding-bottom: 0">
    <p class="oneri"><svg class="evre" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d='""" + ay(.25) + """'></path></svg>A · Gece vitrini</p>
    <p class="oneri-alt">Koyu bant. Ortadaki kart odakta, yandakiler küçülüp söner. Yazı şeridin altında değişir; aylar dolarak ilerler.</p>
    <div class="a-bol">
      <div class="a-ust">""" + BASLIK.replace('class="h2"', 'class="h2"') + """<span class="a-say" aria-hidden="true"><b>{{aNo}}</b> / 4</span></div>
      <div class="a-serit noscroll" onScroll="{{aKay}}">
        <sc-for list="{{kartA}}" as="k" hint-placeholder-count="4"><div class="{{k.cls}}"><img src="{{k.src}}" alt="{{k.alt}}" style="object-position: {{k.pos}}"><span class="cip">""" + EV_SVG % 'k.ev' + """{{k.cip}}</span></div></sc-for>
      </div>
      <div class="a-metin" aria-live="polite"><p class="a-bas">{{aBas}}<span>.</span></p><p class="a-yazi">{{aYazi}}</p><sc-if value="{{aSecVar}}" hint-placeholder-val="{{true}}"><button class="a-sec" type="button">{{aSec}}""" + OK + """</button></sc-if></div>
      <div class="a-aylar" role="group" aria-label="Kartlar"><sc-for list="{{aAy}}" as="m" hint-placeholder-count="4"><button class="{{m.cls}}" type="button" onClick="{{m.git}}" aria-label="{{m.lbl}}" aria-pressed="{{m.bas}}">""" + EV_SVG % 'm.ev' + """</button></sc-for></div>
    </div>
  </section>

  <section class="sec" style="padding-top: 28px">
    <p class="oneri"><svg class="evre" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d='""" + ay(.5) + """'></path></svg>B · Kemerli pencere</p>
    <p class="oneri-alt">Krem zemin, dergi düzeni. Fotoğraf kemer pencerede, içeriden ince çerçeve. Kaydırdıkça ay çizgide ilerler ve dolar.</p>
    <div class="b-ust">""" + BASLIK + """<span class="b-cizgi" aria-hidden="true"><span class="b-ay" style="transform: translateX({{bX}}px)">""" + EV_SVG % 'bEv' + """</span></span></div>
    <div class="b-serit noscroll" onScroll="{{bKay}}">
      <sc-for list="{{kartB}}" as="k" hint-placeholder-count="4"><div class="b-kart"><div class="b-foto"><img src="{{k.src}}" alt="{{k.alt}}" style="object-position: {{k.pos}}"></div><p class="b-etiket">""" + EV_SVG % 'k.ev' + """{{k.cip}}</p><p class="b-bas">{{k.bas}}<span>.</span></p><p class="b-yazi">{{k.yazi}}</p><sc-if value="{{k.secVar}}" hint-placeholder-val="{{true}}"><button class="b-sec" type="button">{{k.sec}}""" + OK + """</button></sc-if></div></sc-for>
      <span aria-hidden="true" style="flex: 0 0 2px"></span>
    </div>
  </section>

  <section class="sec">
    <p class="oneri"><svg class="evre" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d='""" + ay(.75) + """'></path></svg>C · Deste</p>
    <p class="oneri-alt">Kartlar üst üste durur. Dokununca öndeki kenara kayar, arkadaki öne gelir. Az yer kaplar.</p>
    <div style="padding: 0 16px">""" + BASLIK + """</div>
    <div class="c-deste">
      <sc-for list="{{kartC}}" as="k" hint-placeholder-count="4"><button class="c-kart" type="button" onClick="{{cSonra}}" aria-hidden="{{k.gizli}}" tabindex="{{k.tab}}" style="transform: {{k.tf}}; opacity: {{k.op}}; z-index: {{k.z}}"><span class="c-foto"><img src="{{k.src}}" alt="{{k.alt}}" style="object-position: {{k.pos}}"><span class="cip">""" + EV_SVG % 'k.ev' + """{{k.cip}}</span></span><span class="c-alt"><span class="c-bas">{{k.bas}}<span>.</span></span><span class="c-yazi">{{k.yazi}}</span></span></button></sc-for>
    </div>
    <div class="c-alt-sira">
      <div class="c-oklar"><button class="c-ok" type="button" onClick="{{cOnce}}" aria-label="Önceki kart">""" + GERI + """</button><button class="c-ok" type="button" onClick="{{cSonra}}" aria-label="Sonraki kart">""" + OK + """</button></div>
      <span class="c-aylar" aria-hidden="true"><sc-for list="{{cAy}}" as="m" hint-placeholder-count="4"><span class="{{m.cls}}">""" + EV_SVG % 'm.ev' + """</span></sc-for></span>
      <sc-if value="{{cSecVar}}" hint-placeholder-val="{{true}}"><button class="c-sec" type="button">{{cSec}}</button></sc-if>
    </div>
  </section>

  <section class="sec">
    <p class="oneri"><svg class="evre" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d='""" + ay(1) + """'></path></svg>D · Hikâye</p>
    <p class="oneri-alt">Instagram hikâyesi gibi: tek büyük kart, üstte dört parça çubuk. Sağa dokun ileri, sola dokun geri. Reklamdan gelen müşteri bu dili zaten biliyor.</p>
    <div style="padding: 0 16px">""" + BASLIK + """</div>
    <div class="d-kart">
      <div class="d-foto"><sc-for list="{{kartD}}" as="k" hint-placeholder-count="4"><img class="{{k.cls}}" src="{{k.src}}" alt="{{k.alt}}" aria-hidden="{{k.gizli}}" style="object-position: {{k.pos}}"></sc-for></div>
      <div class="d-cubuk" aria-hidden="true"><sc-for list="{{dSeg}}" as="s" hint-placeholder-count="4"><i class="{{s}}"></i></sc-for></div>
      <div class="d-marka"><span class="d-av">""" + EV_SVG % 'dEv' + """</span>Ayluna<span>{{dCip}}</span></div>
      <button class="d-dokun sol" type="button" onClick="{{dOnce}}" aria-label="Önceki kart"></button><button class="d-dokun sag" type="button" onClick="{{dSonra}}" aria-label="Sonraki kart"></button>
      <div class="d-levha" aria-live="polite"><p class="d-bas">{{dBas}}<span>.</span></p><p class="d-yazi">{{dYazi}}</p><div class="d-sira"><sc-if value="{{dSecVar}}" hint-placeholder-val="{{true}}"><button class="d-sec" type="button">{{dSec}}""" + OK + """</button></sc-if><sc-if value="{{dSecYok}}" hint-placeholder-val="{{false}}"><span></span></sc-if><span class="d-no" aria-hidden="true">{{dNo}} / 4</span></div></div>
    </div>
  </section>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { a: 0, b: 0, c: 0, d: 0 }; }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    var EV = """ + str([ay(f) for f in EVRE]) + """;
    // Yer tutucu görseller; çocuklu kareler Flow'dan gelecek
    var K = [
      { id: 'fd0bca1b99cf3837b69fb025cc4e2cd9', pos: '50% 40%', alt: 'Gece çocuk odası: komodinde yanan LunaDream Kız, tavanda ay ve yıldızlar', cip: 'Kız modeli · Tavşanlı', bas: 'Tavanda masal', yazi: 'Işığı kapatınca seçtiği masal diski tavana yansır.', sec: 'Kız modelini seç' },
      { id: '8b1f621be2cb3b6133b7b78bc14e1963', pos: '50% 30%', alt: 'Kucakta yanan LunaDream Kız', cip: 'İki modelde de ninni', bas: 'Birlikte dinleyin', yazi: 'En sevdiği ninniyi telefondan aç; ses lambadan gelsin.', sec: '' },
      { id: '31751eb35473aca04420825deb3c3ce0', pos: '62% 50%', alt: 'Gece çocuk odası: komodinde yanan LunaDream Erkek (Uzay Kaşifi), duvarda yıldızlar', cip: 'Erkek modeli · Uzay Kaşifi', bas: 'Tavanda uzay', yazi: 'Uzay diskini tak, tavan yıldızlarla dolsun.', sec: 'Erkek modelini seç' },
      { id: '5b284c77c252b08a2974bde8e43de126', pos: '50% 40%', alt: 'Kubbesi açık LunaDream ve masal diskleri', cip: 'Kutuda 12 disk', bas: 'Masalı o seçsin', yazi: 'Bu gecenin masalını kutudaki 12 diskten çocuğun seçsin.', sec: '' }
    ];
    function git(k, i) { return function () { var o = {}; o[k] = i; self.setState(o); if (k === 'a') { var el = document.querySelector('.a-serit'); if (el) el.scrollTo({ left: i * 292, behavior: 'smooth' }); } }; }
    function kay(k, adim) { return function (e) { var el = e && (e.currentTarget || e.target); if (!el) return; var i = Math.max(0, Math.min(3, Math.round(el.scrollLeft / adim))); if (i !== S[k]) { var o = {}; o[k] = i; self.setState(o); } }; }
    function temel(k, i) { return { src: B + k.id, pos: k.pos, alt: k.alt, cip: k.cip, bas: k.bas, yazi: k.yazi, sec: k.sec, secVar: !!k.sec, ev: EV[i] }; }
    var a = K[S.a], c = K[S.c], d = K[S.d];
    var kartC = K.map(function (k, i) {
      var r = temel(k, i), dd = i - S.c;
      if (dd < 0) { r.tf = 'translateX(-112%) rotate(-5deg)'; r.op = 0; r.z = 1; }
      else { r.tf = 'translateY(' + (dd * 16) + 'px) scale(' + (1 - dd * .05).toFixed(2) + ')'; r.op = dd > 2 ? 0 : 1; r.z = 10 - dd; }
      r.gizli = dd === 0 ? 'false' : 'true'; r.tab = dd === 0 ? '0' : '-1'; return r; });
    return {
      kartA: K.map(function (k, i) { var r = temel(k, i); r.cls = 'a-kart' + (i === S.a ? ' on' : ''); return r; }),
      aAy: K.map(function (k, i) { return { ev: EV[i], cls: 'a-ay' + (i === S.a ? ' on' : ''), lbl: (i + 1) + '. kart: ' + k.bas, bas: i === S.a ? 'true' : 'false', git: git('a', i) }; }),
      aNo: S.a + 1, aBas: a.bas, aYazi: a.yazi, aSec: a.sec, aSecVar: !!a.sec, aKay: kay('a', 292),
      kartB: K.map(temel), bX: Math.round(S.b * 88 / 3), bEv: EV[S.b], bKay: kay('b', 286),
      kartC: kartC, cAy: K.map(function (k, i) { return { ev: EV[i], cls: i === S.c ? 'on' : '' }; }), cSec: c.sec, cSecVar: !!c.sec,
      cSonra: function () { self.setState({ c: (S.c + 1) % 4 }); }, cOnce: function () { self.setState({ c: (S.c + 3) % 4 }); },
      kartD: K.map(function (k, i) { var r = temel(k, i); r.cls = i === S.d ? 'on' : ''; r.gizli = i === S.d ? 'false' : 'true'; return r; }),
      dSeg: K.map(function (k, i) { return i < S.d ? 'bitti' : i === S.d ? 'on' : ''; }),
      dEv: EV[S.d], dCip: d.cip, dBas: d.bas, dYazi: d.yazi, dSec: d.sec, dSecVar: !!d.sec, dSecYok: !d.sec, dNo: S.d + 1,
      dSonra: function () { if (S.d < 3) self.setState({ d: S.d + 1 }); }, dOnce: function () { if (S.d > 0) self.setState({ d: S.d - 1 }); }
    };
  }
}"""

open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · E oda arayüzleri', css=CSS) + HTML + TAIL.format(h=int(os.environ.get('O_H', 3900)), js=JS))
print('yazıldı:', os.path.abspath(OUT))
