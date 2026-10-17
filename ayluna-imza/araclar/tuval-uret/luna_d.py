# LunaDream ürün sayfası · D "Oda ve Tavan" (Tur 18, sıfırdan). Çalıştır: python3 luna_d.py
# Kullanıcı: "Yeni, sıfırdan bir tasarım yap; her şeyi yeni ajanlar karar versin."
# Süreç: 3 yön ajanı (A frontend-design, B Impeccable, C Taste) aynı brifle plan yazdı; eleştirmen A'yı seçti,
# C'den 3 parça aldı (amber sayaç şeridi, saatle koyulaşan Bir gece satırları, ay evreli teslim çizelgesi).
# Planlar ve karar: ogrenme/tur18/ (brif, plan-A/B/C, karar).
# Fikir: sayfa 20:00'de lambası yanan çocuk odası. Açık bantlar lambanın ışığını alan duvarlar; karanlık yalnız
# tavanda (Diskler) ve gecede (galeri, 20:45–21:00). Tek imza an: disk tavana açılır.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import TL_JS
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamD.dc.html')


def ay(f, r=9, c=12):
    # Ay evresi yolu: f = dolu kısım (0..1)
    rx = abs(1 - 2 * f) * r
    return 'M%d %dA%d %d 0 0 1 %d %dA%.2f %d 0 0 %d %d %dZ' % (c, c - r, r, r, c, c + r, rx, r, 0 if f < .5 else 1, c, c - r)


HILAL = '<svg class="logo-ay" viewBox="0 0 24 24" aria-hidden="true"><path d="M15.5 3.5a8.5 8.5 0 1 0 5 15.4A7 7 0 0 1 15.5 3.5z"></path></svg>'
YILDIZ5 = ''.join('<path transform="translate(%d 0)" d="M8 1.2l2 4.3 4.7.5-3.5 3.2 1 4.6L8 11.4l-4.2 2.4 1-4.6L1.3 6l4.7-.5z"></path>' % (i * 17) for i in range(5))


def yildiz(idn):
    # Kesirli puan yıldızları (4,7 → %94 dolu); puan Loox'tan gelir
    return ('<svg class="yildiz" viewBox="0 0 84 15" aria-hidden="true"><defs><clipPath id="%s"><rect x="0" y="0" width="{{starW}}" height="15"></rect></clipPath></defs>'
            '<g class="bos">%s</g><g class="dolu" clip-path="url(#%s)">%s</g></svg>') % (idn, YILDIZ5, idn, YILDIZ5)


IK = {  # 1,5px çizgi ikonlar
    'kargo': '<path d="M3 7h11v9H3zM14 10h4l3 3v3h-7z"></path><circle cx="7" cy="17.5" r="1.8"></circle><circle cx="17.5" cy="17.5" r="1.8"></circle>',
    'iade': '<path d="M4 12a8 8 0 1 0 3-6.2"></path><path d="M4 4v4h4"></path>',
    'kilit': '<rect x="5" y="10.5" width="14" height="10" rx="2.5"></rect><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"></path>',
    'disk': '<circle cx="12" cy="12" r="8.5"></circle><circle cx="12" cy="12" r="2.2"></circle>',
    'menu': '<path d="M4 8h16M4 16h11"></path>',
    'canta': '<path d="M5 8h14l-1 12H6z"></path><path d="M9 8a3 3 0 0 1 6 0"></path>',
    'oynat': '<path d="M9 7l8 5-8 5z"></path>',
    'arti': '<path d="M12 6v12M6 12h12"></path>',
}


def ikon(ad, cls='ik'):
    return '<svg class="%s" viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % (cls, IK[ad])


CSS = r"""
/* Tokenlar (karar.md): renk dışı ton yok */
.pg{--gece:#1A2142;--lamba:#F2A65A;--kehribar:#9A561B;--carsaf:#FFF8F0;--duvar:#F8E8DA;--sis:#5C6078;--cizgi:rgba(26,33,66,.16);--e:cubic-bezier(.22,1,.36,1);
  width:390px;position:relative;overflow:clip;timeline-scope:--fiyat;background:var(--carsaf);color:var(--gece);font-family:"Atkinson Hyperlegible Next",ui-sans-serif,system-ui,sans-serif;font-size:15px;line-height:1.5;-webkit-font-smoothing:antialiased}
.pg *{box-sizing:border-box}
:where(.pg) button{font:inherit;color:inherit}
.pg button{touch-action:manipulation;-webkit-tap-highlight-color:transparent}
.pg :focus-visible{outline:2px solid var(--gece);outline-offset:2px}
.koyu :focus-visible{outline-color:var(--lamba)}
.lit{font-family:"Literata",Georgia,serif;font-weight:500;letter-spacing:-.005em}
.tab{font-variant-numeric:tabular-nums}
.ik{width:20px;height:20px;flex:none;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.sr{position:absolute;width:1px;height:1px;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* Bant: kenardan kenara, komşusundan farklı ton. İçeride 8/16/24, bantlar arası 32+32 = 64 ve ton değişimi */
.bant{position:relative;padding:32px 20px}
.b-c{background:var(--carsaf)}.b-d{background:var(--duvar)}.b-g{background:var(--gece);color:var(--carsaf)}
.h2{margin:0;font-size:22px;line-height:1.25;text-wrap:balance}
.bas{display:flex;align-items:flex-end;justify-content:space-between;gap:12px}
.bas-yan{font-size:13px;color:var(--sis);white-space:nowrap}
.alt-yazi{margin:4px 0 0;font-size:14px;color:var(--sis)}
.koyu .alt-yazi{color:rgba(255,248,240,.72)}
.etk{margin:0;font-size:13px;font-weight:700;color:var(--kehribar)}
.not{margin:8px 0 0;font-size:13px;color:var(--sis)}
.yildiz{width:84px;height:15px}
.yildiz .bos{fill:var(--cizgi)}.yildiz .dolu{fill:var(--lamba)}
/* Bölüm girişi (kullanıcı isteği §10): içerik 16px aşağıdan ve saydamdan, bir kez. Bant opak kalır.
   Canlıda IntersectionObserver ile 640 ms ve içerik 80 ms sonra; panoda kaydırma zaman çizelgesiyle. */
/* Kapsayıcı overflow:clip (hidden değil): kaydırma kabı oluşmaz, yapışkan çubuk ve view() zaman çizelgesi çalışır.
   Bir gece satırları bant olduğu için orada yalnız satır içerikleri hareket eder (bant soluklaşmaz). */
@supports (animation-timeline: view()){
  .gir > *,.gir2 .gece-bas > *,.gir2 .an > *{animation:gir linear both;animation-timeline:view();animation-range:entry 0% entry 40%}
  @keyframes gir{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
  /* Yapışkan çubuk: fiyat bandı ekrandan çıkınca gelir (ilk ekranda güven satırını örtmez). Canlıda 5. bölüm ekrandayken de gizlenir (IntersectionObserver). */
  .ad{view-timeline-name:--fiyat}
  .yapis{animation:yapis-gir linear both;animation-timeline:--fiyat;animation-range:exit 0% exit 100%}
  @keyframes yapis-gir{from{opacity:0;transform:translateY(100%);visibility:hidden}to{opacity:1;transform:none;visibility:visible}}
  /* İmza an ilk kez sahne ekrana girerken oynar */
  .yans.on.ilk,.yans.on.ilk .hal{animation-timeline:view();animation-range:entry 30% cover 45%;animation-delay:0s}
}

/* 1 · Sayaç şeridi (Lamba): her gece 23:59'da (İstanbul) sıfırlanır */
.serit{display:flex;justify-content:center;align-items:center;gap:8px;height:32px;background:var(--lamba);color:var(--gece);font-size:13px}
.serit b{font-weight:700}

/* 2 · Galeri (Gece): logo ve küçük resimler fotoğrafın üstünde */
.galeri{position:relative;height:430px;background:var(--gece);color:var(--carsaf);overflow:hidden}
.galeri header{position:absolute;left:0;right:0;top:0;z-index:3;height:44px;display:flex;align-items:center;justify-content:space-between;padding:0 4px}
.ust-ikon{width:48px;height:48px;display:grid;place-items:center;border:0;background:transparent;cursor:pointer}
.logo{display:flex;align-items:center;gap:6px;font-size:20px;line-height:1}
.logo-ay{width:18px;height:18px;fill:var(--lamba)}
.kare{position:absolute;left:0;right:0;top:0;bottom:0}
.kare img{position:absolute;left:0;width:390px;object-fit:cover;opacity:0;transition:opacity .24s var(--e)}
.kare img.on{opacity:1}
.kare::before{content:"";position:absolute;inset:auto 0 0 0;height:120px;z-index:1;background:linear-gradient(0deg,rgba(26,33,66,.72),rgba(26,33,66,0));pointer-events:none}
.kare::after{content:"";position:absolute;inset:0 0 auto 0;height:96px;background:linear-gradient(180deg,rgba(26,33,66,.78),rgba(26,33,66,0));pointer-events:none}
.gec{position:absolute;top:44px;bottom:72px;z-index:2;width:50%;border:0;background:transparent;cursor:pointer;padding:0}
.kucukler{position:absolute;left:20px;right:20px;bottom:14px;z-index:3;display:flex;align-items:center;gap:8px}
.kucukler-ray{display:flex;gap:6px;flex:1;min-width:0;overflow-x:auto;scrollbar-width:none;padding:3px}
.kucukler-ray::-webkit-scrollbar{display:none}
.kc{flex:none;width:48px;height:48px;padding:0;border:2px solid rgba(255,248,240,.32);border-radius:14px;overflow:hidden;background:var(--gece);cursor:pointer;transition:transform .16s var(--e)}
.kc:active{transform:scale(.96)}
.kc.on{border-color:var(--carsaf)}
.kc img{width:100%;height:100%;object-fit:cover;display:block}
.sira{flex:none;font-size:13px;font-weight:700;color:var(--carsaf)}

/* 3 · Ad bandı (Çarşaf) */
.ad{padding:12px 20px 32px}
.ad-ust{display:flex;align-items:center;justify-content:space-between;gap:12px}
.puan{display:inline-flex;align-items:center;gap:8px;min-height:48px;font-size:14px;color:var(--gece);text-decoration:none}
.puan span{color:var(--sis)}
.stok{display:inline-flex;align-items:center;gap:8px;font-size:14px}
.nokta{width:8px;height:8px;border-radius:50%;background:var(--kehribar);flex:none}
.urun-ad{margin:0;font-size:28px;line-height:1.15}
.fiyat{display:flex;align-items:baseline;flex-wrap:wrap;gap:4px 12px;margin:8px 0 0}
.fiyat b{font-size:20px;font-weight:700}
.fiyat s{font-size:14px;color:var(--sis)}
.fiyat .ind{font-size:13px;font-weight:700;color:var(--kehribar)}
.kampanya{margin:2px 0 0;font-size:13px;color:var(--sis)}
.guven{display:flex;justify-content:space-between;gap:8px;margin:12px 0 0;padding:0;list-style:none;font-size:13px}
.guven li{display:flex;align-items:center;gap:8px}
.guven .ik{color:var(--kehribar)}

/* 4 · Sihirli özellikler (Duvar): kart yok, ince artı çizgisiyle ayrılan 2×2 pencere */
.pencere{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));margin-top:12px;position:relative}
.pencere::before,.pencere::after{content:"";position:absolute;background:var(--cizgi)}
.pencere::before{left:50%;top:0;bottom:0;width:1.5px;margin-left:-.75px}
.pencere::after{top:50%;left:0;right:0;height:1.5px;margin-top:-.75px}
.bolme{display:flex;flex-direction:column;gap:8px;padding:16px 12px 16px 0}
.bolme:nth-child(2n){padding-left:16px;padding-right:0}
.bolme b{font-size:15px;font-weight:700;line-height:1.3}
.bolme > span:last-child{font-size:13px;color:var(--sis);line-height:1.4}
.anim{position:relative;width:40px;height:40px;border-radius:14px;background:var(--gece);color:var(--lamba);display:grid;place-items:center;overflow:hidden;isolation:isolate}
.anim svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
/* Sihirli döngüleri (kullanıcı istisnası): yavaş, yalnız transform/opacity; canlıda ekran dışındayken durur */
/* Hale ayın arkasında nefes alır; ay (amber) haleyle karışmasın diye hale soluk ve küçük başlar */
@keyframes nefes{0%,100%{transform:scale(.7);opacity:.3}50%{transform:scale(1.05);opacity:.6}}
.hale{position:absolute;inset:2px;z-index:-1;border-radius:50%;background:radial-gradient(circle,rgba(242,166,90,.55),rgba(242,166,90,0) 68%);transform:scale(.8);opacity:.45;animation:nefes 4.5s var(--e) infinite}
/* Durağan hâl (ve azaltılmış hareket) açık yelpaze; döngüde kapanıp yeniden açılır */
@keyframes yelpaze{0%,30%{transform:rotate(var(--r))}55%,70%{transform:rotate(0)}100%{transform:rotate(var(--r))}}
.yel{position:relative;width:30px;height:30px}
.yel img{position:absolute;left:7px;top:2px;width:16px;height:16px;border-radius:50%;transform-origin:50% 160%;transform:rotate(var(--r));animation:yelpaze 5s var(--e) infinite;border:1.5px solid var(--gece)}
.yel img:nth-child(1){--r:-28deg}.yel img:nth-child(2){--r:0deg}.yel img:nth-child(3){--r:28deg}
@keyframes ses{0%,100%{transform:scaleY(.3)}50%{transform:scaleY(1)}}
.dalga{display:flex;align-items:center;gap:3px;height:20px}
.dalga i{display:block;width:3px;height:20px;border-radius:2px;background:var(--lamba);transform-origin:50% 50%;animation:ses 2.4s ease-in-out infinite}
.dalga i:nth-child(2){animation-delay:-.4s}.dalga i:nth-child(3){animation-delay:-.8s}.dalga i:nth-child(4){animation-delay:-1.2s}
@keyframes sarj{0%{transform:scaleX(.15);opacity:0}8%{opacity:1}70%,90%{transform:scaleX(1);opacity:1}100%{transform:scaleX(1);opacity:0}}
.pil{position:relative;width:24px;height:13px;border:1.5px solid var(--lamba);border-radius:3px;padding:1.5px}
.pil::after{content:"";position:absolute;right:-4px;top:3.5px;width:2px;height:4px;border-radius:0 1px 1px 0;background:var(--lamba)}
.pil i{display:block;height:100%;border-radius:1px;background:var(--lamba);transform-origin:0 50%;animation:sarj 3.8s var(--e) infinite}

/* 5 · Satın al (Çarşaf) */
.al{padding:32px 20px}
.grup{margin-top:24px}
.grup:first-child{margin-top:0}
.etk-satir{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px}
.modeller{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.mk{display:grid;grid-template-columns:48px minmax(0,1fr);gap:12px;align-items:center;min-height:64px;padding:8px;border:1.5px solid var(--cizgi);border-radius:14px;background:var(--carsaf);text-align:left;cursor:pointer;transition:transform .16s var(--e)}
.mk:active,.pk:active{transform:scale(.98)}
.mk.on{border:2px solid var(--gece);background:var(--duvar);padding:7.5px}
.mk-foto{width:48px;height:48px;border-radius:14px;overflow:hidden;background:var(--duvar)}
.mk-foto img{width:100%;height:100%;object-fit:cover;transform:scale(1.5);transform-origin:50% 62%}
.mk b{display:block;font-size:15px;font-weight:700;line-height:1.2}
.mk span span{font-size:13px;color:var(--sis)}
.paketler{display:flex;flex-direction:column;gap:12px}
.pk{position:relative;display:grid;grid-template-columns:20px 44px minmax(0,1fr);gap:12px;align-items:center;min-height:76px;padding:12px 16px 12px 12px;border:1.5px solid var(--cizgi);border-radius:14px;background:var(--carsaf);text-align:left;cursor:pointer;transition:transform .16s var(--e)}
.pk.on{border:2px solid var(--gece);background:var(--duvar);padding:11.5px 15.5px 11.5px 11.5px}
.radyo{width:20px;height:20px;border-radius:50%;border:1.5px solid var(--gece);display:grid;place-items:center}
.radyo i{width:10px;height:10px;border-radius:50%;background:var(--gece);transform:scale(0);transition:transform .16s var(--e)}
.pk.on .radyo i{transform:scale(1)}
.pk-lamba{position:relative;width:44px;height:48px}
.pk-lamba img{position:absolute;bottom:0;height:44px;width:auto;max-width:36px}
.pk-lamba img:first-child{left:0}.pk-lamba img.iki{left:16px;height:40px}
.pk-satir{display:flex;justify-content:space-between;align-items:baseline;gap:8px}
.pk-ad{font-size:15px;font-weight:700}
.pk-fiyat{font-size:20px;font-weight:700}
.pk-alt{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-top:2px;font-size:13px;color:var(--sis)}
.pk-alt .hed{display:inline-flex;align-items:center;gap:4px;color:var(--gece)}
.pk-alt .hed .ik{width:16px;height:16px;color:var(--kehribar)}
.pk-alt .ind{font-weight:700;color:var(--kehribar)}
.pk-alt s,.pk-ikinci s{color:var(--sis)}
/* İkinci satır: solda hediye, sağda eski fiyat ya da tane fiyatı; sığmazsa sağdaki alta iner, hediye bölünmez */
.pk-ikinci{flex-wrap:wrap;gap:0 8px;margin-top:2px;font-size:13px;color:var(--sis)}
.pk-ikinci .hed{display:inline-flex;align-items:center;gap:4px;color:var(--gece);white-space:nowrap}
.pk-ikinci .hed .ik{width:16px;height:16px;color:var(--kehribar)}
.pk-ikinci .ind{font-weight:700;color:var(--kehribar)}
.sekme{position:absolute;right:16px;top:-11px;padding:2px 8px;border-radius:0;background:var(--lamba);color:var(--gece);font-size:12px;font-weight:700;line-height:1.5}
.ikili{display:flex;flex-direction:column;gap:8px;margin-top:12px;animation:belir .24s var(--e) both}
@keyframes belir{from{opacity:0;transform:translateY(8px)}}
.lsat{display:flex;align-items:center;justify-content:space-between;gap:12px;font-size:14px}
.seg{display:inline-flex;gap:4px}
.seg button{min-width:72px;min-height:48px;border:1.5px solid var(--cizgi);border-radius:14px;background:transparent;font-size:15px;font-weight:700;color:var(--sis);cursor:pointer}
.seg button.on{background:var(--gece);border-color:var(--gece);color:var(--carsaf)}
.stok-satir{display:flex;align-items:center;gap:8px;margin:24px 0 0;font-size:14px}
.btn-ana{display:flex;align-items:center;gap:10px;width:100%;min-height:56px;margin-top:12px;padding:0 16px;border:0;border-radius:14px;background:var(--lamba);color:var(--gece);font-size:15px;font-weight:700;cursor:pointer;transition:transform .16s var(--e)}
.btn-ana:active,.btn-kp:active{transform:scale(.98)}
.btn-ana .fy{margin-left:auto}
.btn-kp{display:flex;align-items:center;justify-content:center;width:100%;min-height:52px;margin-top:16px;border:1.5px solid var(--gece);border-radius:14px;background:transparent;font-size:15px;font-weight:700;cursor:pointer;transition:transform .16s var(--e)}
.btn-not{margin:8px 0 0;font-size:13px;color:var(--sis)}
.teslim{position:relative;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));margin:24px 0 0;padding:0;list-style:none}
.teslim::before{content:"";position:absolute;left:16.6%;right:16.6%;top:11px;height:1.5px;background:var(--cizgi)}
.teslim li{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;gap:2px;font-size:13px;color:var(--sis)}
.teslim b{font-size:15px;font-weight:700;color:var(--gece)}
.teslim svg{width:24px;height:24px;margin-bottom:6px;background:var(--carsaf);border-radius:50%}
.teslim circle{fill:var(--carsaf);stroke:var(--gece);stroke-width:1.5}
.teslim path{fill:var(--lamba)}

/* 6 · Diskler (Gece) · imza an "Disk tavana açılır". Üst kenar kubbe: sayfadaki tek eğri */
.tavan{padding:64px 20px 32px;border-radius:50% 50% 0 0 / 56px 56px 0 0;background:var(--gece);color:var(--carsaf)}
.tavan .h2{text-align:center}
.tavan .alt-yazi{text-align:center}
.sahne{position:relative;height:346px;margin-top:16px}
.yer{position:absolute;right:0;top:0;font-size:12px;font-weight:700;color:rgba(255,248,240,.72)}
.yans{position:absolute;left:50%;top:16px;width:250px;height:250px;margin-left:-125px;opacity:0;transform-origin:50% 100%}
.yans.on{opacity:.9;animation:acil .64s var(--e) .08s both}
.yans.eski{animation:son .2s var(--e) both}
@keyframes acil{0%{opacity:0;transform:translateY(96px) scale(.2)}44%{opacity:.9}100%{opacity:.9;transform:none}}
@keyframes son{from{opacity:.9}to{opacity:0}}
.yans .hal{position:absolute;inset:-24px;border-radius:50%;background:radial-gradient(circle,rgba(242,166,90,.22),rgba(242,166,90,0) 70%)}
.yans.on .hal{animation:hale .64s var(--e) .08s both}
@keyframes hale{from{transform:scale(.6)}to{transform:none}}
.yans img{position:relative;width:250px;height:250px;border-radius:50%;object-fit:cover;display:block}
.lamba-kes{position:absolute;left:50%;bottom:0;height:96px;width:auto;transform:translateX(-50%)}
.disk-adlar{position:relative;height:24px;margin-top:12px;text-align:center}
/* Ad çapraz geçişi: eski ve yeni aynı anda, 240 ms sonra 160 ms */
.disk-adlar span{position:absolute;inset:0;font-size:15px;font-weight:700;opacity:0;transition:opacity .16s var(--e) .24s}
.disk-adlar span.on{opacity:1}
.diskler{display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin:16px auto 0;width:348px}
.dk{width:48px;height:48px;padding:0;border:0;border-radius:50%;background:transparent;cursor:pointer}
.dk img{width:48px;height:48px;border-radius:50%;display:block;transition:transform .16s var(--e)}
/* Seçim: diskin çevresinde Lamba halka. Odak: daha dışta kesik Çarşaf halka (ikisi ayırt edilir) */
.dk.on img{outline:2px solid var(--lamba);outline-offset:3px}
.koyu .dk:focus-visible{outline:2px dashed var(--carsaf);outline-offset:7px}
.dk.on img{animation:bas .16s var(--e)}
@keyframes bas{50%{transform:scale(.92)}}
.tavan .not{text-align:center;color:rgba(255,248,240,.72)}

/* 7 · Kapına ne gelir (Duvar) */
.kutu-izg{display:grid;grid-template-columns:132px minmax(0,1fr);gap:16px;align-items:start;margin-top:12px}
.elde img{width:132px;height:176px;border-radius:20px;object-fit:cover;display:block;background:var(--carsaf)}
.elde span{display:block;margin-top:6px;font-size:12px;font-weight:700;color:var(--sis)}
.icerik{list-style:none;margin:0;padding:0}
.icerik li{display:grid;grid-template-columns:36px minmax(0,1fr);gap:12px;align-items:baseline;padding:12px 0;border-bottom:1.5px solid var(--cizgi);font-size:14px}
.icerik li:first-child{padding-top:2px}
.icerik b{font-size:20px;font-weight:700;text-align:right}

/* 8 · Videolar (Çarşaf): canlıda Shopify videoları; gerçek video yoksa bölüm gizlenir */
.ray{display:flex;align-items:flex-start;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding:0 20px;margin:12px -20px 0;padding:0 20px 4px;scrollbar-width:none}
.ray::-webkit-scrollbar{display:none}
.vid{flex:0 0 160px;scroll-snap-align:start;padding:0;border:0;background:transparent;text-align:left;cursor:pointer}
.vid-kap{position:relative;display:block;height:284px;border-radius:20px;overflow:hidden;background:var(--gece)}
.vid-kap img{width:100%;height:100%;object-fit:cover;display:block}
.oynat{position:absolute;left:50%;top:50%;width:52px;height:52px;margin:-26px 0 0 -26px;border-radius:50%;background:var(--carsaf);display:grid;place-items:center;color:var(--gece)}
.oynat .ik{fill:currentColor;width:22px;height:22px;margin-left:2px}
.vid-et{position:absolute;left:12px;top:12px;padding:2px 8px;background:rgba(26,33,66,.72);color:var(--carsaf);font-size:12px;font-weight:700}
.vid b{display:block;margin-top:8px;font-size:15px;font-weight:700;line-height:1.3}
.vid > span{font-size:13px;color:var(--sis)}

/* 9 · Yorumlar (Duvar): liste, kart yok; konu çipleriyle süzülür */
.puan-buyuk{display:flex;flex-direction:column;align-items:flex-end;gap:2px}
.puan-buyuk b{font-size:22px;line-height:1}
.mfoto{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin-top:16px}
.mfoto img{width:100%;aspect-ratio:1;border-radius:20px;object-fit:cover;display:block}
.cipler{display:flex;gap:8px;margin-top:16px;overflow-x:auto;scrollbar-width:none}
.cip{flex:none;min-height:48px;padding:0 16px;border:1.5px solid var(--cizgi);border-radius:14px;background:transparent;font-size:15px;font-weight:700;cursor:pointer}
.cip.on{background:var(--gece);border-color:var(--gece);color:var(--carsaf)}
.yorumlar{list-style:none;margin:8px 0 0;padding:0}
.yorumlar li{padding:16px 0;border-bottom:1.5px solid var(--cizgi)}
.yorumlar q{display:block;font-size:15px;line-height:1.55;quotes:"“" "”"}
.yorumlar q::before{content:open-quote}.yorumlar q::after{content:close-quote}
.yorumlar small{display:block;margin-top:6px;font-size:13px;color:var(--sis)}
.btn-ince{display:flex;align-items:center;justify-content:center;width:100%;min-height:52px;margin-top:16px;border:1.5px solid var(--gece);border-radius:14px;color:var(--gece);font-size:15px;font-weight:700;text-decoration:none}

/* 10 · Bir gece, beş an: her satır kendi bandı; akşam kararır, sabah açılır. Soldaki saat rayı satırları bağlar */
.gece-bas{padding:32px 20px 8px}
.an{position:relative;display:grid;grid-template-columns:52px 9px minmax(0,1fr) 72px;gap:12px;align-items:center;padding:16px 20px}
.an::before{content:"";position:absolute;left:87.75px;top:0;bottom:0;width:1.5px;background:var(--cizgi)}
.an.koyu::before{background:rgba(255,248,240,.24)}
.an.ilk::before{top:50%}
.an.son::before{bottom:50%}
.saat{position:relative;z-index:1;font-size:20px;color:var(--kehribar)}
.an.koyu .saat{color:var(--lamba)}
.nok{position:relative;z-index:1;width:9px;height:9px;border-radius:50%;background:var(--kehribar)}
.an.koyu .nok{background:var(--lamba)}
.an b{display:block;font-size:15px;font-weight:700;line-height:1.3}
.an p{margin:2px 0 0;font-size:14px;color:var(--sis);line-height:1.4}
.an.koyu p{color:rgba(255,248,240,.72)}
.an img{width:72px;height:96px;border-radius:20px;object-fit:cover;display:block}

/* 11 · 30 gün iade (Çarşaf) */
.otuz{display:grid;grid-template-columns:auto minmax(0,1fr);gap:16px;align-items:center}
.otuz .say{font-size:40px;line-height:1;color:var(--kehribar)}
.otuz span > b{display:block;font-size:15px;font-weight:700}
.otuz p{margin:2px 0 0;font-size:14px;color:var(--sis)}

/* 12 · SSS (Duvar): anında açılır (yükseklik canlandırılmaz) */
.sss-liste{margin-top:12px;border-top:1.5px solid var(--cizgi)}
.sss{border-bottom:1.5px solid var(--cizgi)}
.sss summary{list-style:none;display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:56px;font-size:15px;font-weight:700;cursor:pointer}
.sss summary::-webkit-details-marker{display:none}
.sss .ac{width:32px;height:32px;flex:none;border:1.5px solid var(--gece);border-radius:50%;display:grid;place-items:center;transition:transform .24s var(--e)}
.sss .ac .ik{width:16px;height:16px}
.sss[open] .ac{transform:rotate(45deg)}
.sss p{margin:0 0 16px;font-size:14px;color:var(--sis)}

/* 13 · Odanın geri kalanı (Çarşaf) */
.urun{flex:0 0 148px;scroll-snap-align:start;text-decoration:none;color:var(--gece)}
.urun-foto{position:relative;display:block;width:148px;height:148px;border-radius:20px;overflow:hidden;background:var(--duvar)}
.urun-foto img{width:100%;height:100%;object-fit:cover;display:block}
.urun b{display:block;margin-top:8px;font-size:15px;font-weight:700;line-height:1.3}
.urun span{font-size:14px}
.urun s{margin-left:6px;font-size:13px;color:var(--sis)}

/* 14 · Alt bilgi (Duvar) */
.yasal{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 16px;margin-top:24px}
.yasal a{display:flex;align-items:center;min-height:48px;font-size:14px;color:var(--gece);text-decoration:none;border-bottom:1.5px solid var(--cizgi)}
.kunye{margin:16px 0 0;font-size:13px;color:var(--sis);line-height:1.6}
.dev{display:flex;align-items:center;gap:8px;margin-top:24px;font-size:40px;line-height:1}
.dev .logo-ay{width:32px;height:32px}
.kdv{margin:16px 0 0;font-size:13px;color:var(--sis)}

/* Yapışkan çubuk (Çarşaf, 64px). Canlıda satın al bölümü ekrandayken gizlenir (IntersectionObserver); env(safe-area-inset-bottom) */
.yapis{position:sticky;bottom:0;z-index:10;display:flex;align-items:center;gap:12px;height:64px;margin-top:-64px;padding:0 12px 0 16px;background:var(--carsaf);border-top:1.5px solid var(--cizgi)}
.yapis-foto{position:relative;width:48px;height:44px;flex:none}
.yapis-foto img{position:absolute;bottom:0;left:0;height:44px;width:auto;max-width:36px}
.yapis-foto img.iki{left:16px;height:40px}
.yapis-yazi{flex:1;min-width:0;display:flex;flex-direction:column;line-height:1.25}
.yapis-yazi b{font-size:15px;font-weight:700}
.yapis-yazi span{font-size:13px;color:var(--sis);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.yapis .btn-ana{width:auto;min-height:48px;margin:0;padding:0 20px}

@media (prefers-reduced-motion:reduce){
  .pg *:not(.yapis){animation:none!important;transition:none!important}
  .yans{transition:opacity .2s!important}
}
"""

DISK_IDS = [('Ay ve yıldız', '4a3a69e8c1d8dddad8c33f8f463b8a0e'), ('Okyanus', 'a24f13e032569f76d64b9b0fbe8d74f7'),
            ('Uzay', 'b088d2c82561b76f6db997fbc3944059'), ('Deniz kızı', '04ed9ce4ae8a36619975caa7d2de9ad8'),
            ('Denizanası', 'e3caea057eb48a63b2ecb70c317f5e3b'), ('Şato', 'bbd010d8d946edc8fef9c0404cba4ea2'),
            ('Hayvanlar', 'ed5548471e30af0d03e8b419f8ab81ee'), ('Kış gecesi', '88d0b83acee35abef0934694ef439827'),
            ('Taşıtlar', 'deaace9b300bee84399862a13f84b2d6'), ('Masal', '6b08a94993cfc00099888dd3bd4cf110'),
            ('Doğum günü', 'c2e8b0c346ed92731ab4a2f83a01d3ef')]

TESLIM = ''.join('<li><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="%s"></path></svg><b>%s</b>%s</li>' % (ay(f), b, s)
                 for f, b, s in [(.25, 'Bugün', 'Siparişin alındı'), (.5, '{{kargo}}', 'Kargoda'), (1, '{{teslim}}', 'Kapında')])

HTML = """<div class="pg">
  <!-- 1 · Sayaç şeridi: her gece 23:59'da (İstanbul) sıfırlanır. Koşul (yalnız sahibine): zam gelse de o günün fiyatı 23:59'a kadar korunur. -->
  <div class="serit" role="timer" aria-label="{{cdAria}}"><span>Bugünkü fiyat garantisi</span><b class="tab">{{cdShort}}</b></div>

  <!-- 2 · Galeri: Shopify ana ürün medyası. Oda sahneleri gerçek üründen (ürün değiştirilmedi); afişler kırpılmadan kare -->
  <section class="galeri koyu" aria-label="LunaDream fotoğrafları">
    <header><button class="ust-ikon" type="button" aria-label="Menü">""" + ikon('menu') + """</button><span class="logo lit">""" + HILAL + """Ayluna</span><button class="ust-ikon" type="button" aria-label="Sepet">""" + ikon('canta') + """</button></header>
    <div class="kare"><sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><img class="{{f.cls}}" src="{{f.src}}" alt="{{f.alt}}" aria-hidden="{{f.gizli}}" style="top: {{f.top}}px; height: {{f.h}}px; object-position: {{f.pos}}"></sc-for></div>
    <button class="gec" type="button" style="left: 0" aria-label="Önceki fotoğraf" onClick="{{gPrev}}"></button>
    <button class="gec" type="button" style="right: 0" aria-label="Sonraki fotoğraf" onClick="{{gNext}}"></button>
    <div class="kucukler"><div class="kucukler-ray"><sc-for list="{{gal}}" as="f" hint-placeholder-count="7"><button class="{{f.kcls}}" type="button" onClick="{{f.pick}}" aria-label="{{f.n}}" aria-pressed="{{f.on}}"><img src="{{f.src}}" alt=""></button></sc-for></div><span class="sira tab">{{gNo}}/{{gCount}}</span></div>
  </section>

  <!-- 3 · Ad: puan ve sayı Loox'tan (teyit bekliyor); "Stokta" Shopify stok bilgisinden -->
  <section class="ad b-c">
    <div class="ad-ust"><a class="puan" href="#yorumlar" aria-label="{{rating}} puan, {{reviews}} yorum. Yorumlara git.">""" + yildiz('yd1') + """<b class="tab">{{rating}}</b><span>({{reviews}} yorum)</span></a></div>
    <h1 class="urun-ad lit">LunaDream</h1>
    <p class="fiyat tab"><b>{{p1}}</b><s>{{c1}}</s><span class="ind">%{{pct}} indirim</span></p>
    <ul class="guven"><li>""" + ikon('kargo') + """Ücretsiz kargo</li><li>""" + ikon('iade') + """30 gün iade</li><li>""" + ikon('kilit') + """Güvenli ödeme</li></ul>
  </section>

  <!-- 4 · Sihirli özellikler (kullanıcı isteği): 4 ürün özelliği, her birinde ürüne özgü küçük canlı çizim -->
  <section class="bant b-d gir">
    <h2 class="h2 lit">Sihirli özellikler</h2>
    <div class="pencere">
      <div class="bolme"><span class="anim" aria-hidden="true"><span class="hale"></span>""" + HILAL.replace('class="logo-ay"', 'style="fill: currentColor; stroke: none"') + """</span><b>Mışıl mışıl uykular</b><span>3 parlaklık ayarı.</span></div>
      <div class="bolme"><span class="anim" aria-hidden="true"><span class="yel"><img src="/_blob/4a3a69e8c1d8dddad8c33f8f463b8a0e" alt=""><img src="/_blob/a24f13e032569f76d64b9b0fbe8d74f7" alt=""><img src="/_blob/b088d2c82561b76f6db997fbc3944059" alt=""></span></span><b>6 + 6 masal diski</b><span>Altısı hediye.</span></div>
      <div class="bolme"><span class="anim" aria-hidden="true"><span class="dalga"><i></i><i></i><i></i><i></i></span></span><b>Bluetooth ninni</b><span>Telefondan bağlan, çalsın.</span></div>
      <div class="bolme"><span class="anim" aria-hidden="true"><span class="pil"><i></i></span></span><b>Kablosuz kullanım</b><span>Şarjlı, her odaya taşı.</span></div>
    </div>
  </section>

  <!-- 5 · Satın al: model → paket → (2'li seçim) → stok → kartla öde → kapıda öde → teslim -->
  <section class="al b-c" id="siparis">
    <div class="grup">
      <div class="etk-satir"><p class="etk">Model</p></div>
      <div class="modeller"><sc-for list="{{models}}" as="m" hint-placeholder-count="2"><button class="{{m.cls}}" type="button" onClick="{{m.pick}}" aria-pressed="{{m.on}}"><span class="mk-foto"><img src="{{m.src}}" alt=""></span><span><b>{{m.n}}</b><span>{{m.sub}}</span></span></button></sc-for></div>
    </div>
    <div class="grup">
      <div class="etk-satir"><p class="etk">Paket</p><span class="bas-yan">Kampanya: 1–31 Ekim</span></div>
      <div class="paketler"><sc-for list="{{paket}}" as="b" hint-placeholder-count="2">
        <button class="{{b.cls}}" type="button" onClick="{{b.pick}}" aria-pressed="{{b.on}}">
          <sc-if value="{{b.rib}}" hint-placeholder-val="{{false}}"><span class="sekme">En avantajlı</span></sc-if>
          <span class="radyo" aria-hidden="true"><i></i></span>
          <span class="pk-lamba" aria-hidden="true"><img src="{{b.src1}}" alt=""><sc-if value="{{b.two}}" hint-placeholder-val="{{false}}"><img class="iki" src="{{b.src2}}" alt=""></sc-if></span>
          <span>
            <span class="pk-satir"><span class="pk-ad">{{b.t}}</span><span class="pk-fiyat tab">{{b.p}}</span></span>
            <span class="pk-satir pk-ikinci"><span class="hed">""" + ikon('disk') + """{{b.hediye}}</span><sc-if value="{{b.hasOld}}" hint-placeholder-val="{{true}}"><span class="tab"><s>{{b.old}}</s> <span class="ind">{{b.pctTxt}}</span></span></sc-if><sc-if value="{{b.two}}" hint-placeholder-val="{{false}}"><span class="tab">{{b.unit}}</span></sc-if></span>
            <sc-if value="{{b.two}}" hint-placeholder-val="{{false}}"><span class="pk-alt"><span class="ind tab">{{b.tasarruf}}</span></span></sc-if>
          </span>
        </button>
      </sc-for></div>
      <!-- 2 Adet seçiliyken: her lambanın modeli (kullanıcı isteği). Paketin dışında, hemen altında (kart içinde kart yok) -->
      <sc-if value="{{ikiliAcik}}" hint-placeholder-val="{{true}}"><div class="ikili" role="group" aria-label="İki lambanın modeli"><sc-for list="{{lambaSec}}" as="l" hint-placeholder-count="2"><div class="lsat"><span>{{l.no}}. lamba</span><span class="seg"><button class="{{l.kCls}}" type="button" onClick="{{l.kPick}}" aria-pressed="{{l.kOn}}" aria-label="{{l.no}}. lamba Kız">Kız</button><button class="{{l.eCls}}" type="button" onClick="{{l.ePick}}" aria-pressed="{{l.eOn}}" aria-label="{{l.no}}. lamba Erkek">Erkek</button></span></div></sc-for></div></sc-if>
    </div>
    <!-- Stok satırı: satıcı elle yazar ve açıp kapatır (Shopify stoğuna bağlı değil). Şimdilik 18. -->
    <p class="stok-satir"><span class="nokta"></span><span>Stokta son <b>18</b> adet</span></p>
    <button class="btn-ana" type="button">""" + ikon('kilit') + """<span>Güvenli Ödeme İle Al</span><span class="fy tab">{{onPrice}}</span></button>
    <p class="btn-not tab">{{onNote}}</p>
    <!-- Canlıda kapıda ödeme uygulamasının formunu açar (ek ürünler ve ₺80 ücret orada) -->
    <button class="btn-kp" type="button">Kapıda Ödeme ile Sipariş Ver</button>
    <p class="btn-not tab">{{kpNote}}</p>
    <ol class="teslim" aria-label="Siparişten teslime">""" + TESLIM + """</ol>
  </section>

  <!-- 6 · Diskler · imza an "Disk tavana açılır": dokununca desen lambanın tepesinden tavana açılır.
       Lamba = seçili modelin arka planı temizlenmiş gerçek fotoğrafı. Yansıma şimdilik disk çizimi; gerçek tavan fotoğrafı gelince değişir. -->
  <section class="tavan koyu gir" id="diskler">
    <h2 class="h2 lit">Bu gecenin masalı</h2>
    <p class="alt-yazi">Diske dokun, tavanda gör.</p>
    <div class="sahne">
      <span class="yer">[gerçek tavan fotoğrafı]</span>
      <sc-for list="{{proj}}" as="p" hint-placeholder-count="2"><span class="{{p.cls}}" aria-hidden="true"><span class="hal"></span><img src="{{p.src}}" alt=""></span></sc-for>
      <img class="lamba-kes" src="{{lambaKes}}" alt="{{lambaAlt}}">
    </div>
    <span class="sr" aria-live="polite">Seçili disk: {{discName}}</span>
    <div class="disk-adlar" aria-hidden="true"><sc-for list="{{discs}}" as="d" hint-placeholder-count="2"><span class="{{d.adCls}}">{{d.n}}</span></sc-for></div>
    <div class="diskler"><sc-for list="{{discs}}" as="d" hint-placeholder-count="11"><button class="{{d.cls}}" type="button" onClick="{{d.pick}}" aria-pressed="{{d.on}}" aria-label="{{d.n}} diskini göster"><img src="{{d.src}}" alt=""></button></sc-for></div>
  </section>

  <!-- 7 · Kapına ne gelir: seçime göre kutu sayısı ve modeller. "12 disk" yazılmaz, "6 + 6 hediye" yazılır. -->
  <section class="bant b-d gir" id="kutu">
    <div class="bas"><h2 class="h2 lit">Kapına ne gelir?</h2><span class="bas-yan">{{kutuSay}}</span></div>
    <div class="kutu-izg">
      <!-- Elde fotoğrafı yalnız Kız modelinde var; seçim yalnız Erkek ise Erkek stüdyo fotoğrafı -->
      <div class="elde"><img src="{{eldeSrc}}" alt="{{eldeAlt}}" style="object-position: {{eldePos}}"><span>{{eldeNot}}</span></div>
      <div>
        <ul class="icerik tab"><li><b>1</b><span>lamba</span></li><li><b>6</b><span>masal diski</span></li><li><b>+6</b><span>hediye disk</span></li><li><b>1</b><span>USB şarj kablosu</span></li></ul>
        <p class="not">{{kutuNot}}</p>
      </div>
    </div>
  </section>

  <!-- 8 · Videolar: canlıda Shopify videoları (kapak = videonun ilk karesi); ekrandayken sessiz, dokununca sesli. Video yoksa bölüm gizlenir. -->
  <section class="bant b-c gir" id="videolar">
    <h2 class="h2 lit">Işık kapanınca ne oluyor?</h2>
    <div class="ray"><sc-for list="{{vids}}" as="v" hint-placeholder-count="4"><button class="vid" type="button" aria-label="{{v.t}}: videoyu oynat"><span class="vid-kap"><img src="{{v.src}}" alt="" style="object-position: {{v.pos}}"><span class="vid-et">[video]</span><span class="oynat">""" + ikon('oynat') + """</span></span><b>{{v.t}}</b><span>{{v.k}}</span></button></sc-for></div>
  </section>

  <!-- 9 · Yorumlar: Loox'tan birebir; puan ve sayı Loox'tan. Müşteri fotoğrafları Loox foto yorumlarından (kullanıcı izni). -->
  <section class="bant b-d gir" id="yorumlar">
    <div class="bas"><h2 class="h2 lit">Aileler ne diyor?</h2><span class="puan-buyuk"><b class="lit tab">{{rating}}</b>""" + yildiz('yd2') + """<span class="bas-yan">{{reviews}} yorum</span></span></div>
    <div class="mfoto"><sc-for list="{{mfoto}}" as="f" hint-placeholder-count="4"><img src="{{f.src}}" alt="{{f.alt}}"></sc-for></div>
    <div class="cipler" role="group" aria-label="Konuya göre süz"><sc-for list="{{topics}}" as="t" hint-placeholder-count="4"><button class="{{t.cls}}" type="button" onClick="{{t.pick}}" aria-pressed="{{t.on}}">{{t.n}}</button></sc-for></div>
    <ul class="yorumlar"><sc-for list="{{revs}}" as="r" hint-placeholder-count="3"><li><q class="lit">{{r.q}}</q><small>{{r.name}}, {{r.tags}} · satın aldı</small></li></sc-for></ul>
    <!-- Canlıda Loox'un tüm yorumlar sayfası (olumsuzlar dahil; mevzuat) -->
    <a class="btn-ince" href="#">{{reviews}} yorumun hepsini oku</a>
    <p class="not">Yorumlar yalnız sipariş verenlerden; hepsi yayımlanır.</p>
  </section>

  <!-- 10 · Bir gece, beş an: her an kendi bandında; akşam kararır (20:45 ve 21:00 gece), sabah açılır -->
  <section aria-labelledby="gece-bas" class="gir2">
    <div class="gece-bas b-c"><h2 class="h2 lit" id="gece-bas">Bir gece, beş an</h2></div>
    <sc-for list="{{moments}}" as="a" hint-placeholder-count="5"><div class="{{a.cls}}"><span class="saat lit tab">{{a.t}}</span><i class="nok" aria-hidden="true"></i><span><b>{{a.title}}</b><p>{{a.text}}</p></span><img src="{{a.src}}" alt="{{a.alt}}" style="object-position: {{a.pos}}"></div></sc-for>
  </section>

  <!-- 11 · 30 gün iade: yasal 14 gün özel avantaj gibi sunulmaz -->
  <section class="bant b-c gir">
    <div class="otuz"><b class="say lit tab">30</b><span><b>gün içinde iade</b><p>Yasal 14 günü 30 güne uzattık. İade kodunu biz göndeririz, kargosu ücretsiz.</p></span></div>
  </section>

  <!-- 12 · SSS -->
  <section class="bant b-d gir">
    <h2 class="h2 lit">Merak edilenler</h2>
    <div class="sss-liste"><sc-for list="{{faq}}" as="f" hint-placeholder-count="6"><details class="sss"><summary>{{f.q}}<span class="ac" aria-hidden="true">""" + ikon('arti') + """</span></summary><p>{{f.a}}</p></details></sc-for></div>
  </section>

  <!-- 13 · Odanın geri kalanı: üstü çizili fiyat yalnız son 10 gün kanıtı olan üründe (canlıda compare_at_price) -->
  <section class="bant b-c gir">
    <div class="bas"><h2 class="h2 lit">Odanın geri kalanı için</h2><span class="bas-yan">{{shopCount}} ürün</span></div>
    <div class="ray"><sc-for list="{{shop}}" as="u" hint-placeholder-count="4"><a class="urun" href="#"><span class="urun-foto"><img src="{{u.src}}" alt="{{u.n}}"></span><b>{{u.n}}</b><span class="tab">{{u.price}}</span><sc-if value="{{u.old}}" hint-placeholder-val="{{true}}"><s class="tab">{{u.old}}</s></sc-if></a></sc-for></div>
  </section>

  <!-- 14 · Alt bilgi -->
  <footer class="bant b-d" style="padding-bottom: 96px">
    <h2 class="h2 lit">İlk geceyi birlikte izleyin.</h2>
    <button class="btn-ana" type="button" style="margin-top: 16px">""" + ikon('kilit') + """<span>Güvenli Ödeme İle Al</span><span class="fy tab">{{onPrice}}</span></button>
    <nav class="yasal" aria-label="Yasal"><a href="#">Mesafeli Satış Sözleşmesi</a><a href="#">KVKK</a><a href="#">İade Politikası</a><a href="#">İletişim</a></nav>
    <p class="kunye">[Ticaret unvanı] · MERSİS [no]<br>[Adres] · [e-posta] · [telefon] · KEP [adres]</p>
    <p class="dev lit">""" + HILAL + """Ayluna</p>
    <p class="kdv">Fiyatlara KDV dahildir. © 2026 Ayluna</p>
  </footer>

  <div class="yapis">
    <span class="yapis-foto" aria-hidden="true"><img src="{{yapisSrc}}" alt=""><sc-if value="{{yapisIki}}" hint-placeholder-val="{{true}}"><img class="iki" src="{{yapisSrc2}}" alt=""></sc-if></span>
    <span class="yapis-yazi tab"><b>{{onPrice}}</b><span>{{adetName}}, kartla · {{cdShort}}</span></span>
    <button class="btn-ana" type="button">Satın al</button>
  </div>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { g: 0, model: 'kiz', adet: 2, l1: null, l2: null, topic: 'Tümü', disc: 0, eski: -1, now: Date.now() }; }
  componentDidMount() { var self = this; this.iv = setInterval(function () { self.setState({ now: Date.now() }); }, 1000); }
  componentWillUnmount() { clearInterval(this.iv); }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    """ + TL_JS + """
    var kiz = S.model === 'kiz';
    // Stüdyo fotoğrafları (model kartı) ve arka planı temizlenmiş kesimler (paket, tavan sahnesi, yapışkan çubuk)
    var KIZ = B + 'e02351b3be4a1c555c5d760d0bbda723', ERKEK = B + '0033dfea6282c5bc479c385213661c00';
    var KES_K = B + 'b823966c39ff35824b4d6e74757646ec', KES_E = B + '20f90021119e4c3bdbc930b283e3635a';
    // Galeri: önce oda sahneleri (tam yükseklik), sonra afişler (kırpılmadan kare, logo bandının altından)
    var G = [
      { id: 'fd0bca1b99cf3837b69fb025cc4e2cd9', n: 'Gece çocuk odası, LunaDream Kız duvara ay ve yıldız yansıtıyor', pos: '50% 60%', oda: true },
      { id: '31751eb35473aca04420825deb3c3ce0', n: 'Gece çocuk odası, LunaDream Erkek (Uzay Kaşifi)', pos: '50% 62%', oda: true },
      { id: 'cbd70711defa628872683fa471fcac61', n: 'Gündüz çocuk odası, komodinde LunaDream Erkek', pos: '50% 70%', oda: true },
      { id: '211acb76d908e8ed6d4f5fcddc987893', n: 'Masalsı gece ışığı', pos: '50% 50%' },
      { id: '652e1893a0ae33a24ee0e3d53edab757', n: 'Müşteri paylaşımı: çocuk odasında LunaDream', pos: '50% 50%' },
      { id: 'a08890007843d79d94bfffc397a3d0ac', n: 'Gece modu', pos: '50% 50%' },
      { id: 'd4efe7e83c74524ece75e962161f7fff', n: 'Deniz altı', pos: '50% 50%' },
      { id: '3ddd8b8b95f040d436d5d0ea350924b8', n: 'Hediye', pos: '50% 50%' },
      { id: '98db755893dbcebe192c69e73ae5afff', n: 'Uzay Kaşifi', pos: '50% 50%' }
    ];
    var gal = G.map(function (g, i) { var on = i === S.g; return { src: B + g.id, n: g.n, alt: on ? g.n : '', gizli: on ? 'false' : 'true', pos: g.pos, top: g.oda ? 0 : 40, h: g.oda ? 430 : 390, on: on ? 'true' : 'false', cls: on ? 'on' : '', kcls: on ? 'kc on' : 'kc', pick: function () { self.setState({ g: i }); } }; });
    var models = [{ id: 'kiz', n: 'Kız', sub: 'Tavşanlı, ninnili', src: KIZ }, { id: 'erkek', n: 'Erkek', sub: 'Robot, ninnili', src: ERKEK }]
      .map(function (m) { var on = S.model === m.id; return { n: m.n, sub: m.sub, src: m.src, on: on ? 'true' : 'false', cls: on ? 'mk on' : 'mk', pick: function () { self.setState({ model: m.id, l1: null, l2: null }); } }; });
    // Paket (canlı sitedeki yapı). ₺1.999 son 10 günde uygulandı (kullanıcı teyidi). 2 Adet'te "2 ayrı almaya göre" tasarruf.
    var P1 = 1699.99, P2 = 2749.99, C1 = 1999;
    var l1 = S.l1 || S.model, l2 = S.l2 || S.model;
    function kes(m) { return m === 'kiz' ? KES_K : KES_E; }
    var lambaSec = [1, 2].map(function (no) {
      var v = no === 1 ? l1 : l2, key = no === 1 ? 'l1' : 'l2';
      // İki lamba aynı modele gelirse model kartı da o modele döner (kart ile seçim çelişmesin)
      function sec(m) { return function () { var n1 = key === 'l1' ? m : l1, n2 = key === 'l2' ? m : l2; if (n1 === n2) self.setState({ model: n1, l1: null, l2: null }); else self.setState({ l1: n1, l2: n2 }); }; }
      return { no: no, kOn: v === 'kiz' ? 'true' : 'false', eOn: v === 'erkek' ? 'true' : 'false', kCls: v === 'kiz' ? 'on' : '', eCls: v === 'erkek' ? 'on' : '', kPick: sec('kiz'), ePick: sec('erkek') };
    });
    var paket = [
      { n: 1, t: '1 Adet', p: TL(P1, true), hediye: '+6 hediye disk', old: TL(C1, true), pctTxt: '%' + Math.round((1 - P1 / C1) * 100), rib: false },
      { n: 2, t: '2 Adet', p: TL(P2, true), hediye: 'Her kutuda +6 hediye', old: '', pctTxt: '', tasarruf: '2 ayrı almaya göre ' + TL(2 * P1 - P2, true) + ' daha az', unit: 'tanesi ' + TL(Math.floor(P2 / 2 * 100) / 100, true), rib: true }
    ].map(function (b) { var on = S.adet === b.n; return { t: b.t, p: b.p, hediye: b.hediye, old: b.old, pctTxt: b.pctTxt, hasOld: !!b.old, tasarruf: b.tasarruf || '', unit: b.unit || '', rib: b.rib, two: b.n === 2,
      src1: b.n === 2 ? kes(l1) : kes(S.model), src2: kes(l2), on: on ? 'true' : 'false', cls: on ? 'pk on' : 'pk', pick: function () { self.setState({ adet: b.n }); } }; });
    var total = S.adet === 2 ? P2 : P1, online = Math.round(total * 0.95 * 100) / 100, kapida = total + 80;
    var adetName = S.adet === 2 ? (l1 !== l2 ? 'Kız + Erkek' : (l1 === 'kiz' ? '2 Kız' : '2 Erkek')) : (kiz ? '1 Kız' : '1 Erkek');
    // Teslim: ertesi iş günü kargoda, +3–7 gün kapında (İstanbul saati)
    var AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
    var now = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kd = new Date(now); do { kd.setDate(kd.getDate() + 1); } while (kd.getDay() === 0 || kd.getDay() === 6);
    var t1 = new Date(kd); t1.setDate(t1.getDate() + 3); var t2 = new Date(kd); t2.setDate(t2.getDate() + 7);
    var teslim = t1.getMonth() === t2.getMonth() ? t1.getDate() + '–' + t2.getDate() + ' ' + AY[t2.getMonth()] : t1.getDate() + ' ' + AY[t1.getMonth()] + '–' + t2.getDate() + ' ' + AY[t2.getMonth()];
    // Bugünkü fiyat sayacı: her gece 23:59'da (İstanbul) sıfırlanır
    function IKI(n) { return n < 10 ? '0' + n : String(n); }
    var ist = new Date(new Date(S.now || Date.now()).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kalan = Math.max(0, new Date(ist.getFullYear(), ist.getMonth(), ist.getDate(), 23, 59, 59, 999).getTime() - ist.getTime());
    var hh = Math.floor(kalan / 3600000), mi = Math.floor(kalan / 60000) % 60, ss = Math.floor(kalan / 1000) % 60;
    // Diskler: mağaza afişinden kesilip Real-ESRGAN ile netleştirildi. Unicorn ve 2025 kutuda yok.
    var DISCS = """ + str([{'n': n, 'id': i} for n, i in DISK_IDS]).replace("'n'", 'n').replace("'id'", 'id') + """;
    var discs = DISCS.map(function (d, i) { var on = i === S.disc; return { n: d.n, src: B + d.id, on: on ? 'true' : 'false', cls: on ? 'dk on' : 'dk', adCls: on ? 'on' : '',
      pick: function () { if (i !== S.disc) self.setState({ disc: i, eski: S.disc }); } }; });
    var proj = DISCS.map(function (d, i) { return { src: B + d.id, cls: i === S.disc ? (S.eski === -1 ? 'yans on ilk' : 'yans on') : (i === S.eski ? 'yans eski' : 'yans') }; });
    var tumErkek = S.adet === 2 ? (l1 === 'erkek' && l2 === 'erkek') : !kiz;
    var KR = ['Kız', 'Erkek'];
    var kutuSay = S.adet === 2 ? (l1 === l2 ? '2 kutu: 2 ' + (l1 === 'kiz' ? KR[0] : KR[1]) : '2 kutu: Kız + Erkek') : '1 kutu: ' + (kiz ? KR[0] : KR[1]);
    var vids = [
      { t: 'Işık kapanınca tavanda masal', k: 'Kız modeli', src: B + '5ce96d9e6f38e8d571ac1cb9e529ec22', pos: '50% 40%' },
      { t: 'Bir müşterimizin akşamı', k: 'Müşteri videosu', src: B + '7ad3cbbe71680f4ed3027dbd056e391f', pos: '50% 40%' },
      { t: 'Uzay Kaşifi tavanda', k: 'Erkek modeli', src: B + 'b2c8d9b92ad3541b532e3aa108a74735', pos: '50% 45%' },
      { t: 'Disk nasıl takılır', k: 'Kurulum', src: B + '5b284c77c252b08a2974bde8e43de126', pos: '50% 50%' }
    ];
    var mfoto = [['4323cd781a0d687b528b3059505be48c', 'LunaDream’e sarılan küçük kız'], ['7ad3cbbe71680f4ed3027dbd056e391f', 'Çocuk odasında yanan LunaDream'], ['f060b12bc3353fae64eedf62798c5711', 'Duvara yansıyan deniz deseni'], ['ec3c3976bbe8f18e5660f4a4c355ebf7', 'Karanlıkta yanan LunaDream']]
      .map(function (f) { return { src: B + f[0], alt: 'Müşteri fotoğrafı: ' + f[1] }; });
    var REV = [
      { tags: ['Uyku'], name: 'Burak G.', q: 'Çocuğum çalıştırmadan uyumuyor, uykuya hemen dalıyor.' },
      { tags: ['Hediye'], name: 'Handan B.', q: 'Torunum filmlerini kendisi seçti ve onunla uyumaya başladı.' },
      { tags: ['Kalite'], name: 'Sevcan Z.', q: '2 tane aldık, gayet sağlam geldi. Paketlenmesi de güzeldi.' },
      { tags: ['Hediye', 'Kalite'], name: 'Abdülkerim T.', q: 'Reklamında nasıl ise aynısı, hatta daha iyisi. Çocuklar için mükemmel bir hediye.' },
      { tags: ['Kalite'], name: 'Mehmet C.', q: 'Anlatıldığı ve gösterildiği gibi çıktı. Bu kadar iyi olmasını beklemiyordum.' }
    ];
    var topics = ['Tümü', 'Uyku', 'Hediye', 'Kalite'].map(function (t) { var on = S.topic === t; return { n: t, cls: on ? 'cip on' : 'cip', on: on ? 'true' : 'false', pick: function () { self.setState({ topic: t }); } }; });
    var revs = REV.filter(function (r) { return S.topic === 'Tümü' || r.tags.indexOf(S.topic) > -1; }).map(function (r) { return { q: r.q, name: r.name, tags: r.tags.join(', ') }; });
    // Bir gece: akşam kararır (20:45, 21:00 gece bandı), sabah açılır. Erkek modelde 20:45 değişir.
    var M = [
      { t: '20:00', b: 'b-c', title: 'Odayı hazırla', text: 'Perdeyi çek, lambayı komodine koy.', id: '8b1f621be2cb3b6133b7b78bc14e1963', alt: 'Elde tutulan, yanan LunaDream', pos: '50% 30%' },
      { t: '20:30', b: 'b-d', title: 'Masalı seç', text: 'Bu gecenin diskini çocuğun seçsin.', id: '5b284c77c252b08a2974bde8e43de126', alt: 'Kubbesi açık LunaDream ve diskler', pos: '50% 40%' },
      kiz ? { t: '20:45', b: 'b-g koyu', title: 'Birlikte dinleyin', text: 'En sevdiği ninniyi telefondan aç.', id: '64229e39b184f68336dc1c9b99e8e850', alt: 'Tavşanlı LunaDream', pos: '50% 45%' }
          : { t: '20:45', b: 'b-g koyu', title: 'Uzay yolculuğu', text: 'Işığı kapat, tavanda uzay başlasın.', id: 'b2c8d9b92ad3541b532e3aa108a74735', alt: 'Uzay Kaşifi LunaDream', pos: '50% 45%' },
      { t: '21:00', b: 'b-g koyu', title: 'Gözler kapanır', text: 'Masal tavanda, sen yanında.', id: kiz ? '3d214a1ba100aaf3d85bb18a27325237' : '49da18af3a87a3c97bb59cb9dbe8817f', alt: 'Gece yatak başında yanan LunaDream, duvarda yıldızlar', pos: '50% 55%' },
      { t: '07:30', b: 'b-d', title: 'Sabah şarja', text: 'Gündüz şarja tak.', id: kiz ? '2288b7fbcc230bd9d47e25ef6550ce78' : 'cbd70711defa628872683fa471fcac61', alt: 'Gündüz komodinde LunaDream', pos: '50% 72%' }
    ];
    var moments = M.map(function (a, i) { return { t: a.t, title: a.title, text: a.text, src: B + a.id, alt: a.alt, pos: a.pos, cls: 'an ' + a.b + (i === 0 ? ' ilk' : '') + (i === M.length - 1 ? ' son' : '') }; });
    var PR = [
      { n: 'Yıldız Işığı Nemlendirici', p: 849.99, c: 1099, id: 'f3f3e14eee224ef5534b9b897030ff58' },
      { n: 'Ayluna Galaksi Night Projektör', p: 2199, c: 2999, id: '2b381f338377f23e32074d6dbb452587' },
      { n: 'Astronot Oda Nemlendirici', p: 799, c: 0, id: '738c2e608984aaa9d11f9559738f36c2' },
      { n: 'Ayluna Çocuk Gece Feneri', p: 1599, c: 0, id: '1b84557bbf4571b164475234e4266b82' },
      { n: 'Galaxy USB Projektör', p: 1599, c: 1999, id: '7055567d8e0fcaae38df5a577f509656' },
      { n: 'Galaksi Ambiyans Işığı', p: 1499, c: 2898, id: 'abe882f12bc58627f99b18a6e9aae0df' },
      { n: 'Aroma Terapi Nemlendirici', p: 1499, c: 1999, id: '1942d96f59772d783f5fca6259071786' },
      { n: 'Eğitici Akıllı Çizim Tahtası', p: 1199, c: 1999, id: 'e3cc38b54acdddf55b1658d706382e82' },
      { n: 'Ayluna AyFeneri', p: 1649.99, c: 2499, id: '94179bf5fda7b68f949842832e376fe6' },
      { n: 'Sunset Lamba', p: 699, c: 999, id: '9bd9f9b4f1a38c4163064ce1c6117bbf' },
      { n: 'Dokunmatik Ambiyans Lamba', p: 1299.99, c: 0, id: '7ada3d5cdd7a8fa792622a30dc3f761b' },
      { n: 'Ayluna Kum Saati Lamba', p: 799, c: 999, id: '408afb48de0f2b2be66d095849fedda8' },
      { n: 'Ayluna Retro Mini Pikap', p: 1499, c: 1999.99, id: '233784939af80bdc12f69eca3b2e25b4' }
    ];
    var shop = PR.map(function (x) { return { n: x.n, src: B + x.id, price: TL(x.p, true), old: x.c > x.p ? TL(x.c, true) : '' }; });
    var faq = [
      { q: 'Ninni hangi modelde var?', a: 'İki modelde de var. İkisi de telefona Bluetooth ile bağlanır; çalan ninni lambadan gelir.' },
      { q: 'Kaç yaş için uygun?', a: 'Her yaş için uygun.' },
      { q: 'Kargo ne zaman gelir?', a: 'Siparişin 1 iş gününde kargoya verilir, Türkiye geneline 3–7 günde ulaşır.' },
      { q: 'Kartla mı, kapıda mı ödeyeyim?', a: 'Tüm kredi ve banka kartları geçer; kartla öderken %5 indirim alırsın, kart bilgin bize gelmez. Kapıda ödemede ₺80 kapıda ödeme ücreti eklenir; ürün geldiğinde nakit ya da kartla ödersin.' },
      { q: 'Beğenmezsem iade edebilir miyim?', a: '30 gün içinde iade edebilirsin. Sana iade kodunu göndeririz, kargosu ücretsizdir. İlk 14 gün yasal cayma hakkındır.' },
      { q: 'Işık çocuğu rahatsız eder mi?', a: 'Sıcak tonlu, yumuşak bir ışığı var. 3 parlaklık ayarından birini seçebilirsin.' }
    ];
    return {
      cdShort: IKI(hh) + ':' + IKI(mi) + ':' + IKI(ss), cdAria: 'Bugünkü fiyat garantisinin bitmesine ' + hh + ' saat ' + mi + ' dakika',
      gal: gal, gNo: S.g + 1, gCount: G.length, gPrev: function () { self.setState({ g: (S.g + G.length - 1) % G.length }); }, gNext: function () { self.setState({ g: (S.g + 1) % G.length }); },
      // Puan ve sayı canlıda Loox'tan (teyit bekliyor); yıldız dolgusu 4,7/5
      rating: '4,7', reviews: 62, starW: Math.round(84 * 4.7 / 5 * 10) / 10,
      p1: TL(P1, true), c1: TL(C1, true), pct: Math.round((1 - P1 / C1) * 100),
      models: models, paket: paket, lambaSec: lambaSec, ikiliAcik: S.adet === 2, adetName: adetName,
      onPrice: TL(online, true), onNote: 'Kartla %5 indirimli, ' + TL(kapida - online, true) + ' daha az', kpNote: '+₺80 kapıda ödeme ücreti, ' + TL(kapida, true),
      kargo: kd.getDate() + ' ' + AY[kd.getMonth()], teslim: teslim,
      discs: discs, proj: proj, discName: DISCS[S.disc].n, lambaKes: kiz ? KES_K : KES_E, lambaAlt: kiz ? 'LunaDream Kız' : 'LunaDream Erkek',
      kutuSay: kutuSay, kutuNot: S.adet === 2 ? 'Her kutuda bunların hepsi var.' : 'Hepsi tek kutuda.',
      eldeSrc: tumErkek ? ERKEK : B + '8f8d1462c27c62b0bbd3066d72c92025', eldeAlt: tumErkek ? 'LunaDream Erkek (Uzay Kaşifi)' : 'Elde tutulan LunaDream Kız', eldeNot: tumErkek ? 'Erkek modeli' : 'Kız modeli, elde', eldePos: tumErkek ? '50% 62%' : '40% 50%',
      vids: vids, mfoto: mfoto, topics: topics, revs: revs, moments: moments, shop: shop, shopCount: PR.length, faq: faq,
      yapisSrc: S.adet === 2 ? kes(l1) : kes(S.model), yapisSrc2: kes(l2), yapisIki: S.adet === 2 && l1 !== l2
    };
  }
}"""

HEAD = """<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<title>LunaDream · D Oda ve Tavan</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,500&amp;family=Atkinson+Hyperlegible+Next:wght@400;700&amp;display=swap">
<style>
body{margin:0;background:#FFF8F0}
a{color:#1A2142}
""" + CSS + """</style>
</helmet>
"""
TAIL = """</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":390,"height":%d}}'>
%s
</script>
</body>
</html>
"""
open(OUT, 'w', encoding='utf-8').write(HEAD + HTML + TAIL % (int(os.environ.get('D_H', 6419)), JS))
print('yazıldı:', os.path.abspath(OUT))
