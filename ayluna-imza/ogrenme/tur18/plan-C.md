YÖN C · Duvar ve Tavan

**1. Yön ve fikir**
Sayfa bir çocuk odasıdır: satın alma ve güven gündüz duvarında (sıcak, açık, dolgulu yüzeyler) durur; lacivert yalnız "tavan" olarak açılır ve orada hep lamba yanar.
Neden bu ürün: LunaDream tavanı masala çevirir, masalı da çocuk seçer (20:30 "Masalı seç"; Handan B.: "Torunum filmlerini kendisi seçti"). "Tavana yansır" her projektörün; "çocuğun seçtiği disk tavanı belirler" yalnız bunun. Anneye ve büyükanneye tanıdık bir oda.

**2. Token sistemi**
Renk
- Duvar `#F7F0EC`: zemin, gül-alçı (çok düşük doygunluk).
- Pembe ışık `#F2DDD6`: ikinci açık alan; duvardaki seçilebilir karolar.
- Gece `#1A2142`: mürekkep, seçili durum, tavan alanları.
- Lamba `#F2A65A`: ana buton, üst şerit, animasyondaki ışık; açıkta yazı olmaz.
- Kehribar `#8F4E15`: açıkta vurgu yazısı (pembede 4,9:1; #A05A1C orada AA'yı geçmiyor).
- Sis `#585C75`: ikincil yazı (≥5:1). Koyuda ikincil yazı Duvar %72.
Krem neden gitti: #F6F1E9 + amber, becerinin "krem + turuncu-pas" uyarısına düşüyor. Gül-alçı sarısız sıcaktır, Kız karuselinin pembesine bağlanır.

Yazı (ikisi de latin-ext, Türkçe tam)
- Literata (kitap yüzü, masal sesi): ürün adı 28, bölüm başlığı 20, saatler 20, "30" 40, yorum alıntısı 15.
- Figtree (arayüz): fiyat 20/600, gövde ve buton 15, açıklama 14, not ve etiket 12. Fiyat ve sayaç tabular-nums.
- Ekran başına en çok üç boyut. Young Serif'in "yumuşak serif = premium" kestirmesi bırakıldı.
- Çelişki: beceri büyük başlık ister; kullanıcı sınırı kazanır, ölçeği fotoğraf ve renk alanı taşır.

Aralık: 4·8·12·16·24·32. Grup içi 4–8, gruplar arası 16–24, alan dolgusu 32, kenar 16. Bölüm arası ek boşluk yok; sınır alan değişimidir.

Köşe: 0 alanlar ve galeri fotoğrafı; 16 fotoğraf ve karolar (içteki küçük resim 8, eşmerkezli); 999 buton, çip, disk.
Çelişki: beceri 12–16px köşeyi zayıf varsayılan sayar; "soğukluk" yüzünden karolarda 16 kalır.

Yüzey: 1px çizgi, kesik çizgi, duran gölge yok. Ayrım tonla: duvarda karo pembe, pembede karo duvar; tek kat. Seçili: Gece dolgu + onay ikonu. Odak: 2px Kehribar halka. Gölge yalnız yüzen yapışkan çubukta. İkon: 24 ızgara, 1,5px çizgi, currentColor.

Eğri: `cubic-bezier(0.22, 1, 0.36, 1)`, her yerde. Basma 140ms scale(.96); durum 180; bölüm girişi 600 (16px, başlık→içerik 80ms ara, bir kez); imza 840. Azaltılmış harekette yalnız 150ms opaklık.

**3. İskelet** (D duvar, P pembe, G gece, L lamba)
Komşu bölümler aynı alanı paylaşmaz (galeri ve ürün başı tek birim): sınır renkle okunur, içerik içte sıkı. İki sol kenar: 16 (başlık, gövde) ve 88 (satırlı bölümlerde metin; soldaki 56px sütunda animasyon, saat ya da rakam). Ortalanan tek an imza sahnesi.

1. Şerit (L): tek satır, gece yazı.
2. Bar + galeri (D): logo üstte, kare foto kenardan kenara, yazı fotoğrafa binmez.
```
☾ Ayluna              [sepet]
████ 390×390 kaydırılır ████
[▫][▫][▫][▫][▫]…        1/9
```
3. Ürün başı (D): sola yaslı yığın; fiyat ilk ekranda (~670px).
```
★ 4,7 · 62 yorum      Stokta
LunaDream
₺1.699,99 ₺1.999,00 %15 indirim
Kampanya · 1–31 Ekim
Ücretsiz kargo · 30 gün iade · Güvenli ödeme
```
4. Sihirli özellikler (P): dört satır liste, kart yok; solda canlı gösterge.
5. Seçim ve ödeme (D): madde 5.
6. Diskler (G): tavan sahnesi, altında seçili modelin kesimi, altında 6+5 disk ızgarası; hepsi görünür.
```
Bu gecenin masalını seç
┌[gerçek tavan fotoğrafı]──┐
│        ( desen )         │
│          lamba           │
└──────────────────────────┘
Okyanus   ○○○○○○ / ○○○○○
Her kutuda 6 masal diski + 6 hediye disk.
```
7. Yorumlar (P): 4 foto tek sıra, çipler, beş alıntı alt alta (karusel yok), not ve "hepsini oku".
8. Videolar (G): 9:16 kartlar (160×284) yatay; başlık kartın altında.
9. Bir gece, beş an: beş tam genişlik satır, her biri kendi alanında; akşam kararır, sabah açılır.
```
20:00 Odayı hazırla      [▪] D
20:30 Masalı seç         [▪] P
20:45 Birlikte dinleyin  [▪] G
21:00 Gözler kapanır     [▪] G
07:30 Sabah şarja        [▪] D
```
10. Kapına ne gelir (P): solda elde tutulan yanan lamba (avuç boyu), sağda rakamlı sayım, altta "2 Adet'te 2 kutu gelir."
11. 30 gün iade (D): tek satır; solda "30", sağda cümle.
12. SSS (P): altı soru, duvar renkli 56px karolar; artı açılınca 45° döner.
13. Odanın geri kalanı (D): 13 ürün yatay, 148px kare foto, ad, fiyat.
14. Alt bilgi (P): "Bu gece masal tavanda başlasın." + buton; 48px yasal satırlar; [yer tutucular]; KDV notu; "☾ Ayluna" 40px.
Yapışkan çubuk (D, gölgeli): küçük resim, kartla fiyat, "2 Kız · kartla", kalan süre, "Satın al"; ana buton çıkınca 240ms ile alttan girer.

**4. İmza an: "Bu gecenin diski"**
Diske dokunursun; disk sıradan kalkıp lambanın tepesine iner, desen oradan tavana açılır. Lamba, satın almada seçili modelin gerçek kesimidir.
- 0ms: disk scale(.96), 2px Lamba halka (kalıcı durağan işaret).
- 0–180: eski desen söner (opacity→0, scale→.96).
- 40–320: disk kopyası lambaya uçar (translate, scale→.4), sonda söner.
- 280–840: yeni desen lamba tepesinden açılır: origin alt orta, scale .15→1, opacity→.92.
- Disk adı 150ms opaklıkla değişir; döngü yok.
Neden satar: ürünün tek vaadini satın almadan önce parmakla yaşatır; 20:30 ritüeli ve Handan B.'nin yorumuyla aynı hareket. 12 diskin değeri elle tutulur (2 Adet'e iter). Beklenen = gelen; kapıda iadeye doğrudan vurur. Gerçek tavan fotoğrafı gelince desenin yerine geçer.

**5. Satın alma bloğu**
```
[▪ Kız           ][▪ Erkek          ]
[▪  1 Adet             ₺1.699,99] P
[   +6 hediye disk     ₺1.999   ]
[▪▪ 2 Adet En avantajlı ₺2.749,99] G
[   Tanesi ₺1.375  ₺649,99 tasarruf]
[   Her kutuda +6 hediye disk  ] L
1. lamba (Kız|Erkek)  2. lamba (Kız|Erkek)
• Stokta son 18 adet
( Güvenli Ödeme İle Al · ₺2.612,49 )  L 56px
  Kartla %5 indirimli · ₺217,50 daha az
( Kapıda Ödeme ile Sipariş Ver )      P 52px
  +₺80 kapıda ödeme ücreti · ₺2.829,99
☾ Bugün   ◐ [ertesi iş günü]  ● [+3–7 gün]
```
- Model: iki karo ("tavşanlı · ninnili", "robot · ninnili"); dokununca iki lamba da o modele döner.
- Paket: canlı yapı; seçili Gece dolgu, alt şeridi Lamba.
- 2'li seçim yalnız 2 Adet'te, 240ms ile açılır; 48px segment.
- Butonlar düz, 3B gölgesiz; etiket seçimle anında güncellenir.
- Teslim: kesik çizgi yerine ay evreleri (hilal, yarım, dolunay), marka adından.

**6. Sıcaklık**
- İnce çizgili beyaz kartların klinik hâli yerine dolgulu sıcak yüzeyler.
- Lacivert hiç boş değil, her koyu alanda lamba yanar; sayfa lamba renginde şeritle açılır.
- Müşteri sözleri kitap yüzüyle, gerçek adlarla, masal gibi okunur.
- Düzensizliğe karşı tek ölçek, iki sol kenar, sabit 8/16/24/32; uzaklığa karşı boşluk değil renk.

**7. Öz denetim**
Kaçtığım varsayılanlar: krem + amber, yumuşak serif, 2×2 çizgili kart ızgarası, 28px lacivert paneller, başlık sonu amber nokta, üst etiket, yorum karuseli, video üstü gradyan, kesik teslim çizgisi, 3B buton, nabız, koyu alt bilgi.
Kurallar: hiçbirini çiğnemiyor. Dikkat isteyenler: (2) iç içe karo yok; (4) 14 bölüm ayrı; (5) koyu yalnız Diskler, Videolar ve Bir gece'nin iki satırında, hepsinde ürün ışığı var; (6) [X]'ler duruyor; (7) döngü yalnız Sihirli'de, ekrandayken; (8) ≥48px, AA hesaplı.
Risk: pembe Erkek alıcıya yabancı gelebilir; Erkek seçilince sahne ve Bir gece fotoğrafları Erkek'e döner. Figtree'nin tabular rakamı denetlenmeli. Becerinin draw.mjs betiği depoda yok; yön elle seçildi.
