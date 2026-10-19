# Ayluna · ana sayfa (18 Eki). Çalıştır: python3 anasayfa.py
# Kullanıcı: "Artık ana sayfa tasarlayıp bunların hepsini derleyebiliriz… benim sitemdeki her kısım burada da aynı şekilde gelmeli.
# Site içinde kendi görselleri var, direkt onları kullanabilirsin. Reklama açık olan 2 ürünüm bunlardı (LunaDream, Galaxy USB)."
# Canlı ana sayfanın sırası korunur (ogrenme/site-envanter.md §1): duyuru → üst menü → slayt → Loox yorumları → öne çıkan ürünler →
# ikon çubuğu → AyFeneri görsel + metin → bülten → alt bilgi → yukarı çık.
# Düzeltilenler: sahte 62 dk sayaç → gün sonu fiyat sayacı (ürün sayfalarıyla aynı); görsele gömülü "4.7/5 · 2467 yorum", "90 gün iade",
# "1 yıl garanti" yazılı slaytlar → yazısız görsel + HTML yazı; emoji ikonlar → çizgi ikon; "Bunlarıda" → doğru yazım; 17 MB GIF → tek kare;
# eksik koleksiyon (9/15) → 15 ürün; İngilizce "SAVE %x" → "%x"; Dokunmatik Lamba'da eski fiyat yeni fiyattan düşük → üstü çizili yok;
# alt bilgide eksik yasal bilgi → yer tutucu; ödeme logoları: VISA, Mastercard, Troy (canlıdaki Amex/Diners/Discover/JCB yanlış).
# Dil: marka çekirdeği (sepetle aynı) lacivert #1A2142 + krem #F6F1E9, Ayluna işareti; Young Serif + Onest.
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL, TL_JS
import luna_e as E
CANVAS = os.path.join(HERE, '..', '..', 'canvas')
OUT = os.path.join(CANVAS, 'Ayluna-Anasayfa.dc.html')  # arşivdeki eski Anasayfa.dc.html korunur
B = '/_blob/'
BL = json.load(open(os.path.join(CANVAS, 'ana', 'bloblar.json')))
U = lambda h: BL['u-%s.jpg' % h]

# Ürünler: canlı mağazadaki fiyat ve stok (products.json, 18 Eki). Reklamdaki iki ürün başta.
URUN = [
    ('lunadream-gece-lambasi', 'LunaDream Gece Lambası', 1699.99, 1999, True),
    ('galayx-usb-projektor', 'Galaxy USB Projektör', 1599, 1999, True),
    ('lamba', 'Ayluna AyFeneri', 1649.99, 2499, True),
    ('ayluna-galaksi-night-projektor', 'Galaksi Night Projektör', 2199, 2999, True),
    ('galaksiambiyanisigi', 'Galaksi Ambiyans Işığı', 1499, 2898, True),
    ('ayluna-cocuk-gece-feneri', 'Çocuk Gece Feneri', 1599, None, True),
    ('ask-saati', 'Kum Saati Lamba', 799, 999, True),
    ('yildiz-isigi-nemlendirici', 'Yıldız Işığı Nemlendirici', 849.99, 1099, True),
    ('astronot-oda-nemlendirici-aroma-difuzor', 'Astronot Nemlendirici', 799, None, True),
    ('sunset-lamba', 'Sunset Lamba', 699, 999, True),
    ('ayluna-retro-mini-pikap', 'Retro Mini Pikap', 1499, 1999.99, True),
    ('egitici-akilli-cizim-tahtasi', 'Eğitici Akıllı Çizim Tahtası', 1199, 1999, True),
    ('aroma-terapi-nemlendirici', 'Aroma Terapi Nemlendirici', 1499, 1999, False),
    ('dokunmatik-ambiyans-lamba', 'Dokunmatik Ambiyans Lamba', 1299.99, None, False),  # canlıda eski fiyat (1.299) yeni fiyattan düşük: gösterilmez
    ('lunadream-gece-lambasi-v2', 'LunaDream Gece Lambası V2', 1449, 1999, False),
]
ANA_SAY = 8  # ana sayfada ilk 8 ürün, gerisi "Tüm ürünler"

# Slayt: yazısız görsel + HTML yazı (görsele gömülü yazı yok). LunaDream ve USB görselleri tuvalde zaten var.
SLAYT = [
    ('fd0bca1b99cf3837b69fb025cc4e2cd9', '50% 55%', 'LunaDream Gece Lambası', 'Masal gibi<br>geceler.', 'Ninni çalar; kutuda 6 + 6 hediye disk.', 'LunaDream\'i incele', 'Gece çocuk odası, komodinde yanan LunaDream'),
    ('7d5f80214a0664a51946b0ece044e8cb', '50% 30%', 'Galaxy USB Projektör', 'Tavanı<br>sahneye çevir.', 'Bir USB girişi, 12 film diski.', 'Galaxy USB\'yi incele', 'Komodinde beyaz Galaxy USB projektör'),
    (BL['ayfeneri-kare.jpg'], '50% 30%', 'Ayluna AyFeneri', 'Duvara<br>ay yansıt.', 'Kumandalı, Bluetooth hoparlörlü deniz feneri.', 'AyFeneri\'ni incele', 'Duvara ay yansıtan AyFeneri deniz feneri lamba'),
]
# Loox yorumları: canlı ana sayfa karuselinden, kelimesi kelimesine (m.28/B: Shopify'da Loox bölümü hepsini otomatik gösterir).
# "Doğrulanmış" ve yıldız yazılmaz: envantere göre bazı ürünlerde yorumlar ürünün eklendiği gün yazılmış, doğrulama etiketi yok.
YORUM = [('Nisan C.', 'Kargo hızlıydı, paketleme sağlamdı. Ürün görseldeki gibi, hiç farkı yok.'),
         ('Yasemin C.', 'Oğluma oyalansın diye aldım eskiden evde tabletle gezerdi 1 haftadır yüzüne bakmıyor'),
         ('Meryem Ö.', 'Kızıma aldım çok kaliteli ve çocuğun dikkatini çekiyor güvenle alabilirsiniz'),
         ('Ebru Ö.', 'Fiyatına göre kesinlikle değer. Masamda çok güzel duruyor, herkes nereden aldın diye soruyor.'),
         ('Cihan Z.', 'Sitede söylendiği gibi hediyeleri ile birlikte geldi')]

CSS = r""".pg{--lac:#1A2142;--koyu:#0C1027;--krem:#F6F1E9;--kart:#FFFDF9;--amber:#F2A65A;--soluk:#5C6078;--cizgi:#E3D8C7;--ease:cubic-bezier(.2,.7,.2,1);font-size:15px}
.pg button{font:inherit;color:inherit;cursor:pointer}
.pg a{text-decoration:none}
.pg button:focus-visible,.pg a:focus-visible,.pg input:focus-visible{outline:2px solid var(--lac);outline-offset:3px}
.h2{font-size:28px}
.h2 .n{color:var(--amber)}
@keyframes sol{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
@keyframes kb{from{transform:scale(1.02)}to{transform:scale(1.09)}}
/* Duyuru: gün sonu fiyat sayacı (ürün sayfalarıyla aynı; canlıdaki her açılışta 1:02:00'dan başlayan sayaç yerine) */
.duyuru{display:flex;align-items:center;justify-content:center;gap:8px;height:38px;background:var(--lac);color:#FFFDF9;font-size:13px;font-weight:600}
.duyuru svg{width:14px;height:14px}.duyuru circle{fill:none;stroke:rgba(255,253,249,.5);stroke-width:2}.duyuru path{fill:var(--amber)}
.duyuru b{font-variant-numeric:tabular-nums;color:var(--amber)}
/* Üst menü */
.ust{display:flex;align-items:center;justify-content:space-between;height:56px;padding:0 4px;background:var(--krem)}
.ust .sag{display:flex}
.ikon{position:relative;width:48px;height:48px;display:grid;place-items:center;border:0;background:transparent;color:var(--lac)}
.ikon svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.ikon i{position:absolute;right:8px;top:8px;min-width:17px;height:17px;padding:0 4px;border-radius:999px;background:var(--lac);color:#fff;font-style:normal;font-size:12px;font-weight:700;line-height:17px;text-align:center}
.marka{display:flex;align-items:center;gap:6px;color:var(--lac)}
.marka b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:20px;letter-spacing:-.01em}
/* Slayt: kaydırılır, 5 sn'de geçer; altta ay evreleri dolar (ürün sayfalarındaki galeriyle aynı dil) */
.slayt{position:relative;margin:0 12px;height:520px;border-radius:24px;overflow:hidden;background:var(--koyu);color:#FFFDF9}
.s-iz{position:absolute;inset:0;display:flex;overflow-x:auto;scroll-snap-type:x mandatory;overscroll-behavior-x:contain;scrollbar-width:none}
.s-iz::-webkit-scrollbar{display:none}
.sl{position:relative;flex:0 0 100%;overflow:hidden;scroll-snap-align:start}
.sl>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.sl.on>img{animation:kb 7s linear both}
.sl::after{content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(180deg,rgba(12,16,39,0) 38%,rgba(12,16,39,.9) 88%)}
.sl-y{position:absolute;left:20px;right:20px;bottom:64px;z-index:1}
.sl-y small{display:block;font-size:13px;font-weight:600;color:#E8DCC8}
.sl-y h2{margin:6px 0 0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:38px;line-height:1.02;letter-spacing:-.02em}
.sl-y p{margin:8px 0 0;font-size:15px;color:#D9D4CC}
.sl.on .sl-y>*{animation:sol .7s var(--ease) both}.sl.on .sl-y p{animation-delay:.08s}.sl.on .sl-y a{animation-delay:.16s}
.sl-y a{display:inline-flex;align-items:center;gap:8px;min-height:48px;margin-top:14px;padding:0 18px;border-radius:999px;background:#FFFDF9;color:var(--lac);font-size:15px;font-weight:700}
.sl-y a svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.ay-iz{position:absolute;left:20px;bottom:24px;z-index:2;display:flex;gap:8px;pointer-events:none}
.ay-iz svg{width:15px;height:15px;transition:transform .45s var(--ease)}
.ay-iz circle{fill:rgba(12,16,39,.45);stroke:rgba(255,253,249,.5);stroke-width:1.6}
.ay-iz path{fill:var(--amber);opacity:0;transform-origin:12px 12px;transform:scale(.5);transition:opacity .5s var(--ease),transform .5s var(--ease)}
.ay-iz .lit path{opacity:1;transform:none}.ay-iz .on{transform:scale(1.4)}.ay-iz .on circle{stroke:#FFFDF9}
/* Bölüm başlığı */
.bb{display:flex;align-items:flex-end;justify-content:space-between;gap:12px;padding:40px 16px 0}
.bb a{flex:none;display:inline-flex;align-items:center;min-height:48px;font-size:14px;font-weight:700;color:var(--lac);text-decoration:underline;text-underline-offset:4px;text-decoration-color:var(--cizgi)}
/* Loox yorumları */
.yorum-serit{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:16px;padding:16px 16px 4px;scrollbar-width:none}
.yorum-serit::-webkit-scrollbar{display:none}
.yk{flex:0 0 260px;scroll-snap-align:start;display:flex;flex-direction:column;gap:10px;padding:18px;border-radius:20px;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi)}
.yk .yildiz{color:var(--amber);letter-spacing:2px;font-size:14px}
.yk p{margin:0;flex:1;font-family:"Young Serif",Georgia,serif;font-size:17px;line-height:1.35;color:var(--lac)}
.yk span{display:flex;align-items:center;gap:6px;font-size:13px;font-weight:600;color:var(--soluk)}
.yk span svg{width:14px;height:14px;fill:none;stroke:#2E6B4F;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.y-not{margin:10px 16px 0;font-size:12px;color:var(--soluk)}
/* Ürün ızgarası */
.izgara{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;padding:16px 16px 0}
.uk{display:flex;flex-direction:column;border-radius:18px;overflow:hidden;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi);color:var(--lac)}
.uk>span:first-child{position:relative;aspect-ratio:1/1;overflow:hidden;background:#EFE6D8}
.uk img{display:block;width:100%;height:100%;object-fit:cover}
.uk em{position:absolute;left:8px;top:8px;padding:2px 8px;border-radius:999px;background:var(--lac);color:#fff;font-style:normal;font-size:12px;font-weight:700}
.uk em.tukendi{background:#FFFDF9;color:var(--lac);box-shadow:inset 0 0 0 1px var(--cizgi)}
.uk.yok img{opacity:.55}
.uk>span:last-child{display:flex;flex-direction:column;gap:4px;padding:10px 12px 14px}
.uk b{font-size:14px;font-weight:600;line-height:1.3;min-height:36px}
.uk .f{display:flex;align-items:baseline;flex-wrap:wrap;gap:2px 6px;font-variant-numeric:tabular-nums}
.uk .f strong{font-size:15px}
.uk .f s{font-size:12px;color:var(--soluk)}
.tum{display:flex;align-items:center;justify-content:center;gap:8px;min-height:52px;margin:16px 16px 0;border-radius:16px;box-shadow:inset 0 0 0 1.5px var(--lac);color:var(--lac);font-size:15px;font-weight:700}
/* İkon çubuğu: güven (canlıdaki emojili AyFeneri maddeleri AyFeneri bölümüne taşındı) */
.guven{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));margin:40px 16px 0;border-radius:20px;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi);overflow:hidden}
.guven div{display:flex;flex-direction:column;gap:4px;padding:16px 14px}
.guven div:nth-child(-n+2){border-bottom:1px solid var(--cizgi)}.guven div:nth-child(odd){border-right:1px solid var(--cizgi)}
.guven svg{width:26px;height:26px;margin-bottom:6px;fill:none;stroke:var(--lac);stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.guven b{font-size:15px}.guven span{font-size:13px;color:var(--soluk);line-height:1.35}
/* AyFeneri: görsel + metin */
.ay-blok{margin:40px 12px 0;border-radius:24px;overflow:hidden;background:var(--lac);color:#FFFDF9}
.ay-blok img{display:block;width:100%;height:420px;object-fit:cover;object-position:50% 20%}
.ay-blok>div{padding:22px 20px 24px}
.ay-blok h2{margin:0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:30px;line-height:1.05;letter-spacing:-.02em}
.ay-blok h2 span{color:var(--amber)}
.ay-blok p{margin:10px 0 0;font-size:15px;color:#C9CEE2}
.cipler{display:flex;flex-wrap:wrap;gap:6px;margin-top:14px}
.cipler span{padding:6px 12px;border-radius:999px;box-shadow:inset 0 0 0 1px rgba(255,253,249,.25);font-size:13px;font-weight:600}
.ay-blok a{display:flex;align-items:center;justify-content:center;gap:8px;min-height:54px;margin-top:18px;border-radius:16px;background:#FFFDF9;color:var(--lac);font-size:15px;font-weight:700}
/* Bülten */
.bulten{margin:40px 16px 0;padding:22px 18px;border-radius:20px;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi)}
.bulten h2{font-size:24px}
.bulten p{margin:6px 0 0;font-size:14px;color:var(--soluk)}
.bulten form{display:flex;gap:8px;margin-top:14px}
.bulten input{flex:1;min-width:0;height:50px;padding:0 14px;border:0;border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1.5px var(--cizgi);font:inherit;font-size:15px;color:var(--lac)}
.bulten button{flex:none;height:50px;padding:0 18px;border:0;border-radius:14px;background:var(--lac);color:#fff;font-weight:700}
/* Alt bilgi */
.alt{margin-top:40px;padding:34px 16px 110px;border-radius:28px 28px 0 0;background:var(--lac);color:#B9BED6}
.alt .sut{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 16px}
.alt h3{margin:0 0 4px;font-size:13px;font-weight:700;color:#FFFDF9}
.alt a{display:flex;align-items:center;min-height:48px;font-size:14px;color:#FFFDF9}
.alt .yasal{margin:18px 0 0;font-size:13px;line-height:1.55}
.kart-logo{display:flex;flex-wrap:wrap;gap:6px;margin-top:18px}
.kart-logo span{display:inline-flex;align-items:center;height:28px;padding:0 10px;border-radius:6px;background:rgba(255,253,249,.08);color:#FFFDF9;font-size:12px;font-weight:800;letter-spacing:.02em}
.alt .imza{display:flex;align-items:center;gap:12px;margin-top:26px;color:#FFFDF9}
.alt .imza span{font-family:"Young Serif",Georgia,serif;font-size:58px;line-height:.8;letter-spacing:-.045em}
.alt .telif{margin:16px 0 0;padding-top:14px;border-top:1px solid rgba(255,253,249,.12);font-size:12px}
/* Yukarı çık (canlıda var): 400px kaydırınca görünür */
.yukari{position:sticky;bottom:18px;z-index:5;display:grid;place-items:center;width:48px;height:48px;margin:-66px 18px 18px auto;border:0;border-radius:50%;background:#FFFDF9;color:var(--lac);box-shadow:inset 0 0 0 1.5px var(--lac)}
.yukari svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
"""

OK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"></path></svg>'
TIK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg>'


def urun_kart(h, ad, p, c, var):
    def tl(x):
        s = ('%.2f' % x).split('.'); t = ''
        n = s[0]
        while len(n) > 3: t = '.' + n[-3:] + t; n = n[:-3]
        return '₺' + n + t + ',' + s[1]
    rozet = '<em class="tukendi">Tükendi</em>' if not var else ('<em>%%%d</em>' % round((1 - p / c) * 100) if c and c > p else '')
    eski = '<s>%s</s>' % tl(c) if c and c > p else ''
    return ('<a class="uk%s" href="#"><span><img src="%s%s" alt="%s">%s</span><span><b>%s</b><span class="f"><strong>%s</strong>%s</span></span></a>'
            % ('' if var else ' yok', B, U(h), ad, rozet, ad, tl(p), eski))


GUVEN = [('<path d="M3 7h11v8H3z"></path><path d="M14 10h4l3 3v2h-7"></path><circle cx="7" cy="17" r="1.8"></circle><circle cx="17" cy="17" r="1.8"></circle>', 'Ücretsiz kargo', 'Türkiye geneline, takip numarasıyla.'),
         ('<path d="M4 12a8 8 0 1 0 2.3-5.6"></path><path d="M4 4v4h4"></path>', '30 gün iade', 'Beğenmezsen geri gönder, kargosu ücretsiz.'),
         ('<rect x="3" y="6" width="18" height="12" rx="2"></rect><path d="M3 10h18M7 15h4"></path>', 'Kartla %5 indirim', 'Kart bilgin bize gelmez. Kapıda ödemede +₺80.'),
         ('<path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"></path>', 'WhatsApp destek', 'Ortalama 2 saatte yanıt.')]

HTML = ('<div class="pg" style="padding-bottom: 0">\n'
        '  <div class="duyuru" role="timer" aria-label="{{cdAria}}"><span>Bugünkü fiyat garantisi</span><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="{{cdAy}}"></path></svg><b>{{cd}}</b></div>\n'
        '  <header class="ust"><button class="ikon" type="button" aria-label="Menü"><svg viewBox="0 0 24 24"><path d="M4 8h16M4 16h11"></path></svg></button>'
        '<a class="marka" href="#" aria-label="Ayluna ana sayfa">' + E.isaret(22, 'rgba(26,33,66,.45)') + '<b>Ayluna</b></a>'
        '<span class="sag"><button class="ikon" type="button" aria-label="Ara"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="6.5"></circle><path d="M16 16l4 4"></path></svg></button>'
        '<button class="ikon" type="button" aria-label="Sepet, 0 ürün"><svg viewBox="0 0 24 24"><path d="M6 8h12l-1 12H7z"></path><path d="M9 8a3 3 0 0 1 6 0"></path></svg><i>0</i></button></span></header>\n'
        '  <!-- Slayt: kaydırılır, 5 sn\'de geçer (elle kaydırınca durur). Yazılar HTML; görsele gömülü yazı yok. Altta ay evreleri dolar. -->\n'
        '  <section class="slayt" aria-label="Öne çıkan ürünler">\n'
        '    <div class="s-iz" onScroll="{{sKay}}"><sc-for list="{{slayt}}" as="s" hint-placeholder-count="3"><div class="{{s.cls}}"><img src="{{s.src}}" alt="{{s.alt}}" style="object-position: {{s.pos}}"><div class="sl-y"><small>{{s.ust}}</small><h2>{{s.bas}}</h2><p>{{s.alt2}}</p><a href="#">{{s.cta}}' + OK + '</a></div></div></sc-for></div>\n'
        '    <span class="ay-iz" aria-hidden="true"><sc-for list="{{slayt}}" as="s" hint-placeholder-count="3"><svg class="{{s.acls}}" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="{{s.ay}}"></path></svg></sc-for></span>\n'
        '  </section>\n'
        '  <!-- Loox yorumları: Shopify\'da Loox karusel bölümü (gerçek yorumlar, hepsi). Burada canlı karuselden beşi, kelimesi kelimesine. -->\n'
        '  <div class="bb"><h2 class="h2">Alanlar ne <br>diyor<span class="n">?</span></h2></div>\n'
        '  <div class="yorum-serit">' + ''.join('<div class="yk"><p>“%s”</p><span>%s</span></div>' % (t, n) for n, t in YORUM) + '<span aria-hidden="true" style="flex: 0 0 4px"></span></div>\n'
        '  <!-- Teyit: bazı ürünlerde yorumlar ürünün eklendiği gün yazılmış ve etiketsiz (ogrenme/urun-envanter.md) -->\n  <p class="y-not">Yorumlar Loox\'tan; tamamı gösterilir.</p>\n'
        '  <!-- Öne çıkan ürünler (canlıda "Bunlarıda sevebilirsin", 9/15 ürün): burada 15 ürün; ilk 8\'i ana sayfada -->\n'
        '  <div class="bb"><h2 class="h2">Odana bir <br>gökyüzü<span class="n">.</span></h2><a href="#">Tümünü gör</a></div>\n'
        '  <div class="izgara">' + ''.join(urun_kart(*u) for u in URUN[:ANA_SAY]) + '</div>\n'
        '  <a class="tum" href="#">Tüm ürünler (' + str(len(URUN)) + ')' + OK.replace('<svg ', '<svg style="width: 16px; height: 16px; fill: none; stroke: currentColor; stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round" ') + '</a>\n'
        '  <!-- İkon çubuğu: güven (emoji yok) -->\n'
        '  <div class="guven">' + ''.join('<div><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg><b>%s</b><span>%s</span></div>' % g for g in GUVEN) + '</div>\n'
        '  <!-- AyFeneri görsel + metin: canlıdaki 17 MB GIF yerine tek kare (Veo filigranı kesildi); emojili maddeler çip -->\n'
        '  <section class="ay-blok"><img src="' + B + BL['ayfeneri-kare.jpg'] + '" alt="Duvara ay yansıtan AyFeneri deniz feneri lamba"><div>'
        '<h2>Ay ışığını <br>evine getir<span>.</span></h2>'
        '<p>Gerçekçi ay yansımasıyla odanı daha sıcak ve sakin bir hâle getirir. Sensör, kumanda ve Bluetooth tek üründe; şarjlı olduğu için kablo karmaşası yok.</p>'
        '<div class="cipler"><span>Gerçek ay yansıması</span><span>Otomatik sensör</span><span>Kumanda</span><span>Şarjlı</span></div>'
        '<a href="#">AyFeneri\'ni incele · ₺1.649,99' + OK.replace('<svg ', '<svg style="width: 16px; height: 16px; fill: none; stroke: currentColor; stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round" ') + '</a></div></section>\n'
        '  <!-- Bülten (canlıda "%5 İNDİRM KAZANMAK İÇİN ABONE OL"): %5 kodunun gerçekten gönderildiği teyit edilmeli -->\n'
        '  <section class="bulten"><h2 class="h2">%5 indirim için <br>abone ol<span class="n">.</span></h2><p>Yeni ürünlerden ilk sen haberdar ol.</p><!-- Teyit: %5 kodu e-postayla gerçekten gönderiliyor mu? -->'
        '<form onSubmit="{{dur}}"><label style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%)" for="b-eposta">E-posta</label><input id="b-eposta" type="email" placeholder="E-posta adresin" autocomplete="email"><button type="submit">Kayıt ol</button></form></section>\n'
        '  <footer class="alt"><div class="sut">'
        '<div><h3>Mağaza</h3><a href="#">Ana sayfa</a><a href="#">Tüm ürünler</a><a href="#">Kargo takip</a><a href="#">İletişim</a></div>'
        '<div><h3>Politikalar</h3><a href="#">İade politikası</a><a href="#">Kargo politikası</a><a href="#">Gizlilik</a><a href="#">Hizmet şartları</a><a href="#">Mesafeli Satış Sözleşmesi</a><a href="#">KVKK</a></div></div>'
        '<p class="yasal">[Ticaret unvanı] · MERSİS [no]<br>[Adres] · [telefon]<br>ecom11001@gmail.com · KEP [adres]</p>'
        '<div class="kart-logo" aria-label="Kabul edilen kartlar"><span>VISA</span><span>Mastercard</span><span>Troy</span></div>'
        '<div class="imza" aria-label="Ayluna">' + E.isaret(48) + '<span aria-hidden="true">Ayluna</span></div>'
        '<p class="telif">Fiyatlara KDV dahildir. © 2026 Ayluna</p></footer>\n'
        '  <button class="yukari" type="button" aria-label="Yukarı çık"><svg viewBox="0 0 24 24"><path d="M12 19V5M6 11l6-6 6 6"></path></svg></button>\n'
        '</div>\n')

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { s: 0, sOto: true, now: Date.now() }; }
  componentDidMount() {
    var self = this;
    if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) this.state.sOto = false;
    this.tik = 0; this.iv = setInterval(function () { self.tik++; if (self.state.sOto && self.tik % 5 === 0) self.git((self.state.s + 1) % """ + str(len(SLAYT)) + """); self.setState({ now: Date.now() }); }, 1000);
  }
  componentWillUnmount() { clearInterval(this.iv); }
  git(i) { var el = document.querySelector('.s-iz'); if (el && el.scrollTo && el.clientWidth) { this.otoKay = Date.now(); el.scrollTo({ left: i * el.clientWidth, behavior: 'smooth' }); } else this.setState({ s: i }); }
  componentDidUpdate() { var el = document.querySelector('.s-iz'); if (el && el.clientWidth && Math.abs(el.scrollLeft - this.state.s * el.clientWidth) > el.clientWidth / 2) { this.otoKay = Date.now(); el.scrollLeft = this.state.s * el.clientWidth; } }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    function AYE(f) { var r = 9, c = 12, rx = Math.abs(1 - 2 * f) * r; return f >= 1 ? 'M12 3a9 9 0 1 1 0 18a9 9 0 1 1 0-18Z' : 'M' + c + ' ' + (c - r) + 'A' + r + ' ' + r + ' 0 0 1 ' + c + ' ' + (c + r) + 'A' + rx.toFixed(2) + ' ' + r + ' 0 0 ' + (f < .5 ? 0 : 1) + ' ' + c + ' ' + (c - r) + 'Z'; }
    var SL = """ + json.dumps([list(x) for x in SLAYT], ensure_ascii=False) + """;
    var slayt = SL.map(function (x, i) { var on = i === S.s; return { src: B + x[0], pos: x[1], ust: x[2], bas: x[3].replace('<br>', ' '), alt2: x[4], cta: x[5], alt: x[6], cls: on ? 'sl on' : 'sl', ay: AYE((i + 1) / SL.length), acls: i < S.s ? 'lit' : (on ? 'lit on' : '') }; });
    function sKay(e) { var el = e && (e.currentTarget || e.target); if (!el || !el.clientWidth) return; var i = Math.round(el.scrollLeft / el.clientWidth), o = {};
      if (i !== self.state.s) o.s = i; if (self.state.sOto && Date.now() - (self.otoKay || 0) > 900) o.sOto = false; if (o.s !== undefined || o.sOto === false) self.setState(o); }
    function IKI(n) { return n < 10 ? '0' + n : String(n); }
    var ist = new Date(new Date(S.now || Date.now()).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kalan = Math.max(0, new Date(ist.getFullYear(), ist.getMonth(), ist.getDate(), 23, 59, 59, 999).getTime() - ist.getTime());
    var hh = Math.floor(kalan / 3600000), mi = Math.floor(kalan / 60000) % 60, ss = Math.floor(kalan / 1000) % 60;
    return { slayt: slayt, sKay: sKay, cd: IKI(hh) + ':' + IKI(mi) + ':' + IKI(ss), cdAy: AYE(Math.max(.02, Math.min(1, kalan / 86400000))),
      cdAria: 'Bugünkü fiyat garantisinin bitmesine ' + hh + ' saat ' + mi + ' dakika', dur: function (e) { if (e && e.preventDefault) e.preventDefault(); } };
  }
}"""

if __name__ == '__main__':
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='Ayluna · Ana sayfa', css=CSS) + HTML + TAIL.format(h=int(os.environ.get('A_H', 4290)), js=JS))
    print('yazıldı:', os.path.abspath(OUT))
