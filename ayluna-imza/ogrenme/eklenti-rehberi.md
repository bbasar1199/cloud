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
