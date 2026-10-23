# Fikir panoları için ortak başlık ve CSS (LunaDreamV2 ile aynı dil)
HEAD = '''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Young+Serif&amp;family=Onest:wght@400;500;600;700&amp;display=swap">
<style>
body{{margin:0;background:#F6F1E9}}
a{{color:#1A2142}}a:hover{{color:#2B3463}}
.pg{{width:390px;background:#F6F1E9;color:#1A2142;font-family:"Onest",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;font-size:16px;line-height:1.5;-webkit-font-smoothing:antialiased;overflow:hidden;position:relative}}
.pg *{{box-sizing:border-box}}
.ser{{font-family:"Young Serif",Georgia,"Times New Roman",serif;font-weight:400;letter-spacing:-.01em}}
.px{{padding-left:16px;padding-right:16px}}
.mut{{color:#5C6078}}
.h2{{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:30px;line-height:1.06;letter-spacing:-.02em;margin:0;text-wrap:balance}}
.ico{{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;flex:none}}
.btn{{display:flex;align-items:center;justify-content:center;gap:10px;width:100%;min-height:58px;border:0;border-radius:16px;background:#1A2142;color:#FFFDF9;font:inherit;font-size:17px;font-weight:600;cursor:pointer;text-decoration:none;transition:transform .15s cubic-bezier(.2,.7,.2,1)}}
.btn:active{{transform:scale(.985)}}
.etiket{{display:flex;justify-content:space-between;align-items:baseline;font-size:12px;font-weight:600;letter-spacing:.02em;color:#1A2142}}
.etiket>span:first-child{{text-transform:uppercase;letter-spacing:.12em;font-size:12px;color:#766B5B}}
.rozet{{display:inline-block;padding:2px 7px;border-radius:999px;font-size:12px;font-weight:700;letter-spacing:.02em;line-height:1.3;white-space:nowrap}}
.odeme{{display:flex;flex-direction:column;justify-content:center;height:62px;padding:0 12px;border-radius:14px;border:1.5px solid;font:inherit;color:#1A2142;text-align:left;cursor:pointer;transition:border-color .25s,background .25s,transform .2s cubic-bezier(.2,.7,.2,1)}}
.odeme:active{{transform:scale(.98)}}
.not{{margin:0 0 6px;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#766B5B}}
{css}
@media (prefers-reduced-motion:reduce){{.pg *{{transition:none!important;animation:none!important}}}}
</style>
</helmet>
'''
TAIL = '''</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":390,"height":{h}}}}}'>
{js}
</script>
</body>
</html>
'''
TL_JS = "function TL(n, kurus) { var s = (kurus ? n.toFixed(2) : String(Math.round(n))).split('.'); return '₺' + s[0].replace(/\\B(?=(\\d{3})+(?!\\d))/g, '.') + (kurus ? ',' + s[1] : ''); }"
# Aynı gün kargo (kullanıcı, 18 Eki: "bugün 16'ya kadar verilen siparişler aynı gün kargoda"). İstanbul saatiyle iş günü
# (Pzt–Cum) 16.00'dan önce verilen sipariş bugün kargoda, sonrası bir sonraki iş günü. Resmî tatiller canlıda tema ayarı.
KARGO_JS = """function KARGO(ms) {
      var ist = new Date(new Date(ms).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
      var isg = function (d) { return d.getDay() !== 0 && d.getDay() !== 6; }, IKI = function (n) { return n < 10 ? '0' + n : String(n); };
      var gun0 = new Date(ist.getFullYear(), ist.getMonth(), ist.getDate()), kalan = gun0.getTime() + 16 * 3600000 - ist.getTime();
      var bugun = isg(ist) && kalan > 0, gun = new Date(gun0);
      if (!bugun) do { gun.setDate(gun.getDate() + 1); } while (!isg(gun));
      var fark = Math.round((gun - gun0) / 86400000), GUN = ['Pazar', 'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi'];
      var hh = Math.floor(kalan / 3600000), mi = Math.floor(kalan / 60000) % 60, ss = Math.floor(kalan / 1000) % 60;
      return { bugun: bugun, gun: gun, sayac: bugun ? IKI(hh) + ':' + IKI(mi) + ':' + IKI(ss) : '',
        metin: bugun ? 'Bugün 16.00’ya kadar verilen siparişler aynı gün kargoda' : 'Bugün verilen siparişler ' + (fark === 1 ? 'yarın' : GUN[gun.getDay()]) + ' kargoda',
        aria: bugun ? 'Aynı gün kargo için ' + hh + ' saat ' + mi + ' dakika kaldı' : '' };
    }"""


# "Odanın geri kalanı için" şeridi (23 Eki, kullanıcı: "burayı kaydırmalı yap, çok uzun iskelet webde iyi durmuyor"): masaüstünde de
# tek satır kayar (ayluna.css); oklar yalnız masaüstünde görünür, telefonda şerit parmakla kaydırılır. Şablonda durur ki her saniyelik çizimde silinmesin.
SERIT_OK_CSS = '.serit-sag{display:flex;align-items:center;gap:12px}.serit-ok,.g-ok{display:none}\n'


def serit_ok(ad, geri='{{kayGeri}}', ileri='{{kayIleri}}'):
    """Masaüstü kaydırma okları; oklar hangi satırdaysa onun hemen altındaki şeridi kaydırır (KAY)."""
    return ('<span class="serit-ok"><button type="button" aria-label="Önceki ' + ad + '" onClick="' + geri + '"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.5 6l-6 6 6 6"></path></svg></button>'
            '<button type="button" aria-label="Sonraki ' + ad + '" onClick="' + ileri + '"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9.5 6l6 6-6 6"></path></svg></button></span>')


SERIT_OK = serit_ok('ürünler')
# KAY: okun satırından yukarı doğru, hemen ardından .noscroll şerit gelen ilk öğeyi bulur; yoksa bölümdeki ilk şerit
KAY_JS = """function KAY(y) { return function (e) { var t = e && (e.currentTarget || e.target), r = t && t.closest && t.closest('.serit-ok'), s = null;
      while (r && !s && r.tagName !== 'SECTION') { var n = r.nextElementSibling; if (n && n.classList.contains('noscroll')) s = n; r = r.parentElement; }
      if (!s) { var b = t && t.closest && t.closest('section'); s = b && b.querySelector('.noscroll'); }
      if (s) s.scrollBy({ left: y * Math.max(220, s.clientWidth * .8), behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); }; }
"""

# Ürün galerisi okları (23 Eki, masaüstü: fareyle kaydırılamıyordu). Telefonda gizli (parmakla kayar); masaüstünde fotoğrafın iki yanında,
# üzerine gelince belirir. Sondan başa döner. Elle kaydırmayla aynı: galerinin kendi onScroll'u sırayı ve otomatik geçişi günceller.
def gal_ok(ad='fotoğraf'):
    return ('<button class="g-ok g-geri" type="button" aria-label="Önceki ' + ad + '" onClick="{{galGeri}}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.5 6l-6 6 6 6"></path></svg></button>'
            '<button class="g-ok g-ileri" type="button" aria-label="Sonraki ' + ad + '" onClick="{{galIleri}}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9.5 6l6 6-6 6"></path></svg></button>')


GAL_OK = gal_ok()
GALOK_JS = """function GALOK(y) { return function (e) { var t = e && (e.currentTarget || e.target), k = t && t.closest && t.closest('.sahne, .hero, .gal, .slayt'), s = k && k.querySelector('.kare-foto, .h-iz, .g-iz, .s-iz');
      if (!s || !s.clientWidth) return; var m = Math.max(1, Math.round(s.scrollWidth / s.clientWidth)), n = (Math.round(s.scrollLeft / s.clientWidth) + y + m) % m;
      s.scrollTo({ left: n * s.clientWidth, behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); }; }
"""

# Ürün galerisi Shopify'daki gibi (kullanıcı, 19 Eki: "fotoğraf kısmını Shopify'daki ile aynı şekle getir"): canlı sıra, kare görsel.
# Liste araclar/canli_galeri.py ile üretilir (uydurma yorum, sağlık iddiası, kutuda olmayan şey çıkarılır).
def canli_galeri(handle):
    import json, os
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'ogrenme', 'galeri-canli.json')
    return [x['id'] for x in json.load(open(p))[handle]]


# Masaüstü iki sütun (kullanıcı, 19 Eki: "mağazanın masaüstü görünüşünü de yapmak lazım"): galeri ile satın alma kutusu
# tek sarmalayıcıda (.urun-ust); solda galeri, sağda satın alma. Telefonda etkisiz.
# oz: satın alma kutusundaki özellik kartları. Masaüstünde galerinin altına geçer (eleştirmen önerisi, kullanıcı seçti 19 Eki):
# DOM'da her an tek kopya olur; renderVals'taki masa/tel bayrağı hangisinin çizileceğini seçer (tuvalde telefon yeri).
MASA_JS = "    var MASA = !!(window.Ayluna && window.matchMedia && matchMedia('(min-width: 1024px)').matches);  // yalnız sitede; tuval hep telefon\n    return { masa: MASA, tel: !MASA,"


def masa_bayrak(js):
    i = js.index('renderVals()')
    j = js.index('\n    return {', i) + 1  # renderVals'ın kendi dönüşü (iç işlevlerin daha içerideki return'leri değil)
    return js[:j] + MASA_JS + js[j + len('    return {'):]


# 23 Eki: imza sayfaları oz vermez (kullanıcı: "emoji benefit neden ürün görsellerinin altında" → "Sağa, fiyatın altına");
# özellik kartları masaüstünde de satın alma kutusunda, galeri solda yapışkan. oz yolu ileride gerekirse diye duruyor.
def urun_ust(html, bas, oz=None):
    sol = ''
    if oz:
        assert html.count(oz) == 1, 'özellik bloğu tek olmalı'
        html = html.replace(oz, '<sc-if value="{{tel}}" hint-placeholder-val="{{true}}">' + oz + '</sc-if>')
        sol = '\n    <sc-if value="{{masa}}" hint-placeholder-val="{{false}}"><div class="sol-oz">' + oz + '</div></sc-if>\n  '
    i = html.index(bas)
    k = html.rindex('<section', 0, html.index('id="siparis"', i))
    d, p = 0, k
    while True:
        a, c = html.find('<section', p + 1), html.find('</section>', p + 1)
        if a != -1 and a < c:
            d, p = d + 1, a
        elif d:
            d, p = d - 1, c
        else:
            son = c + len('</section>')
            break
    if oz:
        return (html[:i] + '<div class="urun-ust"><div class="urun-sol">' + html[i:k] + sol + '</div>\n  '
                + html[k:son] + '</div>' + html[son:])
    return html[:i] + '<div class="urun-ust">' + html[i:son] + '</div>' + html[son:]


# Müşteri mesajları (19 Eki): LunaDream siparişlerinden gerçek, izinli sohbet ekran görüntüleri (canvas/musteri, tuval asset'i).
# Kullanıcı: "WhatsApp konuşmaları için olan kısım eksik, bir tek LunaDream'de var" → diğer ürün sayfalarında da var. Mesajlar LunaDream
# siparişlerinden olduğu için başlığın altında bu yazar (müşteri o ürün hakkında yazılmış sanmasın). Kutu vaadiyle ya da kargo sözüyle
# çelişen iki mesaj (mesaj-6 "hayvanlar çıkmadı", mesaj-7 "gümrükte") yok. Kartlar dokununca büyür; Esc ya da dokunuş kapatır.
MESAJ_ID = ['bfa2c1457ff701500133bafa4a53605c', '32cce494ace36080ef05c6fda3dddcab', 'dd91892546cddf3d9e1b066b51659996',
            'f588a714a98cbc77c1ea79dbd24d8f2e', '9f72b52adc531fbbc2c19b68852ac418', '3389d58e6756cdaf84214ee47c529234']
MESAJ_CSS = r"""
/* Sizden gelen mesajlar (ortak.mesaj_bolum) */
.mesaj-bol{padding-top:8px}
.mesaj-bol .serit-ok,.g-ok{display:none}
.m-alt{margin:8px 0 0;font-size:15px;line-height:1.45;color:#5C6078}
.mkarma{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:16px;padding:16px 16px 4px;scrollbar-width:none}
.mkarma::-webkit-scrollbar{display:none}
.mkarma button{flex:none;height:320px;aspect-ratio:9/16;padding:0;border:1px solid #E3D8C7;border-radius:18px;overflow:hidden;background:#FFFDF9;scroll-snap-align:start;cursor:pointer}
.mkarma button:active{transform:scale(.98)}
.mkarma img{display:block;width:100%;height:100%;object-fit:cover;object-position:50% 0}
.mbuyuk{position:fixed;inset:0;z-index:1000;display:grid;place-items:center;padding:56px 16px 24px;background:rgba(12,16,39,.92)}
/* Büyük görünüm üst menünün (900) ve satın alma çubuğunun üstünde; görsel ekran boyunu aşmaz (23 Eki, masaüstü denetimi) */
.mbuyuk img{width:auto;max-width:100%;max-height:calc(100vh - 80px);max-height:calc(100dvh - 80px);border-radius:16px;object-fit:contain}
.mb-x{position:absolute;top:10px;right:10px;width:48px;height:48px;padding:0;border:0;border-radius:50%;background:rgba(255,253,249,.14);display:grid;place-items:center;cursor:pointer}
.mb-x svg{width:22px;height:22px;fill:none;stroke:#FFFDF9;stroke-width:2;stroke-linecap:round}
"""


def mesaj_bolum(baslik):
    """Başlık (panonun kendi h2 biçimiyle) + not + mesaj şeridi + büyük görünüm."""
    return ('\n  <!-- Sizden gelen mesajlar (ortak.mesaj_bolum, 19 Eki) -->\n'
            '  <section class="bolum mesaj-bol" id="mesajlar">\n'
            '    <div class="px">' + baslik + '<p class="m-alt">LunaDream siparişlerinden; müşterilerimizin izniyle paylaşılan gerçek sohbetler.<span class="dokun"> Dokun, büyüsün.</span></p>' + serit_ok('mesajlar', '{{mGeri}}', '{{mIleri}}') + '</div>\n'
            '    <div class="noscroll mkarma"><sc-for list="{{mesajlar}}" as="m" hint-placeholder-count="3"><button type="button" onClick="{{m.ac}}" aria-label="{{m.n}}, büyüt">'
            '<img src="{{m.src}}" alt="{{m.n}}" loading="lazy"></button></sc-for><span aria-hidden="true" style="flex: 0 0 6px"></span></div>\n'
            '  </section>\n'
            '  <sc-if value="{{buyukVar}}" hint-placeholder-val="{{false}}"><div class="mbuyuk" role="dialog" aria-modal="true" aria-label="{{buyukAd}}" onClick="{{buyukKapat}}">'
            '<img src="{{buyuk}}" alt="{{buyukAd}}"><button class="mb-x" type="button" aria-label="Kapat"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg></button></div></sc-if>\n')


MESAJ_VERI = """var _mk = this;
    """ + KAY_JS.replace('function KAY(', 'function _mKAY(') + GALOK_JS + """    function _mKapat() { _mk.setState({ buyuk: null }); document.documentElement.style.overflow = ''; }
    if (!_mk._mEsc) { _mk._mEsc = function (e) { if (e.key === 'Escape' && _mk.state.buyuk) _mKapat(); }; document.addEventListener('keydown', _mk._mEsc); }
    var mesajlar = """ + str(MESAJ_ID) + """.map(function (id, i) { var src = '/_blob/' + id, n = 'Müşteri mesajı ' + (i + 1);
      return { src: src, n: n, ac: function () { _mk.setState({ buyuk: src, buyukAd: n }); document.documentElement.style.overflow = 'hidden'; } }; });
"""


def mesaj_js(js):
    """renderVals'a mesaj verisini ve büyük görünüm durumunu ekler (masa_bayrak'tan önce ya da sonra)."""
    i = js.index('renderVals()')
    j = js.index('\n    return ', i) + 1   # renderVals'ın kendi dönüşü: "return {" ya da "return Object.assign(R, {"
    k = js.index('{', j) + 1
    return (js[:j] + '    ' + MESAJ_VERI + js[j:k] + ' mesajlar: mesajlar, buyuk: this.state.buyuk || \'\', buyukAd: this.state.buyukAd || \'\', buyukVar: !!this.state.buyuk, buyukKapat: _mKapat, mGeri: _mKAY(-1), mIleri: _mKAY(1), galGeri: GALOK(-1), galIleri: GALOK(1),'
            + js[k:])
