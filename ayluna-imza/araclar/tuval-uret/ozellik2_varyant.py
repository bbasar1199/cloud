# LunaDream · "Neler yapabiliyor?" 2. tur (21 Eki). Çalıştır: python3 ozellik2_varyant.py
# Kullanıcı (1. tur Satırlar / Sekmeler / Kaydırmalı için): "Hayır, o da çok boğar; daha iyi bir şeyler mi düşünsek, çok sıkıcı duruyor böyle."
# Liste düzeni tamamen çıkar: ürün büyük, yazı en az. "Işığı aç/kapat" anahtarı yok (17 Eki).
# İlk taslak (A Yörünge 7/5, B Etiketli ürün 6/6, C Masal kitabı 5/3; git geçmişinde d090a34). Eleştirmenin üç seçimi:
#   1 · Aydınlık sahne: B'nin büyük stüdyo fotoğrafı + A'nın etkileri lambanın çevresinde (halkalar, ses dalgaları, rozetler).
#   2 · Gece kadranı: A sadeleşti; düğüm daireleri yok, yayda dört yazı, amber ay noktası yazıdan yazıya; pencere 200 px.
#   3 · Etiketli ürün (güvenli yedek): fotoğraf, dört eylem etiketi, altta tek cümle.
# Eleştirmen düzeltmeleri (hepsine):
#   - Etiketler eylem ("Diski tak", "Işığı kıs", "Ninni çal", "Kablosuz kullan"): Sihirli'nin "ne" kartlarını tekrar etmez.
#   - "[X] ışık seçeneği" sayfada yok; "Üç kademe: kısık, orta, parlak." (3 kademe teyitli).
#   - Disk lambanın tepesine inmez (takıldığı yer çizilmez); disk rozette belirir. Gece fotoğrafı yok (Videolar gösteriyor).
#   - Her durum 6 sn; sekanslar bir kez oynar ve son karede kalır. Ekrana girince tek tur (24 sn), Masal'da durur; dokununca durur.
#     Azaltılmış harekette ilerlemez. Yeni sonsuz döngü yok.
#   - Etkin etiket: lacivert dolgu katmanı (opacity); renk ve gölge canlandırılmaz. Pasif yazılar opak gri, yarı saydam değil.
#   - "Kabloyu çıkar, odaya taşı" yerine "kablo takılı değilken de yanar" (pil süresi ima edilmez).
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL
import sihirli2_varyant as S2
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE-Ozellik2.dc.html')

E = 'cubic-bezier(.2,.7,.2,1)'
FOTO = {'kiz': 'e02351b3be4a1c555c5d760d0bbda723', 'erkek': '0033dfea6282c5bc479c385213661c00'}
DISK = {'kiz': ('4a3a69e8c1d8dddad8c33f8f463b8a0e', 'Ay ve yıldız'), 'erkek': ('b088d2c82561b76f6db997fbc3944059', 'Uzay')}


def model(f):  # sayfada modele bağlı (renderVals: sihKiz / sihErkek)
    return ('<sc-if value="{{sihKiz}}" hint-placeholder-val="{{true}}">' + f('kiz') + '</sc-if>'
            '<sc-if value="{{sihErkek}}" hint-placeholder-val="{{false}}">' + f('erkek') + '</sc-if>')


OZ = [  # (anahtar, eylem etiketi, kadran adı, başlık (2), cümle)
    ('masal', 'Diski tak', 'Masal', 'Diski tak, tavana yansısın', 'Diski tak; masal tavana yansısın.'),
    ('isik', 'Işığı kıs', 'Işık', 'Uyurken en kısığa al', 'Üç kademe: kısık, orta, parlak.'),
    ('ninni', 'Ninni çal', 'Ninni', 'Telefondan ninni çal', 'Telefondan bağla; ninni lambadan çalsın.'),
    ('sarj', 'Kablosuz kullan', 'Şarj', 'Şarj et, kablosuz kullan', 'Kablo takılı değilken de yanar.'),
]

# Rozetler (lambanın altında; etkin duruma göre biri görünür)
ROZET = ('<span class="rz rz-disk">' + model(lambda m: '<img src="/_blob/%s" alt=""><b>%s diski</b>' % DISK[m]) + '</span>'
         '<span class="rz rz-kad">' + ''.join('<i><span>%s</span><span class="e">%s</span></i>' % (w, w) for w in ('Kısık', 'Orta', 'Parlak')) + '</span>'
         '<span class="rz rz-cal"><span class="eq"><i></i><i></i><i></i><i></i></span><b>Ninni çalıyor</b></span>'
         '<span class="rz rz-pil"><span class="rz-bat"><i></i><i></i><i></i><i></i></span><span class="durum"><i>Şarj oluyor</i><i>Kablosuz</i></span></span>')
HALKA = '<div class="hk" aria-hidden="true"><i></i><i></i><i></i></div>'
DALGA = '<div class="dl" aria-hidden="true"><span class="sol"><i></i><i></i><i></i></span><span class="sag"><i></i><i></i><i></i></span></div>'

# Etiketteki minik simge (etkinken bir kez oynar)
EK_IK = {
    'masal': model(lambda m: '<img class="ek-dsk" src="/_blob/%s" alt="">' % DISK[m][0]),
    'isik': '<span class="ek-kd"><i></i><i></i><i></i></span>',
    'ninni': '<span class="eq ek-eq"><i></i><i></i><i></i><i></i></span>',
    'sarj': '<span class="ek-bat"><i></i><i></i><i></i></span>',
}


def foto():
    return model(lambda m: '<img class="ft-img" src="/_blob/%s" alt="LunaDream %s modeli, stüdyo çekimi">' % (FOTO[m], 'Kız' if m == 'kiz' else 'Erkek'))


def etiketler(k, alt):  # k: durum öneki; alt: alttaki etiketlerin üst konumu (px)
    pos = ['left: 12px; top: 14px', 'right: 12px; top: 14px', 'left: 12px; top: %dpx' % alt, 'right: 12px; top: %dpx' % alt]
    return ''.join('<button class="{{%sc%d}}" type="button" style="%s" onClick="{{%sg%d}}" aria-pressed="{{%sp%d}}"><span class="ek-ik">%s</span><span class="ek-ad">%s</span></button>'
                   % (k, i, pos[i], k, i, k, i, EK_IK[o[0]], o[1]) for i, o in enumerate(OZ))


def cumle(k):
    return '<div class="ft-metin" aria-live="polite">' + ''.join('<p class="{{%sm%d}}" aria-hidden="{{%sh%d}}">%s</p>' % (k, i, k, i, o[4]) for i, o in enumerate(OZ)) + '</div>'


# 1 · Aydınlık sahne: çerçeve 358 × 440; lamba merkezi (179, 224)
def aydinlik():
    return ('<div class="{{aCls}}" data-tur="a"><div class="ft">' + foto() + '</div>' + HALKA + DALGA +
            '<div class="rz-yer" aria-hidden="true">' + ROZET + '</div>' + etiketler('a', 380) + '</div>' + cumle('a'))


# 2 · Gece kadranı: panel 358 × 432; pencere merkezi (179, 220), çap 200; yay yarıçapı 136, yazılar 162
YAZI = [(39, 139), (124, 68), (234, 68), (319, 139)]  # θ = -60, -20, 20, 60 derece


def kadran():
    dug = ''.join('<button class="{{bd%d}}" type="button" style="left: %dpx; top: %dpx" onClick="{{bg%d}}" aria-pressed="{{bp%d}}">%s</button>'
                  % (i, x - 32, y - 24, i, i, o[2]) for i, (o, (x, y)) in enumerate(zip(OZ, YAZI)))
    metin = ''.join('<div class="{{bm%d}}" aria-hidden="{{bh%d}}"><h3 class="gk-bas">%s</h3><p class="gk-p">%s</p></div>' % (i, i, o[3], o[4]) for i, o in enumerate(OZ))
    pen = model(lambda m: '<img class="%s" src="/_blob/%s" alt="">' % (m, FOTO[m]))
    return ('<div class="{{bCls}}" data-tur="b">'
            '<div class="gk-yay" aria-hidden="true"><i></i></div>'
            '<div class="gk-kol" aria-hidden="true" style="--a: {{bAci}}deg"><i></i></div>' + HALKA + DALGA +
            '<div class="gk-pen" aria-hidden="true">' + pen + '</div>'
            '<div class="rz-yer" aria-hidden="true">' + ROZET + '</div>' + dug +
            '<div class="gk-metin" aria-live="polite">' + metin + '</div></div>')


# 3 · Etiketli ürün: çerçeve 358 × 420
def etiketli():
    return '<div class="{{cCls}}" data-tur="c"><div class="ft">' + foto() + '</div>' + etiketler('c', 358) + '</div>' + cumle('c')


CSS = r""".pg{background:#F6F1E9;font-size:15px}
.sec{padding:0 16px 44px}
.oneri{display:flex;align-items:center;gap:8px;margin:0 0 6px;padding-top:16px;border-top:1px dashed #D6CAB6;font-size:12px;font-weight:700;color:#A05A1C}
.oneri-alt{margin:0 0 16px;font-size:13px;color:#5C6078;text-wrap:balance}
.pg button{font:inherit;cursor:pointer;-webkit-tap-highlight-color:transparent}
.pg :focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
.h2 span.n{color:#F2A65A}

/* Fotoğraf çerçevesi (1 ve 3): kare fotoğraf üstte, altı zemin rengine erir */
.sa,.et{position:relative;margin-top:16px}
.sa{height:440px}.et{height:420px}
.ft{position:absolute;inset:0;border-radius:22px;overflow:hidden;background:#EEE4DA}
.ft-img{position:absolute;left:0;top:0;width:100%;height:358px;object-fit:cover;-webkit-mask-image:linear-gradient(#000 80%,transparent);mask-image:linear-gradient(#000 80%,transparent)}
.ft-metin{display:grid;align-items:center;min-height:48px;margin-top:12px}
.ft-m{grid-area:1/1;margin:0;font-size:16px;line-height:1.4;color:#1A2142;white-space:nowrap;opacity:0;transform:translateY(6px);transition:opacity .3s EASE,transform .3s EASE}
.ft-m.on{opacity:1;transform:none}

/* Eylem etiketleri: 48 px; etkin olan lacivert dolgu katmanıyla (opacity), yazı rengi anında değişir */
.ek{position:absolute;display:inline-flex;align-items:center;gap:8px;min-height:48px;padding:0 16px 0 7px;border-radius:999px;border:1px solid #E3D8C7;background:#FFFDF9;color:#1A2142;font-size:14px;font-weight:600;white-space:nowrap;isolation:isolate;animation:ekgir .5s EASE both}
.ek::before{content:"";position:absolute;inset:-1px;z-index:-1;border-radius:inherit;background:#1A2142;opacity:0;transition:opacity .3s EASE}
.ek.on::before{opacity:1}
.ek.on{color:#FFFDF9}
.ek:nth-of-type(2){animation-delay:.12s}.ek:nth-of-type(3){animation-delay:.24s}.ek:nth-of-type(4){animation-delay:.36s}
@keyframes ekgir{from{opacity:0;transform:translateY(8px)}}
.ek-ik{display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:#F1E8DA;overflow:hidden}
.ek-dsk{display:block;width:26px;height:26px;border-radius:50%;object-fit:cover}
.ek.on .ek-dsk{animation:dkg .8s EASE both}
.ek-kd{display:flex;gap:3px}
.ek-kd i{width:6px;height:6px;border-radius:50%;background:#1A2142;opacity:.3}
.ek-kd i:first-child{opacity:1}
.ek.on .ek-kd i{background:#A05A1C}
.ek.on .ek-kd i:nth-child(2){animation:kd2 6s EASE both}.ek.on .ek-kd i:nth-child(3){animation:kd3 6s EASE both}
@keyframes kd2{0%,30%{opacity:.3}37%,100%{opacity:1}}
@keyframes kd3{0%,63%{opacity:.3}70%,100%{opacity:1}}
.ek-eq{height:14px;margin:0;animation:none}
.ek-eq i{height:14px;background:#1A2142;animation:none;transform:scaleY(.5)}
.ek-eq i:nth-child(2){transform:scaleY(.8)}.ek-eq i:nth-child(3){transform:scaleY(.4)}.ek-eq i:nth-child(4){transform:scaleY(.65)}
.ek.on .ek-eq i{background:#A05A1C;animation:ses 2s EASE 3}
.ek-bat{position:relative;display:flex;gap:1.5px;width:20px;height:12px;padding:1.5px;border:1.5px solid #1A2142;border-radius:3.5px}
.ek-bat::after{content:"";position:absolute;right:-4px;top:2.5px;width:2px;height:4px;border-radius:0 1px 1px 0;background:#1A2142}
.ek-bat i{flex:1;border-radius:1px;background:#1A2142}
.ek.on .ek-bat i:nth-child(1){animation:rp1 6s EASE both}.ek.on .ek-bat i:nth-child(2){animation:rp2 6s EASE both}.ek.on .ek-bat i:nth-child(3){animation:rp3 6s EASE both}

/* Etki katmanları (1 ve 2): halkalar, ses dalgaları; merkez --mx/--my */
.sa{--mx:179px;--my:224px}
.gk{--mx:179px;--my:220px}
.hk i{position:absolute;left:var(--mx);top:var(--my);border-radius:50%;box-shadow:inset 0 0 0 1.5px #F2A65A;opacity:0;transition:opacity .4s EASE}
.sa .hk i:nth-child(1){width:200px;height:200px;margin:-100px 0 0 -100px}
.sa .hk i:nth-child(2){width:236px;height:236px;margin:-118px 0 0 -118px}
.sa .hk i:nth-child(3){width:272px;height:272px;margin:-136px 0 0 -136px}
.gk .hk i:nth-child(1){width:214px;height:214px;margin:-107px 0 0 -107px}
.gk .hk i:nth-child(2){width:230px;height:230px;margin:-115px 0 0 -115px}
.gk .hk i:nth-child(3){width:246px;height:246px;margin:-123px 0 0 -123px}
.s1 .hk i:nth-child(1){opacity:.9}
.s1 .hk i:nth-child(2){opacity:.55;animation:hk2 6s EASE both}
.s1 .hk i:nth-child(3){opacity:.3;animation:hk3 6s EASE both}
@keyframes hk2{0%,30%{opacity:0;transform:scale(.92)}37%,100%{opacity:.55;transform:none}}
@keyframes hk3{0%,63%{opacity:0;transform:scale(.92)}70%,100%{opacity:.3;transform:none}}
.dl span{position:absolute;top:calc(var(--my) - 24px);width:48px;height:48px}
.sa .dl .sol{left:calc(var(--mx) - 124px)}.sa .dl .sag{left:calc(var(--mx) + 76px)}
.gk .dl .sol{left:calc(var(--mx) - 158px)}.gk .dl .sag{left:calc(var(--mx) + 110px)}
.dl i{position:absolute;inset:0;border-radius:50%;opacity:0}
.dl .sol i{box-shadow:inset 1.5px 0 0 0 #F2A65A}.dl .sag i{box-shadow:inset -1.5px 0 0 0 #F2A65A}
.s2 .dl .sol i{animation:dll 2s EASE 3}.s2 .dl .sag i{animation:dlr 2s EASE 3}
.s2 .dl i:nth-child(2){animation-delay:.67s}.s2 .dl i:nth-child(3){animation-delay:1.33s}
@keyframes dll{0%{opacity:0;transform:none}25%{opacity:1}100%{opacity:0;transform:translateX(-20px) scale(1.25)}}
@keyframes dlr{0%{opacity:0;transform:none}25%{opacity:1}100%{opacity:0;transform:translateX(20px) scale(1.25)}}

/* Rozetler: lambanın altında tek rozet; 13 px; pasif yazı opak gri */
.rz-yer{position:absolute;left:0;right:0;display:grid;justify-items:center;height:32px}
.sa .rz-yer{top:340px}.gk .rz-yer{top:304px}
.rz{grid-area:1/1;display:flex;align-items:center;gap:8px;height:32px;padding:0 12px;border-radius:999px;background:#FFFDF9;box-shadow:inset 0 0 0 1px #E3D8C7;font-size:13px;font-weight:600;color:#1A2142;white-space:nowrap;
  opacity:0;transform:translateY(4px);transition:opacity .35s EASE,transform .35s EASE}
.gk .rz{background:#1A2142;box-shadow:inset 0 0 0 1px rgba(246,241,233,.24);color:#FFFDF9}
.s0 .rz-disk,.s1 .rz-kad,.s2 .rz-cal,.s3 .rz-pil{opacity:1;transform:none}
.rz b{font-weight:600}
.rz-disk img{width:22px;height:22px;border-radius:50%;object-fit:cover}
.s0 .rz-disk img{animation:dkg .9s EASE both}
@keyframes dkg{0%{opacity:0;transform:translateX(24px) rotate(90deg)}100%{opacity:1;transform:none}}
.rz-kad{gap:10px}
.rz-kad i{position:relative;font-style:normal;color:#6B6F86}
.gk .rz-kad i{color:#8E93AE}
.rz-kad .e{position:absolute;left:0;top:0;color:#1A2142;opacity:0}
.gk .rz-kad .e{color:#FFFDF9}
.rz-kad i:nth-child(3) .e{opacity:1}
.s1 .rz-kad i:nth-child(1) .e{animation:kw1 6s EASE both}.s1 .rz-kad i:nth-child(2) .e{animation:kw2 6s EASE both}.s1 .rz-kad i:nth-child(3) .e{animation:kw3 6s EASE both}
@keyframes kw1{0%,30%{opacity:1}37%,100%{opacity:0}}
@keyframes kw2{0%,30%{opacity:0}37%,63%{opacity:1}70%,100%{opacity:0}}
@keyframes kw3{0%,63%{opacity:0}70%,100%{opacity:1}}
.rz-cal .eq{height:14px;margin:0;animation:none}
.rz-cal .eq i{height:14px;animation:none;transform:scaleY(.6)}
.s2 .rz-cal .eq i{animation:ses 2s EASE 3}
.rz-bat{position:relative;display:flex;gap:2px;width:34px;height:17px;padding:2px;border:1.5px solid currentColor;border-radius:5px}
.rz-bat::after{content:"";position:absolute;right:-5px;top:4px;width:3px;height:6px;border-radius:0 2px 2px 0;background:currentColor}
.rz-bat i{flex:1;border-radius:1.5px;background:currentColor}
.s3 .rz-bat i:nth-child(1){animation:rp1 6s EASE both}.s3 .rz-bat i:nth-child(2){animation:rp2 6s EASE both}.s3 .rz-bat i:nth-child(3){animation:rp3 6s EASE both}.s3 .rz-bat i:nth-child(4){animation:rp4 6s EASE both}
@keyframes rp1{0%{opacity:.15}10%,100%{opacity:1}}
@keyframes rp2{0%,10%{opacity:.15}22%,100%{opacity:1}}
@keyframes rp3{0%,22%{opacity:.15}34%,100%{opacity:1}}
@keyframes rp4{0%,34%{opacity:.15}46%,100%{opacity:1}}
.rz-pil .durum{color:inherit;font-size:13px}
.rz-pil .durum i:first-child{opacity:0}
.s3 .rz-pil .durum i:first-child{animation:sd1 6s EASE both}.s3 .rz-pil .durum i:last-child{animation:sd2 6s EASE both}
@keyframes sd1{0%,58%{opacity:1}64%,100%{opacity:0}}
@keyframes sd2{0%,60%{opacity:0}66%,100%{opacity:1}}

/* 2 · Gece kadranı */
.gk{position:relative;height:432px;margin-top:16px;border-radius:28px;background:#1A2142;overflow:hidden;color:#FFFDF9}
.gk-yay{position:absolute;left:43px;top:84px;width:272px;height:136px;overflow:hidden}
.gk-yay i{position:absolute;left:0;top:0;width:272px;height:272px;border-radius:50%;box-shadow:inset 0 0 0 1px rgba(246,241,233,.2)}
.gk-kol{position:absolute;left:43px;top:84px;width:272px;height:272px;transform:rotate(var(--a));transition:transform 1s EASE}
.gk-kol i{position:absolute;left:50%;top:-6px;width:12px;height:12px;margin-left:-6px;border-radius:50%;background:#F2A65A}
.gk-pen{position:absolute;left:79px;top:120px;width:200px;height:200px;border-radius:50%;overflow:hidden;background:#EEE4DA;transition:opacity .5s EASE}
.gk-pen img{position:absolute;left:-30px;top:-68px;width:260px;height:260px;max-width:none}
.gk-pen img.erkek{left:-29px;top:-66px}
.gk.s1 .gk-pen{animation:gkb 6s EASE both}
.gk.s3 .gk-pen{animation:gks 6s EASE both}
@keyframes gkb{0%,30%{opacity:.6}37%,63%{opacity:.8}70%,100%{opacity:1}}
@keyframes gks{0%,58%{opacity:.4}66%,100%{opacity:1}}
.gk-d{position:absolute;width:64px;height:48px;padding:0;border:0;background:none;color:#8E93AE;font-size:14px;font-weight:600}
.gk-d.on{color:#FFFDF9}
.gk-metin{position:absolute;left:20px;right:20px;top:356px;display:grid}
.gk-m{grid-area:1/1;opacity:0;transform:translateY(6px);transition:opacity .35s EASE,transform .35s EASE}
.gk-m.on{opacity:1;transform:none}
.gk-bas{margin:0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:22px;line-height:1.2;letter-spacing:-.01em;color:#FFFDF9}
.gk-p{margin:6px 0 0;font-size:15px;line-height:1.45;color:#B9BED6}
""".replace('EASE', E)

BAS = '<h2 class="h2">Neler<br>yapabiliyor<span class="n">?</span></h2>'

HTML = """<div class="pg">
  <div style="padding: 18px 16px 10px">
    <h1 class="h2" style="font-size: 22px">LunaDream · Neler yapabiliyor? 2. tur, eleştirmenin sırası</h1>
    <p style="margin: 6px 0 0; font-size: 13px; color: #5C6078">Ürün büyük, yazı en az. Etiketler eylem söyler (Sihirli "ne" der). Her durum 6 sn; ekrana girince tek tur, Masal'da durur, dokununca durur. Yeri: Videolar'ın altı, Odası'nın üstü.</p>
  </div>

  <section class="sec">
    <p class="oneri">1 · Aydınlık sahne</p>
    <p class="oneri-alt">Büyük stüdyo fotoğrafı; etkin özelliğin etkisi lambanın çevresinde: üç amber halka, iki yanda ses dalgaları, altta disk, kademe ve pil rozeti.</p>
    """ + BAS + aydinlik() + """
  </section>

  <section class="sec">
    <p class="oneri">2 · Gece kadranı</p>
    <p class="oneri-alt">Beğenilen gece kadranının dili: lacivert sahne, yuvarlak pencerede ürün, yayda dört yazı; amber ay noktası yazıdan yazıya gider.</p>
    """ + BAS + kadran() + """
  </section>

  <section class="sec">
    <p class="oneri">3 · Etiketli ürün</p>
    <p class="oneri-alt">Güvenli yedek: fotoğraf, dört eylem etiketi, altta tek cümle. Etkin etiketin simgesi bir kez oynar.</p>
    """ + BAS + etiketli() + """
  </section>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { a: 0, aDur: false, b: 0, bDur: false, c: 0, cDur: false }; this.tm = {}; }
  componentDidMount() {
    // Ekrana girince tek tur: her durum 6 sn, dört adımda Masal'a döner ve durur. Dokununca o yön durur. Azaltılmış harekette ilerlemez.
    var self = this;
    if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    ['a', 'b', 'c'].forEach(function (k) {
      var el = document.querySelector('[data-tur="' + k + '"]'); if (!el) return;
      var basla = function () { var n = 0;
        var adim = function () { if (self.state[k + 'Dur']) return; var o = {}; o[k] = (self.state[k] + 1) % 4; self.setState(o); if (++n < 4) self.tm[k] = setTimeout(adim, 6000); };
        self.tm[k] = setTimeout(adim, 6000); };
      if (typeof IntersectionObserver === 'undefined') return basla();
      var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); basla(); } }, { threshold: .5 });
      io.observe(el);
    });
  }
  componentWillUnmount() { for (var k in this.tm) clearTimeout(this.tm[k]); }
  renderVals() {
    var self = this, S = this.state, o = { sihKiz: true, sihErkek: false };
    o.aCls = 'sa s' + S.a; o.bCls = 'gk s' + S.b; o.cCls = 'et s' + S.c; o.bAci = -60 + 40 * S.b;
    for (var i = 0; i < 4; i++) (function (i) {
      ['a', 'c'].forEach(function (k) { var on = i === S[k];
        o[k + 'c' + i] = 'ek' + (on ? ' on' : ''); o[k + 'p' + i] = on ? 'true' : 'false';
        o[k + 'g' + i] = function () { var s = {}; s[k] = i; s[k + 'Dur'] = true; self.setState(s); };
        o[k + 'm' + i] = 'ft-m' + (on ? ' on' : ''); o[k + 'h' + i] = on ? 'false' : 'true'; });
      var on = i === S.b;
      o['bd' + i] = 'gk-d' + (on ? ' on' : ''); o['bp' + i] = on ? 'true' : 'false';
      o['bg' + i] = function () { self.setState({ b: i, bDur: true }); };
      o['bm' + i] = 'gk-m' + (on ? ' on' : ''); o['bh' + i] = on ? 'false' : 'true'; })(i);
    return o;
  }
}"""

if __name__ == '__main__':
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · Neler yapabiliyor 2', css=S2.MINI_CSS + CSS) + HTML + TAIL.format(h=int(os.environ.get('OZ2_H', 2249)), js=JS))
    print('yazıldı:', os.path.abspath(OUT))
