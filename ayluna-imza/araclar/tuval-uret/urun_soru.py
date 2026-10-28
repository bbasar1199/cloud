# Ayluna · ürün soruları (22 Eki). LunaDream'deki teslim altı soru kartının (luna_e.py, .urs) diğer ürün sayfalarına taşınmış hâli.
# Kullanıcı: "Diğer ürünler için de benzer SSS kısımlarını oluştur."
# Düzen LunaDream'le aynı: teslim çizgisinin hemen altında en fazla 4 ürün sorusu (kapalıyken hilal, açılınca dolunay); kalan ürün
# soruları alttaki "Merak edilenler"in başında, ardından satın alma soruları (kargo, iade, ödeme, garanti). Aynı soru iki yerde yok.
# Cevaplar ogrenme/urun-icerik.json'daki teyitli bilgiden ve kullanıcının teyitlerinden (TASARIM-BILGISI). Mağazadaki açılır sorular
# kullanılmadı: çoğu başka üründen kopya ("çocuğun odası, ninni" Galaksi Ambiyans'ta, "2400 mAh batarya" birkaç üründe).
# Bilinmeyen köşeli yer tutucu kalır. Pil süresi soran soru ("ne kadar gider") yok; şarj sorusu yalnız şarjlı mı / nasıl şarj olur.
import luna_e as E

URS_AY, URS_OK = E.URS_AY, E.URS_OK

# LunaDream'deki kartın aynısı; renkler sayfanın değişkenlerinden (ay ürünün vurgu renginde), yoksa LunaDream'in renkleri
URS_CSS = """
.urs{margin-top:12px;padding:2px 16px;border-radius:20px;background:var(--yuzey,#FFFDF9);border:1px solid var(--cizgi,#E3D8C7);text-align:left}
.urs-s+.urs-s{border-top:1px solid #EFE6D8;border-top-color:color-mix(in srgb,var(--cizgi,#E3D8C7) 60%,transparent)}
.urs-s summary{list-style:none;display:flex;align-items:center;gap:12px;min-height:48px;padding:6px 0;font-size:14px;font-weight:600;line-height:1.3;color:var(--lac,#1A2142);cursor:pointer;-webkit-tap-highlight-color:transparent}
.urs-s summary::-webkit-details-marker{display:none}
.urs-s summary:focus-visible{outline:2px solid var(--v2,#1A2142);outline-offset:2px;border-radius:8px}
.urs-ay{position:relative;flex:none;width:22px;height:22px}
.urs-ay .evre{position:absolute;inset:0;width:22px;height:22px;transition:opacity .35s cubic-bezier(.2,.7,.2,1)}
.urs-ay .evre circle{fill:var(--yuzey,#FFFDF9);stroke:var(--lac,#1A2142);stroke-width:1.4}
.urs-ay .evre path{fill:var(--v,#F2A65A)}
.urs-ay .dolu,.urs-s[open] .urs-ay .hilal{opacity:0}
.urs-s[open] .urs-ay .dolu{opacity:1}
.urs-q{flex:1;min-width:0}
.urs-ok{flex:none;width:18px;height:18px;fill:none;stroke:var(--soluk,#5C6078);stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;transition:transform .3s cubic-bezier(.2,.7,.2,1)}
.urs-s[open] .urs-ok{transform:rotate(180deg)}
.urs-s p{margin:0;padding:0 0 16px 34px;font-size:14px;line-height:1.55;color:var(--soluk,#5C6078)}
@media (prefers-reduced-motion:reduce){.urs-ay .evre,.urs-ok{transition:none}}
"""


def urs_html(sorular, stil=''):
    """Teslim çizgisinin altına konan soru kartı (statik <details>)."""
    return ('<div class="urs" role="group" aria-label="Ürün hakkında sorular"%s>' % (' style="%s"' % stil if stil else '') +
            ''.join('<details class="urs-s"><summary><span class="urs-ay" aria-hidden="true">%s</span><span class="urs-q">%s</span>%s</summary><p>%s</p></details>'
                    % (URS_AY, q, URS_OK, a) for q, a in sorular) + '</div>')


# handle → urs: teslim altı 4 soru; sss: alttaki SSS'de satın alma sorularından önce gelen ürün soruları
SORU = {
    'galayx-usb-projektor': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Tavana ve duvara ay, gezegen ve galaksi desenleri yansıtan masa üstü projektör. Gövdesi yumuşak ışıkla yandığı için gece lambası olarak da kullanılır: 2’si 1 arada.'),
             ('Nasıl çalışıyor?', 'USB’ye tak, film diskini yerleştir ve başlığı tavana ya da duvara çevir. Işığı kapatınca diskteki desen yansır.'),
             ('Prize mi takılır?', 'USB girişinden çalışır: laptop, powerbank ya da evdeki USB-A girişli telefon şarj başlığı yeter. Şarj başlığı (adaptör) kutuda yok.'),
             ('Kutu içeriğinde neler var?', '1 Galaxy USB projektör ve 12 film diski: 6’sı renkli, 6’sı beyaz desen.')]),
    'lamba': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Deniz feneri biçiminde gece lambası ve Bluetooth hoparlör, 2’si 1 arada. Fener ışığı sıcak sarı yanar, tepesinden duvara ay yansır.'),
             ('Duvara ay nasıl yansıyor?', 'Fenerin tepesindeki yansıtmayı açınca duvara ay görüntüsü düşer; kumandayla açıp kapatırsın. Oda karanlıkken ay belirginleşir.'),
             ('Bluetooth var mı, ne işe yarıyor?', 'Var. Telefonunu Bluetooth ile bağlarsın; çaldığın müzik gövdedeki hoparlörden gelir. Ayrıca dahili deniz sesi modu var.'),
             ('Kumandayla neler yapılır?', 'Işığı ve ay yansıtmayı yerinden kalkmadan yönetirsin. Kumanda kutudan çıkar.')],
        sss=['Kutudan ne çıkıyor?', 'Şarjlı mı?', 'Hareket sensörü var mı?', 'Ölçüleri nedir?']),
    'ayluna-galaksi-night-projektor': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Tavana ya da duvara gökyüzü ve uzay sahneleri yansıtan masa üstü projektör. Diski değiştirince sahne değişir; yansıyan görüntü yavaşça döner.'),
             ('Tavana mı duvara mı yansıtır?', 'İkisine de. Başlık eğilir; görüntüyü tavana ya da duvara çevirirsin. Oda ne kadar karanlıksa görüntü o kadar net olur.'),
             ('Şarjlı mı?', 'Hayır. USB-C kabloyla prize ya da bir USB çıkışına takılıyken çalışır; pil bitmesi derdi yok. USB adaptör kutuda mı [teyit].'),
             ('Diskler nasıl değişir?', 'Disk başlıktaki yuvaya elle takılıp çıkarılır, alet gerekmez.')],
        sss=['Kutudan ne çıkıyor?', 'Görüntü bulanık, ne yapmalıyım?']),
    'astronot-oda-nemlendirici-aroma-difuzor': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Odanın havasını nemlendiren, aroma difüzörü olarak da satılan astronot figürlü nemlendirici. Kapsülün içi sıcak sarı ışıkla aydınlanır.'),
             ('Nasıl çalışıyor?', 'Haznedeki suyu buhar olarak verir. Hazne hacmi ve buhar ayarı [teyit].'),
             ('Aroma için yağ konur mu?', 'Aroma difüzörü olarak satılıyor; hangi yağın, kaç damla kullanılacağı [teyit].'),
             ('Kutu içeriğinde neler var?', '[teyit]')],
        sss=['Prize mi takılır, şarjlı mı?', 'Hazne ne kadar su alır, kaç saat çalışır?']),
    'ayluna-retro-mini-pikap': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Pikap görünümlü Bluetooth hoparlör: telefondan müzik çalar, doğa sesleri verir. Ön yüzde dijital saat, plak yerinde ışıklı disk var.'),
             ('Plak çalar mı?', 'Hayır. Pikap görünümlü bir Bluetooth hoparlördür; plak takılmaz.'),
             ('Telefonsuz müzik çalar mı?', 'Evet, TF (microSD) karta yüklediğin müziği doğrudan çalar.'),
             ('Kutu içeriğinde neler var?', 'Hoparlör, USB şarj kablosu ve kullanım kılavuzu.')],
        ek=[('Hangi doğa sesleri var?', 'Dalga, kuş, ateş ve akarsu sesi; beyaz gürültü olarak da kullanılır.'),
            ('Alarm ve zamanlayıcı var mı?', 'Evet. Ön yüzdeki saatle alarm kurulur; zamanlayıcı ses ve ışığı belirlediğin sürede kapatır.'),
            ('Şarjlı mı?', 'Dahili pille çalışır, USB ile şarj edilir; şarjdayken de kullanılır. Tam şarjla kullanım süresi [teyit].')],
        sss=[]),
    'egitici-akilli-cizim-tahtasi': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Çocuğun çizgileri takip ederek resim çizdiği projeksiyonlu çizim masası. Sarı ya da pembe renkte.'),
             ('Nasıl çalışıyor?', 'Diski zürafanın başına takıp ışığı açarsın; resim masaya yansır, çocuk çizgileri kalemle takip eder. Çizim silinir, yeniden başlanır.'),
             ('Pil gerekiyor mu?', 'Pille çalışır. Pil tipi, adedi ve kutuda olup olmadığı [teyit].'),
             ('Kutu içeriğinde neler var?', 'Çizim masası, 3 projeksiyon diski, 12 renkli kalem, silgi ve temizleme bezi. Pil kutuda mı [teyit].')],
        ek=[('Kaç farklı resim var?', '3 projeksiyon diski var; disk değiştirince farklı resimler yansır. Toplam desen sayısı [teyit: 24].')],
        sss=['Kaç yaş için uygun?']),
    'dokunmatik-ambiyans-lamba': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Şarjlı ambiyans lambası: dokunarak ya da kumandayla açılır, 3 ışık rengi ve parlaklık ayarı var. Gövdedeki ekranda saat görünür.'),
             ('Kumandayla neler yapılır?', 'Açma-kapama, parlaklık ayarı ve 3 ışık rengi arasında geçiş.'),
             ('Nasıl şarj edilir?', 'Type-C kabloyla şarj edilir, dahili pille kablosuz çalışır. Şarj durumu gövdedeki ekranda görünür.'),
             ('Kutu içeriğinde neler var?', '[teyit: görsellerde lamba, kumanda ve Type-C kablo görünüyor]')],
        ek=[('Hangi ışık renkleri var?', 'Sıcak (gün batımı), doğal beyaz ve soğuk (gün ışığı).'),
            ('Kendiliğinden kapanır mı?', 'Evet, belirli süre sonra kendiliğinden kapanır. Süre seçenekleri [teyit].')],
        sss=['Ölçüleri nedir?']),
    'sunset-lamba': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Duvara ya da tavana gün batımı ışığı yansıtan lamba. Turuncudan maviye, mora ve gökkuşağına 16 renk arasında kumandayla geçersin.'),
             ('Nasıl kullanılır?', 'USB’ye tak, döner başlığı duvara ya da tavana çevir, rengi kumandadan seç. En iyi sonucu karanlık odada, düz bir duvara yansıtınca verir.'),
             ('Prize takılır mı?', None),
             ('Kutu içeriğinde neler var?', 'Lamba, USB kablo ve uzaktan kumanda. Kumanda pili ve USB adaptör [teyit].')],
        ek=[('Kumandayla neler yapılır?', 'Renk, parlaklık ve açma-kapama.')],
        sss=['Gövde rengi ne?']),
    'ayluna-cocuk-gece-feneri': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Çocuk odası için gece feneri: kubbesi yumuşak ışık verir, tema diskiyle duvara ve tavana dönen görüntü yansıtır.'),
             ('Yansıtma nasıl çalışır?', None),
             ('Şarjlı mı?', 'Evet, USB ile şarj edilip kablosuz kullanılır. Tam şarjla kullanım süresi [teyit].'),
             ('Kutu içeriğinde neler var?', 'Gece feneri, tema diskleri [teyit: 6 mı, 9 mu?], USB şarj kablosu ve kullanım kılavuzu.')],
        sss=['Bluetooth ya da hoparlör var mı?']),
    # 28 Eki: yeni ürün (kullanıcının kutu fotoğrafı, montaj kartı ve videosu; internette ürüne özel kaynak yok)
    'yilbasi-agaci-projektor-lamba': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Kendin süsleyip kurduğun minik bir yılbaşı ağacı lambası: USB’ye takınca tavana yılbaşı desenleri yansıtır.'),
             ('Nasıl kurulur?', None),
             ('Prize takılır mı?', 'USB ile çalışır: telefon şarj adaptörüne, powerbank’e ya da bilgisayara takılır. Pil yok; USB adaptör kutuda yok.'),
             ('Kutu içeriğinde neler var?', None)],
        sss=['Diski nasıl değiştiririm?', 'Çocuklar yapabilir mi?']),
    'galaksiambiyanisigi': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Tavana ve duvara yıldızlı nebula deseni yansıtan ambiyans ışığı; Bluetooth hoparlörüyle müzik de çalar.'),
             ('Kumandayla neler yapılır?', '14 renk arasında geçiş, desenin hareket hızı (4 kademe) ve açma-kapama.'),
             ('Bluetooth hoparlöre nasıl bağlanırım?', None),
             ('Kutu içeriğinde neler var?', 'Lamba, uzaktan kumanda, kablo ve kullanım kılavuzu.')],
        sss=['Şarjlı mı?']),
    'lunadream-gece-lambasi-v2': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Paletli robot gövdeli gece lambası: kubbe başlığı yumuşak ışık verir, tema diskiyle duvara ve tavana sahne yansıtır.'),
             ('Projeksiyon nasıl çalışıyor?', 'Tema diskini takıp yansıtmayı açarsın; diskteki sahne (doğum günü, deniz altı, yıldızlar) duvara ve tavana yansır.'),
             ('Kaç disk var?', None),
             ('Kutu içeriğinde neler var?', '[teyit: görselde robot projektör, uzay macerası diskleri ve kitapçık yazıyor; disk sayısı ve kablo belirsiz]')],
        sss=['Şarjlı mı, kabloyla mı çalışır?', 'Müzik çalar mı?']),
    'aroma-terapi-nemlendirici': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Odayı nemlendiren, suya uçucu yağ ekleyince koku veren ve LED ışıkla alev görüntüsü oluşturan nemlendirici.'),
             ('Gerçek ateş mi?', None),
             ('Kumandayla neler yapılır?', 'Işık, buhar ve zamanlayıcı yerinden kalkmadan ayarlanır. Alev rengi turuncu dışında mavi, mor, pembe, yeşil, sarı ve kırmızıya döner.'),
             ('Kutu içeriğinde neler var?', 'Nemlendirici, uzaktan kumanda, USB güç kablosu ve kullanım kılavuzu.')],
        ek=[('Uçucu yağ koyabilir miyim?', 'Evet, suya uçucu yağ eklenebilir. Uygun yağ ve miktar [teyit].')],
        sss=['Hazne ne kadar su alır, kaç saat çalışır?', 'Nasıl temizlenir?']),
    'yildiz-isigi-nemlendirici': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Suyu ince buhar olarak veren ultrasonik nemlendirici. Ön yüzde renkli ışık halkası var; yansıtma modunda tavana yıldız düşer.'),
             ('Yönü ayarlanır mı?', 'Evet. Gövde ayak üzerinde eğilir; buharı ve yansıtmayı istediğin yöne çevirirsin.'),
             ('Uçucu yağ koyabilir miyim?', None),
             ('Kutu içeriğinde neler var?', '[teyit]')],
        sss=['Hazne ne kadar su alır?', 'Şarjlı mı, kabloyla mı çalışır?']),
    'ask-saati': dict(
        urs=[('Bu ürün ne işe yarıyor?', 'Masa üstü kum sanatı lambası: cam çerçevedeki mavi kum akarak dağ manzarası çizer, LED taban ışığı çerçeveyi alttan aydınlatır.'),
             ('Işık nasıl açılır?', 'Tabandaki dokunmatik tuşla açılıp kapanır.'),
             ('Kum nasıl hareket eder?', None),
             ('Kutu içeriğinde neler var?', '[teyit]')],
        sss=['Şarjlı mı, kabloyla mı çalışır?', 'Çerçeve rengi ne?']),
}
# Sade sayfadaki AyFeneri ve Galaksi Night (özel sayfaların eşi) aynı soruları kullanır.


def sorular(icerik):
    """urun-icerik.json kaydından (handle, sss) → (urs 4 soru, alttaki SSS listesi). Cevabı None olan soru içerikteki cevabı alır."""
    h = icerik['handle']; d = SORU[h]
    c = dict((x['s'], x['c']) for x in icerik['sss'])
    urs = [(q, a if a is not None else c[q]) for q, a in d['urs']]
    satin = [(x['s'], x['c']) for x in icerik['sss'][:4]]  # kargo, iade, ödeme, garanti (her üründe aynı dört)
    sss = list(d.get('ek', []))
    for q in d.get('sss', []):
        sss.append((q, icerik['kutuda'] if q == 'Kutudan ne çıkıyor?' else c[q]))
    sss += satin
    uq = set(q for q, a in urs)
    assert not [q for q, a in sss if q in uq], h + ': aynı soru iki yerde'
    return urs, sss
