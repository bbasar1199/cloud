# Rapor · 17 Ekim 2026

## Yapılanlar
- **Bir gece, beş an videoları** (Remotion, `onizleme/v/`): 5 an + erkek modeli için 2 ek (m3, m5). 720×1280 H.264, sessiz, 5-6 sn döngü, her biri 0,5-0,9 MB, poster jpg'leri yanında. Hareketler: elde lambanın sönüp yeniden yanması, açık kubbe yakın planı ve dönen diskler, nefes alan hale, tavan yansımasının yavaş dönüşü, gece→gündüz→gece. Ürünün görünüşü değişmedi. Kartlarda `<video muted playsinline loop autoplay preload="metadata" poster>`; görünen oynar, görünmeyen durur; azaltılmış harekette yalnız poster var. Kaynak: `araclar/remotion/`.
- **Fikirler index'e girdi** (eski hâli: `onizleme/yedek/index-fikirlerden-once.html`):
  - Diski tak → 3B disk halkasının yerine. Model seçimine göre oda değişiyor, dokunulmazsa 2 sn sonra ilk diski kendisi takıyor, buton artık "Baştan".
  - Ay bitmeden → yalnız ay kartı alındı, eski geri sayımın yerine geçti (tek satır, ince ilerleme çizgisi, saniye yok, son gün "Bugün son gün").
  - Gece hikâyeleri → not destesinin yerine. Yükseklik 460px, Abdülkerim T. yorumu eklendi, ugc4 eklendi, ugc1'in yazısı kırpıldı (`g/ugc1k.jpg`).
- **Shopify bölümleri** (`shopify/*.txt`, 12 bölüm + `KURULUM.txt`): Fiyat, karşılaştırma fiyatı, indirim yüzdesi, adet fiyatı, kazanç, masal başına fiyat ve kardeş butonu varyant verisinden hesaplanıyor. Ay sonu sayacı JS ile ayın son günü 23:59:59'a sayıyor. Model seçimi bütün bölümlere `ayluna:model` olayıyla gidiyor. Theme Check'ten hatasız geçti. Sahte verili Liquid çizimiyle telefonda denendi; görünüş index ile aynı. Derleyici: `araclar/shopify-derle.py`.
- Düzeltmeler: SSS mührünün çevre yazısı görünmüyordu (aynı id çakışması), kutudaki elde görselinde poster yazısı kırpıldı, masal başına fiyat ₺141 yerine yuvarlanarak ₺142.

## Eleştirmenin seçimi
- **Diski tak: girsin.** Ürünü odada, gündüzden geceye geçerken gösteriyor. Halka yalnız diskleri gösteriyordu.
- **Gece hikâyeleri: girsin.** Meta'dan gelen kullanıcı bu düzeni tanıyor. Fotoğraf ve yorum tek yerde, eski bölümden daha az yazılı.
- **Ay bitmeden: kısmen.** Ay kartı dürüst ve güzel bulundu. Paket kartları levhadakileri tekrarladığı için alınmadı; ikinci bir paket seçici kafa karıştırırdı.

## Teyit bekleyenler
- Ölçüler, pil süresi, yaş aralığı, teslim süresi, 16:00 kargo kesimi, online ödemede %5, firma unvanı, WhatsApp numarası.
- 2'li pakette hediye disk sayısı, 12 disk adı (kutu içeriğiyle karşılaştır), "Satın aldı" etiketi, 4,7 · 62 yorum.
- Shopify'da LunaDream varyant yapısı: Model × Paket seçenekleri ve "2 lamba" ayrı bir varyant olmalı.
- Kapıda ödeme uygulamasının buton seçicisi.
- Videolar bu ortamda yalnız çerçeve çerçeve kontrol edildi (test tarayıcısı H.264 oynatmıyor). Gerçek telefonda oynatılması denenmeli.
