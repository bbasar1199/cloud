# Grup 3 · 7 gönderi

Kareler: `ozet/kare-grup3/` (tam çözünürlük kareler + `m-*.jpg` birleştirmeler).

---

### DdpN5LRAFYm · Viktor (viktoroddy) · 12.8 sn · konuşma yok
- Konu: Laptop ekranında "Axle" adlı şehir ulaşımı sitesi. Ekran yazısı: "Opus 5.5 + this prompt = 4 min animated site". Ardından adımlar: MotionSites.ai galerisi, "Copy full prompt" düğmesi, Lovable'a yapıştırma, "Site is ready". Site son sahnede yüklenirken gösteriliyor.
- Adı geçenler:
  - **MotionSites.ai** (0.0 sn logo, 3.9-5.6 sn "Go to MotionSites.ai"): Hazır animasyonlu site prompt'larının galerisi. Kartlar: Agent Crew, Skybridge 404, Mostar Guide, Intelligent Operation, Augmented Sight, Cloud Kicks, Personal Showcase, TrustFlow, Relocation Card, Form & Function. Bir kartta "motionsites backgrounds: Animated backgrounds designed to convert, impress, and amaze" yazıyor. Açıklamada "600+ prompt" deniyor.
  - **Axle Journey · Dashboard** prompt sayfası (5.6-7.3 sn): "40 likes", "Copy full prompt", "HTML Code · Copy".
  - **Lovable**, lovable.dev (7.3-8.9 sn): "Build something Lovable / Create apps and websites by chatting with AI". Kutuda yalnız yer tutucu yazı var ("Ask Lovable to create a landing page for my..."). Yapıştırılan prompt görünmüyor.
  - Tarayıcı sekmeleri: "MotionSites – P…", "Veldara", "lovable.dev" (7.8 sn).
- Öğrenilecek teknik: Axle'nin düzeni bento yapısında. Solda üst üste üç kart var: koyu "4K Connected Mobility Points", açık renkte noktalı halka gösterge "Emissions −42" ve koyu "Electric Journeys 88%" ilerleme çubuğu. Sağda büyük, yuvarlak köşeli kahraman alanı: izometrik 3B şehir görseli, hap biçimli menü (Home, City Mobility, Energy Hubs, Our Progress, Better Journeys), ince başlık "Less friction. More possibility." ve hap biçimli "Discover Our Network" düğmesi. Yükleme sırasında (9.2→9.9 sn) önce şehir görseli geliyor. Ardından kart içerikleri (logo, etiketler, halka, metin) yaklaşık 0.5 sn içinde sırayla soluklaşarak beliriyor. CSS'te her öğeye `opacity:0; translateY(8px)` verilir. Sonra `animation-delay: calc(var(--i)*60ms)` ile açılır. Halka için `stroke-dashoffset` animasyonu kullanılır.
- Ayluna'ya uygunluk: düşük. Bu bir masaüstü pano görünümü. "88%", "−42" gibi süs sayılar Ayluna'nın "uydurma sayı yok" kuralına aykırı. Yalnız "yüklemede kademeli belirme" fikri alınabilir.
- Durum: yeni (MotionSites, Lovable).
- Güven notu: Yorum tuzağı var ("Comment PROMPT", prompt DM ile geliyor). Abartılı iddialar da var: "4 dakika", "model fark etmez, aynı prompt aynı sonucu verir". Videoda Claude kullanılırken hiç görünmüyor; yalnız Lovable açılış ekranı var. MotionSites'ın fiyatı videoda görünmüyor.

---

### Dc-4bsGuE6V · Rusty Émérite (ui_ux_rusty_freelancer) · 7.7 sn · konuşma yok (yalnız ses efekti: "Ha! My name is Billy!")
- Konu: Önce/sonra karşılaştırması. Gri tel çerçeve bir kahraman alanı ("Before") bulanık bir geçişle mavi, hareketli bir süt ürünü kahraman alanına ("After") dönüşüyor. Ürün şişesi, dev "PLAIN MILK" yazısının önüne yükseliyor. Süt sıçraması üstten düşüyor.
- Adı geçenler: Sunum çerçevesindeki hap düğmeler (6.8 sn): "TUTORIEL", "FIGMA", "FABLE", "TEMPLATE". Açıklama etiketleri #figma #figmadesign. "FABLE"ın ne olduğu videoda açıklanmıyor, bu yüzden okundu ama yorumlanmadı. Araç adresi yok.
- Öğrenilecek teknik (yeniden yapılabilir sıra):
  1. 1.4-1.7 sn: "Before" kartı dikey hareket bulanıklığıyla silinip maviye geçiyor (yaklaşık 0.3 sn, kamçı geçişi).
  2. 1.7-3.9 sn: Mavi radyal degrade kart, ortada beyaz damla logo. Bu bir ön yükleyici, yaklaşık 2 sn.
  3. 3.9-4.4 sn: Üst bar soluklaşarak geliyor: "MILK" logosu, "SHOP" hap düğmesi, sepet ikonu.
  4. 4.4-4.6 sn: Sol üstte "Pure Milk. Simply Better." başlığı ve küçük açıklama beliriyor.
  5. 4.6-5.0 sn: "PLAIN" ve "MILK" harfleri tek tek, küçük ölçekten tam boya büyüyerek açılıyor. Harfler arasında 40-60 ms kademe var, hafif taşmalı yaylanma (P, L, A ve M, İ, L sırasıyla). Aynı anda şişe alttan `translateY` ile yukarı kayıyor (yaklaşık 0.4 sn, yavaşlayarak). Süt sıçraması üstten aşağı düşüp şişeyi sarıyor.
  6. 5.0-5.4 sn: Yüzen etiket hapları ("Freshness Taste", "Pure Milk"), boyut seçici (0.5 / 1 / 2), adet seçici (− 2 +), "Shop Now", "Explore membership", "Taste It" ve "$59.99" fiyatı soluklaşarak geliyor.
  - Katman düzeni: dev yazı arkada, şeffaf PNG şişe ortada, sıçrama parçaları önde. Düz renk zemin ve tek ürün kullanılıyor.
  - CSS: Harfler `span{display:inline-block; transform:scale(.4) translateY(20px); opacity:0}` ile başlar. Sonra `cubic-bezier(.34,1.56,.64,1)` 450 ms ve `animation-delay: calc(var(--i)*50ms)` ile açılır. Ürün için `translateY(30%)→0` 500 ms ease-out ve `z-index` katmanları kullanılır.
- Ayluna'ya uygunluk: yüksek. "Dev yazı arkada, ürün önde, ürün yükselerek girer" düzeni LunaDream kahraman alanına doğrudan uyar: lamba alttan yükselir, arkasında büyük ad durur. 2 sn'lik ön yükleyici ise alınmamalı, çünkü kapıda ödeme yapan mobil kullanıcıyı bekletir. Toplam giriş 700 ms'yi geçmemeli. `prefers-reduced-motion` desteği eklenmeli.
- Durum: yeni (teknik).
- Güven notu: Yorum tuzağı var ("Comment GO"). Gönderide 3 beğeni, 1188 yorum var; yorum toplama gönderisi gibi görünüyor. Gösterilen tasarım muhtemelen Figma prototipi; canlı kod olduğu kanıtlanmıyor.

---

### DbBx33MRslX · Jerry Rogers (jerrythewebdev) · 10.8 sn · konuşma yok
- Konu: Ekranda "Websites after leaving ChatGPT for Claude" yazıyor. Laptopta kaydırmayla ilerleyen, Rönesans tablosu temalı bir site gösteriliyor. Bir POS donanımı 3B olarak sahneden sahneye uçuyor. Tarayıcı adres çubuğuna göre site Shopify'ın kendi resmi sitesi.
- Adı geçenler:
  - **Shopify Editions | Winter '26**, adres `shopify.com/editions/winter2026` (2.2 ve 7.2 sn, sekme başlığı ve adres çubuğu). Site içinde "The Renaissance Edition" yazıyor. Bölüm başlıkları: "Retail" (1.2 sn), "Meet your standard hub" (3.2 sn), "Connections that never drop" (5.2 sn), "The only hub with processing power" (7.2 sn), "Marketing" (10.2 sn), "Shopify Product Network" (10.7 sn).
  - Açıklama etiketleri: #opus #fable5 #mythos (videoda açıklanmıyor).
- Öğrenilecek teknik: Kaydırmaya bağlı sinematik kamera.
  - Arka plan tablo/3B mimari sahnesi. Kamera kemerlerin içinden ilerliyor (3.2→5.2 sn), sonra yukarı dönüp kubbe freskine bakıyor (6.2 sn).
  - Ürün (hub cihazı) her bölümde farklı açıyla dönüp ölçekleniyor: büyük ve eğik girer (2.2 sn), masa üstünde küçülür (4.2 sn), göğe doğru güvercinlerle uçar (6.2 sn), alt yüzü yakın planda görünür (7.2 sn).
  - Solda yapışkan, dikey içindekiler listesi var.
  - Bölüm başlıkları dev beyaz yazı ("Retail") ile italik serif alt yazıdan oluşuyor.
  - Bölüm geçişleri beyaz perde/silme ile yapılıyor (9.2 sn).
  - Tetik kaydırma; ilerleme kaydırmayla birebir oranlı.
  - Yapımı: `position:sticky` kap (yaklaşık 400vh). İçindeki `<canvas>`'a, kaydırma ilerlemesine göre kare dizisi ya da WebGL kamera konumu yazılır (GSAP ScrollTrigger `scrub` ya da CSS `animation-timeline: scroll()`).
- Ayluna'ya uygunluk: orta. Ağır 3B mobil ürün sayfası için uygun değil. Ama "ürün yapışkan kalsın, kaydırdıkça bölüm metni ve arka plan değişsin" fikri hafif biçimde kurulabilir: tek ürün görseli ve 3-4 adımlık sahne (gece odası → tavana yıldız yansıması). Bu bir Shopify sitesi; tema yazarken ilham kaynağı olarak açılabilir.
- Durum: yeni (ilham sitesi).
- Güven notu: Yanıltıcı. Üst yazı sitenin Claude ile yapıldığını ima ediyor, ama gösterilen site Shopify'ın resmi Editions sayfası. Açıklama metni ("AI hızlandırır, zevk sonucu belirler") ise doğru bir ders.

---

### DbbcJXZuExe · Textura Agency (textura.eu) · 10.9 sn · konuşma yok
- Konu: "How I make Website like this in 5 minutes" yazısı ve "Prompts Library + Claude". Karanlık, 3B "Lumea" sitesi gösteriliyor ("Crafted to spark wonder"). Adımlar: Getlayers'tan prompt kopyalama, "AI Builder"a yapıştırma, sonuç.
- Adı geçenler:
  - **getlayers** (3.9-7.5 sn). Menü: Library, Pricing, Docs, MCP, Affiliate, Contact us. Başlık: "Every prompt, in one place", "New templates arrive every week". Sayılar: tümü (177), Templates (34), 3D Scenes (55), Sections (10), Backgrounds (78). Ruh hali süzgeçleri: Dark 127, Light 50, Luxe, Technical, Organic, Playful, Brutalist, Calm. Sağ üstte kullanıcı planı "Full Stack · Yearly". Tam alan adı ekranda okunamadı; açıklama etiketi #getlayersai.
  - **Lumea** şablon sayfası (6-7.5 sn): "Premium", "Commercial licence", "A stone monk meditates on a floating rock in a slow spiral of tumbling debris…", "Copy prompt → Copying… → Copied!", "Download source code". Etiketler: hero, threejs, nextjs.
  - **Claude masaüstü uygulaması, Code sekmesi** (7.5-9 sn). Oturum: "Local deployment port conflict", proje "getlayers-stackside-main". Claude yaptıklarını Rusça anlatıyor: `yarn install` çalıştırdı, Next.js 16.2.0 dev sunucusunu 3201 portunda açtı, "kodda, bağımlılıklarda, mimaride hiçbir değişiklik yapılmadı".
- Öğrenilecek teknik: Lumea kahraman alanı.
  - Siyah zemin. Ortada kaya üstünde oturan figür, etrafında yavaşça dönen enkaz parçacıkları.
  - Üstte ve altta iki ince, parlayan elips halka (bloom ışıması), yukarıdan inen dikey ışık huzmesi.
  - Solda serif başlık "Crafted to spark wonder". Altta ortalı küçük büyük harfli satır.
  - Sürekli, yavaş döngü (birkaç saniyelik tur).
  - Three.js ile yapılır: torus + bloom, parçacıklar için `InstancedMesh`. Hafif sürümü CSS'te mümkün: dönen `border-radius:50%` elips + `filter: blur()` ile parlama, `linear-gradient` huzme, birkaç `@keyframes` ile süzülen nokta.
- Ayluna'ya uygunluk: orta (yalnız estetik). "Parlayan halka + ışık huzmesi + süzülen toz" dili gece lambası/projektör ürününe çok yakışıyor; CSS ile hafif bir yorumu tuvalde denenebilir. Three.js/Next.js yığını ise Shopify Liquid teması için uygun değil.
- Durum: yeni (Getlayers).
- Güven notu: Ücretli/abonelik ("Premium", "Commercial licence", "Full Stack · Yearly"). Yorum tuzağı var ("Comment Prompt"). Açıklamada ajans reklamı var ("DM me Project"). Yanıltıcı: "5 dakikada prompt'tan site" deniyor, ama ekranda Claude yalnız indirilmiş hazır kaynak kodu kurup çalıştırıyor ve kendisi "kod değişmedi" diyor.

---

### DeW5NQ1DZhh · Divjot Sahni (sahni.ai) · 7.6 sn · konuşma yok
- Konu: "6 Claude Skills for Better Web Design" başlıklı hızlı bir liste. Her skill kartı yaklaşık 0.9 sn ekranda kalıyor; kartta ad, tek cümle açıklama ve kurulum komutu var.
- Adı geçenler (ekrandaki komutlarla):
  1. **UX Designer** (1.1-2.0 sn): "Plans flows, error states, touch targets, and WCAG contrast." `npx skills add szilu/ux-designer-skill`
  2. **Canvas Design** (2.0-2.9 sn): "Describe the artwork. Get a finished PNG." `npx skills add anthropics/skills --skill canvas-design`
  3. **App Store Screenshots** (2.9-3.8 sn): "Every required size, with mockups, captions, and light/dark variants." `npx skills add ParthJadhav/app-store-screenshots`
  4. **Taste** (3.8-4.7 sn): "Gives Claude a palette, typeface, hierarchy, and actual taste." `npx skills add Leonxlnx/taste-skill -s design-taste-frontend`
  5. **Transitions.dev** (4.7-5.6 sn): "Production-ready motion for modals, dropdowns, and page reveals." `npx skills add Jakubantalik/transitions.dev -s transitions-dev`. Örnek kutular: Card resize, Number pop-in, Notification badge, Page side-by-side, Text states swap, Menu dropdown, Modal open/close, Avatar group hover.
  6. **Web Artifacts Builder** (5.6-6.5 sn): "Builds working React and Tailwind UI right in the chat." `npx skills add anthropics/skills --skill web-artifacts-builder`
- Öğrenilecek teknik: Hepsi `npx skills add <sahip/repo> [-s|--skill <ad>]` biçiminde, tek komutla kuruluyor. Transitions.dev, modal, açılır menü ve sepet çekmecesi gibi tekrar eden etkileşimlere hazır hareket tarifi veriyor.
- Ayluna'ya uygunluk:
  - Transitions.dev: orta. Sepet çekmecesi, akordeon ve yapışkan "Sepete ekle" için işe yarar, ama mevcut Emil Kowalski skill'leriyle (review-animations, animation-performance) ve make-interfaces-feel-better ile çakışır. Kurmadan önce lisansı ve içeriği okunmalı.
  - UX Designer: orta. Dokunma hedefi ve WCAG konuları web-design-guidelines ve design:accessibility-review ile çakışıyor.
  - Taste: kurulu.
  - Canvas Design: düşük-orta. Instagram görselleri için kullanılabilir.
  - Web Artifacts Builder: düşük. React/Tailwind kuruyor; Ayluna Liquid ve tuval kullanıyor.
  - App Store Screenshots: düşük.
- Durum:
  - Taste: kurulu (design-taste-frontend).
  - Canvas Design ve Web Artifacts Builder: claude.ai hesabında anthropic-skills altında zaten var.
  - UX Designer, App Store Screenshots, Transitions.dev: yeni.
- Güven notu: Yorum tuzağı var ("Comment DESIGN"). Açıklamada "half my design stack'i değiştirdi" ve "Claude'a gerçek zevk verir" gibi abartılı iddialar var. Ücret belirtilmiyor ("no subscriptions").

---

### DXruEuojJLI · Yasin Arsal · 49.2 sn · konuşma var (Türkçe)
- Konu: "Claude kodlamada harika, ön yüzde zorlanıyor" diye açılıyor. Önerilen çözüm: tasarımı Google Stitch'te ücretsiz üretmek, Stitch'i MCP ile Claude Code'a bağlamak, sonra uzun bir hareket/kalite prompt'uyla tasarımı koda çevirtmek. Ekranda Stitch'in tüm export ve MCP kurulum adımları ile Claude Code'un yazdığı dosyalar görünüyor.
- Adı geçenler:
  - **Stitch** (8-23 sn; Google Stitch, konuşmada 3.8 sn). "Welcome to Stitch.." ekranında App/Web seçimi, model "3.1 Pro" ve **"Start with a DESIGN.md"** seçeneği var (15-17 sn). Örnek prompt (17 sn): "Design a Cinematic landing page for Space-Travel private business named "COSMOS" with an animated hero section, fully scrollable with 8 different sections, micro animations, a shared liquid-glass design system, and Framer Motion entrance animations." Çıktı: "AEON – Complete 8-Section Journey", hero "Venture Past Our Sky Across the Universe" (21.5 sn).
  - **Dribbble** logosu (19.5 sn) ilham görseli kaynağı olarak gösteriliyor. Açıklamada Pinterest de geçiyor.
  - **Stitch Export menüsü** (23.5 sn): AI Studio (PREVIEW), Figma, Jules, .zip, Code to Clipboard, MCP, Project Brief.
  - **Setup MCP** (25.5-28 sn): Client listesinde Cursor, Antigravity, VS Code, … Claude Code. Altında API Key ve şu komut var: `claude mcp add stitch --transport http --url "https://stitch.googleapis.com/mcp" --header "X-Goog-Api-Key: …"`.
  - **Claude Code** (VS Code paneli). Oturum adı "Import and audit Stitch design via MCP" (40.5 sn). Yazılan dosyalar: `index.css` (193 satır), `tokens.ts`, `CountUp.tsx`, `FadingVideo.tsx`, `LineReveal1.tsx`. Yapılacaklar listesi: Vite + React + TS iskeleti, Tailwind + Framer Motion, token sistemi, ortak bileşenler (FadingVideo, AnimatedSection, WordReveal), Nav, 8 bölüm + Footer, animasyon düzeltmeleri, 375/768/1280 duyarlı geçiş + erişilebilirlik, 3000 portunda dev sunucu.
- Öğrenilecek teknik: Yapıştırılan prompt'taki hareket tarifi (38.5-39.5 sn). Değerler somut ve olduğu gibi alınabilir:
  - Kademeli liste/ızgara: Ebeveyn görünüme girince tetiklenir. Her çocuk sırayla 0.09 sn gecikmeyle "bulanıktan kayarak yukarı" girer. "Asla hepsini aynı anda oynatma."
  - Kelime kelime başlık: Her kelime `inline-block`, aralarında `margin-right:.28em`. Kelime şu sırayla açılır: blur 10px, opacity 0, y 40 → (yarıda) blur 4px, opacity .5, y −4 → blur 0, opacity 1, y 0. Süre 0.7 sn, kelime başına 100 ms kademe. Ebeveyn `flex-wrap`, `row-gap:.1em`.
  - Kart üzerine gelme: `y −7`, `scale 1.018`, yay (spring).
  - Bağlantı üzerine gelme: Ölçek yok. Yönlü bağlantıda `x:3`. Menü bağlantısında `::after` alt çizgi `scaleX 0→1`, `transform-origin:left`, 0.25 sn.
  - Koşullu öğeler (modal, çekmece, açılır menü, sekme, akordeon). Giriş: opacity 0, scale .9, blur 8px, y 10 → 1 / 1 / 0 / 0, 0.3 sn. Çıkış: opacity 0, scale .95, blur 4px, y −6, 0.2 sn.
  - Sayaç: Görünüme girince 0'dan değere, 1.4 sn, ease-out.
  - Paralaks: Arka plan 0.4×, ön yazı 0.85× hızda. Hero çıkarken ölçek 1→1.08. `position:fixed` hilesi yok.
  - Azaltılmış hareket (her projede zorunlu): Bulanık-kayma yerine yalnız opacity 0→1. Ölçek kaldırılır, süre aynı kalır.
  - Duyarlı geçiş: 375 / 768 / 1280 px, dokunma hedefi en az 44×44.
  - Erişilebilirlik geçişi: aria-label, button type, alt metin, klavye sırası, modalda odak tuzağı.
  - Sunucu: 3000 doluysa 3001, sonra 3002.
- Ayluna'ya uygunluk:
  - Hareket tarifi: yüksek. Framer Motion yerine CSS/WAAPI ile birebir çevrilebilir; Ayluna'nın sepet çekmecesi, SSS akordeonu, yorum kartları ve başlık girişi için hazır sayılar sunuyor. Sayaç kısmı yalnız gerçek sayıyla kullanılmalı.
  - Stitch: orta. Seçilmiş tasarım (`canvas/Main.dc.html`) zaten olduğu için ana akışa girmez; yeni bölüm fikri üretmek için ikinci kaynak olabilir. "Start with a DESIGN.md" fikri, Ayluna'nın `TASARIM-BILGISI.md` yaklaşımıyla aynı.
- Durum: Stitch ve Stitch MCP yeni. Claude Code kurulu.
- Güven notu:
  - Yorum tuzağı var ("Yorumlara Kodlama yazın").
  - Videoda Stitch API anahtarı açıkça görünüyor (27.5-41 sn). Not almadım; kullanılmamalı.
  - Ekran kaydındaki dosya yolu `C:\Users\shubh\space\aeon\…`. Kayıt başka birinin videosundan alınmış olabilir (çıkarım).
  - Stitch "tamamen ücretsiz" deniyor; videoda fiyat sayfası yok.
  - "Sihirli şekilde yayına hazır kod" ifadesi abartılı.

---

### DYsQ_8uKvfx · Defne İncekara (defneincekara.ai) · 37.8 sn · konuşma var (Türkçe)
- Konu: "Web tasarımcısı tutmayı unutun, Claude Code az önce 10.000 dolarlık bir site oluşturdu" diye açılıyor. Dört adımlı kurulum anlatılıyor: Claude Code, Framer Motion, UI/UX Pro Max, 21st.dev. Video "İşte kritik kısım" (34.6 sn) dedikten sonra takip kartıyla bitiyor; kritik kısım yalnız açıklamada yazıyor.
- Adı geçenler:
  - Örnek siteler (0-7 sn): "to the unknown" (gezegen + iki gezgin), koyu küreli bir site ("02"), "MIRA" mücevher sitesi ("We design every piece with love and intention"). 31 sn'de "loria" moda sitesi.
  - **Claude Code** (8.6-13.6 sn). "Download Claude: Chat, Claude Cowork, and Claude Code, all in one place" sayfası. Kurulum satırları: macOS/Linux/WSL `curl -fsSL https://claude.ai/install.sh | bash`, Windows PowerShell `irm https://claude.ai/install.ps1 | iex`. Terminalde "Claude Code v2.1.81 · Sonnet 4.6 · Claude Pro" (28.5 sn).
  - **framer-motion** npm sayfası (13.6-20 sn): sürüm 12.38.0, "Motion for React – An open source animation library for React", `npm i framer-motion`, depo `github.com/motiondivision/motion`. Terminalde `npm install motion`.
  - **UI UX Pro Max · Design Intelligence** (20-23 sn): "Searchable database of UI styles, color palettes, font pairings, chart types, and UX guidelines…". Komut `uipro init --ai antigravity`. Desteklenenler: Cursor, Windsurf, Antigravity, GitHub Copilot, Kiro. Claude Code'a "Install this skill" yazılıyor (22.5 sn).
  - **21st**, `21st.dev/home` (24-28 sn): UI Components, Agent Templates, Agents SDK, Magic Chat menüleri; bir bileşende "Copy prompt". Claude Code'a "[Pasted text #1 +710 lines]" yapıştırılıyor. Açıklamada "21st.dev Magic, hazır React bileşeni çeken MCP server, API key gerektirir" deniyor.
- Öğrenilecek teknik: Yeni teknik yok, bir kurulum sırası anlatılıyor. Açıklamadaki asıl ders doğru: AI markayı tanımıyor, metin yazmıyor, erişilebilirlik test etmiyor; hızı artırıyor ama tasarımcının yerini almıyor.
- Ayluna'ya uygunluk: düşük. Framer Motion ve 21st.dev React içindir, Ayluna teması Liquid + düz JS/CSS olacak. UI/UX Pro Max daha önce incelenip gerekçeyle reddedildi.
- Durum: Claude Code kurulu. UI/UX Pro Max bakıldı, kurulmadı. Framer Motion ve 21st.dev Magic yeni (önerilmez).
- Güven notu:
  - Yanıltıcı: açılıştaki "to the unknown" sitesinde "Made with Slider Revolution" ve "A WordPress parallax slider… Slider Revolution brings the WOW back" yazıyor (0.5 sn). Yani bu bir WordPress eklenti demosu, Claude çıktısı değil.
  - Abartılı: "10.000 dolarlık site", "tek satır kod yeterli".
  - Yorum tuzağı var ("Rehber" yazın, PDF).
  - Claude Code aylık 20 dolardan başlıyor; 21st.dev Magic API anahtarı gerektiriyor, ücretsiz katmanı sınırlı (açıklamaya göre).
  - UI UX Pro Max ekranında Claude değil "antigravity" kurulum komutu gösteriliyor.

---

## Grup 3 · tekilleştirilmiş araç tablosu

| Ad | Tür | Adres | Gönderiler | Uygunluk |
|---|---|---|---|---|
| Transitions.dev | skill | `Jakubantalik/transitions.dev` (`-s transitions-dev`) | DeW5NQ1DZhh | orta (yeni; Emil skill'leriyle çakışır) |
| UX Designer | skill | `szilu/ux-designer-skill` | DeW5NQ1DZhh | orta (yeni; web-design-guidelines ile çakışır) |
| Taste (design-taste-frontend) | skill | `Leonxlnx/taste-skill` | DeW5NQ1DZhh | kurulu |
| Canvas Design | skill | `anthropics/skills --skill canvas-design` | DeW5NQ1DZhh | düşük-orta (claude.ai'de var) |
| Web Artifacts Builder | skill | `anthropics/skills --skill web-artifacts-builder` | DeW5NQ1DZhh | düşük (claude.ai'de var) |
| App Store Screenshots | skill | `ParthJadhav/app-store-screenshots` | DeW5NQ1DZhh | düşük |
| UI UX Pro Max | skill | `uipro init` | DYsQ_8uKvfx | bakıldı-kurulmadı |
| Google Stitch + Stitch MCP | site + MCP | MCP: `https://stitch.googleapis.com/mcp` (site adresi ekranda yok) | DXruEuojJLI | orta (yeni) |
| 21st.dev / Magic | site + MCP | `21st.dev` | DYsQ_8uKvfx | düşük (React, API key) |
| Framer Motion / Motion for React | kütüphane | npm `framer-motion` / `motion`, `github.com/motiondivision/motion` | DYsQ_8uKvfx, DXruEuojJLI | düşük (React; tarifleri CSS'e çevrilir) |
| Claude Code / Claude masaüstü | uygulama | `claude.ai/install.sh` | DbbcJXZuExe, DXruEuojJLI, DYsQ_8uKvfx | kurulu |
| MotionSites | site (prompt kütüphanesi) | `MotionSites.ai` | DdpN5LRAFYm | düşük |
| Getlayers | site (ücretli prompt/kaynak kod, MCP'si var) | alan adı okunamadı (#getlayersai) | DbbcJXZuExe | düşük |
| Lovable | site (AI site kurucu) | `lovable.dev` | DdpN5LRAFYm | düşük |
| Shopify Editions Winter '26 | site (ilham) | `shopify.com/editions/winter2026` | DbBx33MRslX | orta |
| Slider Revolution | WordPress eklentisi (yanlış atıfla gösterilen demo) | — | DYsQ_8uKvfx | düşük |
| Dribbble / Pinterest | site (ilham) | — | DXruEuojJLI | düşük |
| Kademeli bulanık-kayma + kelime kelime başlık + çekmece giriş/çıkış değerleri | teknik | DXruEuojJLI prompt'u (38.5-39.5 sn) | DXruEuojJLI | yüksek |
| Dev yazı arkada, ürün önde, ürün alttan yükselir, harf harf ölçek girişi | teknik | — | Dc-4bsGuE6V | yüksek |
| Yapışkan ürün + kaydırmaya bağlı sahne değişimi | teknik | — | DbBx33MRslX | orta (hafif sürüm) |
| Parlayan elips halka + ışık huzmesi + süzülen parçacık | teknik | — | DbbcJXZuExe | orta (CSS sürümü) |
| Yüklemede kart içeriklerinin kademeli belirmesi | teknik | — | DdpN5LRAFYm | düşük-orta |
