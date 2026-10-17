# Ayluna · LunaDream imza ürün sayfası — devam notu

Bu klasör, Ayluna (ayluna.shop) için yeniden tasarlanan LunaDream ürün sayfasının çalışan önizlemesidir. Yeni bir oturum buradan devam edebilir.

## Kullanıcı hakkında (çalışma biçimi)
- Her zaman **Türkçe** konuş. Kısa yaz; uzun açıklama ve istenmeyen dosya gönderme.
- Türkiye'de Shopify + **kapıda ödeme** ile satış; trafik Meta reklamlarından, **mobil**.
- Tasarım akışı: önce yap → **kullanıcıyı taklit eden eleştirmen ajan** her bölümü denetleyip revize etsin → gerekirse alternatifleri göster → eleştirmenin en beğendiği **3 fikri** ayrı ayrı sun.
- Shopify tema kodunu kopyala-yapıştır **.txt** dosyaları olarak ister.
- Sevmedikleri: emoji ikonlar, boğucu/çok yazılı sayfa, Shopify teması gibi sıradan düzen, tamamen koyu tema, uydurma sayı/sayaç, abartılı efekt.
- İstedikleri: "acayip ama sıkmayan" tarz, doğa gibi uyumlu hareketler, güven veren, dönüşüm odaklı; bundle, ay sonu fiyat geri sayımı (her ay zam yapıyor), sosyal kanıt; tek ürün mağazası değil (15 ürün).

## Dosyalar
- `onizleme/index.html` — ana sayfa (saf HTML/CSS/JS). Görseller `onizleme/g/`, fontlar `onizleme/f/` (Young Serif + Onest, Fontsource).
- `onizleme/fikirler.html` — eleştirmenin 3 fikri: Diski tak, Ay bitmeden, Gece hikâyeleri.
- `araclar/ekran-goruntusu.js` — 390×844 telefon ekranında sayfa boyunca ekran görüntüsü alır:
  `NODE_PATH=$(npm root -g) node ayluna-imza/araclar/ekran-goruntusu.js /tmp/ekran [index.html|fikirler.html]`
  Her değişiklikten sonra çalıştır ve görüntülere bakarak kontrol et.

## Tasarım sistemi
- Renkler: krem #F6F1E9 / #FFFDF9, lacivert #1A2142 / #141A36 / #0C1027, amber #F2A65A, ikincil #5C6078.
- Tek yumuşatma eğrisi: cubic-bezier(.2,.7,.2,1). Animasyon yalnız transform/opacity.
- Sayfa yukarıdan aşağı gündüzden geceye akar.

## Ürün bilgileri
- LunaDream: 1 lamba ₺1.699,99 (₺1.999,00), 2 lamba ₺2.749,99 (₺3.998,00). Kız modeli = tavşanlı karusel, Bluetooth ninni hoparlörlü; Erkek modeli = Uzay Kaşifi robot, hoparlörsüz. Kutuda 6 disk + 6 hediye disk (2'li pakette hediye sayısı teyit edilecek).
- Gerçek yorumlar: Burak G., Handan B., Abdülkerim T., Sevcan Z., Mehmet C.; 4,7 · 62 yorum (teyit edilecek).
- Teyit bekleyenler: ölçüler, pil süresi, yaş aralığı, teslim süresi, 16:00 kargo kesimi, online ödemede %5, firma unvanı, WhatsApp numarası.
- Ürün görselleri gerçek üründen Google Flow (Nano Banana Pro) ile üretildi; ürünün kendisi değiştirilmez.

## Sıradaki işler
1. Remotion ile "Bir gece, beş an" kartları için kısa videolar (mevcut görsellerden).
2. Kullanıcının seçtiği fikirleri `index.html`'e yerleştirmek.
3. Onaydan sonra bölümleri Shopify OS 2.0 section olarak `.txt` çıkarmak (schema ile düzenlenebilir).
