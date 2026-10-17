# Ayluna · LunaDream imza ürün sayfası — devam notu

Bu klasör, Ayluna (ayluna.shop) için yeniden tasarlanan LunaDream ürün sayfasının çalışan önizlemesidir. Yeni bir oturum buradan devam edebilir.

**Sonra mutlaka `TASARIM-BILGISI.md`'yi oku.** İçinde şunlar var:
- tasarım sistemi
- kullanıcının zevki ve seçim geçmişi
- iş verisi (iade, dönüşüm)
- eleştirmen ajanın kişiliği
- bilinen hatalar
- açık kararlar

Güncel beceri dosyaları `beceriler/` klasöründe; claude.ai'deki sürümleri bayat. Ham araştırma notları `ogrenme/` klasöründe.

## Kullanıcı hakkında (çalışma biçimi)
- Her zaman **Türkçe** konuş. Kısa yaz; uzun açıklama ve istenmeyen dosya gönderme.
- Türkiye'de Shopify + **kapıda ödeme** ile satış; trafik Meta reklamlarından, **mobil**.
- Tasarım akışı: önce yap → **kullanıcıyı taklit eden eleştirmen ajan** her bölümü denetleyip revize etsin → gerekirse alternatifleri göster → eleştirmenin en beğendiği **3 fikri** ayrı ayrı sun.
- Shopify tema kodunu kopyala-yapıştır **.txt** dosyaları olarak ister.
- Sevmedikleri: emoji ikonlar, boğucu/çok yazılı sayfa, Shopify teması gibi sıradan düzen, tamamen koyu tema, uydurma sayı/sayaç, abartılı efekt.
- İstedikleri: "acayip ama sıkmayan" tarz, doğa gibi uyumlu hareketler, güven veren, dönüşüm odaklı; bundle, ay sonu fiyat geri sayımı (her ay zam yapıyor), sosyal kanıt; tek ürün mağazası değil (15 ürün).

## Dosyalar
- **`canvas/Main.dc.html`: kullanıcının seçtiği tasarım. Yeni iş buradan başlar.**
- `onizleme/index.html` ve `onizleme/iskelet.html`: eski önizleme denemeleri. Saf HTML/CSS/JS. Görseller `onizleme/g/`, fontlar `onizleme/f/` (Young Serif + Onest, Fontsource).
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
- Teyit bekleyenler: ölçüler, pil süresi, yaş aralığı, teslim süresi, 16:00 kargo kesimi, firma unvanı, WhatsApp numarası.
- Online ödemede %5: kullanıcı 17 Ekim'de kendisi söyledi ("kartla %5 indirim"). İndirim kodu Shopify'da tanımlanmalı.
- Ürün görselleri gerçek üründen Google Flow (Nano Banana Pro) ile üretildi; ürünün kendisi değiştirilmez.

## Sıradaki işler (17 Ekim, güncel)
1. **Shopify bölümlerini Main.dc'den yeniden türet.** Bugünkü bölümler iskelet.html'den geliyor, seçilen tasarımı yansıtmıyor. Main'in kusurlarını taşırken düzelt (`TASARIM-BILGISI.md` §4).
2. Fiyat ve mevzuat soruları: son 10 günün fiyatı, Kasım zammı, iade metni (`TASARIM-BILGISI.md` §11).
3. Kullanıcıdan teyitler: ölçü, pil, yaş, teslim, varyant yapısı, kapıda ödeme seçicisi.
4. Shopify'a kurulum ve gerçek telefonda, Instagram içinden deneme.
5. Masaüstü düzeni: solda yapışkan galeri, sağda satın alma kutusu.
6. Gerçek müşteri videosu gelirse video karesi.

## Kullanıcının netleştirdiği yön (17 Ekim, sonra)
- İnsanların alıştığı kalıplar (emoji fayda listesi, indirim sayacı, "dün satılan", stok alarmı) atılmaz; iyileştirilir. Baskı unsurları istiyor; gerçek veriye bağlanır (stok: Shopify envanteri, dün satılan: Flow ile metafield, sayaç: gerçek ay sonu zammı).
- Gösteriş/yeniden kurgu değil, işe yarayan iyileştirme bekliyor.

## Yeni iskelet denemesi (17 Ekim 2026)
- `onizleme/iskelet.html`: canlı sitenin işe yarayan mantığı (uyku rutini vaadi, sosyal kanıt, garanti, kolay kullanım, SSS) + bilgi veren özellik bölümü, tuşlar, Tavşanlı/Uzay Kaşifi karşılaştırması, masaüstü düzeni (solda yapışkan galeri). Onaylanırsa index ve Shopify bölümlerine taşınacak.
- Canlı sitede düzeltilmesi gerekenler: 90 gün iade (gerçeği 30), sahte aciliyet (35 kişi bakıyor, 3 günde 399 adet), yorum sayısı çelişkisi (2467/63), "Tükendi" + "Sepete ekle" birlikte.

## Son durum (17 Ekim 2026)
- Ödeme: kartla öde varsayılan (%5), kapıda ikinci; teslimat adımları otomatik tarihli. Fayda ve Kapanış bölümleri eklendi.
- Videolar: `onizleme/v/` (kaynak `araclar/remotion/`, `npm run video`).
- Seçilen fikirler index'te; eski hâli `onizleme/yedek/index-fikirlerden-once.html`.
- Shopify: kaynak `araclar/shopify-kaynak/*.liquid` → `python3 ayluna-imza/araclar/shopify-derle.py` → `shopify/*.txt`. Liquid ve şema denetlenir. CSS **iskelet.html**'den alınır (`shopify-derle.py:16`), index.html'den değil. Bölümler henüz seçilen Main.dc'yi yansıtmıyor; ayrıntı `ogrenme/depo-denetimi.md`'de. Sahte verili önizleme: `araclar/shopify-onizle.js` (liquidjs gerekir).

## Sohbetten devir notu (17 Ekim 2026, 15:00)
- Claude Design tuvali: https://claude.ai/artifact/CHmRtH4tjbapGmPtuQGsTH ("Ayluna İmza Tasarım"). Kullanıcının seçtiği pano `project/Main.dc.html`; kopyası `canvas/Main.dc.html`. Yayın: Artifact publish, root = `project/` klasörünün bir üstü, file_path `project/Main.dc.html` (kökte ayrı Main.dc.html oluşmasın).
- Bu panoda son yapılanlar: emojisiz ince özellik şeridi, küçük model kartları (Flow'da krem stüdyo görselleri: `canvas/magaza/m-kiz.jpg`, `m-erkek.jpg`), sade paket satırları ("Kardeşe" rozeti, "En çok tercih" kaldırıldı), ince ay sonu sayaç şeridi, ödeme seçimi (Kartla öde %5 varsayılan, kapıda ikinci; fiyatlar otomatik), galeride mağazadaki 9 ürün fotoğrafı (`canvas/magaza/ld0-8.jpg`).
- .dc.html'i yerelde görmek: `NODE_PATH=$(npm root -g) node ayluna-imza/araclar/dc-onizle.js <dosya.dc.html> cikti.png '{"pay":"kapida"}' 0 1100`.
  - Yollar artık betiğe göre çözülüyor.
  - y değeri levhanın tepesinden ölçülür; sayfanın en üstü için −470 ver.
  - Yerelde yalnız `canvas/magaza/` görselleri var. Chrome'da tuval açılınca donuyor, bu yüzden yerel önizleme kullan.
- Flow (Nano Banana Pro) iş akışı: flow.google.com, "Eki 17 - 02:24" projesi; + ile projeden referans seç (lunadream-8.png kız, lunadream-erkek.png robot), istem yaz. Görseli almak için büyük img'yi sayfaya sabit katman olarak koyup save_to_disk ekran görüntüsü al (ilk deneme zaman aşımına düşebilir, ikinci denemede çalışır), PIL ile kırp.
- Mağaza ürün verisi: Chrome'da `ayluna.shop/products.json?limit=250` (kabuktan ayluna.shop ve cdn.shopify.com engelli).
