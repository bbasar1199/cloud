# LunaDream · premium fotoğraf seti (21 Eki)

Kullanıcı: "Biraz daha kurumsal bir görüntü oluşturmanı istiyorum; ürünün premium fotoğrafları olmalı."
Bugünkü galeri canlı mağazanın afişleri: yazılı başlıklar, rozetler, düğme çizimleri, mor-mavi neon, yorum kolajı. Her biri ayrı bir dil konuşuyor; kurumsal görünmeyi en çok bu engelliyor. Benzer markalar (Hatch, Yoto, Tonies; `ogrenme/rakip-sayfalar.md`) tek bir stüdyo dili kullanıyor: aynı fon, aynı ışık, yazısız kare. Yazı sayfada HTML olarak duruyor.

Araç: **ChatGPT** (kullanıcı, 21 Eki: "ChatGPT'den yaptır"); Google Flow da olur. Higgsfield kullanılmaz. Kopyala-yapıştır istemler: `chatgpt-istemleri-lunadream.txt`; referans paketi: `lunadream-referans.zip` (dosyalar `canvas/` altında). Ürün sıfırdan üretilmez: her istemde gerçek ürün fotoğrafı referans verilir, şekli, rengi, oranı aynen kalır. Görselde yazı, logo, rozet yok.

## Ayluna stüdyo dili (bütün kareler için)
- **İki fon, başka fon yok.**
  - **Gündüz:** sıcak krem kâğıt fon (#F1E8DA tonu), sonsuz fon (duvar ve zemin birleşik). Yumuşak pencere ışığı soldan, ürünün sağında yumuşak gölge.
  - **Gece:** derin lacivert fon (#141A36 tonu). Işık yalnız lambadan gelir. Fonda ve tavanda gerçek diskin deseni, yumuşak ve gerçek parlaklıkta.
- **Kamera:** 85 mm, ürün göz hizasının 15° üstünden, ortada, keskin. Arka plan hafif flu. Ürün karenin yüzde 45-55'ini kaplar.
- **Renk:**
  - sıcak açık tonlar, lacivert gölgeler, amber lamba ışığı;
  - mor, pembe neon, turkuaz yok;
  - doygunluk ılımlı, siyahlar tam siyah değil, koyu lacivert.
- **Dekor:** en çok bir yüzey (açık meşe komodin ya da keten kumaş). Gerekirse tek bir sade nesne (örgü oyuncak, yazısı okunmayan kitap). Kalabalık sahne yok.
- **Boyutlar:** galeri 1:1 (2048×2048), vitrin 4:5 (1080×1350; sayfada 3:4 kırpılır). WebP ya da JPG.
- **Kontrol:** her kare büyütülüp bakılır. Ürün detayı değiştiyse (tavşan sayısı, kubbe kıvrımı, robotun yüzü, yazı), el ya da parmak bozuksa yeniden üretilir.

## Çekim listesi
Referanslar `canvas/` altında; yüklenecek paket: `lunadream-referans.zip` (aynı dosyalar, 01-13 numaralı).

| # | Dosya | Oran | Sahne | Referans | Sayfada |
|---|---|---|---|---|---|
| 1 | `p-kiz-gunduz.jpg` | 1:1 | Kız, gündüz stüdyosu, 3/4 açı, lamba sönük | magaza/m-kiz.jpg | Galeri 1 (ilk kare), Kız model kartı |
| 2 | `p-kiz-gece.jpg` | 1:1 | Kız, gece stüdyosu, lamba yanıyor; fonda Ay ve yıldız deseni | m-kiz.jpg, diskler/disk-ay-yildiz.jpg, c-gorsel/c-kiz-gece.jpg (ışık tonu) | Galeri 2 |
| 3 | `p-erkek-gunduz.jpg` | 1:1 | Erkek (Uzay Kaşifi), gündüz stüdyosu, 3/4 açı | magaza/m-erkek.jpg | Galeri 3, Erkek model kartı |
| 4 | `p-erkek-gece.jpg` | 1:1 | Erkek, gece stüdyosu, lamba yanıyor; fonda Uzay deseni | m-erkek.jpg, diskler/disk-uzay.jpg, c-gorsel/c-erkek-gece.jpg | Galeri 4 |
| 5 | `p-kiz-detay.jpg` | 1:1 | Yakın çekim: yanan kubbe ve dönen tavşanlar, sığ alan derinliği | m-kiz.jpg, c-gorsel/c-elde.jpg | Galeri 5 |
| 6 | `p-elde.jpg` | 1:1 | Bir yetişkinin iki eli yanan Kız lambayı tutuyor, keten kumaş üstünde, boyutu gösterir | c-gorsel/c-elde.jpg, m-kiz.jpg | Galeri 6, vitrin "Birlikte dinleyin" yedeği |
| 7 | `p-diskler.jpg` | 1:1 | Üstten: krem yüzeyde yelpaze gibi açılmış 6 masal diski ve yanında Kız lamba | diskler/disk-masal, disk-okyanus, disk-sato, disk-deniz-kizi, disk-hayvanlar, disk-ay-yildiz + m-kiz.jpg | Galeri 7, Diskler bölümü |
| 8-11 | `lo-kiz-masal`, `lo-ninni`, `lo-erkek-uzay`, `lo-disk-sec` | 4:5 | Çocuklu oda kareleri (gece) | `flow-istemleri-lunadream-oda.md` | Odası böyle görünecek (vitrin), galeri 8-9 |

## İstemler (Türkçe yazılabilir; İngilizce daha tutarlı sonuç verir; ChatGPT için tam metinler `chatgpt-istemleri-lunadream.txt`'de)

1. **p-kiz-gunduz** · ref: m-kiz.jpg
   - "Ürün fotoğrafı. Referanstaki pembe tavşanlı LunaDream gece lambası (şekli, rengi, kubbesi, tavşanları aynen), sıcak krem renkli sonsuz kâğıt fonun ortasında, 3/4 açı. Soldan yumuşak pencere ışığı, sağında yumuşak gölge. 85 mm, keskin ürün, hafif flu fon. Sade, premium, katalog çekimi. Yazı, logo, başka nesne yok."
   - "Premium studio product photo of the exact night lamp from the reference (pink dome, carousel bunnies, gold trim; keep shape, color and proportions identical), centered on a seamless warm cream paper backdrop, three-quarter view, soft window light from the left, soft shadow to the right, 85mm, sharp product, gentle background falloff, minimal, catalog quality. No text, no logo, no props."
2. **p-kiz-gece** · ref: m-kiz.jpg + disk-ay-yildiz.jpg + c-kiz-gece.jpg
   - "Aynı lamba (referanstaki ürün aynen), derin lacivert sonsuz fonun önünde, lamba yanıyor ve sıcak amber ışık veriyor. Fonun üst kısmına referans diskteki ay ve yıldız deseni yumuşakça yansıyor, gerçekçi parlaklıkta. Başka ışık yok. 85 mm, premium ürün fotoğrafı, sakin. Mor ya da neon renk yok, yazı yok."
   - "The exact lamp from the reference, switched on, glowing warm amber, in front of a deep navy seamless backdrop. The moon-and-stars pattern from the reference disc softly projected on the upper backdrop at realistic brightness. No other light source. 85mm premium product photo, calm. No purple or neon tones, no text."
3. **p-erkek-gunduz** · ref: m-erkek.jpg — istem 1'in aynısı, ürün: "referanstaki robot biçimli Uzay Kaşifi gece lambası (siyah tekerlekler, sarı ayrıntılar, beyaz kubbe, yüz ekranı aynen)".
4. **p-erkek-gece** · ref: m-erkek.jpg + disk-uzay.jpg — istem 2'nin aynısı, desen: "referans diskteki uzay deseni (gezegenler, yıldızlar)".
5. **p-kiz-detay** · ref: m-kiz.jpg + c-elde.jpg
   - "Makro ürün fotoğrafı: referanstaki lambanın yanan kubbesi ve içindeki tavşanlı atlıkarınca, yakından, sığ alan derinliği. Sıcak amber ışık, lacivert karanlık arka plan. Ürün ayrıntıları aynen. Yazı yok."
6. **p-elde** · ref: c-elde.jpg + m-kiz.jpg
   - "Bir yetişkinin iki eli, referanstaki yanan pembe tavşanlı lambayı göğüs hizasında tutuyor; arkada krem keten kumaş, yüz görünmüyor. Lambanın boyutu ellere göre gerçek (referanstaki gibi). Doğal, sıcak ışık. Eller ve parmaklar doğal ve kusursuz. Yazı yok."
7. **p-diskler** · ref: 6 disk + m-kiz.jpg
   - "Üstten çekim: sıcak krem bir yüzeyde referanstaki yuvarlak masal diskleri yelpaze gibi açılmış (desenleri aynen), yanında referanstaki sönük pembe tavşanlı lamba. Yumuşak gün ışığı, sade, katalog düzeni. Yazı yok."

## Sayfaya giriş (kareler gelince)
- **Galeri:** yazılı afişlerin yerine 1-7 ve iki oda karesi gelir. Afişlerdeki bilgi (tema projeksiyonu, Bluetooth, hediye) zaten sayfada HTML olarak var. Müşteri fotoğrafı (ld1, minikesnaftr) galeriden çıkar; "Evlerinizden" şeridinde kalır.
- **Model kartları:** 1 ve 3.
- **Odası böyle görünecek:** 8-11.
- **Diskler:** 7.
- Kare yetmezse o yer bugünkü görselle kalır, eksik kare uydurulmaz.
