---
name: "ayluna-tasarim"
description: "Ayluna (ayluna.shop) Shopify sitesi, tema bölümleri, ürün sayfaları, ürün metinleri veya Ayluna görselleri/Instagram kiti üzerinde çalışırken kullan."
---

# Ayluna tasarım kuralları (v2 · 17 Ekim 2026)

Ayluna, Türkiye'de Meta reklamıyla telefondan gelen annelere ve büyükannelere gece lambası, projektör ve nemlendirici satıyor. 15 ürün var; cironun çoğu LunaDream'den geliyor.

**İşe başlamadan:**
1. Depo `bbasar1199/cloud`, dal `ayluna-imza-onizleme`.
2. Sırayla oku: `ayluna-imza/DEVAM.md`, `ayluna-imza/RAPOR.md`, `ayluna-imza/TASARIM-BILGISI.md`.

**Güncel ve seçilmiş tasarım:**
- "Ayluna İmza Tasarım" tuvalindeki `project/Main.dc.html` (https://claude.ai/artifact/CHmRtH4tjbapGmPtuQGsTH).
- Depodaki kopyası: `ayluna-imza/canvas/Main.dc.html`.
- Eski "H yönü / Bricolage + Figtree" bilgisi geçersiz.

## Çalışma biçimi
- Türkçe, kısa yaz. İstenmeyen dosya ya da açıklama yok.
- Tema kodu kopyala-yapıştır `.txt` dosyası olarak verilir. Zip, index ve rehber yalnız istenirse.
- Önce mobil (390px), sonra masaüstü.
- Beğenilen bölüm silinmez, geliştirilir.
- **Her bölüm kararı önce eleştirmen ajana denetletilir.** Ajan kullanıcıyı taklit eder; kişilik tanımı `TASARIM-BILGISI.md` §1a'da. Ajanın en beğendiği 3 fikir kullanıcıya ayrı ayrı gösterilir.
- Her değişiklikten sonra telefon genişliğinde ekran görüntüsü alıp bakılır (`araclar/ekran-goruntusu.js`, `araclar/dc-onizle.js`).
- Kararlar `DEVAM.md`'ye ve tuval notuna yazılır. Kullanıcı yorum bırakmıyor; iz yalnız orada kalır.

## Kullanıcının zevki
- **Sevmez:**
  - emoji ikon
  - çok yazılı, boğucu sayfa
  - "Shopify teması gibi" sıradan düzen
  - tamamen koyu tema
  - uydurma sayı ya da sayaç
  - abartılı efekt, yıldız animasyonu
  - süsle başlayan tasarım
- **Sever:**
  - "acayip ama sıkmayan" tarz
  - doğa gibi uyumlu hareket
  - güven veren, satan sayfa
  - paket
  - ay sonu fiyat sayacı (her ay zam yapıyor)
  - sosyal kanıt
- Alışılmış satış kalıpları (fayda listesi, sayaç, stok, "dün satılan") atılmaz; inceltilir ve gerçek veriye bağlanır.
- Gidişat: büyük ve gösterişliden kompakt ve tanıdığa doğru. Yeni öneri "daha az, daha net" olmalı.

## Tasarım sistemi (Main.dc)
- **Renkler:**
  - krem #F6F1E9 zemin, #FFFDF9 yüzey, #E3D8C7 çizgi
  - lacivert #1A2142 metin ve açık zeminde ana buton
  - gece #141A36 / #0C1027: yalnız ürünün ışığını gösteren bantlarda, yapışkan çubukta ve alt bilgide
  - amber #F2A65A: ışık ve koyu zeminde ana buton; #E59A4C yıldız ve ikon
  - soluk #5C6078 ikincil metin
  - yeşil #2E6B4F: Stokta, %5 rozeti, kartla öde dürtmesi
  - 11px etiket için #766B5B, sayaç için #A05A1C kullan. Eski #8A7F6E ve #B4651F kontrastta kalıyor.
- **Yazı:**
  - Young Serif 400 yalnız başlıkta: H1 50px/.95, H2 30px/1.06.
  - Onest gövde 15px. 16px öneriliyor; kararı kullanıcıda.
  - 12px altı yazı yok. Rakamlar `tabular-nums`.
- **Şekil:**
  - Köşe: levha 28, kart 14–22, buton 16, input 12, çip 999.
  - Kenar boşluğu 16px. Gölge yerine 1px çizgi.
  - Dokunma alanı ≥44px, ana buton 58px.
- **Hareket:**
  - Tek eğri `cubic-bezier(.2,.7,.2,1)`, yalnız transform ve opacity.
  - İmza an "Işığı kapat" anahtarı (oda gündüzden geceye).
  - Yeni sonsuz döngü eklenmez. `prefers-reduced-motion` desteklenir.
- **İkon:** ince çizgili SVG, ilk çizgi amber. Emoji asla.

## Sayfa akışı (ürün sayfası)
1. Gece sahnesi: ışık anahtarı ve galeri.
2. Üstüne binen karar levhası. Sırası:
   - puan ve Stokta, H1
   - 4'lü özellik şeridi
   - Model (küçük stüdyo fotoğraflı kartlar)
   - Paket (1 lamba / 2 lamba "Kardeşe")
   - ince ay sonu şeridi, birlikte al
   - **Ödeme: Kartla öde %5 varsayılan, Kapıda öde ikinci**
   - CTA (tutarı ve seçimi taşır), kapıda formu sayfa içinde
   - güven üçlüsü, müşteri fotoğrafları
3. Bir gece, beş an.
4. Çipli yorumlar.
5. 12 disk.
6. Avucuna sığar ve kutu içeriği.
7. Videolar.
8. 30 gün iade mührü.
9. SSS.
10. Odanın geri kalanı.
11. Kapanış ve dev "Ayluna" alt bilgi.
12. Yapışkan çubuk.

## Gerçekler (uydurma yerine bunlar)
- İade 30 gün (90 değil). Ücretsiz kargo. 1 iş gününde kargoda, 3–7 günde teslim. Kargo takibi Track123.
- LunaDream fiyatları:
  - 1 lamba ₺1.699,99 (karşılaştırma ₺1.999,00)
  - 2 lamba ₺2.749,99 (karşılaştırma ₺3.998,00)
- Diğer fiyatlar:
  - AyFeneri ₺1.649,99 / ₺2.499
  - Galaksi Ambiyans ₺1.499 / ₺2.898
  - Galaxy USB ₺1.599 / ₺1.999
  - Kum Saati ₺799 / ₺999
  - Galaksi Night ₺2.199 / ₺2.999
  - Yıldız Işığı Nemlendirici ₺849,99 / ₺1.099
- Modeller: Kız = tavşanlı, Bluetooth ninni hoparlörlü. Erkek = Uzay Kaşifi robot, hoparlörsüz. Bluetooth vaadi modele bağlanır.
- Kutu: lamba + 6 disk + 6 hediye disk + USB kablo. Unicorn diski kutuda yok; gösterilmez.
- Yorumlar: Burak G., Handan B., Abdülkerim T., Sevcan Z., Mehmet C. Puan Loox'tan çekilir (4,7 · 62, teyit bekliyor). "Elif K.", 2.467, 10.000+ ve 12.000+ uydurmadır.
- Bilinmeyen değer köşeli yer tutucu kalır: [X] cm, [X] saat, [yaş], [Firma unvanı], [numara].

## İş verisi → tasarım kuralı
- Kapıda ödemede iade %28,6, ön ödemede %0,8. İadelerin %92'si "alıcı bulunamadı".
  - Kartla öde varsayılan ve indirimli.
  - Kapıda seçilirse toplam, teslim aralığı ve WhatsApp onayı formda görünür.
  - "Kartla öde, ₺X daha az öde" hatırlatması gösterilir.
- PTT'de iade %40. PTT öne çıkarılmaz.
- Gerçek dönüşüm sipariş ÷ oturum (≈%1,7); Shopify'ın oranı kapıda ödemeyi saymaz. Başarı teslim edilen ciroyla ölçülür.

## Dürüstlük
- Aciliyet yalnız gerçek kurala bağlanır:
  - ay sonu zammı (gerçekten varsa)
  - Shopify stok eşiği
  - Flow ile yazılan "dün satılan"
  - elle girilen sayı tarih taşır, eskiyince gizlenir
- "X kişi bakıyor", sahte geri sayım ve uydurma satış adedi yok.
- Sağlık iddiası ve teyitsiz teknik rakam yok. Sayfa vaadi kutuyla birebir aynı olur.
- Mevzuat ayrıntısı `ayluna-imza/ogrenme/arastirma.md`'de.

## Görsel
- Ürün asla sıfırdan üretilmez. Gerçek fotoğraf referans alınır, sahne ve ışık değişir.
- Araç: Google Flow (Nano Banana Pro). İş akışı DEVAM.md'de.
- Görselde yazı üretilmez; metin HTML'de eklenir.
- Gerçek müşteri fotoğrafı ve videosu önceliklidir.

## Shopify
- Horizon (veya mevcut tema) + Ayluna'ya özel bölümler.
- Kaynak `araclar/shopify-kaynak/*.liquid` → `python3 ayluna-imza/araclar/shopify-derle.py` → `shopify/*.txt`. Kurulum: `shopify/KURULUM.txt`.
- Bölümler Main.dc'ye göre yazılır.
- Bilinen hatalar `TASARIM-BILGISI.md` §8'de.
