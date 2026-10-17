# LunaDream ürün sayfası · C "Gece hikâyesi" denemesi. Çalıştır: python3 luna_c.py
# B+'nın kullanıcı onaylı parçaları (sahne, levha, Sihirli, model, paket, lamba seçimi, butonlar, SSS, diğer ürünler,
# alt bilgi, yapışkan çubuk) B+ üreticisinden birebir alınır; C yalnız şunları değiştirir:
#   1. "Kapına gelecek" satırı: seçime göre kapıya kaç kutu ve kutuda ne geleceğini gösterir (paket ile butonlar arası).
#   2. Videolar, yorumlar, Bir gece, diskler, kutu ve 30 gün bölümleri tek bir "Gece hikâyesi"nde toplanır:
#      Instagram hikâyesi gibi kareler, ilerleme çizgisi yerine ay evreleri (Ay-luna). Sayfa kısalır.
import ast, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL, TL_JS
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamC.dc.html')

# B+ üreticisini çalıştırmadan değişkenlerini oku
_ag = ast.parse(open(os.path.join(HERE, 'luna_bplus.py'), encoding='utf-8').read())
_ns = {'TL_JS': TL_JS}
for _n in _ag.body:
    if isinstance(_n, ast.Assign) and len(_n.targets) == 1 and getattr(_n.targets[0], 'id', '') in ('CSS', 'STAR', 'LOGO', 'HTML', 'JS'):
        _ns[_n.targets[0].id] = eval(compile(ast.Expression(_n.value), 'luna_bplus.py', 'eval'), dict(_ns))
CSS, STAR, HTML, JS = _ns['CSS'], _ns['STAR'], _ns['HTML'], _ns['JS']


def degis(s, eski, yeni):
    assert s.count(eski) == 1, ('bulunamadı ya da birden çok', eski[:60])
    return s.replace(eski, yeni)


CSS += r"""
/* C · Kapına gelecek: kapıya gelen kutular (çizgi kutu + gerçek ürün fotoğrafı), yanında her kutunun içeriği tek cümle.
   Çerçeve yok (seçilebilir öğe değil). İkinci kutu eklenince 8px aşağıdan ve saydamdan gelir. */
.kutun{display:grid;grid-template-columns:auto minmax(0,1fr);gap:14px;align-items:center;margin-top:18px;padding-top:14px;border-top:1px solid #E3D8C7}
.kutular{display:flex;gap:4px}
.kutu{display:flex;flex-direction:column;align-items:center;gap:2px;width:68px;animation:kutu-gir .45s cubic-bezier(.2,.7,.2,1) both}
@keyframes kutu-gir{from{opacity:0;transform:translateY(8px)}}
.kutu-ill{position:relative;display:block;width:68px;height:62px}
.kutu-ill img{position:absolute;left:50%;top:0;height:44px;width:auto;max-width:44px;transform:translateX(-50%)}
.kutu-ill svg{position:absolute;inset:0;width:68px;height:62px;fill:none;stroke:#1A2142;stroke-width:1.5;stroke-linejoin:round;stroke-linecap:round}
.kutu-ill svg .on-yuz{fill:#F6F1E9}
.kutu b{font-size:12px;font-weight:600;color:#5C6078}
.kutun-yazi{display:flex;flex-direction:column;gap:2px;line-height:1.35}
.kutun-yazi b{font-size:15px}
.kutun-yazi span{font-size:14px;color:#5C6078;text-wrap:pretty}
/* C · Gece hikâyesi (imza an). Kareler kendiliğinden ilerlemez; sağa dokun ileri, sola dokun geri, aya dokun o kareye git.
   Ay evreleri: her kare bir evre, son kare dolunay. Görülen kareler dolu, görülmeyenler yalnız çizgi; etkin ayın altında nokta.
   Geçiş (design-review bulgusu sonrası): önce çıkan kare 160 ms'de söner, sonra giren kare gelir; iki yazı üst üste binmez.
   Gizli kare visibility:hidden olur, içindeki düğmeler Tab ile odak almaz. */
.hk-no{font-size:13px;font-weight:600;color:#5C6078;font-variant-numeric:tabular-nums;padding-bottom:3px}
.aylar{display:flex;justify-content:space-between;margin-top:6px}
.ay{position:relative;flex:1;height:48px;display:grid;place-items:center;padding:0;border:0;background:transparent;cursor:pointer;touch-action:manipulation;-webkit-tap-highlight-color:transparent}
.ay.on::after{content:"";position:absolute;left:50%;bottom:3px;width:5px;height:5px;margin-left:-2.5px;border-radius:50%;background:#1A2142}
.ay svg{width:26px;height:26px;opacity:.8;transform:scale(.84);transition:opacity .35s cubic-bezier(.2,.7,.2,1),transform .35s cubic-bezier(.2,.7,.2,1)}
.ay svg circle{fill:#1A2142;stroke:#1A2142;stroke-width:1.2}
.ay svg path{fill:#F2A65A}
.ay.on svg{opacity:1;transform:none}
.ay.sonra svg circle{fill:transparent;stroke-width:1.4}
.ay.sonra svg path{opacity:0}
.ay:focus-visible,.hk .ust3:focus-visible,.hk .dbtn:focus-visible{outline:2px solid #1A2142;outline-offset:2px;border-radius:12px}
.hk-kart:not(.acik) .ust3:focus-visible,.hk-kart:not(.acik) .dbtn:focus-visible{outline-color:#FFFDF9}
/* İleri/geri alanı etkin karenin altında kalır; odaklanınca bütün hikâye çerçevelenir */
.hk:has(.hk-geri:focus-visible),.hk:has(.hk-ileri:focus-visible){outline:3px solid #1A2142;outline-offset:3px}
.sr{position:absolute;width:1px;height:1px;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.hk{position:relative;height:480px;margin-top:4px;border-radius:24px;overflow:hidden;background:#0C1027;isolation:isolate;color:#FFFDF9}
.hk-kart{position:absolute;inset:0;opacity:0;visibility:hidden;pointer-events:none;transition:opacity .16s cubic-bezier(.2,.7,.2,1),visibility 0s linear .16s}
/* Etkin kare dokunma alanlarının üstünde ama yalnız düğmeleri dokunma alır; gerisi alttaki ileri/geri alanına geçer */
.hk-kart.on{z-index:3;opacity:1;visibility:visible;transition:opacity .32s cubic-bezier(.2,.7,.2,1) .12s,visibility 0s}
.hk-kart.on .ust3{pointer-events:auto}
.hk-kart.acik{background:#FFFDF9;color:#1A2142;box-shadow:inset 0 0 0 1px #E3D8C7;border-radius:24px}
.hk-foto{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hk-kart.karart::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(12,16,39,.9) 0,rgba(12,16,39,.55) 26%,rgba(12,16,39,0) 50%)}
.hk-alt{position:absolute;left:18px;right:18px;bottom:20px;z-index:1}
.hk-ust{position:absolute;left:18px;right:18px;top:18px;z-index:1}
.hk-baslik{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:22px;line-height:1.15;letter-spacing:-.01em;margin:0;text-wrap:balance}
.hk-alt p,.hk-ust p{margin:6px 0 0;font-size:14px;line-height:1.4;color:#D9DCEB;text-wrap:pretty}
.acik .hk-ust p,.acik .hk-alt p{color:#5C6078}
.hk-geri,.hk-ileri{position:absolute;top:0;bottom:0;z-index:2;padding:0;border:0;background:transparent;cursor:pointer;outline:0;touch-action:manipulation;-webkit-tap-highlight-color:transparent}
.hk .ust3,.hk .dbtn{touch-action:manipulation}
.hk-geri{left:0;width:30%}
.hk-ileri{right:0;width:70%}
.ust3{position:relative;z-index:3}
.tavan2{position:absolute;left:50%;top:94px;width:216px;height:216px;margin-left:-108px;border-radius:50%;background:radial-gradient(closest-side,#232B55,#0C1027)}
.yans2{position:absolute;inset:0;border-radius:50%;overflow:hidden;opacity:0;transform:scale(.94);transition:opacity .6s cubic-bezier(.2,.7,.2,1),transform .6s cubic-bezier(.2,.7,.2,1)}
.yans2.on{opacity:.92;transform:none}
.yans2 img{width:100%;height:100%;object-fit:cover;display:block}
.tavan-not{position:absolute;left:50%;top:318px;transform:translateX(-50%);font-size:12px;font-weight:600;color:#B9BED6;white-space:nowrap}
.hk-diskler{position:absolute;left:0;right:0;bottom:52px;display:flex;gap:4px;overflow-x:auto;padding:0 14px;scroll-snap-type:x mandatory;scroll-padding:0 14px}
.hk-diskler .dbtn{scroll-snap-align:start}
.yorum3{list-style:none;margin:16px 0 0;padding:0;display:flex;flex-direction:column;gap:14px}
.yorum3 li{display:flex;flex-direction:column;gap:4px}
.yorum3 q{font-family:"Young Serif",Georgia,serif;font-size:16px;line-height:1.3;quotes:none}
.yorum3 span{font-size:13px;color:#5C6078}
.kolaj{position:absolute;left:12px;right:12px;top:12px;height:330px;display:grid;grid-template-columns:3fr 2fr;grid-template-rows:1fr 1fr;gap:6px}
.kolaj img{width:100%;height:100%;object-fit:cover;border-radius:12px;display:block}
.kolaj img:first-child{grid-row:1 / 3}
.rahat{list-style:none;margin:18px 0 0;padding:0;display:flex;flex-direction:column}
.rahat li{display:grid;grid-template-columns:58px minmax(0,1fr);gap:12px;align-items:center;padding:10px 0;border-top:1px solid #E3D8C7}
.rahat .say{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:40px;line-height:.9;letter-spacing:-.03em;color:#A05A1C;text-align:center;font-variant-numeric:tabular-nums}
.rahat .ico{width:26px;height:26px;margin:0 auto;color:#A05A1C}
.rahat b{display:block;font-size:15px}
.rahat span{font-size:14px;color:#5C6078}
.hk-ipucu{margin:8px 0 0;text-align:center;font-size:13px;color:#5C6078}"""

KUTU_SVG = ('<svg viewBox="0 0 68 62"><path d="M10 34 2 26l7-5"></path><path d="M58 34l8-8-7-5"></path>'
            '<rect class="on-yuz" x="10" y="34" width="48" height="26" rx="3"></rect><path d="M24 44h20"></path></svg>')

KUTUN = """    <!-- C · Kapına gelecek: seçime göre kaç kutu ve kutuda ne var. Brif şikâyeti "12 disk yazıyor, 6 geliyor" ve iade verisi
         yüzünden sayfa vaadi kutuyla birebir. Her lamba kendi kutusunda gelir (kullanıcı: her kutuda hepsi çıkar). -->
    <div class="kutun" aria-live="polite">
      <div class="kutular"><sc-for list="{{kutular}}" as="k" hint-placeholder-count="2"><span class="kutu"><span class="kutu-ill" aria-hidden="true"><img src="{{k.src}}" alt="">""" + KUTU_SVG + """</span><b>{{k.ad}}</b></span></sc-for></div>
      <span class="kutun-yazi"><b>Kapına {{kutuSay}} gelir</b><span>{{kutuMetin}}</span></span>
    </div>
"""

KARGO = '<svg class="ico" viewBox="0 0 24 24"><path d="M3 7h11v9H3zM14 10h4l3 3v3h-7z"></path><circle cx="7" cy="17.5" r="1.8"></circle><circle cx="17.5" cy="17.5" r="1.8"></circle></svg>'
KAPI = '<svg class="ico" viewBox="0 0 24 24"><rect x="3" y="6" width="18" height="13" rx="2"></rect><path d="M3 10h18M7 15h4"></path></svg>'

HIKAYE = """  <!-- C · Gece hikâyesi (imza an). Kaynak fikir: Instagram hikâye kalıbı (Meta'dan gelen müşteriye tanıdık; onizleme/fikirler.html Fikir 3).
       İlerleme çizgileri yerine ay evreleri: her kare bir evre, son kare dolunay. Kendiliğinden ilerlemez (yeni sonsuz döngü yok).
       Videolar, yorumlar, Bir gece, diskler ve 30 gün iade bu karelerde. Canlıda 1. kare Shopify videosu olur: ekrandayken sessiz döner,
       sağ üstte ayrı "Sesi aç" düğmesi (ust3) bulunur; kareye dokunmak yine ilerletir (design-review bulgusu). -->
  <section class="bolum gir" id="hikaye">
    <div class="px" style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px"><h2 class="h2">Işık kapanınca<span class="n">.</span></h2><span class="hk-no" aria-hidden="true">{{hNo}}/{{hCount}}</span><span class="sr" aria-live="polite">{{hDuyuru}}</span></div>
    <div class="px"><div class="aylar" role="group" aria-label="Hikâye kareleri"><sc-for list="{{aylar}}" as="a" hint-placeholder-count="6"><button class="{{a.cls}}" type="button" aria-current="{{a.cur}}" aria-label="{{a.label}}" onClick="{{a.pick}}"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="{{a.d}}"></path></svg></button></sc-for></div></div>
    <div class="px"><div class="hk" role="region" aria-roledescription="hikâye" aria-label="LunaDream ile bir gece">
      <button class="hk-geri" type="button" aria-label="Önceki kare" onClick="{{hPrev}}"></button>
      <button class="hk-ileri" type="button" aria-label="Sonraki kare" onClick="{{hNext}}"></button>

      <article class="{{hc1}}" aria-hidden="{{ah1}}"><img class="hk-foto" src="{{img1}}" alt="{{alt1}}" style="object-position: 50% 45%">
        <div class="hk-alt"><h3 class="hk-baslik">Oda masala döner.</h3><p>Diski tak, ışığı kapat; desen tavana yansır.</p></div></article>

      <article class="{{hc2}}" aria-hidden="{{ah2}}">
        <div class="hk-ust"><h3 class="hk-baslik">Bu geceki masal</h3><p>{{discName}}. Her kutuda 6 + 6 hediye disk.</p></div>
        <div class="tavan2"><sc-for list="{{proj}}" as="p" hint-placeholder-count="2"><span class="{{p.cls2}}" aria-hidden="true"><img src="{{p.src}}" alt=""></span></sc-for></div>
        <span class="tavan-not">[gerçek tavan fotoğrafı]</span>
        <div class="hk-diskler noscroll ust3"><sc-for list="{{discs}}" as="d" hint-placeholder-count="11"><button class="{{d.cls}}" onClick="{{d.pick}}" aria-pressed="{{d.on}}" aria-label="{{d.n}} diskini göster"><img src="{{d.src}}" alt=""></button></sc-for></div>
        <div class="hk-alt" style="bottom: 18px"><p style="margin: 0; text-align: center">Diske dokun, tavanda gör.</p></div></article>

      <article class="{{hc3}}" aria-hidden="{{ah3}}"><img class="hk-foto" src="{{img3}}" alt="{{alt3}}" style="object-position: {{pos3}}">
        <div class="hk-alt"><h3 class="hk-baslik">Ninni lambadan çalar.</h3><p>Telefonunu Bluetooth ile bağla. Işığı 3 parlaklıktan birine ayarla.</p></div></article>

      <!-- Yorumlar Loox'tan birebir; puan ve sayı Loox'tan (teyit bekliyor), veri yoksa kare gizlenir -->
      <article class="{{hc4}}" aria-hidden="{{ah4}}" id="yorumlar">
        <div class="hk-ust"><div style="display: flex; align-items: baseline; gap: 8px"><b class="ser" style="font-size: 32px; line-height: 1; font-weight: 400">{{rating}}</b>""" + STAR + """<span style="font-size: 13px; color: #5C6078">{{reviews}} yorum</span></div>
          <ul class="yorum3"><sc-for list="{{revs3}}" as="r" hint-placeholder-count="3"><li><q>{{r.q}}</q><span>{{r.name}} · satın aldı</span></li></sc-for></ul></div>
        <!-- Canlıda Loox'un tüm yorumlar sayfasına gider (olumsuzlar dahil; mevzuat kuralı 3) -->
        <div class="hk-alt"><a href="#" class="cip ust3" style="display: flex; justify-content: center">{{reviews}} yorumun hepsini oku</a><p style="text-align: center; font-size: 13px">Yorumlar yalnız sipariş verenlerden; hepsi yayımlanır.</p></div></article>

      <!-- Müşteri fotoğrafları: Loox foto yorumlarından (kullanıcı izni, 17 Eki). Yorum metniyle eşleştirilmez. -->
      <article class="{{hc5}}" aria-hidden="{{ah5}}">
        <div class="kolaj"><sc-for list="{{mfoto3}}" as="f" hint-placeholder-count="3"><img src="{{f.src}}" alt="{{f.alt}}" style="object-position: {{f.pos}}"></sc-for></div>
        <div class="hk-alt"><h3 class="hk-baslik">Müşterilerimizin evinden.</h3><p>Fotoğraflar sipariş verenlerin yorumlarından.</p></div></article>

      <article class="{{hc6}}" aria-hidden="{{ah6}}">
        <div class="hk-ust"><h3 class="hk-baslik">Gönlün rahat olsun.</h3>
          <ul class="rahat">
            <li><b class="say">30</b><span><b>gün içinde iade</b>Yasal 14 günü 30 güne uzattık. İade kodunu biz göndeririz, kargosu ücretsiz.</span></li>
            <li>""" + KARGO + """<span><b>Ücretsiz kargo</b>1 iş gününde kargoda, {{teslim}} arası kapında.</span></li>
            <li>""" + KAPI + """<span><b>Kapıda ödeme de var</b>Kapıda ödeme ücreti ₺80.</span></li>
          </ul></div>
        <div class="hk-alt"><button class="btn-on ust3" type="button" style="margin-top: 0">{{onLabel}}</button><p style="text-align: center; font-size: 13px">{{onNote}}</p></div></article>
    </div></div>
    <p class="hk-ipucu">{{hIpucu}}</p>
  </section>

"""

HTML = degis(HTML, '<a href="#yorumlar" style="', '<a href="#hikaye" onClick="{{toReviews}}" style="')
HTML = degis(HTML, '    <!-- Stok satırı:', KUTUN + '    <!-- Stok satırı:')
_a, _b = HTML.index('  <!-- Videolar:'), HTML.index('  <!-- SSS -->')
HTML = HTML[:_a] + HIKAYE + HTML[_b:]

# Galeri: oda sahneleri yerel dosyalardan yeniden yüklendi (canvas/c-gorsel/; yerel önizleme = tuval). Erkek modelin gece odası da eklendi.
JS = degis(JS, """      { id: '34462d69c62584aeefaca4cff769f3b5', n: 'Gece çocuk odası, LunaDream tavana ay ve yıldız yansıtıyor', pos: '50% 55%', oda: true },
      { id: '05d7f0466966800b2be9e851b9ada476', n: 'Gündüz çocuk odası, komodinde LunaDream', pos: '62% 66%', oda: true },
      { id: 'd0c41725fb735b5851374f373ff814f3', n: 'Gece yanan LunaDream', pos: '50% 50%', oda: true },""",
"""      { id: 'fd0bca1b99cf3837b69fb025cc4e2cd9', n: 'Gece çocuk odası, LunaDream Kız duvara ay ve yıldız yansıtıyor', pos: '50% 60%', oda: true },
      { id: '31751eb35473aca04420825deb3c3ce0', n: 'Gece çocuk odası, LunaDream Erkek (Uzay Kaşifi)', pos: '50% 62%', oda: true },
      { id: '2288b7fbcc230bd9d47e25ef6550ce78', n: 'Gündüz çocuk odası, komodinde LunaDream Kız', pos: '50% 72%', oda: true },""")
JS = degis(JS, "topic: 'Tümü', disc: 1, now: Date.now() }", "topic: 'Tümü', disc: 1, h: 0, now: Date.now() }")
JS = degis(JS, "    return {\n      gal: gal,", """    // C · Kapına gelecek: 1 Adet = seçili model; 2 Adet = iki lambanın seçimi
    // Kutudaki lamba: stüdyo fotoğrafından yalnız arka planı temizlenmiş kesim (ürün pikselleri aynı; canvas/c-gorsel/lamba-*.png)
    var kutular = (S.adet === 2 ? [l1, l2] : [S.model]).map(function (m) { return { src: B + (m === 'kiz' ? 'b823966c39ff35824b4d6e74757646ec' : '20f90021119e4c3bdbc930b283e3635a'), ad: m === 'kiz' ? 'Kız' : 'Erkek' }; });
    // C · Gece hikâyesi: kareler ve ay evreleri (f = dolu kısım; son kare dolunay)
    var HK = ['Oda masala döner', 'Bu geceki masal', 'Ninni lambadan çalar', 'Aileler ne diyor', 'Müşterilerimizin evinden', 'Gönlün rahat olsun'];
    function ayD(f) { var rx = Math.abs(1 - 2 * f) * 9; return 'M12 3A9 9 0 0 1 12 21A' + rx.toFixed(2) + ' 9 0 0 ' + (f < 0.5 ? 0 : 1) + ' 12 3Z'; }
    var aylar = HK.map(function (t, i) { var on = i === S.h; return { d: ayD((i + 1) / HK.length), cur: on ? 'step' : 'false', cls: on ? 'ay on' : (i > S.h ? 'ay sonra' : 'ay'), label: (i + 1) + '. kare: ' + t, pick: function () { self.setState({ h: i }); } }; });
    var hk = {}; HK.forEach(function (t, i) { var on = i === S.h, acik = i === 3 || i === 5; hk['hc' + (i + 1)] = 'hk-kart' + (acik ? ' acik' : ' karart') + (on ? ' on' : ''); hk['ah' + (i + 1)] = on ? 'false' : 'true'; });
    var revs3 = [REV[0], REV[1], REV[2]].map(function (r) { return { q: r.q, name: r.name }; });
    var mfoto3 = [{ id: '4323cd781a0d687b528b3059505be48c', pos: '50% 35%', alt: 'Müşteri fotoğrafı: LunaDream’e sarılan küçük kız' }, { id: 'ec3c3976bbe8f18e5660f4a4c355ebf7', pos: '50% 50%', alt: 'Müşteri fotoğrafı: karanlık odada yanan LunaDream' }, { id: 'f060b12bc3353fae64eedf62798c5711', pos: '50% 60%', alt: 'Müşteri fotoğrafı: duvara yansıyan deniz deseni' }].map(function (f) { return { src: B + f.id, alt: f.alt, pos: f.pos }; });
    var proj2 = DISCS.map(function (d, i) { return { src: B + d.id, cls2: i === S.disc ? 'yans2 on' : 'yans2' }; });
    return {
      kutular: kutular, kutuSay: S.adet === 2 ? '2 kutu' : '1 kutu',
      kutuMetin: (S.adet === 2 ? 'Her kutuda' : 'Kutuda') + ' lamba, 6 + 6 hediye disk ve USB şarj kablosu.',
      hDuyuru: (S.h + 1) + '. kare, ' + HK.length + ' kareden: ' + HK[S.h], hIpucu: S.h === HK.length - 1 ? 'Dokun, başa dön.' : 'Sağa dokun, sonraki kare.',
      aylar: aylar, hNo: S.h + 1, hCount: HK.length, revs3: revs3, mfoto3: mfoto3,
      hc1: hk.hc1, hc2: hk.hc2, hc3: hk.hc3, hc4: hk.hc4, hc5: hk.hc5, hc6: hk.hc6, ah1: hk.ah1, ah2: hk.ah2, ah3: hk.ah3, ah4: hk.ah4, ah5: hk.ah5, ah6: hk.ah6,
      hPrev: function () { self.setState({ h: (S.h + HK.length - 1) % HK.length }); }, hNext: function () { self.setState({ h: (S.h + 1) % HK.length }); },
      toReviews: function () { self.setState({ h: 3 }); }, pos3: kiz ? '50% 30%' : '50% 45%',
      img1: kiz ? B + '3d214a1ba100aaf3d85bb18a27325237' : B + '49da18af3a87a3c97bb59cb9dbe8817f', alt1: kiz ? 'Gece yatak başında yanan LunaDream Kız, duvarda yıldızlar' : 'Gece yatak başında yanan LunaDream Erkek, duvarda yıldızlar',
      img3: kiz ? B + '8b1f621be2cb3b6133b7b78bc14e1963' : B + 'b2c8d9b92ad3541b532e3aa108a74735', alt3: kiz ? 'Elde tutulan, yanan LunaDream Kız' : 'Masal diskleriyle LunaDream Erkek',
      gal: gal,""")
JS = degis(JS, "discs: discs, proj: proj,", "discs: discs, proj: proj2,")

open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · C Gece hikâyesi', css=CSS) + HTML + TAIL.format(h=int(os.environ.get("C_H", 3999)), js=JS))
print('yazıldı:', os.path.abspath(OUT))
