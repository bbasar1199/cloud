# ayluna.shop site envanteri

Tarih: 18 Ekim 2026. Telefon görünümü 390×844, deviceScaleFactor 1. İzleme alan adları engelli, salt okuma.
Sepete ürün eklenmedi, form gönderilmedi, COD formu açılmadı. Sepet çekmecesinin dolu hâli bu yüzden görülmedi; içeriği HTML'den ve tema kodundan çıkarıldı.

Kaynak dosyalar (hepsi `/tmp/claude-0/-home-user-cloud/d6c53161-fb62-5d87-b54b-d11d394e16d5/scratchpad/site/` altında):
- Canlı HTML (JS çalıştıktan sonra): `html/<ad>.html`, bölüm özetleri `html/<ad>.bilgi.json`, ağ istekleri `html/<ad>.istekler.txt`
- Ham sunucu HTML'i (curl): `ham/ana-curl.html`, 15 ürün sayfası `ham/urun/<handle>.html`, tema JS `ham/tema/`
- Ekran görüntüleri: `ss/` (1000 px parçalar, liste en altta)
- Menü, arama, boş sepet, Loox metni: `html/etkilesim.json`

---

## 0. Genel

- **Tema:** Shopfinity 1.5.4 (Shrine Solutions, alt bilgide "Powered by Shrine"). Tema adı `ayluna-orijinal-iskelet-korunmus`, tema id 188900311268, varlık yolu `/cdn/shop/t/13/`, `theme_store_id: null`.
- **Mağaza:** `xueyyn-qm.myshopify.com`, shop id 79235711204, para birimi TRY, dil tr. **Mağaza ülkesi GB** (Shopify `countryCode: "GB"`).
- **Sayfa sayısı (sitemap):** 15 ürün, 2 sayfa (`/pages/contact`, `/pages/i̇letisim-kopyasi`), 1 koleksiyon (`frontpage`), 1 blog (`haberler`, yazı yok).
- **Yazı tipleri:** Poppins 400/700 (gövde ve başlık; başlık ölçeği 1.3). Duyuru bandında Google Fonts'tan Nunito Sans 400/600/700. Material Symbols Outlined (ikon fontu, ana sayfada boş).
- **Renkler (canlıdan ölçüldü):**
  - Zemin `#F7F4EF` (krem)
  - Metin `#121212` (%90 opak)
  - Vurgu / buton / alt bilgi / indirim rozeti / fiyat `#1F2A44` (lacivert)
  - Duyuru bandı `#1F2A44` ↔ `#374A79` arasında 6 sn'de bir renk değiştiriyor
  - "Ay ışığını evine getir" başlık vurgusu `#6D388B` (mor)
  - Hero butonu: beyaz zemin, siyah yazı
  - EasySell butonu: siyah `#000000`, 25 px köşe, zıplama animasyonu
- **Biçim:** buton köşesi 8 px (`--buttons-radius` 6 px), kart köşesi 12 px, harf aralığı 0.9–1 px (her yerde geniş).
- **SEO:** `<title>Ayluna</title>`. Meta description yok, `og:image` yok. `og:description` sadece "Ayluna". Organization şemasında `sameAs` dizisi tamamen boş, yani tema ayarlarında hiçbir sosyal hesap girilmemiş.
- **Favicon / logo:** https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Adsiz_tasarim_66.png?v=1769445970 (2,3 MB PNG; 32 px'e kırpılıp kullanılıyor)

### Yüklü uygulamalar (script ve uygulama bloklarından)
| Uygulama | Kanıt | Ne yapıyor |
|---|---|---|
| **EasySell COD Form** | `cdn.shopify.com/extensions/01a120e4-…/easysell-cod-form-525/` (easysell.js, helpers.js, vendor.js, phonevalidator.js, COUNTRIES-TR.js), `EASYSELL_CONFIG`, `EASYSELL_BUMPS`, `EASYSELL_DOWNSELLS` | Kapıda ödeme açılır formu, sipariş artırıcı teklifler (bump), vazgeçme indirimi (downsell), 80 TL kapıda ödeme ücreti, ürün sayfasında yapışkan buton |
| **Kaching Bundles** | `extensions/01a14f06-…/kaching-bundles-2091/` (loader.js, kaching-bundles.js, kaching-bundles-api.js) | Ürün sayfasında adet indirimi ve hediye kutuları (ör. LunaDream "Sınırlı süreli teklif", "1 Adet / 2 Adet %20 İndirim", "+ 6 Tane Ücretsiz Hediye Disk") |
| **Loox** | `loox.io/widget/3DlBqrswrJ/loox.1769446524232.js`, ana sayfada `loox_card_carousel_section`, ürünlerde `loox_dynamic_section` | Yorum yıldızları, ana sayfa yorum karuseli, ürün yorum bölümü |
| **Track123** | `/apps/track123`, `shp.track123.com/tracking-page-spa/app-proxy-tradition.js` | Kargo takip sayfası |
| **Meta (Facebook & Instagram)** | web pixel 1935540452, `pixel_id 1221305419422624`, `fbevents.js` | Reklam pikseli |
| **Olasılıkla Klaviyo** | web pixel 2034467044, `accountID "RR86v2"`, apiClientId 123074, `enableAddedToCartEvents: true` | E-posta / pazarlama pikseli. Sitede Klaviyo formu görünmüyor |
| **Bilinmeyen uygulama pikseli** | web pixel 1926693092, apiClientId 2935586817, ayar `shopifyDomain` | Kaching ayarında `webPixel: true` var; büyük olasılıkla Kaching |
| **Shopify özel piksel** | `shopify-custom-pixel` (LAX) | İçeriği sayfadan okunamıyor. TikTok kodu storefront'ta yok; varsa burada olabilir |
| Shop / Shopify | shop-js `init-shop-cart-sync`, perf-kit, trekkie | Standart |

---

## 1. Ana sayfa (https://ayluna.shop/)

Sayfa yüksekliği 3586 px. Ekran görüntüleri: `ss/ana-00.png` … `ss/ana-03.png`.

Sıra (yukarıdan aşağı):

### 1.1 `shopify-section-sections--28025597690084__custom_liquid_XWzNR9`: duyuru bandı (custom liquid, header grubu)
- **Metin:** "Bugüne Özel %20 İndirim" + sayaç kutuları "01 SAAT : 01 DK : 47 SAN".
- **Bağlantı:** yok, tıklanmıyor.
- **Sayaç kodu:** `countdownDuration = 1 saat 2 dk`. Bitiş zamanı her sayfa yüklenişinde `new Date() + 62 dk` olarak yeniden kuruluyor. Süre bitince de yeniden başlıyor. Yani **sahte sayaç**: her ziyaretçi, her sayfada 1:02:00'dan başlayan bir sayaç görüyor.
- **Stil:** zemin #1F2A44 ↔ #374A79 animasyonlu, beyaz sayı kutuları, Nunito Sans (Google Fonts `@import`). Mobilde yazı 12 px, sayı 14 px, etiket 7 px.
- **Kapsam:** her sayfada görünüyor (header grubu). Ürün şablonlarında bunun altında ayrıca ürüne özel `announcement_bar` var (bkz. 9).

### 1.2 `shopify-section-sections--28025597690084__header`: üst menü
- **Düzen (mobil):** solda hamburger, ortada logo, sağda arama ve sepet ikonu. Masaüstünde "Oturum aç" ikonu da var.
- **Logo:** https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Adsiz_tasarim_66.png?v=1769445970 (alt "Ayluna"; görselin içinde fener, hilal ve "AYLUNA" yazısı). `<h1>` içinde, metin boş.
- **Menü çekmecesi** (başlık "Menu"; İngilizce kalmış). Alt menü yok, tek seviye:
  1. Ana sayfa → `/`
  2. Galaxy Usb Projektör → `/products/galayx-usb-projektor`
  3. LunaDream Gece Lambası → `/products/lunadream-gece-lambasi`
  4. Ayluna™ AyFeneri → `/products/lamba`
  5. Tüm Ürünler → `/collections/frontpage` (dikkat: 15 ürünün yalnız 9'unu içeriyor)
  6. Biz Burdayız → `/pages/i%CC%87letisim-kopyasi`
  7. İletişim → `/policies/contact-information`
  8. Kargo Takip → `https://ayluna.shop/apps/track123`
  9. alt satırda kişi ikonu + "Oturum aç" → `https://ayluna.shop/customer_authentication/redirect?locale=tr&region_country=TR`
- **Menüde olmayanlar:** sosyal medya bağlantısı, dil/para seçici.
- **Arama:** tam ekran arama modalı, tahminli arama açık. "lamba" yazınca:
  - "ÖNERİLER: gece lambası"
  - "ÜRÜNLER": 7 ürün, fiyat ve üstü çizili fiyatla
  - "'lamba' için arama yap" bağlantısı
  - Ekran: `ss/etk-arama.png`, `ss/etk-arama-oneri.png`
- **Sepet ikonu:** `#cart-icon-bubble`, `/cart`. Tıklayınca sepet çekmecesi açılıyor.
- Menü ekranı: `ss/etk-menu.png`.

### 1.3 `shopify-section-cart-drawer`: sepet çekmecesi (ayrıntı 3. bölümde)

### 1.4 `shopify-section-template--28025596739812__cfca4268-6358-426c-98ab-d292aeef11e5`: slayt gösterisi (slideshow)
- **Genel:** 2 slayt, otomatik geçiş kapalı. Ok (‹ ›) ve nokta kontrolleri slaytın altında. Mobilde yükseklik 436 px. `aria-label` "Slideshow about our brand" (İngilizce).
- **Slayt 1**
  - Masaüstü görseli: https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260215_080741_935a0da0-5e1d-4d79-a871-16173e17732a.png?v=1771143114
  - Mobil görseli: https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260215_082547_150a315a-581b-4319-abfb-841f109d45a6.png?v=1771143990 (1,5 MB PNG)
  - Görselin içine gömülü yazılar: Ayluna logosu, "MASALSI GECE IŞIĞI", "Saniyeler içinde ortamı büyülü bir atmosfere çevir.", "4.7/5 | 2467 Onaylı Yorum", sahte "ŞİMDİ KEŞFET" düğmesi, "Ücretsiz Kargo | 1 Yıl Garanti | 90 Gün İade", "ayluna.shop".
  - Üstte gerçek HTML buton: **"Şimdi İncele"** → `/products/lunadream-gece-lambasi`. Beyaz buton, ortada. Görseldeki sahte "ŞİMDİ KEŞFET" ile çift CTA oluşuyor. Ok ikonu yazının üstüne biniyor ("İncele" kelimesinin sonunda).
- **Slayt 2**
  - Masaüstü görseli: https://cdn.shopify.com/s/files/1/0792/3571/1204/files/ChatGPT_Image_26_Oca_2026_17_03_25.png?v=1769436591
  - Mobil görseli: https://cdn.shopify.com/s/files/1/0792/3571/1204/files/ChatGPT_Image_26_Oca_2026_17_10_57.png?v=1769436700
  - Görselin içine gömülü yazılar: "Ayluna" (hilal logo), "Ay Işığı, Evinize Rehberlik Etsin". Görselde AyFeneri, ay ve deniz feneri var.
  - Buton yok, bağlantı yok; tıklanınca bir yere gitmiyor.

### 1.5 `shopify-section-template--28025596739812__1771142687a92ebed8`: Loox yorum karuseli (uygulama bölümü)
- **Kaynak:** blok `loox_reviews_loox_card_carousel_section_ybUKz3`, iframe https://loox.io/widget/3DlBqrswrJ/v2/carousel?…
- **Ayarlar:** kart tipi, mobilde 1 kart, masaüstünde 4. En çok 100 karakter, gölge `offset-dark`. Mobilde ok yok, sayfalama yok, otomatik oynatma yok. Yükseklik yaklaşık 513 px.
- **Kartlar:** fotoğraf, 5 yıldız, isim + doğrulama ikonu, kısaltılmış yorum. Altında "Destekleyen: LOOX".
- **20 yorum, sırayla:** Handan B., Miray D., Uğur Ö., Büşra S., Yasemin E., Berke T., Ebru Ö., Ali A., Nisan C., Elif D., Mehmet Ç., Onur A., Fatma R., Cihan Z., Yasemin C., Mehmet B., Zehra K., Meryem Ö., Deniz S., Ceren N.
- **İçerik:** yorumlar ürünlere göre karışık. Bir kısmı hoparlör/saat/alarm/beyaz gürültü anlatıyor, yani Retro Mini Pikap ya da benzeri bir ürüne ait. Ürün adı kartta yazmıyor.
- **İlk yorum (kısaltılmış):** "ABD'de yaşayan, tatilini anne ve babasıyla birlikte bizimle İzmir'de geçiren 6 yaşındaki torunum..."
- **Yorum görselleri (images.loox.io):**
  - https://images.loox.io/uploads/2026/8/24/x0pFxuzm3.jpg
  - https://images.loox.io/uploads/2026/6/18/jRJvEgDQs.jpg
  - https://images.loox.io/uploads/2026/6/18/RKRL2l43s.jpg
  - https://images.loox.io/uploads/2026/6/18/aZoz5BkftC.jpg
  - https://images.loox.io/uploads/2026/6/18/0ldELIZQX8.jpg
  - https://images.loox.io/uploads/2026/6/18/0oMcVre-9.jpg
  - https://images.loox.io/uploads/2026/6/18/t04tVHQwo.jpg
  - https://images.loox.io/uploads/2026/6/18/yWH_CwWjW.jpg
  - https://images.loox.io/uploads/2026/6/18/PWlNEDcjv.jpg
  - https://images.loox.io/uploads/2026/6/18/xdTN-A5wv.jpg
  - https://images.loox.io/uploads/2026/6/18/0Ldqo5XJZ.jpg
  - https://images.loox.io/uploads/2026/5/20/orsakikCk.jpg
  - https://images.loox.io/uploads/2026/5/20/dPQDEqR4s.jpg
  - https://images.loox.io/uploads/2026/5/20/XtEZQH4r9.jpg
  - https://images.loox.io/uploads/2026/5/20/8MKPXdQhX.jpg
  - https://images.loox.io/uploads/2026/5/20/RFftwFgRp.jpg
  - https://images.loox.io/uploads/2026/5/20/gDlsrmAypP.jpg
  - https://images.loox.io/uploads/2026/5/20/aLguf3odWX.jpg
  - https://images.loox.io/uploads/2026/5/20/NAuqUzliY.jpg
  - https://images.loox.io/uploads/2026/5/18/vflSG8BIL.jpg
- Tam yorum metinleri: `html/etkilesim.json` → `loox.text`.

### 1.6 `…__section_divider_MqmdQf` ve 1.7 `…__section_divider_P8yE9i`: dalga ayırıcı (iki tane art arda)
- Animasyonlu SVG dalga (4 katman paralaks), lacivert/gri, her biri 30 px. Ekranda tek bir bant gibi görünüyor.

### 1.8 `shopify-section-template--28025596739812__featured_collection_XhApy7`: öne çıkan koleksiyon
- **Başlık:** "Bunlarıda sevebilirsin" (yazım hatası: "Bunları da").
- **Kaynak:** `frontpage` koleksiyonu ("Ana sayfa"), 9 ürün.
- **Düzen:** Splide karusel, mobilde 1 kart, ok ve 9 nokta. "Tümünü gör" bağlantısı yok.
- **Kart içeriği:** kare görsel, sol altta "SAVE %x" rozeti (İngilizce), ürün adı, Loox yıldızı ve sayısı, fiyat, üstü çizili fiyat. Kartta sepete ekle butonu yok (koleksiyon sayfasında var).
- **Ürünler, sırayla:**
  | # | Ürün | Bağlantı | Fiyat / eski fiyat | Rozet | Loox | Görsel |
  |---|---|---|---|---|---|---|
  | 1 | LunaDream Gece Lambası | /products/lunadream-gece-lambasi | 1.699,99 / 1.999,00 | SAVE 14% | 62 | https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260210_151801_d206f2aa-f1b6-4b23-a9bd-c53ec4c35ddd.png?v=1770739751 |
  | 2 | Galaxy Usb Projektör | /products/galayx-usb-projektor | 1.599,00 / 1.999,00 | SAVE 20% | 2 (4.0) | https://cdn.shopify.com/s/files/1/0792/3571/1204/files/ChatGPTImage11Eyl202601_02_48_1.png?v=1789078073 |
  | 3 | Ayluna AyFeneri | /products/lamba | 1.649,99 / 2.499,00 | SAVE 33% | 43 | https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260212_125544_58e8b2af-ee81-4a04-a2d0-b338ebc94713.png?v=1770903660 |
  | 4 | Ayluna Kum Saati Lamba | /products/ask-saati | 799,00 / 999,00 | SAVE 20% | 1 | https://cdn.shopify.com/s/files/1/0792/3571/1204/files/imgi_8_1_org_zoom.jpg?v=1769961005 |
  | 5 | Yıldız Işığı Nemlendirici | /products/yildiz-isigi-nemlendirici | 849,99 / 1.099,00 | SAVE 22% | 6 | https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260210_160835_4caca476-596c-43c9-a7c4-6e673c21a860.png?v=1770741660 |
  | 6 | Ayluna Galaksi Night Projektör | /products/ayluna-galaksi-night-projektor | 2.199,00 / 2.999,00 | SAVE 26% | 6 | https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Galaxy_projector_product_infogra__202609012212.jpg?v=1788290005 |
  | 7 | Aroma Terapi Nemlendirici | /products/aroma-terapi-nemlendirici | 1.499,00 / 1.999,00 | Tükendi | 6 | https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260220_182854_ee737255-f473-4745-8844-055529745da8.jpg?v=1771612404 |
  | 8 | Galaksi Ambiyans Işığı | /products/galaksiambiyanisigi | 1.499,00 / 2.898,00 | SAVE 48% | 13 | https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260216_184339_38775b04-d940-4bc4-9b97-dbdc26c9d678.png?v=1771268652 |
  | 9 | Dokunmatik Ambiyans Lamba | /products/dokunmatik-ambiyans-lamba | 1.299,99 / "1.299,00" (eski fiyat yeni fiyattan düşük) | Tükendi | 7 | https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260515_190625_aaa51f3c-2643-46eb-8ad0-ff33f7f5b2ba.png?v=1778946575 |
- **Biçim:** fiyatlar "1,699.99TL" olarak yazılıyor (İngilizce ayraç, TL bitişik).

### 1.9 `shopify-section-template--28025596739812__6aa09428-a417-429d-9159-a4e8afd49590`: ikon çubuğu (icon bar / multicolumn)
- **Maddeler:** 4 başlık, emoji ile:
  - "🌙 Gerçek Ay Yansıması"
  - "🚶 Otomatik Sensör"
  - "🎛️ Kumanda Kontrolü"
  - "🔋 Şarjlı Kullanım"
- **Ek metin ve ikon:** açıklama metni yok. Material ikon alanları boş.
- **Düzen:** mobilde Splide karusel, 1 madde, ok ve nokta. Yükseklik 158 px.
- **Bağlam:** maddeler AyFeneri'ye ait ama bölüm genel ürün karuselinin altında. Ürün adı yazmıyor.

### 1.10 `shopify-section-template--28025596739812__image_with_text_Yxredh`: görsel + metin
- **Görsel:** animasyonlu GIF https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Grselden_Video_Oluturma-ezgif.com-video-to-gif-converter.gif?v=1769439718
  - 1500×2666, **16,9 MB**. Shopify `width=1500` parametresiyle küçültmüyor, mobilde aynen iniyor.
  - Sağ altta "Veo" filigranı görünüyor.
  - İçerik: ay yansıtan deniz feneri lamba.
- **Başlık (h2):** "Ay ışığını evine getir" (vurgu rengi #6D388B).
- **Metin:** "Gerçekçi ay yansımasıyla bulunduğun ortamı anında daha sıcak ve huzurlu hale getirir. Sensör, kumanda ve Bluetooth özellikleri tek üründe birleşir; hem dekoratif görünür hem de günlük kullanımda gerçek bir konfor sağlar. Şarjlı yapısıyla kablo karmaşası olmadan istediğin köşeye yerleştir."
- **Buton:** "Şimdi Keşfet" → `/products/lamba` (lacivert).

### 1.11 `…__section_divider_BL4aX6`: dalga ayırıcı (alt bilgiye geçiş)

### 1.12 `shopify-section-promo-popup`: boş (bkz. 4)
### 1.13 `shopify-section-scroll-to-top-btn`: yukarı çık (bkz. 5)
### 1.14 `shopify-section-global-music-player`: boş (bkz. 5)
### 1.15 `shopify-section-sections--28025597657316__footer`: alt bilgi (bkz. 6)

---

## 2. Duyuru bandı ve üst menü: özet
- Duyuru: 1.1 (sahte sayaç, %20 vaadi, bağlantısız).
- Üst menü: 1.2 (9 bağlantı, alt menü yok, "Tüm Ürünler" eksik koleksiyona gidiyor).
- **Ürün sayfalarındaki ikinci bant** (şablona özel `announcement_bar`, global bandın altında):
  - LunaDream ve V2: "Online Ödemede Sepette %5 İndirim 🚀"
  - AyFeneri ve Astronot: "3D Güvenli Ödeme İle Satın Al Ertesi Gün Kargoda"
  - Aroma Terapi: "Kredi Kartı İle Yapılan Alışverişler Aynı Gün Kargoya verilir. ✨"
  - Galaksi Night: "Kredi Kartı ile Yapılan Alışverişlerde Aynı Gün Kargo"
  - Çocuk Gece Feneri: "Çocuğun Odasını Masala Çevir ✨"
  - Retro Pikap: "🚚 Stoklarla Sınırlı · Müziğin Tasarımla Buluştuğu An ✨"
  - Dokunmatik Lamba ve Çizim Tahtası: "YAZ-ÇİZ-ÖĞRET HEPSİ BİR ARADA" (Dokunmatik Lamba sayfasında da çizim tahtası metni, şablon ortak)
  - Galaksi Ambiyans: "Evinde kendi huzur köşeni oluştur✨"
  - Sunset: "Güneş Artık Odanda Batıyor ✨"
  - Kum Saati, Galaxy USB, Yıldız Işığı: ikinci bant yok

---

## 3. Sepet çekmecesi (`shopify-section-cart-drawer`)

Ekran (boş hâl): `ss/etk-sepet-bos.png`.

### 3.1 Boş hâl (canlıda görülen)
- Mobilde tam ekran çekmece. Sağ üstte X.
- **Boş sepet metni:** "Sepetiniz boş", ardından "Hesabınız var mı?" ve "Daha hızlı ödeme yapmak için oturum açın." (bağlantı customer_authentication'a).
- **Koleksiyon kartı:** "Ana sayfa →" (`/collections/frontpage`), görseli LunaDream: https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260210_151801_d206f2aa-f1b6-4b23-a9bd-c53ec4c35ddd.png?v=1770739751. Kartın adı "Ana sayfa" kalmış.

### 3.2 Dolu hâlin iskeleti (HTML'de, ürün yokken gizli)
- **Başlık:** "Sepetinde • 0 ürün var".
- **Rezervasyon sayacı (`cart-timer`):** "Süre bitene kadar senin için ayrıldı 05:00" (`countdown-timer data-duration="299"`). Her açılışta 5 dakikadan başlıyor; gerçek bir stok ayırma yok.
- **Ürün satırları:** `cart-drawer-items`. Görsel genişliği %20, başlık 1.5rem.
- **Toplam:** "Ödenecek Tutar 0.00TL" (2.0rem kalın). Altında toplam tasarruf satırı (`cart-drawer__total-savings`, ürün yokken boş).
- **Koşul onay uyarısı:** `tnc-checkbox-warning` butonun üstünde ve altında, gizli. Tema "şartları kabul ediyorum" kutusunu destekliyor, uyarı alanları hazır.
- **Buton:** "Ödeme" (`#CartDrawer-Checkout`, `name=checkout`) → Shopify ödeme sayfası.
- **Ödeme logoları:** American Express, Diners Club, Discover, JCB, Mastercard, Visa.

### 3.3 Temanın desteklediği ama doğrulanamayan bloklar
- Tema JS'inde (`ham/tema/main.js`) şu özellikler var: `cart-drawer-upsell` (sepet içi ek ürün, varyant seçicili, "upsell__add-btn"), `cart-drawer-gift` (hediye ürün), `cart-note` (sipariş notu), `cart-discount-field` (indirim kodu alanı), `countdown-timer`, `TncCheckbox`.
- Ücretsiz kargo çubuğu için temada JS bulunamadı.
- Bu blokların açık olup olmadığı yalnız sepette ürün varken görünür. Ürün eklemek yasak olduğu için doğrulanmadı.

### 3.4 Kullanıcının gördüğü ek teklifler: kaynak = EasySell COD Form "bump"ları
- Teklifler **sepet çekmecesinden ya da sepet uygulamasından gelmiyor**. Kapıda ödeme formu uygulaması **EasySell**'in "order bump" ayarı (`EASYSELL_BUMPS`) her sayfanın HTML'inde duruyor.
- Hepsi `criteria: all`, yani her üründe COD formunda gösteriliyor.
- EasySell ayarında `excluded_pages: ["drawer"]` var: form sepet çekmecesinde değil, ürün sayfası ve koleksiyon kartlarındaki "Kapıda Ödeme ile Sipariş Ver" açılır formunda.

| Formdaki metin | EasySell id | Teklif fiyatı | Mağaza ürünü | Ürün id / varyant id | Normal fiyat | Görsel |
|---|---|---|---|---|---|---|
| "🔥 **Hızlı Kargo** sadece **79.99TL**" + "Siparişiniz öncelikli olarak hazırlanır ve aynı gün kargoya teslim edilir. Acil ihtiyaçlarınız için sunulan bu hizmet, standart gönderime göre daha hızlı işlem önceliği sağlar." | 24584 | 79,99 | ürün değil, ücret kalemi | – | – | yok (yeşil kesikli çerçeve, #f6fff4 zemin) |
| "🔥 Siparişinize özel **Işıklı Nemlendirici** sadece **749.99TL!**" | 24858 | 749,99 | **Yıldız Işığı Nemlendirici** (`/products/yildiz-isigi-nemlendirici`) | 8912641196260 / 47885730906340 | 849,99 (eski 1.099,00) | https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260210_160835_4caca476-596c-43c9-a7c4-6e673c21a860.png?v=1770741660 (mor #dad7ff zemin, mavi kesikli çerçeve) |
| "🔥 Siparişinize özel **Kum Saati Lamba** sadece **699.99TL!**" (10pt) | 28102 | 699,99 | **Ayluna Kum Saati Lamba** (`/products/ask-saati`) | 8906010132708 / 47528723742948 | 799,00 (eski 999,00) | https://cdn.shopify.com/s/files/1/0792/3571/1204/files/imgi_8_1_org_zoom.jpg?v=1769961005 (animasyonlu, #f4f7ff zemin) |
| "🔥 **Astronot Hava Temizleyici** sadece **749.00TL** karşılığında sepete ekleyin" | 29071 | 749,00 (`useProductPrice: true` ama metin 749 diyor) | **Astronot Oda Nemlendirici Aroma Difüzör** (`/products/astronot-oda-nemlendirici-aroma-difuzor`) | 9134406271204 / 49374709285092 | 799,00 | https://cdn.shopify.com/s/files/1/0792/3571/1204/files/EkranResmi2026-07-1022.46.52.png?v=1783712831 (yeşil kesikli çerçeve) |

- **"Işıklı Nemlendirici" kararı: Yıldız Işığı Nemlendirici.**
  - Bump ayarındaki ürün kimliği doğrudan 8912641196260'ı gösteriyor.
  - Görsel aynı: beyaz, eğik gövdeli ultrasonik nemlendirici, RGB ışık halkası, "Ortamınızı RENKLENDİRİN".
  - Aroma Terapi Nemlendirici (alev efektli, tükendi) ve Astronot (ayrı bump) değil.
- **İsim uyuşmazlığı:** "Astronot Hava Temizleyici" adı yanlış. Bağlı ürün bir oda nemlendiricisi ve aroma difüzörü; görselde astronotlu uzay kapsülü nemlendirici var. Hava temizleyici değil.

### 3.5 EasySell formunun geri kalanı (ayar JSON'undan; form açılmadı)
- **Tip:** açılır pencere (`form_type: popup`). Ürün sayfasında yapışkan buton altta (`sticky: true`).
- **Buton:** "Kapıda Ödeme ile Sipariş Ver" (sepet ikonu, siyah, zıplama animasyonu). "Hemen al" (Shopify dinamik ödeme) butonu gizli (`hidebuy: true`, CSS ile).
- **Form alanları, sırayla:**
  1. Başlık "Sipariş vermek için lütfen formu doldurun"
  2. Sepet içeriği
  3. Sipariş özeti (Ara toplam / İndirim / Kargo / Toplam / "Tüm vergiler dahil")
  4. Kargo seçenekleri (tek seçenekse gizli)
  5. Ad
  6. Soyad
  7. Telefon ("Başına 0 koyarak numaranızı giriniz")
  8. Adres
  9. İl (81 il listesi)
  10. İlçe
  11. Onay kutusu "Yeni ürünler ve fırsatlardan haberdar olmak için abone olun!"
  12. Zorunlu "Kapıda Ödeme Tipi": Nakit Ödeme / Kredi Kartı
  13. Buton "ŞİMDİ SATIN AL - {toplam}" (siyah, 24 px köşe, zıplama)
- **Ücret:** "Kapıda Ödeme Ücreti" **80 TL**, sabit, her siparişe.
- **Vazgeçme teklifi (downsell, id 18159):** form bir kez kapatılınca açılır.
  - Başlık "Bekle!", rozet "%5"
  - Alt başlık "Tebrikler! Özel bir indirim açtınız!"
  - Metin "Şimdi satın al, indirim kazan!"
  - Butonlar "{%5} İNDİRİMLE siparişi tamamla" (turuncu-pembe gradyan) ve "Hayır, teşekkürler"
  - İndirim %5
- **Teşekkür metni:** "Teşekkürler, {ad}! 🎉 Siparişiniz onaylandı." + sipariş özeti + toplam.
- **Diğer:** Sadece TR. OTP kapalı. UTM ekleniyor. Siparişe etiket ekleniyor. Makbuz e-postası gidiyor. Pikseller otomatik algılanıyor.

---

## 4. Açılır pencere (`shopify-section-promo-popup`)
- Bölüm hem sunucu HTML'inde hem canlıda **boş**. Kapalı ya da içeriği girilmemiş.
- İçerik, açılma zamanı, indirim kodu: **yok**.
- Sitedeki tek gerçek açılır pencereler EasySell'in:
  - COD formu
  - "Bekle!" %5 downsell (form kapatılınca)
- Bülten %5 indirim vaat ediyor ama sitede kod yok. Kodun e-postayla gidip gitmediği görülemiyor.

## 5. Müzik çalar ve yukarı çık butonu
- **`global-music-player`:** sadece konum CSS'i var (sağ alt, mobilde 1.5rem kenar boşluğu). Çalar HTML'i ve ses dosyası yok. Ekranda hiçbir şey görünmüyor (kapalı ya da parça seçilmemiş).
- **`scroll-to-top-btn`:**
  - Konum: sağ alt, yuvarlak, vurgu rengi lacivert (`color-accent-1`), mobilde kenardan 1.5rem.
  - Davranış: `scrollY > 400` olunca görünüyor, tıklanınca `window.scrollTo({top:0, behavior:"smooth"})`.
  - Ürün sayfasındaki EasySell yapışkan butonuyla aynı köşeye düşebilir.

## 6. Alt bilgi (`sections--28025597657316__footer`)
Ekran: `ss/ana-03.png`. Zemin #1F2A44, beyaz yazı. Üstünde dalga ayırıcı.
- **Bülten:**
  - Başlık "%5 İNDİRM KAZANMAK İÇİN ABONE OL" (yazım hatası: İNDİRİM)
  - Metin: "Bizimle e-mail adresin ile bizlere kayıt olarak %5 indirimi kazan ve yeni ürünlerden ilk sen haberdar ol"
  - Alan "E-posta", buton "Kayıt Ol" (beyaz)
  - Form `/contact#ContactFooter`, `contact[tags]=newsletter`. Shopify müşteri kaydı olarak düşüyor.
- **Sütunlar / menü:** **yok**. Alt bilgide menü sütunu yok.
- **Sosyal medya:** **yok**. Sitenin hiçbir yerinde Instagram/TikTok/Facebook bağlantısı yok; şema `sameAs` boş.
- **Ödeme logoları:** American Express, Diners Club, Discover, JCB, Mastercard, Visa (Shopify varsayılan simgeleri; Troy yok).
- **Telif:** "© 2026, Ayluna" (→ `/`) "Powered by Shrine" (→ https://shrinesolutions.io/).
- **Politika bağlantıları:**
  - Gizlilik politikası → `/policies/privacy-policy`
  - Para iade politikası → `/policies/refund-policy`
  - Hizmet şartları → `/policies/terms-of-service`
  - Kargo politikası → `/policies/shipping-policy`
  - İletişim bilgileri → `/policies/contact-information`
- **Firma bilgisi, adres, telefon, e-posta:** alt bilgide **hiçbiri yok**.
- **Sitede bulunan tek iletişim verisi:** ecom11001@gmail.com (yalnız politikalarda). Telefon numarası hiçbir yerde yok.
- **İkinci bülten:** 404, arama, blog, koleksiyon ve sepet sayfalarında alt bilginin üstünde **ikinci bir bülten bölümü** daha var. İngilizce: "Subscribe to our emails / Join our email list for exclusive offers and the latest news. / E-posta / Sign up" (gri zemin, siyah buton).

---

## 7. Diğer sayfalar

### 7.1 `/pages/contact` ("İletişim – Ayluna"), ekran `ss/contact-00.png`
- **Bölüm:** `template--28025596805348__contact_form_U9ptC4`.
- **Başlık:** "Tüm sorularını buradan bize iletebilirsin."
- **Alanlar:** Ad, E-posta, Telefon numarası, Yorum. Buton "Gönder" (lacivert). Hata metni İngilizce "This field is required".
- **Diğer içerik:** başka bilgi yok (adres, telefon, saat yok). Menü ve alt bilgiden bağlantı yok; yalnız sitemap'te.

### 7.2 `/pages/i̇letisim-kopyasi` ("İletişim kopyası – Ayluna", menüde "Biz Burdayız"), ekran `ss/biz-burdayiz-00.png`
- 7.1'in birebir kopyası (aynı şablon, aynı form).
- Sayfa başlığı "İletişim kopyası" kalmış. URL'de noktalı İ (`i%CC%87`).

### 7.3 `/collections/frontpage` ("Ana sayfa – Ayluna"), ekran `ss/col-frontpage-00…03.png`
- **Bölümler:**
  - `main-collection-banner`: "Koleksiyon:" + "Ana sayfa"
  - `main-collection-product-grid`
  - `newsletter` (İngilizce)
- **Araç çubuğu:** "Filtrele ve sırala", "9 ürün".
  - Filtreler: Stok durumu, Fiyat.
  - Sıralama: Öne çıkan, En alakalı, En çok satan, A-Z, Z-A, Fiyat artan/azalan, Tarih eski/yeni.
- **Kartlar:** 2 sütun. Görsel ve hover'da ikinci görsel, SAVE rozeti, ad, Loox, fiyat.
  - Tema butonu **"Güvenli Ödeme İle Al"**: sepete ekleyip çekmeceyi açar. Varyantlı üründe "Seçenekleri belirle".
  - EasySell butonu **"Kapıda Ödeme ile Sipariş Ver"**: siyah, dar kartta kelime kelime kırılıp çok büyük bir blok oluyor.
- **Ürünler:** 1.8'deki 9 ürün.

### 7.4 `/collections/all` ("Ürünler – Ayluna"), ekran `ss/col-all-00…04.png`
- **Düzen:** aynı şablon. "15 ürün", Stokta 12 / Stokta yok 3, en yüksek fiyat 2.199 TL.
- **Hata (iki kez doğrulandı):** bu sayfada **EasySell butonu 15 kartın hepsinde gri "Tükendi" yazıyor**, stokta olanlarda da. Listenin ilk ürünü tükenmiş Aroma Terapi; uygulama onun durumunu hepsine uyguluyor gibi.
- **Tüm ürünler** (alfabetik):
  | Ürün | Handle | Fiyat | Eski fiyat | Stok | Loox |
  |---|---|---|---|---|---|
  | Aroma Terapi Nemlendirici | aroma-terapi-nemlendirici | 1.499,00 | 1.999,00 | Tükendi | 6 |
  | Astronot Oda Nemlendirici Aroma Difüzör | astronot-oda-nemlendirici-aroma-difuzor | 799,00 | – | var | 0 |
  | Ayluna AyFeneri | lamba | 1.649,99 | 2.499,00 | var | 43 |
  | Ayluna Çocuk Gece Feneri | ayluna-cocuk-gece-feneri | 1.599,00 | – | var | 0 |
  | Ayluna Galaksi Night Projektör | ayluna-galaksi-night-projektor | 2.199,00 | 2.999,00 | var | 6 |
  | Ayluna Kum Saati Lamba | ask-saati | 799,00 | 999,00 | var | 1 |
  | Ayluna Retro Mini Pikap | ayluna-retro-mini-pikap | 1.499,00 | 1.999,99 | var | 10 |
  | Dokunmatik Ambiyans Lamba | dokunmatik-ambiyans-lamba | 1.299,99 | 1.299,00 (ters) | Tükendi | 7 |
  | Eğitici Akıllı Çizim Tahtası | egitici-akilli-cizim-tahtasi | 1.199,00 | 1.999,00 | var (varyantlı) | 12 |
  | Galaksi Ambiyans Işığı | galaksiambiyanisigi | 1.499,00 | 2.898,00 | var | 13 |
  | Galaxy Usb Projektör | galayx-usb-projektor | 1.599,00 | 1.999,00 | var | 2 |
  | LunaDream Gece Lambası | lunadream-gece-lambasi | 1.699,99 | 1.999,00 | var (Kız / Erkek Çocuklar İçin) | 62 |
  | LunaDream Gece Lambası V2 | lunadream-gece-lambasi-v2 | 1.449,00 | 1.999,00 | Tükendi | 0 |
  | Sunset Lamba | sunset-lamba | 699,00 | 999,00 | var | 0 |
  | Yıldız Işığı Nemlendirici | yildiz-isigi-nemlendirici | 849,99 | 1.099,00 | var | 6 |
- **Toplam Loox yorumu:** 168. `frontpage` dışında kalan 6 ürün: Astronot, Çocuk Gece Feneri, Retro Pikap, Çizim Tahtası, LunaDream V2, Sunset.

### 7.5 `/blogs/haberler` ("Haberler – Ayluna"), ekran `ss/blog-00.png`
- Başlık "Haberler". **Yazı yok** (Atom akışı da boş).
- Altında İngilizce bülten bölümü.

### 7.6 `/search` ("Ara – Ayluna"), ekran `ss/search-00.png`
- Başlık "Ara", tek arama kutusu.
- Altında İngilizce bülten bölümü.

### 7.7 `/cart` ("Alışveriş Sepetiniz – Ayluna"), ekran `ss/cart-00.png`, `ss/cart-01.png`
- **Boş hâl:** "Sepetiniz", "Alışverişe devam et" (→ `/collections/all`), "Sepetiniz boş", "Hesabınız var mı? Daha hızlı ödeme yapmak için oturum açın."
- **Dolu hâl iskeleti:** "Alt toplam 0.00 TRY" (çekmecedeki "Ödenecek Tutar" ile farklı ifade ve biçim), buton "Ödeme".
- **"You may also like" (İngilizce):** 4 ürün karusel: Aroma Terapi (Tükendi), Astronot Oda Nemlendirici, AyFeneri, Çocuk Gece Feneri. Altında "Tümünü görüntüle" → `/collections/all`; ok ikonu yazının üstüne biniyor.
- **Bülten:** İngilizce bülten bölümü.

### 7.8 Kargo takip `/apps/track123` (menüde "Kargo Takip"), ekran `ss/track123-00.png`
- **Üst görsel:** Track123'ün hazır "TRACKING" yazılı kamyon görseli (marka görseli değil). Mobil adresi: https://xinglian-prod-1254213275.cos.accelerate.myqcloud.com/SHOPIFY-TRACK/STORE-LOGO/17187671428203105/traditional_bg_truck_mobile.jpg (imzalı URL; tam hâli `html/track123.html` içinde).
- **Sekmeler:**
  - "Sipariş numarası": alanlar "Sipariş numarası" + "E-posta veya telefon numarası"
  - "Takip numarası": alan "Takip numarası"
- **Buton:** "Siparişini takip et" (lacivert). Altında "Powered by Track123". Sayfa `<title>` "Track order status".

### 7.9 Hakkımızda / SSS / Yasal bildirim
- `/pages/hakkimizda`, `/pages/sss`: **404**. Sitemap'te de yok, menüde ve alt bilgide bağlantı yok.
- SSS yalnız ürün şablonlarında akordeon olarak var (`collapsible_content_7zjVTU`).
- `/policies/legal-notice`: **404** ("Sayfa bulunamadı", "Alışverişe devam et" → `/collections/all`). Ekran `ss/pol-legal-notice-00.png`.
- 404 sayfası: `ss/sayfa-404-00.png`.

### 7.10 Politikalar

**Para iade politikası** (`/policies/refund-policy`, ekran `ss/pol-refund-policy-00…03.png`). Shopify hazır şablonu, düzeltilmemiş:
- **"30 günlük iade politikamız"**: ürünü aldıktan sonra 30 gün.
- Şart: "giyilmemiş veya kullanılmamış, etiketli ve orijinal ambalajında", makbuz gerekli.
- İade başlatma: ecom11001@gmail.com.
- İade adresi: **"[İADE ADRESİNİ GİRİN]"** yer tutucusu sayfada aynen duruyor.
- Hasarlı ürün: hemen iletişime geçin.
- İstisnalar: bozulabilir, kişiye özel, kişisel bakım, tehlikeli madde. "İndirimdeki ürünler ve hediye kartları iade edilemez". Sitedeki bütün ürünler indirimli gösteriliyor.
- Değişim: iade + yeni satın alma.
- "Avrupa Birliği'ndeki 14 günlük cayma süresi".
- Para iadesi onaydan sonra **10 iş günü** içinde. **15 iş günü** geçerse e-posta atın.

**Kargo politikası** (`/policies/shipping-policy`, ekran `ss/pol-shipping-policy-00.png`):
- "Tüm Türkiye'ye **3-7 gün** içersinde hızlı teslimat yapılır. kargolarımız ücretsizdir."
- "Ortalama yanıt süresi: **2 Saat**"
- "İade/Değişim: **30** gün içinde • Başlatmak için sipariş numaranızla bize yazın."
- "Kargo süresi: **1 İş Günü**"
- "Kargo firması: Aras-Yol-DHL-PTT Kargo ile çalışmaktayız."

**İletişim bilgileri** (`/policies/contact-information`, menüde "İletişim", ekran `ss/pol-contact-information-00.png`):
- "İLETİŞİM / Sipariş, kargo ve iade/değişim için hızlı destek veriyoruz."
- "Ortalama yanıt süresi: 2 Saat", "Çalışma saatleri: 09.00-18.00", "İade/Değişim: 30 gün içinde…", "Kargo süresi: 1 İş Günü", "Kargo firması: Aras-Yol-DHL-PTT Kargo".
- "Not: Operasyon/depo adresimiz güvenlik nedeniyle paylaşılmamaktadır; iade yönlendirmesi destek ekibimiz tarafından iletilir."
- **Firma unvanı, adres, telefon, e-posta yok.**

**Gizlilik politikası** (`/policies/privacy-policy`, 1.809 kelime, ekran `ss/pol-privacy-policy-00…13.png`):
- Shopify hazır metni. "Son Güncelleme: 14 Ekim 2026".
- İşleten: "Ayluna".
- Bölümler: toplanan bilgiler, kaynaklar, kullanım, paylaşım, Shopify ilişkisi, çocuklar, güvenlik, haklar, şikayet, uluslararası aktarım, değişiklikler, iletişim.
- İletişim cümlesi aynen: "lütfen  numarasını arayın veya ecom11001@gmail.com adresine e-posta gönderin ya da **YVZNL LTD, Suite 8820, 5 Brayford Square, Londra E1 0SG, Birleşik Krallık** adresinden bizimle iletişime geçin". Telefon boş kalmış.
- KVKK / 6698 sayılı kanun geçmiyor.

**Hizmet şartları** (`/policies/terms-of-service`, 2.997 kelime, 24 bölüm, ekran `ss/pol-terms-of-service-00…19.png`):
- Mağaza adı yerine **"Mağazam"** yazıyor ("Mağazam mağazasına hoş geldiniz!").
- Dört yerde **"[LINK]"** yer tutucusu.
- Bölüm 5: "Kargo ve teslimat gecikmelerinden sorumlu tutulamayız… Ürünleri kargo şirketine aktardığımızda, mülkiyet ve kayıp riski size geçer." Türk tüketici hukukuyla çelişir.
- Bölüm 21: "Mağazam genel merkezinin bulunduğu yargı bölgesindeki **federal ve eyalet** … mahkemeleri". ABD şablonu.
- İletişim: ecom11001@gmail.com.
- Mesafeli satış sözleşmesi ve ön bilgilendirme formu yok.

---

## 8. Ekran görüntüleri (390 px, 1000 px parçalar)
Kök: `/tmp/claude-0/-home-user-cloud/d6c53161-fb62-5d87-b54b-d11d394e16d5/scratchpad/site/ss/`
- **Ana sayfa:** `ana-00.png` … `ana-03.png`
- **Etkileşimler:** `etk-menu.png` (menü açık), `etk-arama.png`, `etk-arama-oneri.png` (tahminli arama), `etk-sepet-bos.png` (boş sepet çekmecesi)
- **İletişim sayfaları:** `contact-00/01.png`, `biz-burdayiz-00/01.png`
- **Koleksiyonlar:** `col-frontpage-00…03.png`, `col-all-00…04.png`
- **Blog, arama, sepet, kargo takip:** `blog-00/01.png`, `search-00/01.png`, `cart-00/01.png`, `track123-00/01.png`
- **Politikalar:** `pol-refund-policy-00…03.png`, `pol-shipping-policy-00/01.png`, `pol-contact-information-00/01.png`, `pol-privacy-policy-00…13.png`, `pol-terms-of-service-00…19.png`, `pol-legal-notice-00/01.png` (404)
- **404 denemeleri:** `sayfa-404-00/01.png` (/pages/hakkimizda), `sayfa-sss-00/01.png` (/pages/sss)
- **Görsel inceleme kopyaları:** `../ham/gorsel/` (hero1-mob, hero1-desk, hero2-mob, hero2-desk, astronot, yildiz, logo)

## 9. Ürün sayfaları (kısa; ayrıntı bu envanterin kapsamı dışında)
- **Şablonlar:** her ürünün kendi şablonu var (ortak olanlar: LunaDream ve V2; AyFeneri ve Astronot; Dokunmatik Lamba ve Çizim Tahtası).
- **Ortak bölümler:**
  - `main` (Kaching blokları, EasySell butonu, "4.7 (2467 Onaylı Kullanıcı Yorumu)", "42 / 35 kişi şu anda bu ürünü inceliyor")
  - `eba88da5…` ("Ayluna'dan Alışveriş yapanlar çok mutlu ☺️")
  - `image_banner_Ae7wdz` ("Gece odanı AY'dınlatsın / Gün bitince herkesin bir feneri olmalı.")
  - `8beb6911…` (özellik kartları)
  - `image_with_text_8UNBF8`
  - `collapsible_content_7zjVTU` (SSS)
  - `b321ab88…`
  - `17694466126b1e0319` (Loox dinamik yorum bölümü)
- **Ürüne göre ek bölümler:** custom_liquid, horizontal_ticker, insta_stories, collage, slideshow.
- Ham HTML'ler: `ham/urun/<handle>.html`.

---

## Sorunlu / tutarsız bilgiler

**Yasal ve kimlik**
1. **Firma kimliği yok:** unvan, MERSİS/vergi no, adres, telefon, KEP hiçbir yerde yok. İletişim sayfası adresin "güvenlik nedeniyle paylaşılmadığını" söylüyor. Mesafeli satış için zorunlu bilgiler eksik.
2. **Gizlilik politikası İngiltere'deki "YVZNL LTD, Suite 8820, 5 Brayford Square, Londra E1 0SG" adresini veriyor.** Shopify mağaza ülkesi de GB. Türkiye'ye kapıda ödemeyle satan siteyle çelişiyor; diğer sayfalarda bu şirket adı yok.
3. **Telefon boş:** gizlilikte "lütfen  numarasını arayın" cümlesi telefon olmadan duruyor.
4. **Şablon yer tutucuları yayında:** "[İADE ADRESİNİ GİRİN]" (iade), "Mağazam" ve 4× "[LINK]" (hizmet şartları), ABD "federal ve eyalet mahkemeleri".
5. **Eksik metinler:** KVKK aydınlatma metni, çerez politikası, çerez onay bandı, mesafeli satış sözleşmesi, ön bilgilendirme formu ve yasal bildirim (`/policies/legal-notice` 404) yok.
6. **İade politikası "indirimdeki ürünler iade edilemez" diyor;** sitede neredeyse her ürün indirimli gösteriliyor. Ayrıca "giyilmemiş, etiketli" giyim şablonu dili kullanıyor. Hizmet şartları teslim öncesi riski alıcıya yüklüyor.

**İade süresi: 4 farklı rakam**
7. Politika: **30 gün**.
8. Hero görseli ve 15 ürün sayfasının hepsi: **"90 Gün İade" / "90 Gün Para İade Garantisi"**.
9. Dokunmatik Lamba ve Çizim Tahtası SSS'si: **"14 gün içinde iade"**.
10. İade politikasında AB için ayrıca 14 gün cayma.

**Garanti**
11. Her yerde "1 Yıl Garanti". Retro Mini Pikap sayfasında aynı anda hem "1 Yıl Garanti" hem "2 yıl garanti".

**Kargo süresi ve ücreti**
12. Kargo süresi için 7 farklı ifade var:
    - Politika "3-7 gün"
    - Aynı politika "Kargo süresi: 1 İş Günü"
    - 4 ürün sayfası "2-5 gün"
    - 2 ürün "1–3 iş günü içinde kargoya verilir"
    - "Hafta içi aynı gün"
    - "14:00'e kadar aynı gün" (Sunset)
    - "Ertesi Gün Kargoda" (AyFeneri ve Astronot bandı)
    - "Kredi kartıyla aynı gün kargo" (Aroma, Galaksi Night)
13. EasySell'de **79,99 TL "Hızlı Kargo"** satılıyor ("aynı gün kargoya teslim"). Ürün sayfaları kartla ödemede aynı günü zaten bedava vaat ediyor.
14. **Kapıda ödeme ücreti 80 TL** (EasySell, sabit). Hiçbir politikada ve ürün sayfasında yazmıyor. Sitede "kargolarımız ücretsizdir" deniyor.

**Uydurma görünen sayılar ve sahte aciliyet**
15. **"2467 Onaylı Yorum / 2467 Onaylı Kullanıcı Yorumu":** hero görselinde ve 15 ürün sayfasının hepsinde aynı sayı, hepsi "4.7". Loox'taki gerçek toplam **168** yorum. 4 ürünün hiç yorumu yok.
16. **"42 kişi şu anda bu ürünü inceliyor":** 12 üründe sabit 42, LunaDream ve Galaksi Night'ta sabit 35.
17. **Mutlu müşteri:** "10.000 Mutlu Müşteri" (Çocuk Gece Feneri) ve "2000 Mutlu Müşteri" (Retro Pikap, Galaksi Ambiyans).
18. **Duyuru bandı:** "Bugüne Özel %20 İndirim" sayacı her sayfa açılışında 1:02:00'dan yeniden başlıyor. Rozetlerdeki indirimler %14–%48 arasında, %20 ile uyuşmuyor.
19. **Sepet çekmecesi:** "Süre bitene kadar senin için ayrıldı 05:00": gerçek rezervasyon yok.
20. **Dokunmatik Ambiyans Lamba:** eski fiyat (1.299,00) yeni fiyattan (1.299,99) düşük, üstü çizili gösteriliyor.

**İsim ve içerik**
21. "Astronot **Hava Temizleyici**" teklifi aslında bir nemlendirici / aroma difüzör ürününe bağlı.
22. Loox ana sayfa karuselinde başka ürünlerin (hoparlör/saat) yorumları ürün adı olmadan gösteriliyor.
23. "Tüm Ürünler" menüsü 9 ürünlük `frontpage`'e gidiyor; 6 ürün menüden ve ana sayfadan ulaşılamıyor.

**Teknik ve görünüm hataları**
24. `/collections/all`'da EasySell butonu stoktaki ürünlerde de **"Tükendi"** yazıyor.
25. Koleksiyon kartında COD butonu dar sütunda devasa siyah bloğa dönüşüyor.
26. Ana sayfadaki GIF **16,9 MB**. Ayrıca "Veo" yapay zekâ filigranı görünüyor. Logo 2,3 MB PNG, hero 1,5 MB PNG.
27. **Yazım hataları:** "Bunlarıda sevebilirsin", "%5 İNDİRM", "içersinde", "Biz Burdayız", sayfa adı "İletişim kopyası", "galayx" handle, "ask-saati" handle'ı Kum Saati'nde.
28. **İngilizce kalan metinler:** "SAVE 14%", "You may also like", "Subscribe to our emails / Join our email list… / Sign up", "Menu", "This field is required", "Track order status", slider aria metinleri.
29. **Çift bülten:** ikincil sayfalarda iki ayrı bülten formu (biri İngilizce) üst üste.
30. **Fiyat biçimi:** "1,699.99TL" (Türkçe değil: 1.699,99 TL). Sepette ayrıca "0.00 TRY".
31. **Hero:** slayt 2'nin bağlantısı yok. Slayt 1'de görsele gömülü sahte buton ile gerçek buton üst üste. "Şimdi İncele" ve "Tümünü görüntüle" butonlarında ok yazının üstüne biniyor.
32. **Alt bilgi:** ödeme logoları Amex/Diners/Discover/JCB; Türkiye'de yaygın Troy yok. Kapıda ödeme seçeneği alt bilgide belirtilmiyor.
33. **Sayfa ve bölüm boşlukları:** sosyal medya hesabı yok. Blog boş. Promo popup ve müzik çalar bölümleri boş ama sayfada yer tutuyor.
34. **Meta açıklaması** ve **paylaşım görseli** (`og:image`) yok.

---

## Yeniden tasarımda taşınması gerekenler (kontrol listesi)

**Üst bölüm**
- [ ] Duyuru bandı: tek mesaj. Sahte sayaç kaldırılmalı ya da gerçek kampanya bitişine bağlanmalı. Ürün şablonlarındaki ikinci bant mesajları gözden geçirilmeli.
- [ ] Logo (https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Adsiz_tasarim_66.png?v=1769445970): küçük ve hafif sürüm, favicon.
- [ ] Menü bağlantıları: Ana sayfa, Galaxy USB Projektör, LunaDream, AyFeneri, Tüm Ürünler (→ `/collections/all` olmalı), İletişim, Kargo Takip (`/apps/track123`), Oturum aç.
- [ ] Tahminli arama (öneri + ürün listesi).
- [ ] Sepet ikonu → çekmece.

**Ana sayfa bölümleri**
- [ ] Hero 2 slayt: LunaDream ve AyFeneri. Yazılar HTML'e taşınmalı, görsele gömülmemeli. Her slayta bağlantı.
- [ ] Loox yorum karuseli (uygulama bloğu `loox_card_carousel_section`, widget 3DlBqrswrJ).
- [ ] Öne çıkan ürün karuseli (9 ürün; "Tümünü gör" eklenmeli).
- [ ] AyFeneri özellik çubuğu (4 madde) ve görsel + metin ("Ay ışığını evine getir", → `/products/lamba`). GIF yerine MP4/WebM.
- [ ] Dalga ayırıcılar (marka öğesi olarak kalacaksa tek tane).

**Sepet çekmecesi**
- [ ] Boş sepet metni, oturum açma satırı, ürün satırları, "Ödenecek Tutar", tasarruf satırı, "Ödeme" butonu, ödeme logoları.
- [ ] Tema özellikleri karar bekliyor: sepet içi ek ürün, hediye, not, indirim kodu, koşul onayı, 5 dk sayaç (önerim kaldırmak).

**EasySell COD formu ve teklifler** (uygulama, tema dışı; yeni tasarımla uyumlu stillenmeli)
- [ ] Buton metni "Kapıda Ödeme ile Sipariş Ver".
- [ ] Form alanları (Ad, Soyad, Telefon, Adres, İl, İlçe, ödeme tipi Nakit / Kredi Kartı), 80 TL ücret satırı.
- [ ] 4 bump:
  - Hızlı Kargo 79,99
  - Yıldız Işığı Nemlendirici 749,99
  - Kum Saati Lamba 699,99
  - Astronot Oda Nemlendirici 749: adı düzeltilmeli
- [ ] "Bekle!" %5 downsell.
- [ ] `/collections/all` "Tükendi" hatası ve koleksiyon kartındaki buton taşması düzeltilmeli.
- [ ] Kaching adet ve hediye blokları (ürün sayfası).

**Kaldırılan bölümler**
- [ ] Promo popup: şu an boş. Kullanılacaksa bülten %5 kodu burada verilebilir.
- [ ] Müzik çalar: boş, kaldırılabilir.

**Yukarı çık butonu**
- [ ] Davranışı aynı kalabilir (400 px sonra, yumuşak kaydırma). EasySell yapışkan butonuyla çakışmamalı.

**Alt bilgi**
- [ ] Bülten (%5), politika bağlantıları, ödeme logoları (Troy ve kapıda ödeme eklenmeli), telif.
- [ ] Eklenecekler: firma bilgileri, iletişim, sosyal hesaplar, menü sütunları.

**Sayfalar**
- [ ] İletişim (iki kopya tek sayfaya indirilmeli).
- [ ] Koleksiyon (filtre: stok, fiyat; 9 sıralama).
- [ ] Arama, sepet ("You may also like" → Türkçe), 404, Track123.
- [ ] Blog (boş): kaldırılabilir ya da doldurulabilir.

**Politikalar** (metinler yeniden yazılmalı; yasal danışmana gösterilmeli)
- [ ] İade: tek süre seçilmeli (30 mu, 90 mı?), yer tutucu silinmeli, gerçek iade süreci yazılmalı.
- [ ] Kargo: tek süre, 80 TL kapıda ödeme ücreti açıkça yazılmalı.
- [ ] Gizlilik → KVKK aydınlatma metni.
- [ ] Hizmet şartları → mesafeli satış sözleşmesi ve ön bilgilendirme formu.
- [ ] İletişim bilgileri: unvan, adres, telefon, e-posta.
- [ ] Yasal bildirim sayfası.

**Genel**
- [ ] Renkler: krem #F7F4EF, lacivert #1F2A44, metin #121212, mor vurgu #6D388B.
- [ ] Yazı tipi: Poppins (Nunito Sans yalnız duyuru bandında).
- [ ] Fiyat biçimi Türkçe (1.699,99 TL).
- [ ] Yerelleştirme: bütün İngilizce kalan metinler.
- [ ] Sayılar: "2467 yorum", "42 kişi inceliyor", "10.000 / 2000 mutlu müşteri" ya gerçek veriye bağlanmalı ya kaldırılmalı.
- [ ] SEO: meta açıklaması, `og:image`, sosyal `sameAs`.
- [ ] Pikseller: Meta piksel, olası Klaviyo, özel piksel ve Kaching pikseli tema değişince korunmalı (uygulama gömmeleri açık kalmalı).
