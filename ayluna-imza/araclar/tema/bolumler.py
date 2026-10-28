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


def ayarla(h, en_cok_yazi=40, en_cok_gorsel=20, kaynak='section'):
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
            parca += [(True, h[i:bas] + sol), (False, '{{ %s.settings.%s | escape }}' % (kaynak, kim[deger])), (True, sag)]
        else:
            anahtar = 'img:' + deger
            if anahtar not in kim:
                if ng >= en_cok_gorsel: continue
                ng += 1; kim[anahtar] = 'g%d' % ng
                ayar.append({'type': 'image_picker', 'id': kim[anahtar], 'label': kisalt('Görsel %d%s' % (ng, (': ' + ek) if ek else ''), 60)})
            g = kim[anahtar]
            parca += [(True, h[i:bas]), (False, '{%%- if %s.settings.%s -%%}{{ %s.settings.%s | image_url: width: 1600 }}{%%- else -%%}%s{%%- endif -%%}' % (kaynak, g, kaynak, g, deger))]
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


def pano_bolumleri(kod, pano, parcala, tur, urun, harita=None):
    """Parça başına bir bölüm (ana sayfa): [(dosya_adi, etiket, liquid)]. kod: varlık adı (ay-ana). harita: {'b01': [(blob, etiket)]}."""
    fontlar, css, govde, js = parcala(pano)
    acilis, ogeler = ust_cocuklar(govde)
    cikti = []
    for n, (gt, et, h) in enumerate(grupla(ogeler), 1):
        dosya = '%s-%02d' % (kod, n)
        tpl, ayar = parca_html(acilis, h, True)
        statik = set(m.group(2)[7:] for m in GORSEL.finditer(h))
        d_ayar, d_esle = gorsel_secici([x for x in (harita or {}).get('b%02d' % n) or [] if x[0] not in statik], len([a for a in ayar if a['type'] == 'image_picker']), 'section')
        ayar = ayar + d_ayar; tpl = d_esle + tpl
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


# --- Ürün sayfaları: varsayılan şablonda, şablon ataması gerekmez (28 Eki, kullanıcı: "hala sectionlar çalışmıyor … tüm sectionlar
# erişilebilir değil"; dört ürünün şablonu atanmamıştı, sayfalar tek parça açılıyordu). Her özel ürünün bir "sayfa" bölümü var, tasarımın
# parçaları o bölümün blokları: düzenleyicide tek tek görünür, yazı/görsel ayarı bloğun içinde, sürüklenir, gizlenir, silinse "Blok ekle"
# ile geri gelir. Bölüm yalnız kendi ürününde çizilir. Uygulama blokları (Kaching, Loox vb.) blokların arasına konabilir.
# Loox (kullanıcı: "looxu yüklüyorum direkt senin yaptığın yorum kısmında olması gerekiyor"): yorum parçasına Loox'un kendi kutusu
# (#looxReviews) gömülü; Loox yerleştirmesi açıkken yorumlar kendiliğinden orada çıkar, blok eklemek gerekmez.
LOOX = ('<div class="ay-uyg ay-loox"><div id="looxReviews" data-product-id="{{ %s.id }}" class="loox-reviews-default">'
        '{{ %s.metafields.loox.reviews }}</div></div>\n')


def yorum_parcasi(gruplar):
    """Loox kutusunun gireceği parçanın sırası: tasarımda "[Loox …]" yer tutucusu olan parça; yoksa "… ne diyor?" başlıklı parça."""
    for k, (_, _, h) in enumerate(gruplar):
        if 'class="yer"' in h: return k
    for k, (_, et, _) in enumerate(gruplar):
        if 'ne diyor' in et: return k
    return -1


# Yorum bloğu ayarları (28 Eki, kullanıcı: "hem Loox görünüyor hem senin koydukların görünüyor"): tasarımdaki yorum kartları, puan ve
# müşteri fotoğrafları (y-tas, y-puan; Loox'taki yorumların kopyası) varsayılan kapalı, müşteri mesajları (y-msj) açık. Bloğun ayarından değişir.
YORUM_AYAR = [
    {'type': 'header', 'content': 'Bu bölümde görünenler'},
    {'type': 'checkbox', 'id': 'mesajlar', 'label': 'Müşteri mesajları (WhatsApp ekran görüntüleri)', 'default': True},
    {'type': 'checkbox', 'id': 'tasarim_yorum', 'label': 'Tasarımdaki yorum kartları, puan ve müşteri fotoğrafları', 'default': False,
     'info': 'Loox yorumları bu bölümde kendiliğinden görünür. Bunu açarsan yorumlar iki kez görünür; Loox kapalıysa aç.'}]
# Videolar bölümü (28 Eki, kullanıcı: "hala videolar görünmüyor, orayı section olarak ekle, ben içeriden seçebileyim görselleri de
# videoları da; bu özellik hep olmalı"): tasarımın "Işık kapanınca ne oluyor?" şeridi bağımsız, Liquid ile çizilen bir bölüm. Her kart bir
# blok: video (İçerik → Dosyalar ya da yükle), kapak görseli, başlık, alt yazı. Kart ekle/sil/sırala düzenleyiciden. Video yoksa kapak
# görseli görünür (oynat işareti yok). Bölüm istenen sayfaya eklenir; "Yalnız bu üründe" seçilirse yalnız o ürünün sayfasında çizilir.
# Görünüş tasarımdaki sınıflarla (.pg > section.bolum > .noscroll > .vid); ayluna.js ekrandaki videoyu sessiz döndürür, dokununca sesli tam ekran.
VIDEO_BOLUMU = """{%- comment -%} Ayluna · Videolar bölümü (araclar/tema/bolumler.py üretir). Kartlar blok: video, kapak görseli, başlık. {%- endcomment -%}
{%- liquid
  assign ay_goster = true
  if section.settings.urun
    if product == nil or product.handle != section.settings.urun.handle
      assign ay_goster = false
    endif
  endif
  assign ay_tasarim = section.settings.tasarim_gorsel | split: ','
  assign ay_kart = 0
  for block in section.blocks
    if block.settings.video or block.settings.gorsel
      assign ay_kart = ay_kart | plus: 1
    elsif section.settings.tasarim and ay_tasarim[forloop.index0].size > 0
      assign ay_kart = ay_kart | plus: 1
    endif
  endfor
-%}
{%- if ay_goster -%}
{%- if ay_kart > 0 or request.design_mode -%}
<div class="pg ay-vb"><section class="bolum" id="videolar">
  {%- if section.settings.baslik != nil and section.settings.baslik != '' -%}<div class="px"><h2 class="h2">{{ section.settings.baslik | escape }}<span class="n">?</span></h2></div>{%- endif -%}
  {%- if section.settings.alt != nil and section.settings.alt != '' -%}<div class="px"><p class="ay-vb-alt">{{ section.settings.alt | escape }}</p></div>{%- endif -%}
  <div class="noscroll ay-vb-serit">
    {%- for block in section.blocks -%}
      {%- liquid
        assign ay_v = block.settings.video
        assign ay_g = block.settings.gorsel
        assign ay_d = ''
        if ay_g == nil and section.settings.tasarim and ay_tasarim[forloop.index0].size > 0
          assign ay_d = ay_tasarim[forloop.index0] | strip | asset_url
        endif
      -%}
      {%- if ay_v -%}
        <button class="vid ay-vid" type="button" aria-label="{{ block.settings.baslik | default: 'Video' | escape }}: videoyu oynat" {{ block.shopify_attributes }}>
          <video muted loop playsinline preload="metadata" poster="{% if ay_g %}{{ ay_g | image_url: width: 600 }}{% elsif ay_v.preview_image %}{{ ay_v.preview_image | image_url: width: 600 }}{% endif %}">
            {%- for s in ay_v.sources -%}{%- if s.format == 'mp4' -%}<source src="{{ s.url }}" type="{{ s.mime_type }}">{%- endif -%}{%- endfor -%}
          </video>
          <span class="vid-oyna" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l11-6.5z"></path></svg></span>
          <span class="vid-alt"><b>{{ block.settings.baslik | escape }}</b><span>{{ block.settings.alt | escape }}</span></span>
        </button>
      {%- elsif ay_g or ay_d != '' -%}
        <div class="vid ay-vb-foto" {{ block.shopify_attributes }}>
          {%- if ay_g -%}{{ ay_g | image_url: width: 700 | image_tag: loading: 'lazy', alt: block.settings.baslik }}{%- else -%}<img src="{{ ay_d }}" alt="{{ block.settings.baslik | escape }}" loading="lazy" width="600" height="1067">{%- endif -%}
          <span class="vid-alt"><b>{{ block.settings.baslik | escape }}</b><span>{{ block.settings.alt | escape }}</span></span>
        </div>
      {%- elsif request.design_mode -%}
        <div class="vid ay-vb-bos" {{ block.shopify_attributes }}><span class="vid-alt"><b>{{ block.settings.baslik | default: 'Yeni kart' | escape }}</b><span>Video ya da görsel seç</span></span></div>
      {%- endif -%}
    {%- endfor -%}
    <span aria-hidden="true" style="flex: 0 0 6px"></span>
  </div>
  {%- if request.design_mode -%}<p class="ay-vid-not">Videolar: soldan bu bölümdeki bir karta tıkla, sağda Video ve Kapak görseli seç. "Kart ekle" ile yeni video eklenir. Videosu ve görseli olmayan kart müşteriye görünmez.</p>{%- endif -%}
</section></div>
{%- endif -%}
{%- endif -%}
"""
VIDEO_SEMA = {
    'name': 'Videolar', 'class': 'ay-bolum ay-vb-bolum',
    'settings': [
        {'type': 'text', 'id': 'baslik', 'label': 'Başlık', 'default': 'Işık kapanınca ne oluyor'},
        {'type': 'text', 'id': 'alt', 'label': 'Alt yazı'},
        {'type': 'product', 'id': 'urun', 'label': 'Yalnız bu ürünün sayfasında göster', 'info': 'Boş bırakırsan bölüm eklendiği her sayfada görünür.'},
        {'type': 'checkbox', 'id': 'tasarim', 'label': 'Görsel seçilmeyen kartlarda tasarım fotoğrafı', 'default': False},
        {'type': 'text', 'id': 'tasarim_gorsel', 'label': 'Tasarım fotoğrafları (tema dosyası, virgülle)',
         'info': 'Temanın kendi fotoğrafları; elle değiştirmen gerekmez. Kapak görseli seçince onun yerine geçer.'}],
    'blocks': [{'type': 'video', 'name': 'Video', 'settings': [
        {'type': 'video', 'id': 'video', 'label': 'Video', 'info': 'Dosya seç ya da yükle. Ekrandayken sessiz döner, dokununca sesli açılır.'},
        {'type': 'image_picker', 'id': 'gorsel', 'label': 'Kapak görseli', 'info': 'Video yoksa bu görsel görünür.'},
        {'type': 'text', 'id': 'baslik', 'label': 'Başlık', 'default': 'Video'},
        {'type': 'text', 'id': 'alt', 'label': 'Alt yazı', 'default': 'Dokun, sesli izle'}]}],
    'max_blocks': 12,
    'presets': [{'name': 'Videolar', 'blocks': [{'type': 'video', 'settings': {'baslik': 'Video 1'}}, {'type': 'video', 'settings': {'baslik': 'Video 2'}}]}]}


def video_bolumu():
    return VIDEO_BOLUMU + '\n{% schema %}\n' + json.dumps(VIDEO_SEMA, ensure_ascii=False, indent=2) + '\n{% endschema %}\n'


def urun_sayfasi(kod, pano, handle, ad_bolum, parcala, harita=None):
    """Özel ürünün sayfa bölümleri: ([(ek, ad, liquid, blok_turleri)], css, js, video_sirasi).
    Tasarımda video şeridi varsa sayfa orada ikiye bölünür; araya bağımsız Videolar bölümü (ay-videolar) girer (video_sirasi: kaçıncı
    bölümden sonra; yoksa None). harita: {blok türü: [(blob, etiket)]} JS ile çizilen görseller için blok içi görsel seçicileri."""
    fontlar, css, govde, js = parcala(pano)
    acilis, ogeler = ust_cocuklar(govde)
    gruplar = grupla(ogeler); ly = yorum_parcasi(gruplar)
    kumeler, video_sirasi = [[]], None
    for n, g in enumerate(gruplar):
        if g[0] == 'video': video_sirasi = len(kumeler) - 1; kumeler.append([]); continue
        kumeler[-1].append((n, g))
    kumeler = [k for k in kumeler if k]
    cikti = []
    for ki, kume in enumerate(kumeler):
        bloklar, vakalar, satin = [], '', False
        for n, (gt, et, h) in kume:
            tip = 'p%02d' % (n + 1)
            p, ayar = ayarla(h, kaynak='block')
            tpl = '<template class="ay-parca">' + liquid([(True, acilis)] + p + [(True, '</div>')]) + '</template>'
            sinif, ek = 'ay-tb', ''  # tema bloğu sarmalayıcısı; tasarımdaki sınıflarla çakışmayan ad (28 Eki: 'ay-blok' ana sayfa tasarımının sınıfıydı, sade sayfaları bozuyordu)
            if gt == 'satin': satin = True
            if 'y-tas' in h or 'y-msj' in h:
                ayar = YORUM_AYAR + ayar
                sinif += "{% unless block.settings.tasarim_yorum %} ay-ytasarimsiz{% endunless %}{% unless block.settings.mesajlar %} ay-ymsjsiz{% endunless %}"
            statik = set(m.group(2)[7:] for m in GORSEL.finditer(h))  # yazılı görsellerin seçicisi zaten var (g…)
            d_ayar, d_esle = gorsel_secici([x for x in (harita or {}).get(tip) or [] if x[0] not in statik], len([a for a in ayar if a['type'] == 'image_picker']))
            ayar = ayar + d_ayar; ek += d_esle
            vakalar += ("  {%- when '" + tip + "' -%}<div class=\"" + sinif + "\" {{ block.shopify_attributes }}>" + ek + tpl + kok('urun', handle)
                        + (LOOX % ('product', 'product') if n == ly else '') + '</div>\n')
            bloklar.append({'type': tip, 'name': et, 'limit': 1, 'settings': ayar})
        ad = ad_bolum if ki == 0 else kisalt(ad_bolum + ' (devam)', 25)
        l = ('{%- comment -%} Ayluna · ' + ad + '. Tasarımın parçaları bu bölümün blokları; yazı ve görseller bloğun ayarında.\n'
             '  araclar/tema/tema_uret.py üretir, elle düzenlenmez. Yalnız ' + handle + ' ürününde çizilir. {%- endcomment -%}\n'
             "{%- if product.handle == '" + handle + "' -%}\n" + varliklar(kod, fontlar)
             + '{%- for block in section.blocks -%}{%- case block.type -%}\n' + vakalar
             + "  {%- when '@app' -%}<div class=\"ay-uyg\" {{ block.shopify_attributes }}>{% render block %}</div>\n{%- endcase -%}{%- endfor -%}\n"
             + (URUN_FORMU if satin else '') + betik(kod) + '{%- endif -%}\n')
        sm = {'name': ad, 'class': 'ay-bolum', 'settings': [], 'blocks': bloklar + [{'type': '@app'}]}
        cikti.append(('' if ki == 0 else '-%d' % (ki + 1), ad,
                      l + '\n{% schema %}\n' + json.dumps(sm, ensure_ascii=False, indent=2) + '\n{% endschema %}\n', [b['type'] for b in bloklar]))
    return cikti, css, js, video_sirasi


def gorsel_secici(liste, var_olan=0, kaynak='block'):
    """JS ile çizilen görseller (28 Eki, kullanıcı: "odası böyle görünecekteki görselleri de değiştirmek istiyorum ama sabit, değişemiyorum"):
    her görsel için bloğun ayarında bir görsel seçici (d1…). Seçilen görsel, ayluna.js'te tasarımdaki görselin (blob kimliği) yerine geçer.
    → (ayarlar, eşleme betiği)."""
    if not liste: return [], ''
    ayar = [{'type': 'header', 'content': 'Bölümdeki görseller'},
             {'type': 'paragraph', 'content': 'Değiştirmek istediğin görseli seç; boş bırakırsan tasarımdaki görsel kalır.'}]
    parca = []
    for k, (blob, et) in enumerate(liste, 1):
        ayar.append({'type': 'image_picker', 'id': 'd%d' % k, 'label': kisalt('Görsel %d%s' % (var_olan + k, (': ' + et) if et else ''), 60)})
        parca.append('{%%- if %s.settings.d%d -%%},%s:{{ %s.settings.d%d | image_url: width: 1600 | json }}{%%- endif -%%}' % (kaynak, k, json.dumps(blob), kaynak, k))
    return ayar, '<script type="application/json" class="ay-gorsel-esle">{"_":0' + ''.join(parca) + '}</script>'


def sade_snippet(kod, pano, handle, parcala):
    """Sade ürünün parçaları tek snippet'te (parca: 'p01'…); ortak bölüm ürüne göre bunu çizer. → (liquid, css, js, gruplar)"""
    fontlar, css, govde, js = parcala(pano)
    acilis, ogeler = ust_cocuklar(govde)
    gruplar = grupla(ogeler); ly = yorum_parcasi(gruplar)
    l = ('{%- comment -%} Ayluna · ' + pano + ' parçaları (Diğer ürünler sayfası bölümü çizer). araclar/tema/tema_uret.py üretir. {%- endcomment -%}\n'
         '{%- if parca == \'varlik\' -%}\n' + varliklar(kod, fontlar) + '{%- elsif parca == \'betik\' -%}\n' + betik(kod) + '{%- else -%}\n{%- case parca -%}\n')
    for n, (gt, et, h) in enumerate(gruplar):
        tpl = '<template class="ay-parca">' + liquid([(True, acilis), (True, h), (True, '</div>')]) + '</template>'
        l += "{%%- when 'p%02d' -%%}" % (n + 1) + tpl + kok('urun', handle) + (LOOX % ('urun', 'urun') if n == ly else '') + '\n'
    return l + '{%- endcase -%}\n{%- endif -%}\n', css, js, gruplar


def sade_sayfasi(sade, ozel, genel):
    """Diğer ürünler sayfası: sade panolu ürünler aynı blokları paylaşır (ayarsız; içerik ürünün kendi panosundan).
    sade: [(handle, snippet_adi, gruplar)], ozel: özel ürünlerin handle'ları (kendi bölümleri çizer), genel: panosuz ürün düzeni."""
    etiket = [et for _, et, _ in sade[0][2]]
    for h, _, g in sade: assert [t for t, _, _ in g] == [t for t, _, _ in sade[0][2]], 'sade panoların parça sırası aynı olmalı: ' + h
    cagir = lambda parca: ('{%- case product.handle -%}' + ''.join("{%%- when '%s' -%%}{%%- render '%s', parca: %s, urun: product -%%}" % (h, sn, parca) for h, sn, _ in sade)
                           + '{%- endcase -%}')
    l = ('{%- comment -%} Ayluna · diğer ürünler sayfası (sade panolu ürünler). Parçalar bu bölümün blokları; içerik ürünün kendi panosundan.\n'
         '  Panosu olmayan yeni ürün sade Shopify düzeniyle açılır. araclar/tema/tema_uret.py üretir. {%- endcomment -%}\n'
         "{%- case product.handle -%}\n{%- when " + ', '.join("'%s'" % h for h, _, _ in sade) + " -%}\n"
         + cagir("'varlik'") + '\n'
         + '{%- for block in section.blocks -%}{%- case block.type -%}\n'
         + "  {%- when '@app' -%}<div class=\"ay-uyg\" {{ block.shopify_attributes }}>{% render block %}</div>\n"
         + '  {%- else -%}<div class="ay-tb" {{ block.shopify_attributes }}>' + cagir('block.type') + '</div>\n'
         + '{%- endcase -%}{%- endfor -%}\n' + URUN_FORMU + cagir("'betik'") + '\n'
         + "{%- when " + ', '.join("'%s'" % h for h in ozel) + " -%}\n"
         + '{%- else -%}\n' + genel + '{%- endcase -%}\n')
    bloklar = [{'type': 'p%02d' % (n + 1), 'name': et, 'limit': 1, 'settings': []} for n, et in enumerate(etiket)]
    s = {'name': 'Diğer ürünler sayfası', 'class': 'ay-bolum', 'settings': [], 'blocks': bloklar + [{'type': '@app'}]}
    return l + '\n{% schema %}\n' + json.dumps(s, ensure_ascii=False, indent=2) + '\n{% endschema %}\n', [b['type'] for b in bloklar]


def urun_sablonu(bolumler):
    """product.json: [(kimlik, bölüm türü, bloklar[, bölüm ayarları])]; blok = tür adı ya da (kimlik, tür, ayarlar)."""
    s = {}
    for b in bolumler:
        kim, tur, bl = b[:3]
        bloklar, sira = {}, []
        for x in bl:
            if isinstance(x, str): bloklar[x] = {'type': x}; sira.append(x)
            else: bloklar[x[0]] = {'type': x[1], 'settings': x[2]}; sira.append(x[0])
        s[kim] = {'type': tur, 'blocks': bloklar, 'block_order': sira}
        if len(b) > 3: s[kim]['settings'] = b[3]
    return json.dumps({'sections': s, 'order': [b[0] for b in bolumler]}, ensure_ascii=False, indent=2) + '\n'
