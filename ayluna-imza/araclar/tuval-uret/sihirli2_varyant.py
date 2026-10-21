# Sihirli Özellikler · kurumsal mini arayüz sekansları, 3 yön (21 Eki). Çalıştır: python3 sihirli2_varyant.py
# Kullanıcı: "Şu emoji benefit kısmını vesaire biraz daha kurumsal yapsak ve UI'lerle doldursak daha profesyonel görünsün;
# mesela dönen diskler sırayla masal diskini gidip gelse gibi tatlı ufak sekanslar."
# Önceki kararlar korunur (17 Eki): kartlar beyaz, koyu ve amber dolu kart yok, gölge yok; amber yalnız hareket eden parçada.
# Sekanslar (yalnız transform/opacity, tek eğri, azaltılmış harekette anlamlı duran kare):
#   Diskler: disk pencereye dönerek gelir, döner, çıkarken sıradaki girer (pencere boş kalmaz); altında adı değişir (8 sn, 4 disk)
#   Parlaklık: üç kademe; halkalar ve kademe göstergesi birlikte ilerler (6 sn)
#   Bluetooth ninni: telefon → lamba noktalar akar ("Bağlanıyor"), sonra ses çubukları ve ilerleme ("Ninni çalıyor") (6 sn)
#   Şarj: lambanın çevresindeki halka dilim dilim dolar, kablo çıkar ("Kablosuz") (6 sn)
#   A · Canlı kartlar: 2×2 kart, her kartın üstünde küçük ekran
#   B · Özellik turu: tek büyük ekran, altında 4 satır; etkin satırın çizgisi dolar, sıradakine geçer (dokununca seçilir)
#   C · Bento: üstte geniş disk kartı (disk şeridi kayar, ortadaki döner), altta üç küçük kare
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE-Sihirli2.dc.html')

E = 'cubic-bezier(.2,.7,.2,1)'
DISK = [('Okyanus', 'a24f13e032569f76d64b9b0fbe8d74f7'), ('Uzay', 'b088d2c82561b76f6db997fbc3944059'),
        ('Deniz kızı', '04ed9ce4ae8a36619975caa7d2de9ad8'), ('Şato', 'bbd010d8d946edc8fef9c0404cba4ea2')]

# Çizgi ikonlar (lacivert çizgi, amber yalnız ışık)
LAMBA = ('<svg class="lmb" viewBox="0 0 32 32" aria-hidden="true"><path class="kb" d="M7 13c0-5 4-9 9-9s9 4 9 9c-1.5 1-3 1-4.5 0-1.5 1-3 1-4.5 0-1.5 1-3 1-4.5 0-1.5 1-3 1-4.5 0z"></path>'
         '<rect class="isk" x="10.5" y="14.5" width="11" height="7" rx="1.5"></rect><path d="M10 14v8M22 14v8"></path><path d="M8.5 22.5h15l-1.5 4h-12z"></path></svg>')
TEL = '<svg class="tel" viewBox="0 0 24 24" aria-hidden="true"><rect x="7" y="2.5" width="10" height="19" rx="2.5"></rect><path d="M11 18.5h2"></path></svg>'
FIS = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12h7M10 8.5h5a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2h-5zM17 10.5h3M17 13.5h3"></path></svg>'


def ui_isik():
    return ('<span class="ui ui-isik" aria-hidden="true"><span class="hl h3"></span><span class="hl h2"></span><span class="hl h1"></span>' + LAMBA +
            '<span class="kad"><i></i><i></i><i></i><b></b></span></span>')


def ui_disk():
    return ('<span class="ui ui-disk" aria-hidden="true"><span class="yuva">' +
            ''.join('<img class="d d%d" src="/_blob/%s" alt="">' % (k + 1, i) for k, (_, i) in enumerate(DISK)) +
            '</span><span class="adlar">' + ''.join('<i class="a%d">%s</i>' % (k + 1, n) for k, (n, _) in enumerate(DISK)) + '</span></span>')


def ui_bt():
    return ('<span class="ui ui-bt" aria-hidden="true"><span class="bt-sira">' + TEL + '<span class="akis"><i></i><i></i><i></i></span>' + LAMBA +
            '<span class="eq"><i></i><i></i><i></i><i></i></span></span><span class="bt-alt"><span class="durum"><i>Bağlanıyor</i><i>Ninni çalıyor</i></span>'
            '<span class="cal"><b></b></span></span></span>')


def ui_sarj():
    return ('<span class="ui ui-sarj" aria-hidden="true"><span class="halka">' +
            ''.join('<i style="transform: rotate(%ddeg) translateY(-25px); animation-delay: %.2fs"></i>' % (k * 30, k * .18) for k in range(12)) +
            '</span>' + LAMBA + '<span class="fis">' + FIS + '</span><span class="durum"><i>Şarj oluyor</i><i>Kablosuz</i></span></span>')


# Bento için geniş disk şeridi: 6 disk (ilk ikisi sonda tekrar, dikişsiz döngü), ortadaki pencerede döner
def ui_serit():
    ds = DISK + DISK[:2]
    return ('<span class="ui ui-serit" aria-hidden="true"><span class="pencere"></span><span class="tren">' +
            ''.join('<span class="sd"><img src="/_blob/%s" alt=""></span>' % i for _, i in ds) + '</span>'
            '<span class="adlar">' + ''.join('<i class="a%d">%s</i>' % (k + 1, n) for k, (n, _) in enumerate(DISK)) + '</span></span>')


OZ = [  # (anahtar, başlık, cümle, mini arayüz)
    ('disk', '6 + 6 masal diski', 'Altısı hediye. Diski tak, masal tavana yansısın.', ui_disk),
    ('isik', '3 parlaklık', 'Kısık, orta ya da parlak; geceye göre ayarla.', ui_isik),
    ('bt', 'Bluetooth ninni', 'Telefondan bağlan; ses lambadan gelsin.', ui_bt),
    ('sarj', 'Şarjlı, kablosuz', 'Şarj et, kablosu olmadan her odaya taşı.', ui_sarj),
]

CSS = r""".pg{background:#F6F1E9;font-size:15px}
.sec{padding:0 16px 40px}
.oneri{display:flex;align-items:center;gap:8px;margin:0 0 6px;padding-top:16px;border-top:1px dashed #D6CAB6;font-size:12px;font-weight:700;color:#A05A1C}
.oneri-alt{margin:0 0 16px;font-size:13px;color:#5C6078;text-wrap:balance}
.ust-yazi{margin:0;font-size:13px;font-weight:700;color:#A05A1C}
.pg button{font:inherit;cursor:pointer;-webkit-tap-highlight-color:transparent}
.pg :focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
img{display:block}

/* Ortak mini arayüz: ekran zemini ton #F1E8DA, çizgiler lacivert, ışık amber */
.ek{position:relative;display:grid;place-items:center;overflow:hidden;border-radius:14px;background:#F1E8DA}
.ui{position:relative;display:block}
.lmb{width:32px;height:32px;fill:none;stroke:#1A2142;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.lmb .kb{fill:#FFFDF9}
.lmb .isk{fill:#F2A65A;stroke:none;opacity:.9}
.tel{width:22px;height:22px;fill:none;stroke:#1A2142;stroke-width:1.5;stroke-linecap:round}
.durum{position:relative;display:grid;font-size:12px;font-weight:600;color:#5C6078;white-space:nowrap}
.durum i{grid-area:1/1;font-style:normal}

/* Parlaklık: 3 kademe (6 sn). Duran kare: üçüncü kademe */
.ui-isik{width:120px;height:64px}
.ui-isik .lmb{position:absolute;left:14px;top:16px}
.ui-isik .hl{position:absolute;left:30px;top:32px;border-radius:50%;border:1.5px solid #F2A65A}
.ui-isik .h1{width:40px;height:40px;margin:-20px 0 0 -20px;opacity:.9}
.ui-isik .h2{width:56px;height:56px;margin:-28px 0 0 -28px;opacity:.55;animation:l2 6s EASE infinite}
.ui-isik .h3{width:72px;height:72px;margin:-36px 0 0 -36px;opacity:.3;animation:l3 6s EASE infinite}
.ui-isik .isk{animation:lisk 6s EASE infinite}
@keyframes l2{0%,30%{opacity:0;transform:scale(.8)}37%,92%{opacity:.55;transform:none}100%{opacity:0;transform:scale(.8)}}
@keyframes l3{0%,63%{opacity:0;transform:scale(.8)}70%,92%{opacity:.3;transform:none}100%{opacity:0;transform:scale(.8)}}
@keyframes lisk{0%,30%{opacity:.35}37%,63%{opacity:.65}70%,92%{opacity:1}100%{opacity:.35}}
.kad{position:absolute;right:0;top:26px;display:flex;gap:8px;padding:4px 6px;border-radius:999px;background:#FFFDF9}
.kad i{width:6px;height:6px;border-radius:50%;background:#D6CAB6}
.kad b{position:absolute;left:4px;top:2px;width:10px;height:10px;border-radius:50%;background:#F2A65A;transform:translateX(28px);animation:kad 6s EASE infinite}
@keyframes kad{0%,30%{transform:none}37%,63%{transform:translateX(14px)}70%,92%{transform:translateX(28px)}100%{transform:none}}

/* Diskler: pencerede sırayla (8 sn, 4 disk × 2 sn). Duran kare: ilk disk ve adı */
.ui-disk{width:120px;height:72px;display:flex;flex-direction:column;align-items:center;gap:6px}
.yuva{position:relative;width:48px;height:48px;border-radius:50%;overflow:hidden;background:#FFFDF9;box-shadow:0 0 0 1.5px #1A2142}
.yuva .d{position:absolute;inset:3px;width:42px;height:42px;border-radius:50%;object-fit:cover;opacity:0}
.yuva .d1{opacity:1}
.ui-disk .d{animation:dsk 8s EASE infinite both}
.ui-disk .d2{animation-delay:2s}.ui-disk .d3{animation-delay:4s}.ui-disk .d4{animation-delay:6s}
@keyframes dsk{0%{transform:translateX(48px) rotate(-90deg);opacity:0}3%{opacity:1}8%{transform:none}24%{transform:rotate(80deg);opacity:1}29%{transform:translateX(-48px) rotate(170deg);opacity:0}100%{transform:translateX(-48px) rotate(170deg);opacity:0}}
.adlar{position:relative;display:grid;font-size:12px;font-weight:600;color:#1A2142;white-space:nowrap}
.adlar i{grid-area:1/1;justify-self:center;font-style:normal;opacity:0}
.adlar .a1{opacity:1}
.ui-disk .adlar i,.ui-serit .adlar i{animation:adk 8s EASE infinite both}
.adlar .a2{animation-delay:2s!important}.adlar .a3{animation-delay:4s!important}.adlar .a4{animation-delay:6s!important}
@keyframes adk{0%,3%{opacity:0;transform:translateY(4px)}8%,23%{opacity:1;transform:none}27%,100%{opacity:0;transform:translateY(-4px)}}

/* Bluetooth: bağlan (0-35%) → çal (38-94%). Duran kare: çalıyor, ilerleme yarıda */
.ui-bt{width:132px;display:flex;flex-direction:column;gap:6px}
.bt-sira{display:flex;align-items:center;gap:4px;height:34px}
.ui-bt .lmb{width:28px;height:28px}
.akis{position:relative;width:30px;height:6px}
.akis i{position:absolute;left:0;top:1px;width:4px;height:4px;border-radius:50%;background:#1A2142;opacity:0;animation:akis 6s EASE infinite}
.akis i:nth-child(2){animation-delay:.25s}.akis i:nth-child(3){animation-delay:.5s}
@keyframes akis{0%{transform:none;opacity:0}4%{opacity:1}22%{transform:translateX(26px);opacity:0}23%{transform:none;opacity:0}27%{opacity:1}34%{transform:translateX(26px);opacity:0}100%{transform:translateX(26px);opacity:0}}
.eq{display:flex;align-items:flex-end;gap:2px;height:18px;margin-left:2px;animation:btg 6s EASE infinite}
.eq i{width:3px;height:18px;border-radius:2px;background:#F2A65A;transform-origin:50% 100%;transform:scaleY(.5);animation:ses 1.2s ease-in-out infinite}
.eq i:nth-child(2){animation-delay:-.3s}.eq i:nth-child(3){animation-delay:-.6s}.eq i:nth-child(4){animation-delay:-.9s}
@keyframes ses{0%,100%{transform:scaleY(.3)}50%{transform:scaleY(1)}}
@keyframes btg{0%,35%{opacity:0}40%,92%{opacity:1}100%{opacity:0}}
.bt-alt{display:flex;flex-direction:column;gap:4px}
.ui-bt .durum i:first-child{opacity:0;animation:d1 6s EASE infinite}
.ui-bt .durum i:last-child{animation:d2 6s EASE infinite}
@keyframes d1{0%,33%{opacity:1}38%,100%{opacity:0}}
@keyframes d2{0%,35%{opacity:0}40%,94%{opacity:1}100%{opacity:0}}
.cal{position:relative;height:3px;border-radius:2px;background:#E3D8C7;overflow:hidden}
.cal b{position:absolute;inset:0;border-radius:2px;background:#1A2142;transform-origin:0 50%;transform:scaleX(.5);animation:cal 6s linear infinite}
@keyframes cal{0%,38%{transform:scaleX(0)}94%{transform:scaleX(1)}100%{transform:scaleX(0)}}

/* Şarj: halka dilim dilim dolar, kablo çıkar (6 sn). Duran kare: dolu halka, kablosuz */
.ui-sarj{width:132px;height:64px}
.halka{position:absolute;left:32px;top:32px;width:0;height:0}
.halka i{position:absolute;left:-1.5px;top:-4px;width:3px;height:8px;border-radius:2px;background:#F2A65A;animation:dilim 6s EASE infinite both}
@keyframes dilim{0%{opacity:.18}5%,62%{opacity:1}72%,100%{opacity:.18}}
.ui-sarj .lmb{position:absolute;left:18px;top:17px;width:28px;height:28px}
.fis{position:absolute;left:60px;top:22px;width:22px;height:22px;opacity:0;animation:fis 6s EASE infinite}
.fis svg{width:22px;height:22px;fill:none;stroke:#1A2142;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round;transform:scaleX(-1)}
@keyframes fis{0%,58%{transform:none;opacity:1}66%,92%{transform:translateX(12px);opacity:0}100%{transform:none;opacity:1}}
.ui-sarj .durum{position:absolute;left:66px;top:42px}
.ui-sarj .durum i:first-child{opacity:0;animation:s1 6s EASE infinite}
.ui-sarj .durum i:last-child{animation:s2 6s EASE infinite}
@keyframes s1{0%,58%{opacity:1}64%,100%{opacity:0}}
@keyframes s2{0%,60%{opacity:0}66%,94%{opacity:1}100%{opacity:0}}

/* A · Canlı kartlar */
.a-izgara{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:12px}
.a-kart{display:flex;flex-direction:column;gap:10px;padding:10px 10px 14px;border-radius:20px;background:#FFFDF9;border:1px solid #E3D8C7;color:#1A2142;text-decoration:none}
.a-kart .ek{height:92px}
.a-kart b{display:block;padding:0 4px;font-size:15px;line-height:1.25}
.a-kart span.t{display:block;margin-top:2px;padding:0 4px;font-size:13px;line-height:1.4;color:#5C6078;text-wrap:balance}

/* B · Özellik turu: tek ekran, 4 satır; etkin satırın çizgisi 5 sn'de dolar */
.b-kutu{margin-top:12px;border-radius:20px;background:#FFFDF9;border:1px solid #E3D8C7;overflow:hidden}
.b-ekran{position:relative;height:150px;margin:10px 10px 0;border-radius:14px;background:#F1E8DA}
.b-sahne{position:absolute;inset:0;display:grid;place-items:center;opacity:0;transform:translateY(6px);transition:opacity .35s EASE,transform .35s EASE}
.b-sahne.on{opacity:1;transform:none}
.b-sahne .ui{transform:scale(1.45)}
.b-liste{list-style:none;margin:0;padding:4px 0 6px}
.b-sat{position:relative;display:block;width:100%;min-height:52px;padding:10px 16px;border:0;background:none;text-align:left;color:#1A2142}
.b-sat+.b-sat{border-top:1px solid #EFE6D8}
.b-sat b{display:block;font-size:15px;line-height:1.25;color:#5C6078;transition:color .25s EASE}
.b-sat .t{display:block;font-size:13px;line-height:1.4;color:#5C6078;opacity:0;transform:translateY(-2px);max-height:0;overflow:hidden;transition:opacity .25s EASE,transform .25s EASE}
.b-sat.on b{color:#1A2142}
.b-sat.on .t{opacity:1;transform:none;max-height:40px;margin-top:2px}
.b-sat .cz{position:absolute;left:16px;right:16px;bottom:0;height:2px;background:#F2A65A;transform-origin:0 50%;transform:scaleX(0)}
.b-sat.on .cz{animation:bcz 5s linear forwards}
@keyframes bcz{to{transform:scaleX(1)}}

/* C · Bento: geniş disk kartı + üç küçük kare */
.c-genis{display:grid;grid-template-columns:minmax(0,1fr) 176px;align-items:center;gap:12px;margin-top:12px;padding:10px 10px 10px 16px;border-radius:20px;background:#FFFDF9;border:1px solid #E3D8C7;color:#1A2142;text-decoration:none}
.c-genis b{display:block;font-size:16px;line-height:1.25}
.c-genis span.t{display:block;margin-top:4px;font-size:13px;line-height:1.4;color:#5C6078}
.c-genis u{color:#A05A1C;text-underline-offset:3px}
.c-genis .ek{height:112px}
.c-uc{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:8px}
.c-kare{display:flex;flex-direction:column;gap:8px;padding:8px 8px 12px;border-radius:18px;background:#FFFDF9;border:1px solid #E3D8C7}
.c-kare .ek{display:flex;align-items:center;justify-content:center;height:76px}
.c-kare .ui{flex:none}
.c-kare .ui{transform:scale(.7)}
.c-kare .durum,.c-kare .bt-alt{display:none}
.c-kare b{display:block;padding:0 2px;font-size:13px;line-height:1.25}
/* Geniş disk şeridi: 6 disk × 46 px; her 2 sn bir disk kayar; ortadaki pencerede döner */
.ui-serit{width:176px;height:96px}
.pencere{position:absolute;left:61px;top:4px;width:54px;height:54px;border-radius:50%;box-shadow:0 0 0 1.5px #1A2142;background:#FFFDF9}
.tren{position:absolute;left:0;top:8px;display:flex;gap:4px;padding-left:65px;animation:tren 8s EASE infinite}
.sd{flex:none;width:46px;height:46px;transform:scale(.72);opacity:.55;animation:sdo 8s EASE infinite}
.sd img{width:46px;height:46px;border-radius:50%;object-fit:cover;animation:don 6s linear infinite}
@keyframes don{to{transform:rotate(360deg)}}
@keyframes tren{0%,20%{transform:none}25%,45%{transform:translateX(-50px)}50%,70%{transform:translateX(-100px)}75%,95%{transform:translateX(-150px)}100%{transform:translateX(-200px)}}
.sd:nth-child(1){animation-name:sd1}.sd:nth-child(2){animation-name:sd2}.sd:nth-child(3){animation-name:sd3}.sd:nth-child(4){animation-name:sd4}.sd:nth-child(5){animation-name:sd5}
@keyframes sd1{0%,20%{transform:none;opacity:1}25%,100%{transform:scale(.72);opacity:.55}}
@keyframes sd2{0%,20%{transform:scale(.72);opacity:.55}25%,45%{transform:none;opacity:1}50%,100%{transform:scale(.72);opacity:.55}}
@keyframes sd3{0%,45%{transform:scale(.72);opacity:.55}50%,70%{transform:none;opacity:1}75%,100%{transform:scale(.72);opacity:.55}}
@keyframes sd4{0%,70%{transform:scale(.72);opacity:.55}75%,95%{transform:none;opacity:1}100%{transform:scale(.72);opacity:.55}}
@keyframes sd5{0%,95%{transform:scale(.72);opacity:.55}100%{transform:none;opacity:1}}
.ui-serit .adlar{position:absolute;left:0;right:0;bottom:4px}
.ui-serit .adlar i{animation-timing-function:EASE}
@media (prefers-reduced-motion:reduce){.sd:nth-child(1){transform:none;opacity:1}}
""".replace('EASE', E)


def kart_a(k):
    a, b, t, f = k
    tag = 'a href="#diskler"' if a == 'disk' else 'div'
    return '<%s class="a-kart"><span class="ek">%s</span><span><b>%s</b><span class="t">%s</span></span></%s>' % (tag, f(), b, t, tag.split()[0])


HTML = """<div class="pg">
  <div style="padding: 18px 16px 10px">
    <h1 class="h2" style="font-size: 22px">Sihirli özellikler · üç kurumsal yön</h1>
    <p style="margin: 6px 0 0; font-size: 13px; color: #5C6078">Satın alma kutusunda, fiyatın altında. Her özellik kendi küçük sekansıyla anlatılır: disk sırayla gelir ve döner, parlaklık üç kademe, Bluetooth bağlanıp çalar, şarj halkası dolar. Kartlar beyaz, amber yalnız hareket eden parçada.</p>
  </div>

  <section class="sec">
    <p class="oneri">A · Canlı kartlar</p>
    <p class="oneri-alt">Bugünkü 2×2 düzen kalır; ikon kutusunun yerine her kartın üstünde küçük bir ekran ve sekansı.</p>
    <p class="ust-yazi">Sihirli özellikler</p>
    <div class="a-izgara">""" + ''.join(kart_a(k) for k in OZ) + """</div>
  </section>

  <section class="sec">
    <p class="oneri">B · Özellik turu</p>
    <p class="oneri-alt">Tek büyük ekran, altında dört satır. Etkin satırın çizgisi 5 sn'de dolar, sıradakine geçer; dokununca o özellik açılır. En "ürün tanıtım sayfası" duran yön.</p>
    <p class="ust-yazi">Sihirli özellikler</p>
    <div class="b-kutu">
      <div class="b-ekran">""" + ''.join('<div class="{{b%d}}" aria-hidden="{{bg%d}}">%s</div>' % (i, i, k[3]()) for i, k in enumerate(OZ)) + """</div>
      <ul class="b-liste">""" + ''.join('<li><button class="{{bs%d}}" type="button" onClick="{{bsec%d}}" aria-pressed="{{bp%d}}"><b>%s</b><span class="t">%s</span><span class="cz" aria-hidden="true"></span></button></li>' % (i, i, i, k[1], k[2]) for i, k in enumerate(OZ)) + """</ul>
    </div>
  </section>

  <section class="sec">
    <p class="oneri">C · Bento</p>
    <p class="oneri-alt">Diskler ürünü ayıran özellik: üstte geniş kart, disk şeridi kayar, ortadaki pencerede döner ve adı değişir. Altta üç küçük kare. En az yer kaplayan yön.</p>
    <p class="ust-yazi">Sihirli özellikler</p>
    <a class="c-genis" href="#diskler"><span><b>6 + 6 masal diski</b><span class="t">Altısı hediye. Diski tak, masal tavana yansısın. <u>Diskleri gör</u></span></span><span class="ek">""" + ui_serit() + """</span></a>
    <div class="c-uc">""" + ''.join('<div class="c-kare"><span class="ek">%s</span><b>%s</b></div>' % (k[3](), k[1]) for k in OZ[1:]) + """</div>
  </section>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { b: 0 }; }
  componentDidMount() {
    // B: etkin satır 5 sn'de bir sıradakine geçer; dokununca 12 sn bekler. Azaltılmış harekette kendiliğinden geçmez.
    var self = this;
    if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    this.iv = setInterval(function () { if (Date.now() - (self.dok || 0) < 12000) return; self.setState({ b: (self.state.b + 1) % 4 }); }, 5000);
  }
  componentWillUnmount() { clearInterval(this.iv); }
  renderVals() {
    var self = this, S = this.state, o = {};
    for (var i = 0; i < 4; i++) (function (i) { var on = i === S.b;
      o['b' + i] = 'b-sahne' + (on ? ' on' : ''); o['bg' + i] = on ? 'false' : 'true';
      o['bs' + i] = 'b-sat' + (on ? ' on' : ''); o['bp' + i] = on ? 'true' : 'false';
      o['bsec' + i] = function () { self.dok = Date.now(); self.setState({ b: i }); }; })(i);
    return o;
  }
}"""

open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · Sihirli özellikler yönleri', css=CSS) + HTML + TAIL.format(h=int(os.environ.get('S2_H', 1500)), js=JS))
print('yazıldı:', os.path.abspath(OUT))
