---
name: "ayluna-tasarim"
description: "Ayluna (ayluna.shop) Shopify sitesi, tema bölümleri, ürün sayfaları, ürün metinleri veya Ayluna görselleri/Instagram kiti üzerinde çalışırken kullan."
---

# Ayluna tasarım kuralları (v2 · 17 Ekim 2026)

Ayluna, Türkiye'de Meta reklamıyla telefondan gelen annelere ve büyükannelere gece lambası, projektör ve nemlendirici satıyor. 15 ürün var; cironun çoğu LunaDream'den geliyor.

**İşe başlamadan:**
1. Depo `bbasar1199/cloud`, dal `ayluna-imza-onizleme`.
2. Sırayla oku: `ayluna-imza/DEVAM.md`, `ayluna-imza/RAPOR.md`, `ayluna-imza/TASARIM-BILGISI.md`. Görünüş Main'den, kurallar TASARIM-BILGISI'nden alınır.

**Güncel ve seçilmiş tasarım:**
- "Ayluna İmza Tasarım" tuvalindeki `project/Main.dc.html` (https://claude.ai/artifact/CHmRtH4tjbapGmPtuQGsTH).
- Depodaki kopyası: `ayluna-imza/canvas/Main.dc.html`.
- Eski "H yönü / Bricolage + Figtree" bilgisi geçersiz.

## Çalışma biçimi
- Türkçe, kısa yaz. İstenmeyen dosya ya da açıklama yok.
- Tema kodu kopyala-yapıştır `.txt` dosyası olarak verilir. Zip, index ve rehber yalnız istenirse.
- Önce mobil (390px), sonra masaüstü.
- Beğenilen bölüm silinmez, geliştirilir.
- **Her bölüm kararı önce eleştirmen ajana denetletilir.** Ajan kullanıcıyı taklit eder. Depoda hazır tanımı var: `.claude/agents/ayluna-elestirmen.md`; kişilik `TASARIM-BILGISI.md` §1a'da. Ajanın en beğendiği 3 fikir kullanıcıya ayrı ayrı gösterilir.
- **Öğrenme döngüsü:** kullanıcı bir şeyi düzeltince aynı turda `TASARIM-BILGISI.md` → "Düzeltme günlüğü"ne yazılır. Kalıcıysa bu beceriye de işlenir. Aynı düzeltme ikinci kez gelmemeli.
- **Hafıza depodadır:** bulut konteyneri her oturumda silinir. Karar ve öğrenilenler commit'lenip dala gönderilir.
- Her değişiklikten sonra telefon genişliğinde ekran görüntüsü alıp bakılır (`araclar/ekran-goruntusu.js`, `araclar/dc-onizle.js`).
- Kararlar `DEVAM.md`'ye ve tuval notuna yazılır. Kullanıcı yorum bırakmıyor; iz yalnız orada kalır.

## Kullanıcının zevki
- **Sevmez:**
  - emoji ikon
  - çok yazılı, boğucu sayfa
  - "Shopify teması gibi" sıradan düzen
  - tamamen koyu tema
  - uydurma sayı ya da sayaç
  - abartılı efekt, yıldız animasyonu
  - süsle başlayan tasarım
- **Sever:**
  - "acayip ama sıkmayan" tarz
  - doğa gibi uyumlu hareket
  - güven veren, satan sayfa
  - paket
  - ay sonu fiyat sayacı (her ay zam yapıyor)
  - sosyal kanıt
- Alışılmış satış kalıpları (sayaç, stok, "dün satılan") gerçek veriye bağlanır.
- **Fayda:** durağan emoji ya da ikon listesi yok. Yerine animasyonlu "Sihirli Özellikler" geliyor.
  - 2×2 kart: ikon, başlık, tek cümle ve ürüne özgü küçük animasyon (nefes alan hale, yelpaze diskler, dolan pil, ses dalgası).
  - Yeri model seçiminden sonra.
  - Uydurma ya da teyitsiz madde yok ("+10.000 Mutlu Anne", "21 ışık modu").
- **Seçilen yön (17 Ekim): B+ Gece Postası.**
  - lacivert üst bant, tam genişlik galeri, büyük "LunaDream." başlığı
  - seçili kart lacivert, fiyatı amber
  - amber, basılınca çöken "Güvenli Ödeme İle Al"; çizgili "Kapıda Ödeme ile Sipariş Ver"
  - noktalı teslim çizgisi
  - Pano: `canvas/YonBPlus-GecePostasi.dc.html`.
- "Işığı kapat" anahtarı ve gece sahnesi kullanılmaz. Galeri ana ürün fotoğraflarından gelir.
- **Paket ve ödeme canlı sitedeki gibi kalır:**
  - alt alta "1 Adet / 2 Adet" kartları ve altlarında "+6 Tane Ücretsiz Hediye Disk" şeridi
  - "Güvenli Ödeme İle Al" ve "Kapıda Ödeme ile Sipariş Ver" diye iki ayrı buton
  - kapıda ödeme formunu uygulama açar; kapıda ödeme ücreti ₺80
- Kullanıcı sade şablon görünümünü "sıkıcı" buluyor; karakterli, akılda kalan bir görsel dil istiyor.
- Main seçildikten sonra sadeleşti (kimin istediği kayıtlı değil). Kompakt kal, ama sıradan Shopify'a düşme; "acayip ama sıkmayan" isteği geçerli.

## Tasarım sistemi (Main.dc)
- **Renkler:**
  - krem #F6F1E9 zemin, #FFFDF9 yüzey, #E3D8C7 çizgi
  - lacivert #1A2142 metin ve açık zeminde ana buton
  - gece #141A36 / #0C1027: yalnız ürünün ışığını gösteren bantlarda, yapışkan çubukta ve alt bilgide
  - amber #F2A65A: ışık ve koyu zeminde ana buton; #E59A4C yıldız ve ikon
  - soluk #5C6078 ikincil metin
  - yeşil #2E6B4F: Stokta, %5 rozeti, kartla öde dürtmesi
  - 11px etiket için #766B5B, sayaç için #A05A1C kullan. Eski #8A7F6E ve #B4651F kontrastta kalıyor.
- **Yazı:**
  - Young Serif 400 yalnız başlıkta: H1 50px/.95, H2 30px/1.06.
  - Onest gövde 16px (Main'de 15).
  - 12px altı yazı yok. Rakamlar `tabular-nums`.
- **Şekil:**
  - Köşe: levha 28, kart 14–22, buton 16, input 12, çip 999.
  - Kenar boşluğu 16px. Gölge yerine 1px çizgi.
  - Dokunma alanı ≥48px, ana buton 58px.
- **Hareket:**
  - Tek eğri `cubic-bezier(.2,.7,.2,1)`, yalnız transform ve opacity.
  - İmza an henüz seçilmedi ("Işığı kapat" kullanıcı tarafından çıkarıldı).
  - Yeni sonsuz döngü eklenmez. `prefers-reduced-motion` desteklenir.
- **İkon:** ince çizgili SVG, ilk çizgi amber. Emoji asla.

## Sayfa akışı (ürün sayfası)
1. Galeri: ana ürün fotoğrafları (gece sahnesi ve ışık anahtarı yok).
2. Üstüne binen karar levhası. Sırası:
   - puan ve Stokta, H1
   - 4'lü özellik şeridi
   - Model (küçük stüdyo fotoğraflı kartlar)
   - Paket: canlı sitedeki 1 Adet / 2 Adet kartları ve hediye disk şeridi
   - ince ay sonu şeridi, birlikte al
   - **İki buton: "Güvenli Ödeme İle Al" (%5) üstte, "Kapıda Ödeme ile Sipariş Ver" altta.** Kapıda ödeme ücreti ₺80 baştan yazılır.
   - güven üçlüsü, müşteri fotoğrafları
3. Bir gece, beş an.
4. Çipli yorumlar.
5. 12 disk.
6. Avucuna sığar ve kutu içeriği.
7. Videolar.
8. 30 gün iade mührü.
9. SSS.
10. Odanın geri kalanı.
11. Kapanış ve dev "Ayluna" alt bilgi.
12. Yapışkan çubuk.

## Gerçekler (uydurma yerine bunlar)
- İade 30 gün (90 değil): 14 gün yasal cayma + 16 gün Ayluna. Ücretsiz kargo. Kargo takibi Track123.
- Mağaza politikasında "1 iş gününde kargoda, 3–7 günde teslim" yazıyor, ama teyit listesinde. 16:00 kesimi teyitsiz.
- LunaDream fiyatları:
  - 1 lamba ₺1.699,99 (karşılaştırma ₺1.999,00)
  - 2 lamba ₺2.749,99 (karşılaştırma ₺3.998,00)
- Diğer fiyatlar:
  - AyFeneri ₺1.649,99 / ₺2.499
  - Galaksi Ambiyans ₺1.499 / ₺2.898
  - Galaxy USB ₺1.599 / ₺1.999
  - Kum Saati ₺799 / ₺999
  - Galaksi Night ₺2.199 / ₺2.999
  - Yıldız Işığı Nemlendirici ₺849,99 / ₺1.099
- Modeller: Kız = tavşanlı, Bluetooth ninni hoparlörlü. Erkek = Uzay Kaşifi robot, hoparlörsüz. Bluetooth vaadi modele bağlanır.
- Kutu: lamba + 6 disk + 6 hediye disk + USB kablo. Unicorn diski kutuda yok; gösterilmez.
- Yorumlar: Burak G., Handan B., Abdülkerim T., Sevcan Z., Mehmet C. Puan Loox'tan çekilir (4,7 · 62, teyit bekliyor). "Elif K.", 2.467, 10.000+ ve 12.000+ uydurmadır.
- Bilinmeyen değer köşeli yer tutucu kalır: [X] cm, [X] saat, [yaş], [Firma unvanı], [numara].

## İş verisi → tasarım kuralı
- Kapıda ödemede iade %28,6, ön ödemede %0,8. İadelerin %92'si "alıcı bulunamadı".
  - Kartla öde varsayılan ve indirimli.
  - Kapıda seçilirse toplam, teslim aralığı ve WhatsApp onayı formda görünür.
  - "Kartla öde, ₺X daha az öde" hatırlatması gösterilir.
- PTT'de iade %40. PTT öne çıkarılmaz.
- Gerçek dönüşüm sipariş ÷ oturum (≈%1,7); Shopify'ın oranı kapıda ödemeyi saymaz. Başarı teslim edilen ciroyla ölçülür.

## Dürüstlük
- Aciliyet yalnız gerçek kurala bağlanır:
  - ay sonu zammı (gerçekten varsa)
  - Shopify stok eşiği
  - Flow ile yazılan "dün satılan"
  - elle girilen sayı tarih taşır, eskiyince gizlenir
- "X kişi bakıyor", sahte geri sayım ve uydurma satış adedi yok.
- Sağlık iddiası ve teyitsiz teknik rakam yok. Sayfa vaadi kutuyla birebir aynı olur.
- **Mevzuat** (1 Ağustos 2026 değişikliği, Resmî Gazete'den doğrulandı):
  - Üstü çizili "önceki fiyat" = indirimden önceki **10 gün** içinde aynı kanalda uygulanan en düşük fiyat. Kampanya tarihleri yazılır.
  - Şartlı indirimler de bu kurala tabi: kartla %5, paket kazancı.
  - Satın alımı doğrulanamayan yorum yayımlanamaz. Olumsuz yorum gizlenemez.
- Yasal cayma 14 gündür. "30 gün iade" = 14 yasal + 16 Ayluna; yasal hak özel avantaj gibi sunulmaz.
- Sayaç İstanbul saatine göre, herkese aynı sabit tarihi gösterir; oturumla sıfırlanmaz.
- Kapıda ödeme gizlenmez. Ücretli ek önceden seçilmez.
- AI görseli "müşteri" diye sunulmaz.
- Ayrıntı: `ayluna-imza/ogrenme/arastirma.md` ve `TASARIM-BILGISI.md` §7.

## Görsel
- Ürün asla sıfırdan üretilmez. Gerçek fotoğraf referans alınır, sahne ve ışık değişir.
- Araç: Google Flow (Nano Banana Pro). İş akışı DEVAM.md'de.
- Görselde yazı üretilmez; metin HTML'de eklenir.
- Gerçek müşteri fotoğrafı ve videosu önceliklidir.

## Shopify
- **Sıfırdan Ayluna teması** (kullanıcı kararı, 17 Ekim). Hiçbir hazır tema (Horizon, Dawn…) kopyalanmaz ya da temel alınmaz; her parça benzersiz yazılır.
- İlk kurulum zip ile yapılır, sonraki değişiklikler `.txt` olarak verilir. Şu an canlıda ChatGPT ile yapılmış bir sürüm var; o da değiştirilecek.
- Kaynak `araclar/shopify-kaynak/*.liquid` → `python3 ayluna-imza/araclar/shopify-derle.py` → `shopify/*.txt`. Kurulum: `shopify/KURULUM.txt`.
- Bölümler Main.dc'ye göre yazılır.
- Bilinen hatalar `TASARIM-BILGISI.md` §8'de.
