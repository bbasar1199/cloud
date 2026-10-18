# Galaxy USB Projektör · ürün sayfası: Yön A'nın sakin düzeni + animasyonlar (18 Eki). Çalıştır: python3 luna_usb.py
# Kullanıcı (Yön A için): "Sarı rengi beğenmedim; her ürün için o koyu lacivert bizim marka rengimiz, sadece diğer renkler
# değişsin. Ürünümün rengi beyaz. Biraz daha animasyon; Herkesin odası daha iyi UI; güven ve baskılayıcı kısımlar."
# Sonra: "USB adaptör yok; içindeki diskler bunlar ve 12 diskli" (mağaza afişi). Eleştirmenden seçtikleri: %5 butonun içinde,
# baskı kartı tek satır, oda düğmeleri çip. Son olarak: "Yön A'yı seçmiştim, onun daha sakin düzenini kullanalım ama yaptığın
# animasyonları beğendim; onları kullanalım" + "fontlar, renk seçimleri pek hoşuma gitmedi, başka hangi renkleri seçebiliriz".
# Düzen (Yön A): tam ekran fotoğraf, başlık ve küçük resimler görselin içinde; birleşik çizgili özellik kutusu (kart yığını yok);
# koyu bölümlerde yazı görselin içinde. Hareketler önceki turdan (galeri, fiş, disk, boyun, gece lambası, cetvel, kargo, tavana düşen disk,
# hikâye kartı, 30 çentik).
# Renk: lacivert #1A2142 sabit marka; ikinci renk, zemin ve yazı tipi TEMA'dan (kullanıcı seçecek; seçenek panoları GalaxyUSB-Renk-*).
# Kullanılmayanlar: "4,7 · 2467" (gerçek Loox 2,0 · 7), 90 gün, 5K, lens sayısı, 130 m², sağlık iddiaları, kutuda olmayan desenler,
# "USB adaptör hediye", 2 Adet'te üstü çizili "2× eski fiyat", AMEX, sahte oranlı stok çubuğu.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import TAIL, TL_JS, KARGO_JS
import luna_e as E
import luna_usb_yon as Y
CANVAS = os.path.join(HERE, '..', '..', 'canvas')
B = '/_blob/'
I = dict(Y.I, bas='7e1339aefa8d185cd41f6c37b16853c5', kesim='5782766948fef68b7273c061529d6324', afis='be86b4a93cb896b0ad69042a2e915e68')
# Kutudaki 12 film diski (kullanıcının paylaştığı afişin sırası). Afişten kırpıldı, Higgsfield ile 4K büyütüldü (desen aynı), 384px. Adlar desenin tarifidir.
DISK = [('Hilal ve bulutlar', '3966dd40e4ad197b240bee587f2f3c53'), ('Kızıl yıldız', 'f59c74007d5decf352040bde12619017'),
        ('Mavi nebula', '80696da4e0a6cd338d881afa47afd6a0'), ('Kuzey ışığı', '1bc307933815c7618200af85edb0279a'),
        ('Pembe nebula', '8a3d874befb7e043b435c052e811fbd4'), ('Sarmal galaksi', 'bc7b40f5daa14441c8b8eb53f575783d'),
        ('Kozmik göz', '31a0391fbe83323ca017666b3ff6e791'), ('Halkalı gezegen', 'cf986d825d9ff793dc49c28dfcd50946'),
        ('Samanyolu', '87a8e831f6bfc2b2904344cef8ca0db9'), ('Ay ve bulutlar', 'c061d46f449f236fa124e0fd5db599bb'),
        ('Denizanası', '70a65e38024f6dd856edc5da1b822c08'), ('Jüpiter', '0e59d26e798205616eaccafa60267877')]
D = dict((n, B + i) for n, i in DISK)
KES = B + I['kesim']

# Tema: lacivert sabit; v = ikinci renk (koyu zeminde), v2 = açık zeminde okunur tonu
TEMA = {
    'buz': dict(ad='Buz mavisi', alt='Şu anki: buz mavisi, Bricolage Grotesque + Figtree', v='#8FD3FF', v2='#3E8FC4', zemin='#F2F4F8', cizgi='#DDE2EC',
                fb='"Bricolage Grotesque"', fg='"Figtree"', bk=800, bls='-.035em',
                font='family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;500;600;700'),
    'kuzey': dict(ad='Kuzey ışığı', alt='Nane yeşili (kuzey ışığı diskinden), Outfit + DM Sans: ferah, her yaşa', v='#62E6B5', v2='#14855E', zemin='#F1F5F3', cizgi='#DCE5E0',
                  fb='"Outfit"', fg='"DM Sans"', bk=700, bls='-.03em', font='family=Outfit:wght@600;700&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700'),
    'pembe': dict(ad='Pembe nebula', alt='Gül pembesi (pembe nebula diskinden), Sora + Manrope: genç, çift', v='#FF92B5', v2='#C2366B', zemin='#F7F2F4', cizgi='#EBDDE3',
                  fb='"Sora"', fg='"Manrope"', bk=700, bls='-.035em', font='family=Sora:wght@600;700&family=Manrope:wght@400;500;600;700'),
    'mercan': dict(ad='Mercan', alt='Mercan (sarmal galaksinin çekirdeğinden), Plus Jakarta Sans: sıcak, enerjik', v='#FF7A6B', v2='#C3392B', zemin='#F7F4F2', cizgi='#EADFD9',
                   fb='"Plus Jakarta Sans"', fg='"Plus Jakarta Sans"', bk=800, bls='-.035em', font='family=Plus+Jakarta+Sans:wght@400;500;600;700;800'),
    # Kullanıcının seçimi (18 Eki). Eleştirmen düzeltmeleri: açık zeminde ikinci ton arduvaz mavisi (v2, 5,5:1); kahramanda "çevir." tek seferlik eğik.
    'gumus': dict(ad='Ay gümüşü', alt='Gümüş ve lacivert, Fraunces + Figtree: sakin, yetişkin, hediye', v='#D3DCEE', v2='#56658A', zemin='#F4F5F7', cizgi='#E1E4EA',
                  fb='"Fraunces"', fg='"Figtree"', bk=600, bls='-.02em', font='family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=Figtree:wght@400;500;600;700',
                  ek='.hero-y .bas-y em{font-style:italic;font-weight:500;letter-spacing:-.01em}'),
}
# Kullanıcı (18 Eki): "Oradaki (Yön A) tasarım dili daha güzeldi; oradaki yazı fontu… sadece o section'u ve yazı fontunu al." → Ay gümüşü renkleri + Yön A yazı tipi
TEMA['gumus-a'] = dict(TEMA['gumus'], ad='Ay gümüşü · Yön A yazısı', alt='Gümüş ve lacivert, Bricolage Grotesque + Figtree (Yön A)', fb='"Bricolage Grotesque"', fg='"Figtree"', bk=800, bls='-.035em',
                       font='family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Figtree:wght@400;500;600;700',
                       ek='.hero-y .bas-y em{font-weight:500;letter-spacing:-.02em}')
ANA_TEMA = os.environ.get('U_TEMA', 'gumus-a')

GAL = [('oda', 'Komodinde beyaz Galaxy USB projektör, tavanda galaksi', '50% 30%'), ('urun', 'Galaxy USB projektör tavana galaksi yansıtıyor', '50% 30%'),
       ('bas', 'Projektör başlığı yakından', '50% 40%'),
       # Mağazanın ürün afişi (yalnız teyitli bilgiler: 360°, USB, 4 cm, 23,5 cm). Diğer afişler 5K, lens sayısı ya da uydurma yorum taşıdığı için alınmadı.
       ('afis', 'Galaxy USB: esnek gövde, 360° döner başlık; başlık 4 cm, toplam boy 23,5 cm', '50% 50%')]
# Herkesin odasına: hikâye kartı. Disk, kutudaki 12 diskten o odaya önerilen.
KIM = [('Çocuk odası', 'cocuk', 'Masaldan sonra galaksi.', 'Uyumadan önce tavana birlikte bakın.', 'Hilal ve bulutlar', '32% 40%'),
       ('Genç odası', 'denizanasi', 'Odan, kurallar senin.', 'Işığı kapat, oda başka bir yere dönsün.', 'Denizanası', '62% 40%'),
       ('İkimiz için', 'cift', 'Bu akşam sahne tavanda.', 'Film yerine tavanda bir akşam.', 'Kuzey ışığı', '44% 40%'),
       ('Kendine zaman', 'saturn', 'Ekran yok, sadece gökyüzü.', 'Gün sonunda telefonu bırak, tavana bak.', 'Halkalı gezegen', '52% 40%')]

IK = Y.IK
OK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"></path></svg>'
FIS = '<svg class="fis-a" viewBox="0 0 60 30" aria-hidden="true"><g class="fis"><rect class="uc" x="2" y="10" width="10" height="10" rx="1.5"></rect><rect class="gv" x="12" y="7" width="16" height="16" rx="4"></rect><path class="kb" d="M28 15h32"></path></g></svg>'


def head(title, css, font):
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
body{margin:0;background:#F2F4F8}
%s
</style>
</helmet>
''' % (title, font.replace('&', '&amp;'), css)


def tema_css(t):
    return '.pg{--v:%(v)s;--v2:%(v2)s;--zemin:%(zemin)s;--cizgi:%(cizgi)s;--fb:%(fb)s,ui-sans-serif,system-ui,sans-serif;--fg:%(fg)s,ui-sans-serif,system-ui,sans-serif;--bk:%(bk)d;--bls:%(bls)s}\n' % t + t.get('ek', '') + '\n'


CSS = r"""
.pg{--lac:#1A2142;--koyu:#141A36;--koyu2:#1F2850;--yuzey:#FFFFFF;--soluk:#5C6078;--acik:#B9BED6;--ease:cubic-bezier(.2,.7,.2,1);
  width:390px;margin:0 auto;background:var(--zemin);color:var(--lac);font-family:var(--fg);font-size:15px;line-height:1.5;-webkit-font-smoothing:antialiased;overflow:clip;position:relative}
@supports not (overflow:clip){.pg{overflow:hidden}}
.pg *{box-sizing:border-box}
.pg button{font:inherit;color:inherit;cursor:pointer}
.pg a{color:inherit}
.pg button:focus-visible,.pg a:focus-visible,.pg summary:focus-visible{outline:2px solid var(--v2);outline-offset:3px}
.koyu button:focus-visible,.hero button:focus-visible,.hk button:focus-visible{outline-color:var(--v)}
.px{padding-left:16px;padding-right:16px}
.bas-y{font-family:var(--fb);font-weight:var(--bk);letter-spacing:var(--bls);line-height:1;margin:0;text-wrap:balance;font-optical-sizing:auto}
.h2{font-size:32px}
.bas-y .n{color:var(--v2)}
.koyu{background:var(--koyu);color:#EEF2FA}
.koyu .bas-y .n{color:var(--v)}
.bolum{padding-top:44px;padding-bottom:44px}
.alt-b{margin:8px 0 0;font-size:15px;color:var(--soluk)}
.koyu .alt-b{color:var(--acik)}
.alt-not{margin:14px 0 0;font-size:12px;color:var(--soluk)}
.koyu .alt-not{color:var(--acik)}
.noscroll{scrollbar-width:none}.noscroll::-webkit-scrollbar{display:none}
@keyframes sol{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
@keyframes don{to{transform:rotate(360deg)}}
@keyframes dol{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes kb{from{transform:scale(1.02)}to{transform:scale(1.1)}}

/* Üst: marka işareti + yazısı (ortak çekirdek) */
.marka{display:flex;align-items:center;gap:6px}
.marka b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:18px;letter-spacing:-.01em}
.u-ust{display:flex;justify-content:space-between;align-items:center;height:52px;padding:0 6px}
.ikon{width:48px;height:48px;display:grid;place-items:center;border:0;background:transparent}
.ikon svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}

/* Tek sayaç: üst şerit; saniye kutusu her saniye tıklar */
.serit{display:flex;justify-content:center;align-items:center;gap:10px;height:40px;background:var(--koyu);color:#EEF2FA;font-size:13px;font-weight:600}
.serit .sy{display:inline-flex;align-items:center;gap:3px;font-variant-numeric:tabular-nums}
.serit .sy b{display:inline-grid;place-items:center;min-width:26px;height:24px;padding:0 4px;border-radius:6px;background:#2A3466;font-size:13px}
.serit .sy b.sn{background:var(--v);color:var(--koyu)}
.serit .sy i{font-style:normal;color:var(--acik)}
@keyframes tikA{from{opacity:.35;transform:translateY(-4px)}to{opacity:1;transform:none}}
@keyframes tikB{from{opacity:.35;transform:translateY(-4px)}to{opacity:1;transform:none}}
.sn.tA{animation:tikA .45s var(--ease)}.sn.tB{animation:tikB .45s var(--ease)}

/* Sinema galeri (Yön A): tam ekran fotoğraf; başlık ve küçük resimler görselin içinde. 5 sn'de geçer, dokununca durur. */
.hero{position:relative;height:560px;overflow:hidden;background:var(--koyu);color:#fff}
.h-iz{position:absolute;left:0;right:0;top:52px;bottom:0;display:flex;overflow-x:auto;scroll-snap-type:x mandatory;overscroll-behavior-x:contain}
.hs{position:relative;flex:0 0 100%;overflow:hidden;scroll-snap-align:start;background:var(--koyu)}
.hs>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hs.on>img{animation:kb 7s linear both}
.hs.afis>img{top:50%;bottom:auto;height:auto;aspect-ratio:1/1;transform:translateY(-58%)}
.hs.afis.on>img{animation:none}
.hs::after{content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(180deg,rgba(20,26,54,.35) 0,rgba(20,26,54,0) 12%,rgba(20,26,54,0) 50%,rgba(20,26,54,.92) 92%)}
.hero .u-ust{position:relative;z-index:2}
.hero-y{position:absolute;left:16px;right:16px;bottom:64px;z-index:2}
.hero-y .bas-y{font-size:44px;line-height:.96}
.hero-y .bas-y>span{display:block;overflow:hidden;padding-bottom:4px}
.hero-y .bas-y i{display:block;font-style:normal;animation:satir .9s var(--ease) both}
.hero-y .bas-y>span+span i{animation-delay:.12s}
.hero-y .bas-y em{font-style:normal;color:var(--v)}
@keyframes satir{from{transform:translateY(105%)}to{transform:none}}
.hero-y p{margin:10px 0 0;font-size:16px;color:#D5DBEA;animation:sol .8s var(--ease) .35s both}
/* Galeri göstergesi (küçük resimlerin yerine): fotoğraf ilerledikçe film diskleri dolar, o anki disk döner */
.h-alt{position:absolute;left:16px;right:16px;bottom:20px;z-index:2;display:flex;align-items:center;justify-content:space-between;pointer-events:none}
.d-iz{display:flex;align-items:center;gap:10px}
.d-iz svg{width:16px;height:16px;fill:none;stroke:rgba(238,242,250,.42);stroke-width:1.6;stroke-linecap:round;transition:transform .4s var(--ease)}
.d-iz .ark{opacity:0}
.d-iz .lit{stroke:var(--v)}.d-iz .lit .ic{fill:var(--v)}.d-iz .lit .ark{opacity:1}
.d-iz .on{transform:scale(1.35)}
.d-iz .on .ark{transform-origin:12px 12px;animation:don 2.4s linear infinite}
.h-alt .sira{display:flex;flex-direction:column;align-items:flex-end;font-size:13px;font-weight:600;color:#D5DBEA;font-variant-numeric:tabular-nums;line-height:1.3}
.h-alt .sira small{font-size:12px;font-weight:500;color:var(--acik)}

/* Satın alma */
.al{padding:24px 16px 40px}
.al h1{font-size:32px}
.fiyat{display:flex;align-items:center;flex-wrap:wrap;gap:6px 12px;margin:14px 0 0;font-variant-numeric:tabular-nums}
.fiyat b{font-family:var(--fb);font-weight:var(--bk);font-size:30px;letter-spacing:-.03em;line-height:1;animation:sol .7s var(--ease) .15s both}
.fiyat s{position:relative;font-size:16px;color:var(--soluk);text-decoration:none}
.fiyat s::after{content:"";position:absolute;left:-2px;right:-2px;top:52%;height:1.5px;background:var(--soluk);transform-origin:0 50%;animation:dol .6s var(--ease) .55s both}
.rozet{display:inline-flex;align-items:center;height:26px;padding:0 10px;border-radius:999px;background:var(--lac);color:var(--v);font-size:13px;font-weight:700;animation:pop .5s var(--ease) .85s both}
@keyframes pop{0%{opacity:0;transform:scale(.6)}70%{opacity:1;transform:scale(1.06)}100%{opacity:1;transform:none}}

/* Birleşik çizgili kutu (Yön A): özellikler ve güven aynı kalıpta; kart yığını yok */
.ozler{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));margin-top:22px;border-radius:16px;background:var(--yuzey);box-shadow:inset 0 0 0 1px var(--cizgi);overflow:hidden}
.oz{display:flex;flex-direction:column;gap:3px;padding:16px 14px}
.oz:nth-child(-n+2){border-bottom:1px solid var(--cizgi)}
.oz:nth-child(3),.oz:nth-child(4){border-bottom:1px solid var(--cizgi)}
.ozler.dort .oz:nth-child(3),.ozler.dort .oz:nth-child(4){border-bottom:0}
.oz:nth-child(odd):not(.genis){border-right:1px solid var(--cizgi)}
.oz .gz{display:flex;align-items:center;height:48px;margin-bottom:8px}
.oz b{font-size:15px;line-height:1.25}
.oz .t{display:block;font-size:13px;color:var(--soluk);line-height:1.35}
.oz.genis{grid-column:1/-1;flex-direction:row;align-items:center;gap:16px}
.oz.genis .gz{margin:0}
.fis-a{width:60px;height:30px;overflow:hidden}
.fis-a .uc{fill:#C9D0DE}.fis-a .gv{fill:var(--lac)}.fis-a .kb{fill:none;stroke:var(--lac);stroke-width:2.6;stroke-linecap:round}
.fis{animation:fis 3.2s var(--ease) infinite}
@keyframes fis{0%,10%{transform:translateX(16px)}36%,80%{transform:none}100%{transform:translateX(16px)}}
.port{position:relative;flex:none;width:22px;height:22px;border-radius:5px;box-shadow:inset 0 0 0 1.8px var(--lac)}
.port::after{content:"";position:absolute;inset:5px;border-radius:2px;background:var(--v2);opacity:.15;animation:led 3.2s var(--ease) infinite}
@keyframes led{0%,34%{opacity:.15}42%,78%{opacity:1}90%,100%{opacity:.15}}
.dn{display:flex}
.dn img{width:44px;height:44px;border-radius:50%;margin-left:-18px;box-shadow:0 0 0 2px var(--yuzey)}
.dn img:first-child{position:relative;z-index:2;margin-left:0;animation:don 14s linear infinite}
.dn img:nth-child(2){z-index:1;position:relative}
.karo{position:relative;flex:none;width:48px;height:48px;border-radius:12px;background:var(--lac);overflow:hidden}
.karo img{position:absolute;left:50%;bottom:-4px;height:50px;width:auto;margin-left:-10px}
.karo.salla img{transform-origin:50% 100%;animation:salla 3.4s ease-in-out infinite alternate}
@keyframes salla{from{transform:rotate(-8deg)}to{transform:rotate(8deg)}}
.karo .hale{position:absolute;left:50%;top:18px;width:30px;height:30px;margin-left:-15px;border-radius:50%;background:radial-gradient(circle,rgba(255,244,226,.95) 0,rgba(255,244,226,0) 68%);animation:hale 2.8s ease-in-out infinite alternate}
@keyframes hale{from{opacity:.3;transform:scale(.8)}to{opacity:1;transform:scale(1.15)}}
.cetvel{position:relative;flex:none;width:120px;height:30px;border:1.6px solid var(--lac);border-radius:6px;background:repeating-linear-gradient(90deg,var(--lac) 0 1.4px,transparent 1.4px 9px) 5px 0/108px 8px no-repeat}
.cetvel i{position:absolute;left:5px;right:5px;bottom:5px;height:6px;border-radius:3px;background:var(--v2);transform-origin:0 50%;animation:cetvel 4s var(--ease) infinite}
@keyframes cetvel{0%{transform:scaleX(.08);opacity:0}15%{opacity:1}60%,85%{transform:scaleX(1);opacity:1}100%{transform:scaleX(1);opacity:0}}
.gv-ik{display:grid;place-items:center;width:44px;height:44px;border-radius:12px;background:var(--lac);overflow:hidden}
.gv-ik svg{width:24px;height:24px;fill:none;stroke:var(--v);stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;overflow:visible}
.kamyon svg{animation:kamyon 2.6s ease-in-out infinite}
@keyframes kamyon{0%,100%{transform:translateX(-2px)}50%{transform:translateX(3px)}}
.kamyon .yl{stroke-dasharray:3 4;animation:yolak .9s linear infinite}
@keyframes yolak{to{transform:translateX(-7px)}}
.donus svg{animation:donus 4s var(--ease) infinite}
@keyframes donus{0%,55%{transform:rotate(0)}85%,100%{transform:rotate(-360deg)}}
.kart-ik svg{animation:kart 3s var(--ease) infinite}
@keyframes kart{0%,60%,100%{transform:none}75%{transform:translateY(-2px) rotate(-6deg)}}
.yaz circle{fill:var(--v);stroke:none;animation:yaz 1.2s ease-in-out infinite}
.yaz circle:nth-of-type(2){animation-delay:.2s}.yaz circle:nth-of-type(3){animation-delay:.4s}
@keyframes yaz{0%,100%{opacity:.25}40%{opacity:1}}
.kartlar{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin-top:14px}
.km{display:inline-flex;align-items:center;height:28px;padding:0 10px;border-radius:6px;background:var(--yuzey);box-shadow:inset 0 0 0 1px var(--cizgi);font-size:12px;font-weight:800;letter-spacing:.02em}
.kartlar span:last-child{margin-left:4px;font-size:12px;color:var(--soluk)}

/* Paket: satır kart; beyaz ürün lacivert karoda */
.pk-bas{display:flex;align-items:center;gap:10px;margin:28px 0 12px;font-size:14px;font-weight:700}
.pk-bas::after{content:"";flex:1;height:1px;background:var(--cizgi)}
.pk{display:flex;flex-direction:column;gap:14px}
.pk-k{position:relative;display:flex;align-items:center;gap:12px;width:100%;min-height:88px;padding:12px 14px 12px 12px;border:0;border-radius:16px;background:var(--yuzey);text-align:left;box-shadow:inset 0 0 0 1.5px var(--cizgi);transition:transform .2s var(--ease)}
.pk-k:active{transform:scale(.985)}
.pk-k.on{box-shadow:inset 0 0 0 2px var(--lac)}
.pk-g{position:relative;flex:none;width:60px;height:60px;border-radius:12px;background:var(--lac);overflow:hidden}
.pk-g img{position:absolute;bottom:-2px;left:50%;height:58px;width:auto;margin-left:-12px}
.pk-g.iki img:first-child{margin-left:-21px;transform:rotate(-8deg)}.pk-g.iki img:nth-child(2){margin-left:-3px;transform:rotate(8deg)}
.pk-o{flex:1;min-width:0;line-height:1.25}
.pk-o b{display:block;font-size:17px}
.pk-o span{display:block;margin-top:3px;font-size:13px;color:var(--soluk)}
.pk-s{display:flex;flex-direction:column;align-items:flex-end;text-align:right;line-height:1.2;font-variant-numeric:tabular-nums;white-space:nowrap}
.pk-s b{font-size:18px}
.pk-s s,.pk-s span{margin-top:3px;font-size:13px;color:var(--soluk)}
.nokta{flex:none;width:22px;height:22px;border-radius:50%;box-shadow:inset 0 0 0 1.6px #B8C0D2}
.nokta i{display:block;width:12px;height:12px;margin:5px;border-radius:50%;background:var(--lac);opacity:0;transform:scale(.3);transition:opacity .25s var(--ease),transform .25s var(--ease)}
.on .nokta{box-shadow:inset 0 0 0 1.6px var(--lac)}
.on .nokta i{opacity:1;transform:none}
.kurdele{position:absolute;right:14px;top:-11px;padding:2px 10px;border-radius:999px;background:var(--lac);color:var(--v);font-size:12px;font-weight:700;line-height:1.5;white-space:nowrap}
/* Dün satırı (kullanıcı, 18 Eki): sayı elle girilir, boşsa satır yok */
.dun{display:flex;align-items:center;gap:8px;margin:10px 0 0;font-size:14px;color:var(--soluk)}
.dun b{color:var(--lac);font-variant-numeric:tabular-nums}
.dun svg{width:18px;height:18px;flex:none;fill:none;stroke:var(--v2);stroke-width:1.8;stroke-linecap:round}
/* Dönen satır (kullanıcı, 18 Eki): "Her kutuda 12 film diski" ↔ aynı gün kargo + 16.00 sayacı. İki satır aynı ızgara hücresinde;
   dönerken yükseklik değişmez. Giren alttan, çıkan yukarı. Hareket azaltılmışsa ikisi alt alta. */
.donen{position:relative;display:grid;margin:14px 0 0;font-size:14px;font-weight:600;overflow:hidden}
.dn-s{grid-area:1/1;display:flex;align-items:center;gap:12px;min-height:30px;opacity:0;transform:translateY(80%);transition:opacity .36s var(--ease),transform .36s var(--ease)}
.dn-s.on{opacity:1;transform:none}.dn-s.ust{transform:translateY(-80%)}
.donen .dn img{width:30px;height:30px;margin-left:-12px}
.donen .dn img:first-child{margin-left:0}
.dn-ik{flex:none;width:30px;height:30px;border-radius:50%;background:var(--lac);display:grid;place-items:center}
.dn-ik svg{width:18px;height:18px;fill:none;stroke:var(--v);stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.dn-m{flex:1;min-width:0;font-size:13px;line-height:1.3}
.dn-sy{flex:none;display:inline-flex;align-items:center;height:26px;padding:0 10px;border-radius:999px;background:var(--lac);color:var(--v);font-size:13px;font-weight:700;font-variant-numeric:tabular-nums;letter-spacing:.02em}
.dn-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
@media (prefers-reduced-motion:reduce){.donen{row-gap:10px}.dn-s{grid-area:auto;opacity:1;transform:none;transition:none}}
/* Baskı: tek satır, butonun hemen üstünde; stok elle yazılır, veri yoksa satır gizlenir */
.stok{display:flex;align-items:center;gap:10px;margin:22px 0 0;font-size:14px;font-weight:600}
.ping{position:relative;flex:none;width:10px;height:10px;margin:0 2px;border-radius:50%;background:var(--v2)}
.ping::after{content:"";position:absolute;inset:0;border-radius:50%;background:var(--v2);animation:ping 1.8s var(--ease) 3}
@keyframes ping{from{transform:scale(1);opacity:.7}to{transform:scale(2.8);opacity:0}}
.btn1{display:flex;align-items:center;justify-content:center;gap:12px;width:100%;min-height:62px;margin-top:12px;padding:8px 16px;border:0;border-radius:16px;background:var(--lac);box-shadow:0 3px 0 #0C1027;transition:transform .12s var(--ease)}
.pg .btn1{color:#fff}
.btn1:active{transform:translateY(3px)}
.btn1 .b-ic{display:flex;flex-direction:column;align-items:center;line-height:1.2}
.btn1 .b-ic>span{font-size:16px;font-weight:700}
.btn1 .b-ic small{margin-top:2px;font-size:12px;font-weight:600;color:var(--v)}
.btn1 svg{width:18px;height:18px;flex:none;fill:none;stroke:var(--v);stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;animation:durt 2.4s var(--ease) infinite}
@keyframes durt{0%,58%,100%{transform:none}68%{transform:translateX(5px)}78%{transform:none}86%{transform:translateX(3px)}94%{transform:none}}
.btn2{display:flex;align-items:center;justify-content:center;width:100%;min-height:56px;margin-top:12px;border-radius:16px;background:transparent;color:var(--lac);border:1.5px solid var(--lac);font-size:15px;font-weight:600}
.pg .btn-b{border:0;border-radius:14px;background:var(--v);color:var(--koyu);font-weight:700;box-shadow:0 3px 0 var(--v2)}
.pg .btn-b svg{stroke:var(--koyu)}

/* Kargo döngüsü: çizgi dolar, paket ilerler, adımlar yanar (8 sn) */
.yol{position:relative;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));list-style:none;margin:28px 0 0;padding:0;text-align:center}
.yol::before{content:"";position:absolute;left:16.6%;right:16.6%;top:9px;border-top:1.5px dashed #B8C0D2}
.yol li{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;gap:2px}
.yol b{font-size:14px}.yol li>span:last-child{font-size:13px;color:var(--soluk)}
.yd{position:relative;width:20px;height:20px;margin-bottom:6px;border-radius:50%;background:var(--zemin);box-shadow:inset 0 0 0 2px var(--lac)}
.yd::after{content:"";position:absolute;inset:5px;border-radius:50%;background:var(--lac)}
.y2 .yd::after{animation:yk2 8s var(--ease) infinite}.y3 .yd::after{animation:yk3 8s var(--ease) infinite}
.yol-iz{position:absolute;left:16.6%;right:16.6%;top:9px;height:2px}
.yol-iz i{position:absolute;top:-.25px;width:50%;height:2px;background:var(--lac);transform-origin:0 50%}
.yol-iz i:first-child{left:0;animation:yc1 8s var(--ease) infinite}.yol-iz i:nth-child(2){left:50%;animation:yc2 8s var(--ease) infinite}
.yol-iz em{position:absolute;left:0;top:0;width:100%;height:0;z-index:2;animation:ypk 8s var(--ease) infinite}
.yol-iz em::before{content:"";position:absolute;left:-6px;top:-5px;width:12px;height:12px;border-radius:50%;background:var(--v2);box-shadow:0 0 0 2px var(--zemin),0 0 0 3.5px var(--lac)}
@keyframes yc1{0%,6%{transform:scaleX(0);opacity:1}26%,88%{transform:scaleX(1);opacity:1}97%,100%{transform:scaleX(1);opacity:0}}
@keyframes yc2{0%,38%{transform:scaleX(0);opacity:1}57%,88%{transform:scaleX(1);opacity:1}97%,100%{transform:scaleX(1);opacity:0}}
@keyframes ypk{0%,4%{transform:none;opacity:0}6%{transform:none;opacity:1}26%,38%{transform:translateX(50%);opacity:1}57%{transform:translateX(100%);opacity:1}60%,100%{transform:translateX(100%);opacity:0}}
@keyframes yk2{0%,26%{opacity:0;transform:scale(.3)}33%,88%{opacity:1;transform:none}97%,100%{opacity:0}}
@keyframes yk3{0%,57%{opacity:0;transform:scale(.3)}64%,88%{opacity:1;transform:none}97%,100%{opacity:0}}

/* Bu gece tavanda ne olsun? (Yön A'dan, kullanıcı istedi): yaşam fotoğrafı, yazı görselin içinde; fotoğraflar yavaşça süzülür */
.sahne-serit{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:16px;padding:18px 16px 0}
.sk{position:relative;flex:0 0 272px;height:380px;border-radius:16px;overflow:hidden;scroll-snap-align:start;background:#000}
.sk img{position:absolute;inset:-4%;width:108%;height:108%;object-fit:cover;animation:suz 16s ease-in-out infinite alternate}
.sk:nth-child(2) img{animation-delay:-4s}.sk:nth-child(3) img{animation-delay:-8s}.sk:nth-child(4) img{animation-delay:-12s}
@keyframes suz{from{transform:scale(1) translateX(-2%)}to{transform:scale(1.06) translateX(2%)}}
.sk::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,26,54,0) 55%,rgba(20,26,54,.88) 100%)}
.sk b{position:absolute;left:16px;bottom:36px;z-index:1;font-family:var(--fb);font-weight:var(--bk);font-size:28px;letter-spacing:-.03em;color:#fff}
.sk span{position:absolute;left:16px;bottom:14px;z-index:1;font-size:13px;color:#D5DBEA}

/* 12 disk: seçilen disk tavana düşer; kendiliğinden sırayla gezer, dokununca durur. Yazı görselin içinde. */
.dk-sahne{position:relative;height:330px;margin-top:6px;overflow:hidden}
.dk-yansi{position:absolute;left:50%;top:4px;width:236px;height:236px;margin-left:-118px;animation:nefes 6s ease-in-out infinite alternate}
@keyframes nefes{from{transform:scale(.97)}to{transform:scale(1.03)}}
.dk-yansi img{position:absolute;inset:0;width:100%;height:100%;border-radius:50%;opacity:0;transform:scale(.84) rotate(-24deg);transition:opacity .7s var(--ease),transform 1s var(--ease);-webkit-mask-image:radial-gradient(circle,#000 50%,transparent 71%);mask-image:radial-gradient(circle,#000 50%,transparent 71%)}
.dk-yansi img.on{opacity:.95;transform:none}
.dk-isik{position:absolute;left:50%;top:148px;width:250px;height:96px;margin-left:-125px;background:linear-gradient(0deg,rgba(214,232,255,.32),rgba(214,232,255,0));clip-path:polygon(47% 100%,53% 100%,100% 0,0 0);animation:isik 3.6s ease-in-out infinite alternate}
@keyframes isik{from{opacity:.5}to{opacity:1}}
.dk-urun{position:absolute;left:50%;bottom:-10px;height:104px;width:auto;margin-left:-22px}
.dk-ad{position:absolute;left:16px;bottom:12px;display:flex;flex-direction:column;line-height:1.2}
.dk-ad span{font-size:12px;color:var(--acik);font-variant-numeric:tabular-nums}
.dk-ad b{font-family:var(--fb);font-weight:var(--bk);font-size:20px;letter-spacing:-.02em}
.dk-iz{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:12px 8px;margin-top:18px}
.dk-iz button{aspect-ratio:1;padding:0;border:0;border-radius:50%;background:transparent;box-shadow:0 0 0 1.5px rgba(238,242,250,.16);transition:transform .3s var(--ease)}
.dk-iz button img{display:block;width:100%;height:100%;border-radius:50%}
.dk-iz button.on{box-shadow:0 0 0 2.5px var(--v);transform:scale(1.1)}

/* Herkesin odasına: hikâye kartı; oda çipleri görselin içinde, çubuklar dolar, dokun: ileri/geri */
.hk{position:relative;height:500px;margin-top:20px;border-radius:22px;overflow:hidden;background:var(--koyu);color:#fff;isolation:isolate}
.hk-f{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .6s var(--ease)}
.hk-f.on{opacity:1;animation:kb 6s linear both}
.hk::after{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;background:linear-gradient(180deg,rgba(20,26,54,.7) 0,rgba(20,26,54,0) 24%,rgba(20,26,54,0) 46%,rgba(20,26,54,.94) 86%)}
.hk-cub{position:absolute;left:12px;right:12px;top:12px;z-index:3;display:flex;gap:4px}
.hk-cub span{position:relative;flex:1;height:3px;border-radius:2px;background:rgba(255,255,255,.3);overflow:hidden}
.hk-cub i{position:absolute;inset:0;background:#fff;transform:scaleX(0);transform-origin:0 50%}
.hk-cub .bitti i,.hk-cub .dur i{transform:none}
.hk-cub .on i{animation:dol 5s linear both}
.hk-sec{position:absolute;left:0;right:0;top:24px;z-index:4;display:flex;gap:6px;overflow-x:auto;padding:0 12px}
.hk-sec button{flex:none;min-height:48px;padding:0 14px;border:0;border-radius:999px;background:rgba(20,26,54,.62);box-shadow:inset 0 0 0 1px rgba(238,242,250,.22);color:#fff;font-size:13px;font-weight:700}
.pg .hk-sec button.on{background:var(--v);color:var(--koyu);box-shadow:none}
.hk-git{position:absolute;top:76px;bottom:0;z-index:2;padding:0;border:0;background:transparent}
.hk-git.geri{left:0;width:35%}.hk-git.ileri{right:0;width:65%}
.hk-y{position:absolute;left:16px;right:16px;bottom:18px;z-index:3;pointer-events:none;opacity:0;visibility:hidden}
.hk-y.on{opacity:1;visibility:visible}
.hk-y .bas-y{max-width:300px;font-size:34px;line-height:1}
.hk-y p{margin:8px 0 0;font-size:15px;color:#D5DBEA}
.hk-y.on .bas-y,.hk-y.on p,.hk-y.on .hk-disk{animation:sol .7s var(--ease) both}
.hk-y.on p{animation-delay:.1s}.hk-y.on .hk-disk{animation-delay:.2s}
.hk-disk{display:inline-flex;align-items:center;gap:8px;margin-top:12px;padding:4px 12px 4px 4px;border-radius:999px;background:rgba(20,26,54,.72);box-shadow:inset 0 0 0 1px rgba(238,242,250,.18);font-size:13px;font-weight:600}
.hk-disk img{width:28px;height:28px;border-radius:50%;animation:don 10s linear infinite}

/* Nereye takılır (Yön A koyu karolar): fiş takılır, cihazın ışığı yanar */
.tak{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:20px}
.tk{display:flex;flex-direction:column;align-items:center;gap:4px;padding:16px 6px 14px;border-radius:16px;background:var(--koyu2);text-align:center}
.tk-g{position:relative;display:flex;align-items:center;height:44px;margin-bottom:6px}
.tk-g>svg:first-child{width:36px;height:36px;flex:none;fill:none;stroke:#EEF2FA;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.tk-g .fis-a{width:48px;height:24px;margin-left:-2px}
.tk-g .fis-a .gv{fill:#EEF2FA}.tk-g .fis-a .kb{stroke:#EEF2FA}.tk-g .fis-a .uc{fill:#8D96B5}
.tk-g::after{content:"";position:absolute;left:28px;top:4px;width:7px;height:7px;border-radius:50%;background:var(--v);opacity:.15;animation:led 3.2s var(--ease) infinite}
.tk:nth-child(2) .fis,.tk:nth-child(2) .tk-g::after{animation-delay:.5s}.tk:nth-child(3) .fis,.tk:nth-child(3) .tk-g::after{animation-delay:1s}
.tk b{font-size:14px}.tk span{font-size:12px;color:var(--acik);line-height:1.3}

/* Kurulum: gerçek sıra olduğu için numaralı */
.kur{list-style:none;margin:18px 0 0;padding:0;border-top:1px solid var(--cizgi)}
.kur li{display:grid;grid-template-columns:44px minmax(0,1fr);gap:12px;align-items:start;padding:14px 0;border-bottom:1px solid var(--cizgi)}
.kur em{display:grid;place-items:center;width:40px;height:40px;border-radius:50%;background:var(--lac);color:var(--v);font-style:normal;font-family:var(--fb);font-weight:var(--bk);font-size:18px}
.kur b{display:block;font-size:16px;line-height:1.3;margin-top:2px}
.kur li>span>span{display:block;margin-top:2px;font-size:14px;color:var(--soluk)}
.wa{display:flex;align-items:center;justify-content:center;gap:8px;min-height:52px;margin-top:16px;border-radius:14px;background:var(--yuzey);box-shadow:inset 0 0 0 1.5px var(--lac);font-size:15px;font-weight:700;text-decoration:none}
.wa svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}

.yer{margin:16px 0 0;padding:20px 16px;border:1.5px dashed #B8C0D2;border-radius:18px;font-size:14px;color:var(--soluk);text-align:center}

/* 30 gün: 30 çentik sırayla yanar */
.otuz{display:grid;grid-template-columns:112px minmax(0,1fr);gap:16px;align-items:center;padding:18px;border-radius:22px;background:var(--lac);color:#EEF2FA}
.ot-h{position:relative;width:112px;height:112px;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1}
.ot-h i{position:absolute;left:55px;top:2px;width:2px;height:9px;border-radius:1px;background:var(--v);transform-origin:1px 54px;opacity:.18;animation:gun 6s linear infinite}
@keyframes gun{0%{opacity:.18}4%,66%{opacity:1}82%,100%{opacity:.18}}
.ot-h b{font-family:var(--fb);font-weight:var(--bk);font-size:38px;letter-spacing:-.04em}
.ot-h small{margin-top:2px;font-size:12px;font-weight:700;color:var(--v)}
.otuz>span:last-child b{display:block;font-size:17px;line-height:1.25}
.otuz>span:last-child span{display:block;margin-top:4px;font-size:14px;color:var(--acik)}

.sss{border-bottom:1px solid var(--cizgi)}
.sss summary{list-style:none;display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:60px;font-weight:700;font-size:15px;cursor:pointer}
.sss summary::-webkit-details-marker{display:none}
.sss .arti{flex:none;display:grid;place-items:center;width:32px;height:32px;border-radius:50%;background:var(--lac);color:var(--v);font-size:18px;font-weight:400;transition:transform .25s var(--ease)}
.sss[open] .arti{transform:rotate(45deg)}
.sss p{margin:0 0 16px;font-size:14px;color:var(--soluk)}

.kart{flex:0 0 168px;scroll-snap-align:start;display:flex;flex-direction:column;border-radius:16px;overflow:hidden;background:var(--yuzey);box-shadow:inset 0 0 0 1px var(--cizgi);text-decoration:none}
.kart>span:first-child{position:relative;aspect-ratio:1/1;overflow:hidden;background:#E6EAF2}
.kart img{display:block;width:100%;height:100%;object-fit:cover}
.kart i{position:absolute;left:8px;top:8px;padding:2px 8px;border-radius:999px;background:var(--lac);color:var(--v);font-style:normal;font-size:12px;font-weight:700}
.kart>span:last-child{display:flex;flex-direction:column;gap:4px;padding:10px 12px 12px}
.kart b{font-size:14px;font-weight:600;line-height:1.25;min-height:35px}

.alt-bilgi{margin-top:44px;padding:36px 0 112px;border-radius:28px 28px 0 0;background:var(--lac);color:var(--acik)}
.alt-bilgi a{display:flex;align-items:center;min-height:48px;color:#fff;text-decoration:none}
.yapis{position:sticky;bottom:0;z-index:5;display:flex;align-items:center;gap:10px;height:76px;margin-top:-76px;padding:0 12px;border-radius:20px 20px 0 0;background:var(--koyu)}
.yapis .karo{width:46px;height:46px;background:#2A3466}
.yapis .karo img{height:48px;margin-left:-10px}

/* Seçenek panosu etiketi */
.secenek{padding:16px 16px 14px;background:#fff;border-bottom:1px solid var(--cizgi)}
.secenek b{display:block;font-family:var(--fb);font-weight:var(--bk);font-size:22px;letter-spacing:var(--bls);line-height:1.1}
.secenek span{display:block;margin-top:4px;font-size:13px;color:var(--soluk)}
.secenek .renk{display:flex;gap:6px;margin-top:10px}
.secenek .renk i{width:28px;height:28px;border-radius:8px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}

@media (prefers-reduced-motion:reduce){.pg *,.pg *::before,.pg *::after{animation:none!important;transition:none!important}.yol-iz em{display:none}}
"""


def disk_yigin():
    return '<span class="dn" aria-hidden="true"><img src="%s" alt=""><img src="%s" alt=""><img src="%s" alt=""></span>' % (D['Sarmal galaksi'], D['Kuzey ışığı'], D['Denizanası'])


# Dün satış (kullanıcı, 18 Eki): gerçek sayı elle girilir (bölüm ayarı ya da Shopify Flow metafield'ı); boşsa satır gizlenir.
DUN = '[X]'
DUN_SATIR = ('    <p class="dun"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="3.5"></circle><path d="M5 20a7 7 0 0 1 14 0"></path></svg><span>Dün <b>%s</b> kişi satın aldı</span></p>\n' % DUN) if DUN else ''
SAAT = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"></circle><path d="M12 7.5V12l3 2"></path></svg>'
WA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"></path></svg>'
# Güven: kartla ödeme kapıda ödemenin önünde (iade kapıda %28,6, ön ödemede %0,8). ₺80 kapıda ücreti formda ve SSS'de.
GUVEN = ('<div class="ozler dort">'
         '<div class="oz"><span class="gz"><span class="gv-ik kamyon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7h11v8H3z"></path><path d="M14 10h4l3 3v2h-7"></path><circle cx="7" cy="17" r="1.8"></circle><circle cx="17" cy="17" r="1.8"></circle><path class="yl" d="M1 21h22"></path></svg></span></span>'
         '<b>Ücretsiz kargo</b><span class="t">1 iş gününde kargoda, adım adım takip.</span></div>'
         '<div class="oz"><span class="gz"><span class="gv-ik donus"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12a8 8 0 1 0 2.3-5.6"></path><path d="M4 4v4h4"></path></svg></span></span>'
         '<b>30 gün iade</b><span class="t">Beğenmezsen geri gönder, iade kargosu ücretsiz.</span></div>'
         '<div class="oz"><span class="gz"><span class="gv-ik kart-ik"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="18" height="12" rx="2"></rect><path d="M3 10h18M7 15h4"></path></svg></span></span>'
         '<b>Kartla güvenli öde</b><span class="t">%5 indirim; kart bilgin bize gelmez.</span></div>'
         '<div class="oz"><span class="gz"><span class="gv-ik yaz"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"></path><circle cx="8.5" cy="12" r="1.2"></circle><circle cx="12" cy="12" r="1.2"></circle><circle cx="15.5" cy="12" r="1.2"></circle></svg></span></span>'
         '<b>WhatsApp destek</b><span class="t">Ortalama 2 saatte yanıt.</span></div></div>'
         '<div class="kartlar"><span class="km">VISA</span><span class="km">Mastercard</span><span class="km">Troy</span><span>[Ödeme altyapısı]</span></div>')

TAK = ('<div class="tak">'
       '<div class="tk"><span class="tk-g">' + IK['laptop'] + FIS + '</span><b>Laptop</b><span>USB girişine</span></div>'
       '<div class="tk"><span class="tk-g">' + IK['powerbank'] + FIS + '</span><b>Powerbank</b><span>Prizsiz yerde</span></div>'
       '<div class="tk"><span class="tk-g">' + IK['priz'] + FIS + '</span><b>Şarj başlığı</b><span>USB-A girişli</span></div></div>'
       '<p class="alt-not">USB adaptör kutuda yok. Evdeki USB-A girişli bir şarj başlığı yeter.</p>')

OTUZ = ''.join('<i style="transform: rotate(%ddeg); animation-delay: %.2fs"></i>' % (k * 12, k * .1) for k in range(30))

SERIT = '<div class="serit" role="timer" aria-label="{{cdAria}}"><span>Bugüne özel fiyat</span><span class="sy" aria-hidden="true"><b>{{hh}}</b><i>:</i><b>{{mm}}</b><i>:</i><b class="{{snCls}}">{{ss}}</b></span></div>'

HERO = ("""
  <!-- Sinema galeri (Yön A): parmakla kaydırılır, 5 sn'de kendiliğinden geçer (kaydırınca durur). Başlık yalnız ilk fotoğrafta.
       Küçük resimler yok (kullanıcı: "görünmesin, kaydırılır olsun"); altta fotoğraf ilerledikçe dolan film diskleri. -->
  <section class="hero" aria-label="Galaxy USB fotoğrafları">
    <div class="h-iz noscroll" onScroll="{{gKay}}"><sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><div class="{{f.cls}}"><img src="{{f.src}}" alt="{{f.n}}" style="object-position: {{f.pos}}"><sc-if value="{{f.ilk}}" hint-placeholder-val="{{true}}"><div class="hero-y"><h2 class="bas-y"><span><i>Tavanı</i></span><span><i>sahneye <em>çevir.</em></i></span></h2><p>Bir USB girişi, koca bir gökyüzü.</p></div></sc-if></div></sc-for></div>
    """ + Y.ust('rgba(238,242,250,.6)') + """
    <div class="h-alt"><span class="d-iz" aria-hidden="true"><sc-for list="{{gal}}" as="f" hint-placeholder-count="4"><svg class="{{f.dcls}}" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><circle class="ic" cx="12" cy="12" r="2.6"></circle><path class="ark" d="M12 3a9 9 0 0 1 9 9"></path></svg></sc-for></span><span class="sira"><small>Temsilî görseller</small></span><span style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap" aria-live="polite">Fotoğraf {{gNo}} / {{gCount}}</span></div>
  </section>
""")

AL = ("""
  <section class="al" id="siparis">
    <h1 class="bas-y">Galaxy USB Projektör</h1>
    <p class="alt-b">2'si 1 arada: galaksi projektörü ve gece lambası.</p>
    <!-- Üstü çizili fiyat için son 10 günün fiyat kaydı gerekir (mevzuat kural 1b); teyit bekliyor -->
    <p class="fiyat" aria-label="₺1.599,00, önceki fiyat ₺1.999,00, %20 indirim"><b aria-hidden="true">₺1.599,00</b><s aria-hidden="true">₺1.999,00</s><span class="rozet" aria-hidden="true">%20 indirim</span></p>
""" + DUN_SATIR + """

    <div class="ozler">
      <div class="oz"><span class="gz" aria-hidden="true"><span class="port"></span>""" + FIS + """</span><b>USB tak, çalıştır</b><span class="t">Laptop, powerbank ya da şarj başlığı.</span></div>
      <div class="oz"><span class="gz">""" + disk_yigin() + """</span><b>12 film diski</b><span class="t">Diski değiştir, tavan değişsin.</span></div>
      <div class="oz"><span class="gz" aria-hidden="true"><span class="karo salla"><img src=\"""" + KES + """\" alt=""></span></span><b>Esnek boyun</b><span class="t">Tavana, duvara, köşeye çevir.</span></div>
      <div class="oz"><span class="gz" aria-hidden="true"><span class="karo"><span class="hale"></span><img src=\"""" + KES + """\" alt=""></span></span><b>Gece lambası da</b><span class="t">Gövdesi yumuşak ışıkla yanar.</span></div>
      <div class="oz genis"><span class="gz" aria-hidden="true"><span class="cetvel"><i></i></span></span><span><b>Az yer kaplar</b><span class="t">Başlık 4 cm, toplam boy 23,5 cm.</span></span></div>
    </div>

    <div class="pk-bas">Çok al, az öde</div>
    <div class="pk"><sc-for list="{{paket}}" as="b" hint-placeholder-count="2">
      <button class="{{b.cls}}" onClick="{{b.pick}}" aria-pressed="{{b.on}}"><sc-if value="{{b.rib}}" hint-placeholder-val="{{false}}"><span class="kurdele">En avantajlı</span></sc-if><span class="{{b.gCls}}"><img src=\"""" + KES + """\" alt=""><sc-if value="{{b.two}}" hint-placeholder-val="{{false}}"><img src=\"""" + KES + """\" alt=""></sc-if></span><span class="pk-o"><b>{{b.t}}</b><span>{{b.sub}}</span></span><span class="pk-s"><b>{{b.p}}</b><sc-if value="{{b.hasOld}}" hint-placeholder-val="{{true}}"><s>{{b.old}}</s></sc-if><span>{{b.unit}}</span></span><span class="nokta"><i></i></span></button>
    </sc-for></div>
    <!-- Dönen satır (kullanıcı, 18 Eki: LunaDream'deki baskı USB'de de): önce disk, sonra aynı gün kargo + 16.00 sayacı (4 sn / 6 sn).
         16.00'dan sonra ve hafta sonu sayaç yok: "Bugün verilen siparişler yarın / Pazartesi kargoda". -->
    <p class="donen"><span class="dn-sr">Her kutuda 12 film diski. {{kgMetin}}.</span><span class="{{dnA}}" aria-hidden="true">""" + disk_yigin() + """<span>Her kutuda 12 film diski</span></span><span class="{{dnB}}" aria-hidden="true"><span class="dn-ik">""" + SAAT + """</span><span class="dn-m">{{kgMetin}}</span><sc-if value="{{kgBugun}}" hint-placeholder-val="{{true}}"><b class="dn-sy">{{kgSayac}}</b></sc-if></span></p>
    <!-- Baskı: tek satır, butonun üstünde. Stok ELLE girilir (kullanıcı, 18 Eki: "stoklar elle girilecek"): Shopify'da bölüm ayarı sayı + aç/kapa; Shopify stoğuna bağlı değil, boşsa satır gizlenir. "Dün [X]" fiyatın altında. -->
    <p class="stok"><span class="ping" aria-hidden="true"></span><span>Stokta son <b>[N]</b> adet</span></p>
    <button class="btn1" type="button"><span class="b-ic"><span>{{onLabel}}</span><small>Kartla %5 indirim dahil</small></span>""" + OK + """</button>
    <button class="btn2" type="button">Kapıda Ödeme ile Sipariş Ver</button>
    <ol class="yol" aria-label="Siparişten teslime"><span class="yol-iz" aria-hidden="true"><i></i><i></i><em></em></span><li class="y1"><span class="yd"></span><b>Bugün</b><span>Sipariş verildi</span></li><li class="y2"><span class="yd"></span><b>{{kargo}}</b><span>Kargoda</span></li><li class="y3"><span class="yd"></span><b>{{teslim}}</b><span>Kapında</span></li></ol>
  </section>
""")

# Sahneler: kutudaki disklerle örtüşenler (Ay, Satürn ≈ halkalı gezegen, Denizanası, Kuzey ışığı). Kelebek ve kara delik kutuda yok, alınmadı.
SAHNE = [('Ay', 'ay', '50% 40%'), ('Satürn', 'saturn', '55% 40%'), ('Denizanası', 'denizanasi', '50% 35%'), ('Kuzey ışığı', 'cift', '50% 40%')]
SAHNELER = ('\n  <section class="koyu bolum" style="padding-bottom: 36px"><div class="px"><h2 class="bas-y h2">Bu gece tavanda<br>ne olsun<span class="n">?</span></h2></div>'
            '<div class="sahne-serit noscroll">' + ''.join('<div class="sk"><img src="%s%s" alt="%s yansıması" style="object-position: %s"><b>%s</b><span>Disk değiştir, tavan değişsin</span></div>' % (B, I[k], n, pos, n) for n, k, pos in SAHNE) +
            '<span aria-hidden="true" style="flex: 0 0 6px"></span></div>'
            '<p class="alt-not px">Görseller temsilîdir; desen kutudaki 12 diskten birine göre değişir, büyüklük odaya ve mesafeye göre.</p></section>\n')

DISKLER = ("""
  <!-- 12 disk: görseller kullanıcının paylaştığı mağaza afişinden kırpılıp büyütüldü (desen aynı). Seçilen disk tavana düşer. -->
  <section class="koyu bolum" id="diskler">
    <div class="px"><h2 class="bas-y h2">Kutuda 12<br>film diski<span class="n">.</span></h2><p class="alt-b">Diski tak, tavan değişsin. Birine dokun, tavanda gör.</p></div>
    <div class="dk-sahne" aria-hidden="true">
      <div class="dk-yansi"><sc-for list="{{disk}}" as="d" hint-placeholder-count="2"><img class="{{d.cls}}" src="{{d.src}}" alt=""></sc-for></div>
      <span class="dk-isik"></span>
      <img class="dk-urun" src=\"""" + KES + """\" alt="">
      <span class="dk-ad"><span>Disk {{dNo}} / 12</span><b>{{dAd}}</b></span>
    </div>
    <div class="px"><div class="dk-iz"><sc-for list="{{disk}}" as="d" hint-placeholder-count="12"><button class="{{d.bcls}}" onClick="{{d.pick}}" aria-label="{{d.n}}" aria-pressed="{{d.on}}"><img src="{{d.src}}" alt=""></button></sc-for></div>
    <p class="alt-not">Disk görselleri mağaza afişinden. Tavanda daha yumuşak görünür; netlik odanın karanlığına ve mesafeye göre değişir.</p></div>
  </section>
""")

GERISI = ("""
  <section class="bolum px">
    <h2 class="bas-y h2">İçin rahat<br>olsun<span class="n">.</span></h2>
    """ + GUVEN + """
  </section>
""" + DISKLER + """
  <!-- Herkesin odasına: hikâye kartı. Oda çipleri görselin içinde. Fotoğraflar temsilî; her karede o odaya önerilen disk. -->
  <section class="bolum px" id="odalar">
    <h2 class="bas-y h2">Herkesin<br>odasına<span class="n">.</span></h2>
    <p class="alt-b">Kimin odası olursa olsun: ışığı kapat, diski seç.</p>
    <div class="hk">
      <sc-for list="{{kim}}" as="k" hint-placeholder-count="2"><img class="{{k.fcls}}" src="{{k.src}}" alt="{{k.alt}}" style="object-position: {{k.pos}}"></sc-for>
      <div class="hk-cub" aria-hidden="true"><sc-for list="{{kim}}" as="k" hint-placeholder-count="4"><span class="{{k.ccls}}"><i></i></span></sc-for></div>
      <div class="hk-sec noscroll"><sc-for list="{{kim}}" as="k" hint-placeholder-count="4"><button class="{{k.scls}}" onClick="{{k.pick}}" aria-pressed="{{k.on}}" aria-label="{{k.n}}">{{k.kisa}}</button></sc-for></div>
      <button class="hk-git geri" type="button" onClick="{{kPrev}}" aria-label="Önceki oda"></button>
      <button class="hk-git ileri" type="button" onClick="{{kNext}}" aria-label="Sonraki oda"></button>
      <sc-for list="{{kim}}" as="k" hint-placeholder-count="2"><div class="{{k.ycls}}"><p class="bas-y">{{k.bas}}</p><p>{{k.t}}</p><span class="hk-disk"><img src="{{k.dsrc}}" alt="">Önerilen disk: {{k.disk}}</span></div></sc-for>
    </div>
    <p class="alt-not">Görseller temsilîdir; tavandaki desen seçtiğin diske göre değişir.</p>
  </section>

  <section class="koyu bolum px">
    <h2 class="bas-y h2">Nereye<br>takılır<span class="n">?</span></h2>
    """ + TAK + """
  </section>

  <section class="bolum px" id="kurulum">
    <h2 class="bas-y h2">Üç adımda<br>tavanda<span class="n">.</span></h2>
    <ol class="kur">
      <li><em>1</em><span><b>USB'ye tak</b><span>USB ucu gövdeye bağlı, ayrı kablo gerekmez.</span></span></li>
      <li><em>2</em><span><b>Diski yerleştir</b><span>Diski başlığa tak, başlığı tavana çevir. [Adımlar teyit edilecek]</span></span></li>
      <li><em>3</em><span><b>Halkayı yavaşça çevir</b><span>Ucundaki halkayı yavaşça çevir. Oda ne kadar karanlıksa görüntü o kadar belirgin.</span></span></li>
    </ol>
    <a class="wa" href="#">""" + WA + """Takılırsan WhatsApp'tan yaz</a>
  </section>

  <!-- Yorumlar: yalnız bu ürünün Loox yorumları, hepsi (m.28/B). Başka ürünün yorumu ya da afişteki kart yok. -->
  <section class="px" id="yorumlar" style="padding-bottom: 44px">
    <h2 class="bas-y h2">Alanlar ne<br>diyor<span class="n">?</span></h2>
    <p class="yer">[Loox: bu ürünün tüm doğrulanmış yorumları; puan ve sayı otomatik]</p>
  </section>

  <section class="px">
    <div class="otuz"><span class="ot-h" aria-hidden="true">""" + OTUZ + """<b>30</b><small>gün</small></span><span><b>Beğenmezsen iade et</b><span>Yasal 14 günü 30 güne uzattık. İade kargosu ücretsiz.</span></span></div>
  </section>

  <section class="bolum px">
    <h2 class="bas-y h2">Merak<br>edilenler<span class="n">.</span></h2>
    <div style="margin-top: 14px; border-top: 1px solid var(--cizgi)">
      <sc-for list="{{faq}}" as="f" hint-placeholder-count="6"><details class="sss"><summary>{{f.q}}<span class="arti" aria-hidden="true">+</span></summary><p>{{f.a}}</p></details></sc-for>
    </div>
  </section>

  <section>
    <div class="px" style="display: flex; align-items: flex-end; justify-content: space-between"><h2 class="bas-y" style="font-size: 26px">Odanın geri<br>kalanı için<span class="n">.</span></h2><span style="font-size: 13px; color: var(--soluk)">{{shopCount}} ürün</span></div>
    <div class="noscroll" style="display: flex; gap: 10px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-left: 16px; padding: 16px 16px 4px">
      <sc-for list="{{shop}}" as="u" hint-placeholder-count="4"><a class="kart" href="#"><span><img src="{{u.src}}" alt="{{u.n}}"><sc-if value="{{u.pct}}" hint-placeholder-val="{{true}}"><i>{{u.pct}}</i></sc-if></span><span><b>{{u.n}}</b><span style="display: flex; align-items: baseline; gap: 6px; font-variant-numeric: tabular-nums"><b style="min-height: 0">{{u.price}}</b><s style="font-size: 12px; color: var(--soluk)">{{u.old}}</s></span></span></a></sc-for>
    </div>
  </section>

  <footer class="alt-bilgi">
    <div class="px">
      <h2 class="bas-y" style="font-size: 34px; color: #fff">Bu gece tavanda<br>galaksi olsun<span class="n" style="color: var(--v)">.</span></h2>
      <button class="btn1 btn-b" type="button" style="margin-top: 18px"><span class="b-ic"><span>{{onLabel}}</span><small style="color: var(--koyu)">Kartla %5 indirim dahil</small></span>""" + OK + """</button>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0 16px; margin-top: 24px; font-size: 14px"><a href="#">Mesafeli Satış Sözleşmesi</a><a href="#">KVKK</a><a href="#">İade Politikası</a><a href="#">İletişim</a></div>
      <p style="margin: 14px 0 0; font-size: 13px; line-height: 1.5">[Ticaret unvanı] · MERSİS [no]<br>[Adres] · [e-posta] · [telefon] · KEP [adres]</p>
      <div aria-label="Ayluna" style="margin-top: 24px; display: flex; align-items: center; gap: 12px; color: #fff">""" + E.isaret(48) + """<span aria-hidden="true" style="font-family: 'Young Serif', Georgia, serif; font-size: 56px; line-height: .8; letter-spacing: -.045em">Ayluna</span></div>
      <p style="margin: 14px 0 0; padding-top: 14px; border-top: 1px solid rgba(238,242,250,.12); font-size: 12px">Fiyatlara KDV dahildir. © 2026 Ayluna</p>
    </div>
  </footer>

  <!-- Yapışkan çubuk: fiyat ve buton; sayaç yalnız üst şeritte (tek sayaç) -->
  <div class="yapis">
    <span class="karo"><img src=\"""" + KES + """\" alt=""></span>
    <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; line-height: 1.25; color: #fff; font-variant-numeric: tabular-nums"><b style="font-size: 17px">{{onPrice}}</b><span style="font-size: 13px; color: var(--acik)">{{adetName}} · kartla %5 dahil</span></span>
    <button class="btn1 btn-b" type="button" onClick="{{alaGit}}" style="flex: 0 0 140px; width: 140px; min-height: 52px; margin: 0">Satın al</button>
  </div>
""")


def secenek_etiket(no, t):
    return ('<div class="secenek"><b>Seçenek %d · %s</b><span>%s</span><span class="renk" aria-hidden="true"><i style="background: #1A2142"></i><i style="background: %s"></i><i style="background: %s"></i><i style="background: %s"></i></span></div>'
            % (no, t['ad'], t['alt'], t['v'], t['v2'], t['zemin']))


def sayfa(tema, kesit=None):
    # kesit: (no) → renk seçenek panosu: etiket + şerit + galeri + satın alma + diskler
    t = TEMA[tema]
    if kesit:
        govde = '<div class="pg">' + secenek_etiket(kesit, t) + SERIT + HERO + AL + DISKLER + '</div>\n'
    else:
        govde = '<div class="pg">\n  ' + SERIT + HERO + AL + SAHNELER + GERISI + '</div>\n'
    return head('Galaxy USB Projektör' + (' · ' + t['ad'] if kesit else ''), tema_css(t) + CSS, t['font']) + govde


JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { g: 0, gOto: true, adet: 2, disk: 3, dOto: true, kim: 0, kBas: 0, kOto: true, t: 0, dn: 0, dnT: 0, now: Date.now() }; }
  componentDidMount() {
    var self = this;
    // Hareket azaltılmışsa kendiliğinden geçişler kapalı
    var azH = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (azH) this.setState({ gOto: false, dOto: false, kOto: false });
    // Tek saat: sayaçlar, galeri (5 sn), disk (3 sn), oda kartı (5 sn), dönen satır (disk 4 sn, kargo 6 sn)
    this.iv = setInterval(function () {
      var S = self.state, t = S.t + 1, o = { now: Date.now(), t: t };
      if (S.gOto && t % 5 === 0) self.galGit((S.g + 1) % """ + str(len(GAL)) + """);
      if (S.dOto && t % 3 === 0) o.disk = (S.disk + 1) % 12;
      if (S.kOto && t - S.kBas >= 5) { o.kim = (S.kim + 1) % """ + str(len(KIM)) + """; o.kBas = t; }
      if (!azH && t - S.dnT >= (S.dn ? 6 : 4)) { o.dn = 1 - S.dn; o.dnT = t; }
      self.setState(o);
    }, 1000);
  }
  // Galeri: kaydırma kabını bir sonraki fotoğrafa götür (kabı yoksa durumu değiştir)
  galGit(i) { var el = document.querySelector('.h-iz'); if (el && el.scrollTo && el.clientWidth) { this.otoKay = Date.now(); el.scrollTo({ left: i * el.clientWidth, behavior: 'smooth' }); } else this.setState({ g: i }); }
  // Çizim sonrası kap başka fotoğrafta kaldıysa (DOM yeniden kurulduysa) durumdaki fotoğrafa geri al
  componentDidUpdate() { var el = document.querySelector('.h-iz'); if (el && el.clientWidth && Math.abs(el.scrollLeft - this.state.g * el.clientWidth) > el.clientWidth / 2) { this.otoKay = Date.now(); el.scrollLeft = this.state.g * el.clientWidth; } }
  componentWillUnmount() { clearInterval(this.iv); }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    """ + TL_JS + """
    var I = """ + str(I) + """;
    var GAL = """ + str([list(x) for x in GAL]) + """;
    var gal = GAL.map(function (g, i) { var on = i === S.g, afis = g[0] === 'afis'; return { src: B + I[g[0]], n: g[1], pos: g[2], ilk: i === 0, cls: 'hs' + (afis ? ' afis' : '') + (on ? ' on' : ''), dcls: i < S.g ? 'lit' : (on ? 'lit on' : '') }; });
    // Kaydırma: hangi fotoğraf ortadaysa o; elle kaydırılınca kendiliğinden geçiş durur
    function gKay(e) { var el = e && (e.currentTarget || e.target); if (!el || !el.clientWidth) return; var i = Math.round(el.scrollLeft / el.clientWidth), o = {};
      if (i !== self.state.g) o.g = i; if (self.state.gOto && Date.now() - (self.otoKay || 0) > 900) o.gOto = false; if (o.g !== undefined || o.gOto === false) self.setState(o); }
    var DISK = """ + str([list(x) for x in DISK]) + """;
    var disk = DISK.map(function (d, i) { var on = i === S.disk; return { n: d[0], src: B + d[1], on: on ? 'true' : 'false', cls: on ? 'on' : '', bcls: on ? 'on' : '', pick: function () { self.setState({ disk: i, dOto: false }); } }; });
    var DS = {}; DISK.forEach(function (d) { DS[d[0]] = B + d[1]; });
    var KIM = """ + str([list(x) for x in KIM]) + """;
    var KISA = ['Çocuk', 'Genç', 'İkimiz', 'Kendime'];
    var kim = KIM.map(function (k, i) { var on = i === S.kim; return { n: k[0], kisa: KISA[i], src: B + I[k[1]], bas: k[2], t: k[3], disk: k[4], dsrc: DS[k[4]], pos: k[5], alt: on ? k[0] + ': ' + k[3] : '', on: on ? 'true' : 'false',
      fcls: on ? 'hk-f on' : 'hk-f', ycls: on ? 'hk-y on' : 'hk-y', scls: on ? 'on' : '', ccls: i < S.kim ? 'bitti' : (on ? (S.kOto ? 'on' : 'dur') : ''),
      pick: function () { self.setState({ kim: i, kBas: S.t, kOto: false }); } }; });
    // Paket: canlı sitedeki Kaching fiyatları. 2 Adet'te üstü çizili "2 × eski fiyat" yok (mevzuat §7 kural 2).
    var P1 = 1599, C1 = 1999, P2 = 2399.99;
    var paket = [
      { n: 1, t: '1 Adet', p: TL(P1, true), old: TL(C1, true), unit: '', sub: '%' + Math.round((1 - P1 / C1) * 100) + ' indirim', rib: false },
      { n: 2, t: '2 Adet', p: TL(P2, true), old: '', unit: 'tanesi ' + TL(Math.floor(P2 / 2 * 100) / 100, true), sub: '2 ayrı almaya göre ' + TL(2 * P1 - P2, true) + ' daha az', rib: true }
    ].map(function (b) { var on = S.adet === b.n; return { t: b.t, p: b.p, old: b.old, hasOld: !!b.old, unit: b.unit, sub: b.sub, rib: b.rib, two: b.n === 2, gCls: b.n === 2 ? 'pk-g iki' : 'pk-g',
      on: on ? 'true' : 'false', cls: on ? 'pk-k on' : 'pk-k', pick: function () { self.setState({ adet: b.n }); } }; });
    var total = S.adet === 2 ? P2 : P1, online = Math.round(total * 0.95 * 100) / 100, onPrice = TL(online, true);
    var AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
    """ + KARGO_JS + """
    var KG = KARGO(S.now || Date.now()), kd = KG.gun;
    var t1 = new Date(kd); t1.setDate(t1.getDate() + 3); var t2 = new Date(kd); t2.setDate(t2.getDate() + 7);
    var teslim = t1.getMonth() === t2.getMonth() ? t1.getDate() + '–' + t2.getDate() + ' ' + AY[t2.getMonth()] : t1.getDate() + ' ' + AY[t1.getMonth()] + '–' + t2.getDate() + ' ' + AY[t2.getMonth()];
    function IKI(n) { return n < 10 ? '0' + n : String(n); }
    var ist = new Date(new Date(S.now || Date.now()).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kalan = Math.max(0, new Date(ist.getFullYear(), ist.getMonth(), ist.getDate(), 23, 59, 59, 999).getTime() - ist.getTime());
    var hh = Math.floor(kalan / 3600000), mi = Math.floor(kalan / 60000) % 60, ss = Math.floor(kalan / 1000) % 60;
    function alaGit() { var h = document.getElementById('siparis'); if (h && h.scrollIntoView) h.scrollIntoView({ behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' }); }
    var faq = [
      { q: 'Kutudan ne çıkıyor?', a: '1 Galaxy USB projektör ve 12 film diski. USB adaptör kutuda yok; laptop, powerbank ya da USB-A girişli bir şarj başlığı yeter.' },
      { q: 'Gece lambası olarak da kullanılır mı?', a: 'Evet, 2’si 1 arada: gövdesi yumuşak ışıkla yanar. [Işık modları teyit edilecek.]' },
      { q: 'En net görüntü için ne yapmalıyım?', a: 'Odayı karart, başlığı tavana çevir ve ucundaki halkayı yavaşça çevir. Oda ne kadar karanlıksa görüntü o kadar belirgin olur.' },
      { q: 'Disk nasıl değişir?', a: '[Adımlar teyit edilecek.] Zorlanırsan WhatsApp’tan yaz.' },
      { q: 'Kargo ne zaman gelir?', a: 'İş günü 16.00’ya kadar verilen sipariş aynı gün, sonrakiler ertesi iş günü kargoya verilir; Türkiye geneline 3–7 günde ulaşır. Takip bağlantısı sana gönderilir.' },
      { q: 'Kartla mı, kapıda mı ödeyeyim?', a: 'Tüm kredi ve banka kartları geçer; kartla öderken %5 indirim alırsın, kart bilgin bize gelmez. Kapıda ödemede ₺80 kapıda ödeme ücreti eklenir; ürün geldiğinde nakit ya da kartla ödersin.' },
      { q: 'Beğenmezsem iade edebilir miyim?', a: '30 gün içinde iade edebilirsin. Sana iade kodunu göndeririz, kargosu ücretsizdir. İlk 14 gün yasal cayma hakkındır.' },
      { q: 'Kırık ya da eksik gelirse?', a: 'Teslim aldığın gün WhatsApp’tan fotoğrafını gönder. [Değişim süreci teyit edilecek.]' }
    ];
    var PR = [
      { n: 'LunaDream Gece Lambası', p: 1699.99, c: 1999, id: 'e02351b3be4a1c555c5d760d0bbda723' },
      { n: 'Ayluna Galaksi Night Projektör', p: 2199, c: 2999, id: '3df93f38bf4441cdf4dc64b625a1e22d' },
      { n: 'Galaksi Ambiyans Işığı', p: 1499, c: 2898, id: '9e6102bb76acbfeb101fca8e2fc1024e' },
      { n: 'Ayluna AyFeneri', p: 1649.99, c: 2499, id: 'd326933d74a22adce90d7f6ac3eabf43' },
      { n: 'Yıldız Işığı Nemlendirici', p: 849.99, c: 1099, id: 'c91c0730a3e7924eb99ad263ae4ea6df' },
      { n: 'Ayluna Kum Saati Lamba', p: 799, c: 999, id: '0307a2c24e8297579b82099467f001d9' },
      { n: 'Sunset Lamba', p: 699, c: 999, id: '46cfbd570f385373a0a0721698f87162' }
    ];
    var shop = PR.map(function (x) { var d = x.c > x.p; return { n: x.n, src: B + x.id, price: TL(x.p, true), old: d ? TL(x.c, true) : '', pct: d ? '%' + Math.round((1 - x.p / x.c) * 100) : '' }; });
    return {
      gal: gal, gNo: S.g + 1, gCount: GAL.length, gKay: gKay,
      disk: disk, dNo: S.disk + 1, dAd: DISK[S.disk][0],
      kim: kim,
      kPrev: function () { self.setState({ kim: (S.kim + KIM.length - 1) % KIM.length, kBas: S.t }); },
      kNext: function () { self.setState({ kim: (S.kim + 1) % KIM.length, kBas: S.t }); },
      paket: paket, adetName: S.adet === 2 ? '2 Adet' : '1 Adet',
      onLabel: 'Güvenli Ödeme ile Al · ' + onPrice, onPrice: onPrice,
      kargo: KG.bugun ? 'Bugün' : kd.getDate() + ' ' + AY[kd.getMonth()], teslim: teslim,
      kgMetin: KG.metin, kgBugun: KG.bugun, kgSayac: KG.sayac,
      dnA: 'dn-s' + (S.dn === 0 ? ' on' : S.t - S.dnT < 1 ? ' ust' : ''), dnB: 'dn-s' + (S.dn === 1 ? ' on' : S.t - S.dnT < 1 ? ' ust' : ''),
      hh: IKI(hh), mm: IKI(mi), ss: IKI(ss), snCls: ss % 2 ? 'sn tA' : 'sn tB', cdAria: 'Bugüne özel fiyatın bitmesine ' + hh + ' saat ' + mi + ' dakika',
      alaGit: alaGit, faq: faq, shop: shop, shopCount: PR.length
    };
  }
}"""

# Renk seçenekleri: aynı düzen, farklı ikinci renk + yazı tipi (lacivert sabit)
SECENEK = ['kuzey', 'pembe', 'mercan', 'gumus']

if __name__ == '__main__':
    h = int(os.environ.get('U_H', 7155))
    open(os.path.join(CANVAS, 'GalaxyUSB.dc.html'), 'w', encoding='utf-8').write(sayfa(ANA_TEMA) + TAIL.format(h=h, js=JS))
    print('yazıldı: GalaxyUSB.dc.html (tema %s, h %d)' % (ANA_TEMA, h))
    hs = int(os.environ.get('U_HS', 2600))
    for no, ad in enumerate(SECENEK, 1):
        open(os.path.join(CANVAS, 'GalaxyUSB-Renk-%s.dc.html' % ad), 'w', encoding='utf-8').write(sayfa(ad, no) + TAIL.format(h=hs, js=JS))
        print('yazıldı: GalaxyUSB-Renk-%s.dc.html' % ad)
