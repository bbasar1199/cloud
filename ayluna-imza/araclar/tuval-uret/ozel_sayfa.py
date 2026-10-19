# AyFeneri ve Galaksi Night Projektör · tam ürün sayfaları (18 Eki). Çalıştır: python3 ozel_sayfa.py
# Kullanıcı: "Galaksi Night için Yön A'yı kullanalım, AyLuna (AyFeneri) için de A; ama çıkarılabilir taban kısmını çıkart.
# 'Oda karanlık, duvarda ay' kısmını ayın tam göründüğü, düzgün çalışan hâle getir. İki ürün için de metin içeren görsel tarzı,
# ürünün nasıl göründüğünü gösteren oda vb. kısımlar oluştur." Sonra: "Görselleri Flow'dan üreteceksin, Higgsfield'dan üretme."
# Oda sahneleri ve yazısı silinmiş afişler bu turda (mesaj gelmeden) Higgsfield'da üretilmişti; kullanıcı "şimdilik kullan" dedi.
# Flow'dan gelenlerle aynı adla değiştirilecek (canvas/ozel/KAYNAK.md, ogrenme/flow-istemleri-ayfeneri-galaksi.md).
# Yön panoları (ozel_yon.py) arşivde kalır; çekirdek Galaxy USB'den (luna_usb.py).
# Eleştirmenden alınanlar (kullanıcının seçimiyle çelişmeyenler): fener göstergesi büyüdü ve yavaşladı, dolgu opaklıkla; netlik halkası
# filtre yerine iki görselin geçişi; AyFeneri'ne de alıcı fotoğrafları ve Loox satırı; A'nın ad/fiyat boyu küçüldü; 12px altı yazı yok.
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import TAIL, TL_JS, canli_galeri, urun_ust, masa_bayrak
import luna_e as E
import luna_usb_yon as Y
import luna_usb as U
import ozel_yon as O
CANVAS = os.path.join(HERE, '..', '..', 'canvas')
B = '/_blob/'
BL = json.load(open(os.path.join(CANVAS, 'ozel', 'bloblar.json')))
BA = json.load(open(os.path.join(CANVAS, 'ana', 'bloblar.json')))
ICERIK = dict((x['handle'], x) for x in json.load(open(os.path.join(HERE, '..', '..', 'ogrenme', 'urun-icerik.json'))))
I = lambda k: B + BL[k]

GAL = {
    'af': [('af-ay', 'Komodinde AyFeneri, arkadaki duvarda ay yansıması', '50% 40%'),
           ('af-kumanda', 'Yatak odasında AyFeneri, duvarda ay, masada kumanda', '55% 50%'),
           ('af-muzik', 'AyFeneri ve yanında müzik çalan telefon', '50% 50%'),
           ('af-kutu', 'AyFeneri ve kutusu', '40% 50%'),
           ('af-urun', 'AyFeneri gövdesi ve çıkarılabilir tabanı', '50% 40%')],
    'gn': [('gn-galaksi', 'Galaksi Night projektör, arkada galaksi görüntüsü', '50% 50%'),
           ('gn-huzme', 'Projektörden yukarı yayılan galaksi ışığı', '50% 50%'),
           ('gn-avuc', 'Avuçta Galaksi Night projektör', '78% 50%'),
           ('gn-salon', 'Salon duvarında galaksi yansıması', '72% 50%')],
}
# Oda sahneleri: yazı görselin içinde (Galaxy USB'nin "Bu gece tavanda ne olsun?" kartları gibi)
ODA = {
    'af': [('Yatak odasında', 'af-kumanda', 'Duvarda dolunay, elinde kumanda.', '30% 50%'),
           ('Uyku saatinde', 'af-uyku', 'Sıcak fener ışığı, kulakta deniz sesi.', '32% 50%'),
           ('Müzik zamanı', 'af-muzik', 'Telefonu bağla, fener çalsın.', '62% 50%'),
           ('Rafta, kitapların yanında', 'af-ay-orta', 'Işığı sönükken de süs.', '50% 30%')],
    'gn': [('Salonda', 'gn-salon', 'Film gecesi yerine duvarda galaksi.', '70% 50%'),
           ('Yatak odasında', 'gn-yatak', 'Bulutsu tavanda ağır ağır döner.', '50% 40%'),
           ('Çocuk odasında', 'gn-cocuk', 'Masaldan sonra tavanda dolunay.', '50% 40%'),
           ('Genç odasında', 'gn-genc', 'Kuzey ışığı tavanda, kurallar senin.', '50% 40%')],
}

CSS = r"""
/* Ad ve fiyat boyu (eleştirmen: A'da 40/36px büyüktü; kullanıcı daha önce "fiyat çok büyük" demişti) */
.al h1{font-size:34px}
.fiyat b{font-size:30px}
.loox{display:flex;align-items:center;gap:8px;margin:10px 0 0;font-size:13px;color:var(--soluk)}
.loox i{font-style:normal;letter-spacing:2px;color:var(--v2)}
.pk-g .x2{font-size:12px}
.alici i{font-size:12px}

/* AyFeneri göstergesi büyüdü (18×28), huzme 4 sn'de bir salınır, tepe ışığı opaklıkla yanar */
.f-iz{gap:16px}
.f-iz svg{width:18px;height:28px}
.f-iz .fn{fill:var(--v);opacity:0;transition:opacity .4s var(--ease)}
.f-iz .lit .fn{opacity:1;fill:var(--v)}
.f-iz .on .hz{animation-duration:4s}

/* Galaksi göstergesi: yörünge çizgisi hep görünür, gezegenler geçtikçe dolar, o anki gezegenin ayı döner */
.y-iz{gap:10px}
.y-iz svg{width:24px;height:24px}
.y-iz .yr{opacity:.45}
.y-iz .on .yr{opacity:1;stroke:var(--v)}

/* ===== Feneri yak (düzeltildi): sahnenin tamamı görünür (fener + ay); yazı ve anahtar alt şeritte.
   Kapalı: oda karanlık, fenerin tepesinde amber kor. Açık: ışık fenerden dairesel yayılır, duvarda ay belirir.
   Kendiliğinden: 2 sn kapalı → yanar, 7 sn açık kalır; dokununca durur. ===== */
.yak{position:relative;margin-top:20px;border-radius:22px;overflow:hidden;background:#0A0F1F;color:#fff;height:auto}
.yak::after{display:none}
.yak-g{position:relative;height:440px;overflow:hidden}
.yak-g img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:77% 50%}
.yak .k0{filter:brightness(.16) saturate(.4)}
.yak .k1{clip-path:circle(0% at 17% 39%);transition:clip-path 1.8s var(--ease) .15s}
.yak.on .k1{clip-path:circle(150% at 17% 39%)}
.yak .kor{left:17%;top:39%;width:16px;height:16px;margin:-8px 0 0 -8px}
.yak-g::after{content:"";position:absolute;left:0;right:0;bottom:0;height:90px;background:linear-gradient(180deg,rgba(10,15,31,0),#0A0F1F)}
/* Kapalıyken ay yok: duvarın karanlık tonuyla örtülür, fener yanınca örtü kalkar */
.ay-ort{position:absolute;left:74.6%;top:22.5%;width:200px;height:200px;margin:-100px 0 0 -100px;border-radius:50%;background:radial-gradient(circle,#070A12 50%,rgba(7,10,18,.6) 62%,rgba(7,10,18,0) 72%);transition:opacity .9s var(--ease) .9s}
.yak.on .ay-ort{opacity:0}
.yak .k0{filter:brightness(.11) saturate(.35)}
.ay-hale{position:absolute;left:74.6%;top:22.5%;width:190px;height:190px;margin:-95px 0 0 -95px;border-radius:50%;background:radial-gradient(circle,rgba(230,236,255,.28) 0,rgba(230,236,255,0) 68%);opacity:0;transition:opacity 1s var(--ease) 1.2s}
.yak.on .ay-hale{opacity:1;animation:hale 4s ease-in-out 2.2s infinite alternate}
.yak-alt{position:relative;left:auto;right:auto;bottom:auto;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:4px 18px 20px}
.yak-alt .bas-y{font-size:32px;line-height:.95;color:#fff;margin:0}
.yak-alt .bas-y span{display:block;transition:color .6s var(--ease)}
.yak.on .yak-alt .bas-y span:last-child{color:var(--v)}
.yak-alt small{display:block;margin-top:6px;font-size:13px;color:#C9D0E2}

/* ===== Oda sahneleri: yazı görselin içinde; fotoğraflar yavaşça süzülür ===== */
.oda-serit{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:16px;padding:18px 16px 0}
.oda-k{position:relative;flex:0 0 280px;height:400px;border-radius:18px;overflow:hidden;scroll-snap-align:start;background:#000;color:#fff}
.oda-k img{position:absolute;inset:-4%;width:108%;height:108%;object-fit:cover;animation:suz 16s ease-in-out infinite alternate}
.oda-k:nth-child(2) img{animation-delay:-4s}.oda-k:nth-child(3) img{animation-delay:-8s}.oda-k:nth-child(4) img{animation-delay:-12s}
.oda-k::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,15,31,.5) 0,rgba(10,15,31,0) 26%,rgba(10,15,31,0) 54%,rgba(10,15,31,.9) 100%)}
.oda-k small{position:absolute;left:16px;top:14px;z-index:1;padding:3px 10px;border-radius:999px;background:rgba(10,15,31,.6);font-size:12px;font-weight:700;color:var(--v)}
.oda-k b{position:absolute;left:16px;right:16px;bottom:40px;z-index:1;font-family:var(--fb);font-weight:var(--bk);font-size:30px;letter-spacing:var(--bls);line-height:.95}
.oda-k span{position:absolute;left:16px;right:16px;bottom:14px;z-index:1;font-size:14px;color:#D5DBEA}

/* ===== Büyük görsel kart (hediye / avucuna sığar): yazı görselin içinde ===== */
.buyuk{position:relative;height:460px;border-radius:22px;overflow:hidden;background:#000;color:#fff}
.buyuk img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.buyuk.on img{animation:kb 9s linear infinite alternate}
.buyuk::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,15,31,0) 40%,rgba(10,15,31,.88) 100%)}
.buyuk.acik::after{background:linear-gradient(180deg,rgba(26,33,66,0) 45%,rgba(26,33,66,.86) 100%)}
.buyuk-y{position:absolute;left:18px;right:18px;bottom:18px;z-index:1}
.buyuk-y .bas-y{font-size:36px;line-height:.95;color:#fff}
.buyuk-y p{margin:8px 0 0;font-size:15px;color:#E3E7F2}

/* Netlik halkası: bulanık ve net iki görselin opaklık geçişi (filtre animasyonu yok) */
.net-g img{animation:none}
.net-g .nt{animation:netgec 5s var(--ease) infinite}
@keyframes netgec{0%,12%{opacity:0}55%,90%{opacity:1}100%{opacity:0}}
.net span>span{font-size:14px}
"""

FENER_SVG = ('<svg class="{{f.dcls}}" viewBox="0 0 14 22"><path class="hz" d="M8 6.5 L22 2 L22 11 Z"></path><path d="M4 5 L7 2 L10 5 Z"></path>'
             '<rect x="4.5" y="5" width="5" height="3"></rect><rect class="fn" x="4.5" y="5" width="5" height="3"></rect><path d="M4.5 8 H9.5 L10.5 20 H3.5 Z"></path><path d="M2 20.5 H12"></path></svg>')

BASLIK = {'af': ('<span><i>Duvarına</i></span><span><i><em>ay</em> doğsun.</i></span>', 'Deniz feneri biçiminde gece lambası: duvara ay yansıtır, müzik çalar.'),
          'gn': ('<span><i>Tavanın</i></span><span><i>gökyüzü <em>olsun.</em></i></span>', 'Diski seç, ışığı kapat; galaksi yavaşça dönsün.')}
AD = {'af': 'Ayluna AyFeneri', 'gn': 'Ayluna Galaksi Night Projektör'}


def hero(u):
    gost = '<span class="d-iz" aria-hidden="true"><sc-for list="{{gal}}" as="f" hint-placeholder-count="5"><i class="{{f.dcls}}"></i></sc-for></span>'  # galeri çizgisi (luna_usb CSS)
    return ("""
  <!-- Galeri: kaydırılır, 5 sn'de kendiliğinden geçer (kaydırınca durur); başlık yalnız ilk fotoğrafta; küçük resim ve sayı yok -->
  <section class="hero kare" aria-label="%s fotoğrafları">
    <div class="h-iz noscroll" onScroll="{{gKay}}"><sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><div class="{{f.cls}}"><img src="{{f.src}}" alt="{{f.n}}" style="object-position: {{f.pos}}"></div></sc-for></div>
    %s
    <div class="h-alt">%s<span style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%%); white-space: nowrap" aria-live="polite">Fotoğraf {{gNo}} / {{gCount}}</span></div>
  </section>
""" % (AD[u], Y.ust('rgba(238,242,250,.6)'), gost))


def ozler(u):
    if u == 'af':
        # Çıkarılabilir taban kutusu çıkarıldı (kullanıcı, 18 Eki)
        return ('<div class="ozler dort">'
                '<div class="oz">' + O.mini(O.AY_IK) + '<b>Duvara ay</b><span class="t">Fenerin tepesinden ay yansır.</span></div>'
                '<div class="oz">' + O.mini(O.ESIT) + '<b>Bluetooth hoparlör</b><span class="t">Telefondan müzik çal.</span></div>'
                '<div class="oz">' + O.mini(O.DALGA) + '<b>Deniz sesi</b><span class="t">Dahili deniz sesi modu.</span></div>'
                '<div class="oz">' + O.mini(O.KUMANDA) + '<b>Kumanda dahil</b><span class="t">Işığı uzaktan yönet.</span></div></div>')
    return O.ozler('gn')


def al(u):
    d = O.URUN[u]
    pct = round((1 - d['P1'] / d['C1']) * 100)
    alt = '2\'si 1 arada: gece lambası ve Bluetooth hoparlör.' if u == 'af' else 'Masa üstü galaksi projektörü, değiştirilebilir disklerle.'
    kutu = ('<p class="kutu-not"><span>Kutuda: AyFeneri + kumanda. USB kablo [teyit]</span></p>' if u == 'af' else
            '<p class="kutu-not">' + O.gdisk_yigin() + '<span>Kutuda [12] tema diski + USB-C kablo</span></p>')
    pk = 'af-ay-yakin' if u == 'af' else 'gn-isik'
    return ("""
  <section class="al" id="siparis">
    <h1 class="bas-y">%s</h1>
    <p class="alt-b">%s</p>
    <!-- Loox yıldızı: puan ve sayı uygulamadan otomatik (AyFeneri 43 yorum, Galaksi Night 6 yorum; 18 Eki) -->
    <p class="loox"><i aria-hidden="true">★★★★★</i><span>[Loox: puan · yorum sayısı otomatik]</span></p>
    <p class="fiyat" aria-label="%s, önceki fiyat %s, %%%d indirim"><b aria-hidden="true">%s</b><s aria-hidden="true">%s</s><span class="rozet" aria-hidden="true">%%%d indirim</span></p>
    %s%s
    <div class="pk-bas">Çok al, az öde</div>
    <div class="pk"><sc-for list="{{paket}}" as="b" hint-placeholder-count="2">
      <button class="{{b.cls}}" onClick="{{b.pick}}" aria-pressed="{{b.on}}"><sc-if value="{{b.rib}}" hint-placeholder-val="{{false}}"><span class="kurdele">En avantajlı</span></sc-if><span class="pk-g"><img src="%s" alt=""><sc-if value="{{b.two}}" hint-placeholder-val="{{false}}"><span class="x2">×2</span></sc-if></span><span class="pk-o"><b>{{b.t}}</b><span>{{b.sub}}</span></span><span class="pk-s"><b>{{b.p}}</b><sc-if value="{{b.hasOld}}" hint-placeholder-val="{{true}}"><s>{{b.old}}</s></sc-if><span>{{b.unit}}</span></span><span class="nokta"><i></i></span></button>
    </sc-for></div>
    %s
    <!-- Stok ELLE girilir (bölüm ayarı: sayı + aç/kapa); boşsa satır gizlenir -->
    <p class="stok"><span class="ping" aria-hidden="true"></span><span>Stokta son <b>[N]</b> adet</span></p>
    <button class="btn1" type="button"><span class="b-ic"><span>{{onLabel}}</span><small>Kartla %%5 indirim dahil</small></span>%s</button>
    <button class="btn2" type="button">Kapıda Ödeme ile Sipariş Ver</button>
    <div class="ay-dis" data-ay-dis></div>
    <ol class="yol" aria-label="Siparişten teslime"><span class="yol-iz" aria-hidden="true"><i></i><i></i><em></em></span><li class="y1"><span class="yd"></span><b>Bugün</b><span>Sipariş verildi</span></li><li class="y2"><span class="yd"></span><b>{{kargo}}</b><span>Kargoda</span></li><li class="y3"><span class="yd"></span><b>{{teslim}}</b><span>Kapında</span></li></ol>
  </section>
""" % (AD[u], alt, O.tl(d['P1']), O.tl(d['C1']), pct, O.tl(d['P1']), O.tl(d['C1']), pct, ozler(u), O.ALICI, I(pk), kutu, U.OK))


def odalar(u, bas, alt):
    # Kartta büyük başlık = oda, alt satır = o odadaki an; ikisi de görselin içinde
    kart = ''.join('<div class="oda-k"><img src="%s" alt="%s: %s" style="object-position: %s"><b>%s</b><span>%s</span></div>'
                   % (I(k), n, t, pos, n, t) for n, k, t, pos in ODA[u])
    return ('\n  <section class="koyu bolum" style="padding-bottom: 36px" id="odalar"><div class="px"><h2 class="bas-y h2">%s</h2><p class="alt-b">%s</p></div>'
            '<div class="oda-serit noscroll">%s<span aria-hidden="true" style="flex: 0 0 6px"></span></div>'
            '</section>\n' % (bas, alt, kart))


FENERI_YAK = """
  <!-- Feneri yak (düzeltildi, kullanıcı 18 Eki: "ayın tam göründüğü, düzgün çalışan hâle getir"): sahnenin tamamı kırpılmadan görünür;
       yazı ve anahtar alt şeritte, görselin üstünde değil. Kapalıyken oda karanlık; açınca ışık fenerin tepesinden yayılır, duvarda ay belirir. -->
  <section class="bolum px">
    <div class="{{yakCls}}" style="margin-top: 0">
      <div class="yak-g">
        <img class="k0" src="@@af-gece@@" alt="">
        <img class="k1" src="@@af-gece@@" alt="Yanan AyFeneri, karşı duvarda dolunay yansıması">
        <span class="ay-ort" aria-hidden="true"></span>
        <span class="ay-hale" aria-hidden="true"></span>
        <span class="kor" aria-hidden="true"></span>
      </div>
      <div class="yak-alt"><div><p class="bas-y"><span>Oda karanlık.</span><span>{{yakYazi}}</span></p><small>Tek dokunuş: fener yanar, duvara ay düşer.</small></div>
        <button class="anahtar" type="button" role="switch" aria-checked="{{yakOn}}" onClick="{{yakSw}}"><b>{{yakEt}}</b><i></i></button></div>
    </div>
  </section>
"""

HUZME = """
  <!-- Fener huzmesi: huzme sırayla dört işe döner (3 sn), dokununca o işte durur -->
  <section class="bolum px" style="padding-top: 0">
    <h2 class="bas-y h2">Bir fener,<br>dört iş<span class="n">.</span></h2>
    <ul class="{{hzCls}}">
      """ + O.FENER_BUYUK + """<span class="hzm-h" aria-hidden="true"></span>
      <sc-for list="{{hz}}" as="h" hint-placeholder-count="4"><li class="{{h.cls}}"><b>{{h.n}}</b><span>{{h.t}}</span><button type="button" onClick="{{h.pick}}" aria-label="{{h.n}}" aria-pressed="{{h.on}}"></button></li></sc-for>
    </ul>
  </section>
"""

HEDIYE = """
  <!-- Hediye: yazı görselin içinde. Hediye paketi sunulmuyor; yalnız kutunun kendisi. -->
  <section class="px">
    <div class="buyuk acik on"><img src="@@af-kutu@@" alt="AyFeneri ve kutusu" style="object-position: 30% 50%"><div class="buyuk-y"><p class="bas-y">Kutusu hazır,<br>hediyesi hazır.</p><p>Annene, torununa, kendine. Kutuda fener ve kumanda.</p></div></div>
  </section>
"""

AVUC = """
  <!-- Avucuna sığar: yazı görselin içinde; ölçü teyit bekliyor -->
  <section class="px">
    <div class="buyuk acik on"><img src="@@gn-avuc@@" alt="Avuçta Galaksi Night projektör" style="object-position: 74% 50%"><div class="buyuk-y"><p class="bas-y">Avucuna<br>sığar.</p><p>Masa üstü boy [15 × 9 cm teyit]. USB-C kabloyla prize ya da USB'ye takılır.</p></div></div>
  </section>
"""

DONEN_GOK = """
  <!-- Tavanda dönen gök: seçilen disk yavaşça döner (70 sn'de bir tur). 4 sn'de kendiliğinden gezer, dokununca durur. -->
  <section class="koyu bolum" id="diskler">
    <div class="px"><h2 class="bas-y h2">Tavanında<br>dönen gök<span class="n">.</span></h2><p class="alt-b">Bir diske dokun, tavanda yavaşça dönsün.</p></div>
    <div class="kb-s" aria-hidden="true">
      <div class="kubbe"><div class="kubbe-d"><sc-for list="{{disk}}" as="d" hint-placeholder-count="2"><img class="{{d.cls}}" src="{{d.src}}" alt=""></sc-for></div></div>
      <span class="kb-isik"></span>
      <span class="kb-ad"><svg viewBox="0 0 24 24"><path d="M20 12a8 8 0 1 1-2.3-5.6"></path><path d="M20 4v4h-4"></path></svg><b>{{dAd}}</b></span>
    </div>
    <div class="px"><div class="kb-iz"><sc-for list="{{disk}}" as="d" hint-placeholder-count="12"><button class="{{d.bcls}}" type="button" onClick="{{d.pick}}" aria-label="{{d.n}}" aria-pressed="{{d.on}}"><img src="{{d.src}}" alt=""></button></sc-for></div>
    <p class="alt-not">Disk görselleri mağaza afişinden. Kutudaki disk sayısı [teyit: 12 mi, Ay diskiyle 13 mü]. Tavanda daha yumuşak görünür.</p></div>
  </section>
  <section class="bolum px">
    <h2 class="bas-y h2">Bulanıksa,<br>halkayı çevir<span class="n">.</span></h2>
    <div class="net"><span class="net-g" aria-hidden="true"><img src="@@gn-d03-bulanik@@" alt=""><img class="nt" src="@@gn-d03-sarmal-galaksi@@" alt=""><svg viewBox="0 0 150 150"><circle cx="75" cy="75" r="70" style="stroke-dasharray: 2 6"></circle><path d="M75 1v10M149 75h-10M75 149v-10M1 75h10"></path></svg></span>
      <span><b>Keskinleşir.</b><span>Netlik halkasını yavaşça çevir; oda karardıkça görüntü belirginleşir.</span></span></div>
  </section>
"""

KURULUM_GN = ("""
  <section class="bolum px" id="kurulum" style="padding-top: 0">
    <h2 class="bas-y h2">Üç adımda<br>tavanda<span class="n">.</span></h2>
    <ol class="kur">
      <li><em>1</em><span><b>USB-C kabloyu tak</b><span>Prize ya da bir USB çıkışına. Şarjlı değil; takılıyken çalışır.</span></span></li>
      <li><em>2</em><span><b>Diski yuvaya yerleştir</b><span>Elle takılıp çıkar, alet gerekmez.</span></span></li>
      <li><em>3</em><span><b>Başlığı çevir, halkayı ayarla</b><span>Tavana ya da duvara çevir; netlik halkasını yavaşça döndür.</span></span></li>
    </ol>
  </section>
""")


def gerisi(u):
    kapanis = 'Bu gece duvarında <br>ay olsun' if u == 'af' else 'Bu gece tavanın <br>gökyüzü olsun'
    karo = 'af-ay-yakin' if u == 'af' else 'gn-isik'
    return ("""
  <section class="bolum px">
    <h2 class="bas-y h2">İçin rahat<br>olsun<span class="n">.</span></h2>
    """ + U.GUVEN + """
  </section>

  <!-- Yorumlar: yalnız bu ürünün Loox yorumları, hepsi (m.28/B); olumsuzlar da görünür. Afişteki uydurma yorum kartları yok. -->
  <section class="px" id="yorumlar" style="padding-bottom: 44px">
    <h2 class="bas-y h2">Alanlar ne<br>diyor<span class="n">?</span></h2>
    <p class="yer">[Loox: bu ürünün tüm yorumları, fotoğraflı olanlar başta; puan dağılımı ve sayı otomatik]</p>
  </section>

  <section class="px">
    <div class="otuz"><span class="ot-h" aria-hidden="true">""" + U.OTUZ + """<b>30</b><small>gün</small></span><span><b>Beğenmezsen iade et</b><span>Yasal 14 günü 30 güne uzattık. İade kargosu ücretsiz.</span></span></div>
  </section>

  <section class="bolum px" id="sss">
    <h2 class="bas-y h2">Merak<br>edilenler<span class="n">.</span></h2>
    <div style="margin-top: 14px; border-top: 1px solid var(--cizgi)">
      <sc-for list="{{faq}}" as="f" hint-placeholder-count="6"><details class="sss"><summary>{{f.q}}<span class="arti" aria-hidden="true">+</span></summary><p>{{f.a}}</p></details></sc-for>
    </div>
  </section>

  <section>
    <div class="px" style="display: flex; align-items: flex-end; justify-content: space-between"><h2 class="bas-y" style="font-size: 26px">Odanın geri<br>kalanı için<span class="n">.</span></h2><span style="font-size: 13px; color: var(--soluk)">{{shopCount}} ürün</span></div>
    <div class="noscroll" style="display: flex; gap: 10px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-left: 16px; padding: 16px 16px 4px">
      <sc-for list="{{shop}}" as="u" hint-placeholder-count="4"><a class="kart" href="#"><span><img src="{{u.src}}" alt="{{u.n}}"><sc-if value="{{u.pct}}" hint-placeholder-val="{{true}}"><i>{{u.pct}}</i></sc-if></span><span><b>{{u.n}}</b><span style="display: flex; align-items: baseline; gap: 6px; font-variant-numeric: tabular-nums"><b style="min-height: 0">{{u.price}}</b><s style="font-size: 12px; color: var(--soluk)">{{u.old}}</s></span></span></a></sc-for>
    </div>
  </section>

  <footer class="alt-bilgi">
    <div class="px">
      <h2 class="bas-y" style="font-size: 34px; color: #fff">""" + kapanis + """<span class="n" style="color: var(--v)">.</span></h2>
      <button class="btn1 btn-b" type="button" style="margin-top: 18px"><span class="b-ic"><span>{{onLabel}}</span><small style="color: var(--koyu)">Kartla %5 indirim dahil</small></span>""" + U.OK + """</button>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0 16px; margin-top: 24px; font-size: 14px"><a href="#">Mesafeli Satış Sözleşmesi</a><a href="#">KVKK</a><a href="#">İade Politikası</a><a href="#">İletişim</a></div>
      <div aria-label="Ayluna" style="margin-top: 24px; display: flex; align-items: center; gap: 12px; color: #fff">""" + E.isaret(48) + """<span aria-hidden="true" style="font-family: 'Young Serif', Georgia, serif; font-size: 56px; line-height: .8; letter-spacing: -.045em">Ayluna</span></div>
      <p style="margin: 14px 0 0; padding-top: 14px; border-top: 1px solid rgba(238,242,250,.12); font-size: 12px">Fiyatlara KDV dahildir. © 2026 Ayluna</p>
    </div>
  </footer>

  <!-- Yapışkan çubuk: fiyat ve buton; sayaç yalnız üst şeritte (tek sayaç) -->
  <div class="yapis">
    <span class="karo"><img src="@@""" + karo + """@@" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; margin: 0"></span>
    <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; line-height: 1.25; color: #fff; font-variant-numeric: tabular-nums"><b style="font-size: 17px">{{onPrice}}</b><span style="font-size: 13px; color: var(--acik)">{{adetName}} · kartla %5 dahil</span></span>
    <button class="btn1 btn-b" type="button" onClick="{{alaGit}}" style="flex: 0 0 140px; width: 140px; min-height: 52px; margin: 0">Satın al</button>
  </div>
""")


def govde(u):
    if u == 'af':
        orta = (FENERI_YAK + odalar('af', 'Hangi odada<br>nasıl durur<span class="n">?</span>', 'Komodinde, rafta, çocuk odasında: fener her yere yakışır.') +
                HUZME + HEDIYE)
    else:
        orta = (odalar('gn', 'Hangi odada<br>nasıl görünür<span class="n">?</span>', 'Salonda duvara, yatak odasında tavana: diski seç, ışığı kapat.') +
                DONEN_GOK + AVUC + '<div style="height: 44px"></div>' + KURULUM_GN)
    h = '<div class="pg">\n  ' + U.SERIT + hero(u) + al(u) + orta + gerisi(u) + '</div>\n'
    return re.sub(r'@@([\w-]+)@@', lambda m: I(m.group(1)), h)


def faq(u):
    c = ICERIK['lamba' if u == 'af' else 'ayluna-galaksi-night-projektor']
    ilk = [{'q': 'Kutudan ne çıkıyor?', 'a': c['kutuda']}]
    return ilk + [{'q': x['s'], 'a': x['c']} for x in c['sss']]


def js(u):
    d = O.URUN[u]
    # Galeri Shopify'daki gibi (kullanıcı, 19 Eki): canlı mağazanın görselleri, aynı sıra, kare (ogrenme/galeri-canli.json)
    gal = [[B + i, '%s görseli %d' % (AD[u], k + 1), '50% 50%'] for k, i in enumerate(canli_galeri({'af': 'lamba', 'gn': 'ayluna-galaksi-night-projektor'}[u]))]
    hz = [['Duvara ay', 'Fenerin tepesinden ay yansır.'], ['Müzik çalar', 'Bluetooth ile telefondan.'], ['Deniz sesi', 'Dahili ses modu.'], ['Kumandalı', 'Işığı ve modu uzaktan seç.']]
    disk = [[n, I(k)] for n, k in O.GDISK]
    kendi = 'lamba' if u == 'af' else 'ayluna-galaksi-night-projektor'
    PR = [('lunadream-gece-lambasi', 'LunaDream Gece Lambası', 1699.99, 1999), ('galayx-usb-projektor', 'Galaxy USB Projektör', 1599, 1999),
          ('lamba', 'Ayluna AyFeneri', 1649.99, 2499), ('ayluna-galaksi-night-projektor', 'Ayluna Galaksi Night Projektör', 2199, 2999),
          ('galaksiambiyanisigi', 'Galaksi Ambiyans Işığı', 1499, 2898), ('yildiz-isigi-nemlendirici', 'Yıldız Işığı Nemlendirici', 849.99, 1099),
          ('ask-saati', 'Ayluna Kum Saati Lamba', 799, 999)]
    shop = [[n, p, c, B + BA['u-%s.jpg' % h]] for h, n, p, c in PR if h != kendi]
    return """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { g: 0, gOto: true, adet: null, yak: false, yOto: true, yBas: 0, hz: 0, hOto: true, disk: 2, dOto: true, t: 0, now: Date.now() }; }
  componentDidMount() {
    var self = this;
    // Hareket azaltılmışsa fener, huzme ve disk durur; galeri yine 5 sn'de geçer ama kaymadan, anında (galGit)
    if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) this.setState({ yOto: false, hOto: false, dOto: false, yak: true });
    // Tek saat: sayaç, galeri (5 sn), fener (2 sn kapalı → 7 sn açık), huzme (3 sn), disk (4 sn)
    this.iv = setInterval(function () {
      var S = self.state, t = S.t + 1, o = { now: Date.now(), t: t };
      if (S.gOto && t % 5 === 0) self.galGit((S.g + 1) % """ + str(len(gal)) + """);
      if (S.yOto && t - S.yBas >= (S.yak ? 7 : 2)) { o.yak = !S.yak; o.yBas = t; }
      if (S.hOto && t % 3 === 0) o.hz = (S.hz + 1) % 4;
      if (S.dOto && t % 4 === 0) o.disk = (S.disk + 1) % 12;
      self.setState(o);
    }, 1000);
  }
  galGit(i) { var el = document.querySelector('.h-iz'); if (el && el.scrollTo && el.clientWidth) { this.otoKay = Date.now(); el.scrollTo({ left: i * el.clientWidth, behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); } else this.setState({ g: i }); }
  componentDidUpdate() { var el = document.querySelector('.h-iz'); if (el && el.clientWidth && Math.abs(el.scrollLeft - this.state.g * el.clientWidth) > el.clientWidth / 2) { this.otoKay = Date.now(); el.scrollLeft = this.state.g * el.clientWidth; } }
  componentWillUnmount() { clearInterval(this.iv); }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    """ + TL_JS + """
    var GAL = """ + json.dumps(gal, ensure_ascii=False) + """;
    var gal = GAL.map(function (g, i) { var on = i === S.g; return { src: g[0], n: g[1], pos: g[2], ilk: i === 0, cls: 'hs' + (on ? ' on' : ''), dcls: i < S.g ? 'lit' : (on ? 'lit on' : '') }; });
    function gKay(e) { var el = e && (e.currentTarget || e.target); if (!el || !el.clientWidth) return; var i = Math.round(el.scrollLeft / el.clientWidth), o = {};
      if (i !== self.state.g) o.g = i; if (self.state.gOto && Date.now() - (self.otoKay || 0) > 900) o.gOto = false; if (o.g !== undefined || o.gOto === false) self.setState(o); }
    var P1 = """ + str(d['P1']) + """, C1 = """ + str(d['C1']) + """, P2 = """ + str(d['P2']) + """;
    var paket = [
      { n: 1, t: '1 Adet', p: TL(P1, true), old: TL(C1, true), unit: '', sub: '%' + Math.round((1 - P1 / C1) * 100) + ' indirim', rib: false },
      { n: 2, t: '2 Adet', p: TL(P2, true), old: '', unit: 'tanesi ' + TL(Math.floor(P2 / 2 * 100) / 100, true), sub: '2 ayrı almaya göre ' + TL(Math.round((2 * P1 - P2) * 100) / 100, true) + ' daha az', rib: true }
    ].map(function (b) { var on = S.adet === b.n; return { t: b.t, p: b.p, old: b.old, hasOld: !!b.old, unit: b.unit, sub: b.sub, rib: b.rib, two: b.n === 2,
      on: on ? 'true' : 'false', cls: on ? 'pk-k on' : 'pk-k', pick: function () { self.setState({ adet: b.n }); } }; });
    var total = S.adet === 2 ? P2 : P1, online = Math.round(total * 0.95 * 100) / 100, onPrice = TL(online, true);
    var HZ = """ + json.dumps(hz, ensure_ascii=False) + """;
    var hz = HZ.map(function (h, i) { var on = i === S.hz; return { n: h[0], t: h[1], cls: on ? 'on' : '', on: on ? 'true' : 'false', pick: function () { self.setState({ hz: i, hOto: false }); } }; });
    var DISK = """ + json.dumps(disk, ensure_ascii=False) + """;
    var disk = DISK.map(function (d, i) { var on = i === S.disk; return { n: d[0], src: d[1], on: on ? 'true' : 'false', cls: on ? 'on' : '', bcls: on ? 'on' : '', pick: function () { self.setState({ disk: i, dOto: false }); } }; });
    var AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
    var now = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kd = new Date(now); do { kd.setDate(kd.getDate() + 1); } while (kd.getDay() === 0 || kd.getDay() === 6);
    var t1 = new Date(kd); t1.setDate(t1.getDate() + 3); var t2 = new Date(kd); t2.setDate(t2.getDate() + 7);
    var teslim = t1.getMonth() === t2.getMonth() ? t1.getDate() + '–' + t2.getDate() + ' ' + AY[t2.getMonth()] : t1.getDate() + ' ' + AY[t1.getMonth()] + '–' + t2.getDate() + ' ' + AY[t2.getMonth()];
    function IKI(n) { return n < 10 ? '0' + n : String(n); }
    var ist = new Date(new Date(S.now || Date.now()).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kalan = Math.max(0, new Date(ist.getFullYear(), ist.getMonth(), ist.getDate(), 23, 59, 59, 999).getTime() - ist.getTime());
    var hh = Math.floor(kalan / 3600000), mi = Math.floor(kalan / 60000) % 60, ss = Math.floor(kalan / 1000) % 60;
    function alaGit() { var h = document.getElementById('siparis'); if (h && h.scrollIntoView) h.scrollIntoView({ behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' }); }
    var PR = """ + json.dumps(shop, ensure_ascii=False) + """;
    var shop = PR.map(function (x) { var d = x[2] > x[1]; return { n: x[0], src: x[3], price: TL(x[1], true), old: d ? TL(x[2], true) : '', pct: d ? '%' + Math.round((1 - x[1] / x[2]) * 100) : '' }; });
    return {
      gal: gal, gNo: S.g + 1, gCount: GAL.length, gKay: gKay, paket: paket, adetName: S.adet === 2 ? '2 Adet' : '1 Adet',
      onLabel: 'Güvenli Ödeme ile Al', onPrice: onPrice,  // düğmede fiyat yok (kullanıcı, 19 Eki)
      kargo: kd.getDate() + ' ' + AY[kd.getMonth()], teslim: teslim,
      hh: IKI(hh), mm: IKI(mi), ss: IKI(ss), snCls: ss % 2 ? 'sn tA' : 'sn tB', cdAria: 'Bugüne özel fiyatın bitmesine ' + hh + ' saat ' + mi + ' dakika',
      yakCls: S.yak ? 'yak on' : 'yak', yakOn: S.yak ? 'true' : 'false', yakEt: S.yak ? 'Açık' : 'Kapalı', yakYazi: S.yak ? 'Duvarda ay.' : 'Feneri yak.',
      yakSw: function () { self.setState({ yak: !self.state.yak, yOto: false }); },
      hz: hz, hzCls: 'hzm k' + S.hz, disk: disk, dAd: DISK[S.disk][0],
      alaGit: alaGit, faq: """ + json.dumps(faq(u), ensure_ascii=False) + """, shop: shop, shopCount: PR.length
    };
  }
}"""


DOSYA = {'af': ('AyFeneri.dc.html', 'af-a'), 'gn': ('GalaksiNight.dc.html', 'gn-a')}


def sayfa(u):
    dosya, yon = DOSYA[u]
    t = O.YON[yon]
    css = O.tema_css(dict(t, ek='')) + U.CSS + O.CSS + t.get('ek', '') + '\n' + CSS
    return U.head(AD[u], css, t['font']) + govde(u)


if __name__ == '__main__':
    for u, (dosya, yon) in DOSYA.items():
        h = int(os.environ.get('S_H_' + u, {'af': 6596, 'gn': 7108}[u]))  # ölçülen pano boyu (19 Eki, kare galeri)
        open(os.path.join(CANVAS, dosya), 'w', encoding='utf-8').write(urun_ust(sayfa(u), '<section class="hero kare"', ozler(u)) + TAIL.format(h=h, js=masa_bayrak(js(u))))
        print('yazıldı:', dosya, h)
