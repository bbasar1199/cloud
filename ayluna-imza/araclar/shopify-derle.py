#!/usr/bin/env python3
"""Shopify bölümlerini derler.
araclar/shopify-kaynak/*.liquid şablonlarındaki /*AYLUNA_CSS*/ yerine, onizleme/iskelet.html
içindeki CSS'ten yalnız o bölümde geçen sınıfların kurallarını #ay-{{ section.id }} ile
kapsayarak koyar; çıktıyı shopify/<ad>.txt olarak yazar. Ardından Liquid etiket dengesini ve
{% schema %} JSON'unu denetler.
Kullanım: python3 ayluna-imza/araclar/shopify-derle.py
"""
import re, json, pathlib, sys

KOK = pathlib.Path(__file__).resolve().parent.parent
KAYNAK = KOK / 'araclar' / 'shopify-kaynak'
CIKTI = KOK / 'shopify'
S = '#ay-{{ section.id }}'

html = (KOK / 'onizleme' / 'iskelet.html').read_text(encoding='utf-8')  # iskelet, index'in CSS'ini ve yeni kalıpları içerir
css = html[html.index('<style>') + 7:html.index('</style>')]
css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)


def kurallar(metin):
    """Üst düzey kuralları (seçici, gövde) olarak böl; @blokları iç içe döndür."""
    out, i, n = [], 0, len(metin)
    while i < n:
        j = metin.find('{', i)
        if j < 0:
            break
        sec = metin[i:j].strip()
        d, k = 1, j + 1
        while d and k < n:
            if metin[k] == '{': d += 1
            elif metin[k] == '}': d -= 1
            k += 1
        out.append((sec, metin[j + 1:k - 1].strip()))
        i = k
    return out


TUM = kurallar(css)
FONT = '''@font-face{font-family:"Young Serif";font-weight:400;font-display:swap;src:url({{ 'young-serif-latin-ext-400-normal.woff2' | asset_url }}) format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:"Young Serif";font-weight:400;font-display:swap;src:url({{ 'young-serif-latin-400-normal.woff2' | asset_url }}) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Onest";font-weight:400;font-display:swap;src:url({{ 'onest-latin-ext-400-normal.woff2' | asset_url }}) format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:"Onest";font-weight:400;font-display:swap;src:url({{ 'onest-latin-400-normal.woff2' | asset_url }}) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Onest";font-weight:600;font-display:swap;src:url({{ 'onest-latin-ext-600-normal.woff2' | asset_url }}) format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:"Onest";font-weight:600;font-display:swap;src:url({{ 'onest-latin-600-normal.woff2' | asset_url }}) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}'''
TEMEL = (S + '{--krem:#F6F1E9;--yuzey:#FFFDF9;--cizgi:#E3D8C7;--lac:#1A2142;--gece:#141A36;--gece2:#0C1027;--metin:#1A2142;--soluk:#5C6078;--gSoluk:#B9BED6;--gMetin:#F4EDE3;--amber:#F2A65A;--amber2:#E59A4C;--e:cubic-bezier(.2,.7,.2,1);'
         'color:var(--metin);font-family:"Onest",system-ui,-apple-system,"Segoe UI",sans-serif;font-size:15px;line-height:1.5;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:100%}\n'
         + S + ' *,' + S + ' *::before,' + S + ' *::after{box-sizing:border-box}\n'
         + S + ' img{display:block;max-width:100%}\n' + S + ' a{color:inherit}\n' + S + ' button{font:inherit;color:inherit}\n'
         + S + ' .ay-ic{max-width:430px;margin:0 auto;position:relative;overflow:clip}\n')


def var(ad, metin):
    return re.search(r'(?<![\w-])' + re.escape(ad) + r'(?![\w-])', metin) is not None


def kapsa(kural_listesi, sablon):
    cikti, animler = [], set()
    for sec, govde in kural_listesi:
        if sec.startswith('@font-face') or sec.startswith('@keyframes'):
            continue
        if sec.startswith('@media'):
            if 'prefers-reduced-motion' in sec:
                continue
            ic = kapsa(kurallar(govde), sablon)[0]
            if ic:
                cikti.append(sec + '{' + ic.replace('\n', '') + '}')
            continue
        secler = []
        for parca in sec.split(','):
            parca = parca.strip()
            siniflar = re.findall(r'\.([\w-]+)', parca)
            idler = re.findall(r'#([\w-]+)', parca)
            if not siniflar and not idler:
                continue  # *, html, body, :root, img, a, button: TEMEL karşılar
            if all(var(c, sablon) for c in siniflar) and all(var(x, sablon) for x in idler):
                secler.append(S + ' ' + parca)
        if secler:
            cikti.append(','.join(secler) + '{' + govde + '}')
            for a in re.findall(r'animation:\s*([\w-]+)', govde):
                animler.add(a)
    return '\n'.join(cikti), animler


def keyframes(animler):
    out = []
    for sec, govde in TUM:
        if sec.startswith('@keyframes') and sec.split()[1] in animler:
            out.append(sec + '{' + govde + '}')
    return '\n'.join(out)


def denetle(ad, metin):
    hatalar = []
    gov = re.sub(r'{%-?\s*schema\s*-?%}.*?{%-?\s*endschema\s*-?%}', '', metin, flags=re.S)
    gov = re.sub(r'{%-?\s*comment\s*-?%}.*?{%-?\s*endcomment\s*-?%}', '', gov, flags=re.S)
    # {% liquid %} içindeki satırları etikete çevir
    def liq(m):
        return '\n'.join('{% ' + s.strip() + ' %}' for s in m.group(1).split('\n') if s.strip())
    gov = re.sub(r'{%-?\s*liquid(.*?)-?%}', liq, gov, flags=re.S)
    yigin = []
    for m in re.finditer(r'{%-?\s*(\w+)', gov):
        e = m.group(1)
        if e in ('if', 'unless', 'for', 'case', 'capture', 'form', 'style', 'paginate', 'javascript'):
            yigin.append(e)
        elif e.startswith('end'):
            if not yigin or yigin[-1] != e[3:]:
                hatalar.append('denge bozuk: ' + e + ' (yığın ' + str(yigin[-3:]) + ')')
            else:
                yigin.pop()
    if yigin:
        hatalar.append('kapanmamış: ' + str(yigin))
    kalan = re.sub(r'{{-?[^{}\n]*?-?}}', '', gov)
    if '{{' in kalan:
        hatalar.append('kapanmamış {{ : ' + kalan[kalan.index('{{'):][:40])
    m = re.search(r'{%-?\s*schema\s*-?%}(.*?){%-?\s*endschema\s*-?%}', metin, flags=re.S)
    if not m:
        hatalar.append('schema yok')
    else:
        try:
            sch = json.loads(m.group(1))
            idler = [x.get('id') for x in sch.get('settings', []) if 'id' in x]
            if len(idler) != len(set(idler)):
                hatalar.append('yinelenen ayar id')
            for b in sch.get('blocks', []):
                bi = [x.get('id') for x in b.get('settings', []) if 'id' in x]
                if len(bi) != len(set(bi)):
                    hatalar.append('yinelenen blok ayar id: ' + b.get('type', '?'))
            if len(sch.get('name', '')) > 25:
                hatalar.append('schema name 25 karakteri aşıyor')
            for x in sch.get('settings', []) + [y for b in sch.get('blocks', []) for y in b.get('settings', [])]:
                if 'label' in x and len(x['label']) > 70:
                    hatalar.append('uzun etiket: ' + x['label'][:30])
                if x.get('type') == 'range':
                    if (x['default'] - x['min']) % x['step'] or not (x['min'] <= x['default'] <= x['max']):
                        hatalar.append('range varsayılanı geçersiz: ' + x['id'])
                    if (x['max'] - x['min']) / x['step'] > 101:
                        hatalar.append('range adım sayısı >101: ' + x['id'])
        except Exception as e:
            hatalar.append('schema JSON hatası: ' + str(e))
    return hatalar


def main():
    CIKTI.mkdir(exist_ok=True)
    tum_hata = 0
    for f in sorted(KAYNAK.glob('*.liquid')):
        sablon = f.read_text(encoding='utf-8')
        govde = sablon.split('{% schema %}')[0]
        kapsanan, animler = kapsa(TUM, govde)
        azalt = '@media (prefers-reduced-motion:reduce){' + S + ' *,' + S + ' *::before,' + S + ' *::after{transition-duration:.01ms!important;animation:none!important}}'
        blok = FONT + '\n' + TEMEL + kapsanan + '\n' + keyframes(animler) + '\n' + azalt
        metin = sablon.replace('/*AYLUNA_CSS*/', blok)
        metin = metin.replace('#BOLUM', S)
        h = denetle(f.stem, metin)
        tum_hata += len(h)
        (CIKTI / (f.stem + '.txt')).write_text(metin, encoding='utf-8')
        print(f'{f.stem:26} {len(metin)//1024:3} KB', 'TAMAM' if not h else h)
    sys.exit(1 if tum_hata else 0)


if __name__ == '__main__':
    main()
