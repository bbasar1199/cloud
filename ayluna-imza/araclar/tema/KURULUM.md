# Ayluna teması 1.0.0 · kurulum

Zip: `tema-zip/ayluna-tema-1.0.0.zip` (üretmek için: `python3 araclar/tema/tema_uret.py`).
Tasarım, önizleme sitesindekiyle aynı. Sepet ve ödeme Shopify'ın kendisi; kapıda ödeme EasySell'de.

## 1. Yükle (yayınlamadan)
1. Shopify yönetici → Online Mağaza → Temalar → Tema ekle → **Zip dosyası yükle** → `ayluna-tema-1.0.0.zip`.
2. Tema "Tema kitaplığı"na düşer. **Yayınla'ya basma.** Önce "…" → **Önizleme** ile gez.

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

## 3. Uygulamalar
- **EasySell (kapıda ödeme):** Ayarlar → düğme/özel seçici alanına `[data-ay-kapida]` yaz. Ürün sayfasında ve sepette aç. EasySell'in kendi düğmesini gizle (tasarımdaki "Kapıda Ödeme ile Sipariş Ver" düğmesi formu açar). Seçilen model ve paket adedi gizli ürün formuna yazılır, EasySell oradan okur.
  - Bilinen sınır: LunaDream 2'li pakette iki farklı model (Kız + Erkek) seçilirse EasySell formu tek varyant görür. Kartla ödemede sorun yok (sepete iki ayrı satır gider).
- **Paket fiyatları (2 adet ₺2.749,99 gibi):** Sayfadaki paket fiyatları, Kaching Bundles'taki ya da otomatik indirimdeki fiyatla **aynı olmalı**. Önizlemede 2 adet sepete koy, sepette ve ödeme sayfasında aynı toplamı gördüğünü denetle. Tutmuyorsa yayınlama, bana yaz.
- **Kartla %5 indirim:** Sepette "Kartla toplam" %5 düşük gösterilir. Ödeme sayfasında da bu indirimin uygulandığını denetle (otomatik indirim ya da ödeme sağlayıcısı). Uygulanmıyorsa yayınlama.
- **Loox:** Yorum kartları tasarımda (gerçek yorumlardan). Loox yıldız/sayı bileşeni bu sürümde bağlı değil.
- **Track123:** "Kargo takip" `/apps/track123`'e gider (tema ayarından değişir).

## 4. Tema ayarları
Özelleştir → Tema ayarları → Ayluna:
- **WhatsApp bağlantısı:** `https://wa.me/905XXXXXXXXX` (boşsa WhatsApp düğmeleri numara yok uyarısı verir).
- **Kargo takip adresi:** `/apps/track123`.

## 5. Yayınlamadan önce dene (telefonda ve bilgisayarda)
- [ ] Ana sayfa, Tüm ürünler, 4 imza ürün (LunaDream, Galaxy USB, AyFeneri, Galaksi Night) ve 2 sade ürün açılıyor.
- [ ] Fiyatlar mağazadakiyle aynı. Ürün sayfasındaki tasarım fiyatı mağaza fiyatından farklıysa tema düzenleyicide "Uyarı: bu sayfadaki fiyat…" yazar; o zaman temayı yeniden üretmem gerekir.
- [ ] LunaDream: model + paket seç → Güvenli Ödeme → sepette doğru model ve adet → Shopify ödeme sayfası.
- [ ] Kapıda Ödeme düğmesi EasySell formunu açıyor; formda doğru ürün/adet; ₺80 kapıda ücreti doğru.
- [ ] Sepet: adet değiştir, sil, "Siparişine özel" ekle-çıkar; rozet adedi doğru.
- [ ] İletişim formu ve bülten kaydı yönetimde görünüyor (Müşteriler / E-posta). Bültende vaat edilen %5 kodu gerçekten gidiyor mu?
- [ ] Politika sayfalarındaki köşeli yer tutucular ([Ticaret unvanı], MERSİS, adres, KEP, telefon) dolduruldu. **Dolmadan yayınlama** (yasal zorunluluk).
- [ ] Meta/TikTok pikseli ve Google etiketleri (uygulama ya da Müşteri etkinlikleri) yeni temada da çalışıyor.

## 6. Bu sürümün sınırları (sonraki sürüm)
- Ürün sayfalarındaki metin ve paket fiyatları tasarımdan gelir (tema düzenleyiciden değişmez). Fiyat/metin değişince temayı ben yeniden üretirim.
- Ürün galerileri tema dosyasındaki görsellerdir (mağazadaki ürün görsellerinin kopyası). Shopify'da ürün görseli değişirse galeri değişmez.
- Yeni eklenen bir ürün sade bir sayfayla açılır (görsel, fiyat, sepete ekle); tasarımlı sayfası için bana yaz.
- Hızlı Kargo seçimi sepette yok; kargo seçeneği Shopify ödeme sayfasında seçilir (Hızlı Kargo bir kargo ücreti olarak tanımlı olmalı).
