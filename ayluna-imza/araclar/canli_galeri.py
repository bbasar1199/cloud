# Ürün galerileri Shopify'daki gibi (kullanıcı, 19 Eki: "fotoğraf kısmını Shopify'daki ile aynı şekle getir").
# Kaynak: canlı mağaza /products.json (ogrenme/canli-urunler.json). Sıra Shopify'daki sıra; görseller kare.
# Çıkarılanlar (mevzuat ve iade riski): uydurma yorum/satış rozeti, sağlık ya da güvenlik iddiası, kutuda olmayan şey ya da başka cihaz.
# Teyitsiz teknik ifade taşıyanlar (5K, katman sayısı vb.) kullanıcının kendi afişi olduğu için kalır; KONTROL listesinde.
# Çıktı: ogrenme/galeri-canli.json  {handle: [{"id": blob, "not": "..."}]}. Çalıştır: python3 araclar/canli_galeri.py
import json, os
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(KOK, *p)
CANLI = {p['handle']: p for p in json.load(open(J('ogrenme', 'canli-urunler.json')))['products']}
ICERIK = {u['handle']: u for u in json.load(open(J('ogrenme', 'urun-icerik.json')))}
BLOB = json.load(open(J('canvas', 'urunler', 'bloblar.json')))
yol = lambda u: u.split('?')[0]
# İçerik dosyasındaki numara (urunler/<handle>/NN.jpg) ile çıkarılanlar
CIKAR = {
    'egitici-akilli-cizim-tahtasi': {'07': 'uydurma yorum', '08': 'uydurma yorum'},
    'dokunmatik-ambiyans-lamba': {'07': 'göz koruma iddiası'},
    'sunset-lamba': {'05': 'uydurma "2.400+ satış" rozeti'},
    'ayluna-cocuk-gece-feneri': {'07': 'başka cihaz', '08': 'uyku iddiası', '09': 'uydurma yorum'},
    'ayluna-galaksi-night-projektor': {'08': 'uydurma yorum'},
    'aroma-terapi-nemlendirici': {'07': 'uydurma yorum'},
    'galaksiambiyanisigi': {'06': 'uydurma yorum', '07': 'uydurma yorum'},
    'lunadream-gece-lambasi-v2': {'08': 'uydurma yorum', '09': 'uydurma yorum'},
    'yildiz-isigi-nemlendirici': {'04': 'cilt iddiası', '06': 'araç içinde kullanım (güvenlik)', '07': 'uydurma yorum (Elif K.)'},
    'lamba': {'08': 'uydurma yorum', '09': 'uydurma yorum'},
}
# Özel sayfalar: canlı sıra numarasıyla (1'den)
LD = ['211acb76d908e8ed6d4f5fcddc987893', '652e1893a0ae33a24ee0e3d53edab757', 'ec0a99ef7b8839a12ab7e6aa4282f7da', '35f6b0090fd4e65b22f48d111fe61905',
      'a08890007843d79d94bfffc397a3d0ac', 'd4efe7e83c74524ece75e962161f7fff', 'fd0a28089115b8aa3de9bcb92a65a8e2', '3ddd8b8b95f040d436d5d0ea350924b8', '98db755893dbcebe192c69e73ae5afff']
OZEL = {
    'lunadream-gece-lambasi': ([(i + 1, b) for i, b in enumerate(LD)], {3: 'kutuda olmayan diskler (unicorn, 2025)', 4: 'uydurma yorum (Elif K.)', 7: 'uydurma yorum kolajı'}),
    'galayx-usb-projektor': ([(1, '153dd8a1b6a1359501859ced79c0a784'), (2, None), (3, '08ad55fd9db11d3f53cd191d9866f207'), (4, 'be86b4a93cb896b0ad69042a2e915e68'), (5, None)],
                             {2: 'kutuda olmayan eski diskler', 5: 'uydurma yorum kartı'}),
}
KONTROL = {'egitici-akilli-cizim-tahtasi': {'06': 'gelişim iddiaları'}, 'ayluna-galaksi-night-projektor': {'06': '153.748 yıldız, 5K', '07': '12 katmanlı lens (başka afişte 7)'},
           'yildiz-isigi-nemlendirici': {'05': 'teknik değerler çelişkili (2,8 / 2,3 L)'}, 'ask-saati': {'04': 'Sevgililer Günü afişi, "Subat" yazımı'},
           'galayx-usb-projektor': {1: '5K HD', 3: '7 katmanlı lens, 5K HD'}}

def main():
    cikti, eksik, rapor = {}, [], []
    for h, p in CANLI.items():
        liste = []
        if h in OZEL:
            sira, cik = OZEL[h]
            for n, b in sira:
                if n in cik: rapor.append('%s #%d çıkarıldı: %s' % (h, n, cik[n])); continue
                liste.append({'id': b, 'not': KONTROL.get(h, {}).get(n, '')})
        else:
            gor = {yol(g['url']): g for g in ICERIK[h]['gorseller']}
            for n, im in enumerate(p['images'], 1):
                g = gor.get(yol(im['src']))
                if not g: eksik.append('%s #%d içerikte yok' % (h, n)); continue
                no = g['dosya'].split('/')[-1][:2]
                if no in CIKAR.get(h, {}): rapor.append('%s #%d çıkarıldı: %s' % (h, n, CIKAR[h][no])); continue
                liste.append({'id': BLOB.get(g['dosya']) or g['dosya'], 'not': KONTROL.get(h, {}).get(no, '')})
        cikti[h] = liste
    json.dump(cikti, open(J('ogrenme', 'galeri-canli.json'), 'w'), ensure_ascii=False, indent=1)
    yukle = sorted({x['id'] for v in cikti.values() for x in v if '/' in (x['id'] or '')})
    print('\n'.join(rapor)); print('eksik:', eksik); print('yüklenecek:', yukle)
    print({h: len(v) for h, v in cikti.items()})

if __name__ == '__main__':
    main()
