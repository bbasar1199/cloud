# Ayluna · tema bölümleri (28 Eki). Kullanıcı: "sectionları tek tek bölümler kısmında görüp düzenleyebileceğim hale getir",
# "loox ekliyorum ama yorum kısmına koyamıyorum", "videolar açılmıyor", "görsel olarak senin içine koyduklarını çekiyor".
# Bir panonun gövdesi (.pg'nin çocukları) parçalara bölünür; her parça bir Shopify bölümü olur. Bölüm parçasını
# <template class="ay-parca"> içinde taşır, ayluna.js hepsini tek bileşenle çizer. Panonun kendi şablonunda (ürünün ya da
# ana sayfanın şablonu) yazılar ve görseller bölüm ayarı olur; her bölüm uygulama bloğu (Loox vb.) alır.
import re, json, html as H

VOID = {'img', 'br', 'input', 'meta', 'link', 'source', 'hr', 'wbr', 'area', 'col', 'embed', 'track', 'param'}
ETIKET = re.compile(r'<!--.*?-->|<(/?)([a-zA-Z][\w:-]*)((?:[^>"\']|"[^"]*"|\'[^\']*\')*)>', re.S)
SINIF = re.compile(r'\bclass="([^"]*)"')
KIMLIK = re.compile(r'\bid="([^"]*)"')


def ust_cocuklar(govde):
    """'<div class="pg" …>…</div>' → (açılış etiketi, [(tür, sınıflar, kimlik, html)]). Yorumlar '!' türüyle ayrı öğe."""
    m = re.search(r'<div class="pg"[^>]*>', govde)
    acilis, i, derin, bas, ogeler = m.group(0), m.end(), 1, None, []
    for t in ETIKET.finditer(govde, i):
        if t.group(0).startswith('<!--'):
            if derin == 1: ogeler.append(('!', '', '', t.group(0)))
            continue
        kapa, ad, ozn = t.group(1), t.group(2).lower(), t.group(3)
        tek = ad in VOID or ozn.rstrip().endswith('/')
        if not kapa:
            if derin == 1:
                bas = t.start()
                if tek:
                    ogeler.append((ad, (SINIF.search(ozn) or [None, ''])[1], (KIMLIK.search(ozn) or [None, ''])[1], t.group(0))); bas = None
                    continue
                ozb = ozn
            if not tek: derin += 1
        else:
            derin -= 1
            if derin == 1 and bas is not None:
                ogeler.append((ad_bas(govde, bas), (SINIF.search(ozb) or [None, ''])[1], (KIMLIK.search(ozb) or [None, ''])[1], govde[bas:t.end()])); bas = None
            if derin == 0: break
    return acilis, ogeler


def ad_bas(govde, i):
    return re.match(r'<([a-zA-Z][\w:-]*)', govde[i:]).group(1).lower()


def duz(s):
    s = re.sub(r'\{\{[^}]*\}\}', '', s)
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)
    return re.sub(r'\s+', ' ', H.unescape(s)).strip()


def kisalt(s, n=25):
    s = s.rstrip('.')
    return s if len(s) <= n else s[:n - 1].rstrip() + '…'


def grupla(ogeler):
    """Üst çocukları bölümlere toplar: [(tür, etiket, html)]."""
    gruplar, bekleyen = [], ''
    for tur, cls, kid, h in ogeler:
        if tur == '!': bekleyen += h + '\n'; continue
        c = cls.split()
        yeni = None
        if 'duyuru' in c: yeni = ('ust', 'Üst kısım')
        elif tur == 'header' or 'u-serit' in c:
            if gruplar and gruplar[-1][0] == 'ust': gruplar[-1][2] += bekleyen + h; bekleyen = ''; continue
            yeni = ('ust', 'Üst kısım')
        elif 'urun-ust' in c: yeni = ('satin', 'Galeri ve satın alma')
        elif tur == 'footer': yeni = ('alt', 'Alt bilgi')
        elif 'yapis' in c: yeni = ('yapis', 'Yapışkan satın al çubuğu')
        elif kid == 'videolar': yeni = ('video', 'Videolar')
        elif tur == 'section' or 'bb' in c:
            yeni = ('bolum', '')
        if yeni is None and gruplar:
            gruplar[-1][2] += bekleyen + h; bekleyen = ''; continue
        if yeni is None: yeni = ('bolum', '')
        gruplar.append([yeni[0], yeni[1], bekleyen + h]); bekleyen = ''
    if bekleyen and gruplar: gruplar[-1][2] += bekleyen
    sonuc = []
    for k, (tur, et, h) in enumerate(gruplar, 1):
        if not et:
            b = re.search(r'<h[12]\b[^>]*>(.*?)</h[12]>', h, re.S)
            et = duz(b.group(1)) if b and duz(b.group(1)) else ''
            if not et and 'slayt' in h[:200]: et = 'Ana görsel'
            if not et and 'id="mesajlar"' in h: et = 'Sizden gelen mesajlar'
            if not et and 'class="otuz"' in h: et = '30 gün iade'
            if not et and 'data-ay-yorum' in h: et = 'Loox yorumları'
            if not et:
                b = re.search(r'class="bas-y"[^>]*>(.*?)</p>', h, re.S)
                et = duz(b.group(1)) if b else ''
            if not et:
                b = re.match(r'\s*<!--\s*([^:(.,<]+)', h)
                et = b.group(1).strip() if b else ''
            if not et: et = 'Bölüm %d' % k
        sonuc.append((tur, kisalt(et), h))
    return sonuc


# Bölüm ayarı olacak yazılar: başlık, paragraf, liste, kısa etiket. {{…}} içeren, harfsiz ya da tek harfli yazı ayar olmaz.
METIN = re.compile(r'(<(h1|h2|h3|h4|p|li|figcaption|b|strong|small|span|em|button|a|label|summary|u)\b[^>]*>)([^<]+)(?=<)')
GORSEL = re.compile(r'(<img\b[^>]*?\bsrc=")(/_blob/[0-9a-f]{32})(")')
ATLA = re.compile(r'<(svg|style|script)\b.*?</\1>', re.S)


def ayarla(h, en_cok_yazi=40, en_cok_gorsel=20):
    """Parça html'i → (Liquid parçaları [(ham_mi, metin)], ayarlar). Aynı yazı tek ayara bağlanır (masaüstü kopyası, gece kopyası)."""
    yasak = [(m.start(), m.end()) for m in ATLA.finditer(h)]
    def yasakta(i): return any(a <= i < b for a, b in yasak)
    bul = []
    for m in METIN.finditer(h):
        ham = m.group(3)
        if yasakta(m.start(3)) or '{{' in ham or '}}' in ham or '{%' in ham: continue
        deger = re.sub(r'\s+', ' ', H.unescape(ham)).strip()
        if len(re.findall(r'[A-Za-zÇĞİÖŞÜçğıöşü]', deger)) < 2: continue
        bul.append((m.start(3), m.end(3), 'm', deger, ham))
    for m in GORSEL.finditer(h):
        if yasakta(m.start(2)): continue
        alt = re.search(r'\balt="([^"]*)"', m.group(0) + h[m.end():m.end() + 300].split('>')[0])
        bul.append((m.start(2), m.end(2), 'g', m.group(2), alt.group(1) if alt and '{{' not in alt.group(1) else ''))
    bul.sort()
    parca, ayar, kim, i, ny, ng = [], [], {}, 0, 0, 0
    for bas, son, tur, deger, ek in bul:
        if tur == 'm':
            if deger not in kim:
                if ny >= en_cok_yazi: continue
                ny += 1; kim[deger] = 'm%d' % ny
                tip = 'text' if len(deger) <= 90 else 'textarea'
                ayar.append({'type': tip, 'id': kim[deger], 'label': kisalt('Yazı: ' + deger, 60), 'default': deger})
            sol = re.match(r'\s*', ek).group(0); sag = ek[len(ek.rstrip()):]
            parca += [(True, h[i:bas] + sol), (False, '{{ section.settings.%s | escape }}' % kim[deger]), (True, sag)]
        else:
            anahtar = 'img:' + deger
            if anahtar not in kim:
                if ng >= en_cok_gorsel: continue
                ng += 1; kim[anahtar] = 'g%d' % ng
                ayar.append({'type': 'image_picker', 'id': kim[anahtar], 'label': kisalt('Görsel %d%s' % (ng, (': ' + ek) if ek else ''), 60)})
            g = kim[anahtar]
            parca += [(True, h[i:bas]), (False, '{%%- if section.settings.%s -%%}{{ section.settings.%s | image_url: width: 1600 }}{%%- else -%%}%s{%%- endif -%%}' % (g, g, deger))]
        i = son
    parca.append((True, h[i:]))
    return parca, ayar


def liquid(parca):
    out = []
    for ham, t in parca:
        if not t: continue
        out.append('{% raw %}' + t + '{% endraw %}' if ham else t)
    return ''.join(out)


UYGULAMA = ('{%- if section.blocks.size > 0 -%}<div class="ay-uyg">{%- for block in section.blocks -%}{%- case block.type -%}{%- when \'@app\' -%}'
            '<div {{ block.shopify_attributes }}>{% render block %}</div>{%- endcase -%}{%- endfor -%}</div>{%- endif -%}\n')
# Satın alma bölümündeki uygulama blokları (Kaching vb.) tasarımdaki satın al düğmesinin altındaki yuvaya taşınır (ayluna.js)
UYGULAMA_GIZLI = ('<div class="ay-uygulama-bloklari" hidden>{%- for block in section.blocks -%}{%- case block.type -%}{%- when \'@app\' -%}'
                  '<div class="ay-uygulama" {{ block.shopify_attributes }}>{% render block %}</div>{%- endcase -%}{%- endfor -%}</div>\n')
URUN_FORMU = '''{%- form 'product', product, data-ay-urun-formu: '', data-ay-shopify: '', hidden: 'hidden', class: 'ay-urun-formu' -%}
  <input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id }}">
  <input type="hidden" name="quantity" value="1">
{%- endform -%}
<div class="ay-arka" aria-hidden="true"><kaching-bundle product-id="{{ product.id }}"></kaching-bundle></div>
'''
OYNA = '<svg viewBox="0 0 24 24"><path d="M8 5.5v13l11-6.5z"></path></svg>'


def parca_html(acilis, h, ayarli):
    """Bölümün şablon parçası (Liquid): .pg sarmalı + parça; ayarlıysa yazı/görsel ayarları."""
    if ayarli:
        p, ayar = ayarla(h)
    else:
        p, ayar = [(True, h)], []
    return '<template class="ay-parca">' + liquid([(True, acilis)] + p + [(True, '</div>')]) + '</template>', ayar


# Yorum bölümü (tasarımda "[Loox …]" yer tutucusu olan parça): Loox bloğu eklenmeden sayfada görünmez; düzenleyicide nasıl
# ekleneceği yazar. Blok eklenince başlık ve Loox yorumları bu bölümde, tasarımdaki yerinde durur.
YORUM_IPUCU = ('{%- if request.design_mode and section.blocks.size == 0 -%}<p class="ay-vid-not">Loox yorumları burada görünür: soldan bu bölümde '
               '"Blok ekle → Uygulamalar → Loox" seç. Blok eklenmezse bu bölüm sayfada görünmez.</p>{%- endif -%}\n')


def yorum_sar(h, icerik):
    if 'class="yer"' not in h: return icerik
    return '{%- if section.blocks.size > 0 -%}\n' + icerik + '{%- endif -%}\n' + YORUM_IPUCU


def kok(tur, urun):
    return '<div class="ay-kok" data-sayfa="%s" data-urun="%s"></div>\n' % (tur, urun)


def varliklar(kod, fontlar):
    return "{{ '%s.css' | asset_url | stylesheet_tag }}\n%s\n" % (kod, fontlar)


def betik(kod):
    return "<script src=\"{{ '%s.js' | asset_url }}\" defer></script>\n" % kod


def sema(ad, ayar, bloklar=None):
    s = {'name': ad, 'class': 'ay-bolum', 'settings': ayar, 'blocks': (bloklar or []) + [{'type': '@app'}]}
    return '\n{% schema %}\n' + json.dumps(s, ensure_ascii=False, indent=2) + '\n{% endschema %}\n'


def video_bolumu(kod, fontlar, acilis, h):
    """LunaDream videoları: bloklarla seçilen Shopify videoları (canlıda gerçek oynatma). Video yoksa bölüm görünmez."""
    b = re.search(r'<h2\b[^>]*>(.*?)</h2>', h, re.S)
    baslik = duz(b.group(1)) + ('?' if b and '?' in b.group(1) and not duz(b.group(1)).endswith('?') else '') if b else 'Videolar'
    govde = ('{%- comment -%} Ayluna · videolar. Blok ekle → Video: Shopify\'a (İçerik → Dosyalar) yüklenen video seçilir. {%- endcomment -%}\n'
             + varliklar(kod, fontlar)
             + '{%- assign ay_vid = 0 -%}{%- for block in section.blocks -%}{%- if block.type == \'video\' and block.settings.video != blank -%}{%- assign ay_vid = ay_vid | plus: 1 -%}{%- endif -%}{%- endfor -%}\n'
             + '{%- if ay_vid > 0 -%}\n<div class="ay-statik">' + acilis + '<section class="bolum" id="videolar">\n'
             + '  <div class="px"><h2 class="h2">{{ section.settings.baslik | escape }}</h2></div>\n'
             + '  <div class="noscroll" style="display: flex; gap: 10px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-left: 16px; padding: 16px 16px 0">\n'
             + '  {%- for block in section.blocks -%}{%- if block.type == \'video\' and block.settings.video != blank -%}\n'
             + '    <button class="vid ay-vid" type="button" aria-label="{{ block.settings.baslik | escape }}: videoyu oynat" {{ block.shopify_attributes }}>'
             + '{{ block.settings.video | video_tag: muted: true, loop: true, playsinline: true, preload: \'metadata\', image_size: \'600x\' }}'
             + '<span class="vid-oyna" aria-hidden="true">' + OYNA + '</span><span class="vid-alt"><b>{{ block.settings.baslik | escape }}</b><span>{{ block.settings.alt | escape }}</span></span></button>\n'
             + '  {%- endif -%}{%- endfor -%}\n  <span aria-hidden="true" style="flex: 0 0 6px"></span></div>\n</section></div></div>\n'
             + '{%- elsif request.design_mode -%}\n<p class="ay-vid-not">Videolar: soldan "Blok ekle → Video" ile Shopify\'a yüklediğin videoları seç. Video seçilmezse bu bölüm sayfada görünmez.</p>\n{%- endif -%}\n'
             + UYGULAMA)
    ayar = [{'type': 'text', 'id': 'baslik', 'label': 'Başlık', 'default': baslik}]
    blok = [{'type': 'video', 'name': 'Video', 'settings': [
        {'type': 'video', 'id': 'video', 'label': 'Video'},
        {'type': 'text', 'id': 'baslik', 'label': 'Başlık', 'default': 'Müşteri videosu'},
        {'type': 'text', 'id': 'alt', 'label': 'Alt yazı', 'default': ''}]}]
    return govde + sema('Videolar', ayar, blok)


def pano_bolumleri(kod, pano, parcala, tur, urun):
    """Kendi şablonu olan pano (özel ürün, ana sayfa): [(dosya_adi, etiket, liquid)]. kod: varlık adı (ay-galaxyusb)."""
    fontlar, css, govde, js = parcala(pano)
    acilis, ogeler = ust_cocuklar(govde)
    cikti = []
    for n, (gt, et, h) in enumerate(grupla(ogeler), 1):
        dosya = '%s-%02d' % (kod, n)
        if gt == 'video':
            cikti.append((dosya, et, video_bolumu(kod, fontlar, acilis, h))); continue
        tpl, ayar = parca_html(acilis, h, True)
        govdeL = ('{%- comment -%} Ayluna · ' + pano + ' · ' + et + '. araclar/tema/tema_uret.py üretir; elle düzenlenmez (yazı ve görseller bölüm ayarından). {%- endcomment -%}\n'
                  + varliklar(kod, fontlar) + yorum_sar(h, tpl + '\n' + kok(tur, urun)))
        if gt == 'satin':
            govdeL += URUN_FORMU + UYGULAMA_GIZLI
        else:
            govdeL += UYGULAMA
        govdeL += betik(kod)
        cikti.append((dosya, et, govdeL + sema(et, ayar)))
    return cikti, css, js


def varlik_css(css, zemin):
    return css + '\nbody{--ay-zemin:' + zemin + '}\n'


def varlik_js(js, pano):
    return ('/* Ayluna · ' + pano + ' bileşeni (araclar/tema/tema_uret.py). Her bölüm bu dosyayı yükler; bileşen bir kez kurulur. */\n'
            '(window.AYLUNA_KUYRUK = window.AYLUNA_KUYRUK || []).push(function () {\n' + js + '\nAyluna.baslat(Component);\n});\n')


def sade_bolumleri(sade, parcala, ad, ozel, genel):
    """Varsayılan ürün şablonu (product.json): sade panolu ürünler aynı 6 bölümü paylaşır; her bölüm ürüne göre kendi panosunun
    parçasını çizer (ayarsız: şablon ortak). Kendi şablonuna geçmemiş özel ürün ilk bölümde tek parça panosuyla, panosuz ürün
    sade Shopify düzeniyle açılır. sade: [(handle, pano)], ozel: {handle: pano}. → ([(dosya, etiket, liquid)], {pano: (css, js)})"""
    parcalar, varlik = {}, {}
    for h, pano in sade:
        fontlar, css, govde, js = parcala(pano)
        acilis, ogeler = ust_cocuklar(govde)
        parcalar[h] = (pano, fontlar, acilis, grupla(ogeler)); varlik[pano] = (css, js)
    ornek = parcalar[sade[0][0]][3]
    turler = [t for t, _, _ in ornek]
    for h, (_, _, _, g) in parcalar.items():
        assert [t for t, _, _ in g] == turler, 'sade panoların bölüm sırası aynı olmalı: ' + h
    etiket = [et for _, et, _ in parcalar['lamba' if 'lamba' in parcalar else sade[0][0]][3]]
    cikti = []
    for n, tur in enumerate(turler):
        l = ('{%- comment -%} Ayluna · ürün sayfası (varsayılan şablon) · ' + etiket[n] + '. Her ürün kendi panosunun bu parçasını çizer;\n'
             '  araclar/tema/tema_uret.py üretir, elle düzenlenmez. {%- endcomment -%}\n{%- case product.handle -%}\n')
        for h, (pano, fontlar, acilis, g) in parcalar.items():
            kod = ad(pano)
            tpl, _ = parca_html(acilis, g[n][2], False)
            l += ("{%- when '" + h + "' -%}\n" + varliklar(kod, fontlar) + yorum_sar(g[n][2], tpl + '\n' + kok('urun', h))
                  + ((URUN_FORMU + UYGULAMA_GIZLI) if tur == 'satin' else UYGULAMA) + betik(kod))
        if n == 0:
            l += ("{%- when " + ', '.join("'%s'" % h for h in ozel) + " -%}\n"
                  "  {%- comment -%} Özel ürün henüz kendi şablonunda değilse (KURULUM): tek parça panosu {%- endcomment -%}\n"
                  "  {%- case product.handle -%}\n" + ''.join("    {%%- when '%s' -%%}{%% render '%s' %%}\n" % (h, ad(p)) for h, p in ozel.items())
                  + "  {%- endcase -%}\n" + URUN_FORMU + UYGULAMA_GIZLI
                  + '{%- else -%}\n' + genel)
        l += '{%- endcase -%}\n'
        cikti.append(('ay-sade-%02d' % (n + 1), etiket[n], l + sema(etiket[n], [])))
    return cikti, varlik


def sablon_json(dosyalar):
    kim = ['b%02d' % (k + 1) for k in range(len(dosyalar))]
    return json.dumps({'sections': {k: {'type': d} for k, d in zip(kim, dosyalar)}, 'order': kim}, ensure_ascii=False, indent=2) + '\n'


UYGULAMA_BOLUMU = '''{%- comment -%} Ayluna · uygulama bloğu. Şablonun istediğin yerine eklenir (Bölüm ekle → Uygulama bloğu); içine Loox yorumları gibi
  uygulama blokları konur. Sayfa sütununda, sayfanın zemininde durur. {%- endcomment -%}
<div class="ay-uyg">{%- for block in section.blocks -%}{%- case block.type -%}{%- when '@app' -%}<div {{ block.shopify_attributes }}>{% render block %}</div>{%- endcase -%}{%- endfor -%}</div>

{% schema %}
{
  "name": "Uygulama bloğu",
  "class": "ay-bolum",
  "settings": [],
  "blocks": [{ "type": "@app" }],
  "presets": [{ "name": "Uygulama bloğu" }]
}
{% endschema %}
'''
