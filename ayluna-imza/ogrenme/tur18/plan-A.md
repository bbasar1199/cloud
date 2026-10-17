# YÖN A — "Oda ve Tavan"

## 1. Yön
**Fikir:** Sayfa, akşam 20:00'de lambası yanan çocuk odasıdır: duvarlar (açık bantlar) lambanın sıcak ışığını alır, karanlık yalnız tavanda ve gecede durur; tek sihirli an, diskin tavana açılmasıdır.
**Neden özgü:** Ürün avuç içi bir diski tavan büyüklüğünde masala çevirir. Annenin iki sessiz sorusu var: "Çocuğum ne görecek?" ve "Kutudan ne çıkacak?" (eski "12 yazıyor, 6 geliyor" yarası). İskelet bu iki soruya göre kurulur. Küçük yazıyı okuyan büyükanneler için okunaklılık kişiliğin parçasıdır.

## 2. Token sistemi
**Renk**
- Gece `#1A2142`: yazı rengi ve 3 koyu bant (siyah yok).
- Lamba `#F2A65A`: ana buton, hale, koyuda saat rakamları. Açık zeminde yazı olmaz.
- Kehribar `#A05A1C`: açık zeminde etiket, indirim, bağlantı (≥4,6:1).
- Çarşaf `#FFFCF8`: ana zemin.
- Işıklı duvar `#FBEEE4`: ikinci bant; beyaz duvarın amber ışık altındaki rengi.
- Sis `#5C6078`: ikincil yazı (≥5,4:1).

Krem `#F6F1E9` bırakıldı: becerinin 1. uyarısıyla (krem + serif) birebir örtüşüyor. Yerine ışıktan türeyen iki ton geldi; sıcaklığı zemin değil ışık verir.

**Yazı (2 aile)**
- **Literata** (opsz, 500): ürün adı 28, bölüm başlığı 22, yorum alıntısı 15/1.55, "30" 40. Kitap okuma yüzü; masal saatinin sesi.
- **Atkinson Hyperlegible Next** (400/700): geri kalan her şey. Az görenler için çizildi; 13–15px'te büyükanne de okur. Rakamlar tabular.
- **Tek ölçek:** 12, 13, 14, 15, 20, 22, 28, 40. Büyük harf etiket yok.

**Aralık:** 4-8-12-16-24-32. Yan boşluk 20. Parça içi 8, öğe 16, grup 24, başlıktan içeriğe 12, bant dolgusu 32.
**Yarıçap:** kontrol 14, medya 20, disk ve hale daire, bant 0; hap yok.
**Yüzey ve çizgi:** düz, gölge yok. Çizgi 1,5px Gece %16. Seçili: 2px Gece kenar ve Işıklı duvar dolgu. İkonlar 1,5px çizgi.
**Eğri:** `cubic-bezier(.22,1,.36,1)`. Süreler 160, 240, 640 ms.

## 3. İskelet
[Ç] Çarşaf · [D] Işıklı duvar · [G] Gece
```
[Ç] Bugünkü fiyat garantisi   05:12:44
[G] =        (hilal) Ayluna         []
    |    ürün fotoğrafı 1:1     |
    [][][][][][][]             1/9
[Ç] ***** 4,7 (62 yorum)    v Stokta
    LunaDream
    ₺1.699,99  ₺1.999,00  %15 indirim
    Kampanya 1–31 Ekim
    kargo, iade, ödeme (çizgi ikonlu)
[D] (hale) Mışıl mışıl | (disk) 6 + 6
    (dalga) Ninni      | (pil) Kablosuz
[Ç] Satın al (bkz. 5)
[G] ‿‿‿ kubbe kenarı ‿‿‿
        (  yansıma 300px  )
              [lamba]
    o o o o o o / o o o o o
[D] [elde foto]   1  lamba (Kız)
                  6  masal diski
                 +6  hediye disk
                  1  USB şarj kablosu
[Ç] Videolar   [9:16][9:16][9:  >
[D] Yorumlar   [f][f][f][f] çipler
    "alıntı" Burak G., Uyku
[G] 20:00 | Odayı hazırla     [foto]
    20:30 o Masalı seç        [foto]
[Ç] 30  gün iade + tek cümle
[D] SSS satırları             +
[Ç] Diğer ürünler [1:1][1:1]>
[D] Kapanış, buton, yasal, Ayluna 40
```
- **Sihirli:** kart yok. Dört bölmeli "pencere", ince artı çizgisiyle ayrılır. Her bölmede 40px canlı çizim, başlık 15/700, tek satır 13.
- **Diskler:** 11 disk 6+5 ızgarada, hepsi görünür. Altında "Her kutuda 6 masal diski + 6 hediye disk."
- **Kapına ne gelir:** sayılar 20, sağa hizalı; liste seçili modeli söyler.
- **Yorumlar:** 5 yorum alt alta liste, çiplerle süzülür. Sonra "hepsini oku" butonu ve not.
- **Bir gece:** dikey saat rayı, saatler Literata 20 Lamba. Model Erkek ise 20:45 ve görseller değişir.
- **Yapışkan çubuk:** [Ç], 64px: `[foto] ₺2.612,49 (2 Kız, kartla, 05:12:44) [Satın al]`. Satın al bölümü ekrandayken gizlenir.

**Sınırlar:** her bölüm kenardan kenara, komşusundan farklı tonda bir banttır. Bant içi en büyük boşluk 24, bölümler arası 64 artı ton değişimi. Oran 1:2:3:8; "ne yakın ne uzak" belirsizliği kalmaz. Karusele gömülen bölüm yok.
**Hizalama:** her şey 20px sol çizgiye hizalı. Rakamlar sağa hizalı ve tabular. Ortalanan tek şey tavan yansıması, çünkü ışık ortadaki lambadan çıkar.

## 4. İmza an: "Disk tavana açılır"
Koyu bandın kubbe biçimli üst kenarı sayfadaki tek eğridir. Ortada 300px yansıma dairesi, altında seçili modelin gerçek kesim PNG'si, köşede "[gerçek tavan fotoğrafı]" etiketi.
- **İlk görünüşte bir kez** "Ay ve yıldız" yansır.
- **Dokununca, 0–160ms:** disk 1 → .92 → 1 olur, Lamba halkası belirir.
- **0–200ms:** eski desen kaybolur.
- **80–720ms:** yeni desen lambanın tepesinden çıkar: `translateY(96px) scale(.2)` → `0, 1`. Opacity ilk 280ms'de dolar. Hale .6 → 1 büyür.
- **240ms:** disk adı çapraz geçer. Sonra her şey durur.
- **Azaltılmış hareket:** yalnız opacity, 200ms.

**Neden satar:** "6 + 6"yı gerçek disk görselleriyle tek tek kanıtlar. Anne telefonu çocuğa uzatıp "hangisini istersin?" diye sorar. Ritüeldeki "Masalı seç" anı satın almadan önce yaşanır.

## 5. Satın alma bloğu
```
Model
[foto] Kız             [foto] Erkek
Tavşanlı, ninnili      Robot, ninnili
Paket
| ( ) [l]  1 Adet          ₺1.699,99 |
|          +6 hediye disk  ₺1.999 %15|
+-----------------[En avantajlı]-----+
| (o) [ll] 2 Adet          ₺2.749,99 |
|      Her kutuda +6 hediye disk     |
|      ₺649,99 tasarruf  Tanesi ₺1.375|
1. lamba          [ Kız | Erkek ]
2. lamba          [ Kız | Erkek ]
o Stokta son 18 adet
[(kilit) Güvenli Ödeme İle Al  ₺2.612,49]
 Kartla %5 indirimli, ₺217,50 daha az
[   Kapıda Ödeme ile Sipariş Ver       ]
 +₺80 kapıda ödeme ücreti, ₺2.829,99
Bugün --- [ertesi iş günü] --- [+3–7 gün]
```
- Paket satırları 76px; küçük lamba resimleri 1. ve 2. lamba seçimini izler.
- "En avantajlı" üst kenara oturan Lamba sekmedir. Hediye satırı ayrı şerit değil, düz metindir.
- 2'li seçim paketin dışında, hemen altında durur (kart içinde kart yok). 1 Adet seçilince 240ms'de kaybolur.
- Ana buton Lamba dolgu, 56px, fiyat sağda ayrı öğe. Kapıda butonu çerçeveli, 52px. Notlar 13 Sis.

## 6. Sıcaklık
- **Işık mantığı:** amber yalnız ışık olacak yerde. Koyu alt bilgi, koyu yapışkan çubuk ve koyu sayaç kalktı; koyu yalnız 3 bantta.
- **Net yakınlık:** bant = bölüm. İçeride 8/16/24, dışarıda 64.
- **İnsan sesi:** gerçek isimli serif alıntılar, elde tutulan fotoğraf, kısa "sen" dili.
- **Sayfa seçimi hatırlar:** model tavanda, kutu listesinde, 20:45'te ve yapışkan çubukta görünür.

## 7. Öz denetim
**Kaçınılan varsayılanlar**
- **Krem + serif:** ışıktan türeyen tonlar geldi. *Revizyon:* ilk taslaktaki pudra pembe bant Erkek alıcıyı dışlıyor, hazır "bebek odası" paletine benziyordu.
- **Kart kiti:** pencere bölmeleri ve yorum listesi var; gölge yok.
- **Şablon süsü:** büyük harf etiket, başlık sonu amber nokta, "→" ve mono yok. Brifteki "·" dizileri virgül ya da ayrı öğe oldu.
- **Hareket:** her bölümde kaydırınca belirme kalktı. "Bir gece" karuseli dikey raya döndü.
- *Revizyon:* imza önce galerideydi. Gerçek fotoğrafla yarıştığı için Diskler'e taşındı. Kubbe kenarı her banttan tek banda indi.

**Beceri ile kural çelişkileri (kural kazanır)**
- Beceri başlık tipografisini aktif öğe ister. Kural 3 gereği kişilik boyuttan değil yazı yüzünden gelir.
- Beceri kendiliğinden hareketi tek ana indirir. Kural 7, Sihirli'deki 4 küçük döngüye izin verir.
- Brif "büyük Ayluna" ister. Kural 3 gereği 40px kalır.

**Değişmez kurallar:** hiçbiri çiğnenmiyor. Koyu yalnız ışık gösteren 3 bantta. Yer tutucular köşeli kalır. Lamba gerçek kesimdir; yansıma, etiketli disk görselidir. Dokunma alanı ≥48px, amber yazı yalnız koyuda.
**Risk:** ğ ş ı İ desteği önceden sınanır.
