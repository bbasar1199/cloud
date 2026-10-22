# LunaDream · "Neler yapabiliyor?" 3. tur: koyu afiş + arayüz kartları, 3 yön (22 Eki). Çalıştır: python3 ozellik3_varyant.py
# Kullanıcı: "Aydınlık sahne kısmını hiç ama hiç beğenmedim, yeni bir tarz deneyelim." (1. tur listeler "çok boğar, sıkıcı"; 2. tur açık
# stüdyo fotoğrafı + çip + halka.) Kullanıcının sitesindeki örnek: koyu zeminde ürün fotoğrafı, üstünde gerçek bir arayüz kartı (afiş).
# Burada aynı dil, markanın renkleriyle: gerçek koyu ürün fotoğrafları (c-an-kiz, c-elde, c-ninni-*, c-*-gunduz), üstünde beyaz arayüz kartları:
#   Masal diski (disk değişir, yalnız kayarken döner) · Işık (kaydırıcı Parlak → Orta → Kısık) · Ninni (telefondan bağlanır, çalar) ·
#   Şarj (pil dolar, fiş çıkar, "Kablosuz"). Kartlar uygulama iddiası taşımaz: lamba bildirim göndermez, ses kaynağı telefon.
# Cam/bulanık efekt, mor gradyan, ışıltı yok. Sekanslar bir kez oynar ve son karede kalır (yeni sonsuz döngü yok); ekrana girince başlar.
#   A · Afiş: tek koyu afiş, dört kart ürünün çevresinde (sitedeki afiş gibi, kart ürünün kenarına biner).
#   B · Hikâye: dört kare, her birinde bir fotoğraf + tek büyük kart + başlık; üstte ilerleme çizgileri; dokununca ileri/geri.
#   C · Bento: dört koyu fotoğraf karosu (geniş, iki kare, geniş), her birinde kart.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL
import sihirli2_varyant as S2
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE-Ozellik3.dc.html')

E = 'cubic-bezier(.2,.7,.2,1)'
B = '/_blob/'
FOTO = {  # modele bağlı koyu fotoğraflar: masal, ışık, ninni, şarj
    'kiz': ['64229e39b184f68336dc1c9b99e8e850', '3b0286a3c7e80c1f887b23193de25c76', '3d214a1ba100aaf3d85bb18a27325237', '2288b7fbcc230bd9d47e25ef6550ce78'],
    'erkek': ['b2c8d9b92ad3541b532e3aa108a74735', '31751eb35473aca04420825deb3c3ce0', '49da18af3a87a3c97bb59cb9dbe8817f', 'cbd70711defa628872683fa471fcac61'],
}
DISKLER = [('Okyanus', 'a24f13e032569f76d64b9b0fbe8d74f7'), ('Uzay', 'b088d2c82561b76f6db997fbc3944059'), ('Ay ve yıldız', '4a3a69e8c1d8dddad8c33f8f463b8a0e')]
BAS = ['Diski tak, tavana yansısın', 'Uyurken ışığı kıs', 'Telefondan ninni çal', 'Şarj et, kablosuz kullan']
KISA = ['Masal', 'Işık', 'Ninni', 'Şarj']


def model(f):
    return ('<sc-if value="{{sihKiz}}" hint-placeholder-val="{{true}}">' + f('kiz') + '</sc-if>'
            '<sc-if value="{{sihErkek}}" hint-placeholder-val="{{false}}">' + f('erkek') + '</sc-if>')


def foto(i, cls='', pos='50% 50%'):
    return model(lambda m: '<img class="%s" src="%s%s" alt="" style="object-position: %s">' % (cls, B, FOTO[m][i], pos))


IK = {
    'disk': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"></circle><circle cx="12" cy="12" r="2"></circle></svg>',
    'isik': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.5"></circle><path d="M12 3v2.5M12 18.5V21M3 12h2.5M18.5 12H21M5.6 5.6l1.8 1.8M16.6 16.6l1.8 1.8M5.6 18.4l1.8-1.8M16.6 7.4l1.8-1.8"></path></svg>',
    'bt': '<svg viewBox="0 0 24 24"><path d="M7 7l10 10-5 5V2l5 5L7 17"></path></svg>',
    'sarj': '<svg viewBox="0 0 24 24"><path d="M13 3L6 13h5l-1 8 7-10h-5z"></path></svg>',
    'fis': '<svg viewBox="0 0 24 24"><path d="M3 12h6M9 8.5h5a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H9zM16 10.5h4M16 13.5h4"></path></svg>',
    'ay': '<svg viewBox="0 0 24 24"><path d="M15.5 4.5a8 8 0 1 0 4 14.4A7 7 0 0 1 15.5 4.5z"></path></svg>',
}


# ---- Arayüz kartları (nw-) ----
def k_disk(g='0s'):
    return ('<div class="nw nw-disk" style="--g: %s"><div class="nw-b">%s<span>Masal diski</span></div><div class="nw-d"><span class="nw-dk">' % (g, IK['disk']) +
            ''.join('<img class="d%d" src="%s%s" alt="">' % (i + 1, B, d) for i, (_, d) in enumerate(DISKLER)) +
            '</span><span class="nw-dt"><span class="nw-ad">' + ''.join('<b class="d%d">%s</b>' % (i + 1, n) for i, (n, _) in enumerate(DISKLER)) +
            '</span><small>6 + 6 disk</small></span></div></div>')


def k_isik(g='0s'):
    return ('<div class="nw nw-isik" style="--g: %s"><div class="nw-b">%s<span>Işık</span></div>' % (g, IK['isik']) +
            '<div class="nw-sl"><i></i><b></b><span class="tut"></span></div>'
            '<div class="nw-kd">' + ''.join('<i><span>%s</span><span class="e">%s</span></i>' % (w, w) for w in ('Kısık', 'Orta', 'Parlak')) + '</div></div>')


def k_ninni(g='0s'):
    return ('<div class="nw nw-ninni" style="--g: %s"><div class="nw-b">%s<span class="nw-dr"><i>Bağlanıyor</i><i>Bağlandı</i></span></div>' % (g, IK['bt']) +
            '<div class="nw-pl"><span class="kap">' + IK['ay'] + '</span><span class="ad"><b>Ninni</b><small>Telefondan</small></span>'
            '<span class="eq"><i></i><i></i><i></i><i></i></span></div><div class="nw-pr"><b></b></div></div>')


def k_sarj(g='0s'):
    return ('<div class="nw nw-sarj" style="--g: %s"><div class="nw-b">%s<span>Şarj</span></div>' % (g, IK['sarj']) +
            '<div class="nw-sj"><span class="fis">' + IK['fis'] + '</span><span class="bat"><i></i><i></i><i></i><i></i></span></div>'
            '<div class="nw-dr"><i>Şarj oluyor</i><i>Kablosuz</i></div></div>')


KART = [k_disk, k_isik, k_ninni, k_sarj]


# A · Afiş: 358 × 480; ürün ortada (c-an-kiz / c-erkek-disk), kartlar köşelerde, kenarlarıyla ürüne biner
def afis():
    yer = ['left: 12px; top: 16px; width: 172px', 'left: 12px; top: 300px; width: 150px', 'right: 12px; top: 112px; width: 168px', 'right: 12px; top: 362px; width: 152px']
    sira = [0, 2, 1, 3]  # giriş sırası: disk, ninni, ışık, şarj
    kartlar = ''
    for n, i in enumerate(sira):
        h = KART[i]('%.1fs' % (n * .5))
        kartlar += h.replace('style="--g:', 'style="%s; --g:' % yer[i], 1)
    return '<div class="{{aCls}}" data-tur="a"><div class="na-f">' + foto(0, 'na-img', '50% 78%') + '</div>' + kartlar + '</div>'


# B · Hikâye: 358 × 540; dört kare, üstte ilerleme; sol üçte bir geri, kalanı ileri
def hikaye():
    pos = ['50% 70%', '0% 40%', '50% 40%', '40% 55%']
    kare = ''.join('<div class="{{bk%d}}" aria-hidden="{{bh%d}}">' % (i, i) + foto(i, 'nb-img', pos[i]) +
                   '<h3 class="nb-bas">%s</h3><div class="nb-kart">%s</div></div>' % (BAS[i], KART[i]('.3s')) for i in range(4))
    cizgi = ''.join('<i class="{{bp%d}}"><b></b></i>' % i for i in range(4))
    return ('<div class="{{bCls}}" data-tur="b"><div class="nb-sahne">' + kare + '</div><div class="nb-p" aria-hidden="true">' + cizgi + '</div>'
            '<button class="nb-geri" type="button" aria-label="Önceki özellik" onClick="{{bGeri}}"></button>'
            '<button class="nb-ileri" type="button" aria-label="Sonraki özellik" onClick="{{bIleri}}"></button></div>')


# C · Bento: geniş (358 × 220), iki kare (173 × 240), geniş (358 × 200)
def bento():
    pos = ['50% 80%', '0% 45%', '50% 45%', '40% 60%']
    kar = ['ng-gen', 'ng-kare', 'ng-kare', 'ng-gen ng-alt']
    return ('<div class="{{cCls}}" data-tur="c">' + ''.join(
        '<div class="ng %s"><span class="ng-f">%s</span><b class="ng-bas">%s</b>%s</div>' % (kar[i], foto(i, 'ng-img', pos[i]), KISA[i] if 0 < i < 3 else BAS[i], KART[i]('%.1fs' % (i * .5)))
        for i in range(4)) + '</div>')


CSS = r""".pg{background:#F6F1E9;font-size:15px}
.sec{padding:0 16px 44px}
.oneri{display:flex;align-items:center;gap:8px;margin:0 0 6px;padding-top:16px;border-top:1px dashed #D6CAB6;font-size:12px;font-weight:700;color:#A05A1C}
.oneri-alt{margin:0 0 16px;font-size:13px;color:#5C6078;text-wrap:balance}
.pg button{font:inherit;cursor:pointer;-webkit-tap-highlight-color:transparent}
.pg :focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
.h2 span.n{color:#F2A65A}

/* Arayüz kartı: beyaz, 18 köşe; koyu fotoğrafın üstünde yumuşak gölgeyle ayrılır (cam/bulanıklık yok) */
.nw{position:absolute;display:flex;flex-direction:column;gap:8px;padding:10px 12px 12px;border-radius:18px;background:#FFFDF9;color:#1A2142;box-shadow:0 10px 28px rgba(8,11,30,.32)}
.bek .nw{opacity:0}
.gir .nw{animation:nwgir .6s EASE both;animation-delay:var(--g)}
@keyframes nwgir{from{opacity:0;transform:translateY(14px)}}
.nw-b{display:flex;align-items:center;gap:6px;font-size:12px;font-weight:600;color:#5C6078;white-space:nowrap}
.nw-b svg{width:16px;height:16px;flex:none;fill:none;stroke:#1A2142;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.nw-dr{position:relative;display:grid}
.nw-dr i{grid-area:1/1;font-style:normal}
.nw-dr i:first-child{opacity:0}
/* Masal diski: disk yalnız kayarken döner (çeyrek tur), durunca sabit; Okyanus → Uzay → Ay ve yıldız (6 sn, bir kez) */
.nw-d{display:flex;align-items:center;gap:10px}
.nw-dk{position:relative;flex:none;width:42px;height:42px;border-radius:50%;box-shadow:0 0 0 1.5px #1A2142;overflow:hidden}
.nw-dk img{position:absolute;inset:3px;width:36px;height:36px;border-radius:50%;object-fit:cover}
.nw-dk .d1,.nw-dk .d2{opacity:0}
.nw-dt{display:flex;flex-direction:column;gap:1px;min-width:0}
.nw-ad{position:relative;display:grid;font-size:15px;line-height:1.25;white-space:nowrap}
.nw-ad b{grid-area:1/1}
.nw-ad .d1,.nw-ad .d2{opacity:0}
.nw-dt small{font-size:12px;color:#5C6078}
.gir .nw-dk .d1{animation:nwd1 6s EASE both;animation-delay:calc(var(--g) + .6s)}.gir .nw-dk .d2{animation:nwd2 6s EASE both;animation-delay:calc(var(--g) + .6s)}.gir .nw-dk .d3{animation:nwd3 6s EASE both;animation-delay:calc(var(--g) + .6s)}
.gir .nw-ad .d1{animation:nwa1 6s EASE both;animation-delay:calc(var(--g) + .6s)}.gir .nw-ad .d2{animation:nwa2 6s EASE both;animation-delay:calc(var(--g) + .6s)}.gir .nw-ad .d3{animation:nwa3 6s EASE both;animation-delay:calc(var(--g) + .6s)}
@keyframes nwd1{0%,30%{opacity:1;transform:none}37%,100%{opacity:0;transform:translateX(-18px) rotate(-90deg)}}
@keyframes nwd2{0%,30%{opacity:0;transform:translateX(18px) rotate(90deg)}37%,63%{opacity:1;transform:none}70%,100%{opacity:0;transform:translateX(-18px) rotate(-90deg)}}
@keyframes nwd3{0%,63%{opacity:0;transform:translateX(18px) rotate(90deg)}70%,100%{opacity:1;transform:none}}
@keyframes nwa1{0%,30%{opacity:1;transform:none}37%,100%{opacity:0;transform:translateY(-6px)}}
@keyframes nwa2{0%,30%{opacity:0;transform:translateY(6px)}37%,63%{opacity:1;transform:none}70%,100%{opacity:0;transform:translateY(-6px)}}
@keyframes nwa3{0%,63%{opacity:0;transform:translateY(6px)}70%,100%{opacity:1;transform:none}}
/* Işık: kaydırıcı Parlak → Orta → Kısık (6 sn, bir kez); son kare Kısık */
.nw-sl{position:relative;height:6px;margin:6px 0 2px;border-radius:3px;background:#E9E0D2}
.nw-sl>b{position:absolute;inset:0;border-radius:3px;background:#F2A65A;transform-origin:0 50%;transform:scaleX(.08)}
.nw-sl .tut{position:absolute;left:0;top:-7px;width:calc(100% - 20px);height:20px}
.nw-sl .tut::after{content:"";position:absolute;left:0;top:0;width:20px;height:20px;border-radius:50%;background:#FFFDF9;box-shadow:0 0 0 1.5px #1A2142}
.gir .nw-sl>b{animation:nws 6s EASE both;animation-delay:calc(var(--g) + .6s)}
.gir .nw-sl .tut{animation:nwt 6s EASE both;animation-delay:calc(var(--g) + .6s)}
@keyframes nws{0%,30%{transform:scaleX(1)}37%,63%{transform:scaleX(.5)}70%,100%{transform:scaleX(.08)}}
@keyframes nwt{0%,30%{transform:translateX(100%)}37%,63%{transform:translateX(50%)}70%,100%{transform:none}}
.nw-kd{display:flex;justify-content:space-between;font-size:12px;font-weight:600}
.nw-kd i{position:relative;font-style:normal;color:#8A8FA6}
.nw-kd .e{position:absolute;left:0;top:0;color:#1A2142;opacity:0}
.nw-kd i:first-child .e{opacity:1}
.gir .nw-kd i:nth-child(3) .e{animation:nwk1 6s EASE both;animation-delay:calc(var(--g) + .6s)}
.gir .nw-kd i:nth-child(2) .e{animation:nwk2 6s EASE both;animation-delay:calc(var(--g) + .6s)}
.gir .nw-kd i:nth-child(1) .e{animation:nwk3 6s EASE both;animation-delay:calc(var(--g) + .6s)}
@keyframes nwk1{0%,30%{opacity:1}37%,100%{opacity:0}}
@keyframes nwk2{0%,30%{opacity:0}37%,63%{opacity:1}70%,100%{opacity:0}}
@keyframes nwk3{0%,63%{opacity:0}70%,100%{opacity:1}}
/* Ninni: telefondan bağlanır, çalar (ses çubukları üç kez); ilerleme dolar */
.nw-pl{display:flex;align-items:center;gap:10px}
.nw-pl .kap{display:grid;place-items:center;flex:none;width:38px;height:38px;border-radius:10px;background:#1A2142}
.nw-pl .kap svg{width:20px;height:20px;fill:#F2A65A}
.nw-pl .ad{display:flex;flex-direction:column;flex:1;min-width:0;line-height:1.25}
.nw-pl .ad b{font-size:15px}.nw-pl .ad small{font-size:12px;color:#5C6078}
.nw-pl .eq{height:16px;margin:0;animation:none}
.nw-pl .eq i{height:16px;animation:none;transform:scaleY(.55)}
.nw-pl .eq i:nth-child(2){transform:scaleY(.9)}.nw-pl .eq i:nth-child(3){transform:scaleY(.4)}.nw-pl .eq i:nth-child(4){transform:scaleY(.7)}
.gir .nw-pl .eq i{animation:ses 2s EASE 3;animation-delay:calc(var(--g) + 2s)}
.nw-pr{position:relative;height:4px;border-radius:2px;background:#E9E0D2;overflow:hidden}
.nw-pr b{position:absolute;inset:0;background:#1A2142;transform-origin:0 50%;transform:scaleX(.62)}
.gir .nw-pr b{animation:nwp 6s linear both;animation-delay:calc(var(--g) + .6s)}
@keyframes nwp{0%,25%{transform:scaleX(0)}100%{transform:scaleX(.62)}}
.gir .nw-ninni .nw-dr i:first-child{animation:nwr1 6s EASE both;animation-delay:calc(var(--g) + .6s)}.gir .nw-ninni .nw-dr i:last-child{animation:nwr2 6s EASE both;animation-delay:calc(var(--g) + .6s)}
@keyframes nwr1{0%,20%{opacity:1}25%,100%{opacity:0}}
@keyframes nwr2{0%,22%{opacity:0}27%,100%{opacity:1}}
/* Şarj: pil dolar, fiş çıkar, "Kablosuz" (lamba çizilmez; pil süresi yok) */
.nw-sj{display:flex;align-items:center;gap:6px;height:30px}
.nw-sj .fis{width:26px;height:26px;opacity:0}
.nw-sj .fis svg{width:26px;height:26px;fill:none;stroke:#1A2142;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.nw-sj .bat{position:relative;display:flex;gap:3px;width:64px;height:28px;padding:3px;border:1.5px solid #1A2142;border-radius:7px}
.nw-sj .bat::after{content:"";position:absolute;right:-6px;top:8px;width:4px;height:9px;border-radius:0 2px 2px 0;background:#1A2142}
.nw-sj .bat i{flex:1;border-radius:2.5px;background:#1A2142}
.gir .nw-sj .bat i:nth-child(1){animation:pl1x 6s EASE both;animation-delay:calc(var(--g) + .6s)}.gir .nw-sj .bat i:nth-child(2){animation:pl2x 6s EASE both;animation-delay:calc(var(--g) + .6s)}
.gir .nw-sj .bat i:nth-child(3){animation:pl3x 6s EASE both;animation-delay:calc(var(--g) + .6s)}.gir .nw-sj .bat i:nth-child(4){animation:pl4x 6s EASE both;animation-delay:calc(var(--g) + .6s)}
@keyframes pl1x{0%{opacity:.12}10%,100%{opacity:1}}
@keyframes pl2x{0%,10%{opacity:.12}22%,100%{opacity:1}}
@keyframes pl3x{0%,22%{opacity:.12}34%,100%{opacity:1}}
@keyframes pl4x{0%,34%{opacity:.12}46%,100%{opacity:1}}
.gir .nw-sj .fis{animation:nwf 6s EASE both;animation-delay:calc(var(--g) + .6s)}
@keyframes nwf{0%,56%{opacity:1;transform:none}64%,100%{opacity:0;transform:translateX(-10px)}}
.nw-sarj .nw-dr{font-size:13px;font-weight:600}
.gir .nw-sarj .nw-dr i:first-child{animation:nws1 6s EASE both;animation-delay:calc(var(--g) + .6s)}.gir .nw-sarj .nw-dr i:last-child{animation:nws2 6s EASE both;animation-delay:calc(var(--g) + .6s)}
@keyframes nws1{0%,58%{opacity:1}64%,100%{opacity:0}}
@keyframes nws2{0%,60%{opacity:0}66%,100%{opacity:1}}

/* A · Afiş */
.na{position:relative;height:480px;margin-top:16px;border-radius:24px;overflow:hidden;background:#141A36}
.na-f,.na-img{position:absolute;inset:0;width:100%;height:100%}
.na-img{object-fit:cover}

/* B · Hikâye */
.nb{position:relative;height:540px;margin-top:16px;border-radius:24px;overflow:hidden;background:#141A36;color:#FFFDF9}
.nb-sahne{position:absolute;inset:0}
.nb-k{position:absolute;inset:0;opacity:0;transition:opacity .5s EASE}
.nb-k.on{opacity:1}
.nb-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.nb-k.on .nb-img{animation:nbz 6s linear both}
@keyframes nbz{from{transform:scale(1.04)}to{transform:none}}
.nb-k::before{content:"";position:absolute;left:0;right:0;top:0;height:200px;z-index:1;background:linear-gradient(rgba(12,16,39,.72),rgba(12,16,39,0))}
.nb-bas{position:absolute;left:20px;right:20px;top:34px;z-index:2;margin:0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:28px;line-height:1.08;letter-spacing:-.015em;text-wrap:balance}
.nb-kart{position:absolute;left:16px;right:16px;bottom:16px;z-index:2}
.nb-kart .nw{position:relative;left:auto;right:auto;padding:14px 16px 16px;gap:10px}
.nb-p{position:absolute;left:12px;right:12px;top:12px;z-index:3;display:flex;gap:4px}
.nb-p i{flex:1;height:3px;border-radius:2px;background:rgba(255,253,249,.3);overflow:hidden}
.nb-p b{display:block;height:100%;background:#FFFDF9;transform-origin:0 50%;transform:scaleX(0)}
.nb-p i.ok b{transform:none}
.nb-p i.on b{animation:nbp 6s linear both}
.nb.dur .nb-p i.on b{animation:none;transform:none}
@keyframes nbp{from{transform:scaleX(0)}to{transform:none}}
.nb-geri,.nb-ileri{position:absolute;top:0;bottom:120px;z-index:4;padding:0;border:0;background:none}
.nb-geri{left:0;width:33%}.nb-ileri{right:0;width:67%}
.nb .nw{opacity:1}
.nb-k:not(.on) .nw *{animation:none!important}

/* C · Bento */
.nc{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:16px}
.ng{position:relative;overflow:hidden;border-radius:22px;background:#141A36;color:#FFFDF9}
.ng-gen{grid-column:1/-1;height:230px}
.ng-kare{height:250px}
.ng-alt{height:200px}
.ng-f,.ng-img{position:absolute;inset:0;width:100%;height:100%}
.ng-img{object-fit:cover}
.ng::before{content:"";position:absolute;left:0;right:0;top:0;height:110px;z-index:1;background:linear-gradient(rgba(12,16,39,.7),rgba(12,16,39,0))}
.ng-bas{position:absolute;left:16px;right:16px;top:14px;z-index:2;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:20px;line-height:1.1}
.ng .nw{z-index:2;left:12px;bottom:12px}
.ng-gen .nw{width:190px}
.ng-kare .nw{left:8px;right:8px;bottom:8px;padding:10px}
.ng-kare .nw-pl{gap:8px}
.ng-kare .nw-pl .kap{width:32px;height:32px}
""".replace('EASE', E)

HTML = """<div class="pg">
  <div style="padding: 18px 16px 10px">
    <h1 class="h2" style="font-size: 22px">LunaDream · Neler yapabiliyor? 3. tur: koyu afiş + arayüz kartları</h1>
    <p style="margin: 6px 0 0; font-size: 13px; color: #5C6078">Sitendeki afiş dili: koyu ürün fotoğrafı, üstünde gerçek arayüz kartı. Kartlar: Masal diski, Işık, Ninni, Şarj; her biri bir kez oynar ve son karede kalır. Ekrana girince başlar.</p>
  </div>

  <section class="sec">
    <p class="oneri">A · Afiş</p>
    <p class="oneri-alt">Tek koyu afiş; dört kart ürünün çevresinde, kenarlarıyla ürüne biner. Sırayla belirir.</p>
    <h2 class="h2">Neler<br>yapabiliyor<span class="n">?</span></h2>
    """ + afis() + """
  </section>

  <section class="sec">
    <p class="oneri">B · Hikâye</p>
    <p class="oneri-alt">Instagram hikâyesi gibi: dört kare, her birinde bir fotoğraf, başlık ve tek büyük kart. 6 sn'de geçer, dokununca ileri/geri.</p>
    <h2 class="h2">Neler<br>yapabiliyor<span class="n">?</span></h2>
    """ + hikaye() + """
  </section>

  <section class="sec">
    <p class="oneri">C · Bento</p>
    <p class="oneri-alt">Dört koyu fotoğraf karosu; her birinde bir kart. Hepsi aynı anda görünür.</p>
    <h2 class="h2">Neler<br>yapabiliyor<span class="n">?</span></h2>
    """ + bento() + """
  </section>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { b: 0, bDur: false }; }
  componentDidMount() {
    // A ve C: ekrana girince kartlar sırayla belirir ve sekanslar bir kez oynar. B: ekrana girince 6 sn'de bir geçer, son karede durur.
    var self = this, azH = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (azH || typeof IntersectionObserver === 'undefined') return;
    ['a', 'c'].forEach(function (k) { var el = document.querySelector('[data-tur="' + k + '"]'); if (!el) return;
      var s = {}; s[k + 'On'] = false; self.setState(s);
      var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); var o = {}; o[k + 'On'] = true; self.setState(o); } }, { threshold: .4 }); io.observe(el); });
    var hb = document.querySelector('[data-tur="b"]');
    if (hb) { var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); self.setState({ bGo: true });
      var adim = function () { if (self.state.bDur || self.state.b >= 3) return; self.setState({ b: self.state.b + 1 }); self.tb = setTimeout(adim, 6000); };
      self.tb = setTimeout(adim, 6000); } }, { threshold: .5 }); io.observe(hb); }
  }
  componentWillUnmount() { clearTimeout(this.tb); }
  renderVals() {
    var self = this, S = this.state, o = { sihKiz: true, sihErkek: false };
    o.aCls = 'na' + (S.aOn === false ? ' bek' : S.aOn ? ' gir' : '');
    o.cCls = 'nc' + (S.cOn === false ? ' bek' : S.cOn ? ' gir' : '');
    o.bCls = 'nb' + (S.bDur ? ' dur' : '');
    for (var i = 0; i < 4; i++) { var on = i === S.b;
      o['bk' + i] = 'nb-k' + (on ? ' on' + (S.bGo || S.bDur ? ' gir' : '') : ''); o['bh' + i] = on ? 'false' : 'true';
      o['bp' + i] = i < S.b ? 'ok' : (on ? 'on' : ''); }
    o.bGeri = function () { self.setState({ b: Math.max(0, self.state.b - 1), bDur: true }); };
    o.bIleri = function () { self.setState({ b: Math.min(3, self.state.b + 1), bDur: true }); };
    return o;
  }
}"""

if __name__ == '__main__':
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · Neler yapabiliyor 3', css=S2.MINI_CSS + CSS) + HTML + TAIL.format(h=int(os.environ.get('OZ3_H', 2542)), js=JS))
    print('yazıldı:', os.path.abspath(OUT))
