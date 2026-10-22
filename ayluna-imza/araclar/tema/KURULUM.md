# Ayluna teması 1.0.15 · kurulum

Zip: `tema-zip/ayluna-SHOPIFY-TEMA-1.0.15.zip` (üretmek için: `python3 araclar/tema/tema_uret.py`).
Tasarım, önizleme sitesindekiyle aynı. Sepet ve ödeme Shopify'ın kendisi; kapıda ödeme EasySell'de.

## 1. Yükle (yayınlamadan)
1. Shopify yönetici → Online Mağaza → Temalar → Tema ekle → **Zip dosyası yükle** → `ayluna-SHOPIFY-TEMA-1.0.15.zip`.
2. Tema "Tema kitaplığı"na düşer. **Yayınla'ya basma.** Önce "…" → **Önizleme** ile gez.
   Yayınlanmamış temayı denemek satışı etkilemez: müşteriler eski temayı görür, sipariş kaçmaz. Uygulamaları da (3. madde) yayınlamadan bu temanın düzenleyicisinde açıp önizlemede denersin.

## 2. Sayfalar (bir kez)
Tasarımlı sayfalar adrese göre açılır. Online Mağaza → Sayfalar'da bu adreslerle **boş** sayfa oluştur (içerik temadan gelir):

| Sayfa adı | Adres (URL ve SEO → handle) |
|---|---|
| İletişim | `iletisim` |
| İade ve değişim | `iade` |
| Kargo ve teslimat | `kargo` |
| Gizlilik ve KVKK | `kvkk` |
| Mesafeli Satış Sözleşmesi | `mesafeli-satis` |
| Ön Bilgilendirme Formu | `on-bilgilendirme` |
| Hizmet şartları | `hizmet-sartlari` |

Menüleri ayrıca kurmana gerek yok; üst menü ve alt bilgi temanın içinde.

## 3. Uygulamalar (yeni temada ayrıca açılır)
Yeni temada uygulama yerleştirmeleri kapalı gelir. Özelleştir → sol altta **Uygulama yerleştirmeleri** (App embeds):
- **Kaching Bundles: aç.** Paket indirimi (2 Adet ₺2.749,99 gibi) buradan gelir. Tema Kaching kutusunu görünmez kurar; müşteri tasarımdaki paket kartını seçince arkada Kaching'deki aynı paket seçilir. Açılışta seçili paket yok (eski temadaki gibi); seçmeden alırsa 1 adet.
  - Ürün bölümüne **Kaching bloğu ekleme**: kutu zaten var, eklersen ikinci kez görünür.
  - Paket fiyatları Kaching'tekiyle aynı (19 Eki'de karşılaştırıldı). Kaching'te fiyat değişirse bana yaz, kartları güncellerim.
- **EasySell (kapıda ödeme): sen koyarsın.** Tema kendi Kapıda düğmesini koymaz. EasySell yerleştirmesini açınca kendi düğmesi "Güvenli Ödeme ile Al" düğmesinin hemen altına gelir. İstersen tema düzenleyicide "Ayluna ürün sayfası" bölümüne EasySell bloğu ekleyebilirsin; o da aynı yere gelir.
  - EasySell formu paket adedini ve indirimi Kaching'ten okur (eski temadaki gibi).
  - Bilinen sınır: LunaDream 2'li pakette iki farklı model (Kız + Erkek) seçilirse kapıda formu iki lambayı da 1. lambanın modeli görür. Kartla ödemede sorun yok (sepete iki ayrı satır, ikisi de indirimli).
  - EasySell'in yapışkan alt düğmesi (sticky) açıksa tasarımın kendi alt çubuğuyla üst üste biner; birini kapat.
- **Loox, Track123:** yerleştirmelerini aç. Yorum kartları tasarımda (gerçek yorumlardan); "Kargo takip" `/apps/track123`'e gider (tema ayarından değişir).
- **Kartla %5 indirim:** Sepette "Kartla toplam" %5 düşük gösterilir. Ödeme sayfasında da bu indirimin uygulandığını denetle (otomatik indirim ya da ödeme sağlayıcısı). Uygulanmıyorsa yayınlama.

## 4. Tema ayarları
Özelleştir → Tema ayarları → Ayluna:
- **Kargo takip adresi:** `/apps/track123`.

## 5. Yayınlamadan önce dene (telefonda ve bilgisayarda)
- [ ] Ana sayfa, Tüm ürünler, 4 imza ürün (LunaDream, Galaxy USB, AyFeneri, Galaksi Night) ve 2 sade ürün açılıyor.
- [ ] Fiyatlar mağazadakiyle aynı. Ürün sayfasındaki tasarım fiyatı mağaza fiyatından farklıysa tema düzenleyicide "Uyarı: bu sayfadaki fiyat…" yazar; o zaman temayı yeniden üretmem gerekir.
- [ ] Ürün sayfası açılışta hiçbir paket seçili değil.
- [ ] LunaDream: 2 Adet + model seç → Güvenli Ödeme → sepette doğru model ve adet, ödeme sayfasında toplam ₺2.749,99 (Kaching indirimi).
- [ ] 2 Adet seç → EasySell düğmesi → formda 2 adet ve ₺2.749,99 + ₺80 kapıda ücreti.
- [ ] Telefonda sayfa ekrana tam sığıyor (yana kaymıyor). Sığmıyorsa ekran görüntüsünü bana gönder.
- [ ] Sepet: adet değiştir, sil, "Siparişine özel" ekle-çıkar; rozet adedi doğru.
- [ ] İletişim formu ve bülten kaydı yönetimde görünüyor (Müşteriler / E-posta). Bültende vaat edilen %5 kodu gerçekten gidiyor mu?
- [ ] Şirket bilgisi (ticaret unvanı, adres, MERSİS, KEP, telefon) sitede şimdilik yok (senin isteğin, 19 Eki). Mesafeli Satış, Ön Bilgilendirme ve KVKK'da satıcı bilgisi yasal zorunluluk: **eklemeden yayınlama.** WhatsApp da yok; eklemek istediğinde bana yaz.
- [ ] Meta/TikTok pikseli ve Google etiketleri (uygulama ya da Müşteri etkinlikleri) yeni temada da çalışıyor.

## 6. Bu sürümün sınırları (sonraki sürüm)
- Ürün sayfalarındaki metin ve paket fiyatları tasarımdan gelir (tema düzenleyiciden değişmez). Fiyat/metin değişince temayı ben yeniden üretirim.
- Ürün galerileri tema dosyasındaki görsellerdir (mağazadaki ürün görsellerinin kopyası). Shopify'da ürün görseli değişirse galeri değişmez.
- Yeni eklenen bir ürün sade bir sayfayla açılır (görsel, fiyat, sepete ekle); tasarımlı sayfası için bana yaz.
- Hızlı Kargo seçimi sepette yok; kargo seçeneği Shopify ödeme sayfasında seçilir (Hızlı Kargo bir kargo ücreti olarak tanımlı olmalı).
