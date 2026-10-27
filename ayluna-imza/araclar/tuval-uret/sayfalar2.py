# Ayluna · sitenin eksik sayfaları (18 Eki). Çalıştır: python3 sayfalar2.py
# Kullanıcı: "Tüm iskeleti index olarak gönder; önce eksiklerini kontrol et, tüm eksik kısımları düzelt; sepet vesaire her kısım tam çalışsın."
# Denetimde eksik çıkanlar: alt bilgideki politika bağlantılarının sayfası yoktu (kargo, KVKK, mesafeli satış, ön bilgilendirme, hizmet şartları),
# arama sonucu göstermiyordu, 404/arama/boş sepet tek panodaydı, hesap sayfası yoktu, ödeme ve "sipariş alındı" ekranı yoktu.
# Politika metinleri TASLAK: köşeli yerler doldurulmadan ve hukukçu onayı olmadan yayına girmez. Şirket bilgisi (unvan, adres, MERSİS, KEP)
# kullanıcı isteğiyle şimdilik yok (19 Eki: "şirketi de kaldır, sonra kendim ekleyeceğim"); yayından önce eklenmeli (KURULUM.md).
# Ödeme ekranı Shopify'ın kendi ödeme sayfasının önizlemesidir (Shopify'da tema bunu çizmez); kart bilgisi alınmaz.
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sayfalar as SY
import sepet as SP
from ortak import HEAD, TAIL, TL_JS
CANVAS = os.path.join(HERE, '..', '..', 'canvas')
OK = SY.OK

EK_CSS = r"""
.taslak{margin:12px 16px 0;padding:10px 12px;border-radius:12px;background:#FFF4E5;box-shadow:inset 0 0 0 1px #F2C98F;font-size:13px;color:#7A4A12}
.pm{margin:16px 16px 0;padding:18px;border-radius:20px;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi);color:var(--lac)}
.pm h2{margin:0 0 6px;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:20px;letter-spacing:-.01em}
.pm p{margin:8px 0 0;font-size:14px;line-height:1.6;color:var(--soluk)}
.pm ul{margin:8px 0 0;padding-left:18px;font-size:14px;line-height:1.6;color:var(--soluk)}
.pm li{margin-top:4px}
.pm b{color:var(--lac)}
.izg{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin:14px 16px 0}
.izg a{display:flex;flex-direction:column;border-radius:16px;overflow:hidden;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi);color:var(--lac)}
.izg img{width:100%;aspect-ratio:1;object-fit:cover;background:#EFE6D8}
.izg span{display:block;padding:8px 10px 10px;font-size:13px;font-weight:600;line-height:1.3}
.izg em{display:block;margin-top:4px;font-style:normal;font-weight:700;font-variant-numeric:tabular-nums}
.sonuc{margin:14px 16px 0;font-size:13px;color:var(--soluk)}
/* Ödeme önizlemesi */
.o-ust{display:flex;align-items:center;justify-content:space-between;height:60px;padding:0 16px;border-bottom:1px solid var(--cizgi);background:#FFFDF9}
.o-ust .marka b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:20px}
.o-ust span{display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:600;color:var(--soluk)}
.o-ust svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.o-ozet{margin:0;padding:12px 16px;background:#EFE6D8;font-size:14px}
.o-ozet summary{display:flex;justify-content:space-between;align-items:center;min-height:44px;font-weight:700;cursor:pointer;list-style:none}
.o-ozet summary::-webkit-details-marker{display:none}
.o-s{display:grid;grid-template-columns:56px minmax(0,1fr) auto;gap:10px;align-items:center;padding:8px 0;border-top:1px solid var(--cizgi)}
.o-s img{width:56px;height:56px;border-radius:10px;object-fit:cover;background:#fff}
.o-s b{display:block;font-size:14px;line-height:1.3}.o-s small{display:block;font-size:12px;color:var(--soluk)}
.o-s em{font-style:normal;font-weight:700;font-variant-numeric:tabular-nums}
.o-top p{display:flex;justify-content:space-between;margin:6px 0 0;color:var(--soluk);font-variant-numeric:tabular-nums}
.o-top p b{color:var(--lac);font-weight:600}
.o-top .t{margin-top:10px;padding-top:10px;border-top:1px dashed var(--cizgi);color:var(--lac);font-weight:700}
.o-top .t b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:22px}
.o-blok{margin:18px 16px 0}
.o-blok h2{margin:0 0 10px;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:20px;color:var(--lac)}
.o-iki{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.o-sec{display:grid;grid-template-columns:22px minmax(0,1fr) auto;gap:10px;align-items:center;width:100%;min-height:52px;margin-top:8px;padding:8px 12px;border:0;border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1.5px var(--cizgi);text-align:left;font-size:14px;color:var(--lac)}
.o-sec.on{box-shadow:inset 0 0 0 2px var(--lac)}
.o-sec i{width:20px;height:20px;border-radius:50%;box-shadow:inset 0 0 0 1.6px #B8C0D2}
.o-sec.on i{box-shadow:inset 0 0 0 6px var(--lac)}
.o-sec small{display:block;font-size:12px;color:var(--soluk)}
.o-sec em{font-style:normal;font-weight:700;font-variant-numeric:tabular-nums}
.o-kart{margin-top:8px;padding:14px;border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1.5px var(--cizgi);font-size:13px;color:var(--soluk)}
.o-kart div{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px}
.o-kart span{display:block;min-height:46px;padding:12px;border-radius:10px;background:#F6F1E9;color:#9AA0B8}
.o-kart span.g{grid-column:1/-1}
.o-hata{min-height:20px;margin:10px 16px 0;font-size:13px;font-weight:600;color:#B3261E}
.o-not{margin:10px 16px 0;font-size:12px;color:var(--soluk);text-align:center}
/* Sipariş alındı */
.tamam{margin:20px 16px 0;padding:28px 20px 22px;border-radius:24px;background:var(--lac);color:#FFFDF9;text-align:center}
.tamam svg{width:84px;height:84px}
.tamam circle{fill:none;stroke:rgba(255,253,249,.35);stroke-width:1.2}.tamam path{fill:var(--amber);transform-origin:12px 12px;animation:dol 1.2s cubic-bezier(.2,.7,.2,1) both}
@keyframes dol{from{opacity:0;transform:scale(.6) rotate(-40deg)}to{opacity:1;transform:none}}
.tamam h1{margin:10px 0 0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:30px;letter-spacing:-.02em}
.tamam p{margin:6px 0 0;font-size:15px;color:#C9CEE2}
.tamam b{color:#fff}
"""
CSS = SY.CSS + EK_CSS


def kart(baslik, *paragraflar):
    return '<div class="pm"><h2>%s</h2>%s</div>' % (baslik, ''.join(paragraflar))


def P(t): return '<p>%s</p>' % t


def L(*m): return '<ul>' + ''.join('<li>%s</li>' % x for x in m) + '</ul>'


TASLAK = '<p class="taslak">Taslak metin: köşeli yerler doldurulup hukukçuya onaylatılmadan yayına girmez.</p>'

POLITIKA = {
    'Politika-Kargo.dc.html': ('Ayluna · Kargo ve teslimat', 'Kargo ve<br>teslimat', 'Kargo ücretsiz; 16.00’ya kadar verilen sipariş aynı gün kargoda.', [
        kart('Süreler', L('<b>Kargoya veriliş:</b> iş günü 16.00’ya kadar verilen sipariş aynı gün, sonrakiler ertesi iş günü kargoya verilir (hafta sonu ve resmî tatiller hariç).',
                         '<b>Teslim:</b> Türkiye geneli 3–7 iş günü.', '<b>Hızlı Kargo (₺79,99):</b> sepette seçilirse sipariş sıranın önüne alınır, öncelikli hazırlanıp kargolanır.',
                         'Yasal üst sınır: sipariş en geç 30 gün içinde teslim edilir; gecikirse sana haber verir, istersen siparişi iptal ederiz.')),
        kart('Ücretler', L('Kargo tüm siparişlerde ücretsiz.', 'Kartla ödemede %5 indirim uygulanır.')),
        kart('Kargo firmaları ve takip', L('Aras Kargo, DHL, PTT [hangisi ne zaman kullanılıyor: teyit].', 'Kargoya verilince takip numarası SMS ve e-postayla gelir; "Kargo takip" sayfasından da bakabilirsin.')),
        kart('Teslimatta', L('Paket hasarlıysa kargo görevlisine tutanak tutturup teslim almayabilirsin.', 'Kırık ya da eksik ürün için teslim aldığın gün fotoğrafla bize yaz; değişim ya da iade ücretsiz.',
                             'Adreste bulunamazsan paket kargo şubesinde [X] gün bekler.', 'Yurt dışına gönderim yapılmıyor.')),
    ]),
    'Politika-KVKK.dc.html': ('Ayluna · Gizlilik ve KVKK', 'Gizlilik ve<br>KVKK', 'Kişisel verilerini neden ve nasıl işliyoruz.', [
        TASLAK,
        kart('Hangi verileri işliyoruz?', L('Kimlik ve iletişim: ad soyad, telefon, e-posta.', 'Teslimat: adres, il, ilçe.', 'Sipariş: aldığın ürünler, tutar, ödeme yolu, sipariş geçmişi.',
                                           'Kart bilgilerin bize gelmez; ödeme kuruluşunun güvenli sayfasında işlenir.', 'Site kullanımı: çerezler ve benzeri teknolojiler (izin verdiğin ölçüde).')),
        kart('Neden işliyoruz? (hukuki sebep)', L('Siparişini almak, göndermek ve iade/değişimini yapmak: sözleşmenin kurulması ve ifası (KVKK m.5/2-c).',
                                                 'Fatura ve kayıt yükümlülükleri: kanunlarda öngörülme ve hukuki yükümlülük (m.5/2-a, ç).', 'Sorularını yanıtlamak, dolandırıcılığı önlemek: meşru menfaat (m.5/2-f).',
                                                 'Kampanya e-postası, SMS ve reklam çerezleri: yalnız açık rızanla; istediğin an geri alabilirsin.')),
        kart('Kimlerle paylaşıyoruz?', L('Kargo firmaları (teslimat için).', 'Ödeme kuruluşu (kartla ödemede).', 'Altyapı ve hizmet sağlayıcılar: Shopify (mağaza altyapısı, yurt dışında), yorum (Loox) ve kargo takip uygulamaları.',
                                         'Reklam ölçümü (Meta) yalnız çerez iznin varsa.', 'Yetkili kamu kurumları (talep olursa).', 'Yurt dışına aktarım KVKK m.9\'a uygun yapılır. [Aktarım dayanağı: teyit]')),
        kart('Ne kadar saklıyoruz?', P('Sipariş ve fatura kayıtları ilgili kanunlardaki süre boyunca [10 yıl, teyit]; pazarlama izinleri geri alınana kadar; diğerleri amaç bitince silinir ya da anonimleştirilir.')),
        kart('Hakların (KVKK m.11)', L('Verinin işlenip işlenmediğini öğrenme, bilgi isteme.', 'Yanlışsa düzeltilmesini, gerekmiyorsa silinmesini isteme.', 'Aktarıldığı kişileri öğrenme.',
                                      'Otomatik analizle aleyhine sonuca itiraz etme.', 'Zarar varsa giderilmesini isteme.'),
             P('Başvuru: ecom11001@gmail.com. En geç 30 gün içinde yanıtlıyoruz.')),
        kart('Çerezler', P('Zorunlu çerezler sepet ve ödeme için kullanılır. Ölçüm ve reklam çerezleri (Meta pikseli gibi) yalnız izin verirsen çalışır. [Çerez izin bandı: Shopify müşteri gizliliği ayarı]')),
    ]),
    'Politika-Mesafeli.dc.html': ('Ayluna · Mesafeli satış sözleşmesi', 'Mesafeli satış<br>sözleşmesi', '6502 sayılı Tüketicinin Korunması Hakkında Kanun ve Mesafeli Sözleşmeler Yönetmeliği uyarınca.', [
        TASLAK,
        kart('1. Taraflar', P('<b>Satıcı:</b> Ayluna (ayluna.shop)'), P('<b>Alıcı:</b> siparişte bilgilerini yazan kişi (ad soyad, adres, telefon, e-posta sipariş özetindedir).')),
        kart('2. Konu', P('Alıcının ayluna.shop üzerinden elektronik ortamda siparişini verdiği ürünün satışı ve teslimine ilişkin hak ve yükümlülükler.')),
        kart('3. Ürün ve fiyat', L('Ürünün temel nitelikleri, adedi, satış fiyatı (KDV dahil) ve varsa ek ürünler sipariş özetinde ve ürün sayfasında yazar.',
                                  'Ödeme kartla yapılır; kartla ödemede %5 indirim uygulanır. Kargo ücretsizdir; Hızlı Kargo seçilirse ₺79,99.')),
        kart('4. Teslimat', L('Ürün alıcının yazdığı adrese kargoyla teslim edilir; sipariş 1 iş gününde kargoya verilir, teslim 3–7 iş günüdür.', 'Teslim süresi yasal 30 günü geçemez.',
                             'Hasarlı paket kargo görevlisine tutanakla bildirilir.')),
        kart('5. Cayma hakkı', L('Alıcı, ürünü teslim aldığı günden itibaren <b>14 gün</b> içinde gerekçe göstermeden ve cezai şart ödemeden cayabilir. Ayluna bu süreyi <b>30 güne</b> uzatır.',
                                'Cayma bildirimi e-postayla (ecom11001@gmail.com) yapılır. Satıcı iade kodu gönderir; iade kargosu ücretsizdir.',
                                'Ürün, bildirimden sonra 10 gün içinde eksiksiz geri gönderilir. Bedel, ürün satıcıya ulaştıktan sonra en geç 14 gün içinde ödemenin yapıldığı karta iade edilir.')),
        kart('6. Cayma hakkının kullanılamadığı durumlar', P('Yönetmelik m.15\'te sayılan hâller (ör. alıcının isteğiyle kişiye özel hazırlanan ürünler). Ayluna ürünlerinde bu istisna [yok, teyit].')),
        kart('7. Uyuşmazlık', P('Şikâyet ve itirazlar, Ticaret Bakanlığının her yıl belirlediği parasal sınırlar içinde alıcının ya da satıcının yerleşim yerindeki Tüketici Hakem Heyetine, sınırı aşanlar Tüketici Mahkemesine yapılır.')),
        kart('8. Yürürlük', P('Alıcı, siparişi onaylamadan önce ön bilgilendirme formunu okuduğunu ve bu sözleşmeyi kabul ettiğini beyan eder. Sözleşme siparişin onaylandığı anda kurulur.')),
    ]),
    'Politika-OnBilgi.dc.html': ('Ayluna · Ön bilgilendirme formu', 'Ön bilgilendirme<br>formu', 'Siparişini onaylamadan önce bilmen gerekenler.', [
        TASLAK,
        kart('Ürün ve ödeme', L('Ürünün temel nitelikleri ürün sayfasında, toplam fiyatı (KDV dahil) sipariş özetinde yazar.', 'Ödeme: kartla (%5 indirimli).',
                               'Kargo ücretsiz; Hızlı Kargo ₺79,99.')),
        kart('Teslimat', P('1 iş gününde kargoda, Türkiye geneli 3–7 iş gününde teslim; en geç 30 gün.')),
        kart('Cayma hakkı', P('Teslimden itibaren 14 gün yasal cayma hakkın var; Ayluna bunu 30 güne uzatır. İade kargosu ücretsizdir. Ayrıntı: Mesafeli Satış Sözleşmesi ve İade sayfası.')),
        kart('Şikâyet', P('E-postayla bize yaz. Çözülmezse Tüketici Hakem Heyeti ya da Tüketici Mahkemesine başvurabilirsin.')),
    ]),
    'Politika-Hizmet.dc.html': ('Ayluna · Hizmet şartları', 'Hizmet<br>şartları', 'ayluna.shop\'u kullanma koşulları.', [
        TASLAK,
        kart('Fiyat ve stok', L('Fiyatlar KDV dahildir. Açık bir yazım hatasında siparişi onaylamadan önce seni ararız.', 'Stok elle güncellenir; ürün tükenirse ödemen iade edilir ya da ürün gelince haber veririz.',
                               '"Bugüne özel fiyat" sayacı her gece 23.59\'da (İstanbul) sıfırlanır; ertesi gün fiyat değişebilir.')),
        kart('Görseller', P('Ürün görselleri temsilîdir; yansıtılan görüntünün büyüklüğü odaya ve mesafeye göre değişir.')),
        kart('Yorumlar', P('Yorumlar yalnız ürünü satın alanlardan toplanır; olumlu ya da olumsuz hiçbir yorum gizlenmez.')),
        kart('Fikrî haklar', P('Sitedeki metin, görsel ve tasarımların hakları satıcıya aittir; izinsiz kullanılamaz.')),
        kart('Değişiklik ve hukuk', P('Bu şartlar güncellenebilir; güncel sürüm bu sayfadadır. Türkiye Cumhuriyeti hukuku uygulanır.')),
    ]),
}


def politika(dosya):
    title, bas, alt, kartlar = POLITIKA[dosya]
    return ('  <section class="sb"><h1>%s<span>.</span></h1><p>%s</p></section>\n  ' % (bas, alt) + '\n  '.join(kartlar) +
            '\n  <div class="kart-k pol-link"><h2 style="margin-bottom: 8px">Diğer politikalar</h2><a href="#">İade politikası<small>30 gün, iade kargosu ücretsiz</small></a>'
            '<a href="#">Kargo politikası<small>3–7 gün, ücretsiz</small></a><a href="#">Gizlilik ve KVKK<small>Kişisel veriler</small></a>'
            '<a href="#">Mesafeli Satış Sözleşmesi<small>Sipariş sözleşmesi</small></a><a href="#">Ön Bilgilendirme Formu<small>Siparişten önce</small></a><a href="#">Hizmet şartları<small>Site kullanımı</small></a></div>\n')


# ——— Arama: yazdıkça süzer; öneri çipleri ———
ARAMA = ("""
  <section class="sb"><h1>Ara<span>.</span></h1><p>Ürün adı ya da tür yaz.</p></section>
  <label class="ara"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"></circle><path d="M16 16l4 4"></path></svg><input type="search" placeholder="Ne arıyorsun?" aria-label="Ara" value="{{q}}" onInput="{{yaz}}" autocomplete="off"></label>
  <div class="oneri"><sc-for list="{{cip}}" as="c" hint-placeholder-count="4"><button class="{{c.cls}}" type="button" onClick="{{c.pick}}" style="display: inline-flex; align-items: center; min-height: 44px; padding: 0 14px; border: 0; border-radius: 999px; background: var(--kart); box-shadow: inset 0 0 0 1px var(--cizgi); font-size: 14px; font-weight: 600; color: var(--lac)">{{c.n}}</button></sc-for></div>
  <p class="sonuc" aria-live="polite">{{sonuc}}</p>
  <div class="izg"><sc-for list="{{bulunan}}" as="u" hint-placeholder-count="4"><a href="#"><img src="{{u.src}}" alt="{{u.ad}}"><span>{{u.ad}}<em>{{u.p}}</em></span></a></sc-for></div>
""")
ARAMA_EK = """
    var U = """ + json.dumps([dict(h=u['h'], ad=u['ad'], p=u['p'], kat=u['kat'], src=u['src'], var=u['var']) for u in SY.URUNLER], ensure_ascii=False) + """; if (window.Ayluna && window.Ayluna.fiyat) U = window.Ayluna.fiyat(U);
    function N(s) { return (s || '').toLocaleLowerCase('tr'); }
    var q = S.q === undefined ? (decodeURIComponent(((location.search + location.hash).match(/[?&]q=([^&]*)/) || [])[1] || '')) : S.q;
    var BUL = U.filter(function (u) { return !q || N(u.ad + ' ' + u.kat).indexOf(N(q).replace(/ları$|leri$/, '')) >= 0 || (N(q) === 'projektör' && u.kat === 'Projektörler') || (N(q) === 'nemlendirici' && u.kat === 'Nemlendiriciler') || (N(q) === 'gece lambası' && u.kat === 'Gece lambaları'); });
    var cip = ['Gece lambası', 'Projektör', 'Nemlendirici', 'LunaDream'].map(function (n) { var on = N(n) === N(q); return { n: n, cls: on ? 'on' : '', pick: function () { self.setState({ q: n }); } }; });
"""
ARAMA_DON = "q: q, yaz: function (e) { self.setState({ q: e.target.value }); }, cip: cip, bulunan: BUL.map(function (u) { return { ad: u.ad, src: u.src, p: u.var ? TL(u.p, true) : 'Tükendi' }; }), sonuc: q ? BUL.length + ' sonuç: \"' + q + '\"' : 'Tüm ürünler (' + U.length + ')'"

AY404 = SY.AY404
S404 = ("""
  <div class="bos" style="margin-top: 24px">""" + AY404 + """<h2>Bu sayfa ayın karanlık yüzünde.</h2><p>Aradığın sayfa taşınmış ya da hiç olmamış.</p><a href="#">Ürünlere dön""" + OK.replace('<svg ', '<svg style="width: 16px; height: 16px; fill: none; stroke: currentColor; stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round" ') + """</a></div>
  <label class="ara" style="margin-top: 20px"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"></circle><path d="M16 16l4 4"></path></svg><input type="search" placeholder="Ne arıyorsun?" aria-label="Ara" onKeyDown="{{araGit}}"></label>
  <div class="oneri"><a href="#">Gece lambası</a><a href="#">Projektör</a><a href="#">Nemlendirici</a><a href="#">LunaDream</a></div>
""")
S404_DON = "araGit: function (e) { if (e.key === 'Enter' && window.Ayluna) window.Ayluna.git('arama.html?q=' + encodeURIComponent(e.target.value)); }"

HESAP = ("""
  <!-- Shopify müşteri hesabı (yeni hesaplar): e-postayla 6 haneli kod; şifre yok -->
  <section class="sb"><h1>Hesabın<span>.</span></h1><p>Siparişlerini görmek için e-postanla giriş yap.</p></section>
  <div class="kart-k"><h2>Giriş yap</h2><p>E-postana 6 haneli bir kod gönderiyoruz; şifre gerekmez.</p>
    <form class="form"><label>E-posta<input type="email" autocomplete="email" placeholder="ornek@eposta.com"></label><button class="btn-l" type="submit">Kod gönder</button></form></div>
  <div class="kart-k"><h2>Hesap şart değil</h2><p>Hesap açmadan da sipariş verebilirsin. Siparişin nerede diye bakmak için sipariş numaran yeter.</p><a class="btn-c" href="#">Kargo takip</a></div>
""")

# ——— Ödeme önizlemesi (Shopify checkout'un yerini tutar) ———
KILIT = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="9" rx="2"></rect><path d="M8 11V8a4 4 0 0 1 8 0v3"></path></svg>'
ODEME = ("""<div class="pg" style="padding-bottom: 24px">
  <div class="o-ust"><a class="marka" href="#" aria-label="Ayluna ana sayfa" style="display: flex; align-items: center; gap: 6px; color: var(--lac)">""" + SY.A.E.isaret(22, 'rgba(26,33,66,.45)') + """<b>Ayluna</b></a><span>""" + KILIT + """Güvenli ödeme</span></div>
  <details class="o-ozet" open><summary><span>Sipariş özeti</span><span>{{toplam}}</span></summary>
    <sc-for list="{{satirlar}}" as="u" hint-placeholder-count="1"><div class="o-s"><img src="{{u.img}}" alt=""><span><b>{{u.ad}}</b><small>{{u.varyant}}</small></span><em>{{u.tutar}}</em></div></sc-for>
    <sc-for list="{{ekler}}" as="u" hint-placeholder-count="0"><div class="o-s"><img src="{{u.img}}" alt=""><span><b>{{u.ad}}</b><small>Siparişine özel</small></span><em>{{u.tutar}}</em></div></sc-for>
    <div class="o-top"><p><span>Ara toplam</span><b>{{ara}}</b></p><p><span>Kargo</span><b>{{kargo}}</b></p><p><span>Kartla ödeme indirimi (%5)</span><b>−{{indirim}}</b></p><p class="t"><span>Toplam</span><b>{{toplam}}</b></p></div>
  </details>
  <form data-kendi onSubmit="{{gonder}}" novalidate>
  <div class="o-blok"><h2>İletişim</h2><div class="form" style="margin: 0"><label>E-posta<input name="eposta" type="email" autocomplete="email" placeholder="Sipariş bilgisi buraya gelir"></label></div></div>
  <div class="o-blok"><h2>Teslimat adresi</h2><div class="form" style="margin: 0">
    <div class="o-iki"><label>Ad<input name="ad" autocomplete="given-name"></label><label>Soyad<input name="soyad" autocomplete="family-name"></label></div>
    <label>Adres<input name="adres" autocomplete="street-address" placeholder="Mahalle, sokak, no, daire"></label>
    <div class="o-iki"><label>İl<input name="il" autocomplete="address-level1"></label><label>İlçe<input name="ilce" autocomplete="address-level2"></label></div>
    <label>Telefon<input name="tel" type="tel" autocomplete="tel" placeholder="05xx xxx xx xx"></label></div></div>
  <div class="o-blok"><h2>Kargo</h2><sc-for list="{{kargolar}}" as="k" hint-placeholder-count="2"><button class="{{k.cls}}" type="button" onClick="{{k.pick}}" aria-pressed="{{k.on}}"><i></i><span>{{k.n}}<small>{{k.t}}</small></span><em>{{k.p}}</em></button></sc-for></div>
  <div class="o-blok"><h2>Ödeme</h2>
    <div class="o-sec on" role="img" aria-label="Kart ile öde seçili"><i></i><span>Kartla öde<small>Tüm kredi ve banka kartları · %5 indirim</small></span><em>VISA · MC · Troy</em></div>
    <div class="o-kart">Kart bilgilerin ödeme kuruluşunun güvenli alanına girilir, Ayluna'ya gelmez.<div><span class="g">Kart numarası</span><span>AA / YY</span><span>CVC</span><span class="g">Kart üzerindeki ad</span></div></div>
</div>
  <p class="o-hata" role="alert">{{hata}}</p>
  <div style="margin: 0 16px"><button class="btn-l" type="submit">Şimdi öde · {{toplam}}</button></div>
  <p class="o-not">Siparişi onaylayarak Ön Bilgilendirme Formu'nu ve Mesafeli Satış Sözleşmesi'ni kabul edersin. Bu ekran Shopify ödeme sayfasının önizlemesidir; kart bilgisi alınmaz.</p>
  </form>
</div>
""")
DEMO = json.dumps({'satirlar': [{'id': 'ld', 'ad': 'LunaDream Gece Lambası', 'varyant': '2 adet · Kız + Erkek', 'birim': 2749.99, 'adet': 1, 'img': '/_blob/' + SP.IMG['ld']}], 'ekler': {}, 'hizli': False}, ensure_ascii=False)
EKLER = json.dumps([dict(k=e['k'], n=e['n'], p=e['p'], img='/_blob/' + e['img']) for e in SP.EKLER], ensure_ascii=False)
ODEME_JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { hata: '', demo: """ + DEMO + """ }; }
  componentDidMount() { var self = this; window.addEventListener('ayluna-sepet', function () { self.setState({}); }); if (window.AylunaSepet && !window.AylunaSepet.oku().satirlar.length && window.Ayluna) window.Ayluna.git('sepet.html'); }
  renderVals() {
    var self = this, S = this.state, SP = window.AylunaSepet;
    """ + TL_JS + """
    var sp = SP ? SP.oku() : S.demo, E = """ + EKLER + """, ek = sp.ekler || {};
    var ara = 0; sp.satirlar.forEach(function (x) { ara += x.birim * x.adet; });
    var ekL = E.filter(function (e) { return ek[e.k]; }); ekL.forEach(function (e) { ara += e.p; });
    var kargo = sp.hizli ? 79.99 : 0, ind = Math.round(ara * 0.05 * 100) / 100, top = Math.round((ara - ind + kargo) * 100) / 100;
    function hizli(h) { if (SP) SP.hizli(h); else { var d = JSON.parse(JSON.stringify(S.demo)); d.hizli = h; self.setState({ demo: d }); } }
    return {
      satirlar: sp.satirlar.map(function (x) { return { ad: x.ad, varyant: x.varyant + (x.adet > 1 ? ' · ×' + x.adet : ''), img: x.img, tutar: TL(x.birim * x.adet, true) }; }),
      ekler: ekL.map(function (e) { return { ad: e.n, img: e.img, tutar: TL(e.p, true) }; }),
      ara: TL(ara, true), kargo: kargo ? TL(kargo, true) : 'Ücretsiz', indirim: TL(ind, true), toplam: TL(top, true), hata: S.hata,
      kargolar: [{ n: 'Standart kargo', t: '16.00’ya kadar aynı gün kargoda, 3–7 günde kapında', p: 'Ücretsiz', h: false }, { n: 'Hızlı Kargo', t: 'Öncelikli hazırlanır ve kargolanır', p: TL(79.99, true), h: true }]
        .map(function (k) { var on = !!sp.hizli === k.h; return { n: k.n, t: k.t, p: k.p, on: on ? 'true' : 'false', cls: on ? 'o-sec on' : 'o-sec', pick: function () { hizli(k.h); } }; }),
      kapida: function () { if (window.Ayluna) window.Ayluna.kapidaAc(); },
      gonder: function (e) { e.preventDefault(); var f = e.target, d = {};
        ['eposta', 'ad', 'soyad', 'adres', 'il', 'ilce', 'tel'].forEach(function (k) { d[k] = (f.elements[k].value || '').trim(); });
        var h = !/^\\S+@\\S+\\.\\S+$/.test(d.eposta) ? 'E-postanı yaz.' : !d.ad || !d.soyad ? 'Adını ve soyadını yaz.' : d.adres.length < 10 ? 'Açık adresi yaz.' : !d.il || !d.ilce ? 'İl ve ilçeyi yaz.' : !/^0?5\\d{9}$/.test(d.tel.replace(/\\D/g, '')) ? 'Telefonu 05xx xxx xx xx biçiminde yaz.' : '';
        self.setState({ hata: h }); if (!h && window.Ayluna) window.Ayluna.siparisVer('kart', d); }
    };
  }
}"""

# ——— Sipariş alındı (Shopify'da teşekkür sayfası; tema değil, ödeme ayarları) ———
TAMAM_AY = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M12 3a9 9 0 1 1 0 18a9 9 0 1 1 0-18Z"></path></svg>'
TAMAM = ("""
  <div class="tamam">""" + TAMAM_AY + """<h1>Siparişin alındı.</h1><p>Sipariş numaran <b>{{no}}</b>. {{yolYazi}}</p></div>
  <div class="kart-k"><h2>Sırada ne var?</h2><ol class="adim">
    <li><em>1</em><span><b>{{adim1}}</b><span>{{adim1t}}</span></span></li>
    <li><em>2</em><span><b>İş günü 16.00’ya kadar aynı gün kargoda</b><span>Takip numarası SMS ve e-postayla gelir.</span></span></li>
    <li><em>3</em><span><b>3–7 günde kapında</b><span>{{adim3}}</span></span></li></ol></div>
  <div class="kart-k"><h2>Özet</h2><ul class="satirlar"><sc-for list="{{satirlar}}" as="u" hint-placeholder-count="1"><li><span>{{u.ad}}</span><b>{{u.tutar}}</b></li></sc-for>
    <li><span>Kargo</span><b>{{kargo}}</b></li>
    <sc-if value="{{indVar}}" hint-placeholder-val="{{true}}"><li><span>Kartla ödeme indirimi</span><b>−{{ind}}</b></li></sc-if><li><span><b style="color: var(--lac)">Toplam</b></span><b>{{toplam}}</b></li></ul>
    <p style="margin-top: 10px">{{adres}}</p></div>
  <div style="margin: 16px 16px 0"><a class="btn-l" href="#">Kargo takip</a><a class="btn-c" href="#">Alışverişe devam et</a></div>
""")
TAMAM_EK = """
    var o = null; try { o = JSON.parse(localStorage.getItem('ayluna-son-siparis')); } catch (e) {}
    if (!o) o = { no: '#1042', yol: 'kart', adres: { ad: 'Ayşe', soyad: 'Y.', il: 'İstanbul', ilce: 'Kadıköy' }, sepet: { satirlar: [{ ad: 'LunaDream Gece Lambası', birim: 2749.99, adet: 1 }], ekler: {}, hizli: false }, toplam: { kargo: 0, indirim: 137.5, toplam: 2612.49 }, ekler: [] };
    var kp = o.yol === 'kapida', sat = o.sepet.satirlar.map(function (x) { return { ad: x.ad + (x.adet > 1 ? ' ×' + x.adet : ''), tutar: TL(x.birim * x.adet, true) }; });
    (o.ekler || []).forEach(function (e) { if (o.sepet.ekler && o.sepet.ekler[e.k]) sat.push({ ad: e.n, tutar: TL(e.p, true) }); });
    var a = o.adres || {};
"""
TAMAM_DON = ("no: o.no, yolYazi: kp ? 'Ödemeyi ürün kapına gelince yapacaksın.' : 'Ödemen alındı.', adim1: kp ? 'Sipariş onayı' : 'E-posta onayı', "
             "adim1t: kp ? 'Siparişin onaylanınca hazırlanıp kargoya verilir.' : 'Sipariş özetin e-postana gönderildi.', "
             "adim3: kp ? 'Kapıda ' + TL(o.toplam.toplam, true) + ' ödersin (nakit ya da kart).' : 'Beğenmezsen 30 gün içinde ücretsiz iade.', "
             "satirlar: sat, kargo: o.toplam.kargo ? TL(o.toplam.kargo, true) : 'Ücretsiz', kapidaVar: kp, indVar: !kp && o.toplam.indirim > 0, ind: TL(o.toplam.indirim || 0, true), toplam: TL(o.toplam.toplam, true), "
             "adres: [((a.ad || '') + ' ' + (a.soyad || '')).trim(), a.ilce, a.il].filter(Boolean).join(' · ')")

SAYFALAR = [
    ('Politika-Kargo.dc.html', None), ('Politika-KVKK.dc.html', None), ('Politika-Mesafeli.dc.html', None), ('Politika-OnBilgi.dc.html', None), ('Politika-Hizmet.dc.html', None),
]


def yaz(ad, title, govde, h, state='{}', ek='', don=''):
    html = '<div class="pg" style="padding-bottom: 0">\n' + SY.DUYURU + SY.UST + govde + SY.ALT + SY.YUKARI + '</div>\n'
    open(os.path.join(CANVAS, ad), 'w', encoding='utf-8').write(HEAD.format(title=title, css=CSS) + html + TAIL.format(h=h, js=SY.js(state, ek, don)))
    print('yazıldı:', ad)


if __name__ == '__main__':
    for d, _ in SAYFALAR:
        yaz(d, POLITIKA[d][0], politika(d), int(os.environ.get('H_' + d.split('.')[0].replace('-', '_'), 2600)))
    yaz('Arama.dc.html', 'Ayluna · Ara', ARAMA, int(os.environ.get('H_ARAMA', 2200)), "{}", ARAMA_EK, ARAMA_DON)
    yaz('Sayfa404.dc.html', 'Ayluna · Sayfa bulunamadı', S404, int(os.environ.get('H_404', 1500)), "{}", '', S404_DON)
    yaz('Hesap.dc.html', 'Ayluna · Hesabın', HESAP, int(os.environ.get('H_HESAP', 1500)))
    yaz('SiparisAlindi.dc.html', 'Ayluna · Siparişin alındı', TAMAM, int(os.environ.get('H_TAMAM', 1900)), "{}", TAMAM_EK, TAMAM_DON)
    open(os.path.join(CANVAS, 'Odeme.dc.html'), 'w', encoding='utf-8').write(HEAD.format(title='Ayluna · Ödeme', css=CSS) + ODEME + TAIL.format(h=int(os.environ.get('H_ODEME', 1900)), js=ODEME_JS))
    print('yazıldı: Odeme.dc.html')
