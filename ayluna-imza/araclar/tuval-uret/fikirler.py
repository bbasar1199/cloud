import sys
sys.path.insert(0,'.')
from ortak import HEAD, TAIL, TL_JS
import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'canvas') + '/'

PAY_JS = """
    var total = 2749.99, onTotal = Math.round(total * 0.95 * 100) / 100, online = S.pay === 'online';
    var pays = [
      { id: 'online', n: 'Kartla öde', price: TL(onTotal, true), old: TL(total, true), pct: true },
      { id: 'kapida', n: 'Kapıda öde', price: TL(total, true), old: '', pct: false }
    ].map(function (o) { var on = S.pay === o.id; return { n: o.n, price: o.price, old: o.old, hasPct: o.pct, on: on ? 'true' : 'false', bd: on ? '#1A2142' : '#E3D8C7', bg: on ? '#FFFDF9' : 'transparent', pick: function () { self.setState({ pay: o.id }); } }; });
"""
PAY_HTML = """      <div class="etiket" style="margin-top: 18px"><span>Ödeme</span></div>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-top: 8px">
        <sc-for list="{{pays}}" as="o" hint-placeholder-count="2">
          <button class="odeme" onClick="{{o.pick}}" aria-pressed="{{o.on}}" style="border-color: {{o.bd}}; background: {{o.bg}}">
            <span style="display: flex; align-items: center; justify-content: space-between; gap: 6px"><b style="font-size: 13.5px; font-weight: 600">{{o.n}}</b><sc-if value="{{o.hasPct}}" hint-placeholder-val="{{false}}"><span class="rozet" style="background: #2E6B4F; color: #FFFDF9">%5 indirim</span></sc-if></span>
            <span style="font-size: 12.5px; font-variant-numeric: tabular-nums; color: #5C6078; margin-top: 4px"><b style="color: #1A2142; font-weight: 600">{{o.price}}</b> <s style="opacity: .6">{{o.old}}</s></span>
          </button>
        </sc-for>
      </div>
"""
DATES_JS = """
    var AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
    var now = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kd = new Date(now); do { kd.setDate(kd.getDate() + 1); } while (kd.getDay() === 0 || kd.getDay() === 6);
    var t1 = new Date(kd); t1.setDate(t1.getDate() + 3); var t2 = new Date(kd); t2.setDate(t2.getDate() + 7);
    var kargo = kd.getDate() + ' ' + AY[kd.getMonth()];
    var teslim = t1.getMonth() === t2.getMonth() ? t1.getDate() + '–' + t2.getDate() + ' ' + AY[t2.getMonth()] : t1.getDate() + ' ' + AY[t1.getMonth()] + '–' + t2.getDate() + ' ' + AY[t2.getMonth()];
"""

# ---------------- Fikir 1: Kapıya kadar ----------------
css1 = """.yol{position:relative;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:18px}
.yol .cizgi{position:absolute;left:12.5%;right:12.5%;top:9px;height:2px;background:#E3D8C7}
.yol .dolu{position:absolute;left:12.5%;right:12.5%;top:9px;height:2px;background:#F2A65A;transform-origin:0 50%;transition:transform .9s cubic-bezier(.2,.7,.2,1)}
.durak{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;gap:2px}
.durak .nokta{width:20px;height:20px;border-radius:50%;border:2px solid #C9BFAE;background:#F6F1E9;margin-bottom:6px;transition:background .3s,border-color .3s}
.durak b{font-size:13px;font-weight:600;line-height:1.2}
.durak span{font-size:12px;color:#5C6078;line-height:1.25}"""
html1 = """<div class="pg" style="padding: 22px 0 26px">
  <div class="px">
""" + PAY_HTML + """      <button class="btn" type="button" style="margin-top: 12px">{{ctaLabel}}</button>

      <!-- Kapıya kadar: tahmini teslim satırının yerine. Tarihler İstanbul saatiyle; 1 iş günü + 3–7 gün (mağaza politikası, teyit bekliyor). -->
      <ol class="yol" aria-label="Siparişten teslime" style="list-style: none; padding: 0; margin-bottom: 0">
        <span class="cizgi" aria-hidden="true"></span>
        <span class="dolu" aria-hidden="true" style="transform: scaleX({{fill}})"></span>
        <sc-for list="{{stops}}" as="d" hint-placeholder-count="4">
          <li class="durak"><span class="nokta" aria-hidden="true" style="background: {{d.bg}}; border-color: {{d.bd}}"></span><b>{{d.t}}</b><span>{{d.s}}</span></li>
        </sc-for>
      </ol>
      <p style="margin: 14px 0 0; padding: 10px 12px; border-radius: 12px; background: #FFFDF9; border: 1px solid #EDE3D3; font-size: 13px; line-height: 1.45; text-align: center">{{tail}}</p>
  </div>
</div>
"""
js1 = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { pay: 'online', fill: 0 }; }
  componentDidMount() { var self = this; this.t = setTimeout(function () { self.setState({ fill: 1 }); }, 300); }
  componentWillUnmount() { clearTimeout(this.t); }
  renderVals() {
    var self = this, S = this.state;
    """ + TL_JS + DATES_JS + PAY_JS + """
    var stops = [
      { t: 'Bugün', s: 'Sipariş' },
      { t: 'Bugün', s: 'WhatsApp onayı' },
      { t: kargo, s: 'Kargoda' },
      { t: teslim, s: online ? 'Kapında' : 'Kapıda öde' }
    ].map(function (d, i) { return { t: d.t, s: d.s, bg: i === 0 ? '#F2A65A' : '#F6F1E9', bd: i === 0 ? '#F2A65A' : '#C9BFAE' }; });
    return {
      pays: pays, stops: stops, fill: S.fill,
      ctaLabel: online ? 'Kartla öde · ' + TL(onTotal, true) : 'Kapıda ödemeyle al · ' + TL(total, true),
      tail: online ? 'Kargo takibin WhatsApp\\'a gelir. İlk masal teslim akşamı.' : 'Teslim günü telefonun açık olsun; ödemeyi kapıda nakit ya da kartla yaparsın.'
    };
  }
}"""
open(OUT+'Fikir4-KapiyaKadar.dc.html','w',encoding='utf-8').write(HEAD.format(title='Fikir · Kapıya kadar', css=css1)+html1+TAIL.format(h=330, js=js1))

# ---------------- Fikir 2: Tavana yansıt ----------------
css2 = """.tavan{position:relative;height:320px;border-radius:22px;overflow:hidden;background:linear-gradient(180deg,#0C1027 0%,#141A36 70%,#1A2142 100%)}
.yansima{position:absolute;left:50%;top:44%;width:250px;height:250px;margin:-125px 0 0 -125px;border-radius:50%;overflow:hidden;opacity:0;transform:scale(.92);transition:opacity .6s cubic-bezier(.2,.7,.2,1),transform .6s cubic-bezier(.2,.7,.2,1);-webkit-mask-image:radial-gradient(closest-side,#000 62%,transparent 100%);mask-image:radial-gradient(closest-side,#000 62%,transparent 100%)}
.yansima.on{opacity:.92;transform:none}
.yansima img{width:100%;height:100%;object-fit:cover;display:block}
.dbtn{display:flex;flex-direction:column;align-items:center;gap:6px;background:transparent;border:0;padding:0;cursor:pointer;color:#B9BED6;font:inherit;font-size:12px;width:62px;min-height:84px;flex:none}
.dbtn img{width:52px;height:52px;border-radius:50%;object-fit:cover;outline:2px solid transparent;outline-offset:3px;transition:transform .25s cubic-bezier(.2,.7,.2,1),outline-color .2s}
.dbtn.on{color:#FFFDF9;font-weight:600}
.dbtn.on img{outline-color:#F2A65A;transform:translateY(-4px)}
.noscroll{scrollbar-width:none}.noscroll::-webkit-scrollbar{display:none}"""
html2 = """<div class="pg" style="background: #141A36; color: #EDE5D8; padding: 34px 0 30px">
  <div class="px">
    <h2 class="h2" style="color: #FFFDF9">Altı masal kutuda,<br>altısı hediye.</h2>
    <p style="margin: 8px 0 0; font-size: 15px; color: #B9BED6">Diski seç, tavanda gör.</p>
  </div>
  <div class="px" style="margin-top: 16px">
    <div class="tavan">
      <!-- Duvar–tavan birleşimi: odada olduğunu hissettiren tek çizgi -->
      <svg aria-hidden="true" viewBox="0 0 358 320" style="position: absolute; inset: 0; width: 100%; height: 100%"><path d="M0 262 L72 214 L286 214 L358 262" fill="none" stroke="rgba(255,253,249,.10)" stroke-width="1.5"></path></svg>
      <sc-for list="{{proj}}" as="p" hint-placeholder-count="2">
        <span class="{{p.cls}}" aria-hidden="true"><img src="{{p.src}}" alt=""></span>
      </sc-for>
      <span aria-hidden="true" style="position: absolute; left: 50%; bottom: -60px; width: 180px; height: 120px; margin-left: -90px; border-radius: 50%; background: radial-gradient(closest-side, rgba(242,166,90,.45), rgba(242,166,90,0))"></span>
      <span style="position: absolute; left: 12px; top: 12px; font-size: 12px; font-weight: 600; color: #FFFDF9; background: rgba(12,16,39,.6); padding: 3px 9px; border-radius: 999px">[gerçek tavan fotoğrafı]</span>
      <span style="position: absolute; left: 14px; bottom: 14px; display: flex; flex-direction: column; line-height: 1.2; color: #FFFDF9"><span style="font-size: 12px; color: #B9BED6">Tavanda</span><b class="ser" style="font-size: 22px; font-weight: 400">{{name}}</b></span>
      <span class="rozet" style="position: absolute; right: 14px; bottom: 16px; background: {{tagBg}}; color: {{tagFg}}">{{tag}}</span>
    </div>
  </div>
  <p class="px not" style="margin: 18px 0 0; color: #B9BED6">Kutuda</p>
  <div class="noscroll" style="display: flex; gap: 6px; overflow-x: auto; padding: 8px 16px 0">
    <sc-for list="{{kutu}}" as="d" hint-placeholder-count="6">
      <button class="{{d.cls}}" onClick="{{d.pick}}" aria-pressed="{{d.on}}" aria-label="{{d.n}} diskini tavanda göster"><img src="{{d.src}}" alt=""><span>{{d.n}}</span></button>
    </sc-for>
  </div>
  <p class="px not" style="margin: 12px 0 0; color: #F2A65A">Hediye</p>
  <div class="noscroll" style="display: flex; gap: 6px; overflow-x: auto; padding: 8px 16px 0">
    <sc-for list="{{hediye}}" as="d" hint-placeholder-count="6">
      <button class="{{d.cls}}" onClick="{{d.pick}}" aria-pressed="{{d.on}}" aria-label="{{d.n}} diskini tavanda göster"><img src="{{d.src}}" alt=""><span>{{d.n}}</span></button>
    </sc-for>
  </div>
  <p class="px" style="margin: 12px 0 0; font-size: 12.5px; color: #B9BED6">[Hangi 6 diskin kutuda, hangisinin hediye olduğu teyit edilecek.]</p>
</div>
"""
js2 = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { disc: 1 }; }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    // Canlıda her diskin gerçek tavan yansıma fotoğrafı kullanılır (çizim/AI değil); yalnız seçilen yüklenir, diğerleri lazy.
    var DISCS = [
      { n: 'Ay ve yıldız', id: '63f8557bf1f7867885fdbdedeb19c5ed' }, { n: 'Okyanus', id: '336d1995fe82f1e73d526c0e2697677e' },
      { n: 'Uzay', id: '2c6f33b11e553e39fd315693c5cf692b' }, { n: 'Deniz kızı', id: '6e25420625a6a34858578ba9e632cda7' },
      { n: 'Denizanası', id: '210c9b211afc86f40a3736f7dca41856' }, { n: 'Şato', id: 'c47c719d14b2dd08716967b126324ad7' },
      { n: 'Hayvanlar', id: '81713384676b51d6a15c426fe5ace95f' }, { n: 'Gökkuşağı', id: '6202a8de2d18ea09b2bd1328835a7221' },
      { n: 'Kış gecesi', id: 'de53d54e97de9b7ea6f936c94e218e26' }, { n: 'Taşıtlar', id: '0fa320a5ec8bbbb5066e6e197ba96666' },
      { n: 'Masal', id: 'e10addf033ab0d3bb401f79055402da8' }, { n: 'Doğum günü', id: '10d49c7a953d26c819ef5c9970cd8c6a' }
    ];
    function btn(d, i) { var on = i === S.disc; return { n: d.n, src: B + d.id, on: on ? 'true' : 'false', cls: on ? 'dbtn on' : 'dbtn', pick: function () { self.setState({ disc: i }); } }; }
    var hediyeMi = S.disc >= 6;
    return {
      proj: DISCS.map(function (d, i) { return { src: B + d.id, cls: i === S.disc ? 'yansima on' : 'yansima' }; }),
      kutu: DISCS.slice(0, 6).map(btn), hediye: DISCS.slice(6).map(function (d, i) { return btn(d, i + 6); }),
      name: DISCS[S.disc].n, tag: hediyeMi ? 'Hediye disk' : 'Kutuda',
      tagBg: hediyeMi ? '#F2A65A' : 'rgba(255,253,249,.14)', tagFg: hediyeMi ? '#1A2142' : '#FFFDF9'
    };
  }
}"""
open(OUT+'Fikir5-TavanaYansit.dc.html','w',encoding='utf-8').write(HEAD.format(title='Fikir · Tavana yansıt', css=css2)+html2+TAIL.format(h=760, js=js2))

# ---------------- Fikir 3: Hediye mi? ----------------
css3 = """.anah{display:grid;grid-template-columns:40px minmax(0,1fr) 52px;gap:12px;align-items:center;width:100%;min-height:64px;padding:10px 12px;border-radius:14px;border:1.5px solid;font:inherit;color:#1A2142;text-align:left;cursor:pointer;transition:border-color .25s,background .25s}
.anah .yuva{width:46px;height:28px;border-radius:999px;position:relative;transition:background .3s}
.anah .top{position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:#FFFDF9;box-shadow:0 1px 4px rgba(0,0,0,.25);transition:transform .3s cubic-bezier(.2,.7,.2,1)}
.alan{display:flex;flex-direction:column;gap:5px}
.alan label{font-size:13px;font-weight:600;color:#3A3F5A}
.alan input,.alan textarea{width:100%;min-height:50px;border:1.5px solid #DDD2C1;border-radius:12px;background:#FFFDF9;padding:0 14px;font:inherit;font-size:16px;color:#1A2142}
.alan textarea{padding:12px 14px;min-height:76px;resize:none}
.bilgi{display:grid;grid-template-columns:18px minmax(0,1fr);gap:8px;font-size:13px;line-height:1.45;color:#3A3F5A}
@keyframes ac{from{opacity:0;transform:translateY(-8px)}}
.acil{animation:ac .3s cubic-bezier(.2,.7,.2,1) both}"""
html3 = """<div class="pg" style="padding: 22px 0 26px">
  <div class="px">
    <!-- Hediye mi?: ödemenin hemen üstü, kapalı başlar. Canlıda alanlar sepet özniteliği (cart attributes) olarak kaydedilir. -->
    <button class="anah" type="button" onClick="{{toggle}}" aria-pressed="{{giftOn}}" style="border-color: {{bd}}; background: {{bg}}">
      <span style="width: 40px; height: 40px; border-radius: 12px; background: #F3E9DA; display: grid; place-items: center"><svg class="ico" viewBox="0 0 24 24" style="color: #1A2142"><path d="M20 12v8H4v-8" stroke="#E59A4C"></path><path d="M2.5 8h19v4h-19zM12 8v12M12 8c-1.5-3-5-3.6-5-1.4C7 8 12 8 12 8zM12 8c1.5-3 5-3.6 5-1.4C17 8 12 8 12 8z"></path></svg></span>
      <span style="display: flex; flex-direction: column; line-height: 1.25"><b style="font-size: 15px; font-weight: 600">Hediye mi?</b><span class="mut" style="font-size: 13px">Not ekle, sürpriz bozulmasın</span></span>
      <span class="yuva" aria-hidden="true" style="background: {{track}}"><span class="top" style="transform: translateX({{knob}})"></span></span>
    </button>

    <sc-if value="{{giftOn}}" hint-placeholder-val="{{false}}">
      <div class="acil" style="margin-top: 10px; padding: 14px; border-radius: 16px; background: #FFFDF9; border: 1px solid #EDE3D3; display: flex; flex-direction: column; gap: 12px">
        <div class="alan"><label for="not">Hediye notu</label><textarea id="not" maxlength="120" placeholder="Sevgili [ad], tatlı rüyalar. — Anneannen"></textarea></div>
        <div class="alan"><label for="alici">Alıcının telefonu</label><input id="alici" type="tel" inputmode="tel" autocomplete="off" placeholder="05XX XXX XX XX"></div>
        <div class="bilgi"><svg class="ico" viewBox="0 0 24 24" style="width: 18px; height: 18px; color: #2E6B4F"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg><span>Fatura kutuya konmaz, e-postana gelir. <span class="mut">[muhasebeci teyidi]</span></span></div>
        <div class="bilgi"><svg class="ico" viewBox="0 0 24 24" style="width: 18px; height: 18px; color: #2E6B4F"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg><span>Kargo, teslimde alıcıyı bu numaradan arar. <span class="mut">[kargo teyidi]</span></span></div>
      </div>
    </sc-if>
""" + PAY_HTML + """
    <sc-if value="{{warn}}" hint-placeholder-val="{{false}}">
      <p class="acil" style="margin: 10px 0 0; padding: 10px 12px; border-radius: 12px; background: #F3E9DA; font-size: 13px; line-height: 1.45; color: #1A2142">Hediyede kapıda ödemeyi alıcı yapar ({{kapida}}). Haberi yoksa teslim alamayabilir. <button type="button" onClick="{{toOnline}}" style="display: inline; min-height: 0; padding: 0; border: 0; background: transparent; font: inherit; font-weight: 600; color: #2E6B4F; text-decoration: underline; text-underline-offset: 3px; cursor: pointer">Kartla öde, {{onSave}} daha az öde</button></p>
    </sc-if>
    <button class="btn" type="button" style="margin-top: 12px">{{ctaLabel}}</button>
  </div>
</div>
"""
js3 = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { gift: false, pay: 'online' }; }
  renderVals() {
    var self = this, S = this.state;
    """ + TL_JS + PAY_JS + """
    var g = S.gift;
    return {
      pays: pays, giftOn: g ? 'true' : 'false',
      toggle: function () { self.setState({ gift: !self.state.gift }); },
      bd: g ? '#1A2142' : '#E3D8C7', bg: g ? '#FFFDF9' : 'transparent',
      track: g ? '#1A2142' : '#C9BFAE', knob: g ? '18px' : '0px',
      warn: g && !online, kapida: TL(total, true), onSave: TL(total - onTotal),
      toOnline: function () { self.setState({ pay: 'online' }); },
      ctaLabel: online ? 'Kartla öde · ' + TL(onTotal, true) : 'Kapıda ödemeyle al · ' + TL(total, true)
    };
  }
}"""
open(OUT+'Fikir6-HediyeMi.dc.html','w',encoding='utf-8').write(HEAD.format(title='Fikir · Hediye mi?', css=css3)+html3+TAIL.format(h=620, js=js3))
print('ok')
