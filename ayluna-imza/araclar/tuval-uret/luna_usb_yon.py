# Galaxy USB Projektör · kendine özgü tasarım dili için üç yön (18 Eki). Çalıştır: python3 luna_usb_yon.py
# Kullanıcı: "Orası sadece çocuklara sattığımız bir ürün değil; çocuklar, anne babalar, gençler, birçok kesim alıyor.
# Sayfadaki özel kısımları ona göre yapalım (renk, bölümler); her sayfanın tasarım dili kendine özel olsun."
# Ve: "Şu anki hâlinin de yararı var ki bu kadar sattı; oradaki yüksek kaliteli görselleri, düzeni göz önünde bulundur."
# Canlı sayfadan korunanlar (satan kalıplar): yetişkin yaşam fotoğrafları (çift, Satürn, kelebek, ay, denizanası, kara delik),
# kare galeri + küçük resim şeridi, "Çok al az öde" paketi (1 Adet ₺1.599 / 2 Adet ₺2.399,99), 2×2 özellik kutuları,
# iki büyük buton, geri sayım. Alınmayanlar: 4,7·2467 (gerçek Loox 2,0·7), 90 gün iade, 5K, lens sayısı, 130 m², sağlık iddiaları.
# Ortak marka çekirdeği: Ayluna işareti + yazısı, satın alma akışı (kartla %5 önce, kapıda ikinci, kapıda butonunda fiyat yok),
# 30 gün iade, teyitsiz bilgi köşeli yer tutucu. Gerisi (renk, yazı tipi, bölüm biçimi) her yönde farklı.
#   A · Sinema: sıcak siyah + sinema sarısı, Bricolage Grotesque; tam ekran yaşam fotoğrafı, kaydırmalı sahne kartları
#   B · Gökyüzü paneli: gece laciverti + buz mavisi, Unbounded; canlıdaki kare galeri, sahne seçici (büyük görsel + çipler)
#   C · Ferah: açık zemin + mercan, Archivo Expanded; büyük ölçü rakamları, "Kimin odası?" sekmeleri
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import TAIL, TL_JS
import luna_e as E
CANVAS = os.path.join(HERE, '..', '..', 'canvas')
B = '/_blob/'
I = dict(cift='eae251a225996e67cae4ea4b714d7513', saturn='10b5c03a83fd85a3eb15b3374830001e', kelebek='1697cee7971bbb267fb51dea65064134',
         ay='a2010776792420e44288cfaf26ea36cf', karadelik='ef1770a1ec7be78054cd32a386216a3a', denizanasi='db2afb7bdda9b8175ad05543628d075b',
         siyah1='ca8e068a09abcce3cee3b6b52014e5d4', siyah2='778e6089a2699acbac7bdf05cab5eae1', cocuk='f2da40fb1654492417c640086532631f',
         urun='192e0198aa722e532541f454e8278561', oda='7d5f80214a0664a51946b0ece044e8cb')

FONT = {
    'A': 'family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&amp;family=Figtree:wght@400;500;600;700',
    'B': 'family=Unbounded:wght@500;600;700&amp;family=Onest:wght@400;500;600;700',
    'C': 'family=Archivo:wdth,wght@100..125,400..800',
}


def head(yon, title, css):
    return '''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<title>%s</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?%s&amp;family=Young+Serif&amp;display=swap">
<style>
body{margin:0;background:var(--zemin,#fff)}
%s
</style>
</helmet>
''' % (title, FONT[yon], css)


# Ortak yapı CSS'i: renk ve yazı tipi her yönün değişkenlerinden gelir
ORTAK = r"""
.pg{width:390px;background:var(--zemin);color:var(--yazi);font-family:var(--govde);font-size:15px;line-height:1.5;-webkit-font-smoothing:antialiased;overflow:clip;position:relative}
.pg *{box-sizing:border-box}
.pg button{font:inherit;cursor:pointer}
.pg button:focus-visible,.pg a:focus-visible{outline:2px solid var(--vurgu);outline-offset:3px}
.px{padding-left:16px;padding-right:16px}
.bas-y{font-family:var(--baslik);font-weight:var(--baslik-k,700);letter-spacing:var(--baslik-ls,-.02em);line-height:1.05;margin:0;text-wrap:balance}
.marka{display:flex;align-items:center;gap:6px}
.marka b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:18px;letter-spacing:-.01em}
.u-ust{display:flex;justify-content:space-between;align-items:center;height:52px;padding:0 6px}
.ikon{width:48px;height:48px;display:grid;place-items:center;border:0;background:transparent;color:inherit}
.ikon svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.sayac{display:inline-flex;align-items:center;gap:4px;font-variant-numeric:tabular-nums}
.fiyat{display:flex;align-items:baseline;flex-wrap:wrap;gap:4px 10px;margin:8px 0 0;font-variant-numeric:tabular-nums}
.fiyat b{font-size:22px;font-weight:700;letter-spacing:-.01em}
.fiyat s{font-size:14px;color:var(--soluk)}
.ozler{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:18px}
.oz{display:flex;flex-direction:column;gap:8px;padding:14px;border-radius:var(--r);background:var(--yuzey);box-shadow:inset 0 0 0 1px var(--cizgi)}
.oz svg{width:24px;height:24px;fill:none;stroke:var(--ikon,var(--vurgu));stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.oz b{font-size:15px;line-height:1.25}
.oz span{font-size:13px;color:var(--soluk);line-height:1.35}
.pk-bas{display:flex;align-items:center;gap:10px;margin:24px 0 12px;font-size:13px;font-weight:700;color:var(--etiket)}
.pk-bas::after{content:"";flex:1;height:1px;background:var(--cizgi)}
.pk{display:flex;flex-direction:column;gap:14px}
.pk-k{position:relative;display:flex;align-items:center;gap:12px;width:100%;min-height:84px;padding:10px 14px 10px 10px;border:0;border-radius:var(--r);background:var(--yuzey);color:var(--yazi);text-align:left;box-shadow:inset 0 0 0 1.5px var(--cizgi);transition:transform .2s cubic-bezier(.2,.7,.2,1)}
.pk-k:active{transform:scale(.985)}
.pk-k.on{box-shadow:inset 0 0 0 2px var(--secili)}
.pk-g{flex:none;position:relative;width:60px;height:60px;border-radius:calc(var(--r) - 6px);overflow:hidden;background:#0D0D10}
.pk-g img{width:100%;height:100%;object-fit:cover}
.pk-o{flex:1;min-width:0;line-height:1.25}
.pk-o b{display:block;font-size:17px}
.pk-o span{display:block;margin-top:3px;font-size:13px;color:var(--soluk)}
.pk-s{display:flex;flex-direction:column;align-items:flex-end;text-align:right;line-height:1.2;font-variant-numeric:tabular-nums}
.pk-s b{font-size:18px}
.pk-s s,.pk-s span{font-size:13px;color:var(--soluk);margin-top:2px}
.nokta{flex:none;width:22px;height:22px;border-radius:50%;box-shadow:inset 0 0 0 1.6px var(--cizgi2)}
.nokta i{display:block;width:12px;height:12px;margin:5px;border-radius:50%;background:var(--vurgu);opacity:0;transform:scale(.3);transition:opacity .25s cubic-bezier(.2,.7,.2,1),transform .25s cubic-bezier(.2,.7,.2,1)}
.on .nokta{box-shadow:inset 0 0 0 1.6px var(--secili)}
.on .nokta i{opacity:1;transform:none}
.kurdele{position:absolute;right:14px;top:-11px;padding:2px 10px;border-radius:999px;font-size:12px;font-weight:700;line-height:1.5;white-space:nowrap;background:var(--kurdele-z);color:var(--kurdele-y)}
.hediye{margin:10px 0 0;font-size:13px;font-weight:600;color:var(--etiket)}
.btn1{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;min-height:60px;margin-top:18px;border:0;border-radius:var(--rb);background:var(--btn-z);color:var(--btn-y);font-size:16px;font-weight:700;transition:transform .12s cubic-bezier(.2,.7,.2,1)}
.btn1:active{transform:translateY(2px)}
.btn1 svg{width:18px;height:18px;flex:none;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.btn2{display:flex;align-items:center;justify-content:center;width:100%;min-height:56px;margin-top:12px;border-radius:var(--rb);background:transparent;color:var(--yazi);border:1.5px solid var(--yazi);font-size:14px;font-weight:600}
.yol{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));position:relative;list-style:none;margin:24px 0 0;padding:0;text-align:center}
.yol::before{content:"";position:absolute;left:16.6%;right:16.6%;top:7px;height:1.5px;background:var(--cizgi2)}
.yol li{position:relative;display:flex;flex-direction:column;align-items:center;gap:2px}
.yol li i{width:16px;height:16px;border-radius:50%;background:var(--zemin);box-shadow:inset 0 0 0 2px var(--yazi);margin-bottom:6px}
.yol li:first-child i{background:var(--vurgu);box-shadow:inset 0 0 0 2px var(--vurgu)}
.yol b{font-size:14px}.yol span{font-size:13px;color:var(--soluk)}
.bolum{padding-top:36px;padding-bottom:36px}
.alt-not{margin:12px 16px 0;font-size:12px;color:var(--soluk)}
.noscroll{scrollbar-width:none}.noscroll::-webkit-scrollbar{display:none}
.tak{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:16px}
.tak div{display:flex;flex-direction:column;align-items:center;gap:8px;padding:16px 8px;border-radius:var(--r);text-align:center;font-size:13px;font-weight:600}
.tak svg{width:34px;height:34px;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.tak small{font-size:12px;font-weight:500;opacity:.75}
@media (prefers-reduced-motion:reduce){.pg *{transition:none!important;animation:none!important}}
"""

YONLER = {
    'A': r"""
.pg{--zemin:#F3F1EC;--yazi:#141217;--soluk:#5F5A55;--yuzey:#FFFFFF;--cizgi:#E2DED6;--cizgi2:#CFC9BE;--vurgu:#FFC83D;--ikon:#141217;--etiket:#141217;--secili:#141217;
  --kurdele-z:#FFC83D;--kurdele-y:#141217;--btn-z:#FFC83D;--btn-y:#141217;--r:14px;--rb:14px;--baslik:"Bricolage Grotesque",sans-serif;--govde:"Figtree",sans-serif;--baslik-k:800;--baslik-ls:-.035em}
.koyu{background:#141217;color:#F3EEE7;--yazi:#F3EEE7;--soluk:#A9A39B;--cizgi:rgba(243,238,231,.14);--cizgi2:rgba(243,238,231,.3);--yuzey:#1E1B21;--zemin:#141217}
.u-serit{display:flex;justify-content:center;align-items:center;gap:10px;height:40px;background:#141217;color:#F3EEE7;font-size:13px;font-weight:600}
.u-serit .sayac b{display:inline-grid;place-items:center;min-width:26px;height:24px;padding:0 4px;border-radius:6px;background:#FFC83D;color:#141217;font-size:13px}
.u-serit .sayac i{font-style:normal;color:#FFC83D}
.hero{position:relative;height:540px;overflow:hidden;background:#141217;color:#F3EEE7}
.hero .hf{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .6s cubic-bezier(.2,.7,.2,1)}
.hero .hf.on{opacity:1}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,18,23,.55) 0,rgba(20,18,23,0) 22%,rgba(20,18,23,0) 45%,rgba(20,18,23,.92) 86%)}
.hero .u-ust{position:relative;z-index:2}
.hero-yazi{position:absolute;left:16px;right:16px;bottom:92px;z-index:2}
.hero-yazi .bas-y{font-size:42px;line-height:.95}
.hero-yazi .bas-y span{color:#FFC83D}
.hero-yazi p{margin:10px 0 0;font-size:15px;color:#D8D2C9}
.kucuk{position:absolute;left:16px;right:16px;bottom:18px;z-index:2;display:flex;gap:8px}
.kucuk button{flex:none;width:56px;height:56px;padding:0;border:0;border-radius:10px;overflow:hidden;box-shadow:0 0 0 1.5px rgba(243,238,231,.3);background:#141217}
.kucuk button.on{box-shadow:0 0 0 2px #FFC83D}
.kucuk img{width:100%;height:100%;object-fit:cover}
.al{padding:22px 16px 30px}
.al h1{font-size:30px}
.ozler{gap:0;border-radius:14px;overflow:hidden;box-shadow:inset 0 0 0 1px var(--cizgi)}
.oz{border-radius:0;box-shadow:none;background:transparent;padding:16px 14px}
.oz:nth-child(1),.oz:nth-child(2){border-bottom:1px solid var(--cizgi)}.oz:nth-child(odd){border-right:1px solid var(--cizgi)}
.oz em{font-style:normal;font-family:var(--baslik);font-weight:800;font-size:26px;letter-spacing:-.03em;line-height:1}
.btn1 svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.sahne-serit{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:16px;padding:18px 16px 0}
.sk{position:relative;flex:0 0 272px;height:380px;border-radius:16px;overflow:hidden;scroll-snap-align:start;background:#000}
.sk img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.sk::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,18,23,0) 55%,rgba(20,18,23,.85) 100%)}
.sk b{position:absolute;left:16px;bottom:34px;z-index:1;font-family:var(--baslik);font-weight:800;font-size:28px;letter-spacing:-.03em;color:#F3EEE7}
.sk span{position:absolute;left:16px;bottom:14px;z-index:1;font-size:13px;color:#D8D2C9}
.kim-liste{display:flex;flex-direction:column;margin-top:16px;border-top:1px solid var(--cizgi)}
.kim-s{display:grid;grid-template-columns:116px minmax(0,1fr);gap:14px;align-items:center;padding:12px 0;border-bottom:1px solid var(--cizgi)}
.kim-s img{width:116px;height:84px;border-radius:10px;object-fit:cover}
.kim-s b{display:block;font-family:var(--baslik);font-weight:800;font-size:20px;letter-spacing:-.02em;line-height:1.1}
.kim-s div span{display:block;margin-top:4px;font-size:14px;color:var(--soluk)}
.tak div{background:#1E1B21;color:#F3EEE7}
.tak svg{stroke:#FFC83D}
""",
    'B': r"""
.pg{--zemin:#EEF1F7;--yazi:#0B1022;--soluk:#5A6283;--yuzey:#FFFFFF;--cizgi:#DCE1EC;--cizgi2:#C3CADB;--vurgu:#3FD7E0;--ikon:#3FD7E0;--etiket:#0B1022;--secili:#0B1022;
  --kurdele-z:#0B1022;--kurdele-y:#3FD7E0;--btn-z:#0B1022;--btn-y:#FFFFFF;--r:20px;--rb:16px;--baslik:"Unbounded",sans-serif;--govde:"Onest",sans-serif;--baslik-k:600;--baslik-ls:-.02em}
.koyu{background:#0B1022;color:#EAF0FF;--yazi:#EAF0FF;--soluk:#9AA5C6;--cizgi:rgba(234,240,255,.13);--cizgi2:rgba(234,240,255,.3);--yuzey:#131A33;--zemin:#0B1022}
.u-serit{display:flex;justify-content:center;align-items:center;gap:10px;height:38px;background:#0B1022;color:#9AA5C6;font-size:13px;font-weight:600;border-bottom:1px solid rgba(234,240,255,.08)}
.u-serit .sayac{color:#3FD7E0;font-weight:700}
.u-serit .sayac i{font-style:normal}
.galeri{position:relative;background:#0B1022;color:#EAF0FF;padding-bottom:14px}
.kare-g{position:relative;height:390px;overflow:hidden}
.kare-g img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .5s cubic-bezier(.2,.7,.2,1)}
.kare-g img.on{opacity:1}
.noktalar{position:absolute;left:0;right:0;bottom:12px;display:flex;justify-content:center;gap:6px}
.noktalar i{width:6px;height:6px;border-radius:50%;background:rgba(234,240,255,.4)}.noktalar i.on{background:#3FD7E0}
.kucuk{display:flex;gap:8px;overflow-x:auto;padding:12px 16px 0}
.kucuk button{flex:none;width:58px;height:58px;padding:0;border:0;border-radius:12px;overflow:hidden;box-shadow:0 0 0 1.5px rgba(234,240,255,.2);background:#131A33}
.kucuk button.on{box-shadow:0 0 0 2px #3FD7E0}
.kucuk img{width:100%;height:100%;object-fit:cover}
.al{padding:22px 16px 30px}
.al h1{font-size:24px;line-height:1.15}
.al .alt-b{margin:6px 0 0;font-size:14px;color:var(--soluk)}
.oz .ik{width:42px;height:42px;display:grid;place-items:center;border-radius:12px;background:#0B1022}
.oz .ik svg{width:22px;height:22px}
.pk-k.on{background:#F5FBFC;box-shadow:inset 0 0 0 2px #0B1022}
.sec-p{margin:0 16px;padding:18px 16px 16px;border-radius:24px;background:#131A33}
.sec-g{position:relative;height:220px;border-radius:16px;overflow:hidden;background:#000}
.sec-g img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(1.04);transition:opacity .5s cubic-bezier(.2,.7,.2,1),transform .8s cubic-bezier(.2,.7,.2,1)}
.sec-g img.on{opacity:1;transform:none}
.sec-ad{position:absolute;left:12px;bottom:12px;padding:4px 10px;border-radius:999px;background:rgba(11,16,34,.75);font-size:13px;font-weight:600;color:#EAF0FF}
.cipler{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.cipler button{min-height:44px;padding:0 14px;border:0;border-radius:999px;background:transparent;color:#C9D2EC;box-shadow:inset 0 0 0 1.5px rgba(234,240,255,.2);font-size:14px;font-weight:600}
.cipler button.on{color:#0B1022;background:#3FD7E0;box-shadow:none}
.kim-iz{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:16px}
.kim-t{position:relative;height:200px;border-radius:20px;overflow:hidden;background:#000;color:#EAF0FF}
.kim-t img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.kim-t::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,16,34,0) 40%,rgba(11,16,34,.88) 100%)}
.kim-t div{position:absolute;left:12px;right:12px;bottom:12px;z-index:1;line-height:1.25}
.kim-t b{display:block;font-family:var(--baslik);font-weight:600;font-size:15px}
.kim-t span{display:block;margin-top:3px;font-size:12px;color:#C9D2EC}
.tak div{background:#FFFFFF;color:#0B1022;box-shadow:inset 0 0 0 1px var(--cizgi)}
.tak svg{stroke:#0B1022}
""",
    'C': r"""
.pg{--zemin:#F6F7F9;--yazi:#101216;--soluk:#5E6470;--yuzey:#FFFFFF;--cizgi:#E3E6EB;--cizgi2:#C8CDD5;--vurgu:#FF5A36;--ikon:#FF5A36;--etiket:#101216;--secili:#FF5A36;
  --kurdele-z:#FF5A36;--kurdele-y:#FFFFFF;--btn-z:#101216;--btn-y:#FFFFFF;--r:18px;--rb:999px;--baslik:"Archivo",sans-serif;--govde:"Archivo",sans-serif;--baslik-k:800;--baslik-ls:-.02em}
.bas-y{font-stretch:125%}
.koyu{background:#101216;color:#F2F3F5;--yazi:#F2F3F5;--soluk:#A2A8B3;--cizgi:rgba(242,243,245,.14);--yuzey:#1A1D22;--zemin:#101216}
.u-serit{display:flex;justify-content:center;align-items:center;gap:10px;height:38px;background:#FF5A36;color:#FFFFFF;font-size:13px;font-weight:700}
.u-serit .sayac i{font-style:normal;opacity:.7}
.giris{padding:6px 16px 0}
.giris .bas-y{font-size:33px;line-height:1}
.giris .bas-y span{color:#FF5A36}
.giris p{margin:10px 0 0;font-size:15px;color:var(--soluk)}
.kart-g{position:relative;margin:18px 16px 0;height:300px;border-radius:24px;overflow:hidden;background:#101216}
.kart-g img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .5s cubic-bezier(.2,.7,.2,1)}
.kart-g img.on{opacity:1}
.kucuk{display:flex;gap:8px;overflow-x:auto;padding:12px 16px 0}
.kucuk button{flex:none;width:58px;height:58px;padding:0;border:0;border-radius:14px;overflow:hidden;box-shadow:inset 0 0 0 1px var(--cizgi);background:#fff}
.kucuk button.on{box-shadow:0 0 0 2px #FF5A36}
.kucuk img{width:100%;height:100%;object-fit:cover}
.al{margin:22px 16px 0;padding:20px 16px 22px;border-radius:24px;background:#fff;box-shadow:inset 0 0 0 1px var(--cizgi)}
.al h1{font-size:22px;font-stretch:125%;line-height:1.1}
.olcu{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1px;margin-top:16px;border-radius:16px;overflow:hidden;background:var(--cizgi)}
.olcu div{padding:14px;background:#fff}
.olcu em{display:block;font-style:normal;font-family:var(--baslik);font-stretch:125%;font-weight:800;font-size:28px;letter-spacing:-.03em;line-height:1;color:#101216}
.olcu em small{font-size:15px;font-weight:700}
.olcu span{display:block;margin-top:6px;font-size:13px;color:var(--soluk);line-height:1.35}
.pk-k{background:#F6F7F9;box-shadow:none}
.pk-k.on{background:#fff;box-shadow:inset 0 0 0 2px #FF5A36}
.btn1 svg{width:18px;height:18px;fill:none;stroke:#FF5A36;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.sekme{display:flex;gap:6px;margin-top:16px;padding:4px;border-radius:999px;background:#fff;box-shadow:inset 0 0 0 1px var(--cizgi);overflow-x:auto}
.sekme button{flex:1 0 auto;min-height:44px;padding:0 12px;border:0;border-radius:999px;background:transparent;color:var(--soluk);font-size:13px;font-weight:700;white-space:nowrap}
.sekme button.on{background:#101216;color:#fff}
.kim-g{position:relative;margin-top:12px;height:260px;border-radius:24px;overflow:hidden;background:#101216}
.kim-g img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .5s cubic-bezier(.2,.7,.2,1)}
.kim-g img.on{opacity:1}
.kim-y{margin:12px 2px 0}
.kim-y b{display:block;font-family:var(--baslik);font-stretch:125%;font-weight:800;font-size:20px;letter-spacing:-.02em}
.kim-y span{display:block;margin-top:4px;font-size:14px;color:var(--soluk)}
.sahne-iz{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:16px}
.sahne-iz figure{margin:0}
.sahne-iz img{width:100%;height:96px;border-radius:14px;object-fit:cover;display:block}
.sahne-iz figcaption{margin-top:6px;font-size:12px;font-weight:700;text-align:center}
.tak div{background:#fff;box-shadow:inset 0 0 0 1px var(--cizgi);color:#101216}
.tak svg{stroke:#FF5A36}
""",
}

SAHNE = [('Ay', 'ay', '50% 40%'), ('Satürn', 'saturn', '55% 40%'), ('Kelebekler', 'kelebek', '50% 30%'),
         ('Denizanası', 'denizanasi', '50% 35%'), ('Kara delik', 'karadelik', '50% 30%'), ('Kuzey ışığı', 'cift', '50% 40%')]
KIM = [('Çocuk odası', 'cocuk', 'Uyumadan önce tavana birlikte bakın.', '35% 40%'),
       ('Genç odası', 'kelebek', 'Işığı kapat, odan başka bir yere dönsün.', '50% 30%'),
       ('İkimiz için', 'cift', 'Film yerine tavanda bir akşam.', '50% 40%'),
       ('Kendine zaman', 'ay', 'Gün sonunda ekranı bırak, tavana bak.', '50% 40%')]
GAL = [('cift', 'Çift, odanın duvarında kuzey ışığı ve balina yansıması', '50% 40%'), ('saturn', 'Yatak odası tavanında Satürn yansıması', '55% 40%'),
       ('kelebek', 'Tavanda renkli kelebek yansımaları', '50% 30%'), ('ay', 'Duvarda dolunay yansıması', '50% 35%'), ('siyah2', 'Galaxy USB projektör, 2 adet', '50% 50%')]

IK = dict(
    usb='<svg viewBox="0 0 24 24"><path d="M9 3h6v5H9z"></path><path d="M7 8h10v5a5 5 0 0 1-10 0z"></path><path d="M12 18v3"></path></svg>',
    disk='<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="2.5"></circle><path d="M12 3a9 9 0 0 1 9 9"></path></svg>',
    don='<svg viewBox="0 0 24 24"><path d="M20 12a8 8 0 1 1-2.3-5.6"></path><path d="M20 4v4h-4"></path></svg>',
    olcu='<svg viewBox="0 0 24 24"><rect x="3" y="8" width="18" height="8" rx="1.5"></rect><path d="M7 8v3M11 8v4M15 8v3M19 8v4"></path></svg>',
    laptop='<svg viewBox="0 0 36 36"><rect x="7" y="9" width="22" height="14" rx="2"></rect><path d="M3 27h30"></path><path d="M24 23v4"></path></svg>',
    powerbank='<svg viewBox="0 0 36 36"><rect x="10" y="5" width="16" height="26" rx="3"></rect><path d="M18 31v2"></path><path d="M14 11h8"></path></svg>',
    priz='<svg viewBox="0 0 36 36"><rect x="9" y="12" width="18" height="16" rx="3"></rect><path d="M14 12V7M22 12V7"></path><path d="M18 28v4"></path></svg>',
    ok='<svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"></path></svg>',
    menu='<svg viewBox="0 0 24 24"><path d="M4 8h16M4 16h11"></path></svg>',
    sepet='<svg viewBox="0 0 24 24"><path d="M6 8h12l-1 12H7z"></path><path d="M9 8a3 3 0 0 1 6 0"></path></svg>',
)


def ust(cizgi):
    return ('<div class="u-ust"><button class="ikon" aria-label="Menü">' + IK['menu'] + '</button><span class="marka">' + E.isaret(22, cizgi) +
            '<b>Ayluna</b></span><button class="ikon" aria-label="Sepet">' + IK['sepet'] + '</button></div>')


SERIT = '<div class="u-serit" role="timer" aria-label="{{cdAria}}"><span>Bugüne özel fiyat</span><span class="sayac"><b>{{hh}}</b><i>:</i><b>{{mm}}</b><i>:</i><b>{{ss}}</b></span></div>'
FIYAT = '<p class="fiyat" aria-label="₺1.599,00, önceki fiyat ₺1.999,00, %20 indirim"><b>₺1.599,00</b><s>₺1.999,00</s><span style="font-size: 13px; font-weight: 700; color: var(--etiket)">%20 indirim</span></p>'
OZLER = ('<div class="ozler">'
         '<div class="oz">' + IK['usb'] + '<b>USB ile çalışır</b><span>Laptop, powerbank ya da şarj başlığı.</span></div>'
         '<div class="oz">' + IK['disk'] + '<b>Tema diskleri</b><span>Diski değiştir, tavan değişsin.</span></div>'
         '<div class="oz">' + IK['don'] + '<b>Esnek boyun</b><span>360° çevir: tavan, duvar, köşe.</span></div>'
         '<div class="oz">' + IK['olcu'] + '<b>Küçücük</b><span>Başlık 4 cm, toplam boy 23,5 cm.</span></div></div>')
PAKET = ('<div class="pk-bas">Çok al, az öde</div><div class="pk"><sc-for list="{{paket}}" as="b" hint-placeholder-count="2">'
         '<button class="{{b.cls}}" onClick="{{b.pick}}" aria-pressed="{{b.on}}"><sc-if value="{{b.rib}}" hint-placeholder-val="{{false}}"><span class="kurdele">En avantajlı</span></sc-if>'
         '<span class="pk-g"><img src="{{b.src}}" alt=""></span><span class="pk-o"><b>{{b.t}}</b><span>{{b.sub}}</span></span>'
         '<span class="pk-s"><b>{{b.p}}</b><sc-if value="{{b.hasOld}}" hint-placeholder-val="{{true}}"><s>{{b.old}}</s></sc-if><span>{{b.unit}}</span></span><span class="nokta"><i></i></span></button>'
         '</sc-for></div><p class="hediye">Her kutuda +[10] ücretsiz disk [teyit]</p>')
BUTON = ('<button class="btn1" type="button">{{onLabel}}' + IK['ok'] + '</button><button class="btn2" type="button">Kapıda Ödeme ile Sipariş Ver</button>'
         '<ol class="yol" aria-label="Siparişten teslime"><li><i></i><b>Bugün</b><span>Sipariş verildi</span></li><li><i></i><b>{{kargo}}</b><span>Kargoda</span></li><li><i></i><b>{{teslim}}</b><span>Kapında</span></li></ol>')
TAK = ('<div class="tak"><div>' + IK['laptop'] + 'Laptop<small>USB girişine</small></div><div>' + IK['powerbank'] + 'Powerbank<small>Kablosuz yer</small></div>'
       '<div>' + IK['priz'] + 'Şarj başlığı<small>Prize [kutuda mı?]</small></div></div>')
TEMSIL = '<p class="alt-not">Görseller temsilîdir; desen ve büyüklük diske, odaya ve mesafeye göre değişir. [Bu desenlerin kutudaki disklerde olduğu teyit edilecek.]</p>'


def html_A():
    return ('<div class="pg">' + SERIT +
            '<section class="hero" aria-label="Galaxy USB fotoğrafları"><sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><img class="hf {{f.cls}}" src="{{f.src}}" alt="{{f.n}}" style="object-position: {{f.pos}}"></sc-for>' +
            ust('rgba(243,238,231,.6)') +
            '<div class="hero-yazi"><h2 class="bas-y">Tavanı<br>sahneye çevir<span>.</span></h2><p>Küçük bir USB projektör, koca bir gökyüzü.</p></div>'
            '<div class="kucuk"><sc-for list="{{gal}}" as="f" hint-placeholder-count="5"><button class="{{f.kcls}}" onClick="{{f.pick}}" aria-label="{{f.n}}" aria-pressed="{{f.on}}"><img src="{{f.src}}" alt=""></button></sc-for></div></section>'
            '<section class="al" id="siparis"><h1 class="bas-y">Galaxy USB Projektör</h1>' + FIYAT +
            OZLER.replace('<div class="oz">' + IK['olcu'] + '<b>Küçücük</b>', '<div class="oz"><em>23,5 cm</em><b>Küçücük</b>') + PAKET + BUTON + '</section>'
            '<section class="koyu bolum"><div class="px"><h2 class="bas-y" style="font-size: 30px">Bu gece tavanda<br>ne olsun?</h2></div>'
            '<div class="sahne-serit noscroll"><sc-for list="{{sahne}}" as="s" hint-placeholder-count="3"><div class="sk"><img src="{{s.src}}" alt="{{s.n}} yansıması" style="object-position: {{s.pos}}"><b>{{s.n}}</b><span>Disk değiştir, tavan değişsin</span></div></sc-for><span aria-hidden="true" style="flex: 0 0 6px"></span></div>' +
            TEMSIL.replace('class="alt-not"', 'class="alt-not" style="color: #A9A39B"') + '</section>'
            '<section class="bolum px"><h2 class="bas-y" style="font-size: 30px">Herkesin<br>odasına<span style="color: #E0A800">.</span></h2>'
            '<div class="kim-liste"><sc-for list="{{kim}}" as="k" hint-placeholder-count="4"><div class="kim-s"><img src="{{k.src}}" alt="" style="object-position: {{k.pos}}"><div><b>{{k.n}}</b><span>{{k.t}}</span></div></div></sc-for></div></section>'
            '<section class="koyu bolum px"><h2 class="bas-y" style="font-size: 30px">Nereye<br>takılır?</h2>' + TAK + '</section></div>')


def html_B():
    return ('<div class="pg">' + SERIT +
            '<section class="galeri" aria-label="Galaxy USB fotoğrafları">' + ust('rgba(234,240,255,.6)') +
            '<div class="kare-g"><sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><img class="{{f.cls}}" src="{{f.src}}" alt="{{f.n}}" style="object-position: {{f.pos}}"></sc-for>'
            '<div class="noktalar" aria-hidden="true"><sc-for list="{{gal}}" as="f" hint-placeholder-count="5"><i class="{{f.ncls}}"></i></sc-for></div></div>'
            '<div class="kucuk noscroll"><sc-for list="{{gal}}" as="f" hint-placeholder-count="5"><button class="{{f.kcls}}" onClick="{{f.pick}}" aria-label="{{f.n}}" aria-pressed="{{f.on}}"><img src="{{f.src}}" alt=""></button></sc-for></div></section>'
            '<section class="al" id="siparis"><h1 class="bas-y">Galaxy USB Projektör</h1><p class="alt-b">Bir USB girişi, koca bir gökyüzü.</p>' + FIYAT +
            OZLER.replace('<div class="oz"><svg', '<div class="oz"><span class="ik"><svg').replace('</svg><b>', '</svg></span><b>') + PAKET + BUTON + '</section>'
            '<section class="koyu bolum"><div class="px"><h2 class="bas-y" style="font-size: 22px; line-height: 1.2">Bu gece tavanda<br>ne olsun?</h2><p style="margin: 8px 0 16px; font-size: 14px; color: #9AA5C6">Bir sahne seç; diski değiştirince tavan değişir.</p></div>'
            '<div class="sec-p"><div class="sec-g"><sc-for list="{{sahne}}" as="s" hint-placeholder-count="2"><img class="{{s.cls}}" src="{{s.src}}" alt="{{s.alt}}" style="object-position: {{s.pos}}"></sc-for><span class="sec-ad">{{sahneAd}}</span></div>'
            '<div class="cipler"><sc-for list="{{sahne}}" as="s" hint-placeholder-count="6"><button class="{{s.ccls}}" onClick="{{s.pick}}" aria-pressed="{{s.on}}">{{s.n}}</button></sc-for></div></div>' +
            TEMSIL.replace('class="alt-not"', 'class="alt-not" style="color: #9AA5C6"') + '</section>'
            '<section class="bolum px"><h2 class="bas-y" style="font-size: 22px; line-height: 1.2">Herkesin odasına</h2>'
            '<div class="kim-iz"><sc-for list="{{kim}}" as="k" hint-placeholder-count="4"><div class="kim-t"><img src="{{k.src}}" alt="" style="object-position: {{k.pos}}"><div><b>{{k.n}}</b><span>{{k.t}}</span></div></div></sc-for></div></section>'
            '<section class="bolum px" style="padding-top: 0"><h2 class="bas-y" style="font-size: 22px; line-height: 1.2">Nereye takılır?</h2>' + TAK + '</section></div>')


def html_C():
    olcu = ('<div class="olcu"><div><em>USB</em><span>Laptop, powerbank ya da şarj başlığı.</span></div><div><em>360°</em><span>Esnek boyun: tavan, duvar, köşe.</span></div>'
            '<div><em>4<small> cm</small></em><span>Başlık genişliği.</span></div><div><em>23,5<small> cm</small></em><span>Toplam boy, kablo dahil.</span></div></div>')
    return ('<div class="pg">' + SERIT + ust('rgba(16,18,22,.35)') +
            '<div class="giris"><h2 class="bas-y">Bir USB girişi,<br>koca bir gökyüzü<span>.</span></h2><p>Çocuk odası, genç odası, salon: ışığı kapat, diski seç.</p></div>'
            '<div class="kart-g"><sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><img class="{{f.cls}}" src="{{f.src}}" alt="{{f.n}}" style="object-position: {{f.pos}}"></sc-for></div>'
            '<div class="kucuk noscroll"><sc-for list="{{gal}}" as="f" hint-placeholder-count="5"><button class="{{f.kcls}}" onClick="{{f.pick}}" aria-label="{{f.n}}" aria-pressed="{{f.on}}"><img src="{{f.src}}" alt=""></button></sc-for></div>'
            '<section class="al" id="siparis"><h1 class="bas-y">Galaxy USB Projektör</h1>' + FIYAT + olcu + PAKET + BUTON + '</section>'
            '<section class="bolum px"><h2 class="bas-y" style="font-size: 26px; font-stretch: 125%">Kimin odası?</h2>'
            '<div class="sekme noscroll" role="tablist"><sc-for list="{{kim}}" as="k" hint-placeholder-count="4"><button class="{{k.scls}}" role="tab" onClick="{{k.pick}}" aria-selected="{{k.on}}">{{k.n}}</button></sc-for></div>'
            '<div class="kim-g"><sc-for list="{{kim}}" as="k" hint-placeholder-count="2"><img class="{{k.icls}}" src="{{k.src}}" alt="" style="object-position: {{k.pos}}"></sc-for></div>'
            '<div class="kim-y"><b>{{kimAd}}</b><span>{{kimYazi}}</span></div></section>'
            '<section class="bolum px" style="padding-top: 0"><h2 class="bas-y" style="font-size: 26px; font-stretch: 125%">Tavanda neler olur?</h2>'
            '<div class="sahne-iz"><sc-for list="{{sahne}}" as="s" hint-placeholder-count="6"><figure><img src="{{s.src}}" alt="{{s.n}} yansıması" style="object-position: {{s.pos}}"><figcaption>{{s.n}}</figcaption></figure></sc-for></div>' +
            TEMSIL.replace('class="alt-not"', 'class="alt-not" style="margin-left: 0; margin-right: 0"') + '</section>'
            '<section class="bolum px" style="padding-top: 0"><h2 class="bas-y" style="font-size: 26px; font-stretch: 125%">Nereye takılır?</h2>' + TAK + '</section></div>')


JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { g: 0, adet: 1, sahne: 0, kim: 0, now: Date.now() }; }
  componentDidMount() { var self = this; this.iv = setInterval(function () { self.setState({ now: Date.now() }); }, 1000); }
  componentWillUnmount() { clearInterval(this.iv); }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    """ + TL_JS + """
    var I = """ + str(I) + """;
    var GAL = """ + str([list(x) for x in GAL]) + """;
    var gal = GAL.map(function (g, i) { var on = i === S.g; return { src: B + I[g[0]], n: g[1], pos: g[2], on: on ? 'true' : 'false', cls: on ? 'on' : '', kcls: on ? 'on' : '', ncls: on ? 'on' : '', pick: function () { self.setState({ g: i }); } }; });
    // Paket: canlı sitedeki Kaching fiyatları (1 Adet ₺1.599 / ₺1.999, 2 Adet ₺2.399,99 / ₺3.998)
    var P1 = 1599, C1 = 1999, P2 = 2399.99, C2 = 3998;
    var paket = [
      { n: 1, t: '1 Adet', p: TL(P1, true), old: TL(C1, true), unit: '', sub: '%' + Math.round((1 - P1 / C1) * 100) + ' indirim', src: B + I.siyah1, rib: false },
      { n: 2, t: '2 Adet', p: TL(P2, true), old: TL(C2, true), unit: 'tanesi ' + TL(Math.round(P2 / 2 * 100) / 100, true), sub: TL(2 * P1 - P2, true) + ' kazanç', src: B + I.siyah2, rib: true }
    ].map(function (b) { var on = S.adet === b.n; return { t: b.t, p: b.p, old: b.old, hasOld: !!b.old, unit: b.unit, sub: b.sub, src: b.src, rib: b.rib, on: on ? 'true' : 'false', cls: on ? 'pk-k on' : 'pk-k', pick: function () { self.setState({ adet: b.n }); } }; });
    var total = S.adet === 2 ? P2 : P1, online = Math.round(total * 0.95 * 100) / 100;
    var SAHNE = """ + str([list(x) for x in SAHNE]) + """;
    var sahne = SAHNE.map(function (s, i) { var on = i === S.sahne; return { n: s[0], src: B + I[s[1]], pos: s[2], alt: on ? s[0] + ' yansıması' : '', on: on ? 'true' : 'false', cls: on ? 'on' : '', ccls: on ? 'on' : '', pick: function () { self.setState({ sahne: i }); } }; });
    var KIM = """ + str([list(x) for x in KIM]) + """;
    var kim = KIM.map(function (k, i) { var on = i === S.kim; return { n: k[0], src: B + I[k[1]], t: k[2], pos: k[3], on: on ? 'true' : 'false', scls: on ? 'on' : '', icls: on ? 'on' : '', pick: function () { self.setState({ kim: i }); } }; });
    var AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
    var now = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kd = new Date(now); do { kd.setDate(kd.getDate() + 1); } while (kd.getDay() === 0 || kd.getDay() === 6);
    var t1 = new Date(kd); t1.setDate(t1.getDate() + 3); var t2 = new Date(kd); t2.setDate(t2.getDate() + 7);
    var teslim = t1.getMonth() === t2.getMonth() ? t1.getDate() + '–' + t2.getDate() + ' ' + AY[t2.getMonth()] : t1.getDate() + ' ' + AY[t1.getMonth()] + '–' + t2.getDate() + ' ' + AY[t2.getMonth()];
    function IKI(n) { return n < 10 ? '0' + n : String(n); }
    var ist = new Date(new Date(S.now || Date.now()).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kalan = Math.max(0, new Date(ist.getFullYear(), ist.getMonth(), ist.getDate(), 23, 59, 59, 999).getTime() - ist.getTime());
    var hh = Math.floor(kalan / 3600000), mi = Math.floor(kalan / 60000) % 60, ss = Math.floor(kalan / 1000) % 60;
    return { gal: gal, paket: paket, onLabel: 'Güvenli Ödeme ile Al · ' + TL(online, true), kargo: kd.getDate() + ' ' + AY[kd.getMonth()], teslim: teslim,
      hh: IKI(hh), mm: IKI(mi), ss: IKI(ss), cdAria: 'Bugüne özel fiyatın bitmesine ' + hh + ' saat ' + mi + ' dakika',
      sahne: sahne, sahneAd: SAHNE[S.sahne][0], kim: kim, kimAd: KIM[S.kim][0], kimYazi: KIM[S.kim][2] };
  }
}"""

AD = {'A': ('GalaxyUSB-YonA.dc.html', 'Galaxy USB · Yön A Sinema', html_A), 'B': ('GalaxyUSB-YonB.dc.html', 'Galaxy USB · Yön B Gökyüzü paneli', html_B),
      'C': ('GalaxyUSB-YonC.dc.html', 'Galaxy USB · Yön C Ferah', html_C)}

if __name__ == '__main__':
    for yon, (dosya, baslik, f) in AD.items():
        h = int(os.environ.get('Y_H_' + yon, {'A': 2960, 'B': 2870, 'C': 2550}[yon]))
        open(os.path.join(CANVAS, dosya), 'w', encoding='utf-8').write(head(yon, baslik, ORTAK + YONLER[yon]) + f() + TAIL.format(h=h, js=JS))
        print('yazıldı:', dosya)
