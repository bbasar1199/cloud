# LunaDream · "Neler yapabiliyor?" = Afiş, ürün önde (22 Eki). Çalıştır: python3 ozellik3_varyant.py
# Kullanıcı: "Aydınlık sahne kısmını hiç ama hiç beğenmedim, yeni bir tarz deneyelim." (1. tur listeler "çok boğar, sıkıcı"; 2. tur açık
# stüdyo fotoğrafı + çip + halka.) Kullanıcının sitesindeki örnek: koyu zeminde ürün fotoğrafı, arayüz kartı ürünün arkasına girer (afiş).
# 3. tur (git f2c6b0c, cbc7a14): A Afiş 7/7, B Hikâye 8/4, C Bento 5/5; kullanıcı 22 Eki "1 · Afiş, ürün önde"yi seçti.
#   - Lamba kesimi kartların önünde (kartlar ürünün arkasına girer). Fotoğraf yerel Real-ESRGAN ile x2, kesim rembg (isnet-general-use);
#     ikisi aynı object-fit/position ile üst üste. Kartta ürüne bakan kenara iç boşluk, içerik dışa yaslı.
#   - Diski tak: kubbe açılır, disk üstten iner, kubbe kapanır (kullanıcı teyidi 22 Eki: "Kubbe açılıp üstten").
#   - Işığı kıs: kaydırıcı Parlak → Orta → Kısık; lambanın koyu kopyası (brightness .76, sabit) ve çevresindeki koyu hale opacity ile belirir.
#   - Kart başlıkları eylem; gölge yok (1 px çizgi); pasif yazı #5C6078; ray #F1E8DA.
# Kullanıcı 22 Eki (son karede duran afişin ekran görüntüsüyle): "Çalışmıyor ki bu kısım." Afiş yalnız bir kez, ekrana girince oynuyordu;
# kartlar resimdi, dokununca bir şey olmuyordu. Şimdi:
#   - Kartlar düğme: Diski tak → sıradaki disk takılır (adı ve görseli değişir); Telefondan çal → baştan bağlanıp çalar;
#     Işığı kıs → Parlak / Orta / Kısık (lamba gerçekten kısılır); Şarj et → pil dolar, fiş çıkar. Dokununca kendiliğinden tur durur.
#   - Kendiliğinden tur: ekrana girince kartlar sırayla gelir, sekanslar tek tek oynar (2,1 / 4,5 / 6,9 / 9,3 sn) ve durur; afiş ekrandan
#     çıkıp yeniden girince (dokunulmadıysa) bir kez daha oynar. Sonsuz döngü yok. Başlangıç ışığı Parlak.
#   - Sekanslar JS ile başlatılır: kartın sınıfı .oa / .ob arasında değişir (aynı anahtar karelerin iki adı), böylece her dokunuşta baştan oynar.
# luna_e.py bu dosyadan AFIS_CSS, afis(), js_afis_tur(), js_afis_yontem(), js_afis_deger(), js_afis_kapat() alır.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL
import sihirli2_varyant as S2
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE-Ozellik3.dc.html')

E = 'cubic-bezier(.2,.7,.2,1)'
B = '/_blob/'
AFIS = {'kiz': ('9fc836c3d9ab1f8fb163f2f255034bbc', '64acd86736049ff811d5db5e441aed6b'),      # c-an-kiz x2, lamba + disk yığını kesimi
        'erkek': ('d78da0ee8e43fa98686a43e648e14295', '55988cac00dcbf39b9ec247b6ccd9e3e')}    # c-erkek-disk x2, robot kesimi
# Diski tak kartında sırayla takılan diskler (kutudaki masallar; adlar Diskler bölümüyle aynı)
DISKLER = [('Ay ve yıldız', '4a3a69e8c1d8dddad8c33f8f463b8a0e'), ('Okyanus', 'a24f13e032569f76d64b9b0fbe8d74f7'), ('Uzay', 'b088d2c82561b76f6db997fbc3944059'),
           ('Deniz kızı', '04ed9ce4ae8a36619975caa7d2de9ad8'), ('Şato', 'bbd010d8d946edc8fef9c0404cba4ea2')]
ISIK = ['Parlak', 'Orta', 'Kısık']


def model(f):
    return ('<sc-if value="{{sihKiz}}" hint-placeholder-val="{{true}}">' + f('kiz') + '</sc-if>'
            '<sc-if value="{{sihErkek}}" hint-placeholder-val="{{false}}">' + f('erkek') + '</sc-if>')


IK = {
    'disk': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"></circle><circle cx="12" cy="12" r="2"></circle></svg>',
    'isik': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.5"></circle><path d="M12 3v2.5M12 18.5V21M3 12h2.5M18.5 12H21M5.6 5.6l1.8 1.8M16.6 16.6l1.8 1.8M5.6 18.4l1.8-1.8M16.6 7.4l1.8-1.8"></path></svg>',
    'bt': '<svg viewBox="0 0 24 24"><path d="M7 7l10 10-5 5V2l5 5L7 17"></path></svg>',
    'sarj': '<svg viewBox="0 0 24 24"><path d="M13 3L6 13h5l-1 8 7-10h-5z"></path></svg>',
    'fis': '<svg viewBox="0 0 24 24"><path d="M3 12h6M9 8.5h5a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H9zM16 10.5h4M16 13.5h4"></path></svg>',
    'ay': '<svg viewBox="0 0 24 24"><path d="M15.5 4.5a8 8 0 1 0 4 14.4A7 7 0 0 1 15.5 4.5z"></path></svg>',
}

# Diski tak ikonu: gövde, disk, kubbe ayrı katman (kubbe kalkar, disk üstten iner, kubbe kapanır). Çizim sihirli2 LAMBA / ROBOT ile aynı.
TK = {
    'kiz': ('<svg class="tk-g" viewBox="0 0 32 32" aria-hidden="true"><rect class="isk" x="10" y="14.6" width="12" height="6.2" rx="1.2"></rect><path d="M9.5 14.5v6.5M22.5 14.5v6.5"></path>'
            '<path d="M8 21h16c0 2.9-3.6 4.6-8 4.6S8 23.9 8 21z"></path><path d="M11.4 25.3c-.4 1.5-1.6 2.2-2.8 1.9M20.6 25.3c.4 1.5 1.6 2.2 2.8 1.9"></path></svg>',
            '<svg class="tk-k" viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="3.6" r="1.5"></circle>'
            '<path class="kb" d="M6 13C6 8.4 10.5 5.4 16 5.4S26 8.4 26 13a2 2 0 0 1-4 0 2 2 0 0 1-4 0 2 2 0 0 1-4 0 2 2 0 0 1-4 0 2 2 0 0 1-4 0z"></path></svg>'),
    'erkek': ('<svg class="tk-g" viewBox="0 0 32 32" aria-hidden="true"><path d="M8.5 16h15v4h-15z"></path><rect x="6" y="20" width="20" height="6.4" rx="3.2"></rect>'
              '<circle cx="10.4" cy="23.2" r="1.4"></circle><circle cx="16" cy="23.2" r="1.4"></circle><circle cx="21.6" cy="23.2" r="1.4"></circle></svg>',
              '<svg class="tk-k" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 6.4V4"></path><circle cx="16" cy="3" r="1.2"></circle><path class="kb" d="M7.5 16a8.5 8.5 0 0 1 17 0z"></path>'
              '<rect x="10" y="9.6" width="12" height="5.2" rx="2.6" fill="#1A2142"></rect><circle class="isk" cx="13.6" cy="12.2" r="1.1"></circle><circle class="isk" cx="18.4" cy="12.2" r="1.1"></circle></svg>'),
}


# ---- Arayüz kartları (düğme): başlık eylem; dokununca sekans baştan oynar ----
def kartlar(k):
    g = lambda i, gir, ad: '<button class="{{%sc%d}}" type="button" style="--g: %s" onClick="{{%sg%d}}" aria-label="%s">' % (k, i, gir, k, i, ad)
    disk = (g(0, '0s', 'Diski tak: sıradaki masal diski') + '<span class="nw-b">%s<span>Diski tak</span></span><span class="nw-d"><span class="tk">' % IK['disk'] +
            model(lambda m: TK[m][0] + '<img class="tk-d" src="{{%sDiskSrc}}" alt="">' % k + TK[m][1]) +
            '</span><span class="nw-dt"><b>{{%sDiskAd}}</b><small>6 + 6 disk</small></span></span></button>' % k)
    ninni = (g(1, '.5s', 'Telefondan çal: ninniyi baştan çal') + '<span class="nw-b">%s<span>Telefondan çal</span></span>' % IK['bt'] +
             '<span class="nw-pl"><span class="kap">' + IK['ay'] + '</span><span class="ad"><b>Ninni</b><small class="nw-dr"><i>Bağlanıyor</i><i>Çalıyor</i></small></span>'
             '<span class="eq"><i></i><i></i><i></i><i></i></span></span><span class="nw-pr"><b></b></span></button>')
    isik = (g(2, '1s', 'Işığı kıs: parlaklığı değiştir') + '<span class="nw-b">%s<span>Işığı kıs</span><span class="nw-dr sag">' % IK['isik'] +
            ''.join('<i>%s</i>' % w for w in ISIK) + '</span></span><span class="nw-sl"><i></i><b></b><span class="tut"></span><em></em><em></em><em></em></span></button>')
    sarj = (g(3, '1.5s', 'Şarj et: şarjı göster') + '<span class="nw-b">%s<span>Şarj et</span></span>' % IK['sarj'] +
            '<span class="nw-sj"><span class="fis">' + IK['fis'] + '</span><span class="bat"><i></i><i></i><i></i><i></i></span></span>'
            '<span class="nw-dr alt"><i>Şarj oluyor</i><i>Kablosuz</i></span></button>')
    return disk + ninni + isik + sarj


# Afiş (ürün önde): 358 × 480. Katmanlar: fotoğraf → koyu hale → kartlar → kesim → kesimin koyu kopyası (ışık kısılınca belirir)
def afis(k='a'):
    gor = lambda i, cls: model(lambda m: '<img class="%s %s" src="%s%s" alt="">' % (cls, m, B, AFIS[m][i]))
    return ('<div class="{{%sCls}}" data-tur="%s">' % (k, k) + gor(0, 'na-img') + '<span class="na-hale" aria-hidden="true"></span>' +
            kartlar(k) + gor(1, 'na-kes') + gor(1, 'na-kes koyu') + '</div><p class="na-ipucu">Kartlara dokunup dene.</p>')


def js_afis_deger(k='a', erkek='false'):
    """renderVals içinde (self ve S tanımlı): <k>V nesnesi (dönüşe ...<k>V ile katılır); erkek: Erkek modeli seçili mi (JS ifadesi)."""
    return ("var %(k)sD = %(d)s, %(k)sP = S.%(k)sP || [0, 0, 0, 0], %(k)sI = S.%(k)sIsik || 0, %(k)sDi = S.%(k)sDisk || 0;\n"
            "    var %(k)sV = { %(k)sCls: 'na i' + %(k)sI + ((%(e)s) ? ' erkek' : '') + (S.%(k)sOn === false ? ' bek' : S.%(k)sOn ? ' gir' : ''),\n"
            "      %(k)sDiskSrc: '/_blob/' + %(k)sD[%(k)sDi][1], %(k)sDiskAd: %(k)sD[%(k)sDi][0] };\n"
            "    ['nw nw-disk k-disk', 'nw nw-ninni k-ninni', 'nw nw-isik k-isik', 'nw nw-sarj k-sarj'].forEach(function (c, i) {\n"
            "      %(k)sV['%(k)sc' + i] = c + (%(k)sP[i] ? (%(k)sP[i] %% 2 ? ' oa' : ' ob') : ''); %(k)sV['%(k)sg' + i] = function () { self.%(k)sDokun(i); }; });\n"
            % {'k': k, 'e': erkek, 'd': str([list(x) for x in DISKLER])})


def js_afis_yontem(k='a'):
    """Component sınıfına eklenecek yöntemler: <k>Oyna (kendiliğinden tur), <k>Cal (kartın sekansını baştan oynat), <k>Dokun (dokunuş)."""
    return ("  %(k)sOyna() { var self = this; (this.%(k)sT || []).forEach(clearTimeout); this.%(k)sT = []; this.%(k)sKos = true;\n"
            "    var at = function (ms, f) { self.%(k)sT.push(setTimeout(f, ms)); };\n"
            "    this.setState({ %(k)sOn: true, %(k)sIsik: 0 });\n"
            "    at(2100, function () { self.%(k)sCal(0); }); at(4500, function () { self.%(k)sCal(1); });\n"
            "    at(6900, function () { self.setState({ %(k)sIsik: 1 }); }); at(7700, function () { self.setState({ %(k)sIsik: 2 }); });\n"
            "    at(9300, function () { self.%(k)sCal(3); }); at(11700, function () { self.%(k)sKos = false; }); }\n"
            "  %(k)sCal(i) { var p = (this.state.%(k)sP || [0, 0, 0, 0]).slice(); p[i]++; this.setState({ %(k)sP: p }); }\n"
            "  %(k)sDokun(i) { (this.%(k)sT || []).forEach(clearTimeout); this.%(k)sKos = false; this.%(k)sElle = true; var S = this.state, o = { %(k)sOn: true };\n"
            "    if (i === 0) o.%(k)sDisk = ((S.%(k)sDisk || 0) + 1) %% %(n)d;\n"
            "    if (i === 2) o.%(k)sIsik = ((S.%(k)sIsik || 0) + 1) %% 3;\n"
            "    this.setState(o); if (i !== 2) this.%(k)sCal(i); }\n" % {'k': k, 'n': len(DISKLER)})


def js_afis_tur(k='a'):
    """componentDidMount içinde (self ve azH tanımlı): ekrana girince tur; çıkıp yeniden girince (dokunulmadıysa) bir kez daha.
    Azaltılmış harekette tur yok, son kare durur; dokunuşlar çalışır."""
    return ("    (function (k) { var el = document.querySelector('[data-tur=\"' + k + '\"]'); if (!el || azH || typeof IntersectionObserver === 'undefined') return;\n"
            "      var s = {}; s[k + 'On'] = false; self.setState(s); var ic = false;\n"
            "      self[k + 'Io'] = new IntersectionObserver(function (es) { var g = es[0].isIntersecting && es[0].intersectionRatio >= .5;\n"
            "        if (g && !ic && !self[k + 'Elle'] && !self[k + 'Kos']) self[k + 'Oyna'](); ic = g; }, { threshold: [0, .5] });\n"
            "      self[k + 'Io'].observe(el); })('%s');\n" % k)


def js_afis_kapat(k='a'):
    """componentWillUnmount içinde."""
    return "(this.%(k)sT || []).forEach(clearTimeout); if (this.%(k)sIo) this.%(k)sIo.disconnect(); " % {'k': k}


def ciftle(css):
    """Sekans kuralları .oa ve .ob için: her @keyframes adının '2' ekli kopyası üretilir, .ob kuralları o adı kullanır."""
    import re
    adlar = re.findall(r'@keyframes (\w+)', css)
    kopya = css
    for a in adlar:
        kopya = re.sub(r'\b%s\b' % a, a + '2', kopya)
    return css + re.sub(r'\.oa\b', '.ob', kopya)


# Sekanslar (2,4 sn, bir kez); .oa / .ob kartın sınıfı. Son kare taban stille aynı.
SEKANS_CSS = ciftle(r"""
.oa .tk-k{animation:tkk 2.4s EASE both}.oa .tk-d{animation:tkd 2.4s EASE both}
@keyframes tkk{0%{transform:none}17%,58%{transform:translateY(-10px)}75%,100%{transform:none}}
@keyframes tkd{0%,17%{opacity:0;transform:translateY(-26px)}21%{opacity:1;transform:translateY(-24px)}40%,60%{opacity:1;transform:none}75%,100%{opacity:0;transform:translateY(2px)}}
.oa .nw-pl .eq i{animation:nwses .8s EASE 3}
@keyframes nwses{0%,100%{transform:scaleY(.3)}50%{transform:scaleY(1)}}
.oa .nw-pr b{animation:nwp 2.4s EASE both}
@keyframes nwp{0%,25%{transform:scaleX(0)}100%{transform:scaleX(.62)}}
.oa.nw-ninni .nw-dr i:first-child{animation:nwr1 2.4s EASE both}.oa.nw-ninni .nw-dr i:last-child{animation:nwr2 2.4s EASE both}
@keyframes nwr1{0%,20%{opacity:1}25%,100%{opacity:0}}
@keyframes nwr2{0%,22%{opacity:0}27%,100%{opacity:1}}
.oa .nw-sj .bat i:nth-child(1){animation:pl1x 2.4s EASE both}.oa .nw-sj .bat i:nth-child(2){animation:pl2x 2.4s EASE both}
.oa .nw-sj .bat i:nth-child(3){animation:pl3x 2.4s EASE both}.oa .nw-sj .bat i:nth-child(4){animation:pl4x 2.4s EASE both}
@keyframes pl1x{0%{opacity:.12}10%,100%{opacity:1}}
@keyframes pl2x{0%,10%{opacity:.12}22%,100%{opacity:1}}
@keyframes pl3x{0%,22%{opacity:.12}34%,100%{opacity:1}}
@keyframes pl4x{0%,34%{opacity:.12}46%,100%{opacity:1}}
.oa .nw-sj .fis{animation:nwf 2.4s EASE both}
@keyframes nwf{0%,56%{opacity:1;transform:none}64%,100%{opacity:0;transform:translateX(-10px)}}
.oa.nw-sarj .nw-dr i:first-child{animation:nws1 2.4s EASE both}.oa.nw-sarj .nw-dr i:last-child{animation:nws2 2.4s EASE both}
@keyframes nws1{0%,58%{opacity:1}64%,100%{opacity:0}}
@keyframes nws2{0%,60%{opacity:0}66%,100%{opacity:1}}
""")

# Kartlar + afiş (sayfaya bu girer). Afiş 358 px tabanlı; dar telefonda ve masaüstünde zoom ile orantılı.
AFIS_CSS = (r"""/* Arayüz kartı (düğme): beyaz, 18 köşe, 1 px çizgi (gölge yok); --g giriş gecikmesi */
.nw{position:absolute;display:flex;flex-direction:column;gap:8px;padding:10px 12px 12px;border:0;border-radius:18px;background:#FFFDF9;color:#1A2142;box-shadow:inset 0 0 0 1px rgba(26,33,66,.1);
  font:inherit;text-align:left;cursor:pointer;-webkit-tap-highlight-color:transparent;--g:0s}
.nw:focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
.nw>span{display:flex}
.bek .nw{opacity:0}
.gir .nw{animation:nwgir .6s EASE both;animation-delay:var(--g)}
@keyframes nwgir{from{opacity:0;transform:translateY(14px)}}
.nw-b{align-items:center;gap:6px;font-size:13px;font-weight:700;color:#1A2142;white-space:nowrap}
.nw-b svg{width:16px;height:16px;flex:none;fill:none;stroke:#1A2142;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.nw-dr{position:relative;display:grid}
.nw-dr i{grid-area:1/1;font-style:normal;opacity:0}
.nw-dr i:last-child{opacity:1}
.nw-dr.sag{margin-left:auto;font-size:12px;font-weight:600;color:#5C6078}
/* Diski tak: kubbe kalkar, disk üstten iner, kubbe kapanır. Son kare: kubbe kapalı */
.nw-d{align-items:center;gap:10px}
.tk{position:relative;flex:none;width:48px;height:48px;border-radius:12px;background:#F1E8DA;overflow:hidden}
.tk svg{position:absolute;left:8px;top:10px;width:32px;height:32px;fill:none;stroke:#1A2142;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.tk .kb{fill:#FFFDF9}
.tk .isk{fill:#F2A65A;stroke:none}
.tk-d{position:absolute;left:17px;top:16px;width:14px;height:14px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 1px #1A2142;opacity:0}
.nw-dt{display:flex;flex-direction:column;gap:1px;min-width:0;line-height:1.25}
.nw-dt b{font-size:15px;white-space:nowrap}
.nw-dt small{font-size:12px;color:#5C6078}
/* Işığı kıs: üç kademe, durum sınıfı afişte (i0 Parlak, i1 Orta, i2 Kısık); kaydırıcı ve lamba geçişle değişir */
.nw-sl{position:relative;height:6px;margin:8px 0 4px;border-radius:3px;background:#F1E8DA}
.nw-sl>b{position:absolute;inset:0;border-radius:3px;background:#F2A65A;transform-origin:0 50%;transform:scaleX(1);transition:transform .6s EASE}
.nw-sl em{position:absolute;top:1px;width:4px;height:4px;margin-left:-2px;border-radius:50%;background:#C9BCA6}
.nw-sl em:nth-of-type(1){left:10px}.nw-sl em:nth-of-type(2){left:50%}.nw-sl em:nth-of-type(3){left:calc(100% - 10px)}
.nw-sl .tut{position:absolute;left:0;top:-7px;z-index:1;width:calc(100% - 20px);height:20px;transform:translateX(100%);transition:transform .6s EASE}
.nw-sl .tut::after{content:"";position:absolute;left:0;top:0;width:20px;height:20px;border-radius:50%;background:#FFFDF9;box-shadow:0 0 0 1.5px #1A2142}
.i1 .nw-sl>b{transform:scaleX(.5)}.i1 .nw-sl .tut{transform:translateX(50%)}
.i2 .nw-sl>b{transform:scaleX(.08)}.i2 .nw-sl .tut{transform:none}
.nw-isik .nw-dr i{opacity:0;transition:opacity .3s EASE}
.i0 .nw-isik .nw-dr i:nth-child(1),.i1 .nw-isik .nw-dr i:nth-child(2),.i2 .nw-isik .nw-dr i:nth-child(3){opacity:1}
/* Telefondan çal: bağlanır, çalar (ses çubukları üç kez), ilerleme dolar */
.nw-pl{align-items:center;gap:10px}
.nw-pl .kap{display:grid;place-items:center;flex:none;width:36px;height:36px;border-radius:10px;background:#1A2142}
.nw-pl .kap svg{width:19px;height:19px;fill:#F2A65A}
.nw-pl .ad{display:flex;flex-direction:column;flex:1;min-width:0;line-height:1.25}
.nw-pl .ad b{font-size:15px}.nw-pl .ad small{font-size:12px;color:#5C6078}
.nw-pl .eq{height:16px;margin:0;animation:none}
.nw-pl .eq i{height:16px;animation:none;transform:scaleY(.55)}
.nw-pl .eq i:nth-child(2){transform:scaleY(.9)}.nw-pl .eq i:nth-child(3){transform:scaleY(.4)}.nw-pl .eq i:nth-child(4){transform:scaleY(.7)}
.nw-pr{position:relative;display:block!important;height:4px;border-radius:2px;background:#F1E8DA;overflow:hidden}
.nw-pr b{position:absolute;inset:0;background:#1A2142;transform-origin:0 50%;transform:scaleX(.62)}
/* Şarj et: pil dolar, fiş çıkar, "Kablosuz" (lamba çizilmez; pil süresi yok) */
.nw-sj{align-items:center;gap:6px;height:28px}
.nw-sj .fis{width:24px;height:24px;opacity:0}
.nw-sj .fis svg{width:24px;height:24px;fill:none;stroke:#1A2142;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.nw-sj .bat{position:relative;display:flex;gap:3px;width:58px;height:26px;padding:3px;border:1.5px solid #1A2142;border-radius:7px}
.nw-sj .bat::after{content:"";position:absolute;right:-6px;top:7px;width:4px;height:9px;border-radius:0 2px 2px 0;background:#1A2142}
.nw-sj .bat i{flex:1;border-radius:2.5px;background:#1A2142}
.nw-dr.alt{display:grid!important;font-size:13px;font-weight:600}

/* Afiş (ürün önde) */
.na{position:relative;width:358px;height:480px;margin:16px auto 0;border-radius:24px;overflow:hidden;background:#141A36;--op:50% 78%;isolation:isolate}
.na-img,.na-kes{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:var(--op);pointer-events:none}
.na-img{z-index:0}
.na-hale{position:absolute;left:50%;top:62%;z-index:1;width:340px;height:340px;margin:-170px 0 0 -170px;border-radius:50%;background:radial-gradient(closest-side,rgba(12,16,39,.35),rgba(12,16,39,0));pointer-events:none}
.na .nw{z-index:2}
.na-kes{z-index:3}
.na-kes.koyu{z-index:4;filter:brightness(.76)}
.na-hale,.na-kes.koyu{opacity:0;transition:opacity .6s EASE}
.na.i1 .na-hale,.na.i1 .na-kes.koyu{opacity:.5}
.na.i2 .na-hale,.na.i2 .na-kes.koyu{opacity:1}
.na-ipucu{width:358px;max-width:100%;margin:10px auto 0;font-size:13px;color:#5C6078}
/* Kartlar: üstte ikisi tam görünür; alttakiler ürünün arkasına girer, ürüne bakan kenarda iç boşluk */
.k-disk{left:12px;top:16px;width:164px}
.k-ninni{right:12px;top:70px;width:160px}
.k-isik{left:12px;top:236px;width:150px;padding-right:44px!important}
.k-sarj{right:12px;bottom:16px;width:140px;padding-left:54px!important}
.na.erkek .k-isik{top:226px}
.na.erkek .k-sarj{width:128px;padding-left:58px!important;bottom:12px}
.na.erkek .k-sarj .fis{display:none}
""" + SEKANS_CSS + r"""
/* 358 px tabanlı afiş: 375 / 360 px telefonda küçülür, masaüstü sütununda büyür (zoom: konumlar ve ürün birlikte) */
@media (max-width:389px){.na{zoom:.958}}
@media (max-width:374px){.na{zoom:.916}}
@media (max-width:359px){.na{zoom:.86}}
@media (min-width:1024px){.na{zoom:1.1}}
""").replace('EASE', E)

PANO_CSS = r""".pg{background:#F6F1E9;font-size:15px}
.sec{padding:0 16px 44px}
.oneri{display:flex;align-items:center;gap:8px;margin:0 0 6px;padding-top:16px;border-top:1px dashed #D6CAB6;font-size:12px;font-weight:700;color:#A05A1C}
.oneri-alt{margin:0 0 16px;font-size:13px;color:#5C6078;text-wrap:balance}
.pg :focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
.h2 span.n{color:#F2A65A}
"""

HTML = """<div class="pg">
  <div style="padding: 18px 16px 10px">
    <h1 class="h2" style="font-size: 22px">LunaDream · Neler yapabiliyor? (seçilen: Afiş, ürün önde)</h1>
    <p style="margin: 6px 0 0; font-size: 13px; color: #5C6078">Ekrana girince kartlar sırayla gelir ve oynar, sonra durur. Kartlara dokununca: disk değişip takılır, ninni baştan çalar, ışık Parlak / Orta / Kısık (lamba da kısılır), şarj dolar.</p>
  </div>

  <section class="sec">
    <p class="oneri">Afiş, ürün önde · kartlar dokunulur</p>
    <h2 class="h2">Neler<br>yapabiliyor<span class="n">?</span></h2>
    """ + afis('a') + """
  </section>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = {}; }
  componentDidMount() {
    var self = this, azH = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
""" + js_afis_tur('a') + """  }
  componentWillUnmount() { """ + js_afis_kapat('a') + """}
""" + js_afis_yontem('a') + """  renderVals() {
    var self = this, S = this.state, o = { sihKiz: true, sihErkek: false };
    """ + js_afis_deger('a', 'o.sihErkek') + """    return Object.assign(o, aV);
  }
}"""

if __name__ == '__main__':
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · Neler yapabiliyor 3', css=S2.MINI_CSS + PANO_CSS + AFIS_CSS) + HTML + TAIL.format(h=int(os.environ.get('OZ3_H', 814)), js=JS))
    print('yazıldı:', os.path.abspath(OUT))
