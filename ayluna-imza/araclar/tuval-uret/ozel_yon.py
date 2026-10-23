# AyFeneri ve Galaksi Night Projektör · kendine özgü tasarım dili için iki yön her biri (18 Eki). Çalıştır: python3 ozel_yon.py
# Kullanıcı: "AyLuna AyFeneri ve Galaksi Night Projector için özel sayfa tasarla" (LunaDream E ve Galaxy USB gibi imza sayfa).
# Ortak çekirdek (değişmez): lacivert #1A2142 marka rengi, Galaxy USB'nin sakin Yön A düzeni (tam ekran fotoğraf, yazı görselin içinde,
# küçük resim yok, kaydırmalı galeri + ürüne özgü gösterge, tek sayaç), satın alma akışı (kartla %5 önce, kapıda ikinci, kapıda butonunda fiyat yok),
# stok satırı elle, 30 gün iade, teyitsiz bilgi köşeli. Her yönde değişen: ikinci renk, zemin, yazı tipi, gösterge, iki imza bölümü.
#   AyFeneri  A · Liman feneri  : sis grisi + fener amberi, Big Shoulders Display. İmza: "Feneri yak" anahtarı, dönen fener huzmesi.
#   AyFeneri  B · Kıyı masalı   : ay ışığı grisi + amber, Instrument Serif. İmza: "Bu akşam hangisi?" mod seçici, cetvelli boy kartı.
#   Galaksi   A · Planetaryum   : gece moru, Sora + Manrope. İmza: tavanda yavaşça dönen gök (12 disk), netlik halkası.
#   Galaksi   B · Gözlemevi     : yıldız mavisi, Archivo geniş. İmza: "Tavan mı, duvar mı?" oda çizimi, temalı disk setleri.
# Kullanıcı (18 Eki): Galaksi Night için pococo.com/products/galaxy-projector-star-projector-silver referans. Alınanlar: alıcı fotoğrafları şeridi,
# koyu bilgi karoları, sayfa içi sekmeler, temalı disk setleri. Alınmayanlar: sağlık iddiaları (kortizol, anksiyete), 2M/30M/5K rakamları, "sahte projektör" kıyası.
# Görseller: mağaza afişlerinin yazısız kısımları ve AyFeneri videosunun kareleri (canvas/ozel). Kullanılmayanlar: 5K, lens sayısı, 153.748 yıldız,
# 130 m², "şarjlı ve kablosuz" (Galaksi kabloyla çalışır), AyFeneri'nde sensör ve pil (teyit), uydurma yorum kartları, sağlık iddiaları, "4,7 · 2467".
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import TAIL, TL_JS
import luna_e as E
import luna_usb_yon as Y
import luna_usb as U
CANVAS = os.path.join(HERE, '..', '..', 'canvas')
B = '/_blob/'
BL = json.load(open(os.path.join(CANVAS, 'ozel', 'bloblar.json')))
I = lambda k: B + BL[k]

# Galaksi Night: kutudaki 12 tema diski (mağaza afişindeki yelpazeden, örtüşmeyen en büyük daire). Adlar desenin tarifidir. Sayı [teyit: 12 mi, Ay diskiyle 13 mü].
GDISK = [('Pembe bulutsu', 'gn-d01-pembe-bulutsu'), ('Halka bulutsu', 'gn-d02-halka-bulutsu'), ('Sarmal galaksi', 'gn-d03-sarmal-galaksi'),
         ('Orion bulutsusu', 'gn-d04-orion'), ('Kızıl gezegenler', 'gn-d05-kizil-gezegenler'), ('Yıldız kümesi', 'gn-d06-yildiz-kumesi'),
         ('Kuyruklu yıldız', 'gn-d07-kuyruklu-yildiz'), ('Kuzey ışığı', 'gn-d08-kuzey-isigi'), ('Dolunay', 'gn-d09-dolunay'),
         ('Samanyolu', 'gn-d10-samanyolu'), ('Samanyolu kıyısı', 'gn-d11-samanyolu-2'), ('Yıldızlı gece', 'gn-d12-yildizli-gece')]

# Ürün bilgisi (canlı mağaza, 18 Eki; ogrenme/urun-icerik.json)
URUN = {
    'af': dict(ad='Ayluna AyFeneri', P1=1649.99, C1=2499, P2=2299.99,
               gal=[('af-ay', 'Komodinde AyFeneri, arkadaki duvarda ay yansıması', '50% 40%'),
                    ('af-oda', 'Gece odasında yanan AyFeneri', '50% 40%'),
                    ('af-urun', 'AyFeneri gövdesi ve çıkarılabilir tabanı', '50% 40%'),
                    ('af-uyku', 'Komodinde yanan AyFeneri, yatakta uyuyan biri', '30% 50%')],
               pk='af-ay-yakin'),
    'gn': dict(ad='Ayluna Galaksi Night Projektör', P1=2199, C1=2999, P2=3499.99,
               gal=[('gn-galaksi', 'Galaksi Night projektör, arkada galaksi görüntüsü', '50% 50%'),
                    ('gn-isik', 'Projektörden yukarı yayılan galaksi ışığı', '50% 50%'),
                    ('gn-el', 'Avuçta Galaksi Night projektör', '50% 50%')],
               pk='gn-isik'),
}

# Yönler: lacivert sabit; v = koyu zeminde ikinci renk, v2 = açık zeminde okunur tonu
YON = {
    'af-a': dict(urun='af', dosya='AyFeneri-YonA.dc.html', ad='Liman feneri', alt='Sis grisi + fener amberi; Big Shoulders Display (liman tabelası) + Figtree',
                 v='#F3B562', v2='#875912', zemin='#F1F3F4', cizgi='#DDE2E5', koyu='#101A33', koyu2='#1B2747',
                 fb='"Big Shoulders Display"', fg='"Figtree"', bk=800, bls='-.005em',
                 font='family=Big+Shoulders+Display:wght@700;800&family=Figtree:wght@400;500;600;700',
                 ek='.pg .h2{font-size:30px;line-height:.96}.pg .fiyat b{font-size:26px}.pg .al h1{font-size:30px}.hero-y .bas-y{font-size:64px;line-height:.86}.al h1{font-size:40px;line-height:.95}.fiyat b{font-size:36px}'),
    'af-b': dict(urun='af', dosya='AyFeneri-YonB.dc.html', ad='Kıyı masalı', alt='Ay ışığı grisi + amber; Instrument Serif (masal kitabı) + Figtree',
                 v='#EAB25C', v2='#82570F', zemin='#EEF0F4', cizgi='#DADFE8', koyu='#0F1630', koyu2='#1A2342',
                 fb='"Instrument Serif"', fg='"Figtree"', bk=400, bls='-.015em',
                 font='family=Instrument+Serif&family=Figtree:wght@400;500;600;700',
                 ek='.pg .h2{font-size:40px;line-height:.98}.hero-y .bas-y{font-size:54px;line-height:.94}.al h1{font-size:38px}.fiyat b{font-family:var(--fg);font-weight:700;font-size:28px}'),
    'gn-a': dict(urun='gn', dosya='GalaksiNight-YonA.dc.html', ad='Planetaryum', alt='Bulutsu moru; Sora + Manrope',
                 v='#B4A9FF', v2='#5546C9', zemin='#F3F3F8', cizgi='#E0E0EC', koyu='#0E1026', koyu2='#1B1E3F',
                 fb='"Sora"', fg='"Manrope"', bk=700, bls='-.04em',
                 font='family=Sora:wght@600;700&family=Manrope:wght@400;500;600;700',
                 ek='.hero-y .bas-y{font-size:44px}.pg .al h1{font-size:24px;line-height:1.1}'),
    'gn-b': dict(urun='gn', dosya='GalaksiNight-YonB.dc.html', ad='Gözlemevi', alt='Yıldız mavisi; Archivo geniş (gözlem aleti yazısı)',
                 v='#9CC3FF', v2='#2D58B3', zemin='#F2F4F7', cizgi='#DEE3EA', koyu='#0C1428', koyu2='#17223F',
                 fb='"Archivo"', fg='"Archivo"', bk=800, bls='-.02em',
                 font='family=Archivo:wdth,wght@100..125,400..800',
                 ek='.bas-y{font-stretch:118%}.hero-y .bas-y{font-size:38px;line-height:1}.pg .h2{font-size:28px;line-height:1.02}.al h1{font-size:26px;line-height:1.05}'),
}


def tema_css(t):
    return ('.pg{--v:%(v)s;--v2:%(v2)s;--zemin:%(zemin)s;--cizgi:%(cizgi)s;--koyu:%(koyu)s;--koyu2:%(koyu2)s;--fb:%(fb)s,ui-sans-serif,system-ui,sans-serif;'
            '--fg:%(fg)s,ui-sans-serif,system-ui,sans-serif;--bk:%(bk)d;--bls:%(bls)s}\n' % t) + t.get('ek', '') + '\n'


# Her iki ürün için ek CSS (USB çekirdeğinin üstüne)
CSS = r"""
.serit .sy b{background:var(--koyu2)}
.pk-g img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;margin:0}
.pk-g .x2{position:absolute;right:4px;bottom:4px;padding:0 5px;border-radius:6px;background:var(--lac);color:var(--v);font-size:11px;font-weight:800;line-height:1.6}
.kutu-not{display:flex;align-items:center;gap:10px;margin:14px 0 0;font-size:14px;font-weight:600}
.kutu-not .dn img{width:30px;height:30px;margin-left:-12px}.kutu-not .dn img:first-child{margin-left:0}

/* AyFeneri galeri göstergesi: küçük deniz fenerleri; geçilen fotoğrafın feneri yanık, o anki fenerin huzmesi döner */
.f-iz{display:flex;align-items:flex-end;gap:14px}
.f-iz svg{width:14px;height:22px;overflow:visible;fill:none;stroke:rgba(238,242,250,.5);stroke-width:1.3;stroke-linejoin:round;transition:transform .4s var(--ease)}
.f-iz .fn{fill:transparent;transition:fill .4s}
.f-iz .lit{stroke:rgba(238,242,250,.95)}.f-iz .lit .fn{fill:var(--v)}
.f-iz .hz{fill:var(--v);stroke:none;opacity:0;transform-origin:7px 6.5px}
.f-iz .on{transform:scale(1.3);transform-origin:50% 100%}
.f-iz .on .hz{opacity:.5;animation:hz 2.6s ease-in-out infinite}
@keyframes hz{0%,100%{transform:rotate(-14deg)}50%{transform:rotate(14deg)}}

/* Galaksi galeri göstergesi: yörünge; geçilen gezegen dolu, o anki gezegenin ayı döner */
.y-iz{display:flex;align-items:center;gap:8px}
.y-iz svg{width:20px;height:20px;overflow:visible;transition:transform .4s var(--ease)}
.y-iz .gz{fill:rgba(238,242,250,.38)}.y-iz .lit .gz{fill:var(--v)}
.y-iz .yr{fill:none;stroke:rgba(238,242,250,.35);stroke-width:1;opacity:0;transition:opacity .4s}
.y-iz .ay{fill:#fff;opacity:0}
.y-iz .on{transform:scale(1.2)}.y-iz .on .yr,.y-iz .on .ay{opacity:1}
.y-iz .on .yo{transform-origin:10px 10px;animation:don 3s linear infinite}

/* Özellik kutusu küçük hareketleri */
.mini{position:relative;display:grid;place-items:center;width:48px;height:48px;border-radius:12px;background:var(--lac);overflow:hidden}
.mini svg{width:28px;height:28px;fill:none;stroke:var(--v);stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;overflow:visible}
.mini .ayi{fill:var(--v);stroke:none;animation:ayi 3s ease-in-out infinite alternate}
@keyframes ayi{from{opacity:.55;transform:scale(.9)}to{opacity:1;transform:scale(1.05)}}
.mini .ayi{transform-origin:14px 14px}
.esit{display:flex;align-items:flex-end;gap:3px;height:22px}
.esit i{width:4px;height:100%;border-radius:2px;background:var(--v);transform-origin:50% 100%;animation:esit 1.1s ease-in-out infinite alternate}
.esit i:nth-child(2){animation-delay:-.3s}.esit i:nth-child(3){animation-delay:-.6s}.esit i:nth-child(4){animation-delay:-.9s}
@keyframes esit{from{transform:scaleY(.25)}to{transform:scaleY(1)}}
.dalga path{stroke-dasharray:6 4;animation:dalga 1.6s linear infinite}
.dalga path:nth-child(2){animation-duration:2.2s}
@keyframes dalga{to{stroke-dashoffset:-20}}
.sinyal path{opacity:.2;animation:sinyal 2.4s ease-in-out infinite}
.sinyal path:nth-of-type(2){animation-delay:.25s}.sinyal path:nth-of-type(3){animation-delay:.5s}
@keyframes sinyal{0%,20%{opacity:.2}40%,70%{opacity:1}90%,100%{opacity:.2}}
.egil .bs{transform-origin:14px 19px;animation:egil 4s var(--ease) infinite}
@keyframes egil{0%,30%{transform:rotate(-35deg)}50%,80%{transform:rotate(35deg)}100%{transform:rotate(-35deg)}}
.halka-ik{animation:halka 5s var(--ease) infinite;transform-origin:14px 14px}
@keyframes halka{0%,20%{transform:rotate(0)}60%,100%{transform:rotate(120deg)}}
.dn.don img:first-child{animation:don 20s linear infinite}

/* ===== AyFeneri A · Feneri yak: oda karanlık; anahtara basınca ışık fenerden yayılır, duvarda ay doğar ===== */
.yak{position:relative;height:470px;margin-top:20px;border-radius:22px;overflow:hidden;background:#07090F;color:#fff}
.yak img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 30%}
.yak .k0{filter:brightness(.13) saturate(.3)}
.yak .k1{clip-path:circle(0% at 54% 35%);transition:clip-path 1.6s var(--ease)}
.yak.on .k1{clip-path:circle(130% at 54% 35%)}
.yak .kor{position:absolute;left:54%;top:35%;width:14px;height:14px;margin:-7px 0 0 -7px;border-radius:50%;background:var(--v);box-shadow:0 0 18px 6px rgba(243,181,98,.45);opacity:.9;transition:opacity .6s}
.yak.on .kor{opacity:0}
.yak::after{content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(180deg,rgba(7,9,15,.55) 0,rgba(7,9,15,0) 26%,rgba(7,9,15,0) 62%,rgba(7,9,15,.85) 100%)}
.yak-y{position:absolute;left:18px;right:18px;top:18px;z-index:2}
.yak-y .bas-y{font-size:40px;line-height:.92;color:#fff}
.yak-y .bas-y span{display:block;transition:color .6s}
.yak.on .yak-y .bas-y span:last-child{color:var(--v)}
.yak-alt{position:absolute;left:18px;right:18px;bottom:16px;z-index:2;display:flex;align-items:center;justify-content:space-between;gap:12px}
.yak-alt p{margin:0;font-size:14px;color:#D5DBEA;line-height:1.35}
.anahtar{flex:none;display:flex;align-items:center;gap:10px;min-height:48px;padding:0 6px 0 14px;border:0;border-radius:999px;background:rgba(255,255,255,.12);box-shadow:inset 0 0 0 1px rgba(255,255,255,.22)}
.pg .anahtar{color:#fff}
.anahtar b{font-size:14px}
.anahtar i{position:relative;width:56px;height:34px;border-radius:999px;background:#2A3149;transition:background .4s var(--ease)}
.anahtar i::after{content:"";position:absolute;left:4px;top:4px;width:26px;height:26px;border-radius:50%;background:#fff;transition:transform .4s var(--ease)}
.yak.on .anahtar i{background:var(--v)}.yak.on .anahtar i::after{transform:translateX(22px)}

/* ===== AyFeneri A · Fener huzmesi: dört iş; huzme sırayla birine döner ===== */
.hzm{position:relative;margin-top:20px;padding:8px 16px 8px 100px;border-radius:22px;background:var(--koyu);color:#EEF2FA;overflow:hidden;list-style:none}
.hzm-f{position:absolute;left:22px;top:50%;width:44px;height:120px;margin-top:-24px;fill:none;stroke:#EEF2FA;stroke-width:1.6;stroke-linejoin:round;stroke-linecap:round;z-index:2}
.hzm-f .fn{fill:var(--v);stroke:var(--v)}
.hzm-h{position:absolute;left:44px;top:50%;width:420px;height:150px;margin-top:-75px;transform-origin:0 50%;background:linear-gradient(90deg,rgba(243,181,98,.6),rgba(243,181,98,.05) 80%);clip-path:polygon(0 47%,100% 0,100% 100%,0 53%);transition:transform .9s var(--ease);z-index:1}
.hzm.k0 .hzm-h{transform:rotate(-33deg)}.hzm.k1 .hzm-h{transform:rotate(-11deg)}.hzm.k2 .hzm-h{transform:rotate(11deg)}.hzm.k3 .hzm-h{transform:rotate(33deg)}
.hzm li{position:relative;z-index:2;padding:13px 0;border-bottom:1px solid rgba(238,242,250,.1);opacity:.42;transition:opacity .5s var(--ease)}
.hzm li:last-child{border-bottom:0}
.hzm li.on{opacity:1}
.hzm li b{display:block;font-family:var(--fb);font-weight:var(--bk);font-size:22px;letter-spacing:var(--bls);line-height:1}
.hzm li span{display:block;margin-top:4px;font-size:14px;color:#C9D0E2}
.hzm li button{position:absolute;inset:0;width:100%;border:0;background:transparent}

/* ===== AyFeneri B · Bu akşam hangisi: dört mod; görsel ve köşedeki hareketli işaret değişir ===== */
.mod{position:relative;height:500px;margin-top:20px;border-radius:22px;overflow:hidden;background:var(--koyu);color:#fff;isolation:isolate}
.mod-f{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .7s var(--ease)}
.mod-f.on{opacity:1;animation:kb 7s linear both}
.mod::after{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;background:linear-gradient(180deg,rgba(15,22,48,.72) 0,rgba(15,22,48,0) 26%,rgba(15,22,48,0) 48%,rgba(15,22,48,.94) 88%)}
.mod-sec{position:absolute;left:0;right:0;top:14px;z-index:3;display:flex;gap:6px;overflow-x:auto;padding:0 14px}
.mod-sec button{flex:none;min-height:48px;padding:0 15px;border:0;border-radius:999px;background:rgba(15,22,48,.6);box-shadow:inset 0 0 0 1px rgba(238,242,250,.22);font-size:14px;font-weight:600}
.pg .mod-sec button{color:#fff}
.pg .mod-sec button.on{background:var(--v);color:var(--koyu);box-shadow:none}
.mod-y{position:absolute;left:18px;right:18px;bottom:18px;z-index:3;opacity:0;visibility:hidden}
.mod-y.on{opacity:1;visibility:visible}
.mod-y.on>*{animation:sol .7s var(--ease) both}.mod-y.on p{animation-delay:.1s}
.mod-y .bas-y{font-size:40px;line-height:.95}
.mod-y p{margin:8px 0 0;font-size:15px;color:#D5DBEA;max-width:300px}
.mod-i{display:inline-grid;place-items:center;width:52px;height:52px;margin-bottom:12px;border-radius:16px;background:rgba(15,22,48,.7);box-shadow:inset 0 0 0 1px rgba(238,242,250,.2)}
.mod-i svg{width:30px;height:30px;fill:none;stroke:var(--v);stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;overflow:visible}
.mod-i .ayi{fill:var(--v);stroke:none;transform-origin:14px 14px;animation:ayi 3s ease-in-out infinite alternate}
.mod-i .isin{transform-origin:15px 15px;animation:don 14s linear infinite}
.mod-i .esit{height:26px}.mod-i .esit i{width:5px}

/* ===== AyFeneri B · Boy kartı: cetvel tabandan tepeye dolar ===== */
.boy{position:relative;height:440px;margin-top:20px;border-radius:22px;overflow:hidden;background:#1C1714;color:#fff}
.boy img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 20%}
.boy::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(15,22,48,.82) 0,rgba(15,22,48,.2) 46%,rgba(15,22,48,0) 70%)}
.boy-c{position:absolute;right:30px;top:40px;bottom:36px;width:2px;z-index:2;background:rgba(255,255,255,.25)}
.boy-c i{position:absolute;left:0;right:0;bottom:0;height:100%;background:var(--v);transform-origin:50% 100%;animation:boyc 4.5s var(--ease) infinite}
.boy-c::before,.boy-c::after{content:"";position:absolute;left:-7px;width:16px;height:2px;background:#fff}
.boy-c::before{top:0}.boy-c::after{bottom:0}
@keyframes boyc{0%{transform:scaleY(0)}45%,85%{transform:scaleY(1)}100%{transform:scaleY(1);opacity:0}}
.boy-y{position:absolute;left:18px;top:22px;bottom:22px;z-index:2;display:flex;flex-direction:column;justify-content:space-between;max-width:200px}
.boy-y .bas-y{font-size:40px;line-height:.95}
.boy-y em{display:block;font-style:normal;font-family:var(--fb);font-size:56px;line-height:.9;color:var(--v)}
.boy-y em small{font-size:22px}
.boy-y p{margin:6px 0 0;font-size:14px;color:#D5DBEA}

/* ===== Galaksi A · Tavanda dönen gök: seçilen disk yavaşça döner; kendiliğinden gezer, dokununca durur ===== */
.kb-s{position:relative;height:350px;margin-top:6px;overflow:hidden}
.kubbe{position:absolute;left:50%;top:6px;width:300px;height:300px;margin-left:-150px;border-radius:50%;overflow:hidden;-webkit-mask-image:radial-gradient(circle,#000 54%,transparent 71%);mask-image:radial-gradient(circle,#000 54%,transparent 71%)}
.kubbe-d{position:absolute;inset:0;animation:don 70s linear infinite}
.kubbe img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(.9);transition:opacity 1.1s var(--ease),transform 1.4s var(--ease);filter:saturate(1.15)}
.kubbe img.on{opacity:1;transform:none}
.kb-isik{position:absolute;left:50%;top:170px;width:220px;height:180px;margin-left:-110px;background:linear-gradient(0deg,rgba(180,169,255,.34),rgba(180,169,255,0));clip-path:polygon(46% 100%,54% 100%,100% 0,0 0);animation:isik 3.6s ease-in-out infinite alternate}
.kb-ad{position:absolute;left:16px;bottom:10px;display:flex;align-items:center;gap:10px}
.kb-ad b{font-family:var(--fb);font-weight:var(--bk);font-size:20px;letter-spacing:-.02em}
.kb-ad svg{width:22px;height:22px;fill:none;stroke:var(--v);stroke-width:1.8;stroke-linecap:round;animation:don 6s linear infinite}
.kb-iz{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:12px 8px;margin-top:16px}
.kb-iz button{aspect-ratio:1;padding:0;border:0;border-radius:50%;background:transparent;box-shadow:0 0 0 1.5px rgba(238,242,250,.16);transition:transform .3s var(--ease)}
.kb-iz button img{display:block;width:100%;height:100%;border-radius:50%}
.kb-iz button.on{box-shadow:0 0 0 2.5px var(--v);transform:scale(1.1)}

/* ===== Galaksi A · Netlik halkası: görüntü bulanıktan netleşir, halka döner ===== */
.net{display:grid;grid-template-columns:150px minmax(0,1fr);gap:18px;align-items:center;margin-top:20px;padding:18px;border-radius:22px;background:var(--koyu);color:#EEF2FA}
.net-g{position:relative;width:150px;height:150px}
.net-g img{position:absolute;inset:14px;width:122px;height:122px;border-radius:50%;object-fit:cover;animation:net 5s var(--ease) infinite}
@keyframes net{0%,12%{filter:blur(7px)}55%,90%{filter:blur(0)}100%{filter:blur(7px)}}
.net-g svg{position:absolute;inset:0;width:150px;height:150px;fill:none;stroke:var(--v);stroke-width:1.6;animation:netr 5s var(--ease) infinite}
@keyframes netr{0%,12%{transform:rotate(0)}55%,90%{transform:rotate(100deg)}100%{transform:rotate(0)}}
.net b{display:block;font-family:var(--fb);font-weight:var(--bk);font-size:22px;letter-spacing:var(--bls);line-height:1.1}
.net span>span{display:block;margin-top:6px;font-size:14px;color:#C9CEE6}

/* ===== Galaksi B · Tavan mı, duvar mı: oda kesiti; başlık eğilir, ışık tavandan duvara geçer ===== */
.oda{position:relative;height:300px;margin-top:20px;border-radius:22px;overflow:hidden;background:var(--koyu)}
.oda::before{content:"";position:absolute;left:18px;right:18px;top:18px;height:0;border-top:1.5px solid rgba(238,242,250,.25)}
.oda::after{content:"";position:absolute;right:18px;top:18px;bottom:18px;width:0;border-right:1.5px solid rgba(238,242,250,.25)}
.oda-z{position:absolute;left:18px;right:18px;bottom:18px;height:0;border-top:1.5px solid rgba(238,242,250,.25)}
.komo{position:absolute;left:58px;bottom:19px;width:84px;height:56px;border-radius:6px 6px 0 0;background:var(--koyu2);box-shadow:inset 0 0 0 1.5px rgba(238,242,250,.25)}
.pj{position:absolute;left:82px;bottom:75px;width:36px;height:36px;border-radius:50%;background:#F4F5FA}
.pj i{position:absolute;left:4px;top:4px;width:28px;height:28px;border-radius:50%;background:conic-gradient(#111 0 50%,transparent 50%);transform:rotate(-90deg);transition:transform 1s var(--ease)}
.oda.duvar .pj i{transform:rotate(0deg)}
.yama{position:absolute;overflow:hidden;opacity:0;transition:opacity .9s var(--ease) .3s}
.yama img{width:100%;height:100%;object-fit:cover;display:block}
.yama.t{left:40px;top:19px;width:240px;height:46px;border-radius:0 0 50% 50%/0 0 100% 100%}
.yama.d{right:19px;top:40px;width:46px;height:200px;border-radius:50% 0 0 50%/50% 0 0 50%}
.koni{position:absolute;opacity:0;transition:opacity .9s var(--ease) .2s;background:linear-gradient(0deg,rgba(156,195,255,.4),rgba(156,195,255,.05))}
.koni.t{left:40px;top:64px;width:240px;height:166px;clip-path:polygon(25% 100%,35% 100%,100% 0,0 0)}
.koni.d{left:100px;top:40px;right:64px;height:200px;background:linear-gradient(270deg,rgba(156,195,255,.4),rgba(156,195,255,.05));clip-path:polygon(0 74%,0 86%,100% 100%,100% 0)}
.oda.tavan .t,.oda.duvar .d{opacity:1}
.oda-sec{position:absolute;left:30px;top:94px;display:flex;gap:6px;z-index:3}
.oda-sec button{min-height:44px;padding:0 14px;border:0;border-radius:999px;background:rgba(238,242,250,.1);box-shadow:inset 0 0 0 1px rgba(238,242,250,.22);font-size:13px;font-weight:700}
.pg .oda-sec button{color:#fff}
.pg .oda-sec button.on{background:var(--v);color:var(--koyu);box-shadow:none}

/* Pococo referansı (kullanıcı, 18 Eki): fiyatın altında alıcı fotoğrafları, koyu bilgi karoları, sayfa içi sekmeler, temalı disk setleri */
.alici{margin:16px 0 0}
.alici>span{display:flex;justify-content:space-between;font-size:13px;font-weight:700}
.alici>span small{font-size:12px;font-weight:500;color:var(--soluk)}
.alici div{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin-top:8px}
.alici i{aspect-ratio:1;border-radius:12px;border:1.5px dashed #B8C0D2;display:grid;place-items:center;font-style:normal;font-size:11px;color:var(--soluk)}
.karo3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:20px}
.karo3 div{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;min-height:92px;padding:12px 6px;border-radius:14px;background:var(--lac);color:#fff;text-align:center}
.karo3 b{font-family:var(--fb);font-weight:var(--bk);font-stretch:118%;font-size:22px;letter-spacing:-.02em;line-height:1;color:var(--v)}
.karo3 span{font-size:12px;line-height:1.3;color:#D5DBEA}
.liste{list-style:none;margin:14px 0 0;padding:0;border-top:1px solid var(--cizgi)}
.liste li{display:flex;align-items:center;gap:12px;min-height:52px;border-bottom:1px solid var(--cizgi);font-size:15px}
.liste li b{flex:none;width:150px}
.liste li span{color:var(--soluk);font-size:14px}
.sekmeler{position:sticky;top:0;z-index:4;display:flex;gap:4px;padding:8px 12px;background:var(--zemin);border-bottom:1px solid var(--cizgi)}
.sekmeler a{flex:1;display:grid;place-items:center;min-height:44px;border-radius:999px;font-size:13px;font-weight:700;text-decoration:none}
.sekmeler a.on{background:var(--lac);color:#fff}
.setler{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:16px;padding:18px 16px 4px}
.set{flex:0 0 250px;scroll-snap-align:start;padding:16px;border-radius:20px;background:var(--koyu);color:#EEF2FA}
.set-d{position:relative;height:150px}
.set-d img{position:absolute;top:10px;width:110px;height:110px;border-radius:50%;box-shadow:0 0 0 3px var(--koyu)}
.set-d img:nth-child(1){left:0;z-index:3;animation:don 30s linear infinite}.set-d img:nth-child(2){left:60px;z-index:2}.set-d img:nth-child(3){left:120px;z-index:1}
.set b{display:block;font-family:var(--fb);font-weight:var(--bk);font-stretch:118%;font-size:20px;letter-spacing:-.02em}
.set span{display:block;margin-top:4px;font-size:13px;color:#C9CEE6;line-height:1.4}
.set small{display:inline-block;margin-top:10px;padding:2px 10px;border-radius:999px;background:var(--koyu2);font-size:12px;font-weight:700;color:var(--v)}

/* ===== Galaksi B · Haftanın gökleri: gün seç, o gecenin diski döner ===== */
.hafta{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:6px;margin-top:18px}
.hafta button{display:flex;flex-direction:column;align-items:center;gap:6px;min-height:72px;padding:8px 0;border:0;border-radius:14px;background:var(--yuzey);box-shadow:inset 0 0 0 1px var(--cizgi);font-size:12px;font-weight:700}
.hafta button img{width:28px;height:28px;border-radius:50%}
.pg .hafta button.on{background:var(--lac);color:#fff;box-shadow:none}
.gece{display:grid;grid-template-columns:150px minmax(0,1fr);gap:18px;align-items:center;margin-top:12px;padding:18px;border-radius:22px;background:var(--koyu);color:#EEF2FA}
.gece-d{position:relative;width:150px;height:150px;border-radius:50%;overflow:hidden;-webkit-mask-image:radial-gradient(circle,#000 58%,transparent 71%);mask-image:radial-gradient(circle,#000 58%,transparent 71%)}
.gece-d>span{position:absolute;inset:0;animation:don 50s linear infinite}
.gece-d img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .8s var(--ease)}
.gece-d img.on{opacity:1}
.gece small{display:block;font-size:13px;font-weight:700;color:var(--v)}
.gece b{display:block;margin-top:2px;font-family:var(--fb);font-weight:var(--bk);font-size:22px;letter-spacing:var(--bls);line-height:1.1}
.gece span>span{display:block;margin-top:6px;font-size:14px;color:#C9CEE6}
"""

# Göstergeler
FENER_SVG = ('<svg class="{{f.dcls}}" viewBox="0 0 14 22"><path class="hz" d="M8 6.5 L22 2 L22 11 Z"></path><path d="M4 5 L7 2 L10 5 Z"></path>'
             '<rect class="fn" x="4.5" y="5" width="5" height="3"></rect><path d="M4.5 8 H9.5 L10.5 20 H3.5 Z"></path><path d="M2 20.5 H12"></path></svg>')
YORUNGE_SVG = ('<svg class="{{f.dcls}}" viewBox="0 0 20 20"><circle class="yr" cx="10" cy="10" r="8"></circle><circle class="gz" cx="10" cy="10" r="3.2"></circle>'
               '<g class="yo"><circle class="ay" cx="18" cy="10" r="1.6"></circle></g></svg>')

BASLIK = {
    'af-a': ('<span><i>Duvarına</i></span><span><i><em>ay</em> doğsun.</i></span>', 'Deniz feneri biçiminde gece lambası: duvara ay yansıtır, müzik çalar.'),
    'af-b': ('<span><i>Bu gece</i></span><span><i>fener <em>sende.</em></i></span>', 'Duvarda ay, odada deniz sesi, elinde kumanda.'),
    'gn-a': ('<span><i>Tavanın</i></span><span><i>gökyüzü <em>olsun.</em></i></span>', 'Diski seç, ışığı kapat; galaksi yavaşça dönsün.'),
    'gn-b': ('<span><i>Odan bu gece</i></span><span><i><em>gözlemevi.</em></i></span>', 'Her gece başka bir gök: diski değiştir, tavan değişsin.'),
}


def hero(yon):
    u = YON[yon]['urun']
    gost = ('<span class="f-iz" aria-hidden="true"><sc-for list="{{gal}}" as="f" hint-placeholder-count="4">' + FENER_SVG + '</sc-for></span>') if u == 'af' else \
           ('<span class="y-iz" aria-hidden="true"><sc-for list="{{gal}}" as="f" hint-placeholder-count="3">' + YORUNGE_SVG + '</sc-for></span>')
    bas, alt = BASLIK[yon]
    return ("""
  <section class="hero" aria-label="%s fotoğrafları">
    <div class="h-iz noscroll" onScroll="{{gKay}}"><sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><div class="{{f.cls}}"><img src="{{f.src}}" alt="{{f.n}}" style="object-position: {{f.pos}}"><sc-if value="{{f.ilk}}" hint-placeholder-val="{{true}}"><div class="hero-y"><h2 class="bas-y">%s</h2><p>%s</p></div></sc-if></div></sc-for></div>
    %s
    <div class="h-alt">%s<span class="sira"><small>Temsilî görseller</small></span><span style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%%); white-space: nowrap" aria-live="polite">Fotoğraf {{gNo}} / {{gCount}}</span></div>
  </section>
""" % (URUN[u]['ad'], bas, alt, Y.ust('rgba(238,242,250,.6)'), gost))


def mini(ic):
    return '<span class="gz" aria-hidden="true"><span class="mini">%s</span></span>' % ic


AY_IK = '<svg viewBox="0 0 28 28"><circle class="ayi" cx="14" cy="14" r="8"></circle><path d="M3 24h22" style="stroke-dasharray: 3 3"></path></svg>'
ESIT = '<span class="esit"><i></i><i></i><i></i><i></i></span>'
DALGA = '<svg class="dalga" viewBox="0 0 28 28"><path d="M2 11c3-3 5-3 8 0s5 3 8 0 5-3 8 0"></path><path d="M2 18c3-3 5-3 8 0s5 3 8 0 5-3 8 0"></path></svg>'
KUMANDA = '<svg class="sinyal" viewBox="0 0 28 28"><rect x="9" y="12" width="10" height="15" rx="2.5"></rect><circle cx="14" cy="17" r="1.6"></circle><path d="M11 8.5a4.5 4.5 0 0 1 6 0"></path><path d="M8.5 5.5a8 8 0 0 1 11 0"></path><path d="M6 2.5a11.5 11.5 0 0 1 16 0"></path></svg>'
EGIL = '<svg class="egil" viewBox="0 0 28 28"><path d="M8 26h12"></path><path d="M14 26v-7"></path><g class="bs"><circle cx="14" cy="13" r="6"></circle><path d="M14 7V3"></path></g></svg>'
HALKA = '<svg viewBox="0 0 28 28"><g class="halka-ik"><circle cx="14" cy="14" r="10"></circle><path d="M14 4v3M24 14h-3M14 24v-3M4 14h3"></path></g><circle cx="14" cy="14" r="3.5"></circle></svg>'
DONUS = '<svg viewBox="0 0 28 28"><g style="transform-origin: 14px 14px; animation: don 8s linear infinite"><circle cx="14" cy="14" r="10" style="stroke-dasharray: 4 3"></circle><circle cx="24" cy="14" r="1.8" style="fill: var(--v)"></circle></g></svg>'


def gdisk_yigin():
    return '<span class="dn don" aria-hidden="true"><img src="%s" alt=""><img src="%s" alt=""><img src="%s" alt=""></span>' % (I(GDISK[2][1]), I(GDISK[7][1]), I(GDISK[0][1]))


def ozler(u):
    if u == 'af':
        return ('<div class="ozler">'
                '<div class="oz">' + mini(AY_IK) + '<b>Duvara ay</b><span class="t">Fenerin tepesinden ay yansır.</span></div>'
                '<div class="oz">' + mini(ESIT) + '<b>Bluetooth hoparlör</b><span class="t">Telefondan müzik çal.</span></div>'
                '<div class="oz">' + mini(DALGA) + '<b>Deniz sesi</b><span class="t">Dahili deniz sesi modu.</span></div>'
                '<div class="oz">' + mini(KUMANDA) + '<b>Kumanda dahil</b><span class="t">Işığı uzaktan yönet.</span></div>'
                '<div class="oz genis">' + '<span class="gz" aria-hidden="true"><span class="cetvel"><i></i></span></span>' +
                '<span><b>Çıkarılabilir taban</b><span class="t">Taban sökülür, masaya sabitlenir. Boy [24,2 cm teyit].</span></span></div></div>')
    return ('<div class="ozler">'
            '<div class="oz"><span class="gz">' + gdisk_yigin() + '</span><b>[12] tema diski</b><span class="t">Diski değiştir, gök değişsin.</span></div>'
            '<div class="oz">' + mini(EGIL) + '<b>Tavan ya da duvar</b><span class="t">Başlık eğilir, istediğine çevir.</span></div>'
            '<div class="oz">' + mini(DONUS) + '<b>Yavaşça döner</b><span class="t">Yansıyan gök ağır ağır akar.</span></div>'
            '<div class="oz">' + mini(HALKA) + '<b>Netlik halkası</b><span class="t">Görüntüyü keskinleştir.</span></div>'
            '<div class="oz genis"><span class="gz" aria-hidden="true"><span class="port"></span>' + U.FIS + '</span>'
            '<span><b>USB-C ile çalışır</b><span class="t">Şarjlı değil: prize ya da USB\'ye takılıyken çalışır, pil derdi yok.</span></span></div></div>')


def al(yon):
    u = YON[yon]['urun']; d = URUN[u]
    pct = round((1 - d['P1'] / d['C1']) * 100)
    alt = '2\'si 1 arada: gece lambası ve Bluetooth hoparlör.' if u == 'af' else 'Masa üstü galaksi projektörü, değiştirilebilir disklerle.'
    kutu = ('<p class="kutu-not"><span>Kutuda: AyFeneri + kumanda. USB kablo [teyit]</span></p>' if u == 'af' else
            '<p class="kutu-not">' + gdisk_yigin() + '<span>Kutuda [12] tema diski + USB-C kablo</span></p>')
    return ("""
  <section class="al" id="siparis">
    <h1 class="bas-y">%s</h1>
    <p class="alt-b">%s</p>
    <p class="fiyat" aria-label="%s, önceki fiyat %s, %%%d indirim"><b aria-hidden="true">%s</b><s aria-hidden="true">%s</s><span class="rozet" aria-hidden="true">%%%d indirim</span></p>
    %s%s
    <div class="pk-bas">Çok al, az öde</div>
    <div class="pk"><sc-for list="{{paket}}" as="b" hint-placeholder-count="2">
      <button class="{{b.cls}}" onClick="{{b.pick}}" aria-pressed="{{b.on}}"><sc-if value="{{b.rib}}" hint-placeholder-val="{{false}}"><span class="kurdele">En avantajlı</span></sc-if><span class="pk-g"><img src="%s" alt=""><sc-if value="{{b.two}}" hint-placeholder-val="{{false}}"><span class="x2">×2</span></sc-if></span><span class="pk-o"><b>{{b.t}}</b><span>{{b.sub}}</span></span><span class="pk-s"><b>{{b.p}}</b><sc-if value="{{b.hasOld}}" hint-placeholder-val="{{true}}"><s>{{b.old}}</s></sc-if><span>{{b.unit}}</span></span><span class="nokta"><i></i></span></button>
    </sc-for></div>
    %s
    <!-- Stok ELLE girilir (bölüm ayarı: sayı + aç/kapa); boşsa satır gizlenir -->
    <p class="stok"><span class="ping" aria-hidden="true"></span><span>Stokta son <b>[N]</b> adet</span></p>
    <button class="btn1" type="button"><span class="b-ic"><span>{{onLabel}}</span><small>Kartla %%5 indirim dahil</small></span>%s</button>
    <button class="btn2" type="button">Kapıda Ödeme ile Sipariş Ver</button>
    <ol class="yol" aria-label="Siparişten teslime"><span class="yol-iz" aria-hidden="true"><i></i><i></i><em></em></span><li class="y1"><span class="yd"></span><b>Bugün</b><span>Sipariş verildi</span></li><li class="y2"><span class="yd"></span><b>{{kargo}}</b><span>Kargoda</span></li><li class="y3"><span class="yd"></span><b>{{teslim}}</b><span>Kapında</span></li></ol>
  </section>
""" % (d['ad'], alt, tl(d['P1']), tl(d['C1']), pct, tl(d['P1']), tl(d['C1']), pct, ALICI if u == 'gn' else '', KARO3 if yon == 'gn-b' else ozler(u), I(d['pk']), kutu, U.OK))


# Pococo'daki "Buyers Shows": alıcıların kendi fotoğrafları (Loox'tan; uydurma yok)
ALICI = ('<div class="alici"><span>Alıcı fotoğrafları<small>[Loox: puan ve sayı otomatik]</small></span>'
         '<div><i>[foto]</i><i>[foto]</i><i>[foto]</i><i>[foto]</i></div></div>')
# Pococo'daki "2M / 30M / 3-Gear" karoları: bizde yalnız teyitli ya da köşeli bilgiler
KARO3 = ('<div class="karo3"><div><b>USB-C</b><span>Kabloyla çalışır,<br>pil derdi yok</span></div><div><b>[12]</b><span>Değiştirilebilir<br>tema diski</span></div>'
         '<div><b>2 yön</b><span>Tavana ya da<br>duvara</span></div></div>'
         '<ul class="liste"><li><b>Yavaşça döner</b><span>Gök ağır ağır akar</span></li><li><b>Netlik halkası</b><span>Görüntüyü keskinleştir</span></li>'
         '<li><b>Masa üstü boy</b><span>[15 × 9 cm teyit]</span></li></ul>')


def tl(n):
    s = '%.2f' % n; a, k = s.split('.')
    return '₺' + '{:,}'.format(int(a)).replace(',', '.') + ',' + k


FENER_BUYUK = ('<svg class="hzm-f" viewBox="0 0 44 120" aria-hidden="true"><path d="M12 18 L22 6 L32 18 Z"></path><rect class="fn" x="14" y="18" width="16" height="11" rx="1"></rect>'
               '<path d="M10 29 H34 V33 H10 Z"></path><path d="M14 33 H30 L35 108 H9 Z"></path><path d="M19 108 V97 a3 3 0 0 1 6 0 V108"></path><circle cx="22" cy="52" r="3"></circle><path d="M4 111 H40"></path></svg>')

IMZA = {
    'af-a': ("""
  <!-- İmza 1 · Feneri yak: oda karanlık; anahtara basınca ışık fenerden yayılır, duvarda ay doğar. 4 sn'de kendiliğinden yanar-söner, dokununca durur. -->
  <section class="bolum px">
    <div class="{{yakCls}}" style="margin-top: 0">
      <img class="k0" src=\"""" + I('af-ay-orta') + """\" alt="">
      <img class="k1" src=\"""" + I('af-ay-orta') + """\" alt="Yanan AyFeneri ve duvardaki ay yansıması">
      <span class="kor" aria-hidden="true"></span>
      <div class="yak-y"><p class="bas-y"><span>Oda karanlık.</span><span>{{yakYazi}}</span></p></div>
      <div class="yak-alt"><p>Tek dokunuş: fener yanar,<br>duvara ay düşer.</p><button class="anahtar" type="button" role="switch" aria-checked="{{yakOn}}" onClick="{{yakSw}}"><b>{{yakEt}}</b><i></i></button></div>
    </div>
    <p class="alt-not">Görsel temsilîdir; ayın büyüklüğü duvara uzaklığa göre değişir.</p>
  </section>
  <!-- İmza 2 · Fener huzmesi: huzme sırayla dört işe döner (3 sn), dokununca o işte durur -->
  <section class="bolum px" style="padding-top: 0">
    <h2 class="bas-y h2">Bir fener,<br>dört iş<span class="n">.</span></h2>
    <ul class="{{hzCls}}">
      """ + FENER_BUYUK + """<span class="hzm-h" aria-hidden="true"></span>
      <sc-for list="{{hz}}" as="h" hint-placeholder-count="4"><li class="{{h.cls}}"><b>{{h.n}}</b><span>{{h.t}}</span><button type="button" onClick="{{h.pick}}" aria-label="{{h.n}}" aria-pressed="{{h.on}}"></button></li></sc-for>
    </ul>
  </section>
"""),
    'af-b': ("""
  <!-- İmza 1 · Bu akşam hangisi: dört mod; görsel ve köşedeki hareketli işaret değişir. 4 sn'de kendiliğinden geçer, dokununca durur. -->
  <section class="bolum px">
    <h2 class="bas-y h2">Bu akşam<br>hangisi<span class="n">?</span></h2>
    <div class="mod">
      <sc-for list="{{mod}}" as="m" hint-placeholder-count="2"><img class="{{m.fcls}}" src="{{m.src}}" alt="{{m.alt}}" style="object-position: {{m.pos}}"></sc-for>
      <div class="mod-sec noscroll"><sc-for list="{{mod}}" as="m" hint-placeholder-count="4"><button class="{{m.scls}}" type="button" onClick="{{m.pick}}" aria-pressed="{{m.on}}">{{m.n}}</button></sc-for></div>
      <div class="{{modY0}}"><span class="mod-i" aria-hidden="true">""" + AY_IK.replace('<path d="M3 24h22" style="stroke-dasharray: 3 3"></path>', '') + """</span><p class="bas-y">Duvarda ay.</p><p>Fenerin tepesinden duvara ay yansır. Masal saati için yeter.</p></div>
      <div class="{{modY1}}"><span class="mod-i" aria-hidden="true"><svg viewBox="0 0 30 30"><g class="isin"><path d="M15 2v5M15 23v5M2 15h5M23 15h5M5.8 5.8l3.5 3.5M20.7 20.7l3.5 3.5M5.8 24.2l3.5-3.5M20.7 9.3l3.5-3.5"></path></g><circle cx="15" cy="15" r="5" style="fill: var(--v)"></circle></svg></span><p class="bas-y">Fener ışığı.</p><p>Tepe ve kapı aralığı sıcak sarı yanar. Odayı aydınlatmaz, yumuşatır.</p></div>
      <div class="{{modY2}}"><span class="mod-i" aria-hidden="true">""" + DALGA.replace('viewBox="0 0 28 28"', 'viewBox="0 0 28 28" style="width: 30px; height: 30px"') + """</span><p class="bas-y">Deniz sesi.</p><p>Dahili deniz sesi modu. Ses seviyesi [teyit].</p></div>
      <div class="{{modY3}}"><span class="mod-i" aria-hidden="true">""" + ESIT + """</span><p class="bas-y">Senin müziğin.</p><p>Telefonu Bluetooth ile bağla; ses gövdedeki hoparlörden gelir.</p></div>
    </div>
    <p class="alt-not">Görseller temsilîdir. Modlar kumandadan da seçilir.</p>
  </section>
  <!-- İmza 2 · Boy kartı: cetvel tabandan tepeye dolar; ölçü teyit bekliyor -->
  <section class="bolum px" style="padding-top: 0">
    <div class="boy">
      <img src=\"""" + I('af-ay-yakin') + """\" alt="Yakından AyFeneri, arkada ay yansıması">
      <span class="boy-c" aria-hidden="true"><i></i></span>
      <div class="boy-y"><p class="bas-y">Komodinine<br>sığar.</p><span><em>[24,2]<small> cm</small></em><p>Boy [teyit] · taban [7,2 cm teyit].<br>Taban sökülür, masaya sabitlenir.</p></span></div>
    </div>
  </section>
"""),
    'gn-a': ("""
  <!-- İmza 1 · Tavanda dönen gök: seçilen disk yavaşça döner (70 sn'de bir tur). 4 sn'de kendiliğinden gezer, dokununca durur. -->
  <section class="koyu bolum" id="diskler">
    <div class="px"><h2 class="bas-y h2">Tavanında<br>dönen gök<span class="n">.</span></h2><p class="alt-b">Bir diske dokun, tavanda yavaşça dönsün.</p></div>
    <div class="kb-s" aria-hidden="true">
      <div class="kubbe"><div class="kubbe-d"><sc-for list="{{disk}}" as="d" hint-placeholder-count="2"><img class="{{d.cls}}" src="{{d.src}}" alt=""></sc-for></div></div>
      <span class="kb-isik"></span>
      <span class="kb-ad"><svg viewBox="0 0 24 24"><path d="M20 12a8 8 0 1 1-2.3-5.6"></path><path d="M20 4v4h-4"></path></svg><b>{{dAd}}</b></span>
    </div>
    <div class="px"><div class="kb-iz"><sc-for list="{{disk}}" as="d" hint-placeholder-count="12"><button class="{{d.bcls}}" type="button" onClick="{{d.pick}}" aria-label="{{d.n}}" aria-pressed="{{d.on}}"><img src="{{d.src}}" alt=""></button></sc-for></div>
    <p class="alt-not">Disk görselleri mağaza afişinden. Kutudaki disk sayısı [teyit: 12 mi, Ay diskiyle 13 mü]. Tavanda daha yumuşak görünür.</p></div>
  </section>
  <!-- İmza 2 · Netlik halkası: görüntü bulanıktan netleşir, halka döner (SSS'deki "bulanık" sorusunun cevabı) -->
  <section class="bolum px">
    <h2 class="bas-y h2">Bulanıksa,<br>halkayı çevir<span class="n">.</span></h2>
    <div class="net"><span class="net-g" aria-hidden="true"><img src=\"""" + I('gn-d03-sarmal-galaksi') + """\" alt=""><svg viewBox="0 0 150 150"><circle cx="75" cy="75" r="70" style="stroke-dasharray: 2 6"></circle><path d="M75 1v10M149 75h-10M75 149v-10M1 75h10"></path></svg></span>
      <span><b>Keskinleşir.</b><span>Netlik halkasını yavaşça çevir. Oda karardıkça ve duvara yaklaştıkça görüntü belirginleşir.</span></span></div>
  </section>
"""),
    'gn-b': ("""
  <!-- Sayfa içi sekmeler (Pococo): uzun sayfada yön bulma; kaydırınca üstte yapışık -->
  <nav class="sekmeler" aria-label="Sayfa bölümleri"><a class="on" href="#odalar">Nasıl</a><a href="#diskler">Diskler</a><a href="#sss">SSS</a><a href="#yorumlar">Yorumlar</a></nav>
  <!-- İmza 1 · Tavan mı, duvar mı: oda kesiti; başlık eğilir, ışık tavandan duvara geçer. 4 sn'de kendiliğinden değişir, dokununca durur. -->
  <section class="bolum px" id="odalar">
    <h2 class="bas-y h2">Tavan mı,<br>duvar mı<span class="n">?</span></h2>
    <div class="{{odaCls}}">
      <span class="oda-z"></span>
      <span class="koni t"></span><span class="koni d"></span>
      <span class="yama t"><img src=\"""" + I('gn-d10-samanyolu') + """\" alt=""></span><span class="yama d"><img src=\"""" + I('gn-d08-kuzey-isigi') + """\" alt=""></span>
      <span class="komo"></span><span class="pj" aria-hidden="true"><i></i></span>
      <div class="oda-sec"><button class="{{tvCls}}" type="button" onClick="{{tvPick}}" aria-pressed="{{tvOn}}">Tavana</button><button class="{{dvCls}}" type="button" onClick="{{dvPick}}" aria-pressed="{{dvOn}}">Duvara</button></div>
    </div>
    <p class="alt-not">Başlık eğilir; yatarken tavana, otururken duvara çevir. Çizim temsilîdir.</p>
  </section>
  <!-- İmza 2 · Disk setleri (Pococo'daki "Set the Mood"): 12 disk üç temada; ilk disk yavaşça döner -->
  <section class="koyu bolum" style="padding-left: 0; padding-right: 0" id="diskler">
    <div class="px"><h2 class="bas-y h2">Kutuda üç<br>ayrı gök<span class="n">.</span></h2><p class="alt-b">[12] disk, üç tema. Her akşam birini seç.</p></div>
    <div class="setler noscroll">
      <div class="set"><div class="set-d"><img src="@@gn-d01-pembe-bulutsu@@" alt=""><img src="@@gn-d02-halka-bulutsu@@" alt=""><img src="@@gn-d04-orion@@" alt=""></div><b>Bulutsular</b><span>Pembe bulutsu, halka bulutsu, Orion, sarmal galaksi</span><small>4 disk</small></div>
      <div class="set"><div class="set-d"><img src="@@gn-d10-samanyolu@@" alt=""><img src="@@gn-d06-yildiz-kumesi@@" alt=""><img src="@@gn-d12-yildizli-gece@@" alt=""></div><b>Yıldızlar</b><span>Samanyolu, Samanyolu kıyısı, yıldız kümesi, yıldızlı gece</span><small>4 disk</small></div>
      <div class="set"><div class="set-d"><img src="@@gn-d09-dolunay@@" alt=""><img src="@@gn-d05-kizil-gezegenler@@" alt=""><img src="@@gn-d08-kuzey-isigi@@" alt=""></div><b>Gök olayları</b><span>Dolunay, kızıl gezegenler, kuzey ışığı, kuyruklu yıldız</span><small>4 disk</small></div>
      <span aria-hidden="true" style="flex: 0 0 6px"></span>
    </div>
    <p class="alt-not px">Disk görselleri mağaza afişinden; set adları sayfa için gruplama. Disk sayısı [teyit].</p>
  </section>
"""),
}


def etiket(yon):
    t = YON[yon]
    return ('<div class="secenek"><b>%s · Yön %s · %s</b><span>%s</span><span class="renk" aria-hidden="true"><i style="background: #1A2142"></i><i style="background: %s"></i><i style="background: %s"></i><i style="background: %s"></i><i style="background: %s"></i></span></div>'
            % ('AyFeneri' if t['urun'] == 'af' else 'Galaksi Night', yon[-1].upper(), t['ad'], t['alt'], t['v'], t['v2'], t['zemin'], t['koyu']))


def js(yon):
    u = YON[yon]['urun']; d = URUN[u]
    gal = [[B + BL[k], n, pos] for k, n, pos in d['gal']]
    mod = [['Ay', I('af-ay'), 'Duvarda ay yansıması', '50% 40%'], ['Fener ışığı', I('af-oda'), 'Gece odasında yanan fener', '50% 40%'],
           ['Deniz sesi', I('af-uyku'), 'Komodinde yanan fener, yatakta uyuyan biri', '62% 50%'], ['Müzik', I('af-urun'), 'Hoparlör ızgaralı fener gövdesi', '50% 30%']]
    hz = [['Duvara ay', 'Fenerin tepesinden ay yansır.'], ['Müzik çalar', 'Bluetooth ile telefondan.'], ['Deniz sesi', 'Dahili ses modu.'], ['Kumandalı', 'Işığı ve modu uzaktan seç.']]
    disk = [[n, I(k)] for n, k in GDISK]
    GUN = [['Pzt', 'Pazartesi', 2], ['Sal', 'Salı', 6], ['Çar', 'Çarşamba', 7], ['Per', 'Perşembe', 0], ['Cum', 'Cuma', 8], ['Cmt', 'Cumartesi', 9], ['Paz', 'Pazar', 5]]
    return """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { g: 0, gOto: true, adet: 1, yak: false, yOto: true, hz: 0, hOto: true, mod: 0, mOto: true, disk: 2, dOto: true, duvar: false, oOto: true, gun: 0, nOto: true, t: 0, now: Date.now() }; }
  componentDidMount() {
    var self = this;
    if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) this.setState({ gOto: false, yOto: false, hOto: false, mOto: false, dOto: false, oOto: false, nOto: false, yak: true });
    // Tek saat: sayaç, galeri (5 sn) ve imza bölümlerinin kendiliğinden geçişleri
    this.iv = setInterval(function () {
      var S = self.state, t = S.t + 1, o = { now: Date.now(), t: t };
      if (S.gOto && t % 5 === 0) self.galGit((S.g + 1) % """ + str(len(gal)) + """);
      if (S.yOto && t % 4 === 0) o.yak = !S.yak;
      if (S.hOto && t % 3 === 0) o.hz = (S.hz + 1) % 4;
      if (S.mOto && t % 4 === 0) o.mod = (S.mod + 1) % 4;
      if (S.dOto && t % 4 === 0) o.disk = (S.disk + 1) % 12;
      if (S.oOto && t % 4 === 0) o.duvar = !S.duvar;
      if (S.nOto && t % 3 === 0) o.gun = (S.gun + 1) % 7;
      self.setState(o);
    }, 1000);
  }
  galGit(i) { var el = document.querySelector('.h-iz'); if (el && el.scrollTo && el.clientWidth) { this.otoKay = Date.now(); el.scrollTo({ left: i * el.clientWidth, behavior: 'smooth' }); } else this.setState({ g: i }); }
  componentDidUpdate() { var el = document.querySelector('.h-iz'); if (el && el.clientWidth && Math.abs(el.scrollLeft - this.state.g * el.clientWidth) > el.clientWidth / 2) { this.otoKay = Date.now(); el.scrollLeft = this.state.g * el.clientWidth; } }
  componentWillUnmount() { clearInterval(this.iv); }
  renderVals() {
    var self = this, S = this.state;
    """ + TL_JS + """
    var GAL = """ + json.dumps(gal, ensure_ascii=False) + """;
    var gal = GAL.map(function (g, i) { var on = i === S.g; return { src: g[0], n: g[1], pos: g[2], ilk: i === 0, cls: 'hs' + (on ? ' on' : ''), dcls: i < S.g ? 'lit' : (on ? 'lit on' : '') }; });
    function gKay(e) { var el = e && (e.currentTarget || e.target); if (!el || !el.clientWidth) return; var i = Math.round(el.scrollLeft / el.clientWidth), o = {};
      if (i !== self.state.g) o.g = i; if (self.state.gOto && Date.now() - (self.otoKay || 0) > 900) o.gOto = false; if (o.g !== undefined || o.gOto === false) self.setState(o); }
    var P1 = """ + str(d['P1']) + """, C1 = """ + str(d['C1']) + """, P2 = """ + str(d['P2']) + """;
    var paket = [
      { n: 1, t: '1 Adet', p: TL(P1, true), old: TL(C1, true), unit: '', sub: '%' + Math.round((1 - P1 / C1) * 100) + ' indirim', rib: false },
      { n: 2, t: '2 Adet', p: TL(P2, true), old: '', unit: 'tanesi ' + TL(Math.floor(P2 / 2 * 100) / 100, true), sub: '2 ayrı almaya göre ' + TL(Math.round((2 * P1 - P2) * 100) / 100, true) + ' daha az', rib: true }
    ].map(function (b) { var on = S.adet === b.n; return { t: b.t, p: b.p, old: b.old, hasOld: !!b.old, unit: b.unit, sub: b.sub, rib: b.rib, two: b.n === 2,
      on: on ? 'true' : 'false', cls: on ? 'pk-k on' : 'pk-k', pick: function () { self.setState({ adet: b.n }); } }; });
    var total = S.adet === 2 ? P2 : P1, online = Math.round(total * 0.95 * 100) / 100;
    // AyFeneri A
    var HZ = """ + json.dumps(hz, ensure_ascii=False) + """;
    var hz = HZ.map(function (h, i) { var on = i === S.hz; return { n: h[0], t: h[1], cls: on ? 'on' : '', on: on ? 'true' : 'false', pick: function () { self.setState({ hz: i, hOto: false }); } }; });
    // AyFeneri B
    var MOD = """ + json.dumps(mod, ensure_ascii=False) + """;
    var mod = MOD.map(function (m, i) { var on = i === S.mod; return { n: m[0], src: m[1], alt: on ? m[2] : '', pos: m[3], fcls: on ? 'mod-f on' : 'mod-f', scls: on ? 'on' : '', on: on ? 'true' : 'false', pick: function () { self.setState({ mod: i, mOto: false }); } }; });
    // Galaksi A
    var DISK = """ + json.dumps(disk, ensure_ascii=False) + """;
    var disk = DISK.map(function (d, i) { var on = i === S.disk; return { n: d[0], src: d[1], on: on ? 'true' : 'false', cls: on ? 'on' : '', bcls: on ? 'on' : '', pick: function () { self.setState({ disk: i, dOto: false }); } }; });
    // Galaksi B
    var GUN = """ + json.dumps(GUN, ensure_ascii=False) + """;
    var gun = GUN.map(function (g, i) { var on = i === S.gun; return { n: g[0], uzun: g[1], d: DISK[g[2]][0], src: DISK[g[2]][1], cls: on ? 'on' : '', icls: on ? 'on' : '', on: on ? 'true' : 'false', pick: function () { self.setState({ gun: i, nOto: false }); } }; });
    var AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
    var now = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kd = new Date(now); do { kd.setDate(kd.getDate() + 1); } while (kd.getDay() === 0 || kd.getDay() === 6);
    var t1 = new Date(kd); t1.setDate(t1.getDate() + 3); var t2 = new Date(kd); t2.setDate(t2.getDate() + 7);
    var teslim = t1.getMonth() === t2.getMonth() ? t1.getDate() + '–' + t2.getDate() + ' ' + AY[t2.getMonth()] : t1.getDate() + ' ' + AY[t1.getMonth()] + '–' + t2.getDate() + ' ' + AY[t2.getMonth()];
    function IKI(n) { return n < 10 ? '0' + n : String(n); }
    var ist = new Date(new Date(S.now || Date.now()).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kalan = Math.max(0, new Date(ist.getFullYear(), ist.getMonth(), ist.getDate(), 23, 59, 59, 999).getTime() - ist.getTime());
    var hh = Math.floor(kalan / 3600000), mi = Math.floor(kalan / 60000) % 60, ss = Math.floor(kalan / 1000) % 60;
    return {
      gal: gal, gNo: S.g + 1, gCount: GAL.length, gKay: gKay, paket: paket,
      onLabel: 'Güvenli Ödeme ile Al · ' + TL(online, true),
      kargo: kd.getDate() + ' ' + AY[kd.getMonth()], teslim: teslim,
      hh: IKI(hh), mm: IKI(mi), ss: IKI(ss), snCls: ss % 2 ? 'sn tA' : 'sn tB', cdAria: 'Bugüne özel fiyatın bitmesine ' + hh + ' saat ' + mi + ' dakika',
      yakCls: S.yak ? 'yak on' : 'yak', yakOn: S.yak ? 'true' : 'false', yakEt: S.yak ? 'Fener açık' : 'Feneri yak', yakYazi: S.yak ? 'Duvarda ay.' : 'Feneri yak.',
      yakSw: function () { self.setState({ yak: !self.state.yak, yOto: false }); },
      hz: hz, hzCls: 'hzm k' + S.hz,
      mod: mod, modY0: S.mod === 0 ? 'mod-y on' : 'mod-y', modY1: S.mod === 1 ? 'mod-y on' : 'mod-y', modY2: S.mod === 2 ? 'mod-y on' : 'mod-y', modY3: S.mod === 3 ? 'mod-y on' : 'mod-y',
      disk: disk, dAd: DISK[S.disk][0],
      odaCls: S.duvar ? 'oda duvar' : 'oda tavan', tvCls: S.duvar ? '' : 'on', dvCls: S.duvar ? 'on' : '', tvOn: S.duvar ? 'false' : 'true', dvOn: S.duvar ? 'true' : 'false',
      tvPick: function () { self.setState({ duvar: false, oOto: false }); }, dvPick: function () { self.setState({ duvar: true, oOto: false }); },
      gun: gun, gunUzun: GUN[S.gun][1], gunDisk: DISK[GUN[S.gun][2]][0]
    };
  }
}"""


def sayfa(yon):
    t = YON[yon]
    govde = '<div class="pg">\n  ' + etiket(yon) + U.SERIT + hero(yon) + al(yon) + IMZA[yon] + '</div>\n'
    govde = re.sub(r'@@([\w-]+)@@', lambda m: I(m.group(1)), govde)
    # Yönün ek CSS'i en sonda: çekirdekteki aynı seçicileri (başlık, fiyat boyu) ezsin
    return U.head('%s · Yön %s %s' % (URUN[t['urun']]['ad'], yon[-1].upper(), t['ad']), tema_css(dict(t, ek='')) + U.CSS + CSS + t.get('ek', '') + '\n', t['font']) + govde


if __name__ == '__main__':
    for yon, t in YON.items():
        h = int(os.environ.get('O_H_' + yon.replace('-', '_'), 2900))
        open(os.path.join(CANVAS, t['dosya']), 'w', encoding='utf-8').write(sayfa(yon) + TAIL.format(h=h, js=js(yon)))
        print('yazıldı:', t['dosya'], h)
