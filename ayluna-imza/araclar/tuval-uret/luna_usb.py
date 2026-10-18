# Galaxy USB Projektör · ürün sayfası, LunaDream E'nin (nihai tasarım, 18 Eki) diliyle. Çalıştır: python3 luna_usb.py
# Kullanıcı: "Nihai tasarımımız bu olacak; şimdi USB projektör için de ona uygun bir tasarım yapalım."
# E'nin CSS'i, logo, ay evresi, teslim çizgisi ve mühür luna_e.py'den gelir; sayfa iskeleti aynı sırayla kurulur:
# sayaç şeridi → sahne galeri → ad + puan → fiyat düşüşü + Stokta → Sihirli özellikler → paket (satır kart) → stok, iki buton,
# kargo döngüsü → Temalar (E'deki Diskler gibi tavan önizlemesi) → Üç adımda kur → Odası böyle görünecek (kaydırmalı) →
# Yorumlar (Loox yer tutucusu) → 30 gün iade → SSS → Diğer ürünler → alt bilgi → yapışkan çubuk.
# Bilgi kaynağı yalnız mağazanın kendi ürün afişleri: 12 tema diski, USB tak & çalıştır, 360° döner başlık,
# başlık 4 cm, toplam boy 23,5 cm, temalar Galaksi / Gezegenler / Ay & Uzay / Nebula. Fiyat ₺1.599 / ₺1.999 (Shopify).
# Kullanılmayanlar (teyitsiz ya da yanlış, canlı sayfada var): 5K, 6/7 katmanlı lens çelişkisi, 130 m², sağlık iddiaları
# (kortizol, anksiyete, uyku kalitesi), "4,7 · 2467 yorum" (gerçek Loox: 2,0 · 7), "90 gün iade" (gerçeği 30),
# afişteki "Elif K." yorum kartı, Bluetooth ve şarj cümleleri (başka ürünün SSS'sinden).
# Görseller: mağaza afişlerinin yazısız bölgelerinden kesildi (canvas/usb/), ürün kesimi rembg ile (ürün piksellerine dokunulmadı).
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL, TL_JS
import luna_e as E
OUT = os.path.join(HERE, '..', '..', 'canvas', 'GalaxyUSB.dc.html')
ay = E.ay
B = '/_blob/'
IMG = dict(oda='7d5f80214a0664a51946b0ece044e8cb', urun='192e0198aa722e532541f454e8278561', bas='7e1339aefa8d185cd41f6c37b16853c5',
           cocuk='f2da40fb1654492417c640086532631f', tavan='a251dbf8b17b830a7802c71491fbfa11', galaksi='3dffc14be651a2ddd70ce994d1e0c177',
           gezegen='9887bb4d17bd3e758da8106a87e89c23', ayuzay='9384df8d05b0859d4af1e833f678e737', nebula='5c507bd7b87e2a43d28acc49e09cc19d',
           kesim='5782766948fef68b7273c061529d6324')
AYR = '<svg class="ayr" viewBox="0 0 24 24" aria-hidden="true"><circle class="h" cx="12" cy="12" r="9"></circle><circle class="d" cx="12" cy="12" r="5"></circle></svg>'
OK = '<svg class="ok-ik" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"></path></svg>'


def evre(f, cls='evre'):
    return '<svg class="%s" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="%s"></path></svg>' % (cls, ay(f))


CSS = E.CSS + r"""
/* ——— Galaxy USB'ye özgü (E dilinde) ——— */
/* Sihirli özelliklerin canlı göstergeleri: USB ışığı nefes alır, döner başlık yavaş döner, cetvel boyu gösterir */
@keyframes usb-nefes{0%,100%{opacity:.35}50%{opacity:1}}
.usb-isik{display:flex;align-items:center;gap:5px}
.usb-isik i{display:block;width:16px;height:7px;border-radius:4px;background:#F2A65A;animation:usb-nefes 2.6s ease-in-out infinite}
.usb-isik i:nth-child(2){animation-delay:-.9s}.usb-isik i:nth-child(3){animation-delay:-1.8s}
@keyframes don{to{transform:rotate(360deg)}}
.don{width:34px;height:34px;animation:don 9s linear infinite}
.don circle{fill:none;stroke:#E3D8C7;stroke-width:2}.don path{fill:none;stroke:#F2A65A;stroke-width:2.4;stroke-linecap:round}
.cetvel{position:relative;width:64px;height:22px;border:1.6px solid #1A2142;border-radius:5px;background:repeating-linear-gradient(90deg,#1A2142 0 1.4px,transparent 1.4px 8px) 4px 0/56px 7px no-repeat}
.cetvel::after{content:"";position:absolute;left:4px;bottom:4px;height:4px;width:46px;border-radius:2px;background:#F2A65A;transform-origin:0 50%;animation:cetvel 4s cubic-bezier(.2,.7,.2,1) infinite}
@keyframes cetvel{0%{transform:scaleX(.1);opacity:0}15%{opacity:1}60%,85%{transform:scaleX(1);opacity:1}100%{transform:scaleX(1);opacity:0}}
@media (prefers-reduced-motion:reduce){.usb-isik i,.don,.cetvel::after{animation:none}}
/* Temalar: E'deki tavan önizlemesi; tema çipi yuvarlak küçük görsel + ad */
.tema-cip{display:inline-flex;align-items:center;gap:8px;flex:none;min-height:48px;padding:0 14px 0 4px;border:1.5px solid rgba(255,253,249,.22);border-radius:999px;background:transparent;color:#EDE5D8;font:inherit;font-size:14px;font-weight:600;cursor:pointer}
.tema-cip img{width:38px;height:38px;border-radius:50%;object-fit:cover}
.tema-cip.on{border-color:#FFFDF9;color:#FFFDF9;box-shadow:inset 0 0 0 .5px #FFFDF9}
/* Üç adımda kur: ay evresiyle dolan adımlar (Bölümler önerisi 2'nin açık hâli) */
.kur{position:relative;list-style:none;margin:16px 0 0;padding:0}
.kur::before{content:"";position:absolute;left:15px;top:22px;bottom:22px;border-left:1.5px dashed #D6CAB6}
.kur li{position:relative;display:grid;grid-template-columns:32px minmax(0,1fr);gap:14px;align-items:start;padding:9px 0}
.kur .evre{width:32px;height:32px;background:#F6F1E9;border-radius:50%}
.kur .evre circle{fill:#F6F1E9;stroke:#1A2142;stroke-width:1.4}.kur .evre path{fill:#F2A65A}
.kur b{display:block;font-size:16px;line-height:1.3}
.kur span{display:block;margin-top:2px;font-size:14px;color:#5C6078}
.kur-yardim{display:flex;align-items:center;gap:10px;margin-top:12px;padding:12px 14px;border-radius:16px;background:#FFFDF9;box-shadow:inset 0 0 0 1px #E3D8C7;font-size:14px;color:#1A2142}
.kur-yardim svg{width:22px;height:22px;flex:none;fill:none;stroke:#1A2142;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
/* Yorum yer tutucusu (gerçek Loox verisi gelince kartlar E'deki gibi) */
.yer-tutucu{margin:14px 16px 0;padding:18px 16px;border:1.5px dashed #D6CAB6;border-radius:20px;font-size:14px;color:#5C6078;text-align:center}
"""

TEMALAR = [('Galaksi', 'galaksi', 'galaksi'), ('Gezegenler', 'gezegen', 'gezegen'), ('Ay ve uzay', 'ayuzay', 'ayuzay'), ('Nebula', 'nebula', 'nebula')]

HTML = """<div class="pg" style="padding-bottom: 0">
  <!-- Üst şerit: E ile aynı (bugünkü fiyat garantisi, 23:59'da sıfırlanır) -->
  <div class="duyuru" role="timer" aria-label="{{cdAria}}"><span>Bugünkü fiyat garantisi</span><svg class="sayac-ay" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="{{cdAy}}"></path></svg><b>{{cdShort}}</b></div>
  <!-- Sahne: mağaza afişlerinin yazısız bölgeleri (temsilî); canlıda Shopify ürün medyası -->
  <section class="sahne" aria-label="Galaxy USB fotoğrafları">
    <header><button class="ikon" aria-label="Menü"><svg class="ico" viewBox="0 0 24 24"><path d="M4 8h16M4 16h11"></path></svg></button><span style="display: flex; align-items: center; gap: 6px">""" + E.LOGO + """<span class="ser" style="font-size: 18px">Ayluna</span></span><button class="ikon" aria-label="Sepet"><svg class="ico" viewBox="0 0 24 24"><path d="M6 8h12l-1 12H7z"></path><path d="M9 8a3 3 0 0 1 6 0"></path></svg></button></header>
    <div class="kare-foto"><sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><img src="{{f.src}}" alt="{{f.n}}" style="opacity: {{f.op}}; object-position: {{f.pos}}; top: 0px; height: 446px"></sc-for><button class="gec" style="left: 0" onClick="{{gPrev}}" aria-label="Önceki fotoğraf"></button><button class="gec" style="right: 0" onClick="{{gNext}}" aria-label="Sonraki fotoğraf"></button></div>
    <!-- Süzülen tema diskleri: fotoğrafın kenarlarında, ürünü kapatmaz -->
    <span class="yuzen" aria-hidden="true" style="left: -16px; top: 330px; width: 46px; height: 46px; --r: -12deg; animation-delay: 0s"><img src=\"""" + B + IMG['gezegen'] + """\" alt=""></span>
    <span class="yuzen" aria-hidden="true" style="left: 364px; top: 340px; width: 38px; height: 38px; --r: 8deg; animation-delay: -2.3s"><img src=\"""" + B + IMG['nebula'] + """\" alt=""></span>
    <div class="seritler">
      <div class="noscroll" style="display: flex; gap: 6px; flex: 1; min-width: 0; overflow-x: auto; padding: 2px">
        <sc-for list="{{gal}}" as="f" hint-placeholder-count="4"><button class="{{f.cls}}" onClick="{{f.pick}}" aria-label="{{f.n}}" aria-pressed="{{f.on}}"><img src="{{f.src}}" alt=""></button></sc-for>
      </div>
      <span class="sira">{{gNo}}/{{gCount}}</span>
    </div>
  </section>

  <section class="px levha" id="siparis">
    <!-- Ad ve puan aynı satırda (E kuralı). Puan ve sayı Loox'tan; bu ürünün Loox verisi 2,0 · 7 yorum (18 Eki).
         Canlı sayfadaki "4,7 · 2467" bu ürüne ait değil, kullanılmaz. Karar kullanıcının: gerçek puan ya da puansız. -->
    <div class="ad-satir">
      <h1 class="dev">Galaxy USB<span>.</span></h1>
      <a class="puan" href="#yorumlar" aria-label="Puan ve yorum sayısı Loox'tan gelecek"><span class="puan-ust">""" + E.STAR + """<b>[puan]</b></span><span class="puan-alt">[N] yorum</span></a>
    </div>
    <p class="fiyat-satir" aria-label="{{p1}}, önceki fiyat {{c1}}, %{{pct}} indirim, stokta"><span class="fy-ilk" aria-hidden="true">{{c1}}</span><b class="fy-yeni" aria-hidden="true">{{p1}}</b><s class="fy-eski" aria-hidden="true">{{c1}}</s><span class="indirim fy-rozet" aria-hidden="true">%{{pct}} indirim</span><span class="stok" aria-hidden="true">Stokta</span></p>

    <p class="ust-yazi" style="margin-top: 22px; margin-bottom: 0">Sihirli özellikler</p>
    <div class="sih">
      <div class="oz"><span class="oz-ust" aria-hidden="true"><span class="ik"><svg viewBox="0 0 24 24"><path d="M9 3h6v5H9z"></path><path d="M7 8h10v5a5 5 0 0 1-10 0z"></path><path d="M12 18v3"></path></svg></span><span class="usb-isik"><i></i><i></i><i></i></span></span><b>USB tak, çalıştır</b><span class="t">Bilgisayar, powerbank ya da adaptör.</span></div>
      <a class="oz" href="#temalar"><span class="oz-ust" aria-hidden="true"><span class="ik"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="2.5"></circle><path d="M12 3a9 9 0 0 1 9 9"></path></svg></span><span class="yelpaze"><img src=\"""" + B + IMG['galaksi'] + """\" alt=""><img src=\"""" + B + IMG['gezegen'] + """\" alt=""><img src=\"""" + B + IMG['nebula'] + """\" alt=""></span></span><b>12 tema diski</b><span class="t">Galaksi, gezegen, ay, nebula. <u>Temaları gör</u></span></a>
      <div class="oz"><span class="oz-ust" aria-hidden="true"><span class="ik"><svg viewBox="0 0 24 24"><path d="M20 12a8 8 0 1 1-2.3-5.6"></path><path d="M20 4v4h-4"></path></svg></span><svg class="don" viewBox="0 0 34 34"><circle cx="17" cy="17" r="13"></circle><path d="M17 4a13 13 0 0 1 13 13"></path></svg></span><b>360° döner başlık</b><span class="t">Tavana, duvara, köşeye çevir.</span></div>
      <div class="oz"><span class="oz-ust" aria-hidden="true"><span class="ik"><svg viewBox="0 0 24 24"><rect x="3" y="8" width="18" height="8" rx="1.5"></rect><path d="M7 8v3M11 8v4M15 8v3M19 8v4"></path></svg></span><span class="cetvel"></span></span><b>Avuç içi kadar</b><span class="t">Başlık 4 cm, boyu 23,5 cm.</span></div>
    </div>

    <!-- Paket: E'nin satır kartı. Mağazada tek varyant; 2'li fiyat tanımlı değil (kullanıcı belirleyecek). -->
    <div class="etiket" style="margin-top: 24px"><span>Paket</span></div>
    <div class="pk-liste">
      <sc-for list="{{paket}}" as="b" hint-placeholder-count="2">
        <div class="{{b.cls}}">
          <sc-if value="{{b.rib}}" hint-placeholder-val="{{false}}"><span class="kurdele">En avantajlı</span></sc-if>
          <button class="sat" onClick="{{b.pick}}" aria-pressed="{{b.on}}"><span class="{{b.tlCls}}"><img src=\"""" + B + IMG['kesim'] + """\" alt=""><sc-if value="{{b.two}}" hint-placeholder-val="{{false}}"><img src=\"""" + B + IMG['kesim'] + """\" alt=""></sc-if></span><span class="sat-orta"><span class="ad">{{b.t}}</span><span class="alt">{{b.sub}}</span></span><span class="sat-sag"><span class="fiyat">{{b.p}}</span><span class="eski"><sc-if value="{{b.hasOld}}" hint-placeholder-val="{{true}}"><s>{{b.old}}</s></sc-if>{{b.unit}}</span></span>""" + AYR + """</button>
        </div>
      </sc-for>
    </div>
    <p class="hediye-sat"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d='""" + ay(.22) + """'></path></svg>Kutuda 12 tema diski</p>
    <ul class="canli">
      <li><i style="background: #A05A1C"></i><span>Stokta son <b>[N]</b> adet</span></li>
    </ul>
    <button class="btn-on" type="button">{{onLabel}}</button>
    <button class="btn-kp" type="button">Kapıda Ödeme ile Sipariş Ver</button>
    <ol class="{{yolCls}}" aria-label="Siparişten teslime"><span class="yol-akis" aria-hidden="true"><i></i><i></i><span class="yol-paket"></span></span>""" + E.YOL + """</ol>
  </section>

  <!-- Temalar: E'deki Diskler gibi tavan önizlemesi. Görseller mağaza afişindeki tema karelerinden; kutuda 12 disk, burada 4'ü. -->
  <section class="gece gir" id="temalar">
    <div class="px"><h2 class="h2" style="color: #FFFDF9">Kutuda 12 tema<span class="n">.</span></h2><p style="margin: 8px 0 0; font-size: 14px; color: #B9BED6">Temayı seç, tavanda nasıl durduğunu gör.</p></div>
    <div class="px" style="margin-top: 16px"><div class="tavan">
      <sc-for list="{{proj}}" as="p" hint-placeholder-count="2"><span class="{{p.cls}}" aria-hidden="true"><img src="{{p.src}}" alt=""></span></sc-for>
      <span style="position: absolute; left: 12px; top: 12px; font-size: 12px; font-weight: 600; color: #FFFDF9; background: rgba(12,16,39,.6); padding: 3px 9px; border-radius: 999px">[gerçek tavan fotoğrafı]</span>
      <span style="position: absolute; left: 14px; bottom: 14px; display: flex; flex-direction: column; line-height: 1.2; color: #FFFDF9"><span style="font-size: 12px; color: #B9BED6">Tema</span><b class="ser" style="font-size: 18px; font-weight: 400">{{temaAd}}</b></span>
    </div></div>
    <div class="noscroll" style="display: flex; gap: 8px; overflow-x: auto; padding: 14px 16px 0">
      <sc-for list="{{temalar}}" as="t" hint-placeholder-count="4"><button class="{{t.cls}}" onClick="{{t.pick}}" aria-pressed="{{t.on}}"><img src="{{t.src}}" alt="">{{t.n}}</button></sc-for>
    </div>
    <p class="px" style="margin: 12px 0 0; font-size: 13px; color: #B9BED6">Kutuda 12 tema diski var; burada dördü.</p>
  </section>

  <!-- Üç adımda kur (gerçek yorumlardaki şikâyetlere karşı: bulanık görüntü, zor dönen odak, sıkışan disk). Adımlar teyit edilmeli. -->
  <section class="px bolum gir" id="kurulum">
    <h2 class="h2">Üç adımda<br>tavanda galaksi<span class="n">.</span></h2>
    <ol class="kur">
      <li>""" + evre(.22) + """<span><b>USB'ye tak</b><span>Bilgisayar, powerbank ya da USB adaptörü yeter.</span></span></li>
      <li>""" + evre(.5) + """<span><b>Diski yerleştir</b><span>Temayı başlığa tak, başlığı tavana çevir.</span></span></li>
      <li>""" + evre(1) + """<span><b>Yavaşça netle</b><span>Odağı yavaş çevir. Oda ne kadar karanlıksa görüntü o kadar net.</span></span></li>
    </ol>
    <p class="kur-yardim"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"></path></svg><span>Takılırsan zorlama; WhatsApp'tan yaz, görüntülü gösterelim.</span></p>
  </section>

  <!-- Odası böyle görünecek: E'deki kaydırmalı posterler. Görseller mağaza afişlerinin yazısız bölgeleri, temsilî. -->
  <section class="bolum gir" id="odalar">
    <div class="px"><h2 class="h2">Odası böyle<br>görünecek<span class="n">.</span></h2></div>
    <div class="b-serit noscroll" onScroll="{{odaKay}}">
      <div class="poster"><div class="p-foto"><img src=\"""" + B + IMG['cocuk'] + """\" alt="Yatağında tavana bakan çocuk ve oyuncak ayı" style="object-position: 30% 50%"><span class="p-cip">""" + evre(.22) + """Çocuk odası</span></div><div class="p-alt"><p class="p-bas">Tavanda galaksi<span>.</span></p><p class="p-yazi">Yatak başına koy, başlığı tavana çevir.</p><button class="p-sec" type="button" onClick="{{alaGit}}">Hemen al""" + OK + """</button></div></div>
      <div class="poster"><div class="p-foto"><img src=\"""" + B + IMG['oda'] + """\" alt="Komodinde Galaxy USB projektör, USB ucu ve esnek boyun" style="object-position: 40% 45%"><span class="p-cip">""" + evre(.78) + """Komodin, masa, raf</span></div><div class="p-alt"><p class="p-bas">Bir USB girişi yeter<span>.</span></p><p class="p-yazi">Bilgisayara, powerbank'e ya da adaptöre tak.</p><button class="p-sec" type="button" onClick="{{alaGit}}">Hemen al""" + OK + """</button></div></div>
      <span aria-hidden="true" style="flex: 0 0 6px"></span>
    </div>
    <div class="b-say" aria-hidden="true"><i class="{{nokta0}}"></i><i class="{{nokta1}}"></i></div>
    <p class="temsil">Görseller temsilîdir; görüntü odanın karanlığına ve temaya göre değişir.</p>
  </section>

  <!-- Yorumlar: yalnız bu ürünün Loox yorumları (başka ürünün yorumu ya da afişteki kart yok). Gelince kartlar E'deki gibi. -->
  <section id="yorumlar" class="bolum gir">
    <div class="px"><h2 class="h2">Aileler<br>ne diyor<span class="n">?</span></h2></div>
    <p class="yer-tutucu">[Loox: bu ürünün gerçek yorumları, puanı ve sayısı burada]</p>
  </section>

  <section class="px bolum gir">
    <div class="otuz"><span class="muhur-kap">""" + E.muhur() + """<span class="muhur-say"><b class="say">30</b><span>gün</span></span></span><span style="display: flex; flex-direction: column; gap: 2px"><b style="font-size: 16px; line-height: 1.2">Beğenmezsen iade et</b><span style="font-size: 14px; color: #5C6078">Yasal 14 günü 30 güne uzattık. İade kargosu ücretsiz.</span></span></div>
  </section>

  <section class="px bolum gir">
    <h2 class="h2">Merak edilenler<span class="n">.</span></h2>
    <div style="margin-top: 14px; border-top: 1.5px solid #E3D8C7">
      <sc-for list="{{faq}}" as="f" hint-placeholder-count="6"><details class="sss"><summary>{{f.q}}<span class="arti" aria-hidden="true">+</span></summary><p style="margin: 0 0 16px; font-size: 14px; color: #5C6078">{{f.a}}</p></details></sc-for>
    </div>
  </section>

  <section class="bolum gir">
    <div class="px" style="display: flex; align-items: flex-end; justify-content: space-between"><h2 class="h2">Odanın geri<br>kalanı için<span class="n">.</span></h2><span style="font-size: 13px; color: #5C6078">{{shopCount}} ürün</span></div>
    <div class="noscroll" style="display: flex; gap: 10px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-left: 16px; padding: 14px 16px 4px">
      <sc-for list="{{shop}}" as="u" hint-placeholder-count="4">
        <a class="kart" href="#"><span style="position: relative; aspect-ratio: 1 / 1; background: #F1E8DA; overflow: hidden"><img src="{{u.src}}" alt="{{u.n}}" style="width: 100%; height: 100%; object-fit: cover; display: block"><sc-if value="{{u.pct}}" hint-placeholder-val="{{true}}"><span style="position: absolute; left: 8px; top: 8px; font-size: 12px; font-weight: 700; background: #FFFDF9; color: #A05A1C; padding: 2px 8px; border-radius: 999px">{{u.pct}}</span></sc-if></span><span style="padding: 10px 12px 12px; display: flex; flex-direction: column; gap: 4px"><b style="font-size: 14px; font-weight: 600; line-height: 1.25; min-height: 35px">{{u.n}}</b><span style="display: flex; align-items: baseline; gap: 6px; font-variant-numeric: tabular-nums"><b style="font-size: 14px">{{u.price}}</b><s style="font-size: 12px; color: #5C6078">{{u.old}}</s></span></span></a>
      </sc-for>
    </div>
  </section>

  <footer class="alt-bilgi">
    <div class="px">
      <h2 class="h2" style="color: #FFFDF9">Bu gece tavanda<br>galaksi olsun<span class="n">.</span></h2>
      <button class="btn-on" type="button" style="margin-top: 16px; box-shadow: 0 3px 0 rgba(12,16,39,.6)">{{onLabel}}</button>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0 16px; margin-top: 24px; font-size: 14px"><a href="#">Mesafeli Satış Sözleşmesi</a><a href="#">KVKK</a><a href="#">İade Politikası</a><a href="#">İletişim</a></div>
      <p style="margin: 14px 0 0; font-size: 13px; line-height: 1.5">[Ticaret unvanı] · MERSİS [no]<br>[Adres] · [e-posta] · [telefon] · KEP [adres]</p>
      <div aria-label="Ayluna" style="margin-top: 22px; display: flex; align-items: center; gap: 12px; color: #FFFDF9">""" + E.isaret(48) + """<span class="ser" aria-hidden="true" style="font-size: 56px; line-height: .8; letter-spacing: -.045em">Ayluna</span></div>
      <p style="margin: 14px 0 0; padding-top: 14px; border-top: 1px solid rgba(255,253,249,.12); font-size: 12px; color: #B9BED6">Fiyatlara KDV dahildir. © 2026 Ayluna</p>
    </div>
  </footer>

  <div class="yapis">
    <span style="position: relative; flex: none; width: 46px; height: 46px; border-radius: 12px; overflow: hidden; background: #2A3260"><img class="kesim" src=\"""" + B + IMG['kesim'] + """\" alt="" style="height: 38px; bottom: 4px"></span>
    <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; line-height: 1.15; color: #FFFDF9; font-variant-numeric: tabular-nums"><b style="font-size: 16px">{{onPrice}}</b><span style="font-size: 12px; color: #B9BED6">{{adetName}} · kartla</span><span style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #B9BED6"><svg class="sayac-ay" viewBox="0 0 24 24" aria-hidden="true" style="width: 12px; height: 12px"><circle cx="12" cy="12" r="9"></circle><path d="{{cdAy}}"></path></svg>{{cdTiny}}</span></span>
    <button class="btn-on" type="button" style="flex: 0 0 150px; width: 150px; min-height: 52px; margin: 0; font-size: 16px; box-shadow: 0 3px 0 rgba(12,16,39,.6)">Satın al</button>
  </div>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { g: 0, adet: 1, tema: 0, now: Date.now() }; }
  componentDidMount() {
    var self = this; this.iv = setInterval(function () { self.setState({ now: Date.now() }); }, 1000);
    // Kargo takibi: E ile aynı; çizelge ekrana girince döngü başlar
    var yol = document.querySelector('.yol');
    if (yol && typeof IntersectionObserver !== 'undefined') {
      this.yolio = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { self.setState({ yolAc: true }); self.yolio.disconnect(); } }, { threshold: .6 });
      this.yolio.observe(yol);
    } else this.setState({ yolAc: true });
  }
  componentWillUnmount() { clearInterval(this.iv); if (this.yolio) this.yolio.disconnect(); }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    """ + TL_JS + """
    var G = [
      { id: '""" + IMG['oda'] + """', n: 'Çocuk odasında Galaxy USB projektör, tavanda galaksi', pos: '45% 40%' },
      { id: '""" + IMG['urun'] + """', n: 'Galaxy USB projektör ve tavana yansıyan galaksi', pos: '50% 35%' },
      { id: '""" + IMG['cocuk'] + """', n: 'Yatağında tavana bakan çocuk', pos: '35% 50%' },
      { id: '""" + IMG['bas'] + """', n: 'Döner başlık yakından', pos: '50% 35%' }
    ];
    var gal = G.map(function (g, i) { var on = i === S.g; return { src: B + g.id, n: g.n, pos: g.pos, on: on ? 'true' : 'false', op: on ? 1 : 0, cls: on ? 'kare on' : 'kare', pick: function () { self.setState({ g: i }); } }; });
    // Fiyat: Shopify (₺1.599 / ₺1.999). 2'li fiyat tanımlı değil: yer tutucu.
    var P1 = 1599, C1 = 1999, P2 = null;
    var paket = [
      { n: 1, t: '1 Adet', p: TL(P1, true), old: TL(C1, true), unit: '', sub: '%' + Math.round((1 - P1 / C1) * 100) + ' indirim', rib: false },
      { n: 2, t: '2 Adet', p: P2 ? TL(P2, true) : '[2’li fiyat]', old: '', unit: P2 ? 'tanesi ' + TL(Math.floor(P2 / 2 * 100) / 100, true) : '', sub: P2 ? TL(2 * P1 - P2, true) + ' kazanç' : '[kazanç]', rib: true }
    ].map(function (b) { var on = S.adet === b.n; return { tlCls: b.n === 2 ? 'tl cift' : 'tl', t: b.t, p: b.p, old: b.old, hasOld: !!b.old, unit: b.unit, sub: b.sub, rib: b.rib, two: b.n === 2,
      on: on ? 'true' : 'false', cls: on ? 'kt on' : 'kt', pick: function () { self.setState({ adet: b.n }); } }; });
    var total = S.adet === 2 ? P2 : P1, online = total ? Math.round(total * 0.95 * 100) / 100 : null;
    var onPrice = online ? TL(online, true) : '[fiyat]';
    var AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
    var now = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kd = new Date(now); do { kd.setDate(kd.getDate() + 1); } while (kd.getDay() === 0 || kd.getDay() === 6);
    var t1 = new Date(kd); t1.setDate(t1.getDate() + 3); var t2 = new Date(kd); t2.setDate(t2.getDate() + 7);
    var teslim = t1.getMonth() === t2.getMonth() ? t1.getDate() + '–' + t2.getDate() + ' ' + AY[t2.getMonth()] : t1.getDate() + ' ' + AY[t1.getMonth()] + '–' + t2.getDate() + ' ' + AY[t2.getMonth()];
    function IKI(n) { return n < 10 ? '0' + n : String(n); }
    var ist = new Date(new Date(S.now || Date.now()).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var gunSonu = new Date(ist.getFullYear(), ist.getMonth(), ist.getDate(), 23, 59, 59, 999);
    var kalan = Math.max(0, gunSonu.getTime() - ist.getTime());
    var hh = Math.floor(kalan / 3600000), mi = Math.floor(kalan / 60000) % 60, ss = Math.floor(kalan / 1000) % 60;
    function AYY(f) { var r = 9, c = 12, rx = Math.abs(1 - 2 * f) * r; return 'M' + c + ' ' + (c - r) + 'A' + r + ' ' + r + ' 0 0 1 ' + c + ' ' + (c + r) + 'A' + rx.toFixed(2) + ' ' + r + ' 0 0 ' + (f < .5 ? 0 : 1) + ' ' + c + ' ' + (c - r) + 'Z'; }
    // Temalar: tavan önizlemesi (Galaksi geniş görselden, diğerleri afişteki tema karelerinden)
    var T = """ + str([[n, IMG[buyuk], IMG[kucuk]] for n, buyuk, kucuk in TEMALAR]) + """;
    var temalar = T.map(function (t, i) { var on = i === S.tema; return { n: t[0], src: B + t[2], on: on ? 'true' : 'false', cls: on ? 'tema-cip on' : 'tema-cip', pick: function () { self.setState({ tema: i }); } }; });
    var proj = T.map(function (t, i) { return { src: B + t[1], cls: i === S.tema ? 'yansima on' : 'yansima' }; });
    function alaGit() { var h = document.getElementById('siparis'); if (h && h.scrollIntoView) h.scrollIntoView({ behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' }); }
    function odaKay(e) { var el = e && (e.currentTarget || e.target); if (!el) return; var i = el.scrollLeft > 150 ? 1 : 0; if (i !== (self.state.oda || 0)) self.setState({ oda: i }); }
    var faq = [
      { q: 'Kutudan ne çıkıyor?', a: '1 Galaxy USB projektör ve 12 tema diski. USB ucu gövdeye bağlı; ayrı kablo gerekmez.' },
      { q: 'Neyle çalışır?', a: 'USB girişi olan her yerde: bilgisayar, powerbank ya da USB adaptör. Takılıyken çalışır.' },
      { q: 'Görüntü bulanık, ne yapmalıyım?', a: 'Odayı karart, başlığı tavana ya da duvara çevir ve odağı yavaşça çevir. En net görüntü karanlık odada olur.' },
      { q: 'Disk nasıl değişir?', a: '[Adımlar teyit edilecek.] Zorlanırsan WhatsApp’tan yaz, görüntülü gösterelim.' },
      { q: 'Çocuk odasında kullanılır mı?', a: 'Evet. Diskler küçük parça; küçük çocuklar gözetimle kullansın.' },
      { q: 'Kargo ne zaman gelir?', a: 'Siparişin 1 iş gününde kargoya verilir, Türkiye geneline 3–7 günde ulaşır.' },
      { q: 'Kartla mı, kapıda mı ödeyeyim?', a: 'Tüm kredi ve banka kartları geçer; kartla öderken %5 indirim alırsın, kart bilgin bize gelmez. Kapıda ödemede ₺80 kapıda ödeme ücreti eklenir; ürün geldiğinde nakit ya da kartla ödersin.' },
      { q: 'Beğenmezsem iade edebilir miyim?', a: '30 gün içinde iade edebilirsin. Sana iade kodunu göndeririz, kargosu ücretsizdir. İlk 14 gün yasal cayma hakkındır.' }
    ];
    var PR = [
      { n: 'LunaDream Gece Lambası', p: 1699.99, c: 1999, id: 'e02351b3be4a1c555c5d760d0bbda723' },
      { n: 'Ayluna Galaksi Night Projektör', p: 2199, c: 2999, id: '2b381f338377f23e32074d6dbb452587' },
      { n: 'Galaksi Ambiyans Işığı', p: 1499, c: 2898, id: 'abe882f12bc58627f99b18a6e9aae0df' },
      { n: 'Ayluna AyFeneri', p: 1649.99, c: 2499, id: '94179bf5fda7b68f949842832e376fe6' },
      { n: 'Yıldız Işığı Nemlendirici', p: 849.99, c: 1099, id: 'f3f3e14eee224ef5534b9b897030ff58' },
      { n: 'Ayluna Kum Saati Lamba', p: 799, c: 999, id: '408afb48de0f2b2be66d095849fedda8' },
      { n: 'Sunset Lamba', p: 699, c: 999, id: '9bd9f9b4f1a38c4163064ce1c6117bbf' }
    ];
    var shop = PR.map(function (x) { var d = x.c > x.p; return { n: x.n, src: B + x.id, price: TL(x.p, true), old: d ? TL(x.c, true) : '', pct: d ? '%' + Math.round((1 - x.p / x.c) * 100) : '' }; });
    return {
      gal: gal, gNo: S.g + 1, gCount: G.length, gPrev: function () { self.setState({ g: (S.g + G.length - 1) % G.length }); }, gNext: function () { self.setState({ g: (S.g + 1) % G.length }); },
      paket: paket, adetName: S.adet === 2 ? '2 Adet' : '1 Adet',
      onLabel: 'Güvenli Ödeme ile Al · ' + onPrice, onPrice: onPrice,
      p1: TL(P1, true), c1: TL(C1, true), pct: Math.round((1 - P1 / C1) * 100),
      kargo: kd.getDate() + ' ' + AY[kd.getMonth()], teslim: teslim, starPct: 0,
      yolCls: S.yolAc ? 'yol on' : 'yol', cdShort: IKI(hh) + ':' + IKI(mi) + ':' + IKI(ss), cdTiny: IKI(hh) + ' sa ' + IKI(mi) + ' dk kaldı',
      cdAy: AYY(Math.round(kalan / 864000) / 100), cdAria: 'Bugünkü fiyat garantisinin bitmesine ' + hh + ' saat ' + mi + ' dakika',
      temalar: temalar, proj: proj, temaAd: T[S.tema][0], alaGit: alaGit, odaKay: odaKay,
      nokta0: (S.oda || 0) === 0 ? 'on' : '', nokta1: (S.oda || 0) === 1 ? 'on' : '', faq: faq, shop: shop, shopCount: PR.length
    };
  }
}"""

if __name__ == '__main__':
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='Galaxy USB Projektör', css=CSS) + HTML + TAIL.format(h=int(os.environ.get('U_H', 5030)), js=JS))
    print('yazıldı:', os.path.abspath(OUT))
