# Ayluna mobil PDP: araştırma notları (17.10.2026)

Biçim: **Kural → neden → [kaynak]**. Etiketler: **[D]** açılan kaynakta okundu/doğrulandı · **[Ç]** benim çıkarımım/önerim · **[Z]** zayıf kanıt (satıcı blogu, forum anekdotu).
Hukuki maddeler bilgi notudur, avukat görüşü değildir. Kaynak numaraları en alttaki listeye bakar.

## 0. Karar özeti (en önemli 10 madde)
1. **İndirim referansı artık SON 10 GÜN** (30 değil). 01.08.2026'dan beri "indirimden önceki fiyat" = indirimin başladığı tarihten önceki 10 günde **aynı kanalda** uygulanan en düşük fiyat. [D] [S10][S12][S13]
2. Üstü çizili fiyat/% indirim gösteriyorsan önceki fiyat + **başlangıç ve bitiş tarihi** + (varsa) sınırlı stok adedi de görünmeli. [D] [S15][S16][S18]
3. **Şartlı indirimler de artık Madde 14 kapsamında** (14/7: miktar/tutar/işlem şartına bağlı indirim). "2'li pakette ₺650 tasarruf" ve "kartla öde %5 indirim" buna girebilir → tarih/ispat yükü doğar. [D: madde] [Ç: Ayluna'ya uygulanışı; hukukçuya teyit ettir]
4. **Cayma hakkı 14 gün** (teslimden başlar), iade kargo bedeli tüketiciye yüklenemez. "30 gün iade" = yasal 14 gün + Ayluna'nın ek 16 günü olarak yazılmalı. [D] [S23]
5. Kanunun verdiği hakkı (14 gün ücretsiz cayma) **Ayluna'ya özel avantaj gibi sunmak yasak** (Ek A/9). [D] [S15]
6. Yorumlar: **yalnız satın alanlar**, olumlu/olumsuz ayrımsız, ≥1 yıl, objektif sıralama; başka satıcı/ürün yorumu (tedarikçi/AliExpress importu) yanıltıcı sayılır. Ağustos 2026'da yorum gizleyen firmaya 2.167.412 TL ceza. [D] [S10][S11][S19][S20]
7. Sahte geri sayım/"son X adet"/sahte sepet-favori sayısı = haksız ticari uygulama riski; Eylül-Ekim 2026'da denetim yoğun. [D] [S15][S16][S20][S21]
8. Mobil galeride **thumbnail** kullan (Horizon'da "mobile pagination: thumbnails" seçeneği var); ana içerikte yatay sekme yerine **dikey açılır bölüm**. [D] [S2][S3][S41]
9. ₺1.699,99'luk tekli sepet, ulusal veride neredeyse hep tek çekim (0–2.500 TL bandı %98,9). 2'li ₺2.749,99 ise %43,9'un 2–3 taksit seçtiği bantta → taksiti **2'li pakette** öne çıkar. [D: veri] [S27] [Ç: uygulama]
10. Instagram/Facebook uygulama içi tarayıcıda otomatik video, Apple Pay/Google Pay ve 100vh güvenilmez; sayfayı videosuz da satacak şekilde kur. [Z] [S50][S51] [D: viewport birimleri S45]

## 1. Baymard: mobil ürün sayfası ve ödeme bulguları
- Mobil PDP'lerin yalnız %38'i "decent" ve üstü (masaüstü %48) → hatasız temel uygulama bile fark yaratır. [D] [S1]
- **Galeri:** Ek görselleri thumbnail ile göster (mobil sitelerin %76'sı göstermiyor). Neden: noktalar küçük, yanlış dokunma çok; thumbnail görsel türlerini (ölçek, kutu içeriği, video) önceden gösteriyor. Son thumbnail'ı yarım göstererek "devamı var" sinyali ver; kaydırma birincil, thumbnail yedek. [D] [S2]
- **Ölçek görseli:** Sitelerin %37'sinde yok. → Lambanın el/komodin/çocuk odası yanında gerçek boyutunu gösteren 1 kare + tavana yansıma alanını gösteren 1 kare koy. [D] [S1] [Ç: içerik]
- **Video/360:** Thumbnail şeridinde video karesi açıkça işaretlensin, yoksa atlanıyor. [D] [S2]
- **Sekme yok, dikey bölüm var:** Yatay sekmeler gözden kaçıyor (sitelerin %29'u hâlâ kullanıyor). Mobilde uzun sayfada "Vertically Collapsed Sections", kısa sayfada açık bölümler. Uzun metni kes ama "devamını oku" açık işaretlensin. [D] [S3]
- **Fazla metin:** Herkes açıklamayı okuyor ama metin bloğu "özellik çöplüğü" gibi algılanıyor. 2–6 ana özelliği "görsel + kısa başlık + tek paragraf" vurgularıyla anlat; ikincil bilgiler "Diğer özellikler" listesine. [D] [S4]
- **Varyant seçimi:** Seçenekleri açılır menü yerine buton olarak göster (sitelerin %57'si yapmıyor). → "1 Adet / 2'li Kardeş Paketi" iki büyük buton. [D] [S1] [Ç: Ayluna uyarlaması]
- **Birim fiyat:** Çoklu pakette birim fiyat göster (%81–86 göstermiyor); toplam fiyat baskın, birim fiyat ikincil ama bulunur olsun. → 2'li: "₺2.749,99 · tanesi ≈ ₺1.375". [D] [S1][S6]
- **Toplam maliyet ve teslim tarihi:** Satın alma alanında kargo dahil toplam maliyet tahmini göster (%67 göstermiyor). Kargo hızı yerine **tahmini teslim tarihi** ver; tarih aralığı 5–7 günden geniş olmasın; kullanıcı tarihi söz olarak algılar, tutturamazsan güven kaybı. [D] [S1][S7]
- **İade politikası:** PDP'de özet + link (%44'ünde yok); footer'da da link. [D] [S1]
- **Yorumlar:** Kullanıcıların %95'i yorumlara bakıyor. En çok kullanılan parça puan dağılımı çubukları. Çubuklar tıklanınca filtrelemeli, filtre gizli olmamalı (gizliyken kullanım %7–11). 5 ve daha az puanda dağılımı gizle. %53'ü özellikle olumsuz yorumları arıyor. Olumsuz yorumlara görünür biçimde cevap ver (%87–89 vermiyor). Yorumcu fotoğrafları tek bir kaydırmalı katmanda gezilebilsin. [D] [S1][S5][S9]
- **Sepet terki nedenleri:** Ek maliyet %40, yavaş teslimat %20, siteye kart bilgisi verme güvensizliği %19, hesap zorunluluğu %18, iade politikası %13, ödeme yöntemi azlığı %9 (ortalama terk %70,22). → Kargo/kapıda ücreti, teslim süresi, iade ve kart güvenliği PDP'de satın alma butonunun yakınında olmalı. [D] [S8]
- **Yapışkan sepete ekle:** Baymard'ın açık bir araştırmasını bulamadım. Tek mağaza A/B testinde sepete ekleme +%6,8 artarken dönüşüm −%7,7 ve RPV −%22 (sonuç belirsiz). → Horizon'un yerleşik çubuğunu aç ama **test et**; dönüşümü/geliri izle, sadece sepete ekleme oranına bakma. [Z] [S34] [D: Horizon davranışı S41]
- **Ödeme formu:** Baymard'a göre sitelerin %54'ünde adres doğrulayıcı yok, %93'ü uyarlanabilir hata mesajı kullanmıyor; mobil klavye hataları çok. Kapıda ödemede yanlış adres = iade maliyeti. [D] [S9]

## 2. Türkiye'ye özel güven normları
- Pazaryeri alışkanlığı [D, kısmen]: Trendyol PDP/kartlarında satış adedi ("son 3 gün"), sepetteki/favorideki kişi sayısı, "Hızlı Teslimat" etiketi, satıcı puanı görünüyor. Hepsiburada'da "Soru Cevap", "Resmi Satıcı" rozeti, ürün ve satıcı puanı ayrı. Trendyol satıcı puanı PDP'de renkli gösteriliyor; arkasında kargoya teslim süresi, soru cevaplama süresi, iptal ve iade oranları var. [S29][S30]
- → Kural [Ç]: Türk alıcı PDP'de "kim satıyor, ne zaman kargoda, kaç kişi aldı, soru sorabilir miyim" cevabını arar. Ayluna PDP'sinde şunlar olsun: (a) gerçek satış/yorum sayısı, (b) "Bugün 14:00'e kadar siparişler bugün kargoda · Tahmini teslim: 20–22 Ekim" ve kargo firması adı, (c) WhatsApp ile soru sor (cevap süresi yaz), (d) fotoğraflı yorumlar, (e) "Satıcı: <ticaret unvanı>" satırı.
- Ödeme payları (2025, Ticaret Bakanlığı): kartlı %62,5, havale/EFT %29,2, kapıda %3,5, diğer %4,8; kartlı ödemelerin %64,1'i 3D Secure. [D] [S26] [Ç: bu ulusal hacim pazaryeri ağırlıklı; Meta'dan gelen DTC trafiğinde kapıda payı çok daha yüksek olabilir, kendi verine bak]
- Taksit (iyzico 2025): 0–2.500 TL sepetlerde %98,9 tek çekim; 2.500–5.000 TL'de %54,3 tek çekim, %43,9 2–3 taksit. Anneler Günü en yüksek sepet ortalaması (2.212 TL). BDDK sınırları kategoriye göre değişiyor (rapor: elektronikte en fazla 4 ay). [D] [S27] → Tekli üründe taksit tablosu kalabalık yapar; 2'li pakette "3 taksit" satırı ver; taksit sınırını POS sağlayıcıdan teyit et. [Ç]
- Taksit gösterimi kuralı: Taksit reklamında **toplam fiyat + taksit sayısı + taksit tutarı birlikte** okunur boyutta olmalı (Kılavuz m.6/7). [D] [S16]
- Kapıda ödeme pratiği: tahsilatı kargo firması yapar, tahsilat komisyonu ~%2–5, para 3–7 iş gününde gelir; alıcı teslim almazsa gidiş-dönüş kargo satıcıya kalır; ödeme "Nakit veya Kartla" olabilir. [D, sektör blogu] [S28]

## 3. Yasal: PDP metnini doğrudan etkileyenler
**3.1 İndirim gösterimi (Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği m.14)**
- 14/3: önceki fiyat = indirim başlangıcından önceki **10 gün** içindeki en düşük fiyat (hizmet/çabuk bozulanlarda bir önceki fiyat). Yürürlük 01.08.2026 (RG 01.07.2026/33297). [D] [S10][S12][S13]
- 14/5: Önceki fiyat yalnız o kanalda belirlenir; Trendyol/mağaza fiyatı ayluna.shop indirimine referans olamaz. [D] [S10][S14]
- 14/7: Belirli miktar, sayı, tutar veya işlem şartına bağlı indirim reklamları da m.14'e tabi (ürün miktarı gösterme kuralları hariç). Not: 2022 Kılavuzu "3 al 2 öde" türünü indirimli satış tanımı dışında sayıyordu; 2026 değişikliği bunu kapsama aldı. [D] [S10][S14][S16]
- Gösterim: önceki fiyat, başlangıç/bitiş tarihleri, sınırlı miktar varsa adet; ispat yükü reklam verende. Bakanlığa göre en sık ihlaller: tarih yazmamak, istisnaları küçük puntoya saklamak, "%50+%20" gibi belirsiz katlı indirimler. 6502 idari para cezası mecraya göre 99.339–39.916.524 TL. [D] [S15][S16][S18]
- Temmuz 2025'te güncellenen Kılavuz 30 günü anlatıyor; 01.08.2026'dan beri yönetmelik 10 gün diyor. Yönetmelik esas alınır. [D: ikisi] [S17][S10] [Ç: öncelik]
- → Ayluna kuralları [Ç]: (a) Sabit fiyatta Shopify "compare-at" alanını boş bırak. (b) Kampanya yapacaksan önceki fiyat, son 10 günün en düşük ayluna.shop fiyatı olsun; PDP'de "Kampanya: 20.10–31.10.2026" yaz; fiyat geçmişini (ekran görüntüsü/CSV) sakla. (c) "Kartla öde %5" ve "2'li pakette tasarruf" ifadelerinde iki net fiyatı yaz, yüzde/tasarruf iddiasını kanıtlanabilir tut; süresizse bunun m.14/1 tarih şartını nasıl karşıladığını hukukçuya sor.

**3.2 Yorumlar (yeni m.28/B, 01.08.2026 + Tüketici Değerlendirmeleri Kılavuzu 2023)**
- Yalnız ürünü satın alan yorum yapabilir; satın alımı doğrulanamayan kanaldan gelen yorum yayımlanamaz; olumlu/olumsuz ayrımı yapılmadan en az 1 yıl, tarih/puan gibi objektif ölçüte göre, yönlendirme yapılmadan yayımlanır; kurallar konu sınırlaması getiremez (ör. "kargo hakkında yorum yapılamaz" olmaz). [D] [S10][S11][S19]
- Başka satıcı veya başka ürünle ilgili yorum yanıltıcıdır, yayımlanmaz. → Tedarikçi/AliExpress/benzer ürün yorumu içe aktarmak yasak. [D] [S19 m.8/2]
- Yasak manipülasyonlar: sadece olumluyu yayımlamak, hazır olumlu şablon, olumsuz yorumu geri çektirmek için müşteriyle temas, **sadece olumlu yorum için hediye/indirim**, olumsuz yorumu zorlaştırmak, açıklanmayan puanlama yöntemi. [D] [S19 m.8/5]
- Bilgilendirme zorunluluğu: doğrulama süreci, tüm yorumların yayımlanıp yayımlanmadığı, ortalama puanın nasıl hesaplandığı ve sıralama mantığı açıkça yazılmalı; reddedilen yorumun gerekçesi tüketiciye bildirilmeli ve düzeltip tekrar gönderme hakkı verilmeli. [D] [S19]
- 2023 Kılavuzu, başka sitedeki gerçek alıcı yorumunun kaynağı ("X sitesinden") veya linkiyle paylaşılmasına izin veriyordu. 2026 metni ise satın alımı doğrulanamayan kanaldan gelen yorumu yasaklıyor. [D] [S19 m.5/5-c][S10] → Instagram DM veya WhatsApp ekran görüntüleri ancak bir sipariş numarasıyla eşleşiyorsa ve kaynağı yazılıyorsa kullanılmalı. [Ç]
- Denetim: Ekim 2026'da yorum/puan satan, favori ve sepete ekleme botu sunan adreslere erişim engeli; Ağustos 2026'da gerçek olumsuz yorumu gerekçesiz yayımlamayan firmaya 2.167.412 TL ceza. [D] [S20]
- → Ayluna [Ç]: Yorum uygulamasında "doğrulanmış alıcı" rozeti, puan dağılımı, olumsuz yorumlar görünür ve yanıtlı, varsayılan sıralama "en yeni"; PDP'de "Yorumlar yalnızca Ayluna'dan sipariş verenlerden toplanır, tümü yayımlanır" notu.

**3.3 Aciliyet, stok, sosyal kanıt**
- Ek A/7: Tüketiciyi bilinçli karar veremeyecek şekilde acele ettirmek için malın sadece çok kısıtlı süre sunulacağını gerçeğe aykırı söylemek her durumda haksız uygulama. [D] [S15]
- Fiyatın süre veya stok sınırı varsa süre ve stok adedi açıkça yazılır (m.13/9, Kılavuz m.6/9). Kılavuz örneği: gerçekte fazlası varken "son 3 oda kaldı". [D] [S15][S16]
- 2023'te Reklam Kurulu önceden seçili opsiyonlar ve diğer seçenekleri zorlaştıran arayüzler için ceza verdi ("karanlık ticari tasarım"). Ücretli ek hizmet tüketicinin açık onayı olmadan önceden seçilemez (Kılavuz m.5/2). [D] [S22][S16]
- Tüketici Birliği Federasyonu Eylül 2026'da sıfırlanan geri sayım sayaçlarının oturumdan bağımsız taranmasını önerdi. → Sayaç denetimi gelmesi muhtemel. [D: öneri] [S21] [Ç: tahmin]
- AI ile üretilen görsel/ses/video aldatıcı olamaz; insanla ayırt edilemeyen AI karakterler tüketici davranışını belirgin etkiliyorsa açıkça belirtilmeli (18/8); gerçek kişilerin AI kopyasıyla ürünü kullanmış/önermiş izlenimi yasak (27/12). Influencer içeriği "Reklam/Tanıtım + marka" etiketiyle, kaydırmadan görünür olmalı (23/A). [D] [S10] → AI "anne-çocuk" görselleri gerçek müşteri deneyimi gibi sunulmasın. [Ç]

**3.4 Mesafeli satış ve iade (Mesafeli Sözleşmeler Yönetmeliği)**
- m.9: 14 gün içinde gerekçesiz ve cezasız cayma; mal satışında süre teslimle başlar. m.12: 14 gün içinde tüm ödemeler iade edilir. Satıcının belirttiği taşıyıcıyla gönderilirse, ya da satıcı taşıyıcı belirtmemişse, iade masrafı tüketiciden istenemez. m.13: tüketici 10 gün içinde geri gönderir; ürünü işleyişine uygun kullanmaktan doğan değişiklikten sorumlu değildir. m.16: teslim en geç 30 gün. [D] [S23]
- m.5 ön bilgilendirme: temel nitelikler, satıcı adı/unvanı, MERSİS, açık adres/iletişim, **vergiler dahil toplam fiyat**, varsa tüm nakliye/teslim ek masrafları, ödeme ve teslimat bilgisi, cayma şartları/süresi/usulü ve iade taşıyıcısı. [D] [S23]
- → PDP iade metni [Ç]: "**30 gün iade.** İlk 14 gün yasal cayma hakkınızdır (anlaşmalı kargo ile ücretsiz). Ayluna, bu süreyi 30 güne uzatır: 15–30. günlerde <koşul + kargo kimde>." "Koşulsuz/ücretsiz iade" ifadesini öne çıkarıyorsan bu yasal kısmın Ayluna'ya özel olmadığını belli et (Ek A/9).

**3.5 Satıcı kimliği ve fiyat**
- Kendi sitesinde satan tacir: ticaret unvanı, MERSİS, merkez adresi; herkes: KEP, e-posta, telefon, varsa işletme adı/tescilli marka, meslek odası bilgisi. Bunlar **ana sayfada ve doğrudan ulaşılabilen "İletişim" başlığı altında** olmalı (ETHS Yönetmeliği 2022 m.5). Esnafsa ad-soyad, VKN, adres. [D] [S24]
- Fiyat tüm vergiler dahil toplam satış fiyatıdır; teslimat ücretleri fiyatla birlikte gösterilir. [D] [S15][S16] → Kapıda ödeme bedeli varsa PDP'de ve ödeme adımında baştan yazılmalı. [Ç]
- 5464 m.17: Üye işyeri, kart kullanıldığı için komisyon vb. adla ek ödeme isteyemez. [D] [S25] → Online kartı %5 ucuzlatmak kart sahibine ek yük değil, doğrudan aykırı görünmüyor. Ama "kapıda kartla" ödemeye "kapıda nakit"ten fazla ücret alma. [Ç]

## 4. Online ödemeye yönlendirme (kapıda ödeme yerine)
- Kanıt düzeyi: Kapıda ödemenin iade/teslim almama oranının ön ödemeliden 2–4 kat fazla olduğu ve %5 ön ödeme indiriminin standart taktik olduğu satıcı verilerinde geçiyor; metodoloji yok. [Z] [S31]
- Çerçeve: Thaler'den beri "nakit indirimi" ile "kart ek ücreti" farklı algılanıyor. Bir çalışmada indirim sunulunca başka yöntemi tercih edecek müşterinin nakit ödeme olasılığı %19 arttı. Yalnızca etiketin etkisi tartışmalı. [D] [S33] → İndirimi kazanç olarak anlat ("Kartla öde, ₺85 kazan"). Kapıda ödemeyi ceza gibi gösterme. [Ç]
- Kurallar [Ç]:
  1. PDP'de iki net fiyatı yan yana yaz: "Kartla online **₺1.614,99** · Kapıda ödeme ₺1.699,99". 2'li için "₺2.612,49 / ₺2.749,99". Sadece "%5" yazıp hesabı müşteriye bırakma (Baymard birim fiyat mantığı).
  2. Kart satırının hemen altına güven bilgisi koy: ödeme altyapısı, 3D Secure, "kart bilgileriniz Ayluna'da saklanmaz" (doğruysa). Neden: sepet terkinde kart güvensizliği %19. [S8]
  3. Ödeme adımında online kart ilk sırada olabilir; Shopify payment customization ile yeniden adlandırılıp sıralanabiliyor. Ama kapıda ödeme aynı ekranda eşit görünür kalmalı. Seçeneği gizlemek/zorlaştırmak karanlık tasarım riski taşır. [D: Shopify yeteneği S42; ceza emsali S22]
  4. Kapıda siparişte teşekkür sayfasında ve WhatsApp onay mesajında "şimdi kartla öde, %5 iade/indirim" bağlantısı ver (Shopflo modeli: kapıda siparişi iptal edip ön ödemeli siparişe çevirir). [D: mekanizma S32] [Z: etki S31]
  5. Instagram içi tarayıcıda Apple Pay/Google Pay butonları görünmeyebilir. Kart formu ve 3D Secure SMS adımı webview'da sorunsuz test edilmeli. [Z] [S51]
- Riskler [Ç]: marj kaybı (%5 × online pay); ilk kez alan ve güvenmeyen kitlenin kapıdan vazgeçip hiç almaması (yaşlı alıcı); 14/7 şartlı indirim yükümlülükleri; bir kampanya gibi sunulursa tarih şartı.

## 5. Paket, aciliyet ve dürüst sosyal kanıt
- **2'li "Kardeş Paketi"** [Ç + S6]: Varyant butonu olsun. Etiket "2'li Kardeş Paketi · tanesi ≈ ₺1.375". Tasarruf yazılacaksa "2 ayrı almaya göre ₺649,99 daha az" (3.399,98 − 2.749,99). Bu ancak tekli fiyat gerçekten ₺1.699,99 olarak duruyorsa doğru; 14/7 nedeniyle kanıtını sakla. "En çok tercih edilen" rozeti ancak sipariş verisi bunu gösteriyorsa kullanılır.
- **Hediye/büyükanne** [Ç + S1]: Sitelerin %78'i PDP'de hediye seçeneği göstermiyor. Ayluna'da "Hediye paketi / fiyatsız fatura / not ekle" satırı büyükanne alıcı için güçlü olabilir; test et.
- **Ay sonu zam sayacı** (yalnız gerçekse) [Ç + S15/S16]: Zam kararı yazılı ve tarihli olsun. Sayaç herkese aynı sabit tarih/saate (TSİ) gitsin, oturumla sıfırlanmasın. Tarih geçince fiyat gerçekten artsın. Yeni fiyatı üstü çizili "indirim" gibi gösterme; "1 Kasım'dan itibaren ₺1.899,99" yaz. Sonra indirime dönersen referans fiyat son 10 günün en düşüğüdür.
- **Gerçek stok:** Horizon `product-inventory` bloğu gerçek `variant.inventory_quantity` değerini okur. Varsayılan eşik 10, adet gösterimi açık. [D] [S41] → Eşiği düşük tut (ör. 5). Stok Trendyol ile ortaksa ve Shopify tek doğruluk kaynağı değilse adet gösterme. [Ç]
- **"Dün X adet gönderildi":** Liquid satış sayısını vermez. Sipariş verisinden günlük bir metafield'a yaz (Flow/Admin API), kayıt tut. Rastgele sayı üreten "şu an 23 kişi bakıyor" uygulamalarını kaldır. [Ç] Sahte sepet/favori sayısı Ekim 2026 denetim konusu. [D] [S20]

## 6. Mobil tipografi, performans ve uygulama içi tarayıcı
- **Gövde metni ≥17–18 px, en az 16 px** [Ç + S48]: Yaşlılar için çalışmalar büyük puntoyu tercih ediyor (İngilizce metin için 14–22 pt aralığı). Belli bir boyutun üstünde okuma hızı yeniden düşüyor; satır aralığını 1,4–1,6 tut. Büyükanne kitlesi için kontrast yüksek, gri-açık metin yok.
- **Form alanları ≥16 px** olsun, yoksa iOS odakta yakınlaştırır ve geri uzaklaştırmaz. `maximum-scale=1` kullanma, erişilebilirliği bozar. [D] [S49]
- **Dokunma hedefi:** Shopify mobilde 48×48 px öneriyor; WCAG 2.2 AA alt sınırı 24×24 px. Buton ve varyant düğmeleri ≥48 px. [D] [S40][S47]
- **Türkçe:** `<html lang="tr">`, büyük harf dönüşümünde i→İ doğru çalışsın (tarayıcı desteği değişken). Fontun latin-ext (ş, ğ, ı, İ) glifleri olmalı ya da sistem fontu kullanılmalı. [D: text-transform S46] [Ç: font]
- **Performans hedefleri:** p75'te LCP ≤2,5 s, INP ≤200 ms, CLS ≤0,1. Lighthouse mobil profili 150 ms RTT, 1,6 Mbps ve 4× CPU ile "yavaş 4G" benzetimi yapar; Meta trafiği için iyi bir vekil. [D] [S43][S44]
- **Shopify kuralları** [D] [S40]: LCP görseline `fetchpriority="high"` ver; ilk ekranda lazy-load ve fade animasyonu kullanma; `image_url` + `srcset/sizes` ile servis et; script'leri `defer` et, bloklayan uygulama script'lerini kaldır; en fazla 1–2 `preload`; fontlar Shopify CDN'den ya da sistem fontu.
- **Bütçe** [Ç]: İlk ekranda tek kahraman görsel (mobilde ~100–150 KB AVIF/WebP). Yorum, paket ve sayaç uygulamalarından ancak tema bloğuyla değiştirilemeyenleri tut. Her yeni app script'inden sonra Lighthouse mobil ölçümü yap.
- **Viewport:** `vh` = `lvh`, tarayıcı çubuğu açılınca içeriğin altını keser. Kahraman alanda `svh`, sabit alt çubukta gerekirse `dvh` kullan; `dvh` kaydırırken yeniden boyutlanıp titreme yapabilir. [D] [S45] Instagram iOS içinde 100vh beyaz şerit bırakıyor ve dvh/svh beklendiği gibi çalışmıyor diye forum raporları var. [Z] → Sabit alt çubuğa `padding-bottom: env(safe-area-inset-bottom)` ver; Instagram ve Facebook uygulamaları içinde iOS ve Android'de gerçek cihazla test et. [Ç]
- **Video:** Instagram iOS tarayıcısında MP4 donuk kalma şikâyeti var, kesin çözüm yok. [Z] [S50] → Video LCP olmasın, `poster` zorunlu, `muted playsinline` kullan. Satış mesajı videosuz da tam olsun; ilk karede ürün ışığı görünsün. [Ç]
- **Cüzdanlar ve oturum:** Instagram/Facebook'tan gelen ziyarette Apple Pay/Google Pay butonları görünmeyebiliyor (2020–2024 raporları). [Z] [S51] Kullanıcı Safari'ye geçerse sepet çerezi taşınmaz. [Ç]

## 7. Shopify Horizon: uyumlu özel geliştirme
- **Mimari** [D] [S41]: Ürün şablonu `product-information` bölümü. İçinde statik `_product-media-gallery` ve `_product-details` blokları var, altta `disclosures` ve `product-recommendations`. `_product-details` şunları kabul eder: `@theme`, `@app`, text, price, variant-picker, buy-buttons, accordion, review, product-inventory…
- **Kural** [Ç + S35][S41]: Ayluna öğelerini (ödeme fiyat kutusu, teslim tarihi, paket seçici, iade özeti) `blocks/` altında **tema bloğu** olarak yaz ve `_product-details` içine ekle. `sections/product-information.liquid` dosyasını çatallama; böylece Horizon güncellemeleri kolay birleşir. Özel dosyaları `ayluna-` önekiyle ayır.
- **Tema blokları** [D] [S35][S37]:
  - `blocks/` klasöründe dururlar ve `{% content_for 'blocks' %}` ile render edilirler.
  - Editörde görünmeleri için en az bir `preset` gerekir.
  - Şema tek ve geçerli JSON olmalı. Tema blokları yerel blok tanımlayamaz.
  - İç içe en fazla **8 seviye** (bölüm hariç). `tag` en fazla 50 karakter.
- **Kısıt:** Bir bölüm ya kendi (yerel) bloklarını ya tema bloklarını destekler, **ikisini birden destekleyemez**. [D] [S35]
- **Statik bloklar** [D] [S36]:
  - Söz dizimi: `{% content_for "block", type: "...", id: "..." %}`.
  - Satıcı taşıyamaz, silemez, kopyalayamaz. `block_order` içinde yer almazlar, `max_blocks` sayısına girmezler.
  - Satıcının yanlışlıkla silmemesi gereken yasal metinler (iade özeti, satıcı satırı) için uygundur. [Ç]
- **App blokları** [D] [S39]: Şemaya `@app` ekle (`limit` verme, hata verir). Statik render edilen bölümlerde çalışmazlar. Yorum uygulamasını `_product-details` içine app bloğu olarak yerleştir.
- **Limitler:** JSON şablonda en fazla 25 bölüm, bölüm başına en fazla 50 blok. [D] [S38]
- **Galeri:** `_product-media-gallery` mobil sayfalama seçenekleri dots / counter / hint / thumbnails → **thumbnails** seç (Baymard). [D] [S41][S2]
- **Yapışkan sepete ekle:** Bölüm ayarı `enable_sticky_add_to_cart`. Asıl satın alma butonları ekranın üstünden çıkınca IntersectionObserver ile görünür. [D] [S41]
- **Güncelleme:** Horizon repo'sunu `upstream` remote olarak ekleyip `git pull upstream main` ile güncelle. Horizon türevleri Theme Store'a gönderilemez. `shopify theme check` çalıştır. [D] [S41]
- **Ödeme adları:** Payment customization fonksiyonu ödeme yöntemlerini yeniden adlandırabilir, sıralayabilir, gizleyebilir. İndirim uygulamaz; indirim ayrı bir mekanizma ister. [D] [S42]

## 8. Açılan kaynaklar
- S1 https://baymard.com/blog/current-state-ecommerce-product-page-ux
- S2 https://baymard.com/research-articles/always-use-thumbnails-additional-images
- S3 https://baymard.com/research-articles/avoid-horizontal-tabs
- S4 https://baymard.com/research-articles/structure-descriptions-by-highlights
- S5 https://baymard.com/research-articles/user-ratings-distribution-summary
- S6 https://baymard.com/research-articles/price-per-unit
- S7 https://baymard.com/research-articles/shipping-speed-vs-delivery-date
- S8 https://baymard.com/lists/cart-abandonment-rate
- S9 https://baymard.com/blog/mobile-ux-ecommerce
- S10 https://www.resmigazete.gov.tr/eskiler/2026/07/20260701-9.htm (RG 01.07.2026/33297, yürürlük 01.08.2026)
- S11 https://www.dunya.com/ekonomi/ticaret-bakanligi-acikladi-sahte-yorumlara-yaptirim-uygulanacak-haberi-842114
- S12 https://www.dunya.com/gundem/once-zam-sonra-indirim-oyununa-son-bakanlik-tarih-verdi-haberi-834077
- S13 https://www.ekonomist.com.tr/gundem/gercegi-yansitmayan-indirim-algisina-yeni-onlem-indirim-oncesi-fiyat-artik-boyle-belirlenecek-77267
- S14 https://www.ticimax.com/blog/indirimli-satis-reklamlari-yeni-kurallar
- S15 https://www.resmigazete.gov.tr/eskiler/2015/01/20150110-5.htm (yönetmeliğin asıl metni + Ek)
- S16 https://www.alomaliye.com/2022/04/26/fiyat-bilgisi-iceren-reklamlar-ile-indirimli-satis-reklamlari-ve-ticari-uygulamalari-hakkinda-kilavuz/
- S17 https://www.capital.com.tr/haberler/tum-haberler/tuketiciyi-korumak-icin-adim-indirimli-urunlerde-fiyat-gecmisi-sarti-geldi
- S18 https://www.btso.org.tr/guncel/haberler-ve-duyurular/haber-duyuru-detay/60765
- S19 https://www.alomaliye.com/wp-content/uploads/2023/09/tuketici-degerlendirmeleri-kilavuz.docx
- S20 https://indigodergisi.com/2026/10/e-ticarette-sahte-yorum-begeni/
- S21 https://yenihavadis.net/tuketicinin-yorumuna-sansur-alisverisine-karanlik-tasarim/
- S22 https://www.aa.com.tr/tr/ekonomi/karanlik-ticari-tasarimlar-reklam-kurulunun-radarina-girdi/2964843
- S23 https://www.resmigazete.gov.tr/eskiler/2014/11/20141127-6.htm (Mesafeli Sözleşmeler Yönetmeliği)
- S24 https://www.resmigazete.gov.tr/eskiler/2022/12/20221229-5.htm (ETHS Yönetmeliği)
- S25 https://www.resmigazete.gov.tr/eskiler/2006/03/20060301-1.htm (5464 sayılı Kanun)
- S26 https://www.alomaliye.com/2026/05/12/turkiyede-e-ticaretin-gorunumu-raporu-2025-yayimlandi/amp/
- S27 https://www.iyzico.com/assets/uploads/pdf/iyzico_ecommerce_report_2025.pdf
- S28 https://birfatura.com/kapida-odeme-uygulamasinin-avantaj-ve-dezavantajlari/
- S29 https://sicakfirsatim.com/tartismalar/hepsiburada-trendyol-n11-ve-amazon-da-satici-guveni-nasil-kontrol-edilir
- S30 https://birfatura.com/trendyol-satici-puani-trendyol-magaza-puani/
- S31 https://www.egrow.com/en/blog/cod-vs-prepaid-payment-ecommerce-2026
- S32 https://www.shopflo.com/help/shopflos-rto-suite
- S33 https://money.com/credit-card-surcharges-spending-habits/
- S34 https://cleancommit.io/ab-tests/mobile-bottom-sticky-add-to-cart-button/
- S35 https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks
- S36 https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/static-blocks
- S37 https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema
- S38 https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates
- S39 https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks
- S40 https://shopify.dev/docs/storefronts/themes/best-practices/performance
- S41 https://github.com/Shopify/horizon (README, templates/product.json, blocks/_product-details, product-inventory, _product-media-gallery, assets/sticky-add-to-cart.js)
- S42 https://shopify.dev/docs/api/functions/latest/payment-customization
- S43 https://web.dev/articles/vitals
- S44 https://github.com/GoogleChrome/lighthouse/blob/main/docs/throttling.md
- S45 https://developer.mozilla.org/en-US/docs/Web/CSS/length
- S46 https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform
- S47 https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- S48 https://pmc.ncbi.nlm.nih.gov/articles/PMC9376262/
- S49 https://weblog.west-wind.com/posts/2023/Apr/17/Preventing-iOS-Textbox-Auto-Zooming-and-ViewPort-Sizing
- S50 https://community.shopify.com/t/mp4-video-doesn-t-play-on-instagram-ios-browser/408539
- S51 https://community.shopify.com/t/apple-pay-g-pay-not-available-on-cart-page-when-clicked-through-from-instagram-bio-or-facebook/16591

Erişilemeyen/açılmayanlar: Trendyol ve Hepsiburada ürün sayfaları (403), ticaret.gov.tr duyuruları (503). Pazaryeri normları bu yüzden ikincil kaynaklara dayanıyor.
