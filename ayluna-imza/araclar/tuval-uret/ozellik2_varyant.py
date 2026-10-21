# LunaDream · "Neler yapabiliyor?" 2. tur (21 Eki). Çalıştır: python3 ozellik2_varyant.py
# Kullanıcı (1. tur Satırlar / Sekmeler / Kaydırmalı için): "Hayır, o da çok boğar; daha iyi bir şeyler mi düşünsek, çok sıkıcı duruyor böyle."
# Liste düzeni tamamen çıkar: ürün büyük, yazı en az. "Işığı aç/kapat" anahtarı yok (17 Eki).
# İlk taslak (A Yörünge 7/5, B Etiketli ürün 6/6, C Masal kitabı 5/3; git geçmişinde d090a34). Eleştirmenin üç seçimi:
#   1 · Aydınlık sahne: B'nin büyük stüdyo fotoğrafı + A'nın etkileri lambanın çevresinde (halkalar, ses dalgaları, rozetler).
#   2 · Gece kadranı: A sadeleşti; düğüm daireleri yok, yayda dört yazı, amber ay noktası yazıdan yazıya; pencere 200 px.
#   3 · Etiketli ürün (güvenli yedek): fotoğraf, dört eylem etiketi, altta tek cümle.
# Kullanıcı 1 · Aydınlık sahne'yi seçti (21 Eki); luna_e.py bu dosyadan NZ_CSS, sahne(), js_degerler(), js_tur() alır.
# Eleştirmen düzeltmeleri (hepsine):
#   - Etiketler eylem ("Diski tak", "Işığı kıs", "Ninni çal", "Kablosuz kullan"): Sihirli'nin "ne" kartlarını tekrar etmez.
#   - "[X] ışık seçeneği" sayfada yok; "Üç kademe: kısık, orta, parlak." (3 kademe teyitli).
#   - Disk lambanın tepesine inmez (takıldığı yer çizilmez); disk rozette belirir. Gece fotoğrafı yok (Videolar gösteriyor).
#   - Her durum 6 sn; sekanslar bir kez oynar ve son karede kalır. Ekrana girince tek tur (24 sn), Masal'da durur; dokununca durur.
#     Azaltılmış harekette ilerlemez. Yeni sonsuz döngü yok.
#   - Etkin etiket: lacivert dolgu katmanı (opacity); renk ve gölge canlandırılmaz. Pasif yazılar opak gri, yarı saydam değil.
#   - "Kabloyu çıkar, odaya taşı" yerine "kablo takılı değilken de yanar" (pil süresi ima edilmez).
# Sahne kapsayıcı genişliğine bağlı (cqw; 358 px tabanı): 343 px telefonda ve masaüstündeki 398 px sütunda aynı oranla kurulur.
# Sınıflar nz- önekli (sayfada .ek ve .hk başka işte).
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL
import sihirli2_varyant as S2
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE-Ozellik2.dc.html')

E = 'cubic-bezier(.2,.7,.2,1)'
FOTO = {'kiz': 'e02351b3be4a1c555c5d760d0bbda723', 'erkek': '0033dfea6282c5bc479c385213661c00'}
DISK = {'kiz': ('4a3a69e8c1d8dddad8c33f8f463b8a0e', 'Ay ve yıldız'), 'erkek': ('b088d2c82561b76f6db997fbc3944059', 'Uzay')}


def model(f):  # sayfada modele bağlı (renderVals: sihKiz / sihErkek)
    return ('<sc-if value="{{sihKiz}}" hint-placeholder-val="{{true}}">' + f('kiz') + '</sc-if>'
            '<sc-if value="{{sihErkek}}" hint-placeholder-val="{{false}}">' + f('erkek') + '</sc-if>')


OZ = [  # (anahtar, eylem etiketi, kadran adı, başlık (2), cümle)
    ('masal', 'Diski tak', 'Masal', 'Diski tak, tavana yansısın', 'Diski tak; masal tavana yansısın.'),
    ('isik', 'Işığı kıs', 'Işık', 'Uyurken en kısığa al', 'Üç kademe: kısık, orta, parlak.'),
    ('ninni', 'Ninni çal', 'Ninni', 'Telefondan ninni çal', 'Telefondan bağla; ninni lambadan çalsın.'),
    ('sarj', 'Kablosuz kullan', 'Şarj', 'Şarj et, kablosuz kullan', 'Kablo takılı değilken de yanar.'),
]

# Rozetler (lambanın altında; etkin duruma göre biri görünür)
ROZET = ('<div class="nz-rzy" aria-hidden="true"><span class="nz-rz nz-disk">' + model(lambda m: '<img src="/_blob/%s" alt=""><b>%s diski</b>' % DISK[m]) + '</span>'
         '<span class="nz-rz nz-kad">' + ''.join('<i><span>%s</span><span class="e">%s</span></i>' % (w, w) for w in ('Kısık', 'Orta', 'Parlak')) + '</span>'
         '<span class="nz-rz nz-cal"><span class="eq"><i></i><i></i><i></i><i></i></span><b>Ninni çalıyor</b></span>'
         '<span class="nz-rz nz-pil"><span class="nz-rbat"><i></i><i></i><i></i><i></i></span><span class="durum"><i>Şarj oluyor</i><i>Kablosuz</i></span></span></div>')
HALKA = '<div class="nz-hk" aria-hidden="true"><i></i><i></i><i></i></div>'
DALGA = '<div class="nz-dl" aria-hidden="true"><span class="sol"><i></i><i></i><i></i></span><span class="sag"><i></i><i></i><i></i></span></div>'

# Etiketteki minik simge (etkinken bir kez oynar)
EK_IK = {
    'masal': model(lambda m: '<img class="nz-dsk" src="/_blob/%s" alt="">' % DISK[m][0]),
    'isik': '<span class="nz-kd"><i></i><i></i><i></i></span>',
    'ninni': '<span class="eq nz-eq"><i></i><i></i><i></i><i></i></span>',
    'sarj': '<span class="nz-bat"><i></i><i></i><i></i></span>',
}


def foto():
    return model(lambda m: '<img class="nz-img" src="/_blob/%s" alt="LunaDream %s modeli, stüdyo çekimi" loading="lazy">' % (FOTO[m], 'Kız' if m == 'kiz' else 'Erkek'))


def etiketler(k):  # üstte iki, altta iki köşe
    pos = ['left: 12px; top: 14px', 'right: 12px; top: 14px', 'left: 12px; bottom: 12px', 'right: 12px; bottom: 12px']
    return ''.join('<button class="{{%sc%d}}" type="button" style="%s" onClick="{{%sg%d}}" aria-pressed="{{%sp%d}}"><span class="nz-ik">%s</span><span class="nz-ad">%s</span></button>'
                   % (k, i, pos[i], k, i, k, i, EK_IK[o[0]], o[1]) for i, o in enumerate(OZ))


def cumle(k):
    return '<div class="nz-metin" aria-live="polite">' + ''.join('<p class="{{%sm%d}}" aria-hidden="{{%sh%d}}">%s</p>' % (k, i, k, i, o[4]) for i, o in enumerate(OZ)) + '</div>'


def sahne(k='nz', sade=False):
    """1 · Aydınlık sahne (sade=True: 3 · Etiketli ürün, etkisiz). k: durum ve renderVals öneki."""
    etki = '' if sade else HALKA + DALGA + ROZET
    return ('<div class="{{%sCls}}" data-tur="%s"><div class="nz-ft">' % (k, k) + foto() + '</div>' + etki + etiketler(k) + '</div>' + cumle(k))


def js_degerler(k='nz', sade=False):
    """renderVals içinde: self ve S tanımlı; sonuç nesnesi <k>V (dönüş nesnesine ...<k>V ile katılır)."""
    return ("var %(k)sV = { %(k)sCls: 'nz%(s)s nzs' + (S.%(k)s || 0) };\n"
            "    for (var i = 0; i < 4; i++) (function (i) { var on = i === (S.%(k)s || 0);\n"
            "      %(k)sV['%(k)sc' + i] = 'nz-ek' + (on ? ' on' : ''); %(k)sV['%(k)sp' + i] = on ? 'true' : 'false';\n"
            "      %(k)sV['%(k)sg' + i] = function () { self.setState({ %(k)s: i, %(k)sDur: true }); };\n"
            "      %(k)sV['%(k)sm' + i] = 'nz-m' + (on ? ' on' : ''); %(k)sV['%(k)sh' + i] = on ? 'false' : 'true'; })(i);\n"
            % {'k': k, 's': ' sade' if sade else ''})


def js_tur(k='nz'):
    """componentDidMount içinde (self ve azH tanımlı): ekrana girince tek tur, her durum 6 sn, Masal'da durur; dokununca durur."""
    return ("    (function (k) { var el = document.querySelector('[data-tur=\"' + k + '\"]'); if (!el || azH) return;\n"
            "      var basla = function () { var n = 0;\n"
            "        var adim = function () { if (self.state[k + 'Dur']) return; var o = {}; o[k] = ((self.state[k] || 0) + 1) %% 4; self.setState(o); if (++n < 4) self['tur' + k] = setTimeout(adim, 6000); };\n"
            "        self['tur' + k] = setTimeout(adim, 6000); };\n"
            "      if (typeof IntersectionObserver === 'undefined') return basla();\n"
            "      var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); basla(); } }, { threshold: .5 });\n"
            "      io.observe(el); })('%s');\n" % k)


# Aydınlık sahne + Etiketli ürün (+ kadranın da kullandığı rozet, halka, dalga görünümü). Sayfaya (luna_e.py) bu girer.
NZ_CSS = r"""/* Neler yapabiliyor? · Aydınlık sahne (21 Eki). Sahne kapsayıcı genişliğine bağlı: 1cqw = genişliğin %1'i (358 px tabanı) */
.nz{position:relative;margin-top:16px;container-type:inline-size;aspect-ratio:358/440}
.nz.sade{aspect-ratio:358/420}
.nz-ft{position:absolute;inset:0;border-radius:22px;overflow:hidden;background:#EEE4DA}
.nz-img{position:absolute;left:0;top:0;width:100%;height:100cqw;object-fit:cover;-webkit-mask-image:linear-gradient(#000 80%,transparent);mask-image:linear-gradient(#000 80%,transparent)}
.nz-metin{display:grid;align-items:center;min-height:48px;margin-top:12px}
.nz-m{grid-area:1/1;margin:0;font-size:16px;line-height:1.4;color:#1A2142;white-space:nowrap;opacity:0;transform:translateY(6px);transition:opacity .3s EASE,transform .3s EASE}
.nz-m.on{opacity:1;transform:none}
/* Eylem etiketleri: 48 px; etkin olan lacivert dolgu katmanıyla (opacity), yazı rengi anında değişir */
.nz-ek{position:absolute;display:inline-flex;align-items:center;gap:8px;min-height:48px;padding:0 16px 0 7px;border-radius:999px;border:1px solid #E3D8C7;background:#FFFDF9;color:#1A2142;font:inherit;font-size:14px;font-weight:600;white-space:nowrap;cursor:pointer;isolation:isolate;-webkit-tap-highlight-color:transparent;animation:nzgir .5s EASE both}
.nz-ek::before{content:"";position:absolute;inset:-1px;z-index:-1;border-radius:inherit;background:#1A2142;opacity:0;transition:opacity .3s EASE}
.nz-ek.on::before{opacity:1}
.nz-ek.on{color:#FFFDF9}
.nz-ek:focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
.nz-ek:nth-of-type(2){animation-delay:.12s}.nz-ek:nth-of-type(3){animation-delay:.24s}.nz-ek:nth-of-type(4){animation-delay:.36s}
@keyframes nzgir{from{opacity:0;transform:translateY(8px)}}
.nz-ik{display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:#F1E8DA;overflow:hidden}
.nz-dsk{display:block;width:26px;height:26px;border-radius:50%;object-fit:cover}
.nz-ek.on .nz-dsk{animation:nzdk .8s EASE both}
.nz-kd{display:flex;gap:3px}
.nz-kd i{width:6px;height:6px;border-radius:50%;background:#1A2142;opacity:.3}
.nz-kd i:first-child{opacity:1}
.nz-ek.on .nz-kd i{background:#A05A1C}
.nz-ek.on .nz-kd i:nth-child(2){animation:nzk2 6s EASE both}.nz-ek.on .nz-kd i:nth-child(3){animation:nzk3 6s EASE both}
@keyframes nzk2{0%,30%{opacity:.3}37%,100%{opacity:1}}
@keyframes nzk3{0%,63%{opacity:.3}70%,100%{opacity:1}}
.nz-eq{height:14px;margin:0;animation:none}
.nz-eq i{height:14px;background:#1A2142;animation:none;transform:scaleY(.5)}
.nz-eq i:nth-child(2){transform:scaleY(.8)}.nz-eq i:nth-child(3){transform:scaleY(.4)}.nz-eq i:nth-child(4){transform:scaleY(.65)}
.nz-ek.on .nz-eq i{background:#A05A1C;animation:ses 2s EASE 3}
.nz-bat{position:relative;display:flex;gap:1.5px;width:20px;height:12px;padding:1.5px;border:1.5px solid #1A2142;border-radius:3.5px}
.nz-bat::after{content:"";position:absolute;right:-4px;top:2.5px;width:2px;height:4px;border-radius:0 1px 1px 0;background:#1A2142}
.nz-bat i{flex:1;border-radius:1px;background:#1A2142}
.nz-ek.on .nz-bat i:nth-child(1){animation:nzp1 6s EASE both}.nz-ek.on .nz-bat i:nth-child(2){animation:nzp2 6s EASE both}.nz-ek.on .nz-bat i:nth-child(3){animation:nzp3 6s EASE both}
/* Etkiler lambanın çevresinde: lamba merkezi (50cqw, 62.57cqw) */
.nz-hk i{position:absolute;border-radius:50%;box-shadow:inset 0 0 0 1.5px #F2A65A;opacity:0;transition:opacity .4s EASE}
.nz .nz-hk i{left:50cqw;top:62.57cqw}
.nz .nz-hk i:nth-child(1){width:55.87cqw;height:55.87cqw;margin:-27.93cqw 0 0 -27.93cqw}
.nz .nz-hk i:nth-child(2){width:65.92cqw;height:65.92cqw;margin:-32.96cqw 0 0 -32.96cqw}
.nz .nz-hk i:nth-child(3){width:75.98cqw;height:75.98cqw;margin:-37.99cqw 0 0 -37.99cqw}
.nzs1 .nz-hk i:nth-child(1){opacity:.9}
.nzs1 .nz-hk i:nth-child(2){opacity:.55;animation:nzh2 6s EASE both}
.nzs1 .nz-hk i:nth-child(3){opacity:.3;animation:nzh3 6s EASE both}
@keyframes nzh2{0%,30%{opacity:0;transform:scale(.92)}37%,100%{opacity:.55;transform:none}}
@keyframes nzh3{0%,63%{opacity:0;transform:scale(.92)}70%,100%{opacity:.3;transform:none}}
.nz-dl span{position:absolute;width:48px;height:48px}
.nz .nz-dl span{top:calc(62.57cqw - 24px)}
.nz .nz-dl .sol{left:calc(31.3cqw - 56px)}.nz .nz-dl .sag{left:calc(68.7cqw + 8px)}
.nz-dl i{position:absolute;inset:0;border-radius:50%;opacity:0}
.nz-dl .sol i{box-shadow:inset 1.5px 0 0 0 #F2A65A}.nz-dl .sag i{box-shadow:inset -1.5px 0 0 0 #F2A65A}
.nzs2 .nz-dl .sol i{animation:nzdl 2s EASE 3}.nzs2 .nz-dl .sag i{animation:nzdr 2s EASE 3}
.nzs2 .nz-dl i:nth-child(2){animation-delay:.67s}.nzs2 .nz-dl i:nth-child(3){animation-delay:1.33s}
@keyframes nzdl{0%{opacity:0;transform:none}25%{opacity:1}100%{opacity:0;transform:translateX(-20px) scale(1.25)}}
@keyframes nzdr{0%{opacity:0;transform:none}25%{opacity:1}100%{opacity:0;transform:translateX(20px) scale(1.25)}}
/* Rozetler: lambanın altında tek rozet; 13 px; pasif yazı opak gri */
.nz-rzy{position:absolute;left:0;right:0;display:grid;justify-items:center;height:32px}
.nz .nz-rzy{top:94.97cqw}
.nz-rz{grid-area:1/1;display:flex;align-items:center;gap:8px;height:32px;padding:0 12px;border-radius:999px;background:#FFFDF9;box-shadow:inset 0 0 0 1px #E3D8C7;font-size:13px;font-weight:600;color:#1A2142;white-space:nowrap;
  opacity:0;transform:translateY(4px);transition:opacity .35s EASE,transform .35s EASE}
.nzs0 .nz-disk,.nzs1 .nz-kad,.nzs2 .nz-cal,.nzs3 .nz-pil{opacity:1;transform:none}
.nz-rz b{font-weight:600}
.nz-disk img{width:22px;height:22px;border-radius:50%;object-fit:cover}
.nzs0 .nz-disk img{animation:nzdk .9s EASE both}
@keyframes nzdk{0%{opacity:0;transform:translateX(24px) rotate(90deg)}100%{opacity:1;transform:none}}
.nz-kad{gap:10px}
.nz-kad i{position:relative;font-style:normal;color:#6B6F86}
.nz-kad .e{position:absolute;left:0;top:0;color:#1A2142;opacity:0}
.nz-kad i:nth-child(3) .e{opacity:1}
.nzs1 .nz-kad i:nth-child(1) .e{animation:nzw1 6s EASE both}.nzs1 .nz-kad i:nth-child(2) .e{animation:nzw2 6s EASE both}.nzs1 .nz-kad i:nth-child(3) .e{animation:nzw3 6s EASE both}
@keyframes nzw1{0%,30%{opacity:1}37%,100%{opacity:0}}
@keyframes nzw2{0%,30%{opacity:0}37%,63%{opacity:1}70%,100%{opacity:0}}
@keyframes nzw3{0%,63%{opacity:0}70%,100%{opacity:1}}
.nz-cal .eq{height:14px;margin:0;animation:none}
.nz-cal .eq i{height:14px;animation:none;transform:scaleY(.6)}
.nzs2 .nz-cal .eq i{animation:ses 2s EASE 3}
.nz-rbat{position:relative;display:flex;gap:2px;width:34px;height:17px;padding:2px;border:1.5px solid currentColor;border-radius:5px}
.nz-rbat::after{content:"";position:absolute;right:-5px;top:4px;width:3px;height:6px;border-radius:0 2px 2px 0;background:currentColor}
.nz-rbat i{flex:1;border-radius:1.5px;background:currentColor}
.nzs3 .nz-rbat i:nth-child(1){animation:nzp1 6s EASE both}.nzs3 .nz-rbat i:nth-child(2){animation:nzp2 6s EASE both}.nzs3 .nz-rbat i:nth-child(3){animation:nzp3 6s EASE both}.nzs3 .nz-rbat i:nth-child(4){animation:nzp4 6s EASE both}
@keyframes nzp1{0%{opacity:.15}10%,100%{opacity:1}}
@keyframes nzp2{0%,10%{opacity:.15}22%,100%{opacity:1}}
@keyframes nzp3{0%,22%{opacity:.15}34%,100%{opacity:1}}
@keyframes nzp4{0%,34%{opacity:.15}46%,100%{opacity:1}}
.nz-pil .durum{color:inherit;font-size:13px}
.nz-pil .durum i:first-child{opacity:0}
.nzs3 .nz-pil .durum i:first-child{animation:nzs1 6s EASE both}.nzs3 .nz-pil .durum i:last-child{animation:nzs2 6s EASE both}
@keyframes nzs1{0%,58%{opacity:1}64%,100%{opacity:0}}
@keyframes nzs2{0%,60%{opacity:0}66%,100%{opacity:1}}
""".replace('EASE', E)

# 2 · Gece kadranı (yalnız pano): panel 358 × 432; pencere merkezi (179, 220), çap 200; yay yarıçapı 136, yazılar 162
YAZI = [(39, 139), (124, 68), (234, 68), (319, 139)]  # θ = -60, -20, 20, 60 derece


def kadran():
    dug = ''.join('<button class="{{bd%d}}" type="button" style="left: %dpx; top: %dpx" onClick="{{bg%d}}" aria-pressed="{{bp%d}}">%s</button>'
                  % (i, x - 32, y - 24, i, i, o[2]) for i, (o, (x, y)) in enumerate(zip(OZ, YAZI)))
    metin = ''.join('<div class="{{bm%d}}" aria-hidden="{{bh%d}}"><h3 class="gk-bas">%s</h3><p class="gk-p">%s</p></div>' % (i, i, o[3], o[4]) for i, o in enumerate(OZ))
    pen = model(lambda m: '<img class="%s" src="/_blob/%s" alt="">' % (m, FOTO[m]))
    return ('<div class="{{bCls}}" data-tur="b">'
            '<div class="gk-yay" aria-hidden="true"><i></i></div>'
            '<div class="gk-kol" aria-hidden="true" style="--a: {{bAci}}deg"><i></i></div>' + HALKA + DALGA +
            '<div class="gk-pen" aria-hidden="true">' + pen + '</div>' + ROZET + dug +
            '<div class="gk-metin" aria-live="polite">' + metin + '</div></div>')


GK_CSS = r"""/* 2 · Gece kadranı (pano) */
.gk{position:relative;height:432px;margin-top:16px;border-radius:28px;background:#1A2142;overflow:hidden;color:#FFFDF9}
.gk .nz-hk i{left:179px;top:220px}
.gk .nz-hk i:nth-child(1){width:214px;height:214px;margin:-107px 0 0 -107px}
.gk .nz-hk i:nth-child(2){width:230px;height:230px;margin:-115px 0 0 -115px}
.gk .nz-hk i:nth-child(3){width:246px;height:246px;margin:-123px 0 0 -123px}
.gk .nz-dl span{top:196px}
.gk .nz-dl .sol{left:21px}.gk .nz-dl .sag{left:289px}
.gk .nz-rzy{top:304px}
.gk .nz-rz{background:#1A2142;box-shadow:inset 0 0 0 1px rgba(246,241,233,.24);color:#FFFDF9}
.gk .nz-kad i{color:#8E93AE}
.gk .nz-kad .e{color:#FFFDF9}
.gk-yay{position:absolute;left:43px;top:84px;width:272px;height:136px;overflow:hidden}
.gk-yay i{position:absolute;left:0;top:0;width:272px;height:272px;border-radius:50%;box-shadow:inset 0 0 0 1px rgba(246,241,233,.2)}
.gk-kol{position:absolute;left:43px;top:84px;width:272px;height:272px;transform:rotate(var(--a));transition:transform 1s EASE}
.gk-kol i{position:absolute;left:50%;top:-6px;width:12px;height:12px;margin-left:-6px;border-radius:50%;background:#F2A65A}
.gk-pen{position:absolute;left:79px;top:120px;width:200px;height:200px;border-radius:50%;overflow:hidden;background:#EEE4DA;transition:opacity .5s EASE}
.gk-pen img{position:absolute;left:-30px;top:-68px;width:260px;height:260px;max-width:none}
.gk-pen img.erkek{left:-29px;top:-66px}
.gk.nzs1 .gk-pen{animation:gkb 6s EASE both}
.gk.nzs3 .gk-pen{animation:gks 6s EASE both}
@keyframes gkb{0%,30%{opacity:.6}37%,63%{opacity:.8}70%,100%{opacity:1}}
@keyframes gks{0%,58%{opacity:.4}66%,100%{opacity:1}}
.gk-d{position:absolute;width:64px;height:48px;padding:0;border:0;background:none;color:#8E93AE;font-size:14px;font-weight:600}
.gk-d.on{color:#FFFDF9}
.gk-metin{position:absolute;left:20px;right:20px;top:356px;display:grid}
.gk-m{grid-area:1/1;opacity:0;transform:translateY(6px);transition:opacity .35s EASE,transform .35s EASE}
.gk-m.on{opacity:1;transform:none}
.gk-bas{margin:0;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:22px;line-height:1.2;letter-spacing:-.01em;color:#FFFDF9}
.gk-p{margin:6px 0 0;font-size:15px;line-height:1.45;color:#B9BED6}
""".replace('EASE', E)

PANO_CSS = r""".pg{background:#F6F1E9;font-size:15px}
.sec{padding:0 16px 44px}
.oneri{display:flex;align-items:center;gap:8px;margin:0 0 6px;padding-top:16px;border-top:1px dashed #D6CAB6;font-size:12px;font-weight:700;color:#A05A1C}
.oneri-alt{margin:0 0 16px;font-size:13px;color:#5C6078;text-wrap:balance}
.pg button{font:inherit;cursor:pointer;-webkit-tap-highlight-color:transparent}
.pg :focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
.h2 span.n{color:#F2A65A}
"""

BAS = '<h2 class="h2">Neler<br>yapabiliyor<span class="n">?</span></h2>'

HTML = """<div class="pg">
  <div style="padding: 18px 16px 10px">
    <h1 class="h2" style="font-size: 22px">LunaDream · Neler yapabiliyor? 2. tur, eleştirmenin sırası</h1>
    <p style="margin: 6px 0 0; font-size: 13px; color: #5C6078">Seçilen: 1 · Aydınlık sahne (21 Eki). Ürün büyük, yazı en az. Etiketler eylem söyler (Sihirli "ne" der). Her durum 6 sn; ekrana girince tek tur, Masal'da durur, dokununca durur. Yeri: Videolar'ın altı, Odası'nın üstü.</p>
  </div>

  <section class="sec">
    <p class="oneri">1 · Aydınlık sahne · seçildi</p>
    <p class="oneri-alt">Büyük stüdyo fotoğrafı; etkin özelliğin etkisi lambanın çevresinde: üç amber halka, iki yanda ses dalgaları, altta disk, kademe ve pil rozeti.</p>
    """ + BAS + sahne('a') + """
  </section>

  <section class="sec">
    <p class="oneri">2 · Gece kadranı</p>
    <p class="oneri-alt">Beğenilen gece kadranının dili: lacivert sahne, yuvarlak pencerede ürün, yayda dört yazı; amber ay noktası yazıdan yazıya gider.</p>
    """ + BAS + kadran() + """
  </section>

  <section class="sec">
    <p class="oneri">3 · Etiketli ürün</p>
    <p class="oneri-alt">Güvenli yedek: fotoğraf, dört eylem etiketi, altta tek cümle. Etkin etiketin simgesi bir kez oynar.</p>
    """ + BAS + sahne('c', sade=True) + """
  </section>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { a: 0, aDur: false, b: 0, bDur: false, c: 0, cDur: false }; }
  componentDidMount() {
    var self = this, azH = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
""" + js_tur('a') + js_tur('b') + js_tur('c') + """  }
  componentWillUnmount() { clearTimeout(this.tura); clearTimeout(this.turb); clearTimeout(this.turc); }
  renderVals() {
    var self = this, S = this.state;
    """ + js_degerler('a') + "    " + js_degerler('c', sade=True) + """    var o = { sihKiz: true, sihErkek: false, bCls: 'gk nzs' + S.b, bAci: -60 + 40 * S.b };
    for (var i = 0; i < 4; i++) (function (i) { var on = i === S.b;
      o['bd' + i] = 'gk-d' + (on ? ' on' : ''); o['bp' + i] = on ? 'true' : 'false';
      o['bg' + i] = function () { self.setState({ b: i, bDur: true }); };
      o['bm' + i] = 'gk-m' + (on ? ' on' : ''); o['bh' + i] = on ? 'false' : 'true'; })(i);
    return Object.assign(o, aV, cV);
  }
}"""

if __name__ == '__main__':
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · Neler yapabiliyor 2', css=S2.MINI_CSS + NZ_CSS + GK_CSS + PANO_CSS) + HTML + TAIL.format(h=int(os.environ.get('OZ2_H', 2269)), js=JS))
    print('yazıldı:', os.path.abspath(OUT))
