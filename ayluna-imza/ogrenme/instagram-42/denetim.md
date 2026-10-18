# Aday araç denetimi (18 Ekim 2026)

Reel'lerde adı geçen ve kurulu olmayan araçlar kurulmadan incelendi. Depolar klonlanıp okundu. Hiçbir betik ya da npm/npx kurulum komutu çalıştırılmadı. Yalnız Chrome DevTools MCP ve Playwright MCP, yerel bir sınama sayfasında denendi.

| Ad | Gerçekte ne | Lisans | Risk | Ayluna | Karar |
|---|---|---|---|---|---|
| Chrome DevTools MCP (`chrome-devtools-mcp@1.11.0`) | Playwright'ta olmayanlar: performans izi, LCP/CLS, ağ ve CPU yavaşlatma, Lighthouse | Apache-2.0 | Kullanım istatistiği varsayılan açık (`--no-usage-statistics` ile kapanır). İz adresleri CrUX'a gider (`--no-performance-crux` ile kapanır). Root'ta `--no-sandbox` gerekir. postinstall betiği yok. | Yüksek: trafik telefondan geliyor | **Kur.** Konteynerde denendi: 32 araç, performans izi çalıştı. `.mcp.json` onayı bekliyor. |
| Playwright MCP (kurulu) | — | Apache-2.0 | Root'ta sandbox hatasıyla açılmıyordu | — | **Düzelt:** `--no-sandbox` ekle. Denendi, çalışıyor. `.mcp.json` onayı bekliyor. |
| transitions.dev (Jakubantalik) | 35 saf CSS geçiş tarifi, hepsinde reduced-motion | Özel: kendi sitende serbest, koleksiyonu yeniden yayımlamak yasak | SKILL.md 26 KB, geniş tetikleyici, "aynen yapıştır" diyor. Depodaki CLI'da giriş ve LLM aktarıcısı var. | Orta: 19/35 tarif blur kullanıyor; akordeon/sekme `grid-template-rows`/`width` canlandırıyor | **Kurulmadı.** Lisans depoya kopyalamayı riskli kılıyor; Emil skill'leriyle örtüşüyor. Fikir olarak bakılabilir. |
| ux-designer-skill (szilu) | Genel UX kural kitabı (WCAG 2.2, form, mobil, karanlık kalıplar) | MIT | Kanca/ağ yok. SKILL.md 16 KB, kendiliğinden tetiklenir. | Orta: design-review ile örtüşür; "gövde ≥16px" ölçek v3'e ters | **Kurulmadı.** Dürüst sayaç/stok bölümü okunmaya değer. |
| prompt-master (nidhinjs) | Başka yapay zekâ araçlarına prompt yazar | MIT | Yalnız metin, 33 KB | Düşük | Kurulmadı. Dört alanlı istek kalıbı (Hedef/Çıktı/Kapsam/Dur) elle kullanılır. |
| app-store-screenshots | Next.js + React + Tailwind editör kurar | MIT | 65 KB SKILL.md, paket kurulumu, betik | Yok | Kurulmadı |
| Google Stitch MCP | Gemini ile metinden ekran üretir (HTML/Tailwind) | Google Labs | API anahtarı gerekir. Claude Code başlığı yok sayıp OAuth deniyor (bilinen hata). Veri Google'a gider. | Düşük: Claude Design aynı işi yapıyor | Kurulmadı |
| Refero Styles | Marka sitelerinden 2.000+ DESIGN.md | Belirtilmemiş | Resmî MCP yalnız Pro'da (~10–14 $/ay) | Düşük | Yalnız fikir |
| AutoAE (autoae.online) | Şablondan MP4 hareketli grafik | CLI MIT, GitHub'da kaynak yok | Skill talimatı her seferinde siteden çekiliyor (uzaktan değişebilir). `npx @autoae/cli` çalıştırır, `~/.autoae`'ye kimlik yazar, medyayı yükler. Ücretsiz plan filigranlı, ticari kullanım kapalı; ücretli 12 $/ay'dan. | Yok | **Kurulmamalı** |
| vividsites | 3D/shader site şablonları, prompt kütüphanesi | Belirtilmemiş | MCP (`vividsites.app/api/connector`) API anahtarı ister, yalnız ücretli planda (25–79 $/ay) | Ters: Three.js/React | Kurulmadı |
| 21st.dev Magic MCP | React + shadcn + Tailwind bileşen üretir | İstemci MIT | API anahtarı, kod 21st.dev'e gider, 15–20 $/ay | Ters | Kurulmadı |
| scrollhaus MCP | Animasyonlu şablon/bileşen | — | Bilinmeyen bir Supabase sunucusuna `--scope user` ile bağlanır; yıllık 159,20 $ | Ters | **Kurulmamalı** |
| Remotion skills (remotion-dev/skills) | 12 skill, React ile kodla video | Skill deposunda LICENSE yok. Remotion 3 çalışana kadar ücretsiz, üstü şirket lisansı (25 $/koltuk/ay) | npm paketi ve Chrome indirir | Reel için uygun, tema için değil | Skill şimdilik kurulmadı. Remotion'ın kendisi projede zaten var (`araclar/remotion`, 4.0.300); lisans koşulu oraya da geçerli. |
| Competitor Ads Extractor | ComposioHQ/awesome-claude-skills; kod yok, Meta Reklam Kütüphanesi kazımayı tarif ediyor | Apache-2.0 | Kazıma Meta koşullarına takılabilir | Elle yapılabilir | Yalnız fikir |
| Voice DNA | Depo bulunamadı; yalnız bir blogda kavram | Doğrulanamadı | — | Marka sesi SKILL.md'de var | Kurulmadı |
| Haikei (haikei.app) | SVG dalga/blob üreten web aracı | Ticari kullanım serbest, atıf yok | Kurulum yok | İyi, ölçülü kullanılırsa | Sitede elle kullanılır |

## DESIGN.md standardı
- Kaynak: google-labs-code/design.md (Apache-2.0, alfa). Başta YAML token'lar (colors, typography, rounded, spacing, components), ardından sekiz bölüm: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts. Hareket bölümü yok ama `## Motion` gibi ek bölümler korunur.
- Koleksiyon: VoltAgent/awesome-design-md (MIT), 84 marka. Başka markaların sistemleri Ayluna'ya alınmaz; yalnız biçim örnek.
- Ayluna için: `TASARIM-BILGISI.md`'den türetilmiş ~3 KB'lık bir DESIGN.md mantıklı (token'lar + `## Motion` + yasaklar). Tek kaynak `TASARIM-BILGISI.md` kalır.

## Bekleyen `.mcp.json` değişikliği
Otomatik izin sistemi Claude'un kendi ayar dosyasını değiştirmesine izin vermedi. Kullanıcı onaylarsa yazılacak hâli:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@0.0.82", "--headless", "--isolated", "--no-sandbox",
               "--viewport-size", "390x844", "--executable-path", "/opt/pw-browsers/chromium"]
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@1.11.0", "--headless", "--isolated",
               "--executable-path", "/opt/pw-browsers/chromium", "--chrome-arg=--no-sandbox",
               "--viewport", "390x844", "--no-usage-statistics", "--no-performance-crux"],
      "env": { "CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS": "1" }
    }
  }
}
```

Not: Playwright MCP `file://` adresini açmaz; sayfa yerel sunucudan açılır (`python3 -m http.server`). Çıktısını çalıştığı klasöre `.playwright-mcp/` olarak yazar.
