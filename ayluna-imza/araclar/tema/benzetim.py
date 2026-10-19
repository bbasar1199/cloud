# Ayluna teması · Shopify benzetimi (mağazasız deneme). Çalıştır: python3 araclar/tema/benzetim.py [port]
# tema/ klasöründeki panoları Shopify'ın vereceği biçimde sunar (AYLUNA_SHOPIFY, AYLUNA_CANLI, AYLUNA_SEPET, AYLUNA_GORSEL)
# ve sepet uç noktalarını taklit eder: /cart.js, /cart/add.js, /cart/change.js, /cart/update.js, /cart/clear.js, /contact.
# Canlı ürün verisi ogrenme/canli-urunler.json'dan (mağazanın /products.json kopyası). Liquid çalıştırmaz; panolar ham hâliyle sunulur.
import os, re, sys, json, threading
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.dirname(__file__))
import tema_uret as T
TEMA = os.path.join(KOK, 'tema')

ham = json.load(open(os.path.join(KOK, 'ogrenme', 'canli-urunler.json')))
URUNLER = ham['products'] if isinstance(ham, dict) else ham
FIYAT_DEGIS = json.loads(os.environ.get('BENZETIM_FIYAT', '{}'))  # {"handle": kuruş} → canlı fiyat farkı denemesi
CANLI, VARYANT = {}, {}
for p in URUNLER:
    vs = [dict(id=v['id'], t=v['title'], a=bool(v.get('available', True)), p=int(round(float(v['price']) * 100))) for v in p['variants']]
    if p['handle'] in FIYAT_DEGIS:
        for v in vs: v['p'] = FIYAT_DEGIS[p['handle']]
    ilk = next((v for v in vs if v['a']), vs[0])
    c = max([int(round(float(v['compare_at_price']) * 100)) for v in p['variants'] if v.get('compare_at_price')] or [0])
    CANLI[p['handle']] = dict(p=ilk['p'], c=c, stok=any(v['a'] for v in vs), vid=ilk['id'], url='/products/' + p['handle'], v=vs)
    for v in vs: VARYANT[v['id']] = dict(h=p['handle'], ad=p['title'], vt=v['t'], p=v['p'], c=c, img=(p.get('images') or [{}])[0].get('src', ''))

SEPET = {'satir': []}  # {key, id, adet, ozellik}
_veri = open(os.path.join(TEMA, 'assets', 'ayluna-veri.js'), encoding='utf-8').read()
V_URUN = json.loads(_veri[_veri.index('=') + 1:].strip().rstrip(';'))['urun']  # tasarım verisi (paketler)
KILIT = threading.Lock()
GORSEL = {}
for f in os.listdir(os.path.join(TEMA, 'assets')):
    m = re.match(r'^([0-9a-f]{32})\.\w+$', f)
    if m: GORSEL[m.group(1)] = '/assets/' + f
GONDERILEN = []  # /contact gönderimleri (test için)
ISTEK = []  # /cart/add.js istek adresleri (kaching_bundles=true denetimi)

# Kaching taklidi (canlı sayfada gözlenen davranış, 19 Eki): <kaching-bundle> yer tutucusuna 1,5 sn sonra kutu kurulur;
# her paket bir radyo (değer = paket kimliği); $$c.selectedVariants() seçili paketin adedini ve __kaching_bundles özelliğini,
# seçim yoksa 1 adet ve boş özellik döndürür; varyant gizli formdaki id'dir.
KACHING_JS = '''<script>
customElements.define('kaching-bundles-block', class extends HTMLElement {
  connectedCallback() {
    var ayar = JSON.parse(document.querySelector('script.kaching-bundles-deal-block-settings').textContent), ad = 'kb' + Date.now(), self = this;
    this.innerHTML = ayar.dealBars.map(function (b) { return '<div class="kaching-bundles__bar"><input type="radio" name="' + ad + '" value="' + b.id + '"><label>' + b.title + '</label></div>'; }).join('');
    this.$$c = { selectedVariants: function () {
      var r = self.querySelector('input:checked'), vid = +document.querySelector('form[data-ay-urun-formu] [name=id]').value;
      if (!r) return [{ variantId: vid, quantity: 1, properties: {} }];
      var b = ayar.dealBars.filter(function (x) { return x.id === r.value; })[0];
      return [{ variantId: vid, quantity: b.quantity, properties: { __kaching_bundles: JSON.stringify({ deal: 'TEST', main: true, bid: b.id }) } }]; } };
  }
});
setTimeout(function () { document.querySelectorAll('kaching-bundle').forEach(function (k) { k.appendChild(document.createElement('kaching-bundles-block')); }); }, 1500);
</script>'''


def sepet_json():
    items, toplam, adet = [], 0, 0
    for s in SEPET['satir']:
        v = VARYANT[s['id']]
        satir = v['p'] * s['adet']
        items.append(dict(key=s['key'], id=s['id'], variant_id=s['id'], handle=v['h'], product_title=v['ad'], variant_title=v['vt'], quantity=s['adet'],
                          final_line_price=satir, original_line_price=satir, price=v['p'], image=v['img'], properties=s['ozellik']))
        toplam += satir; adet += s['adet']
    return dict(items=items, total_price=toplam, item_count=adet, currency='TRY')


def ekle(kalem):
    vid = int(kalem['id']); oz = kalem.get('properties') or {}; n = int(kalem.get('quantity', 1))
    if vid not in VARYANT: raise ValueError('Ürün bulunamadı')
    for s in SEPET['satir']:
        if s['id'] == vid and s['ozellik'] == oz: s['adet'] += n; return
    SEPET['satir'].append(dict(key='%d:%d' % (vid, len(SEPET['satir']) + int(threading.get_ident() % 997)), id=vid, adet=n, ozellik=oz))


def snippet(ad):
    s = open(os.path.join(TEMA, 'snippets', ad + '.liquid'), encoding='utf-8').read()
    s = re.sub(r'\{%-? comment -?%\}.*?\{%-? endcomment -?%\}', '', s, flags=re.S)
    return re.sub(r'\{%-? (end)?raw -?%\}', '', s)


def sayfa(govde, baslik):
    css = open(os.path.join(TEMA, 'assets', 'ayluna.css'), encoding='utf-8').read()
    return ('<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>%s</title>'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Young+Serif&family=Onest:wght@400;500;600;700&display=swap"><style>%s</style>'
            '<script>window.AYLUNA_GORSEL = %s;</script><script>window.AYLUNA_CANLI = %s; window.AYLUNA_SEPET = %s;</script>'
            '<script>window.AYLUNA_SHOPIFY = true; window.AYLUNA_AYAR = { takip: "/apps/track123" };</script>'
            '<script src="/assets/ayluna-veri.js" defer></script><script src="/assets/ayluna.js" defer></script></head><body>%s</body></html>'
            % (baslik, css, json.dumps(GORSEL), json.dumps(CANLI, ensure_ascii=False), json.dumps(sepet_json(), ensure_ascii=False), govde))


def rota(yol):
    if yol in ('/', ''): return snippet('ay-ayluna-anasayfa'), 'Ayluna'
    if yol in ('/collections/all', '/collections'): return snippet('ay-koleksiyon'), 'Tüm ürünler'
    if yol == '/cart': return snippet('ay-sepet'), 'Sepet'
    if yol == '/search': return snippet('ay-arama'), 'Ara'
    m = re.match(r'^/products/([\w-]+)$', yol)
    if m:
        h = m.group(1); pano = dict(T.URUN_PANO).get(h)
        if not pano or h not in CANLI: return None
        c = CANLI[h]
        form = ('<form method="post" action="/cart/add" data-ay-urun-formu data-ay-shopify hidden class="ay-urun-formu"><input type="hidden" name="id" value="%d">'
                '<input type="hidden" name="quantity" value="1"></form>' % c['vid'])
        pk = [b for b in (V_URUN.get(h) or {}).get('paket') or []]
        if len(pk) > 1:  # paketli ürün: Kaching ayarı + gizli kutu
            bars = [dict(id='bar-%d' % b['n'], title='%d Adet' % b['n'], quantity=b['n']) for b in pk]
            form += ('<script class="kaching-bundles-product" data-product-id="1" data-main="true" type="application/json">{}</script>'
                     '<script class="kaching-bundles-deal-block-settings" data-product-id="1" type="application/json">%s</script>'
                     '<div class="ay-arka" aria-hidden="true"><kaching-bundle product-id="1"></kaching-bundle></div>' % json.dumps(dict(dealBars=bars)) + KACHING_JS)
        return snippet(T.ad(pano)) + form, h
    m = re.match(r'^/pages/([\w-]+)$', yol)
    if m:
        for el, pano, _ in T.ICERIK_PANO:
            if m.group(1) in el: return snippet(T.ad(pano)), m.group(1)
    return None


class Isleyici(BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def yanit(self, kod, govde, tur='application/json; charset=utf-8'):
        b = govde.encode() if isinstance(govde, str) else govde
        self.send_response(kod); self.send_header('Content-Type', tur); self.send_header('Content-Length', str(len(b))); self.end_headers(); self.wfile.write(b)

    def do_GET(self):
        u = urlparse(self.path); yol = u.path
        if yol == '/cart.js': return self.yanit(200, json.dumps(sepet_json(), ensure_ascii=False))
        if yol == '/__gonderilen': return self.yanit(200, json.dumps(GONDERILEN, ensure_ascii=False))
        if yol == '/__istek': return self.yanit(200, json.dumps(ISTEK, ensure_ascii=False))
        if yol.startswith('/assets/'):
            f = os.path.join(TEMA, 'assets', os.path.basename(yol))
            if os.path.exists(f):
                tur = {'.js': 'application/javascript', '.css': 'text/css', '.jpg': 'image/jpeg', '.webp': 'image/webp'}.get(os.path.splitext(f)[1], 'application/octet-stream')
                return self.yanit(200, open(f, 'rb').read(), tur)
        r = rota(yol)
        if r: return self.yanit(200, sayfa(*r), 'text/html; charset=utf-8')
        return self.yanit(404, sayfa(snippet('ay-sayfa404'), 'Bulunamadı'), 'text/html; charset=utf-8')

    def do_POST(self):
        n = int(self.headers.get('Content-Length') or 0); ham = self.rfile.read(n)
        yol = urlparse(self.path).path
        if yol == '/cart/add.js': ISTEK.append(self.path)
        if yol == '/contact':
            GONDERILEN.append(ham.decode('utf-8', 'replace')); return self.yanit(200, '<p>ok</p>', 'text/html')
        try: d = json.loads(ham or b'{}')
        except Exception: d = {}
        with KILIT:
            try:
                if yol == '/cart/add.js':
                    for k in d.get('items') or [d]: ekle(k)
                    return self.yanit(200, json.dumps({'items': []}))
                if yol == '/cart/change.js':
                    for s in SEPET['satir']:
                        if s['key'] == d['id']: s['adet'] = int(d['quantity'])
                    SEPET['satir'] = [s for s in SEPET['satir'] if s['adet'] > 0]
                    return self.yanit(200, json.dumps(sepet_json(), ensure_ascii=False))
                if yol == '/cart/update.js':
                    for k, q in (d.get('updates') or {}).items():
                        for s in SEPET['satir']:
                            if s['key'] == k: s['adet'] = int(q)
                    SEPET['satir'] = [s for s in SEPET['satir'] if s['adet'] > 0]
                    return self.yanit(200, json.dumps(sepet_json(), ensure_ascii=False))
                if yol == '/cart/clear.js':
                    SEPET['satir'] = []; return self.yanit(200, json.dumps(sepet_json()))
            except Exception as e:
                return self.yanit(422, json.dumps({'status': 422, 'description': str(e)}, ensure_ascii=False))
        self.yanit(404, '{}')


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8790
    print('benzetim: http://127.0.0.1:%d' % port)
    ThreadingHTTPServer(('127.0.0.1', port), Isleyici).serve_forever()
