# LunaDream · "Neler yapabiliyor?" 3. tur: koyu afiş + arayüz kartları (22 Eki). Çalıştır: python3 ozellik3_varyant.py
# Kullanıcı: "Aydınlık sahne kısmını hiç ama hiç beğenmedim, yeni bir tarz deneyelim." (1. tur listeler "çok boğar, sıkıcı"; 2. tur açık
# stüdyo fotoğrafı + çip + halka.) Kullanıcının sitesindeki örnek: koyu zeminde ürün fotoğrafı, arayüz kartı ürünün arkasına girer (afiş).
# İlk taslak (git f2c6b0c): A Afiş 7/7, B Hikâye 8/4, C Bento 5/5. Eleştirmenin seçimi ve düzeltmeleri:
#   1 · A "ürün önde": lamba kesimi kartların önünde (kartlar ürünün arkasına girer). Fotoğraf yerel Real-ESRGAN ile x2, kesim rembg
#       (isnet-general-use) ile; ikisi aynı object-fit/position ile üst üste. Kartta ürüne bakan kenara iç boşluk, içerik dışa yaslı.
#   2 · Işık kartı lambayı kısar: kaydırıcı Parlak → Orta → Kısık giderken lambanın koyu kopyası (brightness .68, sabit) ve çevresindeki
#       koyu hale yalnız opacity ile belirir; son kare Kısık.
#   3 · Masal kartında "takma anı": diskin nasıl takıldığı teyit edilmedi, çizilmez; kart başlığı eylem ("Diski tak"). [teyit sorulacak]
#   Kart başlıkları eylem; gölge yok (1 px çizgi); pasif yazı #5C6078; ray #F1E8DA. Kartlar sırayla girer (0 / 0,5 / 1 / 1,5 sn), sekanslar
#   tek tek oynar (2,1 / 4,5 / 6,9 / 9,3 sn, her biri 2,4 sn), sonra durur. Kartlar dokunulmaz (resim), sahte kontrol yok.
#   B · Hikâye (yedek): Ken Burns yok, geçişte başlıklar üst üste binmez, tur Masal'a dönüp durur.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL
import sihirli2_varyant as S2
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE-Ozellik3.dc.html')

E = 'cubic-bezier(.2,.7,.2,1)'
B = '/_blob/'
AFIS = {'kiz': ('9fc836c3d9ab1f8fb163f2f255034bbc', '64acd86736049ff811d5db5e441aed6b'),      # c-an-kiz x2, lamba + disk yığını kesimi
        'erkek': ('d78da0ee8e43fa98686a43e648e14295', '55988cac00dcbf39b9ec247b6ccd9e3e')}    # c-erkek-disk x2, robot kesimi
FOTO = {  # B: masal, ışık, ninni, şarj
    'kiz': ['9fc836c3d9ab1f8fb163f2f255034bbc', '3b0286a3c7e80c1f887b23193de25c76', '3d214a1ba100aaf3d85bb18a27325237', '2288b7fbcc230bd9d47e25ef6550ce78'],
    'erkek': ['d78da0ee8e43fa98686a43e648e14295', '31751eb35473aca04420825deb3c3ce0', '49da18af3a87a3c97bb59cb9dbe8817f', 'cbd70711defa628872683fa471fcac61'],
}
DISKLER = [('Okyanus', 'a24f13e032569f76d64b9b0fbe8d74f7'), ('Uzay', 'b088d2c82561b76f6db997fbc3944059'), ('Ay ve yıldız', '4a3a69e8c1d8dddad8c33f8f463b8a0e')]
BAS = ['Diski tak, tavana yansısın', 'Uyurken ışığı kıs', 'Telefondan ninni çal', 'Şarj et, kablosuz kullan']


def model(f):
    return ('<sc-if value="{{sihKiz}}" hint-placeholder-val="{{true}}">' + f('kiz') + '</sc-if>'
            '<sc-if value="{{sihErkek}}" hint-placeholder-val="{{false}}">' + f('erkek') + '</sc-if>')


IK = {
    'disk': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"></circle><circle cx="12" cy="12" r="2"></circle></svg>',
    'isik': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.5"></circle><path d="M12 3v2.5M12 18.5V21M3 12h2.5M18.5 12H21M5.6 5.6l1.8 1.8M16.6 16.6l1.8 1.8M5.6 18.4l1.8-1.8M16.6 7.4l1.8-1.8"></path></svg>',
    'bt': '<svg viewBox="0 0 24 24"><path d="M7 7l10 10-5 5V2l5 5L7 17"></path></svg>',
    'sarj': '<svg viewBox="0 0 24 24"><path d="M13 3L6 13h5l-1 8 7-10h-5z"></path></svg>',
    'fis': '<svg viewBox="0 0 24 24"><path d="M3 12h6M9 8.5h5a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H9zM16 10.5h4M16 13.5h4"></path></svg>',
    'ay': '<svg viewBox="0 0 24 24"><path d="M15.5 4.5a8 8 0 1 0 4 14.4A7 7 0 0 1 15.5 4.5z"></path></svg>',
}


def zaman(g, s, d):  # g: giriş, s: sekans başlangıcı, d: sekans süresi
    return '--g: %s; --s: %s; --d: %s' % (g, s, d)


# ---- Arayüz kartları (nw-): başlık eylem, sekans bir kez oynar, son kare durur ----
def k_disk(z, cls=''):
    return ('<div class="nw nw-disk %s" style="%s"><div class="nw-b">%s<span>Diski tak</span></div><div class="nw-d"><span class="nw-dk">' % (cls, z, IK['disk']) +
            ''.join('<img class="d%d" src="%s%s" alt="">' % (i + 1, B, d) for i, (_, d) in enumerate(DISKLER)) +
            '</span><span class="nw-dt"><span class="nw-ad">' + ''.join('<b class="d%d">%s</b>' % (i + 1, n) for i, (n, _) in enumerate(DISKLER)) +
            '</span><small>6 + 6 disk</small></span></div></div>')


def k_isik(z, cls=''):
    return ('<div class="nw nw-isik %s" style="%s"><div class="nw-b">%s<span>Işığı kıs</span><span class="nw-dr sag">' % (cls, z, IK['isik']) +
            '<i>Parlak</i><i>Orta</i><i>Kısık</i></span></div><div class="nw-sl"><i></i><b></b><span class="tut"></span><em></em><em></em><em></em></div></div>')


def k_ninni(z, cls=''):
    return ('<div class="nw nw-ninni %s" style="%s"><div class="nw-b">%s<span>Telefondan çal</span></div>' % (cls, z, IK['bt']) +
            '<div class="nw-pl"><span class="kap">' + IK['ay'] + '</span><span class="ad"><b>Ninni</b><small class="nw-dr"><i>Bağlanıyor</i><i>Çalıyor</i></small></span>'
            '<span class="eq"><i></i><i></i><i></i><i></i></span></div><div class="nw-pr"><b></b></div></div>')


def k_sarj(z, cls=''):
    return ('<div class="nw nw-sarj %s" style="%s"><div class="nw-b">%s<span>Şarj et</span></div>' % (cls, z, IK['sarj']) +
            '<div class="nw-sj"><span class="fis">' + IK['fis'] + '</span><span class="bat"><i></i><i></i><i></i><i></i></span></div>'
            '<div class="nw-dr alt"><i>Şarj oluyor</i><i>Kablosuz</i></div></div>')


# A · Afiş (ürün önde): 358 × 480. Katmanlar: fotoğraf → koyu hale → kartlar → kesim → kesimin koyu kopyası (Işık sekansıyla belirir)
def afis():
    gor = lambda i, cls: model(lambda m: '<img class="%s %s" src="%s%s" alt="">' % (cls, m, B, AFIS[m][i]))
    kartlar = (k_disk(zaman('0s', '2.1s', '2.4s'), 'k-disk') + k_ninni(zaman('.5s', '4.5s', '2.4s'), 'k-ninni') +
               k_isik(zaman('1s', '6.9s', '2.4s'), 'k-isik') + k_sarj(zaman('1.5s', '9.3s', '2.4s'), 'k-sarj'))
    return ('<div class="{{aCls}}" data-tur="a" aria-label="LunaDream: diski tak, telefondan ninni çal, ışığı kıs, şarj et">' + gor(0, 'na-img') + '<span class="na-hale" aria-hidden="true"></span>' +
            '<div aria-hidden="true">' + kartlar + '</div>' + gor(1, 'na-kes') + gor(1, 'na-kes koyu') + '</div>')


# B · Hikâye (yedek): 358 × 540
def hikaye():
    pos = ['50% 75%', '0% 40%', '50% 40%', '40% 55%']
    kart = [k_disk, k_isik, k_ninni, k_sarj]
    kare = ''.join('<div class="{{bk%d}}" aria-hidden="{{bh%d}}">' % (i, i) +
                   model(lambda m, i=i: '<img class="nb-img" src="%s%s" alt="" style="object-position: %s">' % (B, FOTO[m][i], pos[i])) +
                   '<h3 class="nb-bas">%s</h3><div class="nb-kart">%s</div></div>' % (BAS[i], kart[i](zaman('.3s', '.9s', '4.2s'))) for i in range(4))
    cizgi = ''.join('<i class="{{bp%d}}"><b></b></i>' % i for i in range(4))
    return ('<div class="{{bCls}}" data-tur="b"><div class="nb-sahne">' + kare + '</div><div class="nb-p" aria-hidden="true">' + cizgi + '</div>'
            '<button class="nb-geri" type="button" aria-label="Önceki özellik" onClick="{{bGeri}}"></button>'
            '<button class="nb-ileri" type="button" aria-label="Sonraki özellik" onClick="{{bIleri}}"></button></div>')


CSS = r""".pg{background:#F6F1E9;font-size:15px}
.sec{padding:0 16px 44px}
.oneri{display:flex;align-items:center;gap:8px;margin:0 0 6px;padding-top:16px;border-top:1px dashed #D6CAB6;font-size:12px;font-weight:700;color:#A05A1C}
.oneri-alt{margin:0 0 16px;font-size:13px;color:#5C6078;text-wrap:balance}
.pg button{font:inherit;cursor:pointer;-webkit-tap-highlight-color:transparent}
.pg :focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
.h2 span.n{color:#F2A65A}

/* Arayüz kartı: beyaz, 18 köşe, 1 px çizgi (gölge yok). --g giriş, --s sekans başlangıcı, --d sekans süresi */
.nw{position:absolute;display:flex;flex-direction:column;gap:8px;padding:10px 12px 12px;border-radius:18px;background:#FFFDF9;color:#1A2142;box-shadow:inset 0 0 0 1px rgba(26,33,66,.1);--g:0s;--s:.6s;--d:6s}
.bek .nw{opacity:0}
.gir .nw{animation:nwgir .6s EASE both;animation-delay:var(--g)}
@keyframes nwgir{from{opacity:0;transform:translateY(14px)}}
.nw-b{display:flex;align-items:center;gap:6px;font-size:13px;font-weight:700;color:#1A2142;white-space:nowrap}
.nw-b svg{width:16px;height:16px;flex:none;fill:none;stroke:#1A2142;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.nw-dr{position:relative;display:grid}
.nw-dr i{grid-area:1/1;font-style:normal;opacity:0}
.nw-dr i:last-child{opacity:1}
.nw-dr.sag{margin-left:auto;font-size:12px;font-weight:600;color:#5C6078}
/* Diski tak: Okyanus → Uzay → Ay ve yıldız; disk yalnız kayarken çeyrek tur döner, durunca sabit */
.nw-d{display:flex;align-items:center;gap:10px}
.nw-dk{position:relative;flex:none;width:42px;height:42px;border-radius:50%;box-shadow:0 0 0 1.5px #1A2142;overflow:hidden}
.nw-dk img{position:absolute;inset:3px;width:36px;height:36px;border-radius:50%;object-fit:cover}
.nw-dk .d1,.nw-dk .d2{opacity:0}
.nw-dt{display:flex;flex-direction:column;gap:1px;min-width:0}
.nw-ad{position:relative;display:grid;font-size:15px;font-weight:700;line-height:1.25;white-space:nowrap}
.nw-ad b{grid-area:1/1}
.nw-ad .d1,.nw-ad .d2{opacity:0}
.nw-dt small{font-size:12px;color:#5C6078}
.gir .nw-dk .d1{animation:nwd1 var(--d) EASE both;animation-delay:var(--s)}.gir .nw-dk .d2{animation:nwd2 var(--d) EASE both;animation-delay:var(--s)}.gir .nw-dk .d3{animation:nwd3 var(--d) EASE both;animation-delay:var(--s)}
.gir .nw-ad .d1{animation:nwa1 var(--d) EASE both;animation-delay:var(--s)}.gir .nw-ad .d2{animation:nwa2 var(--d) EASE both;animation-delay:var(--s)}.gir .nw-ad .d3{animation:nwa3 var(--d) EASE both;animation-delay:var(--s)}
@keyframes nwd1{0%,30%{opacity:1;transform:none}37%,100%{opacity:0;transform:translateX(-18px) rotate(-90deg)}}
@keyframes nwd2{0%,30%{opacity:0;transform:translateX(18px) rotate(90deg)}37%,63%{opacity:1;transform:none}70%,100%{opacity:0;transform:translateX(-18px) rotate(-90deg)}}
@keyframes nwd3{0%,63%{opacity:0;transform:translateX(18px) rotate(90deg)}70%,100%{opacity:1;transform:none}}
@keyframes nwa1{0%,30%{opacity:1;transform:none}37%,100%{opacity:0;transform:translateY(-6px)}}
@keyframes nwa2{0%,30%{opacity:0;transform:translateY(6px)}37%,63%{opacity:1;transform:none}70%,100%{opacity:0;transform:translateY(-6px)}}
@keyframes nwa3{0%,63%{opacity:0;transform:translateY(6px)}70%,100%{opacity:1;transform:none}}
/* Işığı kıs: kaydırıcı Parlak → Orta → Kısık; durum sağda; son kare Kısık */
.nw-sl{position:relative;height:6px;margin:8px 0 4px;border-radius:3px;background:#F1E8DA}
.nw-sl>b{position:absolute;inset:0;border-radius:3px;background:#F2A65A;transform-origin:0 50%;transform:scaleX(.08)}
.nw-sl em{position:absolute;top:1px;width:4px;height:4px;margin-left:-2px;border-radius:50%;background:#C9BCA6}
.nw-sl em:nth-of-type(1){left:10px}.nw-sl em:nth-of-type(2){left:50%}.nw-sl em:nth-of-type(3){left:calc(100% - 10px)}
.nw-sl .tut{position:absolute;left:0;top:-7px;z-index:1;width:calc(100% - 20px);height:20px}
.nw-sl .tut::after{content:"";position:absolute;left:0;top:0;width:20px;height:20px;border-radius:50%;background:#FFFDF9;box-shadow:0 0 0 1.5px #1A2142}
.gir .nw-sl>b{animation:nws var(--d) EASE both;animation-delay:var(--s)}
.gir .nw-sl .tut{animation:nwt var(--d) EASE both;animation-delay:var(--s)}
@keyframes nws{0%,30%{transform:scaleX(1)}37%,63%{transform:scaleX(.5)}70%,100%{transform:scaleX(.08)}}
@keyframes nwt{0%,30%{transform:translateX(100%)}37%,63%{transform:translateX(50%)}70%,100%{transform:none}}
.gir .nw-isik .nw-dr i:nth-child(1){animation:nwk1 var(--d) EASE both;animation-delay:var(--s)}
.gir .nw-isik .nw-dr i:nth-child(2){animation:nwk2 var(--d) EASE both;animation-delay:var(--s)}
.gir .nw-isik .nw-dr i:nth-child(3){animation:nwk3 var(--d) EASE both;animation-delay:var(--s)}
@keyframes nwk1{0%,30%{opacity:1}37%,100%{opacity:0}}
@keyframes nwk2{0%,30%{opacity:0}37%,63%{opacity:1}70%,100%{opacity:0}}
@keyframes nwk3{0%,63%{opacity:0}70%,100%{opacity:1}}
/* Telefondan çal: bağlanır, çalar (ses çubukları üç kez), ilerleme dolar */
.nw-pl{display:flex;align-items:center;gap:10px}
.nw-pl .kap{display:grid;place-items:center;flex:none;width:36px;height:36px;border-radius:10px;background:#1A2142}
.nw-pl .kap svg{width:19px;height:19px;fill:#F2A65A}
.nw-pl .ad{display:flex;flex-direction:column;flex:1;min-width:0;line-height:1.25}
.nw-pl .ad b{font-size:15px}.nw-pl .ad small{font-size:12px;color:#5C6078}
.nw-pl .eq{height:16px;margin:0;animation:none}
.nw-pl .eq i{height:16px;animation:none;transform:scaleY(.55)}
.nw-pl .eq i:nth-child(2){transform:scaleY(.9)}.nw-pl .eq i:nth-child(3){transform:scaleY(.4)}.nw-pl .eq i:nth-child(4){transform:scaleY(.7)}
.gir .nw-pl .eq i{animation:ses calc(var(--d) / 3) EASE 3;animation-delay:var(--s)}
.nw-pr{position:relative;height:4px;border-radius:2px;background:#F1E8DA;overflow:hidden}
.nw-pr b{position:absolute;inset:0;background:#1A2142;transform-origin:0 50%;transform:scaleX(.62)}
.gir .nw-pr b{animation:nwp var(--d) EASE both;animation-delay:var(--s)}
@keyframes nwp{0%,25%{transform:scaleX(0)}100%{transform:scaleX(.62)}}
.gir .nw-ninni .nw-dr i:first-child{animation:nwr1 var(--d) EASE both;animation-delay:var(--s)}.gir .nw-ninni .nw-dr i:last-child{animation:nwr2 var(--d) EASE both;animation-delay:var(--s)}
@keyframes nwr1{0%,20%{opacity:1}25%,100%{opacity:0}}
@keyframes nwr2{0%,22%{opacity:0}27%,100%{opacity:1}}
/* Şarj et: pil dolar, fiş çıkar, "Kablosuz" (lamba çizilmez; pil süresi yok) */
.nw-sj{display:flex;align-items:center;gap:6px;height:28px}
.nw-sj .fis{width:24px;height:24px;opacity:0}
.nw-sj .fis svg{width:24px;height:24px;fill:none;stroke:#1A2142;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.nw-sj .bat{position:relative;display:flex;gap:3px;width:58px;height:26px;padding:3px;border:1.5px solid #1A2142;border-radius:7px}
.nw-sj .bat::after{content:"";position:absolute;right:-6px;top:7px;width:4px;height:9px;border-radius:0 2px 2px 0;background:#1A2142}
.nw-sj .bat i{flex:1;border-radius:2.5px;background:#1A2142}
.gir .nw-sj .bat i:nth-child(1){animation:pl1x var(--d) EASE both;animation-delay:var(--s)}.gir .nw-sj .bat i:nth-child(2){animation:pl2x var(--d) EASE both;animation-delay:var(--s)}
.gir .nw-sj .bat i:nth-child(3){animation:pl3x var(--d) EASE both;animation-delay:var(--s)}.gir .nw-sj .bat i:nth-child(4){animation:pl4x var(--d) EASE both;animation-delay:var(--s)}
@keyframes pl1x{0%{opacity:.12}10%,100%{opacity:1}}
@keyframes pl2x{0%,10%{opacity:.12}22%,100%{opacity:1}}
@keyframes pl3x{0%,22%{opacity:.12}34%,100%{opacity:1}}
@keyframes pl4x{0%,34%{opacity:.12}46%,100%{opacity:1}}
.gir .nw-sj .fis{animation:nwf var(--d) EASE both;animation-delay:var(--s)}
@keyframes nwf{0%,56%{opacity:1;transform:none}64%,100%{opacity:0;transform:translateX(-10px)}}
.nw-dr.alt{font-size:13px;font-weight:600}
.gir .nw-sarj .nw-dr i:first-child{animation:nws1 var(--d) EASE both;animation-delay:var(--s)}.gir .nw-sarj .nw-dr i:last-child{animation:nws2 var(--d) EASE both;animation-delay:var(--s)}
@keyframes nws1{0%,58%{opacity:1}64%,100%{opacity:0}}
@keyframes nws2{0%,60%{opacity:0}66%,100%{opacity:1}}

/* A · Afiş (ürün önde) */
.na{position:relative;height:480px;margin-top:16px;border-radius:24px;overflow:hidden;background:#141A36;--op:50% 78%;isolation:isolate}
.bek .na-hale,.bek .na-kes.koyu{opacity:0}
.na-img,.na-kes{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:var(--op);pointer-events:none}
.na-img{z-index:0}
.na-hale{position:absolute;left:50%;top:62%;z-index:1;width:340px;height:340px;margin:-170px 0 0 -170px;border-radius:50%;background:radial-gradient(closest-side,rgba(12,16,39,.35),rgba(12,16,39,0))}
.na .nw{z-index:2;pointer-events:none}
.na-kes{z-index:3}
.na-kes.koyu{z-index:4;filter:brightness(.76)}
.gir .na-hale,.gir .na-kes.koyu{animation:nak 2.4s EASE both;animation-delay:6.9s}
@keyframes nak{0%,30%{opacity:0}37%,63%{opacity:.5}70%,100%{opacity:1}}
/* Kartlar: üstte ikisi tam görünür; alttakiler ürünün arkasına girer, ürüne bakan kenarda iç boşluk */
.k-disk{left:12px;top:16px;width:164px}
.k-ninni{right:12px;top:70px;width:160px}
.k-isik{left:12px;top:236px;width:150px;padding-right:44px!important}
.k-sarj{right:12px;bottom:16px;width:140px;padding-left:54px!important}
.na.erkek .k-isik{top:226px}
.na.erkek .k-sarj{width:128px;padding-left:58px!important;bottom:12px}
.na.erkek .k-sarj .fis{display:none}

/* B · Hikâye (yedek) */
.nb{position:relative;height:540px;margin-top:16px;border-radius:24px;overflow:hidden;background:#141A36;color:#FFFDF9}
.nb-sahne{position:absolute;inset:0}
.nb-k{position:absolute;inset:0;opacity:0;transition:opacity .25s EASE}
.nb-k.on{opacity:1;transition:opacity .45s EASE .2s}
.nb-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.nb-k::before{content:"";position:absolute;left:0;right:0;top:0;height:200px;z-index:1;background:linear-gradient(rgba(12,16,39,.72),rgba(12,16,39,0))}
.nb-bas{position:absolute;left:20px;right:20px;top:34px;z-index:2;margin:0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:24px;line-height:1.1;letter-spacing:-.01em;text-wrap:balance}
.nb-kart{position:absolute;left:16px;right:16px;bottom:16px;z-index:2}
.nb-kart .nw{position:relative;padding:14px 16px 16px;gap:10px}
.nb-p{position:absolute;left:12px;right:12px;top:12px;z-index:3;display:flex;gap:4px}
.nb-p i{flex:1;height:3px;border-radius:2px;background:rgba(255,253,249,.3);overflow:hidden}
.nb-p b{display:block;height:100%;background:#FFFDF9;transform-origin:0 50%;transform:scaleX(0)}
.nb-p i.ok b{transform:none}
.nb-p i.on b{animation:nbp 6s EASE both}
.nb.dur .nb-p i.on b{animation:none;transform:none}
@keyframes nbp{from{transform:scaleX(0)}to{transform:none}}
.nb-geri,.nb-ileri{position:absolute;top:0;bottom:130px;z-index:4;padding:0;border:0;background:none}
.nb-geri{left:0;width:33%}.nb-ileri{right:0;width:67%}
.nb-k:not(.on) .nw *{animation:none!important}
""".replace('EASE', E)

HTML = """<div class="pg">
  <div style="padding: 18px 16px 10px">
    <h1 class="h2" style="font-size: 22px">LunaDream · Neler yapabiliyor? 3. tur, eleştirmenin seçimi</h1>
    <p style="margin: 6px 0 0; font-size: 13px; color: #5C6078">Sitendeki afiş dili: koyu ürün fotoğrafı, arayüz kartları ürünün arkasına girer. Kartlar sırayla gelir, her biri bir kez oynar; Işık kartı lambayı da kısar.</p>
  </div>

  <section class="sec">
    <p class="oneri">1 · Afiş, ürün önde (önerilen)</p>
    <p class="oneri-alt">Tek koyu afiş; lamba kartların önünde. Diski tak → Telefondan çal → Işığı kıs (lamba da kısılır) → Şarj et; sonra durur.</p>
    <h2 class="h2">Neler<br>yapabiliyor<span class="n">?</span></h2>
    """ + afis() + """
  </section>

  <section class="sec">
    <p class="oneri">2 · Hikâye (yedek)</p>
    <p class="oneri-alt">Dört kare, her birinde fotoğraf, başlık ve tek kart; 6 sn'de geçer, Masal'a dönüp durur; dokununca ileri/geri.</p>
    <h2 class="h2">Neler<br>yapabiliyor<span class="n">?</span></h2>
    """ + hikaye() + """
  </section>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { b: 0, bDur: false }; }
  componentDidMount() {
    // A: ekrana girince kartlar sırayla gelir, sekanslar tek tek oynar ve durur. B: 6 sn'de bir geçer, Masal'a dönüp durur.
    var self = this, azH = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (azH || typeof IntersectionObserver === 'undefined') return;
    var ha = document.querySelector('[data-tur="a"]');
    if (ha) { self.setState({ aOn: false }); var ia = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { ia.disconnect(); self.setState({ aOn: true }); } }, { threshold: .4 }); ia.observe(ha); }
    var hb = document.querySelector('[data-tur="b"]');
    if (hb) { var ib = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { ib.disconnect(); self.setState({ bGo: true }); var n = 0;
      var adim = function () { if (self.state.bDur) return; self.setState({ b: (self.state.b + 1) % 4 }); if (++n < 4) self.tb = setTimeout(adim, 6000); };
      self.tb = setTimeout(adim, 6000); } }, { threshold: .5 }); ib.observe(hb); }
  }
  componentWillUnmount() { clearTimeout(this.tb); }
  renderVals() {
    var self = this, S = this.state, o = { sihKiz: true, sihErkek: false };
    o.aCls = 'na' + (o.sihErkek ? ' erkek' : '') + (S.aOn === false ? ' bek' : S.aOn ? ' gir' : '');
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
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · Neler yapabiliyor 3', css=S2.MINI_CSS + CSS) + HTML + TAIL.format(h=int(os.environ.get('OZ3_H', 1618)), js=JS))
    print('yazıldı:', os.path.abspath(OUT))
