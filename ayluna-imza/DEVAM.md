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

## Tur 4 · yeni site başladı (17 Ekim, akşam)
- Kullanıcı kararı: **sıfırdan, benzersiz Ayluna teması.** Hazır tema kopyalanmaz; şu an canlıda ChatGPT ile yapılmış bir sürüm var. İlk iş LunaDream sayfası.
- `canvas/LunaDreamV2.dc.html` tuvale eklendi ("Tur 4"). Main'den farkları:
  - Main'in 8 kusuru düzeltildi; mevzuat düzeltmeleri yapıldı.
  - Galeride "Elif K." ve doğrulanmamış yorum kolajı içeren mağaza posterleri vardı; yazısız ürün sahneleriyle değiştirildi.
  - Zam sayacı `zamSayaci` ayarıyla, varsayılan kapalı.
  - Kampanya şeridine dokununca "Fiyat nasıl?" açıklaması açılıyor.
- Eleştirmenin seçtiği 3 fikir panosu kullanıcı onayı bekliyor:
  - `Fikir4-KapiyaKadar`: tarihli teslim çizgisi
  - `Fikir5-TavanaYansit`: disk seçilince tavanda görünür; gerçek tavan fotoğrafları çekilmeli
  - `Fikir6-HediyeMi`: hediye anahtarı
- Theme Check yerelde kurulabilir: `npm i @shopify/theme-check-node` (scratchpad'e), sonra `node node_modules/@shopify/theme-check-node/dist/cli.js <tema-klasörü>`.

## Tur 5 · "sıkıcı" geri bildirimi (17 Ekim, gece)
- Kullanıcı:
  - ikonlu ya da emojili fayda yok
  - model kartları idare eder
  - galeri ana ürün fotoğrafları olacak
  - "Işığı kapat" yok
  - tasarım hâlâ sıkıcı
  - canlı sitedeki kapıda ödeme ve paket yapısı korunacak
- Canlı sayfa Playwright ile görüldü (`araclar/canli-sayfa.js`).
  - Paket: alt alta 1/2 Adet kartları, "+6 Tane Ücretsiz Hediye Disk", "En Çok Tercih Edilen".
  - Butonlar: "Güvenli Ödeme İle Al" ve "Kapıda Ödeme ile Sipariş Ver".
  - Kapıda ödeme formu uygulamadan geliyor ve **₺80 ücret** ekliyor.
- Tuvale 4 pano eklendi, Main'in sağında (x=1880):
  - B+ (eleştirmenin önerisi)
  - A Masal Kitabı
  - B Gece Postası
  - C Yörünge
- Eleştirmen puanları: B 8, A 5, C 5. A ve C'de kemer/daire kırpması poster yazılarını kesiyor.
- Üretim betikleri `araclar/tuval-uret/` altında. `python3 yonler.py`, ardından `python3 bplus.py`.
- Uyarı: galerideki "Temalar" posterinde unicorn diski görünüyor (kutudan çıkmıyorsa 2 şikâyet var).

## Tur 6 · B+ seçildi, tam sayfa (17 Ekim, gece)
- Kullanıcı: "B+ ile devam et, ama emoji benefit olmalı; önceden animasyonlu bir benefit yapmıştık".
  - Bu blok, "Ayluna Yeni Tasarım" tuvalinin I yönündeki "Sihirli özellikler" (YonI.dc.html).
- Tam sayfa: `canvas/LunaDreamBPlus.dc.html` (üretim: `araclar/tuval-uret/luna_bplus.py`). Tuvalde B+'nın altında (x=1880, y=2200).
- Sihirli Özellikler:
  - 2×2 kart, animasyon ikonun içinde.
  - Kartlar: Mışıl mışıl uykular · 6 + 6 masal (disklere götürür) · Bluetooth ninni (Kız) / Uzay Kaşifi (Erkek) · Kablosuz kullanım.
  - Uydurma "+10.000 Mutlu Anne" ve teyitsiz "21 ışık modu" konmadı.
- Eleştirmenin 3 iyileştirmesi uygulandı:
  - fiyat ilk ekranda
  - animasyon ikonun içinde
  - tekrar budandı ("Bir gece" yeni cümleler, 3 yorum)

## Tur 7 · Sihirli Özellikler sakinleşti (17 Ekim, gece)
- Kullanıcı: "Görsel kısmını diğeri gibi yapalım ama emoji benefit kısmını biraz daha iyileştirelim; renkler vesaire çok boğuyor."
- 3 varyant (`araclar/tuval-uret/sihirli_varyant.py`, tuvalde x=2350–3290, y=2260):
  - V1 Sade beyaz: 6/10
  - V2 Tek vurgu: 4/10
  - V3 Liste: 8/10, seçildi
- Eleştirmenin düzeltmeleri sayfaya işlendi (`luna_bplus.py`):
  - ikon kutusu krem, amber yalnız hareket eden parçada
  - gösterge sütunu 72px, diskler 34px
  - açıklamalar 15px
  - etiket `#A05A1C`
  - gölge yok
  - pil opacity ile söner
  - Erkek satırı "Tavanda uzay"
- Önizleme hatası düzeltildi: `.pg` üstüne dolgu verilirse sayfa 422px oluyordu. Dolgu iç `div`'e verilir.
- Açık: "hayal" bandındaki müşteri fotoğrafının paylaşım izni.
- **Sonra kullanıcı V1'i seçti** ("Sihirli V1 iyi gibi"). Sayfadaki blok V1'e döndü (`luna_bplus.py`):
  - 2×2 beyaz kart, lacivert ikon kutusu + amber ikon
  - gösterge her kartta sağ üstte
  - ay halesi ikon kutusunun arkasında
  - 15px açıklama, `text-wrap: balance`
  - "6 + 6 masal diski · Diskleri gör", Erkek'te "Tavanda uzay"
  - Eleştirmenin V3 için önerdiği renk ve yazı düzeltmeleri V1'e uygulandı.

## Tur 8 · Galeri gece sahnesi oldu (17 Ekim, gece)
- Kullanıcı Main'in galerisini gösterdi: "Görsel kısmı böyle olsun ama bizim ürün görsellerimiz olacak yine".
- `luna_bplus.py` → `.sahne`:
  - gece laciverti zemin, üstte logo
  - kare ürün posteri 390×390, kırpılmaz; alt kenarı geceye karışır
  - 3 hediye diski kenarlarda süzülür (7 sn)
  - küçük resimler ve "1/7" fotoğrafın üstünde
  - altına yuvarlak köşeli levha biner (tutamak, puan, Stokta)
- "Işığı aç" anahtarı ve saat konmadı (17 Ekim kararı).
- Kullanıcı tuvalde alt başlığı ve "hayal" bandını sildi; üreticiye işlendi. Pano yüksekliği 6100.
- "Stokta" canlıda Shopify stok bilgisinden gelir; stok yoksa görünmez.
- Eleştirmen 7/10. Uygulananlar:
  - "Temalar" afişi galeriden çıktı. Kutuda olmayan diskler gösteriyor (unicorn, 2025); afiş düzelince geri gelir.
  - iç disk kalktı; iki disk alttaki karanlık bantta, ekran kenarına yarı taşar
  - şerit sağda solar, sayaç zemini dolu
  - tutamak ve `border-color` geçişi kalktı
  - tuvalde fotoğrafın sol/sağ yarısına dokununca önceki/sonraki
- Canlı temada yapılacak: ana fotoğraf parmakla kaydırılır (scroll-snap) ve sayaç güncellenir; seçili küçük resim görünür alana kayar; diskler ekrandan çıkınca durur (IntersectionObserver); puan Loox'tan gelir, veri yoksa gizlenir.
- Uygulanmadı: yapışkan buton ilk ekranda. Kural: ana buton ekrandan çıkınca açılır.

## Tur 9 · Videolar, yorum duvarı, baskı unsurları (17 Ekim, gece)
- Kullanıcı:
  - robot da ninnili; model seçimi Sihirli'nin altına
  - diskler daha kaliteli
  - odada profesyonel görseller
  - yorum ve video bölümleri
  - üst kısım ve görseller tek parça
  - baskılayıcılar artsın
- Yapılanlar (`luna_bplus.py`):
  - **Üst:** logo bandı fotoğrafın üstünde; sahne 420px; galeri 9 kare (3 oda sahnesi + 6 afiş).
  - **Diskler:** 11 disk mağaza afişinden yeniden kesildi (`araclar/disk/disk_kes.py` → `canvas/diskler/`, tuvale asset olarak yüklendi; id'ler `araclar/blob-yerel.json`). Unicorn/2025 yok.
  - **Sıra:** fiyat → kampanya sayacı → Sihirli → Model → Paket → stok/dün satırları → butonlar.
  - **Erkek:** "Robot · ninnili"; Sihirli kartı "Ninnili robot / Uyku öncesi ninni çalar."
  - **Videolar:** satın alma kutusunun altında, 4 kart; kapaklar mevcut görsellerden, `[video]` yer tutucu.
  - **Yorum duvarı:** puan + yıldız, 5 müşteri fotoğrafı, konu çipleri, kaydırmalı beyaz kartlar (5 gerçek yorum), "Satın aldı" işareti.
- Canlıda bağlanacak veriler:
  - kampanya bitiş tarihi (ayar)
  - stok eşiği (ayar; Shopify envanteri)
  - dünkü sipariş sayısı (Shopify Flow → ürün metafield'i)
  - videolar (blok başına Shopify videosu)
  - Loox puanı ve yorumları
- Eleştirmen sonrası düzeltmeler:
  - SSS "Erkek modelinde hoparlör yoktur" yerine "İki modelde de ninni var"; robotta Bluetooth [teyit] (yer tutucu)
  - stok satırı "Stokta son [X] adet"
  - dün satırı 3'ten azsa gizli
  - yapışkan çubuk "2 Adet · kartla" + "14 gün kaldı"
  - sayaç şeridi "Kampanya 31 Ekim'de bitiyor" (tarih yazılır; yayında varsayılan kapalı)
  - yazılı afişler logo bandının altından başlar; oda sahneleri bandın altına uzanır
  - disk önizlemesinde "Tavanda" yerine "Disk"
  - 2. video kapağı altyazısız kare
  - konu çipi kontrastı yükseltildi
- Canlıda yapılacak:
  - Loox puan dağılımı eklenecek
  - "Satın aldı" etiketi yalnız doğrulanmış yorumda
  - video yoksa Videolar bölümü gizlenir
  - her disk için karanlık odada çekilmiş gerçek tavan fotoğrafı istenecek
- Sorulacak: robotta Bluetooth var mı, ninni dahili mi? Videolar hangileri (dosyalar)? Kampanya bitiş tarihi?

## Tur 10 · Net diskler ve günlük fiyat sayacı (17 Ekim, gece)
- Kullanıcı:
  - "Diskler için yüksek kalite yapmamışsın."
  - "Her gün sıfırlanan sayaç gerçek sayılır, çünkü toptancı zammı gelince hemen zam yapıyorum."
- **Diskler:** 11 disk Real-ESRGAN çizim modeliyle x4 netleştirildi (512px). `araclar/disk/disk_kes.py --sr`, kurulum TASARIM-BILGISI §9'da. Tuvale yeni asset olarak yüklendi; eski Lanczos sürümler silindi (biri izin verilmediği için kaldı, kullanılmıyor).
- **Sayaç:** "Bugünkü fiyat garantisi" + saat:dk:sn, her gece 23:59'da (İstanbul) sıfırlanır. Altında "Toptancı zammı gelirse fiyat ertesi gün güncellenir." Yapışkan çubukta "Bugünkü fiyat: 06sa 39dk".
- Kullanıcıya söylendi: gün içinde zam gelse de o günün fiyatı 23:59'a kadar korunmalı, yoksa sayaç yanıltıcı sayılır.

## Tur 11 · Yazı ölçeği düzeldi (17 Ekim, gece)
- Kullanıcı: "Yazı fontu bazı yerlerde çok büyük, düzensizlik var."
- Sayfada 20'den fazla farklı yazı boyutu (12–100px) ve iki etiket stili vardı.
- Tek ölçeğe bağlandı. Küçülenler:
  - LunaDream 56 → 44
  - bölüm başlıkları 30/26 → 26
  - puan 52 → 40
  - saatler 46 → 40
  - "30" 88 → 56
  - paket adı 24 → 20
  - alt marka yazısı 100 → 72
- Ara boyutlar 13/15'e toplandı.
- "MODEL/PAKET" büyük harf etiketleri diğer bölüm etiketleriyle aynı stile geçti.
- Ölçek TASARIM-BILGISI §4 ve §10'da.

## Tur 12 · Sade başlık, üst sayaç, sıkı aralar (17 Ekim, gece)
- Kullanıcı:
  - LunaDream ve fiyat çok büyük; fiyat satırında üç fiyat vardı.
  - Müşteriye "toptancı zammı" yazılmaz.
  - Fazla boşluk var; bölüm geçişlerinde hafif animasyon olsun.
  - Bir gece beş an görselleri gerekiyor.
- Yapılanlar:
  - **Üst kısım:**
    - en üstte amber şerit "Bugünkü fiyat garantisi 06:17:46", her gece sıfırlanır
    - ürün adı 32px
    - fiyat satırı: fiyat + eski fiyat + "%15 indirim"
    - hemen altında "Ücretsiz kargo · 30 gün iade · Güvenli ödeme"
    - levhadaki ikinci büyük başlık kalktı
  - **Satın alma:**
    - kurdele "En avantajlı"
    - 2'li pakette "₺649,99 tasarruf"
    - kapıda ödeme butonu sakinleşti (15px, ince çerçeve)
    - Model etiketindeki tekrar kalktı
  - **Sıra:** Videolar → Yorumlar → Bir gece → Diskler.
  - **Düzen:**
    - bölüm arası 36px; koyu bölümler yuvarlak köşeli panel
    - kaydırınca hafif geçiş
    - Bir gece kartları 240×320
    - 30 gün paneli krem
    - disk alt yazısı "Diski seç, desenini gör."
    - 07:30 metni "Gündüz şarja tak."
  - **Görseller:** HF ücretsiz kotası dolu; `araclar/gorsel/bir_gece_uret.py` hazır, `HF_TOKEN` ortam değişkeni eklenince çalışır. 20:30 için mevcut "kubbesi açık" görseli kalır.
- Eleştirmen 7/10. En beğendiği 3 fikir:
  - ödeme ikilisi
  - teslim tarih çizgisi
  - disk seçici
- Açık sorular:
  - varsayılan paket 2'li mi kalsın (yapışkan çubukta ₺2.612,49 görünüyor)?
  - 2'li pakette hediye disk sayısı

## Tur 13 · Ölçek v3, az yazı, Kız + Erkek paketi, eleştirmenin 26 maddesi (17 Ekim, gece)
- Kullanıcı:
  - 2'li varsayılan kalsın ama bir kız bir erkek seçilebilsin.
  - Yazı hâlâ büyük, fazla ve iç içe.
  - "Eleştirmenin 10 vermesini engelleyenleri bana sormadan ekle, sonra karar verelim."
- **Ölçek v3:** ürün adı 28, bölüm başlığı 22, gövde 15, açıklama 14, fiyat 20. Gereksiz etiketler ve uzun notlar kalktı; gölge ve iç çerçeveler azaldı.
- **2'li paket:**
  - "2 Kız / Kız + Erkek / 2 Erkek" (3 sütun), model kartlarıyla senkron
  - karışıkta iki model kartı da seçili
  - Sihirli 3. kart "Ninni iki modelde · Kızda Bluetooth ile."
- Eleştirmenin 26 maddesi (önceki puan 8/10) uygulandı:
  - kutu listesi seçime bağlı; 2'li kutu fotoğrafı yer tutucu
  - yapışkan çubukta iki lamba ve "Kız + Erkek · kartla" / "Bugünkü fiyat · 06:02"
  - kart notu "Kapıda ödemeye göre ₺X daha az"
  - kart markaları satırı (VISA, Mastercard, troy · 3D Secure · [ödeme altyapısı]; teyit)
  - kapanışta "Kapıda ödemek istersen · ₺X"
  - 2'li alt satır "2 ayrı alıma göre ₺649,99 az"; kurdele "Kardeşe"
  - SVG yıldızlar (4,7 doğru dolum); puan dağılımı [X]; "Yalnız sipariş verenlerin yorumları."
  - disk rayı "Kutuda [teyit]" 6 + "Hediye [teyit]" 5 + boş daire; tavan etiketi "[gerçek tavan fotoğrafı: ad]" ve küçük disk
  - "Yumuşak ay ışığı"; "Telefondan çal."
  - diğer ürünlerde eski fiyat ve rozet yok (10 gün kanıtı yok)
  - Bir gece krem zeminde, kartta yalnız saat ve başlık
  - yorum kartında konu hapı yok
  - süzülen diskler kenarda tam görünür, yalnız oda sahnelerinde
  - buton gölgesi 3px; "30" 32px
- Bilinçli istisnalar:
  - 2'lide "+6 hediye disk" (canlı sitedeki teklif)
  - teslim süreleri (mağaza politikası)

## Tur 13b · Eleştirmen 9/10, son 5 madde (17 Ekim, gece)
- Eleştirmen 26 maddeden sonra 9/10 verdi. Kalan 5 tasarım maddesi uygulandı:
  - **Tek model kontrolü:** 1 Adet'te Kız / Erkek kartları; 2 Adet'te aynı yerde 2 Kız / Kız + Erkek / 2 Erkek (iki lamba yan yana). Paketin altındaki çipler kalktı.
  - **Kısa Sihirli kartları:** ~150 → ~110px; ikon 36, açıklama tek satır ("Altısı hediye ›", "Şarjlı, taşınır.").
  - **Tekrar yok:** üst güven satırı "Ücretsiz kargo · 30 gün iade · Kartla %5 indirim"; 1 Adet alt satırı "Kendine" (2 Adet "Kardeşe").
  - **Kart logoları:** Visa (simple-icons çizimi), Mastercard (resmi iki daire), troy (marka renginde yazı; açık kaynak çizimi yok).
  - **Yorum kartı:** alıntı ile isim arası boşluk kalktı.
- Yorum kartına yıldız ve model etiketi eklenmedi: yorum başına puan ve model bilgisi yok, Loox'tan gelince eklenir.
- Gerçek veri bekleyenler:
  - puan, yorum sayısı ve dağılımı
  - stok ve "dün aldı" sayısı
  - videolar
  - müşteri fotoğrafları (izin)
  - tavan fotoğrafları
  - kutuda ve hediye diskler, 12. disk
  - 2'li kutu fotoğrafı
  - boyut, pil, yaş
  - 15–30. gün iade koşulu
  - ödeme altyapısı ve kart markaları
  - ticari bilgiler
  - kampanya tarihi
  - robotta ninninin nasıl çaldığı
  - Bir gece görselleri (HF_TOKEN)

## Tur 14 · Eleştirmen değişiklikleri geri alındı (17 Ekim, gece)
- Kullanıcı: Tur 13'teki kendi isteklerini (2'li varsayılan + kız/erkek seçimi, daha küçük ve az yazı, iç içe olmayan düzen) istedi. Eleştirmen için yapılanları geri aldırdı.
- `luna_bplus.py`, `1cef207` (Tur 13 ara) sürümüne döndü. Tur 13 ve 13b'deki eleştirmen değişiklikleri yok.
- Model kartı yalnız Kız / Erkek. 2 Adet seçilince paketin altında "1. lamba [Kız/Erkek] · 2. lamba [Kız/Erkek]" (durum `l1`, `l2`; boşsa model kartındaki seçim). 2'li paket görseli ve yapışkan çubuk ("2 Kız", "2 Erkek", "Kız + Erkek") seçime göre değişir.
- Kural: eleştirmen önerileri kullanıcı seçmeden toplu uygulanmaz.

## Tur 15 · Gerçek bilgiler işlendi (17 Ekim, gece)
- Kullanıcının verdikleri sayfaya işlendi:
  - Kampanya 1–31 Ekim
  - "Stokta son 18 adet" (elle; "dün" satırı kalktı)
  - 2'li pakette "Her kutuda +6 hediye disk"
  - Sihirli: "3 parlaklık ayarı"; Bluetooth ninni iki modelde
  - SSS: her yaş, Bluetooth iki modelde, tüm kartlar, ücretsiz iade kodu, 3 parlaklık
  - 30 gün: "İade kargosu ücretsiz."
  - boyut/pil satırı kalktı
- Hâlâ bekleyenler:
  - satıcı bilgileri
  - Loox 4,7/62 teyidi
  - videolar
  - tavan fotoğrafları
  - Bir gece görselleri: Flow bu bulut oturumundan çalışmaz; claude.ai sohbetinde Claude in Chrome ile ya da HF_TOKEN ile. İstemler `araclar/gorsel/bir_gece_uret.py` içinde.

## Tur 16 · Yeni deneme: C "Gece hikâyesi" ve yeni ajanların ilk testi (17 Ekim, gece)
- Kullanıcı: "Yeni bir dokunuşa başlayalım, yeni bir tasarım dene; yeni ajanlar işe yarayacak mı?"
- **Pano:** `canvas/LunaDreamC.dc.html` (üretici `araclar/tuval-uret/luna_c.py`). Tuvalde B+'nın sağında (x=2350, y=3100), Sürüm 54. B+ değişmedi.
  - B+'nın onaylı parçaları üreticiden birebir alınır: sahne, levha, Sihirli, model, paket, lamba seçimi, butonlar, SSS, diğer ürünler, alt bilgi, yapışkan çubuk.
  - **Kapına gelecek:** paket ile butonlar arasında. 1 ya da 2 çizgi kutu; içinden gerçek lamba çıkar. Lamba görselleri stüdyo fotoğrafından yalnız arka planı temizlenmiş kesimlerdir (`canvas/c-gorsel/lamba-*.png`, OpenCV GrabCut). Metin: "Kapına 2 kutu gelir. Her kutuda lamba, 6 + 6 hediye disk ve USB şarj kablosu."
  - **Gece hikâyesi:** videolar, yorumlar, Bir gece, diskler, kutu ve 30 gün tek bölümde toplandı. 6 kare:
    1. masal
    2. disk seç ve tavanda gör
    3. ninni
    4. 3 yorum
    5. müşteri fotoğrafları
    6. iade, kargo, kapıda ödeme ve buton
    - Kareler dokunarak ilerler, kendiliğinden ilerlemez. İlerleme çizgisi yerine 6 ay evresi var: görülen kare dolu, görülmeyen yalnız çizgi, son kare dolunay.
  - Sayfa 6150 → 3999px.
  - Galerinin ilk üç fotoğrafı yerel dosyalardan yeniden yüklendi (`canvas/c-gorsel/`). Yerel önizleme artık tuvalle aynı görselleri gösteriyor.
- **design-review (teknik):**
  - Engel yok. 2 Yüksek bulgu:
    - gizli karelerdeki 13 düğme Tab ile odak alıyordu
    - ileri/geri odak çizgisi görünmüyordu
  - Orta bulgular:
    - ay düğmesi 44px
    - eksik tablist kalıbı
    - geçişte "hayalet" yazı
    - açık zeminde amber "30"
    - kare yüksekliği 520px
  - Hepsi düzeltildi. Gizli kare `visibility:hidden` oldu, geçiş "önce sön, sonra gel" biçiminde. Betikle doğrulandı: odak alan gizli öğe 0, ay düğmesi 48px.
- **Eleştirmen (zevk):**
  - Puanlar: B+ 6/10, C 7/10.
  - En beğendiği 3 fikir:
    1. Kapına gelecek
    2. 3 karelik ürün hikâyesi
    3. Ay evreleri
  - Beğenmedikleri:
    - yorumlar ve müşteri fotoğrafları dokunmanın arkasında kalıyor
    - Videolar bölümü kalktı (kullanıcı istemişti)
    - 6. kare "Işık kapanınca" başlığının altında anlatıyı koparıyor
  - Kural düzeltmeleri hemen uygulandı:
    - "Yasal 14 günü 30 güne uzattık" (mevzuat 4)
    - 48px dokunma alanı
    - daha kısa kutu metni
  - Zevk önerileri uygulanmadı; kullanıcı seçecek.
- **Kullanıcıya soruldu:** C'den B+'ya ne taşınsın? Seçenekler:
  - Kapına gelecek
  - ürün hikâyesi (yorum şeridi dışarıda kalsın)
  - ay evreleri
  - C'nin tamamı
- Riskler:
  - `[gerçek tavan fotoğrafı]` hâlâ yer tutucu
  - yeni oda sahnelerindeki duvar yıldızları gerçek yansımadan net olabilir; gerçek fotoğrafla karşılaştırılmalı
  - canlıda 1. kare video olursa "Sesi aç" ayrı düğme olmalı

## Tur 17 · C2 "Ay yaprakları": bölümler geri, iskelet yeniden (17 Ekim, gece)
- Kullanıcı (C hikâyesine): "Çok kısaltmışız; hâlâ soğukluk, düzensizlik var, tam yakın değil uzak değil. Alt kısım section olarak görünmeli; değişiklik bölümler, iskelet, sayfanın görünüşü üzerine olmalıydı."
  - Kural olarak TASARIM-BILGISI §10 ve SKILL'e yazıldı.
- **C2** (`luna_c.py` → `canvas/LunaDreamC.dc.html`, tuvalde kullanıcının taşıdığı yerde, Sürüm 57). İçerik B+ ile aynı; iskelet değişti:
  - **Yapraklar:** her alt bölüm bir öncekinin üstüne 28px biner (levha motifi). Ton sırası: kum `#EEE3D2`, ak `#FFFDF9`, gece `#1A2142` ve `#121735`.
  - Bölüm sınırını boşluk değil yüzey değişimi gösterir.
  - **Ay tutamakları:** her yaprağın tepesinde, aşağı indikçe dolar; alt bilgide dolunay.
  - Gece yapraklarının tepesinde hafif amber ışık var. Açık yapraklarda iç kartlar çizgisiz ve krem dolgulu.
  - Sıra: Videolar, Yorumlar, Bir gece, **Kapına ne gelir?**, Diskler, 30 gün, SSS, Diğer, Alt bilgi.
    - Kutu, iki gece yaprağının arasına alındı; yoksa ~950px kesintisiz koyu blok oluşuyordu.
    - "Kapına ne gelir?" seçime göre 1 ya da 2 kutu gösterir. Elde fotoğrafı yalnız Kız modelinde var; seçim yalnız Erkek ise Erkek stüdyo fotoğrafı görünür.
- **design-review:** Engel yok. Düzeltilenler:
  - `.gir` canlıda yaprağı yarı saydam yapıyordu; artık yalnız içerik hareket ediyor.
  - Elde fotoğrafı seçimi izlemiyordu.
  - Fotoğrafta afiş yazısı ("Ge…") vardı; kırpıldı.
  - İki gece yaprağı arasındaki kontrast 1,12:1 idi; sıra değişti.
  - Çip kontrastı, kaydırıcı odak halkası, yapışkan çubuk z-index'i.
  - Lamba seçici 48px oldu. B+'da hâlâ 42px.
  - Panoda `.pg{overflow:hidden}` yüzünden view() hareketi hiç oynamıyor; hareket ancak canlıda denetlenebilir.
- **Eleştirmen:** B+ 6,5/10, C2 7,5/10.
  - En beğendiği 3 fikir:
    1. yaprak iskeleti (9/10)
    2. Kapına ne gelir? (8/10)
    3. çizgisiz krem kartlar ve gece yapraklarındaki amber ışık (8/10)
  - Beğenmedikleri:
    - ay tutamakları (4/10; 18px'te evreler okunmuyor, ortada ikinci eksen açıyor; ya kaldır ya sola al ve 5 evre yap)
    - levha hâlâ çizgili beyaz kartlarla en soğuk yer
    - 30 gün yaprağı ince bir şerit gibi kalıyor (mühür ağırlığı verilmeli)
  - Hatalar ve kural ihlalleri düzeltildi: kutu kapakları ok gibi görünüyordu, "Ge" kırpması, 48px, teslim çizelgesi aralığı. Zevk önerileri kullanıcıya soruldu.

## Tuval düzeni (17 Ekim, gece)
- Kullanıcı: "Nihai tasarımımız ve yeni ajanlardan sonra yaptığımız tasarım kalsın, diğerlerini kapat; silme."
- Tuvalde iki sayfa var (`canvas.json` → `pages`), Sürüm 58:
  - **Güncel:** açılış sayfası (`launch.page`). Yalnız B+ (x=0) ve C2 (x=470) yan yana.
  - **Arşiv:** diğer 26 pano ve eski başlıklar. Hiçbiri silinmedi.
- Yeni pano eklerken `boards` girdisine `"page": "guncel"` ya da `"arsiv"` yazılır. Sayfa yazılmazsa pano ilk sayfaya (Güncel) düşer.

## Tur 18 · D "Oda ve Tavan": sıfırdan, kararları ajanlar verdi (17 Ekim, gece)
- Kullanıcı: "Yeni, sıfırdan bir tasarım yap. Her şeyi yeni ajanlar karar versin. Yepyeni bir düzen, mükemmel bir çıktı."
- **Süreç** (belgeler `ogrenme/tur18/`):
  1. Ortak brif yazıldı. Değişmezler: kurallar, gerçek veri, kullanıcı düzeltmeleri. Serbest: düzen, yazı, renk, imza an.
  2. Üç yön ajanı ayrı becerilerle plan yazdı:
     - A "Oda ve Tavan": Anthropic frontend-design
     - B "Yorgan": Impeccable
     - C "Duvar ve Tavan": Taste ve make-interfaces-feel-better
  3. Eleştirmen karar verdi: A 8, C 7, B 5. Kazanan A; C'den üç parça alındı:
     - amber sayaç şeridi
     - saatle koyulaşan Bir gece satırları
     - ay evreli teslim çizelgesi
     Karar belgesi: `ogrenme/tur18/karar.md`.
  4. Kurulum: `araclar/tuval-uret/luna_d.py` → `canvas/LunaDreamD.dc.html`. B+'dan bağımsız, sıfırdan.
  5. design-review ve eleştirmen paralel denetledi. Bulguların hepsi işlendi; kullanıcı bu turda kararı ajanlara bıraktı.
- **D'nin dili:**
  - Renkler: Gece #1A2142, Lamba #F2A65A, Kehribar #9A561B, Çarşaf #FFF8F0, Işıklı duvar #F8E8DA, Sis #5C6078.
    - Krem #F6F1E9 ve Young Serif bırakıldı ("krem + serif" yapay zekâ kalıbı).
  - Yazı: Literata 500 başlıklarda, Atkinson Hyperlegible Next 400/700 gövdede (büyükanne için okunaklı).
  - İskelet: her bölüm kenardan kenara bir bant. Bant içinde 8/16/24, bantlar arasında 64 ve ton değişimi.
  - Köşe: kontrol 14, medya 20, daire. Hap ve gölge yok.
  - İmza an "Disk tavana açılır":
    - kubbe kenarlı Diskler bandında
    - desen lambanın (seçili modelin arka planı temizlenmiş kesimi) tepesinden 250px yansımaya açılır
    - ilk kez sahne ekrana girerken oynar
  - Bölüm sırası:
    1. sayaç şeridi
    2. gece galerisi
    3. ad ve fiyat
    4. Sihirli (2×2 pencere)
    5. satın al
    6. Diskler (imza an)
    7. Kapına ne gelir
    8. Videolar
    9. Yorumlar
    10. Bir gece, beş an
    11. 30 gün
    12. SSS
    13. Odanın geri kalanı
    14. Alt bilgi
- **Denetimden düzeltilenler:**
  - `.pg{overflow:hidden}` yerine `clip`: yapışkan çubuk ve kaydırınca giriş hareketi canlıda çalışır.
  - Yapışkan çubuk fiyat bandı ekrandan çıkınca gelir. İlk ekranda (390×664) güven satırı 624px'te biter, örtülmez.
  - Buton yazıları 700 oldu (`:where(.pg) button`).
  - İki lamba aynı modele gelince model kartı da döner.
  - Ölçek dışı köşe, boşluk ve yazı değerleri düzeltildi.
  - "2 ayrı almaya göre ₺649,99 daha az" yazıldı.
  - Video kapaklarına "[video]" etiketi kondu.
  - Yinelenen görseller değişti: 21:00 yatak başı, galeri 3. görsel Erkek gündüz.
  - Duvar bir ton koyulaştı.
  - Disk odağı ile seçimi ayrıldı; ekran okuyucu metinleri düzeltildi.
- Tuvalde Güncel sayfası: B+ (x=0), C2 (x=470), D (x=940). Sürüm 59.
- 18 Ekim, kullanıcı: "Hayır olmamış, o section için UI tasarım istiyorum." Satır satır açılma kaldırıldı. Yerine **kaydırınca ilerleyen gece sahnesi** geldi (D, Sürüm 61).
  - Sahne 560px ve yapışık. Telefonda her an ~70vh kaydırmayla değişir (IntersectionObserver, ekranın ortası).
  - Değişenler:
    - gök (Gece katmanının opaklığı)
    - lamba ışığı
    - yükselip batan ay
    - yıldızlar
    - fotoğraf ve metin geçişi
  - Altta 5 saatlik şerit; dokununca o ana gider.
  - Durum tek sınıfta (`.an0`–`.an4`).
  - Tuvalde (görüntü alanı 1600px+) kaydırma adımları kapanır, şeritle gezilir.
  - Ayrı pano `LunaDreamD-BirGece.dc.html` (`luna_d_gece.py`): 5 an soldan sağa, Güncel sayfasında.
- (Önceki deneme, Sürüm 60: satırlar kaydırıldıkça tek tek açılıyordu; kullanıcı beğenmedi.)
  - Her an ekrana girince bir kez açılır (IntersectionObserver %35).
  - Ray çizilir, nokta belirir; saat soldan, metin aşağıdan, fotoğraf sağdan gelir.
  - 20:45'te açık perde söner (gece çöker), 07:30'da gece perdesi söner (sabah).
  - Gözlemci yoksa ya da azaltılmış hareket açıksa satırlar hiç kapanmaz.
- **Açık sorular:**
  - Kutuda 12 disk var, sayfada 11 disk görseli var. 12. disk hangisi?
  - Gerçek tavan fotoğrafları yok.
  - 4,7 / 62 Loox teyidi bekliyor.

## Tur 19 · 42 Instagram reel'i incelendi (18 Ekim)
- Hepsi indirildi, döküldü, kare kare okundu. Özet: `ogrenme/instagram-42/README.md`.
- Kurulacak: Playwright MCP'ye `--no-sandbox` (root'ta açılmıyordu) ve Chrome DevTools MCP 1.11.0 (performans izi, Lighthouse).
  - İkisi de denendi.
  - `.mcp.json` değişikliği kullanıcı onayı bekliyor; hazır metin `ogrenme/instagram-42/denetim.md` sonunda.
- İmza an adayları:
  - dev "LUNA" yazısı önünde yükselen lamba
  - yarıktan basılan kapıda ödeme fişi
  - seçince zemin ve görselin değiştiği model seçimi
- Önerilen sonraki iş: `TASARIM-BILGISI.md`'den kısa bir `DESIGN.md` türetmek (Google biçimi).

## Bekleyen karar: ana sayfa slaytı (28 Eki)
- Kullanıcı: "şurayı beğenmedim, tam mı oturtsak, görünüşü beğenmedim" (kenarlardan boşluklu, yuvarlak köşeli koyu kart; yazı görselin üstünde).
- Yönler: A kenardan kenara koyu (6/10), B kenardan kenara görsel + yazı altta krem zeminde (9/10), C kısa + tam genişlik düğme (6/10), D ince kart (3/10). Eleştirmen sırası B, C, A; B için iyileştirme: yazı bloğu sabit yükseklik, görsel-yazı arası 20-24 px, istenirse başlık altına fiyat satırı. Görüntüler scratchpad/hero (CSS denemesi, `anasayfa.py` .slayt). Kullanıcı seçim yapmadan "başka tema gönderme, kodu ver ben değiştiririm" dedi → önce B verildi, sonra kullanıcı C'yi seçti ("C'yi yapayım"); depoda C: kod `ayluna.css` sonunda (telefon/tablet, ≤1023 px; masaüstü aynı). Kullanıcı canlı temada assets/ayluna.css sonuna elle yapıştırıyor.

## Tema 1.0.36-1.0.37: 404 düzeltmesi, Videolar bölümü, görsel seçiciler (28 Ekim, en güncel)
- 1.0.35 yüklenince bütün ürün sayfaları 404: video bloğunda 4 ayarın varsayılanı boştu (`"default": ""`), Shopify LunaDream bölümünü reddetti. 1.0.36 düzeltir; `araclar/tema/sema_denetim.py` zip'ten önce yükleme kurallarını denetler.
- 1.0.37: `sections/ay-videolar.liquid` (Liquid ile çizilen bağımsız bölüm; kart = `video` bloğu: video, kapak görseli, başlık, alt yazı; ayar `urun` ile ürüne sınırlanır, `tasarim`/`tasarim_gorsel` görsel seçilmeyen kartta tasarım fotoğrafı). LunaDream sayfası video noktasında ikiye bölündü: `ay-lunadream` (p01-p02) → `lunadream-video` → `ay-lunadream-2` (p04-p12). `bolumler.urun_sayfasi` artık bölüm listesi döndürür; `urun_sablonu` bölüm/blok ayarı alır.
- JS görselleri: `araclar/tema/gorsel_harita.js` benzetimde (BENZETIM_MEDYA dört ürün, ayrı port) her bloğu açıp düğmelere basarak görselleri toplar → `araclar/tema/gorsel-harita.json`; `bolumler.gorsel_secici` blok/bölüm ayarına `d1…` görsel seçici ve `<script class="ay-gorsel-esle">` ekler; `ayluna.js gorselEsle()` V.blob'u değiştirir (düzenleyicide yeniden yüklemede sıfırdan). Ürün kartları ve galeri Shopify'dan geldiği için haritada yok. Sade ürün sayfalarında görsel seçici yok (bloklar 11 ürünün ortak bloğu).
- Benzetim: `BENZETIM_DSEC` (ilk d1 dolu), Videolar bölümünün ilk kartında video (`BENZETIM_VIDEO`), ürün ayarı handle → nesne. Testler: tema HEPSİ TAMAM, site 179 TAMAM, Theme Check yalnız RemoteAsset.

## Tema 1.0.35: EasySell seçimi, canlı denetim düzeltmeleri (28 Ekim)
- Canlı denetim (ayluna.shop, 1.0.34; 440 px ve 1440 px, izleyiciler engelli, sipariş verilmedi): JS hatası yok.
- EasySell (kullanıcı kapıda ödemeyi EasySell ile yeniden açtı): `ES_GET_VARIANT_ID` gizli formdan okuyup `/cart/update.js` ile ekliyordu; önceki model sepette kalıyor, karışık 2'li pakette iki Erkek gidiyordu. Çözüm: `formEsitle` → `window.pmpr_cart_item` = `kalemler(seçim)`; EasySell'in paket uygulaması kancası (`getBundlesAppUpdates`) sepeti boşaltıp yalnız bunları ekler. Form adedi ilk kalemin adedi; `properties[_paket]` eklendi. EasySell düğmesi gizli forma düşerse yuvaya (`[data-ay-dis]`) taşınır; `#es-sticky` varsa `html.ay-es-yapis` ile bizim `.yapis` gizli.
- Sade sayfalar bozuktu: blok sarmalayıcısı `ay-blok` ana sayfa tasarımının sınıfıydı → `ay-tb`.
- Köşeli yer tutucular canlıda görünüyordu → `yerTutucuGizle` (Shopify'da soru/madde/satırla gizler). LunaDream "[gerçek tavan fotoğrafı]" etiketi kaldırıldı.
- Video bölümü: mağazada video yok; bölüm artık gizlenmez, tasarım fotoğrafları oynat işaretsiz kalır. Remotion videoları `onizleme/v/` kullanıcıya gönderildi (ürün medyasına yüklenebilir).
- Aynı sürümde (önceden): ürün kartı görselleri Shopify'dan, yorum tasarım kartları varsayılan kapalı (Loox varken), video bloğunda video seçici, Erkek seçilince galeri varyant görseline kayar, menüde LunaDream ürün sayfasına gider, `.pg` 500 px.
- Testler: tema benzetimi HEPSİ TAMAM (yeni: EasySell kalemleri, düğme yuvada, yapışkan gizli), site 179 TAMAM, Theme Check yalnız RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.35.zip`.

## Tema 1.0.34: ürünler blok blok, Loox gömülü, ürün videoları, ince yapışkan çubuk (28 Ekim)
- Canlıda 1.0.33 yayındaydı ama dört özel ürün kendi şablonuna atanmamıştı (canlı sayfada hepsi `template--…__b01…b06`); sayfalar tek parça açılıyordu.
  Kullanıcı: "Hâlâ section'lar çalışmıyor; Loox'u yüklüyorum, direkt senin yaptığın yorum kısmında olması gerekiyor; videolar açılmıyor; tüm section'lar erişilebilir değil; görselde gönderdiğim kısım hâlâ aynı."
- 1.0.34: şablon ataması yok. `product.json` = 5 bölüm: `ay-lunadream` (12 blok), `ay-galaxy-usb` (16), `ay-ayfeneri` (14), `ay-galaksi-night` (15), `ay-urun-diger` (6; sade ürünler, parçalar `snippets/ay-u-<handle>.liquid`). Her bölüm yalnız kendi ürününde çizilir; tasarım parçaları blok (`p01…`, yazı `m…` ve görsel `g…` blok ayarı, `limit: 1`). `bolumler.urun_sayfasi`, `sade_snippet`, `sade_sayfasi`, `urun_sablonu`.
- Loox: yorum parçasına `<div id="looxReviews" data-product-id … class="loox-reviews-default">{{ product.metafields.loox.reviews }}</div>` (yer tutuculu parça, yoksa "… ne diyor?" parçası); Loox yerleştirmesi açıkken kendiliğinden dolar. Kutu DC çiziminin dışında, silinmez.
- Videolar: layout `#ay-medya` = `{"g": galeri, "v": ürünün mp4 videoları}`; `Ayluna.videolar()`; LunaDream video bölümü ürün videolarını `<video>` olarak çizer, video yoksa `ay-yok` ile gizli. Önizlemede tasarım kapakları.
- Yapışkan çubuk (eleştirmenin 1. önerisi, kullanıcı seçmeden "hâlâ aynı" dedi): 60 px, 36 px karo, ad + seçim (+ LunaDream'de sayaç) tek satır, 48 px düğme, lacivert basma gölgesi, alt güvenli boşluk; paketler ve ana düğme ekrandayken `data-ay-cekil` ile aşağı çekilir (`ayluna.js yapisBak`). LunaDream, USB, AyFeneri, Galaksi Night.
- Testler: tema benzetimi HEPSİ TAMAM (USB 16 blok, Loox kendiliğinden yorumda ve kalıcı, LunaDream ürün videosu sesli oynar, çubuk 60 px ve paket alanında çekilir, düzenleyici yeniden çizimi, Galaksi Night 15 blok, Sunset galeri), site 179 TAMAM, Theme Check yalnız RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.34.zip`; tuval Sürüm 168, site Sürüm 51.

## Tema bölüm bölüm (Loox, videolar, galeri) + yapışkan çubuk yönleri (28 Ekim)
- Canlı mağazada 1.0.32 yayında (ayluna.shop, role main). Kullanıcı: "İçine Loox eklenmemiş; Loox ekliyorum ama yorum kısmına koyamıyorum, senin koyduğun şekilde kalıyor. Videolar açılmıyor. Section'ları tek tek bölümler kısmında görüp düzenleyebileceğim hale getir; görsel olarak senin içine koyduklarını çekiyor; varsayılan ürün tarafında 2 ürün görünüyor sadece, hangilerini değiştirmek gerekiyorsa değiştir. Görseldeki video yazılarını da kaldır."
- Tema 1.0.33 (`araclar/tema/bolumler.py`): panonun `.pg` çocukları bölümlere ayrılır (Üst kısım, Galeri ve satın alma, başlığı olan her bölüm, Alt bilgi, Yapışkan çubuk). Her bölüm parçasını `<template class="ay-parca">` + `.ay-kok` ile taşır; `ayluna.js` hepsini tek bileşenle çizer (`parcalar`, düzenleyicide `shopify:section:load/unload/reorder` ile yeniden toplar). Panonun kendi şablonunda yazılar (`m1…`) ve görseller (`g1…`, image_picker; boşsa tasarım görseli) bölüm ayarı.
  - Şablonlar: `product.lunadream`, `product.galaxy-usb`, `product.ayfeneri`, `product.galaksi-night` (kullanıcı bu 4 ürüne atar, KURULUM 1b). `product.json` (varsayılan): sade 11 ürün ortak 6 bölüm (`ay-sade-01…06`, ürüne göre `case`); atanmamış özel ürün ilk bölümde tek parça panosuyla açılır. `index.json`: ana sayfa 7 bölüm.
  - Loox: her bölüm `@app` blok alır, blok bölümün altında (`.ay-uyg`) görünür; "Uygulama bloğu" bölümü (`ayluna-uygulama`) her yere eklenir. "[Loox …]" yer tutuculu bölüm blok yoksa görünmez (düzenleyicide ipucu).
  - Videolar (LunaDream): bölüm blokları (video ayarı, başlık, alt yazı), `video_tag`; ekrandayken sessiz döner, dokununca sesli tam ekran. Video yoksa bölüm yok. "[video]" etiketi tasarımdan da kalktı.
  - Galeri: layout'ta `#ay-medya` (ürünün Shopify görselleri, tema ayarı `galeri_urun`); bütün ürün panoları `Ayluna.medya()` ile kullanır.
  - Yapışkan çubuk bölümlü sayfada ekrana sabit (`html.ay-coklu .yapis`).
- Benzetim artık şablonları python-liquid ile çizer (`pip install python-liquid==1.12.1`); `BENZETIM_LOOX`, `BENZETIM_VIDEO`, `BENZETIM_MEDYA`, `BENZETIM_VARSAYILAN`. Testler: tema benzetimi HEPSİ TAMAM (16 bölüm, Loox yorum bölümünde, video oynar, düzenleyici yeniden çizimi, atanmamış özel ürün, Shopify galerisi), site 179 TAMAM, Theme Check yalnız RemoteAsset (bölüm başına Google Fonts bağlantısı). Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.33.zip`; tuval Sürüm 166, site Sürüm 50.
- Yapışkan çubuk (kullanıcı: "burası yapışık kalıp çok fazla alan kaplıyor, neler yapabiliriz bak"): 4 taslak (A ince şerit 60 px, B yüzen düğme, C kaydırınca saklanan, D tam genişlik düğme). Eleştirmen: 1) A + paket alanında çekilme (8/10; 20 px üst köşe, 48 px düğme, lacivert basma gölgesi, sayaç ikinci satırda), 2) tek satır 56 px + aynı çekilme (7/10), 3) şimdiki + yalnız çekilme (6/10); B ve D'yi beğenmedi. Ayrıca: şimdiki çubuk ana düğme ekrandayken onun hemen altında (iki amber düğme), alt güvenli boşluk yok. Kullanıcı seçecek (`ogrenme/yapis-yonleri-28eki.png`: 1, 2, 3 ve paket alanında çekilmiş hâl; ilk taslaklar `ogrenme/yapis-taslaklar-28eki.png`).

## Kapıda ödeme kalktı + Galaxy USB iyileştirmeleri (27 Ekim)
- Kullanıcı: "Artık yüklüyorum siteyi; kapıda ödemeyi kaldır, bir de USB projektör ürün sayfasındaki yapılması gereken iyileştirmeleri de yap."
- Kapıda ödeme: bütün sitede ve temada kapıda düğmesi, formu, sepet notu, SSS ve politika maddeleri kalktı (commit 0dad574); ödeme yalnız kartla (%5). KURULUM: EasySell yerleştirmesini ve Shopify COD yöntemini kapat.
- Galaxy USB (`luna_usb.py`; eleştirmen + `design-review` denetimi):
  - Fiyat LunaDream sırasıyla (`.fiyat-satir`, 20 px/600); ekran okuyucu görünmez metni okur (`.sr-m`). Aynı erişilebilirlik düzeltmesi LunaDream, AyFeneri, Galaksi Night'ta.
  - Özellik kartları kurumsal: 28 px gösterge (fiş, 3 disk yığını, boyun, gece lambası halesi, cetvel), gri ekran ve dönen etiketler yok; lens rengi animasyonu (fill) kalktı.
  - "İçin rahat olsun" güven kutusu satın almanın hemen altında; "[Ödeme altyapısı]" çipi kalktı, "Kartla güvenli öde" geniş kartı düzeldi.
  - Sahneler: alt yazılar "Kutudaki Dolunay/Satürn diski"; üçüncü kart (tavanda galaksi yok) "Gece lambası · Gövdesi yumuşak ışıkla yanar" oldu.
  - Başlıklarda zorla satır kırma yok. "Disk N / 12" sayacı yerine "Kutudaki disk". Kurulum numarası 32 px, SSS artısı ince halka, kart çipleri 700.
  - Yer tutucular: "Disk nasıl değişir?" (cevap teyitsiz) SSS'den kalktı; "Kırık ya da eksik" cevabı teyitli bilgiyle; kurulum adım 2'deki köşeli not kalktı.
  - Yorumlar tek akış: "Alanlar ne diyor?" → müşteri mesajları (küçük etiket) → Loox kutusu. Shopify'da bölüme eklenen Loox bloğu bu kutuya taşınır, blok yoksa kutu görünmez (`ayluna.js` `data-ay-yorum`).
  - Paket alt yazısı "₺798,01 kazanç" (LunaDream gibi). Çapraz satış kartları yazısız kesim (canvas/capraz).
  - Yapışkan "Satın al" paketlerin başına iner (paket, düğme, teslim aynı ekranda). Oda kartında görünmez ileri/geri dokunuşu turu durdurur.
  - Hareket: düğme oku 2 kez, güven ikonları 3 döngü, oda çipindeki disk dönmez. Kullanıcının sevdiği hareketler (fiş, boyun, lamba, cetvel, kargo, tavana düşen disk, 30 çentik) kaldı.
  - Erişilebilirlik: koyu zeminde odak halkası açık ton; yapışkan çubuk odağı örtmez (`scroll-padding-bottom: 88px`); mesaj büyütme penceresi odağı alır, Tab içeride kalır, kapanınca geri verir (bütün ürün sayfaları); ürün sorularında odak halkası koyu ton; galeri canlı bölgesi yalnız elle geçişte okur; ilk galeri görseli öncelikli, diğer görseller tembel yüklenir. Masaüstü galeri okları 48 px.
- Shopify: "Dün N kişi" ve "Son N adet" ürün alanından (`ayluna.dun_satis`, `ayluna.stok_kurdele`; boşsa tasarımdaki sayı, 0 ise satır yok; KURULUM). Benzetimde deneniyor (`BENZETIM_ELLE`, `BENZETIM_LOOX`).
- Pano boyları (kapıda ödeme sonrası ölçüldü): LunaDreamE 7186, GalaxyUSB 6579, AyFeneri 6574, GalaksiNight 6907, Ayluna-Anasayfa 4151, Sepet 1191, sade ürünler `yukseklik.json`; politika, ödeme, arama, koleksiyon sayfaları boy-olc ile.
- Site testleri 179 HEPSİ TAMAM; tema benzetimi HEPSİ TAMAM (Loox kutusu + elle sayı dahil), Theme Check 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.32.zip`; tuval Sürüm 164, site Sürüm 49.
- Açık: USB'de "Dün 62" LunaDream'in sayısı (kullanıcı 18 Eki) — USB için gerçek sayı ya da 0; %5 kart indirimi ödeme sayfasında uygulanıyor mu; galerinin ilk iki görselindeki "5K HD" ve "7 katmanlı optik lens" yazıları teyitsiz (galeri canlı mağazanın görselleri, temaya gömülü; kalsın mı, çıksın mı, Flow'da yazısız mı üretilsin, kullanıcı karar verecek); "Disk nasıl değişir?" adımları.

## Üst blok: sayaç şeridi + beyaz başlık, beyaz ↔ lacivert döngü (25 Ekim)
- Kullanıcı (ekran görüntüsüyle, üstteki lacivert sayaç şeridi ve lacivert başlık): "Şu kısmını beğenmiyorum dostum, hem de hiç; neler yapabiliriz, biraz akıl üret." Gerçek LunaDream sayfasına 4 yön giydirildi (`scratchpad/baslik-yon.js`): A beyaz başlık + sayaç fiyatta, B ince açık şerit, C tek lacivert bant, D beyaz başlık + kategori çipleri. Eleştirmen: A 8, B 6, C 5, D 3 (çipler ürün sayfasında müşteriyi dağıtır; ana sayfa/koleksiyonda işe yarar).
- Kullanıcı: "Buradaki A iyi ama üstünde yine sayım olsun ve beyazdan bizim ana rengimiz maviye değişsin, sürekli renk değişimi yapsın, yumuşak."
- Yapılan: `ortak.ust_blok(zaman, işaret)` + `ortak.UST_CSS` + `ortak.gece_kopya`. Bütün sayfalar aynı bloğu kullanır: LunaDream (`luna_e`, galerinin içindeki başlık kalktı), Galaxy USB / AyFeneri / Galaksi Night (`luna_usb.SERIT`, galerideki `.u-ust` kalktı, "Bugüne özel fiyat" → "Bugünkü fiyat garantisi", ay evresi `cdAy` eklendi), ana sayfa ve ondan türeyen sade ürün + diğer sayfalar (`anasayfa`, `sayfalar` düzenli ifadeleri güncellendi).
  - Şerit 30 px (beyaz evrede #F3F4F7 zemin, lacivert yazı; lacivert evrede #0C1027, #B9BED6 yazı, amber rakam). Başlık 52 px (beyaz/1 px gri çizgi ↔ #1A2142); solda işaret + Ayluna, sağda menü ve sepet. Arama menüye taşındı ("Ara").
  - Döngü 16 sn: 5,5 sn beyaz, 2,5 sn geçiş, 5,5 sn lacivert, 2,5 sn geçiş (`rd-gece`). Yalnız opacity: içeriğin `aria-hidden` kopyası (`.gk`, düğmeler span) üstte belirip kaybolur; dokunma alttaki beyaz katmana geçer. `--rd-t` (ayluna.js) bütün katmanları duvar saatine bağlar; masaüstü başlığı (`.ay-masa`) da aynı döngüde (kopyası çalışma zamanında). Sepet sayısı kopyada da (`.gk-sepet`). Hareket azaltılmışsa beyaz kalır.
- Pano boyları: LunaDreamE 7234, GalaxyUSB 7156, AyFeneri 6712, GalaksiNight 7037, Ayluna-Anasayfa 4168, sade ürünler `yukseklik.json`.
- Test: başlıktaki "Ara" testi menüye taşındı; yeni test: iki lacivert katman aynı an, kopya gizli ve dokunulmaz. Site testleri 170 HEPSİ TAMAM; tema benzetimi tamam, Theme Check 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.31.zip`; tuval Sürüm 163, site Sürüm 48.

## LunaDream fiyat sırası + kurumsal özellik kartları (23 Ekim)
- Kullanıcı (ekran görüntüsüyle): "Aradaki boşluğu kapat, bir de fiyat çok büyük; 1.999 olarak gelsin, çizgi çekilsin, yana kayıp gerçek fiyat gelsin, sonra o üstü çizilen fiyat gidip yerine %15 indirim yazısı gelsin." `luna_e.py`: `.fiyat-satir` = `fy-yeni` + `fy-yuva` (eski fiyat ve rozet aynı ızgara hücresinde). Eski fiyat başta `translateX(calc(-100% - 10px))` ile gerçek fiyatın yerinde (tabular rakam, aynı genişlik), çizilir, yerine kayıp .82'ye küçülür, gerçek fiyat belirir, sonra eski fiyat gider ve "%15 indirim" gelir (3 sn, bir kez). Fiyat 20 → 17 px. Ad satırında puan sağda yüzer (`position:absolute`), ad ile fiyat arası 4 px.
- Kullanıcı: "Her bir emoji benefitin bu kadar kısmı çalışıyor, boş olan kısımları silebilirsin, tamamen kurumsal bir hissiyat versin, her şey yerli yerinde olsun." `luna_e.kart_k`: gri ekran kutusu kalktı; her kartta solda 28 px'lik çalışan gösterge (3 disk, lamba + 3 kademe çubuğu, telefon ··· lamba + ses çubukları, lamba + pil), başlık 14/600, açıklama 13 px; beyaz kart, 1 px gri çizgi. Model değişince lamba/robot ikonu yine değişir. Test: 360 px'te gösterge kartta, gri ekran yok, "Diskleri gör" tek satır.
- Pano boyu LunaDreamE 7244.
- Site testleri 169 HEPSİ TAMAM; tema benzetimi tamam, Theme Check 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.30.zip`; tuval Sürüm 160, site Sürüm 47.

## Büyük site inceliği: kalınlık ve ikon karoları (23 Ekim)
- Kullanıcı: "Hâlâ biraz büyük geliyor gözüme; mükemmel otursun, tüm kısımlar, tüm section'lar, tüm yazılar büyük olmasın; büyük sitelerin tasarımlarından örnek alabilirsin."
- Ölçüm (`scratchpad/ref-olc.js`, izleyiciler engelli, sepet/form yok): Hatch Restore 3 (ad 32/500, fiyat 22/500, h2 28), Loftie Lamp (36/400, 17, h2 25-34), Glossier (28/500, 14), Allbirds (24/400), Oura (40/400). Yazı boyumuz onlardan büyük değil; fark kalınlıkta (bizde 700-800) ve dolu lacivert 44-48 px ikon karolarında.
- Yapılan: USB başlık yazı tipi (Bricolage) 800 → 600 (600 yüklendi), AyFeneri (Big Shoulders) 800 → 700, Galaksi Night (Sora) 700 → 600; fiyatlar 700 → 600 (LunaDream, sade); özellik ikon karosu `.mini` 48 → 36 (ikon 22), güven karosu `.gv-ik` 44 → 36 (ikon 20); alt çubukta ürün adı 17 → 15/600; LunaDream öne çıkan yorum 21 → 18, yorum listesi 17 → 15; dergi kapağı sözcüğü 128 → 104 px.
- Galeri kapağındaki "Tavanı masala çeviren lamba" yazısı görselin içinde (ürün görseli); CSS ile küçülmez.
- Site testleri 169 HEPSİ TAMAM; tema benzetimi tamam, Theme Check 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.29.zip` (ad/fiyat/başlık küçültmesi + kalınlık/ikon inceliği); tuval Sürüm 159, site Sürüm 46.

## Ürün adı, fiyat ve iri başlıklar küçüldü (23 Ekim)
- Kullanıcı: "Ürün ismi ve fiyat etiketi kısmı da biraz büyük." + "Kısaca büyük olan, görüntüyü gereksiz yere bozan tüm kısımları kontrol et ve ona göre düzenle." Telefonda 22 px üstü bütün yazılar tarandı (`scratchpad/iri-yazi.js`), tam sayfa görüntülerine bakıldı.
- Ürün adı: LunaDream/USB/Galaksi Night/sade 28 → 24, AyFeneri (Big Shoulders) 34 → 30; Galaksi Night adı tek satıra indi. Fiyat: USB/Galaksi 30 → 22, AyFeneri 26, sade 24 → 20 (LunaDream 20 kaldı); eski fiyat 16 → 14; rozet 26 → 22 px boy, 12 px.
- Başlıklar: USB/Galaksi bölüm 28 → 24, AyFeneri 36 → 30; koyu afiş başlıkları ("Masaldan sonra galaksi", "Kutusu hazır", "Avucuna sığar", "Oda karanlık", kapanış) 32-36 → 28-30; 30 gün rakamı 38 → 30; oda kartı 30 → 24; disk adı 28 → 22; AyFeneri "Bir fener, dört iş" maddeleri 26 → 22; LunaDream puan ve 30 gün 32 → 28.
- Ana sayfa: slayt 38 → 32, bölüm 28 → 24, "Ay ışığını evine getir" 30 → 26, bülten 24 → 22. Sayfa başlıkları 30 → 28; boş sepet 26 → 22.
- Masaüstü (`ayluna.css`): ürün bölüm başlığı 36 → 30, ana sayfa slayt 64 → 52, bölüm 40 → 32, ay bloğu 48 → 38, koleksiyon/arama başlığı 48 → 40, alt bilgi başlığı 40 → 34.
- Bilinçli bırakılanlar: LunaDream dergi kapağındaki dev sözcük (Tak./Çal., 128 px) ve alt bilgideki dev Ayluna yazısı (56 px); kullanıcı isterse küçülür.
- Pano boyları: GalaxyUSB 7166, AyFeneri 6722, GalaksiNight 7047, Ayluna-Anasayfa 4180, sade ürünler `yukseklik.json`.

## Bütün sitede olağan boyut (23 Ekim)
- Kullanıcı: "Model seçme kısımları gibi sitenin her yerini kontrol et, düzgün görünsün, boyut olarak büyük olmasın." 31 sayfa telefonda (390) ölçüldü; büyükler LunaDream ölçüsüne çekildi:
  - Galaxy USB, AyFeneri, Galaksi Night (`luna_usb.py` çekirdek): paket kartı 88 → 62 (görsel 60 → 48, ad 17 → 15, fiyat 18 → 16), kurdeleli satın al 68 → 58, satın al 62 → 52, Kapıda 56 → 48, SSS 60 → 52, özellik kartı görseli 48 → 40 (iç boşluk 16 → 12), ürün adı ve bölüm başlığı 32 → 28. AyFeneri (Big Shoulders, yoğun) bölüm başlığı 42 → 36; Galaksi Night ürün adı 34 → 28 (`ozel_yon.py` `ek`).
  - 13 sade ürün (`urun_sade.py`): paket kartı 72 → 60, satın al 62 → 52, Kapıda 56 → 48, SSS 56 → 52, özellik listesi sıkı (14/13 px, ikon 20).
  - Ürün soruları (`urun_soru.py`, bütün ürünler) 54 → 48, 14 px; LunaDream SSS 60 → 52 (`BOYUT_CSS`'teki soru satırı kuralı çekirdeğe taşındı).
  - Sepet satın al 62 → 52, Kapıda 56 → 48; diğer sayfalar (`sayfalar.py`, `sayfalar2.py`): form düğmesi 56 → 52, arama kutusu 56 → 52, ödeme seçeneği 56 → 52, sayfa başlığı 34 → 30; kapıda formu düğmesi (`ayluna.css` `.ay-btn`) 56 → 52.
- Pano boyları ölçüldü ve üreticilere yazıldı: LunaDreamE 7334, GalaxyUSB 7268, AyFeneri 6855, GalaksiNight 7171, Sepet 1281, sade ürünler `canvas/urunler/yukseklik.json`. `sayfalar.py`/`sayfalar2.py` boy kayması yine geri alındı, sonra ölçüldü.
- Site testleri 169 HEPSİ TAMAM; tema benzetimi tamam, Theme Check 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.28.zip` (LunaDream satın alma kutusu boyutu da içinde); tuval Sürüm 156, site Sürüm 45.

## Satın alma kutusu olağan boyutta (23 Ekim)
- Kullanıcı: "Emoji benefit kısmı, model seçimi kısmı vesaire çok büyük, daha default bir boyuta getir, orantısızlıkları düzelt." `luna_e.py` `BOYUT_CSS` (CSS'in sonuna eklenir, yalnız LunaDream): Sihirli 164 → 135 px, model 74 → 58, paket 82 → 62, düğmeler 62/56 → 52/48, teslim 137 → 125, 4 soru satırı 54 → 48. Kutu 1524 → 1323 px; E_H 7647 → 7430.

## LunaDream zemini beyaz, renkler sade (23 Ekim)
- Kullanıcı: "Fazla mı animasyon var?" → ölçüldü (ilk 3 telefon ekranında Sihirli kartları, teslim kartı sürekli; iki dönen satır, iki sayaç, galeri). Öneri verildi (Sihirli ve teslim ekrana girince bir tur oynayıp dursun; Dün şeridinde satır içi hareket yalnız ilk satırda); kullanıcı henüz seçmedi.
- Kullanıcı: "Arka planı beyaza çevir, renk olarak daha sade bir renge getir." Kapsam: yalnız LunaDream. `luna_e.py` `SADE` + `sade()` yazarken açık paleti çevirir: #F6F1E9/#FFFDF9 → #FFFFFF, #F1E8DA → #F3F4F7, #EFE6D8 → #ECEEF2, #E3D8C7 → #E4E6EB, #D6CAB6 → #C9CED8, #766B5B → #6B7080, #A05A1C → #1A2142. `.pg{--zemin:#FFFFFF}` ile site/tema dış zemini beyaz. Koyu bölümler, amber düğme, yeşil Dün şeridi aynı.
- Site testleri 169 HEPSİ TAMAM; tema benzetimi tamam, Theme Check 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.27.zip`; tuval Sürüm 155, site Sürüm 44.

## Dün şeridi yeşil + giriş hareketi (23 Ekim)
- Kullanıcı: "Renk olarak içime sinmedi." 5 yön çizildi (`scratchpad/dsr-yon/`), eleştirmen amber 8 / yeşil 7 / krem 6; kullanıcı: "Önceki gibi yeşil olan ile olsun, yine gelirken animasyon ile gelsin, renkler çok sıkıcı durmasın."
- `ortak.tk_css(metin, vurgu, nokta, gecik)`: lacivert 600 yazı, vurgu/ikon #2E6B4F, nokta #2E9E62; görünen satıra `on` (TK_DEGER `tkC0..4`): ikon/nokta `dsr-pop`, vurgu `dsr-dus`, nokta `dsr-nabiz` ×2 (sonsuz yok); ilk satır sayfa girişiyle gecikmeli (LunaDream 1,9 sn, USB 1,2 sn); kenar maskesi. `tk_adim(tik, ilk)`: ilk satır girişten sonra ~3 sn (LunaDream ilk=3, USB ilk=2).
- Site testleri 169 HEPSİ TAMAM; tema benzetimi tamam, Theme Check 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.26.zip`; tuval Sürüm 153, site Sürüm 43.

## Dün satırı canlıdaki gibi dönen şerit (23 Ekim)
- Kullanıcı: "Dün 62 kişi satın aldı kısmı şu an sitemdeki gibi dönen ücretsiz kargo vesaire olan kısım gibi olsun, girip bi kontrol et." Canlı LunaDream tarandı (izleyiciler engelli): fiyat bölgesinde `.live-checkout` (24 px pencere, 4 satır alt alta, `translateY` 0,5 sn `cubic-bezier(.22,.61,.36,1)`, ~3 sn bekleme, ilk satırda nabız noktası, vurgu #F27A1A kalın, 12-13 px). Satırlar: "31 kişi şu anda inceliyor" (sayı canlı oynuyor), "3 günde 399 adet satıldı", "Son 10 günün en düşük fiyatı", "Kargo bedava".
- Yapılan: `ortak.py` `tk_html(dun)`, `tk_css(metin, vurgu, nokta)`, `tk_adim(tik)`, `TK_DEGER` (sınıflar `dsr-`; `.tk` USB kurulum kartıyla çakışıyordu). LunaDream ve USB'de `DUN_SATIR = tk_html(DUN)`. Satırlar: Dün 62 kişi → Ücretsiz kargo ile kapına → 30 gün iade hakkı → Kartla öde, %5 indirim (+ ilk satırın kopyası). Uydurma ve teyitsiz satırlar alınmadı. Temada sayı sabit (62).
- Site testleri 169 HEPSİ TAMAM (yeni: şerit döner, ilk satır Dün 62, uydurma satır yok). Tema benzetimi tamam, Theme Check 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.25.zip`; tuval Sürüm 151, site Sürüm 42.

## Sadeleştirme geri alındı + masaüstü denetim düzeltmeleri (23 Ekim)
- Kullanıcı: "Bi de yaptığımız sadeleştirmeleri geri getir." (e27d8ee'deki sadeleştirme) Geri gelenler (`luna_e.py`, `sihirli2_varyant.py`): fiyatın altında dönen satır ("Her kutuda 6 masal diski" ↔ aynı gün kargo + 16.00 sayacı; teslim kartındaki `.yol-not` kalktı), `DUN = '62'`, telefondaki yapışkan çubukta sayaç (`adetName` + `cdTiny`), SSS 12 soru, Sihirli şarj "Her odaya taşı". Kalanlar: Videolar (zaten geri gelmişti), çapraz satışta yazısız ürün kesimleri (teyitsiz poster yazısı yüzünden). Sayfa telefonda 7324 → 7647 (E_H). Masaüstünde 9+ soruluk SSS iki sütun (458 px). Kural: sadeleştirme kullanıcının istediği öğeyi silmez (TASARIM-BILGISI, SKILL).
- design-review ajanının masaüstü raporu işlendi:
  - Mesaj/fotoğraf büyütme penceresi (`.mbuyuk`, `.buyuk`) z-index 60 → 1000 (kapat düğmesi üst menünün altındaydı), görsel ekran boyunu aşmaz.
  - İmza sayfalarının alt bilgisi 5 öğeye göre (imza sağa, telif sol yarıya düşüyordu).
  - Oda kartlarında başlık + alt yazı akışta (1024-1110'da biniyordu).
  - Ana sayfa slaytına oklar (`gal_ok('slayt')`), fare üstündeyken ve odakta otomatik geçiş durur (WCAG 2.2.2); pano yüksekliği 4210'da sabit (`A_H`).
  - Galeri okları görselin sol/sağ kenarının ortasında, yarısı dışarıda (26 galeri karesine bakıldı; sağ üst AyFeneri/Sunset başlıklarına biniyordu).
  - "Yukarı" düğmesi masaüstünde ekranın sağ alt köşesinde; `footer.alt` boş satırı kalktı; çapraz satış başlığı şeritle hizalı; mesaj başlığı 760 sütunda, şerit sağda ekran kenarına uzanır.
  - Sepet satırı masaüstünde tek sıra, 1024'te panel kenara yapışmaz.
  - Ufaklar: Galaksi Night ara boşluğu (`.ara`) masaüstünde yok; kargo takip / iade / iletişim başlıklarında satır sonu yok; "Dokun, büyüsün" masaüstünde gizli; 768-820 px yüksek ekranda koyu bant dolgusu 56 px.
  - Yapılmayan (düşük öncelik): ödeme önizlemesi tek sütun (gerçekte Shopify ödeme sayfası), kapıda formu masaüstünde alttan panel (Shopify'da EasySell), şerit ok uçlarda pasifleşmiyor.
- Site testleri 167 HEPSİ TAMAM (LunaDream dönen satır testi geri, SSS 12). Tema benzetimi HEPSİ TAMAM, Theme Check 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.24.zip`; tuval Sürüm 150, site Sürüm 41.
- Bekleyen: "6 hediye disk" satırı (kutu listesi, afiş 5) kalsın mı; 5 görsel dosya olarak gelmedi.

## Masaüstünde her bölüm ekrana sığar (23 Ekim)
- Kullanıcı: "Tüm sectionlar masaüstünde mükemmel çalışsın, tam sığsın." Ölçü: 1280×800'de üst menü + satın alma çubuğu (140 px) düşülünce 660 px; 1024×768'de 628 px. Ölçüm betiği: bölüm yükseklikleri ve yana taşma 1024/1280/1440/1920 (`scratchpad/ld-denet.js` mantığı, `test.js`'te kalıcı).
- LunaDream (`ayluna.css` masaüstü bloğu): Neler yapabiliyor 430 px sütun → 1136 px dergi yayılımı (söz + yazı + sekmeler solda, lamba sağda, 500 px); Odası böyle görünecek 928 → 592 px (yazı + aylar solda, kart şeridi sağda; ortalama JS'i aynı); Aileler ne diyor 1505 → 1075 px (mesaj şeridi tam genişlik; altta solda fotoğraf şeridi + öne çıkan yorum, sağda yorum listesi). Sayfa 7610 → 6778 px. Telefon değişmedi (7324).
- Oklar (`ortak.py`): `serit_ok(ad)` her kayan şeridin başlık satırına; `KAY` okun satırından sonraki `.noscroll`'u bulur. `GAL_OK` + `GALOK` ürün galerisinde sağ üst köşede iki ok (afişlerde yazı solda), sondan başa döner, galerinin üzerine gelince belirir; dört üreticide (luna_e, luna_usb, ozel_sayfa, urun_sade). Mesaj bölümü (`mesaj_bolum`) başlığında oklar (`mGeri/mIleri`, `MESAJ_VERI` içinde). Telefonda hepsi gizli.
- Galaxy USB: "Bu gece tavanda" kart 520 → 440 px (bölüm 638); "Herkesin odasına" yazı dikeyde ortada, kart 560 px, çipler kart kenarına yapışmıyor (genel `.noscroll` iç boşluk sıfırlaması `.hk-sec`'i de sıfırlıyordu). Mesaj bölümleri bütün ürün sayfalarında 1136 px.
- AyFeneri / Galaksi Night: oda kartları 4 sütun ızgara (1024'te 158 px yana taşıyordu). Galaksi Night diskler: dönen gök (`.kb-s`) iki satıra yayıldı, 763 → 500 px.
- Hata: oda/sahne kartlarının fotoğrafı kartın %108'i, sitedeki genel `img{max-width:100%}` kırpınca sağda 16 px siyah şerit (telefonda da). `.sk img,.oda-k img{max-width:none}`.
- 1024-1199 px üst menü aralıkları daraldı (1024'te 30 px taşıyordu).
- Site testleri 160 HEPSİ TAMAM (yeni: her bölüm 1280×800'e sığar, 1024'te taşma yok, galeri okları sondan başa, mesaj şeridi okla kayar, telefonda ok yok; vitrin ve Neler testleri yeni düzene göre). Tema benzetimi HEPSİ TAMAM, Theme Check 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.23.zip`; tuval Sürüm 149, site Sürüm 40.
- Bekleyen: "6 hediye disk" satırı (kutu listesi, afiş 5) kalsın mı; 5 görsel dosya olarak gelmedi; design-review ajanının diğer sayfalar raporu (gelince işlenecek).

## Masaüstü şerit + telefon PDF'i (23 Ekim)
- Kullanıcı: "Index olarak versene bana tasarımı" → `site-tek/index.html` (13,7 MB, bütün site; sayfalar # ile: `#lunadream-gece-lambasi`).
- "WhatsApp'tan attım, telefonda görünmüyor" → HTML dosyası telefonda JavaScript çalıştırmaz. `site-tek/LunaDream-telefon.pdf` (390 px, 2x, 9 sayfa, 1,2 MB; yapışkan çubuk gizli) üretildi: `scratchpad/pdf-cek.js` ile tam sayfa görüntü + PIL ile sayfalara bölme.
- (Masaüstü ızgara ekran görüntüsüyle) "Burayı kaydırmalı yap, çok uzun iskelet webde iyi durmuyor" → `ayluna.css` masaüstü bloğu: `.noscroll:has(>.kart)` tek satır kayar (kart 204 px). Oklar şablonda (`ortak.SERIT_OK`, `KAY_JS`, `SERIT_OK_CSS`; her saniyelik çizimde silinmesin diye çalışma anında eklenmez), yalnız masaüstünde görünür. Bağlı: `luna_e.py`, `luna_usb.py`, `ozel_sayfa.py`. Site testi: 4 sayfada tek satır, ok kaydırır, telefonda ok yok.
- Site testleri, tema benzetimi HEPSİ TAMAM; Theme Check 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.21.zip`; tuval Sürüm 146, site Sürüm 38.
- Kullanıcı: "Emoji benefit neden ürün görsellerinin altında?" → seçim "Sağa, fiyatın altına". `urun_ust` artık imza sayfalarında `oz` almıyor (luna_e, luna_usb, ozel_sayfa): masaüstünde galeri solda yapışkan, özellik kartları sağda satın alma kutusunda (telefon sırasıyla aynı). Site testi: masaüstünde `.sol-oz` yok, Sihirli galerinin sağında. Buton artık ilk ekranın altında kaldığı için masaüstü yapışkan çubuk hızlı kaydırmada açılmıyordu; `ayluna.js cubukBak` kaydırmada butonun yerine de bakar. Site testleri (159), tema benzetimi HEPSİ TAMAM; Theme Check 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.22.zip`; tuval Sürüm 148, site Sürüm 39.

## Galeri 2. tur + LunaDream sadeleşti (23 Ekim)
- Kullanıcı: "Site görsellerini beğenmedim; satış odaklı değil, yorum görseli yapılmamış, çok sönük." 3 yön çizildi (`araclar/gorsel/afis_yon.py`, `canvas/p-gorsel/yon/`); eleştirmen A'yı (gece vitrini) öne aldı (A 7, B 5, C 5) ve karmayı seçti.
- Yeni galeri 5 kare (`araclar/gorsel/afis_uret.py` → `canvas/p-gorsel/afis-1..5.jpg`): 1 açılış "Tavanı masala çeviren lamba" (Kız, gece, tavanda yansıma, lamba büyük; 3 halka) · 2 yorum "Reklamındaki gibi mi?" (Abdülkerim T., Mehmet C., Handan B.; Loox birebir, düz kart, 36 px) · 3 "Her gece başka bir masal" (disk yayı) · 4 "Uzay Kaşifi erkek modeli" (c-erkek-gece, etiketli robot) · 5 "Kutudan ne çıkıyor?" + güven şeridi (Ücretsiz kargo · 30 gün iade · Kartla %5 indirim; "kapıda ödeme" yazılmaz). Açılış ve Erkek kırpması Real-ESRGAN ile büyütüldü (`canvas/c-gorsel/hd`).
- Asset'ler: 756460fe…, 447d1a0f…, 992615e3…, 3c0683cd…, 1bf394a6… (`P_GAL`, `blob-yerel.json`). Site testi `PREMIUM` 5.
- Kullanıcı: "Site çok mu karmaşık, boğucu mu?" → eleştirmen 6/10, sebep tekrar. "Düzelt, kötü ve gereksiz kısımları bir mantığa oturt." Yapılanlar (`luna_e.py`): dönen satır kalktı, kargo sayacı teslim kartında (`.yol-not`); yapışkan çubukta "1 Adet · Kız" (sayaç yok); `DUN = ''` (bayat "Dün 62" gizli; temada sayı + aç/kapa); SSS 7 soru; Sihirli şarj kartı "USB kabloyla şarj olur"; çapraz satış görselleri yazısız kesim (`canvas/capraz/`, 12 yeni asset). Diskler başlığı "Bu gece hangi masal?", dönen satırdaki "+6 hediye" de kalktı. Sayfa 7679 → 7324 px (E_H 7324; Videolar geri geldikten sonra).
- Site testleri (158) ve tema benzetimi HEPSİ TAMAM; Theme Check yalnız 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.19.zip`. Tuval Sürüm 142, site Sürüm 36.
- Erkek galerisi artık c-erkek-gece (yan plakada "UZAY KAŞİFİ PROJEKTÖR" baskısı var); baskısız p-erkek kareleri galeride yok.
- Kullanıcı: "Gerçek ürün videoları olan kısım gitmiş oldu ama." Videolar bölümü sadeleştirmede yanlışlıkla kaldırılmıştı (önizlemedeki kapaklar yer tutucu; canlıda gerçek Shopify videoları). Eski yerine geri geldi; testler yine Videolar → Neler → Odası sırasını bekler. Site testleri ve tema benzetimi HEPSİ TAMAM, Theme Check 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.20.zip`; tuval Sürüm 144, site Sürüm 37.
- Galaxy USB ve diğer sayfaların çapraz satış kartlarında hâlâ yazılı afişler var (bu tur yalnız LunaDream).
- Bekleyen: kutu listesindeki "6 hediye disk" satırı kalsın mı (SSS ve afiş 5); 5 görsel dosya olarak gelmedi.

## Ürün soruları bütün ürün sayfalarında (22 Ekim)
- Kullanıcı: "Diğer ürünler için de benzer SSS kısımlarını oluştur."
- `araclar/tuval-uret/urun_soru.py`: kartın CSS'i (`URS_CSS`, LunaDream'in `.urs`'i; renkler sayfa değişkenlerinden), `urs_html()`, ürün başına `SORU` (urs: teslim altı 4 soru; ek/sss: alttaki SSS'ye giden ürün soruları) ve `sorular(icerik)` (aynı soru iki yerde olursa hata verir).
- Bağlananlar: `urun_sade.py` (11 sade ürün + sade AyFeneri/Galaksi Night; "Kutuda ne var" bölümü kalktı, kutu 4. soruda), `ozel_sayfa.py` (AyFeneri, Galaksi Night; teslim çizgisinin altında), `luna_usb.py` (teslim kartının altında; SSS'den "Kutudan ne çıkıyor" ve "Gece lambası" çıktı).
- Mağazadaki açılır sorular kaynak alınmadı (çoğu başka üründen kopya). Cevaplar `ogrenme/urun-icerik.json` ve kullanıcı teyitlerinden; bilinmeyen [teyit].
- Pano boyları ölçüldü: GalaxyUSB 7595, AyFeneri 7188, GalaksiNight 7529; sade sayfalar `canvas/urunler/yukseklik.json`.
- Site testi: diğer 14 ürün sayfasında kart teslimin hemen altında, 4 soru, satır ≥ 48 px, açılınca dolunay, SSS'de tekrar yok, "Kutuda ne var" yok.
- Site testleri (165) ve tema benzetimi HEPSİ TAMAM; Theme Check yalnız 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.18.zip`. Tuval Sürüm 140, site Sürüm 35.

## Galeri = satış afişleri (22 Ekim)
- Kullanıcı: "Ürün görsellerini beğenmedim, düzeltmeni istiyorum." → "Eskilerinin ki satış odaklı görseller olsun, USB'ninki gibi." Salt fotoğraf galerisi kalktı; galeri USB galerisi gibi afiş.
- `araclar/gorsel/afis_uret.py`: premium fotoğraflardan 6 afiş (1080 kare JPG) → `canvas/p-gorsel/afis-1..6.jpg`. Yazı HTML (Young Serif + Onest, `onizleme/f`), Playwright ile basılır. Çalıştırma: PIL'li Python + `NODE_PATH=/opt/node-tools/node_modules`.
  1. Masal anlatan / gece lambası (koyu, Kız gece; 6 masal diski, Bluetooth ninni, 3 kademe ışık)
  2. Her gece / yeni bir masal (krem, diskler; "Kutuda 6 masal diski, masalı o seçsin.")
  3. Telefondan ninni, / lambadan çalsın (sıcak, elde; Bluetooth, ninni ve masal, şarjlı)
  4. Uzay Kaşifi / erkek modeli (krem, Erkek gündüz)
  5. Işık kapanınca / masal başlar (koyu, Erkek gece; yazı sağ altta)
  6. Kutudan / ne çıkıyor? (krem, Kız tam + 6 disk + kutu listesi)
- Tuval asset'leri: 431c14e7…, 19fdd440…, 6aaf7301…, 7805eb49…, 726517a5…, 39ff6e02… (`blob-yerel.json`). `luna_e.py` `P_GAL` bunlara döndü; site testi `PREMIUM` 6.
- Değiştirmek için: `AFIS` listesinde başlık/alt yazı/özellik değiştir → betiği çalıştır → asset'leri yeniden yükle, `P_GAL` ve `blob-yerel.json` id'lerini güncelle.
- Kullanıcı: "6+6 masal yerine 6 masal yaz sadece." Afiş 1, 2, 4, 5 yeniden basıldı (etiket "6 masal / diski", afiş 2 alt yazısı "Kutuda 6 masal diski, masalı o seçsin."); Sihirli disk kartı "6 masal diski · Her gece başka masal." (`sihirli2_varyant.OZ`); Odası çipi "6 masal diski"; ana sayfa slaydı "kutuda 6 masal diski". Kutu listeleri (SSS cevabı, afiş 6) "6 hediye disk" satırını koruyor; kullanıcıya soruldu.
- Site testleri, tema benzetimi HEPSİ TAMAM; Theme Check yalnız 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.17.zip`. Tuval Sürüm 139, site Sürüm 34.
- Bekleyen: Erkek "UZAY KAŞİFİ" baskısı kararı; gelmeyen 5 kare (Kız gündüz gelince 1. afişin yanına ya da model kartına).

## Galeri = premium set (22 Ekim)
- Kullanıcı ChatGPT'de üretip 5 kare gönderdi (dosya olarak gelen: 21-25). Sohbet arasında gönderdiği 5 kare daha (Kız gündüz, disk seçen eller, erkek odası, ninni, kız odası) görüldü ama dosya olarak gelmedi; yeniden istendi.
- `canvas/p-gorsel/`: p-kiz-gece (23), p-elde (22), p-diskler (21), p-erkek-gunduz (25), p-erkek-gece (24). Tuval asset'leri a31842e2…, 3d65f756…, 4fef037f…, 2d42fce7…, 0c17d626… (`blob-yerel.json`).
- `luna_e.py`: `P_GAL` (5 kare, alt yazılı) galeriyi besler; `canli_galeri` ve yazılı afişler (AD_LD) LunaDream galerisinden çıktı. Müşteri paylaşımı "Evlerinizden" şeridinde.
- Kontrol: Kız kareleri gerçek ürünle birebir. Erkek karelerinde yan plakadaki "UZAY KAŞİFİ PROJEKTÖR" baskısı yok; kullanıcıya soruldu.
- Bekleyen: p-kiz-gunduz (gelince ilk kare ve Kız model kartı), Erkek model kartı (p-erkek-gunduz, Kız kartıyla birlikte değişecek), 4 oda karesi → Odası böyle görünecek.
- Site testi: LunaDream galerisi 5 kare (`PREMIUM` istisnası), diğer ürünler mağaza sırası. Site ve tema benzetimi HEPSİ TAMAM; Theme Check yalnız 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.16.zip`. Tuval Sürüm 135, site Sürüm 33.

## Premium fotoğraf seti · GPT ile üretim betiği (22 Ekim)
- Kullanıcı ("görsellerde değişmesi iyi olur dediğin kısım neresi?") → 4 yer gösterildi: galeri (6 karenin 5'i yazılı afiş), model kartları, Odası böyle görünecek (4 yer tutucu), Diskler ("[gerçek tavan fotoğrafı]", kullanıcı çekecek).
- Kullanıcı: "Girip yap direkt GPT'den." Bu oturumda `OPENAI_API_KEY` yok (api.openai.com 401), Chrome uzantısı da bağlı değil; ChatGPT'ye girilemedi. Kullanıcıya anahtarı ortam ayarına eklemesi söylendi (sohbete değil).
- `araclar/gorsel/gpt_uret.py`: istemleri `ogrenme/chatgpt-istemleri-lunadream.txt`'den okur, ekleri depodaki dosyalardan (REF eşlemesi) yükler, `images/edits` (gpt-image-1, high) ile 11 kareyi `canvas/p-gorsel/`'e yazar. `--dene` yalnız planı gösterir (11 kare, ekler tamam). Anahtar yalnız ortamdan, komut satırına yazılmaz.
- Anahtar gelince: üret → her kareyi büyütüp gerçek ürünle karşılaştır (tavşan, kubbe, robot yüzü, el, yazı) → uyanlar galeri 1-7, model kartları 1 ve 3, Odası 8-11, Diskler 7; gelmeyen yerde bugünkü görsel kalır.

## Tema 1.0.15 · Teslim kartının altında yalnız 4 soru (22 Ekim)
- Kullanıcı: "O kadar çok soru olmasın kargo takibin altında."
- `.urs` artık 4 soru: Bu ürün ne işe yarıyor? / Projeksiyon nasıl çalışıyor? / Bluetooth var mı, ne işe yarıyor? (hoparlör cevabı buna katıldı) / Kutu içeriğinde neler var? "7 soru daha" düğmesi ve `ursHepsi` kalktı.
- Diğer 8 ürün sorusu (şarj, gece rutini, ışık, güvenlik, tuşlar, hareket sensörü, Bluetooth bağlanma ve sorun) alttaki "Merak edilenler" SSS'nin başında; ardından yaş, kargo, ödeme, iade (12 soru). E_H=7647. Site testleri (teslim altında 4 soru, satır 54 px, dolunay, SSS tekrarı yok) ve tema benzetimi HEPSİ TAMAM; Theme Check yalnız 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.15.zip`. Tuval Sürüm 134, site Sürüm 32.

## Tema 1.0.14 · Ürün soruları teslim kartının altında; site görsel düzeltmesi (22 Ekim)
- Kullanıcı: "Görsel görünmüyor ya dostum." Neden: site önizlemesine (Sürüm 29) yalnız sayfa ve görseller gitti, `veri.js` gitmedi; `/_blob/` → `g/` eşlemesinde yeni lamba parçaları yoktu. `veri.js` yayınlandı (Sürüm 30). **Site yayınında yeni görsel varsa `veri.js` de gönderilir.** Tema ve yerel site doğruydu.
- Kullanıcı (mağazadaki açılır sorular ve SSS ekran görüntüleriyle): "Bunları da ekle, kargo takibin altına; o kısma mükemmel otursun."
  - `luna_e.py`: teslim kartının hemen altında `.urs` (aynı kart: krem, 1 px çizgi, 20 köşe). `<details>` satırları ≥ 54 px; kapalıyken hilal, açılınca dolunay (`URS_AY`, teslim çizgisinin `ay()` çizimi; opacity), ok döner. İlk 6 soru, "7 soru daha" (`ursHepsi`).
  - 13 soru; cevaplar canlı LunaDream sayfasından (`scratchpad` dışında saklanmadı) ayıklandı: "Bu model hareket sensörlü değildir" → "Hareket sensörü var mı? Yok."; sensörün nasıl çalıştığı (AyFeneri kopyası) alınmadı; "Şarjı ne kadar gider?" canlıda da boş ve pil süresi yazılmaz → yok; "göz yormaz", "güvenlidir" gibi iddialar yerine kullanım önerisi; kutu içeriği teyitli liste (kılavuz yazılmadı). Projeksiyon cevabı modele bağlı (Kubbeyi / Robotun başını).
  - Alttaki "Merak edilenler" SSS'den kutu, ninni ve ışık soruları çıktı (yukarıda var); SSS satın alma sorularına kaldı (yaş, kargo, ödeme, iade).
  - Canlıdaki "1 Yıl Garanti · 90 Gün Para İade Garantisi" bandı alınmadı: iade 30 gün, garanti teyitsiz.
- E_H=7321. Site testleri (yeni: soru kartı yeri, 6 + "7 soru daha", satır 54 px, dolunay, 13 soru, SSS tekrarı yok, pil sorusu yok) ve tema benzetimi HEPSİ TAMAM; Theme Check yalnız 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.14.zip`. Tuval Sürüm 133, site Sürüm 31.

## Tema 1.0.13 · "Neler yapabiliyor?" = Dergi kapağı (22 Ekim)
- Kullanıcı 4. turda (sayfa içi GIF) "Dergi kapağı"nı seçti. Erkek sorusuna: "Başı açılır, üstten" (teyitli ürün bilgisi).
- `luna_e.py`: OZ3 (afiş) çıktı; `import ozellik4_varyant as OZ4`, CSS `OZ4.CSS`, `#neler` = `OZ4.dergi()`, JS `OZ4.js_tur('dk')` + `OZ4.JS_ORTAK + OZ4.JS_DK` + `OZ4.js_kapat('dk')` + `OZ4.js_dk_deger("S.model === 'erkek'")` (dönüşte `...dkV`). Sınıf öneki `dg-` (USB Diskler `dk-` kullanır).
- Erkek: robot kesimi baş/gövde (`parca/erkek-ust|alt.webp`, baş dışındaki sütunlar gövdede kalır; tuval asset 825ac9de…, de7706ac…). Robot daha alçak (290 px), yazı sütunu 116 px; "Robotun başını aç, masal diskini üstten tak."
- Masaüstünde 1,1 zoom (394 px, 430 px sütunda ortada). E_H=7107, OZ4_H=883.
- Testler (site): sıra, 4 kelime / 4 düğme, kubbe-gövde ayrı, lamba kelimenin önünde, beyaz kart yok; ekrana girince tur; Kıs → i2 ve lamba kısılır; Şarj → sarjdol, lambaya dokununca yeniden; Erkek; masaüstü. Site + tema benzetimi HEPSİ TAMAM; Theme Check yalnız 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.13.zip`. Tuval Sürüm 132, site Sürüm 29 (yayındaki sayfa önce okundu, e19f3cd derlemesiyle aynıydı).

## "Neler yapabiliyor?" 4. tur: Dergi kapağı (22 Ekim)
- Kullanıcı (dokunulur afişten sonra): "Yine çok beğenmedim, sıkıcı geliyor gözüme."
- Teşhis: afiş, hemen üstteki Sihirli özellikler'in dört beyaz mini arayüz kartını (disk, ışık, Bluetooth, şarj) aynı dille tekrar ediyordu. Kural: aynı özellik iki bölümde aynı dille anlatılmaz (TASARIM-BILGISI, SKILL).
- Ürün kesimi ikiye bölündü (`canvas/c-gorsel/parca/`: kiz-ust/alt/tam, erkek-ust/alt/tam; tuval asset'leri `blob-yerel.json`'da). Kubbe gerçekten kalkar.
- `ozellik4_varyant.py` → `canvas/LunaDreamE-Ozellik4.dc.html` (tuvalde x=4230, y=8989; Sürüm 130):
  - Üç taslak yapıldı (git c70efe8): A Dergi kapağı 8, B Atlıkarınca 4, C Albüm 3. Eleştirmen B ve C'yi eledi (21 Eki "yörünge düğümleri geri getirilmez", "deste premium değil"; C'de ürün oynamıyor). Dürüst seçenek olarak "bölüm kalksın" 6.
  - **A · Dergi kapağı:** dev tek kelime Tak. / Çal. / Kıs. / Şarj. (Young Serif 128 px), lamba kelimenin önünde; her kelimede zemin perdesi alttan yükselir (ton → lacivert → gece → #FFFDF9). Tak: kubbe kalkar, disk üstten girer. Çal: üç nota. Kıs: Parlak/Orta/Kısık (koyu kopya opacity, kelimeler amber kopyayla). Şarj: lamba söner, ışık alttan yukarı dolar (pencere yukarı, içi aşağı kayar; kablo/port/süre çizilmez). Tur bir kez, "Tak."ta biter; alt sözcüklere ya da lambaya dokununca o oynar.
  - Eleştirmen düzeltmeleri işlendi: "Taşı / istediğin yere" (taşıma, pil vaadi) → "Şarj. Şarjlı, kablosuz kullanılır."; hikâye göstergesi gibi dolan çizgi yok; pasif etiket #5C6078; sabah zemini kenarlı.
  - Kullanıcıya sayfa içinde (Videolar ile Odası arasında) GIF gösterildi; Dergi kapağı seçildi (yukarıda).

## Tema 1.0.12 · "Neler yapabiliyor?" kartları dokunulur (22 Ekim)
- Kullanıcı durgun afişin ekran görüntüsüyle: "Çalışmıyor ki bu kısım." Kartlar yalnız bir kez oynayıp duruyordu, dokununca hiçbir şey olmuyordu.
- `ozellik3_varyant.py` yeniden yazıldı: kartlar `<button>`; sekanslar CSS gecikmesi yerine JS zamanlayıcıyla (`kOyna`: 2,1 / 4,5 / 6,9-7,7 / 9,3 sn, 11,7 sn'de biter). Her oynatışta kart sınıfı `oa`/`ob` arasında değişir (`ciftle()` keyframe'leri `2` ekiyle çoğaltır), böylece animasyon baştan başlar.
  - Diski tak → sıradaki disk (Ay ve yıldız, Okyanus, Uzay, Deniz kızı, Şato) takılır, adı kartta yazar.
  - Işığı kıs → Parlak / Orta / Kısık (`i0/i1/i2`); lambanın koyu kopyası ve hale opacity ile kısılır.
  - Telefondan çal, Şarj et → sekans yeniden oynar.
  - Tur: IntersectionObserver; afiş ekrana her girişte tur baştan oynar. Dokunulduysa (`kElle`) tur bir daha başlamaz. `azH` (azaltılmış hareket) açıksa tur yok, dokunuş çalışır.
  - Altında ipucu: "Kartlara dokunup dene."
- Tuval panosu yalnız afiş (Hikâye yedeği çıktı), OZ3_H=814; E_H=7097. Testler: dokunuş (disk → Okyanus, `oa/ob`, `i1`, koyu .5), Erkek, masaüstü; site + tema benzetimi HEPSİ TAMAM; Theme Check yalnız 31 RemoteAsset.
- Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.12.zip`. Tuval Sürüm 128, site Sürüm 28.

## Tema 1.0.11 · "Neler yapabiliyor?" = Afiş, ürün önde (22 Ekim)
- Kullanıcı 3. turda "1 · Afiş, ürün önde"yi seçti. Disk sorusuna: "Kubbe açılıp üstten" (teyitli ürün bilgisi).
- `luna_e.py`: Aydınlık sahne (OZ2) çıktı; `#neler` = `OZ3.afis('nf')`, CSS `OZ3.AFIS_CSS`, JS `OZ3.js_afis_tur('nf')` + `OZ3.js_afis_deger('nf', "S.model === 'erkek'")` (dönüşte `...nfV`). Durum `nfOn` (false: bekler, true: kartlar oynar).
- "Diski tak" kartı: tonda kutuda çizgi lamba (Kız atlıkarınca / Erkek robot); kubbe 10 px kalkar, Ay ve yıldız diski üstten iner, kubbe kapanır (2,4 sn, bir kez). Erkek'te robotun başı kubbe sayıldı (aynı mekanizma varsayıldı; teyit gerekirse sorulacak).
- Afiş 358 px tabanlı; 375/360 px telefonda zoom .958/.916, masaüstünde 1,1 (394 px, 430 px sütunda ortada).
- E_H=7067, OZ3_H=1618. Site testleri (sıra, 4 kart, lamba kartların önünde, ekrana girince oynar, Erkek fotoğrafı, masaüstü genişlik/orta/kesim hizası, 360 px disk şeridi) ve tema benzetimi HEPSİ TAMAM; Theme Check yalnız 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.11.zip`. Tuval Sürüm 125, site Sürüm 27.
- Site önizlemesinde 19 görsel hiç yayınlanmamıştı (AyFeneri, Galaksi Night, Mesajlar ve LunaDream'de kullanılan); hepsi yüklendi. Diğer ürün sayfalarının yayındaki HTML'i yerel derlemeden eski olabilir; ilk fırsatta karşılaştırılıp yayınlanmalı.

## Disk kartı sığar; "Neler yapabiliyor?" 3. tur: koyu afiş + arayüz kartları (22 Ekim)
- Kullanıcı (Sihirli disk kartının ekran görüntüsüyle): "Disk kartı tam sığmıyor; Aydınlık sahne kısmını hiç ama hiç beğenmedim, yeni bir tarz deneyelim."
- **Disk kartı:** şerit (`S2.ui_serit`, `SERIT_CSS`) = ortadaki disk + iki tam komşu (k 128 px, b 152 px); solda bir komşu (son disk), sağda döngü için iki disk; pencere halkası kesilmez. "Diskleri gör" bölünmez. USB ortak şeridi de aynı (5 → 7 disk öğesi). Test: 360 px'te şerit ≤ kart ekranı. Tuval Sürüm 123, site Sürüm 25 (yayında).
- **Neler 3. tur** (`ozellik3_varyant.py` → `canvas/LunaDreamE-Ozellik3.dc.html`): sitedeki afiş dili (images/18.png: koyu ürün fotoğrafı, arayüz kartı ürüne biner).
  - İlk taslak: A Afiş 7/7, B Hikâye 8/4, C Bento 5/5 (git f2c6b0c).
  - Eleştirmenin seçimi işlendi: **A "ürün önde"**: c-an-kiz / c-erkek-disk yerel Real-ESRGAN x2 (`/tmp/sr-env`, `scratchpad/sr.py`), lamba kesimi rembg isnet-general-use (`scratchpad/kes.py`); fotoğraf → koyu hale → kartlar → kesim → kesimin koyu kopyası. Kartlar ürünün arkasına girer, ürüne bakan kenarda iç boşluk. Başlıklar eylem (Diski tak, Telefondan çal, Işığı kıs, Şarj et); gölge yok; kartlar 0/0,5/1/1,5 sn'de gelir, sekanslar 2,1/4,5/6,9/9,3 sn'de tek tek (2,4 sn) oynar ve durur. **Işık kartı lambayı kısar** (koyu kopya + hale, yalnız opacity).
  - Yeni asset'ler (tuval): c-an-kiz-x2 9fc836c3…, c-an-kiz-kesim.webp 64acd867…, c-erkek-disk-x2 d78da0ee…, c-erkek-disk-kesim.webp 55988cac… (`blob-yerel.json`).
  - Yedek: B Hikâye (Ken Burns yok, başlıklar binmez, Masal'a dönüp durur).
  - Eleştirmenin 3. fikri (Masal kartında kubbe açılıp disk iner) diskin nasıl takıldığı teyit edilmeden çizilmez; kullanıcıya soruldu.
  - Seçim bekleniyor. Sayfadaki Aydınlık sahne seçilen yönle değişecek (tema 1.0.11).

## Tema 1.0.10 · LunaDream "Neler yapabiliyor?" = Aydınlık sahne (21 Ekim; 22 Ekim'de kullanıcı beğenmedi)
- Kullanıcı 1. tur için (Satırlar / Sekmeler / Kaydırmalı): "Hayır, o da çok boğar; daha iyi bir şeyler mi düşünsek, çok sıkıcı duruyor böyle." "21 animasyon" sorusuna tercih belirtmedi ([X] kalır, sayfaya çıkmaz).
- İlk taslak (`ozellik2_varyant.py`, git d090a34): A Yörünge sahnesi 7/5, B Etiketli ürün 6/6, C Masal kitabı 5/3. Eleştirmen: A'nın düğümleri akıllı ev uygulaması gibi, Tur 20 yörüngesine benziyor; B, Sihirli'nin aynısı ve hareketsiz; C kapakla içeriği saklıyor, Tur 5 kitabının aynısı.
- Eleştirmenin seçtiği üç yön işlendi (`ozellik2_varyant.py` → `canvas/LunaDreamE-Ozellik2.dc.html`, tuval Sürüm 120, Güncel sayfa x=3290):
  1. **Aydınlık sahne:** stüdyo fotoğrafı (358 × 440), etkiler lambanın çevresinde (üç amber halka, ses dalgaları), altta disk / kademe / pil rozeti; dört eylem etiketi.
  2. **Gece kadranı:** lacivert sahne, 200 px yuvarlak pencere, yayda dört yazı, amber ay noktası yazıdan yazıya. Seçilirse vitrinle arasında en az 36 px krem boşluk.
  3. **Etiketli ürün:** fotoğraf, dört eylem etiketi, altta tek cümle (güvenli yedek).
- Ortak: "[X] ışık seçeneği" yok ("Üç kademe: kısık, orta, parlak."); disk lambanın tepesine inmez, rozette belirir; gece fotoğrafı yok (Videolar gösteriyor); her durum 6 sn, ekrana girince tek tur, Masal'da durur, dokununca durur; renk/gölge canlandırılmaz.
- Kesim temizliği denendi (açık kenar + zemin): kesimin alt kısmı bozuk; koyu sahnede kesim yerine yuvarlak pencerede stüdyo fotoğrafı.
- GIF'ler gönderildi. Kullanıcı: **1 · Aydınlık sahne**.
- Uygulandı: `luna_e.py`'de Videolar ile Odası arasında `<section id="neler">`. Kod pano ile ortak: `ozellik2_varyant.NZ_CSS`, `sahne('nz')`, `js_degerler('nz')` (renderVals dönüşüne `...nzV`), `js_tur('nz')` (componentDidMount; `clearTimeout(this.turnz)`). Durum `nz`, `nzDur`. Sınıflar `nz-` önekli (sayfada `.ek` ve `.hk` başka işte).
- Sahne kapsayıcı genişliğine bağlı (`container-type:inline-size`, cqw; 358 tabanı, oran 358/440): 375 px telefonda ve masaüstündeki 430 px sütunda (`ayluna.css` `#neler{max-width:430px}`, sahne 398 px) aynı oranla kurulur.
- Fotoğraf yer tutucu: m-kiz / m-erkek (galeride de var). Premium set gelince p-kiz-gunduz / p-erkek-gunduz.
- E_H=7087, OZ2_H=2269. Site testleri (sıra, 4 etiket, rozet, dokununca durur, Erkek fotoğrafı, masaüstü oran ve halka ortası) ve tema benzetimi HEPSİ TAMAM; Theme Check yalnız 31 RemoteAsset. Tema `tema-zip/ayluna-SHOPIFY-TEMA-1.0.10.zip`. Tuval Sürüm 122, site Sürüm 24.

## Tema 1.0.9 · Galaxy USB canlı kartlar; LunaDream "Neler yapabiliyor?" taslakları (21 Ekim)
- Kullanıcı (sitesindeki özellik anlatımının ekran görüntüsüyle): "USB için de yap aynısını; bir de LunaDream için sitemde olan bu tarz bir tasarım istiyorum, yine UI kullanabiliriz."
- **USB (uygulandı):** `luna_usb.py` özellik hücrelerinde `.uk-ek` ekranları (UK_TAK, ortak disk şeridi `S2.ui_serit('k', UK_DISK)`, UK_BOYUN, UK_LAMBA, cetvel); teslim `.teslim` kartı + `.y-ik` USB ikonu. Disk şeridi CSS'i `S2.SERIT_CSS` (USB'de `.fis` çakıştığı için yalnız şerit alınır; `.ui-serit` kendi `position:relative`'i ile kırpılır). U_H=7480. Test: 5 ekran, şerit, teslim ikonu.
- **LunaDream özellik anlatımı (karar bekliyor):** `ozellik_varyant.py` → `canvas/LunaDreamE-Ozellik.dc.html`. Eleştirmen 1. tur: Satırlar 7, Sekmeler 6, Kaydırmalı 5; düzeltmeler işlendi (gerçek ürün kesimi modele bağlı, kumanda paneli yok, eylem başlıkları, tek cümle, ekran 140 px, iddia temizliği). Yeri: Videolar'ın altı, Odası'nın üstü. Kullanıcıya soruldu: yön, ışık seçeneği sayısı ([X]), desen dönüyor mu.

## Tema 1.0.8 · Sihirli özellikler canlı kartlar, teslim kartı (21 Ekim)
- Kullanıcı: "Emoji benefit kısmını vesaire biraz daha kurumsal yapsak ve UI'lerle doldursak; dönen diskler sırayla masal diskini gidip gelse gibi tatlı ufak sekanslar."
- `sihirli2_varyant.py` → `canvas/LunaDreamE-Sihirli2.dc.html`: üç yön (Canlı kartlar 7, Bento 6, Özellik turu 4); eleştirmen düzeltmeleri işlendi (disk yalnız kayarken yuvarlanır; pil sekansı, lamba şarjda sönük; LunaDream ikonu; cümleler kısa). GIF'ler kullanıcıya gönderildi.
- Kullanıcı: **Canlı kartlar** + aynı dil **teslim çizelgesine**.
- `luna_e.py`: eski V1 kartları ve CSS'i gitti; `.sih` içinde `S2.kart_a` kartları, CSS `S2.MINI_CSS` (pano ile ortak; `sihirli2_varyant` yalnız doğrudan çalışınca dosya yazar). İkon `S2.IKON` (renderVals `sihKiz`/`sihErkek`). Teslim: `<div class="teslim">` içinde mevcut `.yol` (ay evreleri ve 8 sn döngü korunur), ton ekran, paket kutusu (`KUTU`), Kapında'da `.yol-lamba`.
- Masaüstünde disk şeridi kendi genişliğinde kırpılır (`.ui-serit{overflow:hidden}`).
- E_H=6485, S2_H=1705. Site testleri (Sihirli 4 ekran, teslim lambası, ikon modele bağlı dahil), tema benzetimi HEPSİ TAMAM; Theme Check yalnız RemoteAsset.

## Premium fotoğraf seti hazırlığı (21 Ekim)
- Kullanıcı: "Biraz daha kurumsal bir görüntü oluşturmanı istiyorum; ürünün premium fotoğrafları olmalı." Sonra: "ChatGPT'den yaptır."
- Bu oturumda Flow da OpenAI anahtarı da yok (api.openai.com 401). Hazırlananlar:
  - `ogrenme/premium-fotograf-seti.md`: fotoğraf dili, 11 karelik çekim listesi, sayfadaki yerleri (galeri, model kartları, vitrin, Diskler).
  - `ogrenme/chatgpt-istemleri-lunadream.txt`: kare başına yapıştırılacak istemler.
  - Referans paketi `lunadream-referans.zip` (canvas/ dosyalarından, 01-13).
- Kareler gelince: galeri yazılı afişler yerine 1-7 + oda kareleri; model kartları 1 ve 3; vitrin 8-11; Diskler 7. Gelmeyen kare için bugünkü görsel kalır.

## Tema 1.0.7 · Bir gece kalktı, yerine Gece vitrini (21 Ekim)
- Kullanıcı: "Bir gece, beş an bir şey hissettirmiyor"; onun yerine çocukların odalarında mutlu hâlini gösteren görseller önerdi, benzer markaları araştırmamı istedi.
- Araştırma (`ogrenme/rakip-sayfalar.md`, `ogrenme/rakip-derleme.jpg`): saat saat ritüel bölümü hiçbir markada yok; mutlu çocuk karesi tek başına değil, çocuk + ürün + ışığı aynı karede (Tonies, Moonlite, Cloud b); gerçek müşteri içeriği ayrı şeritte.
- Eleştirmen: Bir gece kalksın; "Odası böyle görünecek" 4 karta çıksın ve onun yerine taşınsın (8/10). Kullanıcı: "Odası böyle görünecek'i yapmıştık zaten" → yeni bölüm değil, aynı bölüm büyüdü; sayfada tek Odası var. Kullanıcı: "Profesyonel bir görüntü istiyorum."
- Dört arayüz denendi (`canvas/LunaDreamE-Oda2.dc.html`, `luna_e_oda2.py`): Gece vitrini 8, Kemerli pencere 6,5, Hikâye 6 (USB'nin tekrarı), Deste 4. Uygulanan: **Gece vitrini**.
- `luna_e.py`: Bir gece kadranının bütün CSS/HTML/JS'i (KAD_*, IZ_*, geceKaydir, geceTuval, moments) ve iki posterli eski #odalar silindi. Yeni `#odalar.vitrin` Videolar ile "Aileler ne diyor?" arasında: lacivert panel (28 px), kart 280×372, ortadaki kart kaydırmayla büyür ve aydınlanır (`animation-timeline: view(inline)`, yoksa sınıf geçişi), yazı altta 280 ms'de değişir, 4 ay gezgini (48 px). Çip fotoğrafa binmez, sayaç yok. Her kartta eylem: Kız modelini seç / Modelini seç / Erkek modelini seç / Diskleri gör.
- Masaüstü (`ayluna.css`): kenardan kenara bant ve şerit, ortadaki kart 360×480, yazı ve aylar altta ortada.
- Görseller yer tutucu: çocuklu 4 kare Flow'da üretilecek (`ogrenme/flow-istemleri-lunadream-oda.md`; tavan deseni gerçek diskten, yüz yakın plan değil, Türk evi, "müşteri" etiketi yok).
- Sayfa yaklaşık 2.500 px kısaldı (E_H=6405). Site testleri (vitrin denetimleri dahil), tema benzetimi HEPSİ TAMAM; Theme Check yalnız RemoteAsset uyarısı.

## Tema 1.0.6 · mesajlar bütün ürün sayfalarında (21 Ekim)
- Kullanıcı: "Şu WhatsApp konuşmaları için olan kısım eksik, bir tek LunaDream'de var."
- `ortak.py`: `mesaj_bolum(baslik)`, `MESAJ_CSS`, `mesaj_js(js)` (renderVals'a mesaj verisi ve büyük görünüm durumu; `return {` ve `return Object.assign(R, {` ikisini de tanır). Büyük görünüm sınıfları `.mbuyuk`/`.mb-x` (ozel_sayfa'daki `.buyuk` ile çakışmasın).
- Galaxy USB, AyFeneri, Galaksi Night: yorumların altında, panonun kendi başlık biçimiyle. 13 sade ürün: "Alanlar ne diyor?" bloğunun altında. Hepsinde "LunaDream siparişlerinden; müşterilerimizin izniyle paylaşılan gerçek sohbetler." Masaüstünde tek satır kayar (400 px).
- Yükseklikler: U_H=7358 S_H_af=6951 S_H_gn=7414 (E_H=6844), sade ürünler `canvas/urunler/yukseklik.json`.
- Site testleri (mesajlar diğer ürünlerde denetimi dahil) ve tema benzetimi HEPSİ TAMAM.

## Tema 1.0.5 · mesajlar kendi şeridinde (19 Ekim)
- Kullanıcı (B düzenine): "E ama WP mesajları falan gidiyor." Karışık şeritte mesajlar fotoğrafların arasında kayboluyordu.
- `#yorumlar` sırası: puan → "Sizden gelen mesajlar" (6 mesaj, 320 px kart, dokununca büyür) → öne çıkan yorum → "Evlerinizden" (5 müşteri fotoğrafı, 200 px) → 4 kısa yorum → hepsini oku → not. Masaüstünde 400/260 px.
- E_H=6844. Site testleri ve tema benzetimi HEPSİ TAMAM.

## Tema 1.0.4 · yorum kısımları tek akış, alt çubukta fiyat yok (19 Ekim)
- Kullanıcı: telefondaki alt çubukta fiyat ("evet görünüyor") ve "yorum kısımlarının hepsi karmaşık, bir düzen oturtalım".
- Alt çubuk (LunaDream, USB, AyFeneri, Galaksi Night): fiyat yerine ürün adı + seçim ("1 Adet"), Satın al.
- Müşteri kanıtı: üç yön (A sekmeli, B tek akış, C duvar) ekran görüntüsüyle gösterildi; eleştirmen B 8/10, A 5/10 (fotoğraf/mesaj sekmede gizli, Loox eklentisine benziyor), C 4/10 (en uzun, dar sütunda okunmuyor). **Kullanıcı B'yi seçti.**
  - `#yorumlar`: puan → öne çıkan yorum (Abdülkerim T., çerçevesiz kart, lacivert tırnak) → "Sizden gelenler" şeridi (5 fotoğraf + 6 mesaj, 280 px aynı yükseklik, fotoğrafla başlar, dokununca büyük görünüm) → 4 kısa yorum → hepsini oku → "Yorumlar yalnız sipariş verenlerden; hepsi yayımlanır. Mesajlar izinle paylaşıldı."
  - Konu çipleri, eski kaydırmalı yorum kartları (.yk2) ve ayrı `#mesajlar` bölümü kalktı. Masaüstünde şerit tek satır kayar (kartlar 360 px).
- Eleştirmen notu: "4,7 · 62 yorum" ve "Dün 62 kişi" sayıları Loox'tan teyit edilmeli (yayından önce).
- E_H=6542. Site testleri (müşteri kanıtı tek bölüm denetimi dahil), tema benzetimi HEPSİ TAMAM; Theme Check yalnız RemoteAsset.

## Tema 1.0.3 · düğmede fiyat yok, müşteri mesajları (19 Ekim)
- Kullanıcı: "Güvenli Ödeme ile Al'da fiyat yazmasın (%5 fark zaten 80 lira az ödemek)" ve "bahsettiğim yorum kısımlarını yapmamışız".
- Kartla öde düğmesi bütün ürün sayfalarında yalnız "Güvenli Ödeme ile Al"; masaüstü çubuğu da (düğme metnini kopyalıyor).
- LunaDream: "Sizden gelen mesajlar" bölümü (yorumların altında): eski sitedeki 8 sohbetten 6'sı (`canvas/musteri/mesaj-*.jpg`, tuval asset'i, `blob-yerel.json`); telefonda kayan dikey kartlar, masaüstünde tek satır şerit; dokununca büyük görünüm (Esc/dokunuş kapatır, sayfa kaymaz, odak kapat düğmesinde, 48 px).
  - Eleştirmen: mesaj-6 ("zürafa/hayvanlar çıkmadı") kutu vaadiyle, mesaj-7 ("ürününüz gümrükte") aynı gün kargo sözüyle çelişiyor → konmadı (dosyalar duruyor).
  - "Aileler ne diyor?"daki müşteri fotoğrafları 84 px kareden 150 px dikey karta büyüdü, dokununca büyür; gerçek müşteri hikâyesi (IMG_4145, `musteri/foto-1.jpg`) eklendi. Eski sitedeki Higgsfield üretimi 5 "mutlu kullanıcı" fotoğrafı konmadı.
  - Öneri (kullanıcıya soruldu): Instagram sohbetlerindeki ad ve profil fotoğrafları bulanıklaştırılsın (KVKK).
- E_H=6632 (LunaDream 1700 px pencerede ölçüldü). Site testleri (düğmede fiyat yok, mesajlar denetimi dahil) ve tema benzetimi HEPSİ TAMAM.

## Tema 1.0.2 · paket seçimsiz açılır, Kaching arkada, Kapıda düğmesi yok (19 Ekim)
- Kullanıcı 1.0.1'i yükleyip yayına aldı, sonra geri kaldırdı (satış sitesi, sipariş kaçmasın). Dedikleri:
  - "Mobile geçirince ekrana tam sığmıyor." (Benzetimde 360/375/414'te taşma yok; büyük ihtimalle uygulamaların sayfaya kendiliğinden eklediği kutu. Ekran görüntüsü istendi.)
  - "Kapıda ödeme için Kaching bundle bağlıydı, o çalışmıyor; direkt 2'li seçili geliyor, seçili olmadan gelsin." → "Kaching bundle dediğim COD form, ben bağlıyorum." → "Kapıda ödeme kısmını ben koyacağım, sen koyma."
  - Seçim: "Bizim kartlar, arkada Kaching."
- Canlı sitede (eski tema) salt okunur inceleme: Kaching kutusu ürün formunun yanına kendiliğinden eklenir, açılışta seçili paket yok; EasySell kapıda formu paketi `kaching-bundle kaching-bundles-block` → `$$c.selectedVariants()`'tan okur ({variantId, quantity, properties.__kaching_bundles}). EasySell düğmesini `easysell-form` kancasının yanına koyar. Kaching sayfadaki `/cart/add` isteklerini yakalayıp kendi seçimiyle değiştirir; adreste `kaching_bundles=true` varsa dokunmaz.
- Yapılanlar:
  - Bütün ürün sayfalarında açılışta paket seçili değil (LunaDream/USB 2'li, AyFeneri/Galaksi/sade 1'li varsayılanı kalktı); seçimsiz alım 1 adet.
  - Shopify'da tasarımdaki Kapıda düğmeleri (ürün, masaüstü çubuğu, sepet) ve sepetteki kapıda notu gizli (`html.ay-shop [data-ay-kapida]`).
  - Satın al düğmesinin altında yuva (`data-ay-dis`, yamada içine dokunulmaz): `easysell-form` kancası + ürün bölümüne eklenen uygulama blokları (`@app`).
  - Ürün bölümünde görünmez `<kaching-bundle product-id>` yer tutucu; `kachingEsitle` tasarımda seçilen adedin Kaching paketini (radyo) seçer; `kalemler` kart ödemesinde satırlara `__kaching_bundles` yazar; ekleme `?kaching_bundles=true` ile (Kız + Erkek korunur).
  - Benzetime Kaching taklidi (gözlenen API) ve testler: paket seçili değil, Kaching 2'li seçildi, iki satırda indirim özelliği, Kapıda gizli, EasySell düğmesi yeniden çizimde yuvada. Tema benzetimi ve site testleri HEPSİ TAMAM; Theme Check yalnız RemoteAsset.
  - Kaching paketleri ile kart fiyatları karşılaştırıldı: hepsi aynı (Yıldız Işığı'nda Kaching %25 → 1 kuruş fark olabilir).
- Mesaj ve müşteri fotoğrafı bölümleri (eski sitede custom liquid): mesajlar gerçek ve izinli; fotoğrafların 5/6'sı `hf_` (Higgsfield) üretimi, müşteri diye gösterilmez. Kullanıcıya öneri sunuldu, karar bekleniyor.

## Tema 1.0.1 · gösterge gömülü, WhatsApp ve şirket bilgisi yok (19 Ekim)
- Kullanıcı (LunaDream galerisi ve "Bir gece" ekran görüntüleriyle): "burası böyle kalıyor ve burası böyle kalıyor" → "aynı sorun tüm sayfalarda var, o gömülü olsun fotoğrafların değiştiği zımbırtı; estetiği bozan hiçbir detay istemiyorum" → "temsili görseller yazısı da duruyor hâlâ" → "WhatsApp zımbırtılarını ve şirketi de kaldır, ben onları sonra kendim ekleyeceğim".
- **Galeri göstergesi fotoğrafın içinde:** bütün ürün sayfalarında (4 imza + 13 sade) fotoğrafın en alt kenarında ortada ince çizgiler; her fotoğrafa bir, geçilenler ve o anki beyaz, sıradakiler soluk; hafif gölge. Ay/disk/fener simgeleri kalktı: gömülünce Galaksi Night'ta afişin sarı bandına biniyor, AyFeneri'de kalabalık duruyordu. Masaüstünde de aynı (alt kenardan 10 px).
- **"Temsilî görseller" ve "Görseller temsilîdir…" notları kalktı** (galeri altı, oda/sahne şeritleri). Yalnız Hizmet şartları sayfasındaki "Görseller" maddesi kaldı (politika metni).
- **Galeri neden duruyordu:** cihazda "animasyonları azalt" açıksa (Windows'ta Animasyon efektleri kapalı) bütün sayfalarda kendiliğinden geçiş kapalıydı. Artık yine 5 sn'de geçer, kaymadan anında.
- **Bir gece:** tuvalin geniş Oynat penceresinde (1024 px+) kaydırınca an değişmiyordu (masaüstü koruması sitede olmayan panoda da çalışıyordu). Koruma yalnız sitenin masaüstü düzeninde.
- **Sağlamlık:** mağazada bir eklenti yüzünden süsleme adımı hata verirse galeri ve kaydırma yine başlar (`ayluna.js` ciz).
- **WhatsApp yok:** menü satırı, iletişim kartı, kargo takip ve iade düğmeleri ("Bize yaz", "İade için yaz" → İletişim), USB ve AyFeneri/Galaksi Night "Takılırsan WhatsApp'tan yaz", ana sayfa/USB/sepet güven kartı (yerine Kapıda ödeme / Ücretsiz kargo), SSS ve politika metinleri, kapıda formu notu, tema ayarı. Kullanıcı sonra kendisi ekleyecek.
- **Şirket bilgisi yok:** alt bilgideki unvan/MERSİS/adres/KEP satırları, iletişim notu, politika sayfalarındaki "Veri sorumlusu" ve "Satıcı" kartları (Taraflar: "Ayluna (ayluna.shop)"). Yasal zorunluluk: yayından önce eklenmeli (KURULUM.md).
- Pano yükseklikleri yeniden ölçüldü: `E_H=5953 U_H=6851 S_H_af=6430 S_H_gn=6906` (LunaDream 1700 px yüksek pencerede ölçülür; Bir gece adımları tuvalde kapanır).
- Test: `araclar/site/test.js` yeni denetimler (gösterge fotoğrafın içinde, "temsilî" yok, azaltılmış harekette galeri geçer, hiçbir sayfada WhatsApp/şirket yok) dahil HEPSİ TAMAM; tema benzetimi HEPSİ TAMAM; Theme Check yalnız RemoteAsset uyarıları.
- Açık: kullanıcının "Bir gece" görüntüsünde neyi kastettiği (takılma mı, kart kenarları mı) netleşmedi; takılma iki yoldan düzeltildi.

## Shopify teması 1.0.0 (19 Ekim)
- Kullanıcı: "Sen bana artık siteyi gönder bakalım bi" → "tema dosyası olarak son halini".
- Önizleme sitesi Shopify teması değildi; `shopify/` altındaki eski bölümler ilk LunaDream tasarımından. Tema sıfırdan kuruldu: `araclar/tema/tema_uret.py` → `tema/` + `tema-zip/ayluna-tema-1.0.0.zip` (241 dosya, 13 MB; ikisi de git dışında, betikle yeniden üretilir).
- Yapı: `layout/theme.liquid`; bölümler `ayluna-sayfa` (ana, koleksiyon, sepet, arama, 404), `ayluna-urun` (ürün adresine göre pano, yoksa sade sayfa + EasySell için gizli ürün formu), `ayluna-icerik` (iletişim ve yasal sayfalar adrese göre, diğerleri sade), `ayluna-sifre`; her pano bir snippet (`ay-*.liquid`); müşteri sayfaları sade.
- `ayluna.js` Shopify kipi: sepet `/cart.js`, mağaza adresleri, canlı fiyat/stok/varyant (`ay-canli`), kapıda ödeme EasySell (`[data-ay-kapida]`), iletişim/bülten `/contact`, WhatsApp tema ayarı. Önizleme kipi değişmedi.
- Doğrulama: Theme Check hatasız (yalnız Google Fonts uyarısı); `araclar/tema/benzetim.py` + `test-tema.js` (38 deneme) geçti. Gerçek mağazada denenmedi: EasySell seçicisi, Kaching paket indirimi, %5 kart indirimi → `araclar/tema/KURULUM.md` yayın öncesi listesi.
- Galerinin altındaki koyu şerit kaldırıldı (kullanıcı: "Şerit kalksın").

## Masaüstü görünüm (19 Ekim)
- Kullanıcı: "Bir de bu mağazanın masaüstü görünüşünü de yapmak lazım."
- 1024 px ve üstü yalnız CSS + ortak üst menü: `araclar/site/ayluna.css` sonundaki masaüstü bloğu, `ayluna.js masaUst()`. Telefon düzeni değişmez (test.js mobil + masaüstü denemeleri).
- Ürün sayfası: galeri + satın alma kutusu `.urun-ust` sarmalayıcısında (`ortak.urun_ust`); galeri yalnız bu kısımda yapışık. Ana sayfa geniş slayt, 4 sütun ürün; koleksiyon ve arama 4 sütun; sepet iki sütun (sağda yapışkan özet).
- Düzeltmeler: ürün alt bilgisi iki sütun; ürün sayfası butonları sepeti katlamaz (`Sepet.koy`); sepette paket satırında "2 × eski fiyat" üstü çizili yok (§7 kural 2); boş sepette ok kayması (telefonda da vardı).
- Eleştirmen (ayluna-elestirmen) 11 öneri verdi; en iyi 3'ü kullanıcıya soruldu, **üçü de seçildi**:
  1. Masaüstü yapışkan satın alma çubuğu (satın alma kutusu ekrandan çıkınca menünün altından iner; kapıda bağlantısında fiyat yok, sayaç yok).
  2. Sihirli Özellikler (ve diğer imza sayfalarındaki özellik kartları) masaüstünde galerinin altına; telefonda sıra aynı.
  3. Alt bölümler masaüstüne açılır: koyu bölümler kenardan kenara gece bandı, Bir gece iki sütun, odalar yan yana, kaydırmalı şeritler ızgara.
- Uygulandı (19 Eki): çubuk `ayluna.js cubukKur` (satın alma butonu ekranın üstünden çıkınca iner); özellik kartları `ortak.urun_ust(..., oz)` + renderVals `masa/tel` bayrağı (yalnız sitede, `window.Ayluna` varken; tuval hep telefon); Bir gece masaüstünde `.g-liste` (kaydırma adımı yok); koyu bölümler gece bandı, diskler iki sütun, odalar yan yana, şeritler ızgara (`ayluna.css`). Başlıklardaki `<br>` masaüstünde gizli; `site_uret.parcala` önüne boşluk koyar.
- Shopify'a taşırken: aynı masaüstü kuralları bölüm CSS'ine `@media (min-width:1024px)` olarak girer; özellik kartlarının iki yeri Liquid'de iki kopya + CSS ile değil, tek kopya + masaüstünde grid alanıyla çözülmeli (bakılacak).
- İmza sayfalarının telefondaki koyu başlık bandı şeffaf denendi (A: sayfa zemininde, B: fotoğrafın üstünde; B afişin kendi logosu ve başlığıyla çakışıyor). Kullanıcı: "boşver kalsın" → koyu bant kalır, tekrar önerilmez.
- Bekleyen eleştirmen önerileri (seçilmedi, sırada): yatay slayt görseli (Flow), koleksiyonda LunaDream için "Seç", slayt noktaları tıklanır, ödeme sayfası iki sütun, % rozeti posterden fiyata, ana sayfaya Loox puanı.

## Galeriler Shopify'daki gibi + masaüstü (19 Ekim)
- Kullanıcı: "Benim şu anda kullandığım ürün görselleri tarzında yapmayı düşünüyorum, yazısı vesaire. Fotoğraf kısmını Shopify'daki ile aynı şekle getir. Bir de mağazanın masaüstü görünüşünü yapmak lazım."
- `araclar/canli_galeri.py`: canlı `/products.json` (`ogrenme/canli-urunler.json`) → `ogrenme/galeri-canli.json` (Shopify sırası, çıkarılanlar ve kontrol listesi kodda). `ortak.canli_galeri(handle)` tüm üreticilerde.
- LunaDream, USB, AyFeneri, Galaksi Night galerileri kare (`.hero.kare`, LunaDream `.sahne`); oda sahneleri galeriden çıktı (sayfanın diğer bölümlerinde duruyor). Basit sayfalar aynı listeyi kullanıyor. test.js her ürünün galeri sayısını ve kareliğini dener.
- Çıkarılan afişler (22): uydurma yorum kartları/kolajları, "2.400+ satış" rozeti, göz/uyku/cilt iddiaları, araçta kullanım, başka cihaz, LunaDream "Temalar" (unicorn, 2025), USB "12 farklı galaksi teması" (eski diskler) ve "Uyku öncesi" (yorum kartı).
- Sıradaki: masaüstü görünüm (önce ana sayfa + ürün sayfası yönü).

## Baskı satırları: aynı gün kargo + Dün satılan (18 Ekim, en güncel)
- Kullanıcı (LunaDream ekran görüntüleriyle): "şu kısım dönsün, ilk hali öyle başlasın; sonra bugün 16'ya kadar verilen siparişler aynı gün kargoda, orada bir sayaç dönsün. Stokta'yı kaldıralım, altına dün şu kadar kişi satın aldı yapalım. Diğer USB için de bu baskılayıcıları koyabiliriz."
- LunaDream (`luna_e.py`) ve Galaxy USB (`luna_usb.py`):
  - Fiyat satırında "Stokta" yok. Altında "Dün [X] kişi satın aldı" (sayı `DUN` sabiti; canlıda bölüm ayarı ya da Shopify Flow metafield'ı, boşsa satır gizli).
  - Dönen satır: hediye/disk satırı (4 sn) ↔ "Bugün 16.00’ya kadar verilen siparişler aynı gün kargoda" + 16.00 sayacı (6 sn). Giren alttan, çıkan yukarı; ikisi aynı ızgara hücresinde, yükseklik değişmez. Hareket azaltılmışsa ikisi alt alta.
  - Saat mantığı ortak: `ortak.py` → `KARGO_JS` (İstanbul saati; Pzt–Cum 16.00 öncesi bugün, sonrası "yarın" ya da gün adı, sayaçsız).
  - Teslim çizgisinde kargo tarihi aynı kurala göre ("Bugün"); SSS ve Kargo politikası 16.00 kuralıyla güncellendi.
  - Test: `test.js` sabit saatle (Pazartesi 12:47:15) dönüşü, sayacı, 16.00 sonrasını ve yoldaki "Bugün"ü dener.
- Hızlı Kargo (kullanıcı: "öncelikli kargo oluyor işte"): "Siparişin sıranın önüne alınır, öncelikli hazırlanıp kargolanır." Sepet, kapıda formu (`ayluna.js`), ödeme, teşekkür, kargo politikası, takip sayfası ve `shopify/ayluna-sss.txt` güncellendi; sepette standart kargo da 16.00 kuralıyla ("Bugün kargoda"). Canlı mağazadaki Hızlı Kargo ürün açıklaması kullanıcı tarafından değiştirilmeli.
- Açık: Cumartesi kargo var mı teyit. Çıkan satırın geçişte üstte kısa süre silik kalması (çıkışı hızlandırma) kullanıcı durdurduğu için yapılmadı.
- Kullanıcı: "Dün kişi satın aldı kısmına 62 yaz, oraya da hafif bir animasyon, tasarım diline uygun." → LunaDream `DUN = '62'`; satır fiyat düşüşü bitince (1,9 sn) 6px aşağıdan gelir, sayı fiyattaki gibi yukarıdan düşer, yeşil nokta 3 kez yumuşak halka verir. USB'de aynı giriş (rozet "pop" diliyle), sayı hâlâ [X].
- Kullanıcı: "Stok kısmı için de uygun bir tasarım deneyebilir miyiz, UI." → `stok_secenek.py` → `canvas/LunaDreamE-Stok.dc.html` (tuvalde Güncel sayfası, LunaDream E sütunu): A Yıldız dizisi, B Serif sayı, C Buton kurdelesi. Eleştirmen: C 8/10, B 5/10, A 4/10. Kullanıcı C'yi seçti → `luna_e.py`: butonun üst kenarında "Son 18 adet" kurdelesi (`STOK`), azalan ay, dokunmayı engellemez, buton ekrana girince bir kez; eski stok satırı (`.canli`) kalktı. USB'ye de geldi (kullanıcı: "evet ona da gelsin"): lacivert dönen satır, Dün 62, "Son [N] adet" kurdelesi (ay gümüşü, lacivert butonda); USB stok sayısı 23 (kullanıcı).
- Kullanıcı (19 Eki): seçim kartlarında Kız/Erkek ve USB görsellerinin arkasında siyahlık → `site_uret.py` saydam kesimleri JPEG'e çeviriyordu; artık `gorsel()` saydam olanı WebP (saydam), diğerini JPEG yazar (15 görsel). Tüm site görselleri tarandı; kalan siyah zeminliler (diskler, gece fotoğrafı, Sunset afişleri) zaten öyle. Zip: scratchpad `ayluna-site.zip` (site + tek-dosya/index.html).
- Kullanıcı (19 Eki): "USB'nin diskleri böyle" (iki görsel) → 12 disk = 6 renkli + 6 beyaz; `luna_usb.py` DISK yeni, görseller `canvas/usb/k-*.webp` (kullanıcının görsellerinden kırpıldı; renkli altısı ~50 px kaynaktan, yumuşatıldı; asıl görsel istenecek). Oda kartları 3'e indi (Çocuk/Uzay balinası, Kendime/Satürn, Dolunay); Genç ve İkimiz kartları için Flow istemi `ogrenme/flow-istemleri-usb-oda.md`. Not: Satürn oda fotoğrafında gezegen renkli, disk beyaz; kullanıcıya soruldu.
- Kullanıcı: "kalitesini arttırmamışsın" → canlı mağazada disklerin büyük aslı yok (ürün JSON'unda yalnız 5 afiş); iki kaynak görsel yerelde Real-ESRGAN x4plus ile 4x büyütülüp diskler yeniden kırpıldı (`araclar/gorsel/sr.py`).
- Kullanıcı: dönen satır "lacivert rengimize çevirsek daha bütün görünür" → `.donen` lacivert zemin, ay beyazı yazı, sayaç çipi yarı saydam beyaz.
- Tuval ve "Ayluna Mağazası" artifact'ı (DgGy66eo4iqLEhjSn1inje) güncellendi. Yanlışlıkla oluşan görselsiz ikinci site artifact'ı kullanıcının isteğiyle silindi. Site yayını her zaman `url` ile asıl adrese yapılır (url'siz yayın yeni adres açar).

## Çalışan site iskeleti (18 Ekim, en güncel)
- Kullanıcı: "Tüm iskeleti index olarak gönder; önce eksiklerini kontrol et, tüm eksik kısımları düzelt; sepet vesaire her kısım tam çalışsın; Shopify için düzenlerken de aynı şekilde."
- **Önizleme:** claude.ai artifact "Ayluna Mağazası" (https://claude.ai/artifact/DgGy66eo4iqLEhjSn1inje), zip olarak da verildi. Üretim: `python3 araclar/site/site_uret.py` → `site/` (git dışı; yayın parçası `site-yayin/index.html`). Test: `araclar/site/test.js` (http.server 8765).
- **Nasıl:** tuval sayfaları (.dc.html) değişmeden kullanılır; `araclar/site/ayluna.js` onları çalıştırır (şablon + DOM yaması) ve siteyi bağlar: yönlendirme, menü, arama, sepet deposu (localStorage), sepet çekmecesi (sepet.html iframe; açılmazsa sepet sayfası), kapıda ödeme formu (EasySell kurgusu), ödeme önizlemesi, sipariş alındı. Ürün verisi `veri.js` (fiyat, paket, seçenek, görsel).
- **Yeni sayfalar** (`sayfalar2.py`, tuvalde "Site: eksik sayfalar"): Ödeme, Sipariş alındı, Arama, 404, Hesap, 5 politika (kargo, KVKK, mesafeli satış, ön bilgilendirme, hizmet şartları; taslak). `sepet.py` gerçek sepetten okur, boş hâl içinde.
- Denetim raporu ve Shopify test listesi: `ogrenme/site-denetimi.md` (20 eksik, hepsi düzeltildi).
- **Tek dosya:** `site-tek/index.html` (≈11 MB; bütün sayfalar, görseller 800px data URI, kod içinde; adres `#sayfa`; sunucusuz ve dosyadan açılır). Test: `araclar/site/test-tek.js`. Kullanıcı bu dosyaya bakıp eksik listesi çıkaracak.
- Kullanıcı: köşeli yer tutucuları kendisi dolduracak, sitede kalsın; teyit için sorulmaz.
- **Sırada:** kullanıcının eksik listesi, sonra Shopify teması (aynı test listesiyle); Flow görselleri.

## AyFeneri ve Galaksi Night · imza sayfaları (18 Ekim, en güncel)
- Kullanıcı: "AyLuna AyFeneri ve Galaksi Night Projector için özel sayfa tasarla"; Galaksi Night için referans pococo.com/products/galaxy-projector-star-projector-silver.
- Yön panoları `ozel_yon.py` (arşivde): AyFeneri A Liman feneri / B Kıyı masalı; Galaksi A Planetaryum / B Gözlemevi (Pococo öğeleri). Eleştirmen raporu kullanıcı seçtikten sonra geldi (AyFeneri B 7, A 5; Galaksi A 7, B 5).
- **Seçim: ikisinde de Yön A.** AyFeneri'nde çıkarılabilir taban kutusu çıktı. "Oda karanlık / Duvarda ay" düzeldi: sahne tam görünür (fener + ay), yazı ve anahtar alt şeritte; kapalıyken ay örtülü, açınca ışık fenerden yayılır (2 sn kapalı → 7 sn açık, dokununca durur).
- Tam sayfalar `ozel_sayfa.py` → `canvas/AyFeneri.dc.html`, `canvas/GalaksiNight.dc.html` (tuvalde "AyFeneri + Galaksi Night" sayfası). Yeni: yazısı görselin içinde oda sahneleri (AyFeneri: yatak odası, uyku, müzik, raf; Galaksi: salon, yatak, çocuk, genç), "Kutusu hazır" ve "Avucuna sığar" büyük kartları, Loox satırı ve alıcı fotoğrafları (iki üründe), Galaksi'de 3 adımlı kurulum.
- Görseller `canvas/ozel/` (kaynak notu `KAYNAK.md`). 10 görsel (yazısı silinmiş afişler + 3 oda sahnesi) Higgsfield'da üretildi; kullanıcı ardından "görseller Flow'dan, Higgsfield'da kredi harcama" dedi, bu görseller "şimdilik kullan" kararıyla **geçici**. Flow istemleri `ogrenme/flow-istemleri-ayfeneri-galaksi.md`; kullanıcı Flow'da üretip yükleyecek, aynı adla değiştirilecek.
- Teyit bekleyen: AyFeneri pil (canlı sayfa "2400 mAh şarjlı" diyor), sensör, 24,2 / 7,2 cm, USB kablo; Galaksi disk sayısı (12 mi, Ay ile 13 mü), 15 × 9 cm, USB adaptör, garanti.
- Ana sayfa AyFeneri slaytındaki teyitsiz "sensörlü, şarjlı" çıkarıldı.

## NİHAİ TASARIM: LunaDream E (18 Ekim)
- Kullanıcı: "Tamam, nihai tasarımımız bu olacak." Seçilen tasarım artık `canvas/LunaDreamE.dc.html` (üretici `araclar/tuval-uret/luna_e.py`). `Main.dc.html` eskidi.
  - `CLAUDE.md` ("Seçilen tasarım `canvas/Main.dc.html`") ve eleştirmen ajanı (`.claude/agents/ayluna-elestirmen.md`) hâlâ Main.dc'yi gösteriyor; güncellenmeli (kullanıcı onayıyla).
- Shopify bölümleri ve diğer ürün sayfaları bu dile göre yazılır.

## Site geneli: sepet, ana sayfa, kalan sayfalar (18 Ekim, en güncel)
- Envanterler: `ogrenme/site-envanter.md` (site geneli, sepet/EasySell, politikalar, 34 sorun) ve `ogrenme/urun-envanter.md` (13 ürün, sorunlu iddialar).
- Sepet: `canvas/Sepet.dc.html` (`sepet.py`). Ek teklifler EasySell COD formunun "bump"ları (Astronot ₺749 → ürün nemlendirici; Kum Saati ₺699,99; Yıldız Işığı ₺749,99; Hızlı Kargo ₺79,99). Shopify'da sepette çalışması için ayrıca kurulum + otomatik indirim gerekir.
- Ana sayfa: `canvas/Ayluna-Anasayfa.dc.html` (`anasayfa.py`; arşivdeki eski `Anasayfa.dc.html` korunur). Kullanıcı eleştirmenin 3 satış önerisini istemedi.
- Kalan sayfalar: `sayfalar.py` → Koleksiyon, Iletisim, KargoTakip, Politika-Iade, Sayfalar-Kucuk (tuvalde x 5170–7050).
- **13 ürünün sade sayfaları:** `urun_sade.py` → `canvas/U-<handle>.dc.html`, tuvalde yeni "Ürünler" sayfası. İçerik `ogrenme/urun-icerik.json` (dürüst; yer tutucular [teyit]); görseller `canvas/urunler/<handle>/` (67 görsel; 23 uydurma yorum kartı ya da sağlık iddialı afiş alınmadı), blob eşlemesi `canvas/urunler/bloblar.json`, yükseklikler `yukseklik.json`. Ürün adları mağazadaki gibi; içerik dosyasındaki ad önerileri (Kum Sanatı Lambası, Zürafalı Projeksiyonlu Çizim Masası, Alev Efektli Aroma Nemlendirici, Retro Pikap Hoparlör) kullanıcıya soruldu.
- Sırada: kullanıcının kararları (ad önerileri, teyitler), sonra Shopify bölüm kodları.
- Kullanıcıya bildirilen site sorunları: yasal bilgi yok (Londra YVZNL LTD), politikalarda yer tutucular, 4 farklı iade süresi, sabit "4.7 (2467)", Astronot/Dokunmatik sayfaları başka ürünü anlatıyor, sağlık iddiaları, /collections/all'da COD "Tükendi" hatası, Loox'ta aynı gün yazılmış etiketsiz yorumlar.

## Galaxy USB · Yön A sakin düzen + animasyonlar (18 Ekim, en güncel)
- Kullanıcı: Yön A'nın sakin düzeni + yaptığım animasyonlar; eleştirmenden 3 öneriyi seçti (%5 butonda, baskı tek satır, oda çipleri); diskleri yeniden üret; fontlar ve renkler beğenilmedi.
- `luna_usb.py` baştan yazıldı: `TEMA` sözlüğü (lacivert sabit; ikinci renk, zemin, yazı tipi), `sayfa(tema, kesit)`. Ana pano `GalaxyUSB.dc.html` (h 6480, şimdilik `buz`; `U_TEMA=<ad> python3 luna_usb.py`). Renk seçenek panoları `GalaxyUSB-Renk-kuzey/pembe/mercan/gumus.dc.html` (h 2600, x 4230–5640). Yön B ve C arşive taşındı.
- Düzen: şerit (tek sayaç) → başlık bandı + tam ekran fotoğraf (oda, ürün, başlık), başlık ve küçük resimler görselin içinde → ad, fiyat → birleşik özellik kutusu → paket → "Her kutuda 12 film diski" → stok satırı → iki satırlı kart butonu → kapıda → kargo döngüsü → İçin rahat olsun (birleşik kutu, kartla öde) → 12 disk → Herkesin odasına (çipler görselin içinde) → Nereye takılır → kurulum → yorumlar → 30 gün → SSS (8) → diğer ürünler → alt bilgi → yapışkan çubuk (sayaçsız).
- Diskler Higgsfield ile büyütüldü (2 kredi; şerit iki kez reddedildi, 4×3 ızgara geçti). Yeni blob'lar `luna_usb.py` DISK ve `araclar/blob-yerel.json`'da.
- Yerel önizlemeye Outfit, DM Sans, Sora, Manrope, Plus Jakarta Sans, Fraunces eklendi.
- **Galeriler (iki sayfa):** küçük resimler kalktı; kaydırılır + 5 sn'de geçer (elle kaydırınca durur). LunaDream E: altta 9 ay, geçtikçe evreler dolar (`luna_e.py` `.ay-iz`, `gKay`, `galGit`). USB: altta film diskleri (`.d-iz`), galeriye `a-esnek.jpg` afişi eklendi (blob be86b4a9…). Gerçek çalışma zamanında DOM yeniden kurulursa `componentDidUpdate` kaydırmayı durumdaki fotoğrafa geri alır. Test: `scratchpad/araclar/galeri-testi.js` (otomatik scrollTo, elle kaydırma, durma).
- **Son tur:** kullanıcı Yön A'nın "Bu gece tavanda ne olsun?" bölümünü ve yazı tipini istedi → tema `gumus-a` (Ay gümüşü + Bricolage/Figtree, ana pano varsayılanı), sahne kartları satın almanın altında (Ay, Satürn, Denizanası, Kuzey ışığı). Ana pano h 7120. Not: sahne ve hikâye kartı aynı yaşam fotoğraflarını kullanıyor (Satürn, Denizanası, çift); ayrı görsel gerekirse Higgsfield ile disk desenli yeni sahne üretilebilir.
- **Renk: kullanıcı Ay gümüşü'nü seçti** (eleştirmen sırası: Kuzey ışığı 8, Pembe 7, Mercan 6, Gümüş 4). Ana pano artık `gumus` (varsayılan `U_TEMA`). Renk panoları arşivde (x 4700–6110).
- Açık sorular: puan (gerçek 2,0 mı, puansız mı), ₺1.999 için son 10 günün fiyat kaydı, stok [N], teslim süresinin teyidi, disk değiştirme adımları, ışık modları, kırık/eksik süreci, çift fotoğrafındaki balina (diskte yok).

## Galaxy USB · Yön A geliştirilmiş: güncel sayfa (18 Ekim)
- Kullanıcı A'yı seçti: sarı yok, koyu lacivert marka rengi her üründe, ürün beyaz, daha çok animasyon, Herkesin odası daha iyi UI, güven ve baskı bölümleri. Sonra: "USB adaptör yok; içindeki diskler bunlar ve 12 diskli" (afiş).
- Pano: `canvas/GalaxyUSB.dc.html` (`araclar/tuval-uret/luna_usb.py`; yalnız `luna_usb_yon` ve `luna_e.isaret` alır, E'nin CSS'i yok). Tuvalde x=3290, h 6890, `expand: fill`. Eski E kopyası taslağın yerine geçti.
- Dil: lacivert #1A2142 + buz mavisi #8FD3FF, zemin #F2F4F8, koyu bölümler #0C1027; Bricolage Grotesque + Figtree; kelime işareti Young Serif.
- Akış: sayaç şeridi (saniye tıklar) → sinema galeri (beyaz ürün önce, 5 sn'de geçer, yavaş yakınlaşma, küçük resimde dolan çizgi) → ad + "2'si 1 arada" + fiyat → 5 canlı özellik (fiş, 12 disk, esnek boyun, gece lambası, cetvel) → baskı kartı ([N] stok, dün [X], gün sonu sayacı) → paket (2 Adet seçili; "2 ayrı almaya göre ₺798,01 daha az", "tanesi ₺1.199,99", üstü çizili yok) → 12/24 disk notu → iki buton → kargo döngüsü → İçin rahat olsun (4 kart + kart logoları) → Kutuda 12 film diski (seçilen disk tavana düşer, 3 sn'de gezer) → Herkesin odasına (hikâye kartı) → Nereye takılır (adaptör kutuda yok) → Üç adımda tavanda → Yorumlar (Loox yer tutucu) → 30 gün (30 çentik) → SSS (9) → diğer ürünler → alt bilgi → yapışkan çubuk.
- Diskler: `canvas/usb/d01-d12.webp` (afişten kırpıldı; adlar desen tarifi), blob eşlemesi `araclar/blob-yerel.json`.
- Eleştirmen (6,5/10): en iyi Diskler 9, hikâye kartı 8, galeri 8; en zayıf yorum yer tutucusu 3, aciliyet kartı 4, güven 5. Uygulanan kural düzeltmeleri: koyu bölümler #141A36 (siyaha kaymasın), AMEX yok, "USB-A girişli şarj başlığı", nabız 3 kez, geçişler yalnız transform, "Her kutuda 12 film diski" (çıplak 24 yok), "Az yer kaplar", galeride "Temsilî görseller" ve çift fotoğrafı yalnız hikâyede, "Masaldan sonra galaksi". "Ortalama 2 saatte yanıt" mağaza bilgisi, kaldı.
- Kullanıcıya soruldu: (1) %5 butonun içinde + güvendeki "Kapıda ödeme" kartı yerine "Kartla güvenli öde", (2) aciliyet kartı tek satıra (butonun üstünde stok, elle; çubuk/parlama/kart içi sayaç kalkar), (3) hikâye kartının altındaki 4 düğme küçük çiplere.
- Açık sorular: puan (gerçek 2,0 mı, puansız mı), ₺1.999 için son 10 günün fiyat kaydı, stok [N] ve dün [X] verisi, disk değiştirme adımları, ışık modları, kırık/eksik gelince süreç, yaşam fotoğraflarındaki desenlerin (kuzey ışığındaki balina, Satürn) disklerle örtüşmesi.

## Galaxy USB · kendine özgü dil, üç yön (18 Ekim)
- Kullanıcı: ürün yalnız çocuklara değil (çocuk, ebeveyn, genç); her sayfanın dili kendine özel; canlı sayfanın satan görsellerini ve düzenini göz önünde bulundur.
- Canlı sayfa telefonda incelendi (`scratchpad/usb/canli/`): kare afiş galerisi, "Premium Özellikler" 2×2, "Çok Al Az Öde" (1 Adet ₺1.599 / 2 Adet ₺2.399,99, "+10 Adet Ücretsiz Disk"), iki büyük buton, yetişkin yaşam fotoğrafları (çift, Satürn, kelebek, ay, denizanası, kara delik). Bu fotoğraflar tuvale yüklendi (`canvas/usb/s-*.jpg`).
- **Ürün rengi:** kullanıcı teyit etti, **beyaz**. Siyah paket fotoğrafları (`p-siyah*`) kullanılmaz.
- Üç yön: `canvas/GalaxyUSB-YonA/B/C.dc.html` (`luna_usb_yon.py`), tuvalde x=3760/4230/4700.
  - A Sinema: sıcak siyah + sinema sarısı, Bricolage Grotesque + Figtree; tam ekran yaşam fotoğrafı, kaydırmalı sahne kartları.
  - B Gökyüzü paneli: gece laciverti + buz mavisi, Unbounded + Onest; kare galeri, sahne seçici.
  - C Ferah: açık zemin + mercan, Archivo Expanded; büyük ölçü rakamları, "Kimin odası?" sekmeleri.
- Yerel önizlemeye yazı tipleri eklendi (`onizleme/f/`, `araclar/yerel-fontlar.json`; değişken yazı tipi desteği `dc-onizle.js`'te).

## Galaxy USB Projektör sayfası · ilk taslak, E kopyası (18 Ekim; yerini Yön A geliştirilmişe bıraktı)
- Kullanıcı: "Şimdi USB projektör için de ona uygun bir tasarım yapalım."
- Pano: `canvas/GalaxyUSB.dc.html` (`araclar/tuval-uret/luna_usb.py`; E'nin CSS'ini ve parçalarını `import luna_e` ile alır). Tuvalde x=3290, y=0.
- Görseller: mağazanın 5 afişinin (yapay zekâ, yazılı) yazısız bölgelerinden kesildi → `canvas/usb/`; ürün kesimi rembg ile. "Elif K." kartlı bölge alınmadı.
- Sayfadaki bilgi yalnız afişlerden: 12 tema diski, USB tak & çalıştır, 360° döner başlık, başlık 4 cm, boy 23,5 cm, temalar Galaksi/Gezegenler/Ay & Uzay/Nebula. Fiyat ₺1.599 / ₺1.999.
- Bölümler: sayaç şeridi, sahne galeri (4), ad + [puan], fiyat düşüşü, Sihirli (USB ışığı / tema yelpazesi / dönen başlık / cetvel), paket (1 Adet; 2 Adet fiyatı yer tutucu), Kutuda 12 tema (tavan önizlemesi), Üç adımda kur (+ WhatsApp yardım), Odası böyle görünecek (kaydırmalı), Yorumlar (Loox yer tutucusu), 30 gün, SSS, diğer ürünler.
- **Canlı sayfadaki sorunlar (kullanıcıya bildirildi):**
  - Puan çelişkisi: "4.7 (2467 Onaylı Kullanıcı Yorumu)" ↔ aynı sayfadaki gerçek yorum kutusu "2.0 / 5, 7 yorum".
  - Gerçek şikâyetler: kırık geldi, görüntü bulanık, odak halkası zor dönüyor, disk sıkıştı, disk eksik, 3 günde ışık zayıfladı, açma tuşu çalışmıyor.
  - "90 Gün Para İade" (gerçeği 30), sağlık iddiaları (kortizol, anksiyete, uyku kalitesi), "5K", "6 lens" ↔ "7 katmanlı lens", "130 m²", SSS'de başka ürünün Bluetooth/şarj cümleleri, afişte "Elif K. doğrulanmış alıcı" kartı.
- Bekleyen: puan kararı (gerçek 2,0 mı, puansız mı), 2'li fiyat, disk değiştirme adımları, stok sayısı, gerçek tavan fotoğrafı.

## Tur 26 · Odası böyle görünecek (18 Ekim)
- Kullanıcı: "Kutudan ne çıkıyor'u kaldıralım; 2 odanın nasıl göründüğünü gösteren görsel yapalım, metin içeren görsel kısmı gibi ama daha iyi dursun."
- Üç seçenek panosu: `canvas/LunaDreamE-Oda.dc.html` (`luna_e_oda.py`), tuvalde x=2820, y=700. A Poster, B Kaydırmalı, C Görsel + binen levha.
  - İlk denemede başlık lambanın üstüne biniyordu; yazı fotoğrafın altına, lacivert banda alındı (ürünün üstüne yazı gelmez).
- **Karar: kullanıcı B'yi seçti; E'ye işlendi** (tuval Sürüm 74, E h 6130):
  - Diskler'den sonra, 30 gün iadeden önce: "Odası böyle görünecek." İki oda posteri yan yana kayar (300px kart, ikincisi kenardan görünür), altında iki nokta.
  - Kart: üstte gece oda fotoğrafı ve model çipi (ay evresiyle), altında lacivert bantta Young Serif başlık ("Tavanda ay ve yıldızlar." / "Odası bir uzay gemisi."), tek cümle ve "… modelini seç" (modeli seçer, model kartlarına kayar).
  - Altında tek satır: "Görseller temsilîdir; tavandaki desen seçtiğin diske göre değişir."
  - "Kutudan ne çıkıyor?" bölümü kalktı; içerik SSS'nin ilk sorusu oldu (1 lamba, 6 masal diski, 6 hediye disk, USB şarj kablosu; iki modelde de aynı).
  - Fotoğraflar Bir gece'nin 20:00 anında da var (aynı oda fotoğrafları).
- **Eleştirmen düzeltmeleri (Sürüm 75, E h 6110):** kart başlığı 20px (bölüm başlığından büyük olmaz), düğme 48px; teyitsiz cümleler değişti: "Tavanda ay ve yıldızlar." → "Tavanda masal."; "Odası bir uzay gemisi. Robot lamba yanınca duvara ve tavana yıldızlar düşer." → "Tavanda uzay. Uzay diskini tak, tavan uzaya dönsün." (desen seçilen diske göre değişir, iki model aynı diskleri kullanır). SSS: "2 Adet'te iki kutu gelir."
- **Kullanıcıya sorulan, bekleyen:**
  - Oda fotoğrafı sayfada üç kez (galeri ilk kare, Bir gece 20:00, oda kartı). Tavanı da gösteren 2 yeni geniş oda görseli gerekli (kullanıcının görseli ya da onayıyla üretim; ürün yeniden çizilmez).
  - Bölüm başlığı "Odası böyle görünecek." + "temsilîdir" notu birbirini zayıflatıyor; eleştirmenin önerisi "Hangisi onun?".
  - "Kutudan ne çıkıyor" ile kaybolan el fotoğrafı (tek boyut ipucu) galeriye taşınsın mı?
  - Adaptör kutuda var mı: [teyit].

## Tur 25 · Kargo döngüsü, kapıda butonu, güven satırı, seçici seçenekleri (18 Ekim)
- Kullanıcı (E'ye bakarak):
  - "Animasyon çalışmıyor" (kargo takibi)
  - "Kapıda Ödeme ile Sipariş Ver'de fiyat yazmasın"
  - fiyatın altındaki "Ücretsiz kargo · 30 gün iade · Güvenli ödeme" satırı "çok kötü duruyor", kalksın
  - "Hâlâ seçiciler çok kötü; bundle ve aralarında bir uyum yok; lamba seçim kısmı da güzel değil"
- E'de yapılanlar (tuval Sürüm 68, h 5864):
  - **Kargo takibi:** tek seferlik oynatma, tuvalde pano açılır açılmaz bakan olmadan bitiyordu. Artık 8 sn'lik sakin döngü: "Bugün" hilali hep dolu; çizgi ve paket noktası Kargoda'ya akar, yarım ay; Kapında'ya akar, dolunay ve ışık halkası; bekler, söner, baştan. Ekrana girene kadar ilk karede durur. Yazılar hep okunur. Paket noktası yüzdeyle gider (ekran genişliğinden bağımsız).
  - **Kapıda butonu:** yalnız "Kapıda Ödeme ile Sipariş Ver". ₺80 ücret ve toplam kapıda ödeme formunun özetinde ve SSS'de yazar (mevzuat: ek ücret sipariş onayından önce bildirilir; formda görünmesi yeter).
  - **Güven satırı** fiyatın altından kalktı (CSS'i de).
- **Seçici seçenekleri** ayrı panoda: `canvas/LunaDreamE-Secici.dc.html` (`luna_e_secici.py`), tuvalde x=2350, y=700. Dört seçenek yapıldı; eleştirmen üçünü seçti, Vitrin'i (segment, 4/10) reddetti. Ortak dil: 2px lacivert çerçeve + amber dolunay noktası, dolu lacivert yok; renk anlık değişir, yalnız nokta hareket eder; hediye "her kutuda +6".
  1. Satır kartlar (7/10): model yan yana iki yarım kart; paket alt alta satır (2 Adet'te "₺649,99 kazanç", "tanesi"); 2 Adet açılınca kartın içinde 2. lamba çipleri; altta tek hediye şeridi.
  2. Yuvarlak örnek (7/10): model iki büyük yuvarlak örnek; paket görselsiz satır; 2. lamba aynı örneğin küçüğü.
  3. Önce paket, sonra model (6/10): paket satırları üstte; model kareleri adede göre (2 Kız / Kız + Erkek / 2 Erkek), ayrı lamba seçimi yok. Sırayı değiştirir (17 Eki: model paketin üstünde). Varsayılan 2 Kız.
- Eleştirmen ₺80'in kapıda butonunda kalmasını istedi; kullanıcının açık isteği öncelikli, uygulanmadı.
- **Karar: kullanıcı 1 · Satır kartlar'ı seçti; E'ye işlendi** (tuval Sürüm 69, E h 5624):
  - Etiket 2 Adet'te "1. lamba", 1 Adet'te "Model". Model yan yana iki yarım kart (kesim görsel, Kız/Tavşanlı, Erkek/Robot, dolunay noktası).
  - Paket alt alta satır kart: görsel, ad, alt satır (1 Adet "%15 indirim", 2 Adet "₺649,99 kazanç"), fiyat, eski fiyat ya da "tanesi", dolunay noktası; 2 Adet'te lacivert "En avantajlı" kurdelesi.
  - 2 Adet seçilince kartın içinde "2. lamba" çipleri (Kız/Erkek, kesim görsel + nokta). 2. lamba açıkça seçilmediyse modeli izler.
  - Altta tek hediye şeridi: "Her kutuda +6 hediye masal diski".
  - Kemerli gece penceresi, dolu lacivert paket ve hap segment kalktı (CSS'leri de, kullanılmayan .mkart ile birlikte).
- **Bir gece boşluğu** (kullanıcı: "Bir gece 5 anın altı neden o kadar çok boş"; tuval Sürüm 70, E h 5700):
  - Sebep: ortak başlıktaki `.pg{overflow:hidden}` sayfayı kaydırma kabı yapıyordu; yapışkan panel telefonda yukarı kayıp gidiyor, altında ~1.900px boş kaydırma adımı kalıyordu. Yapışkan satın al çubuğu da aynı sebeple çalışmıyordu.
  - Düzeltme: E'de `.pg{overflow:clip}`; clip'i tanımayan tarayıcıda kaydırma adımları kapanır (yay ve oklarla gezilir).
  - Panel telefonda üst kenar ile satın al çubuğu arasında ortalanmış kart olarak yapışır (844px ekranda 54px eşit krem pay). Kaydırdıkça an değişir, ay dolar.
  - Pano yüksekliği yazı tipleri yüklendikten sonra ölçülür (önceki 5624 eksikti, alt 71px kesiliyordu).
- **"Kaydırdıkça değişmiyor"** (tuval Sürüm 71): tuvalde pano kendi kaymaz, tuval kayar; sayfa kaydırmasını dinleyen kod hiç tetiklenmiyordu.
  - Telefon ve Oynat: sayfa kaydırması (scroll + requestAnimationFrame); ekranın ortasını geçen son adım anı seçer. Eski IntersectionObserver'ın rootMargin'i başka kökenli çerçevede yok sayılır, o yüzden bırakıldı.
  - Tuval: panelin 2000px üstünden altına 25px arayla görünmez noktalar (`.gece-iz`); ekranda görünenler ekranın kenarlarını verir, ekranın ortası panelden geçerken an 0 → 4. Kullanıcı yay ya da okla seçerse, kaydırma başka bir ana geçene kadar seçimine dokunmaz.
  - Pano `expand: "fill"`: Oynat'ta küçültülüp sığdırılmaz, telefon sayfası gibi kayar (390px sütun ortada).
  - Sınama: `araclar/kaydirma-testi.js` (telefon + başka kökenli çerçevede tuval, x1 ve x0,6).
- **Puan ürün adının yanında** (kullanıcı: "yorum kısmı ürün ismi yanında olsun, yıldız sayısı ve ortalaması tasarıma uygun"; tuval Sürüm 72, E h 5670): solda "LunaDream.", sağda iki satır, sağa yaslı: amber yıldızlar + "4,7" (kalın), altında "62 yorum" (soluk, ince alt çizgi); dokununca yorumlara iner. Adın üstündeki puan/Stokta satırı kalktı; "Stokta" fiyat satırının sağ ucuna geçti.

## Tur 24 · Fiyat düşüşü, gece penceresi, dolan ay, kargo animasyonu, yeni bölümler (18 Ekim)
- Kullanıcı:
  - fiyat önce 1999 olsun, indirimliye düşsün
  - model seçimi estetik olsun
  - Bir gece UI olsun, ay kaydırdıkça dolsun
  - kargo takibi "verildi"den başlayan animasyonla çalışsın
  - buton altı yazılar silinsin
  - satış için yeni bölümler, influencer için bir kısım düşünülsün
- E'de yapılanlar (tuval Sürüm 67, h 5893):
  - **Fiyat:** 1,6 sn, bir kez oynar. ₺1.999,00 görünür, çizilir, sağa kayıp küçülür; ₺1.699,99 yukarıdan düşer; "%15 indirim" belirir. Azaltılmış harekette doğrudan son hâl.
  - **Model:** gece penceresi. Kemerli pencerede lamba kesimi; seçilene gece iner, yıldızlar çıkar, lamba yanar; adın önünde dolunay noktası.
  - **Bir gece:** yaydaki noktalar ay evresi (hilal → dolunay). Büyük ay her anda biraz daha dolar; telefonda kaydırdıkça dolar.
  - **Kargo takibi:** "Sipariş verildi" hilali dolar, amber çizgi ve paket noktası Kargoda'ya akar, yarım ay, sonra Kapında dolunayı ve tek seferlik ışık halkası. Toplam ~3 sn, ekrana girince bir kez (IntersectionObserver).
  - **Buton altı yazılar silindi.** Kapıda butonu iki satır: "Kapıda Ödeme ile Sipariş Ver" ve "₺2.829,99 · ₺80 kapıda ödeme ücreti dahil". ₺80'in baştan yazılması mevzuat gereği.
- **Yeni bölüm önerileri** ayrı panoda: `canvas/LunaDreamE-Bolumler.dc.html` (`luna_e_bolumler.py`), tuvalde x=1880, y=700. Kullanıcı seçecek.
  1. Annelerin gözünden (influencer): dikey video kartları, hesap çipi, kısa söz. Hesap ve söz yer tutucu. Yorumların üstüne.
  2. Kapıda öde, için rahat olsun: koyu panel; ay evresiyle 3 adım (sipariş ver → WhatsApp'tan onayla → kapıda öde); güven satırı; "Kartla ödersen ₺217,50 daha az". Butonların altına.
  3. Sıradan bir gece lambası değil: karşılaştırma, yalnız teyitli özellikler. Sihirli'nin altına ya da Diskler'in üstüne.

## Tur 23 · E: eleştirmenin 3 fikri (18 Ekim)
- Kullanıcı üç fikri de seçti. Hepsi uygulandı; tuval Sürüm 66, E h 5804.
- **1 · Amber tek vurgu:**
  - Üst sayaç şeridi koyu (#0C1027); sahneyle tek parça. Rakamlar amber kaldı.
  - "En avantajlı" kurdelesi krem, lacivert yazı. Seçili paket fiyatı beyaz, hediye şeridi krem yazı.
  - İkinci turuncu (#E59A4C) kalktı; tek amber #F2A65A.
  - Mühürdeki "30" lacivert. Stok noktası kehribar.
  - Koyu zeminde butonun basma gölgesi lacivert (kahverengi şerit yok).
- **2 · Ay evresi marka işareti:**
  - Logo: ince daire içinde amber hilal (evre çizimiyle aynı). Başta ve alt bilgide aynı kilit, işaret solda.
  - Sayacın yanında gün ilerledikçe sönen ay (kalan süre / 24 saat, İstanbul). Üst şeritte ve yapışkan çubukta var.
  - Seçili model kartı: dolu lacivert yerine 2px çerçeve ve dolunay noktası. Lamba seçiminde de aynı (beyaz hap, çerçeve, amber nokta).
  - Dolu lacivert yalnız pakette kaldı.
  - Hediye şeritlerinde küçük hilal.
- **3 · Tek fotoğraf dili:**
  - Model, paket ve yapışkan çubukta küçük ürün görselleri hep arka planı temizlenmiş stüdyo kesimi; açık kartta ton karede, koyu kartta lacivert karede.
  - Kadranın 20:00'ı gece oda fotoğrafı (Kız ve Erkek ayrı); gündüz yalnız 07:30'da.
  - Disk deseni tavanda ışık gibi (screen karışımı, durağan).
  - **Bekleyen:** galerideki yazılı afişlerin yazısız sürümleri. Kullanıcının Shopify'daki yazısız ürün görselleri gerekiyor. Gece fotoğraflarını Flow ile yenilemek de kullanıcının tarayıcısını ya da HF_TOKEN'ı gerektiriyor.
- Ayrıca "62 yorumun hepsini oku" düğmesinin alt çizgisi kalktı.

## Tur 22 · E: renk uyumu ve ay evreleri (18 Ekim)
- Kullanıcı: "Yarım ay, tam ay olma efektini kullanmaya devam et. Hâlâ düzensizlikler, renklerin birbirine girdiği, büyük marka hissi vermeyen yerler var."
- **Renk:** 50 tondan ~12'ye indi.
  - Açık ve koyu tonlar tekleşti: #F1E8DA, #D6CAB6, #5C6078, koyuda #B9BED6.
  - Güven satırı lacivert ve amber noktalı.
  - Seçili paketin hediye şeridi koyu, yazısı amber.
  - Ürün rozetleri fiyat rozeti biçiminde.
  - SSS artısı ince halka.
  - Sihirli'deki ay halesi küçüldü.
  - Kadranın lamba ışığı ve sabahı kahverengiye dönmüyor: sabah lacivert açılır, küçük bir güneş belirir.
- **Ay evreleri:**
  - Teslim çizgisi hilal → yarım ay → dolunay; kaydırınca sırayla dolar.
  - 30 gün iade için 8 evreli mühür; yazısı "Beğenmezsen iade et".
- **Sıra:** Bir gece → Yorumlar → Diskler. Böylece açık ve koyu bölümler sırayla gelir (§5 ve beceri sırası).
- Tuval Sürüm 64: E h 5797.
- **Eleştirmen (7,5/10):**
  - En iyi parça teslim çizgisindeki ay evreleri (9).
  - Kusurlar düzeltildi (Sürüm 65, h 5803):
    - Mühürdeki "30" kehribar (2,06:1 → 5:1).
    - "%15 indirim" rozeti yüzey zeminde (4,35 → 5:1).
    - Lamba seçici ve yay saatleri 48px.
    - Ay halesi küçüldü.
    - Kadranın 07:30'u: gri-mor örtü ve ayın üstündeki güneş kalktı, alttan ince şafak geldi.
  - **Kullanıcıya sorulan 3 fikir:**
    1. Amber yalnız ışık ve eylem: üst şerit koyu; kurdele krem; seçili paket fiyatı beyaz; ikinci amber (#E59A4C) kalkar; her ekranda tek amber yüzey butondur.
    2. Ay evresi tek marka işareti: logo hilali evre çiziminden; baştaki ve alttaki logo aynı; sayacın yanında gün ilerledikçe sönen ay; model ve lamba seçiminde dolu lacivert yerine çerçeve ve dolunay noktası.
    3. Fotoğraf dili tek: küçük ürün görselleri aynı stüdyo setinden; kadranın gece anları gece ışığında (Flow); disk tavanda ışık gibi (screen karışımı); galerideki yazılı afişlerin yazısız sürümleri.

## Tur 21 · E, B+'nın diliyle yeniden (18 Ekim)
- Kullanıcı (E'ye bakarken): "Sipariş fişini kaldır, emoji benefiti düzelt, yazım hataları berbat, yazı fontu kötü; her şey çok yabancı duruyor, bir bütün ve uyum yakala."
- Teşhis: D ve Tur 20'deki E seçilen B+'dan ayrı bir dil kurmuştu.
  - Yazı: Literata + Atkinson. Atkinson'ın sıfırı çizgili; "3Ø", "₺1.999,ØØ" gibi okunuyor.
  - Başka bir renk paleti.
  - Sihirli yörünge düzenine çevrilmişti; kullanıcının seçtiği V1, 2×2 beyaz kartlardı.
- Yapılan: `luna_e.py` B+ üretecinden (`luna_bplus.py`) yeniden kuruldu; Tur 20 sürümü git geçmişinde.
  - B+'dan aynen gelenler: Young Serif + Onest, krem/lacivert/amber, Sihirli V1, canlı paket ve iki buton, teslim çizgisi, yorum duvarı, diskler, kutu, 30 gün, SSS, alt bilgi.
  - Sipariş fişi yok.
  - Tek yenilik: **Bir gece kadranı**, B+'nın koyu panelinde.
    - Yayda beş saat var; ay seçili saate yay boyunca gider.
    - Akşam lamba ışığı, gece yıldızlar, 07:30'da amber şafak.
    - Fotoğraf yuvarlak pencerede; saat Young Serif.
    - Gezinme: yaydaki saate ya da noktaya dokunma, yandaki oklar, telefonda kaydırma.
  - Yazım düzeltmeleri:
    - "Aileler ne diyor?" ve "Kutudan ne çıkıyor?" (nokta yerine soru işareti)
    - "Kutuda altı masal, altı da hediye."
    - "Güvenli Ödeme ile Al"
    - 2 Adet: "2 ayrı almaya göre ₺649,99 daha az" (mevzuat §7.2)
    - "tanesi ₺1.374,99"
    - "07 sa 01 dk kaldı"
  - Görseller tuvaldeki en yeni kimliklerle değişti: oda sahneleri, Bir gece, videolar, müşteri fotoğrafları, elde.
- Tuval Sürüm 63: E (x=1410, h 5755).

## Tur 20 · E "Işık": daha güzel arayüz (18 Ekim)
- Kullanıcı: "Daha güzel bir UI yapmanı istiyorum." (Önceki istek: Bir gece için "UI tasarım istiyorum".)
- Üreteç `araclar/tuval-uret/luna_e.py` → `canvas/LunaDreamE.dc.html`. D'nin kopyası; D'nin içeriği, bölüm sırası, rengi ve yazısı korunur, D dosyası değişmez.
- **Değişenler (bölüm = ürüne özgü arayüz parçası):**
  - Ad levhası fotoğrafın üstüne 24px biner, üst köşeler 28.
  - Sihirli: seçili modelin lambası kendi ışığında ortada. Dört özellik köşelerde, ince yörüngeye bağlı. Parça yeri iddia edilmez; çizgiler yörüngeye gider.
  - Model kartı dikey: lamba kesimi dairenin üstünden taşar, seçilince ışık ve işaret.
  - Buton notları ve teslim çizelgesi yerine **sipariş fişi**:
    - içerik: seçim, disk, kartla ve kapıda toplam, ay evreli teslim satırları ("Kapında (tahmini)")
    - görünüm: tırtıklı kâğıt; telefonda kaydırınca yarıktan basılır
  - Diskler: tavanda soluk yıldızlar; metin "Diske dokun, desenini gör." Gerçek tavan fotoğrafı gelince eski metne dönülür.
  - Kutu listesi ikonlu. Yorumlarda baş harfli açık daire. 30 gün ay evreli mühür.
  - **Bir gece kadranı:**
    - Yuvarlak fotoğraf penceresinin çevresindeki yayda 5 saat; ay seçili ana yay boyunca gider.
    - Gök durumları: 20:00 ışıklı duvar, 20:30 sıcak alacakaranlık, 20:45–21:00 gece, 07:30 sabah.
    - Gezinme: yaydaki nokta ya da saat yazısı, yanlardaki oklar, telefonda kaydırma (adım 48vh).
    - Telefonda kadran ekranı doldurur (`--gh`), tuvalde 468px.
  - Kapanışta "ya da kapıda öde" bağlantısı.
- **Denetim:**
  - Eleştirmen: güzellik D 6 → E 8, satış 7 → 7. En beğendiği üç parça: gece kadranı, sipariş fişi, Sihirli yörüngesi ile dikey model kartları.
  - Eleştirmen düzeltmeleri işlendi:
    - Alt başlık kaldırıldı (kullanıcı 17 Ekim'de silmişti; §10'a ders yazıldı).
    - Sihirli ve model kartı kısaldı.
    - Kadran kontrastı düzeltildi.
    - Fişte kart farkı gösterildi.
  - design-review düzeltmeleri işlendi:
    - Saat yazısı dokunulur.
    - Koyu durumda odak halkası Lamba.
    - Kadranın altındaki boşluk giderildi.
    - Ay yay boyunca gider.
    - Yapışkan çubuk yarı saydam kalmaz; zaman çizelgesi desteklemeyen tarayıcı için gözlemci yedeği eklendi.
    - Fiş tekrarı giderildi; geçersiz `dl` düzeltildi.
- **Kullanıcıya sorulacak:**
  - Sihirli, seçilmiş V1 2×2 düzeninden bilinçli olarak ayrıldı.
  - D ve E'nin yazısı (Literata + Atkinson) ve rengi Main'den farklı.
  - Teslim tarihi hesabı resmî tatilleri bilmiyor.
  - Yapışkan çubukta kapıda ödeme seçeneği yok.
- Tuval (Sürüm 62), Güncel sayfası: B+ (x=0), C2 (470), D (940), E (1410, h 6858), D-BirGece (1880).

## Sıradaki işler (17 Ekim, güncel)
1. Kullanıcı B+ tam sayfayı onaylasın; sonra sıfırdan tema (`ayluna-tema/`) ve LunaDream şablonu B+'dan.
2. **Sıfırdan Ayluna teması** (`ayluna-tema/`): layout, değişkenler, fontlar, üst menü, alt bilgi; sonra LunaDream ürün şablonu v2'den. Eski `shopify/*.txt` dosyaları iskelet.html'den geliyor ve artık kullanılmayacak.
2. Fiyat ve mevzuat soruları: son 10 günün fiyatı, Kasım zammı, iade metni (`TASARIM-BILGISI.md` §11).
3. Kullanıcıdan teyitler: ölçü, pil, yaş, teslim, varyant yapısı, kapıda ödeme seçicisi.
4. Shopify'a kurulum ve gerçek telefonda, Instagram içinden deneme.
5. Masaüstü düzeni: solda yapışkan galeri, sağda satın alma kutusu.
6. Gerçek müşteri videosu gelirse video karesi.

## Kullanıcının netleştirdiği yön (17 Ekim, sonra)
- İnsanların alıştığı kalıplar (emoji fayda listesi, indirim sayacı, "dün satılan", stok alarmı) atılmaz; iyileştirilir. Baskı unsurları istiyor; gerçek veriye bağlanır (stok: Shopify envanteri, dün satılan: Flow ile metafield, sayaç: her gece sıfırlanan bugünkü fiyat garantisi; Tur 10).
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

## Sepet: indirim, küçültme, beyaz, C2 baskı (28 Ekim)
- Sepette karşılaştırma fiyatından indirim görünür: satırda −%X + üstü çizili; özet Ürünler → İndirim → Kargo → Toplam.
- Sepet yazı ve parçaları küçüldü (başlık 20, satır 14, Toplam 22, düğme 15; dokunma alanları 48 px).
- Sepet zemini beyaz; site krem kalır.
- Baskı: C2 son hâl ("Ekim fiyatı X gün Y sa sonra bitiyor" + stok kurdelesi düğmeye yarı biner). B teslim çizelgesi kaldırıldı.
- Kullanıcıya verilen: `kodlar/nihai/ay-sepet.liquid` (snippets/ay-sepet.liquid tamamı) + ayluna.css/ayluna.js sonundaki baskı blokları.

## Yeni ürün: Yılbaşı Ağacı Projektör Lamba (28 Ekim)
- Handle: `yilbasi-agaci-projektor-lamba` (kullanıcı Shopify'da bu adresle açmalı). Fiyat geçici 999; canlıda Shopify'dan.
- Sade sayfa: `canvas/U-yilbasi-agaci-projektor-lamba.dc.html`; görseller `canvas/urunler/yilbasi-agaci-projektor-lamba/` (01 tavan, 02 kutu, 03–04 kurulum).
- Kullanıcıya verilen: `kodlar/yilbasi/` (+ `kodlar/yilbasi-dosyalar.zip`). Tema 1.0.38 zip'i de hazır (yalnız gerekirse).
- Simülatör: `BENZETIM_EK_URUN` ile mağazada olmayan ürün denenir.
- Yeni ürünü sonra eklemek için yol: urun-icerik.json + urun_soru.SORU + anasayfa.URUN (sona) + sayfalar.KAT + site_uret.ADLAR + bloblar (görsel) → urun_sade.py, site_uret, tema_uret.
- İmza sayfa yönleri (28 Eki): `onizleme/yilbasi-yon/` (A hediye kutusu 7/10, B tavan 5/10, C birlikte yap 6/10). Eleştirmen önerisi: Main sistemi + A'nın "Kutuda ne var?" + B'nin disk seçicisi (yalnız bir gece bandı) + C'nin "yaparken/yanınca" ikilisi. Kullanıcı seçimi bekleniyor; gerekenler: fiyat, 2'li paket fiyatı, gerçek tavan çekimi, disk/parça sayısı.
- İmza sayfa yapıldı (28 Eki): `araclar/tuval-uret/yilbasi_sayfa.py` → `canvas/YilbasiAgaci.dc.html`; temada `sections/ay-yilbasi.liquid` (+ product.json'a "yilbasi" bölümü). Görseller `canvas/ozel/yb-*`. Tema 1.0.38. Önizleme `onizleme/yilbasi-yon/imza-sayfa.jpg`.
- Bekleyen: gerçek fiyat ve karşılaştırma fiyatı (Shopify'a girilince canlıda otomatik), gerçek tavan çekimi (disk seçici + galeri), disk sayısı teyidi, 2 adet indirimi tanımlanırsa paket yazısı güncellenir.
- 2.–3. tur (28 Eki, kullanıcı: "çok sade ve sıkıcı"): çam yeşili + altın bantlar; Ağacı yak (ışık anı + "Kutudan çıkan" küçük kare), dergi kapağı Sar./Süsle./Tak./Yansıt., dönen tavan + disk seçici, görselli "Kime hediye?" kartları, takvim yaprağı (son sipariş 23 Aralık), yeşil satın alma kutusu ve yapışkan çubuk. Eleştirmen 2. tur 6,5; ilk ekran önerileri uygulandı. Önizleme `onizleme/yilbasi-yon/imza-sayfa-v3.jpg`.
