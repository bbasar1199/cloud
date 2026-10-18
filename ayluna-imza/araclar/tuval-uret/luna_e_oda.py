# LunaDream · E için "Odası böyle görünecek" seçenekleri (Tur 26). Çalıştır: python3 luna_e_oda.py
# Kullanıcı: "Kutudan ne çıkıyoru kaldıralım; 2 tane odanın nasıl göründüğünü gösteren görsel yapalım, metin içeren görsel
# kısmı gibi ama daha iyi dursun." Kutu bölümünün yerine iki oda: Kız (tavşanlı, tavanda ay ve yıldızlar) ve Erkek
# (Uzay Kaşifi, tavanda yıldızlar). Görseller tuvaldeki gece oda fotoğrafları (gerçek ürün referansıyla üretildi);
# yazı fotoğrafa gömülmez, HTML katmanıdır (düzenlenebilir, Türkçe harf hatası olmaz). B+ dili: Young Serif + Onest,
# krem/lacivert/tek amber, ay evresi işareti.
#   A · Poster: tam genişlik iki kart; üstte fotoğraf, altında lacivert yazı bandı (yazı ürünün üstüne binmez)
#   B · Kaydırmalı: iki dikey kart yan yana kayar, ikincisi kenardan görünür
#   C · Görsel + binen levha: tam genişlik fotoğraf, altına yazılı beyaz levha biner; ikinci oda aynalı
# Hepsinde: kartta küçük "Bu modeli seç" (canlıda modeli seçer, satın alma alanına kaydırır) ve tek satır temsilî notu.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE-Oda.dc.html')


def ay(f, r=9, c=12):
    rx = abs(1 - 2 * f) * r
    return 'M%d %dA%d %d 0 0 1 %d %dA%.2f %d 0 0 %d %d %dZ' % (c, c - r, r, r, c, c + r, rx, r, 0 if f < .5 else 1, c, c - r)


def evre(f, cls='evre'):
    return '<svg class="%s" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="%s"></path></svg>' % (cls, ay(f))


OK = '<svg class="ok-ik" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"></path></svg>'

CSS = r""".pg{background:#F6F1E9;font-size:15px}
.sec{padding:0 0 36px}
.oneri{display:flex;align-items:center;gap:8px;margin:0 16px 6px;padding-top:16px;border-top:1px dashed #D6CAB6;font-size:12px;font-weight:700;color:#A05A1C}
.oneri .evre{width:14px;height:14px}
.oneri-alt{margin:0 16px 18px;font-size:13px;color:#5C6078;text-wrap:balance}
.evre circle{fill:none;stroke:#1A2142;stroke-width:1.6}
.evre path{fill:#F2A65A}
.h2{font-size:22px;line-height:1.15}
.h2 span.n{color:#F2A65A}
.bas{padding:0 16px}
.temsil{margin:12px 16px 0;font-size:12px;color:#5C6078}
.pg button:focus-visible,.pg a:focus-visible{outline:2px solid #F2A65A;outline-offset:3px}
.ok-ik{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
/* Poster ortak: üstte fotoğraf (lamba ve tavan açık kalır), altında lacivert yazı bandı; yazı ürünün üstüne binmez */
.poster{position:relative;display:flex;flex-direction:column;overflow:hidden;border-radius:24px;background:#1A2142;color:#FFFDF9}
.p-foto{position:relative;flex:none;height:400px;overflow:hidden;background:#0C1027}
.p-foto img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.p-cip{position:absolute;left:14px;top:14px;z-index:1;display:inline-flex;align-items:center;gap:6px;padding:5px 11px 5px 7px;border-radius:999px;background:rgba(255,253,249,.94);color:#1A2142;font-size:12px;font-weight:700}
.p-cip .evre{width:14px;height:14px}
.p-alt{display:flex;flex-direction:column;gap:6px;padding:18px 18px 18px}
.p-bas{margin:0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:24px;line-height:1.1;letter-spacing:-.015em;text-wrap:balance}
.p-bas span{color:#F2A65A}
.p-yazi{margin:0;font-size:14px;line-height:1.45;color:#B9BED6}
.p-sec{display:inline-flex;align-items:center;gap:6px;align-self:flex-start;min-height:44px;margin-top:4px;padding:0 14px;border:1.5px solid rgba(255,253,249,.55);border-radius:999px;background:transparent;color:#FFFDF9;font:inherit;font-size:14px;font-weight:600;cursor:pointer}

/* A · Poster: alt alta, 4:5 */
.a-liste{display:flex;flex-direction:column;gap:14px;margin:16px 16px 0}

/* B · Kaydırmalı */
.b-serit{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:16px;padding:16px 16px 0;scrollbar-width:none}
.b-serit::-webkit-scrollbar{display:none}
.b-serit .poster{flex:0 0 300px;scroll-snap-align:start}
.b-serit .p-foto{height:340px}
.b-say{display:flex;justify-content:center;gap:6px;margin-top:12px}
.b-say i{width:6px;height:6px;border-radius:50%;background:#D6CAB6}.b-say i:first-child{background:#1A2142}

/* C · Görsel + binen levha */
.c-oda{margin-top:16px}
.c-oda+.c-oda{margin-top:28px}
.c-foto{position:relative;height:440px;overflow:hidden;background:#0C1027}
.c-foto img{width:100%;height:100%;object-fit:cover;display:block}
.c-cip{position:absolute;top:14px;left:16px}
.c-oda.ayna .c-cip{left:auto;right:16px}
.c-levha{position:relative;z-index:1;margin:-44px 16px 0;padding:18px 18px 16px;border-radius:22px;background:#FFFDF9;box-shadow:0 0 0 1px #E3D8C7,0 14px 30px -18px rgba(26,33,66,.35)}
.c-oda.ayna .c-levha{margin-left:40px}
.c-oda:not(.ayna) .c-levha{margin-right:40px}
.c-bas{margin:0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:22px;line-height:1.15;letter-spacing:-.01em;color:#1A2142}
.c-bas span{color:#F2A65A}
.c-yazi{margin:6px 0 0;font-size:14px;line-height:1.45;color:#5C6078}
.c-sec{display:inline-flex;align-items:center;gap:6px;min-height:44px;margin-top:6px;padding:0;border:0;background:none;color:#1A2142;font:inherit;font-size:14px;font-weight:700;cursor:pointer;text-decoration:underline;text-decoration-color:#D6CAB6;text-underline-offset:4px}
"""

KIZ, ERKEK = '/_blob/fd0bca1b99cf3837b69fb025cc4e2cd9', '/_blob/31751eb35473aca04420825deb3c3ce0'
ODA = [
    dict(src=KIZ, pos='50% 40%', alt='Gece çocuk odası: komodinde yanan LunaDream Kız, tavanda ay ve yıldızlar', cip='Kız modeli · Tavşanlı',
         bas='Tavanda ay ve<br>yıldızlar<span>.</span>', yazi='Işığı kapatınca seçtiğin masal diski tavana yansır.', sec='Kız modelini seç', evre=.22),
    dict(src=ERKEK, pos='62% 50%', alt='Gece çocuk odası: komodinde yanan LunaDream Erkek (Uzay Kaşifi), duvarda yıldızlar', cip='Erkek modeli · Uzay Kaşifi',
         bas='Odası bir uzay<br>gemisi<span>.</span>', yazi='Robot lamba yanınca duvara ve tavana yıldızlar düşer.', sec='Erkek modelini seç', evre=.78),
]


def poster(o):
    return ('<div class="poster"><div class="p-foto"><img src="%(src)s" alt="%(alt)s" style="object-position: %(pos)s"><span class="p-cip">' % o + evre(o['evre']) +
            '%(cip)s</span></div><div class="p-alt"><p class="p-bas">%(bas)s</p><p class="p-yazi">%(yazi)s</p><button class="p-sec" type="button">%(sec)s' % o + OK + '</button></div></div>')


def levha(o, ayna):
    return ('<div class="c-oda%s"><div class="c-foto"><img src="%s" alt="%s" style="object-position: %s"><span class="p-cip c-cip">' % (' ayna' if ayna else '', o['src'], o['alt'], o['pos']) +
            evre(o['evre']) + '%(cip)s</span></div><div class="c-levha"><p class="c-bas">%(bas)s</p><p class="c-yazi">%(yazi)s</p><button class="c-sec" type="button">%(sec)s' % o + OK + '</button></div></div>')


BASLIK = '<div class="bas"><h2 class="h2">Odası böyle<br>görünecek<span class="n">.</span></h2></div>'
TEMSIL = '<p class="temsil">Görseller temsilîdir; tavandaki desen seçtiğin diske göre değişir.</p>'

HTML = """<div class="pg">
  <div style="padding: 18px 16px 10px">
    <h1 class="h2" style="font-size: 22px">Odası böyle görünecek · üç seçenek</h1>
    <p style="margin: 6px 0 0; font-size: 13px; color: #5C6078">"Kutudan ne çıkıyor"un yerine. İki oda, yazı fotoğrafın içinde ama düzenlenebilir HTML.</p>
  </div>

  <section class="sec">
    <p class="oneri">""" + evre(.22) + """Seçenek A · Poster</p>
    <p class="oneri-alt">Tam genişlik iki dikey kart, alt alta. Yazı fotoğrafın altında.</p>
    """ + BASLIK + """
    <div class="a-liste">""" + ''.join(poster(o) for o in ODA) + """</div>
    """ + TEMSIL + """
  </section>

  <section class="sec">
    <p class="oneri">""" + evre(.5) + """Seçenek B · Kaydırmalı</p>
    <p class="oneri-alt">İki dikey kart yan yana kayar; ikincisi kenardan görünür. Daha kısa yer kaplar.</p>
    """ + BASLIK + """
    <div class="b-serit">""" + ''.join(poster(o) for o in ODA) + """<span aria-hidden="true" style="flex: 0 0 6px"></span></div>
    <div class="b-say" aria-hidden="true"><i></i><i></i></div>
    """ + TEMSIL + """
  </section>

  <section class="sec">
    <p class="oneri">""" + evre(1) + """Seçenek C · Görsel + binen levha</p>
    <p class="oneri-alt">Tam genişlik fotoğraf, altına yazılı beyaz levha biner; ikinci oda aynalı.</p>
    """ + BASLIK + """
    """ + levha(ODA[0], False) + levha(ODA[1], True) + """
    """ + TEMSIL + """
  </section>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = {}; }
  renderVals() { return {}; }
}"""

open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · E oda seçenekleri', css=CSS) + HTML + TAIL.format(h=int(os.environ.get('O_H', 3700)), js=JS))
print('yazıldı:', os.path.abspath(OUT))
