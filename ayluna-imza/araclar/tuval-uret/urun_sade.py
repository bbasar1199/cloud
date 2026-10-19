# Ayluna · diğer 13 ürün için sade ürün sayfaları (18 Eki). Çalıştır: python3 urun_sade.py
# Kullanıcı: "Geriye kalan ürünlerim için de onların kendi sayfa düzenine uygun olacak şekilde basit tasarımlar yap…
# site içerisinde kendi görselleri var, direkt onları kullanabilirsin."
# Kaynak: ogrenme/urun-icerik.json (dürüst içerik; sahte puan, 90 gün, sağlık iddiası, başka üründen kopya metin yok) ve
# canvas/urunler/<handle>/ (sitedeki görseller; uydurma yorum kartı ya da sağlık iddiası taşıyan afişler alınmadı).
# İskelet canlıdaki ortak şablonun sırası: galeri → ad + fiyat → özellikler → paket → stok (elle) → iki buton → teslim → kutuda → SSS → yorumlar.
# Dil: marka çekirdeği (krem + lacivert, Young Serif + Onest, üst bant, menü, alt bilgi ana sayfayla aynı); ürünün kendi rengi vurgu.
# Ürün adları mağazadaki gibi (içerik dosyasındaki ad önerileri kullanıcıya soruldu).
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL, TL_JS, canli_galeri
import anasayfa as A
import sayfalar as SY
ROOT = os.path.join(HERE, '..', '..')
CANVAS = os.path.join(ROOT, 'canvas')
B = '/_blob/'
ICERIK = json.load(open(os.path.join(ROOT, 'ogrenme', 'urun-icerik.json'), encoding='utf-8'))
BLOB = json.load(open(os.path.join(CANVAS, 'urunler', 'bloblar.json')))
AD = dict((h, ad) for h, ad, p, c, v in A.URUN)
YUK = json.load(open(os.path.join(CANVAS, 'urunler', 'yukseklik.json'))) if os.path.exists(os.path.join(CANVAS, 'urunler', 'yukseklik.json')) else {}

CSS = SY.CSS + r"""
.pg{--v:#F2A65A}
.u-serit{display:flex;align-items:center;justify-content:center;min-height:38px;padding:8px 16px;font-size:13px;font-weight:600;color:var(--lac);text-align:center;line-height:1.35}
/* Galeri: kaydırılır, 5 sn'de geçer; fotoğrafın en altında ince çizgiler, geçilenler beyaz (kullanıcı, 19 Eki: "gömülü olsun") */
.gal{position:relative;margin:0 12px;border-radius:22px;overflow:hidden;background:#EFE6D8;aspect-ratio:1/1}
.g-iz{position:absolute;inset:0;display:flex;overflow-x:auto;scroll-snap-type:x mandatory;overscroll-behavior-x:contain;scrollbar-width:none}
.g-iz::-webkit-scrollbar{display:none}
.gs{position:relative;flex:0 0 100%;scroll-snap-align:start}
.gs img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.g-alt{position:absolute;left:0;right:0;bottom:8px;z-index:1;display:flex;justify-content:center;gap:4px;pointer-events:none;filter:drop-shadow(0 1px 1.5px rgba(12,16,39,.5))}
.g-alt i{display:block;width:16px;height:3px;border-radius:2px;background:rgba(255,253,249,.4);transition:background-color .3s var(--ease)}
.g-alt .lit{background:#FFFDF9}
/* Ad, fiyat */
.bilgi{padding:18px 16px 0}
.bilgi h1{margin:0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:28px;line-height:1.08;letter-spacing:-.02em;color:var(--lac)}
.bilgi h1 span{color:var(--v)}
.bilgi .kisa{margin:8px 0 0;font-size:15px;color:var(--soluk)}
.fiyat{display:flex;align-items:center;flex-wrap:wrap;gap:6px 10px;margin:14px 0 0;font-variant-numeric:tabular-nums;color:var(--lac)}
.fiyat b{font-size:24px;font-weight:700;letter-spacing:-.01em}
.fiyat s{font-size:15px;color:var(--soluk)}
.fiyat em{padding:3px 9px;border-radius:999px;background:var(--lac);color:#fff;font-style:normal;font-size:12px;font-weight:700}
.fiyat em.yok{background:#E9E2D6;color:var(--lac)}
/* Özellikler */
.oz-l{list-style:none;margin:18px 16px 0;padding:4px 16px;border-radius:20px;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi)}
.oz-l li{display:grid;grid-template-columns:28px minmax(0,1fr);gap:10px;padding:12px 0;border-top:1px solid var(--cizgi);color:var(--lac)}
.oz-l li:first-child{border-top:0}
.oz-l svg{width:24px;height:24px}.oz-l circle{fill:none;stroke:var(--lac);stroke-width:1.4}.oz-l path{fill:var(--v)}
.oz-l b{display:block;font-size:15px}.oz-l span{display:block;margin-top:2px;font-size:14px;color:var(--soluk)}
/* Seçenek ve paket */
.ust-y{margin:22px 16px 10px;font-size:14px;font-weight:700;color:var(--lac)}
.sec{display:flex;gap:8px;padding:0 16px}
.sec button{min-height:48px;padding:0 18px;border:0;border-radius:999px;background:var(--kart);box-shadow:inset 0 0 0 1.5px var(--cizgi);font-size:15px;font-weight:600;color:var(--lac)}
.sec button.on{box-shadow:inset 0 0 0 2px var(--lac)}
.pk{display:flex;flex-direction:column;gap:12px;padding:0 16px}
.pk button{position:relative;display:grid;grid-template-columns:22px minmax(0,1fr) auto;gap:12px;align-items:center;min-height:72px;padding:12px 14px;border:0;border-radius:16px;background:var(--kart);box-shadow:inset 0 0 0 1.5px var(--cizgi);text-align:left;color:var(--lac)}
.pk button.on{box-shadow:inset 0 0 0 2px var(--lac)}
.pk b{display:block;font-size:16px}.pk small{display:block;margin-top:2px;font-size:13px;color:var(--soluk)}
.pk .pf{text-align:right;font-variant-numeric:tabular-nums}.pk .pf strong{display:block;font-size:16px}.pk .pf s{font-size:13px;color:var(--soluk)}
.pk .kurdele{position:absolute;right:14px;top:-10px;padding:2px 10px;border-radius:999px;background:var(--lac);color:#fff;font-size:12px;font-weight:700}
.nokta{width:22px;height:22px;border-radius:50%;box-shadow:inset 0 0 0 1.6px #B8AE9C}
.nokta i{display:block;width:12px;height:12px;margin:5px;border-radius:50%;background:var(--lac);opacity:0;transform:scale(.3);transition:opacity .25s var(--ease),transform .25s var(--ease)}
.on .nokta{box-shadow:inset 0 0 0 1.6px var(--lac)}.on .nokta i{opacity:1;transform:none}
/* Stok, butonlar */
.stok{display:flex;align-items:center;gap:10px;margin:20px 16px 0;font-size:14px;font-weight:600;color:var(--lac)}
.ping{position:relative;width:10px;height:10px;border-radius:50%;background:var(--v)}
.ping::after{content:"";position:absolute;inset:0;border-radius:50%;background:var(--v);animation:ping 1.8s var(--ease) 3}
@keyframes ping{from{transform:scale(1);opacity:.7}to{transform:scale(2.8);opacity:0}}
.al{padding:0 16px}
.btn1{display:flex;align-items:center;justify-content:center;gap:12px;width:100%;min-height:62px;margin-top:12px;padding:8px 16px;border:0;border-radius:16px;background:var(--lac)}
.pg .btn1{color:#fff}
.btn1 .b-ic{display:flex;flex-direction:column;align-items:center;line-height:1.2}
.btn1 .b-ic>span{font-size:16px;font-weight:700}
.btn1 .b-ic small{margin-top:2px;font-size:12px;font-weight:600;color:#C9CEE2}
.btn1 svg{width:18px;height:18px;flex:none;fill:none;stroke:#fff;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.btn1[disabled]{background:#E9E2D6;cursor:not-allowed}
.pg .btn1[disabled]{color:var(--lac)}
.btn1[disabled] .b-ic small{color:var(--soluk)}
.btn2{display:flex;align-items:center;justify-content:center;width:100%;min-height:56px;margin-top:12px;border-radius:16px;background:transparent;color:var(--lac);border:1.5px solid var(--lac);font-size:15px;font-weight:600}
/* Teslim, kutu, SSS, yorum */
.yol-k{margin:22px 16px 0}
.blk{margin:24px 16px 0}
.blk h2{margin:0 0 10px;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:22px;letter-spacing:-.01em;color:var(--lac)}
.blk h2 span{color:var(--v)}
.kutu{padding:16px;border-radius:18px;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi);font-size:15px;color:var(--lac);line-height:1.5}
.sss{border-bottom:1px solid var(--cizgi)}
.sss summary{list-style:none;display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:56px;font-weight:700;font-size:15px;color:var(--lac);cursor:pointer}
.sss summary::-webkit-details-marker{display:none}
.sss .arti{flex:none;display:grid;place-items:center;width:30px;height:30px;border-radius:50%;box-shadow:inset 0 0 0 1.5px var(--lac);color:var(--lac);font-size:17px;transition:transform .25s var(--ease)}
.sss[open] .arti{transform:rotate(45deg)}
.sss p{margin:0 0 14px;font-size:14px;color:var(--soluk)}
"""


def ay_ik(f):
    return '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="%s"></path></svg>' % A.E.ay(f)


def tl(x):
    s = ('%.2f' % x).split('.'); n = s[0]; t = ''
    while len(n) > 3: t = '.' + n[-3:] + t; n = n[:-3]
    return '₺' + n + t + ',' + s[1]


def govde(u):
    h = u['handle']; ad = AD.get(h, u['ad'])
    gal = [B + i for i in canli_galeri(u['handle'])]  # Shopify sırası (araclar/canli_galeri.py)
    eski = u['eski'] if u['eski'] and u['eski'] > u['fiyat'] else None
    rozet = '<em class="yok">Tükendi</em>' if not u['stokta'] else ('<em>%%%d indirim</em>' % round((1 - u['fiyat'] / eski) * 100) if eski else '')
    serit = ('  <p class="u-serit" style="background: %s2E">%s</p>\n' % (u['renk']['vurgu'], u['duyuru'])) if u.get('duyuru') else ''
    oz = ''.join('<li>%s<span><b>%s</b><span>%s</span></span></li>' % (ay_ik(.25 + .75 * k / max(1, len(u['ozellikler']) - 1)), o['baslik'], o['aciklama']) for k, o in enumerate(u['ozellikler']))
    sec = ''
    if u.get('secenek'):
        sec = ('  <p class="ust-y">%s</p>\n  <div class="sec"><sc-for list="{{secenek}}" as="s" hint-placeholder-count="2"><button class="{{s.cls}}" type="button" onClick="{{s.pick}}" aria-pressed="{{s.on}}">{{s.n}}</button></sc-for></div>\n' % u['secenek'][0]['ad'])
    pk = ''
    if u.get('paket'):
        pk = ('  <p class="ust-y">Çok al, az öde</p>\n  <div class="pk"><sc-for list="{{paket}}" as="b" hint-placeholder-count="2"><button class="{{b.cls}}" type="button" onClick="{{b.pick}}" aria-pressed="{{b.on}}">'
              '<sc-if value="{{b.rib}}" hint-placeholder-val="{{false}}"><span class="kurdele">En avantajlı</span></sc-if><span class="nokta"><i></i></span>'
              '<span><b>{{b.t}}</b><small>{{b.alt}}</small></span><span class="pf"><strong>{{b.p}}</strong><s>{{b.e}}</s></span></button></sc-for></div>\n')
    if u['stokta']:
        al = ('  <!-- Stok satırı ELLE girilir (Shopify bölüm ayarı: sayı + aç/kapa); boşsa gizlenir -->\n'
              '  <p class="stok"><span class="ping" aria-hidden="true"></span><span>Stokta son <b>[N]</b> adet</span></p>\n'
              '  <div class="al"><button class="btn1" type="button"><span class="b-ic"><span>Güvenli Ödeme ile Al</span><small>Kartla %5 indirim dahil</small></span>' + A.OK + '</button>'
              '<button class="btn2" type="button">Kapıda Ödeme ile Sipariş Ver</button><div class="ay-dis" data-ay-dis></div></div>\n')
    else:
        al = ('  <div class="al" style="margin-top: 18px"><button class="btn1" type="button" disabled><span class="b-ic"><span>Tükendi</span><small>Yeniden gelince haber verelim</small></span></button>'
              '<button class="btn2" type="button">Gelince haber ver</button></div>\n')
    sss = ''.join('<details class="sss"><summary>%s<span class="arti" aria-hidden="true">+</span></summary><p>%s</p></details>' % (q['s'], q['c']) for q in u['sss'])
    return ad, gal, (serit +
        '  <!-- Galeri: sitedeki görseller (uydurma yorum kartı ve sağlık iddialı afişler alınmadı); kaydırılır, 5 sn\'de geçer -->\n'
        '  <div class="urun-ust"><div class="ust-sol">\n'  # masaüstünde sol sütun (galeri); telefonda etkisiz
        '  <div class="gal"><div class="g-iz" onScroll="{{gKay}}"><sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><div class="gs"><img src="{{f.src}}" alt="{{f.alt}}"></div></sc-for></div>'
        '<div class="g-alt" aria-hidden="true"><sc-for list="{{gal}}" as="f" hint-placeholder-count="4"><i class="{{f.acls}}"></i></sc-for></div></div>\n'
        '  </div><div class="ust-sag">\n'  # masaüstünde sağ sütun (satın alma)
        '  <section class="bilgi" id="siparis"><h1>%s<span>.</span></h1><p class="kisa">%s</p>'
        '<p class="fiyat"><b>%s</b>%s%s</p></section>\n' % (ad, u['kisa'], tl(u['fiyat']), '<s>%s</s>' % tl(eski) if eski else '', rozet) +
        '  <ul class="oz-l">' + oz + '</ul>\n' + sec + pk + al +
        '  <ol class="yol-k" aria-label="Siparişten teslime">' + SY.YOL + '</ol>\n  </div></div>\n'
        '  <section class="blk"><h2>Kutuda ne var<span>?</span></h2><p class="kutu">%s</p></section>\n' % u['kutuda'] +
        '  <section class="blk"><h2>Merak edilenler<span>.</span></h2><div style="border-top: 1px solid var(--cizgi)">' + sss + '</div></section>\n'
        '  <!-- Yorumlar: Shopify\'da bu ürünün Loox kutusu (hepsi, m.28/B). Loox: %s -->\n'
        '  <section class="blk"><h2>Alanlar ne diyor<span>?</span></h2><p class="yer" style="margin: 0">[Loox: bu ürünün tüm yorumları]</p></section>\n' % (u['loox'].get('not') or ''))


def js(u, gal):
    pk = u.get('paket') or []
    tek = u['fiyat']
    paket = []
    for b in pk:
        e = b['eski'] if b.get('eski') and b['eski'] > b['fiyat'] else None
        paket.append({'n': b['adet'], 't': '%d Adet' % b['adet'], 'alt': b.get('alt') or '', 'p': tl(b['fiyat']), 'e': tl(e) if e else '', 'f': b['fiyat'], 'rib': b['adet'] == 2})
    sec = (u.get('secenek') or [{}])[0].get('degerler', []) if u.get('secenek') else []
    st = "{ g: 0, gOto: true, pk: %s, sec: 0 }" % ('null' if len(paket) > 1 else '1')  # açılışta paket seçili değil (19 Eki)
    ek = """
    var GAL = """ + json.dumps(gal) + """, AD = """ + json.dumps(AD.get(u['handle'], u['ad']), ensure_ascii=False) + """;
    var gal = GAL.map(function (s, i) { return { src: s, alt: AD + ' görseli ' + (i + 1), ay: AYE((i + 1) / GAL.length), acls: i < S.g ? 'lit' : (i === S.g ? 'lit on' : '') }; });
    function gKay(e) { var el = e && (e.currentTarget || e.target); if (!el || !el.clientWidth) return; var i = Math.round(el.scrollLeft / el.clientWidth), o = {};
      if (i !== self.state.g) o.g = i; if (self.state.gOto && Date.now() - (self.otoKay || 0) > 900) o.gOto = false; if (o.g !== undefined || o.gOto === false) self.setState(o); }
    var PK = """ + json.dumps(paket, ensure_ascii=False) + """;
    var paket = PK.map(function (b) { var on = S.pk === b.n; return { t: b.t, alt: b.alt, p: b.p, e: b.e, rib: b.rib, on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: function () { self.setState({ pk: b.n }); } }; });
    var SEC = """ + json.dumps(sec, ensure_ascii=False) + """;
    var secenek = SEC.map(function (n, i) { var on = S.sec === i; return { n: n, on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: function () { self.setState({ sec: i }); } }; });
    var sp = PK.filter(function (b) { return b.n === S.pk; })[0], tutar = sp ? sp.f : """ + str(tek) + """;
"""
    don = "gal: gal, gKay: gKay, paket: paket, secenek: secenek, kart: TL(Math.round(tutar * 0.95 * 100) / 100, true)"
    base = SY.js(st, ek, don)
    # Galeri: kendiliğinden geçiş (5 sn) ve kaydırma kabını durumda tutma
    base = base.replace("componentDidMount() { var self = this; this.iv = setInterval(function () { self.setState({ now: Date.now() }); }, 1000); }",
        "componentDidMount() { var self = this;\n"
        "    this.tik = 0; this.iv = setInterval(function () { self.tik++; if (self.state.gOto && self.tik % 5 === 0) self.git((self.state.g + 1) % " + str(max(1, len(gal))) + "); self.setState({ now: Date.now() }); }, 1000); }\n"
        "  git(i) { var el = document.querySelector('.g-iz'); if (el && el.scrollTo && el.clientWidth) { this.otoKay = Date.now(); el.scrollTo({ left: i * el.clientWidth, behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); } else this.setState({ g: i }); }\n"
        "  componentDidUpdate() { var el = document.querySelector('.g-iz'); if (el && el.clientWidth && Math.abs(el.scrollLeft - this.state.g * el.clientWidth) > el.clientWidth / 2) { this.otoKay = Date.now(); el.scrollLeft = this.state.g * el.clientWidth; } }")
    assert 'git(i)' in base
    return base


if __name__ == '__main__':
    for u in ICERIK:
        ad, gal, g = govde(u)
        css = CSS.replace('.pg{--v:#F2A65A}', '.pg{--v:%s}' % u['renk']['vurgu'])
        html = '<div class="pg" style="padding-bottom: 0">\n' + SY.DUYURU + SY.UST + g + SY.ALT + SY.YUKARI + '</div>\n'
        dosya = 'U-%s.dc.html' % u['handle']
        open(os.path.join(CANVAS, dosya), 'w', encoding='utf-8').write(HEAD.format(title='Ayluna · ' + ad, css=css) + html + TAIL.format(h=YUK.get(dosya, 3800), js=js(u, gal)))
        print('yazıldı:', dosya, len(gal), 'görsel')
