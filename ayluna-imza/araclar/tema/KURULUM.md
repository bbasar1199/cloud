# Ayluna teması 1.0.33 · kurulum

Zip: `tema-zip/ayluna-SHOPIFY-TEMA-1.0.33.zip` (üretmek için: `python3 araclar/tema/tema_uret.py`).
Tasarım, önizleme sitesindekiyle aynı. Sepet ve ödeme Shopify'ın kendisi. Ödeme yalnız kartla; kapıda ödeme yok (27 Eki).

## 1. Yükle (yayınlamadan)
1. Shopify yönetici → Online Mağaza → Temalar → Tema ekle → **Zip dosyası yükle** → `ayluna-SHOPIFY-TEMA-1.0.33.zip`.
2. Tema "Tema kitaplığı"na düşer. **Yayınla'ya basma.** Önce "…" → **Önizleme** ile gez.
   Yayınlanmamış temayı denemek satışı etkilemez: müşteriler eski temayı görür, sipariş kaçmaz. Uygulamaları da (3. madde) yayınlamadan bu temanın düzenleyicisinde açıp önizlemede denersin.

## 1b. Ürün şablonlarını ata (1.0.33, bir kez)
Dört ürünün kendi şablonu var; her bölümü ayrı düzenlenebilsin diye. Ürünler → ürünü aç → sağda **Tema şablonu**:

| Ürün | Tema şablonu |
|---|---|
| LunaDream Gece Lambası (`lunadream-gece-lambasi`) | `lunadream` |
| Galaxy USB Projektör (`galayx-usb-projektor`) | `galaxy-usb` |
| AyFeneri (`lamba`) | `ayfeneri` |
| Galaksi Night Projektör (`ayluna-galaksi-night-projektor`) | `galaksi-night` |

Diğer bütün ürünler **Varsayılan ürün** şablonunda kalır (ortak 6 bölüm, her ürün kendi tasarımıyla). Atamayı yapmasan da sayfa açılır
(tek parça hâliyle), ama bölümler ayrı görünmez.

## 1c. Bölümler (1.0.33)
- Özelleştir'de ana sayfa ve her ürün şablonu bölüm bölüm görünür (Üst kısım, Galeri ve satın alma, İçin rahat olsun, …).
  Bölümün yazıları ve görselleri sağdaki ayarlarda; görsel seçmezsen tasarımdaki görsel kalır.
- **Bölümü silme, gizle** (göz simgesi): silinen bölüm "Bölüm ekle" listesinde yok, geri eklenemez. Sürükleyerek sırası değişir.
- **Loox:** yorum bölümünde ("Alanlar ne diyor?" / "Aileler ne diyor?") → **Blok ekle → Uygulamalar → Loox**. Loox o başlığın altında görünür.
  İstersen herhangi bir yere **Bölüm ekle → Uygulama bloğu** ekleyip Loox'u oraya koy. LunaDream'deki tasarım yorum kartlarını istemezsen
  "Aileler ne diyor?" bölümünü gizle, yerine Uygulama bloğu ekle. Loox bloğu eklenmeyen yorum yer tutucusu sayfada görünmez.
- **Videolar (LunaDream):** önce İçerik → Dosyalar'a videoları yükle. Sonra LunaDream şablonu → **Videolar** bölümü → **Blok ekle → Video** →
  videoyu seç, başlık ve alt yazıyı yaz. Video eklenmezse bölüm görünmez. Sayfada ekrandayken sessiz döner, dokununca sesli ve tam ekran açılır.
- **Galeri:** ürün galerileri Shopify'daki ürün görsellerinden gelir (ürüne görsel ekle/sırala, sayfa aynen gösterir).
  Tema ayarları → Ayluna → "Ürün galerisi Shopify'daki ürün görsellerinden gelsin" kapatılırsa tasarımdaki galeri kullanılır.

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
  - "Galeri ve satın alma" bölümüne **Kaching bloğu ekleme**: kutu zaten var, eklersen ikinci kez görünür.
  - Paket fiyatları Kaching'tekiyle aynı (19 Eki'de karşılaştırıldı). Kaching'te fiyat değişirse bana yaz, kartları güncellerim.
- **Kapıda ödeme yok (27 Eki).** Temada kapıda düğmesi, formu ya da yazısı yok. **EasySell'in yerleştirmesini kapat** (Uygulama yerleştirmeleri) ya da uygulamayı kaldır; açık kalırsa kendi "Kapıda Ödeme" düğmesini sayfaya ekler. Shopify ödeme ayarlarında "Kapıda ödeme (COD)" yöntemi açıksa onu da kapat.
- **Loox, Track123:** yerleştirmelerini aç. Yorum kartları tasarımda (gerçek yorumlardan); "Kargo takip" `/apps/track123`'e gider (tema ayarından değişir).
- **Loox yorumları:** 1c'deki gibi yorum bölümüne blok olarak eklenir.
- **Dün satılan ve "Son N adet" (27 Eki):** Ayarlar → Özel veriler → Ürünler → Tanım ekle: `ayluna.dun_satis` ("Dün satılan", tam sayı) ve `ayluna.stok_kurdele` ("Stok kurdelesi", tam sayı). Her ürünün sayfasında sayıyı elle yaz. Boş bırakırsan tasarımdaki sayı kalır (LunaDream: Dün 62, Son 18; Galaxy USB: Dün 62, Son 23); **0** yazarsan satır hiç görünmez.
- **Kartla %5 indirim:** Sepette "Kartla toplam" %5 düşük gösterilir. Ödeme sayfasında da bu indirimin uygulandığını denetle (otomatik indirim ya da ödeme sağlayıcısı). Uygulanmıyorsa yayınlama.

## 4. Tema ayarları
Özelleştir → Tema ayarları → Ayluna:
- **Kargo takip adresi:** `/apps/track123`.

## 5. Yayınlamadan önce dene (telefonda ve bilgisayarda)
- [ ] Ana sayfa, Tüm ürünler, 4 imza ürün (LunaDream, Galaxy USB, AyFeneri, Galaksi Night) ve 2 sade ürün açılıyor.
- [ ] Fiyatlar mağazadakiyle aynı. Ürün sayfasındaki tasarım fiyatı mağaza fiyatından farklıysa tema düzenleyicide "Uyarı: bu sayfadaki fiyat…" yazar; o zaman temayı yeniden üretmem gerekir.
- [ ] Ürün sayfası açılışta hiçbir paket seçili değil.
- [ ] LunaDream: 2 Adet + model seç → Güvenli Ödeme → sepette doğru model ve adet, ödeme sayfasında toplam ₺2.749,99 (Kaching indirimi).
- [ ] Ürün sayfasında, sepette ve ödeme sayfasında hiçbir yerde "Kapıda" yazmıyor (EasySell kapalı).
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
