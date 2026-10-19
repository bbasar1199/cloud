---
name: "ayluna-tasarim"
description: "Ayluna (ayluna.shop) Shopify sitesi, tema bölümleri, ürün sayfaları, ürün metinleri veya Ayluna görselleri/Instagram kiti üzerinde çalışırken kullan."
---

# Ayluna tasarım kuralları (v2 · 17 Ekim 2026)

Ayluna, Türkiye'de Meta reklamıyla telefondan gelen annelere ve büyükannelere gece lambası, projektör ve nemlendirici satıyor. 15 ürün var; cironun çoğu LunaDream'den geliyor.

**İşe başlamadan:**
1. Depo `bbasar1199/cloud`, dal `ayluna-imza-onizleme`.
2. Sırayla oku: `ayluna-imza/DEVAM.md`, `ayluna-imza/RAPOR.md`, `ayluna-imza/TASARIM-BILGISI.md`. Görünüş Main'den, kurallar TASARIM-BILGISI'nden alınır.

**Güncel ve seçilmiş tasarım:**
- "Ayluna İmza Tasarım" tuvalindeki `project/Main.dc.html` (https://claude.ai/artifact/CHmRtH4tjbapGmPtuQGsTH).
- Depodaki kopyası: `ayluna-imza/canvas/Main.dc.html`.
- Eski "H yönü / Bricolage + Figtree" bilgisi geçersiz.

## Çalışma biçimi
- Türkçe, kısa yaz. İstenmeyen dosya ya da açıklama yok.
- Tema kodu kopyala-yapıştır `.txt` dosyası olarak verilir. Zip, index ve rehber yalnız istenirse.
- Önce mobil (390px), sonra masaüstü.
- Beğenilen bölüm silinmez, geliştirilir.
- **Her bölüm kararı önce eleştirmen ajana denetletilir.** Ajan kullanıcıyı taklit eder. Depoda hazır tanımı var: `.claude/agents/ayluna-elestirmen.md`; kişilik `TASARIM-BILGISI.md` §1a'da. Ajanın en beğendiği 3 fikir kullanıcıya ayrı ayrı gösterilir.
- **Öğrenme döngüsü:** kullanıcı bir şeyi düzeltince aynı turda `TASARIM-BILGISI.md` → "Düzeltme günlüğü"ne yazılır. Kalıcıysa bu beceriye de işlenir. Aynı düzeltme ikinci kez gelmemeli.
- **Hafıza depodadır:** bulut konteyneri her oturumda silinir. Karar ve öğrenilenler commit'lenip dala gönderilir.
- Her değişiklikten sonra telefon genişliğinde ekran görüntüsü alıp bakılır (`araclar/ekran-goruntusu.js`, `araclar/dc-onizle.js`).
- Kararlar `DEVAM.md`'ye ve tuval notuna yazılır. Kullanıcı yorum bırakmıyor; iz yalnız orada kalır.

## Kullanıcının zevki
- **Sevmez:**
  - emoji ikon
  - çok yazılı, boğucu sayfa
  - "Shopify teması gibi" sıradan düzen
  - tamamen koyu tema
  - uydurma sayı ya da sayaç
  - abartılı efekt, yıldız animasyonu
  - süsle başlayan tasarım
- **Sever:**
  - "acayip ama sıkmayan" tarz
  - doğa gibi uyumlu hareket
  - güven veren, satan sayfa
  - paket
  - ay sonu fiyat sayacı (her ay zam yapıyor)
  - sosyal kanıt
- Alışılmış satış kalıpları (sayaç, stok, "dün satılan") gerçek veriye bağlanır.
- **Fayda:** durağan emoji ya da ikon listesi yok. Yerine animasyonlu "Sihirli Özellikler" geliyor.
- **Sayfa sırası (LunaDream):** sahne galeri (logo fotoğrafın üstünde) → LunaDream + puan (aynı satır) → fiyat + Stokta → kampanya sayacı → Sihirli Özellikler → Model (Kız tavşanlı ninnili / Erkek robot ninnili) → Paket → stok ve "dün X aile" satırları → iki buton → teslim çizelgesi → Videolar → Bir gece → Yorum duvarı → Diskler → Odası böyle görünecek → İade → SSS (ilk soru: kutudan ne çıkıyor).
- **Yazı ölçeği v3 (kesin):** ürün adı 28 · bölüm başlığı 22 · büyük rakam 32 · paket adı 17 / fiyatı 18 · fiyat 20 · gövde 15 · açıklama 14 · not 13 · etiket 12 · buton 16/14. Ara boyut yok. Kullanıcı büyük ve düzensiz yazıyı iki kez düzeltti.
- **Az yazı, iç içe değil:** başlığı olan bölümde üst etiket yok; tek cümle açıklama; kart içinde kart yok; gölge yok.
- **Model ve 2'li paket:** model kartı yalnız Kız / Erkek. 2 Adet (varsayılan) seçilince paketin altında küçük seçim: "1. lamba [Kız/Erkek] · 2. lamba [Kız/Erkek]". Tur 25'ten beri: model kartı = 1. lamba; 2. lamba, 2 Adet kartının içinde çiple seçilir (hap segment yok).
- **Eleştirmen önerileri toplu uygulanmaz;** en iyi 3 fikir kullanıcıya gösterilir, kullanıcı seçer (kullanıcı toplu uygulamayı geri aldırdı).
- **Fiyat satırı:** fiyat + üstü çizili eski fiyat + "%X indirim" rozeti. Kartla fiyat başlıkta yok, yalnız ödeme butonunda.
- **Müşteriye iç gerekçe yazılmaz** (toptancı, maliyet, zam sebebi).
- **Boşluk ve geçiş:** bölüm arası 36px; koyu bölümler yuvarlak köşeli panel; bölümler kaydırınca hafifçe (20px, saydamdan) gelir.
- **Bölümler hep ayrı ve görünür** (17 Eki, Tur 16 düzeltmesi): yeni deneme içerik kesmez, bölümleri hikâye/karusel içine toplamaz. Tasarım turu iskelete ve görünüşe dokunur: bölüm yüzeyleri, aralık ritmi, sıcaklık. Yakınlık net olur: grup içi sıkı, bölüm sınırı yüzey değişimiyle okunur. Soğuk ince çizgili beyaz kartlar yerine sıcak dolgulu yüzeyler. Kullanıcının tarifi: "soğukluk, düzensizlik; tam yakın değil uzak değil".
- **Baskı unsurları istenir** (sayaç, stok, dün satılan) ama yalnız gerçek veriyle; veri yoksa gizlenir.
  - Sayaç = sayfanın en üstünde ince amber şerit "Bugüne özel fiyat 06:26:42", her gece 23:59'da (İstanbul) sıfırlanır. Koşul (yalnız sahibine söylenir): gün içinde zam gelse de o günün fiyatı 23:59'a kadar korunur.
- **Disk görselleri:** mağaza afişinden kesilip yapay zekâ ile netleştirilmiş diskler (Real-ESRGAN çizim modeli, 512px); sadece büyütmek yetmez. Unicorn ve 2025 kutuda yok.
  - Biçim (kullanıcı seçimi): 2×2 beyaz kart. Lacivert ikon kutusu + amber ikon; sağ üstte ürüne özgü küçük canlı gösterge; altında başlık ve tek cümle. Koyu ya da amber dolu kart yok; kullanıcı renkli kartları "boğucu" buldu.
  - Açık zeminde amber yazı okunmaz: küçük etiketler `#A05A1C`.
  - 2×2 kart: ikon, başlık, tek cümle ve ürüne özgü küçük animasyon (nefes alan hale, yelpaze diskler, dolan pil, ses dalgası).
  - Yeri model seçiminden sonra.
  - Uydurma ya da teyitsiz madde yok ("+10.000 Mutlu Anne", "21 ışık modu").
- **Seçilen yön (17 Ekim): B+ Gece Postası.**
  - gece sahnesi galeri (aşağıda), büyük "LunaDream." başlığı
  - seçili kart lacivert, fiyatı amber
  - amber, basılınca çöken "Güvenli Ödeme İle Al"; çizgili "Kapıda Ödeme ile Sipariş Ver"
  - noktalı teslim çizgisi
  - Pano: `canvas/YonBPlus-GecePostasi.dc.html`.
- **Nihai tasarım (18 Eki): LunaDream E** (`canvas/LunaDreamE.dc.html`).
- **Her ürün sayfasının kendi tasarım dili** (18 Eki, kullanıcı): renk, yazı tipi, bölüm biçimi ve imza bölümü ürüne ve gerçek kitlesine göre (Galaxy USB: çocuk, ebeveyn, genç, çift). Ortak çekirdek yalnız Ayluna işareti + yazısı, satın alma akışı (kartla %5 önce, kapıda ikinci, kapıda butonunda fiyat yok), 30 gün iade, yer tutucu kuralı ve yasaklar.
- **Marka rengi sabit** (18 Eki, kullanıcı): koyu lacivert #1A2142 her ürün sayfasında; ürüne göre değişen yalnız ikinci renk ve zemin (Galaxy USB: buz mavisi #8FD3FF + #F2F4F8). Sarı kullanılmaz. Ürün gerçek renginde gösterilir (Galaxy USB beyaz).
- **Hareket:** her özellik kendi işini gösteren sakin bir döngüyle anlatılır (fiş takılır, disk döner); yıldız parıltısı gibi süs hareketi yok.
- **Kutu içeriği afişle birebir:** diskler mağaza afişinden kırpılıp gerçek hâliyle gösterilir; kutuda olmayan desen ya da aksesuar (Galaxy USB: adaptör) gösterilmez, yazılmaz.
- **Galaxy USB dili (18 Eki, kullanıcı seçti):** gümüş #D3DCEE + lacivert #1A2142, zemin #F4F5F7, açık zeminde ikinci ton #56658A; yazı Yön A'nınki: Bricolage Grotesque 800 + Figtree (Fraunces denendi, kullanıcı Yön A yazısını istedi). İmza bölüm: "Bu gece tavanda ne olsun?" sahne kartları (yazı görselin içinde). Kullanıcı sakin yönü eleştirmenin renkli önerilerine tercih etti.
- **Seçilen yönün yazı tipi ve imza bölümleri beğenilen dildir;** renk dışında bunları değiştirmeden önce sor.
- **Ürün galerisi** (18 Eki): küçük resim kutusu yok; parmakla kaydırılır, 5 sn'de kendiliğinden geçer, elle kaydırınca durur. Altında ürünün diline uygun ilerleme göstergesi: LunaDream'de geçtikçe dolan ay evreleri (sonda dolunay), Galaxy USB'de dolan film diskleri. Sayı ("1 / 4") yazılmaz.
- **Site geneli** (18 Eki): ana sayfa, sepet ve politika/iletişim sayfaları marka dilinde (krem + lacivert, Young Serif + Onest); ürün sayfaları kendi dilinde. Canlı sitenin bölüm sırası korunur, sorunlu içerik düzeltilir. Stok satırı her üründe elle (sayı + aç/kapa).
- **Sepet ek teklifleri:** "Siparişine özel" kartlar, dokununca eklenir; mağaza fiyatı düz yazı (üstü çizili değil); Hızlı Kargo teslimat seçeneği olarak.
- **Seçilen yönün düzeni korunur** (18 Eki): kullanıcı bir yönü seçtiyse sonraki turlar yalnız istenen parçayı ekler; düzeni baştan kurmak "yabancı" durur.
- **Ödeme düğmesi:** kartla %5 indirim ana butonun içinde ikinci satır ("Kartla %5 indirim dahil"); güven kutusunda kapıda ödeme övülmez, "Kartla güvenli öde" yazar.
- **Baskı:** stok, Güvenli Ödeme butonunun üst kenarındaki lacivert kurdele ("Son [N] adet", azalan ay; elle, veri yoksa yok; dokunmayı engellemez, buton ekrana girince bir kez belirir). Stok için nokta dizisi ya da oranlı çubuk yok. Fiyat satırında "Stokta" yazmaz; fiyatın altında "Dün [X] kişi satın aldı" (elle, veri yoksa gizli; fiyat düşüşünden sonra bir kez girer). Paketin altında lacivert dönen satır (ay beyazı yazı, ışık yalnız hilalde): önce hediye/disk, sonra "Bugün 16.00’ya kadar verilen siparişler aynı gün kargoda" + 16.00 sayacı (İstanbul saati; 16.00 sonrası ve hafta sonu sayaçsız "yarın / Pazartesi kargoda"). Üst şeritteki fiyat sayacı dışında yalnız bu kargo sayacı olur.
- **Sahne kartı:** ana nesne (ay, ürün) kırpılmaz; yazı onu örtecekse kartın alt şeridine iner. Işık aç/kapa sahnesinde kapalıyken yansıma görünmez.
- **İmza ürün sayfasında oda sahneleri:** yazısı görselin içinde kartlar (oda adı + o odadaki an) ve bir büyük görsel kart (hediye / avucuna sığar).
- **Disk görselleri net:** afiş kırpıntısı küçükse desen değiştirilmeden büyütülür (Flow ile; Higgsfield kullanılmaz), 384px.
- **Yeni ürün sayfasından önce canlı sayfa telefonda incelenir;** satan kalıplar (yaşam fotoğrafları, kare galeri, "Çok al az öde", büyük butonlar) korunur, çelişkili sayı ve sağlık iddiası alınmaz.
- **Bütünlük (18 Eki, kullanıcı: "her şey çok yabancı duruyor, bir bütün ve uyum yakala"):**
  - Yeni deneme, seçilen yönün (B+) dilinden çıkmaz: Young Serif + Onest; krem, lacivert ve amber; Sihirli V1; canlı sitedeki paket ve iki buton.
  - Yenilik, bölüm içinde tek bir parça olarak denenir; örnek: Bir gece kadranı. Yazı tipini ve renkleri değiştiren turlar (D; Tur 20'deki E) "yabancı" bulundu.
  - Sipariş fişi istenmiyor.
  - **Ay evresi dili** (18 Eki, kullanıcı: "yarım ay, tam ay olma efektini kullanmaya devam et"): hilal → yarım ay → dolunay, markanın motifi. Teslim çizgisinde (Bugün / Kargoda / Kapında, kaydırınca sırayla dolar) ve 30 gün mühründe (halkada 8 evre) kullanılır.
  - **Renk disiplini** (kullanıcı: "renkler birbirine giriyor, büyük marka hissi yok"):
    - Yaklaşık 12 ton. Açık yüzeyler: krem, yüzey, tek açık ton #F1E8DA.
    - Çizgiler: tek çizgi, tek kesik çizgi.
    - Yazı: lacivert, soluk, kehribar. Yeşil yalnız "Stokta" ve "Satın aldı".
    - Amber yalnız ışıkta ve ana butonda; bir ekranda tek amber blok.
    - Koyu panelde geniş amber parıltı yok (kahverengiye döner).
    - Açık ve koyu bölümler sırayla gelir.
    - Tek turuncu #F2A65A. Yalnız ışık (ay, yıldız, evre, başlık noktası) ve ana butonda kullanılır; şerit, kurdele ve seçili fiyat amber olmaz.
  - **Marka işareti:** ince daire içinde amber hilal (evre çizimi). Başta ve alt bilgide aynı kilitle kullanılır. Sayacın yanında gün bittikçe söner.
  - **Seçili durum (Tur 25):** model, paket ve 2. lamba aynı dille seçilir: 2px lacivert çerçeve ve amber dolunay noktası. Dolu lacivert seçili kart yok (kullanıcı: "bundle ve aralarında uyum yok"). Renk değişimi anlık; yalnız nokta hareket eder.
  - **Küçük ürün görselleri:** her yerde arka planı temizlenmiş stüdyo kesimi kullanılır, bej kare kullanılmaz.
  - **Küçük görsel gerçekten büyütülür:** önce büyük aslı aranır (canlı mağaza `/products/<handle>.json`); yoksa yerelde Real-ESRGAN x4plus (`araclar/gorsel/sr.py`, ücretsiz). Yumuşatıp bırakmak yetmez; Higgsfield yok.
  - **Kesimler saydam kalır:** arka planı temizlenmiş görsel hiçbir çıktıda JPEG'e çevrilmez (saydamlık siyah olur); sitede WebP, Shopify'da PNG/WebP. Teslimden önce gerçek çıktıda seçim kartlarına bakılır.
  - **Fiyat düşüşü** (kullanıcı isteği): açılışta bir kez ₺1.999,00 → çizilir → indirimli fiyat yukarıdan düşer → rozet. Sayan rakam kuralının tek istisnasıdır.
  - **Seçiciler = satır kartlar** (Tur 25, kullanıcı seçimi): model yan yana iki yarım kart; paket alt alta satır kart (görsel, ad, "%15 indirim" / "₺649,99 kazanç", fiyat, eski fiyat / "tanesi", dolunay noktası, lacivert "En avantajlı" kurdelesi); 2 Adet açılınca kartın içinde "2. lamba" çipleri; altta tek hediye şeridi "Her kutuda +6 hediye masal diski". Kemerli gece penceresi ve hap segment kullanılmaz.
  - **Ay evresi hareketi:** Bir gece'de ay her anda biraz daha dolar. Kargo takibi "Sipariş verildi"den başlar, sırayla dolar; 8 sn'lik sakin döngü, ekrana girene kadar durur. Tek seferlik animasyon kullanılmaz: tuvalde bakan olmadan biter, "çalışmıyor" sanılır.
  - **Buton altında not yazılmaz.** Kapıda butonunda fiyat da yazmaz (Tur 25). ₺80 kapıda ödeme ücreti formun özetinde ve SSS'de yazar (mevzuat: sipariş onayından önce).
  - Fiyatın altında "Ücretsiz kargo · 30 gün iade · Güvenli ödeme" gibi güven satırı yok (kullanıcı: "çok kötü duruyor").
  - Hediye diski "her kutuda +6" diye yazılır; çıplak "12 disk" yazılmaz.
  - **Yapışkan öğe** (Bir gece paneli, satın al çubuğu): hiçbir atasında `overflow:hidden` olmaz; taşma `overflow:clip` ile kesilir. Kaydırmalı bölüm telefon boyunda kaydırılarak denetlenir (tuval boyu hatayı göstermez). Panel ekranda ortalanmış kart olarak yapışır.
  - **Kaydırmaya bağlı hareket tuvalde de çalışmalı:** tuvalde pano kaymaz, tuval kayar. Sayfa kaydırmasının yanında tuvalin görünür alanı da izlenir (görünmez işaretler + IntersectionObserver, rootMargin'siz). Pano `expand: "fill"`. Sınama: `araclar/kaydirma-testi.js`.
  - **Puan ürün adının yanında** (Tur 25): solda ad, sağda yıldızlar + ortalama, altında "N yorum"; dokununca yorumlara iner. "Stokta" fiyat satırının sağ ucunda.
  - **Odası böyle görünecek** (Tur 26, "Kutudan ne çıkıyor"un yerine): iki oda posteri yan yana kayar; fotoğraf üstte, yazı altında lacivert bantta; yazı ürünün üstüne binmez; "… modelini seç" modeli seçer; altında temsilî notu. Kutu içeriği SSS'de.
  - Soru başlıkları soru işaretiyle biter.
  - Sıfırı çizgili yazı tipi kullanılmaz (Atkinson Hyperlegible Next'teki "Ø" yazım hatası gibi görünür).
- "Işığı aç/kapat" anahtarı ve saat kullanılmaz. Galeri ana ürün fotoğraflarından gelir, ama Main'deki gibi gece sahnesi çerçevesinde: lacivert zemin, üstte logo, kare poster kırpılmadan tam genişlik, kenarlarda süzülen hediye diskleri (ürünü kapatmaz), fotoğrafın üstünde küçük resimler ve "1/7", altına binen yuvarlak köşeli levha.
- **Paket ve ödeme canlı sitedeki gibi kalır:**
  - alt alta "1 Adet / 2 Adet" kartları ve altlarında "+6 Tane Ücretsiz Hediye Disk" şeridi
  - "Güvenli Ödeme İle Al" ve "Kapıda Ödeme ile Sipariş Ver" diye iki ayrı buton
  - kapıda ödeme formunu uygulama açar; kapıda ödeme ücreti ₺80
- Kullanıcı sade şablon görünümünü "sıkıcı" buluyor; karakterli, akılda kalan bir görsel dil istiyor.
- Main seçildikten sonra sadeleşti (kimin istediği kayıtlı değil). Kompakt kal, ama sıradan Shopify'a düşme; "acayip ama sıkmayan" isteği geçerli.

## Tasarım sistemi (Main.dc)
- **Renkler:**
  - krem #F6F1E9 zemin, #FFFDF9 yüzey, #E3D8C7 çizgi
  - lacivert #1A2142 metin ve açık zeminde ana buton
  - gece #141A36 / #0C1027: yalnız ürünün ışığını gösteren bantlarda, yapışkan çubukta ve alt bilgide
  - amber #F2A65A: ışık ve koyu zeminde ana buton; #E59A4C yıldız ve ikon
  - soluk #5C6078 ikincil metin
  - yeşil #2E6B4F: Stokta, %5 rozeti, kartla öde dürtmesi
  - 11px etiket için #766B5B, sayaç için #A05A1C kullan. Eski #8A7F6E ve #B4651F kontrastta kalıyor.
- **Yazı:**
  - Young Serif 400 yalnız başlıkta: H1 50px/.95, H2 30px/1.06.
  - Onest gövde 16px (Main'de 15).
  - 12px altı yazı yok. Rakamlar `tabular-nums`.
- **Şekil:**
  - Köşe: levha 28, kart 14–22, buton 16, input 12, çip 999.
  - Kenar boşluğu 16px. Gölge yerine 1px çizgi.
  - Dokunma alanı ≥48px, ana buton 58px.
- **Hareket:**
  - Tek eğri `cubic-bezier(.2,.7,.2,1)`, yalnız transform ve opacity.
  - İmza an henüz seçilmedi ("Işığı kapat" kullanıcı tarafından çıkarıldı).
  - Yeni sonsuz döngü eklenmez. `prefers-reduced-motion` desteklenir.
- **İkon:** ince çizgili SVG, ilk çizgi amber. Emoji asla.

## Sayfa akışı (ürün sayfası)
1. Galeri: gece sahnesi çerçevesinde ana ürün fotoğrafları (ışık anahtarı yok).
2. Üstüne binen karar levhası. Sırası:
   - puan ve Stokta, H1
   - 4'lü özellik şeridi
   - Model (küçük stüdyo fotoğraflı kartlar)
   - Paket: canlı sitedeki 1 Adet / 2 Adet kartları ve hediye disk şeridi
   - ince ay sonu şeridi, birlikte al
   - **İki buton: "Güvenli Ödeme İle Al" (%5) üstte, "Kapıda Ödeme ile Sipariş Ver" altta.** Kapıda ödeme ücreti ₺80 baştan yazılır.
   - güven üçlüsü, müşteri fotoğrafları
3. Bir gece, beş an.
4. Çipli yorumlar.
5. 12 disk.
6. Avucuna sığar ve kutu içeriği.
7. Videolar.
8. 30 gün iade mührü.
9. SSS.
10. Odanın geri kalanı.
11. Kapanış ve dev "Ayluna" alt bilgi.
12. Yapışkan çubuk.

## Gerçekler (uydurma yerine bunlar)
- İade 30 gün (90 değil): 14 gün yasal cayma + 16 gün Ayluna. Ücretsiz kargo. Kargo takibi Track123.
- Kargo: iş günü 16.00’ya kadar verilen sipariş aynı gün kargoda (kullanıcı, 18 Eki), sonrası ertesi iş günü; Türkiye geneli 3–7 günde teslim. Cumartesi kargo teyitsiz. Hızlı Kargo (₺79,99) "aynı gün" diye değil, öncelikli hazırlık olarak anlatılır: "Siparişin sıranın önüne alınır, öncelikli hazırlanıp kargolanır."
- LunaDream fiyatları:
  - 1 lamba ₺1.699,99 (karşılaştırma ₺1.999,00)
  - 2 lamba ₺2.749,99 (karşılaştırma ₺3.998,00)
- Diğer fiyatlar:
  - AyFeneri ₺1.649,99 / ₺2.499
  - Galaksi Ambiyans ₺1.499 / ₺2.898
  - Galaxy USB ₺1.599 / ₺1.999
  - Kum Saati ₺799 / ₺999
  - Galaksi Night ₺2.199 / ₺2.999
  - Yıldız Işığı Nemlendirici ₺849,99 / ₺1.099
- Modeller: Kız = tavşanlı, Bluetooth ninni hoparlörlü. Erkek = Uzay Kaşifi robot, hoparlörsüz. Bluetooth vaadi modele bağlanır.
- Galaxy USB (18 Eki): beyaz; kutuda projektör + 12 film diski, **USB adaptör yok**; 2'si 1 arada (projektör + gece lambası); başlık 4 cm, toplam boy 23,5 cm; 1 Adet ₺1.599 / ₺1.999, 2 Adet ₺2.399,99 (Kaching). Loox 2,0 · 7 yorum; canlıdaki "4,7 · 2467" ve "90 gün" yanlış.
- Kutu: lamba + 6 disk + 6 hediye disk + USB kablo. Unicorn diski kutuda yok; gösterilmez.
- Yorumlar: Burak G., Handan B., Abdülkerim T., Sevcan Z., Mehmet C. Puan Loox'tan çekilir (4,7 · 62, teyit bekliyor). "Elif K.", 2.467, 10.000+ ve 12.000+ uydurmadır.
- Bilinmeyen değer köşeli yer tutucu kalır: [X] cm, [X] saat, [yaş], [Firma unvanı], [numara].
- LunaDream (17 Eki teyidi): iki model de Bluetooth ninni; 3 parlaklık ayarı; her yaş için; her kutuda 6 + 6 hediye disk; boyut ve pil süresi yazılmaz; Ekim kampanyası 1–31 Ekim; tüm kartlar geçer; stok satırı elle (şimdilik 18); iade kodu Ayluna'dan, iade kargosu ücretsiz; Loox müşteri fotoğrafları kullanılabilir.

## İş verisi → tasarım kuralı
- Kapıda ödemede iade %28,6, ön ödemede %0,8. İadelerin %92'si "alıcı bulunamadı".
  - Kartla öde varsayılan ve indirimli.
  - Kapıda seçilirse toplam, teslim aralığı ve WhatsApp onayı formda görünür.
  - "Kartla öde, ₺X daha az öde" hatırlatması gösterilir.
- PTT'de iade %40. PTT öne çıkarılmaz.
- Gerçek dönüşüm sipariş ÷ oturum (≈%1,7); Shopify'ın oranı kapıda ödemeyi saymaz. Başarı teslim edilen ciroyla ölçülür.

## Dürüstlük
- Aciliyet yalnız gerçek kurala bağlanır:
  - ay sonu zammı (gerçekten varsa)
  - Shopify stok eşiği
  - Flow ile yazılan "dün satılan"
  - elle girilen sayı tarih taşır, eskiyince gizlenir
- "X kişi bakıyor", sahte geri sayım ve uydurma satış adedi yok.
- Sağlık iddiası ve teyitsiz teknik rakam yok. Sayfa vaadi kutuyla birebir aynı olur.
- **Mevzuat** (1 Ağustos 2026 değişikliği, Resmî Gazete'den doğrulandı):
  - Üstü çizili "önceki fiyat" = indirimden önceki **10 gün** içinde aynı kanalda uygulanan en düşük fiyat. Kampanya tarihleri yazılır.
  - Şartlı indirimler de bu kurala tabi: kartla %5, paket kazancı.
  - Satın alımı doğrulanamayan yorum yayımlanamaz. Olumsuz yorum gizlenemez.
- Yasal cayma 14 gündür. "30 gün iade" = 14 yasal + 16 Ayluna; yasal hak özel avantaj gibi sunulmaz.
- Sayaç İstanbul saatine göre, herkese aynı sabit tarihi gösterir; oturumla sıfırlanmaz.
- Kapıda ödeme gizlenmez. Ücretli ek önceden seçilmez.
- AI görseli "müşteri" diye sunulmaz.
- Ayrıntı: `ayluna-imza/ogrenme/arastirma.md` ve `TASARIM-BILGISI.md` §7.

## Görsel
- Ürün asla sıfırdan üretilmez. Gerçek fotoğraf referans alınır, sahne ve ışık değişir.
- Araç: Google Flow (Nano Banana Pro). İş akışı DEVAM.md'de.
- **Higgsfield'da üretim, düzenleme ya da büyütme yapılmaz, kredi harcanmaz** (kullanıcı, 18 Eki: "görselleri Flow'dan üreteceksin, Higgsfield'dan üretme"). Flow'a erişim yoksa başka araca geçilmez: istem + referans hazırlanır, kullanıcıya sorulur.
- Görselde yazı üretilmez; metin HTML'de eklenir.
- Gerçek müşteri fotoğrafı ve videosu önceliklidir.

## Teslim: çalışan site
- Köşeli yer tutucular sitede kalır, kullanıcı gerekirse doldurur; teyit için ısrar edilmez. Site tek dosya `index.html` olarak da verilir (`python3 araclar/site/site_uret.py` → `site-tek/index.html`).
- Kullanıcı (18 Eki) "tüm iskelet, her kısım tam çalışsın" der: önce denetim (bağlantı, düğme, form, sepet, ödeme, kapıda, boş hâller, politikalar, 320px), eksik listesi, hepsini düzelt; gerçek tarayıcıda uçtan uca tıklama testi geçmeden gönderme. Seçilen paket/model/seçenek sepete aynen gider. Shopify teması da aynı listeyle test edilir (`ogrenme/site-denetimi.md`).

## Shopify
- **Sıfırdan Ayluna teması** (kullanıcı kararı, 17 Ekim). Hiçbir hazır tema (Horizon, Dawn…) kopyalanmaz ya da temel alınmaz; her parça benzersiz yazılır.
- İlk kurulum zip ile yapılır, sonraki değişiklikler `.txt` olarak verilir. Şu an canlıda ChatGPT ile yapılmış bir sürüm var; o da değiştirilecek.
- Kaynak `araclar/shopify-kaynak/*.liquid` → `python3 ayluna-imza/araclar/shopify-derle.py` → `shopify/*.txt`. Kurulum: `shopify/KURULUM.txt`.
- Bölümler Main.dc'ye göre yazılır.
- Bilinen hatalar `TASARIM-BILGISI.md` §8'de.
