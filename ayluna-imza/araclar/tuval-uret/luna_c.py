# LunaDream ürün sayfası · C2 "Ay yaprakları" denemesi. Çalıştır: python3 luna_c.py
# Kullanıcı (Tur 16'dan sonra): "Çok kısaltmışız; hâlâ soğukluk, düzensizlik var; alt kısım section olarak görünmeli;
# değişiklik bölümler, iskelet, sayfanın görünüşü üzerine olmalıydı." Bu yüzden C2 içerik kesmez, iskeleti değiştirir:
#   1. B+'nın bütün bölümleri yerinde ve ayrı (Videolar, Yorumlar, Bir gece, Diskler, Kutu, 30 gün, SSS, Diğer, Alt bilgi).
#   2. Her bölüm bir "yaprak": fotoğrafın üstüne binen levha gibi, bir öncekinin üstüne 28px biner (aynı motif tüm sayfada).
#      Yaprak tonları sıcak ve sırayla değişir (kum, ak, gece); bölüm sınırı boşlukla değil yüzey değişimiyle okunur.
#      Grup içi aralık sıkı (8–16), bölüm arası belirgin (28 + kenar + 42). "Yakın mı uzak mı" belirsizliği kalkar.
#   3. Her yaprağın tepesinde küçük bir ay (tutamak). Aşağı indikçe dolar; alt bilgide dolunay (sayfa akşamdan geceye akar).
#   4. Gece yapraklarında tepede hafif amber ışık (lambanın ışığı). Açık yapraklarda iç kartlar çizgisiz, krem dolgulu.
#   5. Tur 16'dan kalan: "Kapına ne gelir" bölümü seçime göre kaç kutu geleceğini gösterir (levha B+ ile aynı kaldı).
# Levha ve üstü (sahne, Sihirli, model, paket, butonlar) B+ üreticisinden birebir alınır.
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


def degis(s, eski, yeni, kac=1):
    assert s.count(eski) == kac, ('beklenen sayıda değil', s.count(eski), eski[:70])
    return s.replace(eski, yeni)


def tutamak(i, n=9):
    # Ay evresi: f = dolu kısım (1/9 ince hilal … 9/9 dolunay)
    f = i / n
    d = 'M12 3A9 9 0 0 1 12 21A%.2f 9 0 0 %d 12 3Z' % (abs(1 - 2 * f) * 9, 0 if f < .5 else 1)
    return '\n    <span class="tutamak" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="%s"></path></svg></span>' % d


CSS += r"""
/* C2 · Ay yaprakları: her bölüm bir öncekinin üstüne 28px biner (levha motifi). Ton sırası: kum, ak, gece, gece2, kum, ak, kum, ak, gece. */
.levha{padding-bottom:60px}
/* Teslim çizelgesi kapıda notuna yakın dursun, yaprak kenarıyla arası belirgin (yakınlık net) */
.levha .yol{margin-top:16px}
/* Ayluna kuralı: dokunma alanı en az 48px (B+'da lamba seçici 42px) */
.seg-b{min-height:48px}
/* Yapışkan çubuk yaprakların üstünde kalsın (DOM sırasına bağlı kalmasın) */
.yapis{z-index:6}
/* Yatay kaydırıcılarda odak halkasının alt kenarı kırpılmasın */
.yaprak .noscroll{padding-bottom:6px!important}
/* Ak yapraktaki krem kartta konu çipi kaybolmasın */
.y-ak .yk2 .konu{background:#E9DCC7}
/* Giriş hareketi yaprağın kendisinde değil içeriğinde: yaprak hep opak kalır, altından zemin ya da önceki yaprağın düz kenarı görünmez */
@supports (animation-timeline: view()){
  .yaprak.gir{animation:none}
  .yaprak.gir > :not(.tutamak){animation:gir linear both;animation-timeline:view();animation-range:entry 0% entry 35%}
}
/* Levha z-index 4 (sahnenin üstüne biner); yapraklar onun da üstüne binmeli. Eşit z-index, DOM sırası: sonraki yaprak üstte. */
.yaprak{position:relative;z-index:5;isolation:isolate;margin-top:-28px;border-radius:28px 28px 0 0;padding-top:42px;padding-bottom:56px}
.y-ak{background:#FFFDF9}
.y-gece{background:#1A2142;color:#EDE5D8}
.y-gece2{background:#121735;color:#EDE5D8}
/* Gece yapraklarında tepede lambanın ışığı gibi hafif amber; yalnız arka planda */
.y-gece::before,.y-gece2::before,.yaprak-son::before{content:"";position:absolute;left:0;right:0;top:0;height:200px;z-index:-1;border-radius:28px 28px 0 0;background:radial-gradient(70% 100% at 50% 0,rgba(242,166,90,.13),rgba(242,166,90,0));pointer-events:none}
.tutamak{position:absolute;left:50%;top:13px;width:18px;height:18px;margin-left:-9px}
.tutamak svg{display:block;width:18px;height:18px}
.tutamak circle{fill:#1A2142}
.tutamak path{fill:#F2A65A}
.y-gece .tutamak circle,.y-gece2 .tutamak circle,.yaprak-son .tutamak circle{fill:#2E3666}
.alt-bilgi.yaprak-son{position:relative;z-index:5;isolation:isolate;margin-top:-28px;padding-top:44px}
/* Açık yapraklarda iç kartlar çizgisiz, krem dolgulu (çizgi soğuk duruyordu) */
.y-ak .yk2,.y-ak .kart{background:#F6F1E9;border-color:transparent}
.y-kum .sss{border-bottom-color:rgba(26,33,66,.12)}
.sss-liste{margin-top:14px;border-top:1.5px solid rgba(26,33,66,.12)}
.y-kum .otuz,.y-ak .otuz{padding:0}
/* "30": açık zeminde amber yazı okunmuyor (2,3:1); etiket rengi #A05A1C (Tur 16 design-review bulgusu) */
.otuz b.say{color:#A05A1C}
.y-kum{background:#EEE3D2}
/* Bölüm başlığı tek kalıp: solda başlık, sağda varsa kısa bilgi */
.bas{display:flex;align-items:flex-end;justify-content:space-between;gap:12px}
.bas-yan{font-size:13px;font-weight:600;color:#5C6078;padding-bottom:3px;white-space:nowrap}
/* Kapına ne gelir: elde fotoğrafı + kutular + içerik */
.kutu-izgara{display:grid;grid-template-columns:132px minmax(0,1fr);gap:16px;align-items:center;margin-top:16px}
.elde{position:relative;height:180px;border-radius:20px;overflow:hidden;background:#E6DAC7}
.elde-not{position:absolute;left:8px;bottom:8px;font-size:12px;font-weight:600;padding:2px 8px;border-radius:999px;background:rgba(255,253,249,.92);color:#1A2142}
.sr{position:absolute;width:1px;height:1px;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.elde img{width:100%;height:100%;object-fit:cover;display:block}
.kutular{display:flex;gap:4px}
.kutu{display:flex;flex-direction:column;align-items:center;gap:2px;width:68px;animation:kutu-gir .45s cubic-bezier(.2,.7,.2,1) both}
@keyframes kutu-gir{from{opacity:0;transform:translateY(8px)}}
.kutu-ill{position:relative;display:block;width:68px;height:62px}
.kutu-ill img{position:absolute;left:50%;top:0;height:44px;width:auto;max-width:44px;transform:translateX(-50%)}
.kutu-ill svg{position:absolute;inset:0;width:68px;height:62px;fill:none;stroke:#1A2142;stroke-width:1.5;stroke-linejoin:round;stroke-linecap:round}
.kutu-ill svg .on-yuz{fill:#EEE3D2}
.kutu b{font-size:12px;font-weight:600;color:#5C6078}
.icerik{list-style:none;margin:10px 0 0;padding:0;display:flex;flex-direction:column;gap:4px;font-size:14px}
.icerik b{display:inline-block;min-width:24px;font-variant-numeric:tabular-nums}
.icerik-not{margin:8px 0 0;font-size:13px;color:#5C6078}"""

KUTU_SVG = ('<svg viewBox="0 0 68 62"><path d="M10 34 5 21"></path><path d="M58 34l5-13"></path>'
            '<rect class="on-yuz" x="10" y="34" width="48" height="26" rx="3"></rect><path d="M24 44h20"></path></svg>')

KUTU = """  <!-- Kapına ne gelir (Tur 16'dan): seçime göre kaç kutu gelir, her kutuda ne var. Elde fotoğrafı boyutu gösterir.
       Brif şikâyeti "12 disk yazıyor, 6 geliyor" yüzünden "6 + 6 hediye" yazılır. Kutudaki lamba: stüdyo fotoğrafından
       yalnız arka planı temizlenmiş kesim (ürün pikselleri aynı; canvas/c-gorsel/lamba-*.png). -->
  <section class="px yaprak y-kum gir" id="kutu">""" + tutamak(4) + """
    <div class="bas"><h2 class="h2">Kapına ne gelir<span class="n">?</span></h2><span class="bas-yan">{{kutuSay}}</span></div>
    <div class="kutu-izgara">
      <!-- Elde fotoğrafı yalnız Kız modelinde var; seçim yalnız Erkek ise Erkek stüdyo fotoğrafı (fotoğraf kutularla çelişmesin) -->
      <div class="elde"><img src="{{eldeSrc}}" alt="{{eldeAlt}}" style="object-position: {{eldePos}}"><span class="elde-not">{{eldeNot}}</span></div>
      <div>
        <span class="sr">{{kutuSr}}</span>
        <div class="kutular" aria-hidden="true"><sc-for list="{{kutular}}" as="k" hint-placeholder-count="2"><span class="kutu"><span class="kutu-ill"><img src="{{k.src}}" alt="">""" + KUTU_SVG + """</span><b>{{k.ad}}</b></span></sc-for></div>
        <ul class="icerik"><li><b>1</b> lamba</li><li><b>6</b> masal diski</li><li><b>+6</b> hediye disk</li><li><b>1</b> USB şarj kablosu</li></ul>
        <sc-if value="{{ikiliAcik}}" hint-placeholder-val="{{true}}"><p class="icerik-not">Her kutuda bunların hepsi var.</p></sc-if>
      </div>
    </div>
  </section>

"""

# Bölümler → yapraklar (sıra ve içerik B+ ile aynı)
HTML = degis(HTML, '  <section class="bolum gir" id="videolar">', '  <section class="yaprak y-kum gir" id="videolar">' + tutamak(1))
HTML = degis(HTML, '  <section id="yorumlar" class="bolum gir">', '  <section id="yorumlar" class="yaprak y-ak gir">' + tutamak(2))
HTML = degis(HTML, '  <!-- Bir gece, beş an -->\n  <section class="gece gir">', '  <!-- Bir gece, beş an -->\n  <section class="yaprak y-gece gir">' + tutamak(3))
HTML = degis(HTML, '  <section class="gece gir" id="diskler">', '  <section class="yaprak y-gece2 gir" id="diskler">' + tutamak(5))
# Sıra: Bir gece → Kapına ne gelir → Diskler. İki gece yaprağı art arda ~950px kesintisiz koyu blok yapıyordu (design-review, eleştirmen);
# kutu ("6 masal diski + 6 hediye") diskler bölümüne de doğal geçiş.
_d, _k, _o = HTML.index('  <!-- Diskler: tavana yansıt -->'), HTML.index('  <!-- Kutuda ne var -->'), HTML.index('  <!-- 30 gün iade -->')
HTML = HTML[:_d] + KUTU + HTML[_d:_k] + HTML[_o:]
HTML = degis(HTML, '  <!-- 30 gün iade -->\n  <section class="px bolum gir">', '  <!-- 30 gün iade -->\n  <section class="px yaprak y-ak gir">' + tutamak(6))
HTML = degis(HTML, '  <!-- SSS -->\n  <section class="px bolum gir">', '  <!-- SSS -->\n  <section class="px yaprak y-kum gir">' + tutamak(7))
HTML = degis(HTML, '<div style="margin-top: 14px; border-top: 1.5px solid #E3D8C7">', '<div class="sss-liste">')
HTML = degis(HTML, '  <!-- Diğer ürünler -->\n  <section class="bolum gir">', '  <!-- Diğer ürünler -->\n  <section class="yaprak y-ak gir">' + tutamak(8))
HTML = degis(HTML, '  <footer class="alt-bilgi">', '  <footer class="alt-bilgi yaprak-son">' + tutamak(9))

# Görseller: yerel dosyalardan yeniden yüklendi (canvas/c-gorsel/), yerel önizleme = tuval
JS = degis(JS, """      { id: '34462d69c62584aeefaca4cff769f3b5', n: 'Gece çocuk odası, LunaDream tavana ay ve yıldız yansıtıyor', pos: '50% 55%', oda: true },
      { id: '05d7f0466966800b2be9e851b9ada476', n: 'Gündüz çocuk odası, komodinde LunaDream', pos: '62% 66%', oda: true },
      { id: 'd0c41725fb735b5851374f373ff814f3', n: 'Gece yanan LunaDream', pos: '50% 50%', oda: true },""",
"""      { id: 'fd0bca1b99cf3837b69fb025cc4e2cd9', n: 'Gece çocuk odası, LunaDream Kız duvara ay ve yıldız yansıtıyor', pos: '50% 60%', oda: true },
      { id: '31751eb35473aca04420825deb3c3ce0', n: 'Gece çocuk odası, LunaDream Erkek (Uzay Kaşifi)', pos: '50% 62%', oda: true },
      { id: '2288b7fbcc230bd9d47e25ef6550ce78', n: 'Gündüz çocuk odası, komodinde LunaDream Kız', pos: '50% 72%', oda: true },""")
JS = degis(JS, "['0f174c24e39d6cc31f00e1e5cec0b71a', '872c633eba2deae50857a393085d6d6e', 'a3904987484c22fc3cb242c93283a2b8', 'bc6c8ee4a959d062430c96eb318b745d', 'e11f41ebd04fb544a2dcfc3fc03a9c26']",
           "['4323cd781a0d687b528b3059505be48c', '7ad3cbbe71680f4ed3027dbd056e391f', 'f060b12bc3353fae64eedf62798c5711', 'ec3c3976bbe8f18e5660f4a4c355ebf7']")
for eski, yeni, kac in [('4279ec63f6d2d18f033818bde2521861', '8b1f621be2cb3b6133b7b78bc14e1963', 1),   # 20:00 sıcak ışık
                        ('a08519c97197df401382b43ca8425d43', '5b284c77c252b08a2974bde8e43de126', 2),   # kubbesi açık (an + video)
                        ('8409b88186ef148c62a07a0bd6f2a19e', '64229e39b184f68336dc1c9b99e8e850', 1),   # tavşanlı
                        ('966c145d86bf4b972aa27d983118b8f7', 'b2c8d9b92ad3541b532e3aa108a74735', 2),   # Uzay Kaşifi (an + video)
                        ('aa906021e8f134fc2cb53a35d7d0f47e', '5ce96d9e6f38e8d571ac1cb9e529ec22', 1),   # tavanda yansıma
                        ('05d7f0466966800b2be9e851b9ada476', '2288b7fbcc230bd9d47e25ef6550ce78', 1),   # gündüz
                        ('34462d69c62584aeefaca4cff769f3b5', 'fd0bca1b99cf3837b69fb025cc4e2cd9', 1),   # video kapağı: gece odası
                        ('e11f41ebd04fb544a2dcfc3fc03a9c26', '7ad3cbbe71680f4ed3027dbd056e391f', 1)]:  # video kapağı: müşteri
    JS = degis(JS, eski, yeni, kac)
JS = degis(JS, "    return {\n      gal: gal,", """    // Kapına ne gelir: 1 Adet = seçili model; 2 Adet = iki lambanın seçimi (kutudaki lamba arka planı temizlenmiş kesim)
    var tumErkek = S.adet === 2 ? (l1 === 'erkek' && l2 === 'erkek') : S.model === 'erkek';
    var kutular = (S.adet === 2 ? [l1, l2] : [S.model]).map(function (m) { return { src: B + (m === 'kiz' ? 'b823966c39ff35824b4d6e74757646ec' : '20f90021119e4c3bdbc930b283e3635a'), ad: m === 'kiz' ? 'Kız' : 'Erkek' }; });
    return {
      kutular: kutular, kutuSay: S.adet === 2 ? '2 kutu' : '1 kutu',
      kutuSr: 'Kapına ' + kutular.length + ' kutu gelir: ' + kutular.map(function (k) { return k.ad; }).join(' ve ') + '.',
      eldeSrc: tumErkek ? ERKEK : B + '8f8d1462c27c62b0bbd3066d72c92025', eldeAlt: tumErkek ? 'LunaDream Erkek (Uzay Kaşifi)' : 'Elde tutulan LunaDream Kız', eldeNot: tumErkek ? 'Erkek modeli' : 'Kız modeli, elde', eldePos: tumErkek ? '50% 62%' : '40% 50%',
      gal: gal,""")

open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · C2 Ay yaprakları', css=CSS) + HTML + TAIL.format(h=int(os.environ.get('C_H', 5854)), js=JS))
print('yazıldı:', os.path.abspath(OUT))
