# Grup 5 · 7 gönderi

Tam çözünürlüklü kareler: `ozet/kare-grup5/<kod>-<sn>.jpg`. İnceleme kolajları: `ozet/kare-grup5/goz/`.

---

### DeecRIEDB8q · Burak Üstün (burak.build) · 33 sn · konuşma var (TR)
- **Konu:** "Claude'u yaratıcı stüdyoya çeviren 5 ücretsiz skill." Her skill için kısa hareketli grafik var. Ortada Claude logosu duruyor, ışıyan yeşil çizgiler onu beş karta bağlıyor.
- **Adı geçenler** (ekranda hiçbirinin adresi yok):
  - **Remotion** (3,4–10 sn): Videoya animasyon ve hareketli grafik ekliyor, baştan sona tanıtım videosu kuruyor. Ekrandaki örnek prompt (9,5 sn): "Make a promotion video in Apple presentation style for VVTerm." Altında kurgu zaman çizelgesi görünüyor ("kurguyu o yapıyor").
  - **Competitor Ads Extractor** (11–17 sn, Meta logosuyla): Rakiplerin yayındaki reklamlarını çekiyor. Ekranda Meta Reklam Kütüphanesi kartları var: "Active", "Library ID", "Started running on 17 Sep 2026", ClickUp, Notion, Asana, monday.com. Reklamın açılış cümlesi vurgulanıyor.
  - **Deep Research** (18–22 sn): Arka planda pazar araştırması yapıyor. Kartta "Market research · Mapping the market… 128 sources" yazıyor.
  - **Voice DNA** (22,5–28 sn): Ses dökümünde "Voisty Enay" diye geçiyor, ekranda "Voice DNA" yazıyor. Senin yazılarını okuyup cümle kuruşunu öğreniyor, Claude'un çıktısını senin üslubunla yazdırıyor.
  - **ElevenLabs** (28,6–33 sn): Metni seslendiriyor, sesini kopyalıyor, iki kişilik podcast hazırlıyor.
- **Öğrenilecek teknik:** Videonun kurgu dili tekrar kullanılabilir.
  - Düğüm haritası (0–2 sn): Merkez ikondan kartlara uzanan çizgiler sırayla çiziliyor. Kartlar ölçek 0.9→1 ve opaklıkla geliyor.
  - Her başlıkta ikonun çevresine yeşil halka çiziliyor (SVG `stroke-dashoffset` 1→0, yaklaşık 0,6 sn).
  - Altyazı kelime kelime çıkıyor. Anahtar kelime neon yeşil oluyor, sahne bulanıktan nete geçiyor.
  - Bunlar Remotion'da React bileşeni olarak ya da CSS'te `@keyframes` + SVG stroke ile yapılır.
  - Competitor Ads mantığı elle de uygulanabilir: Meta Reklam Kütüphanesi'nde rakip gece lambası/projektör reklamlarının açılış cümleleri ve vaatleri toplanır.
- **Ayluna'ya uygunluk:** orta. Remotion, LunaDream tanıtım reel'i için yüksek, ürün sayfası için düşük. Rakip reklam taraması ürün metni ve teklif kararı için faydalı.
- **Durum:** yeni (beşi de kurulu değil).
- **Güven notu:** "Ücretsiz" deniyor ama ElevenLabs ve Deep Research için o servislerde hesap gerekiyor (açıklama da söylüyor). Ekranda depo adresi ya da sahibi yok, kaynağı doğrulanmadan kurulmamalı. Remotion'ın şirket kullanımı için lisans koşulu var, kurmadan önce okunmalı. Yorum tuzağı yok.

### Deglhh-lDwu · Dolunay Özeren · 45 sn · konuşma var (TR)
- **Konu:** "Claude'la yaptığın site sıradan çıkıyor çünkü kurulum eksik" diyor. Çözüm iki adım: (1) Claude'a görsel tasarım skill'i eklemek, (2) Claude'u gerçek tarayıcı araçlarına bağlamak, böylece tahmin yürütmeden sayfayı görerek düzeltiyor. Üç kaynaklık liste gösteriliyor.
- **Adı geçenler:**
  - **frontend design skill**, `github.com / anthropics` (3 sn). 20–24 sn'de SKILL.md görünüyor: "name: frontend-design", "Guidance for distinctive, intentional visual design…", "Ground your designs in the subject matter".
  - **tasarım rehberi: "Improving frontend design through Skills"**, `claude.com` (3 sn). 39 sn'deki DM metninde "Anthropic Tasarım Blog" olarak geçiyor.
  - **chrome devtools mcp**, `github.com / ChromeDevTools` (5 sn), kart başlığı "Chrome DevTools for agents". 35–37 sn'deki animasyonda Claude, site önizlemesini Elements/Styles/Console sekmeleriyle inceliyor ("yapı ve görünüm birlikte inceleniyor").
  - DM metni (39 sn) aynı üç bağlantıyı ve "Claude Code ile site kurma örnekleri"ni listeliyor.
- **Öğrenilecek teknik:** İş akışı bizim kurduğumuzla aynı: zevk için beceri, göz için tarayıcı aracı. Chrome DevTools MCP'nin Playwright'tan farkı performans izi, ağ ve konsol erişimi (aracın bilinen özellikleri; videoda gösterilmiyor). Kurgu tekniği: kaynak kartları −5° eğik düşüp 0°'a dönerek alt alta diziliyor (yaklaşık 0,4 sn yay eğrisi).
- **Ayluna'ya uygunluk:** yüksek, ama yeni bir şey getirmiyor, mevcut kurulumu doğruluyor. Chrome DevTools MCP yalnız tema aşamasında performans ölçümü için aday.
- **Durum:** frontend-design **kurulu**. Tarayıcı gözü **kurulu**, aynı işi Playwright MCP görüyor. Chrome DevTools MCP **yeni**. Blog yazısı okunabilir.
- **Güven notu:** Yorum tuzağı var: "Yoruma SİTE yaz" (448 beğeniye 1.937 yorum, etkileşim kasma). Kaynakların kendisi resmi ve ücretsiz.

### DemSHfZOGSO · Alphenex (alphenex.ai) · 40 sn · konuşma var (EN)
- **Konu:** "3 secret tools" ile çok animasyonlu "immersive landing page" yapılabileceğini anlatıyor. Demo olarak "Sweet Tape" adlı bant markasının sitesi kaydırılıyor, sonra üç site gösteriliyor. Monitör telefonla çekilmiş, çoğu yazı bulanık.
- **Adı geçenler:**
  - **Motionsites** (8,9–12 sn, sözlü ve altyazıda "REPLICA OF MOTIONSITES"): Ücretli araç olarak anılıyor. 1 numaralı araç bunun "bedava kopyası" diye sunuluyor. Adres yok.
  - **MotionPrompt AI Design Library** (9–17 sn): "Official Collection of 132 AI Website & App Prompts", "3D & Animated AI Website Prompts". Açıklaması "…Website Prompts for Lovable, Bolt, Cursor, and Claude Code… Just copy, paste, and launch." Kartlarda "Copy Prompt" ve "Copy Full Prompt Text" düğmeleri var. Adres okunamadı.
  - **HeroPrompts** (logo bulanık, büyük olasılıkla bu; 20–26 sn): Başlık "Hero sections that look expensive, from a prompt." Alt metin: "Copy one prompt into Claude, Cursor, or v0 and get back a complete, animated, production-ready hero in React. Every preview below is a real build of the prompt. No mockups." Düğme "Start free: 3 premium prompts", kartlarda "PREMIUM" rozetleri var. 26 sn: "Specified to the pixel: Exact hex palettes, Google Fonts weights, cubic-bezier curves, animation timings in milliseconds. The AI has nothing to improvise…" Adres okunamadı.
  - **scrollhaus** (27–35 sn): Animasyonlu site şablonları ve UI bileşenleri sunuyor (Toast Stack, OTP Input, Gradient Border Button, Sliding Tabs, Number Ticker, Day/Night Toggle, Floating Navbar). Menüde "Backgrounds · Effects · Journal · MCP" var.
    - 34 sn, MCP komutu: `claude mcp add scrollhaus --scope user --transport http https://<okunamadı>.supabase.co/functions/v1/mcp`. Codex için ayrı ayar da gösteriliyor.
    - 32 sn, fiyat şeridi: "$13.27/MO EQUIVALENT · first year with SCROLL20 · $159.20 billed annually".
- **Öğrenilecek teknik** (Sweet Tape demo sayfası, 0–8 sn ve 35–38 sn):
  - Açılışta gökkuşağı şeritli yükleme ekranı neon yeşil hero'ya dönüyor.
  - Hero: dev, sıkışık, kalın yeşil başlık "STICK BY YOU". Altta ortada ürünün kendisi duruyor (bant rulosu), sağ üstte "PULL ME" bant ucu var.
  - Kaydırınca rulo dönerek açılıyor, çıkan bant şeridi bölümleri birbirine bağlıyor.
  - 2. bölüm: kraft kâğıt + limon desenli kâğıt kolajı, sağda turuncu sıkışık metin listesi ("DIY FAIL, MOVING DAY CHAOS…") ve yeşil ok.
  - 3. bölüm: turuncu zemin üstünde eğri bir yeşil şerit, şeridin üstünde yazı akıyor ("…S MESSY, SOMETHING…"). "MASKING TAPE" rulosu ve dağınık çıkartma rozetleri var. Kapanış: "LET'S MAKE IT STICK!"
  - CSS/JS karşılığı: Rulo için `animation-timeline: scroll()` ile `rotate`. Eğri akan yazı için SVG `<textPath>` + `startOffset` animasyonu. Şerit için `scaleX`/`clip-path` kaydırmaya bağlanır.
  - Ayrı ders (HeroPrompts'un "Specified to the pixel" cümlesi): Prompt'a hex, font ağırlığı, cubic-bezier ve ms süre yazılırsa model doğaçlamıyor.
- **Ayluna'ya uygunluk:** orta-düşük.
  - Uygun olan fikir: ürünün kendisi animasyonun kahramanı olabilir (bant rulosu yerine projektörün ışık konisi).
  - "Specified to the pixel" ilkesi tuval brifleri için yüksek uygunlukta.
  - Araçlar ise hazır prompt kütüphanesi. Ortalama "AI sitesi" üretiyorlar, Ayluna kurallarıyla çelişir.
- **Durum:** yeni (dördü de).
- **Güven notu:**
  - Emoji yorum tuzağı var: "Follow first, or the auto-DM won't reach you". 3 beğeniye 60 yorum.
  - "Secret tools" ve "free and unlimited" abartı. Gerçekte #2 freemium, #3 ücretli abonelik (yıllık $159,20).
  - scrollhaus MCP bilinmeyen bir Supabase sunucusuna bağlanıyor ve `--scope user` ile tüm projelere ekleniyor. Kurulmamalı.

### DeeZPyaoN3O · Julia (design4me__) · 9,7 sn · konuşma yok (müzik)
- **Konu:** iMac ekranında "ücretsiz" portfolyo şablonları vitrini. Açılış yazısı: "imagine spending weeks on your portfolio and then finding these". Her sahnede küçük serif başlık ve alt başlık var, sahneler 0,8–1,8 sn'de bir değişiyor. Sahne sınırları ölçüldü: 1,58 · 2,5 · 3,35 · 4,25 · 6,05 · 6,82 · 7,57 · 8,07 · 9,02 sn.
- **Adı geçenler** (ekran başlığı + tarayıcı sekmesi):
  - "unknown reality archive" (0–1,6 sn). Adres çubuğunda yalnız kısmi adres okunuyor: "…hive.com/?content=BodyCell".
  - "storm lab · interactive showcase" (1,6–2,5 sn), sekmede "Storm Lab — Never Stop Exp…".
  - "filmstrip · minimal gallery template" (2,5–3,35 sn).
  - "foldfolio · foldable phone portfolio" (3,35–4,25 sn), sekmede "Foldfolio".
  - "mondragon · digital agency template" (4,25–6,8 sn), sekmede "Mondragon 1 – Framer Templ…".
  - "nika stern · creative portfolio template" (6,8–7,5 sn), sekmede "Nika Stern | Fashion & Beauty".
  - "mondragon 4 · creative agency template" (7,5–9,7 sn), sekmede "Mondragon 4 – Framer Temp…".
  - Ayrıca "Cubo Agency — Brands built…" sekmesi açık. Adres çubuğunda "…framer.app" okunuyor (1,9 sn). Yani bunlar **Framer şablonları**.
- **Öğrenilecek teknik:**
  1. **Parçacık portre** (unknown reality archive): Web kamerası görüntüsü yuvarlak noktalara bölünüp el hareketiyle dağılıyor. Canvas'ta görüntü ızgarayla örneklenir, her hücreye parlaklığına göre daire çizilir, imleç/el yakınındaki daireler itilir.
  2. **Storm Lab:** Kırmızı zemin, kapüşonlu figürün kesik fotoğrafı, "never stop testing" yazısı figürle katmanlı (bir kısmı figürün arkasında kalıyor). Sağda "01%" sayaçlı halka var. Yapılışı: arka plan + yazı + kesilmiş figür PNG'si üç `z-index` katmanı olarak dizilir.
  3. **Foldfolio:** Katlanabilir telefon maketinin iki paneli içinde portfolyo var, paneller `rotateY` ile açılıyor.
  4. **Mondragon:** Ekran genişliğinde dev "MONDRAGON" yazısı ve üstünde görsel kartlardan 3B sarmal kurdele (kartlar kurdele boyunca dönerek akıyor). Hizmet listesinde (WEB DESIGN, BRAND STRATEGY…) üzerine gelinen satır siyaha dönüyor, yanında küçük görsel beliriyor (hover reveal). Siyah sahnede iki holografik kart imleçle 3B dönüyor.
  5. **Nika Stern:** Tam ekran kırmızı, solda dev "NIKA", sağda soluk "STERN", küçük görsel kartı.
  6. **Mondragon 4:** Beyaz zemin, kalın grotesk "Lars Dekker". Sağda havada dağılmış eğik görsel düzlemleri var (perspektif + imleç paralaksı). "Cases" başlığının içine küçük renkli kareler gömülü ("Product Design ◼ Branding ◼ Web Dev"), satır yatay kayıyor.
- **Ayluna'ya uygunluk:** düşük-orta. Framer şablonları Shopify'a taşınmaz ve hepsi masaüstü odaklı. İki fikir alınabilir: "başlığın içine gömülü küçük ürün görseli" ve "figürün arkasından geçen yazı". İkincisi LunaDream ışığının başlığın arkasından taşması olarak uygulanabilir.
- **Durum:** yeni (site/şablon).
- **Güven notu:** "TEMPLATE" yorum tuzağı var (15,7 bin beğeni, 5,5 bin yorum). "Free" iddiası ekranda doğrulanmıyor.

### Dem0dU5uq2v · AGI Point (agi_point) · 13,8 sn · konuşma yok
- **Konu:** Aynı prompt'la iki model aynı ekranda yarışıyor: üstte **Claude Opus 5.5 ($2.10)**, altta **Gemini 4 Argon ($4.00)**. Konu dürtülebilen, oyulabilen, atılabilen bir 3B "jöle balkabağı". Açıklamaya göre bu tek bir testçinin denemesi. Gemini'nin API'si 30 Kasım'a kadar token başına yarı fiyat olduğu halde bu testte Opus daha ucuz çıkmış.
- **Adı geçenler:** Claude Opus 5.5, Gemini 4 Argon (0–13,8 sn boyunca etiket olarak). Araç ya da adres yok.
- **Opus çıktısı** (0,5 sn karesi tam çözünürlükte okundu):
  - Başlık italik serif "jelly / Pumpkin.", alt metin "Carved by hand, lit from inside, wobbles when poked. Pull the stem. Tap to jiggle. Drop it, if you dare."
  - Sağdaki panel: FLAVOR "Spiced orange" ve 5 renk yuvarlağı, CANDLE %80 ve WOBBLE %64 kaydırıcıları, Face "Classic grin", turuncu "Carve a new face" ve siyah "Pour candy" düğmeleri.
  - Altta "Pull the stem · Tap to jiggle · Drag to carve", sağ altta "SEASONAL 4.20 €".
- **Gemini çıktısı:** Düz, low-poly turuncu kabak. Metin "Click the pumpkin to make it wobble!", seçenekler Orange/Purple/Green, Glow kaydırıcısı, "Carve Face" ve "Add Candy" düğmeleri; ham HTML kontrolleri.
- **Öğrenilecek teknik:**
  - Yarı saydam jöle malzemesi içten ışıyor.
  - Dürtünce squash-stretch ile sönümlü yay sallanması (yaklaşık 0,6–1 sn).
  - Sap çekilince uzuyor ve yaylanarak geri dönüyor (6,5 sn).
  - Yüz ifadesi değişiyor (sırıtma → şaşkın), fizikle düşen jelibon yağmuru, zıplayıp düşme.
  - Yapılışı: Three.js `MeshPhysicalMaterial` (transmission/thickness) + yay simülasyonlu vertex kaydırma. Bu iş CSS'le olmaz.
  - Asıl ders: Opus sayfayı **ürün sayfası gibi** kurmuş (seçenek yuvarlakları + kaydırıcı + birincil/ikincil düğme + fiyat + kullanım ipucu satırı) ve her seçim anında görsele yansıyor.
- **Ayluna'ya uygunluk:** orta. WebGL 3B, mobil Shopify'da ve kapıda ödeme kitlesinin düşük cihazlarında ağır kalır. "Seçenek → anında önizleme" deseni ise LunaDream'in renk/mod seçimi için yüksek uygunlukta.
- **Durum:** teknik / bilgi (kurulacak bir şey yok).
- **Güven notu:** Tek denemelik karşılaştırma, maliyet rakamları doğrulanamaz. Reklam ve yorum tuzağı yok.

### DehcS3aAXVi · Catherine Kravchun (cathweb.design) · 8,7 sn · konuşma yok
- **Konu:** "Opus 5.5 and 10 minutes" yazısı altında "brewns coffee house" adlı kurgusal kahve markasının sitesi baştan sona kaydırılıyor. Önce laptop çekimi, sonra ekrana yakınlaşma, sonda radyal zoom-blur geçişiyle döngü. Kare kare bakıldı (yaklaşık 0,7 sn aralıkla 14 kare).
- **Adı geçenler:** Yalnız "Opus 5.5" (yazı) ve "brewns" (kurgusal marka). Prompt kütüphanesinin adı ekranda yok, açıklamada yalnız "Comment LIBRARY" var.
- **Öğrenilecek teknik** (bölüm bölüm):
  1. **Hero** (0–2,4 sn): Kahve-siyah degrade zemin, mono etiket "// SPECIALTY COFFEE HOUSE", kalın grotesk "COFFEE FOR YOUR".
     - El yazısı "moment" kelimesi harf harf **yazılıyor** (yaklaşık 2 sn; SVG `stroke-dashoffset` ya da soldan sağa `clip-path`).
     - Sağda bardak ve "slow roast" paketi var. Paketin üstüne gelince fiyat etiketi açılıyor: "// IN THE BAG · SLOW ROAST $18.00 · 250 G · WHOLE BEAN · COPENHAGEN".
     - Hero'nun altında bilgi şeridi: "OPEN DAILY 07:00–21:00 · adres · INSTAGRAM/TIKTOK".
  2. **Menü** (3,1–4,5 sn): "// OUR MENU · FAVORITES MADE DAILY" başlığı satır satır maskenin altından kayarak geliyor. Dört ürün kartı ince çizgili ızgarada duruyor. **Fiyat rakamları karışık karakterlerden yerine oturuyor** (text scramble, "$?.40" → "$3.10", yaklaşık 0,5 sn).
  3. **Konumlar** (4,5–5,9 sn): Ortada dev bir saat kadranı, merkezinde buzlu latte var; kaydırdıkça kadran yukarı akıyor. Solda 3 adres, sağda "OPEN DAILY" saatleri (yapışkan sütunlar).
  4. **Felsefe** (5,9–6,6 sn): Siyah zemin. Havada farklı hızlarda süzülen kahve çekirdekleri var (paralaks). "THE CITY NEVER STOPS. YOUR COFFEE SHOULDN'T SLOW YOU DOWN." satırları alttan maskeyle geliyor, dev bardak alttan kayarak giriyor.
  5. **Sipariş** (7,3–8,0 sn): Üstten çekilmiş masa fotoğrafı (matcha kek), "COFFEE FOR RIGHT NOW" yazısı.
     - Ortadaki **yazıcı yarığından bir fiş aşağı doğru basılıyor.**
     - Fişte ürün görseli, "SKIP THE LINE. ORDER AHEAD.", barkod ve "ORDER NOW" düğmesi var. Yanında "ORDER RIGHT NOW ↗".
  6. **Altbilgi:** Siyah zemin, arkada dev ve silik el yazısı logo.
  - CSS karşılığı:
    - Fiş: `animation-timeline: view()` ile `translateY(-100%) → 0`, yarık kapsayıcıda `overflow: clip`.
    - Fiyat scramble: küçük bir JS ile her harfi 8–12 kare rastgele karakter gösterip sonra sabitlemek.
    - Çekirdekler: `view()` ile farklı `translateY` hızları.
- **Ayluna'ya uygunluk:** **yüksek.** Yarıktan basılan fiş, kapıda ödeme sipariş özeti ya da "siparişin hazırlanıyor" anı için birebir uyuyor. Ayrıca alınabilecekler:
  - el yazısı çizimiyle vurgulanan başlık kelimesi
  - ürün üstünde açılan fiyat etiketi (mobilde dokunmayla)
  - kahve çekirdeği yerine yıldız/ay parçacıkları
  - Hepsi saf CSS ve az JS ile yapılır.
- **Durum:** teknik (yeni). Kütüphane bilinmiyor.
- **Güven notu:** "LIBRARY" yorum tuzağı var. "Opus 5.5 and 10 minutes" abartılı ve doğrulanamaz. Kütüphane "erişim" ile sunuluyor, büyük olasılıkla ücretli (fiyat gösterilmiyor).

### DeoOwg2jhzP · Thane (buildingwiththane) · 23,8 sn · konuşma yok (müzik; döküm tek satır, anlamsız)
- **Konu:** "Websites that make me a 10x better vibe coder" başlığıyla üç site tanıtılıyor. Etiketler #ad ve #manuspartner, yani **Manus reklamı**. Sahne değişimleri yaklaşık 1–1,5 sn'de bir.
- **Adı geçenler:**
  - **SiteReel.ai** (1,7–7,5 sn ve 19–20 sn): "Massive collection of prompts to build websites with AI", "Copy any prompt and paste it into your builder of choice". Ekranda görünen örnekler:
    - "Find your spark."
    - "Nival — Offworld Collection — Interactive Website Template"
    - "Sprig — Playful Product Website Template"
    - "Signalhouse — Data Visualization Website Template"
  - **Manus.im** (7,5–15,7 sn): Altyazılar "Build flawless backend powered websites and apps with AI", "Just type a simple prompt", "And wait for the agent to build everything".
    - Örnek: "Pure Zero · Refreshingly Clean" soda sitesi.
    - "Publish straight to the web in one click": "Your site is now live!", alan adı `…manus.space`.
    - "With built-in analytics and SEO tracker": Page views 2.72K, Visits 1.24K.
    - Adres çubuğunda `manus.im/app/…` (9 sn).
  - **Realtime Colors** (16,4–19 sn): "Test a colour palette and font pairing on a full fake website, live". Site başlığı "Visualize Your Colors & Fonts On a Real Site". Adres ekranda yok.
- **Öğrenilecek teknik:** Realtime Colors'ın mantığı: paleti ve font çiftini gerçek bir sahte sayfa üzerinde anında denemek. Bizde karşılığı tuvalde `:root{--bg;--ink;--accent}` değişkenlerine bağlı bir palet anahtarı kurmak, birkaç aday aynı sayfada yan yana. SiteReel yalnız ilham kaynağı. Manus, Claude Code + Shopify akışıyla çakışıyor.
- **Ayluna'ya uygunluk:** Realtime Colors orta (palet seçili ama ikincil renk/yazı denemesinde işe yarar). SiteReel düşük-orta. Manus düşük (Shopify dışında barındırıyor, gereksiz).
- **Durum:** yeni.
- **Güven notu:** Ücretli ortaklık reklamı (#ad #manuspartner). "BUILD" yorum tuzağı var. "10x better" ve "flawless" abartı. Analitik rakamları demo.

---

## Grup 5 · tekilleştirilmiş araç tablosu

| Ad | Tür | Adres (ekranda görüldüğü kadar) | Gönderi | Uygunluk |
|---|---|---|---|---|
| frontend-design skill | skill | github.com/anthropics | Deglhh-lDwu | **kurulu** |
| "Improving frontend design through Skills" | site (Anthropic blog) | claude.com | Deglhh-lDwu | yüksek (okuma) |
| Chrome DevTools MCP | MCP | github.com/ChromeDevTools | Deglhh-lDwu | orta (Playwright MCP ile örtüşür; performans izi için aday) |
| Remotion | skill / kütüphane | yok | DeecRIEDB8q | orta (tanıtım reel'i) |
| Competitor Ads Extractor | skill | yok | DeecRIEDB8q | orta (pazarlama; elle de yapılır) |
| Deep Research | skill / servis | yok | DeecRIEDB8q | düşük-orta |
| Voice DNA | skill | yok | DeecRIEDB8q | orta (marka üslubu) |
| ElevenLabs | servis (hesap gerekli) | yok | DeecRIEDB8q | düşük |
| Motionsites | site (ücretli) | okunamadı | DemSHfZOGSO | düşük |
| MotionPrompt AI Design Library | site (prompt kütüphanesi) | okunamadı | DemSHfZOGSO | düşük |
| HeroPrompts (logo bulanık) | site (freemium) | okunamadı | DemSHfZOGSO | düşük; "specified to the pixel" ilkesi yüksek |
| scrollhaus | site + MCP (yıllık $159,20) | MCP: `https://<okunamadı>.supabase.co/functions/v1/mcp` | DemSHfZOGSO | düşük, **kurulmamalı** |
| Framer şablonları (Storm Lab, Foldfolio, Mondragon 1/4, Nika Stern, Cubo Agency, filmstrip) | site / şablon | …framer.app | DeeZPyaoN3O | düşük (fikir alınır) |
| unknown reality archive | site | "…hive.com" (kısmi) | DeeZPyaoN3O | düşük |
| SiteReel.ai | site (prompt kütüphanesi) | SiteReel.ai | DeoOwg2jhzP | düşük-orta |
| Manus | uygulama (reklam) | manus.im, manus.space | DeoOwg2jhzP | düşük |
| Realtime Colors | site | yok | DeoOwg2jhzP | orta |
| Claude Opus 5.5 / Gemini 4 Argon | model (bilgi) | yok | Dem0dU5uq2v | yok |
| Kaydırmayla yarıktan basılan fiş + fiyat scramble + el yazısı çizimi | teknik | yok | DehcS3aAXVi | **yüksek** |
| "Seçenek → anında önizleme" ürün paneli | teknik | yok | Dem0dU5uq2v | yüksek |
| Ürün animasyonun kahramanı (rulo açılıyor) + eğri akan yazı | teknik | yok | DemSHfZOGSO | orta |
| Figür arkasından geçen yazı, başlığa gömülü küçük görsel, parçacık portre | teknik | yok | DeeZPyaoN3O | orta-düşük |
| Düğüm haritası, halka çizimi, kelime kelime altyazı (video kurgusu) | teknik | yok | DeecRIEDB8q | orta (reel) |
