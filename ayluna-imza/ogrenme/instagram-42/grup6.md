# Grup 6 · 6 + 1 gönderi

Kareler: `ozet/kare-grup6/` (Dc09 için `ozet/kare-grup6/Dc09/`, 0,5 sn arayla 30 kare).
Ayluna kurallarıyla karşılaştırma `ayluna-imza/TASARIM-BILGISI.md` §4 ve §8'e göre yapıldı: yalnız transform/opacity, tek eğri, yeni sonsuz döngü yok, ince çizgili SVG ikon, uydurma sayı yok, sayfa videosuz da satmalı, Instagram tarayıcısı.

---

### DenBDjWiUjR · Viktor (@viktoroddy) · 13,4 sn · konuşma yok (müzik)
- **Konu:** "how i make 3d sites like this in 5 minutes". Dizüstünde SynapticForge adlı hazır bir site, ardından MotionSites galerisi gösteriliyor: prompt kopyalanıp bir yapay zekâ sohbet uygulamasına yapıştırılıyor, sonra "Site is ready" deniyor. Kodun yazıldığı ya da çalıştığı an gösterilmiyor.
- **Adı geçenler:**
  - **MotionSites.ai** (3,6–4,8 sn, "Go to MotionSites.ai"). Animasyonlu site prompt kütüphanesi. Açıklamaya göre 600'den fazla prompt var. Galeri kartları: Bold Studio, Particle Field (WebGL Portfolio), Data Storytelling (SaaS), Prisma, Interactive Discovery (Hero), Quantum Human. Menüde "3D NEW", "Affiliate", "Contact".
  - **SynapticForge · Interactive** kartı (4,8–6,7 sn). Kartta "7 likes", "Copy full prompt" ve "Copy source code" var. Altında **"Sponsored"** başlığıyla "Build in AI Studio · Build apps with Gemini" ve "Build in Manus · General AI agent" reklamları.
  - **Yapıştırılan uygulama** (6,8–8,4 sn): koyu bir sohbet arayüzü ("Chat | Work" sekmeleri, "What should we work on?", "Ask for approval", "Choose project", "Plugins"). Model seçicide "5.6 Terra Extra High" yazıyor. Uygulamanın adı ekranda yok. Açıklama "Cursor ran it" diyor ama görünen arayüz Cursor değil.
  - **Ekranda okunan prompt** (8,0 sn, tam kare): *"Build ONE standalone HTML file that recreates the Orla. conceptual eco-clothing site EXACTLY. Output a single file only: all CSS in `<style>`, all JS in `<script type="module">`. No other files. Do not invent extra sections, copy, colors, fonts, or products. DELIVERABLE · Single HTML file, served over HTTP (file:// is not allowed). · Title: Orla. — Conceptual eco clothing · Before first paint: `<script>document.documentElement.classList.add('js')</script>` · Load MP4Box: cdn.jsdelivr.net/npm/mp4box@0.5.2/dist/mp4box.all.min.js (defer) · Needs internet. Videos are HEVC Main 10: they play only where the OS has a hardware HEVC decoder (Mac/iOS, some Windows)…"* **Yapıştırılan prompt Orla sitesine ait, gösterilen sonuç ise SynapticForge.**
- **Öğrenilecek teknik:**
  - **Hero:** krem zemin, ortada iki tonlu başlık ("SynapticForge" siyah, "Machines" gri, "that empathize" siyah). Arkada yanardöner, bulanık bir halka var. İnsan eli ve robot eli iki yandan uzanıyor ("Adem'in Yaratılışı" göndermesi). 0,5–9,5 sn'de eller birbirine yakın, 11,5 sn'de kenarlara çekilmiş. Hareket sağa sola kayma; tetik videodan anlaşılmıyor. Pill menü ("More", "Frontier Science", "Learning AI"), sol altta küçük etiket ve 3 satır açıklama, sağ altta çipler ("Automation", "ML").
    - CSS: iki PNG'ye `transform: translateX()`; halka için `conic-gradient` + `mask: radial-gradient` + `filter: blur`.
  - **Prompt yapısı:** "birebir yeniden kur", "tek dosya", "bölüm, metin, renk uydurma", teslim maddeleri. Ayluna brifleri için iyi bir kalıp.
  - **Uyarı dersi:** HEVC Main 10 videolar Android'de ve Instagram tarayıcısının çoğunda oynamaz. Ayluna videoları H.264 MP4 ve poster kare ile verilmeli.
  - `classList.add('js')` ilk boyamadan önce eklenir. Böylece animasyonlar JS yüklenmeden gizlenmez (aşamalı geliştirme).
- **Ayluna'ya uygunluk:** düşük. Three.js ağırlıklı masaüstü sahneler, kapıda ödemeli mobil ürün sayfasında hız ve satış kaybettirir. Yalnız prompt kalıbı ve HEVC uyarısı işe yarar.
- **Durum:** yeni (MotionSites bakılmadı).
- **Güven notu:** yorum tuzağı ("Comment PROMPT", DM'den gönderim). Sitede sponsorlu bağlantılar var. Gösterilen prompt ile sonuç farklı. Araç adı açıklamayla çelişiyor. "5 dakikada" iddiası abartılı. Ücret ekranda görünmüyor.

---

### Dei6J0AvlXw · Byron (@buildwithbyron) · 37,3 sn · konuşma var (yalnız stil adlarını okuyor)
- **Konu:** "20 animation styles you can ask Claude for (Screenshot this)". Kişi kameraya stil adlarını okuyor. Üstte numaralı liste dolarak ilerliyor, o anki madde sarı. Göğüs hizasındaki kare kartta her stilin canlı örneği oynuyor (~1,8 sn).
- **Adı geçenler** (ekrandaki tam liste, 36,9 sn): 1. Liquid morph, 2. ASCII art, 3. Holographic foil, 4. Bauhaus shapes, 5. Neon glow, 6. Dithering, 7. Clay 3D, 8. Halftone dots, 9. Kinetic typography, 10. Pixel art, 11. Particle swarm, 12. Risograph print, 13. Glitch effect, 14. Topographic lines, 15. Glassmorphism, 16. Paper cutout, 17. Vaporwave grid, 18. Flow fields, 19. Metaballs, 20. Ray-marched fractals. Araç ya da adres yok. (Ses dökümündeki "Neon Blow", "Glass Bolphism", "Metabores" Whisper hatası.)
- **Öğrenilecek teknik** (0,5 sn arayla kart kırpımlarıyla izlendi):
  - **Liquid morph (0–1,9 sn):** mor-mavi degrade damla, şekli sürekli değişiyor, üstte parlama. SVG path morph ya da gürültülü `border-radius` keyframes.
  - **ASCII art (2–3,4):** yeşil karakterlerle (`$#*!=;:~`) dönen küre ya da simit. Canvas'ta parlaklığı karaktere eşleme.
  - **Holographic foil (3,5–5,9):** "HOLO ★ RARE FOIL ★" kartı Y ekseninde eğiliyor, gökkuşağı yanardöner yüzey. `perspective` + `rotateY` + `background-position` kaydırma + `mix-blend-mode`.
  - **Bauhaus shapes (6–7,9):** krem ızgara zemin; kırmızı daire yuvarlanıyor, mavi üçgen dönüyor, sarı yarım daire ve siyah kare var, dikey "BAUHAUS" yazısı. CSS `translate` + `rotate` keyframes.
  - **Neon glow (8–9,4):** camgöbeği çerçeve içinde pembe "NEON" yazısı, kapalıdan açığa titreyerek yanıyor. Çok katmanlı `text-shadow` + opacity titremesi.
  - **Dithering (9,5–10,9):** Bayer noktalarıyla ay ya da küre, ışık evresi kayıyor. Canvas'ta sıralı titreklik (ordered dithering).
  - **Clay 3D (11–12,9):** pastel pembe zemin; pembe küre, mavi yuvarlak küp, sarı kapsül ve yeşil simit hafifçe yüzüyor, yumuşak gölgeli. CSS radial-gradient ya da Three.js.
  - **Halftone dots (13–14,9):** krem üstünde magenta-siyah noktalar, nokta boyu merkezden dışa küçülüyor, merkez geziniyor.
  - **Kinetic typography (15–16,9):** dev kelimeler (FAST, BOLD, TYPE, LOUD, MOVE) bulanık kaymayla yer değiştiriyor. Altta ve üstte "TYPE IN MOTION ·" kayan bant. "LOUD"da zemin sarıya dönüyor.
  - **Pixel art (17–18,9):** şerit gün batımı, yeşil karakter zıplıyor, kalp yükseliyor, yıldızlar parlıyor.
  - **Particle swarm (19–20,9):** mor parçacıklar girdap halkasında dönüyor. Canvas.
  - **Risograph print (21–22,9):** kırmızı güneş, kayık baskılı ışınlar, mavi dalga, "RISO" yazısı renk kaymasıyla.
  - **Glitch (23–24,9):** "GLITCH" yazısında RGB ayrışması ve tarama çizgileri, yatay dilim kaymaları.
  - **Topographic lines (25–26,9):** gürültüden eş yükselti çizgileri akıyor, kırmızı nokta işaretçi. Marching squares.
  - **Glassmorphism (27–28,9):** hareketli renkli bulanık lekeler üstünde buzlu "Glass card · Frosted, translucent" kartı, "Continue" butonu. `backdrop-filter: blur()`.
  - **Paper cutout (29–30,4):** katmanlı dağlar (turuncu, magenta, mor) gölgeli; güneş, kuşlar, sallanan kayık. Katmanlara farklı hızda `translate` (paralaks).
  - **Vaporwave grid (30,5–32,4):** "VAPOR" neon yazı, şeritli güneş, perspektifli magenta ızgara izleyiciye akıyor. `rotateX` + `background-position` animasyonu.
  - **Flow fields (32,5–34,4):** binlerce ince çizgi gürültü alanında akıyor. Canvas.
  - **Metaballs (34,5–35,9):** sarı-turuncu ışıklı toplar birleşip ayrılıyor. SVG "gooey" filtresi (blur + feColorMatrix) ya da shader.
  - **Ray-marched fractals (36–37,3):** dönen mor-turuncu 3D fraktal (Mandelbulb benzeri). WebGL shader.
  - **Asıl ders:** tekniğin adını doğru koymak Claude'dan istenen sonucu netleştirir.
- **Ayluna'ya uygunluk:** orta.
  - Gece lambasına yakın olanlar: dithering/halftone ay dokusu (durağan görsel olarak), paper cutout katmanlı gece göğü (kaydırmaya bağlı, tek seferlik paralaks), particle/yıldız (projeksiyon sahnesi).
  - Örneklerin çoğu sonsuz döngü ve canvas/WebGL kullanıyor. Ayluna'da "yeni sonsuz döngü eklenmez" ve "yalnız transform/opacity" kuralı var; bu yüzden ancak sadeleştirilerek ve `prefers-reduced-motion` ile alınabilir.
- **Durum:** yeni (teknik sözlüğü; araç değil).
- **Güven notu:** reklam ya da yorum tuzağı yok. "Claude'a sor" diyor ama örneklerin nasıl üretildiği gösterilmiyor.

---

### DeO8WC0zxol · Keith AI (@keithai_) · 15,5 sn · konuşma yok (müzik)
- **Konu:** "How I make 5k sites in minutes". Orison adlı moda sitesi gösteriliyor. Ardından "Go to vividsites", "Copy the prompt you like", "Paste into your AI coder", "Done! comment 'prompt' for the link" adımları geliyor.
- **Adı geçenler:**
  - **vividsites** (5,1–7,1 sn). Alan adı ekranda okunmadı; yalnız "vividsites" yazıyor. Menü: Create (NEW), Templates, Components, Motion (NEW), Assets, Pricing.
  - **Orison · Couture House · Landing page** kartı (7,1–9,1 sn). Butonlar: "Copy prompt" ve "Remix". Adımlar:
    1. "Copy the prompt. It's the whole build brief, with the assets linked in."
    2. "Paste it into Claude Code, Cursor or v0 in an empty folder and send it."
    3. "Open the inde[x]… Then ask for your colours in plain…" (kesik).
  - **Yapıştırılan uygulama** (9,1–11,1 sn): sol menü Chat, Imagine, Library, Automations, Projects; sağ altta **"SuperGrok"**, kutuda "Switch to Build Mode to create apps", mod "Fast", ek "pasted-text.txt". Yani Grok kullanılmış, Claude değil (açıklamada #claude #fable5 etiketleri var).
- **Öğrenilecek teknik (Orison hero):**
  - Ekranı kaplayan siyah serif "ORISON" kelime markası. Kanatlı figür (dekupe PNG) harflerin önünde, R-I-S harflerini kısmen örtüyor (yazı arkada, figür önde: katmanlı derinlik).
  - Kanatlar yavaşça açılıp kapanıyor (1,0 ile 12,5 sn arasında kanat açısı farklı), tüyler süzülüyor.
  - Sol altta "PARIS, SINCE 1931 / Worn like a vow." italik vurgulu serif başlık, "VIEW THE COLLECTION" pill butonu. Sağda büyük rakamlar (11,340 / 4,200h).
  - **Yükleme ekranı** (11,2 sn): ortada "100" sayacı ve ışınsal çizgi halkası. Ardından hero açılıyor, sol alt metin gecikmeli beliriyor (12,5 sn'de henüz yok, 13,5'ta var).
  - CSS: `z-index` katmanı (yazı < figür PNG), kanatlar için `rotate` + `transform-origin`, metinler için kademeli `opacity/translateY`.
- **Ayluna'ya uygunluk:** düşük–orta.
  - "Ürün dekupesi başlık harflerinin önünde" fikri bir lansman görseli ya da Instagram kiti için uyarlanabilir.
  - Sayaçlı yükleme ekranı kapıda ödemede satış kaybettirir; alınmaz.
  - vividsites'ın "prompt + bağlı görseller + boş klasörde Claude Code" akışı bizim tuval akışına benziyor.
- **Durum:** yeni (bakılmadı).
- **Güven notu:**
  - Yorum tuzağı: "comment 'prompt'". 151 yorum, 146 beğeni; yorum toplama amaçlı.
  - "5k sites" değer iddiası abartılı.
  - Pricing sekmesi var, fiyat ekranda görünmüyor.
  - Gösterilen araç Grok iken etiketler Claude.

---

### DduMdekhQrI · Short content editor (@jordancastle.edit) · 18,3 sn · konuşma yok (müzik; dökümdeki satır şarkı sözü)
- **Konu:** "10/10 Websites for vibe coders". HorizonX sitesinin bölümleri hızlı kesmelerle gösteriliyor: şablonlar, Shaders, Textures, Tools. Sonda "Comment 'Tools' and i'll send you the link."
- **Adı geçenler:**
  - **Horizonx.so** (2,6–4,7 sn). "The premium UI & code library for the vibecoding era". Menü: Explore, Tools, Pricing, FAQ, Docs, Affiliate, Community. Üst bantta **"20% off your first month 05:56:01 left · See plans"** geri sayımı.
  - **"+1000 Websites templates and components"** (4,7–6,2 sn). Örnekler: Apex Roadster ("MOTION, REDUCED TO ITS PUREST FORM."), Vigil: Landing Page.
  - **Shaders** (6,3–8,3 sn): Neural Noise Cursor, Flowing Waves ("Liquid waves with silver highlights, flowing distortion and adjustable center dimming"), dalgalı noktalı shader. Butonda "Export MP4".
  - **Textures** (8,3–11,8 sn): titreşimli heykel portresi ("Export PNG"), "2" rakamlarından lale (karakter dokusu), Newsprint Type (Dither Text), Winged Reverie (ASCII), True Mosaic, Jumbotron, Chromatic Echo (Trace Motion), Prism Dust, Ink Current, Retro Matrix.
  - **Membership kartı** (11,7 sn): "The whole catalogue, one subscription" · Templates, components, assets: All 27 · Downloads 3/day · Premium items 3/month · from ~~$24.99~~ **$19.99/month** · "Get Starter" · "5.0 on Gumroad, 14 ratings".
  - **Tools** (11,8–14 sn): Particle Sphere, Entrance Bloom, Entrance Orbit, Orbit Card. Alt çubuk: "Reset all", "Copy to Figma", "Copy Prompt" (kilitli), "MCP", "Export HTML" (kilitli).
- **Öğrenilecek teknik:**
  - Fotoğrafı karakter ya da noktaya çeviren "doku" efektleri (görüntüyü ızgaraya bölüp parlaklığa göre glif ya da nokta boyu seçmek).
  - Etkileşimli parçacık küresi (imleçle yarılıyor).
  - Ayarları URL'de base64 JSON olarak saklama (adres çubuğunda `eyJpbWFnZXMiOlsi…` görünüyor).
- **Ayluna'ya uygunluk:** düşük. Ücretli, karanlık ve WebGL ağırlıklı. Mobil ürün sayfasına uymuyor. "AI'a somut referans ver" mesajı doğru ama bunu zaten `TASARIM-BILGISI.md` yapıyor.
- **Durum:** yeni (bakılmadı).
- **Güven notu:** reklam (açıklama satış metni). Ücretli abonelik ($19.99/ay), aciliyet geri sayımı, kilitli özellikler. Yorum tuzağı ("Comment 'Tools'"). "No more AI slop" iddiası.

---

### DemwcsvI1kW · Tahir Yildiz (@tahiryildiz) · 61,4 sn · konuşma var (Türkçe)
- **Konu:** "Tasarımcıysan bu 8 siteyi kaydet". Bir landing page'in her bölümü (stil, menü, hero, ikon, efekt, buton, footer) için bir ilham sitesi anlatılıyor. Her sitenin ekran görüntüsünün sağ üstünde adresi yazıyor.
- **Adı geçenler** (adresler tam karede okundu):
  1. **Refero Styles · styles.refero.design** (7–18 sn). Gerçek ürünlerden 2.000'den fazla tasarım sistemi (Apple iPhone Duo, Perplexity AI, Slush, Superhuman, Ramp, OpenAI…). Seçilen stil **DESIGN.md** olarak alınıp "Claude Code'a veya Cursor'a" verilebiliyor. Kişi en çok bunu sevdiğini söylüyor.
  2. **navbar.gallery** (18–22 sn). 500'den fazla menü örneği, mega menüden yan menüye.
  3. **supahero.io** (22–28 sn). "Website hero section library". Hero örnekleri: Timeless Craft, New Era of Rank Tracking, Did Global Cinema.
  4. **3dicons.co** (28–34 sn). "Beautifully Crafted open source & premium 3D Icons". Videoda 1.400'den fazla, ücretsiz ve ticari projede kaynak göstermeden kullanılabilir deniyor. Sayfada "premium" da yazıyor; hepsinin ücretsiz olduğu doğrulanmadı.
  5. **glass.samasante.com** (34–38 sn). "Liquid glass · Real glass refraction for the web. Works [in Safari,] Firefox and Chrome. Zero depend[encies]". Kod: `pnpm add @samasante/liq…` (kesik). Oyun alanında ayarlar: Refraction (Strength 0.140, Depth 0.950, Curvature 0.500, Dispersion 0.200), Edge (Bend 0.400, Width 0.070), Sheen (Intensity 1.2, Thickness 3.5), Lens 150×150.
  6. **cta.gallery** (38–44 sn). Satın al, bülten, fiyatlandırma gibi kategorilere ayrılmış CTA örnekleri: Button, Form, Newsletter, Pricing, Modal.
  7. **footer.design** (44–48 sn). Filtreler: Typographic, Small Type, Illustrative, Grid. Örnekler: Trove, Aperios Design, Nothin', Decimals.
  8. **Bonus · scrolltide.co** (48–57 sn). "A curated library of scroll-driven templates and prompts. Copy one, paste it into your AI, and launch a site that doesn't look AI-made." Kutu: "Build a scroll-driven 3D landing page w…" + "Kopyala". Üst bant: "REGIONAL PRICING ~~$39~~ $29/month — 26% off — 00:13:06 left". "Go Unlimited", "10,000+ builders shipping faster", "121 templates in the library" (VALMORA, Whisker Ops, SELENE, Earshot; çoğu "Premium").
- **Öğrenilecek teknik:**
  - **Videonun kendi kurgusu**, Instagram kiti için iyi bir şablon:
    - üstte 7 parçalı ilerleme çubuğu ve "02 / 07 · STİL REFERO" bölüm etiketi (monospace),
    - söylenen kelime kelime beliren başlık (vurgu kelimesi açık yeşil, sıradaki kelimeler gri; bazı kelimeler italik serif),
    - sağ altta "landing.page" tel kafes kartı (stil → menü → hero → ikon → efekt → buton → footer) her sitede bir bölüm doluyor, sonda "hazır ✓ 7/7".
    - CSS: kelimelere sırayla `opacity` geçişi; kart bölümleri için `scale/opacity`.
  - **DESIGN.md:** tasarım sistemini (renk, yazı, boşluk, bileşen) yapay zekâya tek markdown dosyasıyla vermek.
- **Ayluna'ya uygunluk:** orta.
  - cta.gallery ve supahero.io ürün sayfası CTA'sı ve ilk ekran için ilham olabilir (Ayluna kuralları önce).
  - DESIGN.md fikri bizim `TASARIM-BILGISI.md`'nin karşılığı.
  - 3D ikonlar Ayluna'nın "ince çizgili SVG ikon" kuralıyla çelişir.
  - Liquid glass, kırılma filtresi yüzünden Instagram tarayıcısında ve düşük donanımlı Android'de ağır olur, "yalnız transform/opacity" kuralının da dışında.
  - Menü ve footer galerileri masaüstü ağırlıklı.
- **Durum:** yeni (sekizi de bakılmadı).
- **Güven notu:**
  - Açıklamada **#tanıtım** etiketi var: ücretli iş birliği olabilir, hangi site için olduğu belirtilmemiş.
  - scrolltide ücretli ($29/ay) ve geri sayımla aciliyet yaratıyor; "10,000+ builders" doğrulanmamış sayı.
  - Yorum tuzağı yok ("kaydet, gönder" çağrısı var).

---

### DdCa0OvqjoF · Serdar Güven (@future_with_serdar) · 49,7 sn · konuşma var (Türkçe)
- **Konu:** "Claude Code'un yaptığı arayüzler hep aynı şablon gibi mi görünüyor?" Ön yüz tasarımını iyileştiren 5 ücretsiz araç, numaralı kartlarla anlatılıyor ("ÖN YÜZ TASARIM ARAÇLARI · 5 ÜCRETSİZ ARAÇ · CLAUDE CODE"). Altyazı kelime kelime veriliyor. GitHub adresi ekranda yok; yalnız adlar var.
- **Adı geçenler:**
  1. **Taste** (6,9–13 sn). "Şablonvari 'AI görünümünü' engelleyen tasarım çerçevesi", rozetler "14 kural", "Ücretsiz · MIT". Örnek: koyu zeminli çiçekçi sitesi ("Botanic Architecture", "Curated Assemblages", "The Architecture of Nature").
  2. **Web Design Guidelines** (13–21 sn). "Kodunu 100+ arayüz kuralına göre satır satır denetliyor", rozetler "Vercel resmî", "dosya:satır rapor". Ekranda "Web Interface Guidelines" belgesi.
  3. **Awesome DESIGN.md** (21,4–29 sn). "70+ markanın tasarım sistemi tek dosyada — kopyala, kullan", rozetler "114 bin yıldız", "Stripe · Apple · Spotify". README'den: *"Copy a DESIGN.md into your project, tell your AI agent 'build me a page that looks like this'… It's just a markdown file. No Figma exports, no JSON schemas… Drop it into your project root and any AI coding agent or Google Stitch instantly understands how your UI should look."* Tablo: AGENTS.md → kodlama ajanları, "nasıl kurulur"; DESIGN.md → tasarım ajanları, "nasıl görünür".
  4. **Image to Code** (29,5–36,8 sn). "Önce tasarım görseli üretiyor, sonra sadık koda çeviriyor", rozetler "Görsel-önce akış", "Ücretsiz · MIT". Demo: "Reading design reference", tel kafes (HEADER / HERO / FOOTER) → `Page.tsx`. Kaynak deposu ekranda yok; okunamadı.
  5. **Playwright** (37,2–45 sn). "Tarayıcıyı açıp hataları sen görmeden yakalıyor", rozetler "Microsoft resmî", "Ekran görüntüsü + test". Demo: CHECKOUT sayfası ve konsol hataları ("Each child in a list should have a unique 'key' prop", LCP görselinde "priority" uyarısı, "TypeError: Cannot read properties of undefined (reading 'items')").
- **Öğrenilecek teknik:**
  - "Görsel önce, kod sonra" akışı (Image to Code). Bizim Claude Design tuvali → kod akışıyla aynı fikir.
  - DESIGN.md + AGENTS.md ayrımı: görünüş kuralları ve kurulum kuralları ayrı dosyalarda tutulur.
  - Playwright ile ekran görüntüsü alıp konsol hatası yakalamak (bizde design-review bunu yapıyor).
- **Ayluna'ya uygunluk:** yüksek (çoğu zaten kurulu).
  - Taste, Web Design Guidelines ve Playwright projede var.
  - Awesome DESIGN.md'deki başka markaların sistemleri Ayluna imzasıyla çelişir; yalnız dosya biçimi örnek alınabilir.
  - Image to Code yöntemi zaten uygulanıyor.
- **Durum:** Taste kurulu (Leonxlnx/taste-skill: design-taste-frontend + redesign). Web Design Guidelines kurulu. Playwright kurulu (Playwright MCP). Awesome DESIGN.md yeni. Image to Code yeni.
- **Güven notu:** yorum tuzağı: "kurulum adımları için yorumlara **STİL** yaz, DM'den göndereyim" (844 yorum, 642 beğeni). Ücretsiz ve MIT dediği araçlarda reklam görünmüyor.

---

### Dc09UoeOz0x · Sergey Lyubavsky (@ui.ux.jam) · 14,8 sn · konuşma yok (müzik; Whisper boş döndü)
Video indi (VP9, 1080×1920). Her 0,5 sn'de bir tam çözünürlüklü kare çıkarıldı (30 kare, `ozet/kare-grup6/Dc09/001–030.jpg`) ve hepsine bakıldı.
- **Konu:** "Amazing Websites for UI/UX Designers". Masada monitör ve dizüstü olan biri. Sonra ekrana yakın çekimle 3 site gösteriliyor, her birinde numaralı etiket ve tek cümle açıklama var.
- **Ekranda geçen site adları (tam):**
  1. **shaders.com** (kare 006–013 · ~2,5–6 sn). "The component library for creative WebGPU effects in the browser". Sayfada "Elevate your designs in seconds with our WebGPU components and presets", menüde presets, docs, pricing. Kartlarda "Explore Collection", dönen sıvı renkli "G" biçimli shader.
  2. **ls.graphics** (kare 014–021 · ~6,5–10 sn). "High-end mockups for serious design work". Etiket yazı tipinde ilk harf küçük L ile büyük I'ya benziyor; ekranda "ls.graphics" olarak okundu. Sayfa: "No need to download – Now you can use mockups online", "We're pretty good making great mockups. Give them a try!", "Edit Online", Linthe branding mockup'ları, "Environment Devices Mockups" (AL-Mockups Apple Devices $32, AH-Mockups iPhone Air $49, AF-Mockup Nothing Phone 3 $49), "Longscroll Mockups".
  3. **ContentCore.xyz** (kare 022–030 · ~10,5–14,8 sn). "3D Mockups and 3D Motion Templates". Dört daireli siyah metalik logo nesnesi dönüyor, ardından tablet 3D olarak dönüp yatıyor.
  - Giriş karelerinde (001–005) monitördeki kitap aboneliği sitesinde ("Our Sept books", "How it works", Mazywood, Blacktail) site adı yazmıyor. Okunamadı, sayılmadı.
- **Öğrenilecek teknik:**
  - ContentCore'da nesnenin kaydırmayla ya da kendiliğinden 3D dönüşü (`rotateX/rotateY` + `perspective`; gerçek 3D için Three.js).
  - shaders.com'da tuvalde canlı shader kartları.
  - ls.graphics'te tarayıcıda mockup düzenleme.
- **Ayluna'ya uygunluk:** düşük.
  - WebGPU efektleri mobil Instagram tarayıcısında risklidir.
  - Telefon/cihaz mockup'ları ancak reklam görselinde (ürün sayfasının telefonda görünümü) işe yarar.
  - 3D motion şablonları gece lambası ürün fotoğrafının yerini tutmaz.
- **Durum:** yeni (bakılmadı).
- **Güven notu:** ls.graphics ücretli ($32–49 ürünler). Diğer ikisinde fiyat ekranda yok (shaders.com'da "pricing" sekmesi var). Yorum tuzağı yok.

---

## Araç tablosu (grup 6, tekilleştirilmiş)

| Ad | Tür | Adres | Gönderiler | Uygunluk |
|---|---|---|---|---|
| Taste | skill | ekranda adres yok (kurulu: Leonxlnx/taste-skill) | DdCa0OvqjoF | **kurulu** |
| Web Design Guidelines | skill | ekranda adres yok (kurulu: vercel-labs) | DdCa0OvqjoF | **kurulu** |
| Playwright | MCP / araç | ekranda adres yok (Microsoft) | DdCa0OvqjoF | **kurulu** (Playwright MCP) |
| Awesome DESIGN.md | GitHub koleksiyonu | ekranda adres yok | DdCa0OvqjoF | orta (biçim örneği; marka sistemleri değil) |
| Image to Code | skill / yöntem | ekranda adres yok, okunamadı | DdCa0OvqjoF | orta (yöntem zaten tuvalde uygulanıyor) |
| DESIGN.md biçimi | teknik | — | DemwcsvI1kW, DdCa0OvqjoF | yüksek (`TASARIM-BILGISI.md`'den türetilebilir) |
| Refero Styles | site | styles.refero.design | DemwcsvI1kW | orta |
| navbar.gallery | site | navbar.gallery | DemwcsvI1kW | düşük–orta |
| supahero.io | site | supahero.io | DemwcsvI1kW | orta |
| cta.gallery | site | cta.gallery | DemwcsvI1kW | orta |
| footer.design | site | footer.design | DemwcsvI1kW | düşük–orta |
| 3dicons | site | 3dicons.co | DemwcsvI1kW | düşük (SVG çizgi ikon kuralıyla çelişir) |
| Liquid glass (samasante) | site + npm paketi | glass.samasante.com | DemwcsvI1kW | düşük |
| Scrolltide | site (ücretli, $29/ay) | scrolltide.co | DemwcsvI1kW | düşük |
| MotionSites | site (prompt kütüphanesi) | MotionSites.ai | DenBDjWiUjR | düşük |
| vividsites | site (prompt + şablon) | alan adı okunmadı ("vividsites") | DeO8WC0zxol | düşük |
| HorizonX | site (ücretli, $19.99/ay) | horizonx.so | DduMdekhQrI | düşük |
| shaders.com | site (WebGPU efektleri) | shaders.com | Dc09UoeOz0x | düşük |
| ls.graphics | site (ücretli mockup) | ls.graphics | Dc09UoeOz0x | düşük (reklam görseli için orta) |
| ContentCore | site (3D mockup / hareket) | ContentCore.xyz | Dc09UoeOz0x | düşük |
| Grok (SuperGrok) | uygulama | — | DeO8WC0zxol | düşük (videoda kullanılan; Claude değil) |
| Adı görünmeyen sohbet uygulaması ("5.6 Terra Extra High") | uygulama | — | DenBDjWiUjR | düşük |
| 20 animasyon stili sözlüğü | teknik | — | Dei6J0AvlXw | orta |
| Bölümlü açıklayıcı reel kurgusu (ilerleme çubuğu + kelime kelime başlık + dolan tel kafes) | teknik | — | DemwcsvI1kW | orta (Instagram kiti) |
| Yazı arkada, dekupe figür önde hero | teknik | — | DeO8WC0zxol | düşük–orta (lansman görseli) |
| H.264 video zorunluluğu (HEVC Android'de oynamaz) | teknik | — | DenBDjWiUjR | yüksek |
