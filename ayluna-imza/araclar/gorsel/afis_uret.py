# LunaDream galeri afişleri (22 Eki). Kullanıcı: "Eskilerinki gibi satış odaklı görseller olsun, USB'ninki gibi."
# USB galerisinin dili: logo, iki satırlık büyük başlık (ikinci satır vurgu rengi), kısa alt satır, simgeli 3 özellik, ürün büyük.
# LunaDream'de: Young Serif başlık + Onest, lacivert / krem zemin, tek vurgu amber. Fotoğraflar premium set (canvas/p-gorsel,
# kullanıcı ChatGPT'de üretti); yazı burada HTML ile dizilir (Türkçe karakter bozulmaz), görsele gömülü yapay zekâ yazısı yok.
# Yalnız teyitli bilgi: 6 masal diski (kullanıcı, 22 Eki: "6 + 6 değil, yalnız 6 masal yaz"), iki modelde Bluetooth ninni, 3 parlaklık, şarjlı, kubbe açılır disk üstten girer,
# kutuda lamba + 6 disk + 6 hediye disk + USB şarj kablosu. Pil süresi, boyut, sağlık iddiası yok.
# Çalıştır: python3 araclar/gorsel/afis_uret.py  →  canvas/p-gorsel/afis-1..6.jpg (1080 × 1080)
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
}


def ikon(k, renk):
    return '<svg viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % (renk, IK[k])


def ay(renk):
    return ('<svg class="ay" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="%s" stroke-width="1.4"/>'
            '<path d="M12 3A9 9 0 0 1 12 21A5 9 0 0 0 12 3Z" fill="#F2A65A"/></svg>' % renk)


# Afişler: (dosya, tema, foto, foto yeri (x, y, en), kenar yumuşatma (sol %, üst %) ya da None, başlık 1, başlık 2, alt satır,
#          özellikler [(ikon, satır1, satır2)], ek). Foto yerleri ürün yazının altına binmeyecek biçimde ölçüldü.
AFIS = [
    ('afis-1', 'gece', 'p-gorsel/p-kiz-gece.webp', (470, 470, 610), (16, 14),
     'Masal anlatan', 'gece lambası', 'Diski tak, ışığı kapat; masal tavana yansır.',
     [('disk', '6 masal', 'diski'), ('nota', 'Bluetooth', 'ninni'), ('isik', '3 kademe', 'ışık')], ''),
    ('afis-2', 'krem', 'p-gorsel/p-diskler.webp', (270, 330, 810), (6, 8),
     'Her gece', 'yeni bir masal', 'Kutuda 6 masal diski,<br>masalı o seçsin.',
     [], ''),
    ('afis-3', 'sicak', 'p-gorsel/p-elde.webp', (330, 380, 760), (14, 12),
     'Telefondan ninni,', 'lambadan çalsın', 'Bluetooth ile ninni, masal ya da müzik.',
     [('bt', 'Bluetooth', 'bağlantı'), ('nota', 'Ninni ve', 'masal'), ('sarj', 'Şarjlı,', 'kablosuz')], ''),
    ('afis-4', 'krem', 'p-gorsel/p-erkek-gunduz.webp', (300, 330, 790), (10, 10),
     'Uzay Kaşifi', 'erkek modeli', 'Aynı masal diskleri, aynı ninni.',
     [('disk', '6 masal', 'diski'), ('nota', 'Bluetooth', 'ninni'), ('sarj', 'Şarjlı,', 'kablosuz')], ''),
    ('afis-5', 'gece', 'p-gorsel/p-erkek-gece.webp', (-140, -140, 1220), None,
     'Işık kapanınca', 'masal başlar', 'Seçtiğin disk tavana ve duvara yansır.',
     [('tavan', 'Tavana', 'yansıtır'), ('isik', '3 kademe', 'ışık'), ('disk', '6 masal', 'diski')], 'alt'),
    ('afis-6', 'krem', 'c-gorsel/parca/kiz-tam.webp', (90, 300, 0), None,
     'Kutudan', 'ne çıkıyor?', 'İki modelde de kutu aynı.',
     [], 'kutu'),
]

TEMA = {
    'gece': {'zem': '#0B1020', 'yazi': '#FFFDF9', 'vurgu': '#F2A65A', 'alt': 'rgba(255,253,249,.78)', 'halka': 'rgba(255,253,249,.32)'},
    'krem': {'zem': '#F1E6D8', 'yazi': '#1A2142', 'vurgu': '#B4651F', 'alt': '#4A5070', 'halka': 'rgba(26,33,66,.28)'},
    'sicak': {'zem': '#C9A27F', 'yazi': '#1A2142', 'vurgu': '#FFFDF9', 'alt': '#2E3352', 'halka': 'rgba(26,33,66,.34)'},
}
DISKLER = ['disk-ay-yildiz', 'disk-okyanus', 'disk-uzay', 'disk-deniz-kizi', 'disk-sato', 'disk-masal']


def afis_html(a):
    ad, tema, foto, (x, y, w), maske, b1, b2, alt, oz, ek = a
    t = TEMA[tema]
    m = ('linear-gradient(to right,transparent 0,#000 %d%%),linear-gradient(to bottom,transparent 0,#000 %d%%);-webkit-mask-composite:source-in' % maske) if maske else 'none'
    if ek == 'kutu':
        govde = ('<img class="kutu-lamba" src="%s">' % P(foto) +
                 '<div class="kutu-sag"><div class="diskler">' + ''.join('<img src="%s">' % P('diskler/%s.jpg' % d) for d in DISKLER) + '</div>'
                 '<ul class="liste">' + ''.join('<li>%s<span>%s</span></li>' % (ikon(k, t['yazi']), s) for k, s in
                 [('kubbe', '1 LunaDream lamba'), ('disk', '6 masal diski'), ('hediye', '6 hediye disk'), ('sarj', 'USB şarj kablosu')]) + '</ul></div>')
    else:
        govde = '<img class="foto" src="%s" style="left:%dpx;top:%dpx;width:%dpx;-webkit-mask-image:%s">' % (P(foto), x, y, w, m)
    perde = '<div class="perde %s"></div>' % ek if ek == 'alt' else ''
    ozler = ('<div class="ozler">' + ''.join('<div class="oz"><span class="halka">%s</span><b>%s</b><i>%s</i></div>' % (ikon(k, t['yazi']), s1, s2)
             for k, s1, s2 in oz) + '</div>') if oz else ''
    metin_sinif = 'metin alt' if ek == 'alt' else 'metin'
    return ('<section class="afis %s" id="%s" style="--zem:%s;--yazi:%s;--vurgu:%s;--alt:%s;--halka:%s">' % (tema, ad, t['zem'], t['yazi'], t['vurgu'], t['alt'], t['halka']) +
            govde + perde + '<div class="logo">%s<span>Ayluna</span></div>' % ay(t['yazi']) +
            '<div class="%s"><h2>%s<em>%s</em></h2><p>%s</p>%s</div></section>' % (metin_sinif, b1, b2, alt, ozler))


CSS = """
@font-face{font-family:"Young Serif";src:url(FYS-latin-400-normal.woff2)}@font-face{font-family:"Young Serif";src:url(FYS-latin-ext-400-normal.woff2);unicode-range:U+0100-024F}
@font-face{font-family:Onest;font-weight:500;src:url(FON-latin-500-normal.woff2)}@font-face{font-family:Onest;font-weight:500;src:url(FON-latin-ext-500-normal.woff2);unicode-range:U+0100-024F}
@font-face{font-family:Onest;font-weight:700;src:url(FON-latin-700-normal.woff2)}@font-face{font-family:Onest;font-weight:700;src:url(FON-latin-ext-700-normal.woff2);unicode-range:U+0100-024F}
body{margin:0;background:#888}
.afis{position:relative;width:1080px;height:1080px;overflow:hidden;background:var(--zem);color:var(--yazi);font-family:Onest,sans-serif;margin:0 0 20px}
.foto{position:absolute;display:block;height:auto}
.perde.alt{position:absolute;inset:0;background:radial-gradient(70% 60% at 100% 100%,rgba(8,11,24,.9),rgba(8,11,24,.55) 55%,rgba(8,11,24,0))}
.logo{position:absolute;left:64px;top:52px;display:flex;align-items:center;gap:14px;font-family:"Young Serif",serif;font-size:42px;letter-spacing:-.01em}
.logo .ay{width:40px;height:40px}
.metin{position:absolute;left:64px;top:148px;width:700px}
.metin.alt{top:auto;bottom:52px;left:auto;right:48px;width:470px;text-align:left}
.metin.alt h2{font-size:64px}.metin.alt p{font-size:30px}.metin.alt .ozler{gap:10px}.metin.alt .oz{width:150px}
.metin h2{margin:0;font-family:"Young Serif",serif;font-weight:400;font-size:84px;line-height:1.02;letter-spacing:-.02em}
#afis-3 .metin h2{font-size:76px}
.metin h2 em{display:block;font-style:normal;color:var(--vurgu)}
.metin p{margin:20px 0 0;font-size:34px;line-height:1.3;font-weight:500;color:var(--alt);max-width:480px}
.ozler{display:flex;gap:16px;margin-top:30px}
.oz{display:flex;flex-direction:column;align-items:center;width:140px;text-align:center}
.oz .halka{display:grid;place-items:center;width:96px;height:96px;border-radius:50%;box-shadow:inset 0 0 0 2.5px var(--halka);margin-bottom:10px}
.oz svg{width:44px;height:44px}
.oz b{font-size:28px;font-weight:700;line-height:1.1}
.oz i{font-style:normal;font-size:26px;font-weight:500;line-height:1.15;color:var(--alt)}
.kutu-lamba{position:absolute;left:70px;bottom:40px;height:640px}
.kutu-sag{position:absolute;right:56px;top:390px;width:480px}
.diskler{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.diskler img{width:100%;aspect-ratio:1;border-radius:50%;object-fit:cover;box-shadow:0 0 0 3px #FFFDF9,0 8px 18px -8px rgba(26,33,66,.45)}
.liste{list-style:none;margin:34px 0 0;padding:0;display:grid;gap:14px}
.liste li{display:flex;align-items:center;gap:14px;font-size:33px;font-weight:700}
.liste svg{width:40px;height:40px;flex:none}
""".replace('FYS', F + 'young-serif').replace('FON', F + 'onest')


if __name__ == '__main__':
    os.makedirs(CIKIS, exist_ok=True)
    html = '<!doctype html><meta charset="utf-8"><style>%s</style>%s' % (CSS, ''.join(afis_html(a) for a in AFIS))
    sayfa = os.path.join(CIKIS, '_afisler.html')
    open(sayfa, 'w', encoding='utf-8').write(html)
    js = os.path.join(CIKIS, '_cek.js')
    open(js, 'w').write("""const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 1 });
  await p.goto('file://%s'); await p.waitForTimeout(800); await p.evaluate(() => document.fonts.ready);
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
