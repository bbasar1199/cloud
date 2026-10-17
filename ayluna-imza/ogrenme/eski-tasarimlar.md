# Ayluna · eski tasarımlar ve öğrenilenler (17 Eki 2026, salt okuma araştırması)

Kaynaklar (hepsi yalnız okundu, hiçbirine yazılmadı):
- A "Ayluna Yeni Tasarım" (Design tuvali, son güncelleme 16 Eki) https://claude.ai/artifact/KxfUtccYZcAriWq72uSs6v
- B "Ayluna Tasarım Yönleri" (eski tuval, 13 Eyl) https://claude.ai/artifact/N8iMbsgD44AcTTaRBFNXA5
- C "LunaDream · Ayluna" (güncel seçilen tasarımın önizlemesi, 17 Eki) https://claude.ai/artifact/8ysSStTVmkY3ue96BTD1X3
- D "İmza Bölümler Kiti" (demo marka Telve, 16 Eki) https://claude.ai/artifact/AEVG41bgFh1dvxLSurTCcN
- E "İade Röntgeni" (7 Eyl) https://claude.ai/artifact/54t2CkS5V9QKfj7dVJPf3V
- Ek bağlam: "Ayluna Yeniden Tasarım Brifi" (Claude Docs, 15–16 Eki) https://claude.ai/artifact/HRsTVcRmCAK2UdDtXf558n,
  ayluna-tasarim becerisi (SKILL.md), yerel /home/user/cloud/ayluna-imza/DEVAM.md + RAPOR.md.

---------------------------------------------------------------------------------------------------
## 0. En önemli bulgular (özet)
1. **Hiçbir artifact'ta kullanıcı yorumu yok.** A, B, C, D, E ve "Ayluna İmza Tasarım" için ArtifactComments: 0 başlık.
   B'nin gömülü belgesindeki `comments` dizisi de boş. Brif dokümanında tek başlık var; o da Claude'un sorusu (bkz. §6).
   → Beğeni/ret sinyali yorumlardan değil; pano başlıkları, tuval notları, brif metni, beceri kuralları ve DEVAM.md'den çıkıyor.
2. **"H yönü (Gece masalı)" tuvalde YOK.** A'da 15 pano var: G, I, J, K, L (mobil) + "I — Masaüstü" (3 pano).
   Hiçbir panoda Bricolage Grotesque / Figtree yok; becerideki H renkleri (#F3B562, #10182B, #EBDDD4, #F5F3EF) hiçbir panoda geçmiyor.
   Tuvalin `createdOnFiles` damgası 2026-10-16 00:40 → H büyük olasılıkla bu yeniden kurulumda I ile değiştirildi/silindi.
   Figtree yalnızca E'de (İade Röntgeni rapor fontu) var. **Beceri (SKILL.md) bu konuda bayat; güncellenmeli.**
3. Kazanan sırası (kanıta göre): B'nin 4 yönü (A–D, Eyl) → brifte "önceki dört denemenin ortak hatası: tasarım süsle başladı" diye
   toptan reddedildi → A tuvalinde G "önceki sürüm" etiketiyle geride bırakıldı → H (beceride "güncel") → **I kazandı** (yalnız I masaüstüne
   genişletildi: "I — Masaüstü"; tuval açılışı UrunGalaxyD) → J/K/L alternatif konsept olarak kaldı ama fikirleri sonraki tasarıma taşındı
   → 17 Eki: **İmza tasarımı (C: krem/lacivert/amber, Young Serif + Onest)** seçildi (DEVAM.md: "Kullanıcının seçtiği pano project/Main.dc.html").

---------------------------------------------------------------------------------------------------
## 1. B · "Ayluna Tasarım Yönleri" (13 Eyl, masaüstü 1440px, 4 yön + Main)
Tuval notları (canvas.json annotations) kararları taşıyor. Main panosu: "seçilen yön buraya işlenecek (şu an A)".
Not: "Seçtiğiniz yönü söyleyin: o yön Main'e işlenir ve ardından gerçek Shopify temasını … sıfırdan yazarım." → Kullanıcı seçimi kayıtlı değil.

| Yön | Palet (hex) | Font | Ruh | İmza fikri | Durum / kanıt |
|---|---|---|---|---|---|
| A · Sıcak Güven | lacivert #22304F, mürekkep #1E1B2E, mercan #E8734A, krem #F3EDE4/#FBF7F1, bej #EADFD2, güven yeşili #1C9C5B, amber #F2A93B | Nunito 600–900 (başlık) + Manrope | "mevcut sitenin evrimi", anne-çocuk yumuşaklığı | Hero'da ürün + canlı "Elif K. az önce sipariş verdi · İstanbul · Kapıda ödeme" kartı; üstte "Bugüne Özel %20 · 23:59:58" sayacı | Main'e varsayılan işlendi ("şu an A"); not: "+ en düşük risk, 9.000 siparişlik akışa en yakın / − rakiplerden çok ayrışmaz". Sonra brifle reddedildi |
| B · Premium Beyaz | siyah #111118, indigo #4F46E5 (tek vurgu), yeşil #16A34A, #F6F6F8, #E7E7EC | Sora 500–700 + DM Sans | Apple tarzı, geniş boşluk | Tek büyük ürün fotoğrafı + rakamlı güven şeridi (9.000+ sipariş, 4.7/5 2.467 yorum, 1–3 gün, 90 gün) | Not: "− duygusal sıcaklık az, kapıda ödeme vurgusu sessiz". Reddedildi |
| C · Ay Işığı Vitrin | gece lacivert #1B2148/#171A33, altın #D4A64A, lila-beyaz #ECEAF8/#F4F3FA, yeşil #1E9E63 | Quicksand 600–700 + Nunito Sans | açık sayfa, yalnız hero gece+altın | Güven şeridi hero'nun üstüne biner; ay/yıldız teması | Not: "+ ürün temasını taşıyan tek yön, akılda kalıcı / − hero foto kalitesine bağlı". Gece-lacivert+sıcak ışık fikri sonraki yönlere taşındı |
| D · Pastel Çocuk | pembe #F26B8A, gök mavisi #5B8DEF, mürekkep #33303F, #FFEEF2, krem #FFF9F5, yeşil #2BB673 | Baloo 2 + Nunito | oyuncu, kapsül butonlar | Yüzen özellik kartları, 9:14 video kartları, 🎁 emojili duyuru | Not: "− projektörlerde nötr değil". Emoji + sevimli dil sonra açıkça yasaklandı |

B'nin ortak hataları (sonradan brif/beceri ile yasaklandı): 2.467 onaylı yorum, "+10.000 mutlu anne", "9.000+ sipariş", "Elif K." (doğrulanmamış),
sahte gün sonu sayacı 23:59:58, **90 gün iade** (gerçeği 30), "1-3 iş günü" teslim (gerçeği 3–7), ödeme ikonu Visa/MC/Troy.

---------------------------------------------------------------------------------------------------
## 2. A · "Ayluna Yeni Tasarım" (Design tuvali, 15 pano)
Tuval başlık notları: "G — önceki sürüm", "I — Ana sayfa + ürün", "J · Bir gece", "K · Hediye kutusu", "L · Ay atlası", "I — Masaüstü".
Sıra (order): Masaüstü I (AnasayfaD, UrunD, UrunGalaxyD) → I → J → K → L → G (en sonda). launch = UrunGalaxyD (son çalışılan).

### G — "önceki sürüm" (YonG "Ana Sayfa (Mobil)", UrunG "LunaDream Ürün Sayfası (Mobil)", başlık "Masalsı Gece Işıkları")
- Palet: mürekkep/mor-gece #1E1B2E, krem #FAF6F0, kil-kahve #9A6B3C, kum #C9AE86, bej #E6DCCB, lavanta griler #A79FB2/#7A7487/#CFC8DA, altın #E2C796, #B98A4A.
- Font: **Cormorant Garamond** (serif, italik) + Be Vietnam Pro.
- Ruh: zarif, masalsı, "Her gece, küçük bir masal." / "Uyku vakti savaşa dönüyorsa, yalnız değilsin."
- İmza: 3,5 sn'de dönen duyuru notu; "Tanıdık geldi mi?" problem→çözüm listesi; 0→21 mod sayacı (50 ms adım); her bölüme reveal (IntersectionObserver);
  "Ses için dokun" UGC videoları; LunaDream vs sıradan lamba tablosu; 1/2/3 paket (₺1.699,99 / ₺2.999 "Kardeş paketi" / ₺4.299 "En avantajlı");
  teslimat yolculuğu (Track123, 3 adım: form → WhatsApp onay → kapıda öde); il seçerek teslim günü (UrunG).
- Durum: **REDDEDİLDİ/geride bırakıldı.** Kanıt: tuvalde "önceki sürüm" etiketi, sırada en sonda; becerinin YAPMA listesi tam bunu tarif ediyor
  ("krem zemin + serif + kil rengi şablonu", "sayaç animasyonu", "her bölüme fade-in"). Ayrıca 90 gün iade hatası.

### H — "Gece masalı" (beceriye göre "güncel"): **tuvalde bulunamadı** (bkz. §0.2).
- Beceriden bilinenler: Bricolage Grotesque + Figtree; amber #F3B562 (lamba ışığı), karanlık oda laciverti #10182B, lamba pembesi #EBDDD4, ay beyazı #F5F3EF;
  kart 8–10px, buton 10px, yalnız çipler hap; hareket tek anlamlı anda ("Işığı kapat" anahtarı, disk→tavan önizlemesi, kayan avantaj bandı).
- Bu fikirlerin bir kısmı C'de yaşıyor ("Işığı kapat" anahtarı, disk→tavan önizlemesi), fontlar ve hex'ler yaşamıyor.

### I — "Ana sayfa + ürün" (YonI/YonI2, UrunI/UrunI2) + "I — Masaüstü" (AnasayfaD, UrunD, UrunGalaxyD)  ← tuvalin kazananı
- Palet: lacivert #18203D (ana metin + buton), beyaz #FFFFFF zemin, altın #E2B86A (vurgu/gold buton), yumuşak gri-mavi #F4F6FA/#EEF1F7/#EDEFF4,
  gece #0F1530 (koyu bloklar), mavi ikon #3D5A9E, koyu amber #C7923E, kaş etiketi kahve #9B6B22, metin griler #5D6478/#667085/#98A0B3/#AEB4C8, pil yeşili #3BB273.
- Font: **Poppins** 300–800 (başlık 700 + ikinci satır 300 "ince satır" kalıbı), gövde de Poppins.
- Ruh: temiz, beyaz, güvenli e-ticaret; gece blokları ürünün ışığını gösteriyor. Başlık: "Uyku vakti, masal vakti."
- İmza fikirleri:
  - **Masal diski seçici**: raydan disk seç → disk eğik lambaya (rotateX 76°) oturup 5 sn'de döner, ışık huzmesi (clip-path), tavanda dairesel maskeli
    yansıma 60 sn'de döner; "Takılı: Okyanus · 3/12". Masaüstünde: "kubbe kalkar, disk yuvasına oturur, kubbe kapanır; ışıklar söner, masal tavana yansır".
  - Gece manifestosu "UYU. HAYAL ET." (koyu blok).
  - Kayan avantaj bandı (marquee 34 sn): kapıda ödeme · 21 mod · +6 hediye disk · ücretsiz kargo · 1 yıl garanti.
  - Özellik karoları mikro-animasyonlu: nefes alan hale 4,5 sn, mod renk çubuğu 6 sn, şarj olan pil 3,8 sn.
  - "Sıradan bir gece lambası alabilirsin. Ya da…" karşılaştırma; "Bizi değil, kullanıcılarımızı dinleyin." (Loox 4,7 · 62).
  - Hediye bölümü "Kutusunu açtığı gece kullanılan hediye." + paketler + "+6 ücretsiz hediye masal diski".
  - Ürün sayfası: foto sayacı "1/8", model kartları (Kız = Tavşan · ninni hoparlörlü / Erkek = Robot · hoparlörsüz), paket, kapıda ödenecek toplam,
    teslim tarih aralığı, "Kartla öde · sepette %5 indirim", yapışkan alt çubuk "Sipariş ver".
  - Masaüstü: gerçek kargo kesim sayacı ("Bugün kargoda için kalan süre: SS:DD:ss", kesimden sonra "Şimdi sipariş ver, {gün} kargoda");
    il seçimli teslim tahmini ("İş günü üzerinden; pazar ve resmî tatil sayılmaz"); "Stokta · Bugün kargoya hazır".
  - Galaxy USB masaüstü: "Bir USB girişi, koca bir galaksi." (Bilgisayar/Powerbank/USB adaptör), teknik tablo, sağlık iddiası yok,
    "Loox yorumları burada görünür" yer tutucusu (yanlış ürünün yorumu yok) → brifin P4 maddesine uyuyor.
- Durum: **TUTULDU (o tarihte)**. Kanıt: J/K/L içinden yalnız I masaüstüne genişletildi; not "I — Masaüstü"; launch = UrunGalaxyD.
  17 Eki'de C (İmza) ile değiştirildi; I'nın satış mantığı (model kartı, paket, toplam, teslim, yapışkan çubuk, disk→tavan) C'ye geçti.
- Kural ihlalleri (beceriye göre): harf aralıklı büyük harf kaş etiketleri (.eb 11px .16em uppercase), 18px radius + gölgeli eş kartlar,
  Unicorn diski listede (kutuda yok!), birçok sürekli animasyon.

### J — "Bir gece" (YonJ/YonJ2) — I sistemi + Caveat el yazısı vurgu (#2B2F45, 30px)
- İmza: saat saat gece hikâyesi, yapışkan saat gezgini: 19:30 Pijama · 20:15 Disk · 20:30 Işıklar · 21:00 Ninni · 03:00 Uyanma · 07:00 Günaydın.
  20:15 "Bu gecenin masalını o seçer" disk seçici; 20:30 **önce/sonra kaydırma çubuğu** (lamba modu ↔ projeksiyon); 21:00 Bluetooth ninni
  ("Dandini dandini dastana", dalga animasyonu); 03:00 parlaklık kaydırıcısı "%{br}"; 07:00 "Sabah gelen mesajlar" (gerçek yorumlar).
  Kopya: "Ekran yerine ışık", "Karanlık korkusu yok", "Bu akşam sipariş ver, birkaç gece sonra masal başlasın."
- Durum: pano olarak genişletilmedi, ama **fikri kalıcı oldu**: beceride "saatli ritüel (20:30 disk seçilir…)" önerisi; C'de "Bir gece, beş an"
  makaraları (20:00 Işığı yak · 20:30 Diski seç · 20:45 Ninni/Robot · 21:00 Tavanda masal · 21:15 Gözler kapanır); RAPOR: "Gece hikâyeleri: girsin".

### K — "Hediye kutusu" (YonK/YonK2) — I sistemi + Caveat
- İmza: "Kimin için?" seçici (Kızıma / Oğluma / Torunuma / Yeğenime / İki kardeşe → doğru model + paket + ilgili yorum + CTA);
  "Noktalara dokun" kutu içeriği hotspotları; **hediye notu kartı** (şablon: Masal / Doğum günü / Cesaret; "Sevgili {kime} … — {kimden}",
  "notunu sipariş notuna yaz, kartı pakete ekleyelim"); "Yetişir mi? Özel gün ne zaman?" (gerçek 3–7 gün teslimden hesaplı uyarı);
  kutu açılışı müşteri videosu; paket 1 / 2 adet (₺2.749,99, ₺1.375/adet); "Sürprizi bozmaz: kart bilgisi yok, ödeme teslimatta"; bütçeye göre hediye.
- Durum: genişletilmedi; **kısmen kalıcı**: becerideki "hediye notu seçeneği", "varyant bazlı kutuda ne var"; C'de "Kutudan ne çıkıyor?" kutu açma
  ve "2 lamba · Kardeşe ₺2.749,99" paketi.

### L — "Ay atlası" (YonL/YonL2) — I sistemi + Caveat
- İmza: 5 ürün = 5 ay evresi (Yeni ay=Kum Saati, Hilal=LunaDream, İlk dördün=Galaxy USB, Şişkin ay=Galaksi Ambiyans, Dolunay=AyFeneri), evre gezgini;
  "Hangi oda, hangi ışık?" oda seçici; "30 saniyelik test: İki soru, doğru ışık"; kurucu notu "Neden ay ışığı?" (yer tutuculu);
  kapıda ödeme **kargo fişi** kartı ("No. AY-0000 … Kapıda ödenecek ₺1.699,99 · Fişi onayla, kapıda öde").
- Durum: genişletilmedi; C'de izi yok. Çoklu ürün/kategori ana sayfası için saklanabilir fikir (brifte "iki kapı: Çocuk Odası / Ambiyans").

---------------------------------------------------------------------------------------------------
## 3. C · "LunaDream · Ayluna" (güncel seçilen tasarım, referans)
- Token: krem #F6F1E9, yüzey #FFFDF9, çizgi #E3D8C7, lacivert #1A2142, gece #141A36/#0C1027, soluk #5C6078, gece metni #F4EDE3/#B9BED6,
  amber #F2A65A / #E59A4C, rozet #F9DFC4/#8A4A12, yeşil #2E6B4F. Font: Young Serif 400 + Onest 400/600 (yerel woff2). Eğri cubic-bezier(.2,.7,.2,1).
- Akış: duyuru → sahne ("Işığı kapat" anahtarı, 1 sn sonra 2,6 sn'de kendiliğinden geceye geçer; 19:30→21:00 saat) → alttan açılan levha
  (başlık köşeli parantez odağı, harf başına 45 ms) → bento → model (kaydırmalı, yerine oturan) → paket 1/2 → ay sonu sayacı (gerçek zam tarihi,
  son 3 günde saniye + amber) → birlikte al (nemlendirici) → **kaydırarak kapıda öde** (CRED uyarlaması, %60 eşik) → sayfa içi form →
  yorum destesi (çipler Tümü/Uyku/Hediye/Kalite, kart fırlatma 430 ms) → kutuyu aç (12 disk sırayla, 60 ms aralık; kaydırınca kendiliğinden açılır) →
  gece bloğu (yakınlaşan sahne + paralaks diskler, 3B disk halkası 30°/disk, "Bir gece, beş an" eğik makaralar, SSS + "30 gün iade" mühür,
  kardeş kapanışı gündüz→gece, diğer ışıklar) → tepeler + dev "Ayluna" yazısı → yapışkan çubuk.

---------------------------------------------------------------------------------------------------
## 4. D · "İmza Bölümler Kiti" (demo marka "Telve", soğuk demleme kahve) — 6 bölüm, mekanizma + zamanlama
Sistem: buz-adaçayı #E6ECE8/#D6DFD9, kart #F7F9F7, espresso #21160F/#3B2A1E, soluk #5F5953/#B9ADA2, tek vurgu kafein sarısı #F2B705/#C99400.
Font: Geist (400–800, gösterim) + Instrument Serif italik (yalnız başlığın "kuyruk" kısmı). Ease cubic-bezier(.2,.7,.2,1); kart 10px, buton 12px.
Her bölümde kaynak etiketi var (tweet/site referansı); reduced-motion'da tüm hareket kapanır, uçuş düz akışa döner.

1. **Söz hero** (zero / PrismDraft): başlık kelime kelime iner — opacity 0 + translateY 16px + blur 12px → net; süre .34 s;
   gecikme 1. satır `i×60ms + 120ms`, 2. satır (serif italik, soluk renk, 1.08em) `i×50ms + 380ms`. Yanda şişe sahnesi + 4 yüzen logo karosu
   (`suz` 6 s ease-in-out alternate, −10px + 6° dönüş, gecikmeler 0/−2/−4 s). CTA "Kapıda ödemeyle al →", altında kargo · 30 gün iade · WhatsApp onayı.
2. **Sayfa uçuşu** (zero 3D video promptu): 200vh bölüm, 100svh yapışkan pin; tek kaydırma ilerlemesi p (0→1) sürer.
   Yaprak: `rotateX(52° − 14°·p) translateY(−22%·p) translateZ(−40px·p)`, perspective 1100px. Adımlar `data-at` .08 / .32 / .56'da,
   pencere .18, smoothstep `l²(3−2l)`; kart `translateZ(l·70px) rotateX(−38°·l)` ile kalkıp sana döner, gölge l ile büyür. rAF ile kısılmış.
3. **Ürün sahnesi** (Bardhyl kahve videosu): koyu bant; aroma çipleri (Sade/Vanilya/Portakal) şişe etiket rengini (`--etiket`) ve uçuşan
   malzemeleri değiştirir (opacity+scale .4 s); her parça `--d` derinliğiyle imleç (mx,my) ve kaydırma (sy = merkeze uzaklık × −1.2) paralaksı alır;
   altta sabit tohumlu 80 çekirdek yığını.
4. **Kapıda ödeme PDP** (Lemme / Stepan): scroll-snap galeri + kenarda kesilen küçük resim şeridi + "1 / 4" sayaç; 4 ikonlu fayda satırı;
   1/2/3 paket radyo ("En avantajlı fiyat/bardak" bandı, birim fiyat); CTA altında: kapıda ödenecek toplam (canlı), tahmini teslim (bugün+2…+5 iş günü,
   hafta sonu atlanır), WhatsApp onayı, 30 gün iade. Yapışkan çubuk: ana CTA ekrandan yukarı çıkınca VE PDP görünürken açılır (2 IntersectionObserver), .3 s.
5. **Yorum duvarı** (HUGGD / ecomlanders): masonry sütun 1 / 2 (≥620px) / 3 (≥960px); konu çipleri (Hepsi/Tat/Pratiklik/Hediye) filtreler;
   alıntılar serif 21px; "örnek" etiketi (uydurma puan gizlenmiyor).
6. **Dev yazı alt bilgi** (HUGGD): marka adı genişliğe sığdırılır (100px'te ölç → genişlik/scrollWidth × .98), fontlar yüklenince yeniden;
   ekranın altındaysa harfler translateY 60% + opacity 0'dan .9 s'de yükselir, harf başına 70 ms gecikme, %30 görünürlükte tetiklenir; son karakter vurgu rengi.
→ C bu kitten 4, 5, 6'yı (PDP mantığı, çipli yorum, dev yazı footer) Ayluna'ya uyarladı; hero kelime-blur ve sayfa uçuşu kullanılmadı.

---------------------------------------------------------------------------------------------------
## 5. E · "İade Röntgeni" (31 Ağu – 6 Eyl 2026; AYLUNA · Steamora)
Görsel: Stripe dili (eğik degrade bant, indigo #635BFF, #0A2540), **Figtree + IBM Plex Mono** (Figtree'nin göründüğü tek yer).
Hafta: 336 gönderi (+%39,4), 253 teslim, 96 iade; ciro ₺473.767 (+%18,8); brüt kâr ₺269.768 (+%31,1, marj %56,9); kargo kesintisi ₺71.464 (+%41).
İade depoya çıkıştan **medyan 9 gün** sonra döner (%75'i ≤17 gün, en uzun 24) → haftalık kâr şişkin; olgun iade oranı **%23,5** vurursa kâr ≈ ₺182.000.
Olgun kohort: 16 Tem–17 Ağu, 1.913 gönderi.
- 01 **Kapıda ödeme iadenin tek sebebi**: kapıda 1.557 gönderiden 446 iade **%28,6**; ön ödemeli 356'dan 3 iade **%0,8** (27,8 puan).
  Kapıda nakit 909 → %30,5; kapıda kart 642 → %26,3; ön ödeme → %0,8. Fazla iade ≈ 95/hafta ≈ ₺13.700 yalnız taşıma.
  Öneri: ön ödemeye indirim (₺100 bile ₺144'lük iade taşımasından ucuz), yüksek iadeli illerde kapıda ödemeyi kapat, **ön ödeme varsayılan**.
- 02 105 gönderi kayıt dışı: ₺159.101 kapıda tahsilat + 121 adet (iki kargo dosyası arası boşluk) → haftalık dosya 1 gün bindirmeli çekilmeli.
- 03 Kargo: Aras 1.056 gönderi %26,1; HepsiJet 419 %17,7; Sürat 56 %3,6; **PTT 144 %40,3**; firması boş 238 %16,4.
  Öneri: PTT'yi durdur (~7 iade/hafta), Aras'tan HepsiJet'e kaydır (100 gönderide 8 iade az), Sürat'ı araştır. ~25 fazla iade/hafta ≈ ₺3.600.
- 04 **İadelerin %92'si "Alıcı Bulunamadı"** (88/96), yalnız 8'i "Müşteri Talebi" → sorun ürün değil teslimatın gerçekleşmemesi.
  Öneri: sipariş sonrası telefon doğrulaması, kargodan önce "yarın teslim" SMS'i, teslimat saati tercihi.
- 05 İller: Diyarbakır %41,9, Gaziantep %38,5, Hatay %37,5, Muğla %35,1, Kahramanmaraş %33,3, Şanlıurfa %30,4 (başlık "%33 üstü" diyor; Şanlıurfa
  altında — rapor içi tutarsızlık). İstanbul iadelerin %22'si (hacimden). Öneri: bu illerde COD kapat ya da COD ücreti al.
- 06 Kum Saati, Işıklı Nemlendirici, Astronot'ta alım kaydı yok (AST01 net −1).
- Ürün: LD01 LunaDream Kız 232 teslim / 69 iade / net 163; LDK Erkek 43/9/34; KUM01 6/4; NEM01 4/3; AST01 1/2. **LD01 cironun %83'ü.**
  (Not: tablo "bu hafta çıkanlar" diyor ama not "bu haftanın çıkışlarından henüz iade dönmedi" diyor → iade sütunu dikkatle okunmalı.)
- Hafta karşılaştırma: ort. sepet ₺1.873, gönderi başı kesinti ₺213, iade taşıma ₺4.644 → ₺16.713 (+%259,9); bu hafta iade ücreti ₺19.467.
- Brifin rakamı: iade/red ≈ %21; olgun ölçüm %23,5. Kâr rakamları KDV/vergi/reklam/paketleme öncesi.
**Tasarım çıkarımları**
- Sayfa, kapıda ödemeyi "kolay ret" olmaktan çıkarmalı: **kartla/online öde varsayılan + görünür indirim** (C-artifact'ta hâlâ COD birincil;
  DEVAM'a göre yerel sürüm kartı varsayılan yaptı — artifact'ın güncellenmesi gerekebilir).
- COD alıcısını bağla: WhatsApp/OTP onayı, "kapıda ödenecek toplam" net, teslim tarih aralığı, formda teslim saati tercihi, "yarın kapında" beklentisi.
- Sahte aciliyet dürtüsel COD siparişi → kapıda ret üretir; aciliyet yalnız gerçek veriye (ay sonu zammı, kargo kesimi, stok).
- %8'lik "müşteri talebi" kısmı için vaat = kutu: Unicorn diski yok, 6+6 disk, Bluetooth yalnız Kız, AI görsel yerine gerçek foto/video.
- Kargo logolarında PTT'yi öne çıkarma; il bazlı COD kapatma Shopify/COD uygulaması ayarıyla, temada "bu ilde online ödeme" mesajı gerekebilir.

---------------------------------------------------------------------------------------------------
## 6. Kullanıcı yorumları (birebir) — konum ve anlamı
- A, B, C, D, E, "Ayluna İmza Tasarım": **yorum başlığı yok** (ArtifactComments read → "No comment threads").
- B gömülü belge (appifact-doc) `comments: []`.
- Brif dokümanı, tek başlık (ae038338-2b71, 15 Eki 21:30, Başar hesabından, yanıtsız), "Altyapı" paragrafında
  "Shopify'ın ücretsiz Horizon teması temel" alıntısına bağlı:
  > "Altyapıyı Horizon + Ayluna'ya özel bölümler olarak seçtim; yoksa yine sıfırdan tam zip tema mı istersin? Buraya yanıt yazabilir ya da dokümanın herhangi bir yerine yorum bırakabilirsin."
  Anlam: Bu Claude'un kullanıcıya sorusu (kullanıcı hesabı adına bırakılmış); yanıt yok → altyapı kararı yorumla onaylanmamış.
  Pratikte C/DEVAM Horizon üzerine .txt bölümlerle ilerliyor (sessiz kabul).
- Yorum dışı kullanıcı geri bildirimi (dolaylı, yerel DEVAM.md; birebir):
  - "Sevmedikleri: emoji ikonlar, boğucu/çok yazılı sayfa, Shopify teması gibi sıradan düzen, tamamen koyu tema, uydurma sayı/sayaç, abartılı efekt."
  - "İstedikleri: "acayip ama sıkmayan" tarz, doğa gibi uyumlu hareketler, güven veren, dönüşüm odaklı; bundle, ay sonu fiyat geri sayımı
    (her ay zam yapıyor), sosyal kanıt; tek ürün mağazası değil (15 ürün)."
  - 17 Eki: "İnsanların alıştığı kalıplar (emoji fayda listesi, indirim sayacı, "dün satılan", stok alarmı) atılmaz; iyileştirilir. Baskı unsurları
    istiyor; gerçek veriye bağlanır" · "Gösteriş/yeniden kurgu değil, işe yarayan iyileştirme bekliyor."
  - Beceri: "Yıldız animasyonu, gereksiz efekt yok (kullanıcı daha önce reddetti)."
  - Brif: "Önceki dört denemenin ortak hatası: tasarım süsle başladı. Bu sefer satış akışından başlıyoruz."

---------------------------------------------------------------------------------------------------
## 7. Eski yönler ↔ güncel tasarım (C) çelişkileri
Font
- Güncel: Young Serif + Onest. Eski: B → Nunito/Manrope, Sora/DM Sans, Quicksand/Nunito Sans, Baloo 2/Nunito; G → Cormorant Garamond + Be Vietnam Pro;
  H (beceri) → Bricolage Grotesque + Figtree; I–L → Poppins (+ Caveat el yazısı J/K/L); D → Geist + Instrument Serif; E → Figtree + IBM Plex Mono.
- **SKILL.md hâlâ "H: Bricolage Grotesque + Figtree" ve "güncel tasarım H yönü" diyor → yanlış yönlendirir; C fontlarıyla güncellenmeli.**
Renk
- Amber: güncel #F2A65A/#E59A4C ↔ beceri #F3B562 ↔ I altını #E2B86A ↔ B-C altını #D4A64A ↔ G #E2C796.
- Lacivert: güncel #1A2142/#141A36/#0C1027 ↔ beceri #10182B ↔ I #18203D/#0F1530 ↔ B-A #22304F ↔ B-C #1B2148.
- Krem: güncel #F6F1E9/#FFFDF9 ↔ G #FAF6F0 ↔ beceri ay beyazı #F5F3EF ↔ I beyaz #FFFFFF. Beceri "lamba pembesi #EBDDD4" C'de yok.
Kural çelişkileri (beceri/brif ↔ C)
- Beceri YAPMA: "krem zemin + serif + kil rengi şablonu" ↔ C = krem + serif (Young Serif) + amber. Fark: kil değil lamba amberi + gece lacivert
  blokları; yine de G'nin reddedilme sebebine yakın → serif'i tek karakterli başlıkta tut, kil/kahve tonlarına kayma.
- Beceri: "kart 8–10px, buton 10px, yalnız çipler hap" ↔ C: kart 14–28px, buton 16px, kaydırma çubuğu ve çipler 999px.
- Beceri/brif: "hareket tek anlamlı anda; efekt yok" ↔ C: otomatik ışık geçişi, başlık odak animasyonu, 3B disk halkası, eğik makaralar,
  paralaks diskler, otomatik kutu açılışı, tepe/ay paralaksı, dev yazı. Kullanıcının sonraki isteği "doğa gibi uyumlu hareketler" bunu kısmen
  meşrulaştırıyor ama "abartılı efekt" sevilmiyor → her hareket bir ürün gerçeğini göstermeli.
- Brif: "koyu renk sadece ürünün ışığını gösteren kartlarda" ↔ C'nin alt yarısı tamamen gece bloğu (DEVAM: "tamamen koyu tema" sevilmiyor; C "gündüzden
  geceye akar" ile sınırda).
- Beceri: "sayaç animasyonu / sayaç yok" ↔ C ay sonu sayacı: kullanıcı istedi, gerçek zam tarihine bağlı → izinli; B'deki sahte 23:59:58 değil.
- Brif: 1/2/3 adet paket ↔ C yalnız 1 / 2 lamba (3'lü yok; G'de 3'lü ₺4.299 vardı).
- E: ön ödeme varsayılan ↔ C-artifact: "Kaydır, kapıda öde" birincil, "Online ödersen ek %5" küçük not (yerel DEVAM'da düzeltilmiş: kart varsayılan).
- Teslim: beceri "1 iş gününde kargoda, 3–7 gün" ↔ C-artifact "Hafta içi 16:00'ya kadar aynı gün kargoda" + 16:00 geri sayımı, SSS "[X] iş günü"
  (DEVAM: 16:00 kesimi kaldırıldı, teyitsiz).
- Kargo: beceri/DEVAM "Aras · DHL · PTT" gösteriyor ↔ E: PTT %40,3 iade, durdurulmalı.
- Menü: brif "Çocuk Odası · Ambiyans & Dekor · Hediye · Kargo Takip" ↔ I/D-masaüstü ürün adı menüsü (LunaDream/AyFeneri/Projektörler/Nemlendiriciler).
- İade: G ve B "90 gün" ↔ gerçek ve C "30 gün". Yorum sayısı: B "2.467 / 10.000+" ↔ gerçek Loox 4,7 · 62.
- Diskler: I/J/K/L/masaüstü listelerinde **Unicorn** var (brifte "görselde unicorn var, kutudan çıkmıyor — 2 şikâyet") ↔ C'nin 12 disk listesinde yok (doğru).
  Disk sayısı: I–L "[adet] tema diski", masaüstü "6 tema diski +6 hediye", C "12 masal diski, 6'sı hediye" (brif şikâyeti "12 disk yazıyor 6 geliyor"
  → C kutuda "6 masal diski + 6 hediye disk" diye ayırıyor; korunmalı, 2'li pakette hediye sayısı teyitsiz).
- I–L'de harf aralıklı BÜYÜK HARF kaş etiketleri, "AYLUNA / GECE IŞIKLARI" logotip → beceride yasak; C kullanmıyor.

---------------------------------------------------------------------------------------------------
## 8. Kalıcı dersler (tekrar kullanılabilir kurallar)
1. Satış akışından başla, süsten değil: B'nin 4 yönü ve G süsle başladığı için düştü. Her bölüm bir satış sorusunu yanıtlamalı.
2. Sayı uydurma: puan/yorum Loox'tan (4,7 · 62), isimler yalnız Burak G., Handan B., Abdülkerim T., Sevcan Z., Mehmet C.; "Elif K.", 2.467, 10.000+, 9.000+ yok.
3. Aciliyet yalnız gerçeğe bağlı: ay sonu zammı, kargo kesimi, gerçek stok/satış (Shopify/Flow). "X kişi bakıyor", sabit 23:59:58 yasak.
4. Vaat = kutu: 30 gün iade; Bluetooth yalnız Kız (Tavşanlı); Erkek = Uzay Kaşifi robot, hoparlörsüz; disk sayısı "6 + 6 hediye" ayrık;
   Unicorn diskini hiçbir listede gösterme; AI parlaklığında görsel yerine gerçek karanlık oda çekimi.
5. Ödeme tasarımı iade tasarımıdır: online/kart varsayılan + görünür indirim; COD seçilirse toplam, teslim aralığı, WhatsApp/OTP onayı,
   teslim saati tercihi formda. "Alıcı bulunamadı" (%92) teslimat taahhüdüyle düşer, ürün metniyle değil.
6. Kargo: PTT'yi rozet/ikon olarak öne çıkarma; il bazlı COD kapatma için sayfada alternatif mesaj alanı bırak.
7. Kazanan desenler (her turda koru, silme): model kartı (Kız/Erkek) + paket + kapıda ödenecek toplam + teslim tarihi + yapışkan çubuk;
   disk seç → tavan önizlemesi; "Işığı kapat" gündüz→gece anahtarı; saatli gece ritüeli (J → "Bir gece, beş an"); kutudan ne çıkıyor (K);
   "Sıradan bir gece lambası alabilirsin. Ya da…" karşılaştırması; çipli yorumlar (Uyku/Hediye/Kalite); "Kardeşe" 2'li paket; hediye notu.
8. Kaybeden desenler: emoji ikonlar, pastel/sevimli Baloo dili, Apple-beyaz soğukluk, krem+serif+kil şablonu, her bölüme fade-in, 0→21 sayaç,
   harf aralıklı büyük harf etiketler, aynı radius+gölgeli eş kart ızgarası, yıldız animasyonu, tamamen koyu tema, uzun metin.
9. Hareket: ürün gerçeğini gösteren, dokunmayla tetiklenen, transform/opacity'li; tek eğri cubic-bezier(.2,.7,.2,1); prefers-reduced-motion'da kapat.
   Otomatik oynayanlar (ışık geçişi, kutu açılışı) tek seferlik olmalı, döngüsel süs olmamalı.
10. Galaxy USB / ambiyans ürünleri: sağlık iddiası yok, "USB ile çalışır" net, yalnız kendi yorumları (yoksa Loox yer tutucusu) — I-masaüstü örneği iyi.
11. Çok ürünlü mağaza: L'nin "ay evresi atlası", "oda seçici" ve "2 soruluk test" fikirleri ana sayfa/kategori için yedekte; brifteki iki kapı
    (Çocuk Odası / Ambiyans) ile birleştirilebilir.
12. Mobil önce (390px), sonra masaüstü (solda yapışkan galeri, sağda satın alma kutusu); teslim: tema bölümleri .txt.
13. Becerideki (SKILL.md) H/font/hex bilgisi bayat: kaynak gerçek olarak C token'larını (krem #F6F1E9, lacivert #1A2142, amber #F2A65A, Young Serif + Onest) esas al.
14. Kayıtlar: kullanıcı geri bildirimi artifact yorumlarında birikmiyor; kararları pano başlığına/tuval notuna ve DEVAM.md'ye yaz ki sonraki tur bulabilsin.
