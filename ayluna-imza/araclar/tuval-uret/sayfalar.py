# Ayluna · kalan sayfalar (18 Eki). Çalıştır: python3 sayfalar.py
# Kullanıcı: "Sitemdeki her kısım burada da aynı şekilde gelmeli… diğer sayfaları da kontrol edip gerekli düzeltmeleri yapabiliriz."
# Kaynak: ogrenme/site-envanter.md §7. Üst bant, menü ve alt bilgi ana sayfayla aynı (anasayfa.py'den).
#   Iletisim     /pages/contact + "Biz Burdayız" kopyası tek sayfada; canlıda yalnız form vardı (adres, saat, kanal yok)
#   Koleksiyon   /collections/all: 15 ürün (frontpage 9'du), filtre ve sıralama; canlıdaki "Tükendi" COD hatası yok
#   KargoTakip   /apps/track123: hazır kamyon görseli yerine teslim çizgisi
#   Politika     İade ve değişim: Shopify şablonundaki "[İADE ADRESİNİ GİRİN]", "indirimdeki ürünler iade edilemez" düzeltildi
#   Kucuk        404, arama, boş sepet (canlıda İngilizce kalan metinler Türkçe)
# Hukuki metinler (KVKK, mesafeli satış, ön bilgilendirme) yazılmaz; sayfada yer tutucu, hukukçu onayı gerekir.
import os, sys, re, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL, TL_JS
import anasayfa as A
CANVAS = os.path.join(HERE, '..', '..', 'canvas')
B = '/_blob/'

DUYURU = re.search(r'  <div class="duyuru[^"]*".*?<\/div>\n', A.HTML, re.S).group(0)
UST = re.search(r'  <header class="ust[^"]*">.*?</header>\n', A.HTML, re.S).group(0)
ALT = re.search(r'  <footer class="alt">.*?</footer>\n', A.HTML, re.S).group(0)
YUKARI = re.search(r'  <button class="yukari".*?</button>\n', A.HTML, re.S).group(0)
OK = A.OK

CSS = A.CSS + r"""
.sb{padding:28px 16px 0}
.sb h1{margin:0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:28px;line-height:1.05;letter-spacing:-.02em;color:var(--lac)}
.sb h1 span{color:var(--amber)}
.sb p{margin:8px 0 0;font-size:15px;color:var(--soluk)}
.kart-k{margin:16px 16px 0;padding:18px;border-radius:20px;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi);color:var(--lac)}
.kart-k h2{margin:0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:22px;letter-spacing:-.01em}
.kart-k p{margin:6px 0 0;font-size:14px;color:var(--soluk)}
.btn-l{display:flex;align-items:center;justify-content:center;gap:10px;width:100%;min-height:52px;margin-top:14px;border:0;border-radius:16px;background:var(--lac);color:#fff;font-size:16px;font-weight:700}
.pg .btn-l{color:#fff}
.btn-l svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.btn-c{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;min-height:52px;margin-top:10px;border-radius:16px;background:transparent;box-shadow:inset 0 0 0 1.5px var(--lac);color:var(--lac);font-size:15px;font-weight:700}
.satirlar{margin:12px 0 0;padding:0;list-style:none}
.satirlar li{display:flex;justify-content:space-between;gap:12px;padding:12px 0;border-top:1px solid var(--cizgi);font-size:14px}
.satirlar li span{color:var(--soluk)}.satirlar li b{text-align:right}
/* Form */
.form{display:flex;flex-direction:column;gap:12px;margin-top:14px}
.form label{display:flex;flex-direction:column;gap:6px;font-size:13px;font-weight:600;color:var(--lac)}
.form input,.form textarea{width:100%;min-height:50px;padding:12px 14px;border:0;border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1.5px var(--cizgi);font:inherit;font-size:16px;color:var(--lac)}
.form textarea{min-height:110px;resize:vertical}
.onay{flex-direction:row!important;align-items:flex-start;gap:10px!important;font-weight:500!important;color:var(--soluk)!important;font-size:13px!important;line-height:1.45}
.onay input{flex:none;width:22px;min-height:22px;height:22px;margin-top:1px;padding:0;accent-color:#1A2142;box-shadow:none}
.onay u{color:var(--lac)}
/* Sekmeler (kargo takip) */
.sekme{display:flex;gap:4px;margin-top:14px;padding:4px;border-radius:999px;background:#EFE6D8}
.sekme button{flex:1;min-height:44px;border:0;border-radius:999px;background:transparent;font-size:14px;font-weight:700;color:var(--soluk)}
.sekme button.on{background:var(--lac);color:#fff}
/* Teslim çizgisi (kargo takip görseli) */
.yol-k{position:relative;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));list-style:none;margin:18px 0 0;padding:0;text-align:center}
.yol-k::before{content:"";position:absolute;left:16.6%;right:16.6%;top:13px;border-top:1.5px dashed var(--cizgi)}
.yol-k li{position:relative;display:flex;flex-direction:column;align-items:center;gap:2px;font-size:13px;color:var(--soluk)}
.yol-k li b{font-size:14px;color:var(--lac)}
.yol-k svg{width:28px;height:28px;margin-bottom:6px;background:var(--kart);border-radius:50%}
.yol-k circle{fill:var(--kart);stroke:var(--lac);stroke-width:1.4}.yol-k path{fill:var(--amber)}
/* Koleksiyon araç çubuğu */
.arac{display:flex;gap:8px;overflow-x:auto;padding:14px 16px 0;scrollbar-width:none}
.arac::-webkit-scrollbar{display:none}
.arac button{flex:none;min-height:44px;padding:0 14px;border:0;border-radius:999px;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi);font-size:14px;font-weight:600;color:var(--lac)}
.arac button.on{background:var(--lac);color:#fff;box-shadow:none}
.sirala{display:flex;align-items:center;justify-content:space-between;padding:12px 16px 0;font-size:13px;color:var(--soluk)}
.sirala button{display:inline-flex;align-items:center;gap:6px;min-height:44px;padding:0;border:0;background:transparent;font-size:14px;font-weight:700;color:var(--lac)}
.uk .ekle-b{display:flex;align-items:center;justify-content:center;min-height:44px;margin-top:8px;border-radius:12px;background:var(--lac);color:#fff;font-size:14px;font-weight:700}
.uk.yok .ekle-b{background:#E9E2D6;color:var(--soluk)}
/* Politika */
.ozet3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin:16px 16px 0}
.ozet3 div{padding:14px 10px;border-radius:16px;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi);text-align:center;color:var(--lac)}
.ozet3 b{display:block;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:26px;letter-spacing:-.02em}
.ozet3 span{display:block;margin-top:2px;font-size:12px;color:var(--soluk);line-height:1.3}
.adim{list-style:none;margin:12px 0 0;padding:0}
.adim li{display:grid;grid-template-columns:36px minmax(0,1fr);gap:12px;padding:12px 0;border-top:1px solid var(--cizgi)}
.adim em{display:grid;place-items:center;width:32px;height:32px;border-radius:50%;background:var(--lac);color:#fff;font-style:normal;font-weight:700;font-size:14px}
.adim b{display:block;font-size:15px}.adim span{display:block;margin-top:2px;font-size:14px;color:var(--soluk)}
.metin{margin:0;padding:0 0 0 18px;font-size:14px;color:var(--soluk);line-height:1.55}
.metin li{margin-top:6px}
.pol-link a{display:flex;align-items:center;justify-content:space-between;min-height:52px;border-top:1px solid var(--cizgi);font-size:15px;font-weight:600;color:var(--lac)}
.pol-link a small{font-size:12px;font-weight:500;color:var(--soluk)}
/* Küçük sayfalar */
.etiket-k{margin:28px 16px 0;padding:6px 10px;border-radius:8px;background:#EFE6D8;font-size:12px;font-weight:700;color:var(--soluk);display:inline-block}
.bos{margin:12px 16px 0;padding:30px 20px;border-radius:24px;background:var(--lac);color:#FFFDF9;text-align:center}
.bos svg.ay404{width:96px;height:96px}
.bos svg.ay404 circle{fill:none;stroke:rgba(255,253,249,.4);stroke-width:1.2}.bos svg.ay404 path{fill:var(--amber)}
.bos h2{margin:12px 0 0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:28px;letter-spacing:-.02em}
.bos p{margin:8px 0 0;font-size:15px;color:#C9CEE2}
.bos a{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:52px;margin-top:16px;padding:0 20px;border-radius:999px;background:#FFFDF9;color:var(--lac);font-weight:700}
.ara{display:flex;align-items:center;gap:10px;margin:12px 16px 0;padding:0 6px 0 14px;min-height:52px;border-radius:16px;background:#fff;box-shadow:inset 0 0 0 1.5px var(--lac)}
.ara svg{width:20px;height:20px;flex:none;fill:none;stroke:var(--lac);stroke-width:1.8;stroke-linecap:round}
.ara input{flex:1;min-width:0;height:52px;border:0;background:transparent;font:inherit;font-size:16px;color:var(--lac)}
.oneri{display:flex;flex-wrap:wrap;gap:8px;margin:12px 16px 0}
.oneri a{display:inline-flex;align-items:center;min-height:44px;padding:0 14px;border-radius:999px;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi);font-size:14px;font-weight:600;color:var(--lac)}
"""


def js(state='{}', ek='', don=''):
    # Ana sayfanın sayaç kodu + sayfaya özel durum
    return """class Component extends DCLogic {
  constructor(p) { super(p); this.state = Object.assign({ now: Date.now() }, """ + state + """); }
  componentDidMount() { var self = this; this.iv = setInterval(function () { self.setState({ now: Date.now() }); }, 1000); }
  componentWillUnmount() { clearInterval(this.iv); }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    """ + TL_JS + """
    function AYE(f) { var r = 9, c = 12, rx = Math.abs(1 - 2 * f) * r; return f >= 1 ? 'M12 3a9 9 0 1 1 0 18a9 9 0 1 1 0-18Z' : 'M' + c + ' ' + (c - r) + 'A' + r + ' ' + r + ' 0 0 1 ' + c + ' ' + (c + r) + 'A' + rx.toFixed(2) + ' ' + r + ' 0 0 ' + (f < .5 ? 0 : 1) + ' ' + c + ' ' + (c - r) + 'Z'; }
    function IKI(n) { return n < 10 ? '0' + n : String(n); }
    var ist = new Date(new Date(S.now || Date.now()).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kalan = Math.max(0, new Date(ist.getFullYear(), ist.getMonth(), ist.getDate(), 23, 59, 59, 999).getTime() - ist.getTime());
    var hh = Math.floor(kalan / 3600000), mi = Math.floor(kalan / 60000) % 60, ss = Math.floor(kalan / 1000) % 60;
    var R = { cd: IKI(hh) + ':' + IKI(mi) + ':' + IKI(ss), cdAy: AYE(Math.max(.02, Math.min(1, kalan / 86400000))), cdAria: 'Bugünkü fiyat garantisinin bitmesine ' + hh + ' saat ' + mi + ' dakika',
      dur: function (e) { if (e && e.preventDefault) e.preventDefault(); } };
    """ + ek + """
    return Object.assign(R, {""" + don + """});
  }
}"""


def sayfa(ad, title, govde, h, state='{}', ek='', don=''):
    html = '<div class="pg" style="padding-bottom: 0">\n' + DUYURU + UST + govde + ALT + YUKARI + '</div>\n'
    open(os.path.join(CANVAS, ad), 'w', encoding='utf-8').write(HEAD.format(title=title, css=CSS) + html + TAIL.format(h=h, js=js(state, ek, don)))
    print('yazıldı:', ad)


# ——— İletişim ———
ILETISIM = ("""
  <!-- Canlıda iki ayrı sayfa (/pages/contact ve "Biz Burdayız" kopyası) yalnız formdu: kanal, saat, adres yoktu. Tek sayfada birleşti. -->
  <section class="sb"><h1>Bize ulaş<span>.</span></h1><p>Sipariş, kargo, iade ve değişim için buradayız.</p></section>
  <div class="kart-k"><h2>İletişim bilgileri</h2><ul class="satirlar">
    <li><span>E-posta</span><b>ecom11001@gmail.com</b></li>
    <li><span>Kargo takip</span><b><a href="#" style="color: var(--lac)">Siparişin nerede?</a></b></li>
    <li><span>Çalışma saatleri</span><b>Hafta içi 09.00–18.00</b></li>
    <li><span>İade adresi</span><b>Destek ekibi iletir</b></li></ul>
    <p style="margin-top: 10px; font-size: 13px">Depo adresimiz güvenlik nedeniyle paylaşılmıyor; iade için sana kod ve yönlendirme gönderiyoruz.</p></div>
  <div class="kart-k"><h2>Mesaj bırak</h2><p>Sipariş numaran varsa yaz, daha hızlı bakalım.</p>
    <form class="form" onSubmit="{{dur}}">
      <label>Adın<input type="text" autocomplete="name" placeholder="Ad Soyad"></label>
      <label>E-posta<input type="email" autocomplete="email" placeholder="ornek@eposta.com"></label>
      <label>Telefon<input type="tel" autocomplete="tel" placeholder="05xx xxx xx xx"></label>
      <label>Mesajın<textarea placeholder="Sipariş numaran ve sorun"></textarea></label>
      <label class="onay"><input type="checkbox"><span>Kişisel verilerimin işlenmesine ilişkin <u>Aydınlatma Metni</u>'ni okudum.</span></label>
      <button class="btn-l" type="submit" style="margin-top: 2px">Gönder</button>
    </form></div>
""")

# ——— Tüm ürünler ———
KAT = {'lunadream-gece-lambasi': 'Gece lambaları', 'lamba': 'Gece lambaları', 'ayluna-cocuk-gece-feneri': 'Gece lambaları', 'ask-saati': 'Gece lambaları',
       'sunset-lamba': 'Gece lambaları', 'dokunmatik-ambiyans-lamba': 'Gece lambaları', 'lunadream-gece-lambasi-v2': 'Gece lambaları',
       'galayx-usb-projektor': 'Projektörler', 'ayluna-galaksi-night-projektor': 'Projektörler', 'galaksiambiyanisigi': 'Projektörler',
       'yildiz-isigi-nemlendirici': 'Nemlendiriciler', 'astronot-oda-nemlendirici-aroma-difuzor': 'Nemlendiriciler', 'aroma-terapi-nemlendirici': 'Nemlendiriciler',
       'ayluna-retro-mini-pikap': 'Diğer', 'egitici-akilli-cizim-tahtasi': 'Diğer'}
URUNLER = [dict(h=h, ad=ad, p=p, c=(c if c and c > p else None), var=v, kat=KAT[h], src=B + A.U(h)) for h, ad, p, c, v in A.URUN]
KOLEKSIYON = ("""
  <section class="sb"><h1>Tüm ürünler<span>.</span></h1><p>{{say}} ürün</p></section>
  <div class="arac"><sc-for list="{{katlar}}" as="k" hint-placeholder-count="5"><button class="{{k.cls}}" onClick="{{k.pick}}" aria-pressed="{{k.on}}">{{k.n}}</button></sc-for></div>
  <div class="sirala"><span>{{stokYazi}}</span><button type="button" onClick="{{sirDegis}}">Sırala: {{sirAd}}<svg viewBox="0 0 24 24" style="width: 16px; height: 16px; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round"><path d="M7 10l5 5 5-5"></path></svg></button></div>
  <!-- Kartta tek buton: canlıda iki buton (sepete + kapıda) dar kartta taşıyordu ve kapıda butonu her kartta yanlışlıkla "Tükendi" diyordu -->
  <div class="izgara"><sc-for list="{{urunler}}" as="u" hint-placeholder-count="6"><div class="{{u.cls}}"><span><img src="{{u.src}}" alt="{{u.ad}}"><sc-if value="{{u.rozet}}" hint-placeholder-val="{{true}}"><em class="{{u.rcls}}">{{u.rozet}}</em></sc-if></span><span><b>{{u.ad}}</b><span class="f"><strong>{{u.p}}</strong><s>{{u.c}}</s></span><button class="ekle-b" type="button">{{u.btn}}</button></span></div></sc-for></div>
""")
KOL_EK = """
    var U = """ + json.dumps(URUNLER, ensure_ascii=False) + """; if (window.Ayluna && window.Ayluna.fiyat) U = window.Ayluna.fiyat(U);
    var KAT = ['Tümü', 'Gece lambaları', 'Projektörler', 'Nemlendiriciler', 'Diğer'];
    var SIR = ['Öne çıkan', 'Fiyat artan', 'Fiyat azalan'];
    var kat = S.kat || 'Tümü', sir = S.sir || 0;
    var L = U.filter(function (u) { return kat === 'Tümü' || u.kat === kat; });
    if (sir === 1) L = L.slice().sort(function (a, b) { return a.p - b.p; }); else if (sir === 2) L = L.slice().sort(function (a, b) { return b.p - a.p; });
    L = L.filter(function (u) { return u.var; }).concat(L.filter(function (u) { return !u.var; }));
    var urunler = L.map(function (u) { return { ad: u.ad, src: u.src, p: TL(u.p, true), c: u.c ? TL(u.c, true) : '', cls: u.var ? 'uk' : 'uk yok',
      rozet: !u.var ? 'Tükendi' : (u.c ? '%' + Math.round((1 - u.p / u.c) * 100) : ''), rcls: u.var ? '' : 'tukendi', btn: u.var ? 'Sepete ekle' : 'Tükendi' }; });
    var katlar = KAT.map(function (k) { var on = k === kat; return { n: k, on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: function () { self.setState({ kat: k }); } }; });
    var stok = L.filter(function (u) { return u.var; }).length;
"""
KOL_DON = "urunler: urunler, katlar: katlar, say: L.length, stokYazi: stok + ' stokta' + (L.length - stok ? ', ' + (L.length - stok) + ' tükendi' : ''), sirAd: SIR[sir], sirDegis: function () { self.setState({ sir: ((S.sir || 0) + 1) % 3 }); }"

# ——— Kargo takip ———
YOL = ''.join('<li><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="%s"></path></svg><b>%s</b>%s</li>' % (A.E.ay(f), b, t)
              for f, b, t in [(.22, 'Sipariş', 'Hazırlanıyor'), (.5, 'Kargoda', 'Yolda'), (1, 'Kapında', 'Teslim')])
TAKIP = ("""
  <!-- Track123 sayfası: hazır "TRACKING" kamyon görseli yerine marka dilinde teslim çizgisi; alanlar uygulamanınki -->
  <section class="sb"><h1>Siparişin<br>nerede<span>?</span></h1><p>Sipariş ya da takip numaranla anında bak.</p></section>
  <div class="kart-k">
    <ol class="yol-k" aria-hidden="true">""" + YOL + """</ol>
    <div class="sekme" role="tablist"><sc-for list="{{sekme}}" as="t" hint-placeholder-count="2"><button class="{{t.cls}}" role="tab" onClick="{{t.pick}}" aria-selected="{{t.on}}">{{t.n}}</button></sc-for></div>
    <form class="form" onSubmit="{{dur}}">
      <sc-if value="{{siparisle}}" hint-placeholder-val="{{true}}"><label>Sipariş numarası<input type="text" placeholder="#1234"></label><label>E-posta ya da telefon<input type="text" placeholder="Siparişte yazdığın"></label></sc-if>
      <sc-if value="{{takiple}}" hint-placeholder-val="{{false}}"><label>Takip numarası<input type="text" placeholder="Kargo takip numarası"></label></sc-if>
      <button class="btn-l" type="submit">Siparişini takip et</button>
    </form></div>
  <div class="kart-k"><h2>Bulamadın mı?</h2><p>Sipariş numaranla bize yaz; kargonun nerede olduğunu biz bakalım.</p><a class="btn-c" href="#">Bize yaz</a>
    <ul class="satirlar"><li><span>Kargoya veriliş</span><b>16.00’ya kadar aynı gün</b></li><li><span>Teslim</span><b>Türkiye geneli 3–7 gün</b></li><li><span>Firmalar</span><b>Aras, DHL, PTT [Yol?]</b></li></ul></div>
""")

# ——— İade ve değişim ———
POLITIKA = ("""
  <!-- Shopify hazır şablonu yerine: "[İADE ADRESİNİ GİRİN]" ve "indirimdeki ürünler iade edilemez" kalktı. Hukuki metin hukukçu onayıyla. -->
  <section class="sb"><h1>İade ve<br>değişim<span>.</span></h1><p>Beğenmezsen 30 gün içinde geri gönder.</p></section>
  <div class="ozet3"><div><b>30</b><span>gün iade</span></div><div><b>₺0</b><span>iade kargosu</span></div><div><b>[10]</b><span>iş günü içinde para iadesi</span></div></div>
  <div class="kart-k"><h2>Nasıl iade ederim?</h2><ol class="adim">
    <li><em>1</em><span><b>Bize yaz</b><span>E-postayla ya da iletişim formundan sipariş numaranı gönder.</span></span></li>
    <li><em>2</em><span><b>İade kodunu al</b><span>Sana iade kodu ve kargo yönlendirmesi gönderiyoruz.</span></span></li>
    <li><em>3</em><span><b>Kargoya ver</b><span>Kodla kargoya bırak; ücret ödemezsin. Ürün bize ulaşınca paran iade edilir.</span></span></li></ol>
    <a class="btn-l" href="#">İade için yaz</a></div>
  <div class="kart-k"><h2>Bilmen gerekenler</h2><ul class="metin">
    <li>İlk 14 gün yasal cayma hakkındır; Ayluna bu süreyi 30 güne uzatır.</li>
    <li>Ürün kutusu ve parçaları eksiksiz olmalı. [Kullanılmış ürün şartı: teyit]</li>
    <li>Kırık ya da eksik gelen ürün için teslim aldığın gün fotoğrafla yaz. [Değişim süreci: teyit]</li>
    <li>Kapıda ödemede ödediğin ₺80 kapıda ödeme ücretinin iadesi: [teyit]</li>
    <li>Para iadesi kartla ödemede karta, kapıda ödemede [IBAN'a] yapılır.</li></ul></div>
  <div class="kart-k pol-link"><h2 style="margin-bottom: 8px">Diğer politikalar</h2>
    <a href="#">Kargo politikası<small>3–7 gün, ücretsiz</small></a><a href="#">Gizlilik ve KVKK<small>Kişisel veriler</small></a>
    <a href="#">Mesafeli Satış Sözleşmesi<small>Sipariş sözleşmesi</small></a><a href="#">Ön Bilgilendirme Formu<small>Siparişten önce</small></a><a href="#">Hizmet şartları<small>Site kullanımı</small></a></div>
""")

# ——— Küçük sayfalar: 404, arama, boş sepet ———
AY404 = '<svg class="ay404" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="%s"></path></svg>' % A.E.ay(.12)
KUCUK = ("""
  <span class="etiket-k">404 · sayfa bulunamadı</span>
  <div class="bos">""" + AY404 + """<h2>Bu sayfa ayın karanlık yüzünde.</h2><p>Aradığın sayfa taşınmış ya da hiç olmamış.</p><a href="#">Ürünlere dön""" + OK.replace('<svg ', '<svg style="width: 16px; height: 16px; fill: none; stroke: currentColor; stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round" ') + """</a></div>
  <span class="etiket-k">Arama</span>
  <label class="ara"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"></circle><path d="M16 16l4 4"></path></svg><input type="search" placeholder="Ne arıyorsun?" aria-label="Ara"></label>
  <div class="oneri"><a href="#">Gece lambası</a><a href="#">Projektör</a><a href="#">Nemlendirici</a><a href="#">LunaDream</a></div>
  <span class="etiket-k">Boş sepet</span>
  <div class="kart-k" style="text-align: center"><h2>Sepetin boş</h2><p>Bu gece tavanda ne olsun? Bir göz at.</p><a class="btn-l" href="#">Ürünlere bak</a><a class="btn-c" href="#">Hesabına giriş yap</a></div>
""")

if __name__ == '__main__':
    sayfa('Iletisim.dc.html', 'Ayluna · İletişim', ILETISIM, int(os.environ.get('H_IL', 2170)))
    sayfa('Koleksiyon.dc.html', 'Ayluna · Tüm ürünler', KOLEKSIYON, int(os.environ.get('H_KO', 3680)), "{ kat: 'Tümü', sir: 0 }", KOL_EK, KOL_DON)
    sayfa('KargoTakip.dc.html', 'Ayluna · Kargo takip', TAKIP, int(os.environ.get('H_KT', 1790)), "{ tab: 0 }",
          "var sekme = ['Sipariş numarası', 'Takip numarası'].map(function (n, i) { var on = (S.tab || 0) === i; return { n: n, on: on ? 'true' : 'false', cls: on ? 'on' : '', pick: function () { self.setState({ tab: i }); } }; });",
          "sekme: sekme, siparisle: (S.tab || 0) === 0, takiple: (S.tab || 0) === 1")
    sayfa('Politika-Iade.dc.html', 'Ayluna · İade ve değişim', POLITIKA, int(os.environ.get('H_PO', 2220)))
    sayfa('Sayfalar-Kucuk.dc.html', 'Ayluna · 404, arama, boş sepet', KUCUK, int(os.environ.get('H_KU', 1800)))
