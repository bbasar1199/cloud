# Ayluna · Shopify yükleme kuralları denetimi (28 Eki). 1.0.35'te dört ayarın varsayılanı boş yazı ("default": "") idi; Shopify
# LunaDream bölümünü reddetti, ürün şablonu o bölüme bağlı olduğu için bütün ürün sayfaları 404 verdi. Theme Check bunu yakalamadı.
# tema_uret.py zip'ten önce çağırır; kural bozulursa zip oluşmaz.
import os, re, json

VARSAYILANSIZ = {'video', 'image_picker', 'product', 'collection', 'video_url', 'page', 'blog', 'article', 'link_list', 'product_list', 'collection_list', 'metaobject'}
BILGI = {'header', 'paragraph'}


def _ayarlar(yer, ayarlar, hata):
    gor = set()
    for s in ayarlar or []:
        t = s.get('type')
        if t in BILGI:
            if not s.get('content'): hata.append('%s: %s içeriksiz' % (yer, t))
            continue
        i = s.get('id')
        if not i: hata.append('%s: kimliksiz ayar (%s)' % (yer, t)); continue
        if i in gor: hata.append('%s: aynı kimlik iki kez: %s' % (yer, i))
        gor.add(i)
        if not s.get('label'): hata.append('%s.%s: etiket yok' % (yer, i))
        if 'default' in s:
            d = s['default']
            if t in VARSAYILANSIZ: hata.append('%s.%s: %s ayarı varsayılan almaz' % (yer, i, t))
            elif isinstance(d, str) and not d.strip(): hata.append('%s.%s: boş varsayılan ("default": "")' % (yer, i))
            elif t == 'checkbox' and not isinstance(d, bool): hata.append('%s.%s: checkbox varsayılanı true/false olmalı' % (yer, i))
        if t in ('select', 'radio') and s.get('default') not in [o.get('value') for o in s.get('options', [])]:
            hata.append('%s.%s: varsayılan seçeneklerde yok' % (yer, i))
    return gor


def denetle(tema):
    hata, semalar = [], {}
    bol = os.path.join(tema, 'sections')
    for f in sorted(os.listdir(bol)):
        if not f.endswith('.liquid'): continue
        ad = f[:-7]; metin = open(os.path.join(bol, f), encoding='utf-8').read()
        m = re.search(r'{%-?\s*schema\s*-?%}(.*?){%-?\s*endschema\s*-?%}', metin, re.S)
        if not m: continue
        try: s = json.loads(m.group(1))
        except ValueError as e: hata.append('%s: şema JSON hatalı (%s)' % (ad, e)); continue
        semalar[ad] = s
        if len(s.get('name', '')) > 25: hata.append('%s: bölüm adı 25 karakteri geçiyor' % ad)
        _ayarlar(ad, s.get('settings'), hata)
        turler = set()
        for b in s.get('blocks', []):
            bt = b.get('type')
            if bt in turler: hata.append('%s: blok türü iki kez: %s' % (ad, bt))
            turler.add(bt)
            if bt.startswith('@'): continue
            if not b.get('name'): hata.append('%s.%s: blok adı yok' % (ad, bt))
            elif len(b['name']) > 25: hata.append('%s.%s: blok adı 25 karakteri geçiyor' % (ad, bt))
            _ayarlar('%s.%s' % (ad, bt), b.get('settings'), hata)
        for p in s.get('presets', []):
            for b in p.get('blocks', []):
                if b.get('type') not in turler: hata.append('%s: hazır ayarda olmayan blok %s' % (ad, b.get('type')))
    # Şablonlar: bölüm türü var mı, bloklar şemada var mı, ayar kimlikleri tanımlı mı
    sab = os.path.join(tema, 'templates')
    for f in sorted(os.listdir(sab)):
        if not f.endswith('.json'): continue
        try: j = json.load(open(os.path.join(sab, f), encoding='utf-8'))
        except ValueError as e: hata.append('%s: JSON hatalı (%s)' % (f, e)); continue
        if len(j.get('sections', {})) > 25: hata.append('%s: 25\'ten çok bölüm' % f)
        for k, b in j.get('sections', {}).items():
            s = semalar.get(b.get('type'))
            if s is None: hata.append('%s: %s bölüm türü yok (%s)' % (f, k, b.get('type'))); continue
            bs = dict((x['type'], x) for x in s.get('blocks', []))
            if len(b.get('blocks', {})) > s.get('max_blocks', 50): hata.append('%s.%s: blok sayısı sınırı aşıyor' % (f, k))
            gecerli = set(x.get('id') for x in s.get('settings', []))
            for ai in (b.get('settings') or {}):
                if ai not in gecerli: hata.append('%s.%s: tanımsız ayar %s' % (f, k, ai))
            for bk, bb in (b.get('blocks') or {}).items():
                if bb.get('type') not in bs and not any(t.startswith('@app') for t in bs): hata.append('%s.%s: blok türü yok %s' % (f, k, bb.get('type'))); continue
                bg = set(x.get('id') for x in bs.get(bb.get('type'), {}).get('settings', []))
                for ai in (bb.get('settings') or {}):
                    if ai not in bg: hata.append('%s.%s.%s: tanımsız ayar %s' % (f, k, bk, ai))
    return hata


if __name__ == '__main__':
    import sys
    h = denetle(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..', '..', 'tema'))
    print('\n'.join(h) if h else 'şema denetimi TAMAM')
    sys.exit(1 if h else 0)
