# Ayluna · LunaDream depo denetimi

Dal `ayluna-imza-onizleme`, son commit `0d61008` (17 Ekim 2026 14:53 +0300). Salt okuma: depoda hiçbir şey değişmedi.
Kısaltmalar: **IDX** = `onizleme/index.html`, **ISK** = `onizleme/iskelet.html`, **DC** = `canvas/Main.dc.html` (kullanıcının seçtiği pano),
**SIP** = `araclar/shopify-kaynak/ayluna-siparis.liquid`. Öteki `.liquid` dosyaları adlarıyla anılıyor; hepsi `araclar/shopify-kaynak/` altında.

## 0. Geçmiş ve hangi dosyanın esas alındığı

- Sıra: `165908a` DC eklendi (11:00 UTC) → `ffe5454` Shopify bölümleri (11:03) → `45fe398` kartla öde, teslimat (11:23) → `23482ae` ISK (11:39)
  → `ddf938b` "dün satılan, stok alarmı, bant" (11:48) → `0d61008` devir notu (DEVAM.md, DC'nin seçildiği yazıyor).
  **Shopify bölümlerinin hiçbiri DC'den türetilmedi.** Hepsi IDX ile ISK karışımından geliyor.
- Esas alınan dosya üç tane:
  1. DC: seçilen tasarım.
  2. ISK: Shopify CSS'inin kaynağı (`araclar/shopify-derle.py:16` CSS'i `iskelet.html`'den okuyor).
  3. IDX: DEVAM.md "CSS index.html'den otomatik alınır" diyor. **Bu bilgi yanlış**, derleyici IDX'i hiç okumuyor.
- `shopify/*.txt` güncel. Kaynakları karalama klasöründe yeniden derledim: 15/15 bölüm "TAMAM", çıktılar birebir aynı.
- `araclar/dc-onizle.js:6` yazı tipi yolu `/home/claude/cloud/...` olarak sabit. Bu ortamda (`/home/user/cloud`) çalışmaz.
  Ayrıca `araclar/p.html`'i depo klasörüne yazıyor (`:35`).

## 1. Tasarım değerleri (token) karşılaştırması

| Konu | IDX | ISK | DC (seçilen) |
|---|---|---|---|
| Token sistemi | `:root` değişkenleri (IDX:16-22): krem, yuzey, cizgi, lac, gece, gece2, metin, soluk, gSoluk, gMetin, amber, amber2, `--e` | IDX ile aynı (ISK:16-22). Derleyici aynısını `#ay-id` içine kopyalıyor (`shopify-derle.py:46`) | **Değişken yok**, her renk elle yazılmış (DC:14-139 ve satır içi stiller) |
| Ana renkler | #F6F1E9 / #FFFDF9 / #E3D8C7 / #1A2142 / #141A36 / #0C1027 / #5C6078 / #F2A65A / #E59A4C | aynı | aynı değerler, sabit yazılmış |
| Gece metni | `--gMetin #F4EDE3`, `--gSoluk #B9BED6` | aynı | #EDE5D8 (DC:330), #F3E9DA (DC:109,444), #C9CDE0 (DC:500), #8E94B3 |
| Ek renkler | #2E6B4F yeşil, #8A4A12/#F9DFC4 rozet, #0A0D20, #7D84A6 | + #FFF0DE/#B4620F (fl), #2E9A62 nabız, #B4471F/#C4572A stok, #FFF3E6 | + #2B3463 hover, #8A7F6E etiket, #3B8A63 stok noktası, #B4651F sayaç, #EDE3D3, #232B55 |
| Yazı tipi yükleme | Kendi sunucusundan woff2: Young Serif 400 + Onest 400/600 (IDX:9-14) | aynı | **Google Fonts**: Onest 400/500/**600**/700 (DC:11-12) |
| Kullanılan ağırlıklar | 400/600 (`.serit` 700 → yüklenmemiş, kalınlık tarayıcıda sentezleniyor, IDX:126) | 400/600 | 400/**500** (`.chip` DC:28, `.serit2` DC:75)/600/**700** (`.rozet` DC:74, paket fiyatı DC:255). Shopify'da yalnız 400/600 yükleniyor (KURULUM 1, `shopify-derle.py:40-45`); `f/` klasöründe 500 ve 700 dosyaları var ama tanımlı değil |
| Gövde metni | 15px/1.5 (IDX:25) | 15px (ISK:25) | 15px/1.5 (DC:16) |
| H1 | `.odak` 54px/.95, -.03em (IDX:68) | 54px, masaüstünde 72px (ISK:444) | 50px/.95, harf harf giriş (DC:222) |
| H2 | 38px/1, -.025em (IDX:34) | 38px, masaüstünde 52px (ISK:446) | **30px**/1.06, -.02em (DC:21); kapanışta 28px |
| Seçimdeki küçük yazı | 11–12.5px (IDX:121,126,174) | ek olarak bant 9px (ISK:412) | 10.5–12.5px (DC:63,68,74,239,252) |
| Buton | min 56px, radius 16, amber (IDX:200) | aynı | min **58px**, radius 16, **lacivert**, 17px (DC:25); "nefes" halkası (DC:123-125) |
| Çip | yok | yok | min **40px**, 14px/500 (DC:28) |
| Kenar boşluğu | 18px (IDX:31) | 18px | **16px** (DC:19) |
| Bölüm arası boşluk | 64px (`.bolum` IDX:203) | 64px | 40–52px (DC:330,368,387…) |
| Köşe yarıçapı | 28 levha · 24 · 22 · 20 · 18 · 16 · 14 · 12 · 10 · 7 · 999 | + 6 (bant, stok) | 28 levha · 22 · 20 · 18 · 16 · 14 (paket/model/ödeme) · 12 (kare, şerit, input) · 10 · 8 · 7 · 999 |
| Gölgeler | kapak `0 24px 40px -20px rgba(0,0,0,.6)` (IDX:233), uçan disk `0 18px 26px -12px …,.7` (IDX:255), odak halkası `0 0 0 3px rgba(242,166,90,.35)` | + `.tus-h` halka | yüzen disk `0 12px 20px -8px …,.65` (DC:37), oynat düğmesi (DC:92), plak `0 30px 50px -20px` (DC:99), disk düğmesi (DC:96), aynı odak halkası (DC:88) |
| Eğri | tek `--e: cubic-bezier(.2,.7,.2,1)` + JS ease-in-out (IDX:632) | aynı | aynı eğri sabit yazılmış; ek olarak `ease`, `ease-in-out` (yüzen disk), `linear` (mühür, plak, kaydırma zaman çizgisi) |
| Kaydırma hareketi | JS `--p` motoru (IDX:815-824) | aynı | CSS `animation-timeline: view()` `@supports` ile korunmuş (DC:40-45, 117-122) |
| Kırılma noktaları | 430px'lik sütun (IDX:26), `@media(min-width:430px)` (IDX:337) | 430–959 ve **≥960 masaüstü ızgarası** (ISK:367-468) | **yok**: sabit `width:390px` (DC:16, 130). Tuval olduğu için akışkan değil |

## 2. Bölüm sırası

| # | IDX | ISK | DC (seçilen) | Shopify (KURULUM sırası) |
|---|---|---|---|---|
| 0 | Duyuru (374) | **Kampanya bandı** sabit, saniyeli (477) | Menü çekmecesi (146-170) | `ayluna-bant` (+ istenirse `ayluna-duyuru`) |
| 1 | Sahne, 4 kare (377) | Sahne + "1 / 4" sayacı (481, 496) | Sahne 500px, **11 kare**, yüzen disk karoları (173-212) | `ayluna-sahne` (4 kare) |
| 2 | Levha: puan, başlık, fiyat, bento, model, paket, ay kartı, ekle, ödeme, kaydırma, teslim, form (401-469) | Levha: puan + "12.000+", fiyat, **dün satılan + stok**, 6 madde, güven, model, paket, ay kartı, ekle, ödeme, kaydırma, teslim (506-581) | Levha: puan + Stokta, başlık, **4'lü özellik şeridi**, küçük model kartları, paket satırları, **ince ay şeridi**, ekle, **ödeme kartları + buton**, form, güven satırı (215-316) | `ayluna-siparis` (ISK levhası) |
| 3 | Fayda "Ekran yok…" (472) | Özellikler "dört işi var" (585) | **Müşteri fotoğraf şeridi** (319-326) | `ayluna-fayda` |
| 4 | Yorumlar, hikâye düzeni (485) | Tuşlar (595) | **Bir gece, beş an** + CTA kartı (330-365) | `ayluna-yorumlar` (hikâye düzeni) |
| 5 | Kutu (498) | Yorumlar, hikâye düzeni (608) | **Yorum duvarı** + konu çipleri (368-384) | `ayluna-kutu` |
| 6 | Dünya (512) | Model karşılaştırma (621) | **Disk plakları** "On iki masal" (387-406) | `ayluna-dunya` |
| 7 | Diski tak (522) | Kutu (636) | Avucuna sığar + kutu satırı (409-420) | `ayluna-diski-tak` |
| 8 | Bir gece (538) | Dünya / Diski tak / Bir gece (650-680) | **Annelerin videoları** (423-440) | `ayluna-bir-gece` |
| 9 | Sorular + mühür (544) | Sorular, 6 yeni soru (682) | **İade mührü kartı** (443-457) | `ayluna-sss` |
| 10 | Kardeş (559) | Kardeş (700) | SSS "Merak edilenler", açık zemin (460-470) | `ayluna-kardes` |
| 11 | Diğer ışıklar (569) | Diğer ışıklar (710) | **Odanın geri kalanı** + kategori çipleri (473-497) | `ayluna-diger-isiklar` |
| 12 | Kapanış WhatsApp (582) | Kapanış (724) | Footer: görsel + CTA + yasal + ETBİS + dev yazı (500-526) | `ayluna-kapanis` |
| 13 | Alt bilgi, tepeler (591) | Alt bilgi (732) | — | `ayluna-alt-bilgi` |
| 14 | Açık yapışkan çubuk (603) | aynı (744) | **Koyu** yapışkan çubuk (529-533) | SIP içinde `.yapis` |

## 3. Eksik analizi: DC ile Shopify arasındaki farklar

### 3a. DC'de olup Shopify'a yansımayanlar (bölüm bölüm)

1. **Galeri (sahne)**: DC'de 11 kare var (DC:577-591): Odada (gündüz→gece geçişi), seçili modelin stüdyo karesi, mağazanın 9 ürün fotoğrafı
   (`canvas/magaza/ld0-8.jpg`). Altta 48px kaydırılabilir küçük resimler, köşede "n/11" sayacı (DC:210), gece olunca yüzen disk karoları (DC:180-182, 594-600).
   `ayluna-sahne` ise 4 sabit `image_picker` kullanıyor (sahne:76-86): `product.media` döngüsü, model karesi, sayaç ve karolar yok.
   Menü düğmesi DC'de kendi kategori çekmecesini açıyor; liquid'de Dawn'a özgü seçiciye tıklıyor (sahne:18), Horizon temada çalışmayabilir.
2. **Levhanın başı**: DC'de büyük fiyat satırı yok; fiyat paket satırlarında ve ödeme kartlarında görünüyor. Alt başlık "Masal projeksiyonlu gece lambası" (DC:223).
   SIP'te ise büyük fiyat ve % rozeti (SIP:108), alt başlık "Diski tak, ışığı kapat…" (SIP:356), baskı satırı (110-115), 6 maddelik liste (116-123) ve güven şeridi (124) var.
3. **Emojisiz özellik şeridi**: DC'de 4 sütun ince SVG ikon var: Yumuşak ay ışığı / 12 masal diski / Bluetooth ninni / Şarjlı, taşınabilir (DC:226-231, `.ozl` 62-66).
   Shopify'da karşılığı yok. Yerine 2 sütunlu, ikon kutulu, açıklamalı 6 maddelik `.fl` liste (daha yazılı) ve ayrı bir "Fayda" bölümü var.
   **DC'de bir hata var:** "Bluetooth ninni" modele bağlı değil, Erkek seçilince de görünüyor (DC:229). SIP'in `model_bagli` maddesi (SIP:120) bunu çözüyor; DC taşınırken bu korunmalı.
4. **Model kartları**: DC'de 2 sütunlu, 68px yüksekliğinde küçük kartlar var. İçlerinde 52px krem stüdyo fotoğrafı (`m-kiz.jpg`/`m-erkek.jpg`, DC:603-604; `.mkart` DC:69-71),
   üst yazı "Kız"/"Erkek", alt yazı "Tavşanlı · ninnili"/"Uzay Kaşifi". Shopify'da 200px yüksek, %74 genişlikte, yatay kaydırmalı oda fotoğraflı kartlar,
   tik ve amber çember var (SIP:129-137, CSS ISK:99-110). Bunun için yeni CSS ve markup gerekiyor. `kart_resim` stüdyo fotoğrafını alabilir ama 640w (SIP:132) gereksiz, ~110w yeter.
5. **Paket satırları**: DC'de satırlar 64px; seçili satır lacivert dolgulu, yazısı beyaz (DC:618). **"Kardeşe" rozeti başlığın yanında satır içi** (DC:251).
   1 lamba alt yazısı "%15 indirim" (DC:616), etiketin sağında "Hediye diskler dahil" (DC:245).
   Shopify'da satırlar beyaz; "Kardeşe" kartın üstüne asılı `.serit` olarak duruyor (SIP:166, ISK:126); 1 lamba alt yazısı "+6 hediye disk"; etiketin sağında "2 lamba seçili" yazıyor.
   Fiyat hesabı ve varsayılan 2 lamba seçimi iki tarafta da aynı.
6. **İnce ay sonu sayaç şeridi**: DC'de tek, 38px'lik şerit var (DC:75, 263-266): solda ay ikonu ve "Ekim fiyatı bitiyor", sağda saniyeli "14g 05:12:33";
   son 3 günde "Son N gün: Ekim fiyatı" (DC:660-662).
   Shopify'da bunun yerine ~70px'lik lacivert ay evresi kartı (SIP:175-182) var, **ayrıca** sayfanın tepesinde `ayluna-bant` var. Aynı sayaç sayfada iki kez çıkıyor.
7. **Ödeme seçimi ve CTA**: DC'de 62px'lik iki kart var (DC:278-285). "Kartla öde" kartında yeşil "%5 indirim" rozeti ve üstü çizili fiyat, "Kapıda öde" kartında düz fiyat var; radyo noktası yok.
   Altında **normal buton** var: "Kartla öde · ₺2.612,49" (DC:289, 763). Kapıda seçiliyken **"Kartla öde, ₺137 daha az öde"** diye bir dürtme bağlantısı çıkıyor (DC:291, 304).
   Kapıda ödemede sayfa içinde form açılıyor: "Kart bilgisi istemiyoruz" notu ve WhatsApp onay satırıyla (DC:293-308).
   Shopify'da radyolu kartlar ve **kaydırarak sipariş** düğmesi var (SIP:188-198). Dürtme bağlantısı yok; form yok, iş COD uygulamasına devrediliyor.
   DC'nin bölümlerindeki CTA'lar ise "Kapıda öde" diye sabit (DC:361, 506), kart seçiliyken bile aynı kalıyor. Bu DC'nin kendi tutarsızlığı.
8. **Kargo satırı**: DC'de "Bugün kargoda: X sa Y dk içinde sipariş ver" yazıyor; hafta içi 16:00 kesimine göre hesaplanıyor (DC:650, 664-672).
   Shopify'da tarihli 3 adımlı teslim çizgisi var (SIP:199-202). **İkisi çelişiyor:** 16:00 kesimi teyit edilmedi ve RAPOR'da kaldırılmıştı (RAPOR "16:00 kesimi kaldırıldı").
9. **Güven satırı**: DC'de CTA'nın hemen altında 3'lü: Ücretsiz kargo / **Güvenli ödeme** / 30 gün iade (DC:311-315).
   Shopify'da model seçiminin üstünde lacivert bir şerit: Kapıda öde / Ücretsiz kargo / 30 gün iade (SIP:124).
10. **Levhadaki sosyal kanıt şeridi**: DC'de 120×150 müşteri fotoğrafları ve "4,7 · 62 yorum — anneler fotoğraflarını paylaştı →" var (DC:319-326). Shopify'da yok.
11. **Bir gece, beş an**: DC'de levhanın hemen ardından geliyor. 280×460 kartlar ölçek ve opaklıkla öne çıkıyor (DC:685). 5. an "07:30 Şarja tak" (DC:682); sonda **"Bu gece başlasın" CTA kartı** var (DC:358-362).
    Shopify'da bu bölüm diski-tak'tan sonra geliyor; 3B eğik makara kullanıyor (bir-gece:63-67), 5. an "21:15 Gözler kapanır", CTA kartı yok. Shopify'da gerçek mp4 var, DC'de yalnız "VİDEO YUVASI".
12. **Yorum duvarı**: DC'de 2 sütunlu masonry, konu çipleri (Tümü/Uyku/Hediye/Kalite) ve "62 yorumun hepsini oku" bağlantısı var (DC:368-384).
    `ayluna-yorumlar` ise hikâye karuseli. Blok ayarlarında "konu" alanı hazır, ama düzen ve filtre yok.
13. **Disk plakları**: DC'de "On iki masal, tek lamba." başlığı, dönen plak ve 12 disk düğmesi var (DC:387-406). Shopify'da karşılığı yok; yerine diski-tak ve dünya bölümleri var.
14. **Avucuna sığar**: DC'de statik fotoğraf, Boyut/Pil satırları ve modele bağlı kutu satırı var (DC:409-420, 705). Shopify'da açılan kutu animasyonu var (`ayluna-kutu`).
15. **Annelerin çektiği videolar**: DC'de bölüm var (DC:423-440), Shopify'da yok. Gerçek müşteri videosu da henüz yok (DEVAM "gelirse").
16. **İade mührü kartı**: DC'de ayrı, koyu bir kart; mühür sürekli dönüyor, çevre yazısı "30 GÜN İADE · KAPIDA ÖDE · ÜCRETSİZ KARGO" (DC:443-457).
    Shopify'da mühür SSS'nin içinde, kaydırdıkça dönüyor, yazısı farklı (sss:13-18, 46).
17. **SSS**: DC'de açık zemin, başlık "Merak edilenler", 6 soru (DC:731-738). Shopify'da koyu zemin, başlık "Sorular", 4 soru (sss:57-60). Kargo cevapları çelişiyor (16:00 ile "1 iş günü").
18. **Odanın geri kalanı**: DC'de kategori çipleri, ürün sayısı ve %'li kartlar var (DC:473-497). Shopify'da `product_list` en fazla 8 ürün alıyor (diger-isiklar:34); çip ve % rozeti yok, karşılaştırma fiyatı varsayılan olarak kapalı.
19. **Footer**: DC'de kapanış görseli, "Bu gece ilk masalı birlikte izleyin." ve CTA, yasal bağlantı ızgarası, ETBİS QR, firma satırı ve harf harf yükselen "Ayluna" var (DC:500-526).
    Shopify'da kapanış WhatsApp kartı ve tepeli alt bilgi var.
20. **Yapışkan çubuk**: DC'de koyu lacivert; model küçük resmi, fiyat, "Bu fiyat 14g 05:12" ve amber buton (DC:529-533).
    Shopify'da açık krem; "31 Ekim'e kadar bu fiyat" ve lacivert buton (SIP:211-217, ISK:358-364).

### 3b. Shopify'da olup DC'de olmayanlar
- `ayluna-bant` (saniyeli sabit bant), `ayluna-duyuru`, dün satılan + stok alarmı (SIP:110-115), "12.000+ sipariş" maddesi (SIP:440), büyük fiyat satırı,
  kaydırarak sipariş, teslim çizgisi, `ayluna-fayda`, hikâye yorumları, kutu animasyonu, `ayluna-dunya`, `ayluna-diski-tak`, `ayluna-kardes`, kapanış WhatsApp kartı, tepeli alt bilgi.
- Yalnız ISK'da olanlar (Shopify'da da yok): 4 maddelik özellik bölümü, tuşlar, model karşılaştırma tablosu, ≥960px masaüstü ızgarası.
- **Kullanıcıya sorulacak:** DC baskı unsurlarını kaldırıyor. Oysa DEVAM'daki "17 Ekim, sonra" notuna göre kullanıcı dün satılan, stok ve sayaç gibi alışılmış kalıpları gerçek veriyle **istiyor**.
  DC'ye ince bir "dün satılan + stok" satırı eklensin mi, eklenecekse nereye?

## 4. Kural ihlalleri

| Kural | Durum | Kanıt |
|---|---|---|
| Emoji ikon olmasın | **Uyuyor.** Taramada emoji çıkmadı; yalnız ★ (U+2605, metin karakteri) ve → var | ★: DC:219,320 · IDX:405,494 · SIP:103 · yorumlar:48. Puan 4,7 olduğu hâlde hep 5 dolu yıldız gösteriliyor (küçük bir dürüstlük açığı) |
| Uydurma sayı / sahte aciliyet | **İhlal var** | "12.000+ sipariş": ISK:511,527 ve SIP:440 (preset). Kaynağı yok |
| | Önizlemede sabit sayılar | "23 kişi dün aldı" ISK:518; `STOK={kiz:17,erkek:24}` ISK:846. Yorumda "örnek değer" yazıyor, ama ISK Shopify'ın CSS kaynağı ve kullanıcıya gösterilen sayfa |
| | Dün satılan: kısmen gerçek | `custom.dun_satilan` metafield'ı Flow ile doluyor (SIP:76-79, gerçek). **Ama** elle girilen `dun_elle` (SIP:365) tarih taşımıyor; eski bir sayı süresiz "dün" diye görünür. Yeşil, sürekli atan "nabız" noktası (ISK:417-419, SIP:112) canlı etkinlik izlenimi veriyor |
| | Stok alarmı: gerçek | `inventory_quantity` verisinden geliyor (SIP:219), eşiğin altındaysa görünüyor (SIP:240-244). Stok takibi kapalıysa gizli. Uyuyor |
| | Ay sonu sayacı | DC:656, bant:22, SIP:293 ayın son günü 23:59:59'a sayıyor ve bir sonraki aya kendiliğinden geçiyor. **Ancak her ay gerçekten zam yapılırsa dürüst.** bant:3'teki "sahte sıfırlanma yok" yorumu bu koşula bağlı. Cihaz saatine göre çalışıyor, İstanbul saatine sabitlenmemiş |
| | Kargo saati aciliyeti | DC:664-672 "X sa Y dk içinde sipariş ver" teyit edilmemiş 16:00 kesimine dayanıyor |
| | Sabit metinler | "Stokta" DC:220 ve IDX:406'da sabit. "Tüm ürünler · 15" (DC:161) yazıyor ama listede 13 ürün var (DC:629-643) |
| Çok yazılı olmasın | **Risk** | SIP levhasında baskı satırı, 6 madde, güven, model, paket, ay kartı, ekle, ödeme, kaydırma, teslim ve alt not üst üste. ISK'ya 4 paragraflı özellik bölümü, tuşlar ve tablo eklenmiş (586-635). DC çok daha sade (4'lü şerit) |
| Mobil öncelik (390px) | IDX ve ISK uyuyor; DC tuval | DC `width:390px` sabit (16, 130). Model alt yazısı `nowrap` ve `overflow:hidden` yok (DC:239), dar ekranda taşabilir. Shopify'da ≥960 kuralları 430px sütunun içinde uygulanıyor (bkz. §5) |
| 30 gün iade (90 değil) | **Uyuyor**, "90" hiçbir yerde yok | IDX:416,451,548 · ISK:563,685 · DC:314,448,454,737 · SIP:370,394 · sss:45-47 |
| Yorum sayısı Loox'tan gelsin | Liquid kısmen uyuyor | `loox.avg_rating`/`num_reviews` okunuyor (SIP:63-70, yorumlar:8-15). Metafield yoksa ayardaki sabit **"62"** sessizce görünüyor (SIP:359, yorumlar:93). Tipli metafield ise `round` için `.value` gerekebilir. DC'de sabit: 219, 320, 371, 383 ("62 yorumun hepsini oku" bağlantısı `#`). IDX:405,494, ISK:510,617 |
| Dokunma alanı ≥44px | **İhlal var (DC)** | `.chip` 40px (DC:28); dürtme bağlantıları 36px (DC:291) ve 32px (DC:304); footer bağlantıları ~31px (DC:511-514); çekmece bağlantılarında yükseklik yok (DC:163-165); puan bağlantıları (DC:219,320); "Instagram →" (DC:426). IDX/Shopify'da `.linkler a` ≈43,5px (IDX:340, alt-bilgi) |
| | Klavye erişimi | Kaydırma düğmesinin `click` dinleyicisi yok, Enter ile sipariş verilemiyor (SIP:325-329, IDX:701-705) |
| Mobilde gövde metni ≥16px | **İhlal var (hepsinde)** | Taban 15px: IDX:25, ISK:25, DC:16, `shopify-derle.py:47`. Açıklamalar 11–12.5px: DC:63 (11.5), 68 (11), 74 (10.5), 239, 252, 350 (10.5); IDX:39, 93, 121, 174 (11.5), 179; ISK:412 (**9px**), 431; SSS cevapları 14.5px (IDX:307, DC:466). Input'lar 16px, bu doğru |
| Türkçe büyük harf (i/İ) | Düşük risk | Tek `text-transform:uppercase` DC:68'de; şu an "Model/Paket/Ödeme" etiketlerine uygulanıyor, i harfi yok. `lang="tr"` var (DC:2). Shopify temasında `<html lang>` "tr" olmalı. Büyük harfle yazılmış metinlerde İ doğru: DC:153,350,448, sss:46, ISK:685 |
| Animasyon yalnız transform/opacity | **İhlal var** | DC:58 `left` geçişi (anahtar topuzu; JS DC:747); DC:25,56-57,69,73,76 background/color/border-color; DC:96 outline-color. IDX/ISK:191-192 `max-height` (form); IDX:253 `border-radius` kaydırmayla değişiyor (dunya, liquid'e de geçiyor); IDX:333 `top` kaydırmayla değişiyor (`.tepeler .ay`, alt-bilgi'ye geçiyor); IDX:279 box-shadow; IDX:114 border/background; ISK:401 background |
| prefers-reduced-motion | Genelde uyuyor | IDX:366-368 ve ISK genel kapatma; Shopify'da her bölüme ekleniyor (`shopify-derle.py:151`), JS'te `az` kontrolü var. DC:139 sınıf listesi tutuyor, ama `.plus` dönüşü (115) ve `:active` ölçekleri dışarıda. Sonsuz döngüler: DC nefes/yüzen/mühür/plak, ISK nabız (418); azaltılmış harekette kapanıyorlar |

## 5. Shopify `.liquid` teknik kalitesi

**Şema**
- 15/15 bölüm derleyici denetiminden geçiyor: JSON, yinelenen id ve range adımları temiz.
- Siparişte artık bir "Bento" başlığı kalmış; altında ayar yok, hemen yeni başlık geliyor (SIP:362).
- `product` nesnesine dayanan bölümlere `"enabled_on": {"templates":["product"]}` eklenmeli: SIP, kardes, diski-tak.
- `id="siparis"` ve `id="yorumlar"` sabit (SIP:99, yorumlar:24). Bölüm iki kez eklenirse kimlikler çakışır.

**Bölüme kapsanmış CSS**
- `#ay-{{ section.id }}` öneki doğru çalışıyor.
- **Hata:** derleyici sınıfları şablonda geçen herhangi bir kelimeyle eşliyor (`shopify-derle.py:53-54, 76`). JS'teki `model`, yorumdaki `sayfa`, `{% form` gibi kelimeler gereksiz kurallar getiriyor.
  Örnekler: kardes.txt:62'de `.sayfa` ve `.model`, sahne.txt:49'da `.dunya`.
- @font-face her bölümde 6 kez tekrar ediyor (15 bölümde 90 tanım). Toplam çıktı ~207 KB, sipariş tek başına 55 KB satır içi.
- **Masaüstü yarım taşınmış:** `.ay-ic{max-width:430px}` (`shopify-derle.py:50`) var, ama ISK'nın ≥960 kuralları da geliyor.
  Sonuç: `.odak` 72px, `.h2` 52px ve `.fl` 3 sütun 430px'lik sütunun içinde (siparis.txt:241, ötekiler aynı satır düzeninde). DEVAM'da "öncelikli" denen masaüstü düzeni Shopify'da yok.
- **Hata:** `ayluna-bant` yapışmıyor. `position:sticky` iç `div`'de (bant:8); onu saran `.shopify-section` sarmalayıcısı bant kadar yüksek olduğundan kayacak alan kalmıyor.
  Kural `#shopify-section-{{ section.id }}` seçicisine taşınmalı.

**JS ayrımı**
- Her bölüm kendi IIFE'si içinde ve sorguları kendi kök öğesine sınırlı.
- Bölümler arası bağ `window.AylunaModel`, `window.__aySiparisVar` ve document olaylarıyla kuruluyor (`ayluna:model|paket|siparis|kardes-gorunur`).
- `shopify:section:unload` temizliği yok. Tema düzenleyicide yeniden çizimde eski düğümlere bağlı dinleyiciler birikir; yalnız kutu:50, yorumlar:78 ve sss:33 olayları ele alıyor.

**Varyant ve fiyat mantığı**
- Fiyat, karşılaştırma fiyatı, %, adet fiyatı ve kazanç varyanttan hesaplanıyor. İyi. Sorunlar:
  1. **URL'deki `?variant=` yok sayılıyor** (SIP:23-41, 237). Meta reklamı Uzay Kaşifi'ne link verse bile sayfa ilk modelle açılıyor.
  2. `bul()` eşleşme bulamazsa sessizce `V[0]`'ı döndürüyor (SIP:238). Seçenek adında yazım hatası olursa sepete yanlış varyant gider.
  3. `available` alanı JSON'a yazılıyor ama kullanılmıyor. Tükenmiş varyantta da kaydırma çalışıyor; "Stokta/Tükendi" yazısı seçim değişince güncellenmiyor (SIP:104).
     Canlı sitedeki "Tükendi + Sepete ekle" sorunu sürüyor.
  4. `kart_kod` boş olsa bile sayfa %5 düşük fiyatı gösteriyor (SIP:82, 190, 196). Ödemede tam fiyat çıkıyor.
  5. İndirim kodu ödeme yöntemine bağlı değil. Ödeme sayfasında kapıda ödeme seçilse de geçerli olur.
  6. Diski tak'taki "masal başına" fiyatı `selected_or_first_available_variant` ile hesaplanıyor (diski-tak:15). İlk varyant 2 lamba ise yanlış çıkar.

**COD (kapıda ödeme) uygulaması bağlantısı**
- `document.querySelector(COD).click()` kullanılıyor (SIP:314-317).
- Ürün formu gizli ve içinde "Sepete ekle" düğmesi yok (SIP:94, 204-207). Uygulama kendini bu düğmeye göre yerleştiriyorsa hiç çizilmeyebilir; seçici `null` döner ve akış sessizce `/checkout`'a düşer.
- "Birlikte al" ürünü `/cart/add.js` ile ekleniyor, ama "hemen al" tipindeki COD formları onu almayabilir (KURULUM 5 bunu kabul ediyor).
- Gerçek uygulamayla (Releasit/EasySell vb.) denenmeli ve seçici bulunamazsa uyarı verilmeli.

**Performans**
- Sahnede LCP görseli `eager` + `fetchpriority=high` + srcset ile doğru yükleniyor (sahne:25). Ama gece görseli de `eager` (sahne:28), ilk ekranın boyutu ikiye katlanıyor.
- Model değişince `srcset` siliniyor (sahne:60, dunya:35); hep 1080w indiriliyor.
- Bir gecedeki 5 video `autoplay preload="metadata"` (bir-gece:44). Ekranda olmayanlar da indirilmeye başlıyor; `preload="none"` olmalı ve oynatmayı yalnız IO başlatmalı.
- Fontlar `asset_url` ile kendi sunucumuzdan geliyor, bu doğru. Ama başlık fontu için `preload` yok. DC'nin Google Fonts bağlantısı (DC:11-12) Shopify'a taşınmamalı.

## 6. Yer tutucular ve teyit edilmemiş bilgiler

**Yer tutucular**
- `[X] cm` / `[X] saat`: DC:414-415, IDX:506, ISK:644, kutu:68 (varsayılan değer).
- `[yaş]`: DC:733, IDX:554, sss:60.
- `[Ölçülen süre eklenecek]`: ISK:691.
- `ETBİS [QR]` ve `[Firma unvanı] · [Adres] · WhatsApp: [numara]`: DC:517-518.
- "VİDEO YUVASI": DC:350, 435. "Annelerin videoları" bölümü müşteri **fotoğraflarını** video gibi gösteriyor (DC:714-718).
- `href="#"` bağlantılar: yasal sayfalar DC:511-514, Kargo takip/İade/WhatsApp DC:163-165, tüm yorumlar DC:383, Instagram DC:426; WhatsApp IDX:586, ISK:727.

**Teyit edilmemiş bilgiler**
- Kartla ödemede %5 (her yerde var; KURULUM'da da teyit bekliyor).
- 4,7 · 62 yorum; "Satın aldı" etiketi (yorumlar:111 varsayılan `true`).
- 12 diskin adları; 2 lamba paketinde hediye disk sayısı (DC:405 "her siparişe 6 hediye").
- Teslimat: 1 iş günü / 3-7 gün; kargo firmaları Aras·DHL·PTT·Track123 (SIP:394, sss:59); **16:00 kesimi** (DC:650, 735).
- "12.000+ sipariş" (ISK:511, SIP:440); "1 yıl garanti" (ISK:563, 685); "genelde 2 saat içinde dönüyoruz" (kapanis:37, IDX:585).
- "Şarj olurken de çalışır" (SIP:438, ISK:525); "LED ısınmaz / Düşük ısılı LED" (SIP:439, ISK:526, 591); "Hareket sensörü yok" (ISK:689); "Güvenli ödeme" (DC:313).
- Disklerin küçük parça uyarısı (ISK:693); ücretsiz kargo; fiyatlar ve yaş aralığı.

## 7. Önerilen sıra (kısa)

1. Esas alınacak tek dosyayı belirle: DC. `shopify-derle.py` CSS'i DC'nin değerlerinden (token'a çevrilmiş hâliyle) alsın. DEVAM.md'deki "index'ten" bilgisini düzelt.
2. SIP levhasını DC'ye göre yeniden yaz: 4'lü şerit (modele bağlı), küçük stüdyo model kartları, satır içi "Kardeşe" rozeti, ince sayaç şeridi,
   ödeme kartları + normal buton + dürtme bağlantısı, CTA altında güven satırı, sosyal kanıt şeridi. Kaydırma düğmesini ve 12.000+ maddesini kaldır.
3. Sahnede `product.media` döngüsü, model karesi ve n/N sayacı.
4. Yeni bölümler: yorum duvarı, disk plağı, avucuna sığar, iade kartı, kategori çipli ürün rafı, DC footer'ı. Bant: ya kaldır ya sticky hatasını düzelt (kullanıcı kararı).
5. Hatalar: `?variant=` desteği, `available` kontrolü, kart kodu boşken %5'i gizle, kaydırma ya da butonun klavye erişimi, bant sticky, derleyicinin kelime eşleşmesi.
6. Tipografi: taban 16px; 12px altını kaldır; çipleri ve bağlantıları 44px yap; font 500/700 ya yükle ya kullanma.
7. Teyitler gelince yer tutucuları doldur; teyit gelmeyen iddiaları sayfadan çıkar.
