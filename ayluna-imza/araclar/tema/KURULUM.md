# Ayluna teması 1.0.36 · kurulum

Zip: `tema-zip/ayluna-SHOPIFY-TEMA-1.0.36.zip` (üretmek için: `python3 araclar/tema/tema_uret.py`).
Tasarım, önizleme sitesindekiyle aynı. Sepet ve ödeme Shopify'ın kendisi. Ödeme kartla ya da EasySell ile kapıda.

## 1. Yükle (yayınlamadan)
1. Shopify yönetici → Online Mağaza → Temalar → Tema ekle → **Zip dosyası yükle** → `ayluna-SHOPIFY-TEMA-1.0.36.zip`.
2. Tema "Tema kitaplığı"na düşer. **Yayınla'ya basma.** Önce "…" → **Önizleme** ile gez.
   Yayınlanmamış temayı denemek satışı etkilemez: müşteriler eski temayı görür, sipariş kaçmaz. Uygulamaları da (3. madde) yayınlamadan bu temanın düzenleyicisinde açıp önizlemede denersin.

## 1b. Bölümler ve bloklar (1.0.36; şablon ataması gerekmez)
- Bütün ürünler **Varsayılan ürün** şablonunda kalır. Önceki sürümde anlatılan şablon atamasını yaptıysan geri al (ürün → Tema şablonu → Varsayılan ürün).
- Özelleştir → üstten Ürünler → Varsayılan ürün → önizlemede ürünü seç (LunaDream, Galaxy USB, …). Solda o ürünün bölümü açılır:
  **LunaDream sayfası**, **Galaxy USB sayfası**, **AyFeneri sayfası**, **Galaksi Night sayfası**, **Diğer ürünler sayfası**. Her bölüm yalnız kendi
  ürününde görünür (diğerleri o üründe boş durur, dokunma).
- Bölümün içindeki **bloklar** sayfanın parçalarıdır (Üst kısım, Galeri ve satın alma, İçin rahat olsun, …). Bloğa tıkla: yazılar ve görseller
  sağda. Sürükle: sıra değişir. Göz simgesi: gizlenir. Silersen **Blok ekle** listesinden geri eklenir. Görsel seçmezsen tasarımdaki kalır.
- Ana sayfa (Özelleştir → Ana sayfa) parça parça bölüm.
- **Loox:** Loox'un uygulama yerleştirmesi (App embeds → Loox) açıkken yorumlar kendiliğinden tasarımın yorum bölümünde çıkar
  (LunaDream'de "Aileler ne diyor?", diğerlerinde "Alanlar ne diyor?" altında). Blok eklemen gerekmez; **ürün bölümüne ayrıca Loox bloğu ekleme**, iki kez görünür.
- **Videolar (LunaDream):** ürünün kendi sayfasında (Ürünler → LunaDream → Medya) video yükle. Sayfadaki video bölümü ürünün videolarını gösterir:
  ekrandayken sessiz döner, dokununca sesli ve tam ekran açılır. Ürünün videosu yoksa bölüm tasarımdaki fotoğraflarla görünür; video ekleyince fotoğrafların yerini alır. Ürüne yüklemek istemezsen: Özelleştir → LunaDream sayfası → "Işık kapanınca ne oluyor" bloğu → Video 1-4. Videonun "alternatif metni" başlık olur.
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
- **EasySell (kapıda ödeme): yerleştirmesi açık kalsın.** Düğmesi ürün sayfasında "Güvenli Ödeme ile Al"ın altına kendiliğinden gelir. Tema, müşterinin seçtiği modeli ve paketi EasySell'e verir: form açılınca sepette yalnız o seçim olur (model değiştirince eskisi kalmaz; 2'li pakette Erkek + Kız ayrı satır). EasySell'in yapışkan düğmesi açıksa temanın alt çubuğu gizlenir; temanınkini istersen EasySell'de yapışkan düğmeyi kapat.
- **Loox, Track123:** yerleştirmelerini aç. Yorum kartları tasarımda (gerçek yorumlardan); "Kargo takip" `/apps/track123`'e gider (tema ayarından değişir).
- **Loox yorumları:** Loox yerleştirmesini açman yeter (1b).
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
- [ ] LunaDream: Kız seç → Kapıda Ödeme ile Sipariş Ver → formda yalnız Kız; kapat, Erkek seç, yeniden aç → formda yalnız Erkek. 2 Adet + 2. lamba Kız → formda Erkek 1 + Kız 1.
- [ ] Ekranın altında tek yapışkan düğme var (iki çubuk üst üste değil).
- [ ] "Işık kapanınca ne oluyor" bölümü görünüyor; video eklediysen dokununca sesli oynuyor.
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
