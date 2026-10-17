# LunaDream ürün sayfası · B+ Gece Postası (tam sayfa). Çalıştır: python3 luna_bplus.py
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL, TL_JS
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamBPlus.dc.html')

CSS = r""".pg{background:#F6F1E9}
.ust{display:flex;justify-content:space-between;align-items:center;height:56px;background:#1A2142;color:#FFFDF9;padding:0 4px}
.ikon{width:48px;height:48px;display:grid;place-items:center;background:transparent;border:0;color:inherit;cursor:pointer}
.galeri{position:relative;height:410px;background:#1A2142;overflow:hidden}
.galeri img.ana{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .45s cubic-bezier(.2,.7,.2,1)}
.sayac{position:absolute;left:16px;bottom:12px;font-family:"Young Serif",Georgia,serif;font-size:40px;line-height:1;color:#F2A65A;font-variant-numeric:tabular-nums;text-shadow:0 2px 12px rgba(12,16,39,.6)}
.sayac small{font-size:18px;color:#FFFDF9}
.kucuk{flex:none;width:58px;height:58px;padding:0;border-radius:12px;border:3px solid transparent;background:#232B55;overflow:hidden;cursor:pointer;transition:transform .2s cubic-bezier(.2,.7,.2,1)}
.kucuk.on{border-color:#F2A65A;transform:translateY(-3px)}
.kucuk img{width:100%;height:100%;object-fit:cover;display:block}
.bant{background:#1A2142;padding:12px 0 18px}
.yildiz{position:relative;display:inline-block;letter-spacing:1px;color:#D9CDB9;line-height:1}
.yildiz i{position:absolute;left:0;top:0;overflow:hidden;white-space:nowrap;color:#E59A4C;font-style:normal}
.dev{font-family:"Young Serif",Georgia,serif;font-size:56px;line-height:.95;letter-spacing:-.04em;margin:8px 0 0;color:#1A2142;white-space:nowrap}
.dev span,.h2 span.n{color:#E59A4C}
.alt{font-family:"Young Serif",Georgia,serif;font-style:italic;font-size:19px;line-height:1.3;margin:8px 0 0;color:#3A3F5A}
.alt em{font-style:italic;background:linear-gradient(transparent 60%,rgba(242,166,90,.5) 60%)}
.mkart{display:grid;grid-template-columns:52px minmax(0,1fr);gap:10px;align-items:center;min-height:70px;padding:8px 10px 8px 8px;border-radius:18px;border:1.5px solid #E3D8C7;background:#FFFDF9;font:inherit;color:#1A2142;text-align:left;cursor:pointer;transition:transform .2s cubic-bezier(.2,.7,.2,1)}
.mkart:active,.pk:active,.cip:active{transform:scale(.985)}
.mkart.on{background:#1A2142;border-color:#1A2142;color:#FFFDF9}
.mkart.on .msub{color:#B9BED6}
.mkart .foto{width:52px;height:52px;border-radius:12px;overflow:hidden;background:#EFE6D8}
.mkart .foto img{width:100%;height:100%;object-fit:cover;transform:scale(1.5);transform-origin:50% 62%}
.msub{font-size:12px;color:#5C6078;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
/* Sihirli Özellikler: 48px dolu, iki tonlu ikon; animasyon ikonun içinde (yalnız transform/opacity). Kullanıcı isteği: sonsuz ama yavaş; canlıda yalnız ekrandayken oynar. */
.sih{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:14px}
.oz{position:relative;min-height:136px;padding:14px;border-radius:20px;display:flex;flex-direction:column;gap:6px;background:#FFFDF9;border:1.5px solid #E3D8C7;color:#1A2142;text-decoration:none}
.oz.koyu{background:#1A2142;border-color:#1A2142;color:#FFFDF9}
.oz.amber{background:#F2A65A;border-color:#F2A65A;color:#1A2142}
.oz b{font-size:16px;font-weight:700;line-height:1.2;margin-top:4px}
.oz span.t{font-size:13px;line-height:1.4;opacity:.85}
.ik{position:relative;width:48px;height:48px;border-radius:14px;display:grid;place-items:center;overflow:visible}
.ik svg{position:relative;z-index:1;width:30px;height:30px}
.ik.ay{background:#2B3463}
.ik.ay .hale{position:absolute;inset:-6px;border-radius:50%;background:radial-gradient(circle,rgba(242,166,90,.7),rgba(242,166,90,0) 62%);animation:nefes 4.5s ease-in-out infinite}
@keyframes nefes{0%,100%{transform:scale(.8);opacity:.45}50%{transform:scale(1.15);opacity:1}}
.ik.disk{background:#F3E9DA}
.ik.disk img{position:absolute;left:9px;top:9px;width:30px;height:30px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 2px #FFFDF9;transform-origin:50% 140%;animation:yel 5s ease-in-out infinite alternate}
.ik.disk img:nth-child(1){--r:-28deg}.ik.disk img:nth-child(2){--r:0deg}.ik.disk img:nth-child(3){--r:28deg}
@keyframes yel{from{transform:rotate(0)}to{transform:rotate(var(--r))}}
.ik.nota{background:#1A2142}
.ik.nota .halka{position:absolute;inset:0;border-radius:14px;border:2px solid #1A2142;animation:yay 2.4s ease-out infinite}
.ik.nota .halka:nth-child(2){animation-delay:1.2s}
@keyframes yay{from{transform:scale(1);opacity:.7}to{transform:scale(1.55);opacity:0}}
.ik.robot{background:#1A2142}
.ik.robot .yor{position:absolute;inset:-8px;border-radius:50%;border:1px dashed rgba(26,33,66,.45);animation:don 7s linear infinite}
.ik.robot .yor::after{content:"";position:absolute;left:50%;top:-4px;width:7px;height:7px;margin-left:-3.5px;border-radius:50%;background:#1A2142}
@keyframes don{to{transform:rotate(360deg)}}
.ik.pil{background:#2B3463}
.ik.pil .dolum{transform-box:fill-box;transform-origin:0 50%;animation:sarj 3.8s ease-in-out infinite}
@keyframes sarj{0%{transform:scaleX(.15)}70%,100%{transform:scaleX(1)}}
.hayal{display:grid;grid-template-columns:minmax(0,1fr) 120px;margin-top:10px;border-radius:20px;overflow:hidden;background:#1A2142;color:#FFFDF9}
.hayal img{width:100%;height:100%;min-height:112px;object-fit:cover;display:block}
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
.ust-yazi{margin:0 0 6px;font-size:13px;font-weight:700;color:#E59A4C}
.gece{background:#1A2142;color:#EDE5D8;padding:44px 0 46px;margin-top:52px}
.an{position:relative;flex:0 0 270px;height:420px;border-radius:24px;overflow:hidden;background:#0C1027;scroll-snap-align:start}
.an img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.an .saat{position:absolute;left:16px;top:14px;font-family:"Young Serif",Georgia,serif;font-size:46px;line-height:1;color:#F2A65A;font-variant-numeric:tabular-nums}
.an .alt2{position:absolute;left:16px;right:16px;bottom:16px;display:flex;flex-direction:column;gap:4px}
.cip{display:inline-flex;align-items:center;min-height:48px;padding:0 18px;border-radius:999px;border:1.5px solid #1A2142;background:transparent;color:#1A2142;font:inherit;font-size:15px;font-weight:600;cursor:pointer;white-space:nowrap}
.cip.on{background:#1A2142;color:#FFFDF9}
.yk{border-radius:20px;padding:16px;display:flex;flex-direction:column;gap:10px}
.yk q{font-family:"Young Serif",Georgia,serif;font-size:19px;line-height:1.25;quotes:"“" "”"}
.yk small{font-size:13px;opacity:.75}
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
.noscroll{scrollbar-width:none}.noscroll::-webkit-scrollbar{display:none}"""

STAR = '<span class="yildiz" aria-hidden="true">★★★★★<i style="width: {{starPct}}%">★★★★★</i></span>'
LOGO = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M15.5 3.5a8.5 8.5 0 1 0 5 15.4A7 7 0 0 1 15.5 3.5z" fill="#F2A65A"></path></svg>'

HTML = """<div class="pg" style="padding-bottom: 0">
  <header class="ust"><button class="ikon" aria-label="Menü"><svg class="ico" viewBox="0 0 24 24"><path d="M4 8h16M4 16h11"></path></svg></button><span style="display: flex; align-items: center; gap: 6px">""" + LOGO + """<span class="ser" style="font-size: 22px">Ayluna</span></span><button class="ikon" aria-label="Sepet"><svg class="ico" viewBox="0 0 24 24"><path d="M6 8h12l-1 12H7z"></path><path d="M9 8a3 3 0 0 1 6 0"></path></svg></button></header>

  <!-- Galeri: Shopify ana ürün medyası, tam genişlik -->
  <section class="galeri" aria-label="LunaDream fotoğrafları">
    <sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><img class="ana" src="{{f.src}}" alt="{{f.n}}" style="opacity: {{f.op}}"></sc-for>
    <span class="sayac">{{gNo}}<small> / {{gCount}}</small></span>
  </section>
  <div class="bant"><div class="noscroll" style="display: flex; gap: 8px; overflow-x: auto; padding: 0 16px">
    <sc-for list="{{gal}}" as="f" hint-placeholder-count="7"><button class="{{f.cls}}" onClick="{{f.pick}}" aria-label="{{f.n}}" aria-pressed="{{f.on}}"><img src="{{f.src}}" alt=""></button></sc-for>
  </div></div>

  <section class="px" id="siparis" style="padding-top: 20px">
    <!-- Puan ve sayı canlıda Loox'tan; veri yoksa gizlenir -->
    <a href="#yorumlar" style="display: inline-flex; align-items: center; gap: 6px; min-height: 48px; font-size: 13.5px; text-decoration: none; color: #5C6078">""" + STAR + """<b style="color: #1A2142">{{rating}}</b> · {{reviews}} yorum</a>
    <h1 class="dev">LunaDream<span>.</span></h1>
    <p class="alt">Işığı kapattığında <em>tavanda masal</em> başlar.</p>
    <p style="margin: 12px 0 0; display: flex; align-items: baseline; flex-wrap: wrap; gap: 4px 10px; font-variant-numeric: tabular-nums"><b style="font-size: 24px; letter-spacing: -.02em">{{p1}}</b><s style="font-size: 15px; color: #5C6078">{{c1}}</s><span style="font-size: 14px; font-weight: 600; color: #2E6B4F">kartla {{p1on}}</span></p>

    <div class="etiket" style="margin-top: 22px"><span>Model</span><b>{{modelName}}</b></div>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-top: 8px">
      <sc-for list="{{models}}" as="m" hint-placeholder-count="2">
        <button class="{{m.cls}}" onClick="{{m.pick}}" aria-pressed="{{m.on}}"><span class="foto"><img src="{{m.src}}" alt=""></span><span style="display: flex; flex-direction: column; min-width: 0; line-height: 1.2"><b style="font-size: 14px; font-weight: 600">{{m.n}}</b><span class="msub">{{m.sub}}</span></span></button>
      </sc-for>
    </div>

    <!-- Sihirli Özellikler (yeri canlıdaki gibi: model seçiminden sonra) -->
    <p class="ust-yazi" style="margin-top: 30px">Sihirli özellikler</p>
    <h2 class="h2" style="font-size: 26px">Uyku vakti savaş değil,<br>minik bir masal<span class="n">.</span></h2>
    <div class="sih">
      <div class="oz koyu"><span class="ik ay" aria-hidden="true"><span class="hale"></span><svg viewBox="0 0 24 24"><path d="M15.5 3.5a8.5 8.5 0 1 0 5 15.4A7 7 0 0 1 15.5 3.5z" fill="#F2A65A"></path><circle cx="18" cy="5" r="1.3" fill="#FFFDF9"></circle></svg></span><b>Mışıl mışıl uykular</b><span class="t">Yumuşacık ışık, huzurlu bir geçiş.</span></div>
      <a class="oz" href="#diskler"><span class="ik disk" aria-hidden="true"><img src="/_blob/336d1995fe82f1e73d526c0e2697677e" alt=""><img src="/_blob/2c6f33b11e553e39fd315693c5cf692b" alt=""><img src="/_blob/6e25420625a6a34858578ba9e632cda7" alt=""></span><b>6 + 6 masal</b><span class="t">Altısı hediye. <u>Diskleri gör</u></span></a>
      <sc-if value="{{kiz}}" hint-placeholder-val="{{true}}"><div class="oz amber"><span class="ik nota" aria-hidden="true"><span class="halka"></span><span class="halka"></span><svg viewBox="0 0 24 24"><path d="M9 17V6l10-2v11" fill="none" stroke="#F2A65A" stroke-width="2" stroke-linecap="round"></path><circle cx="6.5" cy="17" r="2.8" fill="#F2A65A"></circle><circle cx="16.5" cy="15" r="2.8" fill="#FFFDF9"></circle></svg></span><b>Bluetooth ninni</b><span class="t">Telefondan bağlan, lambadan çalsın.</span></div></sc-if>
      <sc-if value="{{erkek}}" hint-placeholder-val="{{false}}"><div class="oz amber"><span class="ik robot" aria-hidden="true"><span class="yor"></span><svg viewBox="0 0 24 24"><path d="M12 2.5v3" stroke="#F2A65A" stroke-width="2" stroke-linecap="round"></path><rect x="4.5" y="5.5" width="15" height="11" rx="3.5" fill="#FFFDF9"></rect><circle cx="9.5" cy="11" r="1.6" fill="#1A2142"></circle><circle cx="14.5" cy="11" r="1.6" fill="#1A2142"></circle><path d="M8 20l1.5-3.5M16 20l-1.5-3.5" stroke="#F2A65A" stroke-width="2" stroke-linecap="round"></path></svg></span><b>Uzay Kaşifi</b><span class="t">Robot projektör, tavanda uzay.</span></div></sc-if>
      <div class="oz koyu"><span class="ik pil" aria-hidden="true"><svg viewBox="0 0 24 24"><rect x="2.5" y="7" width="16" height="10" rx="2.5" fill="none" stroke="#FFFDF9" stroke-width="1.8"></rect><rect class="dolum" x="4.5" y="9" width="12" height="6" rx="1.2" fill="#F2A65A"></rect><path d="M21 10.5v3" stroke="#FFFDF9" stroke-width="2" stroke-linecap="round"></path></svg></span><b>Kablosuz kullanım</b><span class="t">Şarj et, her yere taşı.</span></div>
    </div>
    <div class="hayal"><div style="padding: 16px; display: flex; flex-direction: column; justify-content: center; gap: 6px"><b style="font-size: 16px; line-height: 1.3">Çocuğunun hayalleri artık odasında.</b><span style="font-size: 13px; color: #B9BED6">Işığı yak, o gülümsemeyi izle.</span></div><img src="/_blob/b9e869a37734e184ce3a88695b4ec64a" alt="Müşteri fotoğrafı"></div>
    <!-- Müşteri fotoğrafı: paylaşım izni teyit edilecek -->

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

    <button class="btn-on" type="button">{{onLabel}}</button>
    <p class="bnot">{{onNote}}</p>
    <!-- Canlıda kapıda ödeme uygulamasının formunu açar (uygulama korunur; ek ürünler ve ₺80 ücret orada). -->
    <button class="btn-kp" type="button">Kapıda Ödeme ile Sipariş Ver</button>
    <p class="bnot">{{kpNote}}</p>
    <ol class="yol" aria-label="Siparişten teslime"><li><b>Bugün</b><span>Siparişin alındı</span></li><li><b>{{kargo}}</b><span>Kargoda</span></li><li><b>{{teslim}}</b><span>Kapında</span></li></ol>
    <p class="guven"><span>Ücretsiz kargo</span><span>30 gün iade</span><span>Güvenli ödeme</span></p>
  </section>

  <!-- Bir gece, beş an -->
  <section class="gece">
    <div class="px"><p class="ust-yazi">Nasıl kullanılır</p><h2 class="h2" style="color: #FFFDF9">Bir gece, beş an<span class="n">.</span></h2></div>
    <div class="noscroll" style="display: flex; gap: 12px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-left: 16px; padding: 18px 16px 0">
      <!-- Canlıda: kısa sessiz döngü videolar (onizleme/v/), yalnız ekrandayken oynar -->
      <sc-for list="{{moments}}" as="a" hint-placeholder-count="5">
        <article class="an"><img src="{{a.src}}" alt="{{a.alt}}" style="object-position: {{a.pos}}"><span aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(0deg, rgba(12,16,39,.88) 0%, rgba(12,16,39,0) 55%)"></span><span class="saat">{{a.t}}</span><span class="alt2"><b style="font-size: 20px; color: #FFFDF9">{{a.title}}</b><span style="font-size: 14px; color: #B9BED6">{{a.text}}</span></span></article>
      </sc-for>
      <span aria-hidden="true" style="flex: 0 0 4px"></span>
    </div>
  </section>

  <!-- Yorumlar -->
  <section id="yorumlar" class="px bolum">
    <div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px"><h2 class="h2">Aileler<br>ne diyor<span class="n">.</span></h2><span style="display: flex; flex-direction: column; align-items: flex-end; line-height: 1"><b class="ser" style="font-size: 52px; font-weight: 400">{{rating}}</b><span style="font-size: 13px; color: #5C6078; margin-top: 4px">{{reviews}} yorum</span></span></div>
    <div class="noscroll" style="display: flex; gap: 8px; overflow-x: auto; margin: 16px -16px 0; padding: 0 16px">
      <sc-for list="{{topics}}" as="t" hint-placeholder-count="4"><button class="{{t.cls}}" onClick="{{t.pick}}" aria-pressed="{{t.on}}">{{t.n}}</button></sc-for>
    </div>
    <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 14px">
      <sc-for list="{{revs}}" as="r" hint-placeholder-count="3">
        <figure class="yk" style="margin: 0; background: {{r.bg}}; color: {{r.fg}}"><q>{{r.q}}</q><small>{{r.name}} · Satın aldı · {{r.tags}}</small></figure>
      </sc-for>
    </div>
    <a href="#" class="cip" style="display: flex; justify-content: center; margin-top: 12px">{{reviews}} yorumun hepsini oku</a>
    <p style="margin: 10px 0 0; font-size: 12.5px; color: #5C6078; text-align: center">Yorumlar yalnız Ayluna'dan sipariş verenlerden toplanır; hepsi yayımlanır.</p>
  </section>

  <!-- Diskler: tavana yansıt -->
  <section class="gece" id="diskler" style="margin-top: 52px">
    <div class="px"><h2 class="h2" style="color: #FFFDF9">Altı masal kutuda,<br>altısı hediye<span class="n">.</span></h2><p style="margin: 8px 0 0; font-size: 15px; color: #B9BED6">Diski seç, tavanda gör.</p></div>
    <div class="px" style="margin-top: 16px"><div class="tavan">
      <sc-for list="{{proj}}" as="p" hint-placeholder-count="2"><span class="{{p.cls}}" aria-hidden="true"><img src="{{p.src}}" alt=""></span></sc-for>
      <span style="position: absolute; left: 12px; top: 12px; font-size: 12px; font-weight: 600; color: #FFFDF9; background: rgba(12,16,39,.6); padding: 3px 9px; border-radius: 999px">[gerçek tavan fotoğrafı]</span>
      <span style="position: absolute; left: 14px; bottom: 14px; display: flex; flex-direction: column; line-height: 1.2; color: #FFFDF9"><span style="font-size: 12px; color: #B9BED6">Tavanda</span><b class="ser" style="font-size: 22px; font-weight: 400">{{discName}}</b></span>
    </div></div>
    <div class="noscroll" style="display: flex; gap: 6px; overflow-x: auto; padding: 14px 16px 0">
      <sc-for list="{{discs}}" as="d" hint-placeholder-count="12"><button class="{{d.cls}}" onClick="{{d.pick}}" aria-pressed="{{d.on}}" aria-label="{{d.n}} diskini tavanda göster"><img src="{{d.src}}" alt=""><span>{{d.n}}</span></button></sc-for>
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
    <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; line-height: 1.15; color: #FFFDF9; font-variant-numeric: tabular-nums"><b style="font-size: 17px">{{onPrice}}</b><span style="font-size: 12px; color: #F2A65A">kartla · {{adetName}}</span></span>
    <button class="btn-on" type="button" style="flex: 0 0 150px; width: 150px; min-height: 52px; margin: 0; font-size: 16px; box-shadow: 0 4px 0 #C97F38">Satın al</button>
  </div>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { g: 0, model: 'kiz', adet: 2, topic: 'Tümü', disc: 1 }; }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    """ + TL_JS + """
    // Galeri = Shopify ana ürün medyası ("Elif K." kartı ve yorum kolajı mevzuat gereği hariç)
    var G = [
      { id: '211acb76d908e8ed6d4f5fcddc987893', n: 'Masalsı gece ışığı' }, { id: 'ec0a99ef7b8839a12ab7e6aa4282f7da', n: 'Temalar' },
      { id: '652e1893a0ae33a24ee0e3d53edab757', n: 'Müşteri' }, { id: 'a08890007843d79d94bfffc397a3d0ac', n: 'Gece modu' },
      { id: 'd4efe7e83c74524ece75e962161f7fff', n: 'Deniz altı' }, { id: '3ddd8b8b95f040d436d5d0ea350924b8', n: 'Hediye' },
      { id: '98db755893dbcebe192c69e73ae5afff', n: 'Uzay Kaşifi' }
    ];
    var gal = G.map(function (g, i) { var on = i === S.g; return { src: B + g.id, n: g.n, on: on ? 'true' : 'false', op: on ? 1 : 0, cls: on ? 'kucuk on' : 'kucuk', pick: function () { self.setState({ g: i }); } }; });
    var kiz = S.model === 'kiz';
    var KIZ = B + 'e02351b3be4a1c555c5d760d0bbda723', ERKEK = B + '0033dfea6282c5bc479c385213661c00';
    var models = [
      { id: 'kiz', n: 'Kız', sub: 'Tavşanlı · ninnili', src: KIZ }, { id: 'erkek', n: 'Erkek', sub: 'Robot · ninnisiz', src: ERKEK }
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
    var REV = [
      { tags: ['Uyku'], name: 'Burak G.', q: 'Çocuğum çalıştırmadan uyumuyor, uykuya hemen dalıyor.' },
      { tags: ['Hediye'], name: 'Handan B.', q: 'Torunum filmlerini kendisi seçti ve onunla uyumaya başladı.' },
      { tags: ['Kalite'], name: 'Sevcan Z.', q: '2 tane aldık, gayet sağlam geldi. Paketlenmesi de güzeldi.' },
      { tags: ['Hediye', 'Kalite'], name: 'Abdülkerim T.', q: 'Reklamında nasıl ise aynısı, hatta daha iyisi. Çocuklar için mükemmel bir hediye.' },
      { tags: ['Kalite'], name: 'Mehmet C.', q: 'Anlatıldığı ve gösterildiği gibi çıktı. Bu kadar iyi olmasını beklemiyordum.' }
    ];
    var RENK = [['#1A2142', '#FFFDF9'], ['#FFFDF9', '#1A2142'], ['#F2A65A', '#1A2142']];
    var topics = ['Tümü', 'Uyku', 'Hediye', 'Kalite'].map(function (t) { var on = S.topic === t; return { n: t, cls: on ? 'cip on' : 'cip', on: on ? 'true' : 'false', pick: function () { self.setState({ topic: t }); } }; });
    var revs = REV.filter(function (r) { return S.topic === 'Tümü' || r.tags.indexOf(S.topic) > -1; }).slice(0, 3).map(function (r, i) { var c = RENK[i % 3]; return { q: r.q, name: r.name, tags: r.tags.join(' · '), bg: c[0], fg: c[1] }; });
    var DISCS = [
      { n: 'Ay ve yıldız', id: '63f8557bf1f7867885fdbdedeb19c5ed' }, { n: 'Okyanus', id: '336d1995fe82f1e73d526c0e2697677e' },
      { n: 'Uzay', id: '2c6f33b11e553e39fd315693c5cf692b' }, { n: 'Deniz kızı', id: '6e25420625a6a34858578ba9e632cda7' },
      { n: 'Denizanası', id: '210c9b211afc86f40a3736f7dca41856' }, { n: 'Şato', id: 'c47c719d14b2dd08716967b126324ad7' },
      { n: 'Hayvanlar', id: '81713384676b51d6a15c426fe5ace95f' }, { n: 'Gökkuşağı', id: '6202a8de2d18ea09b2bd1328835a7221' },
      { n: 'Kış gecesi', id: 'de53d54e97de9b7ea6f936c94e218e26' }, { n: 'Taşıtlar', id: '0fa320a5ec8bbbb5066e6e197ba96666' },
      { n: 'Masal', id: 'e10addf033ab0d3bb401f79055402da8' }, { n: 'Doğum günü', id: '10d49c7a953d26c819ef5c9970cd8c6a' }
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
      { q: 'Bluetooth hoparlör hangi modelde?', a: 'Yalnızca Kız (tavşanlı) modelinde. Erkek (Uzay Kaşifi) modelinde hoparlör yoktur.' },
      { q: 'Kaç yaş için uygun?', a: '[yaş] yaş ve üzeri çocuklar için uygundur.' },
      { q: 'Kargo ne zaman gelir?', a: 'Siparişin 1 iş gününde kargoya verilir, Türkiye geneline 3–7 günde ulaşır.' },
      { q: 'Kartla mı, kapıda mı ödeyeyim?', a: 'Kartla öderken %5 indirim alırsın; kart bilgin bize gelmez. Kapıda ödemede ₺80 kapıda ödeme ücreti eklenir; ürün geldiğinde nakit ya da kartla ödersin.' },
      { q: 'Beğenmezsem iade edebilir miyim?', a: '30 gün içinde iade edebilirsin. İlk 14 gün yasal cayma hakkındır ve iade kargosu ücretsizdir. 15–30. günler: [koşul ve kargo bedeli].' },
      { q: 'Işık çocuğu rahatsız eder mi?', a: 'Sıcak tonlu, yumuşak bir ışığı var. [Parlaklık ayarı teyit edilecek]' }
    ];
    return {
      gal: gal, gNo: S.g + 1, gCount: G.length, models: models, modelName: kiz ? 'Kız · tavşanlı' : 'Erkek · Uzay Kaşifi', modelSrc: kiz ? KIZ : ERKEK,
      kiz: kiz, erkek: !kiz, paket: paket, adetName: S.adet === 2 ? '2 Adet' : '1 Adet',
      onLabel: 'Güvenli Ödeme İle Al · ' + TL(online, true), onPrice: TL(online, true),
      p1: TL(P1, true), c1: TL(C1, true), p1on: TL(Math.round(P1 * 0.95 * 100) / 100, true),
      onNote: 'Kartla %5 indirim · kapıda ödemeye göre ' + TL(kapida - online, true) + ' az',
      kpNote: 'Kapıda ödeme ücreti ₺80 · toplam ' + TL(kapida, true),
      kargo: kd.getDate() + ' ' + AY[kd.getMonth()], teslim: teslim,
      // Puan ve sayı canlıda Loox'tan (teyit bekliyor)
      rating: '4,7', reviews: 62, starPct: 94,
      moments: moments, topics: topics, revs: revs, discs: discs, proj: proj, discName: DISCS[S.disc].n,
      boxModel: kiz ? 'tavşanlı lamba' : 'Uzay Kaşifi lamba', shop: shop, shopCount: PR.length, faq: faq
    };
  }
}"""

open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · B+ Gece Postası', css=CSS) + HTML + TAIL.format(h=6500, js=JS))
print('yazıldı:', os.path.abspath(OUT))
