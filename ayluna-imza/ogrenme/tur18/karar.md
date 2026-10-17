# Karar · Tur 18 sıfır tasarım (mağaza sahibi)

## 1. Puanlar
- **A "Oda ve Tavan": 8/10.** Işık mantığı sayfayı tek fikre bağlıyor; onayladığım gece galerisini ve model kartlarını koruyor, okunaklı yazıyı büyükanne için seçiyor. Ama istediğim bölüm girişini atmış, Bir gece'yi tamamen koyu yapmış.
- **C "Duvar ve Tavan": 7/10.** Sistemi en düzenli olan bu. Ama gece galerisini açığa çeviriyor, Sihirli'yi seçmediğim liste biçimine (V3) döndürüyor; pembe zemin ve Figtree sıradan.
- **B "Yorgan": 5/10.** En "acayip" fikir bu, ama beş zemin rengi, kesik dikiş ve Gluten hem boğuyor hem çocuksu. Eylül'de reddettiğim "Baloo/pembe"ye yakın; koyu sayaç şeridi de kural 5'e aykırı.

## 2. Kazanan: A
Ses A'nın: ışık yalnız lambanın olduğu yerde. Diğerlerinden yalnız üç parça alınır:
1. **Amber sayaç şeridi (C).** Sayfa lamba ışığıyla açılır ve gece galerisinden ayrılır. Koyu olmadığı için kuralı çiğnemez.
2. **Saatle koyulaşan Bir gece satırları (C; B'de de var).** Akşam kararır, sabah açılır. A'nın dikey saat rayı beş satırı tek bölüm olarak bağlar.
3. **Ay evreli teslim çizelgesi (C).** Hilal, yarım ay, dolunay. Markadan gelir, yazı eklemez.

## 3. Kesin kararlar
**Renk** (başka renk yok):
- Gece `#1A2142`: yazı, koyu bantlar, seçili kenar.
- Lamba `#F2A65A`: ana buton, sayaç şeridi, "En avantajlı" sekmesi, hale, koyuda rakam. Açık zeminde yazı olmaz.
- Kehribar `#A05A1C`: açık zeminde etiket, indirim, stok noktası (Çarşaf'ta 5,0:1, Duvar'da 4,6:1).
- Çarşaf `#FFF8F0`: ana açık bant. A'nın #FFFCF8'i telefonda beyaz okunur; bir ton ısıtıldı.
- Işıklı duvar `#FBEEE4`: ikinci açık bant, seçili dolgu.
- Sis `#5C6078`: ikincil yazı. Koyuda ikincil yazı Çarşaf %72. Çizgi 1,5px Gece %16.

**Yazı:**
- **Literata 500 (opsz):** ürün adı 28, bölüm başlığı 22, saatler 20, alıntı 15/1,55; "30" ve alt bilgideki "Ayluna" 40.
- **Atkinson Hyperlegible Next 400/700:** fiyat 20/700, gövde 15, açıklama 14, not 13, etiket 12/700, buton 15/700. "Model" ve "Paket" etiketleri 13/700 Kehribar. Rakamlar tabular. Büyük harf yok.

**Bölüm sırası** (Ç Çarşaf, D Duvar, G Gece, L Lamba):
1. Sayaç şeridi · L, Gece yazı 13
2. Galeri · G; logo ve küçük resimler fotoğrafın üstünde
3. Ad, puan, fiyat, güven · Ç
4. Sihirli özellikler · D; A'nın artı çizgili 2×2 penceresi, her bölmede 40px Gece ikon kutusunda amber canlı çizim (V1)
5. Satın al · Ç
6. Diskler (imza an) · G, üst kenarı kubbe
7. Kapına ne gelir · D
8. Videolar · Ç (gerçek video yoksa gizlenir)
9. Yorumlar · D
10. Bir gece, beş an · 20:00 Ç, 20:30 D, 20:45 G, 21:00 G, 07:30 D
11. 30 gün iade · Ç
12. SSS · D
13. Odanın geri kalanı · Ç
14. Alt bilgi · D

Yapışkan çubuk: Ç, 64px, üstünde çizgi; yalnız 5. bölüm ekrandayken gizlenir.
İlk ekranda (390×664, çubuk dahil) fiyat ve güven satırı görünür. Bu, ekran görüntüsüyle kanıtlanır.

**İmza an "Disk tavana açılır" (A):**
- İlk görünüşte bir kez "Ay ve yıldız" yansır.
- 0–160ms: disk 1 → .92 → 1 olur; 2px Lamba halka belirir ve kalır.
- 0–200ms: eski desen kaybolur (opaklık 0).
- 80–720ms: yeni desen lambadan çıkar: `translateY(96px) scale(.2)` → `0, 1`. Opaklık ilk 280ms'de .9 olur, hale .6 → 1 büyür.
- 240ms: disk adı 160ms'de çapraz geçer, sonra her şey durur.
- Art arda dokunuşta önceki animasyon iptal olur.
- Azaltılmış hareket: yalnız opaklık, 200ms.

**Satın alma bloğu:** A'nın taslağı, şu farklarla:
- Model kartları stüdyo fotoğraflı. Seçili: 2px Gece kenar, Duvar dolgu.
- Paket satırı en az 76px. "+6 hediye disk" disk ikonlu ayrı satır.
- 2'li seçim segmentleri 48px. Yer anında açılır; segmentler opaklık ve 8px kaymayla gelir.
- Ana buton Lamba, 56px, kilit ikonlu, fiyat sağda. Kapıda butonu çerçeveli, 52px.
- Fiyatlar seçimle değişir. 1 Adet: ₺1.614,99 · ₺165 daha az · kapıda ₺1.779,99.
- Teslim: ay evreleri düz çizgiyle bağlanır.

**Şekil ve hareket:**
- Köşe: kontrol 14, medya 20, daire (disk, hale, radyo, ay), bant 0. Hap ve gölge yok.
- Aralık: 4-8-12-16-24-32. Yan 20, parça içi 8, öğe 16, grup 24, başlık-içerik 12, bant dolgusu 32.
- Tek eğri `cubic-bezier(.22,1,.36,1)`; süreler 160, 240, 640ms.
- Bölüm girişi (§10'da istedim, A atmıştı): 16px aşağıdan ve saydamdan, 640ms, bir kez; içerik 80ms sonra. Galeride ve satın almada yok.

## 4. Riskler
- **Pembe Erkek alıcıyı dışlar:** pembe zemin yok; pembe yalnız Kız fotoğrafında.
- **Gluten çocuksu:** hiçbir yerde yok.
- **Literata Türkçe:** latin-ext var. Yine de "İğne · Işık · Gözler kapanır" 28/22/15px'te denenir. ğ ile İ çakışırsa satır yüksekliği 1,25 olur.
- **Atkinson tabular rakam:** sayaçta denenir. Titrerse rakamlar sabit genişlikli kutuya girer.
- **Sayaç şeridi:** Lamba dolgu, Gece yazı (7,7:1), İstanbul saati. Söz gerçektir: zam gelse de o günün fiyatı 23:59'a kadar korunur. Tutamazsam şeridi kapatırım.
- **Vaat ile kutu:** yansıma şimdilik disk çizimi, gerçeğinden net. Yayından önce her diskin tavan fotoğrafını çekerim; o zamana kadar "[gerçek tavan fotoğrafı]" kalır.
- **Puan ve yorum sayısı** Loox'tan canlı gelir.

## 5. Yasaklar
1. Ölçek dışı boyut: 12px altı yazı, ara boyut, 48px altı dokunma alanı.
2. Pembe zemin, çocuksu yuvarlak yazı, üçüncü aile, kart içinde kart, gölge, hap buton.
3. Transform/opacity dışı animasyon: yükseklik açma (SSS anında açılır), blur, clip-path. Sihirli dışında döngü ya da nabız.
4. Uydurma bilgi: cihaz saatli sayaç, "X kişi bakıyor", çıplak "12 disk", iç gerekçe, Unicode hilal karakteri ya da emoji (hilal SVG olur).
5. Kapıda ödemeyi öne almak: varsayılan yapmak, ana buton görünümü vermek, ₺80'i saklamak. Her buton kartla fiyatı taşır.
