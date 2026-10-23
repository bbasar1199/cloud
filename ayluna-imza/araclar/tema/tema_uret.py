# Ayluna · Shopify teması v1 (sıfırdan, Online Store 2.0). Çalıştır: python3 araclar/tema/tema_uret.py
# Kullanıcı (19 Eki): "Sen bana artık siteyi gönder bakalım bi … tema dosyası olarak son halini."
# Tasarım tuval panolarının (.dc.html) kendisi: her pano bir snippet; ayluna.js onları çalıştırır (önizlemedekiyle aynı).
# Shopify kipi (AYLUNA_SHOPIFY): sepet Shopify sepeti (/cart.js), ödeme Shopify ödeme sayfası, kapıda ödeme EasySell,
# fiyat/stok/varyant canlı ürünlerden (ay-canli), görseller tema dosyalarından (ay-gorseller).
# Çıktı: ayluna-imza/tema/ (klasör) + scratchpad'e ya da TEMA_ZIP yoluna ayluna-tema.zip. Kurulum: araclar/tema/KURULUM.md
import os, re, sys, json, shutil, zipfile
KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(KOK, 'araclar', 'site'))
import site_uret as S
CIKTI = os.path.join(KOK, 'tema')
SURUM = '1.0.28'

# Pano → kullanıldığı yer. Ödeme, sipariş alındı, hesap ve kargo takip Shopify'ın (ve Track123'ün) kendi sayfaları.
SAYFA_PANO = [('ana', 'Ayluna-Anasayfa', 'ana', 'Ana sayfa'), ('koleksiyon', 'Koleksiyon', 'koleksiyon', 'Koleksiyon'), ('sepet', 'Sepet', 'sepet', 'Sepet'),
              ('arama', 'Arama', 'arama', 'Arama'), ('404', 'Sayfa404', '404', 'Bulunamadı')]
URUN_PANO = [(h, S.OZEL_SAYFA.get(h, 'U-' + h)) for h, *_ in S.A.URUN]
ICERIK_PANO = [(('iletisim', 'contact', 'biz-burdayiz'), 'Iletisim', 'iletisim'), (('iade', 'iade-ve-degisim'), 'Politika-Iade', 'politika'),
               (('kargo', 'kargo-ve-teslimat'), 'Politika-Kargo', 'politika'), (('kvkk', 'gizlilik'), 'Politika-KVKK', 'politika'),
               (('mesafeli-satis', 'mesafeli-satis-sozlesmesi'), 'Politika-Mesafeli', 'politika'), (('on-bilgilendirme', 'on-bilgilendirme-formu'), 'Politika-OnBilgi', 'politika'),
               (('hizmet-sartlari',), 'Politika-Hizmet', 'politika')]


def ad(pano):
    return 'ay-' + re.sub(r'[^a-z0-9]+', '-', pano.lower()).strip('-')


def yaz(yol, icerik, ikili=False):
    tam = os.path.join(CIKTI, yol); os.makedirs(os.path.dirname(tam), exist_ok=True)
    open(tam, 'wb' if ikili else 'w', **({} if ikili else {'encoding': 'utf-8'})).write(icerik)


def pano_snippet(pano, tur, urun=''):
    fontlar, css, govde, js = S.parcala(pano)
    z = re.search(r'--zemin:(#[0-9A-Fa-f]{6})', css)
    return ('{%- comment -%} Ayluna · ' + pano + ' panosu. araclar/tema/tema_uret.py üretir; elle düzenlenmez (tuvalden yeniden üretilir). {%- endcomment -%}\n'
            + fontlar + '\n<style>body{--ay-zemin:' + (z.group(1) if z else '#F6F1E9') + '}</style>\n'
            + '{%- raw -%}\n<style>' + css + '</style>\n<template id="T">' + govde + '</template>\n{%- endraw -%}\n'
            + '<div id="kok" data-sayfa="' + tur + '" data-urun="' + urun + '"></div>\n'
            + '{%- raw -%}\n<script>\n(window.AYLUNA_KUYRUK = window.AYLUNA_KUYRUK || []).push(function () {\n' + js + '\nAyluna.baslat(Component);\n});\n</script>\n{%- endraw -%}\n'), govde + js + css


GENEL_UST = '''{%- comment -%} Pano olmayan sayfalar (blog, hesap, yeni ürün) için sade üst ve alt bilgi {%- endcomment -%}
<header class="ay-g-ust"><a href="{{ routes.root_url }}" class="ay-g-logo" aria-label="Ayluna ana sayfa"><svg viewBox="0 0 24 24" aria-hidden="true" width="24" height="24"><circle cx="12" cy="12" r="10" fill="none" stroke="rgba(26,33,66,.45)" stroke-width="1.6"></circle><path d="M12 2a10 10 0 0 1 0 20a7 10 0 0 0 0-20Z" fill="#F2A65A"></path></svg><b>Ayluna</b></a>
<nav aria-label="Ana menü"><a href="{{ routes.all_products_collection_url }}">Tüm ürünler</a><a href="{{ routes.cart_url }}">Sepet ({{ cart.item_count }})</a></nav></header>
'''
GENEL_ALT = '''<footer class="ay-g-alt"><p>Fiyatlara KDV dahildir. © {{ 'now' | date: '%Y' }} Ayluna</p></footer>
'''
GENEL_CSS = '''<style>
.ay-g-ust{display:flex;align-items:center;justify-content:space-between;gap:16px;max-width:1136px;margin:0 auto;padding:16px;font-family:"Onest",system-ui,sans-serif}
.ay-g-logo{display:flex;align-items:center;gap:8px;color:#1A2142;text-decoration:none}.ay-g-logo b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:22px}
.ay-g-ust nav{display:flex;gap:18px}.ay-g-ust nav a{color:#1A2142;font-weight:600;text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
.ay-g{max-width:760px;margin:0 auto;padding:24px 16px 64px;font-family:"Onest",system-ui,sans-serif;color:#1A2142;line-height:1.6}
.ay-g h1{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:34px;line-height:1.1;margin:8px 0 18px}
.ay-g a{color:#1A2142}.ay-g input,.ay-g textarea,.ay-g select{width:100%;box-sizing:border-box;min-height:50px;padding:12px 14px;margin:6px 0 12px;border:0;border-radius:12px;background:#FFFDF9;box-shadow:inset 0 0 0 1.5px #E3D8C7;font:inherit;font-size:16px}
.ay-g button,.ay-g .ay-g-btn{display:inline-flex;align-items:center;justify-content:center;min-height:52px;padding:0 22px;border:0;border-radius:14px;background:#1A2142;color:#fff;font:inherit;font-weight:700;text-decoration:none;cursor:pointer}
.ay-g-urun{display:grid;gap:24px}.ay-g-urun img{width:100%;height:auto;border-radius:20px;background:#EFE6D8}
.ay-g-fiyat{font-size:22px;font-weight:700}.ay-g-fiyat s{font-size:15px;font-weight:500;color:#5C6078;margin-left:8px}
.ay-g-alt{max-width:1136px;margin:0 auto;padding:24px 16px 40px;color:#5C6078;font:13px "Onest",system-ui,sans-serif}
@media (min-width:1024px){.ay-g-urun{grid-template-columns:minmax(0,1fr) 420px;align-items:start}}
</style>
'''


def main():
    if os.path.exists(CIKTI): shutil.rmtree(CIKTI)
    os.makedirs(CIKTI)
    kullanilan = set()

    def ids(metin):
        for i in re.findall(r'(?<![0-9a-f])([0-9a-f]{32})(?![0-9a-f])', metin):
            if S.blob_yolu(i): kullanilan.add(i)

    # 1) Pano snippet'leri
    for _, pano, tur, _ in SAYFA_PANO:
        sn, ham = pano_snippet(pano, tur); yaz('snippets/%s.liquid' % ad(pano), sn); ids(ham)
    for h, pano in URUN_PANO:
        sn, ham = pano_snippet(pano, 'urun', h); yaz('snippets/%s.liquid' % ad(pano), sn); ids(ham)
    for _, pano, tur in ICERIK_PANO:
        sn, ham = pano_snippet(pano, tur); yaz('snippets/%s.liquid' % ad(pano), sn); ids(ham)

    # 2) Veri ve görseller
    V = S.veri()
    for u in V['urun'].values(): kullanilan.add(u['img'][7:])
    for e in V['ekler']: kullanilan.add(e['img'][7:])
    gorsel = {}
    for i in sorted(kullanilan):
        p = S.blob_yolu(i)
        if not p: continue
        bayt, uz, _ = S.gorsel(p, 1200, 82)
        yaz('assets/%s.%s' % (i, uz), bayt, ikili=True); gorsel[i] = '%s.%s' % (i, uz)
    yaz('assets/ayluna-veri.js', '/* Ayluna · ürün ve teklif verisi (tema_uret.py). Fiyat, stok ve varyant mağazadan canlı gelir (ay-canli). */\nwindow.AYLUNA_VERI = '
        + json.dumps(V, ensure_ascii=False) + ';\n')
    yaz('snippets/ay-gorseller.liquid', '{%- comment -%} Tasarım görselleri: blob kimliği → tema dosyası {%- endcomment -%}\n<script>window.AYLUNA_GORSEL = {\n'
        + ',\n'.join('%s: {{ %s | asset_url | json }}' % (json.dumps(i), json.dumps(f)) for i, f in gorsel.items()) + '\n};</script>\n')
    shutil.copy(os.path.join(S.KAYNAK, 'ayluna.js'), os.path.join(CIKTI, 'assets', 'ayluna.js'))
    css = open(os.path.join(S.KAYNAK, 'ayluna.css'), encoding='utf-8').read()
    yaz('assets/ayluna.css', css + '\nbody{background:var(--ay-zemin,#F6F1E9)}\n')

    # 3) Canlı ürün verisi ve sepet
    yaz('snippets/ay-canli.liquid', '''{%- comment -%} Mağazanın kendi verisi: fiyat (kuruş), eski fiyat, stok, varyantlar, adres; ilk sepet {%- endcomment -%}
<script>
window.AYLUNA_CANLI = {
{%- for p in collections.all.products -%}
{{ p.handle | json }}: {"p": {{ p.price }}, "c": {{ p.compare_at_price | default: 0 }}, "stok": {{ p.available | json }}, "vid": {{ p.selected_or_first_available_variant.id | json }}, "url": {{ p.url | json }}, "v": [
{%- for v in p.variants -%}{"id": {{ v.id }}, "t": {{ v.title | json }}, "a": {{ v.available | json }}, "p": {{ v.price }}}{%- unless forloop.last -%},{%- endunless -%}{%- endfor -%}
]}{%- unless forloop.last -%},{%- endunless %}
{%- endfor -%}
};
window.AYLUNA_SEPET = {{ cart | json }};
</script>
''')

    # 4) Layout
    yaz('layout/theme.liquid', '''<!doctype html>
<html lang="{{ request.locale.iso_code | default: 'tr' }}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <meta name="theme-color" content="#1A2142">
  <link rel="canonical" href="{{ canonical_url }}">
  <title>{{ page_title }}{% unless page_title contains shop.name %} · {{ shop.name }}{% endunless %}</title>
  {%- if page_description %}<meta name="description" content="{{ page_description | escape }}">{% endif %}
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Ccircle cx='12' cy='12' r='11' fill='%231A2142'/%3E%3Cpath d='M12 4a8 8 0 1 0 0 16a6 6 0 0 1 0-16Z' fill='%23F2A65A'/%3E%3C/svg%3E">
  <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Young+Serif&family=Onest:wght@400;500;600;700&display=swap">
  {{ 'ayluna.css' | asset_url | stylesheet_tag }}
  {% render 'ay-gorseller' %}
  {% render 'ay-canli' %}
  <script>
    window.AYLUNA_SHOPIFY = true;
    window.AYLUNA_AYAR = { takip: {{ settings.kargo_takip_url | default: '/apps/track123' | json }} };
  </script>
  <script src="{{ 'ayluna-veri.js' | asset_url }}" defer></script>
  <script src="{{ 'ayluna.js' | asset_url }}" defer></script>
  {{ content_for_header }}
</head>
<body>
  {{ content_for_layout }}
</body>
</html>
''')
    yaz('layout/password.liquid', '''<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{{ shop.name }}</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Young+Serif&family=Onest:wght@400;500;600;700&display=swap">
  {{ content_for_header }}
</head>
<body style="margin:0;background:#1A2142;color:#FFFDF9">
  {{ content_for_layout }}
</body>
</html>
''')

    # 5) Bölümler
    secenek = [dict(value=k, label=e) for k, _, _, e in SAYFA_PANO]
    yaz('sections/ayluna-sayfa.liquid', '{%- comment -%} Ayluna · tasarım panosu olan sayfalar (ana sayfa, koleksiyon, sepet, arama, 404) {%- endcomment -%}\n{%- case section.settings.sayfa -%}\n'
        + ''.join("  {%%- when '%s' -%%}{%% render '%s' %%}\n" % (k, ad(p)) for k, p, _, _ in SAYFA_PANO)
        + '{%- endcase -%}\n\n{% schema %}\n' + json.dumps({'name': 'Ayluna sayfası', 'class': 'ay-bolum', 'settings': [
            {'type': 'select', 'id': 'sayfa', 'label': 'Sayfa', 'options': secenek, 'default': 'ana'}]}, ensure_ascii=False, indent=2) + '\n{% endschema %}\n')
    yaz('sections/ayluna-urun.liquid', '''{%- comment -%} Ayluna · ürün sayfası. Her ürünün kendi tasarım panosu var; panosu olmayan yeni ürün sade sayfayla açılır.
  Gizli ürün formu kapıda ödeme (EasySell) ve Kaching içindir: ayluna.js seçilen modeli/paketi buraya yazar (data-ay-urun-formu).
  Kaching paket kutusu görünmez durur; tasarımdaki paket kartları onu seçer (kapıda formu paketi ve indirimi oradan okur).
  Kapıda ödeme düğmesini mağaza sahibi EasySell ile koyar; tema koymaz. EasySell düğmesi ve bu bölüme eklenen uygulama blokları
  tasarımda satın al düğmesinin altındaki yuvaya taşınır. {%- endcomment -%}
{%- assign ay_pano = true -%}
{%- case product.handle -%}
''' + ''.join("  {%%- when '%s' -%%}{%% render '%s' %%}\n" % (h, ad(p)) for h, p in URUN_PANO) + '''  {%- else -%}
    {%- assign ay_pano = false -%}
    ''' + GENEL_CSS.replace('\n', '\n    ') + GENEL_UST + '''    <main class="ay-g"><div class="ay-g-urun">
      <div>{%- for m in product.media limit: 6 -%}{{ m.preview_image | image_url: width: 1200 | image_tag: loading: 'lazy', alt: product.title }}{%- endfor -%}</div>
      <div>
        <h1>{{ product.title }}</h1>
        <p class="ay-g-fiyat">{{ product.price | money }}{%- if product.compare_at_price > product.price %}<s>{{ product.compare_at_price | money }}</s>{% endif %}</p>
        {%- form 'product', product, data-ay-shopify: '' -%}
          {%- if product.has_only_default_variant -%}<input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id }}">
          {%- else -%}<label>Seçenek<select name="id">{%- for v in product.variants -%}<option value="{{ v.id }}"{% unless v.available %} disabled{% endunless %}>{{ v.title }}</option>{%- endfor -%}</select></label>{%- endif -%}
          <button type="submit"{% unless product.available %} disabled{% endunless %}>{% if product.available %}Sepete ekle{% else %}Tükendi{% endif %}</button>
        {%- endform -%}
        {%- for block in section.blocks -%}{%- case block.type -%}{%- when '@app' -%}<div {{ block.shopify_attributes }}>{% render block %}</div>{%- endcase -%}{%- endfor -%}
        <div class="rte">{{ product.description }}</div>
      </div>
    </div></main>
    ''' + GENEL_ALT + '''{%- endcase -%}
{%- if ay_pano -%}
{%- form 'product', product, data-ay-urun-formu: '', data-ay-shopify: '', hidden: 'hidden', class: 'ay-urun-formu' -%}
  <input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id }}">
  <input type="hidden" name="quantity" value="1">
{%- endform -%}
<div class="ay-arka" aria-hidden="true"><kaching-bundle product-id="{{ product.id }}"></kaching-bundle></div>
<div class="ay-uygulama-bloklari" hidden>{%- for block in section.blocks -%}{%- case block.type -%}{%- when '@app' -%}<div class="ay-uygulama" {{ block.shopify_attributes }}>{% render block %}</div>{%- endcase -%}{%- endfor -%}</div>
{%- endif -%}

{% schema %}
{ "name": "Ayluna ürün sayfası", "class": "ay-bolum", "settings": [], "blocks": [{ "type": "@app" }] }
{% endschema %}
''')
    vakalar = ''.join("  {%%- when %s -%%}{%% render '%s' %%}\n" % (', '.join("'%s'" % x for x in el), ad(p)) for el, p, _ in ICERIK_PANO)
    yaz('sections/ayluna-icerik.liquid', '''{%- comment -%} Ayluna · sayfalar. İletişim ve yasal metinlerin tasarım panosu sayfa adresine (handle) göre seçilir;
  diğer sayfalar, blog ve yazılar sade düzenle açılır. {%- endcomment -%}
{%- liquid
  assign pano = false
  if template.name == 'page'
    case page.handle
''' + ''.join("      when %s\n        assign pano = '%s'\n" % (', '.join("'%s'" % x for x in el), p) for el, p, _ in ICERIK_PANO) + '''    endcase
  endif
-%}
{%- if pano -%}
  {%- case page.handle -%}
''' + vakalar + '''  {%- endcase -%}
{%- else -%}
  ''' + GENEL_CSS.replace('\n', '\n  ') + GENEL_UST + '''  <main class="ay-g">
    {%- case template.name -%}
      {%- when 'blog' -%}
        <h1>{{ blog.title }}</h1>
        {%- for a in blog.articles -%}<article><h2><a href="{{ a.url }}">{{ a.title }}</a></h2><p>{{ a.excerpt_or_content | strip_html | truncate: 160 }}</p></article>{%- else -%}<p>Henüz yazı yok.</p>{%- endfor -%}
      {%- when 'article' -%}
        <h1>{{ article.title }}</h1><div class="rte">{{ article.content }}</div>
      {%- else -%}
        <h1>{{ page.title }}</h1><div class="rte">{{ page.content }}</div>
    {%- endcase -%}
  </main>
  ''' + GENEL_ALT + '''{%- endif -%}

{% schema %}
{ "name": "Ayluna içerik", "class": "ay-bolum", "settings": [] }
{% endschema %}
''')
    yaz('sections/ayluna-sifre.liquid', '''<main style="min-height:100vh;display:grid;place-items:center;padding:24px;font-family:Onest,system-ui,sans-serif;text-align:center">
  <div style="max-width:420px">
    <h1 style="font-family:'Young Serif',Georgia,serif;font-weight:400;font-size:44px;margin:0">Ayluna</h1>
    <p style="color:#C9CFE2">{{ shop.password_message | default: 'Çok yakında.' }}</p>
    {%- form 'storefront_password' -%}
      {{ form.errors | default_errors }}
      <label for="Sifre" style="display:block;margin:18px 0 6px">Mağaza şifresi</label>
      <input id="Sifre" type="password" name="password" autocomplete="current-password" style="width:100%;min-height:50px;border-radius:12px;border:0;padding:0 14px;font:inherit">
      <button type="submit" style="margin-top:12px;min-height:52px;width:100%;border:0;border-radius:14px;background:#F2A65A;color:#1A2142;font:inherit;font-weight:700">Gir</button>
    {%- endform -%}
  </div>
</main>

{% schema %}
{ "name": "Ayluna şifre sayfası", "settings": [] }
{% endschema %}
''')

    # 6) Şablonlar
    def sablon(tip, ayar=None, bolum='ana'):
        b = {'type': tip}
        if ayar: b['settings'] = ayar
        return json.dumps({'sections': {bolum: b}, 'order': [bolum]}, ensure_ascii=False, indent=2) + '\n'
    yaz('templates/index.json', sablon('ayluna-sayfa', {'sayfa': 'ana'}))
    yaz('templates/collection.json', sablon('ayluna-sayfa', {'sayfa': 'koleksiyon'}))
    yaz('templates/list-collections.json', sablon('ayluna-sayfa', {'sayfa': 'koleksiyon'}))
    yaz('templates/cart.json', sablon('ayluna-sayfa', {'sayfa': 'sepet'}))
    yaz('templates/search.json', sablon('ayluna-sayfa', {'sayfa': 'arama'}))
    yaz('templates/404.json', sablon('ayluna-sayfa', {'sayfa': '404'}))
    yaz('templates/product.json', sablon('ayluna-urun', bolum='urun'))
    for t in ('page', 'blog', 'article'):
        yaz('templates/%s.json' % t, sablon('ayluna-icerik', bolum='icerik'))
    yaz('templates/password.json', json.dumps({'layout': 'password', 'sections': {'sifre': {'type': 'ayluna-sifre'}}, 'order': ['sifre']}, indent=2) + '\n')
    yaz('templates/gift_card.liquid', '''{%- layout none -%}
<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Hediye kartı · {{ shop.name }}</title></head>
<body style="font-family:system-ui,sans-serif;background:#F6F1E9;color:#1A2142;display:grid;place-items:center;min-height:100vh;margin:0">
  <main style="text-align:center;padding:24px">
    <h1>{{ gift_card.balance | money }}</h1>
    <p>Hediye kartı kodu: <b>{{ gift_card.code | format_code }}</b></p>
    {%- if gift_card.expired %}<p>Süresi doldu.</p>{% endif -%}
    <p><a href="{{ shop.url }}">Alışverişe başla</a></p>
  </main>
</body></html>
''')
    # Müşteri hesabı: mağaza yeni müşteri hesaplarını kullanıyorsa bunlar açılmaz; klasik hesaplar için sade formlar
    MUSTERI = {
        'login': '''<h1>Giriş yap</h1>
{%- form 'customer_login' -%}{{ form.errors | default_errors }}
<label>E-posta<input type="email" name="customer[email]" autocomplete="email" required></label>
<label>Şifre<input type="password" name="customer[password]" autocomplete="current-password" required></label>
<button type="submit">Giriş yap</button>{%- endform -%}
<p><a href="{{ routes.account_register_url }}">Hesap oluştur</a></p>
{%- form 'recover_customer_password' -%}{{ form.errors | default_errors }}<label>Şifremi unuttum (e-posta)<input type="email" name="email" autocomplete="email"></label><button type="submit">Bağlantı gönder</button>{%- endform -%}''',
        'register': '''<h1>Hesap oluştur</h1>
{%- form 'create_customer' -%}{{ form.errors | default_errors }}
<label>Ad<input name="customer[first_name]" autocomplete="given-name"></label><label>Soyad<input name="customer[last_name]" autocomplete="family-name"></label>
<label>E-posta<input type="email" name="customer[email]" autocomplete="email" required></label><label>Şifre<input type="password" name="customer[password]" autocomplete="new-password" required></label>
<button type="submit">Oluştur</button>{%- endform -%}''',
        'account': '''<h1>Hesabın</h1><p><a href="{{ routes.account_logout_url }}">Çıkış yap</a> · <a href="{{ routes.account_addresses_url }}">Adreslerim</a></p>
<h2>Siparişler</h2>{%- for o in customer.orders -%}<p><a href="{{ o.customer_url }}">{{ o.name }}</a> · {{ o.created_at | date: '%d.%m.%Y' }} · {{ o.total_price | money }} · {{ o.fulfillment_status_label }}</p>{%- else -%}<p>Henüz sipariş yok.</p>{%- endfor -%}''',
        'order': '''<h1>Sipariş {{ order.name }}</h1><p>{{ order.created_at | date: '%d.%m.%Y' }} · {{ order.financial_status_label }} · {{ order.fulfillment_status_label }}</p>
{%- for l in order.line_items -%}<p>{{ l.title }} × {{ l.quantity }} · {{ l.final_line_price | money }}</p>{%- endfor -%}<p><b>Toplam: {{ order.total_price | money }}</b></p>
<p><a href="{{ routes.account_url }}">Hesabıma dön</a></p>''',
        'addresses': '''<h1>Adreslerim</h1>{%- for a in customer.addresses -%}<p>{{ a | format_address }}</p>{%- else -%}<p>Kayıtlı adres yok.</p>{%- endfor -%}
{%- form 'customer_address', customer.new_address -%}{{ form.errors | default_errors }}
<label>Ad<input name="address[first_name]"></label><label>Soyad<input name="address[last_name]"></label><label>Adres<input name="address[address1]"></label>
<label>İlçe<input name="address[city]"></label><label>İl<input name="address[province]"></label><label>Telefon<input name="address[phone]" type="tel"></label>
<input type="hidden" name="address[country]" value="Turkey"><button type="submit">Adres ekle</button>{%- endform -%}''',
        'activate_account': '''<h1>Hesabını etkinleştir</h1>{%- form 'activate_customer_password' -%}{{ form.errors | default_errors }}
<label>Şifre<input type="password" name="customer[password]" autocomplete="new-password"></label><label>Şifre tekrar<input type="password" name="customer[password_confirmation]" autocomplete="new-password"></label>
<button type="submit">Etkinleştir</button>{%- endform -%}''',
        'reset_password': '''<h1>Yeni şifre</h1>{%- form 'reset_customer_password' -%}{{ form.errors | default_errors }}
<label>Şifre<input type="password" name="customer[password]" autocomplete="new-password"></label><label>Şifre tekrar<input type="password" name="customer[password_confirmation]" autocomplete="new-password"></label>
<button type="submit">Kaydet</button>{%- endform -%}'''}
    for k, govde in MUSTERI.items():
        yaz('templates/customers/%s.liquid' % k, GENEL_CSS + GENEL_UST + '<main class="ay-g">\n' + govde + '\n</main>\n' + GENEL_ALT)

    # 7) Ayarlar ve dil
    yaz('config/settings_schema.json', json.dumps([
        {'name': 'theme_info', 'theme_name': 'Ayluna', 'theme_version': SURUM, 'theme_author': 'Ayluna', 'theme_documentation_url': 'https://ayluna.shop', 'theme_support_url': 'https://ayluna.shop'},
        {'name': 'Ayluna', 'settings': [
            {'type': 'paragraph', 'content': 'Kapıda ödeme: EasySell ayarlarında özel düğme seçicisine [data-ay-kapida] yazın. Paket fiyatları için Kaching Bundles ya da otomatik indirim tanımlı olmalı (KURULUM).'},
            {'type': 'text', 'id': 'kargo_takip_url', 'label': 'Kargo takip adresi', 'default': '/apps/track123'}]}], ensure_ascii=False, indent=2) + '\n')
    yaz('config/settings_data.json', json.dumps({'current': {'kargo_takip_url': '/apps/track123'}}, indent=2) + '\n')
    yaz('locales/tr.default.json', json.dumps({'genel': {'marka': 'Ayluna'}}, ensure_ascii=False, indent=2) + '\n')

    # 8) Zip
    zyol = os.environ.get('TEMA_ZIP') or os.path.join(KOK, 'tema-zip', 'ayluna-SHOPIFY-TEMA-%s.zip' % SURUM)
    os.makedirs(os.path.dirname(zyol), exist_ok=True)
    with zipfile.ZipFile(zyol, 'w', zipfile.ZIP_DEFLATED) as z:
        for dp, _, fs in os.walk(CIKTI):
            for f in sorted(fs):
                tam = os.path.join(dp, f); z.write(tam, os.path.relpath(tam, CIKTI))
    dosya = sum(len(fs) for _, _, fs in os.walk(CIKTI))
    print('tema:', CIKTI, '· dosya:', dosya, '· görsel:', len(gorsel), '· zip: %s (%.1f MB)' % (zyol, os.path.getsize(zyol) / 1e6))


if __name__ == '__main__':
    main()
