# Grup 1 · 7 gönderi

Kareler: `ozet/kare-grup1/` (her gönderi için 10-15 tam kare + kırpılmış montajlar `*-mont*.jpg`).
Ayluna'da zaten olan: `canvas/Main.dc.html` kaydırmaya bağlı belirme (`animation-timeline: view()`, `.rv/.kalk/.harf/.buyut`) ve yapışkan alt satın alma çubuğu. Kaydırmaya bağlı **ürün videosu/kare dizisi** ve **ürün hotspot'u** yok.

---

### DeACi9uRWgn · Ascenta Studio | Web Design · 13.7 sn · konuşma yok (döküm müzik sözü, güven 0.36)
- Konu: Ajans, "PIVOINE" adlı tek ürünlü şakayık kremi sitesini aynı anda kavisli monitörde ve telefonda kaydırıyor. Kaydırdıkça şakayık açılıyor, kavanoz çiçeğin içinden yükselip öne geliyor, kapak açılıp havada süzülüyor, kremin üstten girdabı görünüyor; sonda 4 ürünlük ızgara.
- Adı geçenler:
  - "PIVOINE" (marka), üst menü "The flower · The cream · The line" + rozetli sepet + "Shop" hap düğmesi (0.5 sn).
  - Bölüm başlıkları: "Peony, at first bloom." + "Add to bag · $128" / "See the line" (0.5), "Picked at dawn, when it's fullest." (2), "One jar, three jobs." (3.5-5), "Whipped, then it melts." (6.5), "Four pieces, one ritual." + "Shop the line" (8-9.5), "Four pieces, one peony." (9.5-13.4).
  - Ürün ızgarası: Renewal Cream $128, Dew Serum $96, Eye Balm $72, Night Oil $88, her birinde "Add to bag" (11-13.4).
  - Yüzen rozet "Built by Ascenta · Get a site like this →" (tüm video, sağ alt / telefonda alt orta).
  - Sitenin adresi ekranda okunamadı. Kullanılan araç adı yok.
- Öğrenilecek teknik: **Kaydırmaya bağlı ürün hikâyesi (scroll-scrub).**
  - Masaüstü: solda metin sütunu (küçük harf aralıklı üst etiket, 2 satır serif başlık, 2. satır italik, kısa gövde). Sağda yapışkan ürün sahnesi. Her bölüm ~1 ekran kaydırma. Metin değişirken eskisi solup yenisi geliyor (~300-400 ms).
  - Mobil: metin üstte, ürün altında yapışkan. Aynı dizi oynuyor. Üstte ortalanmış kapsül menü (logo, sepet, Shop). Altta yüzen hap.
  - Renk: soluk lila-pembe zemin, koyu mürdüm kapak, mor hap düğmeler. Başlıklar Playfair benzeri yüksek kontrastlı serif (masaüstünde ~40-48px).
  - Yapımı: 400-500vh yüksekliğinde dış kap + `position: sticky` sahne. Sahnede önceden yüklenmiş WebP kare dizisi `<canvas>`'a kaydırma oranıyla çizilir (ya da `video.currentTime = oran × süre`). Metinler IntersectionObserver veya `animation-timeline: view()` ile değişir.
- Ayluna'ya uygunluk: **yüksek**. LunaDream için birebir eşleşiyor: lamba kapalı → açılıyor → tavana yıldızlar → renk modları → ürün/paket ızgarası. Mobil düzen 390px'e uygun. İlk ekranda fiyat ve "Sepete ekle" vermesi de iyi örnek. Dikkat: kare dizisi ağır olur (afiş görseli + tembel yükleme şart). Ayluna kuralı "sayfa videosuz da satmalı" korunmalı.
- Durum: yeni (teknik). Kaydırmaya bağlı CSS belirme zaten kurulu; ürün kare dizisi yok.
- Güven notu: Ajans reklamı ("Get a site like this" rozeti). Açıklamadaki "ucuz ürünü pahalı gösterir" bir pazarlama cümlesi. Yorum tuzağı yok, ücret bilgisi yok.

### DeKUZvGsiDk · MotionLove · 14.4 sn · konuşma yok
- Konu: Laptop ekranında "CLAUDE – MOTION REEL 2026" adlı 7 sahnelik bir showreel oynuyor. Üstte Claude yıldız logosu ve "5.5 is ridiculous at motion" yazısı var. Sahneler sırasıyla kimlik/tipografi, 3D mograph, kinetik tipografi, veri/infografik, üretken parçacıklar, UI/ürün hareketi ve şekil/sıvı. Kapanış: "Claude motion designer · EVERY FRAME, ON PURPOSE".
- Adı geçenler:
  - "5.5" (0-14 sn). Hangi ürün olduğu yazmıyor. Logo yüzünden Claude model sürümü olabilir ama doğrulanmadı.
  - "CLAUDE – MOTION REEL 2026", "SCENE 0X / 07" sayacı ve zaman kodu (2.5-12.5).
  - Sahne etiketleri:
    - "IDENTITY / TYPE" (2.5)
    - "3D / MOGRAPH" (3.5-4.5)
    - "KINETIC TYPOGRAPHY" (5.5-6.5)
    - "DATA / INFOGRAPHICS": "+312%", "78% RETENTION", "MONTHLY REACH" (7.5)
    - "GENERATIVE / PARTICLES": "n = 2,400 · φ = 137.508°" (8.5-9.5)
    - "UI / PRODUCT MOTION": "Render queue · Motion blur · Frame rate 30/60 · Render" (10.5)
    - "SHAPE / LIQUID": "r(θ) = superformula" (12.5)
  - Etiketler #aftereffects #claude, ama After Effects arayüzü görünmüyor. Nasıl üretildiği gösterilmiyor.
- Öğrenilecek teknik: Tarayıcıda yeniden yapılabilir hareket kataloğu.
  - Nokta ızgarası üstünde parlayan turuncu nokta girişi.
  - Beyaz flaşla turuncu zemine geçiş. Dev grotesk "CLAUDE." harflerinin kalınlığı tek tek değişiyor (değişken yazı tipi `font-variation-settings: 'wght'` animasyonu). Altında italik serif "motion designer".
  - Dalgalanan küp ızgarası ve yörünge halkalı cam küre (Three.js InstancedMesh).
  - İçi boş kontur kelime satırları kayıyor, ortadaki kelime dolu (kinetik marquee).
  - Sayı sayacı (count-up), halka grafik ve çubuk grafik büyümesi, çizgi grafiği çizilmesi (`stroke-dashoffset`).
  - Akış alanı parçacık çizgileri, ardından ayçiçeği sarmalı (phyllotaxis: `r = c·√i`, `θ = i·137.508°`).
  - Perspektifli üst üste kartlar, anahtar ve segment düğme animasyonu.
  - Superformula ile morflanan blob.
  - Kapanışta karışık harflerin çözülerek yazıya dönüşmesi (text scramble).
  - Hepsi HUD çerçevesi içinde: köşe parantezleri ve monospace etiketler.
  - Yapımı: GSAP timeline ya da canvas. Scramble için her karede rastgele harfi hedef harfle değiştiren küçük bir JS döngüsü.
- Ayluna'ya uygunluk: **orta**. Ürün sayfasına doğrudan değil. Ama phyllotaxis/parçacık yıldız alanı LunaDream "yıldızlı tavan" hero'su için hafif bir canvas ilhamı olabilir. Ayrıca "Claude ile HTML animasyon yaz → ekran kaydı al → Reels" akışı Ayluna Instagram kiti için kullanılabilir. Mobil sayfada ağır olur.
- Durum: yeni (teknik). Araç gösterilmedi.
- Güven notu: "Do you want a tutorial? ⬇️" + 1.858 yorum, yorum toplama kalıbı. "5.5 is ridiculous" abartılı iddia. Claude'un tek başına yaptığı kanıtlanmıyor (AE etiketi var).

### Dd9HttYsLEX · arif | AI Influencer & UGC Creator · 51.9 sn · konuşma var (Türkçe)
- Konu: Anlatıcı "Prompt Master" adlı Claude becerisini tanıtıyor. Dağınık bir cümle yazınca beceri yapılandırılmış bir istek döndürüyor (Hedef / Çıktı / Kapsam / Dur). İddiaya göre 35 "kredi yakan" durumu kontrol ediyor ve önceki kararları hatırlıyor. Kurulum: repo ZIP → claude.ai → Customize → Skills → Upload. Ekranın üst yarısı animasyonlu arayüz maketi, alt yarısı konuşan kafa.
- Adı geçenler:
  - **Prompt Master**, `github.com/nidhinjs/prompt-master` (6-11 sn, 29 sn, 43 sn).
    - Ekranda: Star 13.9k, Fork 1.6k, Issues 21, Pull requests 13, MIT license. Dosyalar: `references/`, `LICENSE`, `README.md`, `SKILL.md` (9-11 sn).
    - Tanıtım afişi "Prompt Master · Write once. Get it right" ve açıklama "A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention…" (8 sn).
    - README "Works with: Claude, ChatGPT, Codex, Grok, Gemini, o1/o3, MiniMax, Cursor, Claude Code, GitHub Copilot, Windsurf, Bolt, v0, Lovable, Devin, Perplexity, Midjourney, DALL-E, Stable Diffusion, ComfyUI, Sora, Runway, ElevenLabs, Zapier, Make" (43 sn).
    - Kurulum adımı "1. Download this repo as a ZIP 2. Go to claude.ai → Sidebar → Customize → Skills → Upload a Skill" (43 sn).
  - Çağırma `/prompt-master` (~19 sn).
  - claude.ai "Your usage · Max (5x)" kullanım ekranı (1 sn) ve "Customize · Skills / Connectors / Plugins · Discover" ekranı (31 sn).
- Öğrenilecek teknik:
  1. Dört alanlı istek şablonu, beceri kurmadan uygulanabilir (23 sn):
     - HEDEF: "Notion hissinde, akıcı animasyonlu landing page"
     - ÇIKTI: "Tek HTML · Inter · beyaz zemin · 6px köşe"
     - KAPSAM: "yalnız index.html — başka dosyaya dokunma"
     - DUR: "hero + 3 bölüm bitince dur, onay iste"
  2. Reel kurgusu: üst yarıda arayüz maketi animasyonu (bulanıktan netleşme, beyaz çerçeveyle vurgu), alt yarıda konuşan kafa, her sözcük için tek kelimelik dev altyazı.
- Ayluna'ya uygunluk: **orta** (şablon) / **düşük** (becerinin kendisi). Claude Code tarafında CLAUDE.md, brif ve Ayluna kuralları bu işi zaten görüyor; beceri ekstra ve çakışan bir katman olur. Şablondaki "KAPSAM" ve "DUR" alanları tuval isteklerinde işe yarar.
- Durum: yeni (bakılanlar listesinde yok).
- Güven notu:
  - Yorum tuzağı: "PROMPT yazın, göndereyim", 406 yorum.
  - Tutarsız sayı: açıklamada "11.000 yıldız", ekranda 13.9k.
  - Abartılı iddialar: "Zero tokens wasted" ve "limite takılmazsın".
  - Ücretsiz ve MIT lisanslı. Üçüncü taraf beceri olduğu için kurmadan önce `SKILL.md` ve `references/` satır satır okunmalı.

### DeXdvIGMrAq · Enkis Web Studio · 10.0 sn · konuşma yok (açıklama yok)
- Konu: Masadaki laptopta "GRIND" adlı kahve sitesi kaydırılıyor: GRIND → POUR → SIP bölümleri. Öğütücü parçalarına ayrılıyor, çekirdekler düşüyor, kettle'dan filtreye su dökülüyor, fincana kahve sıçrıyor. Sonda "SIP Premium Coffee", 3 ürün kartı (ORIGIN, ROAST, FLAVOR) ve "FIND YOUR CUP →".
- Adı geçenler:
  - "GRIND" logosu (0.3-9.9), "Log in", "Sign Up", "FIND YOUR CUP →" (8.4-9.9).
  - Menü ve gövde metinleri anlamsız harf dizileri ("Sofee", "Fead more"), okunamadı. Bu yüzden video büyük olasılıkla yapay zekâ video üreticisiyle yapılmış bir maket, gerçek site değil.
  - Araç adı yok.
- Öğrenilecek teknik:
  - **Dev kelimenin önünde ürün:** her bölümde ~20vw boyutunda display kelime (GRIND/POUR/SIP) ürünün arkasında duruyor, dekupe ürün görseli harfleri kısmen örtüyor.
  - Organik blob şekiller. Renkler: terracotta ~#b8735a, krem ~#f3e6d6, koyu kahve ~#3b2420. Dört köşeli yıldız süsler.
  - Bölüm geçişi: ürün aşağı kayıp hareket bulanıklığıyla çıkıyor, yenisi alttan geliyor.
  - Öğütücü yatayda patlatılmış görünüme ayrılıyor (3-4 sn).
  - Sağ kenarda dikey bölüm noktaları.
  - Son bölüm: ortalanmış başlık + fincan + hafif dönük, gölgeli yüzen ürün kartları.
  - Yapımı: tam ekran bölümler ve `scroll-snap-type: y mandatory`. Kelime `position:absolute; z-index:0`, ürün PNG/WebP `z-index:1`. Girişler GSAP ScrollTrigger veya `animation-timeline: view()` ile `translateY` + `filter: blur()`.
- Ayluna'ya uygunluk: **orta**. "Dev kelimenin önünde ürün" ve "yüzen ürün kartları" hafif, mobilde de çalışan ve Ayluna hero'suna uyan bir katman fikri (ör. dev "LUNA" yazısının önünde lamba). Main.dc.html'deki `.harf` dev yazısıyla birleşebilir. Gösterilen hali gerçek bir site değil.
- Durum: yeni (teknik).
- Güven notu: Büyük olasılıkla AI üretimi video (anlamsız yazılar); "site" gibi sunulması yanıltıcı. Reklam veya yorum tuzağı yok.

### DbpDjkivpOK · wearebrand · 10.6 sn · konuşma yok
- Konu: iMac'te gerçek bir kurumsal site geziliyor. Önce gece lacivertinde dağ, sonra bulutlar içinde gri dağ; "TRADING · CAPITAL · MARITIME" kelimeleri yatayda kayıyor. Dağ yeşile dönüyor, kamera göl ve çayırın üstünden alçalıyor. Çimen dokusunun üstünde "MONTFORT CAPITAL IS A NEWLY FOUNDED FUND MANAGEMENT COMPANY, BUILT ON THE EXPERTISE OF A GLOBAL LEADER IN COMMODITY TRADING." Altbilgide Geneva / Dubai / Singapore. Ekranın üstünde "Claude Code can't do that 🤩" yazısı.
- Adı geçenler:
  - "MONTFORT TRADING" ve menü "MONTFORT GROUP · MONTFORT TRADING · MONTFORT CAPITAL · MONTFORT MARITIME · FORT ENERGY" (0.3 sn).
  - "SCROLL DOWN TO DISCOVER" (0.3).
  - Adres çubuğu "mont-fort.com/trading/" (0.3, bulanık ama okunuyor), sonra "…/capital" (9.3, bulanık).
  - Siteyi yapan ajans veya araç ekranda yok.
- Öğrenilecek teknik:
  - WebGL 3D arazi (yükseklik haritalı dağ) ve alfa sprite bulut katmanları.
  - Kaydırma kamerayı bir yol üzerinde ilerletiyor.
  - Bölüm adları dağın önünde yatay şerit halinde kayıyor; aktif olan ortada ve koyu.
  - Sahne geçişinde ince dikey ışık çizgileri.
  - Gri dokudan yeşil dokuya renk geçişi. Kamera yere eğilip metni dokunun üstüne koyuyor.
  - İnce, geniş harf aralıklı sans başlıklar (~0.3em) ve daire şeklinde özel imleç.
  - Yapımı: Three.js PlaneGeometry + displacement map, GSAP ScrollTrigger ile kamera `position`/`lookAt` scrub.
- Ayluna'ya uygunluk: **düşük**. Mobil Shopify ürün sayfası için fazla ağır (WebGL, büyük dokular) ve satışa hizmet etmiyor. Yalnız "kaydırmayla kamera yolculuğu" fikri not.
- Durum: yeni (teknik).
- Güven notu: "Claude Code can't do that" kışkırtıcı bir ajans reklamı. Açıklama "Future of webdesign is NOW" + #wordpress. Sitenin wearebrand işi olduğu ekranda doğrulanmıyor.

### DdsO05yDfxh · Altra Labs | Educação em IA · 12.7 sn · konuşma yok
- Konu: Telefonda (arkada laptopta) "awwwards. × estudio/nk" imzalı "THE MAGIC BOTTLE" etkileşimli 3D şişe sitesi geziliyor. Sırasıyla: yükleme sayacı, dönen şişe, numaralı özellik noktaları, "kapağı sürükleyerek aç", "salla", şişenin beyaza dönmesi. Üstte "Site criado com Chat GPT" yazısı.
- Adı geçenler:
  - Adres `magic.estudionk.com` (0.3-12.3) ve imza "awwwards. × estudio/nk" (1.2-12.3).
  - Üstteki yazı "Site criado com Chat GPT" (tüm video).
  - Ekrandaki metinler:
    - "TAP ANYWHERE TO START / OR CONTINUE WITHOUT AUDIO" (0.3)
    - "THE MAGIC BOTTLE · EXPLORE · LET'S TALK" (1.2-2.1)
    - "SCREW CAP" (3-3.9)
    - "NON-SLIP BASE" (4.8)
    - "ELEGANT DESIGN – Solid color design from top to bottom and beautiful smooth rubber exterior. *Drops not included." (5.7)
    - "TAKE THE CAP OFF · DRAG IT FROM LEFT TO RIGHT · CONTINUE" (8.4)
    - "SHAKE IT · SUPERFAAAASSSST" (9.3-11.1)
  - Sağ kenarda dikey "KEEP SCROLLING", altta çerez çubuğu.
- Öğrenilecek teknik:
  - 00→99 yükleme sayacı ve sesli/sessiz giriş seçimi.
  - GLTF şişe kaydırmayla dönüp yaklaşıyor.
  - Ürünün üstünde numaralı, nabız atan halka "hotspot"lar.
  - Çok dar (condensed) dev başlıklar bulanık/kaymalı girişle geliyor.
  - Sürükleme jestiyle kapak çıkarma (pointer events).
  - "Salla" adımında köpük/kabarcık parçacıkları.
  - Renk varyantı değişimi (materyal rengi siyahtan beyaza).
  - Turkuaz duman arka plan.
  - Yapımı: Three.js/R3F + ScrollTrigger. Hotspot = 3D noktanın ekrana izdüşümüne konan HTML düğmesi.
- Ayluna'ya uygunluk: **orta**. Üç fikir güçlü: renk/mod seçince ürün görselinin değişmesi, özellik hotspot'ları (şarj, kumanda, projeksiyon diski) ve "dokun / kaydır: lambayı aç" etkileşimi. WebGL, ses ve 3D model mobil KÖ sayfası için ağır. Hafif sürüm: 2-3 fotoğraf veya kısa video + mutlak konumlu hotspot düğmeleri.
- Durum: yeni (teknik).
- Güven notu: "Site criado com Chat GPT" iddiası ekrandaki "awwwards. × estudio/nk" imzasıyla çelişiyor, yanıltıcı. Yorum tuzağı: "comente LINK" (251 yorum) + bio linki. Hesap bir AI eğitimi satıyor.

### DbP0tEXxYNF · Keith AI · 11.7 sn · konuşma yok
- Konu: Laptopta "uiprompts.app" adlı prompt kütüphanesi hızla kaydırılıyor: "Cinematic UI, one prompt away." ve onlarca sinematik hero kartı. Ardından bir örnek site: "VERMEIL" saat sitesi. Kaydırdıkça saat parçalarına ayrılıyor (exploded view), etiketleniyor ve geri birleşiyor. Ekranın üstünde "10k websites in 5 minutes 😱".
- Adı geçenler:
  - **uiprompts.app** (0.2-9 sn).
    - Slogan: "Cinematic UI, one prompt away. Copy a prompt, paste it into your AI coder, and ship a site that doesn't look AI-made. The source video comes wired in." Düğmeler "Browse the library" ve "Build with the MCP" (0.2).
    - Menü "Library · MCP · Learn · Get the pack".
    - Üst şerit "Founding price — lifetime access $?? $499 · rising soon →" (0.2; ilk fiyat okunamadı).
    - Kartlarda "Free"/"Premium" rozetleri ve "hero section · react · tailwind" etiketleri. Örnek kart adları: Flowstate, Stillwater, Nox, Beacon, Mercury, Magma, Cobalt, Event Horizon, Wormhole, Nebula, Monument (1.8-5).
  - **VERMEIL** demo sitesi (8.2-11.5).
    - Menü "CALIBRE · CRAFT · COLLECTION · ATELIER", "ENQUIRE" düğmesi.
    - Bölümler "I · ARRIVAL / II · ANATOMY / III · RETURN", sağ altta "SCROLL TO DISASSEMBLE".
    - Parça etiketleri: SAPPHIRE CRYSTAL, FLUTED BEZEL, CALIBRE 3235, OYSTER CASE BACK, PRESIDENT BRACELET.
    - Özellik hapları "70H POWER RESERVE · 28,800 VIB/HOUR · 18CT EVEROSE GOLD", son CTA "Request an audience".
    - Sol altta 20 → 94 ilerleme sayacı.
  - Açıklama etiketleri: #opus #claude #fable5.
- Öğrenilecek teknik: **Kaydır → ürünü sök → anlat → birleştir.**
  - Tam ekran yapışkan sahne. Ürün videosu veya kare dizisi kaydırma oranına bağlı oynuyor.
  - Ürünün arkasında düşük opaklıklı dev serif "TIMELESS" yazısı.
  - Üstte I/II/III bölüm göstergesi (aktif olanın yanında çizgi).
  - Parçalar ayrılınca ince yazı etiketleri beliriyor. Alt ortada 3 sayısal özellik hapı.
  - Sol altta 0-100 ilerleme sayısı ve çizgisi. Sonda birleşme ve tek CTA.
  - Yapımı: `height: 400vh` dış kap + `position: sticky; top: 0` sahne + `<video muted playsinline preload>` için kaydırmada `currentTime` ya da canvas kare dizisi. Sayaç `Math.round(oran × 100)`, etiketler oran eşiklerinde `opacity`.
  - "The source video comes wired in" = prompt'la birlikte hazır bir AI videosu geliyor ve sayfa onu kaydırmayla oynatıyor (PIVOINE ile aynı teknik).
- Ayluna'ya uygunluk: **yüksek** (teknik) / **düşük** (paketi satın almak). Vermeil kurgusu LunaDream'e doğrudan uyar: "lambanın içi: LED, yıldız diski, şarj, kumanda" parçalara ayrılıp etiketlenir, sonra "Sepete ekle". Tekniği Claude Code ile kendimiz yazarız. Video için ürünün kendi çekimi ya da Ayluna görsel kitinden üretilen kısa bir klip gerekir.
- Durum: yeni.
- Güven notu:
  - Ücretli: "Founding price — lifetime access", "Get the pack", Premium kartlar, MCP.
  - Yorum tuzağı: "comment prompt" (11.186 yorum).
  - Abartılı ve tutarsız: ekranda "10k websites in 5 minutes", açıklamada "over 90 … websites".
  - Hesabın kendi ürünü mü yoksa ortaklık (affiliate) mı, belirsiz.

---

## Grubun araç tablosu (tekilleştirilmiş)

| Ad | Tür | Adres | Gönderiler | Uygunluk |
|---|---|---|---|---|
| Kaydırmaya bağlı ürün videosu / kare dizisi (sticky sahne + scrub) | teknik | — | DeACi9uRWgn, DbP0tEXxYNF, DeXdvIGMrAq | yüksek |
| Exploded view + parça etiketleri + ilerleme sayacı (Vermeil kurgusu) | teknik | — (uiprompts.app demosu) | DbP0tEXxYNF, DeXdvIGMrAq | yüksek |
| Dev kelimenin önünde dekupe ürün (katmanlı hero) | teknik | — | DeXdvIGMrAq, DbP0tEXxYNF | orta |
| Ürün hotspot'ları + sürükle/dokun etkileşimi + varyantla görsel değişimi | teknik | — | DdsO05yDfxh | orta |
| Yüzen kapsül menü + yüzen alt hap (mobil) | teknik | — | DeACi9uRWgn | orta (Ayluna'da yapışkan alt çubuk zaten var) |
| HTML hareket kataloğu (count-up, text scramble, phyllotaxis yıldız alanı, değişken yazı kalınlığı) | teknik | — | DeKUZvGsiDk | orta |
| Dört alanlı istek şablonu (Hedef / Çıktı / Kapsam / Dur) | teknik | — | Dd9HttYsLEX | orta |
| Prompt Master | skill | github.com/nidhinjs/prompt-master | Dd9HttYsLEX | düşük |
| uiprompts.app (ücretli sinematik prompt kütüphanesi + MCP) | site | uiprompts.app | DbP0tEXxYNF | düşük |
| PIVOINE demo / Ascenta Studio | site (ajans örneği) | okunamadı | DeACi9uRWgn | yüksek (referans) |
| The Magic Bottle (awwwards × estudio/nk) | site (referans) | magic.estudionk.com | DdsO05yDfxh | orta (referans) |
| Montfort | site (referans) | mont-fort.com/trading/ | DbpDjkivpOK | düşük |
| WebGL arazi + kamera yolu | teknik | — | DbpDjkivpOK | düşük |
