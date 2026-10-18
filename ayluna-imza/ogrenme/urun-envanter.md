# Ürün sayfaları envanteri — ayluna.shop

Tarih: 18 Ekim 2026 (pazar). Kapsam: 13 ürün sayfası, telefon görünümü 390×844. Sadece okundu: sepete ekleme, satın al, form yok.

Kaynaklar: `products/<handle>.json` ve `.js` (fiyat, varyant, stok, görseller), sayfanın kendisi (bölüm sırası, metinler), Loox yorum iframe'i (gerçek puan). Görsellerin hepsi tek tek açılıp okundu.

Yöntem notu: Her sayfa bir kez açıldı. Meta, TikTok ve Google alan adları her sayfada engelliydi. İlk açılan sayfada (Sunset) Shopify'ın kendi analitik isteği (`/api/collect`) engellenmeden gitti. Kalan 12 sayfada Shopify analitiği de engellendi.

Ham veri ve ekran görüntüleri: `/tmp/claude-0/-home-user-cloud/d6c53161-fb62-5d87-b54b-d11d394e16d5/scratchpad/site/urun/` (bulut oturumu kapanınca silinir; kalıcı olan bu dosyadır).

- `<handle>-N.png`: tam sayfa ekran görüntüsü, 1000 px yükseklikte parçalar
- `pano/<handle>-sayfaK.jpg`: parçaların 4'lü özet panosu; `gorsel/pano/<handle>-pK.jpg`: ürün görsellerinin 2×2 panosu
- `veri/<handle>.json` (bölümler, bloklar, Loox metni), `html/`, `json/`, `js/`, `loox/`, `ozet/`

## Özet tablo

Bölüm = ürün şablonundaki bölüm sayısı (ayraçlar hariç; üst şerit, başlık, altbilgi gibi global bölümler sayılmadı). Loox = yorum uygulamasındaki gerçek kayıt; "sayfada" = başlık altında yazan.

| # | Ürün | Fiyat / karşılaştırma | Görsel | Bölüm | Loox gerçek ↔ sayfada | En ciddi sorun |
|---|---|---|---|---|---|---|
| 1 | Astronot Oda Nemlendirici Aroma Difüzör (`astronot-oda-nemlendirici-aroma-difuzor`) | 799,00 TL / — | 1 | 8 | 0 yorum ↔ 4.7 / 2467 | Sayfa gövdesi AyFeneri'ninki; kutu "masa lambası" diyor |
| 2 | Ayluna Retro Mini Pikap (`ayluna-retro-mini-pikap`) | 1.499,00 TL / 1.999,99 TL (gerçek %25) | 9 | 11 | 5.0 / 10 yorum ↔ 4.7 / 2467 | 4.7/2467 ↔ Loox 10 (aynı gün); yapay zekâ "Doğrulanmış Alıcı" fotoğrafları |
| 3 | Eğitici Akıllı Çizim Tahtası (`egitici-akilli-cizim-tahtasi`) | 1.199,00 TL / 1.999,00 TL (gerçek %40) | 8 | 13 | 5.0 / 12 yorum ↔ 4.7 / 2467 | Gelişim iddiaları + SSS'de 14 gün iade |
| 4 | Dokunmatik Ambiyans Lamba (`dokunmatik-ambiyans-lamba`) | 1.299,99 TL / 1.299,00 TL (karşılaştırma < fiyat) · **Tükendi** | 7 | 13 | 5.0 / 7 yorum ↔ 4.7 / 2467 | Tüm sayfa çizim tahtası içeriği; karşılaştırma < fiyat |
| 5 | Sunset Lamba (`sunset-lamba`) | 699,00 TL / 999,00 TL (gerçek %30) | 5 | 10 | 0 yorum ↔ 4.7 / 2467 | 4.7/2467 + "4.9 · 2.400+ satış" ↔ Loox 0 |
| 6 | Ayluna Çocuk Gece Feneri (`ayluna-cocuk-gece-feneri`) | 1.599,00 TL / — | 9 | 10 | 0 yorum ↔ 4.7 / 2467 | Uyku iddiaları + "+10.000 müşteri" ↔ Loox 0 |
| 7 | Ayluna Galaksi Night Projektör (`ayluna-galaksi-night-projektor`) | 2.199,00 TL / 2.999,00 TL (gerçek %27) | 8 | 12 | 5.0 / 6 yorum ↔ 4.7 / 2467 | "Anksiyete giderici, kortizol" sağlık iddiası |
| 8 | Aroma Terapi Nemlendirici (`aroma-terapi-nemlendirici`) | 1.499,00 TL / 1.999,00 TL (gerçek %25) · **Tükendi** | 7 | 9 | 5.0 / 6 yorum ↔ 4.7 / 2467 | Uydurma "Doğrulanmış Müşteri" kartları; Loox 6 aynı gün |
| 9 | Galaksi Ambiyans Işığı (`galaksiambiyanisigi`) | 1.499,00 TL / 2.898,00 TL (gerçek %48) | 7 | 9 | 5.0 / 13 yorum ↔ 4.7 / 2467 | Şişirilmiş karşılaştırma fiyatı (%50) + 2 yıl/1 yıl garanti |
| 10 | LunaDream Gece Lambası V2 (`lunadream-gece-lambasi-v2`) | 1.449,00 TL / 1.999,00 TL (gerçek %28) · **Tükendi** | 9 | 11 | 0 yorum ↔ 4.7 / 2467 | Tükenmiş üründe "3 günde 399 satıldı"; sayfa başka ürünü gösteriyor |
| 11 | Yıldız Işığı Nemlendirici (`yildiz-isigi-nemlendirici`) | 849,99 TL / 1.099,00 TL (gerçek %23) | 7 | 6 | 5.0 / 6 yorum ↔ 4.7 / 2467 | Teknik tablo ve kutu içeriği AyFeneri'nin; 280 ml ↔ 2,8 L |
| 12 | Ayluna Kum Saati Lamba (`ask-saati`) | 799,00 TL / 999,00 TL (gerçek %20) | 4 | 3 | 1.0 / 1 yorum ↔ 4.7 / 2467 | Tek gerçek yorum 1★ "ürün gelmedi" ↔ sayfa 4.7/2467 |
| 13 | Ayluna AyFeneri (`lamba`) | 1.649,99 TL / 2.499,00 TL (gerçek %34) | 9 | 8 | 4.9 / 43 yorum ↔ 4.7 / 2467 | 4.7/2467 ↔ Loox 43 (4.9); dört farklı indirim oranı |

## Ortak sayfa iskeleti

Tema: Shopfinity 1.5.4 (tema adı "ayluna-orijinal-iskelet-korunmus"). Bütün ürün şablonları aynı tabandan kopyalanmış: bölüm anahtarları (`announcement_bar_m7VX6j`, `eba88da5…`, `horizontal_ticker_rbYQET`, `image_banner_Ae7wdz`, `8beb6911…`, `image_with_text_8UNBF8`, `collapsible_content_7zjVTU`, `17694466126b1e0319`) her şablonda aynı. Kopyalanınca metinlerin çoğu güncellenmemiş.

Yukarıdan aşağıya:

1. `sections--28025597690084__custom_liquid_XWzNR9`: üst geri sayım şeridi, "Bugüne Özel %20 İndirim 01:01:xx" (global).
2. `sections--28025597690084__header`: menü, logo, arama, sepet (yapışkan, global). `cart-drawer`: gizli sepet çekmecesi.
3. `announcement_bar_*`: ürüne özel tek cümle, kayarak tekrar eder. Yıldız Işığı ve Kum Saati sayfalarında yok.
4. `__main`, ana ürün bölümü. Blok sırası:
   galeri (kaydırıcı + küçük resimler) → başlık → "4.7 (2467 Onaylı Kullanıcı Yorumu)" → fiyat + indirim rozeti → (kısa açıklama) → kargo sayacı "… içerisinde sipariş verirsen bugün kargoda" → özellik başlığı + 5–7 ikonlu kart → "X kişi şu anda bu ürünü inceliyor" → kargo notu "KREDİ KARTI İLE VERİLEN SİPARİŞLER HIZLI KARGO İLE ÇIKARTILMAKTADIR" → (Kaching paket teklifi) → "GÜVENLİ ÖDEME İLE AL" + "Kapıda Ödeme ile Sipariş Ver" (EasySell formu; kapıda ödeme ücreti 80 TL) → ödeme logoları → teslimat zaman çizelgesi (bugün → +1-2 gün kargoda → +3-5 gün teslim) → (video yorumlar) → güven şeridi "1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi" → yapışkan sepet çubuğu → 3'lü kısa yorum kaydırıcısı → açılır SSS ya da teknik bilgi.
5. Sosyal kanıt: `eba88da5…` WhatsApp/DM ekran görüntüsü kaydırıcısı ("+2000 Mutlu Annenin söylediklerini okuyun" ya da "%100 Müşteri Memnuniyeti"), `insta_stories_xe3xA6` (3 hikâye), `horizontal_ticker_*` kayan şerit.
6. Anlatım: `image_banner_Ae7wdz` GIF afiş + başlık, `8beb6911…` 4 başlıklı özellik satırları + görsel, `image_with_text_8UNBF8` görsel + metin + buton.
7. SSS: `collapsible_content_7zjVTU` ya da `custom_liquid_*`.
8. `b321ab88…` ayraç → `17694466126b1e0319` Loox yorum iframe'i.
9. Global: `promo-popup`, `scroll-to-top-btn`, `global-music-player` (görünmüyor) → altbilgi: "%5 İNDİRM KAZANMAK İÇİN ABONE OL" e-posta formu, ödeme logoları, politika bağlantıları.

Her sayfada ortak olan sorunlar:

- "4.7 (2467 Onaylı Kullanıcı Yorumu)" tema içine sabit yazılmış. 13 sayfada aynı sayı var. Loox'taki gerçek sayılar 0 ile 43 arasında.
- "X kişi şu anda bu ürünü inceliyor" sayısını JavaScript 30 ile 50 arasında rastgele üretiyor.
- Üst sayaç her sayfa yüklemesinde 1 saat 2 dakikadan yeniden başlıyor, yani sahte. Kargo sayacı her gün saat 15:00'e sayıyor ve pazar günü de "bugün kargoda" yazıyor.
- Güven şeridinde "90 Gün Para İade Garantisi" yazıyor. Gerçek iade süresi 30 gün.
- "+2000 Mutlu Annenin" kaydırıcısında 16 ekran görüntüsü var. Aynı görüntüler 7 farklı ürünün sayfasında kullanılmış. Konuşmalar yıldız/galaksi projeksiyonlu ürünlerle ilgili; o sayfanın ürünüyle değil. AyFeneri şablonunu kullanan sayfalarda ise fener müşterilerinin sohbetleri var.
- Fiyat ekran okuyucu etiketleri ters: indirimli fiyat "Normal fiyat", üstü çizili fiyat "İndirimli fiyat" diye okunuyor.
- Kaching'in ürün verisi stok sayısını sayfa kaynağında herkese gösteriyor (ör. AyFeneri -612, Kum Saati -246). Çoğu üründe stok politikası "continue": stok bitse de satış açık kalıyor. "Stoklar sınırlı" yazısıyla çelişiyor.
- Yazım hataları: "ŞİPARİŞLER", "İNDİRM", "terchi", "Tabikide", "mevcuttun", "olucak", "Proyeksiyonlu".
- Açıklama alanı (`body_html`) 13 üründe de boş. Bütün metin tema bölümlerinde duruyor.

## Ürünler arası farklar

- **Aynı şablonu paylaşanlar:** AyFeneri ile Astronot aynı şablonu kullanıyor (`template--28025597165796`). Çizim Tahtası ile Dokunmatik Lamba da aynı şablonda (`template--28025597100260`). Bu yüzden Astronot ve Dokunmatik sayfaları başka bir ürünü anlatıyor.
- **Kaching paket teklifi olanlar:** Pikap, Çizim, Dokunmatik, Galaksi Projektör, Aroma, Galaksi Ambiyans, LunaDream V2, Yıldız, AyFeneri. Olmayanlar: Astronot, Sunset, Çocuk Feneri, Kum Saati.
- **Ek ürün öneren paketler:** Galaksi Projektör (+Yıldız), Galaksi Ambiyans (+AyFeneri), LunaDream V2 (+Yıldız), Yıldız (+LunaDream), AyFeneri (+Kum Saati, +Yıldız).
- **Kargo sayacı:** "bugün kargoda" sayacı Astronot, Pikap, Çizim, Dokunmatik, Sunset, Çocuk Feneri ve AyFeneri'de var. Galaksi Projektör ile LunaDream V2'de onun yerine "yarın kargoda" yazısı, il seçimli teslim tahmini ve "3 günde 399 adet satıldı / Son 10 günün en düşük fiyatı" var.
- **Video yorumlar:** Sunset ve Çocuk Feneri'nde ana bölümün içinde. Galaksi Projektör ve LunaDream V2'de ayrı bölüm olarak.
- **Özel Liquid hikâye bölümleri:** Pikap (2), Çizim/Dokunmatik (2), Galaksi Projektör (video ve mesajlar), LunaDream V2 (video, mesajlar, mutlu kullanıcılar). Sağlık iddialı slayt yalnız Galaksi Projektör'de.
- **Tükenenler:** Dokunmatik, Aroma, LunaDream V2. Varyantı olan tek ürün Çizim Tahtası (Sarı / Pembe).
- **Sayfa uzunluğu:** 3.168 px (Kum Saati) ile 11.901 px (Pikap) arasında. Galaksi Ambiyans, Yıldız ve Kum Saati'nde yapışkan buton İngilizce ("Add to cart").

---

## 1. Astronot Oda Nemlendirici Aroma Difüzör — `astronot-oda-nemlendirici-aroma-difuzor`

- **Adres:** https://ayluna.shop/products/astronot-oda-nemlendirici-aroma-difuzor
- **Fiyat:** 799,00 TL · karşılaştırma: yok
- **Varyantlar** (Title): Default Title — 799,00 TL — satışta
- **Şablon:** `template--28025597165796` · sayfa yüksekliği 6283 px · vendor: Ayluna
- **Ekran görüntüleri** (7 parça, klasör `…/scratchpad/site/urun/`): `astronot-oda-nemlendirici-aroma-difuzor-1.png`, `astronot-oda-nemlendirici-aroma-difuzor-2.png`, `astronot-oda-nemlendirici-aroma-difuzor-3.png`, `astronot-oda-nemlendirici-aroma-difuzor-4.png`, `astronot-oda-nemlendirici-aroma-difuzor-5.png`, `astronot-oda-nemlendirici-aroma-difuzor-6.png`, `astronot-oda-nemlendirici-aroma-difuzor-7.png`
- Şablon AyFeneri (`lamba`) ile aynı (`template--28025597165796`). Başlık, fiyat ve tek görsel dışında her şey AyFeneri içeriği: özellikler, teknik tablo, kutu içeriği, SSS, afiş GIF'i, fener görselleri ve fener müşteri sohbetleri.
- Nemlendiriciye ait tek satır bilgi yok (hazne, buhar, aroma, kullanım süresi).

### Görseller (1)

1. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/EkranResmi2026-07-1022.46.52.png?v=1783712831
   Ürün fotoğrafı, yazısız; başka yerden alınmış düşük çözünürlüklü ekran görüntüsü (dosya adı "EkranResmi…", 822×762). Uzay kapsülü içinde astronot figürü, sarı ışık. Sayfada üstüne "EN ÇOK SATAN" rozeti biniyor.

### Bölüm sırası

Tam id biçimi: şablon bölümleri `shopify-section-template--28025597165796__<anahtar>`, global bölümler `shopify-section-sections--28025597690084__<anahtar>` (altbilgi `…28025597657316__footer`).

1. `custom_liquid_XWzNR9` — Üst geri sayım şeridi (global): "Bugüne Özel %20 İndirim" + sayaç
2. `header` — Başlık (global): menü, logo, arama, sepet
3. `announcement_bar_dEW9QR` — Duyuru şeridi: 3D Güvenli Ödeme İle Satın Al Ertesi Gün Kargoda
4. `main` — **Ana ürün bölümü** (galeri 1 görsel), blok sırası:
   - Başlık: Astronot Oda Nemlendirici Aroma Difüzör
   - Puan satırı: 4.7 ( 2467 Onaylı Kullanıcı Yorumu)
   - Fiyat satırı: 799,00 TL · rozet "%25 İndirim"
   - Kısa açıklama: Geceye bir ışık yak, sesini aç ve odanı kendi küçük kaçışına çevir.
   - Kargo sayacı: 🚚 · 19:34:35 içerisinde sipariş verirsen bugün kargoda.
   - Özellik kartları: Gerçek Ay Işığı Ambiyansı · Otomatik Sensörlü Aydınlatma · Uzaktan Kontrol (Kumanda / Bluetooth) · Şarjlı ve Kablosuz Kullanım · Her Odaya Uyumlu Modern Tasarım
   - Canlı izleyici sayacı: 32 kişi şu anda bu ürünü inceliyor.
   - Kargo notu: KREDİ KARTI İLE VERİLEN SİPARİŞLER HIZLI KARGO İLE ÇIKARTILMAKTADIR
   - Satın al butonları: GÜVENLİ ÖDEME İLE AL · Kapıda Ödeme ile Sipariş Ver
   - Ödeme logoları: Amex, Diners, Discover, JCB, Mastercard, Visa
   - Teslimat zaman çizelgesi: 18 Ekm · Siparişiniz Oluşturuldu · 19 Ekm - 20 Ekm · Kargonuz Hazırlandı · 21 Ekm - 23 Ekm · Evinize Teslim Edildi
   - Güven şeridi: 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi
   - Yapışkan sepet çubuğu: Astronot Oda Nemlendirici Aroma Difüzör · 799.00TL · Sepete Ekle
   - Kısa yorum kaydırıcısı (3 yorum): Ambiyansı inanılmaz değiştirdi. Ay yansıması çok gerçekçi ve ışık tonu göz yormuyor. · Mehmet L. · Gece kalkınca sensör otomatik yakıyor, büyük rahatlık. Kumanda ve Bluetooth’un hepsi tek üründe olması çok iyi · Gülsüm S. · Şarjlı olması harika; istediğim yere taşıyorum. Hem dekor gibi duruyor hem de gerçekten işe yarıyor · Zeynep R.
   - Açılır: Teknik Özellikler: Güç Kaynağı: Dahili batarya · Stil Seçenekleri: Kumandalı, Bluetooth, Sensörlü · Voltaj: ≤ 36V · Boyut: 70 × 72 × 242 mm · Modelleme: Geometrik üç boyutlu tasarım · Tarz: Modern ve sade · Giriş Voltajı: 5V – 1A · Nominal Güç: 5W · LED Gücü: 1.5W (5×0.2W LED modülü + 1×3W LED modülü) · Hoparlör Gücü (Bluetooth model): 4 Ω, 3W · Batarya Kapasitesi: 2400 mAh
   - Açılır: Kutu İçeriği: Masa Lambası × 1 · USB Kablo × 1 · 16 ülke için uyumlu adaptör/başlık × 1 · Uzaktan Kumanda × 1
   - Açılır soru: Hoparlör olarak kullanabilir miyim ?
   - Açılır soru: Ay ışığı ne kadar belirgin?
   - Açılır soru: Hediyem zamanında yetişir mi?
   - Açılır soru: Hep fişe mi takılı olucak?
5. `eba88da5-80ac-47fc-aa75-997cfe7b2e59` — Yorum ekran görüntüsü kaydırıcısı: Ayluna'dan Alışveriş yapanlar çok mutlu ☺️ [6 görsel: WhatsApp_Image_2026-01-31_at_23.23.27_91fc5e…, WhatsApp_Image_2026-01-26_at_17.14.10.jpg, WhatsApp_Image_2026-01-26_at_17.21.47.jpg …]
6. `image_banner_Ae7wdz` — GIF afiş + başlık: Gece odanı AY'dınlatsın · GÜN BİTİNCE HERKESİN BİR FENERİ OLMALI. [1 görsel: Grselden_Video_Oluturma-ezgif.com-video-to-g…]
7. `8beb6911-28c6-482c-976a-e5421ad3e8df` — Özellik satırları (4 başlık + görsel): Gerçek Ay Işığı Ambiyansı · Duvara yansıyan ay görüntüsüyle bulunduğun ortamı anında daha sıcak, sakin ve dekoratif hale getirir. · Otomatik Sensörlü Aydınlatma · Hareketi algıladığında otomatik yanar; gece düğme aramadan güvenle yürümeyi sağlar. · Uzaktan Kontrol · Işığı yataktan kalkmadan aç/kapat, modları yönet. Uygun modelde Bluetooth ile daha fazla kontrol. · Şarjlı ve Kablosuz Kullanım · Dahili batarya sayesind … [1 görsel: ChatGPT_Image_26_Oca_2026_16_34_42.png]
8. `image_with_text_8UNBF8` — Görsel + metin + buton: Ay Işığı Ambiyansı, Tek Dokunuşla · Ayluna, duvara gerçekçi ay yansıması vererek bulunduğun alanı anında daha sıcak ve huzurlu hale getirir. Yumuşak ışığıyla gece kullanımı için idealdir. · Huzurlu Ambiyansı Keşfet [1 görsel: ChatGPT_Image_26_Oca_2026_16_49_38.png]
9. `collapsible_content_7zjVTU` — SSS (açılır): SSS, 8 soru (aşağıda)
10. `b321ab88-2b59-4dba-bade-54885c874ca5` — Ayraç
11. `17694466126b1e0319` — Loox yorum uygulaması (iframe; ayrıntı aşağıda)
12. `footer` — Altbilgi (global): %5 indirim için e-posta aboneliği, ödeme logoları, politikalar

### Paket teklifi, geri sayım, kargo

- **Paket (Kaching):** yok
- **Geri sayım:** üst şerit "Bugüne Özel %20 İndirim 01 SAAT : 01 DK : 38 SAN" (her yüklemede yeniden başlar); kargo sayacı "… içerisinde sipariş verirsen bugün kargoda" (15:00'e sayar)
- **Duyuru şeridi:** 3D Güvenli Ödeme İle Satın Al Ertesi Gün Kargoda
- **Güven şeridi:** 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi

### SSS

**Kaynak: `main`**

- **Hoparlör olarak kullanabilir miyim ?** Tabikide evet gelişmiş uzaktan bağlantı özelliği sayesinde telefonunuzdan bağlanarak dilediğiniz müziği açabilir ve evinizin ambiyansını daha üst seviyelere çıkartabilirsiniz.
- **Hediyem zamanında yetişir mi?** Tüm Türkiye'ye hızlı kargo ile 2-5 gün arasında kargolama yapmaktayız her gün kargo çıkışlarımız yapılmaktadır içiniz rahat bir şekilde satın alabilirsiniz.
- **Ay ışığı ne kadar belirgin?** Ürünümüzde en güncel projeksiyon çipi mevcuttun hd kalitede yansıtma yapar Gökyüzünü odanıza taşımak için bir adım uzaktasınız.
- **Hep fişe mi takılı olucak?** Tabikide hayır :)2400mh bataryası sayesinde uzun süre şarjlı bir şekilde istediğiniz ortamda kullanım sağlayabilirsiniz.

**Kaynak: `collapsible_content_7zjVTU`**

- **Bu modelde hangi özellikler var?** Bu modelde hareket sensörü, uzaktan kumanda, Bluetooth hoparlör ve şarjlı (kablosuz) kullanım özelliklerinin tamamı birlikte bulunur.
- **Hareket sensörü nasıl çalışır?** Sensör, hareket algıladığında ışığı otomatik olarak açar. Belirli bir süre hareket algılamazsa ışık kendiliğinden kapanır. Gece koridor, yatak yanı ve çocuk odası kullanımında çok pratiktir.
- **Kumanda ile neleri kontrol edebilirim?** Kumanda ile ışığı açıp kapatabilir, uygun modlarda ışık ayarlarını yönetebilirsin. Günlük kullanımda özellikle yataktan kalkmadan kontrol için idealdir.
- **Bluetooth hoparlöre nasıl bağlanırım?** Telefonunun Bluetooth ayarlarını aç, cihaz listesinden ürünü seç ve eşleştir. Eşleştirdikten sonra müzik, meditasyon sesleri veya video sesleri hoparlörden oynatılabilir.
- **Ürün şarjlı mı, prizde mi çalışır?** Ürün dahili bataryalıdır (2400 mAh). USB ile şarj edilir ve şarj olduktan sonra kablosuz şekilde kullanılabilir.
- **Şarjı ne kadar gider?** Kullanım süresi; ışık parlaklığı, sensörün ne kadar sık devreye girdiği ve Bluetooth kullanımına göre değişir. Standart kullanımda günlük ihtiyaçlar için yeterli performans sunar.
- **Gece kullanımında göz yorar mı?** Hayır. Yumuşak ve loş LED ışık verdiği için gece kullanımına uygundur. Gece kalkışlarında ortamı rahatsız etmeden aydınlatmaya yardımcı olur.
- **Çocuk odasında kullanmak güvenli mi?** LED aydınlatma düşük ısı üretir. Bu nedenle gece lambası olarak güvenli bir kullanım sunar. Yine de şarj/kablo işlemlerini çocukların tek başına yapmamasını öneririz.


### Yorumlar

- **Sayfada yazan:** "4.7 (2467 Onaylı Kullanıcı Yorumu)" (sabit metin)
- **Loox gerçek:** 0 yorum ("Yorum yapan ilk kişi olun")

### Açıklama (body_html)

- Boş. Ürün metni yalnız tema bölümlerinde.

### Sorunlu iddialar

- **Kopya içerik (kritik):** Sayfa gövdesi tümüyle AyFeneri: "Gerçek Ay Işığı Ambiyansı", "Otomatik Sensörlü Aydınlatma", "Şarjlı ve Kablosuz", Teknik Özellikler (70×72×242 mm, 2400 mAh, hoparlör 3 W), Kutu İçeriği "Masa Lambası × 1… 16 ülke adaptör", SSS "Ay ışığı ne kadar belirgin?", afiş "Gece odanı AY'dınlatsın".
- **Kutu çelişkisi:** Nemlendirici satılıyor, kutu içeriği "Masa Lambası" yazıyor.
- **Fiyat:** Karşılaştırma fiyatı yok ama rozet "%25 İndirim"; üst şerit "%20".
- **Uydurma puan:** Sayfa "4.7 (2467 Onaylı Kullanıcı Yorumu)"; Loox: 0 yorum.
- **Uydurma yorum:** Kısa yorumlar AyFeneri'nden ("Ay yansıması çok gerçekçi", "sensör otomatik yakıyor").
- **İade:** Güven şeridi "90 Gün Para İade Garantisi" (gerçek 30 gün).
- **Görsel:** Tek görsel, başka yerden alınmış ekran görüntüsü; "EN ÇOK SATAN" rozeti teyitsiz.

---

## 2. Ayluna Retro Mini Pikap — `ayluna-retro-mini-pikap`

- **Adres:** https://ayluna.shop/products/ayluna-retro-mini-pikap
- **Fiyat:** 1.499,00 TL · karşılaştırma: 1.999,99 TL → gerçek indirim %25.0
- **Varyantlar** (Title): Default Title — 1.499,00 TL — satışta
- **Şablon:** `template--28025597329636` · sayfa yüksekliği 11901 px · vendor: Ayluna
- **Ekran görüntüleri** (12 parça, klasör `…/scratchpad/site/urun/`): `ayluna-retro-mini-pikap-1.png`, `ayluna-retro-mini-pikap-2.png`, `ayluna-retro-mini-pikap-3.png`, `ayluna-retro-mini-pikap-4.png`, `ayluna-retro-mini-pikap-5.png`, `ayluna-retro-mini-pikap-6.png`, `ayluna-retro-mini-pikap-7.png`, `ayluna-retro-mini-pikap-8.png`, `ayluna-retro-mini-pikap-9.png`, `ayluna-retro-mini-pikap-10.png`, `ayluna-retro-mini-pikap-11.png`, `ayluna-retro-mini-pikap-12.png`
- En uzun ve en "özel" sayfalardan biri: iki büyük özel Liquid bölümü (özellik hikâyesi + "Gerçek Müşteriler" kartları).
- SSS iki kez var (ana bölüm içinde + ayrı bölüm, aynı 10 soru).

### Görseller (9)

1. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260618_172659_f644ec15-4ec2-41c0-b509-e40bc3e08b81.png?v=1781804314
   Yaşam + afiş (masa, klavye, kahve): "MÜZİĞİN TASARIMLA BULUŞTUĞU AN." Yüksek Ses Kalitesi · Bluetooth 5.3 Bağlantı · Uzun Pil Ömrü.
2. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260618_172649_96e434ab-f9d9-41d5-a36f-1883fe94f8e4.png?v=1781804314
   Yaşam + afiş (havuz kenarı): "BEYAZ GÜRÜLTÜ HOPARLÖRÜ · NET SES. ODAKLI ZİHİN." Beyaz Gürültü Teknolojisi · Ayarlanabilir Ses · Zamanlayıcı · TF Kart.
3. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260618_172712_76f2d63c-dca1-4dfd-919f-25fdb0a7b4a3.png?v=1781804314
   Afiş (komodin, telefon): "MÜZİK HER YÖNDEN SİZİ SARMALASIN" 360° Çevresel Ses · Bluetooth 5.3 · Uzun Pil Ömrü · Premium Tasarım.
4. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260618_204930_ecc6b038-9dba-4aa9-a49b-781f9455ba50.png?v=1781815901
   4'lü panel, yatak odası RGB ışık: "HER ANINA BİR RENK · Odanın ruh halini sen seç · Hemen Sahip Ol".
5. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260618_172719_c35c92d3-5990-4906-8657-6a08fda1a8e0.png?v=1781804314
   Yaşam + afiş (gece, mum): "MÜZİĞİN RİTMİNDE HUZURLU ANLAR" 4 Doğal Ses Modu · Bluetooth 5.3 · Uzun Pil Ömrü · Premium Tasarım.
6. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260618_172727_04476fee-f1c1-4e1a-bcf6-304316c52092.png?v=1781804314
   Afiş + uyuyan kadın: "DOĞANIN BÜTÜNLEŞTİREN SESİ, HER AN YANINIZDA" Dalga · Kuş · Ateş · Akarsu sesi.
7. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260618_172738_a4917cba-8b9b-48e9-9d4c-81884094541d.png?v=1781804314
   Afiş (su, çiçek): "TEKNOLOJİ DUYGULARA EŞLİK EDER · mühendislik harikası" Üstün Ses Kalitesi · Gelişmiş Bağlantı · Uzun Pil Ömrü · Dayanıklı Tasarım.
8. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260618_172748_1079cab0-4849-4d29-9068-c773392e1f2e.png?v=1781804314
   Afiş (ahşap masa): "SESİNİZ. TARZINIZ. Zamanın Ötesinde Bir Deneyim." Bluetooth 5.3 · Yüksek Çözünürlüklü Ses · Uzun Pil Ömrü · Dokunmatik Kontrol.
9. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260618_172638_1bbbdd9f-9b15-4958-ade4-74567adf79cf.png?v=1781804314
   Beyaz zemin ölçü görseli: "Kompakt Tasarım · 14 x 14 x 18 cm".

### Bölüm sırası

Tam id biçimi: şablon bölümleri `shopify-section-template--28025597329636__<anahtar>`, global bölümler `shopify-section-sections--28025597690084__<anahtar>` (altbilgi `…28025597657316__footer`).

1. `custom_liquid_XWzNR9` — Üst geri sayım şeridi (global): "Bugüne Özel %20 İndirim" + sayaç
2. `header` — Başlık (global): menü, logo, arama, sepet
3. `announcement_bar_m7VX6j` — Duyuru şeridi: 🚚 Stoklarla Sınırlı · Müziğin Tasarımla Buluştuğu An ✨
4. `main` — **Ana ürün bölümü** (galeri 9 görsel), blok sırası:
   - Başlık: Ayluna Retro Mini Pikap
   - Puan satırı: 4.7 ( 2467 Onaylı Kullanıcı Yorumu)
   - Kargo sayacı: 🚚 · 19:34:08 içerisinde sipariş verirsen bugün kargoda.
   - Özellik başlığı: ✨ Öne Çıkan Özellikler ✨ · Nostaljik tasarım, modern teknolojiyle buluşuyor
   - Özellik kartları: Bluetooth 5.3 Kablosuz Bağlantı · 4 Doğal Ses & Beyaz Gürültü Modu · Çalar Saat ve Zamanlayıcı · TF Kart Desteği · Şarjlı & Uzun Pil Ömrü · 3D Su Dalgası Işık Efektli Disk · Dokunmatik Kontrol
   - Canlı izleyici sayacı: 48 kişi şu anda bu ürünü inceliyor.
   - Kargo notu: KREDİ KARTI İLE VERİLEN ŞİPARİŞLER HIZLI KARGO İLE ÇIKARTILMAKTADIR
   - Paket teklifi (Kaching) + satın al butonları: BUNDLE & SAVE · 1 Adet · %20 İndirim · 1,499.00TL · 1,999.99TL · 2 Adet · %20 İndirim · 2,499.99TL · 3,999.98TL · GÜVENLİ ÖDEME İLE AL · Kapıda Ödeme ile Sipariş Ver
   - Ödeme logoları: Amex, Diners, Discover, JCB, Mastercard, Visa
   - Teslimat zaman çizelgesi: 18 Ekm · Siparişiniz Oluşturuldu · 19 Ekm - 20 Ekm · Kargonuz Hazırlandı · 21 Ekm - 23 Ekm · Evinize Teslim Edildi
   - Güven şeridi: 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi
   - Yapışkan sepet çubuğu: Ayluna Retro Mini Pikap · 1,499.00TL · 1,999.99TL · Sepete Ekle
   - Kısa yorum kaydırıcısı (3 yorum): Eşim bayıldı 💙 Her gece müzik dinlemeyi çok seviyor Işık yumuşacık, ses kalitesi çok güzel · Elif K. · En büyük artısı ortamı bir anda sakinleştirmesi. Sakinleştirici dalga sesini tavsiye ederim · Gülsüm S. · Hediye aldım, alan kişi aşık oldu 🎁 Temalar çok güzel, odanın havasını değiştiriyor. Işık göz yormuyor; gece boyunca açık kalsa bile rahatsız etmiyor. · Zeynep R.
   - SSS (ana bölüm içinde): sorular aşağıdaki SSS listesinde
5. `horizontal_ticker_rbYQET` — Kayan şerit: 🚚 Hızlı Kargo & Güvenli Ödeme · ⭐ 2467+ Mutlu Müşteri · 4.7 Puan · 🛡️ 1 Yıl Garanti · Stoklarla Sınırlı
6. `eba88da5-80ac-47fc-aa75-997cfe7b2e59` — Yorum ekran görüntüsü kaydırıcısı: +2000 Mutlu Müşterinin Hakkımızda söylediklerini okuyun [16 görsel: imgi_22_saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa…, imgi_15_saaaaaaaaaaaa_6.png, imgi_16_Adsiz_tasarim_36.png …]
7. `custom_liquid_TL6T4w` — Özel Liquid: EN ÇOK TERCİH EDİLEN NOSTALJİK HEDİYE · Müziği, Huzuru ve Tasarımı Tek Cihazda Yaşa · Aşağıda bu küçük dev cihazın neden binlerce kişinin masasında ve komodininde yer aldığını keşfedeceksin. Birkaç saniyeni ayır, gerisini kendisi anlatıyor 👇 · 4 Doğal Ses ve Beyaz Gürültü Modu · Dalga, kuş, ateş ve akarsu seslerinden ilham alan modlarla dikkat dağıtan gürültüleri bastırır; daha derin odaklanma, rahatlama ve kaliteli … [1 görsel: hf_20260618_172712_76f2d63c-dca1-4dfd-919f-2…]
8. `custom_liquid_Gr6hAz` — Özel Liquid: GERÇEK MÜŞTERİLER, GERÇEK ANLAR · Binlerce Kişi Şimdiden Aramıza Katıldı · Onlar da senin gibi tereddüt etti, sonra denedi ve vazgeçemedi. İşte Ayluna Retro Mini Pikap'ı evine alanların gerçek anları 👇 · ★★★★★ · 4.7 / 5 · · 2.467 onaylı kullanıcı yorumu · Doğrulanmış Alıcı · "Kutudan çıkar çıkmaz bağlandım! Hem sesi hem ışığı beklediğimden çok daha iyi." · — Emre T. · "Mutfakta kahve yaparken müzik açıyorum, bütün ev … [4 görsel: hf_20260618_182602_48622084-0358-4a84-8c0a-4…, hf_20260618_182239_0934c592-2d19-4807-901f-4…, hf_20260618_182554_d30a1592-c37d-4d08-87cb-7… …]
9. `image_banner_Ae7wdz` — GIF afiş + başlık: Müzik Ruhun Gıdasıdır. · MÜZİK DİNLEMEYE BAYILDIĞINI BİLİYORUZ BİZDE TAMAMEN SENİN İÇİN BUNU BİR IŞIK ŞOVUNA ÇEVİRDİK. [1 görsel: ssstik.io_roseandrosestr_1781804932655-ezgif…]
10. `section_divider_ARXJ86` — Ayraç
11. `section_divider_qmrTwn` — Ayraç
12. `image_with_text_8UNBF8` — Görsel + metin + buton: Masanı ve uykunu değiştirecek o küçük dokunuş. · Müzik, huzur ve tasarım artık tek bir cihazda. Bluetooth bağlantısıyla sevdiğin parçaları dinle, doğadan ilham alan ses modlarıyla rahatla, yumuşak ışığıyla odana sıcak bir atmosfer kat. · Ayluna Retro Mini Pikapı Keşfet [1 görsel: hf_20260618_172738_a4917cba-8b9b-48e9-9d4c-8…]
13. `insta_stories_xe3xA6` — Instagram hikâyeleri: İnstagram'da Ayluna · Bizleri tercih eden mutlu müşterilerin hikayeleri sizlerle BİZİ TAKİP ET ❤️ [3 görsel: IMG_4145.jpg, IMG_4146.jpg, IMG_4147.jpg]
14. `custom_liquid_H9Gw8b` — Özel Liquid: SSS, 10 soru (aşağıda)
15. `b321ab88-2b59-4dba-bade-54885c874ca5` — Ayraç
16. `17694466126b1e0319` — Loox yorum uygulaması (iframe; ayrıntı aşağıda)
17. `footer` — Altbilgi (global): %5 indirim için e-posta aboneliği, ödeme logoları, politikalar

### Paket teklifi, geri sayım, kargo

- **Paket (Kaching):** BUNDLE & SAVE · 1 Adet · %20 İndirim · 1,499.00TL · 1,999.99TL · 2 Adet · %20 İndirim · 2,499.99TL · 3,999.98TL
- **Geri sayım:** üst şerit "Bugüne Özel %20 İndirim 01 SAAT : 01 DK : 33 SAN" (her yüklemede yeniden başlar); kargo sayacı "… içerisinde sipariş verirsen bugün kargoda" (15:00'e sayar)
- **Duyuru şeridi:** 🚚 Stoklarla Sınırlı · Müziğin Tasarımla Buluştuğu An ✨
- **Güven şeridi:** 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi

### SSS

**Kaynak: `main`**

- **Bu ürün ne işe yarıyor?** Nostaljik plak çalar görünümlü, çok fonksiyonlu bir Bluetooth hoparlördür. Hem müzik dinleyebilir, hem beyaz gürültü ve doğa sesleriyle rahatlayabilir, hem de çalar saat ve dekoratif gece lambası olarak kullanabilirsin. Çalışma masası, komodin ve yatak odası i …
- **Bluetooth var mı, nasıl bağlanıyor?** Evet, Bluetooth 5.3 ile gelir. Cihazı açıp telefonunun Bluetooth menüsünden eşleştirmen yeterli; saniyeler içinde bağlanır ve kesintisiz, kararlı bir ses akışı sunar. Telefon, tablet ve bilgisayarla uyumludur.
- **Beyaz gürültü ve doğa sesleri nasıl çalışıyor?** Cihazda yerleşik olarak 4 doğal ses modu bulunur: dalga sesi, kuş sesleri, ateş sesi ve akarsu sesi. Sağ düğmeyi kullanarak ses modları arasında geçiş yapabilirsin. Bu sesler dikkat dağıtan gürültüleri bastırarak daha rahat odaklanmanı ve daha kaliteli uyumanı …
- **Çalar saat ve zamanlayıcı özelliği var mı?** Evet. Ön yüzdeki dijital LED ekranda saat görünür; alarm kurabilir ve zamanlayıcı (uyku modu) ayarlayabilirsin. Böylece uykuya dalarken çalan ses belirlediğin süre sonunda otomatik kapanır.
- **3D ışık efekti çalışırken rahatsız eder mi?** Hayır. Diskteki 3D su dalgası ışık efekti yumuşak ve göz yormayan bir aydınlatma sunar; gözü rahatsız etmez. Gece lambası gibi loş, huzurlu bir atmosfer oluşturur ve istersen ışığı kapatıp sadece ses olarak da kullanabilirsin.
- **Şarjlı mı, pil ömrü nasıl?** Cihaz dahili şarj edilebilir bataryaya sahiptir. USB ile şarj edilir ve tek şarjla uzun süre kablosuz kullanım sunar. İstersen kabloya takılı halde de kullanmaya devam edebilirsin.
- **TF (hafıza) kart desteği var mı?** Evet, TF (microSD) kart desteği vardır. Sevdiğin şarkıları karta yükleyip telefona ihtiyaç duymadan, doğrudan cihazdan dinleyebilirsin.
- **Düğmeler ne işe yarıyor, nasıl kontrol ediyorum?** Sağ düğmeyi çevirerek sesi ayarlar, çift tıklayarak önceki, tek tıklayarak sonraki ses moduna/parçaya geçersin. Diskin ortasındaki dokunmatik düğmeyle de oynat/duraklat yapabilirsin. Kullanımı son derece basittir.
- **Kutu içeriğinde neler var?** Kutudan 1 adet nostalji plak çalar Bluetooth hoparlör, 1 adet USB şarj kablosu ve kullanım kılavuzu çıkar. Ürün özel ambalajıyla güvenli şekilde gönderilir.
- **Bluetooth bağlanmıyor, ne yapmalıyım?** Önce cihazın açık ve şarjlı olduğundan emin ol. Telefonunda daha önce eşleştirilmiş eski bağlantı varsa onu "unut" yapıp tekrar eşleştir. Cihazı kapatıp açman da çoğu sorunu çözer. Sorun devam ederse mağazamızdan bizimle iletişime geçebilirsin, yardımcı oluruz …

- *`custom_liquid_H9Gw8b` bölümü yukarıdaki soruların aynısı (tekrar).*

### Yorumlar

- **Sayfada yazan:** "4.7 (2467 Onaylı Kullanıcı Yorumu)" (sabit metin)
- **Loox gerçek:** 10 yorum, ortalama 5.0 (dağılım: 5★×10); ilk 20 yorumun tarihleri: 18.06.2026 ×10; "Doğrulanmış" etiketi: 0
- **Loox örnek:** "Çalışırken beyaz gürültü açıyorum, odaklanmama gerçekten yardımcı oluyor. Memnun kaldım." / "Tasarımı bayıldım, retro görünümü çok tatlı. Odamın havasını değiştirdi diyebilirim." / "Şarjı uzun gidiyor, sürekli prize takmaya gerek yok. Bu yönüyle çok rahat." / "Saat özelliği çok pratik, alarmı da kuruyorum. Tek üründe her şey var resmen."

### Açıklama (body_html)

- Boş. Ürün metni yalnız tema bölümlerinde.

### Sorunlu iddialar

- **Uydurma puan:** Sayfada 3 yerde "4.7 / 2.467 onaylı yorum", şeritte "2467+ Mutlu Müşteri". Loox: 10 yorum, 5.0, hepsi 18.06.2026 (ürünün eklendiği gün), hiçbirinde "Doğrulanmış" yok.
- **Uydurma yorum:** "GERÇEK MÜŞTERİLER, GERÇEK ANLAR" kartları yapay zekâ ile üretilmiş kadın fotoğrafları (`hf_20260618_…`) + "Doğrulanmış Alıcı" etiketi. "+2000 Mutlu Müşterinin" kaydırıcısı başka ürünlerin (yıldız projektörü) WhatsApp sohbetleri.
- **Sağlık:** "daha derin odaklanma, rahatlama ve kaliteli bir uyku sunar", SSS "daha kaliteli uyumanı destekler", görsel "ODAKLI ZİHİN", "Masanı ve uykunu değiştirecek".
- **Garanti çelişkisi:** Özel bölümlerde "✓ 2 yıl garanti", güven şeridi ve kayan şeritte "1 Yıl Garanti".
- **İade:** "90 Gün Para İade Garantisi".
- **Teyitsiz teknik:** Bluetooth 5.3, "360° Çevresel Ses", "Yüksek Çözünürlüklü Ses", 14×14×18 cm, "Uzun pil ömrü".
- **Ürün adı:** "Pikap" plak çalmıyor; plak görünümlü Bluetooth/beyaz gürültü hoparlörü (SSS bunu söylüyor, başlık söylemiyor).
- **Fiyat etiketi:** Paket: "1 Adet %20 İndirim" (gerçek %25), "2 Adet %20 İndirim" (gerçek %37,5).
- **Aciliyet:** "Stoklar hızla tükeniyor", "Stoklarla Sınırlı"; stok politikası "continue" (stok sıfırken satış açık).
- **Görsel:** Afiş GIF'i TikTok'tan indirilmiş (`ssstik.io_roseandrosestr…`), satılmayan pembe renk.

---

## 3. Eğitici Akıllı Çizim Tahtası — `egitici-akilli-cizim-tahtasi`

- **Adres:** https://ayluna.shop/products/egitici-akilli-cizim-tahtasi
- **Fiyat:** 1.199,00 TL · karşılaştırma: 1.999,00 TL → gerçek indirim %40.0
- **Varyantlar** (Renk Seçenekleri): Sarı — 1.199,00 TL — satışta; Pembe — 1.199,00 TL — satışta
- **Şablon:** `template--28025597100260` · sayfa yüksekliği 10377 px · vendor: Ayluna
- **Ekran görüntüleri** (11 parça, klasör `…/scratchpad/site/urun/`): `egitici-akilli-cizim-tahtasi-1.png`, `egitici-akilli-cizim-tahtasi-2.png`, `egitici-akilli-cizim-tahtasi-3.png`, `egitici-akilli-cizim-tahtasi-4.png`, `egitici-akilli-cizim-tahtasi-5.png`, `egitici-akilli-cizim-tahtasi-6.png`, `egitici-akilli-cizim-tahtasi-7.png`, `egitici-akilli-cizim-tahtasi-8.png`, `egitici-akilli-cizim-tahtasi-9.png`, `egitici-akilli-cizim-tahtasi-10.png`, `egitici-akilli-cizim-tahtasi-11.png`
- Tek varyantlı ürün değil: "Renk Seçenekleri" Sarı / Pembe (ikisi de satışta). 2'li pakette iki ayrı renk seçimi var.
- Şablon Dokunmatik Ambiyans Lamba ile ortak (`template--28025597100260`).

### Görseller (8)

1. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260519_171823_d1aaef3b-e1b8-422e-b42c-5e1bffc79866.png?v=1779211765
   Afiş (krem zemin, ürün + kutu): "ZÜRAFALI ÇİZİM MASASI · HEDİYE KALEMLER DAHİL! · 12 RENKLİ KALEM — ÜCRETSİZ HEDİYE · SEPETE EKLE". 3 disk, 12 kalem, silgi, bez görünüyor.
2. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260519_172311_224fef6a-b2d0-43f9-bd98-1c65b06e7afd.png?v=1779211764
   Afiş yakın çekim: "NASIL ÇALIŞIR? Diski tak, ışık yansısın, çiz!" Projeksiyon diski · 24 FARKLI KONU · 3 DİSK PAKETTE · ANINDA DEĞİŞTİR · SATIN AL.
3. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260519_172028_87ee3676-b676-45eb-a290-ed2211cddf9d.png?v=1779211765
   9'lu kolaj (yapay zekâ çocuk): "NASIL KULLANILIR? Tak — Yansıt — Çiz — Eğlen" · HEMEN AL.
4. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260519_172256_24378384-58cf-4ceb-8922-86787a1ffaa8.png?v=1779211764
   Yaşam (yapay zekâ kız çocuk) + fayda listesi: YARATICILIK GELİŞTİRİR · EL-GÖZ KOORDİNASYONU (ince motor becerilerini güçlendirir) · RESİM ÖĞRETİR · EĞLENEREK ÖĞRENİR.
5. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260519_174239_98408413-a9e8-4a8e-8381-863a84274aaa.png?v=1779212751
   Yorum afişi "ANNELER NE DİYOR?": 6 kart (Selin A., Fatma K., Merve T., Ayşe D., Zeynep Y., Büşra M.), hepsi 5 yıldız ve "Doğrulanmış Alıcı".
6. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260519_172330_8d770091-f169-449d-9367-877661d7b64c.png?v=1779211761
   Afiş: "ÇİZMEYİ SEVDİRİYOR · Proyeksiyonlu zürafayla çocuğunuz ilk resmini çizer" · 3-8 YAŞ · 12 RENKLİ KALEM HEDİYE · HEMEN TESLİMAT ("Proyeksiyonlu" yazım hatası).
7. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260519_172321_b3b22f89-89de-4e36-b529-38770fe2133d.png?v=1779211763
   Yorum kartı: Selin A. "Doğrulanmış Alıcı 5/5", yapay zekâ portre, "Tavsiye ediyorum" mührü; Güvenli Alışveriş · Hızlı Kargo · Kolay İade.
8. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260520_201934_002e4fc8-e114-4b73-9748-f52c01197f88.png?v=1779308469
   Ürün fotoğrafı, pembe varyant, krem zemin: kutu, 3 disk, kalemler, silgi, bez.

### Bölüm sırası

Tam id biçimi: şablon bölümleri `shopify-section-template--28025597100260__<anahtar>`, global bölümler `shopify-section-sections--28025597690084__<anahtar>` (altbilgi `…28025597657316__footer`).

1. `custom_liquid_XWzNR9` — Üst geri sayım şeridi (global): "Bugüne Özel %20 İndirim" + sayaç
2. `header` — Başlık (global): menü, logo, arama, sepet
3. `announcement_bar_m7VX6j` — Duyuru şeridi: YAZ-ÇİZ-ÖĞRET HEPSİ BİR ARADA
4. `main` — **Ana ürün bölümü** (galeri 8 görsel), blok sırası:
   - Başlık: Eğitici Akıllı Çizim Tahtası
   - Puan satırı: 4.7 ( 2467 Onaylı Kullanıcı Yorumu)
   - Kargo sayacı: 🚚 · 19:33:42 içerisinde sipariş verirsen bugün kargoda.
   - Özellik başlığı: 🎨 Neden Bu Çizim Tahtası? 🎨 · Eğlenerek öğrenmenin en renkli yolu
   - Özellik kartları: Projeksiyon ile Çizim Rehberliği · Dahili Müzik Sistemi · Silinebilir Çizim Yüzeyi · El-Göz Koordinasyonu Geliştirir · 37 cm Geniş Çizim Alanı · 3 Yaş ve Üzeri İçin Uygun
   - Canlı izleyici sayacı: 50 kişi şu anda bu ürünü inceliyor.
   - Kargo notu: KREDİ KARTI İLE VERİLEN ŞİPARİŞLER HIZLI KARGO İLE ÇIKARTILMAKTADIR
   - Paket teklifi (Kaching) + satın al butonları: ÇOK AL & TASARRUF ET · 1 Adet · Yaz'a Özel Fiyat · 1,199.00TL · 1,999.00TL · 12 ADET BOYA KALEMİ HEDİYE 🎁 · 1 ADET ÖZEL SİLGİ HEDİYE 🎁 · İKİNCİ ÜRÜNDE DEV İNDİRİM · 2 ADET · ÇOK AL AZ ÖDE · 1,999.00TL · 3,998.00TL · Renk Seçenekleri · Sarı · Pembe · Sarı · Pembe · 24 ADET BOYA KALEMİ HEDİYE 🎁 · 2 ADET ÖZEL SİLGİ HEDİYE · GÜVENLİ ÖDEME İLE AL · Kapıda Ödeme ile Sipariş Ver
   - Ödeme logoları: Amex, Diners, Discover, JCB, Mastercard, Visa
   - Teslimat zaman çizelgesi: 18 Ekm · Siparişiniz Oluşturuldu · 19 Ekm - 20 Ekm · Kargonuz Hazırlandı · 21 Ekm - 23 Ekm · Evinize Teslim Edildi
   - Güven şeridi: 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi
   - Yapışkan sepet çubuğu: Eğitici Akıllı Çizim Tahtası · 1,199.00TL · 1,999.00TL · Sepete Ekle
5. `custom_liquid_B6DtbY` — Özel Liquid: ANNELERDEN GELENLER · Binlerce mutlu çocuktan sadece 4 tanesini paylaştık, Onlar eğlenerek öğrenmeyi seçti. Sen neyi bekliyorsun ? 🎨 · Çocuğum çok sevdi 🎨 · Saatler geçiyor farkında bile olmuyor · Projeksiyon harika 💡 · Çizim yapmayı hızlı öğrendi · Müzikle birlikte oynuyor 🎵 · Hem eğleniyor hem öğreniyor · Kesinlikle tavsiye ederim ⭐ · Silinebilir yüzey süper pratik [4 görsel: hf_20260519_174948_b945b1f2-ab82-4c03-9381-8…, hf_20260519_174941_250a0267-b733-42aa-ad12-f…, hf_20260519_174934_39dcdee4-061c-4ea7-8315-a… …]
6. `horizontal_ticker_LaJrRW` — Kayan şerit: GÜVENLİ KARGO 📦 · EĞLENCE KAYNAĞI ✨ · ÇOCUKLARA ÖZEL
7. `custom_liquid_w4Hmnf` — Özel Liquid: ✦ ANNELERİN FAVORİSİ · Sadece Bir Oyuncak Değil, · Sanat Dolu Bir Deneyim · Kaydırarak detayları keşfedin · 👉 · ✦ Çocuğunuz İçin Özel · Hayal Gücünü · Işıkla Yakala · Zürafanın sihirli ışığı masaya yansıyor — çocuğunuz sadece takip ediyor ve saniyeler içinde kendi şaheserini yaratıyor. · ✨ 24 Farklı Projeksiyon Konusu · 🎁 12 Renkli Kalem Hediye · 👶 3-8 Yaş Arası İçin İdeal · Hemen Satın Al · → · ★★★★★ · Binlerce Mutl … [3 görsel: hf_20260519_174524_7949dc41-3e98-4a51-a467-4…, hf_20260519_174529_33767cc6-a934-47a9-9958-e…, hf_20260519_174534_c11fe737-8bcb-4b16-9a81-9…]
8. `horizontal_ticker_rbYQET` — Kayan şerit: Ücretsiz Kargo 📦 · 3 Farklı Mod ✨ · Hızlı Kargo
9. `8beb6911-28c6-482c-976a-e5421ad3e8df` — Özellik satırları (4 başlık + görsel): 24 Farklı Sihirli Şablon · Kutu içerisinden çıkan 3 farklı projeksiyon diski ile tam 24 farklı hayvan, taşıt ve nesne figürünü masaya yansıtır. Çocuğunuzun çizime başlarken ihtiyaç duyduğu o sihirli rehberlik tam da burada. · Silin ve Tekrar Başlayın · Yanlış çizmek dert değil! Kutuya dahil olan özel silgi ve temizleme bezi sayesinde tahta saniyeler içinde tertemiz olur. Hem kağıt israfını önler hem de çocuğunuza sın … [5 görsel: stars_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg, ink_highlighter_move_24dp_000000_FILL0_wght4…, hf_20260519_174534_c11fe737-8bcb-4b16-9a81-9… …]
10. `image_with_text_8UNBF8` — Görsel + metin + buton: Ekranlara Veda, Renklere Merhaba · Ayluna ailesi olarak her ürünü titizlikle seçiyoruz. Dijital ekranların yerini alacak; hem eğlendiren hem de el-göz koordinasyonunu geliştiren sihirli bir alternatif. Yansıyan figürleri takip etmek, çocuğunuzun odaklanma süresini uzatır ve ince motor becerilerini hızla güçlendirir. · Eğitici Akıllı Çizim Tahtası [1 görsel: hf_20260519_174529_33767cc6-a934-47a9-9958-e…]
11. `horizontal_ticker_edVL3c` — Kayan şerit: Ücretsiz Kargo 📦 · 3 Farklı Mod ✨ · Hızlı Kargo
12. `insta_stories_xe3xA6` — Instagram hikâyeleri: İnstagram'da Ayluna · Bizleri tercih eden mutlu anne ve çocuklarımızın hikayeleri sizlerle ❤️ [3 görsel: IMG_4145.jpg, IMG_4146.jpg, IMG_4147.jpg]
13. `eba88da5-80ac-47fc-aa75-997cfe7b2e59` — Yorum ekran görüntüsü kaydırıcısı: +2000 Mutlu Annenin söylediklerini okuyun [16 görsel: imgi_22_saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa…, imgi_15_saaaaaaaaaaaa_6.png, imgi_16_Adsiz_tasarim_36.png …]
14. `custom_liquid_bGxbxk` — Özel Liquid: SSS, 9 soru (aşağıda)
15. `b321ab88-2b59-4dba-bade-54885c874ca5` — Ayraç
16. `17694466126b1e0319` — Loox yorum uygulaması (iframe; ayrıntı aşağıda)
17. `footer` — Altbilgi (global): %5 indirim için e-posta aboneliği, ödeme logoları, politikalar

### Paket teklifi, geri sayım, kargo

- **Paket (Kaching):** ÇOK AL & TASARRUF ET · 1 Adet · Yaz'a Özel Fiyat · 1,199.00TL · 1,999.00TL · 12 ADET BOYA KALEMİ HEDİYE 🎁 · 1 ADET ÖZEL SİLGİ HEDİYE 🎁 · İKİNCİ ÜRÜNDE DEV İNDİRİM · 2 ADET · ÇOK AL AZ ÖDE · 1,999.00TL · 3,998.00TL · Renk Seçenekleri · Sarı · Pembe · Sarı · Pembe · 24 ADET BOYA KALEMİ HEDİYE 🎁 · 2 ADET ÖZEL SİLGİ HEDİYE
- **Geri sayım:** üst şerit "Bugüne Özel %20 İndirim 01 SAAT : 01 DK : 34 SAN" (her yüklemede yeniden başlar); kargo sayacı "… içerisinde sipariş verirsen bugün kargoda" (15:00'e sayar)
- **Duyuru şeridi:** YAZ-ÇİZ-ÖĞRET HEPSİ BİR ARADA
- **Güven şeridi:** 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi

### SSS

**Kaynak: `custom_liquid_bGxbxk`**

- **Çocuğumun gelişimine gerçekten katkısı var mı?** Evet, birden fazla alanda somut katkı sağlar: projeksiyon takibi ile el-göz koordinasyonu, serbest çizimle ince motor becerileri ve yaratıcılık, müzik eşliğiyle işitsel gelişim ve konsantrasyon. Öğrenmeyi oyuna dönüştürdüğü için çocuklar farkında olmadan geliş …
- **Projeksiyon özelliği nasıl çalışıyor?** Zürafa figürünün başındaki projektör, farklı şekil ve görselleri çizim tahtasına yansıtır. Çocuklar yansıyan şeklin üzerinden kalemi geçirerek çizim yapmayı öğrenir. Bu yöntem el-göz koordinasyonunu çok etkili biçimde geliştirir ve birden fazla şablon seçeneği …
- **Müzik özelliği var mı, nasıl kullanılıyor?** Evet, dahili müzik sistemi mevcuttur. Farklı melodiler ve sesler içeren bu özellik çizim sırasında çocuğun dikkatini canlı tutar ve öğrenmeyi eğlenceli hale getirir. Müzik tuşlarına basarak açılır, ses seviyesi ayarlanabilir.
- **Çizim yüzeyi silinebilir mi, kalıcı mı?** Çizim yüzeyi tamamen silinebilir. Kuru veya hafif nemli bir bezle kolayca temizlenir. Çocuğunuz istediği kadar çizebilir, silip yeniden başlayabilir. Kağıt ve kalem tüketimi olmadığı için hem ekonomik hem de çevre dostudur.
- **Bu ürün kaç yaş için uygun?** 3 yaş ve üzeri çocuklar için idealdir. Okul öncesi dönemdeki küçük çocukların motor becerilerini geliştirirken büyük çocukların da yaratıcılığını destekler. Projeksiyon ve müzik özellikleri sayesinde her yaştan çocuğun ilgisini çeker.
- **İade ve değişim koşulları nelerdir?** Teslim tarihinden itibaren 14 gün içinde iade veya değişim talebinde bulunabilirsiniz. Ürünün orijinal ambalajında, kullanılmamış ve eksiksiz olması gerekmektedir. Detay için müşteri hizmetlerimizle iletişime geçebilirsiniz.
- **Pille mi çalışıyor, piller kutuda mı geliyor?** Ürün pil ile çalışmaktadır. Piller ürünle birlikte gelmeyebilir; satın almadan önce kutu içeriğini kontrol etmenizi öneririz. Pil kapağı ebeveynler tarafından kolayca açılabilecek şekilde tasarlanmıştır.
- **Kaç günde teslim edilir?** Siparişler 1–3 iş günü içinde kargoya verilir, teslim süresi bölgeye göre 2–5 iş günüdür. Kargo takip bilgisi sipariş sonrası e-posta ile iletilir. Hafta içi verilen siparişler aynı gün kargoya teslim edilir.
- **Ürünün boyutları nedir, taşınabilir mi?** Çizim yüzeyi 37 cm genişliğinde olup kompakt ve hafif yapısıyla her yerde kullanılabilir. Masada, zeminde ve seyahatte rahatlıkla kullanım sunar. Çanta içine sığabilecek boyuttadır.


### Yorumlar

- **Sayfada yazan:** "4.7 (2467 Onaylı Kullanıcı Yorumu)" (sabit metin)
- **Loox gerçek:** 12 yorum, ortalama 5.0 (dağılım: 5★×12); ilk 20 yorumun tarihleri: 20.05.2026 ×12; "Doğrulanmış" etiketi: 0
- **Loox örnek:** "Çok beğendikkkk. yaz tatili için aldık herkes bunu almalı" / "Sitede söylendiği gibi hediyeleri ile birlikte geldi" / "Oğluma oyalansın diye aldım eskiden evde tabletle gezerdi 1 haftadır yüzüne bakmıyor" / "Biz pembe olanı aldık hızlı geldi teşekkürler ayluna"

### Açıklama (body_html)

- Boş. Ürün metni yalnız tema bölümlerinde.

### Sorunlu iddialar

- **Sağlık / gelişim:** "El-göz koordinasyonu geliştirir", "ince motor becerilerini hızla güçlendirir", "odaklanma süresini uzatır", "%100 Ekransız Gelişim", SSS "somut katkı sağlar… işitsel gelişim ve konsantrasyon", görsel 4 fayda listesi.
- **İade çelişkisi:** SSS "Teslimden itibaren 14 gün içinde iade"; güven şeridi "90 Gün"; gerçek 30 gün.
- **Uydurma yorum:** Görsel 5 (6 kart) ve 7 (Selin A.) "Doğrulanmış Alıcı"; "ANNELERDEN GELENLER" görselleri yapay zekâ (`hf_20260519_…`). Loox 12 yorum, 5.0, hepsi 20.05.2026, "Doğrulanmış" yok. Sayfa "4.7 (2467)", "Binlerce Mutlu Aile".
- **Teyitsiz teknik:** "Dahili Müzik Sistemi" (hiçbir görselde yok), "37 cm Geniş Çizim Alanı", "24 farklı konu".
- **Kutu çelişkisi:** Silgi + bez bir yerde "kutuya dahil", paket teklifinde "HEDİYE"; 12 kalem her yerde "hediye" ama hep dahil; SSS "Piller ürünle birlikte gelmeyebilir".
- **Yaş çelişkisi:** "3 Yaş ve Üzeri" ↔ "3-8 Yaş Arası".
- **Fiyat / güncellik:** Paket etiketi "Yaz'a Özel Fiyat" (Ekim); karşılaştırma 1.999 TL ile %40 indirim.
- **Kopya şerit:** "3 Farklı Mod ✨" (üründe mod yok).

---

## 4. Dokunmatik Ambiyans Lamba — `dokunmatik-ambiyans-lamba`

- **Adres:** https://ayluna.shop/products/dokunmatik-ambiyans-lamba
- **Fiyat:** 1.299,99 TL · karşılaştırma: 1.299,00 TL → karşılaştırma fiyatı satış fiyatından düşük
- **Varyantlar** (Title): Default Title — 1.299,99 TL — TÜKENDİ
- **Şablon:** `template--28025597100260` · sayfa yüksekliği 9844 px · vendor: Ayluna
- **Ekran görüntüleri** (10 parça, klasör `…/scratchpad/site/urun/`): `dokunmatik-ambiyans-lamba-1.png`, `dokunmatik-ambiyans-lamba-2.png`, `dokunmatik-ambiyans-lamba-3.png`, `dokunmatik-ambiyans-lamba-4.png`, `dokunmatik-ambiyans-lamba-5.png`, `dokunmatik-ambiyans-lamba-6.png`, `dokunmatik-ambiyans-lamba-7.png`, `dokunmatik-ambiyans-lamba-8.png`, `dokunmatik-ambiyans-lamba-9.png`, `dokunmatik-ambiyans-lamba-10.png`
- Şablon Eğitici Çizim Tahtası ile ortak (`template--28025597100260`): galeri dışındaki bütün bölümler çizim tahtasını anlatıyor.
- Ürün tükendi; satın al butonları "TÜKENDİ".

### Görseller (7)

1. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260515_190625_aaa51f3c-2643-46eb-8ad0-ff33f7f5b2ba.png?v=1778946575
   Afiş (koyu, mumlar): "Geceyi Senin İçin Tasarladık. Dokunmatik • Kumandalı • Dijital Saatli" Şarjlı · 3 Işık Modu · Otomatik Kapanma · Dijital Saat.
2. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260515_190619_13482025-6379-4e68-b15e-d2a678bcc120.png?v=1778946575
   Afiş + CE işareti: Dokunmatik Aç-Kapa · Parlaklık Ayarı · Dijital Saat + Şarj Göstergesi · 3 Renk Modu — Uzaktan Kumanda; WARM / WHITE / COOL.
3. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260515_190601_f6883ea4-8502-4281-8ce8-195db9441bf5.png?v=1778946575
   Bilgi afişi: "3 Renk Modu" (Gün Batımı, Doğal Beyaz, Gün Işığı) · "Parlaklık Kontrolü" %10–%100.
4. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260515_190610_56c8587c-9cbf-40be-b822-5a315932b917.png?v=1778946575
   Yaşam fotoğrafı: uyuyan kadın, komodinde lamba ve kumanda (yazısız).
5. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260515_190407_56fa9800-6abf-4e9d-8b51-4e9362afb071.png?v=1778946576
   Beyaz zemin ölçü: 11 cm × 8 cm; Dokunmatik Kontrol, Dijital Saat, Type-C USB Şarj, ON/OFF, Parlaklık Butonu; kumanda ve kablo görünüyor; "Hafif. Akıllı. Şarjlı."
6. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260515_190504_bb70c884-a860-4c3a-8d62-41af66a9caaa.png?v=1778946575
   Afiş (koyu): Göz Koruyucu Filtre · Dokunmatik Renk Değiştirme · Anlık Şarj Seviyesi Ekranı · 12 LED Göz Dostu Teknoloji · Her Zaman Çalışan Dijital Saat · Darbeye & Suya Dayanıklı Gövde.
7. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260515_190310_0784da48-2352-4167-9d96-cd7e809a0416.png?v=1778946577
   6'lı kullanım kolajı: yatak odası, bebek odası (biberon), kitaplık, çalışma masası, kamp çadırı, köpüklü küvet kenarı.

### Bölüm sırası

Tam id biçimi: şablon bölümleri `shopify-section-template--28025597100260__<anahtar>`, global bölümler `shopify-section-sections--28025597690084__<anahtar>` (altbilgi `…28025597657316__footer`).

1. `custom_liquid_XWzNR9` — Üst geri sayım şeridi (global): "Bugüne Özel %20 İndirim" + sayaç
2. `header` — Başlık (global): menü, logo, arama, sepet
3. `announcement_bar_m7VX6j` — Duyuru şeridi: YAZ-ÇİZ-ÖĞRET HEPSİ BİR ARADA
4. `main` — **Ana ürün bölümü** (galeri 7 görsel), blok sırası:
   - Başlık: Dokunmatik Ambiyans Lamba
   - Puan satırı: 4.7 ( 2467 Onaylı Kullanıcı Yorumu)
   - Kargo sayacı: 🚚 · 19:33:18 içerisinde sipariş verirsen bugün kargoda.
   - Özellik başlığı: 🎨 Neden Bu Çizim Tahtası? 🎨 · Eğlenerek öğrenmenin en renkli yolu
   - Özellik kartları: Projeksiyon ile Çizim Rehberliği · Dahili Müzik Sistemi · Silinebilir Çizim Yüzeyi · El-Göz Koordinasyonu Geliştirir · 37 cm Geniş Çizim Alanı · 3 Yaş ve Üzeri İçin Uygun
   - Canlı izleyici sayacı: 40 kişi şu anda bu ürünü inceliyor.
   - Kargo notu: KREDİ KARTI İLE VERİLEN ŞİPARİŞLER HIZLI KARGO İLE ÇIKARTILMAKTADIR
   - Paket teklifi (Kaching) + satın al butonları: ÇOK AL & TASARRUF ET · 1 Adet · Hızlı ve Ücretsiz Kargo · 1,299.99TL · Çocuklu Ailelerin Tercihi · 2 Adet · 600 ₺ İNDİRİM · 1,999.99TL · 2,599.98TL · TÜKENDİ · Tükendi
   - Ödeme logoları: Amex, Diners, Discover, JCB, Mastercard, Visa
   - Teslimat zaman çizelgesi: 18 Ekm · Siparişiniz Oluşturuldu · 19 Ekm - 20 Ekm · Kargonuz Hazırlandı · 21 Ekm - 23 Ekm · Evinize Teslim Edildi
   - Güven şeridi: 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi
   - Yapışkan sepet çubuğu: Dokunmatik Ambiyans Lamba · 1,299.99TL · Tükendi
5. `custom_liquid_B6DtbY` — Özel Liquid: ANNELERDEN GELENLER · Binlerce mutlu çocuktan sadece 4 tanesini paylaştık, Onlar eğlenerek öğrenmeyi seçti. Sen neyi bekliyorsun ? 🎨 · Çocuğum çok sevdi 🎨 · Saatler geçiyor farkında bile olmuyor · Projeksiyon harika 💡 · Çizim yapmayı hızlı öğrendi · Müzikle birlikte oynuyor 🎵 · Hem eğleniyor hem öğreniyor · Kesinlikle tavsiye ederim ⭐ · Silinebilir yüzey süper pratik [4 görsel: hf_20260519_174948_b945b1f2-ab82-4c03-9381-8…, hf_20260519_174941_250a0267-b733-42aa-ad12-f…, hf_20260519_174934_39dcdee4-061c-4ea7-8315-a… …]
6. `horizontal_ticker_LaJrRW` — Kayan şerit: GÜVENLİ KARGO 📦 · EĞLENCE KAYNAĞI ✨ · ÇOCUKLARA ÖZEL
7. `custom_liquid_w4Hmnf` — Özel Liquid: ✦ ANNELERİN FAVORİSİ · Sadece Bir Oyuncak Değil, · Sanat Dolu Bir Deneyim · Kaydırarak detayları keşfedin · 👉 · ✦ Çocuğunuz İçin Özel · Hayal Gücünü · Işıkla Yakala · Zürafanın sihirli ışığı masaya yansıyor — çocuğunuz sadece takip ediyor ve saniyeler içinde kendi şaheserini yaratıyor. · ✨ 24 Farklı Projeksiyon Konusu · 🎁 12 Renkli Kalem Hediye · 👶 3-8 Yaş Arası İçin İdeal · Hemen Satın Al · → · ★★★★★ · Binlerce Mutl … [3 görsel: hf_20260519_174524_7949dc41-3e98-4a51-a467-4…, hf_20260519_174529_33767cc6-a934-47a9-9958-e…, hf_20260519_174534_c11fe737-8bcb-4b16-9a81-9…]
8. `horizontal_ticker_rbYQET` — Kayan şerit: Ücretsiz Kargo 📦 · 3 Farklı Mod ✨ · Hızlı Kargo
9. `8beb6911-28c6-482c-976a-e5421ad3e8df` — Özellik satırları (4 başlık + görsel): 24 Farklı Sihirli Şablon · Kutu içerisinden çıkan 3 farklı projeksiyon diski ile tam 24 farklı hayvan, taşıt ve nesne figürünü masaya yansıtır. Çocuğunuzun çizime başlarken ihtiyaç duyduğu o sihirli rehberlik tam da burada. · Silin ve Tekrar Başlayın · Yanlış çizmek dert değil! Kutuya dahil olan özel silgi ve temizleme bezi sayesinde tahta saniyeler içinde tertemiz olur. Hem kağıt israfını önler hem de çocuğunuza sın … [5 görsel: stars_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg, ink_highlighter_move_24dp_000000_FILL0_wght4…, hf_20260519_174534_c11fe737-8bcb-4b16-9a81-9… …]
10. `image_with_text_8UNBF8` — Görsel + metin + buton: Ekranlara Veda, Renklere Merhaba · Ayluna ailesi olarak her ürünü titizlikle seçiyoruz. Dijital ekranların yerini alacak; hem eğlendiren hem de el-göz koordinasyonunu geliştiren sihirli bir alternatif. Yansıyan figürleri takip etmek, çocuğunuzun odaklanma süresini uzatır ve ince motor becerilerini hızla güçlendirir. · Eğitici Akıllı Çizim Tahtası [1 görsel: hf_20260519_174529_33767cc6-a934-47a9-9958-e…]
11. `horizontal_ticker_edVL3c` — Kayan şerit: Ücretsiz Kargo 📦 · 3 Farklı Mod ✨ · Hızlı Kargo
12. `insta_stories_xe3xA6` — Instagram hikâyeleri: İnstagram'da Ayluna · Bizleri tercih eden mutlu anne ve çocuklarımızın hikayeleri sizlerle ❤️ [3 görsel: IMG_4145.jpg, IMG_4146.jpg, IMG_4147.jpg]
13. `eba88da5-80ac-47fc-aa75-997cfe7b2e59` — Yorum ekran görüntüsü kaydırıcısı: +2000 Mutlu Annenin söylediklerini okuyun [16 görsel: imgi_22_saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa…, imgi_15_saaaaaaaaaaaa_6.png, imgi_16_Adsiz_tasarim_36.png …]
14. `custom_liquid_bGxbxk` — Özel Liquid: SSS, 9 soru (aşağıda)
15. `b321ab88-2b59-4dba-bade-54885c874ca5` — Ayraç
16. `17694466126b1e0319` — Loox yorum uygulaması (iframe; ayrıntı aşağıda)
17. `footer` — Altbilgi (global): %5 indirim için e-posta aboneliği, ödeme logoları, politikalar

### Paket teklifi, geri sayım, kargo

- **Paket (Kaching):** ÇOK AL & TASARRUF ET · 1 Adet · Hızlı ve Ücretsiz Kargo · 1,299.99TL · Çocuklu Ailelerin Tercihi · 2 Adet · 600 ₺ İNDİRİM · 1,999.99TL · 2,599.98TL
- **Geri sayım:** üst şerit "Bugüne Özel %20 İndirim 01 SAAT : 01 DK : 37 SAN" (her yüklemede yeniden başlar); kargo sayacı "… içerisinde sipariş verirsen bugün kargoda" (15:00'e sayar)
- **Duyuru şeridi:** YAZ-ÇİZ-ÖĞRET HEPSİ BİR ARADA
- **Güven şeridi:** 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi

### SSS

**Kaynak: `custom_liquid_bGxbxk`**

- **Çocuğumun gelişimine gerçekten katkısı var mı?** Evet, birden fazla alanda somut katkı sağlar: projeksiyon takibi ile el-göz koordinasyonu, serbest çizimle ince motor becerileri ve yaratıcılık, müzik eşliğiyle işitsel gelişim ve konsantrasyon. Öğrenmeyi oyuna dönüştürdüğü için çocuklar farkında olmadan geliş …
- **Projeksiyon özelliği nasıl çalışıyor?** Zürafa figürünün başındaki projektör, farklı şekil ve görselleri çizim tahtasına yansıtır. Çocuklar yansıyan şeklin üzerinden kalemi geçirerek çizim yapmayı öğrenir. Bu yöntem el-göz koordinasyonunu çok etkili biçimde geliştirir ve birden fazla şablon seçeneği …
- **Müzik özelliği var mı, nasıl kullanılıyor?** Evet, dahili müzik sistemi mevcuttur. Farklı melodiler ve sesler içeren bu özellik çizim sırasında çocuğun dikkatini canlı tutar ve öğrenmeyi eğlenceli hale getirir. Müzik tuşlarına basarak açılır, ses seviyesi ayarlanabilir.
- **Çizim yüzeyi silinebilir mi, kalıcı mı?** Çizim yüzeyi tamamen silinebilir. Kuru veya hafif nemli bir bezle kolayca temizlenir. Çocuğunuz istediği kadar çizebilir, silip yeniden başlayabilir. Kağıt ve kalem tüketimi olmadığı için hem ekonomik hem de çevre dostudur.
- **Bu ürün kaç yaş için uygun?** 3 yaş ve üzeri çocuklar için idealdir. Okul öncesi dönemdeki küçük çocukların motor becerilerini geliştirirken büyük çocukların da yaratıcılığını destekler. Projeksiyon ve müzik özellikleri sayesinde her yaştan çocuğun ilgisini çeker.
- **İade ve değişim koşulları nelerdir?** Teslim tarihinden itibaren 14 gün içinde iade veya değişim talebinde bulunabilirsiniz. Ürünün orijinal ambalajında, kullanılmamış ve eksiksiz olması gerekmektedir. Detay için müşteri hizmetlerimizle iletişime geçebilirsiniz.
- **Pille mi çalışıyor, piller kutuda mı geliyor?** Ürün pil ile çalışmaktadır. Piller ürünle birlikte gelmeyebilir; satın almadan önce kutu içeriğini kontrol etmenizi öneririz. Pil kapağı ebeveynler tarafından kolayca açılabilecek şekilde tasarlanmıştır.
- **Kaç günde teslim edilir?** Siparişler 1–3 iş günü içinde kargoya verilir, teslim süresi bölgeye göre 2–5 iş günüdür. Kargo takip bilgisi sipariş sonrası e-posta ile iletilir. Hafta içi verilen siparişler aynı gün kargoya teslim edilir.
- **Ürünün boyutları nedir, taşınabilir mi?** Çizim yüzeyi 37 cm genişliğinde olup kompakt ve hafif yapısıyla her yerde kullanılabilir. Masada, zeminde ve seyahatte rahatlıkla kullanım sunar. Çanta içine sığabilecek boyuttadır.


### Yorumlar

- **Sayfada yazan:** "4.7 (2467 Onaylı Kullanıcı Yorumu)" (sabit metin)
- **Loox gerçek:** 7 yorum, ortalama 5.0 (dağılım: 5★×7); ilk 20 yorumun tarihleri: 18.05.2026 ×7; "Doğrulanmış" etiketi: 0
- **Loox örnek:** "Ürün videolardaki gibi tavsiye ediyorum" / "Evimin dinlenme köşesi için aldım gayet hoş" / "Ürün siparişinden çok kısa zamanda elime geçti,özenli paketleme ve uzaktan kumandalı , şık duruşu ile çok beğendim😍 Tafsiye ederim.." / "Ürün sipariş verdiğim günün sonrası elime ulaştı gayet sağlam ve güvenilir paketlenmişti. İsteği bağlı loş ve parlak renkleri ışık derecesin …"

### Açıklama (body_html)

- Boş. Ürün metni yalnız tema bölümlerinde.

### Sorunlu iddialar

- **Kopya içerik (kritik):** Galeri dışındaki her şey Eğitici Çizim Tahtası: "Neden Bu Çizim Tahtası?", "37 cm Geniş Çizim Alanı", "3 Yaş ve Üzeri", "ANNELERDEN GELENLER", "Sadece Bir Oyuncak Değil", zürafa görselleri, 9 soruluk çizim tahtası SSS'si, duyuru "YAZ-ÇİZ-ÖĞRET HEPSİ BİR ARADA".
- **Fiyat:** Fiyat 1.299,99 TL, karşılaştırma 1.299,00 TL (karşılaştırma fiyattan düşük).
- **Sağlık:** Görsel 6: "Göz Koruyucu Filtre", "12 LED Göz Dostu Teknoloji".
- **Teyitsiz teknik / güvenlik:** CE işareti (belge yok), "Darbeye & Suya Dayanıklı Gövde"; görsel 7 küvet kenarında kullanım.
- **İade çelişkisi:** Kopya SSS "14 gün iade"; güven şeridi "90 gün".
- **Uydurma puan:** Sayfa "4.7 (2467)"; Loox 7 yorum, 5.0, hepsi 18.05.2026, "Doğrulanmış" yok.
- **Kutu:** Sayfada bu ürünün kutu içeriği yok; görsel 5'te lamba + kumanda + Type-C kablo.

---

## 5. Sunset Lamba — `sunset-lamba`

- **Adres:** https://ayluna.shop/products/sunset-lamba
- **Fiyat:** 699,00 TL · karşılaştırma: 999,00 TL → gerçek indirim %30.0
- **Varyantlar** (Title): Default Title — 699,00 TL — satışta
- **Şablon:** `template--28025597427940` · sayfa yüksekliği 7351 px · vendor: Ayluna
- **Ekran görüntüleri** (8 parça, klasör `…/scratchpad/site/urun/`): `sunset-lamba-1.png`, `sunset-lamba-2.png`, `sunset-lamba-3.png`, `sunset-lamba-4.png`, `sunset-lamba-5.png`, `sunset-lamba-6.png`, `sunset-lamba-7.png`, `sunset-lamba-8.png`
- Ana bölüm içinde ayrıca 3 video ("Gerçek Kullanıcılar") ve 7 soruluk SSS var; aynı SSS sayfanın altında bir kez daha tekrar ediyor.
- Paket teklifi (Kaching) yok.

### Görseller (5)

1. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Square_1_1_product_image._A_202605101854.jpg?v=1778428533
   Afiş (koyu zemin, ürün render): "SUNSET LAMP · 16 Renk · Uzaktan Kumandalı · USB" + "ÜCRETSİZ KARGO" rozeti.
2. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Square_1_1_product_image._4-panel_202605101854.jpg?v=1778428533
   4'lü panel afiş: "16 RENK SEÇENEĞİ · Tek Dokunuşla Atmosferi Değiştir" (turuncu, mavi, gökkuşağı, mor).
3. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Square_1_1_product_infographic_image._202605101855.jpg?v=1778428533
   Bilgi afişi: "NEDEN BU LAMBA?" Uzaktan Kumanda · USB Bağlantı · 360° Döner Kafa · 16 Renk Modu.
4. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Square_1_1_lifestyle_product_image._202605101855.jpg?v=1778428533
   Yaşam (yatak odası): "Her Gece Bir Gün Batımı" + rozet "4.9 · 2.400+ Satış".
5. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Square_1_1_promotional_product_image._202605101855.jpg?v=1778428533
   Kampanya afişi: "BUGÜN %30 İNDİRİM · Stoklar Sınırlı! · HEMEN SATIN AL · Ücretsiz Kargo · Hızlı Teslimat". Gövde pembe/rose, kumanda görünüyor (1. görselde siyah).

### Bölüm sırası

Tam id biçimi: şablon bölümleri `shopify-section-template--28025597427940__<anahtar>`, global bölümler `shopify-section-sections--28025597690084__<anahtar>` (altbilgi `…28025597657316__footer`).

1. `custom_liquid_XWzNR9` — Üst geri sayım şeridi (global): "Bugüne Özel %20 İndirim" + sayaç
2. `header` — Başlık (global): menü, logo, arama, sepet
3. `announcement_bar_m7VX6j` — Duyuru şeridi: Güneş Artık Odanda Batıyor ✨
4. `main` — **Ana ürün bölümü** (galeri 5 görsel), blok sırası:
   - Başlık: Sunset Lamba
   - Puan satırı: 4.7 ( 2467 Onaylı Kullanıcı Yorumu)
   - Fiyat satırı: 699,00 TL · 999,00 TL üstü çizili · rozet "%20 İndirim"
   - Kargo sayacı: 🚚 · 19:35:57 içerisinde sipariş verirsen bugün kargoda.
   - Özellik başlığı: 🌅 Neden Bu Lamba? 🌅 · Odanı birkaç saniyede atmosfere dönüştür
   - Özellik kartları: 16 Canlı Renk Modu · Uzaktan Kumandalı · 360° Döner Projektör Kafa · USB ile Kolay Bağlantı · Sinematik Gün Batımı Efekti
   - Canlı izleyici sayacı: 33 kişi şu anda bu ürünü inceliyor.
   - Kargo notu: KREDİ KARTI İLE VERİLEN ŞİPARİŞLER HIZLI KARGO İLE ÇIKARTILMAKTADIR
   - Satın al butonları: Güvenli Ödeme İle Al · Kapıda Ödeme ile Sipariş Ver
   - Ödeme logoları: Amex, Diners, Discover, JCB, Mastercard, Visa
   - Teslimat zaman çizelgesi: 18 Ekm · Siparişiniz Oluşturuldu · 19 Ekm - 20 Ekm · Kargonuz Hazırlandı · 21 Ekm - 23 Ekm · Evinize Teslim Edildi
   - Video yorumlar (3 video): Gerçek Kullanıcılar · Binlerce mutlu müşteriden sadece 3 tanesini paylaştık 🌅 · Odamı değiştirdi 🌅 · Atmosfer bambaşka oldu · 16 rengi denedim ✨ · Her biri ayrı güzel · Gün batımı evimde 🔥 · Uzaktan kumanda süper
   - Güven şeridi: 1 Yıl Garanti · Ücretsiz Kargo · 90 Gün Para İade Garantisi
   - Yapışkan sepet çubuğu: Sunset Lamba · 699.00TL · 999.00TL · Sepete Ekle
   - Kısa yorum kaydırıcısı (3 yorum): Kızım bayıldı 💙 Her gece kullanıyor Işık yumuşacık, uykuya geçişimiz inanılmaz kolaylaştı. Masal açıp birlikte izlemek de ayrı keyif. · Elif K. · En büyük artısı ortamı bir anda sakinleştirmesi. Kız arkadaşınıza alabilirsiniz · Gülsüm S. · Hediye aldım, alan kişi aşık oldu 🎁 Temalar çok güzel, odanın havasını değiştiriyor. Işık göz yormuyor; gece boyunca açık kalsa bile rahatsız etmiyor. · Mehmet Ö.
   - SSS (ana bölüm içinde): sorular aşağıdaki SSS listesinde
5. `insta_stories_xe3xA6` — Instagram hikâyeleri: İnstagram'da Ayluna · Bizleri tercih eden mutlu anne ve çocuklarımızın hikayeleri sizlerle ❤️ [3 görsel: IMG_4145.jpg, IMG_4146.jpg, IMG_4147.jpg]
6. `section_divider_ARXJ86` — Ayraç
7. `section_divider_qmrTwn` — Ayraç
8. `eba88da5-80ac-47fc-aa75-997cfe7b2e59` — Yorum ekran görüntüsü kaydırıcısı: +2000 Mutlu Annenin söylediklerini okuyun [16 görsel: imgi_22_saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa…, imgi_15_saaaaaaaaaaaa_6.png, imgi_16_Adsiz_tasarim_36.png …]
9. `horizontal_ticker_rbYQET` — Kayan şerit: Ücretsiz Kargo 📦 · 21 Farklı Mod ✨ · Çocuklara Özel 👶🏻
10. `image_banner_Ae7wdz` — GIF afiş + başlık: Senin Odan, Senin Güneşin · EN SEVDİĞİNİZ YERLERİ EĞLENCE İLE DONATIN. [1 görsel: Savetik_1778428724.gif]
11. `8beb6911-28c6-482c-976a-e5421ad3e8df` — Özellik satırları (4 başlık + görsel): 16 Renk, Sonsuz Atmosfer · Tek dokunuşla turuncu gün batımından elektrik mavisine, derin mordan gökkuşağı gradyanına 16 farklı renk arasında geçiş yap. Her mod farklı bir his yaratır. · Uzaktan Kumanda Kolaylığı · Renk değiştirmek, parlaklığı ayarlamak veya lambayı açıp kapatmak için yerinden kalkmanı gerekmiyor. Dahili uzaktan kumanda ile her şey parmak ucunda. · Sinematik Projektör Efekti · Lamba duvarına mükemmel … [1 görsel: Square_1_1_product_infographic_image._202605…]
12. `image_with_text_8UNBF8` — Görsel + metin + buton: Gün Batımını Odana Taşı · Ayluna, ailesi olarak en son teknoloji ürünleri terchi ettiğimizi belirtmek isteriz. Son teknoloji projeksiyon çipimiz sayesinde mükemmel yansıtma gücü sağlar. · Sunset Lambayı Sipariş Ver [1 görsel: Square_1_1_promotional_product_image._202605…]
13. `custom_liquid_bGxbxk` — Özel Liquid: SSS, 7 soru (aşağıda)
14. `b321ab88-2b59-4dba-bade-54885c874ca5` — Ayraç
15. `17694466126b1e0319` — Loox yorum uygulaması (iframe; ayrıntı aşağıda)
16. `footer` — Altbilgi (global): %5 indirim için e-posta aboneliği, ödeme logoları, politikalar

### Paket teklifi, geri sayım, kargo

- **Paket (Kaching):** yok
- **Geri sayım:** üst şerit "Bugüne Özel %20 İndirim 01 SAAT : 01 DK : 40 SAN" (her yüklemede yeniden başlar); kargo sayacı "… içerisinde sipariş verirsen bugün kargoda" (15:00'e sayar)
- **Duyuru şeridi:** Güneş Artık Odanda Batıyor ✨
- **Güven şeridi:** 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi

### SSS

**Kaynak: `main`**

- **Bu lamba gerçekten gün batımı efekti yaratıyor mu?** Evet! Lamba, duvarınıza gerçek bir gün batımını andıran büyük dairesel bir ışık yansıtır. Turuncu, pembe, kırmızı ve daha pek çok renkte mükemmel bir atmosfer yaratır. Karanlık bir odada etkisi çok daha dramatik görünür.
- **Nasıl bağlanıyor, prize takıyor muyum?** Lamba USB ile çalışır. Paketten çıkan USB kablo ile bilgisayarınıza, power bank'e veya herhangi bir USB adaptörüne bağlayabilirsiniz. Standart prize takmak için evinizdeki USB şarj başlıklarından herhangi birini kullanabilirsiniz.
- **Oda ne kadar büyük olmalı, küçük odada çalışır mı?** Her boyuttaki odada kullanılabilir. Küçük odalarda ışık daha yoğun ve etkileyici görünür. Büyük odalarda duvara yakın konumlandırmak daha iyi sonuç verir. En iyi etki için odanızı karartmanızı öneririz.
- **Kaç farklı renk seçeneği var?** Toplam 16 farklı renk modu bulunuyor. Klasik turuncu gün batımından elektrik mavisine, gökkuşağı gradyanından derin mora kadar her atmosfere uygun bir seçenek var. Renk değiştirmek için uzaktan kumandayı kullanabilirsiniz.
- **Uzaktan kumanda dahil mi geliyor?** Evet, uzaktan kumanda kutu içinde geliyor. Kumanda ile renk değiştirme, parlaklık ayarı ve açma/kapama işlemlerini kolayca yapabilirsiniz. Pil dahildir, kullanıma hazır olarak teslim edilir.
- **Projektör kafası döndürülebiliyor mu?** Evet, 360° döner kafa sayesinde ışığı istediğiniz yöne, tavana veya duvara yönlendirebilirsiniz. Boyutları da ayarlanabilir olduğundan farklı mesafelerde ve açılarda kullanım mümkündür.
- **Kaç günde teslim edilir?** Siparişleriniz genellikle 2–5 iş günü içinde kapınıza ulaşır. Kargo takip bilgisi sipariş sonrası e-posta ile gönderilir. Hafta içi saat 14:00'e kadar verilen siparişler aynı gün kargoya verilir.

- *`custom_liquid_bGxbxk` bölümü yukarıdaki soruların aynısı (tekrar).*

### Yorumlar

- **Sayfada yazan:** "4.7 (2467 Onaylı Kullanıcı Yorumu)" (sabit metin)
- **Loox gerçek:** 0 yorum ("Yorum yapan ilk kişi olun")

### Açıklama (body_html)

- Boş. Ürün metni yalnız tema bölümlerinde.

### Sorunlu iddialar

- **Uydurma puan:** Sayfa "4.7 (2467 Onaylı)"; görsel 4 "4.9 · 2.400+ Satış"; Loox: 0 yorum.
- **Kopya yorum:** Kısa yorumlar LunaDream'den: "Kızım bayıldı… Masal açıp birlikte izlemek", "Temalar çok güzel" (bu üründe masal/tema yok). "+2000 Mutlu Annenin" kaydırıcısı başka ürünlerin sohbetleri.
- **Fiyat çelişkisi:** Rozet ve üst şerit "%20 İndirim", görsel 5 "BUGÜN %30 İNDİRİM"; gerçek oran %30 (699/999).
- **Kopya şerit:** "21 Farklı Mod ✨ · Çocuklara Özel 👶🏻" (ürün 16 renk, yetişkin dekor ürünü).
- **Teyitsiz teknik:** "Son teknoloji projeksiyon çipimiz", "profesyonel stüdyo havası", "Boyutları da ayarlanabilir".
- **Kargo çelişkisi:** SSS "Hafta içi 14:00'e kadar aynı gün kargo"; sayaç 15:00'e sayıyor ve pazar günü de "bugün kargoda" diyor.
- **Kutu:** SSS "kumanda pili dahil" (teyitsiz); görsel 1 siyah gövde, görsel 5 pembe gövde.
- **İade:** "90 Gün Para İade Garantisi".

---

## 6. Ayluna Çocuk Gece Feneri — `ayluna-cocuk-gece-feneri`

- **Adres:** https://ayluna.shop/products/ayluna-cocuk-gece-feneri
- **Fiyat:** 1.599,00 TL · karşılaştırma: yok
- **Varyantlar** (Title): Default Title — 1.599,00 TL — satışta
- **Şablon:** `template--28025597460708` · sayfa yüksekliği 7091 px · vendor: Ayluna
- **Ekran görüntüleri** (8 parça, klasör `…/scratchpad/site/urun/`): `ayluna-cocuk-gece-feneri-1.png`, `ayluna-cocuk-gece-feneri-2.png`, `ayluna-cocuk-gece-feneri-3.png`, `ayluna-cocuk-gece-feneri-4.png`, `ayluna-cocuk-gece-feneri-5.png`, `ayluna-cocuk-gece-feneri-6.png`, `ayluna-cocuk-gece-feneri-7.png`, `ayluna-cocuk-gece-feneri-8.png`
- Ana bölüm içinde "Sizden Gelenler" 3 video; başlıklar yer tutucu kalmış ("Video 1 · Ürünü keşfet 🎥").
- Paket teklifi yok.

### Görseller (9)

1. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260418_163141_23c3a797-5981-4534-873d-9ea2ceda9a92.png?v=1776530205
   Afiş (gece odası): "MASALSI GECE IŞIĞI · Saniyeler içinde ortamı büyülü bir atmosfere çevir." Tema projeksiyonları · Yumuşak ambiyans ışığı · Hediye için harika · ŞİMDİ KEŞFET.
2. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260418_162334_889eab85-b500-4115-9fd7-793cdec87a5b.png?v=1776530205
   Düz çekim (pembe kâğıt, kurutulmuş çiçek): "6 Film · USB Şarj · 360° Rotasyon"; 6 disk (geyik, gezegenler, balina, doğum günü, takımyıldız, çift), USB kablo, hediye etiketi.
3. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260418_163134_34436b2a-5bd8-449f-a57d-3a3d372a4417.png?v=1776530205
   Afiş: "TEK LAMBA, FARKLI TEMALAR · Film diskini tak, duvarın canlansın." 9 disk gösteriliyor (Doğum günü, Yıldızlar, Deniz altı…) · Diski seç · Tak & çalıştır · Yansıt.
4. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260418_162134_a84d8942-5806-405f-b815-559d34b38254.png?v=1776530205
   Yaşam (çocuk odası): "Odasını Okyanusa Çevir" — duvar/tavan boyu balina projeksiyonu; masadaki cihaz farklı (taçlı mavi kubbe).
5. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260418_163401_59c2c00f-6cff-4043-8d65-9c0f331a85c8.png?v=1776530205
   Afiş (hediye kutusu): "EN GÜZEL HEDİYE SIHIRLI BİR GECE" Özel hediye kutusunda gelir · 6 tema diski dahil · Sevdiklerinizi şaşırtın · HEDİYE AL.
6. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260418_163347_a6ff20f1-987f-4366-8c6c-b2ae1c16faf4.png?v=1776530205
   Karşılaştırma afişi: "NEDEN HER ANNE ALIYOR?" Sıradan gece lambaları: "tek renk, sıkıcı, çocuğu uyutamaz" / Yıldız Projektörü: "6 farklı tema, 360° döner projeksiyon, anında uyku ortamı" · 6 Değişebilir Film Diski · 360° Döner Projeksiyon · USB ile Şarj.
7. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260418_163125_39849f74-b1de-440b-9e7f-36f1a16f0751.png?v=1776530205
   Yorum kartı: "Kızım bayıldı 💙 Her gece yıldızları yak diyor… artık daha kolay uykuya geçiyor" Zeynep A. 5/5 "Doğrulanmış Alıcı" · SEPETE EKLE.
8. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260418_161909_3c796747-1f39-433f-86c6-4b6bfff5ec3f.png?v=1776530205
   Yaşam (iki çocuk çadırda kitap okuyor, tavanda ay/geyik/yıldız): "Hayalin Işığını Yak".
9. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260418_163408_b14d434e-1e93-4a95-a615-b7e44e6d2956.png?v=1776530151
   Afiş (uyuyan çocuk): "YILDIZLARI ODASINA TAŞI ✨ Her gece farklı bir evren — 6 tema, sonsuz hayal." 6 Film Diski · 360° Projeksiyon · Yumuşak Gece Işığı.

### Bölüm sırası

Tam id biçimi: şablon bölümleri `shopify-section-template--28025597460708__<anahtar>`, global bölümler `shopify-section-sections--28025597690084__<anahtar>` (altbilgi `…28025597657316__footer`).

1. `custom_liquid_XWzNR9` — Üst geri sayım şeridi (global): "Bugüne Özel %20 İndirim" + sayaç
2. `header` — Başlık (global): menü, logo, arama, sepet
3. `announcement_bar_m7VX6j` — Duyuru şeridi: Çocuğun Odasını Masala Çevir ✨
4. `main` — **Ana ürün bölümü** (galeri 9 görsel), blok sırası:
   - Başlık: Ayluna Çocuk Gece Feneri
   - Puan satırı: 4.7 ( 2467 Onaylı Kullanıcı Yorumu)
   - Fiyat satırı: 1.599,00 TL · rozet "%20 İndirim"
   - Kargo sayacı: 🚚 · 19:32:58 içerisinde sipariş verirsen bugün kargoda.
   - Özellik başlığı: ✨ Sihirli Özellikler ✨ · Çocuğunuzun hayallerini gerçeğe dönüştürün
   - Özellik kartları: Uyku Dostu Yumuşak Işık · 6 Tema Diski ve Projeksiyon · +10.000 Mutlu Müşteri · Şarjlı ve Kablosuz Kullanım · Çocuğunuzun hayalleri artık odasında
   - Canlı izleyici sayacı: 32 kişi şu anda bu ürünü inceliyor.
   - Kargo notu: KREDİ KARTI İLE VERİLEN ŞİPARİŞLER HIZLI KARGO İLE ÇIKARTILMAKTADIR
   - Satın al butonları: GÜVENLİ ÖDEME İLE AL · Kapıda Ödeme ile Sipariş Ver
   - Ödeme logoları: Amex, Diners, Discover, JCB, Mastercard, Visa
   - Teslimat zaman çizelgesi: 18 Ekm · Siparişiniz Oluşturuldu · 19 Ekm - 20 Ekm · Kargonuz Hazırlandı · 21 Ekm - 23 Ekm · Evinize Teslim Edildi
   - Video yorumlar (3 video): Sizden Gelenler · 10.000 anneden sadece 3 tanesini sizinle paylaştık 🩷 · Video 1 · Ürünü keşfet 🎥 · Video 2 · Detayları gör ✨ · Video 3 · Hemen dene 🚀
   - Güven şeridi: 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi
   - Yapışkan sepet çubuğu: Ayluna Çocuk Gece Feneri · 1,599.00TL · Sepete Ekle
   - Kısa yorum kaydırıcısı (3 yorum): Kızım bayıldı 💙 Her gece yıldızları yak diye tutturuyor. Işık yumuşacık, uykuya geçişimiz inanılmaz kolaylaştı. Masal açıp birlikte izlemek de ayrı keyif. · Elif K. · En büyük artısı ortamı bir anda sakinleştirmesi. Oğlum karanlıktan korkuyordu, şimdi odasında daha rahat uyuyor. Bluetooth’tan ninni açınca resmen rutin oturdu. · Gülsüm S. · Hediye aldım, alan kişi de çocuk da aşık oldu 🎁 Temalar çok güzel, odanın havasını değiştiriyor. Işık göz yormuyor; gece boyunca açık kalsa bile rahatsız etmiyor. · Zeynep R.
   - Açılır soru: Gece rutinine nasıl entegre ederim?
   - Açılır soru: Bu ürün ne işe yarıyor?
   - Açılır soru: Projeksiyon nasıl çalışıyor?
   - Açılır soru: Hoparlör olarak kullanabilir miyim ?
   - Açılır soru: Bluetooth var mı, ne işe yarıyor?
   - Açılır soru: Parlaklığı çocuğu rahatsız eder mi?
   - Açılır soru: Kutu içeriğinde neler var?
   - Açılır soru: Bluetooth bağlanmıyor, ne yapmalıyım?
5. `insta_stories_xe3xA6` — Instagram hikâyeleri: İnstagram'da Ayluna · Bizleri tercih eden mutlu anne ve çocuklarımızın hikayeleri sizlerle ❤️ [3 görsel: IMG_4145.jpg, IMG_4146.jpg, IMG_4147.jpg]
6. `section_divider_ARXJ86` — Ayraç
7. `section_divider_qmrTwn` — Ayraç
8. `eba88da5-80ac-47fc-aa75-997cfe7b2e59` — Yorum ekran görüntüsü kaydırıcısı: +2000 Mutlu Annenin söylediklerini okuyun [16 görsel: imgi_22_saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa…, imgi_15_saaaaaaaaaaaa_6.png, imgi_16_Adsiz_tasarim_36.png …]
9. `horizontal_ticker_rbYQET` — Kayan şerit: Ücretsiz Kargo 📦 · 6 Farklı Mod ✨ · Çocuklara Özel 👶🏻
10. `image_banner_Ae7wdz` — GIF afiş + başlık: En Güzel Hediye · ÇOCUKLARIMIZIN EN SEVDİĞİ YERLERİ OLAN ODALARINI ONLAR İÇİN EĞLENCE İLE DONATIN. [1 görsel: hf_20260418_163401_59c2c00f-6cff-4043-8d65-9…]
11. `8beb6911-28c6-482c-976a-e5421ad3e8df` — Özellik satırları (4 başlık + görsel): Çeşitli Animasyon Seçenekleri · Gece lambası projektörümüz, 6 farklı animasyon seçeneği ile odanızı büyülü bir hale getirir. · Projektör ve Işık Efektleri · Gece lambası projektörü, ışık efektleri ve projeksiyonları ile odanızı aydınlatırken etkileyici bir görsel deneyim sunar. · Bluetooth Özelliği ile Müzik ve Hikaye Dinleme · Cihazı telefon veya tabletinize bağlayarak çocuğunuzun favori müziklerini veya sesli hikay … [1 görsel: hf_20260418_163125_39849f74-b1de-440b-9e7f-3…]
12. `image_with_text_8UNBF8` — Görsel + metin + buton: Yıldız Işığı Ambiyansı, Tek Dokunuşla · Ayluna, ailesi olarak en son teknoloji ürünleri terchi ettiğimizi belirtmek isteriz. Son teknoloji projeksiyon çipimiz sayesinde mükemmel yansıtma gücü sağlar. · Ayluna Çocuk Gece Feneri [1 görsel: hf_20260418_163408_b14d434e-1e93-4a95-a615-b…]
13. `collapsible_content_7zjVTU` — SSS (açılır): SSS, 8 soru (aşağıda)
14. `b321ab88-2b59-4dba-bade-54885c874ca5` — Ayraç
15. `17694466126b1e0319` — Loox yorum uygulaması (iframe; ayrıntı aşağıda)
16. `footer` — Altbilgi (global): %5 indirim için e-posta aboneliği, ödeme logoları, politikalar

### Paket teklifi, geri sayım, kargo

- **Paket (Kaching):** yok
- **Geri sayım:** üst şerit "Bugüne Özel %20 İndirim 01 SAAT : 01 DK : 40 SAN" (her yüklemede yeniden başlar); kargo sayacı "… içerisinde sipariş verirsen bugün kargoda" (15:00'e sayar)
- **Duyuru şeridi:** Çocuğun Odasını Masala Çevir ✨
- **Güven şeridi:** 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi

### SSS

**Kaynak: `main`**

- **Hoparlör olarak kullanabilir miyim ?** Tabikide evet gelişmiş uzaktan bağlantı özelliği sayesinde telefonunuzdan bağlanarak dilediğiniz müziği açabilir ve evinizin ambiyansını daha üst seviyelere çıkartabilirsiniz.
- **Bu ürün ne işe yarıyor?** Çocuğun odasını yumuşak bir gece ışığı ve projeksiyon efektleri ile daha sakin bir uyku ortamına çevirir.Ayrıca Bluetooth ile telefondan ninni müzik masal açabilirsiniz.
- **Gece rutinine nasıl entegre ederim?** Uyku öncesi 10 dakika: ışığı aç → favori temayı yansıt → telefondan kısa ninni/masal aç → aynı rutini her gece tekrarla.
- **Projeksiyon nasıl çalışıyor?** Cihazın projeksiyon modunu açıp seçtiğiniz temayı kullanarak duvar/tavan üzerine görsel yansıma alırsınız.
- **Bluetooth var mı, ne işe yarıyor?** Evet — telefon/tablete bağlayıp çocuğun sevdiği ninni, müzik veya sesli hikâyeleri çalabilirsiniz.
- **Parlaklığı çocuğu rahatsız eder mi?** Tabikide hayır :)Yumuşak ambiyans için tasarlandı; gece boyunca göz yormayan kullanım hedeflendi
- **Kutu içeriğinde neler var?** Cihaz + Tema diskleriŞarj kablosu Kullanım kılavuzu

**Kaynak: `collapsible_content_7zjVTU`**

- **Bu modelde hangi özellikler var?** Bu model hareket sensörlü değildir. (Bazı modellerde sensör bulunabiliyor.) Bu üründe tüm kontrol tuşlar/kumanda üzerinden yapılır; böylece gece kullanımında daha stabil ve sürprizsiz bir deneyim sağlar.
- **Hareket sensörü nasıl çalışır?** Sensör, hareket algıladığında ışığı otomatik olarak açar. Belirli bir süre hareket algılamazsa ışık kendiliğinden kapanır. Gece koridor, yatak yanı ve çocuk odası kullanımında çok pratiktir.
- **Tuşlar ile neleri kontrol edebilirim?** Genellikle aç/kapat, ışık modu/efekti geçişi, parlaklık ayarı, projeksiyon modları, müzik ses kontrolü gibi temel işlevleri kolayca yönetebilirsiniz.
- **Bluetooth hoparlöre nasıl bağlanırım?** Ürünü açın ve Bluetooth modunu aktif edin.Telefonunuzda Bluetooth’u açın → cihaz listesinden ürünü seçin Bağlandıktan sonra Spotify/YouTube/telefonunuzdaki ninnileri doğrudan hoparlörden çalabilirsiniz.
- **Ürün şarjlı mı, prizde mi çalışır?** Ürün şarjlıdır ve kablosuz kullanılabilir. İsterseniz şarj ederken de kullanabilirsiniz (kullanım alışkanlığına göre pratiklik sağlar).
- **Şarjı ne kadar gider?** Şarj süresi; parlaklık seviyesi, projeksiyonun açık kalması, Bluetooth ses düzeyi gibi etkenlere göre değişir. Gece rutininde (orta parlaklık düşük ses) genelde birkaç saatlik kullanım sağlar.
- **Gece kullanımında göz yorar mı?** Uyku için tasarlanan yumuşak ışık modunda rahatsız etmez. En iyi deneyim için:Parlaklığı orta/düşük kullanın,Işığı doğrudan göze değil, duvara/tavana yansıtın.
- **Çocuk odasında kullanmak güvenli mi?** Evet, çocuk odası kullanımına uygundur. LED ışık düşük ısı üretir. Güvenlik için:Ürünü düz ve sağlam bir zemine koyun,Tema diskleri küçük parça olabileceği için küçük çocuklarda ebeveyn gözetimiyle kullanın,Kabloyla kullanımda kabloyu ortalıkta bırakmayın.


### Yorumlar

- **Sayfada yazan:** "4.7 (2467 Onaylı Kullanıcı Yorumu)" (sabit metin)
- **Loox gerçek:** 0 yorum ("Yorum yapan ilk kişi olun")

### Açıklama (body_html)

- Boş. Ürün metni yalnız tema bölümlerinde.

### Sorunlu iddialar

- **Sağlık:** "Uyku Dostu Yumuşak Işık", "daha sakin bir uyku ortamı", görsel 6 "Sıradan gece lambaları çocuğu uyutamaz… anında uyku ortamı", yorum "Oğlum karanlıktan korkuyordu, şimdi daha rahat uyuyor".
- **Uydurma puan:** Sayfa "4.7 (2467)", "+10.000 Mutlu Müşteri", "10.000 anneden sadece 3 tanesi"; Loox: 0 yorum.
- **Uydurma yorum:** Görsel 7 Zeynep A. "Doğrulanmış Alıcı 5/5"; kısa yorumlar LunaDream'den kopya.
- **Kopya SSS:** "Bu model hareket sensörlü değildir" cevabının hemen ardından "Hareket sensörü nasıl çalışır?" (AyFeneri'nden). "Hoparlör olarak kullanabilir miyim? Tabikide evet" — Bluetooth hiçbir görselde yok (görsel 2: "6 Film · USB Şarj · 360° Rotasyon").
- **Kutu çelişkisi:** "6 film/tema diski" (görsel 2, 5, 9) ↔ görsel 3'te 9 disk; "Özel hediye kutusunda gelir" teyitsiz.
- **Görsel:** Görsel 4 başka bir cihaz (taçlı mavi kubbe) ve oda boyu abartılı projeksiyon.
- **Fiyat:** Karşılaştırma fiyatı yok ama "%20 İndirim" rozeti.
- **İade:** "90 Gün Para İade Garantisi".

---

## 7. Ayluna Galaksi Night Projektör — `ayluna-galaksi-night-projektor`

- **Adres:** https://ayluna.shop/products/ayluna-galaksi-night-projektor
- **Fiyat:** 2.199,00 TL · karşılaştırma: 2.999,00 TL → gerçek indirim %26.7
- **Varyantlar** (Title): Default Title — 2.199,00 TL — satışta
- **Şablon:** `template--28025597362404` · sayfa yüksekliği 11017 px · vendor: Ayluna
- **Ekran görüntüleri** (12 parça, klasör `…/scratchpad/site/urun/`): `ayluna-galaksi-night-projektor-1.png`, `ayluna-galaksi-night-projektor-2.png`, `ayluna-galaksi-night-projektor-3.png`, `ayluna-galaksi-night-projektor-4.png`, `ayluna-galaksi-night-projektor-5.png`, `ayluna-galaksi-night-projektor-6.png`, `ayluna-galaksi-night-projektor-7.png`, `ayluna-galaksi-night-projektor-8.png`, `ayluna-galaksi-night-projektor-9.png`, `ayluna-galaksi-night-projektor-10.png`, `ayluna-galaksi-night-projektor-11.png`, `ayluna-galaksi-night-projektor-12.png`
- En çok bölümlü sayfa: video, "Neden En İyisi?", katmanlı lens videosu, WhatsApp mesajları, kolaj, sağlık slaytı, özellik satırları.
- Ana bölümde başlık sırası farklı: puan + "Son 10 Günün en düşük fiyatı" başlığın ÜSTÜNDE.
- Teslim tahmini kutusu (il seçimi) ve "18 saat 32 dakika içinde sipariş verirsen yarın kargoda" yalnız bu ve LunaDream V2'de.
- SSS iki kez (ana bölüm + ayrı bölüm, aynı 12 soru).

### Görseller (8)

1. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Galaxy_projector_product_infogra__202609012212.jpg?v=1788290005
   Afiş (lacivert): "Evinin Tavanında Gerçek Bir Galaksi · 5K Ultra HD disklerle" Gerçek uzay görselleri · 12 katmanlı optik lens · 153.748 yıldız detayı · Şarjlı ve kablosuz · Planetaryum Kalitesi · Sessiz Çalışma · 1 Yıl Garanti.
2. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Galaxy_projector_product_infogra__202609012139.jpg?v=1788288406
   Afiş (krem): "FARKLI TEMALAR HER GECE YENİ SAHNE · Değiştirilebilir 12 adet 5K diskle" Kolay disk değişimi · 12 farklı gökyüzü · "Değiştirilebilir 12 Adet 5K Ultra HD Disk".
3. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Star_projector_infographic_design_202609012133.jpg?v=1788288406
   Afiş: "153.748 YILDIZ GERÇEK DERİNLİK" 5K Ultra HD disk · Doğal yıldız dokusu · "Göz yormayan ışık" (iki kez) · Gerçek Projeksiyon Kalitesi.
4. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Projector_lens_system_infographic_202609012139.jpg?v=1788288406
   Afiş: "12 KATMANLI OPTİK LENS SİSTEMİ" Yüksek iletim oranı · Keskin kenar netliği · Homojen aydınlatma · Premium Lens Teknolojisi.
5. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Projector_displaying_galaxy_in_room_202609012139.jpg?v=1788288406
   Afiş (salon): "130 m² KADAR GENİŞ YANSITMA" Geniş açı · Ayarlanabilir başlık · Duvar ve tavan modu · "Tek Cihaz, Tüm Oda".
6. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Galaxy_projector_product_infogra__202609012141.jpg?v=1788288406
   Ölçü afişi (elde): "KOMPAKT VE ŞIK TASARIM · USB-C kablosu ile prize tak" 15 cm × 9 cm · Masa üstü · Kolay taşınır · USB-C güç girişi · "USB Bağlantısı ile Kesintisiz Kullanım".
7. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Galaxy_projector_product_infogra__202609012144.jpg?v=1788288406
   Yorum afişi: "Kullanıcılardan Yorumlar · 4.7 ★ Çok memnun kaldık" Elif K. - İstanbul "Doğrulanmış yorum" (metin: "Kızım bayıldı, her gece yıldızları yak diyor…").
8. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Product_infographic_unboxing_layout_202609012143.jpg?v=1788288406
   Kutu afişi: "KUTUDAN NE ÇIKIYOR?" Galaksi Projektör · 12 Adet Tema Diski · USB-C Güç Kablosu · Kullanım Kılavuzu · Premium Ürün Kutusu.

### Bölüm sırası

Tam id biçimi: şablon bölümleri `shopify-section-template--28025597362404__<anahtar>`, global bölümler `shopify-section-sections--28025597690084__<anahtar>` (altbilgi `…28025597657316__footer`).

1. `custom_liquid_XWzNR9` — Üst geri sayım şeridi (global): "Bugüne Özel %20 İndirim" + sayaç
2. `header` — Başlık (global): menü, logo, arama, sepet
3. `announcement_bar_m7VX6j` — Duyuru şeridi: Kredi Kartı ile Yapılan Alışverişlerde Aynı Gün Kargo
4. `main` — **Ana ürün bölümü** (galeri 8 görsel), blok sırası:
   - Puan satırı: 4.7 ( 2467 Onaylı Kullanıcı Yorumu)
   - Canlı izleyici sayacı: 45 kişi şu anda bu ürünü inceliyor. · 🚀 3 günde 399 Adet satıldı · 🚨 Son 10 Günün en düşük fiyatı · 📦 Kargo Bedava
   - Başlık: Ayluna Galaksi Night Projektör
   - Özellik başlığı: ✨ Sihirli Özellikler ✨ · Odanın tavanı her gece yeni bir gökyüzü
   - Özellik kartları: 153.748 Yıldız · Gerçek gökyüzü derinliği · 7 Katmanlı Lens · Net ve keskin projeksiyon · 5K Ultra HD Diskler · Her gece yeni bir hayal · 130 m² Yansıtma · Odanın tamamını kaplar · Kesintisiz Kullanım · Şarj derdi yok, gece boyu açık · Göz Yormayan Işık · Yumuşak gece modu · ✨ Gerçek Bir Galaksi Artık Odasında · Işığı yakın, o gülümsemeyi izleyin
   - Paket teklifi (Kaching) + satın al butonları: Çok Al Az Öde · 1 Adet · %20 İndirim · 2,199.00TL · 2,999.00TL · + Yıldız Işığı Nemlendirici %20 İndirimli · 680.00TL · 1,099.00TL · En Çok Tercih Edilen · 2 Adet · %25 İndirimli · 3,499.99TL · 5,998.00TL · + Yıldız Işığı Nemlendirici %20 İndirimli · 680.00TL · 1,099.00TL · GÜVENLİ ÖDEME İLE AL · Kapıda Ödeme ile Sipariş Ver
   - Ödeme logoları: Amex, Diners, Discover, JCB, Mastercard, Visa
   - Teslimat zaman çizelgesi: 18 Ekm · Siparişiniz Oluşturuldu · 19 Ekm - 20 Ekm · Kargonuz Hazırlandı · 21 Ekm - 23 Ekm · Evinize Teslim Edildi
   - Teslim tahmini kutusu (il seçimli): 18 saat 32 dakika içinde sipariş verirsen yarın kargoda! · Tahmini Teslim: · Adresini seç, teslim tarihini öğren! · Konum Seç · 1. ADIM · İL SEÇ · Süreler iş günü üzerinden hesaplanır; pazar ve resmî tatiller sayılmaz. Yoğun dönem ve hava koşullarında değişebi …
   - Güven şeridi: 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi
   - Yapışkan sepet çubuğu: Ayluna Galaksi Night Projektör · 2,199.00TL · 2,999.00TL · Sepete Ekle
   - SSS (ana bölüm içinde): sorular aşağıdaki SSS listesinde
5. `custom_liquid_nyxFab` — Özel Liquid: GERÇEK KULLANICILAR · GERÇEK VİDEOLAR · Sizden Gelenler · Ayluna'yı odasına taşıyanlardan üç kısa video ✨ · Ses için dokun · ✨ · 2.400+ · onaylı kullanıcı yorumu · · · 4,7/5 · ortalama puan
6. `rich_text_QnJHN8` — Zengin metin: Neden En İyisi? · Tüm özellikleri görmek için aşağı kaydır
7. `image_with_text_NABifj` — Görsel + metin + buton: Çok katmanlı HD lenslerle geliştirilmiş · Galaxy projektörlerimiz; 6 adet yüksek şeffaflığa sahip optik lens ve 2M’e kadar çözünürlük sunar. Ayrıca 5K Ultra HD disklerimizle eşleştirildiğinde, evinizin konforunda evrenin hayranlık uyandıran harikalarını artık yakından deneyimleyebilirsiniz!
8. `custom_liquid_xGpXUf` — Özel Liquid: SİZDEN GELEN MESAJLAR · Bizi Değil Kullanıcılarımızı Dinleyin · Gün boyu konfor deneyimleyen kullanıcılarımızdan gerçek geri bildirimler. · Mesajlar, müşterilerimizin izniyle paylaşılan · gerçek sohbetlerdir. [8 görsel: imgi_13_saaaaaaaaaaaa_4.png, imgi_17_Adsiz_tasarim_31.png, imgi_12_Adsiz_tasarim_48.png …]
9. `collage_xHBJ9H` — Kolaj: Evinin Her Duvarında [3 görsel: 3.3_9265950b-1b84-488b-b692-7d67b40b16ae.webp, 3.1_44cc1a31-423a-4f44-ac67-e3f9f3e45592.webp, 3.2_32b2c821-6034-4ebf-8f74-a289651428cf.webp]
10. `slideshow_JQwNaH` — Slayt gösterisi: Anksiyete Giderici · Simüle edilmiş doğal ortamlara maruz kalmak kortizol seviyelerini düşürebilir ve sakinlik ve refah hissini artırabilir. · Zihinsel Sıfırlama · Araştırmalar, sürükleyici yıldızlı gökyüzü gibi büyüleyici görsellere sahip ortamların odaklanmayı canlandırmaya, stresi azaltmaya ve zihinsel iyileşmeyi desteklemeye yardımcı olduğunu göstermektedir. · Daha iyi uyku kalitesi · Yenileyici ortamlara tekrar … [3 görsel: 3.1.webp, 3.2.webp, 3.3.webp]
11. `section_divider_zHFAHg` — Ayraç
12. `section_divider_8nqGY7` — Ayraç
13. `8beb6911-28c6-482c-976a-e5421ad3e8df` — Özellik satırları (4 başlık + görsel): Gerçek Galaksi Diskleri · 5K Ultra HD disklerle otantik uzay görsellerini evine taşı. Her sahne; doku, derinlik ve yıldız detaylarıyla gerçek bir planetaryum hissi verir. · 12 Katmanlı Optik Lens, Ultra Net Projeksiyon · 12 adet yüksek iletimli optik lens sayesinde daha net, daha keskin ve daha temiz bir görüntü. Işık efektinden değil, gerçek projeksiyon kalitesinden gelen premium bir deneyim. · 153.748 Yıldız Detayı … [1 görsel: Product_infographic_unboxing_layout_20260901…]
14. `image_with_text_8UNBF8` — Görsel + metin + buton: Ambiyans Bizim İşimiz · Ayluna, ailesi olarak en son teknoloji ürünleri terchi ettiğimizi belirtmek isteriz. Son teknoloji projeksiyon çipimiz sayesinde mükemmel yansıtma gücü sağlar. · Ayluna Galaksi Night Projektör [1 görsel: hf_20260225_185821_69ebd7bc-de68-47ea-a538-0…]
15. `custom_liquid_pxXnTb` — Özel Liquid: SSS, 12 soru (aşağıda)
16. `b321ab88-2b59-4dba-bade-54885c874ca5` — Ayraç
17. `17694466126b1e0319` — Loox yorum uygulaması (iframe; ayrıntı aşağıda)
18. `footer` — Altbilgi (global): %5 indirim için e-posta aboneliği, ödeme logoları, politikalar

### Paket teklifi, geri sayım, kargo

- **Paket (Kaching):** Çok Al Az Öde · 1 Adet · %20 İndirim · 2,199.00TL · 2,999.00TL · + Yıldız Işığı Nemlendirici %20 İndirimli · 680.00TL · 1,099.00TL · En Çok Tercih Edilen · 2 Adet · %25 İndirimli · 3,499.99TL · 5,998.00TL · + Yıldız Işığı Nemlendirici %20 İndirimli · 680.00TL · 1,099.00TL
- **Geri sayım:** üst şerit "Bugüne Özel %20 İndirim 01 SAAT : 01 DK : 36 SAN" (her yüklemede yeniden başlar)
- **Teslim tahmini:** 18 saat 32 dakika içinde sipariş verirsen yarın kargoda! · Tahmini Teslim: · Adresini seç, teslim tarihini öğren! · Konum Seç · 1. ADIM · İL SEÇ · Süreler iş günü üzerinden hesaplanır; pazar ve resmî …
- **Duyuru şeridi:** Kredi Kartı ile Yapılan Alışverişlerde Aynı Gün Kargo
- **Güven şeridi:** 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi

### SSS

**Kaynak: `main`**

- **Bu ürün ne işe yarıyor?** Ayluna Galaksi Night Projektör, odanın duvarına ve tavanına gerçek uzay görselleri yansıtır. Gece lambası gibi yumuşak bir ışık verirken, aynı zamanda küçük bir planetaryum atmosferi oluşturur. Çocuk odasında uyku rutinini kolaylaştırmak, yatak odasında rahatl …
- **Nasıl çalışıyor, kurulumu zor mu?** Kurulum gerektirmez. Kutudan çıkarın, kabloyu takın, istediğiniz diski yerleştirin ve açın. Cihazı düz bir yüzeye koyun Yansıtma başlığını duvara veya tavana doğru çevirin Diski yuvasına yerleştirin Tuşlarla açın ve netliği ayarlayın Uygulama, hesap veya inter …
- **Şarjlı mı, kabloyla mı çalışıyor?** Ürün kabloyla çalışır, şarjlı değildir. Kutudan çıkan kabloyu takıp kullanmaya başlarsınız. Bunun en büyük avantajı şu: pil bitmez. Şarjlı modellerde en sık yaşanan sorun, cihazın gecenin ortasında kapanmasıdır. Kablolu kullanımda projeksiyon sabah olana kadar …
- **Gece boyunca açık kalabilir mi?** Evet. LED ışık kaynağı düşük ısı üretir ve uzun süreli kullanıma uygundur. Sabit güç aldığı için gece boyunca aynı parlaklıkta çalışır. Yine de her elektrikli üründe olduğu gibi, uzun süre yanınızda olmadığınız durumlarda kapatmanızı öneririz.
- **Işık çocuğun gözünü yorar mı?** Hayır. Işık doğrudan göze değil, duvara ve tavana yansıtılacak şekilde tasarlanmıştır. Yansıyan görüntü yumuşaktır ve keskin parlaklık oluşturmaz. En rahat kullanım için: Cihazı yatağın karşısına değil, yan tarafına konumlandırın Yansıtmayı tavana yönlendirin …
- **Kaç yaşından itibaren uygun?** Her yaş grubunun odasında kullanılabilir. Ancak tema diskleri küçük parça olduğu için, 3 yaş altındaki çocuklarda ebeveyn gözetimi gerekir. Cihazı ve kabloyu çocuğun uzanamayacağı bir yere, düz ve sağlam bir zemine yerleştirin.
- **Ne kadar alana yansıtıyor?** Cihazın duvara olan mesafesine göre yansıtma alanı büyür. Standart bir çocuk odasında tavanın tamamını rahatlıkla kaplar. Daha büyük bir görüntü için cihazı duvardan uzaklaştırın, daha yoğun ve parlak bir görüntü için yaklaştırın. En iyi sonuç için odayı karar …
- **Diskleri nasıl değiştiriyorum?** Diskler yansıtma başlığındaki yuvaya elle takılıp çıkarılır, alet gerektirmez. Birkaç saniyede değiştirebilirsiniz. Her disk farklı bir gökyüzü sahnesi içerir, böylece her gece odada başka bir manzara olur. Diskleri kullanmadığınızda kutusunda saklamanızı öner …
- **Kutu içeriğinde neler var?** Ayluna Galaksi Night Projektör Tema diskleri Bağlantı kablosu Kullanım kılavuzu Premium ürün kutusu Ürün kutudan çıktığı gibi kullanıma hazırdır, ayrıca bir şey satın almanız gerekmez.
- **Görüntü bulanık çıkıyor, ne yapmalıyım?** Neredeyse her zaman basit bir ayar meselesidir: Netlik halkasını yavaşça çevirerek odaklamayı ayarlayın Cihazın mesafesini biraz değiştirin Diskin yuvaya tam oturduğundan emin olun Lensi ve diski yumuşak bir bezle silin Odayı tamamen karartın; ortam ışığı netl …
- **Gece rutinine nasıl entegre ederim?** En iyi sonucu veren yöntem, projektörü rutinin başlangıç işareti yapmaktır. Çocuk "yıldızlar yanınca yatma vakti geldi" bağlantısını hızlıca kurar. Yatmadan 20 dakika önce odanın ana ışığını kapatın Projektörü açın ve diski birlikte seçin Yansıyan sahne üzerin …
- **Kargo ve iade nasıl işliyor?** Kredi kartı ile verilen siparişler aynı gün kargoya teslim edilir. Kargo ücretsizdir. Ürünle ilgili 1 yıl garanti ve 90 gün para iade güvencesi sunuyoruz. Memnun kalmazsanız süre içinde iade edebilirsiniz.

- *`custom_liquid_pxXnTb` bölümü yukarıdaki soruların aynısı (tekrar).*

### Yorumlar

- **Sayfada yazan:** "4.7 (2467 Onaylı Kullanıcı Yorumu)" (sabit metin)
- **Loox gerçek:** 6 yorum, ortalama 5.0 (dağılım: 5★×6); ilk 20 yorumun tarihleri: 27.03.2026 ×1, 28.02.2026 ×5; "Doğrulanmış" etiketi: 6
- **Loox örnek:** "Cok begendim.3 adet daha siparis verdim" / "Yegenime hediye olarak aldim. 12 farkli goruntu var ve tahmin ettigimden cok daha gercekci , cok begendim.Ayrica hizli kargo icin cok tesekk …" / "kizima hediye aldim çözünürlük guzel yavas yavas donmesi ayri Hava katiyor sessizligi de guzel tek eksik prize takili olmasi gerekli keşke ş …" / "ürün çok güzel. renkleri de çok iyiydi çocuklarla bayildik. Ay ile birlikte toplam 13 adet var. aynı zamanda yavas hareket de ediyor. sesli …"

### Açıklama (body_html)

- Boş. Ürün metni yalnız tema bölümlerinde.

### Sorunlu iddialar

- **Sağlık (kritik):** Slayt bölümü: "Anksiyete Giderici… kortizol seviyelerini düşürebilir", "Zihinsel Sıfırlama… Araştırmalar… stresi azaltmaya ve zihinsel iyileşmeyi desteklemeye", "Daha iyi uyku kalitesi… sirkadiyen ritimlerin iyileşmesine ve daha derin bir uykuya yol açar". Ayrıca "Göz yormayan ışık".
- **Teyitsiz teknik:** Lens sayısı üç farklı: "12 katmanlı" (görsel 1, 4, özellik satırı), "7 Katmanlı Lens" (özellik kartı), "6 adet optik lens ve 2M'e kadar çözünürlük" (görsel+metin). "5K Ultra HD", "153.748 yıldız", "130 m²", "Planetaryum Kalitesi".
- **Kutu / güç çelişkisi:** Görsel 1 "Şarjlı ve kablosuz" ↔ SSS "kabloyla çalışır, şarjlı değildir" ↔ gerçek yorum "keşke şarjlı olsaydı". "12 disk" ↔ gerçek yorum "Ay ile birlikte toplam 13 adet".
- **Uydurma puan / yorum:** Sayfa "4.7 (2467)" ve "2.400+ onaylı kullanıcı yorumu · 4,7/5"; Loox 6 yorum (5.0, Doğrulanmış). Görsel 7 "Elif K. Doğrulanmış yorum" kartı uydurma. "SİZDEN GELEN MESAJLAR… gerçek sohbetlerdir" başka ürünlerin sohbetleri.
- **Uydurma satış:** "🚀 3 günde 399 Adet satıldı", "🚨 Son 10 Günün en düşük fiyatı".
- **İade:** SSS ve şerit "90 gün para iade güvencesi".
- **Fiyat etiketi:** Paket: "%20" (gerçek %26,7), "2 Adet %25" (gerçek %41,6), ek ürün "%20 İndirimli" (gerçek %38).

---

## 8. Aroma Terapi Nemlendirici — `aroma-terapi-nemlendirici`

- **Adres:** https://ayluna.shop/products/aroma-terapi-nemlendirici
- **Fiyat:** 1.499,00 TL · karşılaştırma: 1.999,00 TL → gerçek indirim %25.0
- **Varyantlar** (Title): Default Title — 1.499,00 TL — TÜKENDİ
- **Şablon:** `template--28025597395172` · sayfa yüksekliği 7603 px · vendor: Ayluna
- **Ekran görüntüleri** (8 parça, klasör `…/scratchpad/site/urun/`): `aroma-terapi-nemlendirici-1.png`, `aroma-terapi-nemlendirici-2.png`, `aroma-terapi-nemlendirici-3.png`, `aroma-terapi-nemlendirici-4.png`, `aroma-terapi-nemlendirici-5.png`, `aroma-terapi-nemlendirici-6.png`, `aroma-terapi-nemlendirici-7.png`, `aroma-terapi-nemlendirici-8.png`
- Ürün tükendi.
- Özellik bloğu ayrı bir özel tasarım ("ayluna-bonfire-wrap", 6 kart).

### Görseller (7)

1. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260220_182854_ee737255-f473-4745-8844-055529745da8.jpg?v=1771612404
   Yaşam + afiş (salon): "EVİNİN MODUNU 30 SANİYEDE DEĞİŞTİR · Alev efekti + nem + aroma… tek cihazda." 280 ML · Zamanlayıcı · Uzaktan Kumanda.
2. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260220_182951_c1b28ce6-ff3f-4329-b92d-62fd6345eb6e.jpg?v=1771612403
   Yaşam + afiş (yatak odası): "GECE RUTİNİNİN EN SAKİN PARÇASI · Sessiz çalışma • Nem • Aroma" LED Modları · Zamanlayıcı · 280 ML.
3. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260220_183040_36dc4b01-f741-42e1-82c5-98453b01c87b.jpg?v=1771612503
   Yaşam + afiş: "TEK CİHAZDA 3 ETKİ · Alev ambiyansı • Nem • Aroma" 280 ML su haznesi · Sessiz çalışma · 2 kademe buhar.
4. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260220_183009_9ca3a1a0-d178-43ea-bcd6-d1a2edebc790.jpg?v=1771612503
   Yaşam + afiş: "TEK TUŞLA KONTROL" Uzaktan Kumanda · Zamanlayıcı · Buhar Seviyesi (kumanda görünüyor).
5. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260220_183019_f7b3d984-c9e2-4712-9103-0707309b1359.jpg?v=1771612503
   Afiş: "LED IŞIK MODLARI · Ambiyansı tek tuşla değiştir." 6 renk paneli.
6. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260220_183027_40e66230-467f-40b0-b636-e3fc1885e45f.jpg?v=1771612503
   Yorum afişi "Müşteri Yorumları": 4 kart (Ayşe K., Zeynep D., Elif K., Sude Y.) 5 yıldız + "Doğrulanmış Müşteri".
7. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260220_183132_8b680953-e832-493e-9563-06b1fec0e6cd.jpg?v=1771612503
   Yaşam + afiş: "EVİNE SICAKLIK KAT · Şömine hissi + aromaterapi, tek dokunuşta." Dekoratif Tasarım · Hediye İçin İdeal.

### Bölüm sırası

Tam id biçimi: şablon bölümleri `shopify-section-template--28025597395172__<anahtar>`, global bölümler `shopify-section-sections--28025597690084__<anahtar>` (altbilgi `…28025597657316__footer`).

1. `custom_liquid_XWzNR9` — Üst geri sayım şeridi (global): "Bugüne Özel %20 İndirim" + sayaç
2. `header` — Başlık (global): menü, logo, arama, sepet
3. `announcement_bar_m7VX6j` — Duyuru şeridi: Kredi Kartı İle Yapılan Alışverişler Aynı Gün Kargoya verilir. ✨
4. `main` — **Ana ürün bölümü** (galeri 7 görsel), blok sırası:
   - Başlık: Aroma Terapi Nemlendirici
   - Puan satırı: 4.7 ( 2467 Onaylı Kullanıcı Yorumu)
   - Özellik kartları: ✨ Premium Özellikler ✨ · Tek dokunuşla alev ambiyansı, nem ve aroma · Şömine Alev Efekti (Ambiyans) · Ultrasonik Nem (İnce Buhar) · Uzaktan Kumanda ile Kontrol · Zamanlayıcı Modu · LED Işık Modları · Aroma Difüzör (Koku)
   - Canlı izleyici sayacı: 39 kişi şu anda bu ürünü inceliyor.
   - Kargo notu: KREDİ KARTI İLE VERİLEN ŞİPARİŞLER HIZLI KARGO İLE ÇIKARTILMAKTADIR
   - Paket teklifi (Kaching) + satın al butonları: Çok Al Az Öde · 1 Adet · %25 İndirim · 1,499.00TL · 1,999.00TL · En Çok Tercih Edilen · 2 Adet · %35 İndirim · 2,499.99TL · 3,998.00TL · TÜKENDİ · Tükendi
   - Ödeme logoları: Amex, Diners, Discover, JCB, Mastercard, Visa
   - Teslimat zaman çizelgesi: 18 Ekm · Siparişiniz Oluşturuldu · 19 Ekm - 20 Ekm · Kargonuz Hazırlandı · 21 Ekm - 23 Ekm · Evinize Teslim Edildi
   - Güven şeridi: 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi
   - Yapışkan sepet çubuğu: Aroma Terapi Nemlendirici · 1,499.00TL · 1,999.00TL · Tükendi
   - Kısa yorum kaydırıcısı (3 yorum): Eşim bayıldı 💙 Her gece ışığında kahve yapıp gelecek planarımızı konuşuyoruz gecemizi romantize ediyoruz. · Elif K. · En büyük artısı ortamı bir anda sakinleştirmesi. · Gülsüm S. · Hediye aldım, alan kişi aşık oldu 🎁 Temalar çok güzel, odanın havasını değiştiriyor. Işık göz yormuyor; gece boyunca açık kalsa bile rahatsız etmiyor. · Zeynep R.
   - Açılır soru: Alev efekti gerçek ateş mi? Güvenli mi?
   - Açılır soru: Bu ürün ne işe yarıyor?
   - Açılır soru: Buhar (mist) nasıl çalışıyor? Ultrasonik ne demek?
   - Açılır soru: Hangi modlar var? LED ışık renkleri nasıl değişiyor?
   - Açılır soru: Zamanlayıcı nasıl kullanılır?
   - Açılır soru: Uzaktan kumanda neyi kontrol ediyor?
   - Açılır soru: 280 ml hazne ne kadar süre gider?
   - Açılır soru: Esansiyel yağ kullanabilir miyim?
   - Açılır soru: Neden buhar çıkmıyor? Ne yapmalıyım?
5. `section_divider_ARXJ86` — Ayraç
6. `section_divider_qmrTwn` — Ayraç
7. `eba88da5-80ac-47fc-aa75-997cfe7b2e59` — Yorum ekran görüntüsü kaydırıcısı: +2000 Mutlu Annenin söylediklerini okuyun [16 görsel: imgi_22_saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa…, imgi_15_saaaaaaaaaaaa_6.png, imgi_16_Adsiz_tasarim_36.png …]
8. `horizontal_ticker_rbYQET` — Kayan şerit: Ücretsiz Kargo 📦 · 6 Farklı Renk Modu ✨ · Yetişkinlere Özel ❤️
9. `image_banner_Ae7wdz` — GIF afiş + başlık: Evinin bir köşesinde HUZUR olsun · EVİNİ GÜZELLETİRMEK SENİN ELİNDE KENDİNİ ŞIMART [1 görsel: 2_Ocak_20_5_1.gif]
10. `8beb6911-28c6-482c-976a-e5421ad3e8df` — Özellik satırları (4 başlık + görsel): Şömine Alev Efekti ile Ambiyans · Gerçek ateş olmadan, LED + buhar birleşimiyle şömine hissi verir. Salon, yatak odası ya da çalışma alanında tek dokunuşla Mükemmel atmosfer. · Ultrasonik Nemlendirme (İnce Buhar) · Ultrasonik teknoloji ile suyu ince buhara çevirir, ortamın havasını yumuşatır. Kuru hava hissini azaltmaya yardımcı olur; gece kullanımına uygundur. · Uzaktan Kumanda ile Kolay Kontrol · Işık modu, buhar s … [1 görsel: hf_20260220_171133_a3f73111-fcd7-417a-8052-1…]
11. `image_with_text_8UNBF8` — Görsel + metin + buton: Geceyi Sakinleştir, Ortamı Yumuşat · Ayluna, Bir yanda gerçekçi alev ambiyansı, diğer yanda ince buharla ferah bir hava. · Birkaç damla aroma ile oda “spa” gibi olur. · Zamanlayıcıyı ayarla, gerisini cihaz halletsin. · Aroma Terapi Nemlendirici'yi Keşfet [1 görsel: hf_20260220_172544_2e21b09d-8817-4679-af12-e…]
12. `collapsible_content_7zjVTU` — SSS (açılır): SSS, 5 soru (aşağıda)
13. `b321ab88-2b59-4dba-bade-54885c874ca5` — Ayraç
14. `17694466126b1e0319` — Loox yorum uygulaması (iframe; ayrıntı aşağıda)
15. `footer` — Altbilgi (global): %5 indirim için e-posta aboneliği, ödeme logoları, politikalar

### Paket teklifi, geri sayım, kargo

- **Paket (Kaching):** Çok Al Az Öde · 1 Adet · %25 İndirim · 1,499.00TL · 1,999.00TL · En Çok Tercih Edilen · 2 Adet · %35 İndirim · 2,499.99TL · 3,998.00TL
- **Geri sayım:** üst şerit "Bugüne Özel %20 İndirim 01 SAAT : 01 DK : 38 SAN" (her yüklemede yeniden başlar)
- **Duyuru şeridi:** Kredi Kartı İle Yapılan Alışverişler Aynı Gün Kargoya verilir. ✨
- **Güven şeridi:** 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi

### SSS

**Kaynak: `main`**

- **Alev efekti gerçek ateş mi? Güvenli mi?** Hayır, gerçek ateş değildir. Ultrasonik buhar ve LED ışık kombinasyonu ile oluşturulan gerçekçi bir alev efekti vardır. Isınma yapmaz, yanma riski oluşturmaz ve gece kullanımı için güvenlidir.
- **Hangi modlar var? LED ışık renkleri nasıl değişiyor?** Farklı alev ışık modları ve ortam ışığı seçenekleri bulunur. Işık modlarını cihaz üzerinden veya kumanda ile kolayca değiştirerek ortama uygun ambiyansı ayarlayabilirsiniz.
- **Buhar (mist) nasıl çalışıyor? Ultrasonik ne demek?** Ultrasonik teknoloji suyu titreştirerek ince, soğuk buhar üretir. Bu sayede ortamı sessizce nemlendirir, ısı oluşturmaz ve gece kullanımı için ideal bir yumuşak mist sağlar.
- **Zamanlayıcı nasıl kullanılır?** Zamanlayıcı özelliği sayesinde cihazı belirli süre sonra otomatik kapanacak şekilde ayarlayabilirsiniz. Bu özellik özellikle gece kullanımında pratik ve güvenli bir deneyim sağlar.
- **Bu ürün ne işe yarıyor?** Ortam havasını nemlendirir, esansiyel yağ ile hoş bir koku yayar ve şömine alev efekti sayesinde odada sakin, premium bir ambiyans oluşturur. Tek cihazda hem dekor hem konfor sunar.
- **Uzaktan kumanda neyi kontrol ediyor?** Uzaktan kumanda ile alev efekti, ışık modları, buhar seviyesi ve zamanlayıcı ayarlarını oturduğunuz yerden kolayca kontrol edebilirsiniz.
- **280 ml hazne ne kadar süre gider?** 280 ml su haznesi kullanım moduna göre ortalama birkaç saat kesintisiz çalışır. Düşük modda daha uzun süre nem ve ambiyans sağlar.

**Kaynak: `collapsible_content_7zjVTU`**

- **Neden buhar çıkmıyor? Ne yapmalıyım?** Öncelikle haznede yeterli su olduğundan emin olun. Pamuk fitilin doğru yerleştiğini ve cihazın düz zeminde olduğunu kontrol edin. İlk kullanımda fitilin tamamen ıslanması için 1-2 dakika beklemek gerekebilir.
- **Kutu içeriğinde neler var?** Kutu içerisinde alev efektli nemlendirici cihaz, uzaktan kumanda, USB güç kablosu ve kullanım kılavuzu bulunmaktadır.
- **Temizliği ve bakımı nasıl yapılır?** Haftada 1 kez hazneyi temiz su ile durulamanız önerilir. Kireç oluşumunu önlemek için mümkünse içme suyu veya arıtılmış su kullanılması cihaz ömrünü uzatır.
- **Gece kullanımı uygun mu? Ses yapar mı?** Ultra sessiz çalışma teknolojisine sahiptir. Yumuşak ışığı göz yormaz, sakin bir atmosfer oluşturur ve gece rutini ile uyumlu şekilde rahat kullanım sunar.
- **Gece kullanımında göz yorar mı?** Uyku için tasarlanan yumuşak ışık modunda rahatsız etmez. En iyi deneyim için:Parlaklığı orta/düşük kullanın,Işığı doğrudan göze değil, duvara/tavana yansıtın.


### Yorumlar

- **Sayfada yazan:** "4.7 (2467 Onaylı Kullanıcı Yorumu)" (sabit metin)
- **Loox gerçek:** 6 yorum, ortalama 5.0 (dağılım: 5★×6); ilk 20 yorumun tarihleri: 20.02.2026 ×6; "Doğrulanmış" etiketi: 0
- **Loox örnek:** "On numara kızlar sevilime aldım çok sevdi" / "Alev gibi görünüyor ama efsaaneee" / "güvenerek alabilirsiniz hızlı kargo ile ertesi gün elime geldi"

### Açıklama (body_html)

- Boş. Ürün metni yalnız tema bölümlerinde.

### Sorunlu iddialar

- **Sağlık:** Ad "Aroma Terapi"; "aromaterapi", "oda spa gibi olur", "Kuru hava hissini azaltmaya yardımcı olur".
- **Güvenlik iddiası:** "Isınma yapmaz, yanma riski oluşturmaz ve gece kullanımı için güvenlidir", "Ultra sessiz çalışma teknolojisi".
- **Uydurma yorum:** Görsel 6: 4 kart "Doğrulanmış Müşteri". Loox 6 yorum, 5.0, hepsi 20.02.2026, "Doğrulanmış" yok. Sayfa "4.7 (2467)".
- **Kopya içerik:** "+2000 Mutlu Annenin" (şeritte "Yetişkinlere Özel"); SSS "Işığı doğrudan göze değil, duvara/tavana yansıtın" (projektör SSS'si); yorum "Temalar çok güzel".
- **Teyitsiz teknik:** 280 ml, 2 kademe buhar, 6 renk.
- **İade:** "90 Gün Para İade Garantisi".

---

## 9. Galaksi Ambiyans Işığı — `galaksiambiyanisigi`

- **Adres:** https://ayluna.shop/products/galaksiambiyanisigi
- **Fiyat:** 1.499,00 TL · karşılaştırma: 2.898,00 TL → gerçek indirim %48.3
- **Varyantlar** (Title): Default Title — 1.499,00 TL — satışta
- **Şablon:** `template--28025597133028` · sayfa yüksekliği 9584 px · vendor: Ayluna
- **Ekran görüntüleri** (10 parça, klasör `…/scratchpad/site/urun/`): `galaksiambiyanisigi-1.png`, `galaksiambiyanisigi-2.png`, `galaksiambiyanisigi-3.png`, `galaksiambiyanisigi-4.png`, `galaksiambiyanisigi-5.png`, `galaksiambiyanisigi-6.png`, `galaksiambiyanisigi-7.png`, `galaksiambiyanisigi-8.png`, `galaksiambiyanisigi-9.png`, `galaksiambiyanisigi-10.png`
- Yapışkan sepet butonu İngilizce: "Add to cart".
- Paket teklifinde ek ürün: Ayluna AyFeneri.

### Görseller (7)

1. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260216_184339_38775b04-d940-4bc4-9b97-dbdc26c9d678.png?v=1771268652
   Yaşam + afiş (yatak odası): "GECEYİ GALAKSİYE ÇEVİR · Yıldız & nebula projeksiyonuyla" 14 RENK • 4 HIZ • KUMANDALI · ŞİMDİ KEŞFET.
2. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260216_184935_f53bccff-394e-4d91-955a-c5f4b4fa9cf5.png?v=1771268652
   Kutu afişi (yatak üstü): "KUTUDAN ÇIKANLAR" Galaxy projeksiyon lamba · Uzaktan kumanda · Kablo + kullanım kılavuzu · "2 YIL GARANTİ" · kutuda "Galaxy Nightlight Projector".
3. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260216_185751_12d02b66-877b-4f30-b897-c6c2e09edd7e.png?v=1771268652
   Yaşam + afiş (çocuk odası): "14 RENK SEÇENEĞİ · Her gece farklı bir atmosfer." Tek tuşla değiştir • Kumandayla kontrol.
4. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260216_185913_55c12a55-dc69-46aa-85ef-eea2d1423365.png?v=1771268652
   Yaşam + afiş: "MÜZİĞİ AÇ, IŞIĞI AÇ · Bluetooth hoparlör + rahatlatıcı ambiyans" Bluetooth ile bağlan · Ninni & sakinleştirici müzik · Uyku rutini yardımcı.
5. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260216_191136_20f2c63f-c4a7-465a-9d54-7654738fd381.png?v=1771269366
   Yorum kartı: Sude Y. "Doğrulanmış Alıcı" 5/5 "Sevgilime hediye aldım… göz yormuyor".
6. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260216_190106_f1f81c43-ec13-497f-8280-fe538beed972.png?v=1771269366
   Yaşam (eller, hediye paketi): "HEDİYEYE HAZIR · Sıcak ambiyansla anında etki." Yumuşak ambiyans · Projeksiyon · Sevdiklerine özel.
7. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260216_190115_74e5ece9-0db7-4f2f-8c0e-572199d4291c.png?v=1771269366
   "GERÇEK YORUMLAR": 8 Instagram tarzı yorum kartı (Elif K., Merve A., Zeynep D., Sude Y. ×2, Kübra Ş., İrem Ç.); "Şarjı da fena değil".

### Bölüm sırası

Tam id biçimi: şablon bölümleri `shopify-section-template--28025597133028__<anahtar>`, global bölümler `shopify-section-sections--28025597690084__<anahtar>` (altbilgi `…28025597657316__footer`).

1. `custom_liquid_XWzNR9` — Üst geri sayım şeridi (global): "Bugüne Özel %20 İndirim" + sayaç
2. `header` — Başlık (global): menü, logo, arama, sepet
3. `announcement_bar_m7VX6j` — Duyuru şeridi: Evinde kendi huzur köşeni oluştur✨
4. `main` — **Ana ürün bölümü** (galeri 7 görsel), blok sırası:
   - Başlık: Galaksi Ambiyans Işığı
   - Puan satırı: 4.7 ( 2467 Onaylı Kullanıcı Yorumu)
   - Fiyat satırı: 1.499,00 TL · 2.898,00 TL üstü çizili · rozet "%50 İndirim"
   - Özellik başlığı: ✨ Ürün Özellikleri ✨ · Odanızı Hayal Dünyanıza Çevirin
   - Özellik kartları: Uyku Dostu Yumuşak Işık · 14 Farklı renk ve Projeksiyon · Bluetooth Müzik-PodCast Hoparlörü · Şarjlı ve Kablosuz Kullanım · Odanızı Huzurla Doldurun Diye %50 İndirimli!
   - Canlı izleyici sayacı: 43 kişi şu anda bu ürünü inceliyor.
   - Kargo notu: TÜM SİPARİŞLER HIZLI KARGO İLE ÇIKARTILMAKTADIR
   - Paket teklifi (Kaching) + satın al butonları: Sınırlı süreli teklif · 1 Adet · %50 İndirim · 1,499.00TL · 2,898.00TL · 2 Adet · İkincisi %50 İndirimli · 2,174.99TL · 5,796.00TL · Ayluna AyFeneri · 1,179.00TL İndirim! · 1,320.00TL · 2,499.00TL · GÜVENLİ ÖDEME İLE AL · Kapıda Ödeme ile Sipariş Ver
   - Ödeme logoları: Amex, Diners, Discover, JCB, Mastercard, Visa
   - Teslimat zaman çizelgesi: 18 Ekm · Siparişiniz Oluşturuldu · 19 Ekm - 20 Ekm · Kargonuz Hazırlandı · 21 Ekm - 23 Ekm · Evinize Teslim Edildi
   - Güven şeridi: 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi
   - Yapışkan sepet çubuğu: Galaksi Ambiyans Işığı · 1,499.00TL · 2,898.00TL · Add to cart
   - Kısa yorum kaydırıcısı (3 yorum): Eşim bayıldı 💙 Her gece yıldızları yak diye tutturuyor. Işık yumuşacık, uykuya geçişimiz inanılmaz kolaylaştı. · Elif K. · En büyük artısı ortamı bir anda sakinleştirmesi. Bluetooth’tan Müzik açıp uyumak rutin haline geldi · Gülsüm S. · Hediye aldım, alan kişi de çocuk da aşık oldu 🎁 Temalar çok güzel, odanın havasını değiştiriyor. Işık göz yormuyor; gece boyunca açık kalsa bile rahatsız etmiyor. · Zeynep R.
   - Açılır soru: Gece rutinine nasıl entegre ederim?
   - Açılır soru: Bu ürün ne işe yarıyor?
   - Açılır soru: Projeksiyon nasıl çalışıyor?
   - Açılır soru: Hoparlör olarak kullanabilir miyim ?
   - Açılır soru: Bluetooth var mı, ne işe yarıyor?
   - Açılır soru: Parlaklığı rahatsız eder mi?
   - Açılır soru: Kutu içeriğinde neler var?
   - Açılır soru: Bluetooth bağlanmıyor, ne yapmalıyım?
5. `section_divider_ARXJ86` — Ayraç
6. `section_divider_qmrTwn` — Ayraç
7. `eba88da5-80ac-47fc-aa75-997cfe7b2e59` — Yorum ekran görüntüsü kaydırıcısı: +2000 Mutlu Müşterimizin söylediklerini okuyun [16 görsel: imgi_22_saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa…, imgi_15_saaaaaaaaaaaa_6.png, imgi_16_Adsiz_tasarim_36.png …]
8. `horizontal_ticker_rbYQET` — Kayan şerit: Ücretsiz Kargo 📦 · 14 Farklı Renk ✨ · Huzur artık odanda 🛋️
9. `image_banner_Ae7wdz` — GIF afiş + başlık: Günün Yorgunluğu Evde Atılır · BÜTÜN GÜNÜN YORGUNLUĞU EVİNDE HOŞ BİR IŞIKTA SEVDİĞİN İNSANLA 2 SAATLİK FİLMLE GİDEBİLİR, İŞTE O ARADIĞIN HOŞ IŞIK BURADA. [1 görsel: Savetik_1771270264-ezgif.com-video-to-gif-co…]
10. `8beb6911-28c6-482c-976a-e5421ad3e8df` — Özellik satırları (4 başlık + görsel): Çeşitli Animasyon Seçenekleri · Gece lambası projektörümüz, 14 farklı animasyon seçeneği ile odanızı büyülü bir hale getirir. · Projektör ve Işık Efektleri · Gece lambası projektörü, ışık efektleri ve projeksiyonları ile odanızı aydınlatırken etkileyici bir görsel deneyim sunar. · Bluetooth Özelliği ile Müzik ve Hikaye Dinleme · Cihazı telefon veya tabletinize bağlayarak çocuğunuzun favori müziklerini veya sesli hika … [1 görsel: hf_20260216_184935_f53bccff-394e-4d91-955a-c…]
11. `image_with_text_8UNBF8` — Görsel + metin + buton: Yıldız Işığı Ambiyansı, Tek Dokunuşla · Ayluna, ailesi olarak en son teknoloji ürünleri terchi ettiğimizi belirtmek isteriz. Son teknoloji projeksiyon çipimiz sayesinde mükemmel yansıtma gücü sağlar. · Dino Lamp Ambiyans Işığını keşfet [1 görsel: hf_20260216_184339_38775b04-d940-4bc4-9b97-d…]
12. `collapsible_content_7zjVTU` — SSS (açılır): SSS, 8 soru (aşağıda)
13. `b321ab88-2b59-4dba-bade-54885c874ca5` — Ayraç
14. `17694466126b1e0319` — Loox yorum uygulaması (iframe; ayrıntı aşağıda)
15. `footer` — Altbilgi (global): %5 indirim için e-posta aboneliği, ödeme logoları, politikalar

### Paket teklifi, geri sayım, kargo

- **Paket (Kaching):** Sınırlı süreli teklif · 1 Adet · %50 İndirim · 1,499.00TL · 2,898.00TL · 2 Adet · İkincisi %50 İndirimli · 2,174.99TL · 5,796.00TL · Ayluna AyFeneri · 1,179.00TL İndirim! · 1,320.00TL · 2,499.00TL
- **Geri sayım:** üst şerit "Bugüne Özel %20 İndirim 01 SAAT : 01 DK : 36 SAN" (her yüklemede yeniden başlar)
- **Duyuru şeridi:** Evinde kendi huzur köşeni oluştur✨
- **Güven şeridi:** 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi

### SSS

**Kaynak: `main`**

- **Hoparlör olarak kullanabilir miyim ?** Tabikide evet gelişmiş uzaktan bağlantı özelliği sayesinde telefonunuzdan bağlanarak dilediğiniz müziği açabilir ve evinizin ambiyansını daha üst seviyelere çıkartabilirsiniz.
- **Bu ürün ne işe yarıyor?** Çocuğun odasını yumuşak bir gece ışığı ve projeksiyon efektleri ile daha sakin bir uyku ortamına çevirir.Ayrıca Bluetooth ile telefondan ninni müzik masal açabilirsiniz.
- **Gece rutinine nasıl entegre ederim?** Uyku öncesi 10 dakika: ışığı aç → favori temayı yansıt → telefondan kısa ninni/masal aç → aynı rutini her gece tekrarla.
- **Projeksiyon nasıl çalışıyor?** Cihazın projeksiyon modunu açıp seçtiğiniz temayı kullanarak duvar/tavan üzerine görsel yansıma alırsınız.
- **Bluetooth var mı, ne işe yarıyor?** Evet — telefon/tablete bağlayıp çocuğun sevdiği ninni, müzik veya sesli hikâyeleri çalabilirsiniz.
- **Parlaklığı rahatsız eder mi?** Tabikide hayır :)Yumuşak ambiyans için tasarlandı; gece boyunca göz yormayan kullanım hedeflendi
- **Kutu içeriğinde neler var?** Cihaz Şarj kablosu Kullanım kılavuzu

**Kaynak: `collapsible_content_7zjVTU`**

- **Bu modelde hangi özellikler var?** Bu model hareket sensörlü değildir. (Bazı modellerde sensör bulunabiliyor.) Bu üründe tüm kontrol tuşlar/kumanda üzerinden yapılır; böylece gece kullanımında daha stabil ve sürprizsiz bir deneyim sağlar.
- **Hareket sensörü nasıl çalışır?** Sensör, hareket algıladığında ışığı otomatik olarak açar. Belirli bir süre hareket algılamazsa ışık kendiliğinden kapanır. Gece koridor, yatak yanı ve çocuk odası kullanımında çok pratiktir.
- **Tuşlar ile neleri kontrol edebilirim?** Genellikle aç/kapat, ışık modu/efekti geçişi, parlaklık ayarı, projeksiyon modları, müzik ses kontrolü gibi temel işlevleri kolayca yönetebilirsiniz.
- **Bluetooth hoparlöre nasıl bağlanırım?** Ürünü açın ve Bluetooth modunu aktif edin.Telefonunuzda Bluetooth’u açın → cihaz listesinden ürünü seçin Bağlandıktan sonra Spotify/YouTube/telefonunuzdaki ninnileri doğrudan hoparlörden çalabilirsiniz.
- **Ürün şarjlı mı, prizde mi çalışır?** Ürün şarjlıdır ve kablosuz kullanılabilir. İsterseniz şarj ederken de kullanabilirsiniz (kullanım alışkanlığına göre pratiklik sağlar).
- **Şarjı ne kadar gider?** Şarj süresi; parlaklık seviyesi, projeksiyonun açık kalması, Bluetooth ses düzeyi gibi etkenlere göre değişir. Gece rutininde (orta parlaklık düşük ses) genelde birkaç saatlik kullanım sağlar.
- **Gece kullanımında göz yorar mı?** Uyku için tasarlanan yumuşak ışık modunda rahatsız etmez. En iyi deneyim için:Parlaklığı orta/düşük kullanın,Işığı doğrudan göze değil, duvara/tavana yansıtın.
- **Çocuk odasında kullanmak güvenli mi?** Evet, çocuk odası kullanımına uygundur. LED ışık düşük ısı üretir. Güvenlik için:Ürünü düz ve sağlam bir zemine koyun,Tema diskleri küçük parça olabileceği için küçük çocuklarda ebeveyn gözetimiyle kullanın,Kabloyla kullanımda kabloyu ortalıkta bırakmayın.


### Yorumlar

- **Sayfada yazan:** "4.7 (2467 Onaylı Kullanıcı Yorumu)" (sabit metin)
- **Loox gerçek:** 13 yorum, ortalama 5.0 (dağılım: 5★×13); ilk 20 yorumun tarihleri: 16.02.2026 ×13; "Doğrulanmış" etiketi: 0
- **Loox örnek:** "Çalışma odamda kullanıyorum çok güzel beğendim" / "Hediye için nokta atışı. kız arkadaşım her akşam bunu açalım diye tutturdu 😂 Kurulum 1 dakika, uğraştırmıyor" / "Fotoğraftan daha şık duruyor. Işık göz yormuyor, ambiyansı çok premium hissettiriyor." / "Bluetooth hoparlör detayı efsane. Ragga oktay yenidena açıp ışığı kısıyoruz, günün stresi direkt gidiyor."

### Açıklama (body_html)

- Boş. Ürün metni yalnız tema bölümlerinde.

### Sorunlu iddialar

- **Fiyat:** Karşılaştırma 2.898 TL fiyatın neredeyse iki katı → "%50 İndirim"; özellik kartında "Odanızı Huzurla Doldurun Diye %50 İndirimli!". "2 Adet · İkincisi %50" 2.174,99 TL (hesap 2.248,50 TL tutar).
- **Garanti çelişkisi:** Görsel 2 "2 YIL GARANTİ" ↔ güven şeridi "1 Yıl".
- **Sağlık:** Görsel 4 "Ninni & sakinleştirici müzik, Uyku rutini yardımcı"; "Uyku Dostu Yumuşak Işık"; yorum "uykuya geçişimiz inanılmaz kolaylaştı".
- **Kopya SSS:** Ana SSS çocuk ürününden ("Çocuğun odasını… ninni/masal"), alt SSS "Hareket sensörü nasıl çalışır?" ve "Tema diskleri küçük parça" (bu üründe disk yok). CTA "Dino Lamp Ambiyans Işığını keşfet" (eski ad).
- **Kutu çelişkisi:** SSS "Cihaz, şarj kablosu, kılavuz" ↔ görsel 2 ayrıca "Uzaktan kumanda".
- **Teyitsiz teknik:** "Şarjlı ve Kablosuz" (görsellerde kablolu), "14 renk • 4 hız", "Bluetooth Müzik-PodCast Hoparlörü".
- **Uydurma yorum:** Görsel 5 Sude Y. "Doğrulanmış Alıcı"; görsel 7 "GERÇEK YORUMLAR" (Sude Y. iki kez). Loox 13 yorum, 5.0, hepsi 16.02.2026, "Doğrulanmış" yok. Sayfa "4.7 (2467)".
- **İade:** "90 Gün Para İade Garantisi".

---

## 10. LunaDream Gece Lambası V2 — `lunadream-gece-lambasi-v2`

- **Adres:** https://ayluna.shop/products/lunadream-gece-lambasi-v2
- **Fiyat:** 1.449,00 TL · karşılaştırma: 1.999,00 TL → gerçek indirim %27.5
- **Varyantlar** (Title): Default Title — 1.449,00 TL — TÜKENDİ
- **Şablon:** `template--28025597591780` · sayfa yüksekliği 7842 px · vendor: Ayluna
- **Ekran görüntüleri** (8 parça, klasör `…/scratchpad/site/urun/`): `lunadream-gece-lambasi-v2-1.png`, `lunadream-gece-lambasi-v2-2.png`, `lunadream-gece-lambasi-v2-3.png`, `lunadream-gece-lambasi-v2-4.png`, `lunadream-gece-lambasi-v2-5.png`, `lunadream-gece-lambasi-v2-6.png`, `lunadream-gece-lambasi-v2-7.png`, `lunadream-gece-lambasi-v2-8.png`
- Ürün tükendi ama sayfa "3 günde 399 adet satıldı" diyor.
- Galeri robot projektörü gösteriyor; sayfanın geri kalanı (GIF, yorum kartı, "Mutlu kullanıcılarımız") pembe LunaDream (V1) ürününü.

### Görseller (9)

1. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/IMG-1613.png?v=1785502716
   Afiş (çizgi film uzay + yapay zekâ çocuk): "UZAY MACERASI BAŞLIYOR!" Paket içeriği: Robot Projektör · Uzay Macerası Diskleri · Uzay Macerası Kitapçığı · "6 FARKLI TEMA DİSKİ" · Net ve canlı görüntü · Güvenli ve dayanıklı · Çocuklar için güvenli malzeme.
2. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260211_125809_ebb68845-b8fb-4ff3-9aca-41813ab40329.jpg?v=1770815968
   Afiş: "TEMA DİSKLERİ" Happy Birthday · Deniz altı · Yıldızlar; kutu + robot.
3. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260211_125837_99a1dae9-e719-4635-9062-374afd360e98.jpg?v=1770815968
   Afiş: "21 Projeksiyon Deseni · TEMA DİSKLERİ 12 ADET DİSK / 9 ADET DİSK"; kutuda "BARBERABAREY" yazısı.
4. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260211_131646_f746ef88-525f-4299-9940-969f0d37fb2c.jpg?v=1770815968
   Yorum kartı: Mert A. "Doğrulanmış Alıcı" 5/5 "Oğlum resmen bayıldı… daha rahat uykuya geçiyor".
5. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260211_125258_fbee879d-0863-4141-9fc6-228022df7276.jpg?v=1770815968
   Yaşam (robotla uyuyan kız): "GECE MODUNU AÇ · Ay & yıldız atmosferiyle" Yumuşak ambiyans · Tema projeksiyonu · Rahatlatıcı gece ışığı · YILDIZLARI YAK.
6. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260211_125026_09110ac5-9a66-4ca2-bdd9-b8d8287d4a42.jpg?v=1770815968
   Yaşam (çocuk odası, duvar boyu balina/uçak): "DUVARINI CANLANDIR · uyku öncesi masal gibi atmosfer" · TEMAYI YANSIT.
7. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260211_124112_f1642c74-40f1-4759-835a-ebcb5dd578a8.jpg?v=1770815968
   Afiş: "MASALSI GECE IŞIĞI" (Çocuk Gece Feneri 1. görselle aynı kalıp) Tema projeksiyonları · Yumuşak ambiyans · Hediye için harika.
8. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260211_130743_d57ee2e9-2652-47cd-9657-6393c9e67263.png?v=1770815968
   7 Instagram tarzı yorum kartı (Elif K., Merve A., Zeynep D., Ayşe T., Sude Y., Kübra Ş., Fatma N.) — "uyku saati kavga bitti", "daha rahat uyuyor".
9. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260211_125452_661c3e85-89b5-48a7-9f91-f31f370480d9.jpg?v=1770815968
   Afiş (dinozor temalı): "HEDİYEYE HAZIR · Gerçek boyutunu gör" Yumuşak ambiyans · Tema projeksiyonu · Sevdiklerine özel.

### Bölüm sırası

Tam id biçimi: şablon bölümleri `shopify-section-template--28025597591780__<anahtar>`, global bölümler `shopify-section-sections--28025597690084__<anahtar>` (altbilgi `…28025597657316__footer`).

1. `custom_liquid_XWzNR9` — Üst geri sayım şeridi (global): "Bugüne Özel %20 İndirim" + sayaç
2. `header` — Başlık (global): menü, logo, arama, sepet
3. `announcement_bar_m7VX6j` — Duyuru şeridi: Online Ödemede Sepette %5 İndirim 🚀
4. `main` — **Ana ürün bölümü** (galeri 9 görsel), blok sırası:
   - Canlı izleyici sayacı: 38 kişi şu anda bu ürünü inceliyor. · 🚀 3 günde 399 Adet satıldı · 🚨 Son 10 Günün en düşük fiyatı · 📦 Kargo Bedava
   - Başlık: LunaDream Gece Lambası V2
   - Puan satırı: 4.7 ( 2467 Onaylı Kullanıcı Yorumu)
   - Özellik başlığı: ✨ Sihirli Özellikler ✨ · Uyku vakti artık savaş değil, minik bir masal
   - Özellik kartları: Mışıl Mışıl Uykular · Yumuşacık ışık, huzurlu geçiş · Hediye Diskler · Her gece yeni bir hayal · +10.000 Mutlu Anne · Binlerce ailenin tercihi · Kablosuz Kullanım · Şarj et, her yere taşı · ✨ Çocuğunuzun Hayalleri Artık Odasında · Işığı yakın, o gülümsemeyi izleyin
   - Paket teklifi (Kaching) + satın al butonları: Sınırlı süreli teklif · 1 Adet · %20 İndirim · 1,449.00TL · 1,999.00TL · 2 Adet · İkincisi %50 İndirimli · 2,174.99TL · 3,998.00TL · Yıldız Işığı Nemlendirici · 308.08TL İndirim! · 790.92TL · 1,099.00TL · Tükendi · Tükendi
   - Ödeme logoları: Amex, Diners, Discover, JCB, Mastercard, Visa
   - Teslimat zaman çizelgesi: 18 Ekm · Siparişiniz Oluşturuldu · 19 Ekm - 20 Ekm · Kargonuz Hazırlandı · 21 Ekm - 23 Ekm · Evinize Teslim Edildi
   - Teslim tahmini kutusu (il seçimli): 18 saat 33 dakika içinde sipariş verirsen yarın kargoda! · Tahmini Teslim: · Adresini seç, teslim tarihini öğren! · Konum Seç · 1. ADIM · İL SEÇ · Süreler iş günü üzerinden hesaplanır; pazar ve resmî tatiller sayılmaz. Yoğun dönem ve hava koşullarında değişebi …
   - Güven şeridi: 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi
   - Yapışkan sepet çubuğu: LunaDream Gece Lambası V2 · 1,449.00TL · 1,999.00TL · Tükendi
   - Açılır soru: Gece rutinine nasıl entegre ederim?
   - Açılır soru: Bu ürün ne işe yarıyor?
   - Açılır soru: Projeksiyon nasıl çalışıyor?
   - Açılır soru: Hoparlör olarak kullanabilir miyim ?
   - Açılır soru: Bluetooth var mı, ne işe yarıyor?
   - Açılır soru: Parlaklığı çocuğu rahatsız eder mi?
   - Açılır soru: Kutu içeriğinde neler var?
   - Açılır soru: Bluetooth bağlanmıyor, ne yapmalıyım?
5. `custom_liquid_KmrhqB` — Özel Liquid: GERÇEK ANNELER · GERÇEK VİDEOLAR · Sizden Gelenler · 10.000 anneden sadece 3 tanesini paylaştık 🩷 · Ses için dokun · 🩷 · 10.000+ · anne kullanıyor · · · 4,9/5 · ortalama puan
6. `custom_liquid_cy3qwQ` — Özel Liquid: SİZDEN GELEN MESAJLAR · Bizi Değil Kullanıcılarımızı Dinleyin · Gün boyu konfor deneyimleyen kullanıcılarımızdan gerçek geri bildirimler. · Mesajlar, müşterilerimizin izniyle paylaşılan · gerçek sohbetlerdir. [8 görsel: imgi_13_saaaaaaaaaaaa_4.png, imgi_17_Adsiz_tasarim_31.png, imgi_12_Adsiz_tasarim_48.png …]
7. `custom_liquid_fcgYdJ` — Özel Liquid: MUTLU KULLANICILARIMIZ · Siz de · Ailemize Katılın · Binlerce mutlu kullanıcımız arasındaki yerinizi alın ve gün boyu konfor deneyiminizi bizimle paylaşın. [6 görsel: hf_20260805_162416_233334de-6e8a-4c53-8dd6-2…, hf_20260805_162424_736b1004-a065-4c61-bb40-6…, hf_20260805_162151_176cabfa-ddb4-445b-84c8-4… …]
8. `horizontal_ticker_rbYQET` — Kayan şerit: Ücretsiz Kargo 📦 · 21 Farklı Mod ✨ · Çocuklara Özel 👶🏻
9. `image_banner_Ae7wdz` — GIF afiş + başlık: Onun evi, odası · ÇOCUKLARIMIZIN EN SEVDİĞİ YERLERİ OLAN ODALARINI ONLAR İÇİN EĞLENCE İLE DONATIN. [1 görsel: f7605d62f7804eb5a52a532361a5adc7-ezgif.com-v…]
10. `8beb6911-28c6-482c-976a-e5421ad3e8df` — Özellik satırları (4 başlık + görsel): Çeşitli Animasyon Seçenekleri · Gece lambası projektörümüz, 21 farklı animasyon seçeneği ile odanızı büyülü bir hale getirir. · Projektör ve Işık Efektleri · Gece lambası projektörü, ışık efektleri ve projeksiyonları ile odanızı aydınlatırken etkileyici bir görsel deneyim sunar. · Bluetooth Özelliği ile Müzik ve Hikaye Dinleme · Cihazı telefon veya tabletinize bağlayarak çocuğunuzun favori müziklerini veya sesli hika … [1 görsel: hf_20260210_160930_3f3a2c34-e86e-41d4-9d18-b…]
11. `image_with_text_8UNBF8` — Görsel + metin + buton: Yıldız Işığı Ambiyansı, Tek Dokunuşla · Ayluna, ailesi olarak en son teknoloji ürünleri terchi ettiğimizi belirtmek isteriz. Son teknoloji projeksiyon çipimiz sayesinde mükemmel yansıtma gücü sağlar. · LunaDream Gece Lambasını Keşfet [1 görsel: hf_20260210_153504_424d39db-e114-43ac-974c-a…]
12. `collapsible_content_7zjVTU` — SSS (açılır): SSS, 8 soru (aşağıda)
13. `b321ab88-2b59-4dba-bade-54885c874ca5` — Ayraç
14. `17694466126b1e0319` — Loox yorum uygulaması (iframe; ayrıntı aşağıda)
15. `footer` — Altbilgi (global): %5 indirim için e-posta aboneliği, ödeme logoları, politikalar

### Paket teklifi, geri sayım, kargo

- **Paket (Kaching):** Sınırlı süreli teklif · 1 Adet · %20 İndirim · 1,449.00TL · 1,999.00TL · 2 Adet · İkincisi %50 İndirimli · 2,174.99TL · 3,998.00TL · Yıldız Işığı Nemlendirici · 308.08TL İndirim! · 790.92TL · 1,099.00TL
- **Geri sayım:** üst şerit "Bugüne Özel %20 İndirim 01 SAAT : 01 DK : 38 SAN" (her yüklemede yeniden başlar)
- **Teslim tahmini:** 18 saat 33 dakika içinde sipariş verirsen yarın kargoda! · Tahmini Teslim: · Adresini seç, teslim tarihini öğren! · Konum Seç · 1. ADIM · İL SEÇ · Süreler iş günü üzerinden hesaplanır; pazar ve resmî …
- **Duyuru şeridi:** Online Ödemede Sepette %5 İndirim 🚀
- **Güven şeridi:** 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi

### SSS

**Kaynak: `main`**

- **Hoparlör olarak kullanabilir miyim ?** Tabikide evet gelişmiş uzaktan bağlantı özelliği sayesinde telefonunuzdan bağlanarak dilediğiniz müziği açabilir ve evinizin ambiyansını daha üst seviyelere çıkartabilirsiniz.
- **Bu ürün ne işe yarıyor?** Çocuğun odasını yumuşak bir gece ışığı ve projeksiyon efektleri ile daha sakin bir uyku ortamına çevirir.Ayrıca Bluetooth ile telefondan ninni müzik masal açabilirsiniz.
- **Gece rutinine nasıl entegre ederim?** Uyku öncesi 10 dakika: ışığı aç → favori temayı yansıt → telefondan kısa ninni/masal aç → aynı rutini her gece tekrarla.
- **Projeksiyon nasıl çalışıyor?** Cihazın projeksiyon modunu açıp seçtiğiniz temayı kullanarak duvar/tavan üzerine görsel yansıma alırsınız.
- **Bluetooth var mı, ne işe yarıyor?** Evet — telefon/tablete bağlayıp çocuğun sevdiği ninni, müzik veya sesli hikâyeleri çalabilirsiniz.
- **Parlaklığı çocuğu rahatsız eder mi?** Tabikide hayır :)Yumuşak ambiyans için tasarlandı; gece boyunca göz yormayan kullanım hedeflendi
- **Kutu içeriğinde neler var?** Cihaz + Tema diskleriŞarj kablosu Kullanım kılavuzu

**Kaynak: `collapsible_content_7zjVTU`**

- **Bu modelde hangi özellikler var?** Bu model hareket sensörlü değildir. (Bazı modellerde sensör bulunabiliyor.) Bu üründe tüm kontrol tuşlar/kumanda üzerinden yapılır; böylece gece kullanımında daha stabil ve sürprizsiz bir deneyim sağlar.
- **Hareket sensörü nasıl çalışır?** Sensör, hareket algıladığında ışığı otomatik olarak açar. Belirli bir süre hareket algılamazsa ışık kendiliğinden kapanır. Gece koridor, yatak yanı ve çocuk odası kullanımında çok pratiktir.
- **Tuşlar ile neleri kontrol edebilirim?** Genellikle aç/kapat, ışık modu/efekti geçişi, parlaklık ayarı, projeksiyon modları, müzik ses kontrolü gibi temel işlevleri kolayca yönetebilirsiniz.
- **Bluetooth hoparlöre nasıl bağlanırım?** Ürünü açın ve Bluetooth modunu aktif edin.Telefonunuzda Bluetooth’u açın → cihaz listesinden ürünü seçin Bağlandıktan sonra Spotify/YouTube/telefonunuzdaki ninnileri doğrudan hoparlörden çalabilirsiniz.
- **Ürün şarjlı mı, prizde mi çalışır?** Ürün şarjlıdır ve kablosuz kullanılabilir. İsterseniz şarj ederken de kullanabilirsiniz (kullanım alışkanlığına göre pratiklik sağlar).
- **Şarjı ne kadar gider?** Şarj süresi; parlaklık seviyesi, projeksiyonun açık kalması, Bluetooth ses düzeyi gibi etkenlere göre değişir. Gece rutininde (orta parlaklık düşük ses) genelde birkaç saatlik kullanım sağlar.
- **Gece kullanımında göz yorar mı?** Uyku için tasarlanan yumuşak ışık modunda rahatsız etmez. En iyi deneyim için:Parlaklığı orta/düşük kullanın,Işığı doğrudan göze değil, duvara/tavana yansıtın.
- **Çocuk odasında kullanmak güvenli mi?** Evet, çocuk odası kullanımına uygundur. LED ışık düşük ısı üretir. Güvenlik için:Ürünü düz ve sağlam bir zemine koyun,Tema diskleri küçük parça olabileceği için küçük çocuklarda ebeveyn gözetimiyle kullanın,Kabloyla kullanımda kabloyu ortalıkta bırakmayın.


### Yorumlar

- **Sayfada yazan:** "4.7 (2467 Onaylı Kullanıcı Yorumu)" (sabit metin)
- **Loox gerçek:** 0 yorum ("Yorum yapan ilk kişi olun")

### Açıklama (body_html)

- Boş. Ürün metni yalnız tema bölümlerinde.

### Sorunlu iddialar

- **Kopya içerik (kritik):** Galeri robot projektör; GIF, yorum kartı, "Mutlu kullanıcılarımız", "Sizden gelen mesajlar" pembe LunaDream (V1) ürününü gösteriyor. CTA "LunaDream Gece Lambasını Keşfet".
- **Kutu çelişkisi:** Görsel 1 "6 farklı tema diski" ↔ görsel 3 "21 desen · 12 + 9 disk" ↔ şerit/bölüm "21 Farklı Mod/animasyon". Görsel 1 kutu: robot + diskler + kitapçık; SSS: cihaz + diskler + şarj kablosu + kılavuz. Görsel 3'te tedarikçi markası "BARBERABAREY".
- **Sağlık:** "Mışıl Mışıl Uykular", "Uyku vakti artık savaş değil", "Rahatlatıcı gece ışığı"; görsel 1 "Çocuklar için güvenli malzeme" (belgesiz).
- **Uydurma puan:** "+10.000 Mutlu Anne", "10.000+ anne · 4,9/5", üstte "4.7 (2467)"; Loox: 0 yorum.
- **Uydurma satış:** Tükenmiş ürüne "🚀 3 günde 399 Adet satıldı", "Son 10 Günün en düşük fiyatı".
- **Uydurma yorum:** Görsel 4 Mert A. ve görsel 8 (7 kart) uydurma.
- **Kopya SSS:** "Hareket sensörü nasıl çalışır?"; Bluetooth/hoparlör iddiası teyitsiz.
- **İade:** "90 Gün Para İade Garantisi".

---

## 11. Yıldız Işığı Nemlendirici — `yildiz-isigi-nemlendirici`

- **Adres:** https://ayluna.shop/products/yildiz-isigi-nemlendirici
- **Fiyat:** 849,99 TL · karşılaştırma: 1.099,00 TL → gerçek indirim %22.7
- **Varyantlar** (Title): Default Title — 849,99 TL — satışta
- **Şablon:** `template--28025597526244` · sayfa yüksekliği 6837 px · vendor: Ayluna
- **Ekran görüntüleri** (7 parça, klasör `…/scratchpad/site/urun/`): `yildiz-isigi-nemlendirici-1.png`, `yildiz-isigi-nemlendirici-2.png`, `yildiz-isigi-nemlendirici-3.png`, `yildiz-isigi-nemlendirici-4.png`, `yildiz-isigi-nemlendirici-5.png`, `yildiz-isigi-nemlendirici-6.png`, `yildiz-isigi-nemlendirici-7.png`
- Duyuru şeridi yok. "%100 Müşteri Memnuniyeti" bölümü AyFeneri müşteri sohbetlerini gösteriyor.
- Yapışkan sepet butonu İngilizce: "Add to cart"; paket ekinde "Save 503.17TL!".

### Görseller (7)

1. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260210_160835_4caca476-596c-43c9-a7c4-6e673c21a860.png?v=1770741660
   Afiş (lacivert): "ULTRASONİK NEMLENDİRİCİ · Ortamınızı RENKLENDİRİN, nem seviyesini dengeleyin" RGB Işık Halkası · 280 ML Su Haznesi · Ayarlanabilir Eğim · Ultrasonik Nemlendirme.
2. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260210_161423_df315f2b-f1a9-4ce1-a8f9-0def789c596c_1.png?v=1770742654
   Afiş (kırmızı buhar): "TAVANA YILDIZ YANSITMA MODU VE VE YOĞUN BUHAR EFEKTİ · ORTAMA HAVA KAT!" ("VE VE" hatası).
3. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260210_161844_4644fa21-dbe9-41bb-bbd6-51776c26b64a.png?v=1770742654
   Afiş: "TEKNİK ÖZELLİKLER" Güç 18 W · Kapasite 2,8 L · RGB Aydınlatma · Ultrasonik Teknoloji (ikonda "2.3L").
4. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260210_162313_243420eb-7a84-4e88-9e44-0276800dc74a.jpg?v=1770742654
   Yaşam (gece komodin, uçucu yağ şişesi): "Ortamı Nemlendirir ve Ambiyans Katar · Sessiz çalışır ve uykuda rahatsız etmez. Cilde nem katar. Uçucu yağ ile güzel koku sağlar."
5. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260210_165356_6017a38b-044a-49f1-a7dd-8d600f87b194.png?v=1770742745
   Yorum kartı: 6 yıldız (!) "Gece modunda neredeyse hiç ses yok. Klima kuruluğunu çok iyi toparladı…" — Elif K., İstanbul.
6. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260210_162045_bdbb5353-41c8-4abc-a863-db172143c5d5.jpg?v=1770742745
   Afiş (araç içi, sürücü kadın): "Taşınabilir Oto Atomizer Nemlendirici · Kuru ve rahatsız edici klimaya sahip arabalara veda edin · Hem Nemlendirici Hem Araç Kokusu Olarak Kullan!"
7. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260210_162443_653ecc3a-3829-45d0-b97a-638ec04390e1.jpg?v=1770742745
   4'lü oda kolajı: YATAK ODASI · OFİS · SALON · ÇOCUK ODASI (cihaz bej renkte; diğer görsellerde beyaz).

### Bölüm sırası

Tam id biçimi: şablon bölümleri `shopify-section-template--28025597526244__<anahtar>`, global bölümler `shopify-section-sections--28025597690084__<anahtar>` (altbilgi `…28025597657316__footer`).

1. `custom_liquid_XWzNR9` — Üst geri sayım şeridi (global): "Bugüne Özel %20 İndirim" + sayaç
2. `header` — Başlık (global): menü, logo, arama, sepet
3. `main` — **Ana ürün bölümü** (galeri 7 görsel), blok sırası:
   - Başlık: Yıldız Işığı Nemlendirici
   - Puan satırı: 4.7 ( 2467 Onaylı Kullanıcı Yorumu)
   - Fiyat satırı: 849,99 TL · 1.099,00 TL üstü çizili · rozet "%20 İndirim"
   - Kısa açıklama: Evinde, arabanda, odanda hem ambians hem ferah bir koku.
   - Özellik kartları: Gerçek Yıldız Ambiyansı · Gelişmiş püskürtme gücü · Kolay Kontrol · Şarjlı ve Kablosuz Kullanım · Her Odaya Uyumlu Modern Tasarım
   - Canlı izleyici sayacı: 45 kişi şu anda bu ürünü inceliyor.
   - Kargo notu: TÜM SİPARİŞLER HIZLI KARGO İLE ÇIKARTILMAKTADIR
   - Paket teklifi (Kaching) + satın al butonları: Sınırlı süreli teklif · 1 Adet · %20 İndirim · 849.99TL · 1,099.00TL · 2 Adet · %50 İndirim · 1,275.00TL · 2,198.00TL · LunaDream Gece Lambası · Save 503.17TL! · 1,495.83TL · 1,999.00TL · GÜVENLİ ÖDEME İLE AL · Kapıda Ödeme ile Sipariş Ver
   - Ödeme logoları: Amex, Diners, Discover, JCB, Mastercard, Visa
   - Teslimat zaman çizelgesi: 18 Ekm · Siparişiniz Oluşturuldu · 19 Ekm - 20 Ekm · Kargonuz Hazırlandı · 21 Ekm - 23 Ekm · Evinize Teslim Edildi
   - Güven şeridi: 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi
   - Yapışkan sepet çubuğu: Yıldız Işığı Nemlendirici · 849.99TL · 1,099.00TL · Add to cart
   - Kısa yorum kaydırıcısı (3 yorum): Kuruluğu gerçekten fark edilir şekilde azalttı. Işık halkası da ortama çok hoş bir hava katıyor. · Arif S. · Gece kalkınca sensör otomatik yakıyor, büyük rahatlık. Kumanda ve Bluetooth’un hepsi tek üründe olması çok iyi · Gülsüm S. · Şarjlı olması harika; istediğim yere taşıyorum. Hem dekor gibi duruyor hem de gerçekten işe yarıyor · Zeynep R.
   - Açılır: Teknik Özellikler: Güç Kaynağı: Dahili batarya · Stil Seçenekleri: Kumandalı, Bluetooth, Sensörlü · Voltaj: ≤ 36V · Boyut: 70 × 72 × 242 mm · Modelleme: Geometrik üç boyutlu tasarım · Tarz: Modern ve sade · Giriş Voltajı: 5V – 1A · Nominal Güç: 5W · LED Gücü: 1.5W (5×0.2W LED modülü + 1×3W LED modülü) · Hoparlör Gücü (Bluetooth model): 4 Ω, 3W · Batarya Kapasitesi: 2400 mAh
   - Açılır: Kutu İçeriği: Masa Lambası × 1 · USB Kablo × 1 · 16 ülke için uyumlu adaptör/başlık × 1
   - Açılır soru: Yıldız ışığı ne kadar belirgin?
   - Açılır soru: 14 Şubata yetişir mi?
   - Açılır soru: Hep fişe mi takılı olucak?
4. `eba88da5-80ac-47fc-aa75-997cfe7b2e59` — Yorum ekran görüntüsü kaydırıcısı: %100 Müşteri Memnuniyeti [3 görsel: WhatsApp_Image_2026-01-31_at_23.23.27_91fc5e…, WhatsApp_Image_2026-01-26_at_17.14.10.jpg, WhatsApp_Image_2026-01-26_at_17.21.47.jpg]
5. `image_banner_Ae7wdz` — GIF afiş + başlık: Odanı gökyüzüne çevir · GÜN BİTİNCE HERKESİN RAHATLAMAYA İHTİYACI VAR [1 görsel: ezgif.com-video-to-gif-converter.gif]
6. `8beb6911-28c6-482c-976a-e5421ad3e8df` — Özellik satırları (4 başlık + görsel): Gerçek Yıldız Işığı Ambiyansı · Duvara yansıyan Yıldız görüntüsüyle bulunduğun ortamı anında daha sıcak, sakin ve dekoratif hale getirir. · Uzun Şarj Süresi · Ne zaman şarja taktığını unutarak kullanabileceksin sakin ol bozuk değil KALİTELİ. · Son Teknoloji Projeksiyon · En güncel çipler ile donatılmış muhteşem bir yansıtma performansı. · Şarjlı ve Kablosuz Kullanım · Dahili batarya sayesinde priz bağımlılığı yok; is … [1 görsel: 96131.webp]
7. `image_with_text_8UNBF8` — Görsel + metin + buton: Yıldız Işığı Ambiyansı, Tek Dokunuşla · Ayluna, duvara gerçekçi Yıldız yansıması vererek bulunduğun alanı anında daha sıcak ve huzurlu hale getirir. Yumuşak ışığıyla gece kullanımı için idealdir. · Huzurlu Ambiyansı Keşfet [1 görsel: imgi_117_71JE-d_E7zL._AC_SL1500.jpg]
8. `b321ab88-2b59-4dba-bade-54885c874ca5` — Ayraç
9. `17694466126b1e0319` — Loox yorum uygulaması (iframe; ayrıntı aşağıda)
10. `footer` — Altbilgi (global): %5 indirim için e-posta aboneliği, ödeme logoları, politikalar

### Paket teklifi, geri sayım, kargo

- **Paket (Kaching):** Sınırlı süreli teklif · 1 Adet · %20 İndirim · 849.99TL · 1,099.00TL · 2 Adet · %50 İndirim · 1,275.00TL · 2,198.00TL · LunaDream Gece Lambası · Save 503.17TL! · 1,495.83TL · 1,999.00TL
- **Geri sayım:** üst şerit "Bugüne Özel %20 İndirim 01 SAAT : 01 DK : 41 SAN" (her yüklemede yeniden başlar)
- **Duyuru şeridi:** yok
- **Güven şeridi:** 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi

### SSS

**Kaynak: `main`**

- **14 Şubata yetişir mi?** Tüm Türkiye'ye hızlı kargo ile 2-5 gün arasında kargolama yapmaktayız her gün kargo çıkışlarımız yapılmaktadır içiniz rahat bir şekilde satın alabilirsiniz.
- **Yıldız ışığı ne kadar belirgin?** Ürünümüzde en güncel projeksiyon çipi mevcuttun hd kalitede yansıtma yapar Gökyüzünü odanıza taşımak için bir adım uzaktasınız.
- **Hep fişe mi takılı olucak?** Tabikide hayır :)2400mh bataryası sayesinde uzun süre şarjlı bir şekilde istediğiniz ortamda kullanım sağlayabilirsiniz.


### Yorumlar

- **Sayfada yazan:** "4.7 (2467 Onaylı Kullanıcı Yorumu)" (sabit metin)
- **Loox gerçek:** 6 yorum, ortalama 5.0 (dağılım: 5★×6); ilk 20 yorumun tarihleri: 10.02.2026 ×6; "Doğrulanmış" etiketi: 0
- **Loox örnek:** "Bence güzel alın odayı güzel nemlendirir tavan görüntüsü harika paketleme falanda güzeldi" / "Ürün göründüğü gibi geldi çok memnun kaldım bir tane daha sipariş vermeyi düşünüyoruz" / "Ürün göründüğü gibi geldi çok memnun kaldım bir tane daha sipariş vermeyi düşünüyoruz" / "Göründüğü gibi geldi .Farklı bir ürün görüntüsü de hoş"

### Açıklama (body_html)

- Boş. Ürün metni yalnız tema bölümlerinde.

### Sorunlu iddialar

- **Kopya içerik (kritik):** "Teknik Özellikler" AyFeneri'nin (70×72×242 mm, 2400 mAh, LED 1,5 W, hoparlör 3 W, "Kumandalı, Bluetooth, Sensörlü"); "Kutu İçeriği: Masa Lambası × 1, 16 ülke adaptörü"; SSS "2400mh batarya"; yorumlar "sensör otomatik yakıyor… Kumanda ve Bluetooth".
- **Teyitsiz teknik:** Hazne: görsel 1 "280 ML" ↔ görsel 3 "2,8 L" (ikonda 2.3 L). Güç: "18 W" ↔ tablo "5 W".
- **Sağlık:** Görsel 4 "Cilde nem katar", "uykuda rahatsız etmez"; "nem seviyesini dengeleyin"; yorum "Kuruluğu gerçekten fark edilir şekilde azalttı".
- **Güvenlik:** Görsel 6 sürüş sırasında araç içinde buhar + ışık ("Oto Atomizer"); kısa açıklama "Evinde, arabanda…".
- **Uydurma yorum:** Görsel 5 altı yıldızlı yorum kartı. Loox 6 yorum, 5.0, hepsi 10.02.2026; iki yorum birebir aynı metin. Sayfa "4.7 (2467)", "%100 Müşteri Memnuniyeti" (AyFeneri sohbetleri).
- **Güncellik:** SSS "14 Şubata yetişir mi?".
- **Fiyat etiketi:** "2 Adet %50 İndirim" (gerçek %42; aslında ikincisi %50).
- **Görsel / telif:** "Görsel + metin" bölümünde Amazon görseli (`imgi_117_71JE-d_E7zL._AC_SL1500.jpg`).
- **İade:** "90 Gün Para İade Garantisi".

---

## 12. Ayluna Kum Saati Lamba — `ask-saati`

- **Adres:** https://ayluna.shop/products/ask-saati
- **Fiyat:** 799,00 TL · karşılaştırma: 999,00 TL → gerçek indirim %20.0
- **Varyantlar** (Title): Default Title — 799,00 TL — satışta
- **Şablon:** `template--28025597198564` · sayfa yüksekliği 3168 px · vendor: Ayluna
- **Ekran görüntüleri** (4 parça, klasör `…/scratchpad/site/urun/`): `ask-saati-1.png`, `ask-saati-2.png`, `ask-saati-3.png`, `ask-saati-4.png`
- En kısa sayfa (3.168 px): ana bölüm + 3 sohbet görseli + Loox. Duyuru şeridi ve paket teklifi yok.
- Yapışkan sepet butonu İngilizce: "Add to cart".

### Görseller (4)

1. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/imgi_8_1_org_zoom.jpg?v=1769961005
   Afiş (yılbaşı süsleri, hediye kutuları): "Mükemmel Hediye · Huzur ve Sakinliği Evinize Getirin · Her Özel An İçin Şık ve Etkileyici LED Kum Sanatı Lambası". Dosya adı "imgi_8_1_org_zoom" (başka satıcıdan indirilmiş).
2. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/imgi_10_1_org_zoom.jpg?v=1769961019
   Beyaz zemin ölçü: 16 cm × 18,5 cm; siyah çerçeve (diğer görsellerde gümüş/şeffaf).
3. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/imgi_12_1_org_zoom.jpg?v=1769961056
   Gerçek ürün fotoğrafı: "Dokunmatik Anahtar" işaretli.
4. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/imgi_60_1_org_zoom.jpg?v=1769961076
   Afiş (kırmızı, kalpler): "Sevgililer Günü'nde Ona Huzuru Hediye Edin · 14 Subat" (sezonu geçmiş; "Subat" yazımı; altta silik "Shop" filigranı).

### Bölüm sırası

Tam id biçimi: şablon bölümleri `shopify-section-template--28025597198564__<anahtar>`, global bölümler `shopify-section-sections--28025597690084__<anahtar>` (altbilgi `…28025597657316__footer`).

1. `custom_liquid_XWzNR9` — Üst geri sayım şeridi (global): "Bugüne Özel %20 İndirim" + sayaç
2. `header` — Başlık (global): menü, logo, arama, sepet
3. `main` — **Ana ürün bölümü** (galeri 4 görsel), blok sırası:
   - Başlık: Ayluna Kum Saati Lamba
   - Puan satırı: 4.7 ( 2467 Onaylı Kullanıcı Yorumu)
   - Fiyat satırı: 799,00 TL · 999,00 TL üstü çizili · rozet "%20 İndirim"
   - Kısa açıklama: Geceye bir ışık yak, odanı kendi küçük kaçışına çevir.
   - Özellik kartları: Kusursuz Aydınlatma · Etkileyici Parlaklık · Tek tuşla kontrol · Şarjlı ve Kablosuz Kullanım · Her Odaya Uyumlu Modern Tasarım
   - Canlı izleyici sayacı: 32 kişi şu anda bu ürünü inceliyor.
   - Kargo notu: TÜM SİPARİŞLER HIZLI KARGO İLE ÇIKARTILMAKTADIR
   - Satın al butonları: GÜVENLİ ÖDEME İLE AL · Kapıda Ödeme ile Sipariş Ver
   - Ödeme logoları: Amex, Diners, Discover, JCB, Mastercard, Visa
   - Teslimat zaman çizelgesi: 18 Ekm · Siparişiniz Oluşturuldu · 19 Ekm - 20 Ekm · Kargonuz Hazırlandı · 21 Ekm - 23 Ekm · Evinize Teslim Edildi
   - Güven şeridi: 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi
   - Yapışkan sepet çubuğu: Ayluna Kum Saati Lamba · 799.00TL · 999.00TL · Add to cart
   - Kısa yorum kaydırıcısı (3 yorum): Ambiyansı inanılmaz değiştirdi. Ay yansıması çok gerçekçi ve ışık tonu göz yormuyor. · Mehmet L. · Gece kalkınca sensör otomatik yakıyor, büyük rahatlık. Kumanda ve Bluetooth’un hepsi tek üründe olması çok iyi · Gülsüm S. · Şarjlı olması harika; istediğim yere taşıyorum. Hem dekor gibi duruyor hem de gerçekten işe yarıyor · Zeynep R.
   - Açılır soru: 14 Şubata yetişir mi?
   - Açılır soru: Hep fişe mi takılı olucak?
4. `eba88da5-80ac-47fc-aa75-997cfe7b2e59` — Yorum ekran görüntüsü kaydırıcısı: %100 Müşteri Memnuniyeti [3 görsel: WhatsApp_Image_2026-01-31_at_23.23.27_91fc5e…, WhatsApp_Image_2026-01-26_at_17.14.10.jpg, WhatsApp_Image_2026-01-26_at_17.21.47.jpg]
5. `17694466126b1e0319` — Loox yorum uygulaması (iframe; ayrıntı aşağıda)
6. `footer` — Altbilgi (global): %5 indirim için e-posta aboneliği, ödeme logoları, politikalar

### Paket teklifi, geri sayım, kargo

- **Paket (Kaching):** yok
- **Geri sayım:** üst şerit "Bugüne Özel %20 İndirim 01 SAAT : 01 DK : 45 SAN" (her yüklemede yeniden başlar)
- **Duyuru şeridi:** yok
- **Güven şeridi:** 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi

### SSS

**Kaynak: `main`**

- **14 Şubata yetişir mi?** Tüm Türkiye'ye hızlı kargo ile 2-5 gün arasında kargolama yapmaktayız her gün kargo çıkışlarımız yapılmaktadır içiniz rahat bir şekilde satın alabilirsiniz.
- **Hep fişe mi takılı olucak?** Tabikide hayır :)2400mh bataryası sayesinde uzun süre şarjlı bir şekilde istediğiniz ortamda kullanım sağlayabilirsiniz.


### Yorumlar

- **Sayfada yazan:** "4.7 (2467 Onaylı Kullanıcı Yorumu)" (sabit metin)
- **Loox gerçek:** 1 yorum, ortalama 1.0 (dağılım: 1★×1); ilk 20 yorumun tarihleri: 28.02.2026 ×1; "Doğrulanmış" etiketi: 1
- **Loox örnek:** "Ürün gelmedi tedarik sorunu var"

### Açıklama (body_html)

- Boş. Ürün metni yalnız tema bölümlerinde.

### Sorunlu iddialar

- **Uydurma puan (kritik):** Loox'taki tek yorum 1 yıldız: "Ürün gelmedi tedarik sorunu var" (Serdar K., Doğrulanmış, 28.02.2026). Sayfa "4.7 (2467 Onaylı Kullanıcı Yorumu)" ve "%100 Müşteri Memnuniyeti".
- **Kopya yorum / SSS:** Kısa yorumlar AyFeneri'nden ("Ay yansıması çok gerçekçi", "sensör otomatik yakıyor… Kumanda ve Bluetooth"); SSS "14 Şubata yetişir mi?" ve "2400mh bataryası sayesinde…" (AyFeneri).
- **Teyitsiz teknik:** "Şarjlı ve Kablosuz Kullanım", "Kusursuz Aydınlatma", ölçü 16 × 18,5 cm.
- **Stok:** Stok sayacı -246, politika "continue"; tedarik şikâyeti var → stoksuz satış riski.
- **Görsel:** Görseller başka satıcıdan ("org_zoom" dosya adları); çerçeve rengi görseller arasında farklı; Sevgililer Günü afişi sezon dışı.
- **İade:** "90 Gün Para İade Garantisi".

---

## 13. Ayluna AyFeneri — `lamba`

- **Adres:** https://ayluna.shop/products/lamba
- **Fiyat:** 1.649,99 TL · karşılaştırma: 2.499,00 TL → gerçek indirim %34.0
- **Varyantlar** (Title): Default Title — 1.649,99 TL — satışta
- **Şablon:** `template--28025597165796` · sayfa yüksekliği 11711 px · vendor: Mağazam
- **Ekran görüntüleri** (12 parça, klasör `…/scratchpad/site/urun/`): `lamba-1.png`, `lamba-2.png`, `lamba-3.png`, `lamba-4.png`, `lamba-5.png`, `lamba-6.png`, `lamba-7.png`, `lamba-8.png`, `lamba-9.png`, `lamba-10.png`, `lamba-11.png`, `lamba-12.png`
- Sitenin gerçek yorum birikimi olan tek ürün (Loox 43 yorum).
- Şablon Astronot ile ortak (`template--28025597165796`). Vendor alanı "Mağazam" (diğerleri "Ayluna").
- Paket teklifinde iki ek ürün: Kum Saati Lamba ve Yıldız Işığı Nemlendirici.

### Görseller (9)

1. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260212_125544_58e8b2af-ee81-4a04-a2d0-b338ebc94713.png?v=1770903660
   Afiş: "MÜZİĞİ AÇ ORTAMI KUR · Bluetooth hoparlör + yumuşak ışık, tek dokunuşla." Bluetooth ile Bağlan · Telefondan Müzik Çal · Kumanda Dahil.
2. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260212_134125_cc13778c-00c4-4b7f-94f6-a278ef384c09.png?v=1770903811
   Afiş + yapay zekâ erkek sunucu: "BU GECE ODANI AYLA DOLDUR · Ay projeksiyonu + yumuşak ışık + deniz sesi" Kumanda Dahil · Bluetooth · "Sepette %25 Otomatik İndirim".
3. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260212_131148_c44be235-7446-4b8f-a7c5-85117777ec6e.jpg?v=1770903811
   Afiş (gece): "GECEYİ SAKİNLEŞTİR DUVARINA AYI TAŞI · gerçekçi ay projeksiyonu" Ay Projeksiyonu · Gece Atmosferi · Yumuşak Işık.
4. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260212_131637_e0b52ca0-ea39-45bb-84ae-3a012af074c8.jpg?v=1770903811
   Ölçü/kutu afişi: "Boyutlar & Kutu İçeriği" Yükseklik 24,2 cm · Taban Çapı 7,2 cm · Kutu İçeriği: Lamba + Kumanda.
5. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/Ayse_K..png?v=1770903811
   Yorum kartı: Ayşe K. 5 yıldız "Gerçekten çok huzurlu bir havası var…" (dosya adı "Ayse_K.").
6. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260212_131401_15489747-73e8-411e-b295-19ddea6e4418.jpg?v=1770903811
   Yaşam + afiş (uyuyan kadın): "UYKU MODUNU AÇ ODAYI SAKİNLEŞTİR · Yumuşak ışık ve deniz sesiyle akşam rutinin hazır" Oda Aydınlatması · Deniz Sesi Simülasyonu.
7. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260212_132116_10cc0939-3f68-4a88-8c75-41e7b54a052c.jpg?v=1770903811
   Yaşam + afiş: "BU GECE ODANI AYLA DOLDUR" Kumanda Dahil · Bluetooth (kumanda görünüyor).
8. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260212_133352_1fa56ee4-b120-47a2-b6db-a9e7f4244efd.png?v=1770903811
   "Müşteri Yorumları": 6 kart (Ayşe K., Zeynep D., Merve A., Sude Y., Elif K., Kübra Ş.) "Doğrulanmış Alıcı"; "Deniz sesi modu… uykuya dalmak kolaylaştı".
9. https://cdn.shopify.com/s/files/1/0792/3571/1204/files/hf_20260126_133556_b1c70f71-b983-4e58-8c4b-aa20850114ea.jpg?v=1770903811
   Ürün fotoğrafı (gerçek ürün, bej zemin): "Çıkarılabilir Taban · Masa Üzerine Sabitle"; gövdede tedarikçi yazısı "LIGHT OF THE LIFE", hoparlör ızgarası ve USB girişi.

### Bölüm sırası

Tam id biçimi: şablon bölümleri `shopify-section-template--28025597165796__<anahtar>`, global bölümler `shopify-section-sections--28025597690084__<anahtar>` (altbilgi `…28025597657316__footer`).

1. `custom_liquid_XWzNR9` — Üst geri sayım şeridi (global): "Bugüne Özel %20 İndirim" + sayaç
2. `header` — Başlık (global): menü, logo, arama, sepet
3. `announcement_bar_dEW9QR` — Duyuru şeridi: 3D Güvenli Ödeme İle Satın Al Ertesi Gün Kargoda
4. `main` — **Ana ürün bölümü** (galeri 9 görsel), blok sırası:
   - Başlık: Ayluna AyFeneri
   - Puan satırı: 4.7 ( 2467 Onaylı Kullanıcı Yorumu)
   - Fiyat satırı: 1.649,99 TL · 2.499,00 TL üstü çizili · rozet "%25 İndirim"
   - Kısa açıklama: Geceye bir ışık yak, sesini aç ve odanı kendi küçük kaçışına çevir.
   - Kargo sayacı: 🚚 · 19:32:45 içerisinde sipariş verirsen bugün kargoda.
   - Özellik kartları: Gerçek Ay Işığı Ambiyansı · Otomatik Sensörlü Aydınlatma · Uzaktan Kontrol (Kumanda / Bluetooth) · Şarjlı ve Kablosuz Kullanım · Her Odaya Uyumlu Modern Tasarım
   - Canlı izleyici sayacı: 45 kişi şu anda bu ürünü inceliyor.
   - Kargo notu: KREDİ KARTI İLE VERİLEN SİPARİŞLER HIZLI KARGO İLE ÇIKARTILMAKTADIR
   - Paket teklifi (Kaching) + satın al butonları: Sınırlı süreli teklif · 1 Adet · %20 İndirim · 1,649.99TL · 2,499.00TL · 2 Adet · İkincisi %50 İndirimli · 2,299.99TL · 4,998.00TL · Ayluna Kum Saati Lamba · 200.00TL İndirim ! · 799.00TL · 999.00TL · Yıldız Işığı Nemlendirici · 308.08TL İndirim! · 790.92TL · 1,099.00TL · GÜVENLİ ÖDEME İLE AL · Kapıda Ödeme ile Sipariş Ver
   - Ödeme logoları: Amex, Diners, Discover, JCB, Mastercard, Visa
   - Teslimat zaman çizelgesi: 18 Ekm · Siparişiniz Oluşturuldu · 19 Ekm - 20 Ekm · Kargonuz Hazırlandı · 21 Ekm - 23 Ekm · Evinize Teslim Edildi
   - Güven şeridi: 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi
   - Yapışkan sepet çubuğu: Ayluna AyFeneri · 1,649.99TL · 2,499.00TL · Sepete Ekle
   - Kısa yorum kaydırıcısı (3 yorum): Ambiyansı inanılmaz değiştirdi. Ay yansıması çok gerçekçi ve ışık tonu göz yormuyor. · Mehmet L. · Gece kalkınca sensör otomatik yakıyor, büyük rahatlık. Kumanda ve Bluetooth’un hepsi tek üründe olması çok iyi · Gülsüm S. · Şarjlı olması harika; istediğim yere taşıyorum. Hem dekor gibi duruyor hem de gerçekten işe yarıyor · Zeynep R.
   - Açılır: Teknik Özellikler: Güç Kaynağı: Dahili batarya · Stil Seçenekleri: Kumandalı, Bluetooth, Sensörlü · Voltaj: ≤ 36V · Boyut: 70 × 72 × 242 mm · Modelleme: Geometrik üç boyutlu tasarım · Tarz: Modern ve sade · Giriş Voltajı: 5V – 1A · Nominal Güç: 5W · LED Gücü: 1.5W (5×0.2W LED modülü + 1×3W LED modülü) · Hoparlör Gücü (Bluetooth model): 4 Ω, 3W · Batarya Kapasitesi: 2400 mAh
   - Açılır: Kutu İçeriği: Masa Lambası × 1 · USB Kablo × 1 · 16 ülke için uyumlu adaptör/başlık × 1 · Uzaktan Kumanda × 1
   - Açılır soru: Hoparlör olarak kullanabilir miyim ?
   - Açılır soru: Ay ışığı ne kadar belirgin?
   - Açılır soru: Hediyem zamanında yetişir mi?
   - Açılır soru: Hep fişe mi takılı olucak?
5. `eba88da5-80ac-47fc-aa75-997cfe7b2e59` — Yorum ekran görüntüsü kaydırıcısı: Ayluna'dan Alışveriş yapanlar çok mutlu ☺️ [6 görsel: WhatsApp_Image_2026-01-31_at_23.23.27_91fc5e…, WhatsApp_Image_2026-01-26_at_17.14.10.jpg, WhatsApp_Image_2026-01-26_at_17.21.47.jpg …]
6. `image_banner_Ae7wdz` — GIF afiş + başlık: Gece odanı AY'dınlatsın · GÜN BİTİNCE HERKESİN BİR FENERİ OLMALI. [1 görsel: Grselden_Video_Oluturma-ezgif.com-video-to-g…]
7. `8beb6911-28c6-482c-976a-e5421ad3e8df` — Özellik satırları (4 başlık + görsel): Gerçek Ay Işığı Ambiyansı · Duvara yansıyan ay görüntüsüyle bulunduğun ortamı anında daha sıcak, sakin ve dekoratif hale getirir. · Otomatik Sensörlü Aydınlatma · Hareketi algıladığında otomatik yanar; gece düğme aramadan güvenle yürümeyi sağlar. · Uzaktan Kontrol · Işığı yataktan kalkmadan aç/kapat, modları yönet. Uygun modelde Bluetooth ile daha fazla kontrol. · Şarjlı ve Kablosuz Kullanım · Dahili batarya sayesind … [1 görsel: ChatGPT_Image_26_Oca_2026_16_34_42.png]
8. `image_with_text_8UNBF8` — Görsel + metin + buton: Ay Işığı Ambiyansı, Tek Dokunuşla · Ayluna, duvara gerçekçi ay yansıması vererek bulunduğun alanı anında daha sıcak ve huzurlu hale getirir. Yumuşak ışığıyla gece kullanımı için idealdir. · Huzurlu Ambiyansı Keşfet [1 görsel: ChatGPT_Image_26_Oca_2026_16_49_38.png]
9. `collapsible_content_7zjVTU` — SSS (açılır): SSS, 8 soru (aşağıda)
10. `b321ab88-2b59-4dba-bade-54885c874ca5` — Ayraç
11. `17694466126b1e0319` — Loox yorum uygulaması (iframe; ayrıntı aşağıda)
12. `footer` — Altbilgi (global): %5 indirim için e-posta aboneliği, ödeme logoları, politikalar

### Paket teklifi, geri sayım, kargo

- **Paket (Kaching):** Sınırlı süreli teklif · 1 Adet · %20 İndirim · 1,649.99TL · 2,499.00TL · 2 Adet · İkincisi %50 İndirimli · 2,299.99TL · 4,998.00TL · Ayluna Kum Saati Lamba · 200.00TL İndirim ! · 799.00TL · 999.00TL · Yıldız Işığı Nemlendirici · 308.08TL İndirim! · 790.92TL · 1,099.00TL
- **Geri sayım:** üst şerit "Bugüne Özel %20 İndirim 01 SAAT : 01 DK : 36 SAN" (her yüklemede yeniden başlar); kargo sayacı "… içerisinde sipariş verirsen bugün kargoda" (15:00'e sayar)
- **Duyuru şeridi:** 3D Güvenli Ödeme İle Satın Al Ertesi Gün Kargoda
- **Güven şeridi:** 1 Yıl Garanti • Ücretsiz Kargo • 90 Gün Para İade Garantisi

### SSS

**Kaynak: `main`**

- **Hoparlör olarak kullanabilir miyim ?** Tabikide evet gelişmiş uzaktan bağlantı özelliği sayesinde telefonunuzdan bağlanarak dilediğiniz müziği açabilir ve evinizin ambiyansını daha üst seviyelere çıkartabilirsiniz.
- **Hediyem zamanında yetişir mi?** Tüm Türkiye'ye hızlı kargo ile 2-5 gün arasında kargolama yapmaktayız her gün kargo çıkışlarımız yapılmaktadır içiniz rahat bir şekilde satın alabilirsiniz.
- **Ay ışığı ne kadar belirgin?** Ürünümüzde en güncel projeksiyon çipi mevcuttun hd kalitede yansıtma yapar Gökyüzünü odanıza taşımak için bir adım uzaktasınız.
- **Hep fişe mi takılı olucak?** Tabikide hayır :)2400mh bataryası sayesinde uzun süre şarjlı bir şekilde istediğiniz ortamda kullanım sağlayabilirsiniz.

**Kaynak: `collapsible_content_7zjVTU`**

- **Bu modelde hangi özellikler var?** Bu modelde hareket sensörü, uzaktan kumanda, Bluetooth hoparlör ve şarjlı (kablosuz) kullanım özelliklerinin tamamı birlikte bulunur.
- **Hareket sensörü nasıl çalışır?** Sensör, hareket algıladığında ışığı otomatik olarak açar. Belirli bir süre hareket algılamazsa ışık kendiliğinden kapanır. Gece koridor, yatak yanı ve çocuk odası kullanımında çok pratiktir.
- **Kumanda ile neleri kontrol edebilirim?** Kumanda ile ışığı açıp kapatabilir, uygun modlarda ışık ayarlarını yönetebilirsin. Günlük kullanımda özellikle yataktan kalkmadan kontrol için idealdir.
- **Bluetooth hoparlöre nasıl bağlanırım?** Telefonunun Bluetooth ayarlarını aç, cihaz listesinden ürünü seç ve eşleştir. Eşleştirdikten sonra müzik, meditasyon sesleri veya video sesleri hoparlörden oynatılabilir.
- **Ürün şarjlı mı, prizde mi çalışır?** Ürün dahili bataryalıdır (2400 mAh). USB ile şarj edilir ve şarj olduktan sonra kablosuz şekilde kullanılabilir.
- **Şarjı ne kadar gider?** Kullanım süresi; ışık parlaklığı, sensörün ne kadar sık devreye girdiği ve Bluetooth kullanımına göre değişir. Standart kullanımda günlük ihtiyaçlar için yeterli performans sunar.
- **Gece kullanımında göz yorar mı?** Hayır. Yumuşak ve loş LED ışık verdiği için gece kullanımına uygundur. Gece kalkışlarında ortamı rahatsız etmeden aydınlatmaya yardımcı olur.
- **Çocuk odasında kullanmak güvenli mi?** LED aydınlatma düşük ısı üretir. Bu nedenle gece lambası olarak güvenli bir kullanım sunar. Yine de şarj/kablo işlemlerini çocukların tek başına yapmamasını öneririz.


### Yorumlar

- **Sayfada yazan:** "4.7 (2467 Onaylı Kullanıcı Yorumu)" (sabit metin)
- **Loox gerçek:** 43 yorum, ortalama 4.9 (dağılım: 5★×39, 4★×2, 3★×2); ilk 20 yorumun tarihleri: 31.03.2026 ×1, 26.02.2026 ×1, 20.02.2026 ×2, 12.02.2026 ×4, 26.01.2026 ×11, 21.05.2026 ×1; "Doğrulanmış" etiketi: 4
- **Loox örnek:** "Çok beğendim çok güzeldi hatta yine sipariş vereceğim arkadaşlarım da istedi kalite harika özenle yapılmış çok beğendim ses kalitesi de güze …" / "Memnun kaldığım nadir ürünlerden birtanesi teşekkür ediyorum" / "En başta görüntüsüyle kalitesiyle çok güzel bir ürün bluetooth ile bağlanıp müzik dinleme özelliği harika ışıklı fener insana huzur veriyor …" / "Kumandası çalışmıyor çalışan aksam sadece projektör hoparlör ve ışıklandırma kumandayla kontrolü 0 vermeme yakın sipariş ettiğim için geri i …"

### Açıklama (body_html)

- Boş. Ürün metni yalnız tema bölümlerinde.

### Sorunlu iddialar

- **Uydurma puan:** Sayfa "4.7 (2467)"; Loox gerçek: 43 yorum, 4.9 (39×5, 2×4, 2×3). Görsel 5 (Ayşe K.) ve 8 (6 kart, "Doğrulanmış Alıcı") uydurma yorum kartı.
- **Teyitsiz teknik:** "Otomatik Sensörlü Aydınlatma" + SSS "hareket sensörü, kumanda, Bluetooth ve şarjlı kullanımın tamamı birlikte" ↔ teknik tablo "Stil Seçenekleri: Kumandalı, Bluetooth, Sensörlü" ve "Hoparlör Gücü (Bluetooth model)" (ayrı modeller gibi). Gerçek yorum: "Kumandası çalışmıyor".
- **Kutu çelişkisi:** Tablo: Masa Lambası + USB kablo + "16 ülke için uyumlu adaptör" + kumanda ↔ görsel 4: "Lamba + Kumanda".
- **Sağlık:** Görsel 6 "UYKU MODUNU AÇ ODAYI SAKİNLEŞTİR", yorum kartı "uykuya dalmak kolaylaştı", SSS "meditasyon sesleri", "Gece kullanımında göz yorar mı? Hayır".
- **Fiyat çelişkisi:** Dört farklı oran: rozet "%25", paket "%20", üst şerit "%20", görsel 2 "Sepette %25 Otomatik İndirim"; gerçek %34 (1.649,99/2.499). "2 Adet · İkincisi %50" 2.299,99 TL (hesap 2.474,99 TL).
- **Teyitsiz teknik:** "en güncel projeksiyon çipi mevcuttun hd kalitede" (yazım hatası + teyitsiz), 2400 mAh, 5 W.
- **İade:** "90 Gün Para İade Garantisi".

