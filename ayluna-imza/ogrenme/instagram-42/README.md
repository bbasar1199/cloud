# 42 Instagram reel'i · ne kurulur, ne öğrenilir (18 Ekim 2026)

Kullanıcı 42 reel paylaştı: "Her birini dikkatlice incele ve izle; kurmamız gerekenleri ve öğrenebileceğim yeni şeyleri öğren, bana anlat."

**Yöntem:**
- Her video indirildi ve ses dökümü çıkarıldı (Whisper).
- Kareler alındı; okunması gereken yazılar tam çözünürlükte büyütülüp okundu.
- 6 ajan 7'şer gönderi inceledi. Gönderi gönderi ayrıntı: `grup1.md` – `grup6.md`. Kareler geçici klasördeydi, saklanmadı.
- Kurulum adayları ayrı bir ajanla, kurulmadan denetlendi: `denetim.md`.

## Önce genel tablo
- Yaklaşık 30 gönderi "yorumlara X yaz" tuzağı.
- Bir kısmı ücretli reklam: Manus #ad (iki kez), uiprompts.app, vividsites, scrolltide, HorizonX, getlayers, scrollhaus, MotionSites.
- "Claude yaptı" diye gösterilen birçok site başkasının işi:
  - activetheory.net: WebGL stüdyosunun kendi sitesi.
  - shopify.com/editions/winter2026: Shopify'ın resmî sayfası.
  - Slider Revolution: WordPress eklenti demosu.
  - The Magic Bottle: awwwards × estudio/nk işi.
  - Enkis'in kahve siteleri: yazıları bozuk yapay zekâ videoları.
- Bir videoda prompt Grok'a yapıştırılıyor; bir başkasında yapıştırılan prompt başka bir siteye ait.
- Değerli olan, araçlardan çok **gösterilen teknikler** ve **çalışma yöntemi**.

## Kurulacaklar
| Ne | Neden | Durum |
|---|---|---|
| Playwright MCP'ye `--no-sandbox` | Root'ta Chromium açılmıyordu; design-review ajanının gözü çalışmıyordu | Denendi, çalışıyor. `.mcp.json` onayı bekliyor |
| Chrome DevTools MCP 1.11.0 | Telefonda hız ölçümü: performans izi, LCP/CLS, Lighthouse, ağ/CPU yavaşlatma. Playwright'ta yok. | Denendi (32 araç, iz çalıştı). Telemetri kapalı. `.mcp.json` onayı bekliyor |
| design-review ajanı | Eski araç adı (`browser_tab_list` → `browser_tabs`) | Düzeltildi |

Bunlar dışında kurulması gereken bir şey çıkmadı. Videoların çoğunun önerdiği "Claude'a tasarım skill'i + tarayıcı gözü" düzeni bizde zaten var: frontend-design, Taste, Web Design Guidelines, Playwright, design-review.

Kurulmayanlar ve gerekçe `denetim.md`'de. Kısaca:
- **UI UX Pro Max:** daha önce elendi.
- **21st.dev Magic ve Framer Motion:** React; Liquid temaya girmez.
- **Stitch:** Claude Design aynı işi yapıyor; Claude Code'da bağlantı hatası var.
- **transitions.dev:** lisansı kopyalamayı kısıtlıyor; tariflerin yarısı blur kullanıyor.
- **AutoAE, scrollhaus:** uzaktan değişen talimat ya da bilinmeyen sunucu.
- **Remotion:** Projede zaten kullanılıyor (`araclar/remotion`, 4.0.300). Resmî skill'i Instagram kiti aşamasında alınabilir. Lisans: 3 çalışana kadar ücretsiz, üstü şirket lisansı.

## Ayluna'ya uyan teknikler (tuvalde denenebilir)
Hepsi saf CSS ve az JS ile, mobilde hafif yapılır. Ayluna kuralları geçerli: tek eğri, yalnız transform/opacity, azaltılmış hareket desteği, sayfa videosuz da satar. `TASARIM-BILGISI` §4'e göre **imza an hâlâ seçilmedi**; ilk üçü bu an için aday.

1. **Dev yazı arkada, lamba önde, alttan yükselir.**
   - Kaynak: Dc-4bsGuE6V (PLAIN MILK), DeXdvIGMrAq (GRIND), DeO8WC0zxol (ORISON).
   - Büyük "LUNA" yazısı arkada, dekupe lamba önde (`lamba-kiz.png` hazır).
   - Lamba 400–500 ms'de yükselir. Harfler 40–60 ms arayla açılır.
   - Ön yükleyici yok; toplam giriş 700 ms'yi geçmez.
2. **Yarıktan basılan fiş.**
   - Kaynak: DehcS3aAXVi (brewns).
   - Kapıda ödeme sipariş özeti, kaydırınca bir yarıktan aşağı uzar: ürün, toplam, teslim tarihi, buton.
   - `view()` zaman çizelgesi + `overflow: clip` + `translateY`.
3. **Seçince sahne değişir.**
   - Kaynak: Dem0dU5uq2v (balkabağı paneli), DdETp-tNFW2 (dondurma kaydırıcı).
   - Kız/Erkek ya da disk seçilince zemin rengi ve ürün görseli yumuşakça değişir. Seçenek → anında önizleme.
   - 500–700 ms yeterli; videodaki 2400 ms yavaş.
4. **Kaydırmaya bağlı ürün sahnesi.**
   - Kaynak: DeACi9uRWgn (PIVOINE), DbP0tEXxYNF (VERMEIL), DbgjytGySiQ (Hungry Tiger), Dd3_W81zVxI (Sumi).
   - Sahne yapışkan kalır, kaydırdıkça ürün değişir. "Bir gece, beş an" bunun hafif hâli.
   - Bir sonraki basamak lambanın kendi kısa çekimi ya da 6–8 kare: kapalı → açılıyor → tavana yıldız → içi (LED, disk, şarj) etiketli.
   - Sumi'nin cümlesi iyi bir ses örneği: "When the lantern is lit, we stop."
5. **Ürün üstünde özellik noktaları.**
   - Kaynak: DdsO05yDfxh.
   - Fotoğraf üstünde dokunulan noktalar: şarj, kumanda, disk yuvası. WebGL gerekmez.
6. **Sayfa boyunca duran ay diski ya da bölümden bölüme taşan ışık huzmesi.**
   - Kaynak: Deaa37pMhT3, DeStzYDMNrQ.
   - Tek SVG + sticky. Yalnız gece bandında.
7. **Küçükler:**
   - Kaydırma ilerleme çizgisi (`scroll()` + `scaleX`).
   - Kenara açılan kart (`clip-path: inset()` + `view()`). Not: clip-path transform/opacity dışında kalır; kullanıcı kararı.
   - El yazısıyla çizilen tek vurgu kelimesi (SVG stroke).

**Uymayanlar:**
- Fiyat rakamlarının karışıp oturması (sayaç kuralına takılır).
- Ön yükleyici ekranı (kapıda ödeme kitlesini bekletir).
- Tam koyu sinematik siteler.
- WebGL, Three.js, shader ve liquid glass (mobil ve Instagram tarayıcısında ağır).

## Hazır hareket değerleri (DXruEuojJLI'deki prompt'tan, CSS'e çevrilir)
- **Liste/ızgara girişi:** çocuklar sırayla 90 ms arayla. Asla hepsi birden değil.
- **Kelime kelime başlık:** 0,7 sn, kelime başına 100 ms.
- **Çekmece/modal:** açılış 0,3 sn (ölçek .9 → 1), kapanış 0,2 sn (ölçek .95, y −6).
- **Menü alt çizgisi:** `scaleX 0→1`, soldan, 0,25 sn.
- **Azaltılmış hareket:** yalnız opacity kalır, süre aynı.

Ayluna'da prompt'taki blur adımları alınmaz; yalnız opacity + translate.

## Çalışma yöntemi dersleri
1. **İsteği ölçüyle yaz.** Hex, font ağırlığı, eğri ve ms verilirse model doğaçlama yapmaz (HeroPrompts, DemSHfZOGSO).
2. **Dört alanlı istek:** Hedef / Çıktı / Kapsam ("yalnız şu dosya") / Dur ("şu bitince dur, onay iste") (Dd9HttYsLEX).
3. **Birebir kur kalıbı:** "bölüm, metin, renk uydurma; tek dosya; teslim maddeleri" (DenBDjWiUjR). Ayluna'nın "uydurma yok" kuralıyla aynı.
4. **Tekniğin adını bil.** Adı doğru konan istek doğru sonuç verir. Gece lambasına yakın olanlar: dithering, halftone ay, paper cutout (katmanlı gece göğü), particle (Dei6J0AvlXw, DdD49RLBYdX).
5. **DESIGN.md.**
   - Google'ın açık biçimi: token'lar + 8 bölüm.
   - `TASARIM-BILGISI.md`'den 3 KB'lık bir DESIGN.md türetilirse Claude Design ve öteki ajanlar doğrudan okur.
   - Tek kaynak yine `TASARIM-BILGISI.md` kalır.
6. **Video biçimi:** H.264 MP4 + kapak karesi. HEVC, Android'de ve Instagram tarayıcısında oynamaz (DenBDjWiUjR).
7. **Aşamalı geliştirme:** JS gelmeden animasyonlu öğeler gizlenmez. İlk boyamadan önce `html.js` sınıfı eklenir.
8. **Rakip reklamları:** Meta Reklam Kütüphanesi'nde gece lambası/projektör reklamlarının açılış cümleleri ve teklifleri elle toplanır (DeecRIEDB8q).
9. **Instagram kiti için kurgu dili:**
   - Kelime kelime altyazı (anahtar kelime renkli).
   - Bölüm ilerleme çubuğu.
   - Ölçek + opaklıkla gelen kartlar.
   - Numaralı rozet.
   - Kaynak: DemwcsvI1kW, DeB-J5doS0R, DeecRIEDB8q.

## Güvenlik dersleri
- **"Linki yapıştır, kur":** depo okunmadan kurulur. İki videoda API anahtarı ekranda açık kaldı.
- **Riskli kurulum biçimleri:**
  - `--scope user` ile bilinmeyen sunucuya MCP bağlamak.
  - GitHub dışı bir adresten `npx skills add`.
  - 710 satırı okumadan yapıştırmak.

  Bizim kuralımız aynı kalır: önce klonla, oku, sonra yalnız gerekeni al.

## Göz atmalık ücretsiz siteler
- **Zaten skill'deki referans listesinde:** cta.gallery, footer.design, navbar.gallery, styles.refero.design.
- **Yeni:**
  - supahero.io (hero örnekleri)
  - Realtime Colors (paleti sahte sitede deneme)
  - haikei.app (SVG dalga ayırıcı)
  - eathungrytiger.com (kaydırınca dönen ürün)
  - magic.estudionk.com (hotspot ve sürükle)
  - shopify.com/editions/winter2026

## Ücretli, gerek yok
| Araç | Ücret |
|---|---|
| uiprompts.app | ömür boyu 499 $ |
| vividsites | 25–79 $/ay |
| scrolltide | 29 $/ay |
| HorizonX | 19,99 $/ay |
| scrollhaus | yıllık 159,20 $ |
| 21st.dev Magic | 15–20 $/ay |
| AutoAE | 12 $/ay'dan, ücretsiz planı filigranlı |
| getlayers | yıllık plan |
| MotionSites | — |
| ls.graphics | ürün başı 32–49 $ |
