# Proje becerileri (tasarım eklentileri)

Kaynaklar GitHub'dan alındı, incelendi, yalnız metin dosyaları kopyalandı. Kanca, program, betik ve telemetri yok.

| Beceri | Kaynak | Lisans | Çalışma |
|---|---|---|---|
| mobile-native | emilkowalski/skills | MIT | kendiliğinden |
| animation-performance | emilkowalski/skills | MIT | kendiliğinden |
| break-ui | emilkowalski/skills | MIT | kendiliğinden |
| review-animations | emilkowalski/skills | MIT | yalnız `/review-animations` |
| impeccable | pbakaus/impeccable (yalnız skill + reference; `scripts/` program yok) | Apache-2.0 | yalnız `/impeccable <komut>` |
| design-taste-frontend | Leonxlnx/taste-skill | MIT | yalnız `/design-taste-frontend` |
| redesign-existing-projects | Leonxlnx/taste-skill | MIT | yalnız `/redesign-existing-projects` |
| frontend-design | anthropics/skills | Apache-2.0 | yalnız `/frontend-design` |
| web-design-guidelines | vercel-labs/agent-skills + web-interface-guidelines (kurallar yerel `rules.md`, ağdan çekilmez) | MIT | kendiliğinden |
| make-interfaces-feel-better | jakubkrehel/make-interfaces-feel-better | MIT | kendiliğinden |

Ajan ve komut (OneRedOak/claude-code-workflows, MIT; Ayluna'ya uyarlandı):
- `.claude/agents/design-review.md`: teknik denetçi. Mobil önce açar; erişilebilirlik, duyarlı düzen, konsol, tutarlılık. Dosya değiştirmez, Türkçe rapor verir. Zevk/satış kararı `ayluna-elestirmen`'in işidir.
- `.claude/commands/design-review.md`: `/design-review [hedef]` bekleyen değişikliği bu ajana denetletir.

**Öncelik:** Ayluna işinde `ayluna-imza/TASARIM-BILGISI.md` ve `ayluna-imza/beceriler/ayluna-tasarim/SKILL.md` her zaman önce gelir. Bu eklentilerin önerileri yalnız öneridir.

Bilinen çelişkiler:
- Taste ve Impeccable krem zemini, 1px çizgili kartları ve ikonlu özellik kartlarını "kalıp" sayar. Ayluna'da bunlar kullanıcının seçimi; değiştirilmez.
- Taste yazıyı büyük kurmayı önerir. Kullanıcı büyük yazıyı iki kez düzeltti; ölçek v3 geçerli.
- Emil'in ve make-interfaces-feel-better'ın kendi yumuşatma eğrileri var (`ease-out`, `cubic-bezier(0.2, 0, 0, 1)`). Ayluna'nın tek eğrisi `cubic-bezier(.2,.7,.2,1)`.
- make-interfaces-feel-better giriş ve ikon geçişinde `blur` önerir. Ayluna'da yalnız transform/opacity canlandırılır.
- frontend-design "krem zemin + yüksek kontrastlı serif"i yapay zekâ izi sayar. Ayluna'nın krem + Young Serif kararı kullanıcının; değiştirilmez. Bu yüzden yalnız elle çağrılır.
- Vercel kuralları başlık/butonda Title Case ve ikinci tekil şahıs ister. Türkçe metin cümle düzeninde yazılır; marka sesi "biz" der.
- Bu eklentilerin ve denetçilerin bulguları da eleştirmen önerileri gibi toplu uygulanmaz; kullanıcı seçer.

Kurulmayanlar ve nedeni: `ayluna-imza/ogrenme/eklenti-rehberi.md`.
