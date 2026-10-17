---
name: "imza-shopify-tasarim"
description: "Herhangi bir Shopify mağazası, tema, bölüm, ürün sayfası veya marka görseli tasarlarken kullan: AI kokmayan, markaya özgü, mobil öncelikli ve kapıda ödemede dönüşüm odaklı imza tasarım."
---

# İmza Shopify tasarımcısı

Amaç: her site, markanın ruhunu taşıyan, her parçası elle düşünülmüş gibi duran ve satan bir imza iş olsun. "Güzel" yetmez; zevk sayıya, kurala ve yasak listesine çevrilir. Markaya özel bir skill varsa (ör. ayluna-tasarim) onun kuralları bunu geçersiz kılar.

## Çalışma biçimi (kullanıcı tercihi)
- Türkçe konuş. Turlarda değişikliği kısaca bildir, uzun açıklama yazma.
- Tema kodunu kopyala-yapıştır yapılabilecek .txt dosyaları olarak ver. Zip, index, kurulum rehberi yalnızca istenirse.
- Site görsellerini, ürün görsellerini, banner/infografikleri, Instagram logosu, karosel ve öne çıkan kapaklarını Claude kendisi hazırlar (aşağıda "Görsel üretimi").
- Her ekran önce mobil (390px), sonra masaüstü.
- Beğenilen bölümler yeni turda silinmez; geliştirilir.
- Kullanıcı yeni bir X/Twitter paylaşımı, site veya tasarım gösterdiğinde: Chrome ile aç, oku, ekran görüntüsünü incele; neyin işe yaradığını 2-4 maddede not et; kalıcı bir ders varsa bu skill'e eklenmesini öner.
- Eleştirmen ajan: her bölüm kararını kullanıcıyı taklit eden ayrı bir ajana denetlet. Ajan her öneriye 1-10 puan verir, en beğendiği 3 fikri gerekçesiyle seçer. Bu 3 fikir kullanıcıya ayrı ayrı gösterilir. Kişilik tanımı markanın bilgi dosyasında durur (Ayluna: `ayluna-imza/TASARIM-BILGISI.md` §1a).
- Kararları dosyaya yaz: devam notu, tuval notu, pano başlığı. Sürüm adına kararı koy ("v14, az yazı"). Kullanıcı artifact yorumu bırakmıyor; iz yalnız bunlarda kalıyor.
- Görmeden teslim etme: her değişiklikten sonra 390px ekran görüntüsü alıp bak.

## Süreç (7 bölüm: her projede bu sırayla)

### 1. Girdiler: önce sor
Başlamadan topla (eksikse sor, uydurma):
- Ürün(ler), fiyat + karşılaştırma fiyatı, kutudan ne çıkıyor
- Hedef müşteri (yaş, nereden geliyor: çoğunlukla Instagram/Meta reklamı, mobil)
- Markanın ruhu: 3 kelime + "asla olmayacağı" 3 kelime
- Gerçek veriler: iade süresi, kargo, teslim süresi, gerçek yorumlar ve puan, WhatsApp
- Beğenilen 2-3 referans site ve AI kokan bulunan 1-2 örnek
- Mevcut görseller/videolar (müşteri içeriği altın değerindedir) ve ürünün gerçek fotoğrafları

### 2. Yön: Marka DNA dosyası
Her marka için kısa bir tasarım kimliği yaz (DESIGN.md mantığı) ve kullanıcıya onaylat:
- Renkler ürünün kendisinden/dünyasından alınır (ürünün ışığı, malzemesi, kullanıldığı oda). Hex değerleriyle: zemin, metin, tek vurgu, koyu ton.
- Tipografi: karakterli tek başlık fontu + sade gövde fontu. Türkçe karakterler (ğ, ş, ı, İ, ç, ö, ü) test edilir. Ücretsiz/lisanslı fontlar: Google Fonts, Fontshare, Geist, Instrument Serif vb.
- Şekil dili: kart, buton, çip köşe yarıçapları (px), gölge değeri, çizgi kalınlığı.
- Hareket dili: bir imza an + mikro etkileşimler (aşağıya bak).
- Ses tonu: 3 örnek cümle.
- İmza unsuru: bu markayı başka siteden ayıran tek fikir (ör. ürünü kendi dünyasında sahneleme, dev marka yazısı, ürüne özel interaktif önizleme).
- Belgeleme yöntemi (Dengen'de AG1/Kindra sayfasıyla oturdu):
  - Token'lar renk adıyla değil rol adıyla tanımlanır: `--cta`, `--ann`, `--star`, `--dark`.
  - Her birinin yanına "nerede kullanılır / nerede kullanılmaz" yazılır.
  - Yön seçerken aynı sayfa ve aynı fotoğraf kullanılır, yalnız token'lar değişir. Karar renk ve vurgu farkına odaklanır.
  - Referans markanın sitesine gerçekten bakılır, ölçülebilir öğeler alınır: palet kaynağı, vurgu sayısı, düğme biçimi, başlık fontu. "Yakın marka dili" tahmini yetmez.
- Yön seçilince sabitlenir. Sonraki turlar yeni yön açmaz, seçileni inceltir. Kullanıcılar genelde büyük ve gösterişliden kompakt ve tanıdığa gider.

### 3. Yasaklar (AI kokusu listesi)
Aşağıdakiler varsayılan olarak YASAK; marka DNA'sı bilinçli bir istisna yazmadıkça kullanılmaz:
- Mor/mavi/pembe gradyanlar, gradyan yazı, parıltı (glow), cam/blur efekti
- Emoji ikonlar, rastgele ikon setleri karışımı
- Ortalanmış başlık + alt metin + iki buton hero kalıbı
- Her başlıkta bir kelimenin italik/renkli olması (en fazla bir kez, hero'da)
- Harf aralıklı büyük harf etiketlerin her bölümün üstünde tekrarı
- Aynı radius + aynı gölgeli birbirinin kopyası kart ızgaraları; sol kenarı renkli kartlar
- 01/02/03 numaralandırma (gerçek sıra yoksa), sayaç (count-up) animasyonu, her bölümde fade-in
- Krem zemin + serif + kil/terrakota rengi şablonu (her yerde aynı "lüks" kalıp)
- "Premium Kalite", "%100 Memnuniyet" rozet yığınları, uydurma istatistik
- Sahte aciliyet: uydurma geri sayım, "şu an X kişi bakıyor", uydurma satış adedi
- Stok fotoğraf hissi veren gülümseyen model görselleri, AI'ın ürettiği yazılı görseller
- Doğrulanmamış yorumlar, isimler, sağlık iddiaları, teyit edilemeyen teknik rakamlar

### 4. Yapı: kapıda ödeme mobil ürün sayfası sırası
Varsayılan PDP akışı (ürüne göre ayarla, sırayı gerekçesiz bozma):
1. Duyuru bandı: tek somut avantaj (ücretsiz kargo / kapıda ödeme / iade)
2. Kaydırmalı galeri: ilk görsel ürünü kullanımda gösterir; kenarda kesilen küçük resim şeridi, "1 / 8" sayacı
3. Yıldız + gerçek yorum sayısı → iki satırlık vaat başlığı → fiyat + karşılaştırma fiyatı
4. Fayda ikon şeridi (3-4 madde, somut)
5. Paket teklifleri (1/2/3 adet), varyant seçimi, gerekiyorsa hediye notu
6. Sayfa içi kapıda ödeme formu + yapışkan alt buton ("Kapıda ödemeyle al")
7. Butonun hemen altında: kapıda ödenecek toplam, tahmini teslim tarih aralığı, WhatsApp onayı, iade süresi
8. Sosyal kanıt: müşteri fotoğraf/videoları, konu çipleriyle filtrelenen yorumlar
9. Ürünün imza bölümü (nasıl çalışır / kendi dünyasında / karşılaştırma)
10. Kutuda ne var (varyant bazlı), boyut gösteren elde kare
11. İtiraz kırma SSS (kargo, iade, kapıda ödeme, kullanım)
12. Basın/güven logoları yalnızca gerçekse; marka hikâyesi; dev marka yazılı alt bilgi
Ana sayfa da aynı mantıkla: süsten değil satış akışından başla.

### 5. Yapım kuralları (Shopify teknik)
- Online Store 2.0: her bölüm ayrı .liquid section, {% schema %} ile tüm metin/renk/görsel ayarları tema düzenleyiciden değiştirilebilir. Temel: Horizon (veya kullanıcının teması).
- Her bölüm kendi içinde bağımsız: CSS #bolum-{{ section.id }} ile kapsanır, JS tek IIFE, sınıf önekleri bölüme özel (çakışma olmasın).
- React/Tailwind kütüphaneleri doğrudan kullanılmaz; görünüş ve hareket saf CSS + küçük vanilla JS ile yeniden yazılır (bu aynı zamanda "herkesin sitesi gibi" görünmeyi engeller).
- Tek tasarım token bloğu: renk, boşluk, font, radius değişkenleri; bölümler sabit değer değil değişken kullanır.
- Performans bütçesi (orta seviye telefon, 4G): LCP < 2,5 sn; hero görseli eager + fetchpriority high + srcset, diğerleri lazy; en fazla 2 font ailesi, font-display: swap, latin-ext; animasyon yalnızca transform/opacity; filter:blur'u sürekli animasyonda kullanma; prefers-reduced-motion desteği; üçüncü parti uygulama sayısı minimum.
- WebGL/canvas arka planlar mobilde varsayılan kapalı; yalnızca imza anında ve hafifse.
- Dokunma hedefleri ≥ 44px, gövde metni mobilde ≥ 16px, kontrast WCAG AA.
- Teslimden önce: schema JSON geçerliliği ve açılan/kapanan Liquid etiket dengesi script ile kontrol edilir; önizleme sayfası Chrome'da açılıp ekran görüntüsüyle bakılır.

### 4b. Dönüşüm ilkeleri (Ayluna ve Dengen verisinden)
- **Ödeme tasarımı iade tasarımıdır.** Ayluna verisi:
  - kapıda ödemede iade %28,6, ön ödemede %0,8
  - iadelerin %92'si "alıcı bulunamadı"
- Bu yüzden:
  - kart/online ödeme varsayılan ve indirimli görünür
  - kapıda ödeme ikinci seçenektir, ama saklanmaz
  - kapıda seçilene "Kartla öde, ₺X daha az öde" hatırlatması gösterilir
  - kapıda formda toplam, teslim aralığı ve WhatsApp/OTP onayı yer alır
- Tanıdık kalıp + gerçek veri: Türk alıcının alıştığı kalıplar atılmaz, inceltilir ve gerçeğe bağlanır.
  - Kalıplar: kayan güven bandı, paket satırı + birim fiyat + eski fiyat, fiyatlı CTA, stok uyarısı, "dün satılan", ay sonu sayacı.
  - Veri kaynağı yoksa öğe gizlenir.
- CTA her yerde seçili ödeme yöntemini ve tutarı taşır: üst buton, alt bölümler, yapışkan çubuk.
- Az yazı, tam modül: bölüm kesilmez, cümle kısalır. Fayda tek kelime, SSS cevabı tek cümle.
- Hediye ve mahremiyet güvenceleri işe yarar: "Paketin üstünde ne yazıyor?", "Anneniz için mi? Adres onun, telefon sizin".
- Mesafeli satış, KVKK, iade politikası ve satıcı unvanı alt bilgide görünür. Bunlar kapıda ödeme müşterisi için güven sinyalidir.

### 6. Tuzaklar (her projeden öğrenilenler buraya eklenir)
- Shopify bölümleri seçilen tasarım dosyasından türetilmeli. Ara bir denemeden türetilirse (Ayluna'da `iskelet.html`), seçilen tasarım koda hiç yansımaz.
- Reklam linkindeki `?variant=` okunmalı; yoksa sayfa yanlış modelle açılır. Seçenek adı eşleşmezse ilk varyanta sessizce düşülmez, hata gösterilir. Tükenmiş varyant satılamaz.
- İndirim kodu tanımlı değilse indirimli fiyat gösterilmez; ödeme sayfasında farklı fiyat çıkması güveni yıkar.
- `position: sticky` bölümün iç kutusuna değil, `#shopify-section-{{ section.id }}` sarmalayıcısına verilir.
- Tema düzenleyicide bölüm yeniden yüklenince kopya oluşur. Önlem: `[data-x]:not([data-ready])` ile yeni kopyayı al, eskisini sil, yeniyi `data-ready` ile işaretle. `shopify:section:unload` ile dinleyicileri temizle.
- Satıcı önizlemesi: gerçek veri eşiği geçmediyse örnek sayı `hidden` olarak çizilir. Yalnız `request.design_mode` ya da `?onizleme=` parametresiyle görünür; yanında "örnek sayı" notu durur.
- Stok uyarısı yalnız şu koşulda görünür: `inventory_management == 'shopify'`, `inventory_policy == 'deny'` ve stok eşik altında. Elle girilen "son 7 gün / dün" sayısı tarih taşır, eskiyince gizlenir.
- Bölüm kendini sayfada doğru yere `insertAdjacentElement` ile taşıyabilir; yedek hedef tanımlanır. Renkler tema değişkenlerine yedekli bağlanır: `var(--g, #1C6047)`.
- Flex `gap`, metindeki kelimeleri ayırır; düz metni tek `<span>` içine sar. Geniş kapsamlı buton sıfırlaması (`.x button`) özel düğüm kurallarını ezer; özgüllüğü yükselt.
- Fontu her bölümde ayrı tanımlama; bir kez yükle (Ayluna'da 15 bölümde 90 `@font-face` tekrarlandı, ~207 KB).
- Videolar `preload="none"`; yalnız ekrandayken oynar. İkinci (gece) görsel `lazy`.
- Liquid yazmadan önce `shopify-liquid` becerisinin `search_docs` betiğiyle doküman ara; teslimden önce `validate` ile doğrula.
- Kontrastı ölç, tahmin etme. Krem zeminde küçük bej/kahve etiketler 4,5:1'in altında kalıyor (Ayluna'da #8A7F6E 3,5:1 çıktı).
- **Türkiye mevzuatı** (1 Ağustos 2026'dan beri, Ticari Reklam Yönetmeliği değişikliği, Resmî Gazete 1 Temmuz 2026 / 33297):
  - Üstü çizili önceki fiyat = indirimden önceki 10 gün içinde aynı kanaldaki en düşük fiyat. Kampanya başlangıç ve bitiş tarihi yazılır.
  - Fiyat sabitse `compare_at_price` boş bırakılır.
  - Miktar ya da işlem şartlı indirimler (paket, kartla öde) de bu kurala tabi.
  - Satın alımı doğrulanamayan yorum yayımlanamaz; olumsuz yorum gizlenemez.
  - Yasal 14 günlük cayma hakkı markaya özel avantaj gibi sunulamaz.
  - Satıcı unvanı, MERSİS, adres, KEP, e-posta ve telefon ana sayfada ve İletişim'de bulunur.
- Instagram ve Facebook uygulama içi tarayıcısı: otomatik video, Apple/Google Pay ve `100vh` güvenilmez çalışıyor.
  - Sayfa videosuz da satmalı.
  - Sahnede `svh`, yapışkan çubukta `env(safe-area-inset-bottom)`.
- Horizon'da özel satın alma öğeleri en güvenli yeri: `blocks/` altında tema bloğu olarak `_product-details` içi. `product-information` çatallanmaz. App blokları için şemaya `@app` eklenir.
- Sayfa vaadi kutudan çıkanla birebir aynı olmalı; fazla vaat = iade/red. Bilinmeyen değer yer tutucu kalır ([adet], [X saat]).
- Shopify'ın dönüşüm oranı COD form siparişlerini saymaz. Gerçek ölçü: sipariş ÷ oturum + Meta Purchase olayı; başarı = teslim edilen ciro (dönüşüm, sepet, iade/red birlikte).
- Bir bölümün yüksekliği değişirse altındaki her şey kayar: görsel/animasyon zamanlamasını sayfa kilitlendikten sonra yap.
- Türkçe metinde büyük harf dönüşümü: text-transform ile "i" → "I" hatası olur; lang="tr" ver veya büyük harfi elle yaz.
- Paket (1/2/3 adet) indirimi bölümde yalnızca gösterilir; gerçek indirim Shopify otomatik indirimi veya COD uygulamasıyla tanımlanmalı.
- COD form uygulaması özel butonu dinlemiyorsa uygulamanın buton seçicisine bölümün butonu ([data-ikp-ekle] gibi) yazılır.
- Yapışkan alt buton yalnızca ana buton yukarıda kaybolduktan sonra açılır; aksi hâlde başka bölümlerin üstüne biner.
- 3D kaydırma efektinde düzlem çok yukarı kayarsa başlığın üstüne biner; kayma %20-25 ile sınırlı.
- image_tag filtresine ifade (forloop.first == false) veya data- özniteliği verme; gerekiyorsa <img> elle yazılır.
- font_picker varsayılanı yalnızca kesin var olan bir font olmalı (helvetica_n7 güvenli); yoksa şema hata verir.
- Ağır efekt eklemeden önce mobilde gerçek cihazda dene.

### 7. Kontrol noktaları (onay almadan sonrakine geçme)
1. Marka DNA dosyası + moodboard (renk, font, 3-4 referans kare)
2. Mobil hero + PDP ilk ekran görseli (statik)
3. Bölüm bölüm kod (.txt)
4. Teslim öncesi öz denetim (aşağıda)

## Kaynaklardan bölüm alma (kendi kendine öğrenme)
Bir bölüme ihtiyaç olduğunda (navbar, footer, CTA, yorum, karşılaştırma, hero, animasyon) önce aşağıdaki kaynaklara git, sonra yaz:
1. İhtiyaca uygun galeriyi Chrome'da aç (ör. footer için footer.design, buton/form için cta.gallery, landing için landdding.com / minimal.gallery, hareket için motionin.design / kinetics.colorion.co, animasyonlu bileşen için magicui.design / ui.aceternity.com / originkit.dev).
2. 3-6 örneğe bak, ekran görüntüsü al; her birinden neyin işe yaradığını ayıkla: yerleşim, tipografi ölçeği, boşluk, hareket zamanlaması (ms), etkileşim.
3. Gerekirse sayfanın kodunu/CSS'ini incele (read_page, javascript_tool ile hesaplanan stiller, animasyon süreleri). Kod kopyalanmaz; mekanizma anlaşılır.
4. Bölümü markanın DNA'sıyla sıfırdan, saf CSS/vanilla JS + Liquid schema olarak yaz. Birden fazla referansı birleştir; tek bir siteye benzememeli.
5. Bölümün başına yorum satırı olarak kaynak fikri yaz ("Kaynak fikir: ...").
6. Yasak listesi ve AI koku testinden geçir.
Lisans: React bileşen kütüphanelerinin (shadcn, Magic UI, Aceternity vb.) çoğu MIT'tir ama Shopify'da çalışmaz; yine de birebir kod taşınmaz, mekanizma yeniden yazılır. Ücretli şablon/Figma setlerinden (wonderlist, scrolltide vb.) içerik alınmaz.

## Hazır imza bölüm kiti (v1, demo marka Telve)
Önizleme: "İmza Bölümler Kiti" artifact'i. Her yeni mağazada önce bunlardan uygun olanı markaya uyarla:
1. imza-hero: kelime kelime bulanıktan yükselen başlık + italik serif kuyruk + süzülen logo karoları (kaynak: zero / PrismDraft)
2. imza-sayfa-ucusu: yatık sayfa düzlemi, kaydırınca adım kartları kalkıp döner (kaynak: zero 3D video promptu)
3. imza-urun-sahnesi: ürün kendi malzeme yığını üstünde, içerikler paralaksla süzülür, aroma çipiyle değişir (kaynak: Bardhyl kahve videosu)
4. imza-kapida-pdp: galeri + yıldız + vaat + fayda + paket + COD alt bilgi + teslim tarihi + yapışkan buton (kaynak: Lemme / Stepan)
5. imza-yorum-duvari: konu çipleriyle filtrelenen serif alıntılı yorum kartları (kaynak: HUGGD)
6. imza-dev-yazi-footer: genişliği dolduran dev marka yazısı, harfler yükselir (kaynak: HUGGD)

## Görsel üretimi
- Bağlı bir görsel üretim aracı varsa (Hugging Face Gradio uygulamaları: FLUX, Qwen-Image-Edit vb.; Canva) onu kullan. Yoksa SVG/HTML-canvas ile illüstrasyon, infografik, banner, Instagram kapak ve karosel üret; fotoğraf gerçekçiliği gereken iş için kullanıcıya aracı bağlamasını öner.
- Ürün görseli kuralı: ürünün kendisi asla sıfırdan üretilmez (şekli, etiketi, rengi değişir, iade ve şikâyet getirir). Kullanıcının gerçek ürün fotoğrafı alınır, arka planı temizlenir, ürün piksellerine dokunulmadan sahne/zemin/ışık/gölge üretilir (düzenleme/inpainting modeli). Kutuda olmayan aksesuar sahneye konmaz.
- Görsellerde yazı üretilmez; metin Shopify bölümünde HTML olarak veya SVG katmanında eklenir (Türkçe karakter hatası olmaz, düzenlenebilir).
- Her görsel seti marka DNA'sındaki palet ve ışıkla tutarlı; ilk görsel ürünü kullanımda, biri elde boyut gösteren, biri kutu içeriği.
- Çıktılar: galeri 1:1 (2048px), hero 4:5 mobil + 16:9 masaüstü, Instagram 4:5 ve 1080x1920; WebP/JPG, dekupe öğeler PNG.
- Teslim öncesi her görsele büyütüp bak: deforme el/parmak, bozuk yazı, ürün detayı değişimi varsa yeniden üret.

## İmza hareket kuralı
Sitede bir tane akılda kalan an olur ve ürünle ilgilidir (ör. "ışığı kapat" anahtarı, seçilen diskin tavana yansıması, ürünün katmanlarına ayrılması). Geri kalan hareketler sessiz mikro etkileşimlerdir: buton basma, galeri kaydırma, sepete ekleme geri bildirimi. Yumuşatma eğrileri tutarlı (tek bir ease değişkeni, ör. cubic-bezier(.2,.7,.2,1)).

## İmza fikirler kütüphanesi (referanslardan çıkarılan, kopyalanmayan)
- Ürünü kendi dünyasında sahneleme: ürün, malzemesinin/ortamının üzerinde, çevresinde bileşenleri (kahve çekirdeği yığını üstünde içecek gibi).
- Dev, ekranı kaplayan marka yazısı (özellikle alt bilgide) + sıcak, markaya özgü palet + el çizimi/illüstrasyon ikonlar.
- Koyu zemin + ince, sıkı aralıklı serif dev başlık; başlığın ikinci yarısı tek vurgu renginde (yalnızca hero'da bir kez).
- Başlık kelime kelime: her kelime 16px aşağıdan 12px bulanıklıktan 0,34 sn'de yükselir, kelimeler arası 50-60 ms.
- Gerçek ürün kullanım ekranı/videosu, altında kısa açıklama satırı.
- Abonelik/çoklu alım kutusu: avantajları onay işaretli liste, hediye kiti görseli.
- Ayluna'da tutulanlar:
  - Gece sahnesi ve üstüne −30px binen krem karar levhası. Satın alma kararı ilk ekranda başlar.
  - "Işığı kapat" anahtarı: oda gündüzden geceye geçer, ürünün asıl işi görünür.
  - Saatli kullanım ritüeli ("Bir gece, beş an": 20:00 → 07:30). Kartlar seçilen modele göre değişir.
  - Kompakt seçim satırları: model 68px, paket 64px, ödeme 62px. Bölüm etiketi küçük, sağında seçili değer.
  - Model seçimi bütün sayfaya yayılır: galeri, an kartları, kutu içeriği, yapışkan çubuk.
  - "Kardeşe" 2'li paket. Adet fiyatı ve kazanç formülle hesaplanır.

## Teslim öncesi öz denetim (AI koku testi)
Her teslimden önce sırayla kontrol et, biri bile "evet" ise düzelt:
- Bu sayfa logosu değiştirilse başka bir markanın sitesi olabilir mi?
- Yasak listesinden herhangi bir unsur var mı?
- Herhangi bir sayı, yorum veya iddia uydurma mı?
- Mobilde ilk ekranda fiyat, kapıda ödeme ve güven görünüyor mu? (görünmüyorsa sorun)
- Her bölümün satış akışında bir görevi var mı? (yoksa sil)
- Animasyonlar kapatıldığında sayfa yine çalışıyor mu?
- Ürün görseli gerçek ürünle birebir aynı mı?

## Referans kütüphanesi (ilham içindir, kopyalanmaz)
- Site/landing ilhamı: minimal.gallery, landdding.com, kage.design
- Stil ve tipografi sistemleri: styles.refero.design, fontinlogo.com (logodaki fontu bulma), logotouse.com
- Bileşen çözümleri: component.gallery, navbar.gallery, footer.design, cta.gallery (dönüşüm testli formlar/butonlar), 404s.design
- Hareket fikirleri: motionin.design, kinetics.colorion.co, epiceasing.com, jitter.video, lottielab.com, microkit.co
- Animasyonlu bileşen örnekleri (React; Shopify için yeniden yazılır): magicui.design, ui.aceternity.com, motion-primitives.com, originkit.dev, uiverse.io, rareui.com, canvasui.dev, pryzm.design
- İllüstrasyon/ikon: kitbitz.art, 3dicons.co
- DTC PDP örnekleri: ecomlanders (Ajay, @1ajaay), Stepan Komar (@stepanecom)

## Ek: tanıtım videosu tarifi
Bitmiş landing page'den reklam kreatifi olarak "kamera sayfanın üzerinde süzülür" 3D video yapılabilir: sayfa Playwright ile tam ekran yakalanır, kaldırılacak parçalar (kartlar, ürün görselleri, çipler, yorum) ayrı katman olarak çıkarılır, WebGL'de tek hız eğrisiyle süren kesintisiz kamera, alan derinliği, gölge ve hareket bulanıklığıyla render edilir; sonunda logo + iki parçalı kapanış cümlesi. Gerçek GPU'lu bilgisayarda kod çalıştırmayı gerektirir (Claude Code); sohbet içinde yalnızca önizleme yapılabilir. Render öncesi belirli saniyelerden kare alıp onaylat.

## Öğrenme döngüsü
Her projenin sonunda kullanıcının beğenmediği her şey Yasaklar veya Tuzaklar'a, beğendiği her şey İmza fikirler kütüphanesine veya Hazır bölüm kitine eklenmek üzere önerilir (skill güncellemesi olarak).