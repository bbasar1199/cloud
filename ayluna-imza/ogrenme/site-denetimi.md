# Site denetimi ve çalışan iskelet (18 Ekim)

Kullanıcı: "Tüm iskeleti index olarak gönder; önce eksiklerini kontrol et, tüm eksik kısımları düzelt; sepet vesaire her kısım tam çalışsın; Shopify için düzenlerken de aynı şekilde."

- Çalışan önizleme: `site/` (üret: `python3 araclar/site/site_uret.py`; yayın: claude.ai artifact "Ayluna Mağazası").
- Test: `(cd site && python3 -m http.server 8765 &)` sonra `NODE_PATH=$(npm root -g) node araclar/site/test.js`. 31 sayfa + 60'a yakın akış adımı; son koşu: **hepsi tamam, konsol hatası yok, eksik görsel yok**.

## Denetimde bulunan eksikler → yapılan

| # | Eksik | Durum |
|---|---|---|
| 1 | Bütün bağlantılar `href="#"` (≈140); hiçbir sayfa birbirine gitmiyordu | Yönlendirme: ürün adları, menü, alt bilgi, politika, kart bağlantıları gerçek sayfaya gider |
| 2 | Başlıktaki menü, arama, sepet düğmeleri çalışmıyordu; sepet adedi hep 0 | Menü çekmecesi, arama sayfası, sepet çekmecesi; rozet gerçek adet |
| 3 | Ürün sayfalarında "Güvenli Ödeme ile Al" ve "Kapıda Ödeme" bir şey yapmıyordu; paket/model/seçenek sepete gitmiyordu | Seçili paket (1/2 adet), LunaDream modeli (Kız/Erkek, ikinci lamba), seçenek (renk vb.) ve fiyatıyla sepete |
| 4 | Sepet örnek veriydi (LunaDream 2 lamba sabit) | Gerçek sepet: satırlar, adet (1–9), kaldır, ek teklifler, Standart/Hızlı Kargo, kartla %5 toplam |
| 5 | Boş sepet ayrı panodaydı | Sepetin içinde boş hâl: "Ürünlere bak", "Hesabına giriş yap" |
| 6 | Kapıda ödeme akışı yoktu (canlıda EasySell) | Form: ad, telefon (05xx doğrulamalı), 81 il, ilçe, adres; ek teklifler + Hızlı Kargo; ₺80 ücret; kapatınca "Bekle! Kartla %5" |
| 7 | Ödeme ve "sipariş alındı" ekranı yoktu | Ödeme önizlemesi (Shopify'ın yerini tutar) + teşekkür sayfası (kart/kapıda farklı adımlar) |
| 8 | Alt bilgideki 5 politika sayfası yoktu | Kargo, Gizlilik ve KVKK, Mesafeli Satış, Ön Bilgilendirme, Hizmet Şartları (taslak; köşeli yerler + hukukçu onayı) |
| 9 | Arama sonuç göstermiyordu; 404/arama/boş sepet tek panodaydı | Arama yazdıkça süzer (öneri çipleri, adres `?q=`); ayrı 404 sayfası, Enter ile aramaya gider |
| 10 | Koleksiyondaki "Sepete ekle" ve kartlar çalışmıyordu | Karta dokununca ürün; "Sepete ekle" 1 adet ekler, çekmece açılır; tükendi ürün eklenmez |
| 11 | Formlar (iletişim, kargo takip, bülten, hesap) gönderilmiyordu | Boş alan uyarısı + onay bildirimi (canlıda Shopify formu / Track123) |
| 12 | Tükendi üründe "Gelince haber ver" bir şey yapmıyordu | Bildirim (canlıda Shopify "stoğa gelince haber ver" uygulaması gerekir) |
| 13 | Sayfalar 390px sabit genişlikteydi; 360px telefonda yana taşar | 320–430px akışkan; 320px'te taşma yok (test) |
| 14 | Bazı sayfalarda `.pg{overflow:hidden}` yapışkan çubukları bozuyordu | Hepsi `overflow:clip` |
| 15 | LunaDream ve USB sayfalarındaki "diğer ürünler" küçük resimleri eski, yerelde olmayan görsellerdi (13 adet) | Ana sayfadaki aynı ürün görselleriyle değiştirildi; tek görsel seti |
| 16 | Hesap sayfası yoktu | E-postayla kodla giriş (Shopify yeni müşteri hesapları) |
| 17 | "Yukarı çık" düğmesi her zaman içeriğin üstündeydi | 400px kaydırınca görünür |
| 18 | WhatsApp numarası yok | Bağlantılar bildirim gösterir: [WhatsApp numarası teyit] |
| 19 | Sepet çekmecesindeki kapat düğmesine adet rozeti biniyordu | Rozet yalnız başlıktaki sepet düğmesinde |
| 20 | Ana sayfa AyFeneri slaytında teyitsiz "sensörlü, şarjlı" | "Kumandalı, Bluetooth hoparlörlü" |

## Önizlemede taklit edilen, Shopify'da gerçek olacaklar
- Ödeme sayfası → Shopify checkout (kart: ödeme sağlayıcısı; %5 indirim otomatik indirim olarak tanımlanmalı).
- Kapıda ödeme formu → EasySell (alanlar, ₺80, bump'lar, "Bekle!" aynı kurgu).
- Sepet → Shopify sepeti (`/cart.js`, `/cart/add.js`, `/cart/change.js`); ek teklif fiyatları otomatik indirimle.
- Yorumlar → Loox; kargo takip → Track123; formlar → Shopify iletişim ve müşteri formu; hesap → Shopify müşteri hesapları; arama → Shopify arama.
- Sepet önizlemede tarayıcıda (localStorage) tutulur; sipariş gerçekten oluşmaz.

## Shopify'da da aynı test listesi (kullanıcı: "Shopify için düzenlerken de aynı şekilde")
Tema teslim edilmeden önce aynı akışlar canlı temada (önizleme temasında) denenir: her sayfa açılır ve taşmaz; her bağlantı bir yere gider; ürün → sepet → ödeme; ürün → kapıda formu; paket/model/seçenek doğru varyantla sepette; sepet adedi/kaldır/ek teklif/teslimat; boş sepet; menü, arama, 404, formlar, politikalar; 320px.

## Hâlâ teyit bekleyenler (sayfalarda köşeli)
Ticaret unvanı, adres, MERSİS, telefon, KEP, WhatsApp numarası · kargo kesim saati (16.00?), firmalar · kapıda ödeme ücretinin iadesi · kapıda kartla ödeme · disk sayıları (Galaksi 12/13) · AyFeneri pil/sensör/ölçü · ürün garantisi · stok [N] · politika metinleri için hukukçu onayı.
