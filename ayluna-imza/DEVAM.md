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
- `onizleme/fikirler.html` — eleştirmenin 3 fikri: Diski tak, Ay bitmeden, Gece hikâyeleri (Diski tak ve Gece hikâyeleri tam, Ay bitmeden yalnız ay kartı olarak index'e girdi).
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
1. Kullanıcıdan teyitler (RAPOR.md "Teyit bekleyenler"): ölçü, pil, yaş, teslim, varyant yapısı, COD seçicisi.
2. Shopify'a kurulum (`shopify/KURULUM.txt`) ve gerçek telefonda deneme: videolar, sayaç, COD akışı.
3. Masaüstü düzeni (öncelikli): solda yapışkan galeri, sağda satın alma kutusu; diğer bölümler geniş ızgara. Bölümler şimdilik 430px sütunda.
4. Gerçek müşteri videosu gelirse hikâyelere video karesi eklemek.

## Son durum (17 Ekim 2026)
- Ödeme: kartla öde varsayılan (%5), kapıda ikinci; teslimat adımları otomatik tarihli. Fayda ve Kapanış bölümleri eklendi.
- Videolar: `onizleme/v/` (kaynak `araclar/remotion/`, `npm run video`).
- Seçilen fikirler index'te; eski hâli `onizleme/yedek/index-fikirlerden-once.html`.
- Shopify: kaynak `araclar/shopify-kaynak/*.liquid` → `python3 ayluna-imza/araclar/shopify-derle.py` → `shopify/*.txt` (CSS index.html'den otomatik alınır, Liquid/şema denetlenir). Sahte verili önizleme: `araclar/shopify-onizle.js` (liquidjs gerekir).
