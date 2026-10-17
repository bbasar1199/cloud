# Dengen / Dengem dersleri → Ayluna için

Kaynaklar: 8 artifact (salt okunur) + `origin/claude/friendly-heisenberg-zalr24:dengen-evre/*.liquid` + `git log --all`.
Yöntem: sürüm başlıkları, sürüm zaman damgaları, CSS katman yorumları (`/* v12 (Smooche-structured PDP) */` gibi) ve metin karşılaştırması.
UYARI: 8 artifactin hiçbirinde yorum dizisi yok. Yörüngedeki geri bildirimler başlıklardan ve değişikliklerden ÇIKARIMDIR, kullanıcının kendi cümlesi değildir.

## 0. Kronoloji (sürüm zaman damgasından, UTC)

| Tarih | Artifact | Ne |
|---|---|---|
| 29 Eyl | Dengem — Denge Yağı (v7, sıcak, ürün önce) | Krem/amber/yeşil, Plus Jakarta Sans, çizim (SVG) şişeler, v5/v6 modül katmanları |
| 3 Eki | Dengen A+ — Ürün v14 (az yazı) + Tasarım gezgini | A nane-beyaz ile B sıcak adaçayı yan yana; v10 → v13 "corporate layer" → v12 "Smooche yapısı" → v14 |
| 4 Eki 09:19 | Denge Kremi (tek ekran karar sayfası) | Manrope+Inter, kâğıt/nane/yeşil/mercan; hepsi ilk ekranda + yoğun aciliyet |
| 4 Eki 10:59 | Tasarım dili seçimi (A/B/C) | Aynı sayfa, 3 palet |
| 4 Eki 11:05 | Tasarım dili: AG1 ve Kindra sistemi | 6 dk sonra: "Gerçek markaların sistemi, bizim ürünle." |
| 8 Eki | Dengen Damla | Ürün damlaya (takviye) döndü; klasik Shopify PDP yapısı, özel serif+sans |
| 14 Eki | Dengen — Denge Çizgisi (Design tuvali) | 390px mobil, yer tutucu veriler, alt sayfa sipariş formu |
| 14 Eki | git: dengen-evre/*.liquid | Canlı temaya gerçek stok, gerçek sipariş rozeti, bitki haritası |
| 17 Eki | git: Ayluna commitleri | "Tanıdık satış kalıpları gerçek veriyle" — aynı dersler Ayluna'ya taşınmış |

Marka adı Dengem → Dengen (3 Eki'den itibaren). Ürün: Denge Yağı → Denge Kremi → Dengen Damla / Evre.

## 1. Tasarım sistemi belgeleme yaklaşımı (AG1/Kindra sayfası = şablon)

Sayfanın iddiası (üst metin): "AG1 ve Kindra'nın sitelerine girdim. İkisinin ortak noktası: palet ambalajdan gelir, tek vurgu rengi vardır."
Biçim: yatay kaydırmalı kartlar (`flex: 0 0 min(86vw,380px)`, `scroll-snap`), her kart = bir sistem. "Aynı sayfa, aynı fotoğraf. Fark sadece renk ve vurgunun nereye düştüğü."

Her kartın başlığı (sistem kimliği):
- Harf + ad ("D · AG1 sistemi", "E · Kindra sistemi", "A · Zümrüt ve fildişi")
- Tek cümle karakter ("Derin yeşil, beyaz, tek limon yeşili düğme. Kalın sans başlık. Fotoğraf öne çıkar.")
- 5 renk yuvarlağı, `title` içinde hex
- Referans satırı + neden ("Referans: AG1 (milyar dolarlık tek ürün markası)"; "Kindra (7.000+ doktor önerisi, menopoz)")

Token sözlüğü (her palet bunları doldurur; rol adıyla, renk adıyla değil):
`--bg --soft --ink --brand --hair` (zemin, galeri zemini, metin, logo, çizgi)
`--ann/--annt` duyuru bandı, `--badge/--badget` rozet, `--star` yıldız, `--rib/--ribt` "EN ÇOK TERCİH" şeridi,
`--cta/--ctat` ana düğme, `--stripbg/--tick` tik şeridi, `--dark/--darkacc` koyu kanıt bloğu + vurgu,
`--btn2/--btn2t` ikincil düğme, `--r` köşe yarıçapı.
Palet farkı CSS'te tek satır: `.pal-d{--bg:#fff;--ink:#0B1F1C;--brand:#0B3B36;--cta:#C8F560;...;--r:12px}` + gerekirse 1–2 istisna (`.pal-d .cta{border-radius:999px}`).

Somut değerler:
- D · AG1: #0B3B36 derin yeşil, #FFFFFF, #C8F560 limon (CTA, rozet, koyu blok vurgusu), #F2F5F3 galeri, #0B1F1C metin; r 12px, CTA hap (999px).
- E · Kindra: beyaz, #1F5F58 marka, #E4F25C limon CTA, #CFE6DF nane güven bandı + tik şeridi; h1 Cormorant Garamond 600 1.95rem/1; CTA hap.
- A · Zümrüt-fildişi (önceki öneri): #1F5F58, #123F3A, #D3B26A altın, #FBF8F2 krem; r 8px.

Tip ölçeği (mock içinde): başlık Plus Jakarta Sans 800, h1 1.5rem/1.05 −0.03em; etiketler .52–.72rem BÜYÜK HARF +.08–.14em; istatistik 1.8rem 900; gövde Inter 400–700.

Bileşen envanteri (her palette aynı sırayla işlenir — test sayfası gibi):
duyuru bandı → header/logo/sepet → galeri + "Çok satan" rozeti → yıldız satırı + yorum sayısı → H1 vaat → ürün adı/hacim/gün → 3 satırlı paket seçici (seçili satır iç çerçeve + üst şerit) → form alanları (Ad Soyad, Telefon) → fiyatlı CTA ("KAPIDA ÖDEMEYLE SİPARİŞ VER · 1.490 ₺") → mikro güven satırı → tik şeridi → koyu kanıt bloğu (%84 / %79 istatistik) + ikincil düğme → alıntı kartı.

Ek iyi pratik (Damla `:root`): her token yanında Türkçe ROL + KISIT yorumu:
`--accent:#B9573A; /* kiremit — sadece rozet */`, `--sage /* duyuru bandı */`, `--gold /* yıldız */`, `--green /* ana koyu (buton) */`.
Denge Çizgisi (en yeni) fiili sistem: zemin #E8E3DC, beyaz kart, #223F3A koyu yeşil (marka/başlık), #141C19 metin, #117A56 sipariş düğmesi, #F5B800 yıldız; Newsreader (serif başlık) + Instrument Sans (gövde); gövde 13–17px; köşe 12/10/6px; max-width 480px.

## 2. Referans markalar ve katkıları

| Referans | Nerede | Katkı |
|---|---|---|
| AG1 | Sistem D | Tek ürün markası disiplini: derin yeşil + beyaz + TEK limon düğme; kalın sans; fotoğraf öne |
| Kindra | Sistem E, A | Menopoz kategorisinin dili: beyaz, serif başlık, limon düğme, nane güven bandı; doktor önerisi otoritesi |
| Bonafide | A, C | Etiket renkleri (zümrüt/fildişi/altın); iki tonlu zümrüt+erik |
| Womaness | C | Kadınsı, ayırt edici ikinci renk (lavanta/erik) |
| Hims & Hers, Ritual | B "Mürekkep ve beyaz" | Siyah-beyaz + tek yeşil tik; "renk fotoğraftan gelir"; en sert, en kurumsal |
| Smooche | v12 "Smooche-structured PDP" | Yapışkan galeri + 6 küçük resim, galeri panelleri (Şişe/Kutu/Set/İçerik/Video), üstte satın alma bloğu, dönüşümlü bloklar, sonuçlar, içerik kartları, fark satırı, teslimat tarihi (bugün + 2 iş günü, hafta sonu atlanır), kargo kesim saati sayacı, scroll'da beliren bloklar |
| Hilma | Gezgin notu "Hilma tarzı hero" | Ürün sayfası hero'su (ayrıntı kaynaklarda yok) |
| Clippiq | — | Bu 8 kaynakta ve git'te hiç iz yok; yalnızca görev metninde geçiyor |

Ortak çıkarım: referans "his" için değil, ölçülebilir sistem için alındı (palet kaynağı, vurgu sayısı, düğme biçimi, başlık fontu).

## 3. Geri bildirim yörüngesi: reddedilen → varılan

Kanıtla, sırayla:
1. **Sıcak krem/amber → klinik beyaz/nane.** v7 "sıcak" (krem #FAF5EC, amber #C98B47). 3 Eki gezgin: "A · Nane-beyaz ... Seçtiğin palet; klinik-temiz, kurumsal." B sıcak adaçayı alternatif olarak kaldı.
2. **Ürün önce.** v7 başlığı "ürün önce": sayfa galeri (Şişe/Kutu/Set/İçerik/Video) + 4,8 yıldız + paket seçici ile açılıyor; hikâye bölümleri aşağıda. Bu sıra sonraki tüm sürümlerde korunuyor.
3. **Uzun metin → az yazı, ama modüller kalsın.** v14 = "kurumsal, az yazı, tüm modüller". Belirtiler tek kelimeye ("Sıcak basması / Gece terlemesi / Bölünen uyku / Şişkinlik"), takvim 4 satıra ("1. gün cilt yumuşar ... 6. hafta ikinci kavanoz"), SSS cevapları tek cümleye indi. v7'de aynı belirtiler açıklamalıydı ("akşama doğru davul gibi karın").
4. **Kurumsal katman.** v13 "corporate layer": köşe 26→18px, ortalı küçük BÜYÜK HARF üst başlık, güven çubuğu, kayan mühür şeridi, numaralı bölümler ("01 · Belirtiler ... 08 · Sorular").
5. **Uydurma/genel palet → gerçek markanın sistemi.** 10:59'da A/B/C (Bonafide, Hers, Womaness'e "yakın marka dili"); 6 dk sonra AG1/Kindra sitelerine girilip "Gerçek markaların sistemi, bizim ürünle"; A "Önceki öneri; karşılaştırma için" diye geriye düştü. Kullanıcı tahmini değil kanıtlı sistem istedi.
6. **Tek ekran karar sayfası denendi, sürdürülmedi.** (4 Eki) Her şey ilk ekranda + "Son 140 kavanoz", "19 kişi bakıyor", geri sayım. Sonraki sürümler uzun, tanıdık PDP'ye döndü (çıkarım).
7. **Özgün kurgu → tanıdık e-ticaret kalıbı.** Damla (8 Eki): kaydırmalı galeri + noktalar, BÜYÜK HARF ürün adı, maddeli faydalar, 3/2/1 paket (3 "en avantajlı"), akordeon, yapışkan sepete ekle, `/cart/add.js → /checkout`. Ayluna commit'i aynı dersi adlandırıyor: "Tanıdık satış kalıpları gerçek veriyle".
8. **Uydurma sayılar → yer tutucu ve gerçek veri.** Erken sürümler: "12.400+ kadın", "%84", "83 sipariş · 19 kişi bakıyor", isimli yorumlar. Denge Çizgisi (14 Eki): `[puan] · [sayı] değerlendirme`, `[fiyat] TL`, `[Ad S.]`, "[Gerçek yorum]". Liquid: stok uyarısı yalnızca gerçek stok ≤25'te, sipariş rozeti elle girilen gerçek 7 günlük sayı, 0 ise gizli.
9. **Serbest sağlık iddiası → mevzuat diline.** Erken: "%85 daha az sıcak basması". Son: "Magnezyum, yorgunluk ve bitkinliğin azalmasına katkıda bulunur", "geleneksel olarak akşam saatlerinde tercih edilir"; altbilgide tam takviye uyarısı; "Yalnızca resmi sitede satılır".
10. **Çizim ürün → gerçek fotoğraf.** v7–v14 ürünler inline SVG çizimdi; Denge Çizgisi `/_blob/...` fotoğraf, Liquid `dengen-sise.webp | asset_url`, Ayluna commit'i "mağaza fotoğrafları".
11. **Masaüstü kompozisyon → mobil kanvas.** Denge Çizgisi 390px artboard, içerik max 480px; sipariş formu ayrı alt sayfa (bottom sheet) çizimi.

Varılan nokta (en yeni iki iş): mobil tek sütun; koyu yeşil + beyaz/krem + tek sipariş rengi; serif başlık + sans gövde; ürün fotoğrafı önde; 3'lü paket "Önerilen"; kapıda ödeme formu (Ad, cep, il/ilçe, açık adres, Nakit/Kartla, "Şimdi ödeme yok. Parayı paketi teslim alırken ödersin."); her blok sonunda "Hemen sipariş ver!" + "30 gün iade garantisi"; gerçek veri, uyumlu dil.

Kalıcı içerik kalıpları (hepsinde tekrar eden, onaylanmış sayılabilir):
- Duyuru bandı / kayan şerit: Ücretsiz kargo · Kapıda ödeme · 30 gün iade · (ürün güvencesi).
- Paket seçici: fiyat + üstü çizili eski fiyat + birim fiyat ("şişesi", "Günde 17 ₺; bir simit, bir çay") + rozet.
- Dürüst takvim (1. gün / 1. hafta / 3. hafta / 6. hafta) — beklenti yönetimi.
- "Kimler kullanmamalı", "Paketin üstünde ne yazıyor? Sadece adınız ve adresiniz", "Ya bende işe yaramazsa?" SSS'leri.
- "Anneniz için mi? Adres onun, telefon sizin" (hediye/başkası için alım).
- Karşılaştırma tablosu (Biz ✓ / Diğerleri ✕ veya "Değişir").
- WhatsApp ekran görüntüsü tarzı yorum, Facebook yorum görünümü.

## 4. Teknik Shopify dersleri (dengen-evre/*.liquid + commitler)

Kurulum modeli
- Her parça "Özel Liquid" bölümüne yapıştırılan tek dosya; başında Türkçe kurulum yorumu (yol: "Ürünler > Dengen Evre > Envanter > 'Miktarı takip et' açık, 'Stokta yokken satışa devam et' kapalı").
- Bölüm kendini doğru yere TAŞIR: `hedef.insertAdjacentElement('afterend', el)`; hedef yoksa yedek hedef (`.pu-ad` yoksa `.pu-st` öncesi). Tema dosyasına dokunmadan yerleşim.
- Renkler tema değişkenlerinden, yedekli: `var(--g,#1C6047)`, `var(--nane,#E8FFF6)`; tema rengi değişince bölüm de değişir.
- Önekli BEM sınıfları (`dgn-stk__`, `dgn-sk__`, `dgn-hm__`) → tema CSS'iyle çakışma yok.

Gerçek stok uyarısı (stok-uyarisi.liquid)
- Koşul: `v.inventory_management == 'shopify' and v.inventory_policy == 'deny' and adet > 0 and adet <= esik` (esik = 25). Değilse müşteriye HİÇ gösterme.
- Doluluk çubuğu `adet*100/esik`, en az %8; `role="status"`; nabız animasyonu `prefers-reduced-motion`'da kapalı.

Sahip önizlemesi (commit d1b10ff)
- Gerçek stok düşük değilse örnek sayı (12) ile render et, ama `hidden` + `data-onizleme`.
- Görünür olduğu yerler: tema düzenleyici (`request.design_mode`) ve `?onizleme=stok` parametresi. JS: `hidden` ve parametre yoksa `el.remove()`.
- Önizlemede kesik çizgili not: "Önizleme: örnek sayı. Bu uyarıyı müşteriler yalnızca gerçek stok 25 şişenin altına düşünce görür."

Editör yeniden yükleme kopyaları (commit d1b10ff)
- Seçici `[data-x]:not([data-ready])` ile yalnız yeni kopyayı al; önce `[data-x][data-ready]` eski taşınmış kopyaları sil; sonra yeniyi `data-ready="1"` işaretleyip taşı. (Taşınan eleman bölüm dışına çıktığı için editör eskisini silmiyor.)
- Etkileşimli bölümde init koruması: `if (root.getAttribute('data-ready')) return;`.

Sosyal kanıt (sosyal-kanit.liquid, commit c4daca4/aaa7871)
- `assign son_7_gun_siparis = 0` → satıcı Analizler > Siparişler (son 7 gün) değerini haftada bir elle yazar; 0 ise blok hiç render edilmez. Başlığın hemen altına taşınır.

Hata dersleri
- Flex `gap` metindeki kelimeleri ayırdı → metni tek `<span>` içine sar (c4daca4).
- Kapsamlı buton sıfırlaması (`.dgn-hm button`) düğümün negatif ortalama margin'ini ezdi → düğüm kuralının özgüllüğünü yükselt (0cb107b).

Bitki haritası (bitki-haritasi.liquid, 5b226ea)
- 7 düğüm şişe etrafında halka: CSS `sin()/cos()`; desteklenmiyorsa JS ile `left/top` hesapla.
- `aria-pressed` düğmeler, `aria-live="polite"` kartlar, ok tuşlarıyla gezinme, önceki/sonraki okları, nokta göstergesi ("1 / 7" sayacı yerine).
- `IntersectionObserver` (eşik .25) ile düğümler sırayla belirir, bir kez; reduced-motion'da kapalı.
- Görsel revizyon: ince çizgi ikon → iki tonlu botanik çizim; şişe taş kaide üstünde, ürün fotoğrafıyla uyumlu; kartlar içeriğe göre boy alır (boş alan yok); etiketler 2 çipe indi.
- Görsel `{{ 'dengen-sise.webp' | asset_url }}`, `width/height`, `loading="lazy"`; altta "Takviye edici gıdadır, ilaç değildir."

Damla sayfasındaki zamanlama kuralları
- Kampanya bitişi = ayın son günü 23:59; kargo kesim 13:00 ("13:00'a kadar siparişler bugün kargoda"); teslimat tarihi bugün + 2 iş günü (hafta sonu atlanır). Sayaç gerçek bir kurala bağlı, sahte döngü değil.

## 5. Kullanıcı yorumları (birebir)

8 artifactin 8'inde de `ArtifactComments read` sonucu: "No comment threads on this artifact yet."
Birebir alıntılanacak kullanıcı yorumu YOK. Kullanıcı tercihine dair tek doğrudan iz, Claude'un yazdığı gezgin metni: "Seçtiğin palet; klinik-temiz, kurumsal." (A · Nane-beyaz).

## 6. Markadan bağımsız kalıcı dersler (Ayluna'ya uygulanacak kurallar)

1. Paleti ambalajdan/ürün fotoğrafından çıkar; ekranda TEK vurgu rengi olsun ve yalnızca sipariş düğmesi + rozet onu kullansın.
2. Token'ları rol adıyla tanımla (`--cta`, `--ann`, `--star`, `--dark`...) ve her birinin yanına "nerede kullanılır / nerede kullanılmaz" yorumu yaz.
3. Sistem önerisini, aynı sayfa ve aynı fotoğraf üzerinde yalnızca token değiştirerek yan yana göster; karar renk/vurgu farkına odaklansın.
4. Referans alırken gerçek markanın sitesine bak ve ölçülebilir öğeleri al (palet kaynağı, vurgu sayısı, düğme biçimi, başlık fontu). "Yakın marka dili" tahmini yetmez.
5. Ürün önce: ilk ekranda ürün fotoğrafı, yıldız + yorum sayısı, vaat başlığı, paket seçici ve CTA. Hikâye aşağıda.
6. Az yazı, tam modül: bölümü kesme, cümleyi kısalt. Belirti/fayda tek kelime, SSS cevabı tek cümle, takvim 4 satır.
7. Kurumsal his için: küçük köşe (12–18px), BÜYÜK HARF küçük üst başlıklar, numaralı bölümler, güven çubuğu, gölgeyi azalt.
8. Tanıdık Türk kapıda ödeme kalıplarını kullan: kayan güven bandı, 3'lü paket "Önerilen" + birim fiyat + eski fiyat, fiyatlı CTA, her bloğun sonunda tekrar CTA + iade satırı, alt sayfa sipariş formu (Ad, cep, il/ilçe, adres, Nakit/Kartla, "Şimdi ödeme yok").
9. Hiç uydurma sayı, yorum veya aciliyet koyma. Bilinmeyen değer köşeli yer tutucu olsun: [fiyat], [puan], [sayı], [Ad S.]. Stok/sipariş göstergeleri yalnızca gerçek veriden; veri yoksa gizle.
10. Her aciliyet öğesi gerçek bir kurala bağlı olsun: kargo kesim saati, ayın son günü kampanya, gerçek stok eşiği.
11. Satıcı için önizleme yolu bırak: `request.design_mode` + `?onizleme=...` parametresi; müşteri görmez; önizlemede "örnek sayı" notu yaz.
12. Özel Liquid bölümleri: tek dosya, başta Türkçe kurulum yorumu, önekli sınıflar, tema değişkenlerine yedekli bağ, kendini hedefe taşıma + yedek hedef, `data-ready` ile kopya temizliği.
13. Kategori mevzuatına uygun dil kullan (Ayluna için: elektrikli ürün/çocuk odası güvenliği, pil, CE beyanı; abartılı uyku iddiası yok). Altbilgide uyarı metni, sayfada "Kimler/ne zaman kullanmamalı".
14. Beklenti yönet: dürüst takvim (ilk gece / ilk hafta / ...), "Ya işe yaramazsa?" SSS'i, 30 gün iade cümlesi CTA'nın hemen altında.
15. Mahremiyet ve hediye: "Paketin üstünde ne yazıyor?", "Anneniz için mi? Adres onun, telefon sizin" gibi alıcıya özel güvenceler.
16. Çizim yerine gerçek ürün fotoğrafı; illüstrasyon yalnızca açıklayıcı modüllerde (bitki haritası gibi) ve fotoğrafla uyumlu (aynı kaide/ışık).
17. Etkileşimli modüllerde erişilebilirlik varsayılan olsun: gerçek `<button>`, `aria-pressed`, `aria-live`, ok tuşları, 44px dokunma alanı, `prefers-reduced-motion`.
18. Mobil önce tasarla: 390px tuval, içerik max ~480px, tek sütun; masaüstü sonra.
19. Font çifti: serif başlık + nötr sans gövde (Newsreader + Instrument Sans gibi); gövde 15–17px, yardımcı metin 13px.
20. Sürüm başlığına kararı yaz ("v14, az yazı", "ürün önce", "Smooche yapısı"); CSS'te katman yorumu bırak (`/* v13 corporate layer */`). Geri bildirim izi böyle okunabilir kalır.
