# Sihirli Özellikler · 3 sakin varyant (V1 Sade beyaz, V2 Tek vurgu, V3 Liste). Çalıştır: python3 sihirli_varyant.py
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL
OUT = os.path.join(HERE, '..', '..', 'canvas') + '/'

# Ortak: animasyonlar (yalnız transform/opacity; yavaş; azaltılmış harekette durur)
ANIM = r"""
@keyframes nefes{0%,100%{transform:scale(.85);opacity:.5}50%{transform:scale(1.1);opacity:1}}
@keyframes yel{from{transform:rotate(0)}to{transform:rotate(var(--r))}}
@keyframes ses{0%,100%{transform:scaleY(.3)}50%{transform:scaleY(1)}}
@keyframes don{to{transform:rotate(360deg)}}
@keyframes sarj{0%{transform:scaleX(.15)}70%,100%{transform:scaleX(1)}}
.hale{position:absolute;right:-24px;top:-24px;width:112px;height:112px;border-radius:50%;background:radial-gradient(circle,rgba(242,166,90,.38),rgba(242,166,90,0) 65%);animation:nefes 4.5s ease-in-out infinite}
.yelpaze{position:absolute;right:12px;top:14px;width:76px;height:42px}
.yelpaze img{position:absolute;top:0;width:38px;height:38px;border-radius:50%;object-fit:cover;border:2px solid #FFFDF9;box-shadow:0 2px 6px rgba(26,33,66,.18);transform-origin:50% 130%;animation:yel 5s ease-in-out infinite alternate}
.yelpaze img:nth-child(1){right:36px;--r:-12deg}.yelpaze img:nth-child(2){right:18px;--r:0deg;animation-delay:-1.6s}.yelpaze img:nth-child(3){right:0;--r:12deg;animation-delay:-3.2s}
.dalga{display:flex;align-items:flex-end;gap:3px;height:20px}
.dalga i{display:block;width:4px;height:20px;border-radius:2px;background:#E59A4C;transform-origin:50% 100%;animation:ses 2.4s ease-in-out infinite}
.dalga i:nth-child(2){animation-delay:-.4s}.dalga i:nth-child(3){animation-delay:-.8s}.dalga i:nth-child(4){animation-delay:-1.2s}.dalga i:nth-child(5){animation-delay:-1.6s}
.yorunge{position:relative;width:24px;height:24px;border-radius:50%;border:1px dashed #C9BFAE;animation:don 8s linear infinite}
.yorunge::after{content:"";position:absolute;left:50%;top:-3px;width:6px;height:6px;margin-left:-3px;border-radius:50%;background:#E59A4C}
.pil{position:relative;width:44px;height:20px;border:1.6px solid #1A2142;border-radius:6px;padding:2px}
.pil::after{content:"";position:absolute;right:-5px;top:5px;width:3px;height:7px;border-radius:0 2px 2px 0;background:#1A2142}
.pil i{display:block;width:100%;height:100%;border-radius:3px;background:#F2A65A;transform-origin:0 50%;animation:sarj 3.8s ease-in-out infinite}
.ik{width:42px;height:42px;border-radius:12px;display:grid;place-items:center;flex:none;position:relative;z-index:1}
.ik svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.hayal{display:grid;grid-template-columns:minmax(0,1fr) 112px;margin-top:10px;border-radius:20px;overflow:hidden;background:#F3E9DA;color:#1A2142}
.hayal img{width:100%;height:100%;min-height:104px;object-fit:cover;display:block}
.cipm{display:inline-flex;align-items:center;min-height:48px;padding:0 16px;border-radius:999px;border:1.5px solid #E3D8C7;background:#FFFDF9;font:inherit;font-size:14px;font-weight:600;color:#1A2142;cursor:pointer}
.cipm.on{border-color:#1A2142}
"""
ICONS = {
 'ay': '<svg viewBox="0 0 24 24"><path d="M15.5 3.5a8.5 8.5 0 1 0 5 15.4A7 7 0 0 1 15.5 3.5z"></path></svg>',
 'disk': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="2.5"></circle><path d="M12 3a9 9 0 0 1 9 9"></path></svg>',
 'nota': '<svg viewBox="0 0 24 24"><path d="M9 17V6l10-2v11"></path><circle cx="6.5" cy="17" r="2.5"></circle><circle cx="16.5" cy="15" r="2.5"></circle></svg>',
 'robot': '<svg viewBox="0 0 24 24"><path d="M12 3v3"></path><rect x="5" y="6" width="14" height="10" rx="3"></rect><circle cx="9.5" cy="11" r="1.2"></circle><circle cx="14.5" cy="11" r="1.2"></circle><path d="M8 19l1.5-3M16 19l-1.5-3"></path></svg>',
 'pil': '<svg viewBox="0 0 24 24"><rect x="2" y="7" width="17" height="10" rx="2"></rect><path d="M22 11v2M6 10v4M10 10v4"></path></svg>',
}
DISKLER = '<img src="/_blob/336d1995fe82f1e73d526c0e2697677e" alt=""><img src="/_blob/2c6f33b11e553e39fd315693c5cf692b" alt=""><img src="/_blob/6e25420625a6a34858578ba9e632cda7" alt="">'
BASLIK = """<p style="margin: 0 0 6px; font-size: 13px; font-weight: 700; color: #E59A4C">Sihirli özellikler</p>
    <h2 class="h2" style="font-size: 26px">Uyku vakti savaş değil,<br>minik bir masal<span style="color: #E59A4C">.</span></h2>"""
MODEL = """<div style="display: flex; gap: 8px; margin-bottom: 18px"><sc-for list="{{mods}}" as="m" hint-placeholder-count="2"><button class="{{m.cls}}" onClick="{{m.pick}}" aria-pressed="{{m.on}}">{{m.n}}</button></sc-for></div>"""
HAYAL = """<div class="hayal"><div style="padding: 16px; display: flex; flex-direction: column; justify-content: center; gap: 4px"><b style="font-size: 15.5px; line-height: 1.3">Çocuğunun hayalleri artık odasında.</b><span style="font-size: 13px; color: #5C6078">Işığı yak, o gülümsemeyi izle.</span></div><img src="/_blob/652e1893a0ae33a24ee0e3d53edab757" alt="Müşteri paylaşımı"></div>"""
JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { model: 'kiz' }; }
  renderVals() {
    var self = this, S = this.state;
    return {
      kiz: S.model === 'kiz', erkek: S.model !== 'kiz',
      mods: [{ id: 'kiz', n: 'Kız modeli' }, { id: 'erkek', n: 'Erkek modeli' }].map(function (m) { var on = S.model === m.id; return { n: m.n, on: on ? 'true' : 'false', cls: on ? 'cipm on' : 'cipm', pick: function () { self.setState({ model: m.id }); } }; })
    };
  }
}"""

def kart(cls, ik_cls, ik_style, icon, title, text, ust='', alt=''):
    return f'<div class="{cls}">{ust}<span class="ik {ik_cls}" style="{ik_style}" aria-hidden="true">{icon}</span><b>{title}</b><span class="t">{text}</span>{alt}</div>'

def dort(cls_list, ik_styles):
    c1, c2, c3, c4 = cls_list; s1, s2, s3, s4 = ik_styles
    k = [kart(c1, '', s1, ICONS['ay'], 'Mışıl mışıl uykular', 'Yumuşacık ışık, huzurlu bir geçiş.', ust='<span class="hale" aria-hidden="true"></span>'),
         kart(c2, '', s2, ICONS['disk'], '+6 hediye disk', 'Her gece yeni bir masal; siparişe dahil.', ust='<span class="yelpaze" aria-hidden="true">' + DISKLER + '</span>'),
         '<sc-if value="{{kiz}}" hint-placeholder-val="{{true}}">' + kart(c3, '', s3, ICONS['nota'], 'Bluetooth ninni', 'Telefondan bağlan, lambadan çalsın.', alt='<span class="dalga" aria-hidden="true" style="margin-top: auto"><i></i><i></i><i></i><i></i><i></i></span>') + '</sc-if>',
         '<sc-if value="{{erkek}}" hint-placeholder-val="{{false}}">' + kart(c3, '', s3, ICONS['robot'], 'Uzay Kaşifi', 'Robot projektör, tavanda uzay.', alt='<span class="yorunge" aria-hidden="true" style="margin-top: auto"></span>') + '</sc-if>',
         kart(c4, '', s4, ICONS['pil'], 'Kablosuz kullanım', 'Şarj et, her yere taşı.', alt='<span class="pil" aria-hidden="true" style="margin-top: auto"><i></i></span>')]
    return '<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; margin-top: 14px">' + ''.join(k) + '</div>'

KART_CSS = """.kk{position:relative;overflow:hidden;min-height:164px;padding:16px;border-radius:20px;display:flex;flex-direction:column;gap:10px;background:#FFFDF9;border:1px solid #EDE3D3;box-shadow:0 10px 26px rgba(26,33,66,.06);color:#1A2142}
.kk b{font-size:15px;font-weight:700;line-height:1.25;position:relative;z-index:1}
.kk span.t{font-size:13px;line-height:1.45;color:#5C6078;position:relative;z-index:1}
.kk.koyu{background:#1A2142;border-color:#1A2142;color:#FFFDF9}
.kk.koyu span.t{color:#B9BED6}"""

# V1 · Sade beyaz (eski bloğa sadık): dört kart beyaz, ikon kutusu lacivert + amber ikon
v1 = """<div class="pg"><div style="padding: 24px 16px 28px">
  """ + MODEL + BASLIK + dort(['kk','kk','kk','kk'], ['background: #1A2142; color: #F2A65A']*4) + HAYAL + """
</div></div>
"""
open(OUT + 'Sihirli-V1-SadeBeyaz.dc.html', 'w', encoding='utf-8').write(HEAD.format(title='Sihirli Özellikler · V1 Sade beyaz', css=ANIM + KART_CSS) + v1 + TAIL.format(h=640, js=JS))

# V2 · Tek vurgu: yalnız ilk kart lacivert; diğerleri beyaz, ikon kutusu krem + lacivert ikon
v2 = """<div class="pg"><div style="padding: 24px 16px 28px">
  """ + MODEL + BASLIK + dort(['kk koyu','kk','kk','kk'], ['background: rgba(255,253,249,.1); color: #F2A65A', 'background: #F3E9DA; color: #1A2142', 'background: #F3E9DA; color: #1A2142', 'background: #F3E9DA; color: #1A2142']) + HAYAL + """
</div></div>
"""
open(OUT + 'Sihirli-V2-TekVurgu.dc.html', 'w', encoding='utf-8').write(HEAD.format(title='Sihirli Özellikler · V2 Tek vurgu', css=ANIM + KART_CSS) + v2 + TAIL.format(h=640, js=JS))

# V3 · Liste: tek beyaz panel, dört satır; animasyon satırın sağında
LISTE_CSS = """.panel{margin-top:14px;border-radius:22px;background:#FFFDF9;border:1px solid #EDE3D3;box-shadow:0 10px 26px rgba(26,33,66,.06);overflow:hidden}
.sat{position:relative;display:grid;grid-template-columns:42px minmax(0,1fr) 56px;gap:12px;align-items:center;min-height:76px;padding:12px 14px;color:#1A2142}
.sat+.sat,.panel sc-if + .sat{border-top:1px solid #EDE3D3}
.sat b{display:block;font-size:15px;font-weight:700;line-height:1.25}
.sat span.t{display:block;font-size:13px;color:#5C6078;line-height:1.4;margin-top:2px}
.sat .yer{position:relative;height:42px;display:grid;place-items:center}
.sat .hale{right:-6px;top:-14px;width:70px;height:70px}
.sat .yelpaze{position:relative;right:auto;top:auto;width:56px;height:30px}
.sat .yelpaze img{width:28px;height:28px}
.sat .yelpaze img:nth-child(1){right:24px}.sat .yelpaze img:nth-child(2){right:12px}"""
def satir(icon, title, text, yer):
    return f'<div class="sat"><span class="ik" style="background: #1A2142; color: #F2A65A" aria-hidden="true">{icon}</span><span><b>{title}</b><span class="t">{text}</span></span><span class="yer" aria-hidden="true">{yer}</span></div>'
v3_rows = (satir(ICONS['ay'], 'Mışıl mışıl uykular', 'Yumuşacık ışık, huzurlu bir geçiş.', '<span class="hale"></span>')
  + satir(ICONS['disk'], '+6 hediye disk', 'Her gece yeni bir masal; siparişe dahil.', '<span class="yelpaze">' + DISKLER + '</span>')
  + '<sc-if value="{{kiz}}" hint-placeholder-val="{{true}}">' + satir(ICONS['nota'], 'Bluetooth ninni', 'Telefondan bağlan, lambadan çalsın.', '<span class="dalga"><i></i><i></i><i></i><i></i><i></i></span>') + '</sc-if>'
  + '<sc-if value="{{erkek}}" hint-placeholder-val="{{false}}">' + satir(ICONS['robot'], 'Uzay Kaşifi', 'Robot projektör, tavanda uzay.', '<span class="yorunge"></span>') + '</sc-if>'
  + satir(ICONS['pil'], 'Kablosuz kullanım', 'Şarj et, her yere taşı.', '<span class="pil"><i></i></span>'))
v3 = """<div class="pg"><div style="padding: 24px 16px 28px">
  """ + MODEL + BASLIK + '<div class="panel">' + v3_rows + '</div>' + HAYAL + """
</div></div>
"""
open(OUT + 'Sihirli-V3-Liste.dc.html', 'w', encoding='utf-8').write(HEAD.format(title='Sihirli Özellikler · V3 Liste', css=ANIM + LISTE_CSS) + v3 + TAIL.format(h=600, js=JS))
print('ok')
