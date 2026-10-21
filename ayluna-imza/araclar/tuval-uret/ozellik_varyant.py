# LunaDream · "Neler yapabiliyor?" özellik anlatımı, 3 yön (21 Eki). Çalıştır: python3 ozellik_varyant.py
# Kullanıcı (sitesindeki başlık + paragraf + afiş düzeninin ekran görüntüsüyle): "LunaDream için sitemde olan bu tarz bir tasarım
# istiyorum ve yine UI kullanabiliriz." Afiş yerine büyük mini arayüz. Sitedeki "Elif K." yorum afişi alınmaz (doğrulanmamış yorum).
# Eleştirmen (1. tur: A 7, B 6, C 5) düzeltmeleri:
#   - Sihirli "ne" der (ikon, tek kelime); bu bölüm "nasıl" der: gerçek ürün kesimi (modele bağlı) ve eylem başlıkları.
#   - Kumanda paneli yok (kutuda kumanda yok; 4 kare örtük "4 mod" sayısı veriyordu). Işık: 3 kademe hale + "Kısık · Orta · Parlak".
#   - "21 animasyon" ve "animasyon" kelimesi teyitli değil: başlık "Işık seçenekleri", sayı [X].
#   - Yansıtma: tek disk, lambanın üstüne girer; desen tavanda yumuşak (radyal maske + hafif bulanıklık), döngünün çoğunda görünür.
#   - Metin iddiası yok: "oyun saatinde parlak", "priz aramazsın", oda adları kalktı; ses kaynağı telefon.
#   - Disk sayısı ve seçimi yalnız Diskler bölümünde; yansıtma satırı "Diskleri gör" ile oraya bağlanır.
#   A · Satırlar: sitedeki gibi alt alta (ekran 140 px, tek cümle)
#   B · Sekmeler: 48 px çipler (seçili: çerçeve + amber nokta), "Sıradaki" bağlantısı; kendiliğinden ilerlemez
#   C · Kaydırmalı: 296 px kartlar
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL
import sihirli2_varyant as S2
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE-Ozellik.dc.html')

E = 'cubic-bezier(.2,.7,.2,1)'
DISK = 'b088d2c82561b76f6db997fbc3944059'


def ay(f, r=9, c=12):
    rx = abs(1 - 2 * f) * r
    return 'M%d %dA%d %d 0 0 1 %d %dA%.2f %d 0 0 %d %d %dZ' % (c, c - r, r, r, c, c + r, rx, r, 0 if f < .5 else 1, c, c - r)


# Gerçek ürün kesimleri (saydam, stüdyo), modele bağlı
KESIM = ('<sc-if value="{{sihKiz}}" hint-placeholder-val="{{true}}"><img class="ob-urun kiz" src="/_blob/b823966c39ff35824b4d6e74757646ec" alt=""></sc-if>'
         '<sc-if value="{{sihErkek}}" hint-placeholder-val="{{false}}"><img class="ob-urun erkek" src="/_blob/20f90021119e4c3bdbc930b283e3635a" alt=""></sc-if>')
AY = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="%s"></path></svg>' % ay(.25)


def ui_isik():
    return ('<span class="bu bu-isik" aria-hidden="true"><span class="bh bh3"></span><span class="bh bh2"></span><span class="bh bh1"></span>' + KESIM +
            '<span class="bu-kad"><i>Kısık</i><i>Orta</i><i>Parlak</i></span></span>')


def ui_tavan():
    return ('<span class="bu bu-tavan" aria-hidden="true"><span class="bt-tavan"><img src="/_blob/%s" alt=""></span><span class="bt-koni"></span>' % DISK +
            KESIM + '<img class="bt-disk" src="/_blob/%s" alt=""></span>' % DISK)


def ui_tel():
    return ('<span class="bu bu-tel" aria-hidden="true"><span class="tf"><span class="tf-ust"><svg viewBox="0 0 24 24"><path d="M7 7l10 10-5 5V2l5 5L7 17"></path></svg>'
            '<span class="durum"><i>Bağlanıyor</i><i>Bağlandı</i></span></span><span class="tf-kart"><span class="tf-kapak">' + AY + '</span>'
            '<span class="tf-ad"><b>Ninni</b><span>Çalıyor</span></span><span class="tf-cal"><b></b></span></span></span>'
            '<span class="tf-dalga"><i></i><i></i><i></i></span><span class="tf-lamba">' + KESIM + '<span class="eq"><i></i><i></i><i></i><i></i></span></span></span>')


def ui_pil():
    # Fiş ürünün tabanına takılı; pil (ürünün kendi bataryası) altında dolar; fiş sola çıkar, ürün yanar
    return ('<span class="bu bu-pil" aria-hidden="true"><span class="bp-sira"><span class="bp-fis"><svg viewBox="0 0 24 24"><path d="M3 12h7M10 8.5h5a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2h-5zM17 10.5h3M17 13.5h3"></path></svg></span>'
            '<span class="bp-urun">' + KESIM + '</span></span><span class="bp-alt"><span class="bp-pil"><i></i><i></i><i></i><i></i></span><span class="durum"><i>Şarj oluyor</i><i>Kablosuz</i></span></span></span>')


OZ = [  # (çip, başlık, cümle, arayüz, bağlantı)
    ('Işık', 'Işık seçenekleri', '[X] ışık seçeneği ve 3 parlaklık; uyurken en kısığa al.', ui_isik, ''),
    ('Yansıtma', 'Diski tak, tavana yansıt', 'Işığı kapat; seçtiğin masal tavana ve duvara yansısın.', ui_tavan, 'Diskleri gör'),
    ('Ninni', 'Telefondan bağla, çalsın', 'Telefonundaki ninniyi, şarkıyı ya da masal kaydını lambadan çal.', ui_tel, ''),
    ('Şarj', 'Şarj et, kabloyu çıkar', 'Kablosu takılı değilken de çalışır; istediğin odaya taşı.', ui_pil, ''),
]

MINI_CSS = r"""/* Büyük mini arayüzler (300×128 tabanı, ekran 140 px). Gerçek ürün kesimi; ton zemin, lacivert çizgi, amber yalnız ışık. */
.ob-ek{position:relative;display:flex;align-items:center;justify-content:center;height:140px;overflow:hidden;border-radius:16px;background:#F1E8DA}
.bu{position:relative;display:block;flex:none;width:300px;height:128px}
.ob-urun{display:block;height:84px;width:auto}
.ob-urun.erkek{height:76px}
/* Işık: ürün ortada, arkasında 3 kademe hale; altta kademe adı */
.bu-isik .ob-urun{position:absolute;left:50%;top:10px;transform:translateX(-50%)}
.bu-isik .bh{position:absolute;left:50%;top:52px;border-radius:50%;border:1.5px solid #F2A65A}
.bu-isik .bh1{width:96px;height:96px;margin:-48px 0 0 -48px;opacity:.9}
.bu-isik .bh2{width:124px;height:124px;margin:-62px 0 0 -62px;opacity:.5;animation:l2 6s EASE infinite}
.bu-isik .bh3{width:152px;height:152px;margin:-76px 0 0 -76px;opacity:.25;animation:l3 6s EASE infinite}
.bu-kad{position:absolute;left:0;right:0;bottom:0;display:grid;grid-template-columns:repeat(3,auto);justify-content:center;gap:14px;font-size:12px;font-weight:600}
.bu-kad i{font-style:normal;color:#5C6078;opacity:.55}
.bu-kad i:nth-child(1){animation:kd1 6s EASE infinite}.bu-kad i:nth-child(2){animation:kd2 6s EASE infinite}.bu-kad i:nth-child(3){opacity:1;animation:kd3 6s EASE infinite}
@keyframes kd1{0%,30%{opacity:1}37%,100%{opacity:.55}}
@keyframes kd2{0%,30%{opacity:.55}37%,63%{opacity:1}70%,100%{opacity:.55}}
@keyframes kd3{0%,63%{opacity:.55}70%,92%{opacity:1}100%{opacity:.55}}
/* Yansıtma: disk yandan gelir, lambanın üstüne girer; koni açılır, desen tavanda yumuşakça belirir (10 sn, çoğu görünür) */
.bt-tavan{position:absolute;left:20px;right:20px;top:0;height:46px;border-radius:12px;background:#141A36;overflow:hidden}
.bt-tavan img{position:absolute;left:50%;top:-52px;width:150px;height:150px;margin-left:-75px;border-radius:50%;object-fit:cover;filter:blur(1.2px);-webkit-mask-image:radial-gradient(circle,#000 30%,transparent 70%);mask-image:radial-gradient(circle,#000 30%,transparent 70%);opacity:.8;animation:tv 10s EASE infinite}
@keyframes tv{0%,16%{opacity:0;transform:scale(.92)}26%,90%{opacity:.8;transform:none}97%,100%{opacity:0;transform:none}}
.bt-koni{position:absolute;left:50%;top:46px;width:0;height:0;margin-left:-26px;border-left:26px solid transparent;border-right:26px solid transparent;border-bottom:16px solid rgba(242,166,90,.26);animation:koni 10s EASE infinite}
@keyframes koni{0%,14%{opacity:0}22%,90%{opacity:1}97%,100%{opacity:0}}
.bu-tavan .ob-urun{position:absolute;left:50%;bottom:0;height:64px;transform:translateX(-50%)}
.bu-tavan .ob-urun.erkek{height:58px}
.bt-disk{position:absolute;left:50%;top:58px;width:28px;height:28px;margin-left:-14px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 1.5px #1A2142;opacity:0;animation:dsk1 10s EASE infinite}
@keyframes dsk1{0%{opacity:0;transform:translate(120px,10px) rotate(-90deg)}3%{opacity:1}11%{opacity:1;transform:none}15%,100%{opacity:0;transform:translateY(14px) scale(.4)}}
/* Bluetooth: telefonda bağlan → çal; dalgalar ürüne akar, ürünün yanında ses çubukları */
.bu-tel .tf{position:absolute;left:24px;top:2px;width:92px;height:124px;padding:9px 8px;border-radius:16px;background:#FFFDF9;box-shadow:0 0 0 1.5px #1A2142;display:flex;flex-direction:column;gap:8px}
.tf-ust{display:flex;align-items:center;gap:4px}
.tf-ust svg{width:14px;height:14px;fill:none;stroke:#1A2142;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.bu-tel .durum i:first-child{opacity:0;animation:d1 6s EASE infinite}.bu-tel .durum i:last-child{animation:d2 6s EASE infinite}
.tf-kart{display:flex;flex-direction:column;gap:5px;padding:6px;border-radius:10px;background:#F1E8DA}
.tf-kapak{display:grid;place-items:center;height:30px;border-radius:6px;background:#1A2142}
.tf-kapak svg{width:18px;height:18px}.tf-kapak circle{fill:none;stroke:rgba(255,253,249,.7);stroke-width:1.6}.tf-kapak path{fill:#F2A65A}
.tf-ad{display:flex;flex-direction:column;line-height:1.2}
.tf-ad b{font-size:12px;color:#1A2142}.tf-ad span{font-size:12px;color:#5C6078}
.tf-cal{position:relative;height:3px;border-radius:2px;background:#E3D8C7;overflow:hidden}
.tf-cal b{position:absolute;inset:0;background:#1A2142;transform-origin:0 50%;transform:scaleX(.5);animation:cal 6s linear infinite}
.tf-dalga{position:absolute;left:126px;top:46px;width:60px;height:36px}
.tf-dalga i{position:absolute;left:0;top:50%;width:20px;height:20px;margin-top:-10px;border-radius:50%;border:1.5px solid #F2A65A;border-left-color:transparent;border-bottom-color:transparent;transform:rotate(45deg) scale(.6);opacity:0;animation:dalga 2.4s EASE infinite}
.tf-dalga i:nth-child(2){animation-delay:.8s}.tf-dalga i:nth-child(3){animation-delay:1.6s}
@keyframes dalga{0%{opacity:0;transform:translateX(0) rotate(45deg) scale(.6)}20%{opacity:1}100%{opacity:0;transform:translateX(40px) rotate(45deg) scale(1.2)}}
.tf-lamba{position:absolute;right:26px;bottom:4px;display:flex;align-items:flex-end;gap:8px}
.tf-lamba .eq{margin-bottom:6px;animation:btg 6s EASE infinite}
/* Şarj: pil sırayla dolar, fiş çıkar; ürün yanında; "Şarj oluyor" → "Kablosuz" */
.bu-pil{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px}
.bp-sira{display:flex;align-items:flex-end;gap:0}
.bp-alt{display:flex;align-items:center;gap:12px}
.bp-pil{position:relative;display:flex;gap:3px;width:52px;height:22px;padding:3px;border:1.5px solid #1A2142;border-radius:6px}
.bp-pil::after{content:"";position:absolute;right:-5px;top:5px;width:3px;height:9px;border-radius:0 2px 2px 0;background:#1A2142}
.bp-pil i{flex:1;border-radius:2px;background:#1A2142;animation:pl1 6s EASE infinite both}
.bp-pil i:nth-child(2){animation-name:pl2}.bp-pil i:nth-child(3){animation-name:pl3}.bp-pil i:nth-child(4){animation-name:pl4}
.bp-fis{width:34px;height:34px;margin:0 -4px 6px 0;opacity:0;animation:bfis 6s EASE infinite}
.bp-fis svg{width:34px;height:34px;fill:none;stroke:#1A2142;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
@keyframes bfis{0%,56%{transform:none;opacity:1}64%,94%{transform:translateX(-14px);opacity:0}100%{transform:none;opacity:1}}
.bp-urun .ob-urun{height:76px;animation:burun 6s EASE infinite}
.bp-urun .ob-urun.erkek{height:64px}
@keyframes burun{0%,58%{opacity:.55}66%,92%{opacity:1}100%{opacity:.55}}
.bu-pil .durum{font-size:12px}
.bu-pil .durum i{justify-self:center}
.bu-pil .durum i:first-child{opacity:0;animation:s1 6s EASE infinite}.bu-pil .durum i:last-child{animation:s2 6s EASE infinite}
""".replace('EASE', E)

PANO_CSS = r""".pg{background:#F6F1E9;font-size:15px}
.sec{padding:0 0 44px}
.oneri{display:flex;align-items:center;gap:8px;margin:0 16px 6px;padding-top:16px;border-top:1px dashed #D6CAB6;font-size:12px;font-weight:700;color:#A05A1C}
.oneri-alt{margin:0 16px 16px;font-size:13px;color:#5C6078;text-wrap:balance}
.pg button{font:inherit;cursor:pointer;-webkit-tap-highlight-color:transparent}
.pg :focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
.ob-bas{margin:0 16px;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:22px;line-height:1.15;letter-spacing:-.01em;color:#1A2142}
.ob-bas span{color:#F2A65A}
.ob-h3{margin:0;font-size:17px;font-weight:700;line-height:1.3;color:#1A2142}
.ob-p{margin:4px 0 0;font-size:15px;line-height:1.5;color:#5C6078;text-wrap:pretty}
.ob-git{display:inline-flex;align-items:center;gap:6px;min-height:48px;padding:0;border:0;background:none;color:#1A2142;font-size:14px;font-weight:700;text-decoration:underline;text-decoration-color:#D6CAB6;text-underline-offset:5px}
.ob-git svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.yt{background:#F1E8DA;color:#7A4513;border-radius:4px;padding:0 3px}
/* A · Satırlar */
.oa-liste{display:flex;flex-direction:column;gap:20px;margin:16px 16px 0}
.oa-sat .ob-ek{margin-top:12px}
/* B · Sekmeler: 48 px çip; seçili 2 px lacivert çerçeve + amber nokta (dolu lacivert yok) */
.ob-cipler{display:flex;gap:6px;margin:16px 16px 0;overflow-x:auto;scrollbar-width:none}
.ob-cip{position:relative;flex:none;display:inline-flex;align-items:center;gap:8px;min-height:48px;padding:0 16px;border-radius:999px;border:1.5px solid #E3D8C7;background:#FFFDF9;color:#1A2142;font-size:14px;font-weight:600}
.ob-cip::before{content:"";width:8px;height:8px;border-radius:50%;background:#E3D8C7}
.ob-cip.on{border:2px solid #1A2142;padding:0 15.5px}
.ob-cip.on::before{background:#F2A65A}
.ob-kutu{margin:12px 16px 0;padding:8px;border-radius:20px;background:#FFFDF9;border:1px solid #E3D8C7}
.ob-gor{position:relative;height:140px}
.ob-gor>.ob-ek{position:absolute;inset:0;opacity:0;transition:opacity .35s EASE}
.ob-gor>.ob-ek.on{opacity:1}
.ob-metin{display:grid;padding:14px 8px 0}
.ob-m{grid-area:1/1;opacity:0;transform:translateY(6px);pointer-events:none;transition:opacity .28s EASE,transform .28s EASE}
.ob-m.on{opacity:1;transform:none;pointer-events:auto}
/* C · Kaydırmalı */
.oc-serit{display:flex;gap:12px;margin-top:16px;padding:0 16px 4px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:16px;scrollbar-width:none}
.oc-kart{flex:0 0 296px;scroll-snap-align:start;padding:8px 8px 12px;border-radius:20px;background:#FFFDF9;border:1px solid #E3D8C7}
.oc-kart .ob-metin{padding:12px 8px 0}
""".replace('EASE', E)

OKSVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"></path></svg>'


def yt(t):  # [X] yer tutucusu görünür işaretlenir
    return t.replace('[X]', '<span class="yt">[X]</span>')


def git(k):
    return ('<a class="ob-git" href="#diskler">%s%s</a>' % (k[4], OKSVG)) if k[4] else ''


BAS = '<h2 class="ob-bas">Neler yapabiliyor<span>?</span></h2>'

HTML = """<div class="pg">
  <div style="padding: 18px 16px 10px">
    <h1 class="h2" style="font-size: 22px">LunaDream · Neler yapabiliyor? Eleştirmenin sırası</h1>
    <p style="margin: 6px 0 0; font-size: 13px; color: #5C6078">Sitendeki başlık + paragraf düzeni; afiş yerine gerçek ürün ve küçük sekans. Sihirli kartlar "ne" der, bu bölüm "nasıl" der. Yeri: Videolar'ın altı, Odası'nın üstü. "Elif K." afişi yok. Işık seçeneği sayısı teyit edilene kadar [X].</p>
  </div>

  <section class="sec">
    <p class="oneri">1 · Satırlar · 7/10</p>
    <p class="oneri-alt">Sitedeki gibi alt alta: başlık, tek cümle, altında ekran. Dört özellik dokunmadan görünür.</p>
    """ + BAS + """
    <div class="oa-liste">""" + ''.join('<div class="oa-sat"><h3 class="ob-h3">%s</h3><p class="ob-p">%s</p>%s<div class="ob-ek">%s</div></div>' % (k[1], yt(k[2]), git(k), k[3]()) for k in OZ) + """</div>
  </section>

  <section class="sec">
    <p class="oneri">2 · Sekmeler · 6/10</p>
    <p class="oneri-alt">Dört çip, tek ekran ve cümle; dokununca değişir, altta "Sıradaki" bağlantısı. Kendiliğinden ilerlemez. Kısa.</p>
    """ + BAS + """
    <div class="ob-cipler" role="tablist">""" + ''.join('<button class="{{bc%d}}" type="button" role="tab" aria-selected="{{bs%d}}" onClick="{{bg%d}}">%s</button>' % (i, i, i, k[0]) for i, k in enumerate(OZ)) + """</div>
    <div class="ob-kutu"><div class="ob-gor">""" + ''.join('<div class="{{be%d}}" aria-hidden="{{bh%d}}">%s</div>' % (i, i, k[3]()) for i, k in enumerate(OZ)) + """</div>
      <div class="ob-metin" aria-live="polite">""" + ''.join('<div class="{{bm%d}}" aria-hidden="{{bh%d}}"><h3 class="ob-h3">%s</h3><p class="ob-p">%s</p><button class="ob-git" type="button" onClick="{{bn%d}}" tabindex="{{bt%d}}">Sıradaki: %s%s</button></div>' % (i, i, k[1], yt(k[2]), i, i, OZ[(i + 1) % 4][1], OKSVG) for i, k in enumerate(OZ)) + """</div></div>
  </section>

  <section class="sec">
    <p class="oneri">3 · Kaydırmalı · 5/10</p>
    <p class="oneri-alt">Dört kart yan yana kayar. Eleştirmen: sayfada altıncı yatay şerit olur.</p>
    """ + BAS + """
    <div class="oc-serit">""" + ''.join('<div class="oc-kart"><div class="ob-ek">%s</div><div class="ob-metin"><div><h3 class="ob-h3">%s</h3><p class="ob-p">%s</p>%s</div></div></div>' % (k[3](), k[1], yt(k[2]), git(k)) for k in OZ) + """<span aria-hidden="true" style="flex: 0 0 4px"></span></div>
  </section>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { b: 0 }; }
  renderVals() {
    var self = this, S = this.state, o = { sihKiz: true, sihErkek: false };
    for (var i = 0; i < 4; i++) (function (i) { var on = i === S.b;
      o['bc' + i] = 'ob-cip' + (on ? ' on' : ''); o['bs' + i] = on ? 'true' : 'false'; o['bg' + i] = function () { self.setState({ b: i }); };
      o['bn' + i] = function () { self.setState({ b: (i + 1) % 4 }); }; o['bt' + i] = on ? '0' : '-1';
      o['be' + i] = 'ob-ek' + (on ? ' on' : ''); o['bm' + i] = 'ob-m' + (on ? ' on' : ''); o['bh' + i] = on ? 'false' : 'true'; })(i);
    return o;
  }
}"""

if __name__ == '__main__':
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · Neler yapabiliyor', css=S2.MINI_CSS + MINI_CSS + PANO_CSS) + HTML + TAIL.format(h=int(os.environ.get('OB_H', 2352)), js=JS))
    print('yazıldı:', os.path.abspath(OUT))
