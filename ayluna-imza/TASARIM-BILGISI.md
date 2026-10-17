# Ayluna · tasarım bilgi dosyası

Her oturumda `DEVAM.md`'den sonra bunu oku. Ayrıntı ve kaynaklar `ogrenme/` klasöründe. Son güncelleme: 17 Ekim 2026.

**Görünüş Main'den, kurallar bu dosyadan.** Çelişkide şu sıra geçerli:
1. Kullanıcının son mesajı.
2. Bu dosyadaki kurallar (dürüstlük, mevzuat, iş verisi).
3. Seçilen pano `canvas/Main.dc.html` (görünüş ve düzen).
4. Beceriler (`beceriler/`). claude.ai'deki eski sürümler bayat; orada hâlâ "H yönü, Bricolage + Figtree" yazıyor.

`index.html` ve `iskelet.html` eski denemelerdir. Yeni iş Main'den başlar.

---

## 1. Çalışma biçimi
- Türkçe, kısa yaz. Shopify kodu kopyala-yapıştır `.txt` olarak verilir. Önce mobil (390px).
- Beğenilen bölüm silinmez, geliştirilir.
- Tasarım kararı süreci:
  1. Taslak yap.
  2. Ekran görüntüsü al ve bak.
  3. `ayluna-elestirmen` ajanına denetlet (`.claude/agents/ayluna-elestirmen.md`).
  4. Ajanın en beğendiği 3 fikri ayrı ayrı göster.
  - Hata düzeltmede bu süreç gerekmez.
- Kararlar `DEVAM.md`'ye yazılır. Kullanıcı artifact yorumu bırakmıyor (incelenen 15 artifact'ta yorum yok).

## 2. Kullanıcıyı tanı
**Kendi sözleri (DEVAM, brif, bu sohbet):**
- Sevmez:
  - emoji ikon
  - boğucu, çok yazılı sayfa
  - "Shopify teması gibi" sıradan düzen
  - tamamen koyu tema
  - uydurma sayı ya da sayaç
  - abartılı efekt
  - süsle başlayan tasarım
- İster:
  - "acayip ama sıkmayan" tarz
  - doğa gibi uyumlu hareket
  - güven veren, satan sayfa
  - paket
  - ay sonu fiyat sayacı (her ay zam yapıyor)
  - sosyal kanıt
  - 15 ürünlü mağaza hissi
  - gösteriş değil, işe yarayan iyileştirme
- 17 Ekim: alışılmış kalıplar (fayda listesi, sayaç, stok, "dün satılan") atılmaz; emojisiz ve inceltilmiş hâliyle gerçek veriye bağlanır.
- 17 Ekim: ödemede öncelik online (kartla %5 indirim), kapıda ödeme ikinci.

**Seçim geçmişi** (tuvallerden çıkarıldı; kullanıcı sözü değil):
- Eylül: 4 yön reddedildi (Nunito/mercan, Sora/indigo, Quicksand/altın, Baloo/pembe). Muhtemelen brifteki "dört deneme".
- Sonra G "önceki sürüm" olarak kaldı (Cormorant + krem + kil). I öne çıktı (Poppins, beyaz/lacivert/altın).
- 17 Ekim: Tur 1 Main seçildi (Young Serif + Onest, krem/lacivert/amber). Seçilmeyenler: Tur 2 Işık (Bricolage) ve Tur 3 İmza (büyük bloklar, paralaks).
- Seçimden sonra Main küçültülüp sadeleşti. Bunu kimin istediği kayıtlı değil.
- *Çıkarım:* kompakt düzen tutuldu. "Acayip ama sıkmayan" isteği de geçerli; sıradan Shopify'a düşmeden ayırt edici kalmalı.

## 3. İş gerçekleri
| Konu | Değer | Kaynak |
|---|---|---|
| Gerçek dönüşüm | sipariş ÷ oturum ≈ %1,70 (Shopify'ın %0,34'ü kapıda ödemeyi saymıyor) | Brif |
| Ortalama sepet | ≈ ₺1.800–1.873 | Brif, İade Röntgeni |
| İade, kapıda ödeme / ön ödeme | %28,6 (1.557'de 446) / %0,8 (356'da 3) | İade Röntgeni |
| İade nedeni | %92 "alıcı bulunamadı" | İade Röntgeni |
| Kargoya göre iade | PTT %40,3 · Aras %26,1 · HepsiJet %17,7 | İade Röntgeni |
| Ürün payı | LunaDream Kız cironun %83'ü | İade Röntgeni |
| Yüksek iadeli iller | Diyarbakır, Gaziantep, Hatay, Muğla, K.Maraş, Ş.Urfa | İade Röntgeni |

**Sonuçlar:**
- **Ödeme tasarımı iade tasarımıdır.** Kartla öde varsayılan ve indirimli görünür. Kapıda öde ikincidir ama saklanmaz.
- Kapıda formda toplam, teslim aralığı ve WhatsApp onayı görünür. Kart satırının altında güven notu bulunur.
- Sonraki adımlar:
  - yüksek iadeli illerde kapıda ödemeyi kapatma ve "bu ilde online öde" mesajı
  - kapıda siparişi teşekkür sayfasında ya da WhatsApp'ta karta çevirme teklifi
- **Risk:** kartta takılan büyükanne hiç almayabilir. Online payı, dönüşüm ve iade birlikte ölçülür.
- PTT rozeti öne çıkarılmaz. Başarı ölçüsü teslim edilen cirodur.

**Canlı kapıda ödeme formu (17 Ekim'de görüldü):**
- Uygulamanın açılır formu. Alanlar: Ad, Soyad, Telefon, Adres, İl, İlçe, abonelik kutusu, "Kapıda Ödeme Tipi: Nakit / Kredi Kartı".
- Ek ürün teklifleri: Astronot Hava Temizleyici ₺749, Kum Saati ₺699,99, Işıklı Nemlendirici ₺749,99, Hızlı Kargo ₺79,99.
- **Kapıda Ödeme Ücreti ₺80.** Kapıda toplam: 1 lamba ₺1.779,99, 2 lamba ₺2.829,99. Kartla ödemenin gerçek avantajı %5 + ₺80: 1 lambada ₺165, 2 lambada ₺217,50.
- Mevzuat gereği ₺80 ürün sayfasında baştan yazılır.
- Canlı sayfadaki hatalar:
  - iki pakette de "%20 İndirim" yazıyor; gerçeği %15 ve %31
  - kart logoları Amex/Diners/Discover/JCB
  - "1 Yıl Garanti · 90 Gün Para İade" yazıyor
  - "35 kişi inceliyor", "3 günde 399 adet"
  - "2467 Onaylı Kullanıcı Yorumu"

**Fiyat kanıtı:** kullanıcı teyit etti, ₺1.999 son 10 günde uygulandı. Kampanya tarihleri sorulacak.

**Ürün gerçekleri:**
- 1 lamba ₺1.699,99, 2 lamba ₺2.749,99.
- Kız = tavşanlı, Bluetooth ninni hoparlörlü. Erkek = Uzay Kaşifi robot, **hoparlörsüz**.
- Kutuda 6 disk + 6 hediye disk. Brif şikâyeti: "12 disk yazıyor, 6 geliyor". Bu yüzden her yerde "6 + 6 hediye" yazılır, çıplak "12 disk" yazılmaz.
- Unicorn diski kutuda yok; gösterilmez.
- Yorumlar: Burak G., Handan B., Abdülkerim T., Sevcan Z., Mehmet C. Puan Loox'tan gelir.
- Uydurma sayılar kullanılmaz: "Elif K.", 2.467, 10.000+, 12.000+.

**Teyit bekleyenler:**
- ölçü, pil süresi, yaş aralığı
- teslim süresi, 16:00 kesimi
- 2'li pakette hediye disk sayısı
- firma unvanı, MERSİS, adres, WhatsApp
- Loox sayıları
- "1 yıl garanti", "LED ısınmaz", "Şarj olurken çalışır"
- son 10 günün fiyat geçmişi, Kasım zammı

Teyit gelene kadar köşeli yer tutucu kalır: [X] cm.

## 4. Tasarım sistemi (Main'den; Shopify'da değişken olarak)
| Değişken | Hex | Kural |
|---|---|---|
| `--krem` `--yuzey` `--cizgi` | #F6F1E9 #FFFDF9 #E3D8C7 | zemin, kart, 1px ayraç |
| `--lac` | #1A2142 | metin, açık zeminde ana buton |
| `--gece` `--gece2` | #141A36 #0C1027 | yalnız ışığı gösteren bant, sahne, yapışkan çubuk, alt bilgi |
| `--amber` `--amber2` | #F2A65A #E59A4C | ışık, koyu zeminde buton / yıldız, ikon |
| `--soluk` | #5C6078 | ikincil metin |
| `--etiket` | **#766B5B** (Main'deki #8A7F6E 3,5:1, eşiğin altında) | 11px etiket |
| `--sayac` | **#A05A1C** (Main'deki #B4651F 3,9:1, eşiğin altında) | sayaç rakamı |
| `--yesil` | #2E6B4F | Stokta, %5, kartla öde dürtmesi |

- **Yazı:** Young Serif 400 yalnız başlıkta (H1 50px, H2 30px). Onest gövde **16px** (Main'de 15). 12px altı yazı yok. Rakamlar `tabular-nums`.
- **Şekil:**
  - Köşe: levha 28, kart 14–22, buton 16, input 12, çip 999.
  - Kenar 16px. Gölge yerine 1px çizgi.
  - Dokunma alanı ≥48px (Shopify önerisi; Main'de çipler 40px). v2'de uygulandı.
- **Hareket:**
  - Tek eğri `cubic-bezier(.2,.7,.2,1)`, yalnız transform ve opacity.
  - İmza an yeniden seçilecek ("Işığı kapat" çıkarıldı, 17 Ekim).
  - Yeni sonsuz döngü eklenmez. `prefers-reduced-motion` desteklenir.
  - **İstisna (kullanıcı isteği, 17 Ekim):** "Sihirli Özellikler" ikonlarındaki yavaş döngüler (ışık halesi 4,5 sn, disk yelpazesi 5 sn, ses çubukları 2,4 sn, yörünge 8 sn, pil 3,8 sn; pil başa sıçramaz, opacity ile söner). Canlıda satır ekrana girince 150 ms arayla başlar, ekrandan çıkınca durur (IntersectionObserver).
- **İkon:** ince çizgili SVG, emoji yok.

**Main'in bilinen kusurları** (taşırken düzelt):
1. Özellik şeridindeki "Bluetooth ninni" Erkek seçilince de görünüyor. Modele bağlanmalı.
2. "12 masal diski" yerine "6 + 6 hediye disk".
3. Alt CTA'lar (Bir gece kartı, kapanış) hep "Kapıda öde" diyor ve indirimsiz fiyat gösteriyor. Ödeme seçimine bağlanmalı.
4. "Stokta" sabit metin; envantere bağlanmalı. 4,7 puana 5 dolu yıldız konmuş; kısmi yıldız gerekli.
5. "Annelerin videoları" bölümü fotoğrafı video gibi gösteriyor. Gerçek video yoksa bölüm gizlenir.
6. 16:00 kargo kesimi teyitsiz. Sayaç cihaz saatiyle çalışıyor; İstanbul saati olmalı.
7. "Tüm ürünler · 15" yazıyor, listede 13 ürün var. 10,5px yazı ve 40px çip var.
8. Galeride mağaza posterleri var ve yazılı. **İkisinde doğrulanmamış yorum var** ("Elif K." kartı, isimli yorum kolajı). v2'de çıkarıldı; canlı sitede ve reklamlarda da kaldırılmalı.

## 5. Sayfa yapısı (Main)
1. Gece sahnesi galeri: ana ürün fotoğrafları kırpılmadan, kenarlarda süzülen diskler, üstte küçük resimler, altına binen levha (Tur 8). "Işığı aç/kapat" anahtarı ve saat yok (17 Ekim).
2. Karar levhası (sahnenin üstüne −30px biner). Sırası:
   - puan, Stokta, H1
   - 4'lü özellik şeridi
   - Model, Paket (canlı sitedeki 1 Adet / 2 Adet kartları)
   - ay sonu şeridi, birlikte al
   - iki buton: online ve kapıda (uygulama formu)
   - güven üçlüsü, müşteri fotoğrafları
3. Bir gece, beş an.
4. Çipli yorumlar.
5. Diskler.
6. Avucuna sığar ve kutu içeriği.
7. Videolar.
8. 30 gün iade mührü.
9. SSS.
10. Odanın geri kalanı.
11. Kapanış, yasal metinler, dev "Ayluna".
12. Yapışkan çubuk.

Kodda "Sihirli Özellikler (yeri korunur)" notu var.

## 6. Kalıp kütüphanesi
- **Tutulanlar:**
  - model → paket → ödeme → toplam → teslim → yapışkan çubuk zinciri
  - ~~"Işığı kapat" anahtarı~~ (17 Ekim: kullanılmayacak)
  - saatli gece ritüeli
  - kutu içeriği
  - "Kardeşe" paketi
  - çipli yorumlar
  - dev yazılı alt bilgi
  - iade mührü
  - "Kartla öde, ₺X daha az öde" dürtmesi
  - sayfa içi kapıda formu
- **Seçilmeyenler:**
  - emoji
  - kurdeleli "EN ÇOK TERCİH"
  - pastel/Baloo, Apple-beyaz
  - krem + serif + kil şablonu
  - her bölümde fade-in, sayan rakamlar
  - harf aralıklı etiket yığını
  - eş kart ızgarası
  - Tur 3'ün büyük paralaks blokları
- **Yedekteki fikirler:**
  - Kapıya kadar
  - Hangisi onun?
  - Kutuyu aç
  - Kardeşin gecesi
  - Anne notları
  - Hediye notu
  - "Kimin için?"
  - Ay atlası (ana sayfa için)
  - Ayrıntı: `ogrenme/tuval-imza.md`, `ogrenme/eski-tasarimlar.md`.

## 7. Mevzuat ve dürüstlük (8 kural; kaynaklar `ogrenme/arastirma.md`)
1. ✓ Üstü çizili önceki fiyat = indirimden önceki **10 gün** içinde ayluna.shop'ta uygulanan en düşük fiyat. Kampanya tarihleri yazılır, ispat satıcıdadır. Fiyat sabitse `compare_at_price` boş kalır. Kaynak: Resmî Gazete 1 Temmuz 2026 / 33297, yürürlük 1 Ağustos 2026.
1b. Bu kural **bütün ürünlerdeki** üstü çizili fiyatlar için geçerli (nemlendirici ₺1.099, projektör ₺2.999 vb.); her birinin son 10 gün kanıtı olmalı.
2. ✓ Şartlı indirimler de bu kurala tabidir: kartla %5, paket kazancı. ₺3.998 gibi "2 × eski fiyat" yerine "2 ayrı almaya göre ₺649,99 daha az" yazılır. Hukukçu teyidi önerilir.
3. ✓ Satın alımı doğrulanamayan yorum yayımlanamaz. Olumsuz yorum gizlenemez. Puan ve sayı Loox'tan gelir; veri yoksa blok gizlenir.
4. Yasal cayma 14 gündür. "30 gün iade" = 14 yasal + 16 Ayluna. Yasal hak özel avantaj gibi sunulmaz.
5. Aciliyet yalnız gerçek kurala bağlıdır: gerçek zam tarihi, stok eşiği, Flow'dan gelen satış. Sayaç İstanbul saatiyle herkese aynı tarihi gösterir. "X kişi bakıyor" yok.
6. Kapıda ödeme gizlenmez. Ücretli ek önceden seçilmez ("Birlikte al" boş başlar).
7. Ana sayfada ve İletişim'de: satıcı unvanı, MERSİS, adres, KEP, e-posta, telefon. Fiyat KDV dahil gösterilir.
8. Sağlık iddiası yok. Teyitsiz teknik rakam yok. AI görseli "müşteri" diye sunulmaz. Sayfa vaadi kutuyla aynıdır.

## 8. Shopify teknik
- Bölümler **Main'den** yeniden türetilmeli. Bugünkü `shopify/*.txt` dosyaları `iskelet.html`'den geliyor (`shopify-derle.py:16`).
- Her bölüm tek `.liquid`:
  - CSS `#ay-{{ section.id }}` kapsamında
  - JS tek IIFE
  - `{% schema %}` ile düzenlenebilir
  - ürüne bağlıysa `enabled_on: product`
- Fiyat varyanttan gelir. Yüzde, adet fiyatı ve kazanç formülle hesaplanır.
- Bilinen hatalar:
  - `?variant=` adresi yok sayılıyor
  - eşleşme yoksa sessizce ilk varyant seçiliyor
  - tükenmiş varyant satılabiliyor
  - indirim kodu boşken %5 düşük fiyat gösteriliyor
  - bant yapışmıyor
  - masaüstü kuralları 430px sütuna sıkışıyor
  - fontlar 15 kez tanımlanıyor
  - videolar `preload` ile yükleniyor
- Kapıda ödeme uygulamasının seçicisi bulunamazsa uyarı verilir; gerçek uygulamayla telefonda denenir.
- Tema düzenleyici:
  - `data-ready` ile kopya temizliği
  - `request.design_mode` ya da `?onizleme=` ile satıcı önizlemesi
  - `shopify:section:unload` temizliği
- Liquid yazmadan önce `shopify-liquid` becerisiyle doküman ara; teslimden önce doğrula.
- **Tema sıfırdan yazılır** (kullanıcı kararı, 17 Ekim). Hazır temadan kod alınmaz.
  - İlk kurulum zip ile yapılır: Shopify'da sıfırdan tema ancak böyle yüklenir. Sonraki değişiklikler dosya dosya `.txt` olarak verilir.
  - Satın alma öğeleri yeniden kullanılabilir tema blokları olarak `blocks/` altında yazılır.
- Instagram tarayıcısı:
  - sayfa videosuz da satmalı
  - sahnede `svh` kullanılır
  - yapışkan çubukta `env(safe-area-inset-bottom)`

## 9. Araçlar
- Ekran görüntüsü:
  - Sayfalar: `NODE_PATH=$(npm root -g) node ayluna-imza/araclar/ekran-goruntusu.js <klasör> <sayfa.html>`
  - Tuval panosu: `node ayluna-imza/araclar/dc-onizle.js ayluna-imza/canvas/Main.dc.html <png> '<durum-json>' <y> <yükseklik>` (aynı `NODE_PATH`). Sayfa başı için y = −470. Yerelde yalnız `canvas/magaza/` görselleri var.
- Shopify derleme: `python3 ayluna-imza/araclar/shopify-derle.py`.
- Görsel üretimi (Flow / Nano Banana Pro):
  - Ürün sıfırdan üretilmez; yalnız sahne değişir.
  - Görselde yazı üretilmez.
  - İş akışı `DEVAM.md`'de.
- Hafıza: bulut konteyneri silinir. Hafıza depodaki dosyalardır; her karar commit'lenir. Eklenti değerlendirmesi: `ogrenme/eklenti-rehberi.md`.

## 10. Düzeltme günlüğü
Kullanıcı bir şeyi düzeltince bir satır eklenir. Kalıcı kural `beceriler/`'e de işlenir.

| Tarih | Kullanıcı | Kural |
|---|---|---|
| 17 Eki | "Kendini tasarımda en üst seviyeye getir, tüm dosyaları öğren" (daha önce de söylemiş) | Her oturum bu dosyayla başlar. Öğrenilen her şey depoya yazılır. |
| 17 Eki | Fayda listesi, sayaç, stok, "dün satılan" atılmasın | Tanıdık kalıp korunur, inceltilir, gerçek veriye bağlanır. |
| 17 Eki | Öncelik online ödeme (%5), kapıda ikinci | Kart varsayılan; bütün CTA'lar seçimi taşır. |
| 17 Eki | "Hiçbir Shopify temasını kopyalamanı istemiyorum. Şu an ChatGPT ile yaptığım bir sürüm bağlı; tüm kısımlarını senin yapmanı istiyorum, benzersiz olmalı." | **Sıfırdan Ayluna teması.** Horizon/Dawn temel alınmaz, hazır temadan kod alınmaz. Shopify'ın zorunlu dosya yapısı kullanılır (layout, templates, sections, snippets, config, locales); kod ve tasarım tamamen özgün. |
| 17 Eki | Üstü çizili ₺1.999 son 10 günde ayluna.shop'ta uygulandı | Üstü çizili fiyat kalır. Kampanya başlangıç ve bitiş tarihi sayfaya yazılır. Fiyat geçmişi kanıtı saklanır. 2'li pakette "2 ayrı almaya göre ₺649,99 daha az". |
| 17 Eki | Aylık zam: "henüz karar vermedim" | Sayaç tasarımda durur, yayında kapalı başlar (ayar). Karar gelince açılır ve yeni fiyat yazılır. |
| 17 Eki | "Emoji benefiti hiçbirinde beğenmedim" | Durağan emoji ya da ikon fayda listeleri beğenilmedi. (Aynı gün daraltıldı: animasyonlu "Sihirli Özellikler" isteniyor, aşağıya bak.) |
| 17 Eki | "Model seçim kısmı idare eder" (Main'deki küçük stüdyo fotoğraflı kartlar) | Model kartları kalır; daha iyisi bulunursa önerilir. |
| 17 Eki | "Ürün fotoğrafları ana ürün fotoğrafları olacak" | Galeri Shopify'daki ana ürün medyasından gelir; özel sahne görseli galeriye konmaz. ("Elif K." ve yorum kolajı içeren 2 görsel mevzuat gereği ürün medyasından çıkarılmalı.) |
| 17 Eki | "Işığı aç kapat kısmını kullanmayız" | "Işığı aç/kapat" anahtarı ve saat yok. (Gece sahnesi çerçevesi sonra geri istendi, aşağıya bak.) |
| 17 Eki | "Basit emojiler, sıkıcı tasarımlar hâlâ devam ediyor" | Tasarım sıkıcı bulunuyor. Sade şablon görünümü yetmez; karakterli, akılda kalan görsel dil gerekir. Yön seçimi yeniden açık. |
| 17 Eki | "B+ ile devam et, ama emoji benefit olmalı; önceden animasyonlu bir benefit yapmıştık, ürünün 4 özelliğini gösteriyordu" | **Seçilen yön: B+ Gece Postası.** "İkonlu fayda yok" kuralı daraltıldı: **durağan** emoji ya da ikon listesi istenmiyor. "Ayluna Yeni Tasarım" tuvali I yönündeki **animasyonlu "Sihirli Özellikler"** bloğu isteniyor. Bu blok 2×2 kart: ikon kutusu, başlık, tek cümle ve ürüne özgü küçük animasyon (nefes alan hale, yelpaze diskler, dolan pil…). Yeri canlıdaki gibi model seçiminden sonra. Uydurma madde ("+10.000 Mutlu Anne") ve teyitsiz madde ("21 ışık modu") konmaz. |
| 17 Eki | "Şu anki kapıda ödeme ve bundle şeklimi koru" | **Canlı sitedeki yapı korunur.** Paket: alt alta "1 Adet / 2 Adet" kartları, ürün küçük resmi, % indirim, fiyat ve eski fiyat, altta "+6 Tane Ücretsiz Hediye Disk" şeridi, 2 Adet'te "En Çok Tercih Edilen" kurdelesi. Altında iki ayrı buton: "Güvenli Ödeme İle Al" (online) ve "Kapıda Ödeme ile Sipariş Ver" (uygulamanın açılır formu). Ödeme seçici kartları kullanılmaz. |
| 17 Eki | "Görsel kısmını diğeri gibi yapalım ama emoji benefit kısmını biraz daha iyileştirelim; renkler vesaire çok boğuyor" | **Sihirli Özellikler sakin olur.** Koyu ve amber dolu kartlar yok; kartlar beyaz. **Amber yalnız ikonda ve hareket eden parçada** (ışık). Gölge yok, 1px çizgi. Açık zeminde amber etiket okunmuyor: etiket rengi `#A05A1C`. Disk satırı "6 + 6 masal diski"; Erkek satırı özellik anlatır ("Tavanda uzay"). Altındaki "hayal" bandı da açık (krem). |
| 17 Eki | "Sihirli V1 iyi gibi, sen ne dersin" (eleştirmen V3 Liste'yi seçmişti) | **Seçilen: V1 Sade beyaz.** 2×2 beyaz kart, lacivert ikon kutusu + amber ikon. Her kartta üst satır: solda ikon, sağda canlı gösterge (aynı yerde); altında başlık ve tek cümle (15px, dengeli kırılım). Ay kartında hale ikon kutusunun arkasında parlar. Eleştirmen kullanıcıdan farklı seçerse karar kullanıcınındır; eleştirmenin düzeltmeleri seçilen varyanta uygulanır. |
| 17 Eki | Main'in galeri ekran görüntüsü: "Görsel kısmı böyle olsun ama bizim ürün görsellerimiz olacak yine" | **Galeri = gece sahnesi.** Gece laciverti zemin, üstte logo, ana ürün fotoğrafı (kare poster) kırpılmadan tam genişlik, alt kenarı geceye karışır; hediye diskleri fotoğrafın kenarında süzülür (ürünü kapatmaz); küçük resimler ve "1/7" sayacı fotoğrafın üstünde; altına yuvarlak köşeli levha biner (tutamak, puan, Stokta). "Işığı aç" anahtarı ve saat yine yok. |
| 17 Eki | Kullanıcı tuvalde sildi: "Işığı kapattığında tavanda masal başlar" alt başlığı ve "hayal" bandı (müşteri fotoğraflı) | Başlıktan hemen sonra fiyat gelir; alt başlık yok. Sihirli Özellikler'in altında ek bant yok. Kullanıcının tuvalde yaptığı silme/taşımalar üreticiye (`luna_bplus.py`) işlenir; yayından önce tuvaldeki sürüm okunur. |

## 11. Kararlar
**Varsayılan olarak uygulanır** (kullanıcı itiraz ederse değişir):
- gövde 16px
- alt CTA'lar ödeme seçimine bağlanır
- PTT rozeti gösterilmez
- tek sayaç, Main'deki ince şerit; üst bant kaldırılır
- yorumların yanına puan dağılımı eklenir

**Sorulacaklar** (sırayla, hepsi birden değil):
1. **Birlikte sor:**
   - Son 10 günde ayluna.shop'ta üstü çizili ₺1.999 uygulandı mı?
   - Her ay gerçekten zam var mı, Kasım fiyatı ne olacak?
   - Paket, sayaç, ödeme kartı ve ceza riski bu iki cevaba bağlı.
2. İade metni "14 yasal + 16 Ayluna" diye açılsın mı? 15–30. günlerde kargoyu kim ödüyor?
3. "Dün satılan" ve stok satırı Main'e eklensin mi?
4. 16:00 kesimi gerçek mi?
5. 3'lü paket olsun mu?
6. 2'li pakette "3 taksit" satırı olsun mu?
7. ~~Yapı~~: karar verildi, sıfırdan özel tema.
