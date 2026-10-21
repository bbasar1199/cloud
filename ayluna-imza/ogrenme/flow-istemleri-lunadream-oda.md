# LunaDream · "Odası böyle görünecek" 4 kart için Flow istemleri (21 Eki)

Neden: "Bir gece, beş an" kalkıyor (kullanıcı: "bir şey hissettirmiyor"). Benzer markalarda mutlu çocuk karesi tek başına değil; çocuk, ürün ve ışığı aynı karede (`ogrenme/rakip-sayfalar.md`). Kartlar: Tavanda masal · Birlikte dinleyin · Tavanda uzay · Masalı o seçsin.

Araç: Google Flow (Nano Banana Pro). Higgsfield kullanılmaz.
Kurallar:
- Ürün sıfırdan üretilmez. Referans `canvas/c-gorsel/lamba-kiz.png` ya da `lamba-erkek.png`; şekli, rengi, oranı aynen kalır.
- Tavandaki desen gerçek diskten (`canvas/diskler/disk-*.jpg`), yumuşak ve gerçek parlaklıkta; yalnız tavanda ve duvarın üst kısmında. Odanın her yerini kaplayan yıldız yok.
- Çocuğun yüzü yakın plan değil: arkadan, yandan ya da tavana bakarken.
- Oda Türk evine benzesin: tül perde, ahşap komodin, pamuklu nevresim, sade duvar. Stok fotoğraf havası, İskandinav vitrin odası yok.
- Görselde yazı yok (yazı sayfada HTML). Telefon ekranı görünmez.
- Sayfada "müşteri" etiketi konmaz; bunlar marka görseli. Yapay duran (el, parmak, yüz bozuk) kare kullanılmaz.
Boyut: 4:5, 1080×1350. Ürün karenin üst yarısında ya da ortasında kalsın; alt kısma yazı levhası gelebilir.

1. `lo-kiz-masal.jpg` · referans: lamba-kiz.png + disk-ay-yildiz.jpg + c-kiz-gece.jpg (ışık tonu için)
   "Gece, ışıkları kapalı bir çocuk odası. Ahşap komodinin üstünde yanan pembe tavşanlı LunaDream gece lambası (referanstaki ürün, şekli ve rengi aynen). Tavanda ve duvarın üst kısmında referans diskteki ay ve yıldız deseni, sıcak amber ışıkla, yumuşak. 4-5 yaşında bir kız çocuğu yatağında sırtüstü uzanmış, yüzü yandan, gülümseyerek tavana bakıyor. Tül perde, pamuklu nevresim, sade bir Türk evi. Gerçekçi fotoğraf, sıcak amber ve lacivert tonlar, sakin."
2. `lo-ninni.jpg` · referans: lamba-kiz.png + c-ninni-kiz.jpg
   "Gece, loş bir çocuk odası. Bir anne yatağın kenarına oturmuş, elinde telefon (ekranı görünmüyor), yüzü yandan. Yatakta battaniyeye sarılı küçük bir çocuk arkadan görünüyor, annesine dönük. Komodinde yanan pembe tavşanlı LunaDream gece lambası (referanstaki ürün aynen), odaya sıcak ışık veriyor; tavanda soluk yıldız deseni. Sade bir Türk evi, tül perde. Gerçekçi fotoğraf, sıcak, samimi, sakin."
   Not: büyükanne isteniyorsa "anne" yerine "büyükanne, gümüş saçlı" yazılır.
3. `lo-erkek-uzay.jpg` · referans: lamba-erkek.png + disk-uzay.jpg + c-erkek-gece.jpg
   "Gece, ışıkları kapalı bir erkek çocuk odası. Komodinde yanan robot biçimli LunaDream Uzay Kaşifi gece lambası (referanstaki ürün, şekli ve rengi aynen). Tavanda referans diskteki uzay deseni (gezegenler, yıldızlar), yumuşak ışıkla. 5 yaşında bir erkek çocuğu pijamasıyla yatağın üstünde oturmuş, sırtı kameraya dönük, eliyle tavandaki gezegeni gösteriyor. Sade bir Türk evi. Gerçekçi fotoğraf, lacivert ve sıcak sarı tonlar, sinematik ama sakin."
4. `lo-disk-sec.jpg` · referans: lamba-kiz.png + c-an-disk.jpg + 3-4 disk görseli (disk-masal, disk-okyanus, disk-sato)
   "Yakın plan, akşam, yatağın üstü. Bir çocuğun küçük elleri pamuklu nevresimin üstüne serilmiş yuvarlak masal disklerinden birini tutuyor (referanstaki diskler). Arkada odakta olmayan, yanan pembe tavşanlı LunaDream gece lambası (referanstaki ürün aynen). Yüz görünmüyor, yalnız eller. Sıcak amber ışık, gerçekçi fotoğraf, sığ alan derinliği."

Üretince aynı adla `canvas/c-gorsel/` içine koy, tuvale yükle (blob kimliği `araclar/blob-yerel.json`'a), sayfada kartların görsel kimlikleri değişir (`luna_e.py`, `luna_e_oda2.py`).
