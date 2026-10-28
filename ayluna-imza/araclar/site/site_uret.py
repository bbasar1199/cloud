# Ayluna · tüm sitenin çalışan önizlemesi (index ve bütün sayfalar). Çalıştır: python3 araclar/site/site_uret.py
# Kullanıcı (18 Eki): "Tüm iskeleti index olarak gönder; önce eksiklerini kontrol et, tüm eksik kısımları düzelt; sepet vesaire her kısım tam çalışsın."
# Tuval sayfaları (.dc.html) olduğu gibi kullanılır; ayluna.js onları çalıştırır (şablon + DOM yaması) ve siteyi bağlar:
# sepet (localStorage), sepet çekmecesi, kapıda ödeme formu, menü, arama, ödeme önizlemesi, sipariş alındı.
# Çıktı: ayluna-imza/site/ (index.html + sayfalar + g/ görseller + ayluna.js/css + veri.js). Görseller 1200px'e küçültülür.
import os, re, sys, io, json, shutil
from PIL import Image
KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TU = os.path.join(KOK, 'araclar', 'tuval-uret'); sys.path.insert(0, TU)
CANVAS = os.path.join(KOK, 'canvas'); MAG = os.path.join(CANVAS, 'magaza')
CIKTI = os.path.join(KOK, 'site'); KAYNAK = os.path.dirname(os.path.abspath(__file__))
import anasayfa as A
import sayfalar as SY
import sepet as SP
import ozel_yon as O

# Yerel görsel eşlemesi (blob kimliği → canvas/magaza'ya göre yol), önizleme aracıyla aynı
BLOB = {'e02351b3be4a1c555c5d760d0bbda723': 'm-kiz', '0033dfea6282c5bc479c385213661c00': 'm-erkek', '211acb76d908e8ed6d4f5fcddc987893': 'ld0', '652e1893a0ae33a24ee0e3d53edab757': 'ld1',
        'ec0a99ef7b8839a12ab7e6aa4282f7da': 'ld2', '35f6b0090fd4e65b22f48d111fe61905': 'ld3', 'a08890007843d79d94bfffc397a3d0ac': 'ld4', 'd4efe7e83c74524ece75e962161f7fff': 'ld5',
        'fd0a28089115b8aa3de9bcb92a65a8e2': 'ld6', '3ddd8b8b95f040d436d5d0ea350924b8': 'ld7', '98db755893dbcebe192c69e73ae5afff': 'ld8'}
BLOB.update(json.load(open(os.path.join(KOK, 'araclar', 'blob-yerel.json'))))


def gorsel(p, en, q):
    """Görseli en'e küçültüp (bayt, uzantı, mime) döndürür. Saydam görsel (arka planı temizlenmiş kesim) WebP olarak saydam
    kalır; JPEG'e çevrilince saydamlık siyah oluyordu (kullanıcı, 19 Eki: "seçim kısmında kız erkekte arkasında siyahlık var").
    Saydam olmayanlar JPEG."""
    im = Image.open(p)
    if im.mode == 'P' and 'transparency' in im.info: im = im.convert('RGBA')
    saydam = im.mode in ('RGBA', 'LA') and im.getchannel('A').getextrema()[0] < 255
    im = im.convert('RGBA' if saydam else 'RGB')
    if im.width > en: im = im.resize((en, round(im.height * en / im.width)), Image.LANCZOS)
    b = io.BytesIO()
    if saydam:
        im.save(b, 'WEBP', quality=q + 6, method=6); return b.getvalue(), 'webp', 'image/webp'
    im.save(b, 'JPEG', quality=q, optimize=True, progressive=True); return b.getvalue(), 'jpg', 'image/jpeg'


def blob_yolu(i):
    v = BLOB.get(i)
    if not v: return None
    p = os.path.normpath(os.path.join(MAG, v if re.search(r'\.\w+$', v) else v + '.jpg'))
    return p if os.path.exists(p) else None


# Ürün verisi: mağaza adı/fiyatı (anasayfa.URUN), paketler ve seçenekler (urun-icerik.json + özel sayfalar)
ICERIK = dict((x['handle'], x) for x in json.load(open(os.path.join(KOK, 'ogrenme', 'urun-icerik.json'))))
BA = json.load(open(os.path.join(CANVAS, 'ana', 'bloblar.json')))
ADLAR = {'lunadream-gece-lambasi': ['LunaDream Gece Lambası', 'LunaDream'], 'galayx-usb-projektor': ['Galaxy USB Projektör', 'Galaxy USB'],
         'lamba': ['Ayluna AyFeneri', 'AyFeneri'], 'ayluna-galaksi-night-projektor': ['Ayluna Galaksi Night Projektör', 'Galaksi Night Projektör', 'Galaksi Night'],
         'galaksiambiyanisigi': ['Galaksi Ambiyans Işığı'], 'yilbasi-agaci-projektor-lamba': ['Yılbaşı Projektör', 'Yılbaşı Ağacı Projektör Lamba', 'Yılbaşı Ağacı Projektör', 'Yılbaşı Ağacı'],
         'ayluna-cocuk-gece-feneri': ['Ayluna Çocuk Gece Feneri', 'Çocuk Gece Feneri'],
         'ask-saati': ['Ayluna Kum Saati Lamba', 'Kum Saati Lamba', 'Kum Saati'], 'yildiz-isigi-nemlendirici': ['Yıldız Işığı Nemlendirici'],
         'astronot-oda-nemlendirici-aroma-difuzor': ['Astronot Oda Nemlendirici', 'Astronot Nemlendirici'], 'sunset-lamba': ['Sunset Lamba'],
         'ayluna-retro-mini-pikap': ['Ayluna Retro Mini Pikap', 'Retro Mini Pikap'], 'egitici-akilli-cizim-tahtasi': ['Eğitici Akıllı Çizim Tahtası', 'Çizim Tahtası'],
         'aroma-terapi-nemlendirici': ['Aroma Terapi Nemlendirici'], 'dokunmatik-ambiyans-lamba': ['Dokunmatik Ambiyans Lamba'], 'lunadream-gece-lambasi-v2': ['LunaDream Gece Lambası V2']}
OZEL_PAKET = {'lunadream-gece-lambasi': [(1, 1699.99, 1999), (2, 2749.99, None)], 'galayx-usb-projektor': [(1, 1599, 1999), (2, 2399.99, None)],
              'lamba': [(1, O.URUN['af']['P1'], O.URUN['af']['C1']), (2, O.URUN['af']['P2'], None)],
              'ayluna-galaksi-night-projektor': [(1, O.URUN['gn']['P1'], O.URUN['gn']['C1']), (2, O.URUN['gn']['P2'], None)]}
OZEL_SAYFA = {'lunadream-gece-lambasi': 'LunaDreamE', 'galayx-usb-projektor': 'GalaxyUSB', 'lamba': 'AyFeneri', 'ayluna-galaksi-night-projektor': 'GalaksiNight',
              'yilbasi-agaci-projektor-lamba': 'YilbasiAgaci'}  # 28 Eki: yılbaşı ağacı imza sayfası (yilbasi_sayfa.py)


def veri():
    U = {}
    for h, ad, p, c, var in A.URUN:
        ic = ICERIK.get(h, {})
        if h in OZEL_PAKET: pk = [dict(n=n, p=f, c=e) for n, f, e in OZEL_PAKET[h]]
        else: pk = [dict(n=b['adet'], p=b['fiyat'], c=b.get('eski') if b.get('eski') and b['eski'] > b['fiyat'] else None) for b in (ic.get('paket') or [])]
        sec = ((ic.get('secenek') or [{}])[0] or {}).get('degerler', []) if ic.get('secenek') else []
        U[h] = dict(ad=ad, p=p, c=c if c and c > p else None, stok=bool(var), img='/_blob/' + BA['u-%s.jpg' % h], kat=SY.KAT[h], adlar=ADLAR[h], paket=pk, secenek=sec)
    return dict(urun=U, sira=[h for h, *_ in A.URUN], ekler=[dict(k=e['k'], n=e['n'], p=e['p'], h=e['h'], img='/_blob/' + e['img']) for e in SP.EKLER])


SAYFALAR = [('index.html', 'Ayluna-Anasayfa', 'ana', None, 'Ayluna · Gece lambaları ve galaksi projektörleri')]
SAYFALAR += [(h + '.html', OZEL_SAYFA.get(h, 'U-' + h), 'urun', h, ad + ' · Ayluna') for h, ad, *_ in A.URUN]
SAYFALAR += [('tum-urunler.html', 'Koleksiyon', 'koleksiyon', None, 'Tüm ürünler · Ayluna'), ('sepet.html', 'Sepet', 'sepet', None, 'Sepetin · Ayluna'),
             ('odeme.html', 'Odeme', 'odeme', None, 'Ödeme · Ayluna'), ('siparis-alindi.html', 'SiparisAlindi', 'tamam', None, 'Siparişin alındı · Ayluna'),
             ('iletisim.html', 'Iletisim', 'iletisim', None, 'İletişim · Ayluna'), ('kargo-takip.html', 'KargoTakip', 'kargo-takip', None, 'Kargo takip · Ayluna'),
             ('iade.html', 'Politika-Iade', 'politika', None, 'İade ve değişim · Ayluna'), ('kargo.html', 'Politika-Kargo', 'politika', None, 'Kargo ve teslimat · Ayluna'),
             ('kvkk.html', 'Politika-KVKK', 'politika', None, 'Gizlilik ve KVKK · Ayluna'), ('mesafeli-satis.html', 'Politika-Mesafeli', 'politika', None, 'Mesafeli satış sözleşmesi · Ayluna'),
             ('on-bilgilendirme.html', 'Politika-OnBilgi', 'politika', None, 'Ön bilgilendirme formu · Ayluna'), ('hizmet-sartlari.html', 'Politika-Hizmet', 'politika', None, 'Hizmet şartları · Ayluna'),
             ('arama.html', 'Arama', 'arama', None, 'Ara · Ayluna'), ('404.html', 'Sayfa404', '404', None, 'Sayfa bulunamadı · Ayluna'), ('hesap.html', 'Hesap', 'hesap', None, 'Hesabın · Ayluna')]

SABLON = '''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#1A2142">
<meta name="description" content="Ayluna: duvara ay yansıtan gece lambaları, galaksi projektörleri ve nemlendiriciler. Ücretsiz kargo, 30 gün iade, kartla %%5 indirim.">
<title>%(title)s</title>
<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%%3E%%3Ccircle cx='12' cy='12' r='11' fill='%%231A2142'/%%3E%%3Cpath d='M12 4a8 8 0 1 0 0 16a6 6 0 0 1 0-16Z' fill='%%23F2A65A'/%%3E%%3C/svg%%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Young+Serif&amp;family=Onest:wght@400;500;600;700&amp;display=swap">
%(fontlar)s
<style>body{--ay-zemin:%(zemin)s}
%(css)s</style>
<link rel="stylesheet" href="ayluna.css">
</head>
<body>
<template id="T">%(govde)s</template>
<div id="kok" class="ay-kok" data-sayfa="%(tur)s" data-urun="%(urun)s"></div>
<noscript><p style="padding:24px;font-family:sans-serif">Ayluna sayfası için JavaScript gerekiyor.</p></noscript>
<script src="veri.js"></script>
<script src="ayluna.js"></script>
<script>
%(js)s
Ayluna.baslat(Component);
</script>
</body>
</html>
'''


def parcala(ad):
    s = open(os.path.join(CANVAS, ad + '.dc.html'), encoding='utf-8').read()
    helmet = s.split('<helmet>')[1].split('</helmet>')[0]
    fontlar = '\n'.join(re.findall(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>', helmet))
    css = re.search(r'<style>(.*?)</style>', helmet, re.S).group(1)
    govde = s.split('</helmet>')[1].split('</x-dc>')[0]
    # Başlıklardaki telefon satır kırılımı masaüstünde gizlenir (ayluna.css); kelimeler birleşmesin diye <br> önüne boşluk
    govde = re.sub(r'(<h[12][^>]*>)(.*?)(</h[12]>)', lambda m: m.group(1) + re.sub(r'(?<=[^\s>])<br>', ' <br>', m.group(2)) + m.group(3), govde, flags=re.S)
    js = re.search(r'data-dc-script[^>]*>(.*?)</script>', s, re.S).group(1)
    return fontlar, css, govde, js


def main():
    if os.path.exists(CIKTI): shutil.rmtree(CIKTI)
    os.makedirs(os.path.join(CIKTI, 'g'))
    V = veri()
    kullanilan, eksik, sayfa_blob = set(), set(), {}
    for dosya, kaynak, tur, urun, title in SAYFALAR:
        fontlar, css, govde, js = parcala(kaynak)
        ids = set(re.findall(r'(?<![0-9a-f])([0-9a-f]{32})(?![0-9a-f])', govde + js + css))
        for i in ids:
            if i in BLOB: (kullanilan if blob_yolu(i) else eksik).add(i)
        z = re.search(r'--zemin:(#[0-9A-Fa-f]{6})', css)
        html = SABLON % dict(title=title, fontlar=fontlar, zemin=z.group(1) if z else '#F6F1E9', css=css, tur=tur, urun=urun or '', govde=govde, js=js)
        open(os.path.join(CIKTI, dosya), 'w', encoding='utf-8').write(html)
        sayfa_blob[dosya] = len(ids)
    for u in V['urun'].values():
        kullanilan.add(u['img'][7:])
    for e in V['ekler']:
        kullanilan.add(e['img'][7:])
    # Görseller: 1200px'e küçült; saydam olan WebP (saydam kalır), diğerleri JPEG
    yol = {}
    for i in sorted(kullanilan):
        p = blob_yolu(i)
        if not p: eksik.add(i); continue
        try:
            bayt, uz, _ = gorsel(p, 1200, 82); hedef = 'g/%s.%s' % (i, uz)
            open(os.path.join(CIKTI, hedef), 'wb').write(bayt)
        except Exception as e:
            print('görsel hatası', i, p, e); continue
        yol[i] = hedef
    # Ürün verisindeki görseller yerel yol
    for u in V['urun'].values(): u['img'] = yol.get(u['img'][7:], u['img'])
    for e in V['ekler']: e['img'] = yol.get(e['img'][7:], e['img'])
    V['blob'] = yol
    open(os.path.join(CIKTI, 'veri.js'), 'w', encoding='utf-8').write('window.AYLUNA_VERI = ' + json.dumps(V, ensure_ascii=False) + ';\n')
    for f in ('ayluna.js', 'ayluna.css'):
        shutil.copy(os.path.join(KAYNAK, f), os.path.join(CIKTI, f))
    # Artifact yayını için ana sayfanın parça sürümü: yayın iskeleti doctype/head/body'yi kendisi ekler
    tam = open(os.path.join(CIKTI, 'index.html'), encoding='utf-8').read()
    bas = tam.split('<head>')[1].split('</head>')[0]
    bas = re.sub(r'<meta charset="utf-8">\n|<meta name="viewport"[^>]*>\n', '', bas).replace(re.search(r'<title>.*?</title>', bas).group(0), '<title>Ayluna Mağazası</title>')
    govde = tam.split('<body>')[1].split('</body>')[0]
    os.makedirs(os.path.join(KOK, 'site-yayin'), exist_ok=True)
    open(os.path.join(KOK, 'site-yayin', 'index.html'), 'w', encoding='utf-8').write(bas.strip() + '\n' + govde.strip() + '\n')
    toplam = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(CIKTI) for f in fs)
    print('sayfa:', len(SAYFALAR), '· görsel:', len(yol), '· eksik görsel:', sorted(eksik) or 'yok', '· boyut: %.1f MB' % (toplam / 1e6))


TEK_SABLON = '''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#1A2142">
<title>Ayluna Mağazası</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
%(fontlar)s
<style>%(ortak_css)s</style>
<style id="sayfa-css"></style>
</head>
<body>
%(sablonlar)s
<div id="kok" class="ay-kok"></div>
<script>window.AYLUNA_TEK = true;</script>
<script>%(veri)s</script>
<script>%(runtime)s</script>
<script>
window.AYLUNA_SAYFALAR = {};
%(sayfalar)s
Ayluna.baslatTek();
</script>
</body>
</html>
'''


def tek():
    # Tek dosya: bütün sayfalar <template>, CSS'leri sayfaya girince takılır, görseller data: URI (800px)
    import base64, io
    V = veri()
    fontlar, sablonlar, sayfalar, ids = set(), [], [], set()
    for dosya, kaynak, tur, urun, title in SAYFALAR:
        f, css, govde, js = parcala(kaynak)
        for l in f.split('\n'):
            if l.strip(): fontlar.add(l.strip())
        ad = dosya[:-5]
        for i in re.findall(r'(?<![0-9a-f])([0-9a-f]{32})(?![0-9a-f])', govde + js + css):
            if blob_yolu(i): ids.add(i)
        z = re.search(r'--zemin:(#[0-9A-Fa-f]{6})', css)
        sablonlar.append('<template id="T-%s">%s</template>' % (ad, govde))
        sayfalar.append('AYLUNA_SAYFALAR[%s] = { tur: %s, urun: %s, title: %s, zemin: %s, css: %s, js: function () {\n%s\nreturn Component; } };'
                        % (json.dumps(ad), json.dumps(tur), json.dumps(urun or ''), json.dumps(title), json.dumps(z.group(1) if z else '#F6F1E9'), json.dumps(css, ensure_ascii=False), js))
    for u in V['urun'].values(): ids.add(u['img'][7:])
    for e in V['ekler']: ids.add(e['img'][7:])
    blob = {}
    for i in sorted(ids):
        p = blob_yolu(i)
        if not p: continue
        bayt, _, mime = gorsel(p, 800, 72)
        blob[i] = 'data:%s;base64,' % mime + base64.b64encode(bayt).decode()
    V['blob'] = blob
    css = open(os.path.join(KAYNAK, 'ayluna.css'), encoding='utf-8').read() + '\nbody{background:var(--ay-zemin,#F6F1E9)}'
    fontlar = sorted(fontlar) + ['<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Young+Serif&amp;family=Onest:wght@400;500;600;700&amp;display=swap">']
    html = TEK_SABLON % dict(fontlar='\n'.join(fontlar), ortak_css=css, sablonlar='\n'.join(sablonlar), veri='window.AYLUNA_VERI = ' + json.dumps(V, ensure_ascii=False) + ';',
                             runtime=open(os.path.join(KAYNAK, 'ayluna.js'), encoding='utf-8').read(), sayfalar='\n'.join(sayfalar))
    os.makedirs(os.path.join(KOK, 'site-tek'), exist_ok=True)
    yol = os.path.join(KOK, 'site-tek', 'index.html')
    open(yol, 'w', encoding='utf-8').write(html)
    print('tek dosya:', yol, '· %.1f MB' % (os.path.getsize(yol) / 1e6), '· görsel:', len(blob))


if __name__ == '__main__':
    main()
    tek()
