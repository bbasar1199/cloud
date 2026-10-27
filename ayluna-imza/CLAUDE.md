# Ayluna · proje notu (Claude bu dosyayı kendiliğinden okur)

Ayluna (ayluna.shop) Shopify mağazasının LunaDream ürün sayfası ve tema bölümleri. Dal: `ayluna-imza-onizleme`.

## İlk iş
1. `DEVAM.md`, `RAPOR.md` ve `TASARIM-BILGISI.md`'yi baştan sona oku.
2. Son durumu 5 maddede özetle, sıradaki işi sor.

## Kurallar
- Türkçe konuş, kısa yaz.
- Emoji ikon, uydurma sayı ve boğucu yazı yok.
- Mobil önce (390px).
- Shopify kodu kopyala-yapıştır `.txt` olarak verilir (`shopify/`).
- Seçilen tasarım `canvas/Main.dc.html`. Shopify bölümleri buna göre yazılır.
- Ödeme: yalnız kartla (%5 indirim). Kapıda ödeme yok (kullanıcı, 27 Eki).
- Teyitsiz bilgi köşeli yer tutucu kalır: [X] cm.

## Tasarım kararı süreci (hata düzeltmede gerekmez)
1. Taslağı yap.
2. Ekran görüntüsü al ve bak (`araclar/ekran-goruntusu.js` ya da `araclar/dc-onizle.js`).
3. `ayluna-elestirmen` ajanına denetlet (`.claude/agents/ayluna-elestirmen.md`).
4. Eleştirmenin en beğendiği 3 fikri kullanıcıya ayrı ayrı göster.
5. Kararı `DEVAM.md`'ye yaz.

## Öğrenme döngüsü
Kullanıcı bir şeyi düzeltirse ya da beğenmezse, aynı turda iki şey yap:
- `TASARIM-BILGISI.md` → "Düzeltme günlüğü"ne tarih, ne dedi ve çıkan kural olarak bir satır ekle.
- Kalıcı bir kuralsa `beceriler/` altındaki ilgili SKILL.md'ye ekle. Kullanıcıya claude.ai'deki beceriyi güncellemesini hatırlat.

Aynı düzeltme ikinci kez gelmemeli.

## Hafıza
- Bulut oturumu kapanınca konteyner silinir. Kalıcı hafıza yalnız bu depodaki dosyalardır.
- Önemli her karar commit'lenip `ayluna-imza-onizleme` dalına gönderilir.
