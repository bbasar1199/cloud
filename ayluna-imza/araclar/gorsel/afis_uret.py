# LunaDream galeri afişleri (23 Eki, 2. tur). Çalıştır: /tmp/sr-env/bin/python araclar/gorsel/afis_uret.py → canvas/p-gorsel/afis-1..5.jpg (1080 × 1080)
# Kullanıcı (1. tur krem/serif afişlere): "Satış odaklı değil, yorum görseli yapılmamış, çok sönük kalmış." Önce: "Eskilerinki gibi satış odaklı, USB'ninki gibi."
# 3 yön çizildi (afis_yon.py); eleştirmen A'yı (gece vitrini, USB dili) öne aldı ve şu karmayı seçti: A'nın kalın iki renkli başlığı ve
# halkaları + büyük, parlak lamba; düz kartlı yorum karesi; C'nin disk yayı. Düzeltmeler: lamba karenin ~%35'i; telefonda yazı ≥ 12 px
# (1080'de ≥ 34 px); eğik kart yok, en fazla 3 kart; güven şeridi tek karede ve kart önde ("Kapıda ödeme" yazılmaz: kapıda iade %28,6,
# kartta %0,8; kapıda ₺80 ücret var); sayfadaki başlıklar tekrarlanmaz ("Aileler ne diyor?", "Bu gece hangi masal?").
# Sıra: 1 açılış (Kız, gece, tavanda yansıma) · 2 yorum · 3 diskler · 4 Erkek (Uzay Kaşifi, gerçek etiketli robot) · 5 kutudan ne çıkıyor + güven şeridi.
# Yazı HTML katmanında (Onest + Young Serif), Playwright ile basılır; görsele yapay zekâ yazısı gömülmez. Yorumlar Loox'taki gerçek
# alıcılardan, metin birebir; puan/sayı ve fiyat gömülmez (değişince görsel eskir). Disk dili yalnız "6 masal diski".
# Kaynak fotoğraflar 720–900 px olduğu için açılış ve Erkek kırpmaları yerel Real-ESRGAN ile büyütüldü (canvas/c-gorsel/hd, araclar/gorsel/sr.py).
import os, subprocess, json

KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
P = lambda f: 'file://' + os.path.join(KOK, 'canvas', f)
F = 'file://' + os.path.join(KOK, 'onizleme', 'f') + '/'
CIKIS = os.path.join(KOK, 'canvas', 'p-gorsel')

IK = {
    'disk': '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="2.2"/><path d="M12 3.5v3"/>',
    'bt': '<path d="M7 7l10 10-5 5V2l5 5L7 17"/>',
    'isik': '<circle cx="12" cy="12" r="3.6"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M5.6 18.4l1.6-1.6M16.8 7.2l1.6-1.6"/>',
    'sarj': '<rect x="3" y="7.5" width="15.5" height="9" rx="2.2"/><path d="M21 10.5v3M7 12h4.5M9.2 9.8v4.4"/>',
    'nota': '<path d="M9 17.5V5.5l10-2v12"/><circle cx="6.5" cy="17.5" r="2.6"/><circle cx="16.5" cy="15.5" r="2.6"/>',
    'hediye': '<rect x="3.5" y="9" width="17" height="11" rx="1.5"/><path d="M3.5 13h17M12 9v11M12 9c-1.5-3.5-5.5-4-5.5-1.5S9.5 9 12 9zM12 9c1.5-3.5 5.5-4 5.5-1.5S14.5 9 12 9z"/>',
    'tavan': '<path d="M4 20h16M7 20l5-9 5 9"/><path d="M5 5l2 2M12 3v3M19 5l-2 2"/>',
    'kubbe': '<path d="M5 11a7 7 0 0 1 14 0z"/><path d="M7 11v7h10v-7M12 4V2"/>',
    'kutu': '<path d="M3.5 7.5L12 3.5l8.5 4v9L12 20.5l-8.5-4z"/><path d="M3.5 7.5L12 11.5l8.5-4M12 11.5v9"/>',
    'kargo': '<path d="M2.5 7h11v9h-11zM13.5 10h4l3 3v3h-7"/><circle cx="6.5" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
    'iade': '<path d="M4 12a8 8 0 1 0 2.4-5.7"/><path d="M4 4v4.5h4.5"/>',
    'kart': '<rect x="2.5" y="5.5" width="19" height="13" rx="2"/><path d="M2.5 10h19M6 15h4"/>',
}
TIK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.2 4.2L19 7"/></svg>'
YORUM = {'burak': ('Burak G.', 'Çocuğum çalıştırmadan uyumuyor, uykuya hemen dalıyor.'),
         'handan': ('Handan B.', 'Torunum filmlerini kendisi seçti ve onunla uyumaya başladı.'),
         'abdulkerim': ('Abdülkerim T.', 'Reklamında nasıl ise aynısı, hatta daha iyisi. Çocuklar için mükemmel bir hediye.'),
         'mehmet': ('Mehmet C.', 'Anlatıldığı ve gösterildiği gibi çıktı. Bu kadar iyi olmasını beklemiyordum.'),
         'sevcan': ('Sevcan Z.', '2 tane aldık, gayet sağlam geldi. Paketlenmesi de güzeldi.')}
GUVEN = [('kargo', 'Ücretsiz kargo'), ('iade', '30 gün iade'), ('kart', 'Kartla %5 indirim')]
DISK = ['disk-ay-yildiz', 'disk-okyanus', 'disk-uzay', 'disk-deniz-kizi', 'disk-sato', 'disk-masal']


def ikon(k, renk):
    return '<svg viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % (renk, IK[k])


def ay(renk):
    return ('<svg class="ay" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="%s" stroke-width="1.4"/>'
            '<path d="M12 3A9 9 0 0 1 12 21A5 9 0 0 0 12 3Z" fill="#F2A65A"/></svg>' % renk)


def logo(renk='#FFFDF9'):
    return '<div class="logo">%s<span>Ayluna</span></div>' % ay(renk)


def kart(k):
    ad, s = YORUM[k]
    return '<div class="kart"><p>%s</p><div class="kim"><b>%s</b><span class="tik">%sSatın aldı</span></div></div>' % (s, ad, TIK)


AFIS = [
    ('afis-1', 'LunaDream Kız gece odasında yanıyor, tavanda ay ve yıldızlar: masal anlatan gece lambası',
     '<img class="tam canli" src="%s"><div class="perde sol"></div>' % P('c-gorsel/hd/c-kiz-gece-kare.jpg') + logo() +
     '<div class="bas"><h2>Tavanı masala<em>çeviren lamba</em></h2><p>Diski tak, ışığı kapat.</p>'
     '<div class="ozler">' + ''.join('<div class="oz"><span class="halka">%s</span><b>%s</b><i>%s</i></div>' % (ikon(k, '#FFFDF9'), a, b)
                                     for k, a, b in [('disk', '6 masal', 'diski'), ('nota', 'Bluetooth', 'ninni'), ('isik', '3 kademe', 'ışık')]) + '</div></div>'),
    ('afis-2', 'Alıcı yorumları: Abdülkerim T., Mehmet C. ve Handan B.',
     '<div class="zem-gece"></div><img class="yz-foto" src="%s">' % P('c-gorsel/c-ninni-kiz2.jpg') + logo() +
     '<div class="bas yz"><h2>Reklamındaki<em>gibi mi?</em></h2><p>Alanlar anlatıyor.</p></div>'
     '<div class="kartlar">' + kart('abdulkerim') + kart('mehmet') + kart('handan') + '</div>'),
    ('afis-3', 'Her gece başka bir masal: LunaDream ve 6 masal diski',
     '<div class="zem-disk"></div>' + logo() +
     '<div class="yay">' + ''.join('<img src="%s" style="--i:%d">' % (P('diskler/%s.jpg' % d), i) for i, d in enumerate(DISK)) + '</div>'
     '<img class="disk-lamba" src="%s">' % P('p-gorsel/p-kiz-gece.webp') +
     '<div class="bas orta"><h2>Her gece<em>başka bir masal</em></h2><p>Kutuda 6 masal diski.</p></div>'),
    ('afis-4', 'LunaDream Erkek modeli Uzay Kaşifi gece odasında, duvarda yıldızlar',
     '<img class="tam canli" src="%s"><div class="perde sol"></div>' % P('c-gorsel/hd/c-erkek-gece-kare.jpg') + logo() +
     '<div class="bas"><h2>Uzay Kaşifi<em>erkek modeli</em></h2><p>Aynı 6 masal diski,<br>aynı Bluetooth ninni.</p></div>'),
    ('afis-5', 'Kutudan ne çıkıyor: LunaDream lamba, 6 masal diski, 6 hediye disk ve USB şarj kablosu. Ücretsiz kargo, 30 gün iade, kartla %5 indirim',
     '<div class="zem-krem"></div><div class="krem-yazi">' + logo('#1A2142') + '</div>' +
     '<div class="bas krem"><h2>Kutudan<em>ne çıkıyor?</em></h2><p>İki modelde de kutu aynı.</p></div>'
     '<img class="kutu-lamba" src="%s">' % P('c-gorsel/parca/kiz-tam.webp') +
     '<div class="kutu-sag"><div class="diskler">' + ''.join('<img src="%s">' % P('diskler/%s.jpg' % d) for d in DISK) + '</div>'
     '<ul class="liste">' + ''.join('<li>%s<span>%s</span></li>' % (ikon(k, '#1A2142'), s) for k, s in
                                    [('kubbe', '1 LunaDream lamba'), ('disk', '6 masal diski'), ('hediye', '6 hediye disk'), ('sarj', 'USB şarj kablosu')]) + '</ul></div>'
     '<div class="guven">' + ''.join('<span>%s%s</span>' % (ikon(k, 'currentColor'), t) for k, t in GUVEN) + '</div>'),
]

FONT_CSS = """
@font-face{font-family:"Young Serif";src:url(FYS-latin-400-normal.woff2)}@font-face{font-family:"Young Serif";src:url(FYS-latin-ext-400-normal.woff2);unicode-range:U+0100-024F}
@font-face{font-family:Onest;font-weight:500;src:url(FON-latin-500-normal.woff2)}@font-face{font-family:Onest;font-weight:500;src:url(FON-latin-ext-500-normal.woff2);unicode-range:U+0100-024F}
@font-face{font-family:Onest;font-weight:700;src:url(FON-latin-700-normal.woff2)}@font-face{font-family:Onest;font-weight:700;src:url(FON-latin-ext-700-normal.woff2);unicode-range:U+0100-024F}
""".replace('FYS', F + 'young-serif').replace('FON', F + 'onest')

CSS = FONT_CSS + """
body{margin:0;background:#888}
.afis{position:relative;width:1080px;height:1080px;overflow:hidden;background:#0B1020;color:#FFFDF9;font-family:Onest,sans-serif;margin:0 0 20px}
.logo{position:absolute;z-index:3;left:64px;top:52px;display:flex;align-items:center;gap:14px;font-family:"Young Serif",serif;font-size:42px;letter-spacing:-.01em}
.logo .ay{width:40px;height:40px}
.tam{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.canli{filter:brightness(1.16) saturate(1.25) contrast(1.05)}
.perde.sol{position:absolute;inset:0;background:linear-gradient(100deg,rgba(8,12,30,.9) 0,rgba(8,12,30,.55) 42%,rgba(8,12,30,0) 66%),linear-gradient(180deg,rgba(8,12,30,.55) 0,rgba(8,12,30,0) 30%)}
.bas{position:absolute;z-index:2;left:64px;top:126px;width:800px}
.bas h2{margin:0;font-weight:700;font-size:92px;line-height:.98;letter-spacing:-.035em}
.bas h2 em{display:block;font-style:normal;color:#F2A65A}
.bas p{margin:14px 0 0;font-size:38px;line-height:1.25;font-weight:500;color:rgba(255,253,249,.9)}
.ozler{display:flex;gap:20px;margin-top:22px}
.oz{display:flex;flex-direction:column;align-items:center;width:170px;text-align:center}
.oz .halka{display:grid;place-items:center;width:96px;height:96px;border-radius:50%;background:rgba(11,16,32,.55);box-shadow:inset 0 0 0 3px #F2A65A;margin-bottom:10px}
.oz svg{width:46px;height:46px}.oz b{font-size:36px;font-weight:700;line-height:1.08}.oz i{font-style:normal;font-size:34px;font-weight:500;line-height:1.1;color:rgba(255,253,249,.85)}
/* yorum */
.zem-gece{position:absolute;inset:0;background:radial-gradient(70% 60% at 85% 10%,#2A3474 0,#141B45 45%,#0B1020 100%)}
.yz-foto{position:absolute;right:0;top:0;width:520px;height:600px;object-fit:cover;object-position:50% 35%;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 30%),linear-gradient(0deg,transparent 0,#000 30%);-webkit-mask-composite:source-in}
.bas.yz{width:600px}.bas.yz h2{font-size:88px}
.kartlar{position:absolute;z-index:2;left:64px;right:64px;top:448px;display:grid;gap:18px}
.kart{padding:22px 28px;border-radius:26px;background:#FFFDF9;color:#1A2142;box-shadow:0 18px 40px -18px rgba(0,0,0,.7)}
.kart p{margin:0;font-family:"Young Serif",serif;font-size:36px;line-height:1.2}
.kim{display:flex;align-items:center;justify-content:space-between;margin-top:10px;font-size:30px}
.kim b{font-weight:700}.tik{display:inline-flex;align-items:center;gap:6px;color:#2E7D4F;font-weight:700}.tik svg{width:30px;height:30px}
/* diskler */
.zem-disk{position:absolute;inset:0;background:radial-gradient(55% 50% at 50% 80%,#3A2C5C 0,#1A1E4A 50%,#0B1020 100%)}
.yay{position:absolute;left:540px;top:940px}
.yay img{position:absolute;width:156px;height:156px;margin:-78px 0 0 -78px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 4px #FFFDF9,0 0 44px rgba(242,166,90,.4);
  transform:rotate(calc(-75deg + var(--i) * 30deg)) translateY(-410px) rotate(calc(75deg - var(--i) * 30deg))}
.disk-lamba{position:absolute;left:50%;bottom:-50px;width:560px;transform:translateX(-50%);-webkit-mask-image:radial-gradient(closest-side,#000 72%,transparent 100%)}
.bas.orta{left:40px;right:40px;width:auto;top:120px;text-align:center}
/* kutu */
.zem-krem{position:absolute;inset:0;background:#F1E6D8}
.krem-yazi .logo{color:#1A2142}
.bas.krem{color:#1A2142}.bas.krem h2 em{color:#B4651F}.bas.krem p{color:#3E4466}
.kutu-lamba{position:absolute;left:80px;bottom:156px;height:490px}
.kutu-sag{position:absolute;right:60px;top:372px;width:430px}
.diskler{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.diskler img{width:100%;aspect-ratio:1;border-radius:50%;object-fit:cover;box-shadow:0 0 0 3px #FFFDF9,0 8px 18px -8px rgba(26,33,66,.45)}
.liste{list-style:none;margin:30px 0 0;padding:0;display:grid;gap:12px;color:#1A2142}
.liste li{display:flex;align-items:center;gap:14px;font-size:36px;font-weight:700}
.liste svg{width:42px;height:42px;flex:none}
.guven{position:absolute;z-index:4;left:40px;right:40px;bottom:64px;display:flex;justify-content:space-between;gap:10px;padding:20px 28px;border-radius:999px;background:#1A2142;color:#FFFDF9;font-size:34px;font-weight:700}
.guven span{display:flex;align-items:center;gap:10px}.guven svg{width:40px;height:40px;color:#F2A65A}
"""


if __name__ == '__main__':
    os.makedirs(CIKIS, exist_ok=True)
    html = '<!doctype html><meta charset="utf-8"><html lang="tr"><style>%s</style>%s' % (CSS, ''.join('<section class="afis" id="%s">%s</section>' % (a[0], a[2]) for a in AFIS))
    sayfa = os.path.join(CIKIS, '_afisler.html')
    open(sayfa, 'w', encoding='utf-8').write(html)
    js = os.path.join(CIKIS, '_cek.js')
    open(js, 'w').write("""const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 1 });
  await p.goto('file://%s'); await p.waitForTimeout(900); await p.evaluate(() => document.fonts.ready);
  for (const id of %s) await (await p.$('#' + id)).screenshot({ path: '%s/' + id + '.png' });
  await b.close(); })();""" % (sayfa, json.dumps([a[0] for a in AFIS]), CIKIS))
    subprocess.run(['node', js], check=True, env=dict(os.environ, NODE_PATH='/opt/node-tools/node_modules'))
    from PIL import Image
    for a in AFIS:
        png = os.path.join(CIKIS, a[0] + '.png')
        Image.open(png).convert('RGB').save(os.path.join(CIKIS, a[0] + '.jpg'), quality=88, optimize=True, progressive=True)
        os.remove(png)
    os.remove(js); os.remove(sayfa)
    print('afişler:', ', '.join(a[0] + '.jpg' for a in AFIS))
