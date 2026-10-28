# Yılbaşı Ağacı Projektör Lamba · imza ürün sayfası (28 Eki). Çalıştır: python3 yilbasi_sayfa.py
# Kullanıcı: "LunaDream için yaptığımız gibi profesyonel ve satışa hazır bir site yap." Üç yön (onizleme/yilbasi-yon) → eleştirmen
# birleşimi: Main sistemi (beyaz zemin, lacivert, amber; Young Serif + Onest), A'nın "Kutuda ne var?" noktalı fotoğrafı,
# B'nin disk seçicisi yalnız bir gece bandında, C'nin "Yaparken / Yanınca" ikilisi, 3 adımda kurulum.
# Satın alma çekirdeği AyFeneri / Galaksi Night ile aynı (ozel_sayfa.py): galeri, ad + fiyat, özellikler, paket, stok (elle), Güvenli Ödeme,
# EasySell yeri, teslim çizgisi, 4 soru, SSS, 30 gün iade, mesajlar, öneri şeridi, alt bilgi, yapışkan çubuk.
# Gerçek aciliyet: yılbaşından önce teslim için son sipariş günü (1 iş gününde kargo + en geç 7 gün; 31 Aralık'tan geriye). Sahte sayaç yok.
# Teyitsiz: fiyat (geçici; canlıda Shopify), disk sayısı (afişte "6+"), parça sayısı. Yorum yok (yeni ürün): Loox yıldız satırı ve yorum bölümü konmadı.
# Görseller: kullanıcının kutu fotoğrafı ve montaj videosu kareleri; tavan ve disk görselleri satıcı afişinin yazısız kısmı (canvas/ozel/yb-*).
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import UST_CSS, TAIL, TL_JS, canli_galeri, urun_ust, masa_bayrak, mesaj_js, MESAJ_CSS, SERIT_OK_CSS, KAY_JS, GAL_OK
import luna_usb as U
import ozel_yon as O
import ozel_sayfa as OS
import urun_soru as US
CANVAS = os.path.join(HERE, '..', '..', 'canvas')
B = '/_blob/'
I = OS.I
H = 'yilbasi-agaci-projektor-lamba'
AD = 'Yılbaşı Ağacı Projektör Lamba'
P1 = 999.0   # GEÇİCİ: ürün Shopify'da yok (28 Eki); canlıda fiyat Shopify'dan gelir (ayluna.js)
C1 = None

TEMA = dict(v='#F2A65A', v2='#8A4F0F', zemin='#FFFFFF', cizgi='#E7E5EA', koyu='#10182B', koyu2='#1A2142',
            fb='"Young Serif"', fg='"Onest"', bk=400, bls='-.02em',
            font='family=Young+Serif&family=Onest:wght@400;500;600;700;800')

# Kutu fotoğrafındaki parçalar (montaj kartındaki "Kit contents" + fotoğraf); konum % (sol, üst)
PARCA = [('Hediye kutusu', 'Yılbaşı baskılı, kağıt dolgulu.', 52, 18), ('Altın abajur', 'Desenli çıkartmayı giydirirsin.', 36, 43),
         ('Desenli çıkartma', 'Abajurun etrafına sarılır.', 77, 48), ('İnci çıkartmalar', 'Kırmızı ve altın; kendinden yapışkanlı.', 60, 60),
         ('"Merry Christmas" çıkartması', 'Ağacın tepesine süs.', 63, 70), ('Tüylü süs çubukları', 'Kabloya sarılır, ağaç olur.', 83, 77),
         ('Projektör ve desen diskleri', 'USB kablolu, lensli modül; diskler değişir.', 36, 85), ('Montaj kartı', 'QR kodunda montaj videosu.', 22, 52)]
DISK = [('Klasik yılbaşı', 'yb-d-klasik'), ('Yeni yıl mesajı', 'yb-d-mesaj'), ('Kar taneleri', 'yb-d-kar'),
        ('Ren geyikleri', 'yb-d-geyik'), ('Kardan adam', 'yb-d-kardan'), ('Çanlar', 'yb-d-can')]
ADIM = [('yb-adim1', 'Sar', 'Tüylü çubukları USB kablonun etrafına sar, bükerek ağaç şekli ver.'),
        ('yb-adim3', 'Giydir', 'Desenli çıkartmayı altın abajura yapıştır; istersen inci çıkartmalarla süsle.'),
        ('yb-adim4', 'Tak, tavana çevir', 'Abajuru tak, USB’ye bağla, ışığı kapat.')]

USB_IK = '<svg viewBox="0 0 28 28"><rect x="9" y="3" width="10" height="9" rx="1.5"></rect><path d="M11 6h2M15 6h2"></path><path d="M14 12v8"></path><path d="M14 20c-4 0-6 2-6 5M14 20c4 0 6 2 6 5"></path></svg>'
HEDIYE_IK = '<svg viewBox="0 0 28 28"><rect x="4" y="11" width="20" height="14" rx="2"></rect><path d="M3 11h22M14 11v14"></path><path d="M14 11c-2-5-8-6-8-2 0 2 4 2 8 2zM14 11c2-5 8-6 8-2 0 2-4 2-8 2z"></path></svg>'
AGAC_IK = '<svg viewBox="0 0 28 28"><path d="M14 3l6 8h-3l5 7h-4l4 5H6l4-5H6l5-7H8z"></path><path d="M14 23v3"></path></svg>'

CSS = r"""
.al h1{font-size:26px;line-height:1.08}
.fiyat b{font-size:22px}
.dsk-y{display:flex}.dsk-y img{width:26px;height:26px;border-radius:50%;object-fit:cover;margin-left:-9px;box-shadow:0 0 0 2px #fff}.dsk-y img:first-child{margin-left:0}
/* Yılbaşından önce kapında: gerçek tarih (1 iş gününde kargo + en geç 7 gün) */
.yb-k{display:grid;grid-template-columns:52px minmax(0,1fr);gap:12px;align-items:center;margin:14px 0 0;padding:12px 14px;border-radius:16px;background:#F3F7F4;box-shadow:inset 0 0 0 1px #D7E6DC;color:var(--lac)}
.yb-k .gk{display:grid;place-items:center;align-content:center;width:52px;height:52px;border-radius:14px;background:#2E6B4F;color:#fff;font-weight:800;font-size:19px;line-height:1;font-variant-numeric:tabular-nums}
.yb-k .gk small{display:block;margin-top:3px;font-size:12px;font-weight:700}
.yb-k b{display:block;font-size:15px;line-height:1.3}
.yb-k span.t{display:block;margin-top:2px;font-size:13px;color:var(--soluk)}
.yb-k.gecti{background:#FFF6EC;box-shadow:inset 0 0 0 1px #F1DEC6}.yb-k.gecti .gk{background:var(--v2)}
.adapt{display:flex;gap:8px;align-items:flex-start;margin:10px 0 0;font-size:13px;color:var(--soluk)}
.adapt svg{flex:none;width:18px;height:18px;margin-top:1px;fill:none;stroke:var(--lac);stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
/* Yaparken / Yanınca */
.ikili{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:8px;margin-top:16px}
.ikili figure{position:relative;margin:0;border-radius:18px;overflow:hidden;aspect-ratio:4/5;background:#0E1220}
.ikili img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ikili figcaption{position:absolute;left:10px;bottom:10px;padding:4px 10px;border-radius:999px;background:#fff;color:var(--lac);font-size:12px;font-weight:700}
.ikili-w .ok{position:absolute;left:50%;top:50%;z-index:1;display:grid;place-items:center;width:36px;height:36px;margin:-18px 0 0 -18px;border-radius:50%;background:var(--v);box-shadow:0 0 0 4px #fff}
.ikili-w .ok svg{width:16px;height:16px;fill:none;stroke:var(--lac);stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.ikili-w{position:relative}
/* Kutuda ne var? */
.kut{position:relative;margin-top:16px;border-radius:20px;overflow:hidden;background:#EFE6D8}
.kut img{display:block;width:100%;height:auto}
.kut button{position:absolute;width:30px;height:30px;margin:-15px 0 0 -15px;padding:0;border:0;border-radius:50%;background:#fff;color:var(--lac);font:800 13px var(--fg);box-shadow:0 0 0 2px var(--lac),0 4px 10px rgba(0,0,0,.25);transition:transform .25s var(--ease),background-color .25s var(--ease)}
.kut button::after{content:"";position:absolute;inset:-9px}
.kut button.on{background:var(--lac);color:#fff;transform:scale(1.18)}
.kl{display:grid;grid-template-columns:28px minmax(0,1fr);gap:10px;align-items:center;margin-top:12px;padding:12px 14px;border-radius:14px;background:#F6F7F9;color:var(--lac)}
.kl em{display:grid;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--lac);color:#fff;font-style:normal;font-weight:800;font-size:13px}
.kl b{display:block;font-size:15px}.kl span{display:block;font-size:13px;color:var(--soluk)}
.kliste{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:6px 12px;margin:14px 0 0;padding:0;font-size:13px;color:var(--lac)}
.kliste li{display:flex;gap:6px}.kliste li::before{content:"";flex:none;width:6px;height:6px;margin-top:7px;border-radius:50%;background:var(--v)}
.kyok{margin:12px 0 0;padding:10px 12px;border-radius:12px;background:#FFF6EC;color:#6B3D0B;font-size:13px}
/* Bu gece hangisi? (tek gece bandı) */
.tav{position:relative;width:260px;height:260px;margin:18px auto 0;border-radius:50%;overflow:hidden;box-shadow:0 0 0 6px rgba(255,255,255,.06),0 0 70px rgba(242,166,90,.22)}
.tav img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:rotate(-5deg) scale(1.06);transition:opacity .5s var(--ease),transform .7s var(--ease)}
.tav img.on{opacity:1;transform:none}
.tav-ad{display:block;margin-top:12px;text-align:center;font-weight:700;color:#fff}
.dk{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:16px}
.dk button{display:flex;flex-direction:column;align-items:center;gap:6px;min-height:48px;padding:8px 4px;border:0;border-radius:14px;background:rgba(255,255,255,.06);color:#E6E8F2;font:600 12px var(--fg);box-shadow:inset 0 0 0 1px rgba(255,255,255,.12)}
.dk button img{width:46px;height:46px;border-radius:50%;object-fit:cover}
.dk button.on{box-shadow:inset 0 0 0 2px var(--v);color:#fff}
.koyu .alt-not{margin:14px 0 0;font-size:12px;color:#A9AEC6;text-align:center}
/* 3 adım */
.adm{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:16px;padding:16px 16px 4px}
.adm figure{flex:0 0 240px;margin:0;scroll-snap-align:start;border-radius:18px;background:#F6F7F9;overflow:hidden}
.adm img{display:block;width:100%;aspect-ratio:1/1;object-fit:cover}
.adm figcaption{padding:12px 14px 14px;font-size:13px;color:var(--soluk)}
.adm figcaption b{display:flex;align-items:center;gap:8px;margin-bottom:2px;font-size:16px;color:var(--lac)}
.adm figcaption b i{display:grid;place-items:center;width:24px;height:24px;border-radius:50%;background:var(--lac);color:#fff;font-style:normal;font-size:12px}
.qr{margin:12px 16px 0;padding:12px 14px;border-radius:14px;background:#F6F7F9;color:var(--lac);font-size:13px}
@media (prefers-reduced-motion:reduce){.tav img,.kut button{transition:none}}
"""


def tl(x): return O.tl(x)


def ozler():
    yigin = '<span class="dsk-y" aria-hidden="true">' + ''.join('<img src="%s" alt="">' % I(k) for _, k in DISK[:3]) + '</span>'
    return ('<div class="ozler dort">'
            '<div class="oz">' + O.mini(AGAC_IK) + '<b>Kendin yap</b><span class="t">Çubukları kabloya sar, ağacı süsle.</span></div>'
            '<div class="oz"><span class="gz">' + yigin + '</span><b>Tavana yılbaşı</b><span class="t">Desen diski değişir, tavan değişir.</span></div>'
            '<div class="oz">' + O.mini(USB_IK) + '<b>USB ile çalışır</b><span class="t">Şarj adaptörü, powerbank ya da bilgisayar.</span></div>'
            '<div class="oz">' + O.mini(HEDIYE_IK) + '<b>Hediye kutusunda</b><span class="t">Açması da kurması da hediye.</span></div></div>')


def hero():
    gost = '<span class="d-iz" aria-hidden="true"><sc-for list="{{gal}}" as="f" hint-placeholder-count="4"><i class="{{f.dcls}}"></i></sc-for></span>'
    return ("""
  <!-- Galeri: Shopify'da ürünün kendi görselleri; kaydırılır, 5 sn'de kendiliğinden geçer -->
  <section class="hero kare" aria-label="%s fotoğrafları">
    <div class="h-iz noscroll" onScroll="{{gKay}}"><sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><div class="{{f.cls}}"><img src="{{f.src}}" alt="{{f.n}}" style="object-position: {{f.pos}}"></div></sc-for></div>%s
    <div class="h-alt">%s<span style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%%); white-space: nowrap" aria-live="polite">Fotoğraf {{gNo}} / {{gCount}}</span></div>
  </section>
""" % (AD, GAL_OK, gost))


def al():
    fiyat = ('<p class="fiyat"><b>%s</b>%s</p>' % (tl(P1), ('<s>%s</s><span class="rozet">%%%d indirim</span>' % (tl(C1), round((1 - P1 / C1) * 100))) if C1 else ''))
    return ("""
  <section class="al" id="siparis">
    <h1 class="bas-y">%s</h1>
    <p class="alt-b">Kendin süslediğin minik yılbaşı ağacı; USB’ye takınca tavana yılbaşı desenleri yansıtır.</p>
    %s
    %s
    <!-- Yılbaşından önce kapında (gerçek tarih; sayaç değil) -->
    <div class="{{ybCls}}"><span class="gk">{{ybGun}}<small>{{ybGunEt}}</small></span><span><b>{{ybBas}}</b><span class="t">{{ybAlt}}</span></span></div>
    <div class="pk-bas">Kaç tane?</div>
    <div class="pk"><sc-for list="{{paket}}" as="b" hint-placeholder-count="2">
      <button class="{{b.cls}}" onClick="{{b.pick}}" aria-pressed="{{b.on}}"><sc-if value="{{b.rib}}" hint-placeholder-val="{{false}}"><span class="kurdele">Hediye için</span></sc-if><span class="pk-g"><img src="%s" alt=""><sc-if value="{{b.two}}" hint-placeholder-val="{{false}}"><span class="x2">×2</span></sc-if></span><span class="pk-o"><b>{{b.t}}</b><span>{{b.sub}}</span></span><span class="pk-f"><b>{{b.p}}</b></span></button>
    </sc-for></div>
    <!-- Stok ELLE girilir (ürün alanı ayluna.stok_kurdele); boşsa satır gizlenir -->
    <p class="stok"><span class="ping" aria-hidden="true"></span><span>Stokta son <b>[N]</b> adet</span></p>
    <button class="btn1" type="button"><span class="b-ic"><span>{{onLabel}}</span></span>%s</button>
    <div class="ay-dis" data-ay-dis></div>
    <p class="adapt"><svg viewBox="0 0 24 24"><rect x="7" y="2" width="10" height="8" rx="1.5"></rect><path d="M12 10v6M8 22h8M12 16v6"></path></svg><span>Telefon şarj adaptörüyle, powerbank ya da bilgisayarla çalışır. Adaptör kutuda yok; pil gerekmez.</span></p>
    <ol class="yol" aria-label="Siparişten teslime"><span class="yol-iz" aria-hidden="true"><i></i><i></i><em></em></span><li class="y1"><span class="yd"></span><b>Bugün</b><span>Sipariş verildi</span></li><li class="y2"><span class="yd"></span><b>{{kargo}}</b><span>Kargoda</span></li><li class="y3"><span class="yd"></span><b>{{teslim}}</b><span>Kapında</span></li></ol>
    %s
  </section>
""" % (AD, fiyat, ozler(), I('yb-kare'), U.OK, US.urs_html(US.sorular(OS.ICERIK[H])[0])))


YANINCA = """
  <!-- Yaparken / Yanınca: kurulum karesi (kullanıcının videosu) ve tavandaki desen -->
  <section class="bolum px">
    <h2 class="bas-y h2">Kutudan çıkar,<br>tavana yansıt<span class="n">.</span></h2>
    <p class="alt-b">Bir akşam birlikte kurarsınız; ışığı kapatınca tavan yılbaşı olur.</p>
    <div class="ikili-w"><div class="ikili">
      <figure><img src="@@yb-adim2@@" alt="Tüylü çubuklar kabloya sarılırken"><figcaption>Yaparken</figcaption></figure>
      <figure><img src="@@yb-tavan@@" alt="Tavanda yılbaşı desenleri" style="object-position: 50% 30%"><figcaption>Yanınca</figcaption></figure>
    </div><span class="ok" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"></path></svg></span></div>
  </section>
"""


def kutuda():
    nok = ''.join('<button style="left: %d%%; top: %d%%" class="{{nk%d}}" type="button" onClick="{{nkSec%d}}" aria-label="%s" aria-pressed="{{nkOn%d}}">%d</button>'
                  % (x, y, i, i, n, i, i + 1) for i, (n, _, x, y) in enumerate(PARCA))
    liste = ''.join('<li>%s</li>' % n for n, _, _, _ in PARCA)
    return ("""
  <!-- Kutuda ne var? (eleştirmen 1. fikir): gerçek kutu fotoğrafında numaralı noktalar; dokununca parça adı. Altta düz liste. -->
  <section class="bolum px" id="kutu">
    <h2 class="bas-y h2">Kutuda<br>ne var<span class="n">?</span></h2>
    <p class="alt-b">Fotoğraftaki numaralara dokun.</p>
    <div class="kut"><img src="@@yb-kutu@@" alt="Kutudan çıkan parçalar">""" + nok + """</div>
    <div class="kl"><em>{{nkNo}}</em><span><b>{{nkAd}}</b><span>{{nkAlt}}</span></span></div>
    <ul class="kliste">""" + liste + """</ul>
    <p class="kyok">USB adaptör kutuda yok: evdeki telefon şarj başlığı, powerbank ya da bilgisayar yeter.</p>
  </section>
""")


def gece():
    return ("""
  <!-- Bu gece hangisi? (eleştirmen 2. fikir): sayfadaki tek koyu bant; 4 sn'de kendiliğinden geçer, dokununca durur -->
  <section class="koyu bolum" id="diskler">
    <div class="px"><h2 class="bas-y h2">Bu gece<br>hangisi<span class="n">?</span></h2><p class="alt-b">Diski değiştir, tavan değişsin.</p>
    <div class="tav" aria-hidden="true"><sc-for list="{{disk}}" as="d" hint-placeholder-count="2"><img class="{{d.cls}}" src="{{d.src}}" alt=""></sc-for></div>
    <span class="tav-ad" aria-live="polite">{{dAd}}</span>
    <div class="dk"><sc-for list="{{disk}}" as="d" hint-placeholder-count="6"><button class="{{d.bcls}}" type="button" onClick="{{d.pick}}" aria-pressed="{{d.on}}"><img src="{{d.src}}" alt="">{{d.n}}</button></sc-for></div>
    <p class="alt-not">Disk değiştirmek: fişi çek, abajuru kaldır, diski değiştir, abajuru tak. Desen görselleri ürün afişinden; tavanda daha yumuşak görünür.</p></div>
  </section>
""")


def adimlar():
    k = ''.join('<figure><img src="@@%s@@" alt="%s"><figcaption><b><i>%d</i>%s</b>%s</figcaption></figure>' % (f, t, i + 1, t, a) for i, (f, t, a) in enumerate(ADIM))
    return ("""
  <!-- 3 adımda ağaç: kullanıcının montaj videosundan kareler -->
  <section class="bolum" id="kurulum">
    <div class="px"><h2 class="bas-y h2">Üç adımda<br>ağaç<span class="n">.</span></h2><p class="alt-b">Videodaki gibi; kaydır.</p></div>
    <div class="adm noscroll">""" + k + """<span aria-hidden="true" style="flex: 0 0 6px"></span></div>
    <p class="qr">Montaj kartının QR kodunda video var. USB ucunu ve projektör lensini kapatma. İnci çıkartmalar küçük parça: küçük çocuklar bir yetişkinle yapsın.</p>
  </section>
""")


def gerisi():
    g = OS.gerisi('af')
    g = re.sub(r'\n  <!-- Yorumlar:.*?</section>\n', '\n', g, flags=re.S)  # yeni ürün: yorum yok, bölüm konmadı
    g = g.replace('Bu gece duvarında <br>ay olsun', 'Bu yılbaşı<br>tavana bak').replace('@@af-ay-yakin@@', '@@yb-kare@@').replace('<b>AyFeneri</b>', '<b>Yılbaşı Ağacı</b>')
    g = g.replace('<small style="color: var(--koyu)">Kartla %5 indirim dahil</small>', '')
    assert 'yb-kare' in g and 'Yılbaşı Ağacı' in g
    return g


def govde():
    h = ('<div class="pg">\n  ' + U.SERIT + hero() + al() + YANINCA + kutuda() + gece() + adimlar() + gerisi() + '</div>\n')
    return re.sub(r'@@([\w-]+)@@', lambda m: I(m.group(1)), h)


def faq():
    return [{'q': q, 'a': a} for q, a in US.sorular(OS.ICERIK[H])[1]]


def js():
    gal = [[B + i, '%s görseli %d' % (AD, k + 1), '50% 50%'] for k, i in enumerate(canli_galeri(H))]
    disk = [[n, I(k)] for n, k in DISK]
    parca = [[n, a] for n, a, _, _ in PARCA]
    BA = OS.BA
    PR = [('lunadream-gece-lambasi', 'LunaDream Gece Lambası', 1699.99, 1999), ('galayx-usb-projektor', 'Galaxy USB Projektör', 1599, 1999),
          ('lamba', 'Ayluna AyFeneri', 1649.99, 2499), ('ayluna-galaksi-night-projektor', 'Ayluna Galaksi Night Projektör', 2199, 2999),
          ('galaksiambiyanisigi', 'Galaksi Ambiyans Işığı', 1499, 2898), ('ask-saati', 'Ayluna Kum Saati Lamba', 799, 999)]
    shop = [[n, p, c, B + BA['u-%s.jpg' % h]] for h, n, p, c in PR]
    nk = ''.join("nk%d: S.nk === %d ? 'on' : '', nkOn%d: S.nk === %d ? 'true' : 'false', nkSec%d: function () { self.setState({ nk: %d }); },\n      " % (i, i, i, i, i, i) for i in range(len(PARCA)))
    return """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { g: 0, gOto: true, adet: null, disk: 0, dOto: true, nk: 1, t: 0, now: Date.now() }; }
  componentDidMount() {
    var self = this;
    if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) this.setState({ dOto: false });
    // Tek saat: şerit sayacı, galeri (5 sn), disk (4 sn)
    this.iv = setInterval(function () {
      var S = self.state, t = S.t + 1, o = { now: Date.now(), t: t };
      if (S.gOto && t % 5 === 0) self.galGit((S.g + 1) % (self.galN || """ + str(len(gal)) + """));
      if (S.dOto && t % 4 === 0) o.disk = (S.disk + 1) % """ + str(len(DISK)) + """;
      self.setState(o);
    }, 1000);
  }
  galGit(i) { var el = document.querySelector('.h-iz'); if (el && el.scrollTo && el.clientWidth) { this.otoKay = Date.now(); el.scrollTo({ left: i * el.clientWidth, behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); } else this.setState({ g: i }); }
  componentDidUpdate() { var el = document.querySelector('.h-iz'); if (el && el.clientWidth && Math.abs(el.scrollLeft - this.state.g * el.clientWidth) > el.clientWidth / 2) { this.otoKay = Date.now(); el.scrollLeft = this.state.g * el.clientWidth; } }
  componentWillUnmount() { clearInterval(this.iv); }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    """ + TL_JS + """
    var MEDYA = (window.Ayluna && Ayluna.medya) ? Ayluna.medya() : null, GAL = MEDYA ? MEDYA.map(function (m) { return [m.src, m.alt, '50% 50%']; }) : """ + json.dumps(gal, ensure_ascii=False) + """;
    self.galN = GAL.length;
    var gal = GAL.map(function (g, i) { var on = i === S.g; return { src: g[0], n: g[1], pos: g[2], cls: 'hs' + (on ? ' on' : ''), dcls: i < S.g ? 'lit' : (on ? 'lit on' : '') }; });
    function gKay(e) { var el = e && (e.currentTarget || e.target); if (!el || !el.clientWidth) return; var i = Math.round(el.scrollLeft / el.clientWidth), o = {};
      if (i !== self.state.g) o.g = i; if (self.state.gOto && Date.now() - (self.otoKay || 0) > 900) o.gOto = false; if (o.g !== undefined || o.gOto === false) self.setState(o); }
    // Fiyat: Shopify'da canlı fiyat (V.urun), tuvalde geçici fiyat. 2 adette indirim tanımlı değil: tasarruf yazılmaz.
    var VU = ((window.AYLUNA_VERI || {}).urun || {})[""" + json.dumps(H) + """] || {}, P1 = VU.p || """ + str(P1) + """;
    var paket = [
      { n: 1, t: '1 Adet', p: TL(P1, true), sub: 'Kendine ya da evine', rib: false },
      { n: 2, t: '2 Adet', p: TL(2 * P1, true), sub: 'Biri sana, biri hediye', rib: true }
    ].map(function (b) { var on = S.adet === b.n; return { t: b.t, p: b.p, sub: b.sub, rib: b.rib, two: b.n === 2, on: on ? 'true' : 'false', cls: on ? 'pk-k on' : 'pk-k', pick: function () { self.setState({ adet: b.n }); } }; });
    var DISK = """ + json.dumps(disk, ensure_ascii=False) + """;
    var disk = DISK.map(function (d, i) { var on = i === S.disk; return { n: d[0], src: d[1], on: on ? 'true' : 'false', cls: on ? 'on' : '', bcls: on ? 'on' : '', pick: function () { self.setState({ disk: i, dOto: false }); } }; });
    var PARCA = """ + json.dumps(parca, ensure_ascii=False) + """;
    var AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'], AYU = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
    var now = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kd = new Date(now); do { kd.setDate(kd.getDate() + 1); } while (kd.getDay() === 0 || kd.getDay() === 6);
    var t1 = new Date(kd); t1.setDate(t1.getDate() + 3); var t2 = new Date(kd); t2.setDate(t2.getDate() + 7);
    var teslim = t1.getMonth() === t2.getMonth() ? t1.getDate() + '–' + t2.getDate() + ' ' + AY[t2.getMonth()] : t1.getDate() + ' ' + AY[t1.getMonth()] + '–' + t2.getDate() + ' ' + AY[t2.getMonth()];
    // Yılbaşından önce teslim için son sipariş: 31 Aralık'tan 7 gün teslim + 1 iş günü kargo geriye; hafta sonu atlanır
    var g0 = new Date(now.getFullYear(), now.getMonth(), now.getDate()), yil = now.getMonth() === 0 && now.getDate() < 7 ? null : new Date(now.getFullYear(), 11, 31);
    var son = yil ? new Date(yil.getFullYear(), 11, 23) : null; if (son) while (son.getDay() === 0 || son.getDay() === 6) son.setDate(son.getDate() - 1);
    var gunYil = yil ? Math.round((yil - g0) / 864e5) : 0, yetisir = son && g0 <= son;
    var ybCls = yetisir ? 'yb-k' : 'yb-k gecti', ybGun = yetisir ? String(gunYil) : '', ybGunEt = yetisir ? 'gün' : '';
    var ybBas = yetisir ? 'Yılbaşından önce kapında' : 'Yılbaşına yetişmeyebilir', ybAlt = yetisir ? ('Yılbaşına ' + gunYil + ' gün var. Yılbaşından önce teslim için son sipariş: ' + son.getDate() + ' ' + AYU[son.getMonth()] + '.') : ('Tahmini teslim: ' + teslim + '.');
    function IKI(n) { return n < 10 ? '0' + n : String(n); }
    var ist = new Date(new Date(S.now || Date.now()).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kalan = Math.max(0, new Date(ist.getFullYear(), ist.getMonth(), ist.getDate(), 23, 59, 59, 999).getTime() - ist.getTime());
    var hh = Math.floor(kalan / 3600000), mi = Math.floor(kalan / 60000) % 60, ss = Math.floor(kalan / 1000) % 60;
    function AYY(f) { var r = 9, c = 12, rx = Math.abs(1 - 2 * f) * r; return 'M' + c + ' ' + (c - r) + 'A' + r + ' ' + r + ' 0 0 1 ' + c + ' ' + (c + r) + 'A' + rx.toFixed(2) + ' ' + r + ' 0 0 ' + (f < .5 ? 0 : 1) + ' ' + c + ' ' + (c - r) + 'Z'; }
    function alaGit() { var h = document.getElementById('siparis'); if (h && h.scrollIntoView) h.scrollIntoView({ behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' }); }
""" + KAY_JS + """    var PR = """ + json.dumps(shop, ensure_ascii=False) + """;
    var shop = PR.map(function (x) { var d = x[2] > x[1]; return { n: x[0], src: x[3], price: TL(x[1], true), old: d ? TL(x[2], true) : '', pct: d ? '%' + Math.round((1 - x[1] / x[2]) * 100) : '' }; });
    return {
      gal: gal, gNo: S.g + 1, gCount: GAL.length, gKay: gKay, paket: paket, adetName: S.adet === 2 ? '2 Adet' : '1 Adet',
      onLabel: 'Güvenli Ödeme ile Al', kargo: kd.getDate() + ' ' + AY[kd.getMonth()], teslim: teslim,
      ybCls: ybCls, ybGun: ybGun, ybGunEt: ybGunEt, ybBas: ybBas, ybAlt: ybAlt,
      hh: IKI(hh), mm: IKI(mi), ss: IKI(ss), snCls: ss % 2 ? 'sn tA' : 'sn tB', cdAria: 'Bugünkü fiyat garantisinin bitmesine ' + hh + ' saat ' + mi + ' dakika', cdAy: AYY(Math.round(kalan / 864000) / 100),
      disk: disk, dAd: DISK[S.disk][0],
      nkNo: S.nk + 1, nkAd: PARCA[S.nk][0], nkAlt: PARCA[S.nk][1],
      """ + nk + """alaGit: alaGit, faq: """ + json.dumps(faq(), ensure_ascii=False) + """, kayGeri: KAY(-1), kayIleri: KAY(1), shop: shop, shopCount: PR.length
    };
  }
}"""


DOSYA = 'YilbasiAgaci.dc.html'


def sayfa():
    css = O.tema_css(dict(TEMA, ek='')) + U.CSS + O.CSS + '\n' + OS.CSS + CSS + US.URS_CSS + SERIT_OK_CSS + MESAJ_CSS + UST_CSS
    return U.head(AD, css, TEMA['font']) + govde()


if __name__ == '__main__':
    h = int(os.environ.get('S_H', 6200))
    open(os.path.join(CANVAS, DOSYA), 'w', encoding='utf-8').write(urun_ust(sayfa(), '<section class="hero kare"') + TAIL.format(h=h, js=masa_bayrak(mesaj_js(js()))))
    print('yazıldı:', DOSYA, h)
