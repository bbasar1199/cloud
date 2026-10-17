YÖN B · Yorgan

1. Ad ve fikir
Yorgan: sayfa, çocuğun üstüne örtülen dikişli bir yorgandır. Her bölüm kendi renginde dolgulu bir parçadır, parçalar dikişle birleşir, ışık yalnız gece parçalarında yanar.
Neden özgü: LunaDream yatakta, uyku anında kullanılır; anne ve büyükanneler yorganı, çeyiz dikişini ezbere bilir. Parçalar birbirine değer (uzak değil), dikiş ayırır (yakın değil): "tam yakın değil uzak değil" tarifinin karşılığı.
Yöntem (shape, mod Persuade): yedi aday (yorgan, sihirli fener, ninni kaseti, masal kitabı, yıldız haritası, uyku çizelgesi, hediye kutusu) içinden seçildi. Kategori rutini (beyaz Shopify) ve karşıtı (koyu galaksi-neon) elendi.

2. Token sistemi
Renk (renk bölümün işini söyler):
- Gece #1A2142: metin, ışık bölümleri, seçili durum.
- Kandil #F2A65A: yalnız ışık. Ana buton dolgusu (Gece metin 7,7:1), koyu zeminde rakam ve animasyon parçası. Açık zeminde metin olmaz.
- Pembe süt #F8EAE3: "karar" parçaları (ad-fiyat, seçim, SSS, alt bilgi).
- Gülkurusu #E8C9BD: "his" parçaları (Sihirli, yorumlar, diğer ürünler).
- Adaçayı #D5DDC8: "güvence" parçaları (kutu, iade).
- Tarçın #8A4A12: etiket (Pembe süt 5,8:1, Adaçayı 4,9:1). Gülkurusu üstünde etiket Gece olur.
İkincil metin Gece'den türer: #4B5070 (açık zeminlerde ≥5:1).

Yazı (Google Fonts, latin-ext; ğ ş ı İ teslimden önce denenir):
- Gluten 600: kabarık, dolgulu harfler; yalnız 4 rol: ürün adı 28, bölüm başlığı 22, saat 22, "30" 40.
- Rubik: büyük x-yüksekliği küçük boyutta okunur; tabular rakam. Fiyat 20/600, gövde 15, açıklama 14, not 13, etiket 12/600, buton 15/600.

Aralık (4 tabanlı): 4, 8, 12, 16, 24, 32. Grup içi 8–12, gruplar arası 24, parça iç boşluğu dikey 32, yan 16. Parçalar arası 0.
Köşe: parça 0, seçilebilir öğe ve buton 16, foto 12, çip 999, disk daire.
Yüzey ve çizgi: gölge yok; derinlik yalnız dolgu farkı. Dikiş: 1,5px kesik çizgi (6/5), parçanın üst kenarından 6px içeride, parçanın koyu tonunda (Gece'de Kandil %50). Düz çerçeve yalnız seçilmemiş seçilebilir öğede. Seçili = Gece dolgu. İkon 1,5px çizgi SVG.
Eğri: cubic-bezier(0.16, 1, 0.3, 1). 120 ms dokunuş, 300 durum, 600 imza.

3. İskelet
Hizalama: tek sol kenar (16px); fiyatlar sağa yaslı.
Bölüm sınırı: renk değişimi + dikiş. Aynı renk komşular (kutu + iade) yalnız dikişle ayrılır: aynı aile, ayrı bölüm.

G Gece, P Pembe süt, R Gülkurusu, A Adaçayı
0 Şerit G: "Bugünkü fiyat garantisi 05:12:44", galeri parçasının üst kenarı.
1 Galeri G: logo üstte, kare foto kırpılmadan, küçük resimler ve 1/9 altında.
   ☾Ayluna  ≡ ⌂ / [foto 390×390] / ▢▢▢▢▢ 1/9
2 Ad P: puan·Stokta / LunaDream / fiyat, üstü çizili, %15 / Kampanya · 1–31 Ekim / güven satırı; alt alta.
3 Sihirli R: başlık ve dikişle dörde bölünmüş tek blok; her hücrede brifteki canlı gösterge (hale, yelpaze, dalga, pil), başlık, tek cümle.
   anim ┆ anim / - - + - - / anim ┆ anim
4 Seçim P: madde 5.
5 Video G: 160×284 dört kapak yan yana kayar, sonuncunun ucu görünür.
6 Yorum R: başlık ve puan, çipler, 4 müşteri fotoğrafı, dikişle ayrılan alt alta alıntılar, "62 yorumun hepsini oku".
7 Bir gece: saate göre koyulaşan beş şerit, yatay kaydırma yok.
   20:00 Odayı hazırla      ▢  P
   20:30 Masalı seç         ▢  R
   20:45 Birlikte dinleyin  ▢  G
   21:00 Gözler kapanır     ▢  G
   07:30 Sabah şarja        ▢  A
8 Diskler G: madde 4 (tavan / lamba / disk rayı).
9 Kutu A: solda elde tutulan foto, sağda dört satır.
10 İade A: "30" ve tek cümle yan yana.
11 SSS P: soru satırları, dikişle ayrılır.
12 Diğer R: 13 ürün yan yana kayar.
13 Alt P: kapanış ve buton, yasal, [künye], KDV, büyük "Ayluna" ☾.
Yapışkan P: ▢ ₺2.612,49 · 2 Kız · kartla · 05:12 [Satın al]

4. İmza an: "Diski tak, tavan açılsın"
Diskler parçası: üstte boş tavan, ortada seçili modelin gerçek kesim PNG'si, altta 11 disklik ray.
- 0 ms: dokunulan diskin kopyası lambanın kubbesine uçar (translate + scale .4), 300 ms.
- 250 ms: kopya söner (120 ms); lambanın arkasındaki ışık katmanı yanar ve yanık kalır (opacity, 300 ms).
- 300 ms: desen dairesi lambadan tavana yükselir: translateY(120px) scale(.25) opacity 0 → yerinde, scale 1, opacity .9; 600 ms.
- Eski desen 150 ms'de söner. İlk girişte "Ay ve yıldız" ile bir kez kendiliğinden oynar.
- Azaltılmış hareket: uçuş yok, desen 200 ms opacity ile gelir.
- Altında disk adı ve "[gerçek tavan fotoğrafı]".
Neden satar: ürünün tek mekanizmasını annenin parmağıyla gösterir; "6 + 6 disk" vaadini sayılabilir yapar (eski "12 yazıyor 6 geliyor" şikâyetine karşı); 20:30 "Masalı seç" anını önceden yaşatır.

5. Satın alma bloğu
Model
[▢ Kız ]  [▢ Erkek ]            64px, iki eşit
 tavşanlı·ninnili  robot·ninnili
Paket          Kampanya · 1–31 Ekim
┌ 1 Adet              ₺1.699,99
└ +6 hediye disk  ₺1.999 · %15
┏ 2 Adet (En avantajlı) ₺2.749,99    Gece dolgu, fiyat Kandil
┃ Her kutuda +6 hediye disk · tanesi ₺1.375
┗ ₺649,99 tasarruf
1. lamba (Kız|Erkek)  2. lamba (Kız|Erkek)
● Stokta son 18 adet
[ Güvenli Ödeme İle Al · ₺2.612,49 ]   Kandil, 56px
  Kartla %5 indirimli · ₺217,50 daha az
[ Kapıda Ödeme ile Sipariş Ver ]       çerçeve, 52px
  +₺80 kapıda ödeme ücreti · ₺2.829,99
◯ Bugün sipariş ┄ ◯ [ertesi iş günü] kargoda ┄ ◯ [+3–7 gün] kapında
- Paket satırı tek seviye: içinde şerit ya da ikinci kutu yok.
- 2'li seçim yalnız 2 Adet seçiliyken görünür (opacity + 8px, 300 ms); segmentler 48px. Model kartı iki lambayı birden çevirir.
- Model seçimi galeriyi, ritüel fotoğraflarını, 20:45 metnini ve disk lambasını değiştirir.
- Buton fiyatları seçimle güncellenir; yeni sayı uydurulmaz.
- Stok noktası durağan; yapışkan çubuk blok ekrandayken gizli.

6. Sıcaklık
- Soğukluğun kaynağı: ince çerçeveli beyaz kartlar, gri metin, gevşek aralık. Yerine dolgulu, birbirine değen kumaş parçaları; ikincil metin Gece'den türer.
- Dikiş el emeği izi, Gluten yumuşak ses verir. Amber yalnız ışık olarak yanar.
- Gerçek aile fotoğrafları, elde tutulan lamba; "sen" diliyle tek cümle.
- Renkler anlam taşır ve sıra tekrar eder: göz bir kural görür, düzensizlik değil.

7. Öz denetim
Kaçılan varsayılanlar:
- Krem zemin + serif başlık + lamba ışığı: becerinin "sıcak, aile, çocuk" konusunda ilk refleks dediği üçlü. #F6F1E9 ve Young Serif bırakıldı; amber marka çapası olarak yalnız ışık rolünde kaldı.
- Başlık üstü etiket yok; "Sihirli özellikler" üst yazısı başlık oldu.
- Sert ofset gölgeli buton yok (şu anki 0 6px 0 kalktı).
- Her bölüme aynı kaydırma girişi yok.
- Eşit ikon kartları yok: Sihirli dikişle bölünmüş tek blok.
Beceri–kural çelişkileri (kural kazandı):
- Beceri gövdeye 16px taban önerir → kural 3: 15px.
- Beceri blur, clip-path, mask önerir → kural 7: yalnız transform/opacity.
- Beceri açık/koyuyu sahneden seçer (loş oda → koyu) → kural 5: açık sayfa.
- Beceri sesi büyük display tipinden alır → kural 3: ses biçimden ve renkten gelir.
Kural kontrolü: 1, 3, 9, 10 tamam; 2 tek cümle, kart içinde kart yok; 4 on üç ayrı parça; 5 koyu yalnız galeri, video, 20:45–21:00, diskler; 6 yalnız brif sayıları, [X] kalır; 7 tek eğri, döngü yalnız Sihirli (ekran dışında durur), videolar dokununca oynar; 8 48px, AA hesaplandı, açık zeminde amber metin yok. Çiğnenen kural yok.
Riskler: Gülkurusu "kız" okunabilir (tozlu ton; Erkek seçilince görseller değişir). Gluten çocuksuya kayabilir; yalnız 4 rolde. Sayaç şeridi ihlal sayılırsa Kandil dolgu + Gece metne döner.
