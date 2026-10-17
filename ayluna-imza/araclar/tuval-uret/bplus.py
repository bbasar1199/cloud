import sys, os
sys.path.insert(0,'.')
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'yonler.py'),encoding='utf-8').read().split("# =========================================================\n# A · MASAL")[0])  # ortak veri ve şablonlar

PAKET_BP = """<div style="display: flex; flex-direction: column; gap: 16px; margin-top: 14px">
        <sc-for list="{{paket}}" as="b" hint-placeholder-count="2">
          <button class="{{b.cls}}" onClick="{{b.pick}}" aria-pressed="{{b.on}}">
            <sc-if value="{{b.rib}}" hint-placeholder-val="{{false}}"><span class="kurdele">En Çok Tercih Edilen</span></sc-if>
            <span class="pk-ust">
              <span class="pk-foto"><span class="lamba"><img src="/_blob/e02351b3be4a1c555c5d760d0bbda723" alt=""></span><sc-if value="{{b.two}}" hint-placeholder-val="{{false}}"><span class="lamba iki"><img src="/_blob/e02351b3be4a1c555c5d760d0bbda723" alt=""></span></sc-if></span>
              <span style="display: flex; flex-direction: column; min-width: 0; line-height: 1.2"><b class="pk-ad">{{b.t}}</b><span class="pk-sub">{{b.sub}}</span></span>
              <span style="display: flex; flex-direction: column; align-items: flex-end; line-height: 1.15; font-variant-numeric: tabular-nums"><b class="pk-fiyat">{{b.p}}</b><sc-if value="{{b.hasOld}}" hint-placeholder-val="{{true}}"><s class="pk-eski">{{b.old}}</s></sc-if><sc-if value="{{b.hasUnit}}" hint-placeholder-val="{{false}}"><span class="pk-eski" style="text-decoration: none">{{b.unit}}</span></sc-if></span>
            </span>
            <span class="pk-hediye">+ 6 Tane Ücretsiz Hediye Disk</span>
          </button>
        </sc-for>
      </div>"""

cssBP = """.pg{background:#F6F1E9}
.ust{display:flex;justify-content:space-between;align-items:center;height:56px;background:#1A2142;color:#FFFDF9}
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
.dev span{color:#E59A4C}
.alt{font-family:"Young Serif",Georgia,serif;font-style:italic;font-size:19px;line-height:1.3;margin:8px 0 0;color:#3A3F5A}
.alt em{font-style:italic;background:linear-gradient(transparent 60%,rgba(242,166,90,.5) 60%)}
.mkart{display:grid;grid-template-columns:52px minmax(0,1fr);gap:10px;align-items:center;min-height:70px;padding:8px 10px 8px 8px;border-radius:18px;border:1.5px solid #E3D8C7;background:#FFFDF9;font:inherit;color:#1A2142;text-align:left;cursor:pointer;transition:transform .2s cubic-bezier(.2,.7,.2,1)}
.mkart:active,.pk:active{transform:scale(.985)}
.mkart.on{background:#1A2142;border-color:#1A2142;color:#FFFDF9}
.mkart.on .msub{color:#B9BED6}
.mkart .foto{width:52px;height:52px;border-radius:12px;overflow:hidden;background:#EFE6D8}
.mkart .foto img{width:100%;height:100%;object-fit:cover;transform:scale(1.5);transform-origin:50% 62%}
.msub{font-size:12px;color:#5C6078;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
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
.poster{flex:0 0 260px;border-radius:24px;overflow:hidden;display:flex;flex-direction:column;scroll-snap-align:start}
.poster .foto{height:170px;overflow:hidden}
.poster .foto img{width:100%;height:100%;object-fit:cover;display:block}
.poster .yazi{padding:14px 16px 18px;display:flex;flex-direction:column;gap:6px}
.poster b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:44px;line-height:.9;letter-spacing:-.03em}
.poster span{font-size:15px;line-height:1.35}
.noscroll{scrollbar-width:none}.noscroll::-webkit-scrollbar{display:none}"""

htmlBP = """<div class="pg" style="padding-bottom: 36px">
  <header class="ust" style="padding: 0 4px"><button class="ikon" aria-label="Menü"><svg class="ico" viewBox="0 0 24 24"><path d="M4 8h16M4 16h11"></path></svg></button><span style="display: flex; align-items: center; gap: 6px"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M15.5 3.5a8.5 8.5 0 1 0 5 15.4A7 7 0 0 1 15.5 3.5z" fill="#F2A65A"></path></svg><span class="ser" style="font-size: 22px">Ayluna</span></span><button class="ikon" aria-label="Sepet"><svg class="ico" viewBox="0 0 24 24"><path d="M6 8h12l-1 12H7z"></path><path d="M9 8a3 3 0 0 1 6 0"></path></svg></button></header>
  <!-- Galeri: Shopify ana ürün medyası, tam genişlik (poster yazısı kesilmez) -->
  <section class="galeri" aria-label="LunaDream fotoğrafları">
    <sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><img class="ana" src="{{f.src}}" alt="{{f.n}}" style="opacity: {{f.op}}"></sc-for>
    <span class="sayac">{{gNo}}<small> / {{gCount}}</small></span>
  </section>
  <div class="bant">
    <div class="noscroll" style="display: flex; gap: 8px; overflow-x: auto; padding: 0 16px">
      <sc-for list="{{gal}}" as="f" hint-placeholder-count="7"><button class="{{f.cls}}" onClick="{{f.pick}}" aria-label="{{f.n}}" aria-pressed="{{f.on}}"><img src="{{f.src}}" alt=""></button></sc-for>
    </div>
  </div>

  <div class="px" style="padding-top: 20px">
    <!-- Puan ve sayı canlıda Loox'tan; veri yoksa gizlenir -->
    <a href="#yorumlar" style="display: inline-flex; align-items: center; gap: 6px; min-height: 32px; font-size: 13.5px; text-decoration: none; color: #5C6078"><span class="yildiz" aria-hidden="true">★★★★★<i style="width: {{starPct}}%">★★★★★</i></span><b style="color: #1A2142">{{rating}}</b> · {{reviews}} yorum</a>
    <h1 class="dev">LunaDream<span>.</span></h1>
    <p class="alt">Işığı kapattığında <em>tavanda masal</em> başlar.</p>
    """ + MODEL_HTML + """
    <div class="etiket" style="margin-top: 22px"><span>Paket</span><span style="font-weight: 600">Kampanya · [tarih aralığı]</span></div>
    """ + PAKET_BP + """
    """ + BTN_HTML + """
    """ + YOL_HTML + """
  </div>

  <!-- Fayda: ikon yok; ana ürün fotoğrafı + büyük kelime + tek cümle. "Ninni" yalnız Kız modelinde. -->
  <div class="noscroll" style="display: flex; gap: 10px; overflow-x: auto; padding: 40px 16px 0; scroll-snap-type: x mandatory">
    <div class="poster" style="background: #1A2142; color: #FFFDF9"><span class="foto"><img src="/_blob/ec0a99ef7b8839a12ab7e6aa4282f7da" alt="Tema diskleri"></span><span class="yazi"><b style="color: #F2A65A">6 + 6</b><span>Altı masal diski kutuda, altısı hediye.</span></span></div>
    <sc-if value="{{kiz}}" hint-placeholder-val="{{true}}"><div class="poster" style="background: #F2A65A; color: #1A2142"><span class="foto"><img src="/_blob/211acb76d908e8ed6d4f5fcddc987893" alt="Tavşanlı LunaDream"></span><span class="yazi"><b>Ninni</b><span>Telefonundan bağlan, ninni lambadan çalsın.</span></span></div></sc-if>
    <sc-if value="{{erkek}}" hint-placeholder-val="{{false}}"><div class="poster" style="background: #F2A65A; color: #1A2142"><span class="foto"><img src="/_blob/98db755893dbcebe192c69e73ae5afff" alt="Uzay Kaşifi"></span><span class="yazi"><b>Robot</b><span>Uzay Kaşifi yıldızları tavana saçar.</span></span></div></sc-if>
    <div class="poster" style="background: #FFFDF9; color: #1A2142; border: 1.5px solid #E3D8C7"><span class="foto"><img src="/_blob/3ddd8b8b95f040d436d5d0ea350924b8" alt="Elde iki lamba"></span><span class="yazi"><b>Şarjlı</b><span>Kablo yok; komodinden yatağın yanına taşı.</span></span></div>
  </div>
</div>
"""
build('YonBPlus-GecePostasi.dc.html','Yön B+ · Gece Postası (önerilen)',cssBP,htmlBP,'',2050)
print('ok')
