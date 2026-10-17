# Tuval notu · "Ayluna İmza Tasarım" (claude.ai/artifact/CHmRtH4tjbapGmPtuQGsTH)

Kaynak: 15 pano (`project/*.dc.html`, sürüm 1792234746-398d) + `canvas.json` + yerel `ayluna-imza/DEVAM.md`, `RAPOR.md`.
Yerel `ayluna-imza/canvas/Main.dc.html` = tuvaldeki `project/Main.dc.html` (birebir aynı, diff boş).
Tuval başlığı: "Ayluna İmza · Gece Masalı". Not başlıkları: "Tur 2 · Tek ışık", "Tur 3 · İmza sürümü".

## 0. Kullanıcı yorumları
- **Tuvalde hiç yorum dizisi yok** (ArtifactComments read: "No comment threads on this artifact yet").
- `canvas.json` içinde ek/not yok; tek açık seçim sinyali pano başlığı: **"Mobil · LunaDream ürün sayfası (seçilen)"** = Main.
- Kodda kullanıcı isteği izi: hem Main hem Imza'da `<!-- Sihirli Özellikler (yeri korunur) -->`
  → canlı sitedeki "Sihirli Özellikler" bölümü ve yeri kullanıcı isteğiyle korunuyor.
- Yorum yerine geçen kullanıcı sinyalleri (yerel DEVAM.md'den, tuval yorumu değil):
  - Sevmedikleri: "emoji ikonlar, boğucu/çok yazılı sayfa, Shopify teması gibi sıradan düzen, tamamen koyu tema, uydurma sayı/sayaç, abartılı efekt."
  - İstedikleri: "acayip ama sıkmayan" tarz, "doğa gibi uyumlu hareketler", güven, dönüşüm; bundle, "ay sonu fiyat geri sayımı (her ay zam yapıyor)", sosyal kanıt; 15 ürünlü mağaza.
  - 17 Ekim netleştirme: "İnsanların alıştığı kalıplar (emoji fayda listesi, indirim sayacı, "dün satılan", stok alarmı) atılmaz; iyileştirilir." Baskı unsuru istiyor ama gerçek veriye bağlı. "Gösteriş/yeniden kurgu değil, işe yarayan iyileştirme bekliyor."
  - Main'e son yapılanlar (DEVAM): emojisiz ince özellik şeridi, küçük model kartları (Flow krem stüdyo görselleri), sade paket satırları ("Kardeşe" rozeti, "En çok tercih" kaldırıldı), ince ay sonu sayaç şeridi, ödeme seçimi (Kartla öde %5 varsayılan), galeride mağazanın 9 ürün fotoğrafı.
- Çıkarım: Kullanıcı Tur 2 (Isik, Bricolage) ve Tur 3 (Imza, büyük bloklar/paralaks) yerine **Tur 1 Main'i** seçti ve onu
  sadeleştirerek (küçültüp, inceltip) geliştirdi. Yani: Young Serif + krem/lacivert/amber dili, kompakt karar levhası, gerçek fotoğraf.

## 1. Pano sırası ve rolleri (canvas.json `order`)
Urun3 (v3, Hatch temizliği + paket) → Urun2 (v2 sade iskelet) → **Main (seçilen, 390×6600)** → Fikir1 Canlı Fiş → Fikir3 Yorum Gökyüzü →
Fikir2 Tavan Çarkı → Anasayfa (Bir gece) → **Isik (Tur 2, 4500)** → FikirC Hangisi onun? → FikirB Kapıya kadar → FikirA Tavana yansıt →
**Imza (Tur 3, 6900)** → T3Fikir3 Anne notları → T3Fikir1 Kutuyu aç → T3Fikir2 Kardeşin gecesi. Hepsi 390px mobil.

## 2. Main · tasarım sistemi (birebir değerler)
### Renkler
| Rol | Hex |
|---|---|
| Sayfa zemini (krem) | #F6F1E9 |
| Yüzey / koyu üstü metin | #FFFDF9 |
| Ana metin, buton, seçili kart | #1A2142 (hover #2B3463) |
| Gece bant / body / yapışkan bar (rgba(20,26,54,.96)) | #141A36 |
| En derin gece (sahne zemini, plak) | #0C1027 |
| Disk sahnesi radyal merkez | #232B55 |
| Amber ışık (koyu üstü CTA, radyo noktası, logo ayı) | #F2A65A |
| Koyu amber (yıldızlar, ikon vurgusu, disk halkası) | #E59A4C |
| Sayaç rakamı | #B4651F |
| Etiket metni kahve / etiket zemini | #8A4A12 / #F3E9DA |
| İkincil metin | #5C6078 ; koyu ikincil #3A3F5A ; büyük harf etiket #8A7F6E |
| Koyu zemin üstü soluk | #B9BED6 ; bant metni #EDE5D8 ; footer metni #C9CDE0 ; telif #8E94B3 |
| Çizgiler | #E3D8C7 (ana), #EDE3D3 (kart kenarı/görsel boşluğu), #DDD2C1 (chip/input), #D9CDB9 (tutamak, kesik çizgi), #C9BFAE (boş radyo/ek ürün) |
| Model foto zemini | #EFE6D8 |
| Yeşil (Stokta, %5 rozeti, "Kartla öde" bağlantısı, WhatsApp satırı) | #2E6B4F ; nokta #3B8A63 |
Sahne örtüsü: `linear-gradient(180deg, rgba(12,16,39,.55) 0%, rgba(12,16,39,0) 22%, rgba(12,16,39,0) 60%, rgba(12,16,39,.72) 100%)`.

### Yazı
- Gövde: **Onest** 400/500/600/700, 15px / 1.5, antialiased. Rakamlar `font-variant-numeric: tabular-nums`.
- Başlık: **Young Serif** 400, `.ser` letter-spacing -.01em. Google Fonts: `family=Young+Serif&family=Onest:wght@400;500;600;700`.
- H1 "LunaDream": 50px / .95, ls -.03em, nowrap, harf harf yükselir.
- `.h2`: 30px / 1.06, ls -.02em, `text-wrap: balance`. Footer h2 28px. Form başlığı 20px serif. İade kartı başlığı 21px/1.15.
- Alt başlık 14px #5C6078. Bölüm etiketi (Model/Paket/Ödeme): 11px BÜYÜK HARF, ls .12em, #8A7F6E; sağ değer 12px 600.
- Özellik şeridi 11.5px/1.25 #3A3F5A; kart adı 13.5px 600; alt 11.5–12px; paket fiyatı 17px 700 ls -.02em; CTA 17px 600.
- An kartı saati 34px serif amber; yorum alıntısı serif 16/1.3; dev "Ayluna" 104px / .8, ls -.045em, #F3E9DA.

### Köşe, boşluk, gölge
- Radius: 999 (chip, rozet, sayaç rozeti) · 28 üst (levha) · 22 (an kartı, disk sahnesi) · 20 (avuç görseli, iade kartı) · 18 (form, video kartı, ürün kartı, yapışkan bar üstü) · 16 (CTA, yorum kartı) · 14 (model/paket/ödeme/ek ürün kartı, UGC foto) · 12 (galeri karesi, sayaç şeridi, input) · 10 (model foto, küçük görsel) · 7 (onay kutusu).
- Kenar boşluğu 16px (`.px`). Bölüm üst boşluğu 48 (çoğu), 40 (iade), 44 (SSS), 52 (diğer ürünler); koyu bant 40/44. Levha içi aralıklar 22/18/12/10/8. Izgara gap 8–10.
- Dokunma hedefi ≥44px; CTA min 58px; input min 50px, 16px yazı (iOS zoom yok).
- Gölge az, çoğunlukla 1–1.5px çizgi kullanılır. Var olanlar: yüzen disk `0 12px 20px -8px rgba(0,0,0,.65), 0 0 0 2px rgba(255,253,249,.3)`; plak `0 0 0 1px rgba(255,255,255,.08), 0 30px 50px -20px rgba(0,0,0,.7)`; oynat düğmesi `0 10px 24px -8px rgba(0,0,0,.6)`; disk düğmesi `0 6px 10px -6px rgba(26,33,66,.6)`; odak halkası `0 0 0 3px rgba(242,166,90,.35)`.

### Hareket
- Tek eğri **cubic-bezier(.2,.7,.2,1)**; arayüz süreleri .15s (buton), .2s (seçim/basma), .25s (kenar/zemin), .3–.35s (kart, ilerleme çubuğu), .45s (menü çekmecesi), .55s (harf), .6s (anahtar rengi).
- Basma: `.btn:active scale(.985)`, kartlar `scale(.98)`, kare `scale(.94)`.
- Sahne ışığı: rAF ile easeInOutQuad; açılışta 900ms sonra 3600ms gündüz→gece, anahtarla 2400ms.
- Sonsuz döngüler (Main'de var, Imza'da kaldırılmıştı): yüzen disk `suz` 7s (−12px, +10°), iade mührü 26s dönüş, plak görseli 40s dönüş, CTA `nefes` halkası 2.8s (2px #F2A65A, inset −5px, scale 1.035).
- Kaydırmaya bağlı (`animation-timeline: view()`, destek yoksa statik): `.rv` 40px yükselip belirme (entry 0–cover 30%), `.kalk` perspective rotateX(34°)+56px+scale .94 → düz, `.harf` dev yazı harfleri %80 aşağıdan, `.buyut` kapanış görseli 1.2→1.
- Ürün kartları `kartGir` .5s, 0.06s kademeli. `prefers-reduced-motion`: hepsi kapalı.

## 3. Main · bölüm sırası (yukarıdan aşağı)
1. **Menü çekmecesi** (gizli): 322px soldan kayar, perde rgba(12,16,39,.55); "KATEGORİLER" Çocuk odası / Projektör / Nemlendirici / Ambiyans (52px görsel + "N ürün"); "Tüm ürünler · 15"; Kargo takip / İade ve değişim / WhatsApp destek.
2. **Sahne 500px** (#0C1027): üstte şeffaf başlık 58px (menü, amber ay + "Ayluna" 21px serif, sepet). Sol üstte ışık anahtarı + saat "19:30"→"21:00" (yalnız 1. karede). Altta 48px kare küçük resimler (yatay kayar) + "1/11" sayacı.
   Galeri 11 kare: Odada (gündüz/gece geçişli), Model (seçili modele göre), sonra mağazadan 9 foto: Masalsı gece ışığı, Müşteri, Temalar, Yorum, Gece modu, Deniz altı, Yorumlar, Hediye, Uzay Kaşifi. Gece olunca 4 disk karosu süzülür.
3. **Karar levhası** (`#siparis`, sahnenin üstüne −30px biner, 28px üst köşe, 40×4 tutamak):
   - "★★★★★ **4,7** · 62 yorum" (→#yorumlar) | yeşil nokta "Stokta".
   - H1 "LunaDream" + "Masal projeksiyonlu gece lambası".
   - Özellik şeridi 4 sütun, ince çizgi ikon: "Yumuşak ay ışığı" · "12 masal diski" · "Bluetooth ninni" · "Şarjlı, taşınabilir".
   - MODEL etiketi + seçili ad ("Kız · tavşanlı"/"Erkek · Uzay Kaşifi"); 2 sütun 68px kart: "Kız" "Tavşanlı · ninnili" / "Erkek" "Uzay Kaşifi".
   - PAKET ("Hediye diskler dahil"): 64px radyo satırları: "1 lamba" "%15 indirim" ₺1.699,99 ~~₺1.999,00~~ ; "2 lamba" [Kardeşe] "adet ₺1.375 · ₺1.248 kazanç" ₺2.749,99 ~~₺3.998,00~~. Varsayılan 2 lamba. Seçili satır lacivert dolgu.
   - Sayaç şeridi 38px: ay simgesi + "Ekim fiyatı bitiyor" | "14g 05:12:33" (son 3 günde "Son 3 gün: Ekim fiyatı" / "Son gün: Ekim fiyatı").
   - Birlikte al satırı 56px: onay kutusu + görsel + "+ Yıldız Işığı Nemlendirici" "+₺849,99".
   - ÖDEME: 2 kart "Kartla öde" [%5 indirim, yeşil] indirimli fiyat + üstü çizili tam fiyat ; "Kapıda öde" tam fiyat. **Varsayılan Kartla öde.**
   - CTA (nefes halkalı): "Kartla öde · ₺2.612,49" veya "Kapıda ödemeyle al · ₺2.749,99"; altında kargo satırı; kapıda seçiliyse yeşil alt çizgili "Kartla öde, ₺138 daha az öde".
   - Kapıda formu (CTA ile sayfa içinde açılır): "Teslimat bilgileri" | "Kart bilgisi istemiyoruz"; Ad soyad (Ayşe Yılmaz), Telefon (05XX XXX XX XX), İl (81 il select), İlçe (Kadıköy), Açık adres; "Kapıda ödenecek · 2 lamba" tutar; "Kartla öde, ₺X daha az öde"; amber "Siparişi tamamla · ₺…" (gönderince "Önizleme: siparişin alındı"); yeşil "Siparişin WhatsApp'tan onaylanır, sonra kargoya verilir".
   - Güven satırı 3 sütun: "Ücretsiz kargo" · "Güvenli ödeme" · "30 gün iade".
   - UGC şeridi: "★ 4,7 · 62 yorum — anneler fotoğraflarını paylaştı →" + 5 müşteri fotoğrafı 120×150.
4. **Bir gece, beş an** (#141A36 bant): "Nasıl kullanılır" (amber) / "Bir gece, beş an." / "Kaydır →"; 5 ilerleme çubuğu; 280×460 kartlar (aktif değilse scale .94, op .7), ortada "VİDEO YUVASI":
   20:00 "Işığı yak" "Sıcak, göz yormayan ay ışığı." · 20:30 "Diski tak" "Kubbeyi aç, bu gecenin masalını seç." · 20:45 Kız: "Ninniyi çal" "Telefondan bağla, lambadan çalsın." / Erkek: "Robotu tavana çevir" "Uzay Kaşifi yıldızları tavana saçar." · 21:00 "Tavanda masal" "Yıldızlar döner, gözler kapanır." · 07:30 "Şarja tak" "Akşam yine hazır." · son kart "Bu gece başlasın" + amber "Kapıda öde · ₺…".
5. **Yorumlar** (#yorumlar): "Anneler ne diyor" + 30px "4,7" / "62 yorum"; chip filtre Tümü/Uyku/Hediye/Kalite; 2 sütun duvar, her 3. kart lacivert; "62 yorumun hepsini oku".
6. **Disk plakları**: "On iki masal,<br>tek lamba." / "Her diskte başka bir masal. Seç, yakından bak."; 300px koyu sahne, amber hale, 210px dönen plak, "Seçili disk" + ad, "2 / 12"; 12 disk düğmesi (58px, seçili amber halka + 6px yukarı); "Kutuda 6 disk var; her siparişe 6 hediye disk ekliyoruz." Varsayılan disk Okyanus.
   Diskler: Ay ve yıldız, Okyanus, Uzay, Deniz kızı, Denizanası, Şato, Hayvanlar, Gökkuşağı, Kış gecesi, Taşıtlar, Masal, Doğum günü.
7. **Avucuna sığar**: "Avucuna sığar, kutusu dolu gelir." 160×220 elde görsel; Boyut "[X] cm", Pil "[X] saat"; "Komodine de sığar, yatağın yanına da taşınır."; kutu satırı "1 tavşanlı lamba · 6 disk · +6 hediye · USB kablo" (modele göre).
8. **Annelerin çektiği videolar** + "Instagram →": 3 yuva 200×356: "Uyku öncesi ritüel", "Karanlık odada LunaDream", "Kutudan ilk çıktığı an".
9. **İade mührü** (lacivert kart): dönen halka yazısı "30 GÜN İADE · KAPIDA ÖDE · ÜCRETSİZ KARGO · ", ortada "30 GÜN"; "Önce gör, sonra öde." / "Beğenmezsen 30 günde geri gönder."
10. **SSS** "Merak edilenler" (6): Bluetooth hoparlör hangi modelde? / Kaç yaş için uygun? / Işık çocuğu rahatsız eder mi? / Kargo ne zaman gelir? / Kapıda ödeme nasıl oluyor? / Beğenmezsem iade edebilir miyim?
11. **Diğer ürünler** (#dunya): "Odanın geri<br>kalanı için" + "13 ürün"; kategori chip'leri; 166px kartlar, amber % rozeti. 13 ürün, mağaza fiyatlarıyla (Nemlendirici ₺849,99… Retro Mini Pikap ₺1.499).
12. **Kapanış + footer** (#141A36): 340px gece görseli (kaydırınca 1.2→1), "Bu gece ilk masalı<br>birlikte izleyin." + amber "Kapıda ödemeyle al · ₺…"; Mesafeli Satış Sözleşmesi / KVKK / İade Politikası / İletişim; ETBİS [QR]; "[Firma unvanı] · [Adres] · WhatsApp: [numara]"; dev "Ayluna" + ay; "© 2026 Ayluna".
13. **Yapışkan bar** 68px: model küçük resmi, fiyat (seçili ödemeye göre), amber "Bu fiyat 14g 05:12", 150px amber buton "Kartla öde"/"Kapıda öde".

## 4. Main · etkileşim ve fiyat mantığı
- Başlangıç state: frame 0, model 'kiz', bundle 2, **pay 'online'**, disc 1, topic 'Tümü', addon false, form false.
- **Model**: Kız/Erkek → galeri 2. kare, yapışkan bar görseli, "Bir gece" 20:45 kartı, kutu satırı, MODEL etiketi değişir. (Sahnedeki oda fotoğrafı her iki modelde aynı tavşanlı oda.)
- **Paket**: `BUND = [{1 lamba, p 1699.99, cmp 1999}, {2 lamba, p 2749.99, cmp 3998, Kardeşe}]`. Yüzde = round((1−p/cmp)·100) → %15 / %31. Adet = p/n kuruşsuz → ₺1.375. Kazanç = cmp−p kuruşsuz → ₺1.248. Yorum: "Fiyatlar tek yerde: Shopify'da price + compare_at_price. Yüzde ve tasarruf otomatik hesaplanır, zamda elle düzeltme yok."
- **Ek ürün**: total = paket p + (ek ? 849.99 : 0).
- **Ödeme**: online = round(total·0.95·100)/100. Tasarruf = total − online (kuruşsuz).
  1 lamba: ₺1.699,99 / kart ₺1.614,99 (₺85) · +ek ₺2.549,98 / ₺2.422,48 (₺128)
  2 lamba: ₺2.749,99 / kart ₺2.612,49 (₺138) · +ek ₺3.599,98 / ₺3.419,98 (₺180)
  Kapıda seçince CTA formu açar; Kartla öde seçince form kapanır (önizlemede ödeme sayfası yok). "Kartla öde, ₺X daha az öde" tek dokunuşla online'a döndürür.
- **Sayaç**: hedef = içinde bulunulan ayın son günü 23:59:59.999 (yerel), 1 sn'de bir güncellenir. calLeft ≤ 3 → "Son N gün"/"Son gün". Gerçek aylık zam olduğu varsayımına dayanır.
- **Kargo satırı**: hafta içi 16:00 öncesi "Bugün kargoda: 3 sa 20 dk içinde sipariş ver", değilse "19 Ekim pazartesi kargoda" (sonraki iş günü).
- **Galeri**: küçük resme dokun → opacity .4s geçiş; ışık anahtarı yalnız "Odada" karesinde.
- **Yorum filtresi**, **kategori filtresi**, **disk seçimi**, **an kaydırma** (scrollLeft/292 → aktif kart + ilerleme çubuğu), **SSS** `<details>`.
- Tutarsızlıklar: "Bu gece başlasın" ve kapanış CTA'sı ödeme seçiminden bağımsız hep "Kapıda öde" + indirimsiz fiyat söyler ve formu açar (pay=online iken bile form görünür). Yorum satırı "6 kare" diyor, gerçek 11. Menü "Tüm ürünler · 15", listede 13 ürün.

## 5. Main'in diğer panolardan farkı
### Imza (Tur 3 · "yeni görseller + hareket") → Main'de olmayan/farklı
- `.h2` 40px/1 ls −.025em (Main 30px). Footer h2 34px.
- Hareket manifestosu: "yalnız transform + opacity, tek eğri, **sonsuz döngü yok**"; üç aile: yükselen harf, kaydırmayla oturan görsel, kaydırmayla dönen daire. Main sonsuz döngüleri korudu (yüzen disk, mühür, plak, nefes).
- Galeri 5 kare (Odada, Elde, Yakın, Tavanda, Müşteri), modele göre **ayrı oda çifti** (Erkek için kendi gündüz/gece odası); sahnede yüzen disk yok.
- Başlık altında ayrı fiyat satırı (30px serif ₺1.699,99, ~~₺1.999,00~~, lacivert %15) + "Kapıda ödeme · Ücretsiz kargo · 30 gün iade".
- "Sihirli Özellikler" başlıklı 2×2 kartsız liste (Mışıl mışıl uyku/Sıcak, yumuşak ışık; 12 masal diski/6'sı hediye; Ninni hoparlörü/Kız modelinde; Şarjlı, kablosuz/Her odaya taşınır).
- Model: büyük foto kartlar (128px foto, tik rozeti, "Kız Çocuklar İçin"/"Erkek Çocuklar İçin").
- Paket: amber üst bant "Kardeşe · adet başı en avantajlı", "₺1.375 / adet", seçilince "+6 hediye disk · ₺1.248 kazancın".
- Sayaç büyük blok: 52×44 rakam kutuları (gün/saat/dk, son 3 günde +sn), "Ekim fiyatı bitiyor — Kasım'da fiyatlar güncelleniyor"; son 3 günde amber zemin.
- Ödeme seçimi yok; yalnız formda "Online öde, %5 indirim kazan". CTA nefes halkasız. CTA altı yalnız WhatsApp satırı.
- 580px paralaks "Ürün sahnesi" ("Her disk,<br>başka bir gece." / "12 masal diski · kutuda 6, hediye 6. Birini seç.") + gece zeminli disk seçici (kaydırmayla dönen plak).
- Bir gece: 3B ray (rotateY ±14°), 260×440, oynat yalnız aktifte.
- Yorumlar: 96px amber tırnaklı büyük alıntı ("Reklamında nasıl ise aynısı, hatta daha iyisi."), kartsız çizgili liste, "Tüm yorumları oku"; "Annelerin çektikleri" (3 video + 2 foto) yorumlarla birleşik. İade mührü SSS başlığına birleşik, SSS 5 soru.
- Main'in Imza'dan aldığı/ortak: sahne + ışık anahtarı + levha, harf harf LunaDream, kapıda formu, ek ürün satırı, iade mührü, diğer ürünler, dev "Ayluna" footer, yapışkan bar.
### Isik (Tur 2 · "Tek ışık, eleştirmen revizyonlu")
- **Bricolage Grotesque** 600 başlık (ls −.03em) + Onest; 20px kenar; üstte duyuru şeridi "Kapıda nakit ya da kartla öde"; başlık sahnenin üstünde değil.
- 420px "imza an" sahnesi: dokun/kaydır, story çubukları, önce oda kararır sonra lamba yanar, diskler ışık noktasından açılır.
- H1 vaat: "Işığı kapat, tavanda masal başlasın."; alt "LunaDream · masal projeksiyonlu gece lambası"; fiyat 28px + "%15 indirim" (#B5651D).
- İkonsuz 3'lü değer şeridi (12 masal diski / Şarjlı kablosuz kullanım / modele göre); model 64px yuvarlak; paket varsayılan 1 lamba; sessiz sayaç cümlesi "Fiyatlar her ay güncellenir · bu fiyat 31 Ekim'e kadar · …"; yapışkan bar krem ve ana buton görünmezken gelir.
- Bölümler: Odalardan gelenler, Bir gece beş an (240×380), statik disk ızgarası (Kutuda/Hediye), Kutuda listesi, Sorular, Odanın diğer ışıkları. **Main bu yönü almadı** (Young Serif ve kompakt levha kaldı).
### Urun2 (v2 · "sade iskelet")
- Krem başlık, 452px dokunmalı galeri + çubuk + 56px küçük resim; "PROJEKSİYONLU GECE LAMBASI" üst etiketi; H1 48px; fiyat + % hap; **segment** model seçici ("Tavşanlı · Kız"/"Robotlu · Erkek"); tek kartta paket satırları ("₺1.248 kâr"); **hap buton (radius 999)** "Kapıda öde · ₺…"; "Bugün kargoda · Fiyat 31 Ekim'e kadar sabit".
- Tek görsel tek cümle "Işığı kapat.<br>Masal başlasın." 44px; "Tek lamba, üç hâl." (Gece lambası / Tavan projektörü / Ninni hoparlörü); koyu bantta dev "12" + sonsuz disk kayan şeridi (46s); tek yorum karuseli + 64px "4,7"; "Bu gece başlasın." kapanış.
- Main'e geçen: renk paleti, Young Serif + Onest, 1/2 lamba fiyatları, "Bu gece başlasın", dev Ayluna footer. Düşen: hap buton, segment, dev 12 bandı, tek yorum karuseli.
### Urun3 (v3 · "Hatch temizliği + paket")
- Beyaz #FFFEFB zemin, #141A36 metin, Shopify/Hatch benzeri düzen; duyuru şeridi "Kapıda ödeme · Ücretsiz kargo · 30 gün iade"; kare galeri + "Kapıda ödeme" etiketi.
- **Emojili fayda listesi** (🌙🎶🔋🎁), renkli ikon dairesi model seçici ("Tavşanlı"/"Robotlu"), "EN ÇOK TERCİH EDİLEN" kurdele, yeşil kazanç + 🎁 etiket; 🚚/🔒 panel "Fiyat 31 Ekim'e kadar sabit · sonra güncelleniyor"; "Online ödemede ek %5 indirim — Nasıl?"; akordeonlar.
- "Uyku vakti,<br>savaş değil masal."; "Üç adımda masal" (Diskini seç / Yuvaya tak / Işığı kapat); "Ailelerin ortak yorumu" özeti; "✓ Doğrulanmış alıcı"; SSS "Soruların mı var? Masal gibi cevaplar."
- Main'de: emojiler ve kurdele atıldı (kullanıcı emoji sevmiyor); paket/kazanç, %5 online, güven üçlüsü, UGC korundu ama sadeleşti.
### Anasayfa ("Bir gece")
- Saat fazlı sahne 19:30/20:30/21:00: "Banyo bitti, pijamalar giyildi." → "Bu gecenin diski seçildi." → "Işık kapandı. Masal başladı."; başlıklar "Uyku vakti savaş olmak zorunda değil." / "Bir disk seç, bir masal seç." / "Her gece tavanda yeni bir masal."
- Satın alma fişi (Bugün sipariş ver → kargoda → kapında öde), "Kapıda ödemeyle al →" Main'e bağlı; Sihirli Özellikler (canlı siteden: Mışıl Mışıl Uykular, Hediye Diskler, "+10.000 Mutlu Anne", Kablosuz Kullanım); "Gündüz bir oyuncak,<br>gece bir masal."; "Gerçek odalardan"; "Anneler ne diyor"; "Ambiyans ve Dekor" kapısı; SSS; dev yazı footer.

## 6. Fikir panoları (her biri 1-2 satır)
- **Fikir1 Canlı Fiş** (satın alma kutusu yerine): seçimler canlı bir "Kapıda ödeme fişi"ne satır satır basılır (disk "dahil", hediye/kargo/kapıda ücreti ₺0), toplam 400ms sayarak değişir, "Bugün kazancın ₺X", sayaç şeridi + nefes CTA. Main'e geçen: nefes halkası, ek ürün satırı, son-3-gün sayaç mantığı; fiş ve emojiler alınmadı.
- **Fikir2 Tavan Çarkı** (disk bölümü yerine): koyu 600px bölüm, tavanda dönen yansıma, 12 disk büyük dönen çarkta, oklar; "masal başına ₺141" etiketi; "Lambayı al ↑". Alınmadı.
- **Fikir3 Yorum Gökyüzü** (yorumlar yerine): ayın ("4,7 · 62 yorum") çevresinde 62 yıldız-nokta, konu chip'i noktaları yakar, 5 müşteri fotoğrafı yıldız. Alınmadı (konu dağılımı 24/16/22 uydurma).
- **FikirA Tavana Yansıt** (Tur 2 diskler yerine): diske dokununca görüntü ışık noktasından büyüyüp tavan dairesine yerleşir (640ms); altta Kutuda/Hediye 6+6 disk.
- **FikirB Kapıya kadar** (buton altı yerine): 4 duraklı zaman çizgisi "Bugün Sipariş ver → Bugün WhatsApp onayı → [tarih] Kargoda → [aralık] Kapıda öde", çizgi 640ms çizilir; "Nakit ya da kartla ödersin · Beğenmezsen 30 gün içinde iade". (RAPOR'a göre yerel index'e teslimat adımları olarak girdi.)
- **FikirC Hangisi onun?** (model seçimi yerine): iki büyük foto kart (Tavşanlı · Ninni hoparlörlü / Uzay Kaşifi · Robot figürlü · hoparlörsüz), seçilmeyen .55 opak; 3'lü bilgi hücresinin sonuncusu modele göre değişir (Ninni ↔ Robot).
- **T3Fikir1 Kutuyu aç** (avucuna sığar yerine): dokununca kapak uçar, lamba ve 6+6 disk kademeli yelpazelenir; "6 masal diski", "+6 hediye disk", "USB şarj kablosu", "Boyut [X] cm · Pil [X] saat".
- **T3Fikir2 Kardeşin gecesi** (kapanış yerine): kardeşin odası (diğer model) gündüz→gece; "Bir lamba, bir oda." → "Kardeşi de aynı masalla uyusun."; amber "2 lamba · kardeşe · ₺2.749,99" + "₺1.375 / adet · ₺1.248 kazancın". 2'li paketi duygusal gerekçeyle satar.
- **T3Fikir3 Anne notları** (yorum listesi yerine): büyük alıntı + chip + üst üste kart destesi (0/−2/+2°), kaydırınca kart sola uçar, "1 / 4" ve oklar.

## 7. Olgular, yer tutucular, doğrulanmamış sayılar
- Fiyatlar (tüm panolarda aynı): 1 lamba ₺1.699,99 (₺1.999,00, %15); 2 lamba ₺2.749,99 (₺3.998,00, %31, adet ₺1.375, kazanç ₺1.248). Ek ürün Yıldız Işığı Nemlendirici ₺849,99 (₺1.099).
- Modeller: Kız = tavşanlı, Bluetooth ninni hoparlörlü; Erkek = Uzay Kaşifi robot, hoparlörsüz (eski panolarda "Robotlu").
- Kutu: lamba + 6 disk + 6 hediye disk + USB kablo. **2'li pakette hediye disk sayısı teyitsiz** (Fikir1 fişi 2'li pakette "12 tema diski · dahil" + "+6 hediye disk · kardeş paketi" yazıyor; Main ve Isik 2'li pakette de "+6 hediye" diyor).
- Yer tutucular: Boyut "[X] cm", Pil "[X] saat", "[yaş] yaş ve üzeri", "[Firma unvanı] · [Adres] · WhatsApp: [numara]", "ETBİS [QR]", Isik'te "[Parlaklık ayarı teyit edilecek]", "Genelde [X] iş gününde", Anasayfa "E-posta: [adres]".
- Teyitsiz: **4,7 · 62 yorum**, "Satın aldı" etiketi, **online ödemede %5**, **16:00 kargo kesimi** (FikirB: "16:00 kargo kesim saati ve 1–3 iş günü teslim süresi mağaza teyidi bekliyor"; RAPOR: index'te 16:00 kaldırıldı, Main'de hâlâ var), "Stokta" (sabit metin, envantere bağlı değil), "Güvenli ödeme", "Parlaklığı lambanın tuşlarıyla kısabilirsin", "30 gün iade" (canlı site 90 diyor, gerçek 30 kabul edilmiş).
- Uydurma/riskli: Anasayfa "+10.000 Mutlu Anne" / "Binlerce ailenin tercihi" (canlı siteden, kanıtsız); "62 yorum · Loox"; Urun2/3 "62 doğrulanmış yorum", "✓ Doğrulanmış alıcı", "62 aile yorumladı"; Urun3 "Ailelerin ortak yorumu" (sentez metin); Fikir3 nokta dağılımı; Fikir2 "masal başına ₺141" (1.699,99/12 = 141,67 → ₺142; RAPOR yerelde düzeltti).
- Ay sonu sayacı ancak her ay gerçekten zam yapılıyorsa dürüst (kullanıcı "her ay zam yapıyor" diyor).
- Görseller gerçek üründen Google Flow (Nano Banana Pro) ile üretildi; galerinin 9 karesi ayluna.shop mağaza fotoğrafı. "VİDEO YUVASI" kartlarında henüz video yok.
- Main'deki ürün listesi 13 ürün (fiyatlar mağazadan); "Ana ürünün V2'si rafta yok."
- Gerçek yorumlar (5): Burak G. "Çocuğum çalıştırmadan uyumuyor, uykuya hemen dalıyor." · Handan B. "Torunum filmlerini kendisi seçti ve onunla uyumaya başladı." · Sevcan Z. "2 tane aldık, gayet sağlam geldi. Paketlenmesi de güzeldi." · Abdülkerim T. "Reklamında nasıl ise aynısı, hatta daha iyisi. Çocuklar için mükemmel bir hediye." · Mehmet C. "Anlatıldığı ve gösterildiği gibi çıktı. Bu kadar iyi olmasını beklemiyordum."

## 8. Kalıcı dersler (yeniden kullanılabilir kurallar)
1. **Dil sabit**: Young Serif 400 başlık + Onest gövde; krem #F6F1E9 / lacivert #1A2142 / amber #F2A65A; koyu yalnız bant ve sahnede (tamamen koyu tema yok). Bricolage (Tur 2) seçilmedi.
2. **İlk ekran = gece sahnesi + üstüne binen krem karar levhası** (−30px, 28px köşe, tutamak). Satın alma kararı levhada, kaydırmadan önce başlar.
3. **Seçimler kompakt**: model 68px satır kart, paket 64px radyo satırı, ödeme 62px kart, ek ürün 56px satır. Büyük foto kart ve renkli bantlar sonradan küçültüldü.
4. **Bölüm etiketi** 11px büyük harf .12em #8A7F6E + sağda seçili değer; ayrı başlık kullanma.
5. **Emoji yok**; ince çizgili (1.6–1.7 stroke) SVG ikon, ilk çizgi amber vurgulu.
6. **Alışılmış satış kalıpları atılmaz, inceltilir**: fayda listesi → 4'lü şerit; dev sayaç → 38px tek satır; "En çok tercih" kurdelesi → küçük "Kardeşe" rozeti.
7. **Fiyat tek kaynaktan**: price + compare_at_price; %, adet fiyatı, kazanç, online indirim hep formülle; kuruşlu ana fiyat, kuruşsuz kazanç/adet.
8. **Ödeme**: Kartla öde %5 varsayılan ve fiyat düşülmüş gösterilir; Kapıda öde ikinci ama eşit görünür; kapıda seçene "Kartla öde, ₺X daha az öde" hatırlatması; kapıda formu sayfa içinde, "Kart bilgisi istemiyoruz", WhatsApp onay satırı.
9. **CTA metni seçime göre değişir ve tutarı taşır** ("Kartla öde · ₺2.612,49" / "Kapıda ödemeyle al · ₺2.749,99"); yapışkan bar da aynı. (Alt CTA'lar da buna uydurulmalı.)
10. **Aciliyet yalnız gerçek veriye bağlı**: ay sonu 23:59:59 sayacı, 16:00 kargo kesimi, Shopify stoğu. Uydurma sayı (10.000 anne, X kişi bakıyor) yok.
11. **Güven CTA'nın hemen altında**: Ücretsiz kargo · Güvenli ödeme · 30 gün iade + müşteri fotoğrafı şeridi; sonra 30 GÜN dönen mührü "Önce gör, sonra öde."
12. **Hareket**: tek eğri cubic-bezier(.2,.7,.2,1), yalnız transform/opacity, 150–600ms; kaydırmaya bağlı efektler `@supports (animation-timeline: view())` içinde; `prefers-reduced-motion` ile hepsi kapanır. İmza anı: ışık anahtarıyla gündüz→gece odası.
13. **Ürünü kullanım anıyla anlat**: saatli "Bir gece, beş an" (20:00–07:30), modele göre değişen kart; gerçek ürün fotoğrafı ve müşteri görseli, video yuvası (muted playsinline loop preload=none + poster).
14. **Model seçimi sayfanın her yerine yayılır** (galeri, an kartı, kutu içeriği, yapışkan bar görseli).
15. **Mağaza tek ürün değil**: menü çekmecesi kategorili, sayfa sonunda "Odanın geri kalanı için" chip filtreli ürün rafı, birlikte al ek ürünü.
16. Mobil kurallar: 390px, 16px kenar, ≥44px dokunma, input 16px yazı, tabular rakam, yatay kaydırmada `scroll-snap` + gizli kaydırma çubuğu.
17. Yer tutucuları köşeli parantezle açıkça bırak ([X] cm, [yaş], [numara]); teyitsiz bilgiyi gerçekmiş gibi yazma.
