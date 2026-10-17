---
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git log:*), Read, Grep, Glob, Task
description: Bekleyen değişikliklerin tasarım denetimi (design-review ajanıyla)
argument-hint: "[denetlenecek dosya ya da sayfa]"
---

<!-- Kaynak: OneRedOak/claude-code-workflows design-review komutu (MIT). Ayluna'ya uyarlandı. -->

GIT DURUMU:

```
!`git status --short`
```

SON COMMITLER:

```
!`git log --oneline -5`
```

COMMITLENMEMİŞ DEĞİŞİKLİKLER:

```
!`git diff --stat HEAD`
```

Denetlenecek hedef: $ARGUMENTS (boşsa yukarıdaki değişen arayüz dosyaları; Ayluna'da varsayılan `ayluna-imza/canvas/LunaDreamBPlus.dc.html`).

GÖREV:
`design-review` ajanını çalıştır ve hedefi denetlet. Ajan önce `ayluna-imza/TASARIM-BILGISI.md` ile `ayluna-imza/beceriler/ayluna-tasarim/SKILL.md`'yi okusun; bu kurallar genel tasarım kurallarından önce gelir.

Kullanıcıya yalnız ajanın Türkçe raporunu ver. Bulguları uygulama; kullanıcı hangilerini istediğini seçer.
