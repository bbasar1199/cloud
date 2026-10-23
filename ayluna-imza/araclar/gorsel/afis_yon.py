# LunaDream galeri afişleri · 2. tur yön taslakları (22 Eki).
# Kullanıcı: "Site görsellerini beğenmedim; LunaDream için satış odaklı değil, yorum görseli yapılmamış, çok sönük kalmış."
# Teşhis: 1. tur afişleri krem zeminli, ince serifli, çoğunda yalnız ürün; eski mağaza afişlerinin ve USB galerisinin satan
# unsurları yoktu: duvara/tavana vuran yansıma, doygun gece rengi, kalın büyük başlık, yorum ve müşteri karesi, güven şeridi.
# Üç yön × üç kare (açılış, yorum, diskler):
#   A · Gece vitrini: USB galerisi gibi; tam kare gece fotoğrafı, kalın iki renkli başlık, simge halkaları, altta güven şeridi.
#   B · Mağaza afişi: eski mağaza afişlerinin enerjisi; büyük harf ağır başlık sağ üstte, lacivert özellik paneli, yorum kartları ürünün çevresinde.
#   C · Masal gecesi: marka serifi (Young Serif) ama canlı gece fotoğrafı; tek büyük alıntı, disk yayı.
# Yorumlar Loox'taki gerçek alıcılardan (Burak G., Handan B., Abdülkerim T., Mehmet C., Sevcan Z.), metin birebir. Puan ve yorum
# sayısı görsele gömülmez (değişince görsel eskir; sayfada zaten Loox'tan gelir). Fiyat yazılmaz. Güven şeridi teyitli:
# ücretsiz kargo, 30 gün iade, kapıda ödeme. "6 + 6" yok, yalnız "6 masal diski".
# Çalıştır: /tmp/sr-env/bin/python araclar/gorsel/afis_yon.py  →  canvas/p-gorsel/yon/{A,B,C}-{1,2,3}.jpg + yonler.jpg (pano)
import os, sys, subprocess, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import afis_uret as U

P, F, ikon, ay = U.P, U.F, U.ikon, U.ay
CIKIS = os.path.join(U.KOK, 'canvas', 'p-gorsel', 'yon')
YORUM = {'burak': ('Burak G.', 'Çocuğum çalıştırmadan uyumuyor, uykuya hemen dalıyor.'),
         'handan': ('Handan B.', 'Torunum filmlerini kendisi seçti ve onunla uyumaya başladı.'),
         'abdulkerim': ('Abdülkerim T.', 'Reklamında nasıl ise aynısı, hatta daha iyisi. Çocuklar için mükemmel bir hediye.'),
         'mehmet': ('Mehmet C.', 'Anlatıldığı ve gösterildiği gibi çıktı. Bu kadar iyi olmasını beklemiyordum.'),
         'sevcan': ('Sevcan Z.', '2 tane aldık, gayet sağlam geldi. Paketlenmesi de güzeldi.')}
TIK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.2 4.2L19 7"/></svg>'
U.IK['kargo'] = '<path d="M2.5 7h11v9h-11zM13.5 10h4l3 3v3h-7"/><circle cx="6.5" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>'
U.IK['iade'] = '<path d="M4 12a8 8 0 1 0 2.4-5.7"/><path d="M4 4v4.5h4.5"/>'
U.IK['kapi'] = '<rect x="3" y="6" width="18" height="12" rx="2"/><circle cx="12" cy="12" r="2.6"/><path d="M6 9.5v5M18 9.5v5"/>'
GUVEN = [('kargo', 'Ücretsiz kargo'), ('iade', '30 gün iade'), ('kapi', 'Kapıda ödeme')]
DISK = ['disk-ay-yildiz', 'disk-okyanus', 'disk-uzay', 'disk-deniz-kizi', 'disk-sato', 'disk-masal']


def logo(renk='#FFFDF9'):
    return '<div class="logo">%s<span>Ayluna</span></div>' % ay(renk)


def guven(sinif='guven'):
    return '<div class="%s">' % sinif + ''.join('<span>%s%s</span>' % (ikon(k, 'currentColor'), t) for k, t in GUVEN) + '</div>'


def halkalar(liste, renk='#FFFDF9'):
    return '<div class="ozler">' + ''.join('<div class="oz"><span class="halka">%s</span><b>%s</b><i>%s</i></div>' % (ikon(k, renk), a, b) for k, a, b in liste) + '</div>'


def kart(k, sinif='kart'):
    ad, s = YORUM[k]
    return '<div class="%s"><p>%s</p><div class="kim"><b>%s</b><span class="tik">%sSatın aldı</span></div></div>' % (sinif, s, ad, TIK)


OZ3 = [('disk', '6 masal', 'diski'), ('nota', 'Bluetooth', 'ninni'), ('isik', '3 kademe', 'ışık')]

AFIS = {
    # ── A · Gece vitrini ───────────────────────────────────────────────────────────────────────────────
    'A-1': '<img class="tam" src="%s" style="object-position:50%% 30%%"><div class="perde-ust"></div>' % P('c-gorsel/c-kiz-gece.jpg') + logo() +
           '<div class="a-bas"><h2>Tavanı masala<em>çeviren lamba</em></h2><p>Diski tak, ışığı kapat:<br>masal tavana yansısın.</p>' + halkalar(OZ3) + '</div>' + guven(),
    'A-2': '<div class="a-yz">' + logo() + '<h2>Alanlar<em>ne diyor?</em></h2><p class="alt">Gerçek alıcılar, birebir yorumlar.</p>'
           '<div class="a-kartlar">' + kart('handan') + kart('burak') + kart('abdulkerim') + '</div></div>'
           '<img class="a-yz-foto" src="%s">' % P('c-gorsel/c-ninni-kiz2.jpg') + guven(),
    'A-3': '<img class="tam" src="%s" style="object-position:50%% 20%%"><div class="perde-alt"></div>' % P('c-gorsel/hd/c-an-disk.jpg') + logo() +
           '<div class="a-bas a-alt"><h2>Her gece<em>başka bir masal</em></h2><p>Kubbeyi aç, diski tak. Kutuda 6 masal diski.</p></div>' + guven(),
    # ── B · Mağaza afişi ───────────────────────────────────────────────────────────────────────────────
    'B-1': '<img class="tam" src="%s" style="object-position:50%% 30%%"><div class="perde-sag"></div>' % P('c-gorsel/c-kiz-gece.jpg') + logo() +
           '<div class="b-bas"><h2 lang="tr">MASAL ANLATAN<em>GECE LAMBASI</em></h2><p>Tavana ay, yıldız ve masal yansıtır.</p></div>'
           '<div class="b-panel">' + ''.join('<div>%s<span><b>%s</b>%s</span></div>' % (ikon(k, '#F2A65A'), a, b) for k, a, b in
                                              [('disk', '6 masal diski', 'Diski tak, masal değişsin'), ('nota', 'Bluetooth ninni', 'Telefondan çalar'), ('isik', '3 kademe ışık', 'Kısık, orta, parlak')]) + '</div>'
           '<div class="b-pil">Kapıda ödeme · Ücretsiz kargo</div>',
    'B-2': '<div class="b-yz-zem"></div><img class="b-yz-lamba" src="%s">' % P('c-gorsel/parca/kiz-tam.webp') + logo() +
           '<h2 class="b-yz-bas" lang="tr">ALANLAR<em>NE DİYOR?</em></h2>'
           + kart('burak', 'kart b-k1') + kart('handan', 'kart b-k2') + kart('abdulkerim', 'kart b-k3') + kart('mehmet', 'kart b-k4') +
           '<div class="b-pil">Gerçek alıcı yorumları</div>',
    'B-3': '<img class="tam" src="%s" style="object-position:50%% 55%%"><div class="perde-sag"></div>' % P('c-gorsel/hd/c-an-tavan.jpg') + logo() +
           '<div class="b-bas"><h2 lang="tr">DUVARINI<em>CANLANDIR</em></h2><p>Okyanus diskini tak, odayı deniz altına çevir.</p></div>'
           '<div class="b-disk">' + ''.join('<img src="%s">' % P('diskler/%s.jpg' % d) for d in DISK) + '<b>6 masal diski</b></div>'
           '<div class="b-pil">Kapıda ödeme · Ücretsiz kargo</div>',
    # ── C · Masal gecesi ───────────────────────────────────────────────────────────────────────────────
    'C-1': '<img class="tam" src="%s" style="object-position:50%% 30%%"><div class="perde-alt"></div>' % P('c-gorsel/c-kiz-gece.jpg') + logo() +
           '<div class="c-bas"><h2>Işık kapanınca<em>masal başlar.</em></h2><div class="c-cizgi"><span>6 masal diski</span><span>Bluetooth ninni</span><span>3 kademe ışık</span></div></div>',
    'C-2': '<img class="tam bulanik" src="%s" style="object-position:50%% 40%%"><div class="perde-tam"></div>' % P('c-gorsel/c-ninni-kiz2.jpg') + logo() +
           '<div class="c-alinti"><span class="tirnak">“</span><p>%s</p><div class="kim"><b>%s</b><span class="tik">%sSatın aldı</span></div></div>' % (YORUM['handan'][1], YORUM['handan'][0], TIK) +
           '<div class="c-diger">' + kart('burak', 'kart c-k') + kart('mehmet', 'kart c-k') + '</div>',
    'C-3': '<div class="c-disk-zem"></div>' + logo() +
           '<div class="c-yay">' + ''.join('<img src="%s" style="--i:%d">' % (P('diskler/%s.jpg' % d), i) for i, d in enumerate(DISK)) + '</div>'
           '<img class="c-lamba" src="%s">' % P('p-gorsel/p-kiz-gece.webp') +
           '<div class="c-bas c-ust"><h2>Bu gece<em>hangi masal?</em></h2><p>Kutuda 6 masal diski. Seçmek ona kalsın.</p></div>',
}

CSS = U.FONT_CSS + """
body{margin:0;background:#888}
.afis{position:relative;width:1080px;height:1080px;overflow:hidden;font-family:Onest,sans-serif;margin:0 0 20px}
.logo{position:absolute;left:64px;top:52px;display:flex;align-items:center;gap:14px;font-family:"Young Serif",serif;font-size:42px;letter-spacing:-.01em}
.logo .ay{width:40px;height:40px}
@font-face{font-family:Bricolage;font-weight:800;src:url(FBG-latin-800-normal.woff2)}@font-face{font-family:Bricolage;font-weight:800;src:url(FBG-latin-ext-800-normal.woff2);unicode-range:U+0100-024F}
.afis{background:#0B1020;color:#FFFDF9}
.tam{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:brightness(1.18) saturate(1.25) contrast(1.05)}
.tam.bulanik{filter:blur(14px) saturate(1.2) brightness(1.1);transform:scale(1.08)}
.logo{z-index:3}
.perde-ust{position:absolute;inset:0;background:linear-gradient(100deg,rgba(8,12,30,.9) 0,rgba(8,12,30,.55) 45%,rgba(8,12,30,0) 70%),linear-gradient(0deg,rgba(8,12,30,.85) 0,rgba(8,12,30,0) 22%)}
.perde-sag{position:absolute;inset:0;background:linear-gradient(250deg,rgba(10,16,48,.88) 0,rgba(10,16,48,.5) 36%,rgba(10,16,48,0) 60%),linear-gradient(80deg,rgba(10,16,48,.7) 0,rgba(10,16,48,0) 45%)}
.perde-alt{position:absolute;inset:0;background:linear-gradient(0deg,rgba(8,12,30,.95) 0,rgba(8,12,30,.7) 30%,rgba(8,12,30,0) 55%)}
.perde-tam{position:absolute;inset:0;background:rgba(10,15,40,.72)}
/* A */
.a-bas{position:absolute;left:64px;top:140px;width:760px}
.a-bas h2,.a-yz h2{margin:0;font-weight:700;font-size:92px;line-height:.98;letter-spacing:-.035em}
.a-bas h2 em,.a-yz h2 em{display:block;font-style:normal;color:#F2A65A}
.a-bas p{margin:22px 0 0;font-size:36px;line-height:1.25;font-weight:500;color:rgba(255,253,249,.88)}
.ozler{display:flex;gap:18px;margin-top:30px}
.oz{display:flex;flex-direction:column;align-items:center;width:150px;text-align:center}
.oz .halka{display:grid;place-items:center;width:100px;height:100px;border-radius:50%;background:rgba(11,16,32,.55);box-shadow:inset 0 0 0 2.5px rgba(242,166,90,.9);margin-bottom:10px}
.oz svg{width:46px;height:46px}.oz b{font-size:29px;font-weight:700;line-height:1.1}.oz i{font-style:normal;font-size:26px;font-weight:500;color:rgba(255,253,249,.8)}
.guven{z-index:4;position:absolute;left:40px;right:40px;bottom:36px;display:flex;justify-content:space-between;gap:10px;padding:18px 26px;border-radius:999px;background:#F2A65A;color:#1A2142;font-size:30px;font-weight:700}
.guven span{display:flex;align-items:center;gap:10px}.guven svg{width:38px;height:38px}
.a-yz{position:absolute;left:0;top:0;width:640px;height:100%;padding:150px 0 0 64px;box-sizing:border-box;z-index:2;background:linear-gradient(90deg,#0B1020 72%,rgba(11,16,32,0))}
.a-yz h2{font-size:84px}.a-yz .alt{margin:16px 0 0;font-size:30px;font-weight:500;color:rgba(255,253,249,.78)}
.a-kartlar{display:grid;gap:18px;margin-top:30px;width:600px}
.kart{padding:22px 26px;border-radius:24px;background:#FFFDF9;color:#1A2142;box-shadow:0 18px 40px -18px rgba(0,0,0,.6)}
.kart p{margin:0;font-family:"Young Serif",serif;font-size:31px;line-height:1.22}
.kim{display:flex;align-items:center;justify-content:space-between;margin-top:12px;font-size:25px}
.kim b{font-weight:700}.tik{display:inline-flex;align-items:center;gap:6px;color:#2E7D4F;font-weight:700}.tik svg{width:26px;height:26px}
.a-yz-foto{position:absolute;right:0;top:0;width:560px;height:100%;object-fit:cover;object-position:50% 40%}
.a-alt{top:auto;bottom:140px;width:960px}.a-alt p{font-size:34px}
/* B */
.b-bas{position:absolute;right:56px;top:120px;width:700px;text-align:right}
.b-bas h2,.b-yz-bas{margin:0;font-family:Bricolage,sans-serif;font-weight:800;font-size:96px;line-height:.92;letter-spacing:-.02em}
.b-bas h2 em,.b-yz-bas em{display:block;font-style:normal;color:#F2A65A}
.b-bas p{margin:20px 0 0 auto;max-width:520px;font-size:32px;line-height:1.25;font-weight:500;color:rgba(255,253,249,.9)}
.b-panel{position:absolute;left:56px;top:520px;width:430px;display:grid;gap:4px;padding:16px 22px;border-radius:26px;background:rgba(14,22,60,.82);box-shadow:inset 0 0 0 1.5px rgba(255,253,249,.18)}
.b-panel div{display:flex;align-items:center;gap:16px;padding:12px 0}.b-panel div+div{border-top:1px solid rgba(255,253,249,.14)}
.b-panel svg{width:48px;height:48px;flex:none}.b-panel span{display:flex;flex-direction:column;font-size:24px;font-weight:500;color:rgba(255,253,249,.78)}
.b-panel b{font-size:31px;font-weight:700;color:#FFFDF9}
.b-pil{z-index:4;position:absolute;left:56px;bottom:52px;padding:18px 30px;border-radius:999px;background:#F2A65A;color:#1A2142;font-size:30px;font-weight:700}
.b-yz-zem{position:absolute;inset:0;background:radial-gradient(60% 55% at 50% 62%,#2B3D8F 0,#16205A 45%,#0B1020 100%)}
.b-yz-lamba{position:absolute;left:50%;bottom:-20px;height:640px;transform:translateX(-50%);filter:drop-shadow(0 0 60px rgba(242,166,90,.55))}
.b-yz-bas{position:absolute;right:56px;top:120px;text-align:right;font-size:88px}
.b-k1,.b-k2,.b-k3,.b-k4{position:absolute;width:380px;padding:18px 22px}.kart.b-k1 p,.kart.b-k2 p,.kart.b-k3 p,.kart.b-k4 p{font-size:26px}
.b-k1{left:40px;top:150px;transform:rotate(-2deg)}.b-k2{left:40px;top:470px;transform:rotate(1.5deg)}.b-k3{right:40px;top:350px;transform:rotate(2deg)}.b-k4{right:40px;top:640px;transform:rotate(-1.5deg)}
.b-k1 .kim,.b-k2 .kim,.b-k3 .kim,.b-k4 .kim{font-size:22px}
.b-disk{position:absolute;left:56px;top:470px;width:430px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:22px;border-radius:26px;background:rgba(14,22,60,.82)}
.b-disk img{width:100%;aspect-ratio:1;border-radius:50%;object-fit:cover;box-shadow:0 0 0 3px #FFFDF9}
.b-disk b{grid-column:1/-1;text-align:center;font-size:30px;font-weight:700}
/* C */
.c-bas{position:absolute;left:64px;bottom:70px;width:900px}
.c-bas h2{margin:0;font-family:"Young Serif",serif;font-weight:400;font-size:100px;line-height:1;letter-spacing:-.02em}
.c-bas h2 em{display:block;font-style:normal;color:#F2A65A}
.c-cizgi{display:flex;gap:0;margin-top:26px;font-size:30px;font-weight:700}
.c-cizgi span+span::before{content:"";display:inline-block;width:10px;height:10px;margin:0 18px 6px;border-radius:50%;background:#F2A65A}
.c-alinti{position:absolute;left:64px;right:64px;top:170px}
.tirnak{display:block;height:110px;font-family:"Young Serif",serif;font-size:220px;line-height:.9;color:#F2A65A}
.c-alinti p{margin:0;font-family:"Young Serif",serif;font-size:66px;line-height:1.12;letter-spacing:-.01em}
.c-alinti .kim{justify-content:flex-start;gap:24px;margin-top:24px;font-size:30px}.c-alinti .tik{color:#8FD6A8}
.c-diger{position:absolute;left:64px;right:64px;bottom:56px;display:grid;grid-template-columns:1fr 1fr;gap:18px}
.kart.c-k{padding:18px 22px}.kart.c-k p{font-size:24px}.kart.c-k .kim{font-size:21px}
.c-disk-zem{position:absolute;inset:0;background:radial-gradient(55% 50% at 50% 78%,#3A2A55 0,#1A1E4A 50%,#0B1020 100%)}
.c-yay{position:absolute;left:540px;top:930px}
.c-yay img{position:absolute;width:150px;height:150px;margin:-75px 0 0 -75px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 3px #FFFDF9,0 0 40px rgba(242,166,90,.35);
  transform:rotate(calc(-75deg + var(--i) * 30deg)) translateY(-400px) rotate(calc(75deg - var(--i) * 30deg))}
.c-lamba{position:absolute;left:50%;bottom:-40px;width:520px;transform:translateX(-50%);-webkit-mask-image:radial-gradient(closest-side,#000 70%,transparent 100%)}
.c-ust{top:120px;bottom:auto;text-align:center;left:90px;width:900px}.c-ust h2{font-size:92px}.c-ust p{margin:18px 0 0;font-size:32px;font-weight:500;color:rgba(255,253,249,.85)}
""".replace('FBG', F + 'bricolage-grotesque')


if __name__ == '__main__':
    os.makedirs(CIKIS, exist_ok=True)
    html = '<!doctype html><meta charset="utf-8"><html lang="tr"><style>%s</style>%s' % (CSS, ''.join('<section class="afis" id="%s">%s</section>' % (k, v) for k, v in AFIS.items()))
    sayfa = os.path.join(CIKIS, '_yon.html'); open(sayfa, 'w', encoding='utf-8').write(html)
    js = os.path.join(CIKIS, '_cek.js')
    open(js, 'w').write("""const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 1 });
  await p.goto('file://%s'); await p.waitForTimeout(900); await p.evaluate(() => document.fonts.ready);
  for (const id of %s) await (await p.$('#' + id)).screenshot({ path: '%s/' + id + '.png' });
  await b.close(); })();""" % (sayfa, json.dumps(list(AFIS)), CIKIS))
    subprocess.run(['node', js], check=True, env=dict(os.environ, NODE_PATH='/opt/node-tools/node_modules'))
    from PIL import Image
    pano = Image.new('RGB', (3 * 540 + 20, 3 * 540 + 20), 'white')
    for n, k in enumerate(AFIS):
        png = os.path.join(CIKIS, k + '.png'); im = Image.open(png).convert('RGB')
        im.save(os.path.join(CIKIS, k + '.jpg'), quality=88, optimize=True, progressive=True); os.remove(png)
        pano.paste(im.resize((540, 540)), ((n % 3) * 550, (n // 3) * 550))
    pano.save(os.path.join(CIKIS, 'yonler.jpg'), quality=85)
    os.remove(js); os.remove(sayfa)
    print('yönler:', ', '.join(AFIS))
