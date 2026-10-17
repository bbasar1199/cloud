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
