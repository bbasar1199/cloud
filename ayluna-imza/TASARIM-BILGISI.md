# Ayluna · tasarım bilgi dosyası

Her oturumda `DEVAM.md`'den sonra bunu oku. Burada ne öğrendiğim, neye dayandığı ve nerede çeliştiği var.
Ayrıntılı ham notlar: `ogrenme/` klasörü. Son güncelleme: 17 Ekim 2026.

**Kaynak sırası** (çelişkide üstteki kazanır):
1. Kullanıcının son mesajı
2. Seçilen pano `canvas/Main.dc.html` (tuvalde "Mobil · LunaDream ürün sayfası (seçilen)")
3. Bu dosya
4. Beceriler (`beceriler/`). claude.ai'deki eski sürümleri bayat: "güncel tasarım H yönü, Bricolage + Figtree" yazıyor. Yanlış.

---

## 1. Çalışma biçimi

- Türkçe, kısa. Uzun açıklama yok, istenmeyen dosya gönderme yok.
- Shopify kodu kopyala-yapıştır `.txt` (`shopify/`). Zip yalnız istenirse.
- Mobil önce (390px), masaüstü sonra.
- Beğenilen bölüm silinmez, geliştirilir. Teslimde her bölümün nereden geldiği bir satırla yazılır.
- **Eleştirmen ajan zorunlu.** Her bölüm kararı önce kullanıcıyı taklit eden ajana denetletilir. Ajan en beğendiği 3 fikri seçer; bunlar kullanıcıya ayrı ayrı gösterilir (`onizleme/fikirler.html` gibi). Ajana verilecek kişilik tanımı aşağıda (§1a).
- Her değişiklikten sonra ekran görüntüsü alıp bak (§9). Görmeden "oldu" deme.
- Kararları tuval notuna, pano başlığına ve `DEVAM.md`'ye yaz. Kullanıcı artifact yorumu bırakmıyor (incelenen ~20 artifact'ta yorum yok); karar izi yalnız bu dosyalarda kalıyor.

### 1a. Eleştirmen ajanın kişiliği ("Başar gibi düşün")
Ajan isteminin başına bunu koy:
> Sen Ayluna'nın sahibisin. Türkiye'de Meta reklamıyla telefondan gelen annelere ve büyükannelere gece lambası satıyorsun. 15 ürünün var; cironun çoğu LunaDream'den geliyor. Sayfaya bakarken şunları sorarsın:
> - Bu satar mı? İlk ekranda fiyat, ödeme ve güven var mı?
> - Yazı çok mu? Boğuyor mu? Bir cümle kısalabilir mi?
> - Emoji, uydurma sayı ya da sahte aciliyet var mı? Varsa reddet.
> - "Herkesin Shopify sitesi" gibi mi duruyor? Ya da AI yapmış gibi mi?
> - İnsanların alıştığı kalıp (paket, sayaç, stok, "dün satılan", fayda listesi) atılmış mı? Atılmamalı; gerçek veriyle ve daha zarif hâliyle kalmalı.
> - Hareket doğal mı? Abartı efekt mi?
> - Sayfanın vaadi kutudan çıkanla aynı mı? Değilse iade gelir.
> - Kartla ödemeye yönlendiriyor mu? Kapıda ödeme iadenin ana sebebi.
> Her öneriye 1-10 puan ver. En beğendiğin 3 fikri gerekçesiyle seç. Beğenmediğini açıkça söyle.

## 2. Kullanıcıyı tanı

**Sevmedikleri:**
- emoji ikon
- boğucu, çok yazılı sayfa
- "Shopify teması gibi" sıradan düzen
- tamamen koyu tema
- uydurma sayı ya da sayaç
- abartılı efekt, yıldız animasyonu
- AI görüntüsü kokan tasarım
- süsle başlayan tasarım (brif: "Önceki dört denemenin ortak hatası: tasarım süsle başladı")

**İstedikleri:**
- "acayip ama sıkmayan" tarz
- doğa gibi uyumlu hareket
- güven veren, dönüşüm odaklı sayfa
- bundle (paket)
- ay sonu fiyat sayacı (her ay zam yapıyor)
- sosyal kanıt
- çok ürünlü mağaza hissi
- "gösteriş değil, işe yarayan iyileştirme"

**17 Ekim netleştirmesi:** alışılmış kalıplar (fayda listesi, indirim sayacı, "dün satılan", stok alarmı) atılmaz; inceltilir ve gerçek veriye bağlanır.

**Seçim geçmişi** (tuvallerden çıkarıldı):

| Tarih | Ne oldu |
|---|---|
| Eylül | 4 yön denendi: Nunito/mercan, Sora/indigo, Quicksand/altın, Baloo/pembe. Hepsi reddedildi. |
| ~15-16 Eki | G "önceki sürüm" olarak kaldı (Cormorant + krem + kil). |
| 16 Eki | Önce H, sonra I öne çıktı. I: Poppins, beyaz/lacivert/altın; masaüstüne yalnız bu genişletildi. |
| 17 Eki | Tur 1 Main seçildi: Young Serif + Onest, krem/lacivert/amber. Tur 2 (Işık, Bricolage) ve Tur 3 (İmza, büyük bloklar, paralaks) seçilmedi. |
| 17 Eki, seçimden sonra | Main küçültülüp inceltildi: küçük model kartları, sade paket satırları, 38px sayaç şeridi, emojisiz özellik şeridi, ödeme seçimi. |

**Desen:** kullanıcı büyük ve gösterişli olandan kompakt ve tanıdık olana doğru gidiyor. Yeni öneri "daha az, daha net" yönünde olmalı.

## 3. İş gerçekleri (karar verirken bunlara dayan)

| Konu | Değer | Kaynak |
|---|---|---|
| Gerçek dönüşüm | sipariş ÷ oturum ≈ %1,70 (Shopify'ın gösterdiği %0,34 kapıda ödemeyi saymıyor) | Brif |
| Ortalama sepet | ≈ ₺1.800–1.873 | Brif, İade Röntgeni |
| İade, kapıda ödeme | %28,6 (1.557 gönderiden 446) | İade Röntgeni |
| İade, ön ödeme | %0,8 (356 gönderiden 3) | İade Röntgeni |
| İade nedeni | %92 "Alıcı bulunamadı" (96'nın 88'i); ürün şikâyeti az | İade Röntgeni |
| Kargo iadesi | PTT %40,3 · Aras %26,1 · HepsiJet %17,7 · Sürat %3,6 (küçük örnek) | İade Röntgeni |
| Ürün payı | LunaDream Kız (LD01) cironun %83'ü | İade Röntgeni |
| İade/red, olgun ölçüm | %23,5 | İade Röntgeni |
| Yüksek iadeli iller | Diyarbakır, Gaziantep, Hatay, Muğla, K.Maraş, Ş.Urfa | İade Röntgeni |

**Sonuçlar:**
- **Ödeme tasarımı iade tasarımıdır.** Kartla öde varsayılan ve %5 indirimli görünür. Kapıda öde ikinci, ama saklanmaz.
- Kapıda ödeme seçilince toplam, teslim aralığı ve WhatsApp onayı formda görünür. Mümkünse teslim saati tercihi de eklenir.
- "Alıcı bulunamadı" sayfa metniyle değil teslimat taahhüdüyle düşer: onay mesajı, "yarın kapında" bildirimi.
- PTT rozeti öne çıkarılmaz.
- Başarı ölçüsü teslim edilen ciro: dönüşüm, sepet ve iade/red oranı birlikte izlenir.

**Ürün gerçekleri:**
- LunaDream 1 lamba ₺1.699,99 (₺1.999,00), 2 lamba ₺2.749,99 (₺3.998,00).
- Kız = tavşanlı karusel, Bluetooth ninni hoparlörlü. Erkek = Uzay Kaşifi robot, **hoparlörsüz**.
- Kutuda 6 disk + 6 hediye disk. 2'li pakette hediye sayısı teyitsiz.
- Unicorn diski kutudan çıkmıyor; hiçbir listede gösterilmez (2 şikâyet var).

**Gerçek yorumlar:**
- İsimler: Burak G., Handan B., Abdülkerim T., Sevcan Z., Mehmet C.
- Puan 4,7 · 62 yorum (Loox, teyit bekliyor). Puan elle yazılmaz, Loox'tan çekilir.
- "Elif K.", 2.467, 10.000+, 9.000+, 12.000+ uydurmadır, kullanılmaz.

**Teyit bekleyenler:**
- ölçüler, pil süresi, yaş aralığı
- teslim süresi, 16:00 kesimi
- 2'li pakette hediye disk sayısı
- firma unvanı, WhatsApp, %5 online indirim
- Loox sayıları, 12 diskin adları
- "1 yıl garanti", "LED ısınmaz", "Şarj olurken çalışır", "2 saatte dönüyoruz"

Teyit gelene kadar köşeli yer tutucu kalır: `[X] cm`. Teyit gelmeyen iddia yayından önce çıkarılır.

## 4. Tasarım sistemi (Main.dc'den; Shopify buna göre yazılır)

### Renkler (rol adlarıyla; bölümler sabit hex değil değişken kullanır)
| Değişken | Hex | Nerede | Nerede değil |
|---|---|---|---|
| `--krem` | #F6F1E9 | sayfa zemini | koyu bantlar |
| `--yuzey` | #FFFDF9 | kart, input, koyu üstü yazı | — |
| `--cizgi` | #E3D8C7 | ayraç, kart kenarı (#EDE3D3 ince, #DDD2C1 çip/input) | — |
| `--lac` | #1A2142 | metin, **açık zeminde ana buton**, seçili kart | büyük zemin alanı |
| `--gece` / `--gece2` | #141A36 / #0C1027 | yalnız ürünün ışığını gösteren bant ve sahne, yapışkan çubuk, alt bilgi | sayfanın tamamı |
| `--amber` | #F2A65A | ışık; **koyu zeminde ana buton**, nefes halkası, ay | açık zeminde yazı |
| `--amber2` | #E59A4C | yıldız, ikonun ilk çizgisi | metin |
| `--soluk` | #5C6078 | ikincil metin (krem üzerinde 5,5:1) | — |
| `--etiket` | #8A7F6E → **#766B5B önerilir** | 11px bölüm etiketi. Şimdiki renk 3,5:1, eşiğin altında. | — |
| `--sayac` | #B4651F → **#A05A1C önerilir** | sayaç rakamı. Şimdiki renk krem üzerinde 3,9:1, eşiğin altında. | — |
| `--yesil` | #2E6B4F | "Stokta", %5 rozeti, "Kartla öde" dürtmesi, WhatsApp satırı | dekor |
| `--rozet` | #F3E9DA / #8A4A12 | "Kardeşe" gibi küçük rozet | — |

### Yazı
- **Young Serif 400:** yalnız başlıklarda. H1 50px/.95, −.03em. H2 30px/1.06, −.02em, `text-wrap: balance`.
- **Onest:** gövde 15px/1.5. Rakamlar `tabular-nums`. Önerim gövdeyi 16px yapmak; kitlede büyükanneler var.
- Bölüm etiketi 11px, büyük harf, .12em. Sağında seçili değer 12px/600. Etiket her bölümün üstüne konmaz; yalnız seçim gruplarında.
- 12px altı yazı yok; 9–10,5px yazılar 12'ye çıkar.
- Yükleme: woff2 kendi sunucudan (`onizleme/f/`), `font-display: swap`, latin-ext.
- Main 500 ve 700 ağırlığını da kullanıyor. Shopify'da ya bu ağırlıklar da yüklenir ya da tasarım 400/600'e indirilir.

### Şekil
- Köşe yarıçapları:
  - 28: levha üstü
  - 22: an kartı, disk sahnesi
  - 18: form, video, ürün kartı
  - 16: buton, yorum kartı
  - 14: seçim kartları
  - 12: galeri karesi, input, şerit
  - 999: yalnız çip ve rozet
- Kenar boşluğu 16px. Bölüm üst boşluğu 40–52px. Levha içinde 8–22px.
- Gölge neredeyse yok; ayırma 1–1,5px çizgiyle yapılır. Gölge yalnız ışıklı nesnelerde (disk, plak).
- Dokunma alanı en az 44px. Ana buton 58px, input 50px ve 16px yazı.

### Hareket
- Tek eğri `cubic-bezier(.2,.7,.2,1)`. Süreler 150–600ms. Yalnız transform ve opacity.
- **İmza an:** "Işığı kapat" anahtarı (oda gündüzden geceye, saat 19:30'dan 21:00'e).
- Basma geri bildirimi: `scale(.985)` ile `.94` arası.
- Kaydırmaya bağlı belirme `@supports (animation-timeline: view())` içinde.
- Main'de sonsuz döngüler var: yüzen disk 7sn, mühür 26sn, plak 40sn, buton "nefes" halkası 2,8sn. Yavaş ve sessiz kaldıkça kabul. Yenisi eklenmez. Azaltılmış hareket ayarında hepsi kapanır.

### İkon
Emoji yok. 1,6–1,7px çizgili SVG; ilk çizgi amber. Tek ikon ailesi.

## 5. Sayfa yapısı (Main.dc sırası ve görevi)
| # | Bölüm | Satış görevi |
|---|---|---|
| 1 | Gece sahnesi 500px: ışık anahtarı, galeri 1/11, küçük resim şeridi | Ürünü kullanımda göstermek, imza an |
| 2 | Karar levhası (sahnenin üstüne −30px biner) | İlk ekranda karar. İçinde: puan, Stokta, H1, 4'lü özellik şeridi, Model, Paket, ay sonu şeridi, birlikte al, Ödeme, CTA, kapıda formu, güven üçlüsü, müşteri fotoğrafları |
| 3 | Bir gece, beş an (koyu bant, 20:00–07:30) | Nasıl kullanılır + rutin vaadi |
| 4 | Anneler ne diyor (çipli duvar) | Sosyal kanıt, itiraz kırma |
| 5 | On iki masal, tek lamba (dönen plak, 12 disk) | Çeşitlilik ve değer |
| 6 | Avucuna sığar + kutu satırı | Boyut ve kutu içeriği (iade önleme) |
| 7 | Annelerin videoları | Gerçeklik (video gelince) |
| 8 | 30 gün iade mührü "Önce gör, sonra öde." | Risk kaldırma |
| 9 | Merak edilenler (6 SSS) | İtiraz kırma |
| 10 | Odanın geri kalanı (kategori çipleri) | Çok ürün, sepet büyütme |
| 11 | Kapanış + yasal + dev "Ayluna" | Son CTA, güven, yasal |
| — | Yapışkan çubuk | CTA her an erişilir |

Kodda bir not var: "Sihirli Özellikler (yeri korunur)". Canlı sitedeki bu bölümün yeri kullanıcı isteğiyle korunuyor.

## 6. Kalıp kütüphanesi

**Kazananlar (koru, geliştir):**
- model kartı → paket → toplam → teslim → yapışkan çubuk
- "Işığı kapat" gündüz→gece anahtarı
- disk seç → tavana yansıma
- saatli gece ritüeli
- kutudan ne çıkıyor
- "Kardeşe" 2'li paket
- çipli yorumlar (Uyku / Hediye / Kalite)
- dev marka yazılı alt bilgi
- iade mührü
- "Kartla öde, ₺X daha az öde" dürtmesi
- sayfa içi kapıda formu ("Kart bilgisi istemiyoruz")

**Kaybedenler (tekrar önerme):**
- emoji fayda listesi, kurdeleli "EN ÇOK TERCİH"
- pastel/Baloo sevimliliği, Apple-beyaz soğukluğu
- krem + serif + kil şablonu
- her bölümde fade-in, 0→21 gibi sayan rakamlar
- harf aralıklı büyük harf etiket yığını
- aynı radius ve gölgeli eş kart ızgarası
- tek ekran karar sayfası
- büyük paralaks bloklar, 3B makaralar (Tur 3)
- kaydırarak sipariş ("swipe to buy")

**Yedekteki fikirler** (sorulursa):
- Kapıya kadar zaman çizgisi
- Hangisi onun? (büyük foto model seçimi)
- Kutuyu aç
- Kardeşin gecesi
- Anne notları destesi
- Hediye notu kartı
- "Kimin için?" seçici
- Ay atlası (çok ürünlü ana sayfa için)

## 7. Dürüstlük ve mevzuat
Kaynaklar `ogrenme/arastirma.md`'de (51 açılmış kaynak). Bu bir bilgi notu, avukat görüşü değil; ✓ işaretliler Resmî Gazete metninden doğrulandı.

**Temel kurallar:**
- Uydurma sayı, isim ve yorum yok. Puan ve sayı Loox'tan gelir; veri yoksa blok gizlenir, sabit "62" gösterilmez.
- Aciliyet yalnız gerçek kurala bağlıdır: ay sonu zammı (gerçekten varsa), gerçek stok eşiği, Flow'dan gelen "dün satılan". "X kişi bakıyor" yok.
- Elle girilen sayı tarih taşır, eskiyince gizlenir.
- Sağlık iddiası ve teyitsiz teknik rakam yok. Sayfa vaadi = kutu içeriği.

**İndirim gösterimi (Ticari Reklam Yönetmeliği m.14, 1 Ağustos 2026 değişikliği):**
- ✓ "Önceki fiyat" artık indirim başlangıcından önceki **10 gün** içinde uygulanan en düşük fiyat (eskiden 30 gündü).
- ✓ Önceki fiyat yalnız o kanalda belirlenir. Trendyol'daki fiyat ayluna.shop'taki indirime referans olamaz.
- ✓ Şartlı indirimler de bu maddeye tabi (belirli miktar, tutar ya da işlem şartına bağlı olanlar). "Kartla öde %5" ve "2 lamba kazancı" bu kapsama girebilir.
- Üstü çizili fiyat gösteriliyorsa önceki fiyat, kampanyanın başlangıç ve bitiş tarihi, sınırlı stoksa adet de yazılır. İspat satıcıdadır. Ceza aralığı 99.339 – 39.916.524 TL.
- **Main'e etkisi:**
  - ₺1.999,00 son 10 günde ayluna.shop'ta gerçekten uygulanmadıysa üstü çizili gösterilemez.
  - ₺3.998,00 (2 × ₺1.999) 2'li paketin gerçek bir önceki fiyatı değil. Daha güvenli ifade: "2 ayrı almaya göre ₺649,99 daha az".
  - Ay sonu zammı varsa "Ekim fiyatı bitiyor" yanına yeni fiyat yazılır: "1 Kasım'dan itibaren ₺X".
  - %5 ve paket kazancı için hukukçu teyidi alınmalı.

**İade ve cayma (Mesafeli Sözleşmeler Yönetmeliği):**
- Yasal cayma 14 gün, teslimle başlar. Ödeme 14 gün içinde iade edilir; satıcının kargosuyla dönüş ücretsizdir.
- Yasal hakkı Ayluna'ya özel avantaj gibi sunmak haksız uygulamadır (Ek A/9).
- Önerilen metin: "30 gün iade: ilk 14 gün yasal cayma hakkın, Ayluna bunu 30 güne uzatır." 15–30. günlerin koşulu ve kargoyu kimin ödediği yazılır.

**Yorumlar (m.28/B, 1 Ağustos 2026):**
- ✓ Satın alımı doğrulanamayan yerden gelen yorum yayımlanamaz.
- Olumlu ve olumsuz yorumlar ayrım yapılmadan en az 1 yıl yayımlanır, objektif sıralama kullanılır.
- Tedarikçi ya da başka ürünün yorumu taşınamaz. Yalnız olumlu yoruma hediye verilemez.
- Ağustos 2026'da olumsuz yorumu gizleyen bir firmaya 2,17 milyon TL ceza verildi.
- PDP'ye not: "Yorumlar yalnız Ayluna'dan sipariş verenlerden toplanır, tümü yayımlanır."

**Sayaç ve aciliyet:**
- Sahte "kısa süre" iddiası her durumda yasaktır (Ek A/7).
- Sayaç herkese aynı sabit tarihi göstermeli, **İstanbul saatine** göre çalışmalı ve oturumla sıfırlanmamalı. Şu an cihaz saatine göre çalışıyor; düzeltilecek.
- Önceden seçili ücretli ek yasaktır. "Birlikte al" kutusu boş başlamalı; şu an öyle.
- Kapıda ödemeyi gizlemek ya da zorlaştırmak karanlık tasarım riskidir. Kart varsayılan olabilir, ama iki seçenek eşit görünür kalır.

**Satıcı kimliği:**
- Ticaret unvanı, MERSİS, merkez adresi, KEP, e-posta ve telefon ana sayfada ve "İletişim"te bulunmalı.
- Fiyat KDV dahil gösterilir. Kapıda ödeme ücreti varsa baştan yazılır.
- Yayından önce `[Firma unvanı]`, `[numara]` ve ETBİS yer tutucuları dolmalı.

**Kart:**
- Kart için ek ücret alınamaz (5464 m.17). Online karta indirim ise aykırı görünmüyor.
- Kapıda kartla ödemeden, kapıda nakitten fazla ücret alınmaz.

**AI görsel:**
- AI ile üretilmiş anne-çocuk görselleri gerçek müşteri deneyimi gibi sunulamaz.
- Flow görselleri "ürün sahnesi"dir; "müşteri" etiketi taşıyamaz.

**Araştırmanın tasarım önerileri:**
- Galeride küçük resim şeridi (Main'de var). Sekme yerine dikey açılır bölümler.
- Birim fiyat ve tahmini teslim tarihi (Main'de var). Teslim aralığı 5–7 günden geniş olmamalı.
- Puan dağılımı çubukları ve filtreleri (Main'de yok). Olumsuz yorumlara görünür yanıt.
- Gövde yazısı en az 16px; büyükanneler için 17–18px daha iyi. Dokunma alanı 48px (Shopify önerisi).
- Taksit: tekli sepetlerin %98,9'u tek çekim; 2'li pakette (2.500–5.000 TL) %43,9'u 2–3 taksit seçiyor. "3 taksit" satırı yalnız 2'li pakette anlamlı. Toplam, taksit sayısı ve tutar birlikte yazılır.
- Instagram uygulama içi tarayıcıda otomatik video, Apple/Google Pay ve 100vh güvenilmez çalışıyor.
  - Sayfa videosuz da satmalı.
  - Sahnede `svh` kullanılır, yapışkan çubukta `env(safe-area-inset-bottom)`.
  - Gerçek cihazda Instagram içinden denenir.
- Horizon'da özel öğelerin en güvenli yeri `blocks/` altında tema bloğu olarak `_product-details` içi. `product-information` çatallanmaz, böylece tema güncellemesi kolay kalır. Bugünkü yöntem ayrı bölüm + özel şablon; karar §12'de.

## 8. Shopify teknik kuralları
- **Kaynak gerçek:** bölümler Main.dc'den türetilir. Şu an derleyici CSS'i `iskelet.html`'den alıyor (`araclar/shopify-derle.py:16`). Main'e geçince değiştirilmeli.
- Her bölüm tek `.liquid`:
  - CSS `#ay-{{ section.id }}` kapsamında
  - JS tek IIFE, bölüme özel önek
  - `{% schema %}` ile tüm metinler düzenlenebilir
- Ürüne bağlı bölümlere `"enabled_on": {"templates": ["product"]}` eklenir. Sabit `id="siparis"` gibi kimlik çakışmasına dikkat.
- Fiyat tek kaynaktan: varyant `price` ve `compare_at_price`. Yüzde, adet fiyatı ve kazanç formülle hesaplanır.
- Bilinen hatalar (düzeltilecek):
  - `?variant=` adresi yok sayılıyor; reklam linki yanlış modeli açıyor
  - eşleşme yoksa sessizce ilk varyant seçiliyor
  - tükenmiş varyant satılabiliyor
  - kart indirim kodu boşken bile %5 düşük fiyat gösteriliyor
  - kaydırma düğmesi klavyeyle çalışmıyor
  - bant yapışmıyor (sticky iç kutuda)
  - masaüstü kuralları 430px sütunun içine sıkışıyor
- Kapıda ödeme uygulaması: buton seçicisi ayardan alınır. Bulunamazsa sessizce `/checkout`'a düşmez, uyarı verir. Gerçek uygulamayla telefonda denenir.
- Tema düzenleyici:
  - Yeniden yüklemede kopya oluşmasın diye `data-ready` işareti kullanılır.
  - Satıcı önizlemesi `request.design_mode` ya da `?onizleme=` ile açılır, müşteri görmez.
  - `shopify:section:unload` ile dinleyiciler temizlenir.
- Performans:
  - Sahne görseli `eager`, `fetchpriority=high` ve `srcset` ile yüklenir; gece görseli `lazy`.
  - Videolar `preload="none"`; yalnız ekrandaysa oynar.
  - Fontlar bir kez tanımlanır (bugün 15 bölümde tekrar ediyor).
- Shopify'ın `shopify-liquid` becerisinde `search_docs` ve `validate` betikleri var. Liquid yazmadan önce doküman ara, teslimden önce doğrula.

## 9. Araçlar
- Telefon ekranı görüntüsü:
  - Sayfalar için: `NODE_PATH=$(npm root -g) node ayluna-imza/araclar/ekran-goruntusu.js <çıktı> [index.html|iskelet.html|fikirler.html]`
  - Tuval panosu için: `NODE_PATH=$(npm root -g) node ayluna-imza/araclar/dc-onizle.js ayluna-imza/canvas/Main.dc.html <çıktı.png> '{"pay":"kapida","form":true}' <y> <yükseklik>`. Yollar artık betiğe göre çözülüyor.
  - Tuvaldeki görsellerin yalnız 11'i yerelde var (`canvas/magaza/`); oda ve disk görselleri boş görünür.
- Shopify derleme: `python3 ayluna-imza/araclar/shopify-derle.py` (Liquid ve şemayı denetler). Sahte verili önizleme: `araclar/shopify-onizle.js`.
- Görsel üretimi:
  - Ürün asla sıfırdan üretilmez. Gerçek fotoğraf referans alınır; yalnız sahne, ışık ve zemin değişir.
  - Araç: Google Flow (Nano Banana Pro), flow.google.com, "Eki 17 - 02:24" projesi. Referanslar `lunadream-8.png` (kız) ve `lunadream-erkek.png` (robot).
  - Görselde yazı üretilmez; metin HTML'de eklenir.
  - Teslimden önce büyütüp bakılır: el, yazı ve ürün detayı.
  - Not: galerideki mağaza posterlerinde yazı var. Kural "yazısız kısım kırpılır" diyor; galeri için yazısız kareler tercih edilmeli.
- Tuval: https://claude.ai/artifact/CHmRtH4tjbapGmPtuQGsTH. Yayın kuralları `DEVAM.md`'de.

## 10. Çalışma ortamı ve eklentiler (17 Ekim, "5 eklenti" rehberinden)
Rehberdeki 5 eklentinin işlevini bu bulut ortamına uyarladım:

| Eklenti | Ne yapıyor | Burada | Karar |
|---|---|---|---|
| Omniroute | Limit dolunca başka yapay zekâ sağlayıcılarına geçiyor | Bulut oturumunda model değiştirilemiyor. Mağaza ve müşteri verisi üçüncü taraflara gider. | Kurulmadı |
| Claude Mem | Oturumlar arası hafıza | Konteyner her oturumda silinir; yerel hafıza kaybolur. Hafıza depoda tutulur: `CLAUDE.md`, `DEVAM.md`, bu dosya. | Depo hafızasıyla karşılandı |
| Headroom | Bağlamı kırpıp token tasarrufu | Oturum bağlamı kendiliğinden özetliyor. Büyük okumalar alt ajanlara veriliyor. | Gerek yok |
| Claude Code setup | Depoyu tarayıp eksik hook, beceri, MCP ve ajanı öneriyor | Anthropic'in resmi eklentisi, katalogda var. Yöntemi uygulandı: `ayluna-imza/CLAUDE.md`, `.claude/agents/ayluna-elestirmen.md`. | Uygulandı, kurulum önerildi |
| Task Observer | Düzeltmeleri izleyip becerileri yeniden yazıyor | Bulutta arka plan izleyici yok. Aynı iş "Düzeltme günlüğü" kuralıyla yapılıyor (§11). | Kuralla karşılandı |

Sonraki adım önerileri (kullanıcı isterse):
- Bir hook: `shopify-kaynak/*.liquid` değişince `shopify-derle.py` kendiliğinden çalışsın.
- `shopify/*.txt` elle düzenlenmesin; bu dosyalar derleyicinin çıktısı.
- `CLAUDE.md` ve `.claude/agents/` ana dala da alınsın. Yeni oturum başlarken kendiliğinden yüklenirler.

## 11. Düzeltme günlüğü (öğrenme döngüsü)
Kullanıcı bir şeyi düzeltince buraya bir satır eklenir: tarih · ne dedi · çıkan kural. Kalıcı kural `beceriler/`'e de işlenir.

| Tarih | Kullanıcı ne dedi | Çıkan kural |
|---|---|---|
| 17 Eki | "Kendini tasarımda inanılmaz seviyeye getir, tüm dosyaları ve eğitimleri öğren" (daha önce de söylemiş) | Her oturum `TASARIM-BILGISI.md` ile başlar. Öğrenilen her şey depoya yazılır, sohbette kalmaz. |
| 17 Eki | Fayda listesi, sayaç, stok, "dün satılan" atılmasın | Tanıdık kalıp korunur, inceltilir, gerçek veriye bağlanır. |
| 17 Eki | Ödemede öncelik online (%5), kapıda ikinci | Kartla öde varsayılan; bütün CTA'lar seçimi taşır. |

## 12. Açık kararlar (kullanıcıya sorulacak)
1. Main'de "dün satılan" ve stok satırı yok, ama 17 Ekim notu bunları istiyor. Eklensin mi? Önerim: Stokta noktasının yanına ince tek satır. Yalnız gerçek veri varsa görünsün.
2. 16:00 kargo kesimi Main'de duruyor ama teyitsiz; RAPOR'a göre kaldırılmıştı. Teyit mi, kaldırma mı?
3. Brif 1/2/3 paket istiyor, Main'de yalnız 1 ve 2 lamba var. 3'lü eklensin mi?
4. Gövde yazısı 15px mi kalsın, 16px mi olsun? Önerim 16px.
5. Alt CTA'lar (Bir gece kartı, kapanış) her zaman "Kapıda öde" ve indirimsiz fiyat diyor. Ödeme seçimine bağlansın mı? Önerim: evet.
6. Kargo logolarında PTT kalsın mı? İade verisine göre önerim: hayır.
7. Üst kampanya bandı: Main'de yok, Shopify'da var. Sayaç şeridiyle birlikte sayfada iki kez çıkıyor. Hangisi kalsın?
8. Üstü çizili ₺1.999,00 son 10 günde ayluna.shop'ta gerçekten uygulandı mı?
   - Evet: kampanya tarihleri yazılır.
   - Hayır: üstü çizili fiyat kaldırılır ve "1 Kasım'dan itibaren ₺X" gibi gerçek zam bilgisi verilir.
   - 2'li pakette ₺3.998,00 yerine "2 ayrı almaya göre ₺649,99 daha az" önerilir.
9. "Kartla %5" ve paket kazancı için hukukçu teyidi alınsın mı? Şartlı indirim artık m.14 kapsamında.
10. İade metni "14 gün yasal + 16 gün Ayluna" diye açılsın mı? 15–30. günlerde kargoyu kim ödüyor?
11. Yapı: bugünkü gibi ayrı bölüm + özel şablon mu, yoksa Horizon'un ürün bloğu içinde tema bloğu mu? Tema bloğu güncellemeye daha dayanıklı.
12. 2'li pakette "3 taksit" satırı gösterilsin mi? Ödeme sağlayıcısının taksit sınırı teyit edilmeli.
