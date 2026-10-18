# Grup 4 özeti (7 gönderi)

Kareler: `ozet/kare-grup4/` (her gönderi için tam çözünürlüklü kareler + birleştirilmiş paftalar `*-m*.jpg`).

---

### DbgjytGySiQ · Surya Narayan (suryaxtech) · 9,3 sn · konuşma yok
(Whisper tek bir müzik parçası yakaladı: "We can jump up.")
- Konu: Üstte "Framerate + Claude = 🤯" başlığı var, altta MacBook ekranında eathungrytiger.com geziliyor. Bu, Hungry Tiger adlı Tikka Masala sos kavanozu markasının sitesi. Kırmızı zeminde 3B kavanoz kaydırdıkça dönüyor, ekranda dev başlıklar var. Altta "Comment 'AI'" yazısı duruyor.
- Adı geçenler:
  - **Framerate**: siyah kare logo, içinde beyaz piksel halka (0–9 sn). Videoda ne işe yaradığı söylenmiyor. Açıklama yalnız "normal bir site kurucu değil, deneyim kurar" diyor. Adresi okunamadı.
  - **Claude**: logo (0–9 sn).
  - **eathungrytiger.com**: adres çubuğu (0,3 sn), örnek site.
- Öğrenilecek teknik:
  - **Kaydırmaya bağlı ürün dönüşü.** Kavanoz sahnenin ortasında yapışkan (sticky) kalıyor. Kaydırdıkça önce eğiliyor, sonra takla atıyor. Yarım saniyelik karelerde üstten, yandan, alttan ve kapak tarafından görünüyor (0,5–4,5 sn).
  - **Başlıklar.** Kalın grotesk, büyük harf, turuncu (#f7a53a civarı). Ekranın %40–90'ını kaplıyorlar: "A NEW ANGLE OF FLAVOR", "BOLD FLAVOR / TIKKA MASALA", "A NEW PERSPECTIVE ON TASTE", "UNWRAP THE ADVENTURE". Girişte 3–4 kopya üst üste dikey kayıyor, sonra tek başlığa oturuyor (yankı/iz efekti).
  - **Bölüm geçişleri zemin rengini değiştiriyor:**
    1. Kırmızı.
    2. Koyu kahve sol panel ("WHAT'S INSIDE", ikonlu malzeme listesi) ve sağda pembe fotoğraf paneli.
    3. Turuncu "TRADITION & CREATION". Fotoğraflar alttan kayarak giriyor.
    4. "WHY THE JAR MATTERS". Pembe vurgulu kelimeler yankıyla geliyor.
    5. Üç sütunlu fotoğraf ızgarası.
    6. Tam ekran pembe kavanoz fotoğrafı, "UNLOCK THE MAGIC INSIDE THE JAR".
    7. "LET'S GET COOKING".
  - **Sabit öğeler.** Sağ altta iki yuvarlak buton (kavanoz ve sepet) hep duruyor. Üst menü hap biçimli butonlardan oluşuyor.
  - **Nasıl yapılır:** sahne `position:sticky` ile sabitlenir. Kaydırma ilerlemesi, canvas'a çizilen WebP kare dizisini ya da bir three.js modelinin dönüşünü sürer (GSAP ScrollTrigger veya `animation-timeline: scroll()`). Yankı başlık, aynı metnin 3 kopyasına gecikmeli `translateY` ve opaklık verilerek yapılır.
- Ayluna'ya uygunluk: **orta-yüksek.** LunaDream'in kaydırdıkça dönmesi (360° ürün) ve sağ altta yüzen sepet, ürün sayfası için güçlü bir fikir. Ama mobilde kare dizisi LCP'yi ve veri yükünü artırır. Hafif bir kare dizisi ya da 6–8 açılık kısa bir dizi yeterli olur.
- Durum: Framerate **yeni** (bakılmadı). Teknik **yeni**.
- Güven notu: Yorum tuzağı var ("AI yaz"). Sitenin Framerate + Claude ile yapıldığına dair videoda hiçbir kanıt yok, yalnızca hazır bir marka sitesi geziliyor. Açıklama abartılı ("everyone's about to start using").

---

### DeAPzXFqVi9 · Aksel Ege (theakselege) · 35,8 sn · konuşma var (TR)
- Konu: "Tek satır kodla 10.000$'lık web sitesi" iddiasıyla 4 adım anlatılıyor:
  1. Claude Code'u kur.
  2. Framer Motion'u kur.
  3. UI UX Pro Max skill'ini kur.
  4. 21st.dev'den satır kopyala.

  Örnek olarak Keychron K4, "SAFARI / Adventura" ve "DEADPOOL / Cine Daily" siteleri gösteriliyor.
- Adı geçenler:
  - **Claude Code**: kurulum belgesi sayfası (5–9 sn). Komutlar şöyle:
    - macOS/Linux/WSL: `curl -fsSL https://claude.ai/install.sh | bash`
    - PowerShell: `irm https://claude.ai/install.ps1 | iex`
    - Windows CMD: `install.cmd`

    Terminalde "Sonnet 4.6 · Claude Pro" görünüyor.
  - **Framer Motion**: npm sayfası (10–15 sn). Paket `framer-motion` 12.38.0, kurulum `npm i framer-motion`, depo `github.com/motiondivision/motion`. React için animasyon kütüphanesi.
  - **UI UX Pro Max** (16–21 sn): sitede "Design Intelligence — Searchable database of UI styles, color palettes, font pairings, chart types, and UX guidelines" yazıyor. Komut `uipro init --ai antigravity`. Claude Code'a "Install this skill https://github.com/nextlevelbuild…" yazılıyor, adres ekranda kesik (21 sn).
  - **21st.dev**: `21st.dev/home` (21–26 sn). Menüde UI Components, Agent Templates, Agents, 1Code, Magic Chat ve Agents SDK var. Bir bileşende "Copy prompt" düğmesine basılıyor, Claude Code'a "[Pasted text #1 +710 lines]" yapıştırılıyor (Claude Code v2.1.81).
- Öğrenilecek teknik: "Bileşen kütüphanesinden prompt kopyala, ajana yapıştır" iş akışı. 21st.dev'deki prompt, bileşen kodunu ve kurulum talimatını içeriyor. React, Tailwind ve shadcn yığınını varsayıyor. Videonun kendi kurgusu: koyu yeşil zemin, turuncu numaralı adım rozeti (1–4), yuvarlak köşeli ekran kartı ve her kelimesi ayrı beliren altyazı.
- Ayluna'ya uygunluk: **düşük.** Framer Motion ve 21st.dev bileşenleri React gerektiriyor. Ayluna teması Liquid, saf CSS ve vanilla JS ile yazılıyor. UI UX Pro Max'a daha önce bakıldı ve kurulmadı (Tailwind varsayılanı, betik çalıştırıyor). 21st.dev en fazla görsel ilham kaynağı olur.
- Durum: Claude Code **kurulu**. UI UX Pro Max **bakıldı-kurulmadı**. Framer Motion **yeni** (kurulmamalı). 21st.dev **yeni**.
- Güven notu: Yorum tuzağı var ("REHBER yaz"). "Tek satır kodla 10.000$" iddiası abartılı. 710 satırlık yapıştırılan metin okunmadan ajana verilirse risk oluşturur. Skill adresi ekranda kesik.

---

### Dc2KI0HEqqk · Thane (buildingwiththane) · 27,6 sn · konuşma yok (müzik)
- Konu: "10/10 niche websites for vibe coders" başlığıyla, dizüstü ekranında dört site arka arkaya geziliyor: Refero Styles, Cult-ui, Shader Gradient ve Manus.im. Etiketlerde #ad ve #manuspartner var, yani video Manus reklamı.
- Adı geçenler:
  - **Refero Styles**: `styles.refero.design` (2–6 sn ve tekrar). Sayfada "High-quality DESIGN.md examples for AI agents. Browse 2,000+ AI-readable design systems from leading product websites… a DESIGN.md you can use in Cursor, Claude Code, Codex, v0, or Lovable" yazıyor. Örnekler: Wise design system (`styles.refero.design/style/367c0c6e-73a7-441c-a8ff-91d139ac60dc`), ORYZO AI, Auros. Sağ panelde DESIGN.md açık. İçinde Theme paragrafı, adlandırılmış renkler (Forest, Lime Volt, Spruce, Linen Mist, Signal Blue, Alarm Red, Charcoal, Obsidian, Pebble, Slate, Fog, Paper), Typography ve Tokens bölümleri var. Sayfada "Beta" yazıyor.
  - **Cult-ui**: `cult-ui.com` (6–11 sn). Videoda "Landing page pieces like animated navbars and testimonial carousels" olarak tanıtılıyor. Görünen bileşenler: DynamicIsland ("Composable, animated Dynamic Island"), Hero Heatmap ("Split-layout hero section with responsive Heatmap shader"), AI SDK Agents, Distorted Glass.
  - **Shader Gradient**: `shadergradient.co` (12–15 sn). Videoda "Animated 3D gradient backgrounds you build in the browser, then copy the code out" diye geçiyor. Hazır ayarlar: "00 Halo", "01 Pensive", "03 Interstellar", "04 Nighty night", "06 Universe". Sitede "Available on Figma, Framer…" ve "Try on web" yazıyor. Ayarlar adres parametresinde tutuluyor (`bgColor1`, `brightness`, `cAzimuthAngle`, `cDistance`…).
  - **Manus.im**: `manus.im/app` (16–23 sn). Videoda "Build flawless backend powered apps and premium websites with AI" diye tanıtılıyor. Rivera Roofing için tasarım planı yazdırılıyor. Örnek olarak "Pure Zero / Refreshingly Clean" soda sitesi gösteriliyor (…manus.space). Panelde "SEO tracking built into the dashboard" (page views, visits, visitors) var, "Max" rozeti görünüyor.
- Öğrenilecek teknik:
  - **DESIGN.md kalıbı.** Bir markanın tasarım sistemi, yapay zekânın okuyacağı tek bir md dosyasında toplanıyor: tema anlatısı, adı ve hex değeriyle renkler, tipografi, aralık ve bileşen tokenları. Ayluna'daki `TASARIM-BILGISI.md` bunun karşılığı, Refero'daki format karşılaştırma için iyi bir örnek.
  - **Shader Gradient.** WebGL ile hareketli degrade zemin (three.js tabanlı). Ayar adres parametresinde tutulur, kod dışa aktarılır.
- Ayluna'ya uygunluk:
  - Refero: **orta.** DESIGN.md formatı ve benzer markaların stil dosyaları referans olarak işe yarar.
  - Shader Gradient: **düşük-orta.** "Nighty night" ve "Universe" gece temasına uyuyor, ama mobilde GPU ve pil maliyeti var. Ancak durağan görsel ya da kısa video olarak dışa aktarılırsa kullanılabilir.
  - Cult-ui: **düşük** (React, Tailwind, shadcn).
  - Manus: **düşük.** Ayrı bir site kurucu, Claude Code ve tuval akışımıza girmez.
- Durum: dördü de **yeni**.
- Güven notu: Video **ücretli reklam** (#ad, #manuspartner). Yorum tuzağı var ("CODE yaz"). Manus'ta "Max" planı görünüyor, ücretli abonelik. Refero'nun fiyatı videoda görünmüyor.

---

### DeB-J5doS0R · Emre Gülümser (emreative) · 42,3 sn · konuşma var (TR)
- Konu: Apple tarzı ürün tanıtım videosu için 3 araç anlatılıyor: Raylight, Shotbase ve AutoAE. Ekrandaki arayüzlerin çoğu yaratıcının kendi canlandırdığı Türkçe maketler ("Raylight · Şablonlar", "Shotbase · kayıt", "Dışa aktar"). Gerçek site görüntüleri yalnız araç başlık kartlarının arkasında, bulanık görünüyor.
- Adı geçenler:
  - **Raylight** ("ARAÇ 01", R logosu, 3–11 sn): hazır ürün videosu şablonları pazarı. Maketteki kategoriler: Lansman, Uygulama tanıtımı, Ürün çekimi, SaaS demo, Mobil uygulama, Logo animasyonu. Akış şöyle: şablon seç, ekran görüntülerini at, "sinematik" video çıksın. Adresi okunamadı.
  - **Shotbase** ("ARAÇ 02", 12–20 sn): ekran kaydı yapıyor, önemli yerlere kendisi zoom ekliyor. Dışa aktarma biçimleri Reels 9:16, YouTube 16:9, Kare 1:1 ve Story 9:16. Arka plandaki gerçek sitede "Screenshots, exactly how you need them" yazıyor. Adresi okunamadı.
  - **AutoAE** ("ARAÇ 03", 20–31 sn): Claude Code skill'i olarak kuruluyor. Maket terminalde `npx skills add https://autoae.online` → "autoae skill'i kuruldu" görünüyor. Sonra "Ürünüm için 5 sn'lik lansman animasyonu yap" yazılıyor ve "render ediliyor %41" çıkıyor. Arka plandaki gerçek sitede "SaaS Product Launch Video", "templates cut for launch day", Motion Graphics, AI Motion ve menüde Product, Solutions, Pricing, Resources, Affiliate var.
  - **After Effects**: üstü çizili, "gerek yok" (32 sn).
- Öğrenilecek teknik: Tanıtım videosu üretim hattı üç adımdan oluşuyor: şablon + ekran görüntüsü, otomatik zoomlu ekran kaydı, prompt ile hareketli grafik. Videonun kendi kurgusu da örnek alınabilir:
  - Krem zemin üzerinde koyu, yuvarlak köşeli "pencere" kartları.
  - Turuncu "ARAÇ 0X" rozeti ve italik serif araç adı.
  - Kart geçişlerinde ölçek ile bulanıklık.
  - Her cümleden bir anahtar kelime altyazı olarak çıkıyor.
  - Sonunda "3 aracın linki" yazılı bir yorum kutusu canlanıyor, "VIDEO" yazılıp gönderiliyor.
- Ayluna'ya uygunluk: **düşük.** Raylight ve Shotbase uygulama ve SaaS ekran videoları için yapılmış, LunaDream fiziksel bir ürün ve gerçek ürün çekimi gerekiyor. AutoAE Instagram kiti için hareketli grafik üretebilir, ama kaynağı okunmadan kurulmamalı.
- Durum: üçü de **yeni**.
- Güven notu: Yorum tuzağı var ("VIDEO yaz, DM'den göndereyim"). Arayüzler maket, araçların gerçek ekranı değil. AutoAE, GitHub dışı bir alan adından `npx skills add` ile kuruluyor; içeriği görülmeden kurmak risk. Menüde "Pricing" var, muhtemelen ücretli (fiyat görünmüyor). "Ajans işi gibi" abartılı.

---

### Dd3_W81zVxI · Keith AI (keithai_) · 19,5 sn · konuşma yok
(Döküm bir rap şarkısının sözleri, konuyla ilgisi yok.)
- Konu: "These websites prompts are insane 🔥" başlığı var. Önce **vividsites** adlı prompt kütüphanesi gösteriliyor. Sonra bu tür bir prompt'la yapılmış izlenimi veren "Sumi" sitesi baştan sona kaydırılıyor. Sumi, Kyoto'da bir mürekkep ve çay atölyesi. Videoda bu sitenin vividsites'tan çıktığı açıkça söylenmiyor.
- Adı geçenler:
  - **vividsites** (0–1,5 sn). Sayfada "Cinematic sites, one prompt away. Copy a prompt, paste it into your AI coder, and ship a site that doesn't look AI-made. The source video comes wired in." yazıyor.
    - Menü: Library, Build, Custom, Pricing, **MCP**.
    - Filtreler: Template, Landing Page, Hero Section, 3D Section, Background, Travel, Automotive, Horology, AI, Nature, Architecture.
    - Kartlar: Brand New Day (Free), Aevia, Murmur, Substrate (Premium).
    - "Unlock premium sites" sayfası: Ripple, Valum, Brandt, Camber, Basalt, America, Updraft, Sprite…

    Adres çubuğu görünmüyor, alan adı okunamadı. Açıklama "160+ sinematik site" diyor.
  - **Sumi** demo sitesi (2,5–19,3 sn).
- Öğrenilecek teknik (Sumi, sahne sahne):
  1. **Yükleme ekranı** (2,5 sn): siyah zemin. Ortada fırçayla çizilen bir halka (ensō) ve içinde yeşil bir nokta var. Üstte küçük serif yazı: "Grind the ink slowly. The pond is already listening." CSS'te SVG `stroke-dashoffset` ile çizilir.
  2. **Hero** (3,5–8 sn): tepeden bakılan koi göleti. Balıklar yüzüyor, nilüfer yaprakları ve bokeh ışıklar var.
     - Sol altta büyük serif başlık: "Still water, moving ink."
     - Sol üstte küçük üst etiket ("INK & TEA ATELIER · KYOTO"), iki satır metin, pembe hap biçimli "BOOK A SITTING" düğmesi ve yanında kırmızı yuvarlak düğme.
     - Üstte ortada hap biçimli menü (ATELIER, CLASSES, TEA, INK, VISIT), sağda "BOOK" ve kırmızı rozet.
     - Sağ kenarda "THE POND" etiketli dikey çizgi cetveli var; bu bir kaydırma ilerleme göstergesi.
  3. **Su altı** (8 sn): kamera suyun altına iniyor. Turkuaz su, ışık huzmeleri ve japon balıkları görünüyor.
  4. **Mürekkep geçişi** (9,5 sn): bir balıktan pembe mürekkep bulutu yayılıyor, ekranı kaplayıp bir sonraki bölüme geçiyor. Bulut sahne geçiş maskesi işi görüyor.
  5. **Beyaz kâğıt bölümü** (11 sn): "Heart, mind and spirit in four strokes" yazıyor. 心 karakteri fırça darbeleriyle çiziliyor, yanında kırmızı mühür var.
  6. **Bambu** (12,5 sn): mürekkeple bambu çiziliyor, yazılar bulanıktan netleşiyor.
  7. **Alacakaranlık gölü** (14 sn): pembe 3B nilüfer, suda yansıması var.
  8. **Gece feneri** (15,5–17 sn): suda yanan taş fener (tōrō), sıcak sarı ışık, ateş böcekleri ve halka dalgalar. Yazı: "EVENING TEA — When the lantern is lit, we stop."
  9. **Kapanış** (18,5–19,3 sn): yukarıdan inen fırça ucu suya değiyor, halka dalgalar yayılıyor. "Come and Sit with us." başlığı, "Sittings run Thursday to Sunday…" metni, "BOOK A SITTING" düğmesi ve altbilgi.

  Nasıl yapıldığı (tahmin): Tek bir tam ekran sahne `position:sticky` ile sabitleniyor. Kaydırma ilerlemesi bir video ya da kare dizisini oynatıyor (scroll-scrub); site "source video comes wired in" diyor. Yazılar `animation-timeline: view()` ile bulanıktan netleşip kayarak giriyor.
- Ayluna'ya uygunluk: **yüksek (atmosfer).** Gece, yanan fener, su, ateş böceği ve sakin bir ritüel var: LunaDream'in "ışık yanınca oda değişir" anlatısına çok yakın. "When the lantern is lit, we stop" cümlesi, ürünün akşam ritüeli olarak satılmasına iyi bir örnek. Ama tam ekran kaydırma videosu mobilde ağır olur, kapıda ödeme düğmesi de gecikmemeli. En fazla tek kısa sahne (poster + 2–3 sn) ve `prefers-reduced-motion` ile durağan yedek kullanılmalı.
- Durum: vividsites **yeni**; MCP'si var, ona bakılmadı.
- Güven notu: Yorum tuzağı var ("prompt yaz"). İçeriğin çoğu Premium/ücretli (menüde Pricing, kartlarda "Premium" etiketi var). "Prompt'la kopyalanabilir" iddiası, sitenin hangi araçla ve kaç turda yapıldığını göstermiyor.

---

### DdD49RLBYdX · Emre (emresir.ai) · 13,8 sn · konuşma var (TR)
- Konu: 10 arayüz stili, her biri yaklaşık 0,7 saniye görünecek şekilde hızlı geçiyor. Görseller "@YOGESH_CREATIVES" filigranlı, yani başka bir hesabın içeriği.
- Adı geçenler: yalnız stil adları (0–8,5 sn). Ekranda yazdığı gibi: "Skeomorphism" (doğrusu Skeuomorphism), Neomorphism, Glassmorphism, Claymorphism, Minimalism, Maximalism, Brutalism, Liquid Glass, Bento Grid, Spatial UI. Bunlar dışında araç yok.
- Öğrenilecek teknik (görsellerde görüldüğü kadarıyla):
  - **Skeuomorphism:** gerçek malzeme taklidi (deri cüzdan, plastik kartlar).
  - **Neomorphism:** açık gri zemin ve aynı renkte kabartmalı öğeler. Biri açık, biri koyu çift `box-shadow` kullanılır.
  - **Glassmorphism:** bulanık bir fotoğraf üzerinde yarı saydam paneller (`backdrop-filter: blur()`).
  - **Claymorphism:** şişkin, iç gölgeli pastel 3B öğeler.
  - **Minimalism:** bol boşluk, siyah-beyaz.
  - **Maximalism:** neon yeşil ve siyah, yoğun büyük yazı.
  - **Brutalism:** kalın siyah çerçeve, sert gölge, karışık renkler.
  - **Liquid Glass:** Apple'ın kırılmalı, büyüteç etkili cam düğmeleri.
  - **Bento Grid:** farklı boyutlarda, yuvarlak köşeli kart ızgarası.
  - **Spatial UI:** visionOS tarzı, derinliği olan yüzen paneller.
- Ayluna'ya uygunluk: **düşük-orta.** Ayluna'nın seçilmiş bir tasarımı var, bu yalnızca sözlük bilgisi. Bento Grid "özellikler" bölümünde işe yarayabilir. Gece zemininde yüzen satın alma çubuğu için cam efekti düşünülebilir, ama `backdrop-filter` mobilde pahalı.
- Durum: **yeni** (yalnız bilgi, kurulacak bir şey yok).
- Güven notu: Yorum tuzağı var ("UI yazın, katalog yolluyorum" ve "takip et"). Görseller başka bir hesaba ait. Ekranda yazım hatası var.

---

### DcLmjeZK1b2 · Brandon Lamont (brandonthewebdev) · 10,1 sn · konuşma yok
- Konu: Ekranda "One click and Claude did this 🤯" yazıyor. MacBook'ta **activetheory.net** kaydırılıyor:
  - WebGL parçacıklarla oluşan logo.
  - "CREATIVE DIGITAL EXPERIENCES" başlığı.
  - 3B eğik kart karuseli: CHILE 20, RACER (Google), PROMETHEUS, KANDINSKY (Google), PAPER PLANES (Google), E.C.H.O.
  - "What are you looking for? → Websites, Installations, XR/VR/AI, Multiplayer, Games" menüsü.
  - Kafes içinde parçacıklardan bir yapı.
  - Sonda parçacık bulutu ve logo.
- Adı geçenler:
  - **Claude**: yazıda (0–1 sn).
  - **activetheory.net**: adres çubuğunda (0–10 sn).
- Öğrenilecek teknik:
  - WebGL parçacık sistemleri, logo parçacıklardan toplanıp dağılıyor.
  - Kart yığını derinlikte dönüyor (cover-flow) ve kaydırmayla ilerliyor.
  - Kartlarda glitch ve RGB ayrışmalı yazı var.
  - Menü ve küçük yazılar eş aralıklı (monospace) fontla.
  - Nasıl yapılır: three.js ile özel shader'lı GPU parçacıkları. Kart karuseli `perspective` ve `rotateY` ile saf CSS'te de yapılabilir.
- Ayluna'ya uygunluk: **düşük.** Bu bir ajans gösteri sitesi, mobil e-ticaret ürün sayfası için çok ağır. Alınabilecek tek fikir, yıldız tozu gibi hafif bir parçacık süsü.
- Durum: **yeni** (araç değil, referans site).
- Güven notu: **İddia yanıltıcı.** Ekrandaki adres activetheory.net, yani bir WebGL stüdyosunun kendi sitesi. Claude'un bunu "tek tıkla" yaptığına dair hiçbir kanıt yok. Yorum tuzağı var ("FLOW yaz"). Biyografideki bağlantıyla ücretli site tasarım hizmeti satılıyor (reklam).

---

## Grubun araç tablosu (tekilleştirilmiş)

| Ad | Tür | Adres | Gönderiler | Uygunluk |
|---|---|---|---|---|
| Framerate | uygulama/site (işlevi belirsiz) | okunamadı | DbgjytGySiQ | belirsiz, yeni |
| eathungrytiger.com (kaydırmayla dönen ürün) | site (referans) + teknik | eathungrytiger.com | DbgjytGySiQ | orta-yüksek |
| Claude Code | uygulama | claude.ai/install.sh | DeAPzXFqVi9 | kurulu |
| Framer Motion (motion) | kütüphane (npm) | npm `framer-motion`, github.com/motiondivision/motion | DeAPzXFqVi9 | düşük (React) |
| UI UX Pro Max | skill | github.com/nextlevelbuild… (kesik), `uipro init` | DeAPzXFqVi9 | düşük, bakıldı-kurulmadı |
| 21st.dev | site (bileşen ve prompt kütüphanesi) | 21st.dev | DeAPzXFqVi9 | düşük (React/Tailwind) |
| Refero Styles | site (DESIGN.md kütüphanesi) | styles.refero.design | Dc2KI0HEqqk | orta |
| Cult-ui | site (bileşen) | cult-ui.com | Dc2KI0HEqqk | düşük |
| Shader Gradient | site/araç (WebGL degrade) | shadergradient.co | Dc2KI0HEqqk | düşük-orta |
| Manus | uygulama (yapay zekâ ile site/uygulama kurucu) | manus.im | Dc2KI0HEqqk | düşük (reklam) |
| Raylight | uygulama (video şablonu) | okunamadı | DeB-J5doS0R | düşük |
| Shotbase | uygulama (ekran kaydı + zoom) | okunamadı | DeB-J5doS0R | düşük |
| AutoAE | skill (prompt'tan hareketli grafik) | autoae.online | DeB-J5doS0R | düşük-orta, riskli kurulum |
| vividsites | site (sinematik site prompt'ları, MCP'li) | okunamadı | Dd3_W81zVxI | orta |
| Sumi demo (fener, su, mürekkep anlatısı) | teknik (kaydırmaya bağlı sahne) | — | Dd3_W81zVxI | yüksek (atmosfer) |
| DESIGN.md kalıbı | teknik | — | Dc2KI0HEqqk | orta |
| UI stilleri sözlüğü | teknik | — | DdD49RLBYdX | düşük-orta |
| activetheory.net | site (referans, WebGL) | activetheory.net | DcLmjeZK1b2 | düşük |

## Grubun en önemli 3 öğrenimi
1. **Kaydırmaya bağlı sahne anlatımı LunaDream'e en çok yakışan fikir.** Hungry Tiger'da kavanoz kaydırdıkça dönüyor. Sumi'de kaydırdıkça önce fener yanıyor, sonra su dalgalanıyor. Mobilde bunun karşılığı şu olur: tek yapışkan sahne, 6–8 karelik hafif bir dizi ya da poster ile kısa bir video, `prefers-reduced-motion` için durağan yedek, ilk ekranda hemen görünen kapıda ödeme düğmesi. "When the lantern is lit, we stop" türünden bir akşam ritüeli cümlesi metin için iyi bir örnek.
2. **DESIGN.md kalıbı (Refero Styles):** markanın tasarım sistemi tek bir yapay zekâ dosyasında toplanıyor (tema paragrafı, adlandırılmış renk tokenları, tipografi, aralık). `TASARIM-BILGISI.md` bu formatla karşılaştırılabilir. Kurulacak bir şey yok, yalnız biçim örneği.
3. **Güven:** 7 gönderinin 7'sinde de yorum tuzağı var. Biri ücretli reklam (Manus). İkisi başka bir sitenin hazır hâlini "Claude yaptı" diye gösteriyor (activetheory.net açıkça; eathungrytiger.com için kanıt yok). İki ayrı yerde uzaktan skill kurma ya da okunmadan 710 satır yapıştırma öneriliyor (AutoAE `npx skills add https://autoae.online`, 21st.dev "Copy prompt"). Bunlar kaynağı okunmadan kurulmamalı.
