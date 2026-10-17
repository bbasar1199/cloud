# "5 eklenti" rehberi (@esadcom) · bu ortama uyarlama (17 Ekim 2026)

Kullanıcı rehberi paylaştı ve "öğren, kendine ekle" dedi. Her eklentinin işlevine bakıldı ve bulut ortamına uygun karşılığı kuruldu.

| Eklenti | Ne yapıyor | Bu ortamda | Karar |
|---|---|---|---|
| Omniroute | Limit dolunca başka yapay zekâ sağlayıcılarına geçiyor | Bulut oturumunda model değiştirilemiyor. Mağaza ve müşteri verisi üçüncü taraflara gider. | Kurulmadı |
| Claude Mem | Oturumlar arası hafıza | Konteyner her oturumda silinir; yerel hafıza kaybolur. Hafıza depoda tutuluyor: `CLAUDE.md`, `DEVAM.md`, `TASARIM-BILGISI.md`. | Depo hafızasıyla karşılandı |
| Headroom | Bağlamı kırpıp token tasarrufu | Oturum bağlamı kendiliğinden özetliyor. Büyük okumalar alt ajanlara veriliyor. | Gerek yok |
| Claude Code setup | Depoyu tarayıp eksik hook, beceri, MCP ve ajanı öneriyor | Anthropic'in resmi eklentisi, katalogda var; kurulum kartı gösterildi. Yöntemi uygulandı: `ayluna-imza/CLAUDE.md`, `.claude/agents/ayluna-elestirmen.md`. | Uygulandı |
| Task Observer | Düzeltmeleri izleyip becerileri yeniden yazıyor | Bulutta arka plan izleyici yok. Aynı işi `TASARIM-BILGISI.md` §10 "Düzeltme günlüğü" kuralı yapıyor. | Kuralla karşılandı |

Sonraki adım önerileri (kullanıcı isterse):
- **Hook:** `shopify-kaynak/*.liquid` değişince `shopify-derle.py` kendiliğinden çalışsın. `shopify/*.txt` elle düzenlenmesin.
- **Ana dal:** `CLAUDE.md` ve `.claude/agents/` ana dala da alınsın. Yeni oturumda kendiliğinden yüklenirler.

---

# İki gönderiden eklentiler (17 Ekim 2026)

Kullanıcı iki gönderi paylaştı:
- "Claude Code uygulama öncesi 4 GitHub reposu" (yapaytu.com)
- @emreative'in "Claude'a yaptırdığın her site aynı mı görünüyor?" reel'i (gönderide bağlantı yok; adlar README'lerden eşlendi)

Kullanıcı "özellikle tasarım tarafı kurulsun" dedi. Her depo klonlandı ve okundu (kancalar, betikler, ağ çağrıları, lisans).

| Depo | Ne yapıyor | Karar | Neden |
|---|---|---|---|
| emilkowalski/skills | Animasyon ve mobil arayüz kuralları | **Kuruldu** (mobile-native, animation-performance, break-ui, review-animations) | Yalnız metin, kanca yok, Ayluna kurallarıyla uyumlu (transform/opacity, reduced-motion, input ≥16px) |
| pbakaus/impeccable | Tasarım yönetmeni skill'i + 24 alt komut + Rust dedektör | **Yalnız skill ve reference kuruldu**, komutla çalışır | Plugin hâli her düzenlemede kanca çalıştırır, program indirir, telemetri varsayılan açık. Dedektör krem zemini ve ikon kartlarını işaretler. |
| Leonxlnx/taste-skill | "Anti-slop" sanat yönetimi | **Çekirdek ve redesign kuruldu**, komutla çalışır | Ev kuralları seçilmiş tasarımla çelişir: krem yasak, 1px çizgi yasak, ikonlu kart yasak, büyük yazı. |
| microsoft/playwright-mcp | Claude sayfayı tarayıcıda açıp bakar | **Kuruldu** (`.mcp.json`, sürüm 0.0.82) | Yerel Chromium, 390×844 |
| Figma MCP | Figma tasarımlarını okur | Eklenti zaten var | Figma hesabı yetkilendirmesi gerekiyor (claude.ai bağlayıcı ayarı) |
| DietrichGebert/ponytail | Kod sadeleştirme kuralları + maliyet bandı | Kurulmadı | Her oturum ve her alt ajanda ~1–1,5k token; her turda dosya yazar. İş tasarım. |
| addyosmani/agent-skills | 25 genel mühendislik skill'i | Kurulmadı (tema aşamasında `frontend-ui-engineering`, `performance-optimization` alınabilir) | Her oturum ~3k token, çoğu backend/CI |
| chaseai-yt/claudex-loop | Claude + Codex çapraz denetim | Kurulmadı | Codex CLI ve OpenAI hesabı gerekir; kod üçüncü sağlayıcıya gider |
| Graphify-Labs/graphify | Projeyi bilgi grafiğine çevirir | Kurulmadı | Her okuma/aramada kanca, genel CLAUDE.md'ye yazar, Liquid desteği yok, proje küçük |

