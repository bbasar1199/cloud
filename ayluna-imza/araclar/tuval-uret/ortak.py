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

# "Dün X kişi satın aldı" dönen şeridi (23 Eki, kullanıcı: "dün 62 kişi satın aldı kısmı şu an sitemdeki gibi dönen ücretsiz kargo vesaire
# olan kısım gibi olsun"). Canlıdaki live-checkout mantığı: 24 px tek satır penceresi, satırlar alt alta, 3 sn'de bir yukarı kayar (0,5 sn),
# ilk satırda nabız noktası, vurgu kalın. Yalnız doğru bilgi: canlıdaki "31 kişi şu anda inceliyor" ve "3 günde 399 adet satıldı"
# (uydurma sayı) ile teyitsiz "son 10 günün en düşük fiyatı" alınmadı; emoji yerine çizgi ikon. Sona ilk satırın kopyası eklenir ki
# başa dönüş görünmeden olsun. Hareket azaltılmışsa yalnız ilk satır durur.
TK_IKON = {'kargo': '<path d="M3 7h11v8H3z"></path><path d="M14 10h4l3 3v2h-7"></path><circle cx="7" cy="17" r="1.8"></circle><circle cx="17" cy="17" r="1.8"></circle>',
           'iade': '<path d="M4.5 12a7.5 7.5 0 1 0 2.2-5.3"></path><path d="M4.5 4.5v3.8h3.8"></path>',
           'kart': '<rect x="3" y="6" width="18" height="12" rx="2"></rect><path d="M3 10h18M7 15h4"></path>'}


def tk_html(dun):
    import re
    sat = [('', 'Dün <b>%s kişi</b> satın aldı' % dun), ('kargo', '<b>Ücretsiz kargo</b> ile kapına'),
           ('iade', '<b>30 gün</b> iade hakkı'), ('kart', 'Kartla öde, <b>%5 indirim</b>')]
    def bir(i, ik, t):
        on = '<i class="dsr-nokta"></i>' if not ik else '<svg viewBox="0 0 24 24">' + TK_IKON[ik] + '</svg>'
        return '<span class="{{tkC%d}}">' % i + on + '<span>' + t + '</span></span>'
    sr = ' '.join(re.sub('<[^>]+>', '', t) + '.' for _, t in sat)
    return ('    <p class="dun dsr"><span class="dsr-sr">' + sr + '</span><span class="dsr-pen" aria-hidden="true">'
            '<span class="{{tkCls}}" style="transform: translateY({{tkY}}px)">' + ''.join(bir(i, *x) for i, x in enumerate(sat)) + bir(4, *sat[0]) + '</span></span></p>\n')


# Renk (23 Eki, kullanıcı: "önceki gibi yeşil olan ile olsun, yine gelirken animasyon ile gelsin, renkler çok sıkıcı durmasın"):
# eski Dün satırının yeşili; şerit sayfaya girerken aşağıdan yükselir (sayfanın .dun.dsr kuralı), her satır girerken simge ya da nokta
# küçükten büyür, vurgu yukarıdan düşer, nokta iki kez halka verir (sonsuz döngü yok; eleştirmen). Kenar maskesi kayarken harf
# çengellerinin pencere kenarında iz bırakmasını önler. gecik: ilk satırın sayfa girişiyle aynı anda oynaması için gecikme.
def tk_css(metin, vurgu, nokta, gecik='0s'):
    g = float(gecik.rstrip('s'))
    return (""".dsr{display:block;margin:8px 0 0;font-size:13px;font-weight:600;line-height:24px;color:%(m)s}
.dsr-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%%);white-space:nowrap}
.dsr-pen{position:relative;display:block;height:24px;overflow:hidden;-webkit-mask-image:linear-gradient(#0000,#000 2px,#000 22px,#0000);mask-image:linear-gradient(#0000,#000 2px,#000 22px,#0000)}
.dsr-iz{display:flex;flex-direction:column;transition:transform .5s cubic-bezier(.2,.7,.2,1)}
.dsr-iz.anlik{transition:none}
.dsr-s{display:flex;align-items:center;gap:8px;height:24px;white-space:nowrap;overflow:hidden}
.dsr-s>span{overflow:hidden;text-overflow:ellipsis}
.dsr-s b{display:inline-block;font-weight:700;color:%(v)s;font-variant-numeric:tabular-nums}
.dsr-s svg{width:16px;height:16px;flex:none;fill:none;stroke:%(v)s;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.dsr-nokta{position:relative;flex:none;width:8px;height:8px;margin:0 4px;border-radius:50%%;background:%(n)s}
.dsr-nokta::after{content:"";position:absolute;inset:0;border-radius:50%%;background:%(n)s;opacity:0}
.dsr-s.on svg,.dsr-s.on .dsr-nokta{animation:dsr-pop .45s cubic-bezier(.2,.7,.2,1) .1s both}
.dsr-s.on b{animation:dsr-dus .5s cubic-bezier(.2,.7,.2,1) .15s both}
.dsr-s.on .dsr-nokta::after{animation:dsr-nabiz 1.4s cubic-bezier(.2,.7,.2,1) .4s 2}
.dsr-s.on:first-child svg,.dsr-s.on:first-child .dsr-nokta{animation-delay:%(g0).2fs}
.dsr-s.on:first-child b{animation-delay:%(g1).2fs}
.dsr-s.on:first-child .dsr-nokta::after{animation-delay:%(g2).2fs}
@keyframes dsr-pop{from{opacity:0;transform:scale(.4)}to{opacity:1;transform:none}}
@keyframes dsr-dus{from{opacity:0;transform:translateY(-9px)}to{opacity:1;transform:none}}
@keyframes dsr-nabiz{0%%{opacity:.6;transform:scale(1)}100%%{opacity:0;transform:scale(2.8)}}
@media (prefers-reduced-motion:reduce){.dsr-iz{transition:none}.dsr-s svg,.dsr-s b,.dsr-nokta,.dsr-nokta::after{animation:none!important}}
""" % {'m': metin, 'v': vurgu, 'n': nokta, 'g0': g + .1, 'g1': g + .2, 'g2': g + .5})


# Zamanlayıcıya (her saniye) eklenir: tik = saniye sayacı adı, S = durum, o = yeni durum. 4 satır + kopya; her satır 3 sn.
def tk_adim(tik, ilk=0):
    # ilk: şerit sayfaya geç girdiği için (fiyat animasyonundan sonra) ilk satırın ek bekleme süresi, sn
    return ("      if (!azH) { var tkd = %(t)s - (S.tkT === undefined ? %(i)d : S.tkT);\n"
            "        if (S.tk === 4 && tkd >= 1) { o.tk = 0; o.tkT = %(t)s - 1; o.tkAn = true; }\n"
            "        else if (tkd >= 3) { o.tk = (S.tk || 0) + 1; o.tkT = %(t)s; o.tkAn = false; } }\n") % {'t': tik, 'i': ilk}


# Görünen satıra "on" (giriş hareketi); kopyadan başa görünmez dönüşte (tkAn) ilk satır yeniden oynamaz
TK_DEGER = ("tkY: -24 * (S.tk || 0), tkCls: 'dsr-iz' + (S.tkAn ? ' anlik' : ''), "
            + ', '.join("tkC%d: 'dsr-s' + ((S.tk || 0) === %d && !(%d === 0 && S.tkAn) ? ' on' : '')" % (i, i, i) for i in range(5)) + ',')


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
    """ + KAY_JS.replace('function KAY(', 'function _mKAY(') + GALOK_JS + """    // Büyük görünüm (27 Eki denetim): açılınca odak Kapat'a geçer, Tab pencerede kalır, kapanınca odak açan mesaja döner
    function _mX() { var x = document.querySelector('.mbuyuk .mb-x'); if (x) x.focus(); }
    function _mKapat() { _mk.setState({ buyuk: null }); document.documentElement.style.overflow = ''; var o = _mk._mAcan; _mk._mAcan = null; if (o && o.focus) setTimeout(function () { o.focus(); }, 0); }
    if (!_mk._mEsc) { _mk._mEsc = function (e) { if (!_mk.state.buyuk) return; if (e.key === 'Escape') _mKapat(); else if (e.key === 'Tab') { e.preventDefault(); _mX(); } }; document.addEventListener('keydown', _mk._mEsc); }
    var mesajlar = """ + str(MESAJ_ID) + """.map(function (id, i) { var src = '/_blob/' + id, n = 'Müşteri mesajı ' + (i + 1);
      return { src: src, n: n, ac: function () { _mk._mAcan = document.activeElement; _mk.setState({ buyuk: src, buyukAd: n }); document.documentElement.style.overflow = 'hidden'; setTimeout(_mX, 30); } }; });
"""


def mesaj_js(js):
    """renderVals'a mesaj verisini ve büyük görünüm durumunu ekler (masa_bayrak'tan önce ya da sonra)."""
    i = js.index('renderVals()')
    j = js.index('\n    return ', i) + 1   # renderVals'ın kendi dönüşü: "return {" ya da "return Object.assign(R, {"
    k = js.index('{', j) + 1
    return (js[:j] + '    ' + MESAJ_VERI + js[j:k] + ' mesajlar: mesajlar, buyuk: this.state.buyuk || \'\', buyukAd: this.state.buyukAd || \'\', buyukVar: !!this.state.buyuk, buyukKapat: _mKapat, mGeri: _mKAY(-1), mIleri: _mKAY(1), galGeri: GALOK(-1), galIleri: GALOK(1),'
            + js[k:])

# Üst blok: sayaç şeridi + başlık, bütün sayfalarda aynı (kullanıcı, 25 Eki: "A iyi ama üstünde yine sayım olsun ve beyazdan bizim ana
# rengimiz maviye değişsin, sürekli renk değişimi yapsın, yumuşak"). Beyaz (lacivert yazı) ↔ lacivert (beyaz yazı), 16 sn'lik döngü:
# 5,5 sn beyaz, 2,5 sn geçiş, 5,5 sn lacivert, 2,5 sn geçiş. Yalnız opacity: içeriğin aria-hidden lacivert kopyası (.gk) üstte belirip
# kaybolur; düğmeler alttaki beyaz katmanda kalır (kopya dokunmayı geçirir). Bütün katmanlar aynı saate bağlı (--rd-t, ayluna.js).
UST_MENU = '<svg class="ico" viewBox="0 0 24 24"><path d="M4 8h16M4 16h11"></path></svg>'
UST_SEPET = '<svg class="ico" viewBox="0 0 24 24"><path d="M6 8h12l-1 12H7z"></path><path d="M9 8a3 3 0 0 1 6 0"></path></svg>'


import re


def gece_kopya(ic):
    k = re.sub(r'<(button|a)\b', '<span', ic)
    k = re.sub(r'</(button|a)>', '</span>', k)
    k = re.sub(r'\s(aria-label|role|onClick|href|type|tabindex)="[^"]*"', '', k)
    k = k.replace('class="ikon sepet"', 'class="ikon sepet gk-sepet"')
    return '<span class="gk" aria-hidden="true">' + k + '</span>'


def ust_blok(zaman, isaret_svg, ay='{{cdAy}}', aria='{{cdAria}}'):
    s_ic = ('<span>Bugünkü fiyat garantisi</span><svg class="sayac-ay" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle>'
            '<path d="%s"></path></svg><b>%s</b>' % (ay, zaman))
    b_ic = ('<a class="marka" href="#" aria-label="Ayluna ana sayfa">' + isaret_svg + '<b>Ayluna</b></a>'
            '<span class="ua-sag"><button class="ikon" type="button" aria-label="Menü">' + UST_MENU + '</button>'
            '<button class="ikon sepet" type="button" aria-label="Sepet">' + UST_SEPET + '</button></span>')
    return ('  <div class="duyuru ua-s rd" role="timer" aria-label="%s">' % aria + s_ic + gece_kopya(s_ic) + '</div>\n'
            '  <header class="ust ua-b rd">' + b_ic + gece_kopya(b_ic) + '</header>\n')


UST_CSS = """
/* Üst blok (25 Eki): beyaz ↔ lacivert yumuşak döngü; yalnız opacity */
.rd{position:relative;isolation:isolate}
.rd>.gk{position:absolute;inset:0;z-index:2;display:flex;align-items:center;justify-content:inherit;gap:inherit;padding:inherit;pointer-events:none;opacity:0;animation:rd-gece 16s cubic-bezier(.45,0,.55,1) var(--rd-t,0s) infinite}
@keyframes rd-gece{0%,34%{opacity:0}50%,84%{opacity:1}100%{opacity:0}}
@media (prefers-reduced-motion:reduce){.rd>.gk{animation:none}}
.duyuru.ua-s{display:flex;justify-content:center;align-items:center;gap:8px;height:30px;margin:0;padding:0 12px;border:0;background:#F3F4F7;color:#1A2142;font-size:13px;font-weight:600}
.duyuru.ua-s b{font-variant-numeric:tabular-nums;font-weight:700;letter-spacing:.02em;color:#1A2142}
.duyuru.ua-s .sayac-ay{width:14px;height:14px;flex:none}
.duyuru.ua-s .sayac-ay circle{fill:none;stroke:#9AA0AE;stroke-width:1.6}
.duyuru.ua-s .sayac-ay path{fill:#F2A65A}
.duyuru.ua-s>.gk{background:#0C1027;color:#B9BED6}
.duyuru.ua-s>.gk b{color:#F2A65A}
.duyuru.ua-s>.gk .sayac-ay circle{stroke:rgba(185,190,214,.6)}
header.ua-b{display:flex;justify-content:space-between;align-items:center;height:52px;margin:0;padding:0 4px 0 14px;background:#FFFFFF;color:#1A2142;box-shadow:inset 0 -1px 0 #E4E6EB}
.ua-b .marka{display:flex;align-items:center;gap:7px;min-height:48px;color:inherit;text-decoration:none}
.ua-b .marka b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:19px;letter-spacing:-.01em}
.ua-b .isaret circle{stroke:#C9CED8}
.ua-b .ua-sag{display:flex}
.ua-b .ikon{position:relative;width:48px;height:48px;display:grid;place-items:center;padding:0;border:0;background:transparent;color:inherit;cursor:pointer}
.ua-b .ico{width:24px;height:24px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
header.ua-b>.gk{background:#1A2142;color:#FFFFFF}
.ua-b>.gk .isaret circle{stroke:rgba(255,253,249,.55)}
.ua-b>.gk [data-ay-adet]::after{background:#F2A65A;color:#1A2142}
.ua-b .ikon:focus-visible,.ua-b .marka:focus-visible{outline:2px solid #F2A65A;outline-offset:-2px;border-radius:12px}
"""
