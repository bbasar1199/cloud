# LunaDream · "Neler yapabiliyor?" 4. tur (22 Eki). Çalıştır: python3 ozellik4_varyant.py
# Kullanıcı (dokunulur afişten sonra): "Yine çok beğenmedim, sıkıcı geliyor gözüme."
# Teşhis: afiş, hemen üstteki Sihirli özellikler'in dört beyaz arayüz kartını (disk, ışık, Bluetooth, şarj) aynı dille tekrar ediyordu.
# Bu turda beyaz arayüz kartı yok; ürünün kendisi oynar (kubbe gerçekten açılır, lamba kısılır, kalkar), yazı büyük, hareket ürüne bağlı.
#   A · Dergi kapağı: dev tek kelime (Tak. Çal. Kıs. Taşı.), ürün kelimenin önünde; her kelimede zemin ve ürün değişir (akşam → gece → sabah).
#   B · Atlıkarınca: lamba ortada, dört fotoğraf balonu çevresinde 3B halkada döner (arkadan geçerken lambanın arkasında kalır); öndeki anlatılır.
#   C · Albüm: gerçek fotoğraflardan (ikisi müşteri) dört kartlık deste; kaydırınca üstteki kart atılır, alta girer.
# Ürün parçaları: c-an-kiz-kesim / c-erkek-disk-kesim kubbe (baş) ve gövde olarak ikiye bölündü (canvas/c-gorsel/parca, scratchpad bol.py).
# Kubbe açılıp disk üstten girer (teyitli, 22 Eki). Erkek'te baş kalkar (varsayım). Ses, pil süresi, kumanda çizilmez.
import os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE-Ozellik4.dc.html')

E = 'cubic-bezier(.2,.7,.2,1)'
B = '/_blob/'
# kubbe (üst), gövde (alt), tam; en/boy oranı
PAR = {'kiz': ('d605d392308a84a33323ff40eded6937', '4617058d97e3ceabb65294479d7d6f37', '680dbd1da6e069189d440927c113c3f3'),
       'erkek': ('0b63136e2e09e31cc155a983ea675132', '78fc28432ba75443c7538f984bf51573', '8e52eb8347fbca90cc90cca9a217a58c')}
DISK_AY = '4a3a69e8c1d8dddad8c33f8f463b8a0e'
FOTO = {'disk': '5b284c77c252b08a2974bde8e43de126', 'elde': '8b1f621be2cb3b6133b7b78bc14e1963',
        'mus2': 'ec3c3976bbe8f18e5660f4a4c355ebf7', 'mus1': '4323cd781a0d687b528b3059505be48c'}
NOTA = '<svg viewBox="0 0 24 24"><path d="M9 17.5V5.5l10-2v12"></path><circle cx="6.5" cy="17.5" r="2.6"></circle><circle cx="16.5" cy="15.5" r="2.6"></circle></svg>'


def model(f):
    return ('<sc-if value="{{sihKiz}}" hint-placeholder-val="{{true}}">' + f('kiz') + '</sc-if>'
            '<sc-if value="{{sihErkek}}" hint-placeholder-val="{{false}}">' + f('erkek') + '</sc-if>')


# Ürün: gövde, gövdenin koyu kopyası, disk, kubbe, kubbenin koyu kopyası (ışık kısılınca koyular opacity ile belirir); notalar; zemin gölgesi
def urun():
    def m(md):
        u, a, t = PAR[md]
        return ('<span class="ur-k %s">' % md + ''.join('<img class="%s" src="%s%s" alt="">' % (c, B, s) for c, s in
                (('ur-alt', a), ('ur-alt koyu', a), ('ur-disk', DISK_AY), ('ur-ust', u), ('ur-ust koyu', u))) + '</span>')
    return ('<span class="ur" aria-hidden="true"><span class="ur-hale"></span><span class="ur-gol"></span><span class="ur-tas">' + model(m) +
            ''.join('<span class="ur-n n%d">%s</span>' % (i, NOTA) for i in range(3)) + '</span></span>')


# Eylem sekansları: çerçevede x-tak / x-cal / x-kis / x-tas + oa/ob (her oynatışta değişir, animasyon baştan başlar); ışık kademesi i0/i1/i2
URUN_CSS_SEK = r"""
.x-tak.oa .ur-ust{animation:kubbe 2.6s EASE both}
@keyframes kubbe{0%{transform:none}16%,60%{transform:translateY(-12%)}80%,100%{transform:none}}
.x-tak.oa .ur-disk{animation:diskin 2.6s EASE both}
@keyframes diskin{0%,16%{opacity:0;transform:translateY(-130%) scaleY(.36)}22%{opacity:1}44%{opacity:1;transform:translateY(0) scaleY(.36)}58%,100%{opacity:0;transform:translateY(50%) scaleY(.36)}}
.x-cal.oa .ur-n{animation:nota 2s EASE both}
.x-cal.oa .ur-n.n1{animation-delay:.45s}.x-cal.oa .ur-n.n2{animation-delay:.9s}
@keyframes nota{0%{opacity:0;transform:translateY(12px) rotate(-10deg)}18%,70%{opacity:1}100%{opacity:0;transform:translateY(-56px) rotate(10deg)}}
.x-tas.oa .ur-tas{animation:tasi 2.4s EASE both}
@keyframes tasi{0%{transform:none}28%,62%{transform:translate(-8px,-20px) rotate(-3deg)}100%{transform:none}}
.x-tas.oa .ur-gol{animation:golge 2.4s EASE both}
@keyframes golge{0%{transform:none;opacity:1}28%,62%{transform:scale(.72);opacity:.45}100%{transform:none;opacity:1}}
"""


def ciftle(css):
    adlar = re.findall(r'@keyframes (\w+)', css)
    kopya = css
    for a in adlar:
        kopya = re.sub(r'\b%s\b' % a, a + '2', kopya)
    return css + re.sub(r'\.oa\b', '.ob', kopya)


URUN_CSS = r"""/* Ürün (parçalı kesim) */
.ur{position:absolute;display:block;--uh:360px}
.ur-tas{position:relative;display:block}
.ur-k{position:relative;display:block;height:var(--uh);width:calc(var(--uh) * .5216)}
.ur-k.erkek{width:calc(var(--uh) * .7535)}
.ur-k img{position:absolute;left:0;top:0;width:100%;height:100%}
.ur-k .koyu{filter:brightness(.42);opacity:0;transition:opacity .7s EASE}
.ur-disk{left:28%!important;top:19%!important;width:44%!important;height:auto!important;aspect-ratio:1;border-radius:50%;opacity:0;box-shadow:0 0 0 2px #C9A46A}
.ur-k.erkek .ur-disk{left:33%!important;top:40%!important;width:28%!important}
.ur-k.erkek .ur-ust{transform-origin:50% 100%}
.ur-hale{position:absolute;left:50%;top:40%;width:150%;aspect-ratio:1;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(closest-side,rgba(242,166,90,.42),rgba(242,166,90,0));opacity:0;transition:opacity .9s EASE;pointer-events:none}
.ur-gol{position:absolute;left:8%;right:8%;bottom:-10px;height:22px;border-radius:50%;background:radial-gradient(closest-side,rgba(10,13,32,.38),rgba(10,13,32,0))}
.ur-n{position:absolute;width:26px;height:26px;opacity:0}
.ur-n svg{width:100%;height:100%;fill:none;stroke:#F2A65A;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.ur-n.n0{left:-14%;top:42%}.ur-n.n1{right:-16%;top:30%}.ur-n.n2{left:60%;top:6%}
.i1 .ur-k .koyu{opacity:.5}.i2 .ur-k .koyu{opacity:1}
""" + ciftle(URUN_CSS_SEK)

ACTIONS = ['tak', 'cal', 'kis', 'tas']


# ---------------- A · Dergi kapağı ----------------
DK = [('Tak.', 'Kubbeyi aç, masal diskini üstten tak.', 'Tak'),
      ('Çal.', 'Telefondaki ninni, Bluetooth ile lambadan çalar.', 'Çal'),
      ('Kıs.', '<span class="s0">Parlak</span>, <span class="s1">orta</span>, <span class="s2">kısık</span>. Uykuya göre ayarla.', 'Kıs'),
      ('Taşı.', 'Şarjlı. Kablo olmadan istediğin yere.', 'Taşı')]


def dergi():
    return ('<div class="{{dkCls}}" data-tur="dk">' + ''.join('<span class="{{dkz%d}}"></span>' % i for i in range(4)) +
            '<p class="dk-soz" aria-hidden="true">' + ''.join('<span class="{{dkw%d}}">%s</span>' % (i, b[0]) for i, b in enumerate(DK)) + '</p>'
            '<p class="dk-alt" aria-live="polite">' + ''.join('<span class="{{dkc%d}}">%s</span>' % (i, b[1]) for i, b in enumerate(DK)) + '</p>'
            '<button class="dk-urun" type="button" onClick="{{dkUrunG}}" aria-label="Bu özelliği yeniden göster">' + urun() + '</button>'
            '<div class="dk-bar">' + ''.join('<button class="{{dkb%d}}" type="button" onClick="{{dkg%d}}"><b></b>%s</button>' % (i, i, b[2]) for i, b in enumerate(DK)) +
            '</div></div>')


DK_CSS = r"""/* A · Dergi kapağı: 358 × 520 */
.dk{position:relative;width:358px;height:520px;margin:16px auto 0;border-radius:24px;overflow:hidden;isolation:isolate}
/* Zemin perdesi: yeni renk alttan yükselir (geri dönüşte üstteki perdeler iner); ara gri ton olmaz */
.dk-z{position:absolute;inset:0;transform:translateY(101%);transition:transform .9s EASE}
.dk-z.on{transform:none}
.dk-z.z0{background:#F1E8DA}.dk-z.z1{background:#1A2142}.dk-z.z2{background:#0C1027}.dk-z.z3{background:#F6F1E9}
.dk-soz{position:absolute;left:14px;right:0;top:6px;height:140px;margin:0;overflow:hidden;font-family:"Young Serif",Georgia,serif;font-size:128px;line-height:140px;letter-spacing:-.045em;z-index:1}
.dk-soz span{position:absolute;left:0;top:0;white-space:nowrap;transform:translateY(105%);transition:transform .8s EASE}
.dk-soz span.ust{transform:translateY(-105%)}
.dk-soz span.on{transform:none}
.dk-soz span:nth-child(1),.dk-soz span:nth-child(4){color:#1A2142}
.dk-soz span:nth-child(2),.dk-soz span:nth-child(3){color:#FFFDF9}
.dk-alt{position:absolute;left:18px;bottom:76px;width:142px;height:110px;margin:0;font-size:16px;line-height:1.4;z-index:1}
.dk-alt>span{position:absolute;left:0;top:0;width:100%;opacity:0;transform:translateY(8px);transition:opacity .5s EASE,transform .5s EASE}
.dk-alt>span.on{opacity:1;transform:none;transition-delay:.25s}
.dk-alt>span:nth-child(1),.dk-alt>span:nth-child(4){color:#3B4160}
.dk-alt>span:nth-child(2),.dk-alt>span:nth-child(3){color:rgba(255,253,249,.8)}
.dk-alt .s0,.dk-alt .s1,.dk-alt .s2{transition:color .3s EASE}
.i0 .dk-alt .s0,.i1 .dk-alt .s1,.i2 .dk-alt .s2{color:#F2A65A}
.dk-urun{position:absolute;right:0;bottom:58px;width:200px;height:362px;padding:0;border:0;background:none;cursor:pointer;z-index:2;-webkit-tap-highlight-color:transparent}
.dk-urun:focus-visible{outline:2px solid #F2A65A;outline-offset:2px;border-radius:12px}
.dk .ur{right:4px;bottom:0;--uh:360px}
.dk.b1 .ur-hale,.dk.b2 .ur-hale{opacity:1}
.dk-bar{position:absolute;left:0;right:0;bottom:0;display:flex;height:56px;padding:0 6px;z-index:3}
.dk-bar button{position:relative;flex:1;height:56px;padding:10px 0 0;border:0;background:none;font:inherit;font-size:14px;font-weight:600;color:#7A7468;cursor:pointer}
.dk-bar button b{position:absolute;left:8px;right:8px;top:8px;height:2px;border-radius:1px;background:currentColor;opacity:.3}
.dk-bar button b::after{content:"";position:absolute;inset:0;border-radius:1px;background:#F2A65A;transform:scaleX(0);transform-origin:0 50%}
.dk-bar button.on{color:#1A2142}
.dk-bar button.on b::after{transform:none}
.kos .dk-bar button.on b::after{animation:dkdol 3.4s linear both}
@keyframes dkdol{from{transform:scaleX(0)}}
.b1 .dk-bar button,.b2 .dk-bar button{color:rgba(255,253,249,.55)}
.b1 .dk-bar button.on,.b2 .dk-bar button.on{color:#FFFDF9}
.dk-bar button:focus-visible{outline:2px solid #F2A65A;outline-offset:-4px;border-radius:10px}
.dk.bek .dk-soz span,.dk.bek .dk-alt,.dk.bek .ur{opacity:0}
.dk.gir .dk-urun{animation:dkgir .9s EASE backwards}
@keyframes dkgir{from{opacity:0;transform:translateY(24px)}}
@media (max-width:389px){.dk{zoom:.958}}
@media (max-width:374px){.dk{zoom:.916}}
@media (max-width:359px){.dk{zoom:.86}}
"""


def js_dk_deger():
    return ("var dB = S.dkB || 0, dP = S.dkP || 0;\n"
            "    var dkV = { dkCls: 'dk b' + dB + ' x-' + %s[dB] + ' i' + (S.dkI || 0) + (dP ? (dP %% 2 ? ' oa' : ' ob') : '') + (S.dkOn === false ? ' bek' : S.dkOn ? ' gir' : '') + (S.dkKos ? ' kos' : ''),\n"
            "      dkUrunG: function () { self.dkDokun(dB); } };\n"
            "    [0, 1, 2, 3].forEach(function (i) { dkV['dkz' + i] = 'dk-z z' + i + (i <= dB ? ' on' : ''); dkV['dkw' + i] = i === dB ? 'on' : i < dB ? 'ust' : ''; dkV['dkc' + i] = i === dB ? 'on' : '';\n"
            "      dkV['dkb' + i] = i === dB ? 'on' : ''; dkV['dkg' + i] = function () { self.dkDokun(i); }; });\n" % str(ACTIONS))


JS_DK = """  dkGit(i) { var self = this; this.setState({ dkB: i, dkP: (this.state.dkP || 0) + 1, dkI: 0, dkOn: true });
    if (i === 2) { this.at('dk', 900, function () { self.setState({ dkI: 1 }); }); this.at('dk', 1800, function () { self.setState({ dkI: 2 }); }); } }
  dkOyna() { var self = this; this.dur('dk'); this.dkKos = true; this.setState({ dkKos: true }); this.dkGit(0);
    [1, 2, 3].forEach(function (i) { self.at('dk', i * 3400, function () { self.dkGit(i); }); });
    this.at('dk', 13600, function () { self.dkKos = false; self.setState({ dkKos: false }); }); }
  dkDokun(i) { this.dur('dk'); this.dkKos = false; this.dkElle = true; this.setState({ dkKos: false }); this.dkGit(i); }
"""


# ---------------- B · Atlıkarınca ----------------
AK = [('Diski tak.', 'Kubbe açılır, masal diski üstten girer.', DISK_AY, '50% 50%', 'Masal diski'),
      ('Ninniyi aç.', 'Telefondaki ninni, Bluetooth ile lambadan çalar.', FOTO['elde'], '50% 42%', 'Elde yanan lamba'),
      ('Işığı kıs.', 'Parlak, orta, kısık: uykuya göre ayarla.', FOTO['mus2'], '50% 55%', 'Müşterimizin odasında kısık ışık'),
      ('Yanına al.', 'Şarjlı. Kablo olmadan istediğin yere.', FOTO['mus1'], '50% 30%', 'Müşterimizin kızı lambayı kucaklıyor')]
CHEV = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.5 6l-6 6 6 6"></path></svg>'


def karusel():
    return ('<div class="{{akCls}}" data-tur="ak"><div class="ak-sahne" onPointerDown="{{akBas}}" onPointerUp="{{akBirak}}">'
            '<span class="ak-hale" aria-hidden="true"></span>'
            '<div class="ak-halka" style="transform: rotateX(-14deg) rotateY({{akRy}}deg)">'
            '<div class="ak-lamba" style="transform: rotateY({{akLy}}deg) rotateX(14deg)">' + urun() + '</div>' +
            ''.join('<button class="{{aki%d}}" type="button" style="transform: rotateY(%ddeg) translateZ(128px) rotateY({{akiy%d}}deg) rotateX(14deg)" '
                    'onClick="{{akig%d}}" aria-label="%s"><img src="%s%s" alt="%s" style="object-position: %s"></button>'
                    % (i, i * 90, i, i, a[0], B, a[2], a[4], a[3]) for i, a in enumerate(AK)) +
            '</div></div>'
            '<div class="ak-alt"><div class="ak-yazi" aria-live="polite">' +
            ''.join('<p class="{{akc%d}}"><b>%s</b><span>%s</span></p>' % (i, a[0], a[1]) for i, a in enumerate(AK)) +
            '</div><button class="ak-ok geri" type="button" onClick="{{akGeri}}" aria-label="Önceki">' + CHEV + '</button>'
            '<button class="ak-ok ileri" type="button" onClick="{{akIleri}}" aria-label="Sonraki">' + CHEV + '</button></div></div>')


AK_CSS = r"""/* B · Atlıkarınca: 358 × 500; halka 3B, öğeler ve lamba hep kameraya bakar */
.ak{position:relative;width:358px;height:500px;margin:16px auto 0;border-radius:24px;overflow:hidden;background:#1A2142;isolation:isolate}
.ak-sahne{position:relative;height:396px;perspective:560px;perspective-origin:50% 42%;touch-action:pan-y;cursor:grab}
.ak-hale{position:absolute;left:50%;top:170px;width:380px;height:380px;margin:-190px 0 0 -190px;border-radius:50%;background:radial-gradient(closest-side,rgba(242,166,90,.32),rgba(242,166,90,0));transition:opacity .9s EASE}
.ak.i1 .ak-hale{opacity:.6}.ak.i2 .ak-hale{opacity:.25}
.ak-halka{position:absolute;left:50%;top:252px;width:0;height:0;transform-style:preserve-3d;transition:transform 1.2s EASE}
.ak-lamba{position:absolute;left:-76px;top:-224px;width:152px;height:292px;transition:transform 1.2s EASE}
.ak .ur{left:0;top:0;--uh:292px}
.ak .ur-gol{opacity:.7}
.ak-lamba .ur-hale{display:none}
.ak-i{position:absolute;left:-42px;top:-42px;width:84px;height:84px;padding:0;border:0;border-radius:50%;overflow:hidden;background:#141A36;box-shadow:0 0 0 3px rgba(255,253,249,.9);cursor:pointer;
  transition:transform 1.2s EASE,opacity .8s EASE;-webkit-tap-highlight-color:transparent}
.ak-i img{width:100%;height:100%;object-fit:cover;display:block}
.ak-i.on{box-shadow:0 0 0 3px #F2A65A}
.ak-i.p2{opacity:.55}
.ak-i:focus-visible{outline:2px solid #F2A65A;outline-offset:4px}
.ak-alt{position:absolute;left:0;right:0;bottom:0;display:flex;align-items:center;gap:8px;height:104px;padding:0 12px 14px 20px}
.ak-yazi{position:relative;flex:1;height:84px}
.ak-yazi p{position:absolute;left:0;top:0;right:0;margin:0;opacity:0;transform:translateY(10px);transition:opacity .5s EASE,transform .5s EASE}
.ak-yazi p.on{opacity:1;transform:none;transition-delay:.3s}
.ak-yazi b{display:block;font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:28px;line-height:1.1;letter-spacing:-.01em;color:#FFFDF9}
.ak-yazi span{display:block;margin-top:6px;font-size:15px;line-height:1.4;color:rgba(255,253,249,.74)}
.ak-ok{display:grid;place-items:center;flex:none;width:48px;height:48px;padding:0;border:0;border-radius:50%;background:none;box-shadow:inset 0 0 0 1px rgba(255,253,249,.28);color:#FFFDF9;cursor:pointer}
.ak-ok svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.ak-ok.ileri svg{transform:scaleX(-1)}
.ak-ok:focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
.ak.bek .ak-i,.ak.bek .ak-yazi{opacity:0}
.ak.gir .ak-i{animation:akgir .8s EASE backwards}
.ak.gir .ak-i:nth-of-type(2){animation-delay:.1s}.ak.gir .ak-i:nth-of-type(3){animation-delay:.2s}.ak.gir .ak-i:nth-of-type(4){animation-delay:.3s}
@keyframes akgir{from{opacity:0}}
@media (max-width:389px){.ak{zoom:.958}}
@media (max-width:374px){.ak{zoom:.916}}
@media (max-width:359px){.ak{zoom:.86}}
"""


def js_ak_deger():
    return ("var aA = S.akA || 0, aF = ((aA %% 4) + 4) %% 4, aP = S.akP || 0;\n"
            "    var akV = { akCls: 'ak x-' + %s[aF] + ' i' + (S.akI || 0) + (aP ? (aP %% 2 ? ' oa' : ' ob') : '') + (S.akOn === false ? ' bek' : S.akOn ? ' gir' : ''),\n"
            "      akRy: -aA * 90, akLy: aA * 90, akGeri: function () { self.akYon(-1); }, akIleri: function () { self.akYon(1); },\n"
            "      akBas: function (e) { self.akX = e.clientX; }, akBirak: function (e) { var d = e.clientX - (self.akX == null ? e.clientX : self.akX); self.akX = null;\n"
            "        if (Math.abs(d) > 30) { self.akKay = Date.now(); self.akYon(d < 0 ? 1 : -1); } } };\n"
            "    [0, 1, 2, 3].forEach(function (i) { var p = ((i - aF) + 4) %% 4; akV['aki' + i] = 'ak-i p' + p + (p === 0 ? ' on' : ''); akV['akiy' + i] = (aA - i) * 90;\n"
            "      akV['akc' + i] = i === aF ? 'on' : ''; akV['akig' + i] = function () { if (Date.now() - (self.akKay || 0) < 400) return; var d = ((i - aF) + 4) %% 4; self.akYon(d === 3 ? -1 : d); }; });\n" % str(ACTIONS))


JS_AK = """  akGit(a) { var self = this, f = ((a % 4) + 4) % 4; this.setState({ akA: a, akP: (this.state.akP || 0) + 1, akI: 0, akOn: true });
    if (f === 2) { this.at('ak', 1100, function () { self.setState({ akI: 1 }); }); this.at('ak', 1900, function () { self.setState({ akI: 2 }); }); } }
  akOyna() { var self = this; this.dur('ak'); this.akKos = true; this.at('ak', 500, function () { self.akGit(0); });
    [1, 2, 3, 4].forEach(function (i) { self.at('ak', 500 + i * 3000, function () { self.akGit(i); }); });
    this.at('ak', 13000, function () { self.akKos = false; }); }
  akYon(d) { if (!d) { this.dur('ak'); this.akElle = true; this.akGit(this.state.akA || 0); return; } this.dur('ak'); this.akKos = false; this.akElle = true; this.akGit((this.state.akA || 0) + d); }
"""


# ---------------- C · Albüm ----------------
AD = [('Diski tak.', 'Kubbe açılır, masal üstten girer.', FOTO['disk'], '50% 34%', '', 'Lamba ve masal diskleri'),
      ('Ninniyi aç.', 'Telefondan, Bluetooth ile.', FOTO['elde'], '50% 40%', '', 'Elde yanan lamba'),
      ('Işığı kıs.', 'Parlak, orta, kısık.', FOTO['mus2'], '50% 55%', 'Müşteri fotoğrafı', 'Müşterimizin odasında kısık ışık'),
      ('Yanına al.', 'Şarjlı, kablosuz.', FOTO['mus1'], '50% 26%', 'Müşteri fotoğrafı', 'Müşterimizin kızı lambayı kucaklıyor')]


def album():
    return ('<div class="{{adCls}}" data-tur="ad"><div class="ad-deste" onPointerDown="{{adBas}}" onPointerUp="{{adBirak}}">' +
            ''.join('<button class="{{adk%d}}" type="button" style="--g: %.2fs" onClick="{{adSonra}}" aria-label="%s, sonraki fotoğraf">'
                    '<span class="ad-f"><img src="%s%s" alt="%s" style="object-position: %s">%s</span>'
                    '<span class="ad-y"><b>%s</b><small>%s</small></span></button>'
                    % (i, .12 * (3 - i), a[0], B, a[2], a[5], a[3], ('<i class="ad-m">%s</i>' % a[4]) if a[4] else '', a[0], a[1])
                    for i, a in enumerate(AD)) +
            '</div><div class="ad-alt"><span class="ad-say">{{adSay}} / 4</span><span class="ad-ipucu">Kaydır ya da dokun</span>'
            '<button class="ad-ok geri" type="button" onClick="{{adOnce}}" aria-label="Önceki fotoğraf">' + CHEV + '</button>'
            '<button class="ad-ok ileri" type="button" onClick="{{adSonra}}" aria-label="Sonraki fotoğraf">' + CHEV + '</button></div></div>')


AD_CSS = r"""/* C · Albüm: 358 × 470, gerçek fotoğraflardan deste */
.ad{position:relative;width:358px;height:470px;margin:8px auto 0;overflow:hidden}
.ad-deste{position:relative;height:404px;touch-action:pan-y}
.ad-k{position:absolute;left:45px;top:24px;width:268px;height:344px;padding:10px 10px 0;border:0;border-radius:6px;background:#FFFDF9;text-align:left;font:inherit;color:#1A2142;cursor:pointer;
  box-shadow:0 1px 2px rgba(26,33,66,.12),0 12px 28px -10px rgba(26,33,66,.28);transition:transform .55s EASE;-webkit-tap-highlight-color:transparent}
.ad-k.s0{z-index:4;transform:rotate(-2deg)}
.ad-k.s1{z-index:3;transform:translate(12px,6px) rotate(4deg)}
.ad-k.s2{z-index:2;transform:translate(-12px,10px) rotate(-6deg)}
.ad-k.s3{z-index:1;transform:translate(4px,14px) rotate(7deg)}
.ad-k.at-l{transform:translate(-128%,-24px) rotate(-18deg)}
.ad-k.at-r{transform:translate(128%,-24px) rotate(18deg)}
.ad-y{transition:opacity .3s EASE}
.ad-k.s1 .ad-y,.ad-k.s2 .ad-y,.ad-k.s3 .ad-y{opacity:0}
.ad-k:focus-visible{outline:2px solid #F2A65A;outline-offset:3px}
.ad-f{position:relative;display:block;height:258px;border-radius:2px;overflow:hidden;background:#141A36}
.ad-f img{width:100%;height:100%;object-fit:cover;display:block}
.ad-m{position:absolute;left:8px;bottom:8px;padding:3px 8px;border-radius:999px;background:#1A2142;color:#FFFDF9;font-style:normal;font-size:12px;font-weight:600}
.ad-y{display:flex;flex-direction:column;gap:2px;padding:12px 4px 0}
.ad-y b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:24px;line-height:1.1;letter-spacing:-.01em}
.ad-y small{font-size:14px;color:#5C6078}
.ad-alt{display:flex;align-items:center;gap:8px;height:56px;padding:0 4px 0 20px}
.ad-say{font-size:14px;font-weight:700;font-variant-numeric:tabular-nums;color:#1A2142}
.ad-ipucu{flex:1;font-size:13px;color:#5C6078}
.ad-ok{display:grid;place-items:center;flex:none;width:48px;height:48px;padding:0;border:0;border-radius:50%;background:none;box-shadow:inset 0 0 0 1px rgba(26,33,66,.18);color:#1A2142;cursor:pointer}
.ad-ok svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.ad-ok.ileri svg{transform:scaleX(-1)}
.ad-ok:focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
.ad.bek .ad-k{opacity:0}
.ad.gir .ad-k{animation:addag .7s EASE backwards;animation-delay:var(--g)}
@keyframes addag{from{opacity:0;transform:translateY(-36px) rotate(-10deg)}}
@media (max-width:374px){.ad{zoom:.916}}
@media (max-width:359px){.ad{zoom:.86}}
"""


def js_ad_deger():
    return ("var dU = S.adU || 0;\n"
            "    var adV = { adCls: 'ad' + (S.adOn === false ? ' bek' : S.adOn ? ' gir' : ''), adSay: dU + 1,\n"
            "      adSonra: function () { if (Date.now() - (self.adKay || 0) < 400) return; self.adElle = true; self.dur('ad'); self.adAt('l'); },\n"
            "      adOnce: function () { self.adElle = true; self.dur('ad'); self.setState({ adU: (dU + 3) % 4 }); },\n"
            "      adBas: function (e) { self.adX = e.clientX; }, adBirak: function (e) { var d = e.clientX - (self.adX == null ? e.clientX : self.adX); self.adX = null;\n"
            "        if (Math.abs(d) > 30) { self.adKay = Date.now(); self.adElle = true; self.dur('ad'); self.adAt(d < 0 ? 'l' : 'r'); } } };\n"
            "    [0, 1, 2, 3].forEach(function (i) { var p = ((i - dU) + 4) % 4; adV['adk' + i] = 'ad-k s' + p + (p === 0 && S.adAt ? ' at-' + S.adAt : ''); });\n")


JS_AD = """  adAt(y) { var self = this; if (this.adMesgul) return; this.adMesgul = true; this.setState({ adAt: y });
    setTimeout(function () { self.setState({ adU: ((self.state.adU || 0) + 1) % 4, adAt: '' }); self.adMesgul = false; }, 420); }
  adOyna() { var self = this; this.dur('ad'); this.setState({ adOn: true, adU: 0 });
    [0, 1, 2, 3].forEach(function (i) { self.at('ad', 2200 + i * 2600, function () { self.adAt('l'); }); }); }
"""


# ---------------- Ortak: zamanlayıcı ve ekrana girince tur ----------------
JS_ORTAK = """  at(k, ms, f) { (this[k + 'T'] = this[k + 'T'] || []).push(setTimeout(f, ms)); }
  dur(k) { (this[k + 'T'] || []).forEach(clearTimeout); this[k + 'T'] = []; }
"""


def js_tur(k):
    """componentDidMount içinde (self, azH tanımlı): ekrana girince (dokunulmadıysa) tur; azaltılmış harekette tur yok."""
    return ("    (function (k) { var el = document.querySelector('[data-tur=\"' + k + '\"]'); if (!el || azH || typeof IntersectionObserver === 'undefined') return;\n"
            "      var s = {}; s[k + 'On'] = false; self.setState(s); var ic = false;\n"
            "      self[k + 'Io'] = new IntersectionObserver(function (es) { var g = es[0].isIntersecting && es[0].intersectionRatio >= .5;\n"
            "        if (g && !ic && !self[k + 'Elle'] && !self[k + 'Kos']) self[k + 'Oyna'](); ic = g; }, { threshold: [0, .5] });\n"
            "      self[k + 'Io'].observe(el); })('%s');\n" % k)


def js_kapat(k):
    return "this.dur('%(k)s'); if (this.%(k)sIo) this.%(k)sIo.disconnect(); " % {'k': k}


CSS = (URUN_CSS + DK_CSS + AK_CSS + AD_CSS).replace('EASE', E)

PANO_CSS = r""".pg{background:#F6F1E9;font-size:15px}
.sec{padding:0 16px 44px}
.oneri{display:flex;align-items:center;gap:8px;margin:0 0 6px;padding-top:16px;border-top:1px dashed #D6CAB6;font-size:12px;font-weight:700;color:#A05A1C}
.oneri-alt{margin:0 0 16px;font-size:13px;color:#5C6078;text-wrap:balance}
.pg :focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
.h2 span.n{color:#F2A65A}
"""

H2 = '<h2 class="h2">Neler<br>yapabiliyor<span class="n">?</span></h2>'
HTML = """<div class="pg">
  <div style="padding: 18px 16px 10px">
    <h1 class="h2" style="font-size: 22px">LunaDream · Neler yapabiliyor? 4. tur</h1>
    <p style="margin: 6px 0 0; font-size: 13px; color: #5C6078">Beyaz arayüz kartı yok (Sihirli özellikler zaten öyle). Ürünün kendisi oynar: kubbe açılır, disk girer, lamba kısılır, kalkar. Ekrana girince bir tur oynar, sonra durur; dokununca istenen gösterilir.</p>
  </div>

  <section class="sec">
    <p class="oneri">A · Dergi kapağı</p>
    <p class="oneri-alt">Dev tek kelime, ürün önünde. Her kelimede zemin değişir: akşam, gece, uyku, sabah.</p>
    """ + H2 + dergi() + """
  </section>

  <section class="sec">
    <p class="oneri">B · Atlıkarınca</p>
    <p class="oneri-alt">Lamba ortada, dört fotoğraf çevresinde döner; öndeki anlatılır, lamba o işi yapar. Kaydır ya da dokun.</p>
    """ + H2 + karusel() + """
  </section>

  <section class="sec">
    <p class="oneri">C · Albüm</p>
    <p class="oneri-alt">Gerçek fotoğraflardan deste (ikisi müşteri). Kaydırınca üstteki kart atılır, alta girer.</p>
    """ + H2 + album() + """
  </section>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = {}; }
  componentDidMount() {
    var self = this, azH = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
""" + js_tur('dk') + js_tur('ak') + js_tur('ad') + """  }
  componentWillUnmount() { """ + js_kapat('dk') + js_kapat('ak') + js_kapat('ad') + """}
""" + JS_ORTAK + JS_DK + JS_AK + JS_AD + """  renderVals() {
    var self = this, S = this.state, o = { sihKiz: true, sihErkek: false };
    """ + js_dk_deger() + "    " + js_ak_deger() + "    " + js_ad_deger() + """    return Object.assign(o, dkV, akV, adV);
  }
}"""

if __name__ == '__main__':
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · Neler yapabiliyor 4', css=PANO_CSS + CSS) + HTML + TAIL.format(h=int(os.environ.get('OZ4_H', 2300)), js=JS))
    print('yazıldı:', os.path.abspath(OUT))
