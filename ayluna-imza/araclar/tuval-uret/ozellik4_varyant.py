# LunaDream · "Neler yapabiliyor?" 4. tur (22 Eki). Çalıştır: python3 ozellik4_varyant.py
# Kullanıcı (dokunulur afişten sonra): "Yine çok beğenmedim, sıkıcı geliyor gözüme."
# Teşhis: afiş, hemen üstteki Sihirli özellikler'in dört beyaz arayüz kartını (disk, ışık, Bluetooth, şarj) aynı dille tekrar ediyordu.
# Bu turda beyaz arayüz kartı yok; ürünün kendisi oynar (kubbe gerçekten açılır, lamba kısılır, kalkar), yazı büyük, hareket ürüne bağlı.
#   A · Dergi kapağı: dev tek kelime (Tak. Çal. Kıs. Şarj.), ürün kelimenin önünde; her kelimede zemin ve ürün değişir (akşam → gece → sabah).
#   B · Atlıkarınca (3B halkada fotoğraf balonları) ve C · Albüm (polaroid deste) taslağı git c70efe8'de. Eleştirmen eledi:
#   21 Eki kuralları "yörünge düğümleri geri getirilmez", "dönen/uçan kart, deste premium değil"; C'de ürün oynamıyor.
# Eleştirmen düzeltmeleri (A 8/10): "Taşı." taşıma/pil vaadi veriyordu → "Şarj." (lamba söner, ışık alttan yukarı dolar; kablo, port,
#   süre çizilmez); hikâye göstergesi gibi dolan çizgi yok, etkin sekme kısa amber çizgi; sabah zemini #FFFDF9 + 1 px kenar;
#   tur "Tak."ta biter; Kıs kelimeleri renk geçişi yerine amber kopya + opacity.
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
NOTA = '<svg viewBox="0 0 24 24"><path d="M9 17.5V5.5l10-2v12"></path><circle cx="6.5" cy="17.5" r="2.6"></circle><circle cx="16.5" cy="15.5" r="2.6"></circle></svg>'


def model(f):
    return ('<sc-if value="{{sihKiz}}" hint-placeholder-val="{{true}}">' + f('kiz') + '</sc-if>'
            '<sc-if value="{{sihErkek}}" hint-placeholder-val="{{false}}">' + f('erkek') + '</sc-if>')


# Ürün: gövde, gövdenin koyu kopyası, disk, kubbe, kubbenin koyu kopyası (ışık kısılınca koyular opacity ile belirir); notalar; zemin gölgesi
def urun():
    def m(md):
        u, a, t = PAR[md]
        return ('<span class="ur-k %s">' % md + ''.join('<img class="%s" src="%s%s" alt="">' % (c, B, s) for c, s in
                (('ur-alt', a), ('ur-alt koyu', a), ('ur-disk', DISK_AY), ('ur-ust', u), ('ur-ust koyu', u))) +
                '<span class="ur-dol"><img src="%s%s" alt=""></span></span>' % (B, t))
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
.x-sarj.oa .ur-dol{animation:sarjdol 2.8s EASE both}.x-sarj.oa .ur-dol img{animation:sarjdoli 2.8s EASE both}
@keyframes sarjdol{0%{opacity:0;transform:none}14%{opacity:1;transform:none}88%,100%{opacity:1;transform:translateY(-101%)}}
@keyframes sarjdoli{0%,14%{transform:none}88%,100%{transform:translateY(101%)}}
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
/* Şarj: koyu kopya penceresi yukarı kayar, içi aşağı (yerinde durur); ışık alttan yukarı dolar */
.ur-dol{position:absolute;inset:0;overflow:hidden;opacity:0}
.ur-dol img{filter:brightness(.38)}
.ur-n{position:absolute;width:26px;height:26px;opacity:0}
.ur-n svg{width:100%;height:100%;fill:none;stroke:#F2A65A;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.ur-n.n0{left:-14%;top:42%}.ur-n.n1{right:-16%;top:30%}.ur-n.n2{left:60%;top:6%}
.i1 .ur-k .koyu{opacity:.5}.i2 .ur-k .koyu{opacity:1}
""" + ciftle(URUN_CSS_SEK)

ACTIONS = ['tak', 'cal', 'kis', 'sarj']


# ---------------- A · Dergi kapağı ----------------
SV = lambda i, w: '<span class="sv s%d">%s<em aria-hidden="true">%s</em></span>' % (i, w, w)
DK = [('Tak.', 'Kubbeyi aç, masal diskini üstten tak.', 'Tak'),
      ('Çal.', 'Telefondaki ninni, Bluetooth ile lambadan çalar.', 'Çal'),
      ('Kıs.', SV(0, 'Parlak') + ', ' + SV(1, 'orta') + ', ' + SV(2, 'kısık') + '. Uykuya göre ayarla.', 'Kıs'),
      ('Şarj.', 'Şarjlı, kablosuz kullanılır.', 'Şarj')]


def dergi():
    return ('<div class="{{dkCls}}" data-tur="dk">' + ''.join('<span class="{{dkz%d}}"></span>' % i for i in range(4)) +
            '<p class="dk-soz" aria-hidden="true">' + ''.join('<span class="{{dkw%d}}">%s</span>' % (i, b[0]) for i, b in enumerate(DK)) + '</p>'
            '<p class="dk-alt" aria-live="polite">' + ''.join('<span class="{{dkc%d}}">%s</span>' % (i, b[1]) for i, b in enumerate(DK)) + '</p>'
            '<button class="dk-urun" type="button" onClick="{{dkUrunG}}" aria-label="Bu özelliği yeniden göster">' + urun() + '</button>'
            '<div class="dk-bar">' + ''.join('<button class="{{dkb%d}}" type="button" onClick="{{dkg%d}}"><b></b>%s</button>' % (i, i, b[2]) for i, b in enumerate(DK)) +
            '</div></div>')


DK_CSS = r"""/* A · Dergi kapağı: 358 × 520 */
.dk{position:relative;width:358px;height:520px;margin:16px auto 0;border-radius:24px;overflow:hidden;isolation:isolate}
.dk::after{content:"";position:absolute;inset:0;z-index:4;border-radius:inherit;box-shadow:inset 0 0 0 1px #E3D8C7;pointer-events:none}
/* Zemin perdesi: yeni renk alttan yükselir (geri dönüşte üstteki perdeler iner); ara gri ton olmaz */
.dk-z{position:absolute;inset:0;transform:translateY(101%);transition:transform .9s EASE}
.dk-z.on{transform:none}
.dk-z.z0{background:#F1E8DA}.dk-z.z1{background:#1A2142}.dk-z.z2{background:#0C1027}.dk-z.z3{background:#FFFDF9}
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
.dk-alt .sv{position:relative;display:inline-block}
.dk-alt .sv em{position:absolute;left:0;top:0;font-style:normal;color:#F2A65A;opacity:0;transition:opacity .3s EASE}
.i0 .dk-alt .s0 em,.i1 .dk-alt .s1 em,.i2 .dk-alt .s2 em{opacity:1}
.dk-urun{position:absolute;right:0;bottom:58px;width:200px;height:362px;padding:0;border:0;background:none;cursor:pointer;z-index:2;-webkit-tap-highlight-color:transparent}
.dk-urun:focus-visible{outline:2px solid #F2A65A;outline-offset:2px;border-radius:12px}
.dk .ur{right:4px;bottom:0;--uh:360px}
.dk.b1 .ur-hale,.dk.b2 .ur-hale{opacity:1}
.dk-bar{position:absolute;left:0;right:0;bottom:0;display:flex;height:56px;padding:0 6px;z-index:3}
.dk-bar button{position:relative;flex:1;height:56px;padding:6px 0 0;border:0;background:none;font:inherit;font-size:14px;font-weight:600;color:#5C6078;cursor:pointer;transition:color 0s .45s}
.dk-bar button b{position:absolute;left:50%;top:10px;width:24px;height:2px;margin-left:-12px;border-radius:1px;background:#F2A65A;transform:scaleX(0);transition:transform .4s EASE}
.dk-bar button.on{color:#1A2142}
.dk-bar button.on b{transform:none}
.b1 .dk-bar button,.b2 .dk-bar button{color:rgba(255,253,249,.66)}
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
            "    var dkV = { dkCls: 'dk b' + dB + ' x-' + %s[dB] + ' i' + (S.dkI || 0) + (dP ? (dP %% 2 ? ' oa' : ' ob') : '') + (S.dkOn === false ? ' bek' : S.dkOn ? ' gir' : ''),\n"
            "      dkUrunG: function () { self.dkDokun(dB); } };\n"
            "    [0, 1, 2, 3].forEach(function (i) { dkV['dkz' + i] = 'dk-z z' + i + (i <= dB ? ' on' : ''); dkV['dkw' + i] = i === dB ? 'on' : i < dB ? 'ust' : ''; dkV['dkc' + i] = i === dB ? 'on' : '';\n"
            "      dkV['dkb' + i] = i === dB ? 'on' : ''; dkV['dkg' + i] = function () { self.dkDokun(i); }; });\n" % str(ACTIONS))


JS_DK = """  dkGit(i) { var self = this; this.setState({ dkB: i, dkP: (this.state.dkP || 0) + 1, dkI: 0, dkOn: true });
    if (i === 2) { this.at('dk', 900, function () { self.setState({ dkI: 1 }); }); this.at('dk', 1800, function () { self.setState({ dkI: 2 }); }); } }
  dkOyna() { var self = this; this.dur('dk'); this.dkKos = true; this.dkGit(0);
    [1, 2, 3].forEach(function (i) { self.at('dk', i * 3400, function () { self.dkGit(i); }); });
    this.at('dk', 13600, function () { self.dkGit(0); }); this.at('dk', 16200, function () { self.dkKos = false; }); }
  dkDokun(i) { this.dur('dk'); this.dkKos = false; this.dkElle = true; this.dkGit(i); }
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


CSS = (URUN_CSS + DK_CSS).replace('EASE', E)

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
    <h1 class="h2" style="font-size: 22px">LunaDream · Neler yapabiliyor? 4. tur: Dergi kapağı</h1>
    <p style="margin: 6px 0 0; font-size: 13px; color: #5C6078">Beyaz arayüz kartı yok (Sihirli özellikler zaten öyle). Dev tek kelime, ürün önünde; ürünün kendisi oynar: kubbe kalkar ve disk girer, ninni notaları, lamba üç kademede kısılır, şarjda ışık alttan dolar. Her kelimede zemin perdesi alttan yükselir. Ekrana girince bir tur oynar, "Tak."ta durur; alttaki sözcüklere ya da lambaya dokununca o gösterilir.</p>
  </div>

  <section class="sec">
    <p class="oneri">A · Dergi kapağı (eleştirmen 8/10; Atlıkarınca ve Albüm elendi)</p>
    """ + H2 + dergi() + """
  </section>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = {}; }
  componentDidMount() {
    var self = this, azH = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
""" + js_tur('dk') + """  }
  componentWillUnmount() { """ + js_kapat('dk') + """}
""" + JS_ORTAK + JS_DK + """  renderVals() {
    var self = this, S = this.state, o = { sihKiz: true, sihErkek: false };
    """ + js_dk_deger() + """    return Object.assign(o, dkV);
  }
}"""

if __name__ == '__main__':
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · Neler yapabiliyor 4', css=PANO_CSS + CSS) + HTML + TAIL.format(h=int(os.environ.get('OZ4_H', 883)), js=JS))
    print('yazıldı:', os.path.abspath(OUT))
