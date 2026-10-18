# Grup 2 · 7 gönderi

Kareler: `ozet/kare-grup2/` (her gönderi için 6-18 tam kare, okunması gereken yerlerde kırpılmış büyütmeler).
Ayluna ölçütü (TASARIM-BILGISI §2, §8): kullanıcı tamamen koyu temayı, abartılı efekti ve uydurma sayıyı sevmez. Sayfa Instagram tarayıcısında videosuz da satmalı. "Işığı aç/kapat" anahtarı reddedildi. Başlık yazısı Young Serif ve bu yazının italiği yok.

---

### DeStzYDMNrQ · Enkis Web Studio · 8,2 sn · konuşma yok
- **Konu:** Masadaki dizüstünde kahve markası sitesi aşağı kayıyor. Kahve çekirdeği ikiye ayrılıp cam hazneye dökülüyor. Sıvı musluktan akıp bir sonraki bölüme geçiyor; orada V60 demleme var, sonunda latte fincanı. Ekrandaki gövde metni, logo ve menü harfleri bozuk ("teaffce Coffe" benzeri). Bu, videonun yapay zekâ video modeliyle üretilmiş bir maket olduğunu düşündürüyor. Çalışan bir site gibi durmuyor.
- **Adı geçenler:** Araç ya da adres yok. Okunan başlıklar: "WAKE THE BEANS", "1", "Specialty Coffee" (0,3 sn); "2" (3-4 sn); "LET IT BLOOM" (5-6 sn); "MAKE TIME TASTE BETTER" ile yüzen "ORIGIN / ROAST / FLAVOR" kartları (7-8 sn). Logo, menü ve buton yazıları okunamadı (bozuk).
- **Öğrenilecek teknik:**
  - **Bölümler arası köprü nesne:** Ürün ya da sıvı bir bölümün altından taşıp bir sonrakinin üstüne iniyor. Böylece kaydırma tek bir hikâyeye dönüşüyor.
  - **Yerleşim:** Solda dev, dar, büyük harfli serif başlık (yaklaşık 3 satır, ekranın üçte biri). Sağda küçük numara ("1", "2"), kısa açıklama ve koyu hap buton.
  - **Son ekran:** Ürünün çevresinde hafifçe dönük yüzen etiket kartları (köken, kavrum, tat).
  - **Nasıl yapılır:** Sabit tam ekran `<canvas>` üzerine kaydırma oranına göre kare dizisi çizilir. Başlıklar `position:sticky` bloklarla değişir. Kartlar `animation-timeline: view()` ile `translate/rotate` alır.
- **Ayluna'ya uygunluk:** Orta. "Köprü nesne" fikri işe yarar (disk ya da ışık huzmesi bölümden bölüme geçebilir). Sinematik kare dizisi ise "abartılı efekt" ve mobil yük riski taşır.
- **Durum:** Yeni (teknik).
- **Güven notu:** Açıklama yok. Yapay zekâ üretimi bir maket, gerçek site gibi sunuluyor. Hesap web stüdyosu, yani hizmet tanıtımı.

### DcnCJjbS4fh · Abhay (designby.abhay) · 10,9 sn · konuşma yok
- **Konu:** "Client: I don't want basic website / Me: How's this?" yazısının altında, telefonla çekilmiş bir dizüstünde lüks bitki çayı sitesi "AURÉA" kaydırılıyor. Çay paketi demliğin üstünde açılıyor, yapraklar suya düşüyor, su altına dönüyor, bardağa dökülüyor. Altı numaralı bölüm var. Siteyi Claude Code'la kurduğunu açıklamada söylüyor.
- **Adı geçenler:**
  - Marka "AURÉA — HERBAL INFUSION". Menü: Ingredients · The Brew · The Pour · Order · "ORDER NOW" (0,2 sn).
  - Hero: "Brewed in *gold*.", "DISCOVER THE RITUAL ↓", "SCROLL TO BREW ↓" (0,2 sn).
  - Bölümler: "01 — THE BLOOM / Nature, unwrapped." (2,5 sn) · "02 — THE DESCENT / Into the *glass*." (3,7) · "03 — THE AWAKENING / The water stirs." (5,0) · "04 — GOLDEN AMBER / A colour of *gold*." (6,2) · "05 — THE POUR / Poured, slowly." (7,5) · "06 — THE RITUAL / Your moment of *calm*." (8,7).
  - Kapanış: "ORDER THE COLLECTION ↗" ve "WATCH AGAIN" (10 sn).
  - Araç adı ekranda yok.
- **Öğrenilecek teknik:**
  - **Kaydırmaya bağlı video:** Arka planda tam ekran video ya da kare dizisi oynuyor. Her bölümde metin bloğu sağa ve sola dönüşümlü geliyor.
  - **Metin geçişi:** Metin bulanık ve çift görüntüyle beliriyor (blur'dan netleşme, kademeli).
  - **İlerleme çubuğu:** Üst menünün altında ince bir kaydırma ilerleme çizgisi soldan sağa doluyor (1,3 sn'de kısa, 7,5 sn'de neredeyse dolu).
  - **Tek italik vurgu:** Başlıkta tek kelime italik ve altın renkte ("gold", "glass", "calm").
  - **Tekrar izle:** Son CTA'nın yanında "Watch again" var; sekans başa sarılabiliyor.
  - **Nasıl yapılır:** Kare dizisi `canvas` üzerinde, oran `scrollY / (bölüm yüksekliği)` ile hesaplanır. İlerleme çubuğu `animation-timeline: scroll()` ve `scaleX(0→1)`, `transform-origin: left` ile yapılır.
- **Ayluna'ya uygunluk:** Orta. İlerleme çubuğu ve numaralı "ritüel" bölüm etiketleri ("01 — …") hafif ve uyarlanabilir. Tam ekran koyu sinematik sekans ise kullanıcının "tamamen koyu tema" ve "abartılı efekt" sınırına takılır, Instagram tarayıcısında da ağır kalır.
- **Durum:** Yeni (teknik).
- **Güven notu:** Yorum tuzağı ("TEA" yaz, prompt gelsin). Reklam: "DM me to get a modern website built".

### DZsygU-MpBj · Talha Ünüvar · 32,7 sn · konuşma var (TR)
- **Konu:** Claude Code'a iki şey kurduruyor. İlki GitHub'dan UI UX Pro Max skill'i: linki Claude Code'a yapıştırıp "bunu kur" diyor. İkincisi 21st.dev'den Magic MCP: kurulum komutunu kopyalayıp Claude Code'a veriyor. Sonra bununla yapılmış örnek siteleri gösteriyor.
- **Adı geçenler:**
  - **UI UX Pro Max Skill:** GitHub araması (7 sn). Sonuç `nextlevelbuilder/ui-ux-pro-max-skill`: "An AI SKILL that provide design intelligence for building professional…", Python, 70k yıldız, "Updated 21 days ago" (7,8 sn). Adres `github.com/nextlevelbuilder/ui-ux-pro-max-skill` (8,5 sn). Claude Code'a `https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git bunu ku[r]` yazılıyor (9,5-10 sn). Kurulum yeri `.claude/skills/ui-ux-pro-max/` (12 sn). Ekrandaki içerik: "67 UI styles, 161 color palettes, 57 font pairings, industry-specific rules… shadcn", Python betikleri (search engine, design system generator) (22 sn). Sesli anlatım "50'den fazla stil" diyor, ekran 67 yazıyor.
  - **21st.dev / Magic MCP:** "Magic Chat → Magic MCP" sayfası (17-19 sn). Araçlar: "Inspiration Search", "SVG Icon Search", "Magic Generate (Pro): Generate 5 polished UI variants… Subscribe for $20/m" (20 sn). Kurulum sekmeleri: Claude Code / Cursor / Windsurf / Cline. Komut: `claude mcp add magic --scope user --env API_KEY="…" …dev/magic@latest` (22 sn). Paket adının başı kesik, okunamadı.
  - **Örnek çıktılar:** "Run your business in Balance" (flamingo, ~23 sn), "The Future Of Digital Money" (~25 sn), "Our AI agent grows your Instagram network worldwide" (~27 sn).
- **Öğrenilecek teknik:** Claude Code'a skill kurmanın en kısa yolu, depo URL'sini verip "kur" demek. Kullanıcı için asıl ders tersi: bu yol depoyu okumadan kurar (bizde her depo klonlanıp okunarak kuruldu). MCP eklemenin genel kalıbı: `claude mcp add <ad> --scope user --env KEY=… <komut>`. Videoda API anahtarının ilk 30 kadar karakteri ekranda açık görünüyor. Anahtar ekrana ya da sohbete yazılmamalı.
- **Ayluna'ya uygunluk:** Düşük.
  - UI UX Pro Max zaten incelendi ve şu nedenle elendi: Tailwind/HTML yığını, betik çalıştırıyor, çıktısı ortalamaya kayıyor.
  - Magic MCP React/shadcn bileşeni üretir. Sıfırdan Liquid teması ve tuval akışına doğrudan girmez. Anahtar ister, asıl üretimi ücretli.
- **Durum:**
  - UI UX Pro Max: bakıldı, kurulmadı.
  - Magic MCP (21st.dev): yeni.
- **Güven notu:**
  - Yorum tuzağı ("Tasarım" yaz).
  - Ücretli: Magic Generate aylık 20 $.
  - Ekranda API anahtarı sızıyor.
  - Abartı: "çok daha şık ve profesyonel", "sen uğraşmadan otomatik".

### Deaa37pMhT3 · Enkis Web Studio · 8,8 sn · konuşma yok
- **Konu:** Loş odada dizüstünde koyu zeminli kahve sitesi "LUNEA". Arkada sabit, parlayan dolunay duruyor. Fincandan süt ve kahve dökülüyor, girdap oluşuyor, sıvı bir sonraki bölüme akıyor. Son bölümde ayın önünde buharı tüten fincan var. Gövde metni bozuk; bu da yapay zekâ videosu maketi.
- **Adı geçenler:**
  - Bölüm 1: "LUNEA", menü "Coffee · Ritual · Shop · Shop" (çift "Shop" bir üretim hatası), "Section 1 / A DARKER KIND OF DESIRE.", "Extraordinary coffee. An everyday indulgence.", "Discover LUNEA" (0,2 sn).
  - Bölüm 2: "Section 2 / DARK MEETS VELVET." ve arkada iri soluk "2" (1-7 sn).
  - Bölüm 3: "Section 3 / YOUR MOMENT, BEAUTIFULLY MADE. / Shop the signature blend" (8-8,7 sn).
  - Araç ya da adres yok.
- **Öğrenilecek teknik:**
  - **Sabit görsel çapa:** Ay diski bütün bölümlerde yerinde kalıyor (sticky). Ürün her bölümde onun önünde başka bir an gösteriyor.
  - **Bölüm etiketi:** Küçük "Section 2" ve arkasında çok büyük, düşük opaklıkta numara.
  - **Diğer öğeler:** Altta nokta sayfalama, sağda ok, sağ altta sabit yuvarlak sohbet butonu.
  - **Nasıl yapılır:** Ay `position:sticky; top:…` bir katmanda durur. Ürün görselleri her bölümde `view()` zaman çizelgesiyle `opacity` ve `translateY` alır. Arkadaki numara `font-size: clamp()` ve `opacity: .08` ile verilir.
- **Ayluna'ya uygunluk:** Orta-yüksek (fikir), düşük (görünüm).
  - Ay/ışık diskinin sayfa boyunca sabit kalması Ayluna'nın adına ve gece lambasına birebir oturur. Mobilde hafif yapılır: tek SVG daire, `radial-gradient` parıltı ve sticky.
  - Tam koyu "lüks kahve" tonu ise kullanıcının koyu tema sınırına aykırı. Fikir yalnız `--gece` bandında kullanılmalı.
- **Durum:** Yeni (teknik).
- **Güven notu:** Açıklama yok. Yapay zekâ maketi gerçek site gibi sunuluyor. Hizmet tanıtımı.

### Dd9nhiOyrZU · Arseni Ger (thearseniodev) · 17,4 sn · konuşma yok
- **Konu:** Üstte "Opus 5.5 absolutely cooked" yazıyor, altta "Relay" adlı bir otomasyon SaaS sitesinin hızlı kaydırması var. Koyu zemin, limon yeşili vurgu, akan neon ışık çizgileri arka planı. Açıklamaya göre ajan, MCP üzerinden bir "gerçek varlık kütüphanesine" (3D sahne, efekt, video arka plan) bağlanmış, siteyi Claude kurmuş.
- **Adı geçenler:**
  - Ekranda araç adı yok. Açıklamanın sonunda "getlayersai" geçiyor; ekranda görünmüyor, adresi yok.
  - Sitedeki bölümler:
    - "The handoffs run *themselves*." ve akış şeması kartı (0-5 sn)
    - "Most of a process is *glue*." (7 sn)
    - "01 One canvas, every branch" (7,5 sn)
    - "02 Approvals where people already are" (8,5 sn)
    - "03 Every run is on the record" ve izometrik 3B çubuk grafik (9 sn)
    - limon yeşili panel, "The best…" (10 sn)
    - "*Boring* in the ways that matter." (11 sn)
    - "A *Tuesday*, seen from Relay." (12,5 sn)
    - "You pay for runs, not *for seats*." (14,5 sn)
    - "Pick the task you *hate* most." ve e-posta formu (16,5 sn)
- **Öğrenilecek teknik:**
  - **Kaydırmada genişleyen kart:** Limon yeşili kart önce kenar boşluklu, yuvarlak köşeli bir dikdörtgen (8 sn). Kaydırdıkça kenara kadar genişliyor. İçindeki başlık kelime kelime beliriyor; üstte daktilo gibi yazılan mono etiket var (10 sn). CSS: `clip-path: inset(8% 6% round 32px) → inset(0 round 0)`, `animation-timeline: view()`. Kelimeler `span` olarak `opacity .15→1` alır.
  - **Karışık yazı:** Sans başlıkta tek kelime italik serif ("themselves", "glue", "Tuesday", "hate").
  - **Mono ayrıntılar:** Küçük mono etiketler ("● content service", "all systems normal" durum hapı) ve ince 1px kartlar.
  - **Grafik:** Son günü vurgulu izometrik çubuk grafik.
- **Ayluna'ya uygunluk:** Orta (yalnız iki teknik).
  - Genişleyen kart, ürün sayfasında "gece sahnesi" bandına geçişte işe yarar.
  - Tek kelime italik vurgu için Young Serif'in italiği yok. Ayrı bir yazı gerekir, kararı kullanıcınındır.
  - Koyu SaaS görünümü ve sayı bölümü ("82%", "58,241") Ayluna'nın koyu tema ve uydurma sayı sınırına aykırı.
- **Durum:**
  - getlayersai: yeni (yalnız açıklamada geçiyor).
  - Teknikler: yeni.
- **Güven notu:**
  - Yorum tuzağı ("Prompt" yaz) ve "link in bio".
  - Abartılı başlık ("absolutely cooked").
  - Açıklamadaki getlayersai büyük olasılıkla gizli reklam ya da ortaklık; doğrulanmadı.

### DdcLYmex8_9 · Bünyamin (bunyamin.dev) · 38,3 sn · konuşma var (TR)
- **Konu:** Önce "vibe kodlanmış" sıradan site ile istenen modern site karşılaştırılıyor. Sonra "her vibe coder'ın bilmesi gereken 4 site" sayılıyor; her biri tarayıcı penceresi kaydıyla gösteriliyor. Pencere başlıkları anlatıcının kendi eklediği etiketler, adres çubuğu görünmüyor.
- **Adı geçenler:**
  - Karşılaştırma: "Vibe Kodlanan Site — Mevcut Durum" (1 sn) ve "İstediğin Tasarım — Modern & Profesyonel" (COFFEE & CO. sitesi, 3 sn).
  - **01 Watermelon UI**, "Landing Page UI" (7,5-12 sn). Pencere: "Watermelon UI — Open Source Landing Components", "Everything you need to ship faster", "364+", "Interactions that delight". Anlatım: açık kaynak açılış sayfası kütüphanesi, üretime hazır.
  - **02 Motion Primitives**, "UI Animasyonları" (13-18 sn). Pencere: "Motion Primitives — Ready-to-use Animated UI". Anlatım: kopyala-yapıştır animasyon kodu.
  - **03 Manus**, "AI Backend & Fullstack" (19-27 sn). Pencere: "Manus — Fullstack AI Backend & Web Apps", "Sizin için ne yapabilirim?". Web sitesi modunda "E-ticaret · Shopify", "Açılış Sayfası", "Figma'dan içe aktar" ve "Web sitesi referansı ekle" seçenekleri var (25 sn). Anlatım: kodlama bilmeden backend ve web uygulaması.
  - **04 Haikei**, "SVG Arka Plan" (27-33 sn). Pencere: "Haikei — Unique SVG Backgrounds & Blobs", "Free, no signups, no credit cards.", "Discover + create unlimited visuals for your designs". Blob, dalga ve gradyan üretip SVG/PNG indiriyor.
  - Hiçbir aracın adresi ekranda yok.
- **Öğrenilecek teknik:**
  - **Haikei:** Tek renk paletinden katmanlı dalga ya da blob SVG'si üretip satır içi koymak, görsel dosyası yüklemeden bölüm ayırıcı yapmanın hafif yoludur (`<svg>` doğrudan Liquid'e yazılır, birkaç KB).
  - **Watermelon UI ve Motion Primitives:** Hazır bileşen kütüphaneleri. Videoda yığın gösterilmiyor. Genel bilgi olarak, videoda geçmiyor: Motion Primitives React + Motion tabanlıdır, yani Liquid'e doğrudan taşınmaz.
- **Ayluna'ya uygunluk:**
  - Haikei: orta. Gece bandı ile krem bant arasında yumuşak dalga geçişi gibi bölüm ayırıcılara uyar. Blob süsü "AI kalıbı" riski taşır.
  - Diğer üçü: düşük. React kütüphaneleri sıfırdan Liquid temaya girmez. Manus, Claude Code ile çakışan ayrı bir yapay zekâ ajanı ve mağaza verisini üçüncü tarafa götürür.
- **Durum:** Dördü de yeni.
- **Güven notu:**
  - Yorum tuzağı ("Aura" yaz).
  - Abartı: "hiç kodlama deneyimi gerekmiyor", "hiç tartışmasız en iyi".
  - Manus'un ücretlendirmesi videoda gösterilmiyor.

### DdETp-tNFW2 · Rina Grim (designgemstudio) · 30,3 sn · konuşma yok
- **Konu:** "ICE CREAM SLIDER IN FIGMA". Önce bitmiş prototip monitörde oynuyor (0-6 sn): "Super Cono" dondurma markası, her slaytta başka bir tat. Arka plan rengi tatla birlikte değişiyor, arkadaki dev tat adı yana kayıyor, meyveler dönerek yer değiştiriyor. Sonra Figma'da adım adım nasıl kurulduğu gösteriliyor.
- **Adı geçenler:**
  - Tatlar: "Ruby Velvet Swirl & Wild Morello", "Violet Bloom Swirl & Mission Fig", "Amber Caramel & Amalfi Lemon", "Midnight Blueberry & Wild Nectar Swirl", "Roast Espresso & Belgian Mocha"; "Luxury Velvet Dream", "Buy Now".
  - Figma adımları, ekrandaki altyazılar:
    - "Adjust the opacity" (9 sn): ad şeridi tek satır metin, "11650 Hug × 399 Hug".
    - "Select all text layers and apply Frame Selection" (11 sn)
    - "Select all ice cream elements, align them and resize them" (13 sn)
    - "Select all elements" ve sağ tık "Frame selection ⌥⌘G" (15 sn)
    - "Add Variant"
    - "Change the position of the elements" (17-19 sn)
    - "Choose Variant 2" (21 sn)
    - "Replace all elements with the next ones" (23-25 sn): Property 1 = Closed/Open
    - "Connect all frames and use these settings" (27-30 sn)
  - Etkileşim ayarı: Trigger **On click**, Action **Navigate to**, Animation **Smart animate**, Easing **Gentle**, Duration **2400ms** (29,5 sn).
  - Sağ tık menüsünde "Send to Figma Make" ve "Add motion"; alt çubukta "Remove background", "Boost resolution", "Edit with prompt" görünüyor (Figma'nın yapay zekâ özellikleri).
- **Öğrenilecek teknik:**
  - **Smart Animate mantığı:** Aynı adlı katmanlar iki çerçeve arasında konum, renk ve boyuttan ara kare üretir.
  - **Kurgu:** Arkadaki dev ad, bütün tatların yan yana yazıldığı tek uzun şerit. Her slaytta şerit bir ad kadar sola kayar. Meyveler bir bileşenin iki varyantında (Closed/Open) farklı konumda durur; geçişte uçuşur.
  - **Web karşılığı:**
    - Yatay `scroll-snap` slayt yapılır. Aktif indeks değişince `--i` değişkeni güncellenir.
    - Ad şeridi: `transform: translateX(calc(var(--i) * -1 * var(--w)))`.
    - Zemin: `background-color` geçişi.
    - Meyveler: `transform: translate/rotate` ile 500-700 ms ve `cubic-bezier(.22,1,.36,1)`.
    - Videodaki 2400 ms satış sayfası için fazla yavaş.
- **Ayluna'ya uygunluk:** Orta.
  - Model ya da renk seçimi (LunaDream Kız/Erkek, disk setleri) için "seçince zemin rengi ve ürün yumuşakça değişir" fikri uyar.
  - Dev arka plan yazısı ve uçuşan meyveler mobilde "abartılı efekt" sınırına yakın. Yalnız renk geçişi ve ürün kayması alınmalı.
  - Figma MCP yetkilendirilirse, bu tür prototip çerçeveleri tuvale okunabilir.
- **Durum:** Figma MCP kurulu, yetki bekliyor. Teknik yeni.
- **Güven notu:** Temiz. Yorum tuzağı, ücret ya da reklam yok. Ürün görselleri büyük olasılıkla yapay zekâ üretimi ama iddia edilmiyor.

---

## Araç tablosu (tekilleştirilmiş)

| Ad | Tür | Adres | Gönderiler | Uygunluk |
|---|---|---|---|---|
| UI UX Pro Max skill (`nextlevelbuilder/ui-ux-pro-max-skill`) | skill | github.com/nextlevelbuilder/ui-ux-pro-max-skill | DZsygU-MpBj | Düşük (bakıldı, kurulmadı) |
| Magic MCP (21st.dev; Magic Generate ücretli, 20 $/ay) | MCP | 21st.dev (komutta paket adı kesik) | DZsygU-MpBj | Düşük |
| Watermelon UI | site (açık kaynak açılış bileşenleri) | ekranda yok | DdcLYmex8_9 | Düşük (ilham) |
| Motion Primitives | site (animasyonlu bileşen) | ekranda yok | DdcLYmex8_9 | Düşük |
| Manus | uygulama (yapay zekâ ajanı, Shopify seçeneği var) | ekranda yok | DdcLYmex8_9 | Düşük |
| Haikei | site (SVG dalga/blob üretici, ücretsiz) | ekranda yok | DdcLYmex8_9 | Orta |
| getlayersai | belirsiz (açıklamada, MCP varlık kütüphanesi) | yok | Dd9nhiOyrZU | Düşük (doğrulanmadı) |
| Figma Smart Animate + Variants | teknik (Figma) | — | DdETp-tNFW2 | Orta |
| Kaydırmaya bağlı video ya da kare dizisi | teknik | — | DcnCJjbS4fh, DeStzYDMNrQ, Deaa37pMhT3 | Orta (ağır; videosuz yedek şart) |
| Bölümler arası köprü nesne (sıvı ya da ürün bölümden taşar) | teknik | — | DeStzYDMNrQ, Deaa37pMhT3 | Orta |
| Sabit görsel çapa (ay diski sticky) | teknik | — | Deaa37pMhT3 | Orta-yüksek |
| Kaydırma ilerleme çubuğu | teknik | — | DcnCJjbS4fh | Orta |
| Kaydırmada genişleyen kart + kelime kelime başlık | teknik | — | Dd9nhiOyrZU | Orta |
| Sans başlıkta tek italik serif kelime | teknik | — | Dd9nhiOyrZU, DcnCJjbS4fh | Orta (Young Serif'te italik yok) |
| Renk değiştiren ürün kaydırıcı (zemin + dev ad şeridi) | teknik | — | DdETp-tNFW2 | Orta |

## Grubun 3 öğrenimi
1. **Sinematik "kaydırınca film oynayan" siteler yapay zekâ videosu ile kare dizisinden yapılıyor.** İki Enkis videosu çalışan site değil; bozuk harfler bunu ele veriyor. Ayluna için alınacak olan film değil, iki hafif fikir:
   - Bölümden bölüme taşan "köprü nesne".
   - Sayfa boyunca sabit duran ay ya da ışık diski.
   İkisi de sticky, `view()` zaman çizelgesi ve tek SVG ile, videosuz kurulur.
2. **Kaydırmaya bağlı küçük hareketler ucuz ve etkili.** İlerleme çubuğu (`scroll()`), kenara açılan kart (`clip-path: inset()` + `view()`) ve renk değiştiren seçim kaydırıcı bunlara örnek. Hepsi yalnız `transform/opacity/clip-path` kullanır ve `prefers-reduced-motion` ile kapatılabilir.
3. **"Linki yapıştır, kur" akışı tehlikeli bir kestirme.** Videoda depo okunmadan kuruluyor ve API anahtarı ekranda açık kalıyor. Bu gruptaki dört gönderide yorum tuzağı, ikisinde gizli ya da açık reklam var. Yeni araçlardan yalnız Haikei (SVG ayırıcı) denemeye değer; ötekiler React ya da ücretli ve Liquid temaya girmez.
