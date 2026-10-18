# LunaDream · E için yeni bölüm önerileri (Tur 24). Çalıştır: python3 luna_e_bolumler.py
# Kullanıcı: "Satış için daha iyi bir section aklına geldiyse onları da bi göster; influencer çalışmalarımız var,
# belki onlar için bir kısım; birkaç yeni bölüm düşün." Üç öneri, E'nin (B+) diliyle: Young Serif + Onest,
# krem/lacivert/tek amber, ay evresi işareti. Kullanıcı seçerse E'ye eklenir.
#   1 · Annelerin gözünden: influencer videoları (dikey kartlar, hesap çipi, kısa söz)
#   2 · Kapıda öde, içi rahat: kapıda ödeme üç adımda (ay evreleriyle), sonunda kartla ödeme dürtmesi
#   3 · Sıradan bir gece lambası değil: karşılaştırma (yalnız teyitli özellikler)
# Teyitsiz içerik köşeli yer tutucu: [@hesap], [kısa söz], [video].
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL, TL_JS
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE-Bolumler.dc.html')


def ay(f, r=9, c=12):
    rx = abs(1 - 2 * f) * r
    return 'M%d %dA%d %d 0 0 1 %d %dA%.2f %d 0 0 %d %d %dZ' % (c, c - r, r, r, c, c + r, rx, r, 0 if f < .5 else 1, c, c - r)


def evre(f, cls='evre'):
    return '<svg class="%s" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="%s"></path></svg>' % (cls, ay(f))


CSS = r""".pg{background:#F6F1E9;font-size:15px}
.h2{font-size:22px;line-height:1.15}
.h2 span.n{color:#F2A65A}
.bolum{padding:32px 0 36px}
.oneri{display:flex;align-items:center;gap:8px;margin:0 16px 14px;padding-top:14px;border-top:1px dashed #D6CAB6;font-size:12px;font-weight:700;color:#A05A1C}
.oneri .evre{width:14px;height:14px}
.evre circle{fill:none;stroke:#1A2142;stroke-width:1.6}
.evre path{fill:#F2A65A}
.alt{margin:8px 0 0;font-size:14px;color:#5C6078;text-wrap:balance}
.noscroll{scrollbar-width:none}.noscroll::-webkit-scrollbar{display:none}

/* 1 · Annelerin gözünden (influencer): dikey video kartları; üstte hesap çipi, altta kısa söz. Canlıda Shopify videosu,
   ekrandayken sessiz döner, dokununca sesli. Hesap adı ve söz influencer izniyle, birebir. */
.inf{position:relative;flex:0 0 206px;height:366px;scroll-snap-align:start;border-radius:22px;overflow:hidden;background:#0C1027;color:#FFFDF9}
.inf img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.inf::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,16,39,.55) 0,rgba(12,16,39,0) 26%,rgba(12,16,39,0) 52%,rgba(12,16,39,.9) 100%)}
.inf-hesap{position:absolute;left:12px;top:12px;right:12px;z-index:1;display:flex;align-items:center;gap:8px;font-size:13px;font-weight:600}
.inf-av{width:30px;height:30px;flex:none;border-radius:50%;display:grid;place-items:center;background:#FFFDF9;color:#1A2142;font-family:"Young Serif",Georgia,serif;font-size:14px;box-shadow:0 0 0 2px #F2A65A}
.inf-oyna{position:absolute;left:50%;top:44%;z-index:1;width:52px;height:52px;margin:-26px 0 0 -26px;border-radius:50%;display:grid;place-items:center;background:rgba(255,253,249,.94)}
.inf-oyna svg{width:20px;height:20px;fill:#1A2142;margin-left:3px}
.inf-alt{position:absolute;left:14px;right:14px;bottom:14px;z-index:1;display:flex;flex-direction:column;gap:8px}
.inf-alt q{font-family:"Young Serif",Georgia,serif;font-size:16px;line-height:1.3;quotes:"“" "”"}
.inf-alt q::before{content:open-quote}.inf-alt q::after{content:close-quote}
.inf-alt span{font-size:12px;color:#B9BED6}
.inf-not{margin:12px 16px 0;font-size:12px;color:#5C6078}

/* 2 · Kapıda öde, içi rahat: koyu panel, üç adım ay evresiyle dolar; sonunda kartla ödeme dürtmesi (iade verisine göre) */
.kapi{margin:0 16px;padding:24px 16px 20px;border-radius:28px;background:#1A2142;color:#EDE5D8}
.kapi .h2{color:#FFFDF9}
.kapi .alt{color:#B9BED6}
.adim{position:relative;list-style:none;margin:20px 0 0;padding:0}
.adim::before{content:"";position:absolute;left:15px;top:20px;bottom:20px;border-left:1.5px dashed rgba(255,253,249,.25)}
.adim li{position:relative;display:grid;grid-template-columns:32px minmax(0,1fr);gap:14px;align-items:start;padding:8px 0}
.adim .evre{width:32px;height:32px;background:#1A2142;border-radius:50%}
.adim .evre circle{stroke:rgba(255,253,249,.75)}
.adim b{display:block;font-size:16px;color:#FFFDF9}
.adim span{display:block;margin-top:2px;font-size:14px;color:#B9BED6}
.kapi-guven{display:flex;flex-wrap:wrap;gap:4px 10px;margin:16px 0 0;padding-top:14px;border-top:1px solid rgba(255,253,249,.12);font-size:13px;font-weight:600;color:#EDE5D8}
.kapi-guven span+span::before{content:"·";margin-right:10px;color:#F2A65A}
.kapi-dur{display:flex;align-items:center;gap:10px;margin-top:16px;padding:12px 14px;border-radius:16px;background:rgba(255,253,249,.07);font-size:14px;color:#EDE5D8}
.kapi-dur b{color:#F2A65A}
.kapi-dur .evre{width:22px;height:22px;flex:none}
.kapi-dur .evre circle{stroke:rgba(255,253,249,.75)}

/* 3 · Sıradan bir gece lambası değil: iki sütun; LunaDream sütunu lacivert, satırlar yalnız teyitli özellik */
.kars{margin:18px 16px 0;border:1px solid #E3D8C7;border-radius:22px;background:#FFFDF9;overflow:hidden}
.kars-bas,.kars-sat{display:grid;grid-template-columns:minmax(0,1fr) 84px 96px;align-items:stretch}
.kars-bas{font-size:12px;font-weight:700;color:#5C6078}
.kars-bas span{display:grid;place-items:center;padding:12px 8px;text-align:center}
.kars-bas span:first-child{place-items:center start;text-align:left;padding-left:14px}
.kars-bas .ld{background:#1A2142;color:#FFFDF9;border-radius:0}
.kars-sat{border-top:1px solid #E3D8C7;font-size:14px}
.kars-sat>span{padding:13px 8px;display:grid;place-items:center;min-height:52px}
.kars-sat>span:first-child{place-items:center start;padding-left:14px;font-weight:600}
.kars-sat .ld{background:#1A2142;border-top:1px solid rgba(255,253,249,.1)}
.kars-sat .evre{width:20px;height:20px}
.kars-sat .ld .evre circle{stroke:rgba(255,253,249,.75)}
.yok{width:14px;height:1.5px;background:#D6CAB6}
.kars-not{margin:10px 16px 0;font-size:12px;color:#5C6078}
"""

INF = ''.join('''<article class="inf"><img src="/_blob/%s" alt="" style="object-position: %s"><span class="inf-hesap"><span class="inf-av">%s</span>%s</span><span class="inf-oyna" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l11-6.5z"></path></svg></span><span class="inf-alt"><q>%s</q><span>%s</span></span></article>''' % a for a in [
    ('7ad3cbbe71680f4ed3027dbd056e391f', '50% 40%', '@', '[@hesap adı]', '[Videodaki kısa söz]', '[video] · Kız modeli'),
    ('4323cd781a0d687b528b3059505be48c', '50% 35%', '@', '[@hesap adı]', '[Videodaki kısa söz]', '[video] · Kız modeli'),
    ('b2c8d9b92ad3541b532e3aa108a74735', '50% 45%', '@', '[@hesap adı]', '[Videodaki kısa söz]', '[video] · Erkek modeli'),
])

ADIM = ''.join('<li>%s<span><b>%s</b><span>%s</span></span></li>' % (evre(f), b, t) for f, b, t in [
    (.22, 'Siparişini ver', 'Adın, adresin ve telefonun yeter; kart bilgisi istemeyiz.'),
    (.5, 'WhatsApp’tan onayla', 'Siparişini WhatsApp’tan teyit ederiz.'),
    (1, 'Kapıda öde', 'Ürün eline geçince nakit ya da kartla ödersin.'),
])

SATIR = [('Işık verir', True, True), ('Tavana masal yansıtır', False, True), ('6 masal diski + 6 hediye', False, True),
         ('Telefondan ninni çalar', False, True), ('Şarjlı, her odaya taşınır', False, True), ('3 parlaklık ayarı', False, True)]
KARS = ''.join('<div class="kars-sat"><span>%s</span><span>%s</span><span class="ld">%s</span></div>' % (
    a, evre(1) if s1 else '<i class="yok" aria-label="yok"></i>', evre(1)) for a, s1, s2 in SATIR)

HTML = """<div class="pg">
  <!-- Öneri 1 · Annelerin gözünden (influencer) -->
  <section class="bolum">
    <p class="oneri">""" + evre(.22) + """Öneri 1 · Influencer çalışmaları</p>
    <div class="px"><h2 class="h2">Annelerin<br>gözünden<span class="n">.</span></h2><p class="alt">LunaDream’i kendi evlerinde deneyen anneler anlatıyor.</p></div>
    <div class="noscroll" style="display: flex; gap: 10px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-left: 16px; padding: 16px 16px 0">""" + INF + """<span aria-hidden="true" style="flex: 0 0 6px"></span></div>
    <p class="inf-not">Canlıda influencer videoları; hesap adı ve söz izinle, birebir. Yerleşim: Yorumların hemen üstü.</p>
  </section>

  <!-- Öneri 2 · Kapıda öde, içi rahat -->
  <section class="bolum" style="padding-top: 0">
    <p class="oneri">""" + evre(.5) + """Öneri 2 · Kapıda ödeme güveni</p>
    <div class="kapi">
      <h2 class="h2">Kapıda öde,<br>için rahat olsun<span class="n">.</span></h2>
      <p class="alt">Üç adımda kapına gelir.</p>
      <ol class="adim">""" + ADIM + """</ol>
      <p class="kapi-guven"><span>Ücretsiz kargo</span><span>30 gün iade</span><span>Kapıda ₺80 ücret</span></p>
      <p class="kapi-dur">""" + evre(.22) + """<span>Kartla ödersen <b class="tab">{{kartFark}}</b> daha az ödersin.</span></p>
    </div>
    <p class="inf-not">Yerleşim: Satın al butonlarının hemen altı (teslim çizgisinin yerine ya da altına).</p>
  </section>

  <!-- Öneri 3 · Sıradan bir gece lambası değil -->
  <section class="bolum" style="padding-top: 0">
    <p class="oneri">""" + evre(1) + """Öneri 3 · Karşılaştırma</p>
    <div class="px"><h2 class="h2">Sıradan bir gece<br>lambası değil<span class="n">.</span></h2></div>
    <div class="kars">
      <div class="kars-bas"><span></span><span>Sıradan lamba</span><span class="ld">LunaDream</span></div>
      """ + KARS + """
    </div>
    <p class="kars-not">Yalnız teyitli özellikler. Yerleşim: Sihirli özelliklerin altı ya da Diskler'in üstü.</p>
  </section>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = {}; }
  renderVals() {
    """ + TL_JS + """
    var P2 = 2749.99, online = Math.round(P2 * 0.95 * 100) / 100, kapida = P2 + 80;
    return { kartFark: TL(kapida - online, true) };
  }
}"""

open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · E yeni bölüm önerileri', css=CSS) + HTML + TAIL.format(h=int(os.environ.get('B_H', 1837)), js=JS))
print('yazıldı:', os.path.abspath(OUT))
