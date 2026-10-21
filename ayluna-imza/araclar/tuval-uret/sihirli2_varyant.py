# Sihirli Özellikler · kurumsal mini arayüz sekansları, 3 yön (21 Eki). Çalıştır: python3 sihirli2_varyant.py
# Kullanıcı: "Şu emoji benefit kısmını vesaire biraz daha kurumsal yapsak ve UI'lerle doldursak daha profesyonel görünsün;
# mesela dönen diskler sırayla masal diskini gidip gelse gibi tatlı ufak sekanslar."
# Önceki kararlar korunur (17 Eki): kartlar beyaz, koyu ve amber dolu kart yok, gölge yok; amber yalnız hareket eden parçada.
# Eleştirmen (1. tur): A 7, C 6, B 4. Düzeltmeleri işlendi:
#   - Disk şeridi (pencere + iki yanda soluk komşular .85): disk yalnız kayarken yuvarlanır (adım başına 90°), durunca sabit
#     (sürekli dönen disk "tavanda dönen desen" vaadi gibi okunuyordu). Kayma 0,6 sn, geçişte pencere halkası .4.
#   - Şarj: lacivert pil 4 dilimle dolar, fiş çıkar; lamba "Şarj oluyor"da sönük, "Kablosuz"da yanar
#     ("şarj olurken çalışır" teyitli değil, çizilmez). Güneş gibi okunan amber halka kalktı.
#   - Lamba ikonu LunaDream Kız'a benzer: tepe topuzu, 5 dalgalı kubbe, ışıklı gövde, yarım çanak taban, iki kıvrık ayak.
#     (Sayfada Erkek seçilince robot ikonu gelir.)
#   - Ses çubukları 2,4 sn (V1'de onaylı hız). Kartlar 0,6 sn arayla başlar. Cümleler kısa, 14 px.
#   - B: bütün satırlarda cümle tek satır (zıplama yok), ekran 112 px, ölçek 1,2, 7 sn'de geçer, dokununca durur.
#   - C: küçük karelerde gösterge lambanın altında, kenara 8 px'ten yakın değil; başlığın altında tek satır.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE-Sihirli2.dc.html')

E = 'cubic-bezier(.2,.7,.2,1)'
DISK = [('Okyanus', 'a24f13e032569f76d64b9b0fbe8d74f7'), ('Uzay', 'b088d2c82561b76f6db997fbc3944059'),
        ('Deniz kızı', '04ed9ce4ae8a36619975caa7d2de9ad8'), ('Şato', 'bbd010d8d946edc8fef9c0404cba4ea2')]

# LunaDream Kız çizgi ikonu: topuz, 5 dalgalı kubbe, ışıklı gövde (amber, yalnız ışık), yarım çanak taban, iki kıvrık ayak
LAMBA = ('<svg class="lmb" viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="3.6" r="1.5"></circle>'
         '<path class="kb" d="M6 13C6 8.4 10.5 5.4 16 5.4S26 8.4 26 13a2 2 0 0 1-4 0 2 2 0 0 1-4 0 2 2 0 0 1-4 0 2 2 0 0 1-4 0 2 2 0 0 1-4 0z"></path>'
         '<rect class="isk" x="10" y="14.6" width="12" height="6.2" rx="1.2"></rect><path d="M9.5 14.5v6.5M22.5 14.5v6.5"></path>'
         '<path d="M8 21h16c0 2.9-3.6 4.6-8 4.6S8 23.9 8 21z"></path><path d="M11.4 25.3c-.4 1.5-1.6 2.2-2.8 1.9M20.6 25.3c.4 1.5 1.6 2.2 2.8 1.9"></path></svg>')
# LunaDream Erkek (Uzay Kaşifi) çizgi ikonu: anten, kubbe baş, koyu yüz paneli ve amber gözler (ışık), gövde, palet
ROBOT = ('<svg class="lmb rb" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 6.4V4"></path><circle cx="16" cy="3" r="1.2"></circle>'
         '<path class="kb" d="M7.5 16a8.5 8.5 0 0 1 17 0z"></path><rect x="10" y="9.6" width="12" height="5.2" rx="2.6" fill="#1A2142"></rect>'
         '<circle class="isk" cx="13.6" cy="12.2" r="1.1"></circle><circle class="isk" cx="18.4" cy="12.2" r="1.1"></circle>'
         '<path d="M8.5 16h15v4h-15z"></path><rect x="6" y="20" width="20" height="6.4" rx="3.2"></rect><circle cx="10.4" cy="23.2" r="1.4"></circle><circle cx="16" cy="23.2" r="1.4"></circle><circle cx="21.6" cy="23.2" r="1.4"></circle></svg>')
# Sayfada modele bağlı: Kız seçiliyken atlıkarınca, Erkek seçiliyken robot (renderVals: sihKiz / sihErkek)
IKON = ('<sc-if value="{{sihKiz}}" hint-placeholder-val="{{true}}">' + LAMBA + '</sc-if>'
        '<sc-if value="{{sihErkek}}" hint-placeholder-val="{{false}}">' + ROBOT + '</sc-if>')
TEL = '<svg class="tel" viewBox="0 0 24 24" aria-hidden="true"><rect x="7" y="2.5" width="10" height="19" rx="2.5"></rect><path d="M11 18.5h2"></path></svg>'
FIS = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12h-7M14 8.5H9a2 2 0 0 0-2 2v3a2 2 0 0 0 2 2h5zM7 10.5H4M7 13.5H4"></path></svg>'


def ui_isik(kucuk=False):
    return ('<span class="ui ui-isik%s" aria-hidden="true"><span class="hl hl3"></span><span class="hl hl2"></span><span class="hl hl1"></span>' % (' kucuk' if kucuk else '') + IKON +
            '<span class="kad"><i></i><i></i><i></i><b></b></span></span>')


def ui_serit(boy, diskler=None):  # boy: 'b' büyük (46 px disk) | 'k' küçük (38 px disk); diskler: [(ad, blob id)] × 4
    dl = diskler or DISK
    ds = dl + dl[:1]
    return ('<span class="ui ui-serit serit-%s" aria-hidden="true"><span class="pencere"></span><span class="tren">' % boy +
            ''.join('<span class="sd"><img src="/_blob/%s" alt=""></span>' % i for _, i in ds) + '</span>'
            '<span class="adlar">' + ''.join('<i class="a%d">%s</i>' % (k + 1, n) for k, (n, _) in enumerate(dl)) + '</span></span>')


def ui_bt(kucuk=False):
    if kucuk:
        return '<span class="ui ui-bt kucuk" aria-hidden="true">' + IKON + '<span class="eq"><i></i><i></i><i></i><i></i></span></span>'
    return ('<span class="ui ui-bt" aria-hidden="true"><span class="bt-sira">' + TEL + '<span class="akis"><i></i><i></i><i></i></span>' + IKON +
            '<span class="eq"><i></i><i></i><i></i><i></i></span></span><span class="bt-alt"><span class="durum"><i>Bağlanıyor</i><i>Ninni çalıyor</i></span>'
            '<span class="cal"><b></b></span></span></span>')


def ui_sarj(kucuk=False):
    return ('<span class="ui ui-sarj%s" aria-hidden="true"><span class="sarj-sira">' % (' kucuk' if kucuk else '') + IKON +
            '<span class="pil"><i></i><i></i><i></i><i></i></span><span class="fis">' + FIS + '</span></span>' +
            ('' if kucuk else '<span class="durum"><i>Şarj oluyor</i><i>Kablosuz</i></span>') + '</span>')


# (anahtar, başlık, kısa cümle, tek satır (B ve C), mini arayüz)
OZ = [
    ('disk', '6 + 6 masal diski', 'Altısı hediye.', 'Altısı hediye', lambda: ui_serit('k')),
    ('isik', '3 parlaklık', 'Kısık, orta, parlak.', 'Kısık · orta · parlak', ui_isik),
    ('bt', 'Bluetooth ninni', 'Telefondan bağlan, çalsın.', 'Telefondan çalar', ui_bt),
    ('sarj', 'Şarjlı, kablosuz', 'Her odaya taşı.', 'Her odaya taşı', ui_sarj),
]

# Disk şeridi (USB sayfası da kullanır; adlar ve disk listesi ui_serit parametresi)
SERIT_CSS = r"""/* Disk şeridi: her 2 sn bir disk kayar (0,6 sn), kayarken 90° yuvarlanır, durunca sabit; ortadaki pencerede, komşular .85 ve soluk */
.ui-serit{position:relative;display:block;flex:none;--d:46px;--adim:50px;--pad:65px;width:176px;height:78px;overflow:hidden}
.ui-serit.serit-k{--d:38px;--adim:42px;--pad:60px;width:158px;height:62px}
.pencere{position:absolute;left:calc(var(--pad) - 4px);top:0;width:calc(var(--d) + 8px);height:calc(var(--d) + 8px);border-radius:50%;box-shadow:0 0 0 1.5px #1A2142;background:#FFFDF9;animation:pen 8s EASE infinite;animation-delay:var(--gec,0s)}
.tren{position:absolute;left:0;top:4px;display:flex;gap:calc(var(--adim) - var(--d));padding-left:var(--pad);animation:tren 8s EASE infinite;animation-delay:var(--gec,0s)}
.sd{flex:none;width:var(--d);height:var(--d);transform:scale(.85);opacity:.5}
.sd img{display:block;width:var(--d);height:var(--d);border-radius:50%;object-fit:cover;animation:yuvar 8s EASE infinite;animation-delay:var(--gec,0s)}
.sd:nth-child(1){transform:none;opacity:1}
.sd:nth-child(1){animation:sd1 8s EASE infinite}.sd:nth-child(2){animation:sd2 8s EASE infinite}.sd:nth-child(3){animation:sd3 8s EASE infinite}.sd:nth-child(4){animation:sd4 8s EASE infinite}.sd:nth-child(5){animation:sd5 8s EASE infinite}
.sd{animation-delay:var(--gec,0s)!important}
@keyframes tren{0%,18%{transform:none}25.5%,43%{transform:translateX(calc(var(--adim) * -1))}50.5%,68%{transform:translateX(calc(var(--adim) * -2))}75.5%,93%{transform:translateX(calc(var(--adim) * -3))}100%{transform:translateX(calc(var(--adim) * -4))}}
@keyframes yuvar{0%,18%{transform:none}25.5%,43%{transform:rotate(-90deg)}50.5%,68%{transform:rotate(-180deg)}75.5%,93%{transform:rotate(-270deg)}100%{transform:rotate(-360deg)}}
@keyframes pen{0%,18%{opacity:1}21.75%{opacity:.4}25.5%,43%{opacity:1}46.75%{opacity:.4}50.5%,68%{opacity:1}71.75%{opacity:.4}75.5%,93%{opacity:1}96.75%{opacity:.4}100%{opacity:1}}
@keyframes sd1{0%,18%{transform:none;opacity:1}25.5%,100%{transform:scale(.85);opacity:.5}}
@keyframes sd2{0%,18%{transform:scale(.85);opacity:.5}25.5%,43%{transform:none;opacity:1}50.5%,100%{transform:scale(.85);opacity:.5}}
@keyframes sd3{0%,43%{transform:scale(.85);opacity:.5}50.5%,68%{transform:none;opacity:1}75.5%,100%{transform:scale(.85);opacity:.5}}
@keyframes sd4{0%,68%{transform:scale(.85);opacity:.5}75.5%,93%{transform:none;opacity:1}100%{transform:scale(.85);opacity:.5}}
@keyframes sd5{0%,93%{transform:scale(.85);opacity:.5}100%{transform:none;opacity:1}}
.adlar{position:absolute;left:0;right:0;bottom:0;display:grid;font-size:12px;font-weight:600;color:#1A2142;white-space:nowrap}
.adlar i{grid-area:1/1;justify-self:center;font-style:normal;opacity:0;animation:adk 8s EASE infinite both}
.adlar .a1{opacity:1;animation-delay:var(--gec,0s)}
.adlar .a2{animation-delay:calc(var(--gec,0s) + 2s)}.adlar .a3{animation-delay:calc(var(--gec,0s) + 4s)}.adlar .a4{animation-delay:calc(var(--gec,0s) + 6s)}
@keyframes adk{0%{opacity:0;transform:translateY(4px)}3%,18%{opacity:1;transform:none}22%,100%{opacity:0;transform:translateY(-4px)}}

""".replace('EASE', E)

MINI_CSS = r"""/* Ortak mini arayüz (Sihirli özellikler, luna_e.py da kullanır). (.sh-ek: sayfadaki .ek ile çakışmasın). Zemin ton #F1E8DA, çizgi lacivert 1,5 px, ışık amber */
.sh-ek{position:relative;display:flex;align-items:center;justify-content:center;overflow:hidden;border-radius:14px;background:#F1E8DA}
.ui{position:relative;display:block;flex:none}
.lmb{width:30px;height:30px;fill:none;stroke:#1A2142;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.lmb .kb{fill:#FFFDF9}
.lmb .isk{fill:#F2A65A;stroke:none;opacity:.9}
.tel{width:22px;height:22px;fill:none;stroke:#1A2142;stroke-width:1.5;stroke-linecap:round}
.durum{position:relative;display:grid;font-size:12px;font-weight:600;color:#5C6078;white-space:nowrap}
.durum i{grid-area:1/1;font-style:normal}

/* Parlaklık: 3 kademe (6 sn). Duran kare: üçüncü kademe */
.ui-isik{width:120px;height:64px}
.ui-isik .lmb{position:absolute;left:15px;top:17px}
.ui-isik .hl{position:absolute;left:30px;top:32px;border-radius:50%;border:1.5px solid #F2A65A}
.ui-isik .hl1{width:40px;height:40px;margin:-20px 0 0 -20px;opacity:.9}
.ui-isik .hl2{width:54px;height:54px;margin:-27px 0 0 -27px;opacity:.55;animation:l2 6s EASE infinite;animation-delay:var(--gec,0s)}
.ui-isik .hl3{width:68px;height:68px;margin:-34px 0 0 -34px;opacity:.3;animation:l3 6s EASE infinite;animation-delay:var(--gec,0s)}
.ui-isik .isk{animation:lisk 6s EASE infinite;animation-delay:var(--gec,0s)}
@keyframes l2{0%,30%{opacity:0;transform:scale(.8)}37%,92%{opacity:.55;transform:none}100%{opacity:0;transform:scale(.8)}}
@keyframes l3{0%,63%{opacity:0;transform:scale(.8)}70%,92%{opacity:.3;transform:none}100%{opacity:0;transform:scale(.8)}}
@keyframes lisk{0%,30%{opacity:.35}37%,63%{opacity:.65}70%,92%{opacity:1}100%{opacity:.35}}
.kad{position:absolute;right:0;top:26px;display:flex;gap:8px;padding:4px 6px;border-radius:999px;background:#FFFDF9}
.kad i{width:6px;height:6px;border-radius:50%;background:#D6CAB6}
.kad b{position:absolute;left:4px;top:2px;width:10px;height:10px;border-radius:50%;background:#F2A65A;transform:translateX(28px);animation:kad 6s EASE infinite;animation-delay:var(--gec,0s)}
@keyframes kad{0%,30%{transform:none}37%,63%{transform:translateX(14px)}70%,92%{transform:translateX(28px)}100%{transform:none}}
/* küçük karede gösterge lambanın altında */
.ui-isik.kucuk{width:76px;height:76px}
.ui-isik.kucuk .lmb{left:23px;top:8px}
.ui-isik.kucuk .hl{left:38px;top:23px}
.ui-isik.kucuk .hl3{width:60px;height:60px;margin:-30px 0 0 -30px}
.ui-isik.kucuk .kad{right:auto;left:12px;top:56px}

""".replace('EASE', E) + SERIT_CSS + r"""/* Bluetooth: bağlan (0-35%) → çal (38-94%). Duran kare: çalıyor, ilerleme yarıda */
.ui-bt{width:136px;display:flex;flex-direction:column;gap:6px}
.bt-sira{display:flex;align-items:center;gap:4px;height:34px}
.ui-bt .lmb{width:28px;height:28px}
.akis{position:relative;width:30px;height:6px}
.akis i{position:absolute;left:0;top:1px;width:4px;height:4px;border-radius:50%;background:#1A2142;opacity:0;animation:akis 6s EASE infinite;animation-delay:var(--gec,0s)}
.akis i:nth-child(2){animation-delay:calc(var(--gec,0s) + .25s)}.akis i:nth-child(3){animation-delay:calc(var(--gec,0s) + .5s)}
@keyframes akis{0%{transform:none;opacity:0}4%{opacity:1}22%{transform:translateX(26px);opacity:0}23%{transform:none;opacity:0}27%{opacity:1}34%{transform:translateX(26px);opacity:0}100%{transform:translateX(26px);opacity:0}}
.eq{display:flex;align-items:flex-end;gap:2px;height:18px;margin-left:2px;animation:btg 6s EASE infinite;animation-delay:var(--gec,0s)}
.eq i{width:3px;height:18px;border-radius:2px;background:#F2A65A;transform-origin:50% 100%;transform:scaleY(.5);animation:ses 2.4s ease-in-out infinite}
.eq i:nth-child(2){animation-delay:-.6s}.eq i:nth-child(3){animation-delay:-1.2s}.eq i:nth-child(4){animation-delay:-1.8s}
@keyframes ses{0%,100%{transform:scaleY(.3)}50%{transform:scaleY(1)}}
@keyframes btg{0%,35%{opacity:0}40%,92%{opacity:1}100%{opacity:0}}
.bt-alt{display:flex;flex-direction:column;gap:4px}
.ui-bt .durum i:first-child{opacity:0;animation:d1 6s EASE infinite;animation-delay:var(--gec,0s)}
.ui-bt .durum i:last-child{animation:d2 6s EASE infinite;animation-delay:var(--gec,0s)}
@keyframes d1{0%,33%{opacity:1}38%,100%{opacity:0}}
@keyframes d2{0%,35%{opacity:0}40%,94%{opacity:1}100%{opacity:0}}
.cal{position:relative;height:3px;border-radius:2px;background:#E3D8C7;overflow:hidden}
.cal b{position:absolute;inset:0;border-radius:2px;background:#1A2142;transform-origin:0 50%;transform:scaleX(.5);animation:cal 6s linear infinite;animation-delay:var(--gec,0s)}
@keyframes cal{0%,38%{transform:scaleX(0)}94%{transform:scaleX(1)}100%{transform:scaleX(0)}}
.ui-bt.kucuk{width:76px;height:76px;align-items:center;justify-content:center;gap:8px}
.ui-bt.kucuk .eq{animation:none;height:16px;margin:0}

/* Şarj: pil 4 dilimle dolar, fiş çıkar; lamba "Şarj oluyor"da sönük, "Kablosuz"da yanar (6 sn). Duran kare: dolu, kablosuz, yanık */
.ui-sarj{width:136px;display:flex;flex-direction:column;align-items:flex-start;gap:6px}
.sarj-sira{display:flex;align-items:center;gap:8px;height:34px}
.ui-sarj .lmb{width:28px;height:28px}
.ui-sarj .isk{animation:sisk 6s EASE infinite;animation-delay:var(--gec,0s)}
@keyframes sisk{0%,58%{opacity:.2}64%,92%{opacity:1}100%{opacity:.2}}
.pil{position:relative;display:flex;gap:2px;width:42px;height:20px;padding:2.5px;border:1.5px solid #1A2142;border-radius:6px}
.pil::after{content:"";position:absolute;right:-5px;top:5px;width:3px;height:7px;border-radius:0 2px 2px 0;background:#1A2142}
.pil i{flex:1;border-radius:2px;background:#1A2142;animation:dilim 6s EASE infinite both}
.pil i:nth-child(1){animation-name:pl1}.pil i:nth-child(2){animation-name:pl2}.pil i:nth-child(3){animation-name:pl3}.pil i:nth-child(4){animation-name:pl4}
.pil i{animation-delay:var(--gec,0s)}
@keyframes pl1{0%{opacity:.12}10%,94%{opacity:1}100%{opacity:.12}}
@keyframes pl2{0%,10%{opacity:.12}22%,94%{opacity:1}100%{opacity:.12}}
@keyframes pl3{0%,22%{opacity:.12}34%,94%{opacity:1}100%{opacity:.12}}
@keyframes pl4{0%,34%{opacity:.12}46%,94%{opacity:1}100%{opacity:.12}}
.fis{width:22px;height:22px;margin-left:-2px;opacity:0;animation:fis 6s EASE infinite;animation-delay:var(--gec,0s)}
.fis svg{width:22px;height:22px;fill:none;stroke:#1A2142;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
@keyframes fis{0%,56%{transform:none;opacity:1}64%,94%{transform:translateX(12px);opacity:0}100%{transform:none;opacity:1}}
.ui-sarj .durum i:first-child{opacity:0;animation:s1 6s EASE infinite;animation-delay:var(--gec,0s)}
.ui-sarj .durum i:last-child{animation:s2 6s EASE infinite;animation-delay:var(--gec,0s)}
@keyframes s1{0%,58%{opacity:1}64%,100%{opacity:0}}
@keyframes s2{0%,60%{opacity:0}66%,94%{opacity:1}100%{opacity:0}}
.ui-sarj.kucuk{width:76px;height:76px;align-items:center;justify-content:center}
.ui-sarj.kucuk .sarj-sira{flex-direction:column;height:auto;gap:6px}
.ui-sarj.kucuk .fis{display:none}

/* A · Canlı kartlar: ekran 72 px, kartlar 0,6 sn arayla başlar */
.a-izgara{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:12px}
.a-kart{display:flex;flex-direction:column;gap:10px;padding:8px 8px 12px;border-radius:20px;background:#FFFDF9;border:1px solid #E3D8C7;color:#1A2142;text-decoration:none}
.a-kart:nth-child(2){--gec:.6s}.a-kart:nth-child(3){--gec:1.2s}.a-kart:nth-child(4){--gec:1.8s}
.a-kart .sh-ek{height:72px}
.a-kart b{display:block;padding:0 6px;font-size:15px;line-height:1.25}
.a-kart span.t{display:block;margin-top:2px;padding:0 6px;font-size:14px;line-height:1.4;color:#5C6078}
.a-kart u{color:#A05A1C;text-underline-offset:3px;text-decoration-thickness:1px}

""".replace('EASE', E)

PANO_CSS = r""".pg{background:#F6F1E9;font-size:15px}
.sec{padding:0 16px 40px}
.oneri{display:flex;align-items:center;gap:8px;margin:0 0 6px;padding-top:16px;border-top:1px dashed #D6CAB6;font-size:12px;font-weight:700;color:#A05A1C}
.oneri-alt{margin:0 0 16px;font-size:13px;color:#5C6078;text-wrap:balance}
.ust-yazi{margin:0;font-size:13px;font-weight:700;color:#A05A1C}
.pg button{font:inherit;cursor:pointer;-webkit-tap-highlight-color:transparent}
.pg :focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
img{display:block}
u{color:#A05A1C;text-underline-offset:3px;text-decoration-thickness:1px}

/* C · Bento: geniş disk kartı + üç küçük kare (gösterge lambanın altında, başlığın altında tek satır) */
.c-genis{display:grid;grid-template-columns:minmax(0,1fr) 176px;align-items:center;gap:12px;margin-top:12px;padding:10px 10px 10px 16px;border-radius:20px;background:#FFFDF9;border:1px solid #E3D8C7;color:#1A2142;text-decoration:none}
.c-genis b{display:block;font-size:16px;line-height:1.25}
.c-genis span.t{display:block;margin-top:4px;font-size:14px;line-height:1.4;color:#5C6078}
.c-genis .sh-ek{height:100px}
.c-uc{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:8px}
.c-kare{display:flex;flex-direction:column;gap:8px;padding:8px 8px 12px;border-radius:18px;background:#FFFDF9;border:1px solid #E3D8C7}
.c-kare:nth-child(2){--gec:.6s}.c-kare:nth-child(3){--gec:1.2s}
.c-kare .sh-ek{height:88px}
.c-kare b{display:block;padding:0 2px;font-size:14px;line-height:1.25}
.c-kare span.t{display:block;padding:0 2px;font-size:13px;line-height:1.3;color:#5C6078}

/* B · Özellik turu: tek ekran (112 px), 4 satır; her satırda tek satır cümle; etkin satırın çizgisi 7 sn'de dolar */
.b-kutu{margin-top:12px;border-radius:20px;background:#FFFDF9;border:1px solid #E3D8C7;overflow:hidden}
.b-ekran{position:relative;height:112px;margin:10px 10px 0;border-radius:14px;background:#F1E8DA}
.b-sahne{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0;transform:translateY(6px);transition:opacity .35s EASE,transform .35s EASE}
.b-sahne.on{opacity:1;transform:none}
.b-sahne .ui{transform:scale(1.2)}
.b-liste{list-style:none;margin:0;padding:4px 0 6px}
.b-sat{position:relative;display:flex;align-items:baseline;gap:8px;width:100%;min-height:52px;padding:14px 16px;border:0;background:none;text-align:left;color:#1A2142;opacity:.6}
.b-sat.on{opacity:1}
.b-sat+.b-sat{border-top:1px solid #EFE6D8}
.b-sat b{font-size:15px;line-height:1.25;white-space:nowrap}
.b-sat .t{font-size:14px;line-height:1.25;color:#5C6078;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.b-sat .cz{position:absolute;left:16px;right:16px;bottom:0;height:2px;background:#F2A65A;transform-origin:0 50%;transform:scaleX(0)}
.b-sat.on .cz{animation:bcz 7s linear forwards}
.b-sat.on.dur .cz{animation:none;transform:none}
@keyframes bcz{to{transform:scaleX(1)}}
""".replace('EASE', E)
CSS = PANO_CSS + MINI_CSS



def kart_a(k):
    a, b, t, _, f = k
    if a == 'disk':
        return '<a class="a-kart" href="#diskler"><span class="sh-ek">%s</span><span><b>%s</b><span class="t">%s <u>Diskleri gör</u></span></span></a>' % (f(), b, t)
    return '<div class="a-kart"><span class="sh-ek">%s</span><span><b>%s</b><span class="t">%s</span></span></div>' % (f(), b, t)


KUCUK = {'isik': lambda: ui_isik(True), 'bt': lambda: ui_bt(True), 'sarj': lambda: ui_sarj(True)}
BUYUK = {'disk': lambda: ui_serit('b'), 'isik': ui_isik, 'bt': ui_bt, 'sarj': ui_sarj}

HTML = """<div class="pg">
  <div style="padding: 18px 16px 10px">
    <h1 class="h2" style="font-size: 22px">Sihirli özellikler · eleştirmenin sırası</h1>
    <p style="margin: 6px 0 0; font-size: 13px; color: #5C6078">Satın alma kutusunda, fiyatın altında. Her özellik kendi küçük sekansıyla: diskler sırayla kayar ve yuvarlanır, parlaklık üç kademe, Bluetooth bağlanıp çalar, pil dolar ve fiş çıkar. Kartlar beyaz, amber yalnız ışıkta.</p>
  </div>

  <section class="sec">
    <p class="oneri">1 · Canlı kartlar · 7/10</p>
    <p class="oneri-alt">Bugünkü 2×2 düzen kalır; her kartın üstünde küçük bir ürün ekranı. Dört özellik aynı anda okunur. Kartlar 0,6 sn arayla başlar.</p>
    <p class="ust-yazi">Sihirli özellikler</p>
    <div class="a-izgara">""" + ''.join(kart_a(k) for k in OZ) + """</div>
  </section>

  <section class="sec">
    <p class="oneri">2 · Bento · 6/10</p>
    <p class="oneri-alt">Ürünü ayıran diskler üstte geniş kartta; altta üç küçük kare. Bugünkü yükseklikte kalır, ödeme düğmesini aşağı itmez.</p>
    <p class="ust-yazi">Sihirli özellikler</p>
    <a class="c-genis" href="#diskler"><span><b>6 + 6 masal diski</b><span class="t">Altısı hediye. Diski tak, tavana yansısın. <u>Diskleri gör</u></span></span><span class="sh-ek">""" + ui_serit('b') + """</span></a>
    <div class="c-uc">""" + ''.join('<div class="c-kare"><span class="sh-ek">%s</span><b>%s</b><span class="t">%s</span></div>' % (KUCUK[k[0]](), k[1], k[3]) for k in OZ[1:]) + """</div>
  </section>

  <section class="sec">
    <p class="oneri">3 · Özellik turu · 4/10</p>
    <p class="oneri-alt">Tek ekran, altında dört satır; etkin satırın çizgisi 7 sn'de dolar, sıradakine geçer; dokununca durur. Eleştirmen: satın alma kutusunda bekletiyor.</p>
    <p class="ust-yazi">Sihirli özellikler</p>
    <div class="b-kutu">
      <div class="b-ekran">""" + ''.join('<div class="{{b%d}}" aria-hidden="{{bg%d}}">%s</div>' % (i, i, BUYUK[k[0]]()) for i, k in enumerate(OZ)) + """</div>
      <ul class="b-liste">""" + ''.join('<li><button class="{{bs%d}}" type="button" onClick="{{bsec%d}}" aria-pressed="{{bp%d}}"><b>%s</b><span class="t">%s</span><span class="cz" aria-hidden="true"></span></button></li>' % (i, i, i, k[1], k[3]) for i, k in enumerate(OZ)) + """</ul>
    </div>
  </section>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { b: 0, dur: false }; }
  componentDidMount() {
    // 3 · Özellik turu: 7 sn'de bir sıradakine geçer; dokununca kalıcı durur. Azaltılmış harekette kendiliğinden geçmez.
    var self = this;
    if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    this.iv = setInterval(function () { if (!self.state.dur) self.setState({ b: (self.state.b + 1) % 4 }); }, 7000);
  }
  componentWillUnmount() { clearInterval(this.iv); }
  renderVals() {
    var self = this, S = this.state, o = { sihKiz: true, sihErkek: false };
    for (var i = 0; i < 4; i++) (function (i) { var on = i === S.b;
      o['b' + i] = 'b-sahne' + (on ? ' on' : ''); o['bg' + i] = on ? 'false' : 'true';
      o['bs' + i] = 'b-sat' + (on ? ' on' : '') + (on && S.dur ? ' dur' : ''); o['bp' + i] = on ? 'true' : 'false';
      o['bsec' + i] = function () { self.setState({ b: i, dur: true }); }; })(i);
    return o;
  }
}"""

if __name__ == '__main__':
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · Sihirli özellikler yönleri', css=CSS) + HTML + TAIL.format(h=int(os.environ.get('S2_H', 1705)), js=JS))
    print('yazıldı:', os.path.abspath(OUT))
