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
- Kız = tavşanlı, Erkek = Uzay Kaşifi robot. **İkisi de Bluetooth ile ninni çalar** (kullanıcı, 17 Eki).
- **3 parlaklık ayarı** var. **Her yaş için uygun.** Boyut ve pil süresi sayfaya yazılmaz (kullanıcı kararı).
- **Kampanya:** Ekim ayı boyunca (1–31 Ekim). Kart: **tüm kredi ve banka kartları** geçer.
- **Stok satırı elle:** kullanıcı Shopify stoğunu kullanmıyor; "Stokta son X adet" satırını kendisi yazar ve açıp kapatır (şimdilik 18). "Dün X aile aldı" satırı veri olmadığı için yok.
- **İade:** 30 gün; iade kodunu Ayluna gönderir, iade kargosu ücretsiz.
- **Müşteri fotoğrafları** (Loox foto yorumları) sayfada kullanılabilir (kullanıcı izni, 17 Eki).
- Kutuda 6 disk + 6 hediye disk; **her kutuda hepsi çıkar** (2'li pakette her kutuda +6 hediye). Brif şikâyeti: "12 disk yazıyor, 6 geliyor". Bu yüzden her yerde "6 + 6 hediye" yazılır, çıplak "12 disk" yazılmaz.
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

- **Yazı:** Young Serif 400 yalnız başlıkta. Ölçek (Tur 13, v3): ürün adı 28, bölüm başlığı 22, gövde 15, açıklama 14, fiyat 20 (eski: ürün adı 32, fiyat 22, H2 26, büyük rakam 40, kart başlığı 18–20, fiyat 24, gövde 16, açıklama 15, not 13, etiket 12. Onest gövde **16px** (Main'de 15). 12px altı yazı yok. Rakamlar `tabular-nums`.
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
6. 16:00 kargo kesimi kullanıcı tarafından teyit edildi (18 Eki); sayaçlar İstanbul saatiyle.
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
- **Denemede (Tur 17, C2 panosu; kullanıcı kararı bekliyor):**
  - Ay yaprakları iskeleti (bölüm = üst üste binen sıcak tonlu yaprak)
  - Kapına ne gelir? (seçime göre kutu sayısı ve içerik)
  - Ay tutamakları (eleştirmen 4/10)
- **Reddedilen (Tur 16):** bölümleri hikâye karelerine toplamak ("çok kısaltmışız").
- **Denemede (Tur 21, E panosu):** B+ ve Bir gece kadranı (yaydaki beş saat, ay seçili saate gider, koyu panel). Kullanıcı kararı bekleniyor.
- **Denemede (Tur 18, D panosu):** "Oda ve Tavan". Yönü ve kararları ajanlar verdi (`ogrenme/tur18/karar.md`): Literata ve Atkinson Hyperlegible Next, bant iskeleti, kubbe kenarlı "Disk tavana açılır", saatle koyulaşan Bir gece. Kullanıcı kararı bekleniyor.

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
- Disk/çizim netleştirme (yapay zekâ, CPU): `python3 -m venv v && v/bin/pip install --index-url https://download.pytorch.org/whl/cpu torch && v/bin/pip install numpy pillow`; model `RealESRGAN_x4plus_anime_6B.pth` (GitHub xinntao/Real-ESRGAN v0.2.2.4); `v/bin/python ayluna-imza/araclar/disk/disk_kes.py <afiş> <çıkış> --sr <model.pth>`. Tuvale yükleme: Artifact `asset: true`; yeni id'ler `araclar/blob-yerel.json`'a (yerel önizleme için).
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
| 17 Eki | "Erkek robotta ninnili ve emoji benefitin altında olsun" | **Robot da ninnili.** Erkek kartı "Robot · ninnili"; Sihirli'de Erkek için "Ninnili robot" (Bluetooth teyit edilmedi, yazılmaz). Model seçimi Sihirli Özellikler'in **altında**, paketin üstünde. |
| 17 Eki | "Disk görüntülerini daha yüksek kaliteyle üretip koy" | Disk görselleri mağazadaki 1024px tema afişinden kesilir, 384px'e netleştirilir (`araclar/disk/disk_kes.py`, `canvas/diskler/`). Desen yeniden çizilmez. Unicorn ve 2025 diskleri kutuda olmadığı için kullanılmaz. Eski 9 KB'lık disk kırpıntıları kullanılmaz. |
| 17 Eki | "Birkaç tane ürünün profesyonel yapılmış görüntüsünü koy, oda içerisinde" | Galerinin başında 2–3 profesyonel oda sahnesi (gerçek üründen Flow ile; ürün değişmez), sonra mağaza afişleri. |
| 17 Eki | "Güzel yorumlarımız var, videolarımız var; onlar için de uygun section oluştur ve kur" | **Videolar** bölümü (9:16 kaydırmalı kartlar, canlıda Shopify videosu; ekrandayken sessiz, dokununca sesli) satın alma kutusunun altında. **Yorum duvarı**: puan, müşteri fotoğrafları, konu çipleri, kaydırmalı beyaz yorum kartları; metinler Loox'tan birebir. |
| 17 Eki | "Gönderdiğim gibi üst kısım ve görseller bir olsun" | Logo bandı ayrı şerit değil; fotoğrafın üstüne biner (Main gibi), üstte koyu geçiş. |
| 17 Eki | "Baskılayıcıları biraz daha arttıralım" | Aciliyet artırılır ama **yalnız gerçek veriyle**: fiyatın altında kampanya sayacı (bitiş tarihi ayarı), butonun üstünde "Stok azalıyor: son X adet" (Shopify envanteri, eşik altı), "Dün X aile sipariş verdi" (Shopify Flow metafield), yapışkan çubukta kalan süre. Veri yoksa satır gizlenir. Uydurma sayı ve sahte sayaç yok. Nabız noktası en fazla 3 kez yanıp söner. |
| 17 Eki | "Görselleri tekrar üretip yüksek kaliteyle koyacaktın, diskler için yapmamışsın" | Kesip büyütmek yetmez; diskler **yapay zekâ ile netleştirilir** (Real-ESRGAN çizim modeli, x4, 512px). Desen değişmez. Büyük önizlemede bulanıklık ya da JPEG kırıntısı kabul edilmez; teslimden önce 260px'te önce/sonra karşılaştırılır. |
| 17 Eki | "Her gün sıfırlanan sayacı koruyabiliriz; toptancı zammı geldiği anda zam yapıyorum, her an olabilir, bu baskılayıcı gerçek sayılır" | **Bugünkü fiyat sayacı** fiyatın altında: her gece 23:59'da (İstanbul) sıfırlanır, altında "Toptancı zammı gelirse fiyat ertesi gün güncellenir." Gerçek olması için koşul: gün içinde zam gelse de o günün fiyatı 23:59'a kadar korunur. Ay sonu kampanya sayacı kalktı. |
| 17 Eki | "Yazı fontu bazı yerlerde çok büyük, düzensizlik, kaos var" | **Tek yazı ölçeği**, dışına çıkılmaz: başlık 1: 44 → Tur 12'de 32 (yalnız ürün adı) · bölüm başlığı: 26 · büyük rakam: 40 (puan, saat, 30 gün: 56) · kart başlığı: 18–20 · fiyat: 24 · gövde: 16 · açıklama: 15 · not: 13 · etiket: 12. Ara boyut (13,5 / 14,5 / 21 / 46 / 52 / 88 / 100) yok. Bölüm etiketi tek stil (13px kalın, #A05A1C, büyük harf ve harf aralığı yok). Yeni öğe eklerken bu ölçekten seçilir. |
| 17 Eki | "LunaDream yazısı çok büyük, fiyat çok büyük, yanında indirimli fiyat, onun yanında kartla fiyat" | Ürün adı **32**. Fiyat satırı yalnız: fiyat (22) + üstü çizili eski fiyat + "%15 indirim" rozeti. Kartla fiyat başlıkta yazılmaz; yalnız ödeme butonunda ve altındaki notta. |
| 17 Eki | "Toptancı zammı falan karıştırmışsın, bu öyle bir şey değil; müşteriye doğru sunum önemli" | **İç gerekçe (toptancı, maliyet, zam sebebi) müşteriye asla yazılmaz.** Sayaç canlıdaki gibi sayfanın en üstünde ince şerit: "Bugüne özel fiyat 06:26:42", her gece sıfırlanır. |
| 17 Eki | "Arada bazı yerlerde fazla boşluk var" | Bölüm arası 36px (52 değil). Koyu bölümler yuvarlak köşeli panel (28px), araları 36px. |
| 17 Eki | "Section aralarına geçiş için hafif animasyonlar yapabilirsin" | Bölümler kaydırınca 20px aşağıdan ve saydamdan gelir (`animation-timeline: view()`, yalnız transform/opacity, destek yoksa ya da azaltılmış harekette yok). "Her bölüme fade-in yasak" kuralı bu kullanıcı için kalktı; yalnız bu hafif biçimde. |
| 17 Eki | "Bir gece 5 an için gerekli görselleri oluştur" | Görseller gerçek ürün fotoğrafından FLUX Kontext ile üretilir (`araclar/gorsel/bir_gece_uret.py`). Bulut ortamında `HF_TOKEN` gerekir; ücretsiz kota ortak IP'de dolu. Kalitesiz (filigranlı, ürünü yeniden çizen) görsel sayfaya konmaz. |
| 17 Eki | "Evet (2'li varsayılan) ama bir kız bir erkek seçilebilir" | Varsayılan paket 2'li kalır. 2'li seçiliyken "İki lamba: 2 Kız / 1 Kız + 1 Erkek" seçimi görünür; karışıkta paket görselinde iki farklı lamba, sepete iki ayrı varyant eklenir. |
| 17 Eki | "Yazı kısımları hâlâ biraz büyük, hâlâ biraz daha yazı var ve iç içe gibi" | **Ölçek v3:** ürün adı 28 · bölüm başlığı 22 · büyük rakam 32 (30 gün: 40) · paket adı 17, paket fiyatı 18 · fiyat 20 · gövde 15 · açıklama 14 · not 13 · etiket 12 · buton 16/14. **Az yazı:** başlığı olan bölümde ayrıca üst etiket yok; tek cümlelik açıklama; yardımcı satırlar birleştirilir; iç notlar sayfada değil yorum satırında. **İç içe değil:** kart içinde kart/panel yok; gölge yok; çerçeve yalnız seçilebilir öğede. |
| 17 Eki | "Eleştirmenin 10 vermesini engelleyen kısımlar neyse bana sormadan direkt siteye ekle" | (GERİ ALINDI, aşağıya bak.) Uygulandı, kullanıcı beğenmedi. |
| 17 Eki | (Tur 13 uygulaması, GERİ ALINDI) | Artık geçerli değil: kutu listesi seçilen pakete bağlı; yapışkan çubuk seçimi aynen söyler; kart notu karşılaştırmayı adlandırır ("kapıda ödemeye göre"); puan yıldızları kesirli ve doğru dolar; üstü çizili fiyat ve % rozeti yalnız 10 gün kanıtı olan üründe; alıntı metni Young Serif 16 (başlık dışındaki tek serif kullanım). |
| 17 Eki | "Eleştirmen için yaptıklarımızı geriye döndür, eski hâlini istiyorum. Model seçimi oradan yapmayalım; 2 adet seçilirse oradan ufak bir seçim kısmı çıksın, erkek mi kız mı" | **Eleştirmenin önerileri toplu uygulanmaz.** Kullanıcıya en iyi 3 fikir gösterilir, kullanıcı seçer. Tur 13 eleştirmen değişiklikleri (yıldız SVG, kart logoları, Kardeşe/Kendine, kutu listesi bağlama, disk rayı ayrımı, Bir gece krem vb.) geri alındı. **Model kartı yalnız Kız / Erkek.** 2 Adet seçiliyken paketin altında küçük seçim: "1. lamba [Kız / Erkek] · 2. lamba [Kız / Erkek]"; model kartına dokununca iki lamba da o modele döner. |
| 17 Eki | Bilgiler: Ekim kampanyası, her kutuda hepsi, boyut/pil yazılmasın, her yaş, Bluetooth iki modelde, 3 parlaklık, tüm kartlar, stok elle (18), ücretsiz iade kodu, müşteri fotoğrafı izni, "Flow ile üretebilirsin" | Bilgiler §3'e işlendi. Flow (Google) yalnız kullanıcının tarayıcısından çalışır; bulut oturumunda tarayıcı bağlantısı yoksa görsel üretimi claude.ai sohbetinde (Claude in Chrome + Flow) yapılır ya da `HF_TOKEN` eklenir. |
| 17 Eki | "Çok kısaltmışız; hâlâ soğukluk, düzensizlik var, tam yakın değil uzak değil. Sitenin alt kısmı section olarak görünmeli. Değişiklik bölümler, iskelet, sayfanın görünüşü üzerine olmalıydı." (Tur 16 C hikâyesine) | **Yeni deneme içerik kesmez, bölümleri birleştirip gizlemez** (hikâye/karusel içine toplamak yok). Her bölüm ayrı ve görünür kalır. Yeni tasarım turu iskelete ve görünüşe dokunur: bölüm yüzeyleri, aralık ritmi, sıcaklık. **Yakınlık net olur:** grup içi sıkı (8–16px), bölüm sınırı boşlukla değil yüzey değişimiyle okunur. Soğuk duran ince çizgili beyaz kartlar yerine sıcak dolgulu yüzeyler. |
| 18 Eki | "Hayır olmamış, o section için UI tasarım istiyorum" (Bir gece) ve "Daha güzel bir UI yapmanı istiyorum" | **Bölüm düz bant + liste olarak kalmaz, ürüne özgü bir arayüz parçası olur:** lamba kendi ışığında özellik sahnesi, sipariş fişi, gece kadranı, ay evreli mühür (E). İçerik ve bölüm sırası korunur. Kullanıcının sildiği bir öğe (ad altındaki alt başlık) yeni turda geri gelmez: eski üretici kopyalanınca bu tablo baştan kontrol edilir. |
| 18 Eki | (Tur 20 E'sine) "Sipariş fişini kaldır, emoji benefiti düzelt, yazım hataları berbat, yazı fontu kötü; her şey çok yabancı duruyor, bir bütün ve uyum yakala" | **Bütünlük önce gelir:** yeni deneme seçilen B+'nın dilinden çıkmaz (Young Serif + Onest, krem/lacivert/amber, Sihirli V1 2×2 beyaz kart, canlı paket ve iki buton); yenilik bölüm içinde tek parça olarak denenir. Bir önceki satırdaki "ışık sahnesi, sipariş fişi, mühür" yaklaşımı geri alındı; yalnız **Bir gece kadranı** B+ diliyle kaldı. Sipariş fişi yok. "Emoji benefit" = Sihirli Özellikler; seçili biçimi V1. Soru başlıkları "?" ile biter; sıfırı çizgili yazı tipi kullanılmaz. |
| 18 Eki | "Yarım ay, tam ay olma efektini kullanmaya devam et (bugün siparişin alındı kısmında vesaire). Hâlâ düzensizlikler, renklerin birbirine girdiği, büyük marka hissi vermeyen yerler var" | **Ay evresi marka motifidir:** teslim çizgisi hilal → yarım → dolunay (kaydırınca sırayla dolar), 30 gün mührü 8 evreli halka. **Renk disiplini:** ~12 ton; tek açık ton #F1E8DA, tek kesik çizgi #D6CAB6, tek ikincil yazı #5C6078, koyuda #B9BED6; güven satırı lacivert (yeşil yalnız Stokta ve Satın aldı); amber yalnız ışık ve ana butonda, bir ekranda tek amber blok; koyu panelde geniş amber parıltı yok. Açık ve koyu bölümler sırayla (Bir gece → Yorumlar → Diskler). |
| 18 Eki | Eleştirmenin 3 fikrinin üçü de seçildi (amber tek vurgu, ay evresi marka işareti, tek fotoğraf dili) | **Tek amber** #F2A65A: ışık (ay, yıldız, evre, başlık noktası) ve ana buton; şerit, kurdele ve seçili paket fiyatı amber değil. **Marka işareti** ince daire içinde amber hilal; başta ve alt bilgide aynı kilit; sayacın yanında gün bittikçe sönen ay. **Seçim:** model ve lamba seçiminde çerçeve ve dolunay noktası; dolu lacivert yalnız pakette. **Küçük ürün görselleri** hep arka planı temizlenmiş stüdyo kesimi. Kadranda gece anları gece fotoğrafıyla. |
| 18 Eki | "Fiyat güzel durmuyor; girince 1999 yazsın, hafif animasyonla indirimli fiyata düşsün. Model seçimi güzel değil. Bir gece UI olsun, ay zımbırtısı kaydırdıkça dolsun. Kargo takibine verildiden başlayan soft animasyon. Satın alma butonu altındaki yazıları sil. Satış için yeni bölümler, influencer çalışmaları için bir kısım düşün" | **Fiyat düşüşü** (kullanıcı isteği, "sayan rakam yok" kuralının istisnası): açılışta bir kez ₺1.999,00 görünür, çizilir, eski fiyat yerine kayar, indirimli fiyat yukarıdan düşer, rozet belirir. **Model = gece penceresi:** kemerli pencerede lamba kesimi; seçilene gece iner, yıldızlar çıkar, lamba yanar. **Bir gece:** yaydaki her saat bir ay evresi; büyük ay her anda biraz daha dolar (hilal → dolunay). **Kargo takibi:** ekrana girince bir kez; "Sipariş verildi" hilali → çizgi ve paket noktası Kargoda'ya akar → yarım ay → Kapında dolunayı ve ışık halkası. **Buton altı not yok;** ₺80 kapıda ödeme ücreti mevzuat gereği kapıda butonunun içinde yazılır ("₺2.829,99 · ₺80 kapıda ödeme ücreti dahil"). Yeni bölüm önerileri ayrı panoda; kullanıcı seçer. |
| 18 Eki | (Tur 24 E'sine) "Animasyon çalışmıyor; Kapıda Ödeme ile Sipariş Ver'de fiyat yazmasın; fiyat altındaki güven satırını kaldır, çok kötü duruyor; hâlâ seçiciler çok kötü, bundle ve aralarında uyum yok, lamba seçimi de güzel değil" | **Tek seferlik animasyon tuvalde görülmez** (pano açılınca biter): sürekli ama sakin döngü kullanılır, ekrana girene kadar ilk karede durur. **Kapıda butonunda fiyat yazmaz;** ₺80 ücret kapıda ödeme formunun özetinde ve SSS'de yazar. **Fiyatın altında güven satırı yok.** **Seçiciler tek dil:** model, paket ve 2. lamba aynı kart, aynı seçili durum (2px lacivert çerçeve + amber dolunay noktası), dolu lacivert yok; kemerli gece penceresi ve hap segment kalktı. Kullanıcı **satır kartlar**ı seçti: model yan yana iki yarım kart, paket alt alta satır, 2. lamba 2 Adet kartının içinde çip, altta tek hediye şeridi. Hediye "her kutuda +6" yazılır, çıplak "12 disk" yazılmaz. |
| 18 Eki | "Bir gece 5 anın altı neden o kadar çok boş" | **Yapışkan öğenin hiçbir atasında `overflow:hidden` olmaz** (kaydırma kabı yapar, yapışkan çalışmaz; panel kayıp gider, altında boş kaydırma adımları kalır). Taşmayı kesmek için `overflow:clip`. Kaydırmalı bölüm telefon boyunda (390×844) gerçekten kaydırılarak denetlenir; tuval boyu (≥1600px) bu hatayı göstermez. Yapışkan panel ekranda ortalanmış kart olarak durur. |
| 18 Eki | "Kaydırdıkça değişmiyor dostum" | **Tuvalde pano kaymaz, tuval kayar:** kaydırmaya bağlı her hareket iki yoldan sürülür: sayfanın kendi kaydırması (telefon, Oynat) ve tuvalin görünür alanı (görünmez işaretler + IntersectionObserver; başka kökenli çerçevede rootMargin çalışmaz). Pano `expand: "fill"` ile Oynat'ta sayfa gibi kayar. Teslimden önce `araclar/kaydirma-testi.js` iki durumu da geçmeli. |
| 18 Eki | "Yorum kısmı ürün ismi yanında olsun; yıldız sayısı ve ortalaması tasarıma uygun olacak şekilde" | **Puan adın yanında:** solda ürün adı, sağda sağa yaslı iki satır (yıldızlar + ortalama kalın, altında "N yorum"); adın üstünde ayrı puan satırı yok. "Stokta" fiyat satırının sağ ucunda. |
| 18 Eki | "Kutudan ne çıkıyor'u kaldıralım; 2 odanın nasıl göründüğünü gösteren görsel yapalım, metin içeren görsel kısmı gibi ama daha iyi" (B'yi seçti) | **Kutu bölümü yok;** kutu içeriği SSS'de. **Odası böyle görünecek:** iki oda posteri yan yana kayar; fotoğraf üstte, yazı altında lacivert bantta (**yazı ürünün üstüne binmez**), "… modelini seç" düğmesi, temsilî notu. Kart cümlesi teyitli olur: desen seçilen diske göre değişir, "ay ve yıldızlar" gibi tek diske bağlı vaat yazılmaz. |
| 18 Eki | "Tamam, nihai tasarımımız bu olacak; şimdi USB projektör için de ona uygun bir tasarım yapalım" | **Nihai tasarım LunaDream E.** Diğer ürün sayfaları E'nin dilini ve bölüm sırasını alır (aynı CSS, `luna_e.py`'den içe aktarılır); ürüne özgü bölüm yalnız gerekirse eklenir (USB: Üç adımda kur). Ürün bilgisi yoksa mağaza afişlerindeki teyit edilebilir bilgiler kullanılır; canlı sayfadaki çelişkili sayı ve sağlık iddiaları alınmaz. |
| 18 Eki | (Galaxy USB E kopyasına) "Sadece çocuklara sattığımız bir ürün değil; çocuklar, anne babalar, gençler, birçok kesim alıyor. Renk seçimleri, bölümler ona göre; her sayfanın tasarım dili kendine özel olsun." + "Şu anki hâlinin de yararı var ki bu kadar sattı; yüksek kaliteli görselleri, düzeni göz önünde bulundur." | **Her ürün sayfasının kendi tasarım dili olur** (renk, yazı tipi, bölüm biçimi, imza bölümü) ve ürünün gerçek kitlesine göre kurulur. **Ortak marka çekirdeği** yalnız: Ayluna işareti + yazısı, satın alma akışı (kartla %5 önce, kapıda ikinci, kapıda butonunda fiyat yok), 30 gün iade, teyitsiz bilgiye yer tutucu, yasaklar. **Yeni sayfadan önce canlı sayfa telefonda incelenir;** satan kalıplar (görseller, paket, düzen) korunur, sorunlu olanlar (çelişkili sayı, sağlık iddiası) alınmaz. Bir önceki satırdaki "diğer sayfalar E'nin dilini alır" kuralı geri alındı. |
| 18 Eki | (Galaxy USB Yön A'ya) "A'yı beğendim ama sarı rengi beğenmedim; her ürün için o koyu lacivert bizim marka rengimiz, sadece diğer renkler değişsin. Ürünümün rengi beyaz. Biraz daha animasyon ekleyelim. Herkesin odası kısmı UI olarak daha iyi görünsün; güven ve baskılayıcı kısımlarını da yapalım" | **Koyu lacivert #1A2142 her ürün sayfasında marka rengidir** (başlıklar, seçili durum, ana buton, güven ve baskı kartları); ürüne göre değişen yalnız ikinci renk, zemin tonu, yazı tipi ve bölüm biçimi (Galaxy USB: buz mavisi #8FD3FF, zemin #F2F4F8). **Sarı yok.** **Ürün gerçek renginde:** Galaxy USB beyaz; siyah tedarikçi fotoğrafı kullanılmaz. **Daha çok hareket, ama her biri anlamlı ve sürekli sakin döngü:** özellik kutuları kendi işini gösterir (fiş takılır, disk döner, boyun sallanır, gece lambası yanar, cetvel dolar). **Herkesin odası = hikâye kartı:** ilerleme çubukları, dokun: ileri/geri, altta dört oda düğmesi, her karede önerilen disk. **Güven:** dört kart (kargo, 30 gün, kapıda ödeme, WhatsApp) + kart logoları. **Baskı:** tek lacivert kart (stok çubuğu, dün satılan, gün sonu sayacı); sayılar gerçek veriden, yoksa yer tutucu. |
| 18 Eki | "USB adaptör yok ama içindeki diskler bunlar ve 12 diskli" (mağaza afişini paylaştı) | **Galaxy USB kutusu = projektör + 12 film diski; USB adaptör yok** (afişteki "USB adaptör hediye" yazılmaz; sayfa "laptop, powerbank ya da evdeki USB'li telefon şarj başlığı" der). **Diskler afişten tek tek kırpılır ve gerçek hâliyle gösterilir;** kutuda olmayan desen (kelebek, kara delik) görselde ya da sahne adında kullanılmaz. Afişten: "2'si 1 arada: galaksi projektörü ve gece lambası". |
| 18 Eki | (Galaxy USB eleştirmen önerilerinden üçünü seçti) + "Kutuda 12 film diskinin görsellerini yine tekrar üret. Fontlar, renk seçimleri pek hoşuma gitmedi; başka hangi renkleri seçebiliriz?" | **Kartla %5 ana butonun içinde** (ikinci satır "Kartla %5 indirim dahil"); güven kutusunda "Kapıda ödeme" yerine "Kartla güvenli öde". **Baskı tek satır,** butonun hemen üstünde (stok elle yazılır, veri yoksa satır gizlenir); kart içi sayaç, stok çubuğu, parlama yok; **tek sayaç** üst şeritte, yapışkan çubukta da yok. **Oda seçimi küçük çipler,** görselin içinde. **Disk görselleri net olur:** afiş kırpıntısı küçükse desen değiştirilmeden yapay zekâyla büyütülür (Higgsfield upscale; uzun şerit reddedildi, 4×3 ızgara geçti), 384px. **Renk ve yazı tipi beğenilmezse** lacivert sabit kalır, seçenekler aynı düzende yan yana panolarla gösterilir, kullanıcı seçer. |
| 18 Eki | "Ben Yön A'yı seçmiştim, onun daha sakin düzenini kullanalım ama yaptığın animasyonları beğendim, onları kullanalım. Flow'u kullan görsel içinde" + "açtım Chrome'dan" | **Seçilen yönün düzeni korunur;** yeni tur yalnız istenen parçaları ekler (burada animasyonlar), düzeni baştan kurmaz. Yön A'nın sakin düzeni: tam ekran fotoğraf, başlık ve küçük resimler görselin içinde, özellik ve güven birleşik çizgili kutuda (kart yığını yok), koyu bölümlerde yazı görselin içinde. **Bulut oturumu kullanıcının Chrome'una bağlanamaz** (Claude in Chrome yok). ~~Görsel işi Higgsfield ile yapılır~~ → 18 Eki düzeltmesine bak: **Higgsfield'da üretim yok.** |
| 18 Eki | (Galaxy USB renk seçenekleri: Kuzey ışığı, Pembe nebula, Mercan, Ay gümüşü) Kullanıcı **Ay gümüşü**nü seçti | **Galaxy USB dili: gümüş #D3DCEE + lacivert, zemin #F4F5F7, Fraunces + Figtree.** Eleştirmen bunu 4/10 ile sona koymuştu (LunaDream'e benzer, ikinci renk yok); kullanıcı sakin, tek renkli lacivert-gümüş ve yumuşak serifi seçti → **eleştirmen kullanıcının sakin/serif zevkini düşük tahmin ediyor;** renk kararını hep kullanıcıya bırak. Seçenekteki eksikler giderildi: açık zeminde ikinci ton arduvaz mavisi #56658A (5,5:1), kahramanda "çevir." tek seferlik Fraunces eğik, kargo noktası arduvaz, oda çipleri 48px. |
| 18 Eki | (Yön A'nın "Bu gece tavanda ne olsun?" ekran görüntüsüyle) "Bunu koymanı istiyorum; oradaki tasarım dili daha güzeldi, oradaki yazı fontu vesaire; sadece o section'u ve yazı fontunu al" | **Galaxy USB yazı tipi Yön A'nınki: Bricolage Grotesque 800 + Figtree** (renk Ay gümüşü kalır; Fraunces bırakıldı). Kahramanda vurgu kelimesi ince ağırlık (500) + gümüş. **"Bu gece tavanda ne olsun?" sahne kartları** satın almanın hemen altında: 272×380 yaşam fotoğrafı, büyük başlık ve alt satır görselin içinde, yavaş süzülme. Yalnız kutudaki disklerle örtüşen sahneler (Ay, Satürn, Denizanası, Kuzey ışığı); kelebek ve kara delik alınmadı. **Ders:** kullanıcı bir yönü seçtiyse o yönün yazı tipi ve imza bölümleri "beğenilen dil"dir; renk dışındaki şeyleri değiştirmeden önce sor. |
| 18 Eki | "Ürün görsellerindeki alttaki ufak kutudaki önizlemeler (hem LunaDream'de hem USB'de): fotoğraflar kendiliğinden geçsin, ürün görselleri de önemli, sadece görünmesin, kaydırılır olsun; altlarına ürünümüzün tasarımı olan ay animasyonunu koy, sayfa geçtikçe tamamlanıyor gibi olsun; USB'ye de onun tasarımına uygun bir şey koy" | **Galeride küçük resim kutusu yok.** Galeri parmakla kaydırılır (scroll-snap), 5 sn'de kendiliğinden geçer, elle kaydırınca durur (hareket azaltılmışsa hiç geçmez). **Gösterge ürünün dilinden:** LunaDream'de her fotoğrafa bir ay, geçtikçe evreler yanar, son fotoğrafta dolunay; Galaxy USB'de her fotoğrafa bir film diski, geçtikçe dolar, o anki döner. Sağda "3/9". USB galerisine mağazanın "Esnek gövde" afişi eklendi (yalnız teyitli bilgi); başlık yalnız ilk fotoğrafta. |
| 18 Eki | (Galeri göstergesine) "1/4 falan yazmasın ama" | **Galeride sayı yazmaz** ("1 / 4", "3/9" yok); ilerlemeyi yalnız gösterge anlatır (ay evreleri, film diskleri). Sıra ekran okuyucu için görünmez metin olarak kalır. USB'de küçük "Temsilî görseller" notu kalır. |
| 18 Eki | "Stoklar elle girilecek şekilde olacak, unutma. Bunların hepsi (ek teklifler) güzel bir şekilde sepette gelecek. Artık ana sayfa tasarlayıp hepsini derleyebiliriz; kalan ürünlerim için kendi sayfa düzenlerine uygun basit tasarımlar. Sitemdeki her kısım burada da aynı şekilde gelmeli; sitedeki kendi görsellerini kullan. Reklama açık 2 ürünüm bunlardı." + eleştirmenin ana sayfa/sepet önerileri için "bunlara gerek yok bence" | **Stok satırı her ürün sayfasında elle** (Shopify bölüm ayarı: sayı + aç/kapa; Shopify stoğuna bağlı değil). **Sepet:** "Siparişine özel" üç teklif (dokununca eklenir, ay dolar; mağaza fiyatı düz yazı), Hızlı Kargo teslimat seçeneği, kartla %5 toplam, iki buton; krem + lacivert. Teklifler bugün EasySell formundan geliyor; Shopify'da sepete ayrıca kurulacak. **Ana sayfa canlıdaki sırayla** (duyuru → menü → slayt → yorumlar → ürünler → ikon çubuğu → AyFeneri → bülten → alt bilgi); marka dili krem + lacivert, Young Serif + Onest. **Eleştirmenin ana sayfa/sepet satış önerileri reddedildi** (kartın farkı, slayta fiyat, iki büyük ürün kartı): bu tasarım böyle kalır. Kalan sayfalar aynı üst bant, menü ve alt bilgiyle: Tüm ürünler, İletişim (iki kopya birleşti), Kargo takip, İade ve değişim, 404/arama/boş sepet. |
| 18 Eki | (AyFeneri/Galaksi Night oda sahneleri Higgsfield'da üretilirken) "Dur dur, görselleri Flow'dan üreteceksin dedim ya; Higgsfield'dan üretme, kredi harcama" | **Görsel üretimi yalnız Google Flow (Nano Banana Pro) ile.** Higgsfield'da üretim, düzenleme, büyütme yok: kredi harcanmaz (yalnız kullanıcı açıkça isterse). "Flow'u kullan" = Google Flow. Bulut oturumunda Flow'a erişim yoksa (Chrome bağlantısı yok) başka araca geçilmez: istemler ve referans görseller hazırlanır, kullanıcıya sorulur (claude.ai sohbetinde Claude in Chrome + Flow ya da kullanıcı üretir). Bu turda mesaj gelmeden 10 görsel gönderilmişti (~27,5 kredi); yeni iş gönderilmedi. |
| 18 Eki | "Galaksi Night için Yön A, AyFeneri için de A; ama çıkarılabilir taban kısmını çıkart. 'Oda karanlık, duvarda ay' kısmını ayın tam göründüğü, düzgün çalışan hâle getir. İki ürün için de metin içeren görsel tarzı, ürünün nasıl göründüğünü gösteren oda vb. kısımlar oluştur." | **Sahne kartında ana nesne (ay, ürün) kırpılmaz;** kart oranı görsele göre seçilir, yazı ana nesnenin üstüne geliyorsa kartın alt şeridine iner. Işık açılıp kapanan sahnede kapalıyken yansıma (ay) görünmez. **Her imza ürün sayfasında yazısı görselin içinde oda sahneleri** (oda adı + o odadaki an, yavaş süzülme) ve en az bir büyük görsel kart (hediye / avucuna sığar). Kullanıcı yön seçtikten sonra gelen eleştirmen raporundan yalnız seçimle çelişmeyenler alınır. |
| 18 Eki | "Şimdi bana tüm iskeleti index olarak gönder; önce eksiklerini kontrol ederek yap ama tüm eksik kısımları düzelt; sepet vesaire tüm her kısım tam çalışır olsun; Shopify için düzenlerken de aynı şekilde" | **Teslim = çalışan site, pano değil.** Önce denetim (her bağlantı, düğme, form, sepet, ödeme, kapıda, boş hâller, politikalar, 320px), eksikler listelenir ve hepsi düzeltilir; sonra gerçek tarayıcıda uçtan uca tıklama testi (ürün → sepet → ödeme → teşekkür; ürün → kapıda formu) geçmeden gönderilmez. Seçilen paket/model/seçenek sepete aynen gider. Shopify teması da aynı test listesinden geçer (`ogrenme/site-denetimi.md`). |
| 18 Eki | "Sitede gördüğün gibi bırak o kısımları, gerekirse ben doldururum; siteyi index olarak da gönder, bakıp eksiklerini çıkarayım" | **Köşeli yer tutucular ([unvan], [N], [teyit]…) sitede kalır; kullanıcı gerekirse doldurur.** Teyit için tekrar sorulmaz, teslimde yalnız kısaca hatırlatılır. Site her teslimde **tek dosya index.html** olarak da verilir (bütün sayfalar, görseller ve kod içinde; sunucusuz açılır). |
| 18 Eki | (LunaDream ekran görüntüleriyle) "Şu kısım dönsün, ilk hali öyle başlasın; sonra bugün 16'ya kadar verilen siparişler aynı gün kargoda, orada bir sayaç dönsün. Stokta'yı kaldıralım, altına dün şu kadar kişi satın aldı yapalım; diğer USB için de bu baskılayıcıları koyabiliriz" | **Aynı gün kargo gerçek:** iş günü 16.00'ya (İstanbul) kadar verilen sipariş aynı gün kargoda; sayfada bu kurala göre canlı sayaç (16.00'dan sonra ve hafta sonu sayaç yok, "yarın / Pazartesi kargoda"). **Dönen satır:** hediye/disk satırı önce, sonra kargo + sayaç; giren alttan, çıkan yukarı, yükseklik sabit. **Fiyat satırında "Stokta" yok;** altında "Dün [X] kişi satın aldı", sayı elle (veri yoksa gizli). Üst şeritteki fiyat sayacına ek ikinci sayaç bu kullanıcı isteğiyle serbest ("tek sayaç" kuralının istisnası; aynı ekranda en çok iki sayaç, farklı amaç). Aynı baskı satırları USB'de de. |
| 18 Eki | (Hızlı Kargo da "aynı gün" diyordu, farkı soruldu) "Öncelikli kargo oluyor işte" | **Hızlı Kargo = öncelikli hazırlık:** "Siparişin sıranın önüne alınır, öncelikli hazırlanıp kargolanır." "Aynı gün" sözü Hızlı Kargo'da kullanılmaz; aynı gün kargo standart kargonun kuralıdır (iş günü 16.00). Sepet, kapıda formu, ödeme, teşekkür, kargo politikası ve takip sayfası buna göre. Canlı mağazadaki Hızlı Kargo ürün açıklaması da aynı şekilde değişmeli. |
| 18 Eki | "Dün kişi satın aldı kısmına 62 yaz, oraya da hafif bir animasyon, tasarım diline uygun." + "Stok kısmı için de uygun bir UI deneyebilir miyiz?" → üç deneme (yıldız dizisi, serif sayı, buton kurdelesi); eleştirmen C 8/10, B 5/10, A 4/10. "C'yi yap." | **Dün satırı** fiyat düşüşünün devamı olarak bir kez girer (satır aşağıdan, sayı yukarıdan, nokta 3 yumuşak halka). **Stok = buton kurdelesi:** Güvenli Ödeme butonunun üst kenarında lacivert hap, azalan ay (hediye hilalinin aynası), "Son N adet"; ayrı stok satırı yok. Kurdele dokunmayı engellemez, buton ekrana girince bir kez belirir. **Stok için nokta dizisi kullanılmaz** (dizinin boyu örtük payda olur, oranlı çubuk yasağının kılık değiştirmiş hâli). |
| 18 Eki | (Dönen satırın ekran görüntüsüyle) "Şurayı lacivert rengimize çevirsek daha bütün görünür renk olarak" | **Dönen satır lacivert** (#1A2142 zemin, ay beyazı yazı, ışık yalnız hilalde; sayaç çipi yarı saydam beyaz). Satın alma alanındaki vurgu kutuları bej/amber değil marka laciverti: dönen satır, stok kurdelesi ve paket kurdelesi aynı renk ailesi. |
| 18 Eki | (Stok kurdelesi, Dün 62 ve lacivert dönen satır USB'ye de gelsin mi?) "Evet ona da gelsin" | Galaxy USB'de de: lacivert dönen satır (diskler lacivert halkalı), fiyatın altında "Dün 62 kişi satın aldı", buton kurdelesi "Son [N] adet". USB'nin ana butonu lacivert olduğu için kurdele **ay gümüşü zemin + lacivert yazı** (paket kurdelesinin tersi); iki satırlı butonda üst iç boşluk 16px ki yazı kurdelenin altında kalmasın. Satın alma alanının baskı unsurları ürünler arasında ortak kalıp; renk her sayfanın kendi paletinden. |
| 19 Eki | "Görsel kısımlarında hatalar görüyorum; seçim kısmında kız erkekte arkasında siyahlık var, USB'de de var; doğru görselleri yapmamız gerekiyor." | **Neden:** site üretimi arka planı temizlenmiş (saydam) ürün kesimlerini JPEG'e çeviriyordu; saydam kısım siyah oluyordu (tuvalde PNG olduğu için görünmüyordu). **Kural:** saydam görsel her çıktıda saydam kalır (sitede WebP, Shopify'da PNG/WebP); JPEG yalnız saydamlığı olmayan fotoğrafa. Teslimden önce gerçek site çıktısında seçim kartlarına bakılır; test.js model kartı görsellerinin saydam olduğunu dener. |
| 19 Eki | (İki ürün görseliyle) "USB'nin diskleri böyle, buna göre revize et." Sonra: 12 disk, hepsi bunlar; "hem renkli hem renksiz attığım gibi, onlar zaten Ay vesaire olduğu için o renkte". | **Galaxy USB kutusu = 12 disk: 6 renkli** (Kızıl sarmal, Mavi nebula, Ay yüzeyi, Yıldız yağmuru, Mavi galaksi, Yıldız kuşağı) **+ 6 beyaz** (Dolunay, Satürn, Uzay balinası, Samanyolu, Bulut sarmalı, Uzak galaksi). Eski afiş diskleri kalktı. **Sayfada yalnız kutudaki desen görünür:** tavanında denizanası (Genç odası) ve kuzey ışığı (İkimiz için) olan fotoğraflar kaldırıldı; sahneler Dolunay, Satürn, Galaksi. Yerlerine Flow istemi hazır (`ogrenme/flow-istemleri-usb-oda.md`). |
| 19 Eki | (Yumuşatılmış USB disklerine) "Kalitesini arttırmamışsın ama bitanem" | **Küçük kaynak görsel yumuşatılarak bırakılmaz, gerçekten büyütülür:** yerelde Real-ESRGAN x4plus (ücretsiz, bu makinede; `araclar/gorsel/sr.py`). Higgsfield ve kredi yok. Önce kaynağın büyük aslı aranır (canlı mağaza JSON'u), yoksa SR. Teslimden önce büyük önizlemede (236 px tavan yansıması) bakılır. |
| 19 Eki | (Fotoğraf dili önerisine: gece belgeseli / gerçek an / stüdyo kartı) "Benim şu anda yaptığım ve kullandığım ürün görselleri tarzında yapmayı düşünüyorum, yazısı vesaire. Sen fotoğraf kısmını Shopify'daki ile aynı şekle getirsene." | **Ürün görselleri kullanıcının kendi afiş tarzında kalır** (yazılı, ikonlu kare afiş); yeni fotoğraf dili dayatılmaz, eleştirmenin "metin HTML'de olsun" önerisi uygulanmaz. **Galeri = Shopify:** canlı mağazanın görselleri, Shopify sırası, kare (1:1), logo bandının altında; üstüne başlık, gölge ya da yüzen öğe binmez (`araclar/canli_galeri.py` → `ogrenme/galeri-canli.json`). Yalnız uydurma yorum/satış rozeti, sağlık ya da güvenlik iddiası ve kutuda olmayan şey gösteren afiş çıkarılır; teyitsiz teknik ifade (5K, katman sayısı) kullanıcının afişi olduğu için kalır, kontrol listesinde. |
| 19 Eki | (İmza sayfası galerisinin altındaki koyu şeridin ekran görüntüsüyle) "Bu altında görsellerin böyle kalmayacak değil mi, tam ekran olacak." Seçenekler gösterildi, seçim: "Şerit kalksın". | **Galerinin altında koyu bant yok:** fotoğraf kenardan kenara kare; ay/disk göstergesi ve "Temsilî görseller" notu fotoğrafın altında sayfanın kendi zemininde. Üstteki koyu logo bandı kalır (kullanıcı: "boşver kalsın"). Dört imza sayfasında (LunaDream, Galaxy USB, AyFeneri, Galaksi Night) aynı. |
| 19 Eki | (Galeri ve Bir gece ekran görüntüleriyle) "Aynı sorun tüm sayfalarda var, o gömülü olsun fotoğrafların değiştiği zımbırtı; estetiği bozan hiçbir detay istemiyorum." Sonra: "Temsili görseller yazısı da duruyor hâlâ." | **Galeri göstergesi fotoğrafın içine gömülür:** en alt kenarda ortada ince çizgiler (her fotoğrafa bir, geçilenler beyaz, hafif gölge); fotoğrafın altında satır, sayaç, not yok. Simge (ay, disk, fener) gömülü göstergede kullanılmaz: afişlerin alt yazısına biner. **"Temsilî görseller" / "Görseller temsilîdir" notu fotoğraf altına yazılmaz** (yalnız politika metninde). Galeri, cihazda "animasyonları azalt" açıkken de geçer (kaymadan, anında); hiçbir sayfada galeri durmaz. |
| 19 Eki | "WhatsApp zımbırtılarını ve şirketi de kaldır, ben onları sonra kendim ekleyeceğim; şu an için istemiyorum." | **Sitede WhatsApp yok** (düğme, menü satırı, güven kartı, SSS/politika metni, tema ayarı); "bize yaz" İletişim sayfasına gider. **Şirket bilgisi yok** (unvan, MERSİS, adres, KEP, telefon; alt bilgi ve politika kartları). Kullanıcı ekleyene kadar geri konmaz; yayından önce yasal zorunluluk olduğu KURULUM'da hatırlatılır. |
| 19 Eki | (Temayı yükleyip yayına alınca) "Kapıda ödeme için Kaching bundle bağlıydı, o çalışmıyor; direkt 2'li seçili olarak geliyor, seçili olmadan gelsin." Sonra: "Kapıda ödeme kısmını ben koyacağım, sen koyma." Seçim: "Bizim kartlar, arkada Kaching." Satış yaptığı site olduğu için temayı geri kaldırdı. | **Açılışta paket seçili değil** (eski temadaki Kaching gibi; seçimsiz alım 1 adet). **Kapıda ödeme düğmesini tema koymaz:** kullanıcı EasySell ile koyar; tasarımdaki Kapıda düğmeleri Shopify'da gizli, satın al düğmesinin altında EasySell için yuva (easysell-form kancası + uygulama blokları). **Paket indirimi Kaching'te:** tasarımdaki paket kartları görünür, Kaching kutusu gizli; kart seçilince Kaching'de aynı paket seçilir, kapıda formu oradan okur, kartla ödemede satırlara `__kaching_bundles` yazılır. **Mağazada deneme:** yayınlanmış temada değil, yayınlanmamış temanın Önizleme'sinde (sipariş kaçmaz). |
| 19 Eki | "Şu anki sitede gelen mesajları ve müşteri fotoğraflarını koyduğum 2 section vardı, onları da mı koysaydık?" | Mesaj görselleri gerçek sohbet ekran görüntüleri (paylaşım izni sohbette görünüyor): sosyal kanıt olarak alınabilir. "Mutlu kullanıcılarımız" fotoğraflarının 6'sından 5'i `hf_` (Higgsfield) üretimi: **yapay zekâ görseli müşteri fotoğrafı diye gösterilmez** (uydurma sosyal kanıt); yalnız gerçek müşteri içeriği (IMG_4145, mesajlardaki fotoğraflar) kullanılır. |
| 19 Eki | "Güvenli Ödeme ile Al'da fiyat yazmasın; %5 fark zaten onlar 80 lira az ödemiş oluyor, kapıda ödemeden farklı olarak orada fiyat yazmasını istemiyorum." | **Kartla öde düğmesinde fiyat yok:** metin yalnız "Güvenli Ödeme ile Al" (ürün sayfası, alt bilgi, masaüstü çubuğu). Fiyat paket kartlarında ve telefondaki alt çubukta kalır. |
| 19 Eki | "Bahsettiğim yorum kısımlarını yapmamışız." | **LunaDream'de "Sizden gelen mesajlar"** (gerçek, izinli sohbet ekran görüntüleri; dokununca büyür) ve "Aileler ne diyor?"da büyük müşteri fotoğrafları (gerçek hikâye eklendi). Sayfanın vaadiyle çelişen mesaj konmaz ("gümrükte", "hayvanlar çıkmadı"). Mesajlar yalnız konu oldukları ürünün sayfasında (eski sitede Galaksi Night'ta da LunaDream mesajları vardı). |
| 19 Eki | "Evet görünüyor" (telefondaki alt çubukta kartla fiyat) | **Telefondaki alt çubukta da fiyat yok:** ürün adı + seçim ("LunaDream / 1 Adet") ve Satın al. |
| 19 Eki | "Şu yorum kısımlarının hepsi karmaşık görünüyor, onlar için bir düzen oturtalım." Üç yön gösterildi (A sekmeli 5/10, B tek akış 8/10, C duvar 4/10); kullanıcı **B**'yi seçti. | **Müşteri kanıtı tek bölüm, tek akış:** puan → öne çıkan tek yorum (çerçevesiz kart) → fotoğraf ve mesajlar aynı yükseklikte tek şerit (fotoğrafla başlar, dokununca büyür) → kısa yorum listesi → hepsini oku → kısa not. Konu çipleri, ayrı mesaj bölümü ve üst üste birden çok şerit yok; fotoğraf ve mesaj sekmeye saklanmaz. |

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
