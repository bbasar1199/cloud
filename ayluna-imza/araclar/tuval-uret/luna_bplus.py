# LunaDream ürün sayfası · B+ Gece Postası (tam sayfa). Çalıştır: python3 luna_bplus.py
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL, TL_JS
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamBPlus.dc.html')

CSS = r""".pg{background:#F6F1E9}
/* Sahne (Tur 8, kullanıcı: "görsel kısmı Main'deki gibi, ama bizim ürün görsellerimiz"): gece laciverti zemin, üstte logo,
   kare ürün fotoğrafı kırpılmadan tam genişlik, alt kenarı geceye karışır; diskler fotoğrafın kenarlarında yavaşça süzülür;
   küçük resimler ve sayaç fotoğrafın üstünde; altına yuvarlak köşeli levha biner. "Işığı aç" anahtarı yok (17 Ekim kararı). */
.sahne{position:relative;height:476px;background:#0C1027;overflow:hidden;color:#FFFDF9}
.sahne header{position:absolute;top:0;left:0;right:0;height:56px;display:flex;justify-content:space-between;align-items:center;padding:0 4px;z-index:3;text-shadow:0 1px 8px rgba(12,16,39,.5)}
.sahne .kare-foto{position:absolute;top:0;left:0;width:390px;height:446px}
.sahne .gec{position:absolute;top:0;bottom:0;width:50%;z-index:1;padding:0;border:0;background:transparent;cursor:pointer}
.sahne .kare-foto img{position:absolute;left:0;width:100%;object-fit:cover;transition:opacity .45s cubic-bezier(.2,.7,.2,1)}
.sahne .kare-foto::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,16,39,.72) 0,rgba(12,16,39,.25) 14%,rgba(12,16,39,0) 24%,rgba(12,16,39,0) 78%,rgba(12,16,39,.97) 86.5%,#0C1027 89%);pointer-events:none}
@keyframes suz{0%,100%{transform:translateY(0) rotate(var(--r))}50%{transform:translateY(-10px) rotate(calc(var(--r) + 10deg))}}
.yuzen{position:absolute;z-index:2;border-radius:50%;overflow:hidden;box-shadow:0 10px 18px -8px rgba(0,0,0,.7),0 0 0 2px rgba(255,253,249,.32);animation:suz 7s ease-in-out infinite}
.yuzen img{width:100%;height:100%;object-fit:cover;display:block}
.seritler{position:absolute;left:16px;right:16px;bottom:42px;z-index:3;display:flex;align-items:flex-end;gap:8px}
.kare{flex:none;width:48px;height:48px;padding:0;border-radius:12px;border:2px solid rgba(255,253,249,.28);background:#0C1027;overflow:hidden;cursor:pointer;transition:transform .2s cubic-bezier(.2,.7,.2,1)}
.kare.on{border-color:#FFFDF9}
.kare:active{transform:scale(.94)}
.kare img{display:block;width:100%;height:100%;object-fit:cover}
.sira{flex:none;font-size:13px;font-weight:600;font-variant-numeric:tabular-nums;padding:4px 9px;border-radius:999px;background:#0C1027}
.levha{position:relative;z-index:4;margin-top:-30px;background:#F6F1E9;border-radius:28px 28px 0 0;padding-top:14px}
.ikon{width:48px;height:48px;display:grid;place-items:center;background:transparent;border:0;color:inherit;cursor:pointer}
.yildiz{position:relative;display:inline-block;letter-spacing:1px;color:#D9CDB9;line-height:1}
.yildiz i{position:absolute;left:0;top:0;overflow:hidden;white-space:nowrap;color:#E59A4C;font-style:normal}
.dev{font-family:"Young Serif",Georgia,serif;font-size:56px;line-height:.95;letter-spacing:-.04em;margin:8px 0 0;color:#1A2142;white-space:nowrap}
.dev span,.h2 span.n{color:#E59A4C}
.mkart{display:grid;grid-template-columns:52px minmax(0,1fr);gap:10px;align-items:center;min-height:70px;padding:8px 10px 8px 8px;border-radius:18px;border:1.5px solid #E3D8C7;background:#FFFDF9;font:inherit;color:#1A2142;text-align:left;cursor:pointer;transition:transform .2s cubic-bezier(.2,.7,.2,1)}
.mkart:active,.pk:active,.cip:active{transform:scale(.985)}
.mkart.on{background:#1A2142;border-color:#1A2142;color:#FFFDF9}
.mkart.on .msub{color:#B9BED6}
.mkart .foto{width:52px;height:52px;border-radius:12px;overflow:hidden;background:#EFE6D8}
.mkart .foto img{width:100%;height:100%;object-fit:cover;transform:scale(1.5);transform-origin:50% 62%}
.msub{font-size:12px;color:#5C6078;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
/* Sihirli Özellikler (Tur 7b, kullanıcı V1'i seçti): 2×2 beyaz kart, lacivert ikon kutusu + amber ikon.
   Her kartta üst satır: solda ikon, sağda ürüne özgü küçük canlı gösterge; altında başlık ve tek cümle.
   Döngüler yavaş, yalnız transform/opacity. Canlıda kart ekrana girince 150 ms arayla başlar (IntersectionObserver). */
.sih{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:14px}
.oz{position:relative;isolation:isolate;overflow:hidden;padding:14px;border-radius:20px;display:flex;flex-direction:column;gap:8px;background:#FFFDF9;border:1px solid #EDE3D3;box-shadow:0 10px 26px rgba(26,33,66,.06);color:#1A2142;text-decoration:none}
.oz-ust{display:flex;align-items:center;justify-content:space-between;gap:8px;height:48px;margin-bottom:2px}
.oz .ik{position:relative;width:44px;height:44px;flex:none;border-radius:12px;display:grid;place-items:center;background:#1A2142;color:#F2A65A}
.oz .ik svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.oz .ik.yan::before{content:"";position:absolute;inset:-22px;z-index:-1;border-radius:50%;background:radial-gradient(circle,rgba(242,166,90,.7),rgba(242,166,90,0) 66%);animation:nefes 4.5s ease-in-out infinite}
.oz b{font-size:16px;font-weight:700;line-height:1.25}
.oz .t{font-size:15px;line-height:1.4;color:#5C6078;text-wrap:balance}
.oz .t u{color:#A05A1C;text-underline-offset:3px;white-space:nowrap}
@keyframes nefes{0%,100%{transform:scale(.8);opacity:.45}50%{transform:scale(1.12);opacity:1}}
@keyframes yel{from{transform:rotate(0)}to{transform:rotate(var(--r))}}
.yelpaze{position:relative;width:72px;height:40px}
.yelpaze img{position:absolute;top:2px;width:34px;height:34px;border-radius:50%;object-fit:cover;border:2px solid #FFFDF9;box-shadow:0 0 0 1px #E3D8C7;transform-origin:50% 130%;animation:yel 5s ease-in-out infinite alternate}
.yelpaze img:nth-child(1){right:38px;--r:-12deg}.yelpaze img:nth-child(2){right:19px;--r:0deg;animation-delay:-1.6s}.yelpaze img:nth-child(3){right:0;--r:12deg;animation-delay:-3.2s}
@keyframes ses{0%,100%{transform:scaleY(.3)}50%{transform:scaleY(1)}}
.dalga{display:flex;align-items:flex-end;gap:4px;height:26px}
.dalga i{display:block;width:4px;height:26px;border-radius:2px;background:#E59A4C;transform-origin:50% 100%;animation:ses 2.4s ease-in-out infinite}
.dalga i:nth-child(2){animation-delay:-.4s}.dalga i:nth-child(3){animation-delay:-.8s}.dalga i:nth-child(4){animation-delay:-1.2s}.dalga i:nth-child(5){animation-delay:-1.6s}
/* Pil: dolar, dolu bekler, opacity ile söner; başa sıçrama görünmez */
@keyframes sarj{0%{transform:scaleX(.15);opacity:0}8%{opacity:1}70%{transform:scaleX(1)}90%{transform:scaleX(1);opacity:1}100%{transform:scaleX(1);opacity:0}}
.pil{position:relative;width:46px;height:22px;border:1.6px solid #1A2142;border-radius:6px;padding:2px}
.pil::after{content:"";position:absolute;right:-5px;top:6px;width:3px;height:7px;border-radius:0 2px 2px 0;background:#1A2142}
.pil i{display:block;width:100%;height:100%;border-radius:3px;background:#F2A65A;transform-origin:0 50%;animation:sarj 3.8s ease-in-out infinite}
/* Paket (canlı sitedeki biçim) */
.pk{position:relative;display:block;width:100%;padding:0;border:1.5px solid #E3D8C7;border-radius:20px;background:#FFFDF9;font:inherit;color:#1A2142;text-align:left;cursor:pointer;transition:transform .2s cubic-bezier(.2,.7,.2,1)}
.pk.on{background:#1A2142;border-color:#1A2142;color:#FFFDF9}
.pk-ust{display:grid;grid-template-columns:78px minmax(0,1fr) auto;gap:12px;align-items:center;padding:18px 14px 14px}
.pk-foto{position:relative;width:78px;height:60px}
.lamba{position:absolute;left:0;top:0;width:52px;height:60px;border-radius:14px;overflow:hidden;background:#EFE6D8;border:2px solid #FFFDF9}
.lamba img{width:100%;height:100%;object-fit:cover;transform:scale(1.55);transform-origin:50% 60%}
.lamba.iki{left:26px}
.pk.on .lamba{border-color:#1A2142}
.pk-ad{font-size:24px;font-weight:700;letter-spacing:-.02em}
.pk-sub{font-size:13px;opacity:.75;margin-top:2px}
.pk-fiyat{font-size:21px;font-weight:700;letter-spacing:-.02em}
.pk.on .pk-fiyat{color:#F2A65A}
.pk-eski{font-size:13px;opacity:.7;margin-top:3px}
.pk-hediye{display:block;padding:10px 14px;font-size:14px;font-weight:700;background:#F3E9DA;color:#8A4A12;border-radius:0 0 18.5px 18.5px}
.pk.on .pk-hediye{background:#F2A65A;color:#1A2142}
.kurdele{position:absolute;right:14px;top:-13px;z-index:1;padding:3px 12px;border-radius:999px;background:#F2A65A;color:#1A2142;font-size:12px;font-weight:700;box-shadow:0 0 0 3px #F6F1E9}
.btn-on{display:flex;align-items:center;justify-content:center;width:100%;min-height:62px;margin-top:20px;border:0;border-radius:20px;background:#F2A65A;color:#1A2142;font:inherit;font-size:18px;font-weight:700;cursor:pointer;box-shadow:0 6px 0 #C97F38;transition:transform .12s cubic-bezier(.2,.7,.2,1)}
.btn-on:active{transform:translateY(4px)}
.btn-kp{display:flex;align-items:center;justify-content:center;width:100%;min-height:56px;margin-top:14px;border:2px solid #1A2142;border-radius:20px;background:transparent;color:#1A2142;font:inherit;font-size:17px;font-weight:600;cursor:pointer}
.bnot{margin:7px 0 0;text-align:center;font-size:13px;color:#5C6078}
.yol{position:relative;list-style:none;padding:0;margin:24px 0 0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr))}
.yol::before{content:"";position:absolute;left:16.6%;right:16.6%;top:13px;border-top:1.5px dashed #C9BFAE}
.yol li{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;gap:2px}
.yol li::before{content:"";width:26px;height:26px;border-radius:50%;background:#F6F1E9;border:1.5px solid #1A2142;margin-bottom:6px;box-shadow:inset 0 0 0 5px #F6F1E9,inset 0 0 0 13px #E3D8C7}
.yol li:first-child::before{box-shadow:inset 0 0 0 5px #F6F1E9,inset 0 0 0 13px #F2A65A}
.yol b{font-size:15px;font-weight:700}
.yol span{font-size:12.5px;color:#5C6078}
.guven{display:flex;justify-content:center;flex-wrap:wrap;gap:6px 14px;margin-top:20px;padding:12px 0;border-top:1px solid #E3D8C7;border-bottom:1px solid #E3D8C7;font-size:13.5px;font-weight:600}
.guven span+span::before{content:"·";margin-right:14px;color:#E59A4C}
/* Bölümler */
.bolum{padding-top:52px}
.ust-yazi{margin:0 0 6px;font-size:13px;font-weight:700;color:#A05A1C}
.gece{background:#1A2142;color:#EDE5D8;padding:44px 0 46px;margin-top:52px}
.an{position:relative;flex:0 0 270px;height:420px;border-radius:24px;overflow:hidden;background:#0C1027;scroll-snap-align:start}
.an img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.an .saat{position:absolute;left:16px;top:14px;font-family:"Young Serif",Georgia,serif;font-size:46px;line-height:1;color:#F2A65A;font-variant-numeric:tabular-nums}
.an .alt2{position:absolute;left:16px;right:16px;bottom:16px;display:flex;flex-direction:column;gap:4px}
.cip{display:inline-flex;align-items:center;min-height:48px;padding:0 18px;border-radius:999px;border:1.5px solid #1A2142;background:transparent;color:#1A2142;font:inherit;font-size:15px;font-weight:600;cursor:pointer;white-space:nowrap}
.cip.on{background:#1A2142;color:#FFFDF9}
.tavan{position:relative;height:300px;border-radius:24px;overflow:hidden;background:radial-gradient(120% 90% at 50% 30%,#232B55 0%,#141A36 60%,#0C1027 100%)}
.yansima{position:absolute;left:50%;top:42%;width:230px;height:230px;margin:-115px 0 0 -115px;border-radius:50%;overflow:hidden;opacity:0;transform:scale(.92);transition:opacity .6s cubic-bezier(.2,.7,.2,1),transform .6s cubic-bezier(.2,.7,.2,1);-webkit-mask-image:radial-gradient(closest-side,#000 62%,transparent 100%);mask-image:radial-gradient(closest-side,#000 62%,transparent 100%)}
.yansima.on{opacity:.92;transform:none}
.yansima img{width:100%;height:100%;object-fit:cover;display:block}
.dbtn{display:flex;flex-direction:column;align-items:center;gap:6px;background:transparent;border:0;padding:0;cursor:pointer;color:#B9BED6;font:inherit;font-size:12px;width:64px;min-height:88px;flex:none}
.dbtn img{width:54px;height:54px;border-radius:50%;object-fit:cover;outline:2px solid transparent;outline-offset:3px;transition:transform .25s cubic-bezier(.2,.7,.2,1)}
.dbtn.on{color:#FFFDF9;font-weight:600}
.dbtn.on img{outline-color:#F2A65A;transform:translateY(-4px)}
.otuz{display:grid;grid-template-columns:auto minmax(0,1fr);gap:16px;align-items:center;padding:20px;border-radius:24px;background:#F2A65A;color:#1A2142}
.otuz b.say{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:88px;line-height:.8;letter-spacing:-.04em}
.sss{border-bottom:1.5px solid #E3D8C7}
.sss summary{list-style:none;display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:60px;font-weight:700;font-size:16px;cursor:pointer}
.sss summary::-webkit-details-marker{display:none}
.sss .arti{width:32px;height:32px;border-radius:50%;background:#1A2142;color:#FFFDF9;display:grid;place-items:center;flex:none;transition:transform .2s}
.sss[open] .arti{transform:rotate(45deg)}
.kart{flex:0 0 168px;scroll-snap-align:start;background:#FFFDF9;border-radius:20px;border:1.5px solid #E3D8C7;overflow:hidden;display:flex;flex-direction:column;text-decoration:none;color:#1A2142}
.alt-bilgi{background:#1A2142;color:#C9CDE0;margin-top:56px;padding:40px 0 100px}
.alt-bilgi a{color:#FFFDF9;text-decoration:none;display:flex;align-items:center;min-height:48px}
.yapis{position:sticky;bottom:0;z-index:5;margin-top:-76px;height:76px;padding:0 12px;background:#1A2142;display:flex;align-items:center;gap:10px;border-radius:20px 20px 0 0}
/* Baskı unsurları (Tur 9, kullanıcı: "baskılayıcıları arttıralım"): yalnız gerçek veriyle, veri yoksa gizlenir.
   Sayaç: kampanya bitiş tarihi (tema ayarı). Stok: Shopify envanteri eşik altındaysa. Dün: Shopify Flow'un yazdığı metafield. */
.sayac2{display:flex;justify-content:space-between;align-items:center;gap:10px;min-height:44px;margin-top:12px;padding:0 12px;border-radius:14px;background:#1A2142;color:#FFFDF9;font-size:13.5px;font-weight:600}
.sayac2 b{font-variant-numeric:tabular-nums;color:#F2A65A;font-weight:700;white-space:nowrap}
.canli{list-style:none;margin:16px 0 0;padding:0;display:flex;flex-direction:column;gap:8px;font-size:14.5px;color:#1A2142}
.canli li{display:flex;align-items:center;gap:10px}
@keyframes nabiz{0%,100%{opacity:1}50%{opacity:.3}}
.canli i{flex:none;width:8px;height:8px;border-radius:50%;animation:nabiz 1.8s ease-in-out 3}
/* Videolar: canlıda blok başına bir Shopify videosu; ekrandayken sessiz döner, dokununca sesli tam ekran */
.vid{position:relative;flex:0 0 172px;height:306px;scroll-snap-align:start;padding:0;border:0;border-radius:20px;overflow:hidden;background:#1A2142;cursor:pointer;color:#FFFDF9;text-align:left;font:inherit}
.vid img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.vid::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(12,16,39,.88) 0,rgba(12,16,39,0) 52%)}
.vid-oyna{position:absolute;left:50%;top:42%;z-index:1;width:56px;height:56px;margin:-28px 0 0 -28px;border-radius:50%;display:grid;place-items:center;background:rgba(255,253,249,.94);box-shadow:0 6px 16px rgba(12,16,39,.35)}
.vid-oyna svg{width:22px;height:22px;fill:#1A2142;margin-left:3px}
.vid-alt{position:absolute;left:12px;right:12px;bottom:12px;z-index:1;display:flex;flex-direction:column;gap:2px;line-height:1.25}
.vid-alt b{font-size:15px}
.vid-alt span{font-size:12.5px;color:#D9DCEB}
.vid-etiket{position:absolute;left:10px;top:10px;z-index:1;font-size:12px;font-weight:600;padding:2px 8px;border-radius:999px;background:rgba(12,16,39,.6)}
/* Yorum duvarı: müşteri fotoğrafları + konu çipleri + kaydırmalı yorum kartları (metinler Loox'tan birebir) */
.mf{flex:none;width:84px;height:84px;padding:0;border:0;border-radius:16px;overflow:hidden;background:#EDE3D3;cursor:pointer}
.mf img{width:100%;height:100%;object-fit:cover;display:block}
.yk2{flex:0 0 284px;scroll-snap-align:start;margin:0;min-height:200px;padding:18px 16px 16px;border-radius:20px;background:#FFFDF9;border:1px solid #E3D8C7;display:flex;flex-direction:column;gap:10px;color:#1A2142}
.yk2 .tirnak{font-family:"Young Serif",Georgia,serif;font-size:44px;line-height:.6;color:#E59A4C;height:20px}
.yk2 q{font-family:"Young Serif",Georgia,serif;font-size:18px;line-height:1.3;quotes:none;flex:1}
.yk2 figcaption{display:flex;align-items:center;justify-content:space-between;gap:8px;font-size:13.5px}
.yk2 .dog{display:inline-flex;align-items:center;gap:4px;font-size:12.5px;font-weight:600;color:#2E6B4F}
.yk2 .konu{align-self:flex-start;font-size:12px;font-weight:600;padding:3px 10px;border-radius:999px;background:#F3E9DA;color:#5C5245}
.noscroll{scrollbar-width:none}.noscroll::-webkit-scrollbar{display:none}"""

STAR = '<span class="yildiz" aria-hidden="true">★★★★★<i style="width: {{starPct}}%">★★★★★</i></span>'
LOGO = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M15.5 3.5a8.5 8.5 0 1 0 5 15.4A7 7 0 0 1 15.5 3.5z" fill="#F2A65A"></path></svg>'

HTML = """<div class="pg" style="padding-bottom: 0">
  <!-- Sahne: oda sahneleri logo bandının altına kadar uzanır (tek parça); yazılı afişler bandın altından başlar (çift logo/yazı çakışması olmasın) -->
  <section class="sahne" aria-label="LunaDream fotoğrafları">
    <header><button class="ikon" aria-label="Menü"><svg class="ico" viewBox="0 0 24 24"><path d="M4 8h16M4 16h11"></path></svg></button><span style="display: flex; align-items: center; gap: 6px">""" + LOGO + """<span class="ser" style="font-size: 22px">Ayluna</span></span><button class="ikon" aria-label="Sepet"><svg class="ico" viewBox="0 0 24 24"><path d="M6 8h12l-1 12H7z"></path><path d="M9 8a3 3 0 0 1 6 0"></path></svg></button></header>
    <div class="kare-foto"><sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><img src="{{f.src}}" alt="{{f.n}}" style="opacity: {{f.op}}; object-position: {{f.pos}}; top: {{f.top}}px; height: {{f.h}}px"></sc-for><button class="gec" style="left: 0" onClick="{{gPrev}}" aria-label="Önceki fotoğraf"></button><button class="gec" style="right: 0" onClick="{{gNext}}" aria-label="Sonraki fotoğraf"></button></div>
    <!-- Süzülen hediye diskleri: fotoğrafın kenarlarında, ürünü kapatmaz -->
    <sc-for list="{{tiles}}" as="t" hint-placeholder-count="2"><span class="yuzen" aria-hidden="true" style="left: {{t.x}}px; top: {{t.y}}px; width: {{t.s}}px; height: {{t.s}}px; --r: {{t.r}}deg; animation-delay: {{t.d}}s"><img src="{{t.src}}" alt=""></span></sc-for>
    <div class="seritler">
      <div class="noscroll" style="display: flex; gap: 6px; flex: 1; min-width: 0; overflow-x: auto; padding: 2px; -webkit-mask-image: linear-gradient(90deg, #000 calc(100% - 24px), transparent); mask-image: linear-gradient(90deg, #000 calc(100% - 24px), transparent)">
        <sc-for list="{{gal}}" as="f" hint-placeholder-count="7"><button class="{{f.cls}}" onClick="{{f.pick}}" aria-label="{{f.n}}" aria-pressed="{{f.on}}"><img src="{{f.src}}" alt=""></button></sc-for>
      </div>
      <span class="sira">{{gNo}}/{{gCount}}</span>
    </div>
  </section>

  <section class="px levha" id="siparis">
    <!-- Puan ve sayı canlıda Loox'tan; veri yoksa gizlenir. "Stokta" Shopify stok bilgisinden; stok yoksa görünmez -->
    <div style="display: flex; justify-content: space-between; align-items: center; gap: 10px">
      <a href="#yorumlar" style="display: inline-flex; align-items: center; gap: 6px; min-height: 48px; font-size: 13.5px; text-decoration: none; color: #5C6078">""" + STAR + """<b style="color: #1A2142">{{rating}}</b> · {{reviews}} yorum</a>
      <span style="display: inline-flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600; color: #2E6B4F"><span aria-hidden="true" style="width: 7px; height: 7px; border-radius: 50%; background: #3B8A63"></span>Stokta</span>
    </div>
    <h1 class="dev">LunaDream<span>.</span></h1>
    <p style="margin: 12px 0 0; display: flex; align-items: baseline; flex-wrap: wrap; gap: 4px 10px; font-variant-numeric: tabular-nums"><b style="font-size: 24px; letter-spacing: -.02em">{{p1}}</b><s style="font-size: 15px; color: #5C6078">{{c1}}</s><span style="font-size: 14px; font-weight: 600; color: #2E6B4F">kartla {{p1on}}</span></p>
    <!-- Bugünkü fiyat sayacı: her gece 23:59'da (İstanbul) sıfırlanır. Toptancı zammı gün içinde gelse de o günün fiyatı 23:59'a kadar korunur. -->
    <div class="sayac2" role="timer" aria-label="{{cdAria}}"><span style="display: flex; align-items: center; gap: 8px; min-width: 0">""" + LOGO.replace('width="20" height="20"','width="16" height="16"') + """<span style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{{cdLine}}</span></span><b>{{cdShort}}</b></div>
    <p style="margin: 6px 2px 0; font-size: 12.5px; color: #5C6078">Toptancı zammı gelirse fiyat ertesi gün güncellenir.</p>

    <!-- Sihirli Özellikler: fiyatın hemen altında; model seçimi bunun altında (Tur 9, kullanıcı isteği). V1 Sade beyaz -->
    <p class="ust-yazi" style="margin-top: 26px">Sihirli özellikler</p>
    <h2 class="h2" style="font-size: 26px">Uyku vakti savaş değil,<br>minik bir masal<span class="n">.</span></h2>
    <div class="sih">
      <div class="oz"><span class="oz-ust" aria-hidden="true"><span class="ik yan"><svg viewBox="0 0 24 24"><path d="M15.5 3.5a8.5 8.5 0 1 0 5 15.4A7 7 0 0 1 15.5 3.5z"></path></svg></span></span><b>Mışıl mışıl uykular</b><span class="t">Odayı loş, sıcak bir ışıkla aydınlatır.</span></div>
      <a class="oz" href="#diskler"><span class="oz-ust" aria-hidden="true"><span class="ik"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="2.5"></circle><path d="M12 3a9 9 0 0 1 9 9"></path></svg></span><span class="yelpaze"><img src="/_blob/a24f13e032569f76d64b9b0fbe8d74f7" alt=""><img src="/_blob/b088d2c82561b76f6db997fbc3944059" alt=""><img src="/_blob/04ed9ce4ae8a36619975caa7d2de9ad8" alt=""></span></span><b>6 + 6 masal diski</b><span class="t">Altısı hediye. <u>Diskleri gör</u></span></a>
      <sc-if value="{{kiz}}" hint-placeholder-val="{{true}}"><div class="oz"><span class="oz-ust" aria-hidden="true"><span class="ik"><svg viewBox="0 0 24 24"><path d="M9 17V6l10-2v11"></path><circle cx="6.5" cy="17" r="2.5"></circle><circle cx="16.5" cy="15" r="2.5"></circle></svg></span><span class="dalga"><i></i><i></i><i></i><i></i><i></i></span></span><b>Bluetooth ninni</b><span class="t">Telefondan bağlan, lambadan çalsın.</span></div></sc-if>
      <sc-if value="{{erkek}}" hint-placeholder-val="{{false}}"><div class="oz"><span class="oz-ust" aria-hidden="true"><span class="ik"><svg viewBox="0 0 24 24"><path d="M9 17V6l10-2v11"></path><circle cx="6.5" cy="17" r="2.5"></circle><circle cx="16.5" cy="15" r="2.5"></circle></svg></span><span class="dalga"><i></i><i></i><i></i><i></i><i></i></span></span><b>Ninnili robot</b><span class="t">Uyku öncesi ninni çalar.</span></div></sc-if>
      <div class="oz"><span class="oz-ust" aria-hidden="true"><span class="ik"><svg viewBox="0 0 24 24"><rect x="2" y="7" width="17" height="10" rx="2"></rect><path d="M22 11v2M6 10v4M10 10v4"></path></svg></span><span class="pil"><i></i></span></span><b>Kablosuz kullanım</b><span class="t">Şarj et, her yere taşı.</span></div>
    </div>

    <div class="etiket" style="margin-top: 28px"><span>Model</span><b>{{modelName}}</b></div>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-top: 8px">
      <sc-for list="{{models}}" as="m" hint-placeholder-count="2">
        <button class="{{m.cls}}" onClick="{{m.pick}}" aria-pressed="{{m.on}}"><span class="foto"><img src="{{m.src}}" alt=""></span><span style="display: flex; flex-direction: column; min-width: 0; line-height: 1.2"><b style="font-size: 14px; font-weight: 600">{{m.n}}</b><span class="msub">{{m.sub}}</span></span></button>
      </sc-for>
    </div>

    <div class="etiket" style="margin-top: 28px"><span>Paket</span><span style="font-weight: 600">Kampanya · [tarih aralığı]</span></div>
    <div style="display: flex; flex-direction: column; gap: 16px; margin-top: 14px">
      <sc-for list="{{paket}}" as="b" hint-placeholder-count="2">
        <button class="{{b.cls}}" onClick="{{b.pick}}" aria-pressed="{{b.on}}">
          <sc-if value="{{b.rib}}" hint-placeholder-val="{{false}}"><span class="kurdele">En Çok Tercih Edilen</span></sc-if>
          <span class="pk-ust">
            <span class="pk-foto"><span class="lamba"><img src="{{modelSrc}}" alt=""></span><sc-if value="{{b.two}}" hint-placeholder-val="{{false}}"><span class="lamba iki"><img src="{{modelSrc}}" alt=""></span></sc-if></span>
            <span style="display: flex; flex-direction: column; min-width: 0; line-height: 1.2"><b class="pk-ad">{{b.t}}</b><span class="pk-sub">{{b.sub}}</span></span>
            <span style="display: flex; flex-direction: column; align-items: flex-end; line-height: 1.15; font-variant-numeric: tabular-nums"><b class="pk-fiyat">{{b.p}}</b><sc-if value="{{b.hasOld}}" hint-placeholder-val="{{true}}"><s class="pk-eski">{{b.old}}</s></sc-if><sc-if value="{{b.hasUnit}}" hint-placeholder-val="{{false}}"><span class="pk-eski">{{b.unit}}</span></sc-if></span>
          </span>
          <span class="pk-hediye">+ 6 Tane Ücretsiz Hediye Disk</span>
        </button>
      </sc-for>
    </div>

    <!-- Stok: Shopify envanteri eşiğin (tema ayarı) altındaysa görünür. Dün: Shopify Flow her gece metafield'e yazar; sayı yoksa ya da 3'ten azsa satır gizli. -->
    <ul class="canli">
      <li><i style="background: #E59A4C"></i><span>Stokta son <b>[X]</b> adet</span></li>
      <li><i style="background: #3B8A63"></i><span>Dün <b>[X]</b> aile sipariş verdi</span></li>
    </ul>
    <button class="btn-on" type="button">{{onLabel}}</button>
    <p class="bnot">{{onNote}}</p>
    <!-- Canlıda kapıda ödeme uygulamasının formunu açar (uygulama korunur; ek ürünler ve ₺80 ücret orada). -->
    <button class="btn-kp" type="button">Kapıda Ödeme ile Sipariş Ver</button>
    <p class="bnot">{{kpNote}}</p>
    <ol class="yol" aria-label="Siparişten teslime"><li><b>Bugün</b><span>Siparişin alındı</span></li><li><b>{{kargo}}</b><span>Kargoda</span></li><li><b>{{teslim}}</b><span>Kapında</span></li></ol>
    <p class="guven"><span>Ücretsiz kargo</span><span>30 gün iade</span><span>Güvenli ödeme</span></p>
  </section>

  <!-- Videolar: canlıda bloklar = Shopify videoları (kapak = videonun kendi ilk karesi). Video yoksa bölüm hiç görünmez. Ekrandayken sessiz döner; dokununca sesli, tam ekran. -->
  <section class="bolum" id="videolar">
    <div class="px"><p class="ust-yazi">Videolar</p><h2 class="h2">Işık kapanınca<br>ne oluyor<span class="n">?</span></h2></div>
    <div class="noscroll" style="display: flex; gap: 10px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-left: 16px; padding: 16px 16px 0">
      <sc-for list="{{vids}}" as="v" hint-placeholder-count="4"><button class="vid" type="button" aria-label="{{v.t}}: videoyu oynat"><img src="{{v.src}}" alt="" style="object-position: {{v.pos}}"><span class="vid-etiket">[video]</span><span class="vid-oyna" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l11-6.5z"></path></svg></span><span class="vid-alt"><b>{{v.t}}</b><span>{{v.k}}</span></span></button></sc-for>
      <span aria-hidden="true" style="flex: 0 0 6px"></span>
    </div>
  </section>

  <!-- Bir gece, beş an -->
  <section class="gece">
    <div class="px"><p class="ust-yazi" style="color: #F2A65A">Nasıl kullanılır</p><h2 class="h2" style="color: #FFFDF9">Bir gece, beş an<span class="n">.</span></h2></div>
    <div class="noscroll" style="display: flex; gap: 12px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-left: 16px; padding: 18px 16px 0">
      <!-- Canlıda: kısa sessiz döngü videolar (onizleme/v/), yalnız ekrandayken oynar -->
      <sc-for list="{{moments}}" as="a" hint-placeholder-count="5">
        <article class="an"><img src="{{a.src}}" alt="{{a.alt}}" style="object-position: {{a.pos}}"><span aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(0deg, rgba(12,16,39,.88) 0%, rgba(12,16,39,0) 55%)"></span><span class="saat">{{a.t}}</span><span class="alt2"><b style="font-size: 20px; color: #FFFDF9">{{a.title}}</b><span style="font-size: 14px; color: #B9BED6">{{a.text}}</span></span></article>
      </sc-for>
      <span aria-hidden="true" style="flex: 0 0 4px"></span>
    </div>
  </section>

  <!-- Yorum duvarı: puan ve sayı Loox'tan; kartlar Loox'taki gerçek yorumlardan birebir seçilir (blok). "Satın aldı" yalnız Loox'un doğruladığı yorumda. Fotoğraflar Loox foto yorumlarından. -->
  <section id="yorumlar" class="bolum">
    <div class="px" style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px"><h2 class="h2">Aileler<br>ne diyor<span class="n">.</span></h2><span style="display: flex; flex-direction: column; align-items: flex-end; line-height: 1"><b class="ser" style="font-size: 52px; font-weight: 400">{{rating}}</b><span style="margin-top: 6px">""" + STAR + """</span><span style="font-size: 13px; color: #5C6078; margin-top: 4px">{{reviews}} yorum</span></span></div>
    <p class="px" style="margin: 18px 0 0; font-size: 13px; font-weight: 700; color: #766B5B">Müşteri fotoğrafları</p>
    <div class="noscroll" style="display: flex; gap: 8px; overflow-x: auto; padding: 8px 16px 0">
      <sc-for list="{{mfoto}}" as="f" hint-placeholder-count="5"><button class="mf" type="button" aria-label="Müşteri fotoğrafını büyüt"><img src="{{f.src}}" alt="{{f.alt}}"></button></sc-for>
    </div>
    <div class="noscroll" style="display: flex; gap: 8px; overflow-x: auto; padding: 16px 16px 0">
      <sc-for list="{{topics}}" as="t" hint-placeholder-count="4"><button class="{{t.cls}}" onClick="{{t.pick}}" aria-pressed="{{t.on}}">{{t.n}}</button></sc-for>
    </div>
    <div class="noscroll" style="display: flex; gap: 10px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-left: 16px; padding: 14px 16px 2px">
      <sc-for list="{{revs}}" as="r" hint-placeholder-count="3">
        <figure class="yk2"><span class="konu">{{r.tags}}</span><span class="tirnak" aria-hidden="true">“</span><q>{{r.q}}</q><figcaption><b>{{r.name}}</b><span class="dog"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg>Satın aldı</span></figcaption></figure>
      </sc-for>
      <span aria-hidden="true" style="flex: 0 0 6px"></span>
    </div>
    <div class="px"><a href="#" class="cip" style="display: flex; justify-content: center; margin-top: 14px">{{reviews}} yorumun hepsini oku</a>
    <p style="margin: 10px 0 0; font-size: 12.5px; color: #5C6078; text-align: center">Yorumlar yalnız Ayluna'dan sipariş verenlerden toplanır; hepsi yayımlanır.</p></div>
  </section>

  <!-- Diskler: tavana yansıt -->
  <section class="gece" id="diskler" style="margin-top: 52px">
    <div class="px"><h2 class="h2" style="color: #FFFDF9">Altı masal kutuda,<br>altısı hediye<span class="n">.</span></h2><p style="margin: 8px 0 0; font-size: 15px; color: #B9BED6">Diski seç, tavanda gör.</p></div>
    <div class="px" style="margin-top: 16px"><div class="tavan">
      <sc-for list="{{proj}}" as="p" hint-placeholder-count="2"><span class="{{p.cls}}" aria-hidden="true"><img src="{{p.src}}" alt=""></span></sc-for>
      <span style="position: absolute; left: 12px; top: 12px; font-size: 12px; font-weight: 600; color: #FFFDF9; background: rgba(12,16,39,.6); padding: 3px 9px; border-radius: 999px">[gerçek tavan fotoğrafı]</span>
      <span style="position: absolute; left: 14px; bottom: 14px; display: flex; flex-direction: column; line-height: 1.2; color: #FFFDF9"><span style="font-size: 12px; color: #B9BED6">Disk</span><b class="ser" style="font-size: 22px; font-weight: 400">{{discName}}</b></span>
    </div></div>
    <div class="noscroll" style="display: flex; gap: 6px; overflow-x: auto; padding: 14px 16px 0">
      <sc-for list="{{discs}}" as="d" hint-placeholder-count="11"><button class="{{d.cls}}" onClick="{{d.pick}}" aria-pressed="{{d.on}}" aria-label="{{d.n}} diskini tavanda göster"><img src="{{d.src}}" alt=""><span>{{d.n}}</span></button></sc-for>
    </div>
    <p class="px" style="margin: 10px 0 0; font-size: 12.5px; color: #B9BED6">[Hangi 6 diskin kutuda, hangisinin hediye olduğu teyit edilecek.]</p>
  </section>

  <!-- Kutuda ne var -->
  <section class="px bolum">
    <h2 class="h2">Kutudan<br>ne çıkıyor<span class="n">.</span></h2>
    <div style="display: grid; grid-template-columns: 150px minmax(0, 1fr); gap: 14px; align-items: center; margin-top: 16px">
      <div style="height: 200px; border-radius: 20px; overflow: hidden; background: #EDE3D3"><img src="/_blob/54f170c0696110348e309338400f7cc7" alt="Elde tutulan LunaDream" style="width: 100%; height: 100%; object-fit: cover"></div>
      <ul style="list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 8px; font-size: 15px">
        <li><b>1</b> {{boxModel}}</li><li><b>6</b> masal diski</li><li><b>+6</b> hediye disk</li><li><b>1</b> USB şarj kablosu</li>
        <li style="color: #5C6078; font-size: 13.5px; padding-top: 6px; border-top: 1px dashed #D9CDB9">Boyut [X] cm · Pil [X] saat</li>
      </ul>
    </div>
  </section>

  <!-- 30 gün iade -->
  <section class="px bolum">
    <div class="otuz"><b class="say">30</b><span style="display: flex; flex-direction: column; gap: 6px"><b style="font-size: 20px; line-height: 1.2">gün içinde iade</b><span style="font-size: 14px; line-height: 1.4">İlk 14 gün yasal cayma hakkın; Ayluna bunu 30 güne uzatır.</span></span></div>
  </section>

  <!-- SSS -->
  <section class="px bolum">
    <h2 class="h2">Merak<br>edilenler<span class="n">.</span></h2>
    <div style="margin-top: 14px; border-top: 1.5px solid #E3D8C7">
      <sc-for list="{{faq}}" as="f" hint-placeholder-count="6"><details class="sss"><summary>{{f.q}}<span class="arti" aria-hidden="true">+</span></summary><p style="margin: 0 0 16px; font-size: 15px; color: #3A3F5A">{{f.a}}</p></details></sc-for>
    </div>
  </section>

  <!-- Diğer ürünler -->
  <section class="bolum">
    <div class="px" style="display: flex; align-items: flex-end; justify-content: space-between"><h2 class="h2">Odanın geri<br>kalanı için<span class="n">.</span></h2><span style="font-size: 13px; color: #5C6078">{{shopCount}} ürün</span></div>
    <div class="noscroll" style="display: flex; gap: 10px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-left: 16px; padding: 14px 16px 4px">
      <sc-for list="{{shop}}" as="u" hint-placeholder-count="4">
        <a class="kart" href="#"><span style="position: relative; aspect-ratio: 1 / 1; background: #EDE3D3; overflow: hidden"><img src="{{u.src}}" alt="{{u.n}}" style="width: 100%; height: 100%; object-fit: cover; display: block"><sc-if value="{{u.pct}}" hint-placeholder-val="{{true}}"><span style="position: absolute; left: 8px; top: 8px; font-size: 12px; font-weight: 700; background: #F2A65A; color: #1A2142; padding: 2px 8px; border-radius: 999px">{{u.pct}}</span></sc-if></span><span style="padding: 10px 12px 12px; display: flex; flex-direction: column; gap: 4px"><b style="font-size: 14px; font-weight: 600; line-height: 1.25; min-height: 35px">{{u.n}}</b><span style="display: flex; align-items: baseline; gap: 6px; font-variant-numeric: tabular-nums"><b style="font-size: 15px">{{u.price}}</b><s style="font-size: 12px; color: #5C6078">{{u.old}}</s></span></span></a>
      </sc-for>
    </div>
  </section>

  <!-- Alt bilgi -->
  <footer class="alt-bilgi">
    <div class="px">
      <h2 class="h2" style="color: #FFFDF9">İlk geceyi<br>birlikte izleyin<span class="n">.</span></h2>
      <button class="btn-on" type="button" style="margin-top: 16px">{{onLabel}}</button>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0 16px; margin-top: 24px; font-size: 14px"><a href="#">Mesafeli Satış Sözleşmesi</a><a href="#">KVKK</a><a href="#">İade Politikası</a><a href="#">İletişim</a></div>
      <p style="margin: 14px 0 0; font-size: 13px; line-height: 1.5">[Ticaret unvanı] · MERSİS [no]<br>[Adres] · [e-posta] · [telefon] · KEP [adres]</p>
      <div aria-label="Ayluna" style="margin-top: 22px; display: flex; align-items: flex-end; gap: 6px; color: #F3E9DA"><span class="ser" aria-hidden="true" style="font-size: 100px; line-height: .8; letter-spacing: -.045em">Ayluna</span><svg width="40" height="40" viewBox="0 0 24 24" aria-hidden="true" style="margin-bottom: 8px; flex: none"><path d="M15.5 3.5a8.5 8.5 0 1 0 5 15.4A7 7 0 0 1 15.5 3.5z" fill="#F2A65A"></path></svg></div>
      <p style="margin: 14px 0 0; padding-top: 14px; border-top: 1px solid rgba(255,255,255,.12); font-size: 12px; color: #8E94B3">Fiyatlara KDV dahildir. © 2026 Ayluna</p>
    </div>
  </footer>

  <!-- Yapışkan çubuk: canlıda sayfa başından görünür, paket ve buton alanı ekrandayken gizlenir (IntersectionObserver); padding-bottom: env(safe-area-inset-bottom) -->
  <div class="yapis">
    <span style="flex: none; width: 46px; height: 46px; border-radius: 12px; overflow: hidden; background: #EFE6D8"><img src="{{modelSrc}}" alt="" style="width: 100%; height: 100%; object-fit: cover; transform: scale(1.5); transform-origin: 50% 62%"></span>
    <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; line-height: 1.15; color: #FFFDF9; font-variant-numeric: tabular-nums"><b style="font-size: 17px">{{onPrice}}</b><span style="font-size: 12px; color: #B9BED6">{{adetName}} · kartla</span><span style="font-size: 12px; color: #F2A65A">{{cdTiny}}</span></span>
    <button class="btn-on" type="button" style="flex: 0 0 150px; width: 150px; min-height: 52px; margin: 0; font-size: 16px; box-shadow: 0 4px 0 #C97F38">Satın al</button>
  </div>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { g: 0, model: 'kiz', adet: 2, topic: 'Tümü', disc: 1, now: Date.now() }; }
  componentDidMount() { var self = this; this.iv = setInterval(function () { self.setState({ now: Date.now() }); }, 1000); }
  componentWillUnmount() { clearInterval(this.iv); }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    """ + TL_JS + """
    // Galeri = Shopify ana ürün medyası ("Elif K." kartı ve yorum kolajı mevzuat gereği hariç)
    // Galeri: önce profesyonel oda sahneleri (gerçek üründen Flow ile; ürün değiştirilmedi), sonra Shopify'daki ana ürün afişleri
    var G = [
      { id: '34462d69c62584aeefaca4cff769f3b5', n: 'Gece çocuk odası, LunaDream tavana ay ve yıldız yansıtıyor', pos: '50% 55%', oda: true },
      { id: '05d7f0466966800b2be9e851b9ada476', n: 'Gündüz çocuk odası, komodinde LunaDream', pos: '62% 66%', oda: true },
      { id: 'd0c41725fb735b5851374f373ff814f3', n: 'Gece yanan LunaDream', pos: '50% 50%', oda: true },
      { id: '211acb76d908e8ed6d4f5fcddc987893', n: 'Masalsı gece ışığı', pos: '50% 50%' },
      // 'Temalar' afişi (ec0a99…) çıkarıldı: kutuda olmayan diskler (unicorn, 2025) gösteriyor; afiş düzelince geri gelir
      { id: '652e1893a0ae33a24ee0e3d53edab757', n: 'Müşteri paylaşımı: çocuk odasında LunaDream', pos: '50% 50%' },
      { id: 'a08890007843d79d94bfffc397a3d0ac', n: 'Gece modu', pos: '50% 50%' },
      { id: 'd4efe7e83c74524ece75e962161f7fff', n: 'Deniz altı', pos: '50% 50%' },
      { id: '3ddd8b8b95f040d436d5d0ea350924b8', n: 'Hediye', pos: '50% 50%' },
      { id: '98db755893dbcebe192c69e73ae5afff', n: 'Uzay Kaşifi', pos: '50% 50%' }
    ];
    var gal = G.map(function (g, i) { var on = i === S.g; return { src: B + g.id, n: g.n, pos: g.pos, top: g.oda ? 0 : 56, h: g.oda ? 446 : 390, on: on ? 'true' : 'false', op: on ? 1 : 0, cls: on ? 'kare on' : 'kare', pick: function () { self.setState({ g: i }); } }; });
    // Süzülen hediye diskleri: fotoğrafın kenarında, yavaş (7 sn), yalnız transform
    var tiles = [
      { id: 'a24f13e032569f76d64b9b0fbe8d74f7', x: -16, y: 330, s: 46, r: -12, d: 0 },
      { id: 'b088d2c82561b76f6db997fbc3944059', x: 364, y: 340, s: 38, r: 8, d: -2.3 }
    ].map(function (t) { return { src: B + t.id, x: t.x, y: t.y, s: t.s, r: t.r, d: t.d }; });
    var kiz = S.model === 'kiz';
    var KIZ = B + 'e02351b3be4a1c555c5d760d0bbda723', ERKEK = B + '0033dfea6282c5bc479c385213661c00';
    var models = [
      { id: 'kiz', n: 'Kız', sub: 'Tavşanlı · ninnili', src: KIZ }, { id: 'erkek', n: 'Erkek', sub: 'Robot · ninnili', src: ERKEK }
    ].map(function (m) { var on = S.model === m.id; return { n: m.n, sub: m.sub, src: m.src, on: on ? 'true' : 'false', cls: on ? 'mkart on' : 'mkart', pick: function () { self.setState({ model: m.id }); } }; });
    // Paket: canlı sitedeki biçim. 1 Adet'te ₺1.999 (son 10 günde uygulandı, kullanıcı teyidi). 2 Adet'te birim fiyat.
    var P1 = 1699.99, P2 = 2749.99, C1 = 1999;
    var paket = [
      { n: 1, t: '1 Adet', p: TL(P1, true), old: TL(C1, true), sub: '%' + Math.round((1 - P1 / C1) * 100) + ' indirim', rib: false },
      { n: 2, t: '2 Adet', p: TL(P2, true), old: '', unit: 'tanesi ' + TL(P2 / 2), sub: '2 tekliden %' + Math.round((1 - P2 / (2 * P1)) * 100) + ' az', rib: true }
    ].map(function (b) { var on = S.adet === b.n; return { t: b.t, p: b.p, old: b.old, hasOld: !!b.old, unit: b.unit || '', hasUnit: !!b.unit, sub: b.sub, rib: b.rib, two: b.n === 2, on: on ? 'true' : 'false', cls: on ? 'pk on' : 'pk', pick: function () { self.setState({ adet: b.n }); } }; });
    var total = S.adet === 2 ? P2 : P1, online = Math.round(total * 0.95 * 100) / 100, kapida = total + 80;
    var AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
    var now = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kd = new Date(now); do { kd.setDate(kd.getDate() + 1); } while (kd.getDay() === 0 || kd.getDay() === 6);
    var t1 = new Date(kd); t1.setDate(t1.getDate() + 3); var t2 = new Date(kd); t2.setDate(t2.getDate() + 7);
    var teslim = t1.getMonth() === t2.getMonth() ? t1.getDate() + '–' + t2.getDate() + ' ' + AY[t2.getMonth()] : t1.getDate() + ' ' + AY[t1.getMonth()] + '–' + t2.getDate() + ' ' + AY[t2.getMonth()];
    var DAY = B + '05d7f0466966800b2be9e851b9ada476';
    var moments = [
      { t: '20:00', title: 'Odayı hazırla', text: 'Perdeyi çek, lambayı komodine koy.', src: B + '4279ec63f6d2d18f033818bde2521861', alt: 'LunaDream sıcak ışıkta', pos: '50% 40%' },
      { t: '20:30', title: 'Masalı seç', text: 'Bu gecenin diskini çocuğun seçsin.', src: B + 'a08519c97197df401382b43ca8425d43', alt: 'Kubbesi açık LunaDream', pos: '50% 50%' },
      kiz ? { t: '20:45', title: 'Birlikte dinleyin', text: 'En sevdiği ninniyi telefondan aç.', src: B + '8409b88186ef148c62a07a0bd6f2a19e', alt: 'Tavşanlı LunaDream', pos: '50% 45%' }
          : { t: '20:45', title: 'Uzay yolculuğu', text: 'Işığı kapat, tavanda uzay başlasın.', src: B + '966c145d86bf4b972aa27d983118b8f7', alt: 'Uzay Kaşifi LunaDream', pos: '50% 45%' },
      { t: '21:00', title: 'Gözler kapanır', text: 'Masal tavanda, sen yanında.', src: B + 'aa906021e8f134fc2cb53a35d7d0f47e', alt: 'Tavanda masal yansıması', pos: '50% 40%' },
      { t: '07:30', title: 'Sabah şarja', text: 'Gün boyu dolar, akşam hazır.', src: DAY, alt: 'Gündüz komodinde LunaDream', pos: '62% 70%' }
    ];
    // Bugünkü fiyat sayacı (kullanıcı kararı): her gece 23:59'da (İstanbul) sıfırlanır. Gerçek olması için:
    // toptancı zammı gün içinde gelse bile o günün fiyatı 23:59'a kadar korunur, yeni fiyat ertesi gün başlar.
    function IKI(n) { return n < 10 ? '0' + n : String(n); }
    var ist = new Date(new Date(S.now || Date.now()).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var gunSonu = new Date(ist.getFullYear(), ist.getMonth(), ist.getDate(), 23, 59, 59, 999);
    var kalan = Math.max(0, gunSonu.getTime() - ist.getTime());
    var hh = Math.floor(kalan / 3600000), mi = Math.floor(kalan / 60000) % 60, ss = Math.floor(kalan / 1000) % 60;
    var cdLine = 'Bugünkü fiyat garantisi';
    var cdShort = IKI(hh) + ':' + IKI(mi) + ':' + IKI(ss);
    var cdTiny = 'Bugünkü fiyat: ' + IKI(hh) + 'sa ' + IKI(mi) + 'dk';
    var cdAria = 'Bugünkü fiyatın bitmesine ' + hh + ' saat ' + mi + ' dakika';
    // Videolar: kapaklar mevcut görsellerden; canlıda gerçek videolar (başlıklar düzenlenebilir)
    var vids = [
      { t: 'Işık kapanınca tavanda masal', k: 'Kız modeli', src: B + '34462d69c62584aeefaca4cff769f3b5', pos: '50% 50%' },
      { t: 'Bir müşterimizin akşamı', k: 'Müşteri videosu', src: B + 'e11f41ebd04fb544a2dcfc3fc03a9c26', pos: '50% 40%' },
      { t: 'Uzay Kaşifi tavanda', k: 'Erkek modeli', src: B + '966c145d86bf4b972aa27d983118b8f7', pos: '50% 45%' },
      { t: 'Disk nasıl takılır', k: 'Kurulum', src: B + 'a08519c97197df401382b43ca8425d43', pos: '50% 50%' }
    ];
    // Müşteri fotoğrafları (Loox foto yorumları)
    var mfoto = ['0f174c24e39d6cc31f00e1e5cec0b71a', '872c633eba2deae50857a393085d6d6e', 'a3904987484c22fc3cb242c93283a2b8', 'bc6c8ee4a959d062430c96eb318b745d', 'e11f41ebd04fb544a2dcfc3fc03a9c26'].map(function (id) { return { src: B + id, alt: 'Müşteri fotoğrafı' }; });
    var REV = [
      { tags: ['Uyku'], name: 'Burak G.', q: 'Çocuğum çalıştırmadan uyumuyor, uykuya hemen dalıyor.' },
      { tags: ['Hediye'], name: 'Handan B.', q: 'Torunum filmlerini kendisi seçti ve onunla uyumaya başladı.' },
      { tags: ['Kalite'], name: 'Sevcan Z.', q: '2 tane aldık, gayet sağlam geldi. Paketlenmesi de güzeldi.' },
      { tags: ['Hediye', 'Kalite'], name: 'Abdülkerim T.', q: 'Reklamında nasıl ise aynısı, hatta daha iyisi. Çocuklar için mükemmel bir hediye.' },
      { tags: ['Kalite'], name: 'Mehmet C.', q: 'Anlatıldığı ve gösterildiği gibi çıktı. Bu kadar iyi olmasını beklemiyordum.' }
    ];
    var topics = ['Tümü', 'Uyku', 'Hediye', 'Kalite'].map(function (t) { var on = S.topic === t; return { n: t, cls: on ? 'cip on' : 'cip', on: on ? 'true' : 'false', pick: function () { self.setState({ topic: t }); } }; });
    var revs = REV.filter(function (r) { return S.topic === 'Tümü' || r.tags.indexOf(S.topic) > -1; }).map(function (r) { return { q: r.q, name: r.name, tags: r.tags.join(' · ') }; });
    // Diskler: mağazadaki 1024px tema afişinden kesildi, Real-ESRGAN (çizim modeli) ile x4 netleştirildi, 512px (araclar/disk/disk_kes.py --sr). Unicorn ve 2025 kutuda yok, alınmadı.
    var DISCS = [
      { n: 'Ay ve yıldız', id: '4a3a69e8c1d8dddad8c33f8f463b8a0e' }, { n: 'Okyanus', id: 'a24f13e032569f76d64b9b0fbe8d74f7' },
      { n: 'Uzay', id: 'b088d2c82561b76f6db997fbc3944059' }, { n: 'Deniz kızı', id: '04ed9ce4ae8a36619975caa7d2de9ad8' },
      { n: 'Denizanası', id: 'e3caea057eb48a63b2ecb70c317f5e3b' }, { n: 'Şato', id: 'bbd010d8d946edc8fef9c0404cba4ea2' },
      { n: 'Hayvanlar', id: 'ed5548471e30af0d03e8b419f8ab81ee' }, { n: 'Kış gecesi', id: '88d0b83acee35abef0934694ef439827' },
      { n: 'Taşıtlar', id: 'deaace9b300bee84399862a13f84b2d6' }, { n: 'Masal', id: '6b08a94993cfc00099888dd3bd4cf110' },
      { n: 'Doğum günü', id: 'c2e8b0c346ed92731ab4a2f83a01d3ef' }
    ];
    var discs = DISCS.map(function (d, i) { var on = i === S.disc; return { n: d.n, src: B + d.id, on: on ? 'true' : 'false', cls: on ? 'dbtn on' : 'dbtn', pick: function () { self.setState({ disc: i }); } }; });
    var proj = DISCS.map(function (d, i) { return { src: B + d.id, cls: i === S.disc ? 'yansima on' : 'yansima' }; });
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
    // Not: üstü çizili fiyatlar her ürün için son 10 gün kuralına tabi; canlıda compare_at_price'tan gelir.
    var shop = PR.map(function (x) { var d = x.c > x.p; return { n: x.n, src: B + x.id, price: TL(x.p, true), old: d ? TL(x.c, true) : '', pct: d ? '%' + Math.round((1 - x.p / x.c) * 100) : '' }; });
    var faq = [
      { q: 'Ninni hangi modelde var?', a: 'İki modelde de var. Kız (tavşanlı) modeli telefona Bluetooth ile bağlanır. Erkek (robot) modelde ninni [dahili mi, Bluetooth mu: teyit edilecek].' },
      { q: 'Kaç yaş için uygun?', a: '[yaş] yaş ve üzeri çocuklar için uygundur.' },
      { q: 'Kargo ne zaman gelir?', a: 'Siparişin 1 iş gününde kargoya verilir, Türkiye geneline 3–7 günde ulaşır.' },
      { q: 'Kartla mı, kapıda mı ödeyeyim?', a: 'Kartla öderken %5 indirim alırsın; kart bilgin bize gelmez. Kapıda ödemede ₺80 kapıda ödeme ücreti eklenir; ürün geldiğinde nakit ya da kartla ödersin.' },
      { q: 'Beğenmezsem iade edebilir miyim?', a: '30 gün içinde iade edebilirsin. İlk 14 gün yasal cayma hakkındır ve iade kargosu ücretsizdir. 15–30. günler: [koşul ve kargo bedeli].' },
      { q: 'Işık çocuğu rahatsız eder mi?', a: 'Sıcak tonlu, yumuşak bir ışığı var. [Parlaklık ayarı teyit edilecek]' }
    ];
    return {
      gal: gal, gNo: S.g + 1, gCount: G.length, tiles: tiles, gPrev: function () { self.setState({ g: (S.g + G.length - 1) % G.length }); }, gNext: function () { self.setState({ g: (S.g + 1) % G.length }); }, models: models, modelName: kiz ? 'Kız · tavşanlı' : 'Erkek · Uzay Kaşifi', modelSrc: kiz ? KIZ : ERKEK,
      kiz: kiz, erkek: !kiz, paket: paket, adetName: S.adet === 2 ? '2 Adet' : '1 Adet',
      onLabel: 'Güvenli Ödeme İle Al · ' + TL(online, true), onPrice: TL(online, true),
      p1: TL(P1, true), c1: TL(C1, true), p1on: TL(Math.round(P1 * 0.95 * 100) / 100, true),
      onNote: 'Kartla %5 indirim · kapıda ödemeye göre ' + TL(kapida - online, true) + ' az',
      kpNote: 'Kapıda ödeme ücreti ₺80 · toplam ' + TL(kapida, true),
      kargo: kd.getDate() + ' ' + AY[kd.getMonth()], teslim: teslim,
      // Puan ve sayı canlıda Loox'tan (teyit bekliyor)
      rating: '4,7', reviews: 62, starPct: 94,
      moments: moments, topics: topics, revs: revs, vids: vids, mfoto: mfoto, cdLine: cdLine, cdShort: cdShort, cdTiny: cdTiny, cdAria: cdAria, discs: discs, proj: proj, discName: DISCS[S.disc].n,
      boxModel: kiz ? 'tavşanlı lamba' : 'Uzay Kaşifi lamba', shop: shop, shopCount: PR.length, faq: faq
    };
  }
}"""

open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · B+ Gece Postası', css=CSS) + HTML + TAIL.format(h=6750, js=JS))
print('yazıldı:', os.path.abspath(OUT))
