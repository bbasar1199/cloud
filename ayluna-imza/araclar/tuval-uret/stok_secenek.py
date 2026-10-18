# LunaDream · E stok satırı seçenekleri (18 Eki). Çalıştır: python3 stok_secenek.py
# Kullanıcı: "Hatta stok kısmı için de uygun bir tasarım deneyebilir miyiz, UI."
# Şimdiki hâl: butonun üstünde düz yazı "Stokta son 18 adet" + 3 kez yanıp sönen nokta.
# Kurallar: sayı elle girilir (tema ayarı), boşsa satır yok; oranlı stok çubuğu yok (paydası uydurma olur);
# sayan rakam yok; tek amber; hareket bir kez, yalnız transform/opacity; azaltılmış harekette durur.
# Üç seçenek, aynı bağlamda (dönen satırın altı, Güvenli Ödeme butonunun üstü):
#   A · Yıldız dizisi: her adet bir nokta (en çok 20; üstünde yalnız yazı). Noktalar soldan sağa bir kez yanar, sonuncusu nabız atar.
#   B · Serif sayı: sayı Young Serif ile büyük, yanında iki satır yazı; altındaki amber çizgi bir kez çizilir.
#   C · Buton kurdelesi: paket kartındaki "En avantajlı" kurdelesinin dili; butonun üst kenarına oturur, satır yer kaplamaz.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL
import luna_e as E
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE-Stok.dc.html')
STOK = 18

HILAL = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="%s"></path></svg>' % E.ay(.22)

CSS = E.CSS + r"""
.pg{background:#F6F1E9;padding-bottom:24px}
.oneri{display:flex;align-items:center;gap:8px;margin:0 0 6px;padding-top:18px;border-top:1px dashed #D6CAB6;font-size:13px;font-weight:700;color:#A05A1C}
.oneri-alt{margin:0 0 14px;font-size:13px;line-height:1.45;color:#5C6078;text-wrap:pretty}
.blok{padding:0 16px 30px}
.blok .btn-on{margin-top:14px}
.btn-on,.btn-kp{pointer-events:none}
.sim .donen{margin-top:0}
/* A · Yıldız dizisi */
.sk-a{margin:16px 0 0}
.sk-a p{margin:0;font-size:14px;color:#1A2142}
.sk-a b{font-variant-numeric:tabular-nums}
.sk-a .dz{display:flex;flex-wrap:wrap;gap:5px;margin-top:8px}
.sk-a .dz i{width:8px;height:8px;border-radius:50%;background:#F2A65A;opacity:0;transform:scale(.4);animation:dz-yan .4s cubic-bezier(.2,.7,.2,1) both;animation-delay:calc(var(--i) * 45ms + .3s)}
.sk-a .dz i:last-child{animation:dz-yan .4s cubic-bezier(.2,.7,.2,1) both,dz-nabiz 1.6s ease-in-out 3;animation-delay:calc(var(--i) * 45ms + .3s),calc(var(--i) * 45ms + .8s)}
@keyframes dz-yan{to{opacity:1;transform:none}}
@keyframes dz-nabiz{0%,100%{box-shadow:0 0 0 0 rgba(242,166,90,.5)}50%{box-shadow:0 0 0 5px rgba(242,166,90,0)}}
/* B · Serif sayı */
.sk-b{display:flex;align-items:center;gap:12px;margin:16px 0 0}
.sk-b .sy{position:relative;font-family:"Young Serif",Georgia,serif;font-size:34px;line-height:1;color:#1A2142;font-variant-numeric:tabular-nums}
.sk-b .sy::after{content:"";position:absolute;left:0;right:0;bottom:-5px;height:2px;border-radius:1px;background:#F2A65A;transform:scaleX(0);transform-origin:0 50%;animation:sy-ciz .7s cubic-bezier(.2,.7,.2,1) .4s both}
@keyframes sy-ciz{to{transform:none}}
.sk-b .yz{display:flex;flex-direction:column;font-size:14px;line-height:1.3;color:#5C6078}
.sk-b .yz b{color:#1A2142}
/* C · Buton kurdelesi */
.sk-c{position:relative;margin-top:24px}
.sk-c .btn-on{margin-top:0}
.sk-c .kd{position:absolute;left:18px;top:-12px;z-index:1;display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 10px 0 8px;border-radius:999px;background:#1A2142;color:#FFFDF9;font-size:12px;font-weight:700;white-space:nowrap;animation:kd-in .5s cubic-bezier(.2,.7,.2,1) .4s both}
.sk-c .kd svg{width:14px;height:14px}.sk-c .kd circle{fill:none;stroke:rgba(255,253,249,.7);stroke-width:1.6}.sk-c .kd path{fill:#F2A65A}
@keyframes kd-in{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.sk-a .dz i,.sk-a .dz i:last-child,.sk-b .sy::after,.sk-c .kd{animation:none;opacity:1;transform:none}}
"""

DONEN = ('<p class="donen"><span class="dn-s on"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle>'
         '<path d="' + E.ay(.22) + '"></path></svg>Her kutuda +6 hediye masal diski</span></p>')
BTN = '<button class="btn-on" type="button">Güvenli Ödeme ile Al · ₺2.612,49</button>'
KP = '<button class="btn-kp" type="button">Kapıda Ödeme ile Sipariş Ver</button>'

A = ('<div class="sk-a" role="img" aria-label="Stokta son %d adet"><p>Stokta son <b>%d</b> adet</p><span class="dz" aria-hidden="true">%s</span></div>'
     % (STOK, STOK, ''.join('<i style="--i: %d"></i>' % i for i in range(min(STOK, 20)))))
B = ('<div class="sk-b"><span class="sy">%d</span><span class="yz"><b>adet kaldı</b><span>stokta</span></span></div>' % STOK)
C = '<div class="sk-c"><span class="kd">%sStokta son %d adet</span>%s</div>' % (HILAL, STOK, BTN)


def blok(ad, alt, ic, btn=True):
    return ('<section class="blok"><p class="oneri">%s</p><p class="oneri-alt">%s</p><div class="sim">%s%s%s%s</div></section>'
            % (ad, alt, DONEN, ic, BTN if btn else '', KP))


HTML = ('<div class="pg">\n<div class="px" style="padding-top: 20px"><h1 class="dev" style="font-size: 26px">Stok satırı<span>.</span></h1>'
        '<p class="oneri-alt" style="margin-top: 6px">Butonun üstündeki "Stokta son 18 adet" için üç deneme. Sayı elle girilir; boşsa hiçbiri görünmez.</p></div>\n'
        + blok('A · Yıldız dizisi', 'Her adet bir nokta; açılınca soldan sağa bir kez yanar, sonuncusu nabız atar. 20 adetten fazlaysa yalnız yazı.', A)
        + blok('B · Serif sayı', 'Sayı başlık yazı tipiyle büyük; altındaki amber çizgi bir kez çizilir. Fiyatla aynı ses.', B)
        + blok('C · Buton kurdelesi', 'Paket kartındaki "En avantajlı" kurdelesinin dili; butonun üst kenarına oturur, ayrı satır kaplamaz.', C, btn=False)
        + '\n</div>\n')

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = {}; }
  renderVals() { return {}; }
}"""

if __name__ == '__main__':
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · E stok satırı', css=CSS) + HTML + TAIL.format(h=int(os.environ.get('SK_H', 1200)), js=JS))
    print('yazıldı:', OUT)
