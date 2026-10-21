# LunaDream · "Neler yapabiliyor?" 2. tur, 3 yeni yön (21 Eki). Çalıştır: python3 ozellik2_varyant.py
# Kullanıcı (1. tur Satırlar / Sekmeler / Kaydırmalı için): "Hayır, o da çok boğar; daha iyi bir şeyler mi düşünsek, çok sıkıcı duruyor böyle."
# Liste düzeni tamamen çıkar: ürün merkezde, yazı en az, tek bir hareketli an. "Işığı aç/kapat" anahtarı yok (17 Eki).
# Sihirli kartlar "ne" der (6 + 6 disk, 3 parlaklık...); bu bölüm "nasıl" der, eylem cümleleriyle.
# Sekans teyitsiz iddia çizmez: disk tavanda dönmez, şarjdayken lamba sönük, kumanda yok, pil süresi yok.
#   A · Yörünge sahnesi: koyu sahne, ortada gerçek ürün; dört düğüm bir yörüngede, amber ay noktası düğümden düğüme gider;
#       seçilen özelliğin etkisi ürünün üstünde (tavanda masal, parlaklık halkaları, ses dalgaları, pil). Ekrandayken ilerler, dokununca durur.
#   B · Etiketli ürün: büyük stüdyo fotoğrafı, çevresinde dört yüzen etiket (parça konumu iddia etmemek için ürüne çizgi yok);
#       etkin etiketin minik simgesi oynar, altında tek cümle.
#   C · Masal kitabı: kapak + dört sayfa; "Sayfayı çevir" ile sayfa çevrilir (yalnız transform). Resimler 1. turun büyük arayüzleri.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL
import sihirli2_varyant as S2
import ozellik_varyant as O
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE-Ozellik2.dc.html')

E = 'cubic-bezier(.2,.7,.2,1)'
FOTO = {'kiz': 'e02351b3be4a1c555c5d760d0bbda723', 'erkek': '0033dfea6282c5bc479c385213661c00'}
DISK = {'kiz': '4a3a69e8c1d8dddad8c33f8f463b8a0e', 'erkek': 'b088d2c82561b76f6db997fbc3944059'}  # Ay ve yıldız / Uzay diski
TAVAN = {'kiz': '3d214a1ba100aaf3d85bb18a27325237', 'erkek': '49da18af3a87a3c97bb59cb9dbe8817f'}  # gerçek gece fotoğrafları (c-ninni-*): tavandaki yansıma kırpılır


def model(f):  # sayfada modele bağlı (renderVals: sihKiz / sihErkek)
    return ('<sc-if value="{{sihKiz}}" hint-placeholder-val="{{true}}">' + f('kiz') + '</sc-if>'
            '<sc-if value="{{sihErkek}}" hint-placeholder-val="{{false}}">' + f('erkek') + '</sc-if>')


OZ = [  # (anahtar, düğüm / etiket, başlık, cümle)
    ('masal', 'Masal', 'Tavana masal', 'Diski tak, tavana yansısın', 'Diski tak, ışığı kapat; seçtiği masal tavanda.'),
    ('isik', 'Işık', '3 kademe ışık', 'Uyurken en kısığa al', 'Kısık, orta, parlak. [X] ışık seçeneği.'),
    ('ninni', 'Ninni', 'Ninni çalar', 'Telefondan ninni çal', 'Bluetooth ile bağla; ninni lambadan çalsın.'),
    ('sarj', 'Şarj', 'Şarjlı, taşınır', 'Kabloyu çıkar, odaya taşı', 'Kablosu takılı değilken de çalışır.'),
]

IK = {  # 24 px çizgi simgeler
    'masal': '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"></circle><circle cx="12" cy="12" r="1.8"></circle><path d="M12 5.4a6.6 6.6 0 0 1 6 3.9"></path></svg>',
    'isik': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 18v-3.5M12 18v-7M18 18V7.5"></path></svg>',
    'ninni': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 17.5V6.6l10-2.1v11"></path><circle cx="6.6" cy="17.5" r="2.4"></circle><circle cx="16.6" cy="15.5" r="2.4"></circle></svg>',
    'sarj': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="7.5" width="16" height="9" rx="2.2"></rect><path d="M21.5 10.5v3M11.8 9.4l-2 2.8h3l-2 2.8"></path></svg>',
}
OKSVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"></path></svg>'
DONSVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12a8 8 0 1 0 2.4-5.7M4 4v4.5h4.5"></path></svg>'


def yt(t, koyu=False):  # [X] yer tutucusu görünür işaretlenir
    return t.replace('[X]', '<span class="yt%s">[X]</span>' % (' koyu' if koyu else ''))


# ---------- A · Yörünge sahnesi ----------
# Sahne 358 × 512; yörünge merkezi (179, 250), yarıçap 136; düğümler köşegenlerde (saat yönünde: Masal, Işık, Ninni, Şarj)
MX, MY, R = 179, 250, 136
POS = [(MX - 96, MY - 96), (MX + 96, MY - 96), (MX + 96, MY + 96), (MX - 96, MY + 96)]


def a_sahne():
    tavan = model(lambda m: '<img class="oy-desen %s" src="/_blob/%s" alt="">' % (m, TAVAN[m]))
    disk = model(lambda m: '<img class="oy-disk" src="/_blob/%s" alt="">' % DISK[m])
    urun = model(lambda m: '<span class="oy-pen"><img class="oy-img %s" src="/_blob/%s" alt=""></span>' % (m, FOTO[m]))
    dug = ''.join('<button class="{{oyd%d}}" type="button" style="left: %dpx; top: %dpx" onClick="{{oyg%d}}" aria-pressed="{{oyp%d}}">'
                  '<span class="oy-ik">%s</span><span class="oy-ad">%s</span></button>' % (i, x - 28, y - 28, i, i, IK[k[0]], k[1])
                  for i, (k, (x, y)) in enumerate(zip(OZ, POS)))
    metin = ''.join('<div class="{{oym%d}}" aria-hidden="{{oyh%d}}"><h3 class="oy-bas">%s</h3><p class="oy-p">%s</p></div>' % (i, i, k[3], yt(k[4], True))
                    for i, k in enumerate(OZ))
    return ('<div class="{{oyCls}}">'
            '<div class="oy-tavan" aria-hidden="true">' + tavan + '</div>'
            '<div class="oy-yor" aria-hidden="true"><span class="oy-kol" style="--a: {{oyAci}}deg"><i></i></span></div>'
            '<div class="oy-hl" aria-hidden="true"><i></i><i></i><i></i></div>'
            '<div class="oy-dal" aria-hidden="true"><span class="sol"><i></i><i></i><i></i></span><span class="sag"><i></i><i></i><i></i></span></div>'
            '<div class="oy-urun" aria-hidden="true">' + disk + urun + '</div>'
            '<div class="oy-alt" aria-hidden="true">'
            '<span class="oy-kad"><i>Kısık</i><i>Orta</i><i>Parlak</i></span>'
            '<span class="oy-cal"><span class="eq"><i></i><i></i><i></i><i></i></span>Ninni çalıyor</span>'
            '<span class="oy-pil"><span class="oy-bat"><i></i><i></i><i></i><i></i></span><span class="durum"><i>Şarj oluyor</i><i>Kablosuz</i></span></span>'
            '</div>' + dug +
            '<div class="oy-metin" aria-live="polite">' + metin + '</div></div>')


# ---------- B · Etiketli ürün ----------
EK_IK = {  # etiketteki minik simge (etkinken oynar)
    'masal': model(lambda m: '<img class="oe-dsk" src="/_blob/%s" alt="">' % DISK[m]),
    'isik': '<span class="oe-kd"><i></i><i></i><i></i></span>',
    'ninni': '<span class="eq oe-eq"><i></i><i></i><i></i><i></i></span>',
    'sarj': '<span class="oe-bat"><i></i><i></i><i></i></span>',
}
EK_POS = ['left: 12px; top: 14px', 'right: 12px; top: 64px', 'left: 12px; top: 376px', 'right: 12px; top: 392px']


def b_sahne():
    foto = model(lambda m: '<img class="oe-img" src="/_blob/%s" alt="LunaDream %s modeli, stüdyo çekimi">' % (FOTO[m], 'Kız' if m == 'kiz' else 'Erkek'))
    cip = ''.join('<button class="{{oec%d}}" type="button" style="%s" onClick="{{oeg%d}}" aria-pressed="{{oep%d}}"><span class="oe-ik">%s</span>%s</button>'
                  % (i, EK_POS[i], i, i, EK_IK[k[0]], k[2]) for i, k in enumerate(OZ))
    metin = ''.join('<p class="{{oem%d}}" aria-hidden="{{oeh%d}}">%s</p>' % (i, i, yt(k[4])) for i, k in enumerate(OZ))
    return '<div class="oe"><div class="oe-foto">' + foto + '</div>' + cip + '</div><div class="oe-metin" aria-live="polite">' + metin + '</div>'


# ---------- C · Masal kitabı ----------
RESIM = {'masal': O.ui_tavan, 'isik': O.ui_isik, 'ninni': O.ui_tel, 'sarj': O.ui_pil}


def c_kitap():
    sayfa = []
    kapak = model(lambda m: '<span class="ok-pen"><img class="%s" src="/_blob/%s" alt=""></span>' % (m, FOTO[m]))
    sayfa.append('<article class="{{okc0}}" style="z-index: 5" aria-hidden="{{okh0}}"><div class="ok-kapak">' + kapak +
                 '<h2 class="ok-kbas">Neler<br>yapabiliyor<span>?</span></h2><p class="ok-kalt">Dört sayfada LunaDream</p></div>'
                 '<div class="ok-alt"><span></span><button class="ok-cevir koyu" type="button" onClick="{{okg0}}" tabindex="{{okt0}}">Sayfayı çevir' + OKSVG + '</button></div></article>')
    for j, k in enumerate(OZ, 1):
        son = j == len(OZ)
        nok = ''.join('<i%s></i>' % (' class="on"' if n == j - 1 else '') for n in range(len(OZ)))
        sayfa.append('<article class="{{okc%d}}" style="z-index: %d" aria-hidden="{{okh%d}}"><div class="ok-resim">%s</div>'
                     '<h3 class="ok-bas">%s</h3><p class="ok-p">%s</p>'
                     '<div class="ok-alt"><span class="ok-nok" aria-hidden="true">%s</span><button class="ok-cevir" type="button" onClick="{{okg%d}}" tabindex="{{okt%d}}">%s</button></div></article>'
                     % (j, 5 - j, j, RESIM[k[0]](), k[3], yt(k[4]), nok, j, j, ('Başa dön' + DONSVG) if son else ('Sayfayı çevir' + OKSVG)))
    return '<div class="ok">' + ''.join(sayfa) + '</div>'


CSS = r""".pg{background:#F6F1E9;font-size:15px}
.sec{padding:0 16px 44px}
.oneri{display:flex;align-items:center;gap:8px;margin:0 0 6px;padding-top:16px;border-top:1px dashed #D6CAB6;font-size:12px;font-weight:700;color:#A05A1C}
.oneri-alt{margin:0 0 16px;font-size:13px;color:#5C6078;text-wrap:balance}
.pg button{font:inherit;cursor:pointer;-webkit-tap-highlight-color:transparent}
.pg :focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
.h2 span.n{color:#F2A65A}
.yt{background:#F1E8DA;color:#7A4513;border-radius:4px;padding:0 3px}
.yt.koyu{background:rgba(242,166,90,.18);color:#F6C893}

/* A · Yörünge sahnesi */
.oy{position:relative;height:512px;margin-top:16px;border-radius:28px;background:#1A2142;overflow:hidden;color:#FFFDF9}
.oy-tavan{position:absolute;left:0;right:0;top:0;height:178px;overflow:hidden;opacity:0;transition:opacity .7s EASE;-webkit-mask-image:linear-gradient(#000 30%,transparent);mask-image:linear-gradient(#000 30%,transparent)}
.oy-desen{position:absolute;left:0;top:0;width:358px;height:auto;opacity:.9;transform:scale(1.04);transform-origin:50% 0;transition:transform 1.4s EASE}
.oy-desen.erkek{top:-120px}
.oy.s0 .oy-tavan{opacity:1}
.oy.s0 .oy-desen{transform:none}
.oy-yor{position:absolute;left:43px;top:114px;width:272px;height:272px;border-radius:50%;box-shadow:inset 0 0 0 1px rgba(246,241,233,.16)}
.oy-kol{position:absolute;inset:0;transform:rotate(var(--a));transition:transform 1s EASE}
.oy-kol i{position:absolute;left:50%;top:-6px;width:12px;height:12px;margin-left:-6px;border-radius:50%;background:#F2A65A}
/* ürün (gerçek kesim), merkezde */
.oy-urun{position:absolute;left:95px;top:166px;width:168px;height:168px}
.oy-pen{position:absolute;inset:0;border-radius:50%;overflow:hidden;background:#EEE4DA;transition:opacity .5s EASE}
.oy-img{position:absolute;left:-26px;top:-56px;width:220px;height:220px;max-width:none}
.oy-img.erkek{left:-25px;top:-58px}
/* Masal: disk lambanın üstüne iner, desen tavanda yumuşakça belirir (dönmez) */
.oy-disk{position:absolute;left:50%;top:-14px;z-index:1;width:26px;height:26px;margin-left:-13px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 1.5px #FFFDF9;opacity:0}
.oy.s0 .oy-disk{animation:oydisk 4.5s EASE both}
@keyframes oydisk{0%{opacity:0;transform:translateY(-34px)}14%{opacity:1}34%{opacity:1;transform:none}48%,100%{opacity:0;transform:translateY(12px) scale(.5)}}
/* Işık: üç halka, kısık → orta → parlak; ürün de kademeyle aydınlanır (6 sn) */
.oy-hl i{position:absolute;left:50%;top:250px;border-radius:50%;box-shadow:inset 0 0 0 1.5px #F2A65A;opacity:0;transition:opacity .4s EASE}
.oy-hl i:nth-child(1){width:190px;height:190px;margin:-95px 0 0 -95px;left:179px}
.oy-hl i:nth-child(2){width:216px;height:216px;margin:-108px 0 0 -108px;left:179px}
.oy-hl i:nth-child(3){width:242px;height:242px;margin:-121px 0 0 -121px;left:179px}
.oy.s1 .oy-hl i:nth-child(1){opacity:.9}
.oy.s1 .oy-hl i:nth-child(2){opacity:.5;animation:oyl2 6s EASE infinite}
.oy.s1 .oy-hl i:nth-child(3){opacity:.25;animation:oyl3 6s EASE infinite}
.oy.s1 .oy-pen{animation:oyik 6s EASE infinite}
@keyframes oyl2{0%,30%{opacity:0;transform:scale(.9)}37%,92%{opacity:.5;transform:none}100%{opacity:0;transform:scale(.9)}}
@keyframes oyl3{0%,63%{opacity:0;transform:scale(.9)}70%,92%{opacity:.25;transform:none}100%{opacity:0;transform:scale(.9)}}
@keyframes oyik{0%,30%{opacity:.6}37%,63%{opacity:.8}70%,92%{opacity:1}100%{opacity:.6}}
/* Ninni: ürünün iki yanından ses dalgaları */
.oy-dal span{position:absolute;top:226px;width:48px;height:48px;opacity:0;transition:opacity .4s EASE}
.oy-dal .sol{left:44px}.oy-dal .sag{left:266px}
.oy-dal i{position:absolute;left:0;top:0;width:48px;height:48px;border-radius:50%;box-shadow:inset 1.5px 0 0 0 #F2A65A;opacity:0}
.oy-dal .sol i{box-shadow:inset 1.5px 0 0 0 #F2A65A}.oy-dal .sag i{box-shadow:inset -1.5px 0 0 0 #F2A65A}
.oy.s2 .oy-dal span{opacity:1}
.oy.s2 .oy-dal .sol i{animation:oydl 2.4s EASE infinite}.oy.s2 .oy-dal .sag i{animation:oydr 2.4s EASE infinite}
.oy-dal i:nth-child(2){animation-delay:.8s!important}.oy-dal i:nth-child(3){animation-delay:1.6s!important}
@keyframes oydl{0%{opacity:0;transform:none}25%{opacity:1}100%{opacity:0;transform:translateX(-22px) scale(1.25)}}
@keyframes oydr{0%{opacity:0;transform:none}25%{opacity:1}100%{opacity:0;transform:translateX(22px) scale(1.25)}}
/* Şarj: pil dolar, lamba şarjdayken sönük; fiş çıkınca "Kablosuz" ve yanar */
.oy.s3 .oy-pen{animation:oysj 6s EASE infinite}
@keyframes oysj{0%,58%{opacity:.4}66%,92%{opacity:1}100%{opacity:.4}}
/* pencerenin altına binen küçük gösterge rozeti (en çok 134 px; alt düğümlere değmez) */
.oy-alt{position:absolute;left:109px;top:318px;width:140px;height:30px;display:grid;justify-items:center;align-items:center;font-size:12px;font-weight:600;color:#B9BED6}
.oy-alt>span{grid-area:1/1;display:flex;align-items:center;gap:8px;height:30px;padding:0 10px;border-radius:999px;background:#1A2142;box-shadow:inset 0 0 0 1px rgba(246,241,233,.22);opacity:0;transform:translateY(4px);transition:opacity .35s EASE,transform .35s EASE;white-space:nowrap}
.oy.s1 .oy-kad,.oy.s2 .oy-cal,.oy.s3 .oy-pil{opacity:1;transform:none}
.oy-kad{gap:8px!important}
.oy-kad i{font-style:normal;opacity:.5}
.oy-kad i:nth-child(3){opacity:1;color:#FFFDF9}
.oy.s1 .oy-kad i:nth-child(1){animation:oyk1 6s EASE infinite}.oy.s1 .oy-kad i:nth-child(2){animation:oyk2 6s EASE infinite}.oy.s1 .oy-kad i:nth-child(3){animation:oyk3 6s EASE infinite}
@keyframes oyk1{0%,30%{opacity:1}37%,100%{opacity:.5}}
@keyframes oyk2{0%,30%{opacity:.5}37%,63%{opacity:1}70%,100%{opacity:.5}}
@keyframes oyk3{0%,63%{opacity:.5}70%,92%{opacity:1}100%{opacity:.5}}
.oy-cal .eq{height:14px;margin:0;animation:none}
.oy-cal .eq i{height:14px}
.oy-bat{position:relative;display:flex;gap:2px;width:36px;height:18px;padding:2.5px;border:1.5px solid #FFFDF9;border-radius:5px}
.oy-bat::after{content:"";position:absolute;right:-5px;top:4px;width:3px;height:6px;border-radius:0 2px 2px 0;background:#FFFDF9}
.oy-bat i{flex:1;border-radius:1.5px;background:#FFFDF9}
.oy.s3 .oy-bat i:nth-child(1){animation:pl1 6s EASE infinite both}.oy.s3 .oy-bat i:nth-child(2){animation:pl2 6s EASE infinite both}
.oy.s3 .oy-bat i:nth-child(3){animation:pl3 6s EASE infinite both}.oy.s3 .oy-bat i:nth-child(4){animation:pl4 6s EASE infinite both}
.oy-pil .durum{color:#B9BED6}
.oy.s3 .oy-pil .durum i:first-child{opacity:0;animation:s1 6s EASE infinite}.oy.s3 .oy-pil .durum i:last-child{animation:s2 6s EASE infinite}
/* düğümler: 56 px; etkin düğümün halkası amber, ay noktası onun altına girer */
.oy-d{position:absolute;width:56px;height:56px;padding:0;border:0;border-radius:50%;background:#1A2142;color:#FFFDF9;box-shadow:inset 0 0 0 1.5px rgba(246,241,233,.3);transition:box-shadow .4s EASE}
.oy-d.on{box-shadow:inset 0 0 0 1.5px #F2A65A}
.oy-ik{display:grid;place-items:center;width:100%;height:100%}
.oy-ik svg{width:24px;height:24px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;opacity:.75;transition:opacity .4s EASE}
.oy-d.on .oy-ik svg{opacity:1}
.oy-ad{position:absolute;left:50%;width:80px;margin-left:-40px;text-align:center;font-size:13px;font-weight:600;color:#B9BED6;transition:color .4s EASE}
.oy-d.ust .oy-ad{bottom:calc(100% + 6px)}.oy-d.alt .oy-ad{top:calc(100% + 6px)}
.oy-d.on .oy-ad{color:#FFFDF9}
.oy-metin{position:absolute;left:20px;right:20px;top:414px;display:grid}
.oy-m{grid-area:1/1;opacity:0;transform:translateY(6px);transition:opacity .35s EASE,transform .35s EASE}
.oy-m.on{opacity:1;transform:none}
.oy-bas{margin:0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:22px;line-height:1.2;letter-spacing:-.01em;color:#FFFDF9}
.oy-p{margin:6px 0 0;font-size:15px;line-height:1.45;color:#B9BED6}

/* B · Etiketli ürün: 358 × 452 çerçeve; fotoğraf üstte kare, altı aynı zemin rengine yumuşakça erir */
.oe{position:relative;height:452px;margin-top:16px}
.oe-foto{position:absolute;inset:0;border-radius:24px;overflow:hidden;background:#EEE4DA}
.oe-img{position:absolute;left:0;top:0;width:100%;height:358px;object-fit:cover;-webkit-mask-image:linear-gradient(#000 80%,transparent);mask-image:linear-gradient(#000 80%,transparent)}
.oe-cip{position:absolute;display:inline-flex;align-items:center;gap:8px;min-height:48px;padding:0 16px 0 7px;border-radius:999px;border:1px solid #E3D8C7;background:#FFFDF9;color:#1A2142;font-size:14px;font-weight:600;white-space:nowrap;
  animation:oegir .5s EASE both;transition:box-shadow .3s EASE}
.oe-cip:nth-of-type(2){animation-delay:.12s}.oe-cip:nth-of-type(3){animation-delay:.24s}.oe-cip:nth-of-type(4){animation-delay:.36s}
@keyframes oegir{from{opacity:0;transform:translateY(8px)}}
.oe-cip.on{box-shadow:0 0 0 1px #1A2142;border-color:#1A2142}
.oe-ik{display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:#F1E8DA;overflow:hidden}
.oe-dsk{display:block;width:26px;height:26px;border-radius:50%;object-fit:cover}
.oe-cip.on .oe-dsk{animation:oedsk 2.4s EASE infinite}
@keyframes oedsk{0%,100%{transform:none}30%{transform:translateY(-3px)}55%{transform:none}}
.oe-kd{display:flex;gap:3px}
.oe-kd i{width:6px;height:6px;border-radius:50%;background:#1A2142;opacity:.25}
.oe-kd i:nth-child(1){opacity:1}
.oe-cip.on .oe-kd i{background:#F2A65A}
.oe-cip.on .oe-kd i:nth-child(1){animation:oyk1 6s EASE infinite;opacity:1}
.oe-cip.on .oe-kd i:nth-child(2){animation:oekd2 6s EASE infinite}.oe-cip.on .oe-kd i:nth-child(3){animation:oekd3 6s EASE infinite}
@keyframes oekd2{0%,30%{opacity:.25}37%,92%{opacity:1}100%{opacity:.25}}
@keyframes oekd3{0%,63%{opacity:.25}70%,92%{opacity:1}100%{opacity:.25}}
.oe-eq{height:14px;margin:0;animation:none}
.oe-eq i{height:14px;background:#1A2142;animation-play-state:paused}
.oe-cip.on .oe-eq i{background:#F2A65A;animation-play-state:running}
.oe-bat{position:relative;display:flex;gap:1.5px;width:20px;height:12px;padding:1.5px;border:1.5px solid #1A2142;border-radius:3.5px}
.oe-bat::after{content:"";position:absolute;right:-4px;top:2.5px;width:2px;height:4px;border-radius:0 1px 1px 0;background:#1A2142}
.oe-bat i{flex:1;border-radius:1px;background:#1A2142}
.oe-cip.on .oe-bat i:nth-child(1){animation:pl1 6s EASE infinite both}.oe-cip.on .oe-bat i:nth-child(2){animation:pl2 6s EASE infinite both}.oe-cip.on .oe-bat i:nth-child(3){animation:pl3 6s EASE infinite both}
.oe-metin{display:grid;margin-top:14px;min-height:48px}
.oe-m{grid-area:1/1;margin:0;font-size:16px;line-height:1.45;color:#1A2142;text-wrap:balance;opacity:0;transform:translateY(6px);transition:opacity .3s EASE,transform .3s EASE}
.oe-m.on{opacity:1;transform:none}

/* C · Masal kitabı: 326 × 452, sağ sayfa; sol kenardan çevrilir (rotateY, perspektif) */
.ok{position:relative;width:326px;height:420px;margin:16px auto 0;perspective:1600px}
.ok::before,.ok::after{content:"";position:absolute;inset:0;border-radius:6px 18px 18px 6px;background:#FBF7F0;border:1px solid #E3D8C7}
.ok::before{transform:translate(8px,6px)}.ok::after{transform:translate(4px,3px)}
.ok-sayfa{position:absolute;inset:0;display:flex;flex-direction:column;padding:14px 14px 8px 22px;border-radius:6px 18px 18px 6px;background:#FFFDF9;border:1px solid #E3D8C7;
  transform-origin:0 50%;backface-visibility:hidden;-webkit-backface-visibility:hidden;transition:transform .9s EASE}
.ok-sayfa::before{content:"";position:absolute;left:0;top:0;bottom:0;width:18px;border-radius:6px 0 0 6px;background:linear-gradient(90deg,rgba(26,33,66,.09),rgba(26,33,66,0))}
.ok-sayfa::after{content:"";position:absolute;inset:0;border-radius:inherit;background:#1A2142;opacity:0;pointer-events:none;transition:opacity .9s EASE}
.ok-sayfa.gecti{transform:rotateY(-180deg)}
.ok-sayfa.gecti::after{opacity:.2}
.ok-sayfa.kapak{background:#1A2142;border-color:#1A2142}
.ok-sayfa.kapak::before{background:linear-gradient(90deg,rgba(0,0,0,.25),rgba(0,0,0,0))}
.ok-kapak{position:relative;flex:1;display:flex;flex-direction:column;justify-content:flex-end;padding:0 4px 8px}
.ok-pen{position:absolute;right:6px;top:10px;width:176px;height:176px;border-radius:50%;overflow:hidden;background:#EEE4DA}
.ok-pen img{position:absolute;left:-24px;top:-60px;width:230px;height:230px;max-width:none}
.ok-kbas{margin:0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:34px;line-height:1.05;letter-spacing:-.02em;color:#FFFDF9}
.ok-kbas span{color:#F2A65A}
.ok-kalt{margin:10px 0 0;font-size:15px;color:#B9BED6}
.ok-resim{position:relative;display:flex;align-items:center;justify-content:center;height:206px;flex:none;border-radius:12px;background:#F1E8DA;overflow:hidden}
.ok-resim .bu{transform:scale(.96)}
.ok-bas{margin:18px 0 0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:24px;line-height:1.15;letter-spacing:-.01em;color:#1A2142;text-wrap:balance}
.ok-p{margin:8px 0 0;font-size:15px;line-height:1.5;color:#5C6078;text-wrap:pretty}
.ok-alt{display:flex;align-items:center;justify-content:space-between;margin-top:auto}
.ok-nok{display:flex;gap:6px}
.ok-nok i{width:6px;height:6px;border-radius:50%;background:#E3D8C7}
.ok-nok i.on{background:#F2A65A}
.ok-cevir{display:inline-flex;align-items:center;gap:6px;min-height:48px;padding:0 4px;border:0;background:none;color:#1A2142;font-size:14px;font-weight:700}
.ok-cevir.koyu{color:#FFFDF9}
.ok-cevir svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
""".replace('EASE', E)

BAS = '<h2 class="h2">Neler<br>yapabiliyor<span class="n">?</span></h2>'

HTML = """<div class="pg">
  <div style="padding: 18px 16px 10px">
    <h1 class="h2" style="font-size: 22px">LunaDream · Neler yapabiliyor? 2. tur</h1>
    <p style="margin: 6px 0 0; font-size: 13px; color: #5C6078">Liste yok: ürün ortada, yazı en az, tek hareketli an. Sihirli kartlar "ne" der, bu bölüm "nasıl" der. Yeri: Videolar'ın altı, Odası'nın üstü. Işığı aç/kapat anahtarı yok.</p>
  </div>

  <section class="sec">
    <p class="oneri">A · Yörünge sahnesi</p>
    <p class="oneri-alt">Koyu sahnede gerçek ürün; amber ay noktası yörüngede düğümden düğüme gider, etkisi ürünün üstünde görünür. Ekrandayken ilerler, dokununca durur.</p>
    """ + BAS + a_sahne() + """
  </section>

  <section class="sec">
    <p class="oneri">B · Etiketli ürün</p>
    <p class="oneri-alt">Büyük stüdyo fotoğrafı, çevresinde dört etiket; etkin etiketin minik simgesi oynar, altta tek cümle. Paragraf yok.</p>
    """ + BAS + b_sahne() + """
  </section>

  <section class="sec">
    <p class="oneri">C · Masal kitabı</p>
    <p class="oneri-alt">Kapak ve dört sayfa; "Sayfayı çevir" ile sayfa soldan çevrilir. Marka "masal" dediği için metafor ona uyar.</p>
    """ + c_kitap() + """
  </section>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { a: 0, aAdim: 0, aDur: false, b: 0, bDur: false, c: 0, cDur: false }; }
  componentDidMount() {
    // Ekrandayken kendiliğinden ilerler (A 4,5 sn, B 4 sn, C 5 sn); dokununca o yön durur. Azaltılmış harekette ilerlemez.
    var self = this;
    if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    this.iv = [setInterval(function () { self.ilerle('a'); }, 4500), setInterval(function () { self.ilerle('b'); }, 4000), setInterval(function () { self.ilerle('c'); }, 5000)];
  }
  componentWillUnmount() { (this.iv || []).forEach(clearInterval); }
  ilerle(k) {
    var S = this.state; if (S[k + 'Dur']) return;
    if (k === 'a') this.setState({ a: (S.a + 1) % 4, aAdim: S.aAdim + 1 });
    if (k === 'b') this.setState({ b: (S.b + 1) % 4 });
    if (k === 'c') this.setState({ c: (S.c + 1) % 5 });
  }
  renderVals() {
    var self = this, S = this.state, o = { sihKiz: true, sihErkek: false };
    o.oyCls = 'oy s' + S.a; o.oyAci = -45 + 90 * S.aAdim;
    for (var i = 0; i < 4; i++) (function (i) { var on = i === S.a, eb = i === S.b;
      o['oyd' + i] = 'oy-d' + (i < 2 ? ' ust' : ' alt') + (on ? ' on' : ''); o['oyp' + i] = on ? 'true' : 'false';
      o['oyg' + i] = function () { var d = (i - self.state.a + 4) % 4; self.setState({ a: i, aAdim: self.state.aAdim + d, aDur: true }); };
      o['oym' + i] = 'oy-m' + (on ? ' on' : ''); o['oyh' + i] = on ? 'false' : 'true';
      o['oec' + i] = 'oe-cip' + (eb ? ' on' : ''); o['oep' + i] = eb ? 'true' : 'false';
      o['oeg' + i] = function () { self.setState({ b: i, bDur: true }); };
      o['oem' + i] = 'oe-m' + (eb ? ' on' : ''); o['oeh' + i] = eb ? 'false' : 'true'; })(i);
    for (var j = 0; j < 5; j++) (function (j) { var ac = j === S.c;
      o['okc' + j] = 'ok-sayfa' + (j === 0 ? ' kapak' : '') + (j < S.c ? ' gecti' : ''); o['okh' + j] = ac ? 'false' : 'true'; o['okt' + j] = ac ? '0' : '-1';
      o['okg' + j] = function () { self.setState({ c: (j + 1) % 5, cDur: true }); }; })(j);
    return o;
  }
}"""

if __name__ == '__main__':
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · Neler yapabiliyor 2', css=S2.MINI_CSS + O.MINI_CSS + CSS) + HTML + TAIL.format(h=int(os.environ.get('OZ2_H', 1900)), js=JS))
    print('yazıldı:', os.path.abspath(OUT))
