# LunaDream ürün sayfası · E (Tur 21): B+ Gece Postası'nın dili. Çalıştır: python3 luna_e.py
# Kullanıcı (E'ye): "Sipariş fişini kaldır, emoji benefiti düzelt, yazım hataları berbat, yazı fontu kötü; her şey çok yabancı
# duruyor, bir bütün ve uyum yakala." E bu yüzden seçilen B+'nın üstüne yeniden kuruldu: Young Serif + Onest, krem/lacivert/amber,
# Sihirli V1 (2×2 beyaz kart), satır kart seçiciler (Tur 25) ve iki buton. 21 Eki: "Bir gece, beş an" kalktı (kullanıcı: "bir şey hissettirmiyor"); yerine "Odası böyle görünecek" Gece vitrini.
# Önceki E (Literata + Atkinson, D'nin dili) git geçmişinde: Tur 20.
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import HEAD, TAIL, TL_JS, KARGO_JS, urun_ust, masa_bayrak, SERIT_OK, SERIT_OK_CSS, KAY_JS, serit_ok, GAL_OK, GALOK_JS
import sihirli2_varyant as S2
import ozellik4_varyant as OZ4



def ay(f, r=9, c=12):
    # Ay evresi yolu: f = aydınlık kısım (0..1), sağdan dolar
    rx = abs(1 - 2 * f) * r
    return 'M%d %dA%d %d 0 0 1 %d %dA%.2f %d 0 0 %d %d %dZ' % (c, c - r, r, r, c, c + r, rx, r, 0 if f < .5 else 1, c, c - r)


def muhur():
    # 30 gün mührü: halkada 8 ay evresi (yeni aydan dolunaya ve geri); 30 gün ≈ bir ay döngüsü
    g = ''
    for i in range(8):
        a = math.radians(-90 + i * 45)
        x, y = 52 + 41 * math.cos(a), 52 + 41 * math.sin(a)
        f = [0, .25, .5, .75, 1, .75, .5, .25][i]
        ters = ' transform="matrix(-1 0 0 1 24 0)"' if i > 4 else ''  # küçülen ay öbür yandan aydınlık
        g += '<g transform="translate(%.1f %.1f) scale(.5)"><circle cx="12" cy="12" r="9"></circle>%s</g>' % (x - 6, y - 6, '<path d="%s"%s></path>' % (ay(f), ters) if f else '')
    return '<svg class="muhur" viewBox="0 0 104 104" aria-hidden="true"><circle class="mh-halka" cx="52" cy="52" r="50.5"></circle>' + g + '</svg>'


# Teslim çizgisi: hilal (bugün) → yarım ay (kargoda) → dolunay (kapında). Kaydırınca sırayla dolar.
YOL = ''.join('<li><svg class="evre" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="%s"></path></svg>%s<b>%s</b><span>%s</span></li>' % (ay(f), ek, b, t)
              for f, b, t, ek in [(.22, 'Bugün', 'Sipariş verildi', ''), (.5, '{{kargo}}', 'Kargoda', ''),
                                  (1, '{{teslim}}', 'Kapında', '<span class="yol-lamba" aria-hidden="true">' + S2.IKON + '</span>')])
# Ürün soruları: kapalı soruda hilal, açılınca dolunay (teslim çizgisiyle aynı ay çizimi); sağda ok
URS_AY = ''.join('<svg class="evre %s" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="%s"></path></svg>' % (c, ay(f)) for c, f in (('hilal', .22), ('dolu', 1)))
URS_OK = '<svg class="urs-ok" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"></path></svg>'
# Paket kutusu (teslim çizelgesinde ekranda akar)
KUTU = '<svg class="kutu" viewBox="0 0 16 16" aria-hidden="true"><path d="M2.5 5.2L8 2.5l5.5 2.7v5.6L8 13.5l-5.5-2.7z"></path><path d="M2.5 5.2L8 7.9l5.5-2.7M8 7.9v5.6"></path></svg>'
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamE.dc.html')

CSS = r""".pg{background:#F6F1E9}
/* Renkler (Tur 22, kullanıcı: "renkler birbirine giriyor, büyük marka hissi yok"): 50 tondan 12'ye indi.
   Açık: krem #F6F1E9 zemin · yüzey #FFFDF9 kart · ton #F1E8DA rozet/çip/boş görsel · çizgi #E3D8C7 · kesik #D6CAB6
   Yazı: lacivert #1A2142 · soluk #5C6078 · kehribar #A05A1C (küçük etiket) · yeşil #2E6B4F (yalnız "Dün [X] kişi satın aldı")
   Işık: amber #F2A65A tek turuncu (buton, ay, yıldız, evre, başlık noktası); açık zeminde basma gölgesi #C97F38, koyuda gölge lacivert
   Koyu: gece #1A2142 panel · gece2 #0C1027 fotoğraf zemini · koyuda ikincil #B9BED6. Amber yalnız ışık ve ana butonda; bir ekranda bir amber blok. */
/* Sahne (Tur 8, kullanıcı: "görsel kısmı Main'deki gibi, ama bizim ürün görsellerimiz"): gece laciverti zemin, üstte logo,
   kare ürün fotoğrafı kırpılmadan tam genişlik, alt kenarı geceye karışır; diskler fotoğrafın kenarlarında yavaşça süzülür;
   küçük resimler ve sayaç fotoğrafın üstünde; altına yuvarlak köşeli levha biner. "Işığı aç" anahtarı yok (17 Ekim kararı). */
/* Kare galeri (kullanıcı, 19 Eki: Shopify'daki gibi): görsel logo bandının altında tam kare, üstüne gölge ya da yüzen öğe binmez; ay göstergesi altında. */
/* Kullanıcı (19 Eki, "bu altında görsellerin böyle kalmayacak değil mi" → "Şerit kalksın"): fotoğrafın altındaki koyu bant yok; logo bandı koyu kalır,
   fotoğraf kenardan kenara kare. Sonra: "o gömülü olsun fotoğrafların değiştiği zımbırtı; estetiği bozan hiçbir detay istemiyorum" →
   gösterge fotoğrafın içinde, en alt kenarda ortada ince çizgiler (her fotoğrafa bir; geçilenler beyaz). Ay simgeleri afişlerin alt yazısına
   biniyordu, çizgi hiçbir afişte yazıya değmez. Altında satır, not ya da "Temsilî görseller" yok. */
.sahne{position:relative;background:transparent;overflow:hidden}
.sahne header{position:relative;height:56px;display:flex;justify-content:space-between;align-items:center;padding:0 4px;z-index:3;background:#0C1027;color:#FFFDF9}
.sahne .kare-foto{position:relative;width:100%;aspect-ratio:1/1;display:flex;overflow-x:auto;scroll-snap-type:x mandatory;overscroll-behavior-x:contain;scrollbar-width:none}
.sahne .kare-foto::-webkit-scrollbar{display:none}
.kf{position:relative;flex:0 0 100%;scroll-snap-align:start}
.sahne .gec{position:absolute;top:0;bottom:0;width:50%;z-index:1;padding:0;border:0;background:transparent;cursor:pointer}
.sahne .kare-foto img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
@keyframes suz{0%,100%{transform:translateY(0) rotate(var(--r))}50%{transform:translateY(-10px) rotate(calc(var(--r) + 10deg))}}
.yuzen{position:absolute;z-index:2;border-radius:50%;overflow:hidden;box-shadow:0 10px 18px -8px rgba(0,0,0,.7),0 0 0 2px rgba(255,253,249,.32);animation:suz 7s ease-in-out infinite}
.yuzen img{width:100%;height:100%;object-fit:cover;display:block}
.seritler{position:absolute;left:0;right:0;bottom:6px;z-index:2;display:flex;justify-content:center;pointer-events:none}
/* Galeri göstergesi (küçük resimlerin yerine, kullanıcı: "görünmesin, kaydırılır olsun; altlarına ay animasyonu, sayfa geçtikçe tamamlanıyor gibi"):
   her fotoğrafa bir ay; geçtikçe evreler yanar, son fotoğrafta dolunay. Hareket yalnız transform/opacity. */
.ay-iz{display:flex;gap:4px;filter:drop-shadow(0 1px 1.5px rgba(12,16,39,.5))}
.ay-iz i{display:block;width:16px;height:3px;border-radius:2px;background:rgba(255,253,249,.4);transition:background-color .3s cubic-bezier(.2,.7,.2,1)}
.ay-iz .lit{background:#FFFDF9}
.sira{flex:none;font-size:13px;font-weight:600;font-variant-numeric:tabular-nums;padding:4px 9px;border-radius:999px;background:#0C1027}
.levha{position:relative;z-index:4;background:#F6F1E9;padding-top:4px}
/* Yazı ölçeği (Tur 11, kullanıcı: "yazı bazı yerlerde çok büyük, düzensiz"):
   başlık 1: 44 (yalnız LunaDream) · bölüm başlığı: 26 · büyük rakam: 40 (puan, saat, 30 gün) · kart başlığı: 18–20
   gövde: 16 · açıklama: 15 · not: 13 · etiket: 12. Bölüm etiketi tek stil: 13px kalın, #A05A1C, büyük harf yok. */
.pg{font-size:15px}
/* overflow:clip kaydırma kabı oluşturmaz; yapışkan öğeler çalışır. Canlı temada sarmalayıcılarda overflow:hidden olmamalı. */
.pg{overflow:clip;margin:0 auto}
.h2{font-size:22px;line-height:1.15}
.etiket{font-size:13px}
.etiket>span:first-child{text-transform:none;letter-spacing:0;font-size:13px;font-weight:700;color:#A05A1C}
.duyuru{display:flex;justify-content:center;align-items:center;gap:8px;height:36px;background:#0C1027;color:#B9BED6;font-size:13px;font-weight:600;border-bottom:1px solid rgba(255,253,249,.08)}
.sayac-ay{width:14px;height:14px;flex:none}.sayac-ay circle{fill:none;stroke:rgba(185,190,214,.6);stroke-width:1.6}.sayac-ay path{fill:#F2A65A}
.duyuru b{font-variant-numeric:tabular-nums;font-weight:700;letter-spacing:.02em;color:#F2A65A}
/* Ad satırı: solda ad, sağda puan (iki satır, sağa yaslı); puanın yıldızları ışık, tek amber */
.ad-satir{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-top:6px}
.ad-satir .dev{margin:0}
.puan{display:flex;flex-direction:column;align-items:flex-end;justify-content:center;gap:3px;min-height:48px;text-decoration:none;color:#1A2142;white-space:nowrap}
.puan-ust{display:flex;align-items:center;gap:6px;font-size:15px;line-height:1}
.puan-ust .yildiz{font-size:14px}
.puan-ust b{font-weight:700;font-variant-numeric:tabular-nums}
.puan-alt{font-size:13px;line-height:1.2;color:#5C6078;text-decoration:underline;text-decoration-color:#D6CAB6;text-underline-offset:3px}
/* Dün satırı (kullanıcı, 18 Eki: "Stokta'yı kaldıralım, altına dün şu kadar kişi satın aldı"): sayı elle girilir, boşsa satır yok */
.dun{display:flex;align-items:center;gap:8px;margin:8px 0 0;font-size:14px;color:#5C6078}
.dun b{color:#1A2142;font-variant-numeric:tabular-nums}
.dun i{position:relative;flex:none;width:8px;height:8px;border-radius:50%;background:#2E6B4F}
/* Dün satırı girişi (kullanıcı, 18 Eki: "hafif bir animasyon, tasarım diline uygun"): fiyat düşüşünün devamı, bir kez.
   Fiyat 1,9 sn'de yerine oturunca satır 6px aşağıdan gelir, sayı fiyattaki gibi yukarıdan düşer, nokta üç kez yumuşak halka verir.
   Sayan rakam yok; yalnız transform/opacity. */
.dun{animation:dun-gel .5s cubic-bezier(.2,.7,.2,1) 1.9s both}
.dun b{display:inline-block;animation:fy-dus 1s cubic-bezier(.2,.7,.2,1) 1.9s both}
.dun i::after{content:"";position:absolute;inset:0;border-radius:50%;background:#2E6B4F;opacity:0;animation:dun-hale 1.8s cubic-bezier(.2,.7,.2,1) 2.5s 3}
@keyframes dun-gel{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
@keyframes dun-hale{0%{opacity:.45;transform:scale(1)}100%{opacity:0;transform:scale(2.8)}}
@media (prefers-reduced-motion:reduce){.dun,.dun b,.dun i::after{animation:none}}
.indirim{font-size:12px;font-weight:700;padding:3px 8px;border-radius:999px;background:#FFFDF9;box-shadow:inset 0 0 0 1px #E3D8C7;color:#A05A1C}
/* Bölüm geçişi (Tur 12, kullanıcı isteği): kaydırınca bölüm 20px aşağıdan ve saydamdan gelir. Yalnız transform/opacity.
   Tarayıcı desteklemiyorsa ya da azaltılmış hareket açıksa hiç oynamaz, içerik hep görünür. */
@supports (animation-timeline: view()){
  .gir{animation:gir linear both;animation-timeline:view();animation-range:entry 0% entry 35%}
  @keyframes gir{from{opacity:.001;transform:translateY(20px)}to{opacity:1;transform:none}}
}
.ikon{width:48px;height:48px;display:grid;place-items:center;background:transparent;border:0;color:inherit;cursor:pointer}
.yildiz{position:relative;display:inline-block;letter-spacing:1px;color:#D6CAB6;line-height:1}
.yildiz i{position:absolute;left:0;top:0;overflow:hidden;white-space:nowrap;color:#F2A65A;font-style:normal}
.dev{font-family:"Young Serif",Georgia,serif;font-size:28px;line-height:1.05;letter-spacing:-.02em;margin:4px 0 0;color:#1A2142;white-space:nowrap}
.dev span,.h2 span.n{color:#F2A65A}
.cip:active{transform:scale(.985)}
.kesim{position:absolute;left:50%;bottom:4px;height:44px;width:auto;max-width:46px;transform:translateX(-50%)}
.msub{font-size:12px;color:#5C6078;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
/* Sihirli Özellikler · Canlı kartlar (21 Eki; kullanıcı: "emoji benefit kısmını daha kurumsal yapsak, UI'lerle doldursak;
   dönen diskler sırayla masal diskini gidip gelse gibi tatlı ufak sekanslar"; eleştirmen 7/10, kullanıcı seçti).
   2×2 beyaz kart kalır; her kartın üstünde ton ekran (#F1E8DA) ve sekans: disk şeridi (kayarken yuvarlanır, durunca sabit),
   3 parlaklık, Bluetooth bağlan → çal, pil dolar ve fiş çıkar (lamba şarjda sönük). Kartlar 0,6 sn arayla başlar.
   Mini arayüz CSS'i sihirli2_varyant.MINI_CSS (pano ile aynı). Lamba ikonu modele bağlı (Kız atlıkarınca / Erkek robot). */
.sih{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:12px}
""" + S2.MINI_CSS + OZ4.CSS + r"""
/* Paket (canlı sitedeki biçim) */
/* Seçiciler (Tur 25, kullanıcı seçimi "Satır kartlar"): model, paket ve 2. lamba tek dil. Aynı kart (yüzey, 1,5px çizgi,
   20px köşe), aynı küçük görsel (açık ton zeminde stüdyo kesimi), aynı seçili durum: 2px lacivert çerçeve + amber dolunay noktası.
   Dolu lacivert kart yok. Renk anlık değişir; hareket yalnız noktada (opacity/transform). */
.kt{position:relative;display:block;width:100%;padding:0;border:1.5px solid #E3D8C7;border-radius:20px;background:#FFFDF9;color:#1A2142;font:inherit;text-align:left;cursor:pointer;transition:transform .2s cubic-bezier(.2,.7,.2,1)}
.kt.on{border-color:#1A2142;box-shadow:inset 0 0 0 .5px #1A2142}
button.kt:active,.kt>button:active,.lcip:active{transform:scale(.985)}
.ayr{width:22px;height:22px;flex:none}
.ayr .h{fill:#FFFDF9;stroke:#D6CAB6;stroke-width:1.6}
.ayr .d{fill:#F2A65A;opacity:0;transform:scale(.3);transform-origin:12px 12px;transition:opacity .25s cubic-bezier(.2,.7,.2,1),transform .25s cubic-bezier(.2,.7,.2,1)}
.on .ayr .h{stroke:#1A2142}
.on .ayr .d{opacity:1;transform:none}
.ek .lcip .ayr .h{stroke:#D6CAB6}.ek .lcip .ayr .d{opacity:0;transform:scale(.3)}
.ek .lcip.on .ayr .h{stroke:#1A2142}.ek .lcip.on .ayr .d{opacity:1;transform:none}
.kurdele{position:absolute;right:14px;top:-11px;z-index:1;padding:2px 10px;border-radius:999px;background:#1A2142;color:#FFFDF9;font-size:12px;font-weight:700;line-height:1.5;white-space:nowrap}
.tl{position:relative;flex:none;width:56px;height:64px;border-radius:14px;background:#F1E8DA;overflow:hidden}
.tl img{position:absolute;left:50%;bottom:6px;height:50px;width:auto;transform:translateX(-50%)}
.tl.cift{width:64px}
.tl.cift img{height:44px}
.tl.cift img:nth-child(1){left:33%}.tl.cift img:nth-child(2){left:69%}
.sat{display:flex;align-items:center;gap:10px;width:100%;min-height:80px;padding:8px 14px 8px 8px;border:0;background:none;font:inherit;color:inherit;text-align:left;cursor:pointer;border-radius:18px}
.sat-orta{flex:1;min-width:0;line-height:1.2}
.sat-sag{display:flex;flex-direction:column;align-items:flex-end;text-align:right;font-variant-numeric:tabular-nums;line-height:1.2}
.ad{display:block;font-size:17px;font-weight:700;letter-spacing:-.02em}
.alt{display:block;margin-top:3px;font-size:13px;color:#5C6078;font-variant-numeric:tabular-nums}
.fiyat{display:block;font-size:18px;font-weight:700;letter-spacing:-.02em}
.eski{display:block;margin-top:2px;font-size:13px;color:#5C6078}
.yarim-iz{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:10px}
.yarim{min-height:72px;padding:8px 10px 8px 8px}
.yarim .tl{width:48px;height:56px}
.yarim .tl img{height:44px}
.pk-liste{display:flex;flex-direction:column;gap:16px;margin-top:16px}
.ek{display:flex;align-items:center;justify-content:space-between;gap:8px;margin:0 14px;padding:10px 0 12px;border-top:1px solid #E3D8C7}
.ek-ad{font-size:13px;font-weight:700;color:#1A2142;white-space:nowrap}
.cipler{display:flex;gap:8px}
.lcip{display:inline-flex;align-items:center;gap:6px;min-height:48px;padding:0 8px 0 4px;border:1.5px solid #E3D8C7;border-radius:999px;background:#FFFDF9;font:inherit;font-size:14px;font-weight:600;color:#1A2142;cursor:pointer;transition:transform .2s cubic-bezier(.2,.7,.2,1)}
.lcip.on{border-color:#1A2142;box-shadow:inset 0 0 0 .5px #1A2142}
.lcip .ayr{width:18px;height:18px}
.cip-y{position:relative;width:36px;height:36px;border-radius:50%;background:#F1E8DA;overflow:hidden}
.cip-y img{position:absolute;left:50%;bottom:3px;height:29px;width:auto;transform:translateX(-50%)}
/* Dönen satır (kullanıcı, 18 Eki): hediye diski ↔ aynı gün kargo + 16.00 sayacı. İki satır aynı ızgara hücresinde, kutu en uzunu
   kadar; dönerken yükseklik değişmez. Giren alttan, çıkan yukarı (yalnız transform/opacity). Hareket azaltılmışsa ikisi alt alta. */
/* Renk (kullanıcı, 18 Eki: "lacivert rengimize çevirsek daha bütün görünür"): lacivert zemin, ay beyazı yazı, ışık yalnız hilalde. */
.donen{position:relative;display:grid;margin:12px 0 0;padding:10px 14px;border-radius:14px;background:#1A2142;font-size:14px;font-weight:700;color:#FFFDF9;overflow:hidden}
.dn-s{grid-area:1/1;display:flex;align-items:center;gap:8px;min-height:24px;opacity:0;transform:translateY(80%);transition:opacity .36s cubic-bezier(.2,.7,.2,1),transform .36s cubic-bezier(.2,.7,.2,1)}
.dn-s.on{opacity:1;transform:none}.dn-s.ust{transform:translateY(-80%)}
.dn-s svg{width:16px;height:16px;flex:none}.dn-s circle{fill:none;stroke:rgba(255,253,249,.7);stroke-width:1.6}.dn-s path{fill:#F2A65A}
.dn-m{flex:1;min-width:0;font-size:13px;line-height:1.3}
.dn-sy{flex:none;padding:3px 8px;border-radius:999px;background:rgba(255,253,249,.14);color:#FFFDF9;font-size:14px;font-variant-numeric:tabular-nums;letter-spacing:.02em}
.dn-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
@media (prefers-reduced-motion:reduce){.donen{row-gap:8px}.dn-s{grid-area:auto;opacity:1;transform:none;transition:none}}
.btn-on{display:flex;align-items:center;justify-content:center;width:100%;min-height:62px;margin-top:20px;border:0;border-radius:20px;background:#F2A65A;color:#1A2142;font:inherit;font-size:16px;font-weight:700;cursor:pointer;box-shadow:0 6px 0 #C97F38;transition:transform .12s cubic-bezier(.2,.7,.2,1)}
.btn-on:active{transform:translateY(4px)}
/* Stok kurdelesi (kullanıcı, 18 Eki: "C'yi yap"; eleştirmen 8/10): paket kartındaki "En avantajlı" kurdelesinin dili, butonun üst
   kenarına oturur, ayrı satır açmaz. Dokunmayı engellemez. Buton ekrana girince bir kez 8px aşağıdan gelir (yalnız transform/opacity). */
.al-on{position:relative;margin-top:24px}
.al-on .btn-on{margin-top:0}
.stok-kd{position:absolute;left:18px;top:-12px;z-index:1;display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 10px 0 8px;border-radius:999px;background:#1A2142;color:#FFFDF9;font-size:12px;font-weight:700;white-space:nowrap;pointer-events:none;opacity:0;transform:translateY(8px);transition:opacity .5s cubic-bezier(.2,.7,.2,1),transform .5s cubic-bezier(.2,.7,.2,1)}
.stok-kd.on{opacity:1;transform:none}
.stok-kd svg{width:14px;height:14px;flex:none}.stok-kd circle{fill:none;stroke:rgba(255,253,249,.7);stroke-width:1.6}.stok-kd path{fill:#F2A65A}
@media (prefers-reduced-motion:reduce){.stok-kd{opacity:1;transform:none;transition:none}}
.btn-kp{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;width:100%;min-height:56px;margin-top:14px;border:1.5px solid #1A2142;border-radius:20px;background:transparent;color:#1A2142;font:inherit;font-size:14px;font-weight:600;cursor:pointer}
.yol{position:relative;list-style:none;padding:0;margin:28px 0 0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr))}
.yol::before{content:"";position:absolute;left:16.6%;right:16.6%;top:14px;border-top:1.5px dashed #D6CAB6}
.yol li{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;gap:2px}
.yol .evre{position:relative;width:28px;height:28px;margin-bottom:6px;background:#F6F1E9;border-radius:50%}
.yol .evre circle{fill:#F6F1E9;stroke:#1A2142;stroke-width:1.4}
.yol .evre path{fill:#F2A65A;transform-origin:12px 12px}
/* Kargo takibi (kullanıcı: "verildiden başlasın, soft bir animasyonla çalışsın"; Tur 25: "animasyon çalışmıyor").
   Tek seferlik oynatma, tuvalde pano açılır açılmaz kimse bakmadan bitiyordu. Artık 8 sn'lik sakin döngü:
   "Bugün" hilali hep dolu → çizgi ve paket noktası Kargoda'ya akar → yarım ay → Kapında'ya akar → dolunay ve ışık halkası →
   bekler, söner, baştan. Ekrana girene kadar ilk karede durur. Yazılar hep okunur; yalnız transform/opacity. */
.yol li{z-index:1}
.yol-akis{position:absolute;left:16.6%;right:16.6%;top:13.25px;height:1.5px;z-index:0}
.yol-akis i{position:absolute;top:0;height:1.5px;width:50%;background:#F2A65A;transform-origin:0 50%}
.yol-akis i:nth-child(1){left:0}.yol-akis i:nth-child(2){left:50%}
/* Paket noktası: çizgi genişliğinde bir taşıyıcı; %50 = Kargoda, %100 = Kapında (ekran genişliğinden bağımsız) */
.yol-paket{position:absolute;left:0;top:0;width:100%;height:0}
.yol-paket::before{content:"";position:absolute;left:-5px;top:-4.25px;width:10px;height:10px;border-radius:50%;background:#1A2142;box-shadow:0 0 0 2px #F6F1E9,0 0 0 3.5px #F2A65A}
.yol li:nth-child(4) .evre::after{content:"";position:absolute;inset:0;border-radius:50%;box-shadow:0 0 0 2px rgba(242,166,90,.6);opacity:0}
@keyframes yk-cizgi1{0%,6%{transform:scaleX(0);opacity:1}26%{transform:scaleX(1);opacity:1}88%{transform:scaleX(1);opacity:1}97%,100%{transform:scaleX(1);opacity:0}}
@keyframes yk-cizgi2{0%,38%{transform:scaleX(0);opacity:1}57%{transform:scaleX(1);opacity:1}88%{transform:scaleX(1);opacity:1}97%,100%{transform:scaleX(1);opacity:0}}
@keyframes yk-paket{0%,4%{transform:none;opacity:0}6%{transform:none;opacity:1}26%{transform:translateX(50%)}38%{transform:translateX(50%)}57%{transform:translateX(100%);opacity:1}60%,100%{transform:translateX(100%);opacity:0}}
@keyframes yk-ay2{0%,26%{opacity:0;transform:scale(.4) rotate(-40deg)}33%{opacity:1;transform:none}88%{opacity:1;transform:none}97%,100%{opacity:0;transform:none}}
@keyframes yk-ay3{0%,57%{opacity:0;transform:scale(.4) rotate(-40deg)}64%{opacity:1;transform:none}88%{opacity:1;transform:none}97%,100%{opacity:0;transform:none}}
@keyframes yk-hale{0%,59%{opacity:0;transform:scale(.6)}66%{opacity:.9}80%,100%{opacity:0;transform:scale(1.7)}}
.yol-akis i,.yol-paket,.yol li:nth-child(3) .evre path,.yol li:nth-child(4) .evre path,.yol li:nth-child(4) .evre::after{animation-duration:8s;animation-timing-function:cubic-bezier(.2,.7,.2,1);animation-iteration-count:infinite;animation-fill-mode:both;animation-play-state:paused}
.yol-akis i:nth-child(1){animation-name:yk-cizgi1}.yol-akis i:nth-child(2){animation-name:yk-cizgi2}.yol-paket{animation-name:yk-paket}
.yol li:nth-child(3) .evre path{animation-name:yk-ay2}.yol li:nth-child(4) .evre path{animation-name:yk-ay3}.yol li:nth-child(4) .evre::after{animation-name:yk-hale}
.yol.on .yol-akis i,.yol.on .yol-paket,.yol.on li:nth-child(3) .evre path,.yol.on li:nth-child(4) .evre path,.yol.on li:nth-child(4) .evre::after{animation-play-state:running}
@media (prefers-reduced-motion:reduce){.yol-akis i,.yol .evre path,.yol li:nth-child(4) .evre::after{animation:none!important}.yol-paket{display:none}}
.yol b{font-size:14px;font-weight:700}
.yol>li>span{font-size:13px;color:#5C6078}
/* Teslim çizelgesi · Canlı kartlar dili (21 Eki, kullanıcı Sihirli'nin dilini buraya da istedi): beyaz kart, ton ekran (#F1E8DA)
   içinde hilal → yarım → dolunay; paket kutusu akar, Kapında'da kutu söner ve LunaDream lambası yanar. Tarihler ekranın altında. */
.teslim{position:relative;margin-top:22px;padding:8px 8px 12px;border-radius:20px;background:#FFFDF9;border:1px solid #E3D8C7}
.teslim::before{content:"";position:absolute;left:8px;right:8px;top:8px;height:64px;border-radius:14px;background:#F1E8DA}
.teslim .yol{margin:0;padding-top:18px}
.teslim .yol::before{top:32px}
.teslim .yol-akis{top:31.25px}
.teslim .yol .evre{margin-bottom:24px;background:#F1E8DA}
.teslim .yol .evre circle{fill:#F1E8DA}
.teslim .yol-paket::before{display:none}
/* Ürün soruları: teslim kartıyla aynı kart (krem, 1 px çizgi, 20 köşe); satır ≥ 54 px; hilal → dolunay, ok döner (yalnız opacity/transform) */
.urs{margin-top:10px;padding:2px 16px;border-radius:20px;background:#FFFDF9;border:1px solid #E3D8C7}
.urs-s+.urs-s{border-top:1px solid #EFE6D8}
.urs-s summary{list-style:none;display:flex;align-items:center;gap:12px;min-height:54px;padding:6px 0;font-size:15px;font-weight:600;line-height:1.3;color:#1A2142;cursor:pointer;-webkit-tap-highlight-color:transparent}
.urs-s summary::-webkit-details-marker{display:none}
.urs-s summary:focus-visible{outline:2px solid #F2A65A;outline-offset:2px;border-radius:8px}
.urs-ay{position:relative;flex:none;width:22px;height:22px}
.urs-ay .evre{position:absolute;inset:0;width:22px;height:22px;transition:opacity .35s cubic-bezier(.2,.7,.2,1)}
.urs-ay .evre circle{fill:#FFFDF9;stroke:#1A2142;stroke-width:1.4}
.urs-ay .evre path{fill:#F2A65A}
.urs-ay .dolu,.urs-s[open] .urs-ay .hilal{opacity:0}
.urs-s[open] .urs-ay .dolu{opacity:1}
.urs-q{flex:1;min-width:0}
.urs-ok{flex:none;width:18px;height:18px;fill:none;stroke:#5C6078;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;transition:transform .3s cubic-bezier(.2,.7,.2,1)}
.urs-s[open] .urs-ok{transform:rotate(180deg)}
.urs-s p{margin:0;padding:0 0 16px 34px;font-size:14px;line-height:1.55;color:#5C6078}
.yol-paket .kutu{position:absolute;left:-8px;top:-8px;width:16px;height:16px;fill:#FFFDF9;stroke:#1A2142;stroke-width:1.3;stroke-linejoin:round}
.yol-lamba{position:absolute;left:calc(50% + 17px);top:0;width:28px;height:28px;opacity:0;transform:translateY(4px)}
.yol-lamba .lmb{width:28px;height:28px}
.yol-lamba{animation:yk-lamba 8s cubic-bezier(.2,.7,.2,1) infinite both;animation-play-state:paused}
.yol.on .yol-lamba{animation-play-state:running}
@keyframes yk-lamba{0%,58%{opacity:0;transform:translateY(4px)}66%,88%{opacity:1;transform:none}97%,100%{opacity:0;transform:none}}
@media (prefers-reduced-motion:reduce){.yol-lamba{animation:none!important;opacity:1;transform:none}}
/* Fiyat düşüşü: 0–0,7 sn ₺1.999,00 büyük; 0,7 sn çizilir; 1,1 sn sağa kayıp küçülür ve söner, yerine soluk eski fiyat gelir;
   aynı anda indirimli fiyat 10px yukarıdan düşer; 1,6 sn rozet belirir. Yalnız transform/opacity, bir kez. */
.fiyat-satir{position:relative;display:flex;align-items:baseline;flex-wrap:wrap;gap:4px 10px;margin:8px 0 0;min-height:28px;font-variant-numeric:tabular-nums}
.fy-yeni{font-size:20px;font-weight:700;letter-spacing:-.01em}
.fy-eski{font-size:14px;color:#5C6078}
.fy-ilk{position:absolute;left:0;top:0;font-size:20px;font-weight:700;letter-spacing:-.01em;color:#1A2142;opacity:0;pointer-events:none;transform-origin:0 70%}
.fy-ilk::after{content:"";position:absolute;left:-2px;right:-2px;top:55%;height:2px;border-radius:1px;background:#1A2142;transform:scaleX(0);transform-origin:0 50%}
@keyframes fy-ilk{0%{opacity:1;transform:none}55%{opacity:1;transform:none}100%{opacity:0;transform:translateX(118px) scale(.7)}}
@keyframes fy-cizgi{0%,30%{transform:scaleX(0)}55%,100%{transform:scaleX(1)}}
@keyframes fy-dus{0%,55%{opacity:0;transform:translateY(-12px)}100%{opacity:1;transform:none}}
@keyframes fy-gel{0%,60%{opacity:0}100%{opacity:1}}
@keyframes fy-rozet{0%,75%{opacity:0;transform:scale(.8)}100%{opacity:1;transform:none}}
.fy-ilk{animation:fy-ilk 1.6s cubic-bezier(.2,.7,.2,1) .3s both}
.fy-ilk::after{animation:fy-cizgi 1.6s cubic-bezier(.2,.7,.2,1) .3s both}
.fy-yeni{animation:fy-dus 1.6s cubic-bezier(.2,.7,.2,1) .3s both}
.fy-eski{animation:fy-gel 1.6s cubic-bezier(.2,.7,.2,1) .3s both}
.fy-rozet{animation:fy-rozet 2s cubic-bezier(.2,.7,.2,1) .3s both}
@media (prefers-reduced-motion:reduce){.fy-ilk,.fy-ilk::after,.fy-yeni,.fy-eski,.fy-rozet{animation:none}.fy-ilk{opacity:0}}
/* Bölümler */
.bolum{padding-top:36px}
.ust-yazi{margin:0 0 6px;font-size:13px;font-weight:700;color:#A05A1C}
.gece{background:#1A2142;color:#EDE5D8;padding:32px 0 34px;margin-top:36px;border-radius:28px}
/* Odası böyle görünecek · Gece vitrini (21 Eki): "Bir gece, beş an" ve iki posterli eski Odası'nın yerine (kullanıcı: "profesyonel bir
   görüntü istiyorum"; eleştirmen dört yönden bunu seçti, 8/10). Diskler paneliyle aynı lacivert ve köşe. Kart 280×372 (3:4), yanlarda 55 px pay.
   Ortaya gelen kart büyür ve aydınlanır (destekleyen tarayıcıda kaydırmayla sürekli, yoksa sınıf geçişi); yazı altta 280 ms'de değişir;
   aylar dolarak ilerler. Çip fotoğrafa (tavana) binmez, sayaç yok. Yalnız transform/opacity. */
.vitrin{margin-top:36px;padding:30px 0 20px;border-radius:28px;background:#1A2142;color:#FFFDF9}
.vitrin>.h2{padding:0 20px;color:#FFFDF9}
.vt-serit{position:relative;display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;padding:22px 55px 0}
.vt-kart{position:relative;flex:0 0 280px;height:372px;border-radius:20px;overflow:hidden;background:#0C1027;scroll-snap-align:center;scroll-snap-stop:always;cursor:pointer;transform:scale(.92);opacity:.6;transition:transform .5s cubic-bezier(.2,.7,.2,1),opacity .5s cubic-bezier(.2,.7,.2,1)}
.vt-kart.on{transform:none;opacity:1;cursor:default}
.vt-kart img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.vt-kart::after{content:"";position:absolute;inset:0;border-radius:20px;box-shadow:inset 0 0 0 1px rgba(255,253,249,.12);pointer-events:none}
@supports (animation-timeline: view()){
  .vt-kart,.vt-kart.on{transition:none;animation:vt-odak linear both;animation-timeline:view(inline)}
  @keyframes vt-odak{0%{transform:scale(.92);opacity:.6}50%{transform:none;opacity:1}100%{transform:scale(.92);opacity:.6}}
}
.vt-metin{display:grid;padding:18px 24px 0;text-align:center}
.vt-m{grid-area:1/1;display:flex;flex-direction:column;align-items:center;opacity:0;transform:translateY(6px);pointer-events:none;transition:opacity .28s cubic-bezier(.2,.7,.2,1),transform .28s cubic-bezier(.2,.7,.2,1)}
.vt-m.on{opacity:1;transform:none;pointer-events:auto}
.vt-etk{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:600;color:#B9BED6}
.vt-etk .evre{width:14px;height:14px}
.vt-etk .evre circle{fill:none;stroke:#B9BED6;stroke-width:1.6}.vt-etk .evre path{fill:#F2A65A}
.vt-bas{margin:6px 0 0;font-family:"Young Serif",Georgia,serif;font-size:22px;line-height:1.12;letter-spacing:-.01em}
.vt-bas span{color:#F2A65A}
.vt-yazi{margin:6px 0 0;max-width:300px;font-size:15px;line-height:1.45;color:#B9BED6;text-wrap:balance}
.vt-sec{display:inline-flex;align-items:center;gap:6px;min-height:48px;margin-top:2px;padding:0 4px;border:0;background:none;color:#F2A65A;font:inherit;font-size:14px;font-weight:700;cursor:pointer}
.vt-aylar{position:relative;display:flex;justify-content:center;gap:28px;margin-top:6px}
.vt-aylar::before{content:"";position:absolute;left:50%;top:50%;width:204px;height:1px;margin-left:-102px;background:rgba(255,253,249,.18)}
.vt-ay{position:relative;display:grid;place-items:center;width:48px;height:48px;padding:0;border:0;border-radius:50%;background:#1A2142;cursor:pointer}
.vt-ay .evre{width:22px;height:22px;transition:transform .4s cubic-bezier(.2,.7,.2,1)}
.vt-ay .evre circle{fill:none;stroke:rgba(255,253,249,.5);stroke-width:1.6}
.vt-ay .evre path{fill:rgba(255,253,249,.28)}
.vt-ay.on .evre{transform:scale(1.18)}
.vt-ay.on .evre circle{stroke:#F2A65A}.vt-ay.on .evre path{fill:#F2A65A}
.vitrin :focus-visible{outline:2px solid #F2A65A;outline-offset:2px}
.ok-ik{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.temsil{margin:10px 16px 0;font-size:12px;color:#5C6078}
.cip{display:inline-flex;align-items:center;min-height:48px;padding:0 18px;border-radius:999px;border:1.5px solid #1A2142;background:transparent;color:#1A2142;font:inherit;font-size:14px;font-weight:600;cursor:pointer;white-space:nowrap}
.cip.on{background:#1A2142;color:#FFFDF9}
.tavan{position:relative;height:280px;overflow:hidden;background:radial-gradient(70% 70% at 50% 45%,#232B55 0%,rgba(26,33,66,0) 100%)}
.yansima{mix-blend-mode:screen;position:absolute;left:50%;top:42%;width:230px;height:230px;margin:-115px 0 0 -115px;border-radius:50%;overflow:hidden;opacity:0;transform:scale(.92);transition:opacity .6s cubic-bezier(.2,.7,.2,1),transform .6s cubic-bezier(.2,.7,.2,1);-webkit-mask-image:radial-gradient(closest-side,#000 62%,transparent 100%);mask-image:radial-gradient(closest-side,#000 62%,transparent 100%)}
.yansima.on{opacity:.92;transform:none}
.yansima img{width:100%;height:100%;object-fit:cover;display:block}
.dbtn{display:flex;flex-direction:column;align-items:center;gap:6px;background:transparent;border:0;padding:0;cursor:pointer;color:#B9BED6;font:inherit;font-size:12px;width:64px;min-height:60px;flex:none}
.dbtn img{width:54px;height:54px;border-radius:50%;object-fit:cover;outline:2px solid transparent;outline-offset:3px;transition:transform .25s cubic-bezier(.2,.7,.2,1)}
.dbtn.on{color:#FFFDF9;font-weight:600}
.dbtn.on img{outline-color:#F2A65A;transform:translateY(-4px)}
.otuz{display:grid;grid-template-columns:104px minmax(0,1fr);gap:16px;align-items:center;padding:4px 0;color:#1A2142}
/* Ay evreli mühür (kullanıcı: "yarım ay, tam ay olma efektini kullanmaya devam et"): teslim çizgisiyle aynı ay dili */
.muhur-kap{position:relative;width:104px;height:104px}
.muhur{position:absolute;left:0;top:0;width:104px;height:104px}
.muhur .mh-halka{fill:none;stroke:#E3D8C7;stroke-width:1.5}
.muhur g circle{fill:#F6F1E9;stroke:#1A2142;stroke-width:2.6}
.muhur g path{fill:#F2A65A}
.muhur-say{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1}
.otuz b.say{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:32px;line-height:1;letter-spacing:-.03em;color:#1A2142}
.muhur-say span{margin-top:2px;font-size:12px;font-weight:700;color:#1A2142}
.sss{border-bottom:1.5px solid #E3D8C7}
.sss summary{list-style:none;display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:60px;font-weight:700;font-size:15px;cursor:pointer}
.sss summary::-webkit-details-marker{display:none}
.sss .arti{width:32px;height:32px;border-radius:50%;border:1.5px solid #1A2142;color:#1A2142;font-weight:400;font-size:18px;display:grid;place-items:center;flex:none;transition:transform .2s}
.sss[open] .arti{transform:rotate(45deg)}
.kart{flex:0 0 168px;scroll-snap-align:start;background:#FFFDF9;border-radius:20px;border:1.5px solid #E3D8C7;overflow:hidden;display:flex;flex-direction:column;text-decoration:none;color:#1A2142}
.alt-bilgi{background:#1A2142;color:#B9BED6;margin-top:36px;padding:32px 0 100px;border-radius:28px 28px 0 0}
.alt-bilgi a{color:#FFFDF9;text-decoration:none;display:flex;align-items:center;min-height:48px}
.yapis{position:sticky;bottom:0;z-index:5;margin-top:-76px;height:76px;padding:0 12px;background:#1A2142;display:flex;align-items:center;gap:10px;border-radius:20px 20px 0 0}
/* Baskı unsurları (Tur 9, kullanıcı: "baskılayıcıları arttıralım"): yalnız gerçek veriyle, veri yoksa gizlenir.
   Sayaç: kampanya bitiş tarihi (tema ayarı). Stok: Shopify envanteri eşik altındaysa. Dün: Shopify Flow'un yazdığı metafield. */
.canli{list-style:none;margin:14px 0 0;padding:0;display:flex;flex-direction:column;gap:6px;font-size:14px;color:#1A2142}
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
.vid-alt b{font-size:14px}
.vid-alt span{font-size:13px;color:#B9BED6}
.vid-etiket{position:absolute;left:10px;top:10px;z-index:1;font-size:12px;font-weight:600;padding:2px 8px;border-radius:999px;background:rgba(12,16,39,.6)}
/* Müşteri kanıtı tek bölüm (kullanıcı, 19 Eki: "yorum kısımlarının hepsi karmaşık, bir düzen oturtalım"; B · Tek akış seçildi) */
.ynot{margin:12px 0 0;font-size:13px;color:#5C6078;text-align:center;line-height:1.45}
.yhep{display:flex;justify-content:center;width:100%;margin-top:16px;text-decoration:none}
.yr{margin:0;padding:16px 0;border-bottom:1px solid #E3D8C7;display:flex;flex-direction:column;gap:10px}
.yr q{font-family:"Young Serif",Georgia,serif;font-size:17px;line-height:1.32;quotes:none;color:#1A2142}
.yr figcaption{display:flex;align-items:center;justify-content:space-between;gap:8px;font-size:13px}
.yr .dog,.yone .dog{display:inline-flex;align-items:center;gap:4px;font-weight:600;color:#2E6B4F}
.yl{margin-top:4px}
.yone{margin:20px 16px 0;padding:18px;border-radius:20px;background:#FFFDF9}
.yone .tirnak{display:block;height:20px;font-family:"Young Serif",Georgia,serif;font-size:36px;line-height:.7;color:#1A2142;opacity:.35}
.yone q{display:block;margin-top:4px;font-family:"Young Serif",Georgia,serif;font-size:21px;line-height:1.28;quotes:none;color:#1A2142}
.yone figcaption{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-top:14px;font-size:13px}
.yara{display:flex;align-items:baseline;justify-content:space-between;margin:24px 0 0;font-size:15px;font-weight:700;color:#1A2142}
.yara span{font-size:13px;font-weight:500;color:#5C6078}
.karma{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:16px;padding:12px 16px 2px;scrollbar-width:none}
.karma::-webkit-scrollbar{display:none}
.karma button{flex:none;display:block;padding:0;border:1px solid #E3D8C7;border-radius:18px;overflow:hidden;background:#FFFDF9;scroll-snap-align:start;cursor:pointer}
.karma button{height:320px}
.karma.kucuk button{height:200px}
.k-msj{aspect-ratio:9/16}.k-foto{aspect-ratio:3/4}
.karma img{display:block;width:100%;height:100%;object-fit:cover;object-position:50% 0}
/* Müşteri fotoğrafları (19 Eki): küçük kare yerine dikey kart, dokununca büyür */
.mf{flex:none;width:150px;aspect-ratio:3/4;padding:0;border:0;border-radius:18px;overflow:hidden;background:#F1E8DA;cursor:pointer}
.mf img{display:block;width:100%;height:100%;object-fit:cover;object-position:50% 0}
.mf:active,.karma button:active{transform:scale(.98)}
.buyuk{position:fixed;inset:0;z-index:1000;display:grid;place-items:center;padding:56px 16px 24px;background:rgba(12,16,39,.92)}
/* Büyük görünüm üst menünün (900) ve satın alma çubuğunun üstünde; görsel ekran boyunu aşmaz (23 Eki, masaüstü denetimi) */
.buyuk img{width:auto;max-width:100%;max-height:calc(100vh - 80px);max-height:calc(100dvh - 80px);border-radius:16px;object-fit:contain}
.buyuk-x{position:absolute;top:10px;right:10px;width:48px;height:48px;padding:0;border:0;border-radius:50%;background:rgba(255,253,249,.14);display:grid;place-items:center;cursor:pointer}
.buyuk-x svg{width:22px;height:22px;fill:none;stroke:#FFFDF9;stroke-width:2;stroke-linecap:round}
.noscroll{scrollbar-width:none}.noscroll::-webkit-scrollbar{display:none}"""

# Dün satış (kullanıcı, 18 Eki): gerçek sayı elle girilir. Canlıda bölüm ayarı (sayı; boşsa satır gizlenir) ya da Shopify Flow'un
# her gece yazdığı metafield. Uydurma sayı yazılmaz; önizlemede yer tutucu.
DUN = '62'  # kullanıcı, 18 Eki; 23 Eki sadeleştirmede gizlenmişti, kullanıcı geri istedi
# Stok (kullanıcı, 18 Eki: "stoklar elle girilecek"): kurdelede "Son N adet". Boşsa kurdele yok.
STOK = '18'
# Azalan ay: hediye satırındaki hilalin aynası (ışık solda), "azalıyor" der; oranlı çubuk yerine.
AZALAN = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path transform="matrix(-1 0 0 1 24 0)" d="%s"></path></svg>' % ay(.15)
STOK_KURDELE = '<div class="al-on"><span class="{{stokCls}}">' + AZALAN + 'Son %s adet</span>' % STOK
DUN_SATIR = ('    <p class="dun"><i aria-hidden="true"></i><span>Dün <b>%s</b> kişi satın aldı</span></p>\n' % DUN) if DUN else ''
# Galeri · premium fotoğraf seti (22 Eki; kullanıcı ChatGPT'de üretti, istemler ogrenme/chatgpt-istemleri-lunadream.txt).
# Galeri = satış afişleri, 2. tur (23 Eki; kullanıcı: "satış odaklı değil, yorum görseli yapılmamış, çok sönük"). araclar/gorsel/afis_uret.py:
# açılış (Kız, gece, tavanda yansıma) · yorum (Loox'taki gerçek alıcılar) · diskler · Erkek (Uzay Kaşifi, etiketli) · kutudan ne çıkıyor + güven şeridi.
P_GAL = [{'id': '756460fee1769304a455ca478fcee1af', 'n': 'LunaDream Kız gece odasında yanıyor, tavanda ay ve yıldızlar: tavanı masala çeviren lamba'},
         {'id': '447d1a0fd314f411baa1860180e51105', 'n': 'Alıcı yorumları: Abdülkerim T., Mehmet C. ve Handan B.'},
         {'id': '992615e38254c615df3e40a553e54032', 'n': 'Her gece başka bir masal: LunaDream ve 6 masal diski'},
         {'id': '3c0683cd0453bc9c12a7d20eae71116b', 'n': 'LunaDream Erkek modeli Uzay Kaşifi gece odasında, duvarda yıldızlar'},
         {'id': '1bf394a66814e821fa3313725f076f0c', 'n': 'Kutudan ne çıkıyor: lamba, 6 masal diski, 6 hediye disk ve USB şarj kablosu; ücretsiz kargo, 30 gün iade, kartla %5 indirim'}]
AD_LD = {'211acb76d908e8ed6d4f5fcddc987893': 'Masalsı gece ışığı', '652e1893a0ae33a24ee0e3d53edab757': 'Müşteri paylaşımı: çocuk odasında LunaDream', 'a08890007843d79d94bfffc397a3d0ac': 'Gece modu', 'd4efe7e83c74524ece75e962161f7fff': 'Deniz altı', '3ddd8b8b95f040d436d5d0ea350924b8': 'Hediyeye hazır', '98db755893dbcebe192c69e73ae5afff': 'Uzay macerası'}
STAR = '<span class="yildiz" aria-hidden="true">★★★★★<i style="width: {{starPct}}%">★★★★★</i></span>'
def isaret(boy, cizgi='rgba(255,253,249,.55)'):
    # Marka işareti: ay evresi çizimi (ince daire + amber hilal); teslim çizgisi ve mühürle aynı çizim
    return '<svg class="isaret" width="%d" height="%d" viewBox="0 0 24 24" aria-hidden="true" style="flex: none"><circle cx="12" cy="12" r="9" fill="none" stroke="%s" stroke-width="1.4"></circle><path d="%s" fill="#F2A65A"></path></svg>' % (boy, boy, cizgi, ay(.22))


LOGO = isaret(22)

# Müşteri kanıtı tek bölüm (19 Eki, B · Tek akış)
YORUM_HTML = ("""  <!-- Müşteri kanıtı tek bölümde (kullanıcı, 19 Eki: "yorum kısımlarının hepsi karmaşık, bir düzen oturtalım"). Üç yön gösterildi (A sekmeli, B tek akış, C duvar); eleştirmen B 8/10, kullanıcı B'yi seçti:
       puan → mesajlar şeridi → öne çıkan tek yorum → fotoğraf şeridi → kısa yorum listesi → hepsini oku (mesajlar karışık şeritte kaybolduğu için ayrıldı).
       Konu çipleri ve ayrı "Sizden gelen mesajlar" bölümü kalktı. -->
  <section id="yorumlar" class="bolum gir yorum-b">
    <div class="px" style="display: flex; align-items: flex-end; justify-content: space-between; gap: 12px"><h2 class="h2">Aileler<br>ne diyor<span class="n">?</span></h2><span style="display: flex; flex-direction: column; align-items: flex-end; line-height: 1"><b class="ser" style="font-size: 32px; font-weight: 400">{{rating}}</b><span style="margin-top: 6px">""" + STAR + """</span><span style="font-size: 13px; color: #5C6078; margin-top: 4px">{{reviews}} yorum</span></span></div>
    <!-- Kullanıcı (19 Eki): "WP mesajları falan gidiyor" → mesajlar karışık şeritte kayboluyordu; bölümün başında kendi başlıklı şeridi,
         fotoğraflar ayrı ve küçük şeritte -->
    <p class="px yara">Sizden gelen mesajlar<span class="dokun">Dokun, büyüsün</span>""" + serit_ok('mesajlar') + """</p>
    <div class="noscroll karma"><sc-for list="{{mesajlar}}" as="m" hint-placeholder-count="3"><button class="k-msj" type="button" onClick="{{m.ac}}" aria-label="{{m.n}}, büyüt"><img src="{{m.src}}" alt="{{m.n}}" loading="lazy"></button></sc-for><span aria-hidden="true" style="flex: 0 0 6px"></span></div>
    <figure class="px yone"><span class="tirnak" aria-hidden="true">“</span><q>{{oneQ.q}}</q><figcaption><b>{{oneQ.name}}</b><span class="dog">{{tik}}Satın aldı</span></figcaption></figure>
    <p class="px yara">Evlerinizden<span>Müşteri fotoğrafları</span>""" + serit_ok('fotoğraflar') + """</p>
    <div class="noscroll karma kucuk"><sc-for list="{{fsira}}" as="f" hint-placeholder-count="4"><button class="k-foto" type="button" onClick="{{f.ac}}" aria-label="{{f.alt}}, büyüt"><img src="{{f.src}}" alt="{{f.alt}}" loading="lazy"></button></sc-for><span aria-hidden="true" style="flex: 0 0 6px"></span></div>
    <div class="px yl"><sc-for list="{{revRest}}" as="r" hint-placeholder-count="3"><figure class="yr"><q>{{r.q}}</q><figcaption><b>{{r.name}}</b><span class="dog">{{tik}}Satın aldı</span></figcaption></figure></sc-for><a href="#" class="cip yhep">{{reviews}} yorumun hepsini oku</a><p class="ynot">Yorumlar yalnız sipariş verenlerden; hepsi yayımlanır. Mesajlar izinle paylaşıldı.</p></div>
  </section>

""").replace('{{tik}}', '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg>')

HTML = """<div class="pg" style="padding-bottom: 0">
  <!-- Üst şerit: bugüne özel fiyat, her gece 23:59'da (İstanbul) sıfırlanır. Kullanıcı kararı: toptancı zammı her an gelebildiği için gerçek; gün içinde zam gelse de o günün fiyatı 23:59'a kadar korunur. -->
  <div class="duyuru" role="timer" aria-label="{{cdAria}}"><span>Bugünkü fiyat garantisi</span><svg class="sayac-ay" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="{{cdAy}}"></path></svg><b>{{cdShort}}</b></div>
  <!-- Sahne: oda sahneleri logo bandının altına kadar uzanır (tek parça); yazılı afişler bandın altından başlar (çift logo/yazı çakışması olmasın) -->
  <section class="sahne" aria-label="LunaDream fotoğrafları">
    <header><button class="ikon" aria-label="Menü"><svg class="ico" viewBox="0 0 24 24"><path d="M4 8h16M4 16h11"></path></svg></button><span style="display: flex; align-items: center; gap: 6px">""" + LOGO + """<span class="ser" style="font-size: 18px">Ayluna</span></span><button class="ikon" aria-label="Sepet"><svg class="ico" viewBox="0 0 24 24"><path d="M6 8h12l-1 12H7z"></path><path d="M9 8a3 3 0 0 1 6 0"></path></svg></button></header>
    <div class="kare-foto" onScroll="{{gKay}}"><sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><div class="kf"><img src="{{f.src}}" alt="{{f.n}}" style="object-position: {{f.pos}}"></div></sc-for></div>""" + GAL_OK + """
    <!-- Kaydırılır galeri, 5 sn'de kendiliğinden geçer (elle kaydırınca durur). Küçük resim yok; fotoğrafın en altında ince çizgiler, geçtikçe beyazlar. -->
    <div class="seritler">
      <span class="ay-iz" aria-hidden="true"><sc-for list="{{gal}}" as="f" hint-placeholder-count="9"><i class="{{f.acls}}"></i></sc-for></span>
      <span style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap" aria-live="polite">Fotoğraf {{gNo}} / {{gCount}}</span>
    </div>
  </section>

  <section class="px levha" id="siparis">
    <!-- Ad ve puan aynı satırda (kullanıcı, Tur 25: "yorum kısmı ürün ismi yanında olsun"). Puan ve sayı canlıda Loox'tan;
         veri yoksa puan gizlenir, ad tek başına kalır. Dokununca yorumlara iner. -->
    <div class="ad-satir">
      <h1 class="dev">LunaDream<span>.</span></h1>
      <a class="puan" href="#yorumlar" aria-label="5 üzerinden {{rating}} puan, {{reviews}} yorum"><span class="puan-ust">""" + STAR + """<b>{{rating}}</b></span><span class="puan-alt">{{reviews}} yorum</span></a>
    </div>
    <!-- Fiyat (kullanıcı: "girince 1999 yazsın, hafif bir animasyonla indirimli fiyata düşsün"): bir kez oynar. Canlıda sayfa açılınca. -->
    <p class="fiyat-satir" aria-label="{{p1}}, önceki fiyat {{c1}}, %{{pct}} indirim"><span class="fy-ilk" aria-hidden="true">{{c1}}</span><b class="fy-yeni" aria-hidden="true">{{p1}}</b><s class="fy-eski" aria-hidden="true">{{c1}}</s><span class="indirim fy-rozet" aria-hidden="true">%{{pct}} indirim</span></p>
""" + DUN_SATIR + """

    <!-- Sihirli Özellikler: fiyatın hemen altında; model seçimi bunun altında (Tur 9, kullanıcı isteği). Canlı kartlar (21 Eki): her kartta küçük ekran ve sekans -->
    <p class="ust-yazi" style="margin-top: 22px; margin-bottom: 0">Sihirli özellikler</p>
    <div class="sih">""" + ''.join(S2.kart_a(k) for k in S2.OZ) + """
    </div>

    <!-- Seçiciler (Tur 25, kullanıcı "Satır kartlar"ı seçti): model yan yana iki yarım kart, paket alt alta satır kart,
         2 Adet açılınca kartın içinde 2. lamba. 1. lamba = model. Canlıda 2 Adet sepete iki ayrı varyant olarak eklenir. -->
    <div class="etiket" id="modeller" style="margin-top: 24px"><span>{{modelEtiket}}</span></div>
    <div class="yarim-iz">
      <sc-for list="{{models}}" as="m" hint-placeholder-count="2">
        <button class="{{m.cls}}" onClick="{{m.pick}}" aria-pressed="{{m.on}}"><span class="sat yarim"><span class="tl"><img src="{{m.src}}" alt=""></span><span class="sat-orta"><span class="ad">{{m.n}}</span><span class="alt">{{m.sub}}</span></span><svg class="ayr" viewBox="0 0 24 24" aria-hidden="true"><circle class="h" cx="12" cy="12" r="9"></circle><circle class="d" cx="12" cy="12" r="5"></circle></svg></span></button>
      </sc-for>
    </div>

    <div class="etiket" style="margin-top: 24px"><span>Paket</span><span style="font-weight: 600">Kampanya · 1–31 Ekim</span></div>
    <div class="pk-liste">
      <sc-for list="{{paket}}" as="b" hint-placeholder-count="2">
        <div class="{{b.cls}}">
          <sc-if value="{{b.rib}}" hint-placeholder-val="{{false}}"><span class="kurdele">En avantajlı</span></sc-if>
          <button class="sat" onClick="{{b.pick}}" aria-pressed="{{b.on}}"><span class="{{b.tlCls}}"><img src="{{b.src1}}" alt=""><sc-if value="{{b.two}}" hint-placeholder-val="{{false}}"><img src="{{b.src2}}" alt=""></sc-if></span><span class="sat-orta"><span class="ad">{{b.t}}</span><span class="alt">{{b.sub}}</span></span><span class="sat-sag"><span class="fiyat">{{b.p}}</span><span class="eski"><sc-if value="{{b.hasOld}}" hint-placeholder-val="{{true}}"><s>{{b.old}}</s></sc-if>{{b.unit}}</span></span><svg class="ayr" viewBox="0 0 24 24" aria-hidden="true"><circle class="h" cx="12" cy="12" r="9"></circle><circle class="d" cx="12" cy="12" r="5"></circle></svg></button>
          <sc-if value="{{b.ac}}" hint-placeholder-val="{{false}}"><div class="ek" role="group" aria-label="2. lambanın modeli"><span class="ek-ad">2. lamba</span><span class="cipler"><sc-for list="{{ikinci}}" as="c" hint-placeholder-count="2"><button class="{{c.cls}}" onClick="{{c.pick}}" aria-pressed="{{c.on}}"><span class="cip-y"><img src="{{c.src}}" alt=""></span>{{c.n}}<svg class="ayr" viewBox="0 0 24 24" aria-hidden="true"><circle class="h" cx="12" cy="12" r="9"></circle><circle class="d" cx="12" cy="12" r="5"></circle></svg></button></sc-for></span></div></sc-if>
        </div>
      </sc-for>
    </div>
    <!-- Dönen satır (23 Eki: sadeleştirme geri alındı, kullanıcı: "yaptığımız sadeleştirmeleri geri getir"; ilk hâli 18 Eki: "ilk hali öyle başlasın, sonra bugün 16'ya kadar verilen siparişler aynı gün kargoda, orada bir sayaç dönsün").
         Hediye 4 sn, kargo 6 sn. Simge yoldaki gibi: hilal hediye, yarım ay kargoda. Ekran okuyucu ikisini düz metin okur, sayacı saniye saniye okumaz.
         16.00'dan sonra ve hafta sonu sayaç yok: "Bugün verilen siparişler yarın / Pazartesi kargoda". -->
    <p class="donen"><span class="dn-sr">Her kutuda 6 masal diski. {{kgMetin}}.</span><span class="{{dnA}}" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d='""" + ay(.22) + """'></path></svg>Her kutuda 6 masal diski</span><span class="{{dnB}}" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d='""" + ay(.5) + """'></path></svg><span class="dn-m">{{kgMetin}}</span><sc-if value="{{kgBugun}}" hint-placeholder-val="{{true}}"><b class="dn-sy">{{kgSayac}}</b></sc-if></span></p>
    <!-- Stok kurdelesi (kullanıcı, 18 Eki: stok denemelerinden C seçildi): Güvenli Ödeme butonunun üst kenarında. Sayı elle
         (tema ayarı: sayı + aç/kapa; Shopify stoğuna bağlı değil), boşsa kurdele yok ve buton eski yerine döner. -->
    """ + (STOK_KURDELE if STOK else '') + """<button class="btn-on" type="button">{{onLabel}}</button>""" + ('</div>' if STOK else '') + """
    <!-- Canlıda kapıda ödeme uygulamasının formunu açar. Butonda fiyat yok (kullanıcı, Tur 25); ₺80 ücret ve toplam,
         sipariş onaylanmadan önce formun özetinde yazar (mevzuat: ek ücret sözleşmeden önce bildirilir). SSS'de de var. -->
    <button class="btn-kp" type="button">Kapıda Ödeme ile Sipariş Ver</button>
    <!-- Shopify: Kapıda düğmesi yok, kapıda ödemeyi kullanıcı EasySell ile koyar; düğmesi bu yuvaya gelir -->
    <div class="ay-dis" data-ay-dis></div>
    <div class="teslim"><ol class="{{yolCls}}" aria-label="Siparişten teslime"><span class="yol-akis" aria-hidden="true"><i></i><i></i><span class="yol-paket">""" + KUTU + """</span></span>""" + YOL + """</ol></div>
    <!-- Ürün soruları (22 Eki, kullanıcı: mağazadaki açılır soruları "kargo takibin altına ekle, o kısma mükemmel otursun").
         Teslim kartıyla aynı kart; soru kapalıyken hilal, açılınca dolunay (teslim çizgisinin ay dili). Yalnız 4 temel soru (kullanıcı: "o kadar çok soru olmasın"); diğerleri alttaki SSS'de.
         Cevaplar canlı sayfadaki LunaDream cevaplarından, yalnız teyitli olanlar: hareket sensörü yok (mağaza "hareket sensörlü değildir"
         diyor; altındaki sensör cevabı AyFeneri'nden kopya), pil süresi yazılmaz (canlıda da boş), sağlık iddiası yok. -->
    <div class="urs" role="group" aria-label="Ürün hakkında sorular">
      <sc-for list="{{urs}}" as="u" hint-placeholder-count="4"><details class="urs-s"><summary><span class="urs-ay" aria-hidden="true">""" + URS_AY + """</span><span class="urs-q">{{u.q}}</span>""" + URS_OK + """</summary><p>{{u.a}}</p></details></sc-for>
    </div>
  </section>

  <!-- Videolar: gerçek ürün videoları; kalır (kullanıcı, 23 Eki: "gerçek ürün videoları olan kısım gitmiş oldu ama"; sadeleştirmede yanlışlıkla kaldırılmıştı).
       Canlıda bloklar = Shopify videoları (kapak = videonun kendi ilk karesi). Video yoksa bölüm hiç görünmez. Ekrandayken sessiz döner; dokununca sesli, tam ekran. -->
  <section class="bolum gir" id="videolar">
    <div class="px"><h2 class="h2">Işık kapanınca<br>ne oluyor<span class="n">?</span></h2></div>
    <div class="noscroll" style="display: flex; gap: 10px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-left: 16px; padding: 16px 16px 0">
      <sc-for list="{{vids}}" as="v" hint-placeholder-count="4"><button class="vid" type="button" aria-label="{{v.t}}: videoyu oynat"><img src="{{v.src}}" alt="" style="object-position: {{v.pos}}"><span class="vid-etiket">[video]</span><span class="vid-oyna" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l11-6.5z"></path></svg></span><span class="vid-alt"><b>{{v.t}}</b><span>{{v.k}}</span></span></button></sc-for>
      <span aria-hidden="true" style="flex: 0 0 6px"></span>
    </div>
  </section>

  <!-- Neler yapabiliyor? · Dergi kapağı (22 Eki, 4. tur; kullanıcı seçti). Afiş (3. tur) Sihirli'nin dört beyaz kartını aynı dille tekrar
       ediyordu ("yine sıkıcı"). Dev tek kelime (Tak. Çal. Kıs. Şarj.), parçalı lamba kesimi önünde ve kendisi oynar: kubbe (Erkek'te robotun başı)
       açılır, disk üstten girer; notalar; Parlak/Orta/Kısık; şarjda ışık alttan dolar. Her kelimede zemin perdesi alttan yükselir.
       Ekrana girince bir tur oynar ve "Tak."ta durur; alttaki sözcüklere ya da lambaya dokununca o gösterilir. Kod ve CSS ozellik4_varyant.py'de. -->
  <section class="px bolum gir" id="neler" aria-labelledby="neler-bas">
    <h2 class="h2" id="neler-bas">Neler<br>yapabiliyor<span class="n">?</span></h2>
    """ + OZ4.dergi() + """
  </section>

  <!-- Odası böyle görünecek · Gece vitrini (21 Eki; "Bir gece, beş an" ve iki posterli eski Odası'nın yerine). Kaydır, karta ya da aya dokun.
       Görseller yer tutucu: çocuk, lamba ve tavandaki ışık aynı karede olan Flow kareleri gelecek (ogrenme/flow-istemleri-lunadream-oda.md).
       Marka görseli; "müşteri" etiketi konmaz. Yazı HTML; fotoğrafa gömülmez. -->
  <section class="vitrin gir" id="odalar" aria-labelledby="oda-bas">
    <h2 class="h2" id="oda-bas">Odası böyle<br>görünecek<span class="n">.</span></h2>
    <div class="vt-serit noscroll" onScroll="{{odaKay}}">
      <sc-for list="{{odalar}}" as="o" hint-placeholder-count="4"><div class="{{o.cls}}" aria-hidden="{{o.gizli}}" onClick="{{o.git}}"><img src="{{o.src}}" alt="{{o.alt}}" loading="lazy" style="object-position: {{o.pos}}"></div></sc-for>
    </div>
    <div class="vt-metin" aria-live="polite"><sc-for list="{{odalar}}" as="o" hint-placeholder-count="4"><div class="{{o.mcls}}" aria-hidden="{{o.gizli}}"><span class="vt-etk"><svg class="evre" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="{{o.ev}}"></path></svg>{{o.cip}}</span><p class="vt-bas">{{o.bas}}<span>.</span></p><p class="vt-yazi">{{o.yazi}}</p><button class="vt-sec" type="button" tabindex="{{o.tab}}" onClick="{{o.eylem}}">{{o.sec}}<svg class="ok-ik" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"></path></svg></button></div></sc-for></div>
    <div class="vt-aylar" role="group" aria-label="Odalar"><sc-for list="{{odalar}}" as="o" hint-placeholder-count="4"><button class="{{o.ayCls}}" type="button" onClick="{{o.git}}" aria-label="{{o.lbl}}" aria-pressed="{{o.basili}}"><svg class="evre" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="{{o.ev}}"></path></svg></button></sc-for></div>
  </section>

  <!-- Puan ve sayı Loox'tan; yorumlar Loox'taki gerçek yorumlardan birebir. "Satın aldı" yalnız Loox'un doğruladığı yorumda. Fotoğraflar Loox foto yorumlarından ve müşteri hikâyesinden. -->
""" + YORUM_HTML + """  <!-- Büyük görünüm: müşteri fotoğrafı ya da mesaj; dokununca ya da Esc ile kapanır -->
  <sc-if value="{{buyukVar}}" hint-placeholder-val="{{false}}"><div class="buyuk" role="dialog" aria-modal="true" aria-label="{{buyukAd}}" onClick="{{buyukKapat}}"><img src="{{buyuk}}" alt="{{buyukAd}}"><button class="buyuk-x" type="button" aria-label="Kapat"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg></button></div></sc-if>

  <!-- Diskler: tavana yansıt -->
  <section class="gece gir" id="diskler">
    <div class="px"><h2 class="h2" style="color: #FFFDF9">Bu gece<br>hangi masal<span class="n">?</span></h2><p style="margin: 8px 0 0; font-size: 14px; color: #B9BED6">Diski seç, desenini gör.</p></div>
    <div class="px" style="margin-top: 16px"><div class="tavan">
      <sc-for list="{{proj}}" as="p" hint-placeholder-count="2"><span class="{{p.cls}}" aria-hidden="true"><img src="{{p.src}}" alt=""></span></sc-for>
      <span style="position: absolute; left: 12px; top: 12px; font-size: 12px; font-weight: 600; color: #FFFDF9; background: rgba(12,16,39,.6); padding: 3px 9px; border-radius: 999px">[gerçek tavan fotoğrafı]</span>
      <span style="position: absolute; left: 14px; bottom: 14px; display: flex; flex-direction: column; line-height: 1.2; color: #FFFDF9"><span style="font-size: 12px; color: #B9BED6">Disk</span><b class="ser" style="font-size: 18px; font-weight: 400">{{discName}}</b></span>
    </div></div>
    <div class="noscroll" style="display: flex; gap: 6px; overflow-x: auto; padding: 14px 16px 0">
      <sc-for list="{{discs}}" as="d" hint-placeholder-count="11"><button class="{{d.cls}}" onClick="{{d.pick}}" aria-pressed="{{d.on}}" aria-label="{{d.n}} diskini göster"><img src="{{d.src}}" alt=""></button></sc-for>
    </div>
    <!-- Kullanıcı: her kutuda bütün diskler çıkar, iki modelde de. Sayfada yalnız "6 masal diski" yazılır (22 Eki: "6 + 6 değil, 6 masal") -->
  </section>

  <!-- 30 gün iade -->
  <section class="px bolum gir">
    <div class="otuz"><span class="muhur-kap">""" + muhur() + """<span class="muhur-say"><b class="say">30</b><span>gün</span></span></span><span style="display: flex; flex-direction: column; gap: 2px"><b style="font-size: 16px; line-height: 1.2">Beğenmezsen iade et</b><span style="font-size: 14px; color: #5C6078">Yasal 14 günü 30 güne uzattık. İade kargosu ücretsiz.</span></span></div>
  </section>

  <!-- SSS -->
  <section class="px bolum gir">
    <h2 class="h2">Merak edilenler<span class="n">.</span></h2>
    <div style="margin-top: 14px; border-top: 1.5px solid #E3D8C7">
      <sc-for list="{{faq}}" as="f" hint-placeholder-count="6"><details class="sss"><summary>{{f.q}}<span class="arti" aria-hidden="true">+</span></summary><p style="margin: 0 0 16px; font-size: 14px; color: #5C6078">{{f.a}}</p></details></sc-for>
    </div>
  </section>

  <!-- Diğer ürünler -->
  <section class="bolum gir">
    <div class="px" style="display: flex; align-items: flex-end; justify-content: space-between"><h2 class="h2">Odanın geri<br>kalanı için<span class="n">.</span></h2><span class="serit-sag"><span style="font-size: 13px; color: #5C6078">{{shopCount}} ürün</span>""" + SERIT_OK + """</span></div>
    <div class="noscroll" style="display: flex; gap: 10px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-left: 16px; padding: 14px 16px 4px">
      <sc-for list="{{shop}}" as="u" hint-placeholder-count="4">
        <a class="kart" href="#"><span style="position: relative; aspect-ratio: 1 / 1; background: #F1E8DA; overflow: hidden"><img src="{{u.src}}" alt="{{u.n}}" style="width: 100%; height: 100%; object-fit: cover; display: block"><sc-if value="{{u.pct}}" hint-placeholder-val="{{true}}"><span style="position: absolute; left: 8px; top: 8px; font-size: 12px; font-weight: 700; background: #FFFDF9; color: #A05A1C; padding: 2px 8px; border-radius: 999px">{{u.pct}}</span></sc-if></span><span style="padding: 10px 12px 12px; display: flex; flex-direction: column; gap: 4px"><b style="font-size: 14px; font-weight: 600; line-height: 1.25; min-height: 35px">{{u.n}}</b><span style="display: flex; align-items: baseline; gap: 6px; font-variant-numeric: tabular-nums"><b style="font-size: 14px">{{u.price}}</b><s style="font-size: 12px; color: #5C6078">{{u.old}}</s></span></span></a>
      </sc-for>
    </div>
  </section>

  <!-- Alt bilgi -->
  <footer class="alt-bilgi">
    <div class="px">
      <h2 class="h2" style="color: #FFFDF9">İlk geceyi <br>birlikte izleyin<span class="n">.</span></h2>
      <button class="btn-on" type="button" style="margin-top: 16px; box-shadow: 0 3px 0 rgba(12,16,39,.6)">{{onLabel}}</button>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0 16px; margin-top: 24px; font-size: 14px"><a href="#">Mesafeli Satış Sözleşmesi</a><a href="#">KVKK</a><a href="#">İade Politikası</a><a href="#">İletişim</a></div>
      <div aria-label="Ayluna" style="margin-top: 22px; display: flex; align-items: center; gap: 12px; color: #FFFDF9">""" + isaret(48) + """<span class="ser" aria-hidden="true" style="font-size: 56px; line-height: .8; letter-spacing: -.045em">Ayluna</span></div>
      <p style="margin: 14px 0 0; padding-top: 14px; border-top: 1px solid rgba(255,253,249,.12); font-size: 12px; color: #B9BED6">Fiyatlara KDV dahildir. © 2026 Ayluna</p>
    </div>
  </footer>

  <!-- Yapışkan çubuk: canlıda sayfa başından görünür, paket ve buton alanı ekrandayken gizlenir (IntersectionObserver); padding-bottom: env(safe-area-inset-bottom) -->
  <div class="yapis">
    <span style="position: relative; flex: none; width: 46px; height: 46px; border-radius: 12px; overflow: hidden; background: #2A3260"><img class="kesim" src="{{modelSrc}}" alt="" style="height: 38px; bottom: 4px"></span>
    <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; line-height: 1.15; color: #FFFDF9; font-variant-numeric: tabular-nums"><b style="font-size: 16px">LunaDream</b><span style="font-size: 12px; color: #B9BED6">{{adetName}}</span><span style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #B9BED6"><svg class="sayac-ay" viewBox="0 0 24 24" aria-hidden="true" style="width: 12px; height: 12px"><circle cx="12" cy="12" r="9"></circle><path d="{{cdAy}}"></path></svg>{{cdTiny}}</span></span>
    <button class="btn-on" type="button" style="flex: 0 0 150px; width: 150px; min-height: 52px; margin: 0; font-size: 16px; box-shadow: 0 3px 0 rgba(12,16,39,.6)">Satın al</button>
  </div>
</div>
"""

JS = """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { g: 0, model: 'kiz', adet: null, l2: null, topic: 'Tümü', disc: 1, oda: 0, dn: 0, dnT: 0, now: Date.now() }; }
  componentDidMount() {
    var self = this;
    // Büyük görünüm Esc ile kapanır
    this.esc = function (e) { if (e.key === 'Escape' && self.state.buyuk) self.setState({ buyuk: null }); };
    document.addEventListener('keydown', this.esc);
    // Azaltılmış hareket (ör. Windows'ta animasyon efektleri kapalı): galeri yine 5 sn'de geçer ama kaymadan, anında (galGit)
    var azH = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    // Neler yapabiliyor?: ekrana girince dört kelime bir kez oynar, "Tak."ta durur; azaltılmış harekette tur yok
""" + OZ4.js_tur('dk') + """    // Tek saat: sayaçlar + galeri 5 sn'de bir sonraki fotoğrafa kayar (elle kaydırılınca durur) + dönen satır (hediye 4 sn, kargo 6 sn)
    this.tik = 0; this.iv = setInterval(function () { self.tik++; var S = self.state, o = { now: Date.now() };
      if (S.gOto !== false && self.tik % 5 === 0) self.galGit((S.g + 1) % Math.max(1, document.querySelectorAll('.kf').length));
      if (!azH && self.tik - S.dnT >= (S.dn ? 6 : 4)) { o.dn = 1 - S.dn; o.dnT = self.tik; }
      self.setState(o); }, 1000);
    // Stok kurdelesi: buton ekrana girince bir kez belirir (gözlemci yoksa hemen)
    var al = document.querySelector('.al-on');
    if (al && typeof IntersectionObserver !== 'undefined') {
      this.stokio = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { self.setState({ stokAc: true }); self.stokio.disconnect(); } }, { threshold: .6 });
      this.stokio.observe(al);
    } else this.setState({ stokAc: true });
    // Kargo takibi: çizelge ekrana girince döngü başlar (gözlemci yoksa hemen)
    var yol = document.querySelector('.yol');
    if (yol && typeof IntersectionObserver !== 'undefined') {
      this.yolio = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { self.setState({ yolAc: true }); self.yolio.disconnect(); } }, { threshold: .6 });
      this.yolio.observe(yol);
    } else this.setState({ yolAc: true });
  }
  componentDidUpdate() {
    var acik = !!this.state.buyuk;
    if (acik !== !!this.buyukAcik) { this.buyukAcik = acik; document.documentElement.style.overflow = acik ? 'hidden' : '';
      if (acik) { var x = document.querySelector('.buyuk-x'); if (x) x.focus(); } }
    // Galeri kabı başka fotoğrafta kaldıysa (DOM yeniden kurulduysa) durumdaki fotoğrafa geri al
    var el = document.querySelector('.kare-foto'); if (el && el.clientWidth && Math.abs(el.scrollLeft - this.state.g * el.clientWidth) > el.clientWidth / 2) { this.otoKay = Date.now(); el.scrollLeft = this.state.g * el.clientWidth; }
  }
""" + OZ4.JS_ORTAK + OZ4.JS_DK + """  galGit(i) { var el = document.querySelector('.kare-foto'); if (el && el.scrollTo && el.clientWidth) { this.otoKay = Date.now(); el.scrollTo({ left: i * el.clientWidth, behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); } else this.setState({ g: i }); }
  componentWillUnmount() { clearInterval(this.iv); """ + OZ4.js_kapat('dk') + """ if (this.esc) document.removeEventListener('keydown', this.esc); if (this.yolio) this.yolio.disconnect(); }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    """ + TL_JS + """
    // Galeri Shopify'daki gibi (kullanıcı, 19 Eki): canlı mağazanın görselleri, aynı sıra, kare (ogrenme/galeri-canli.json).
    // Çıkarılanlar: 'Temalar' afişi (kutuda olmayan diskler), 'Elif K.' kartı ve yorum kolajı (uydurma yorum).
    var G = """ + str(P_GAL) + """;
    // Ay göstergesi: i. fotoğrafın evresi (i+1)/N; geçilenler ve o anki yanar, son fotoğrafta dolunay
    function AYE(f) { var r = 9, c = 12, rx = Math.abs(1 - 2 * f) * r; return f >= 1 ? 'M12 3a9 9 0 1 1 0 18a9 9 0 1 1 0-18Z' : 'M' + c + ' ' + (c - r) + 'A' + r + ' ' + r + ' 0 0 1 ' + c + ' ' + (c + r) + 'A' + rx.toFixed(2) + ' ' + r + ' 0 0 ' + (f < .5 ? 0 : 1) + ' ' + c + ' ' + (c - r) + 'Z'; }
    var gal = G.map(function (g, i) { var on = i === S.g; return { src: B + g.id, n: g.n, pos: '50% 50%', top: 56, h: 390, ay: AYE((i + 1) / G.length), acls: i < S.g ? 'lit' : (on ? 'lit on' : '') }; });
    function gKay(e) { var el = e && (e.currentTarget || e.target); if (!el || !el.clientWidth) return; var i = Math.round(el.scrollLeft / el.clientWidth), o = {};
      if (i !== self.state.g) o.g = i; if (self.state.gOto !== false && Date.now() - (self.otoKay || 0) > 900) o.gOto = false; if (o.g !== undefined || o.gOto === false) self.setState(o); }
    var kiz = S.model === 'kiz';
    var KIZ = B + 'e02351b3be4a1c555c5d760d0bbda723', ERKEK = B + '0033dfea6282c5bc479c385213661c00';
    // Küçük ürün görselleri tek dil: stüdyo fotoğrafından arka planı temizlenmiş kesim (model, paket, yapışkan çubuk)
    var KES_K = B + 'b823966c39ff35824b4d6e74757646ec', KES_E = B + '20f90021119e4c3bdbc930b283e3635a';
    var SRC = function (m) { return m === 'kiz' ? KES_K : KES_E; };
    var MOD = { kiz: { n: 'Kız', sub: 'Tavşanlı' }, erkek: { n: 'Erkek', sub: 'Robot' } };
    var models = ['kiz', 'erkek'].map(function (id) { var on = S.model === id; return { n: MOD[id].n, sub: MOD[id].sub, src: SRC(id), on: on ? 'true' : 'false', cls: on ? 'kt on' : 'kt', pick: function () { self.setState({ model: id }); } }; });
    // Paket: canlı sitedeki fiyatlar. 1 Adet'te ₺1.999 (son 10 günde uygulandı, kullanıcı teyidi). 2 Adet'te birim fiyat ve kazanç.
    var P1 = 1699.99, P2 = 2749.99, C1 = 1999;
    // 2 Adet: 1. lamba = model kartı; 2. lamba kartın içinde seçilir (açıkça seçilmediyse modeli izler).
    // İki lamba aynı model ya da 1 Kız + 1 Erkek (canlıda sepete iki ayrı varyant eklenir).
    var l1 = S.model, l2 = S.l2 || S.model;
    var ikinci = ['kiz', 'erkek'].map(function (id) { var on = l2 === id; return { n: MOD[id].n, src: SRC(id), on: on ? 'true' : 'false', cls: on ? 'lcip on' : 'lcip', pick: function () { self.setState({ l2: id }); } }; });
    var paket = [
      { n: 1, t: '1 Adet', p: TL(P1, true), old: TL(C1, true), unit: '', sub: '%' + Math.round((1 - P1 / C1) * 100) + ' indirim', rib: false },
      { n: 2, t: '2 Adet', p: TL(P2, true), old: '', unit: 'tanesi ' + TL(Math.floor(P2 / 2 * 100) / 100, true), sub: TL(2 * P1 - P2, true) + ' kazanç', rib: true }
    ].map(function (b) { var on = S.adet === b.n; return { src1: b.n === 2 ? SRC(l1) : SRC(S.model), src2: SRC(l2), tlCls: b.n === 2 ? 'tl cift' : 'tl', t: b.t, p: b.p, old: b.old, hasOld: !!b.old, unit: b.unit, sub: b.sub, rib: b.rib, two: b.n === 2,
      on: on ? 'true' : 'false', ac: on && b.n === 2, cls: on ? 'kt on' : 'kt', pick: function () { self.setState({ adet: b.n }); } }; });
    var total = S.adet === 2 ? P2 : P1, online = Math.round(total * 0.95 * 100) / 100, kapida = total + 80;
    var AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
    """ + KARGO_JS + """
    var KG = KARGO(S.now || Date.now()), kd = KG.gun;
    var t1 = new Date(kd); t1.setDate(t1.getDate() + 3); var t2 = new Date(kd); t2.setDate(t2.getDate() + 7);
    var teslim = t1.getMonth() === t2.getMonth() ? t1.getDate() + '–' + t2.getDate() + ' ' + AY[t2.getMonth()] : t1.getDate() + ' ' + AY[t1.getMonth()] + '–' + t2.getDate() + ' ' + AY[t2.getMonth()];
    // Bugünkü fiyat sayacı (kullanıcı kararı): her gece 23:59'da (İstanbul) sıfırlanır. Gerçek olması için:
    // toptancı zammı gün içinde gelse bile o günün fiyatı 23:59'a kadar korunur, yeni fiyat ertesi gün başlar.
    function IKI(n) { return n < 10 ? '0' + n : String(n); }
    var ist = new Date(new Date(S.now || Date.now()).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var gunSonu = new Date(ist.getFullYear(), ist.getMonth(), ist.getDate(), 23, 59, 59, 999);
    var kalan = Math.max(0, gunSonu.getTime() - ist.getTime());
    var hh = Math.floor(kalan / 3600000), mi = Math.floor(kalan / 60000) % 60, ss = Math.floor(kalan / 1000) % 60;
    var cdLine = 'Bugünkü fiyat garantisi';
    var cdShort = IKI(hh) + ':' + IKI(mi) + ':' + IKI(ss);
    var cdTiny = IKI(hh) + ' sa ' + IKI(mi) + ' dk kaldı';
    // Sayaç ayı: gün başında dolunay, gün bittikçe söner (kalan süre / 24 saat). Dakikada bir görünür değişir.
    function AYY(f) { var r = 9, c = 12, rx = Math.abs(1 - 2 * f) * r; return 'M' + c + ' ' + (c - r) + 'A' + r + ' ' + r + ' 0 0 1 ' + c + ' ' + (c + r) + 'A' + rx.toFixed(2) + ' ' + r + ' 0 0 ' + (f < .5 ? 0 : 1) + ' ' + c + ' ' + (c - r) + 'Z'; }
    var cdAy = AYY(Math.round(kalan / 864000) / 100);
    var cdAria = 'Bugünkü fiyat garantisinin bitmesine ' + hh + ' saat ' + mi + ' dakika';
    // Videolar: kapaklar mevcut görsellerden; canlıda gerçek videolar (başlıklar düzenlenebilir)
    var vids = [
      { t: 'Işık kapanınca tavanda masal', k: 'Kız modeli', src: B + '5ce96d9e6f38e8d571ac1cb9e529ec22', pos: '50% 40%' },
      { t: 'Bir müşterimizin akşamı', k: 'Müşteri videosu', src: B + '7ad3cbbe71680f4ed3027dbd056e391f', pos: '50% 40%' },
      { t: 'Uzay Kaşifi tavanda', k: 'Erkek modeli', src: B + 'b2c8d9b92ad3541b532e3aa108a74735', pos: '50% 45%' },
      { t: 'Disk nasıl takılır', k: 'Kurulum', src: B + '5b284c77c252b08a2974bde8e43de126', pos: '50% 50%' }
    ];
    // Müşteri fotoğrafları (Loox foto yorumları)
    // Gerçek müşteri içeriği. Eski sitedeki "mutlu kullanıcı" fotoğraflarının 5'i Higgsfield üretimi (hf_): müşteri diye konmaz; yalnız IMG_4145 (minikesnaftr hikâyesi) alındı.
    function buyut(src, ad) { return function () { self.setState({ buyuk: src, buyukAd: ad }); }; }
    // Eleştirmen (19 Eki): mesaj-6 ("zürafa çıkmadı") kutu vaadiyle, mesaj-7 ("ürününüz gümrükte") aynı gün kargo sözüyle çelişir; şeritte yok
    var MSJ = ['bfa2c1457ff701500133bafa4a53605c', '32cce494ace36080ef05c6fda3dddcab', 'dd91892546cddf3d9e1b066b51659996', 'f588a714a98cbc77c1ea79dbd24d8f2e',
      '9f72b52adc531fbbc2c19b68852ac418', '3389d58e6756cdaf84214ee47c529234'];
    var mesajlar = MSJ.map(function (id, i) { var n = 'Müşteri mesajı ' + (i + 1); return { src: B + id, n: n, ac: buyut(B + id, n) }; });
    // Müşteri kanıtı: öne çıkan yorum + fotoğraf ve mesajların karışık şeridi + kısa yorum listesi
    var mfoto = [['f17eea08d28f448f84ae69364c4320a3', 'LunaDream ile oynayan küçük kız (müşterinin paylaştığı hikâye)'], ['4323cd781a0d687b528b3059505be48c', 'LunaDream’e sarılan küçük kız'], ['7ad3cbbe71680f4ed3027dbd056e391f', 'Çocuk odasında yanan LunaDream'], ['f060b12bc3353fae64eedf62798c5711', 'Duvara yansıyan deniz deseni'], ['ec3c3976bbe8f18e5660f4a4c355ebf7', 'Karanlıkta yanan LunaDream']]
      .map(function (f) { var a = 'Müşteri fotoğrafı: ' + f[1]; return { src: B + f[0], alt: a, ac: buyut(B + f[0], a) }; });
    var REV = [
      { tags: ['Uyku'], name: 'Burak G.', q: 'Çocuğum çalıştırmadan uyumuyor, uykuya hemen dalıyor.' },
      { tags: ['Hediye'], name: 'Handan B.', q: 'Torunum filmlerini kendisi seçti ve onunla uyumaya başladı.' },
      { tags: ['Kalite'], name: 'Sevcan Z.', q: '2 tane aldık, gayet sağlam geldi. Paketlenmesi de güzeldi.' },
      { tags: ['Hediye', 'Kalite'], name: 'Abdülkerim T.', q: 'Reklamında nasıl ise aynısı, hatta daha iyisi. Çocuklar için mükemmel bir hediye.' },
      { tags: ['Kalite'], name: 'Mehmet C.', q: 'Anlatıldığı ve gösterildiği gibi çıktı. Bu kadar iyi olmasını beklemiyordum.' }
    ];
    var revAll = REV.map(function (r) { return { q: r.q, name: r.name }; });
    var oneQ = revAll[3], revRest = revAll.filter(function (r, i) { return i !== 3; });
    // Fotoğraf şeridi lambaya sarılan kızla başlar
    var fsira = [mfoto[1], mfoto[0], mfoto[2], mfoto[3], mfoto[4]];
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
    // Görseller yazısız ürün kesimleri (23 Eki): mağaza afişlerindeki "153.748 yıldız detayı", "1 Yıl Garanti" gibi teyitsiz yazılar kartta yok (canvas/capraz)
""" + KAY_JS + GALOK_JS + """    var PR = [
      { n: 'Yıldız Işığı Nemlendirici', p: 849.99, c: 1099, id: '18992c2375dc098b76ce965f442b1fac' },
      { n: 'Ayluna Galaksi Night Projektör', p: 2199, c: 2999, id: '8dec4fb3201c17c5af97a727f760fc22' },
      { n: 'Astronot Oda Nemlendirici', p: 799, c: 0, id: 'd8080b6820c271f87bc04c6e4740f45e' },
      { n: 'Ayluna Çocuk Gece Feneri', p: 1599, c: 0, id: '6f398702127fe04cec0b55cbea8d417a' },
      { n: 'Galaxy USB Projektör', p: 1599, c: 1999, id: '41f7a27eea89e7b4288be3202350a7c1' },
      { n: 'Galaksi Ambiyans Işığı', p: 1499, c: 2898, id: '25a27f563fc8df1f0ba6a183605872c0' },
      { n: 'Aroma Terapi Nemlendirici', p: 1499, c: 1999, id: '0eed23be3ba0b89b788601cc2ce21eda' },
      { n: 'Eğitici Akıllı Çizim Tahtası', p: 1199, c: 1999, id: '861b0ab4da17f667a9b093797c4c3e81' },
      { n: 'Ayluna AyFeneri', p: 1649.99, c: 2499, id: 'd77d9351df992b5c2d25a76be3cfe019' },
      { n: 'Sunset Lamba', p: 699, c: 999, id: 'ede1c77509a69c04052181b5db4a8f54' },
      { n: 'Dokunmatik Ambiyans Lamba', p: 1299.99, c: 0, id: '99a7d6be05cb9fa65839c7398154f621' },
      { n: 'Ayluna Kum Saati Lamba', p: 799, c: 999, id: 'c1be20769938c100b273d139871a766c' },
      { n: 'Ayluna Retro Mini Pikap', p: 1499, c: 1999.99, id: '68a527f889ae6e33cd6c38eb1d44b12c' }
    ];
    // Not: üstü çizili fiyatlar her ürün için son 10 gün kuralına tabi; canlıda compare_at_price'tan gelir.
    var shop = PR.map(function (x) { var d = x.c > x.p; return { n: x.n, src: B + x.id, price: TL(x.p, true), old: d ? TL(x.c, true) : '', pct: d ? '%' + Math.round((1 - x.p / x.c) * 100) : '' }; });
    // Odalar: "… modelini seç" modeli seçer, model kartlarına kayar; şerit kaydıkça nokta değişir
    function odaSec(m) { return function () { self.setState({ model: m }); var h = document.getElementById('modeller');
      if (h && h.scrollIntoView) h.scrollIntoView({ behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'center' }); }; }
    function odaKay(e) { var el = e && (e.currentTarget || e.target); if (!el || !el.children.length) return; var m = el.scrollLeft + el.clientWidth / 2, en = 0, ef = 1e9;
      for (var k = 0; k < el.children.length; k++) { var c = el.children[k], f = Math.abs(c.offsetLeft + c.offsetWidth / 2 - m); if (f < ef) { ef = f; en = k; } }
      if (en !== (S.oda || 0)) self.setState({ oda: en }); }
    // Odası böyle görünecek · Gece vitrini: karta ya da aya dokununca o oda ortaya kayar. Görseller yer tutucu; Flow kareleri gelince kimlikler değişir.
    var AZH = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    function odaGit(i) { return function () { var el = document.querySelector('.vt-serit'), c = el && el.children[i]; if (i !== (S.oda || 0)) self.setState({ oda: i });
      if (c && el.scrollTo) el.scrollTo({ left: c.offsetLeft - (el.clientWidth - c.offsetWidth) / 2, behavior: AZH ? 'auto' : 'smooth' }); }; }
    function diskGit() { var h = document.getElementById('diskler'); if (h && h.scrollIntoView) h.scrollIntoView({ behavior: AZH ? 'auto' : 'smooth', block: 'start' }); }
    var ODA = [
      { id: 'fd0bca1b99cf3837b69fb025cc4e2cd9', pos: '50% 40%', alt: 'Gece çocuk odası: komodinde yanan LunaDream Kız, tavanda ay ve yıldızlar', cip: 'Kız modeli · Tavşanlı', bas: 'Tavanda masal', yazi: 'Işığı kapatınca seçtiği masal diski tavana yansır.', sec: 'Kız modelini seç', e: 'kiz' },
      { id: '8b1f621be2cb3b6133b7b78bc14e1963', pos: '50% 30%', alt: 'Kucakta yanan LunaDream Kız', cip: 'İki modelde de ninni', bas: 'Birlikte dinleyin', yazi: 'En sevdiği ninniyi telefondan aç; ses lambadan gelsin.', sec: 'Modelini seç', e: '' },
      { id: '31751eb35473aca04420825deb3c3ce0', pos: '62% 50%', alt: 'Gece çocuk odası: komodinde yanan LunaDream Erkek (Uzay Kaşifi), duvarda yıldızlar', cip: 'Erkek modeli · Uzay Kaşifi', bas: 'Tavanda uzay', yazi: 'Uzay diskini tak, tavana uzay yansısın.', sec: 'Erkek modelini seç', e: 'erkek' },
      { id: '5b284c77c252b08a2974bde8e43de126', pos: '50% 40%', alt: 'Kubbesi açık LunaDream ve masal diskleri', cip: '6 masal diski', bas: 'Masalı o seçsin', yazi: 'Bu gecenin diskini kutudaki masallardan çocuğun seçsin.', sec: 'Diskleri gör', e: 'disk' }
    ];
    var OEV = """ + str([ay(f) for f in (.25, .5, .75, 1)]) + """, oi = S.oda || 0;
    var odalar = ODA.map(function (o, i) { var on = i === oi; return { src: B + o.id, pos: o.pos, alt: o.alt, cip: o.cip, bas: o.bas, yazi: o.yazi, sec: o.sec, ev: OEV[i],
      cls: 'vt-kart' + (on ? ' on' : ''), mcls: 'vt-m' + (on ? ' on' : ''), ayCls: 'vt-ay' + (on ? ' on' : ''), gizli: on ? 'false' : 'true', tab: on ? '0' : '-1', basili: on ? 'true' : 'false',
      lbl: (i + 1) + '. oda: ' + o.bas, git: odaGit(i), eylem: o.e === 'disk' ? diskGit : odaSec(o.e || S.model || 'kiz') }; });
    // Ürün soruları (teslim kartının altı; 22 Eki kullanıcı "o kadar çok soru olmasın"): yalnız 4 temel soru; gerisi alttaki SSS'de
    var URS = [
      { q: 'Bu ürün ne işe yarıyor?', a: 'Gece lambası ve masal projektörü bir arada. Seçtiğin masal diskini tavana yansıtır, telefondaki ninniyi Bluetooth ile çalar. Işığı üç kademede kısılır, şarjla kablosuz çalışır.' },
      { q: 'Projeksiyon nasıl çalışıyor?', a: (kiz ? 'Kubbeyi' : 'Robotun başını') + ' aç, masal diskini üstten tak ve kapat. Odanın ışığını kapatınca diskteki masal tavana ve duvara yansır.' },
      { q: 'Bluetooth var mı, ne işe yarıyor?', a: 'İki modelde de var. Telefona ya da tablete bağlanır; açtığın ninni, müzik ya da sesli masal lambanın hoparlöründen çalar.' },
      { q: 'Kutu içeriğinde neler var?', a: 'Her kutuda: seçtiğin modelde 1 lamba, 6 masal diski, 6 hediye disk ve USB şarj kablosu. İki modelde de aynı; 2 Adet’te iki kutu gelir.' }
    ];
    // Merak edilenler (alttaki SSS): ürün kullanımı soruları (canlı sayfadan, teyitli olanlar), sonra satın alma soruları
    // 23 Eki: sadeleştirmede 12 → 7'ye inmişti; kullanıcı geri istedi, 12 soru
    var faq = [
      { q: 'Ürün şarjlı mı, prizde mi çalışır?', a: 'Şarjlı; şarjı varken kablosuz çalışır. Kutudaki USB kabloyla şarj edilir, şarj olurken de kullanılabilir.' },
      { q: 'Gece rutinine nasıl entegre ederim?', a: 'Yatmadan önce ana ışığı kapatın, diski birlikte seçip takın, telefondan kısa bir ninni açın ve ışığı kısığa alın. Her gece aynı sırayla yapınca yatma vakti belli olur.' },
      { q: 'Işığı göz yorar mı, çocuğu rahatsız eder mi?', a: 'Işığı sıcak tonlu ve yumuşak. Gece için orta ya da kısık kademeyi seç; ışığı göze değil, duvara ya da tavana yansıt.' },
      { q: 'Çocuk odasında kullanmak güvenli mi?', a: 'Düz ve sağlam bir yere koy. Masal diskleri küçük parça sayılır; küçük çocuklar diskleri büyüklerle birlikte kullansın. Şarj ederken kabloyu ortada bırakma.' },
      { q: 'Tuşlar ile neleri kontrol edebilirim?', a: 'Lambanın tuşlarıyla açıp kapatır, ışığı parlak, orta ve kısık arasında değiştirir, Bluetooth’u açarsın. Sesi telefondan da ayarlayabilirsin.' },
      { q: 'Hareket sensörü var mı?', a: 'Yok. Lamba tuşlarla açılıp kapanır; gece kendiliğinden yanıp sönmez.' },
      { q: 'Bluetooth hoparlöre nasıl bağlanırım?', a: 'Lambayı aç ve Bluetooth’unu aç. Telefonda Bluetooth’u açıp listeden lambayı seç. Bağlanınca telefondaki ninniler ve müzik uygulamaları lambadan çalar.' },
      { q: 'Bluetooth bağlanmıyor, ne yapmalıyım?', a: 'Telefonda Bluetooth’u kapatıp aç, lambayı kapatıp aç. Eski eşleşmeyi “unut” deyip yeniden bağlan ve yakından dene. Olmazsa İletişim sayfasından yaz, yardımcı olalım.' },
      { q: 'Kaç yaş için uygun?', a: 'Her yaş için uygun.' },
      { q: 'Kargo ne zaman gelir?', a: 'İş günü 16.00’ya kadar verilen sipariş aynı gün, sonrakiler ertesi iş günü kargoya verilir; Türkiye geneline 3–7 günde ulaşır.' },
      { q: 'Kartla mı, kapıda mı ödeyeyim?', a: 'Tüm kredi ve banka kartları geçer; kartla öderken %5 indirim alırsın, kart bilgin bize gelmez. Kapıda ödemede ₺80 kapıda ödeme ücreti eklenir; ürün geldiğinde nakit ya da kartla ödersin.' },
      { q: 'Beğenmezsem iade edebilir miyim?', a: '30 gün içinde iade edebilirsin. Sana iade kodunu göndeririz, kargosu ücretsizdir. İlk 14 gün yasal cayma hakkındır.' }
    ];
    """ + OZ4.js_dk_deger("S.model === 'erkek'") + """    return { ...dkV,
      gal: gal, gNo: S.g + 1, gCount: G.length, gKay: gKay, gPrev: function () { self.setState({ g: (S.g + G.length - 1) % G.length }); }, gNext: function () { self.setState({ g: (S.g + 1) % G.length }); }, models: models, modelName: kiz ? 'Kız · tavşanlı' : 'Erkek · Uzay Kaşifi', modelSrc: kiz ? KES_K : KES_E,
      kiz: kiz, erkek: !kiz, paket: paket, ikinci: ikinci, modelEtiket: S.adet === 2 ? '1. lamba' : 'Model', adetName: S.adet === 2 ? (l1 !== l2 ? 'Kız + Erkek' : (l1 === 'kiz' ? '2 Kız' : '2 Erkek')) : '1 Adet',
      onLabel: 'Güvenli Ödeme ile Al', onPrice: TL(online, true),  // düğmede fiyat yok (kullanıcı, 19 Eki)
      p1: TL(P1, true), c1: TL(C1, true), pct: Math.round((1 - P1 / C1) * 100),
      onNote: 'Kartla %5 indirimli · ' + TL(kapida - online, true) + ' daha az',
      kargo: KG.bugun ? 'Bugün' : kd.getDate() + ' ' + AY[kd.getMonth()], teslim: teslim,
      kgMetin: KG.metin, kgBugun: KG.bugun, kgSayac: KG.sayac, kgAria: KG.aria,
      dnA: 'dn-s' + (S.dn === 0 ? ' on' : self.tik - S.dnT < 1 ? ' ust' : ''), dnB: 'dn-s' + (S.dn === 1 ? ' on' : self.tik - S.dnT < 1 ? ' ust' : ''),
      // Puan ve sayı canlıda Loox'tan (teyit bekliyor)
      rating: '4,7', reviews: 62, starPct: 94,
      yolCls: S.yolAc ? 'yol on' : 'yol', sihKiz: S.model !== 'erkek', sihErkek: S.model === 'erkek', stokCls: S.stokAc ? 'stok-kd on' : 'stok-kd', vids: vids, mfoto: mfoto, mesajlar: mesajlar,
      oneQ: oneQ, revRest: revRest, fsira: fsira,
      buyuk: S.buyuk || '', buyukAd: S.buyukAd || '', buyukVar: !!S.buyuk, buyukKapat: function () { self.setState({ buyuk: null }); }, cdLine: cdLine, cdShort: cdShort, cdTiny: cdTiny, cubukAlt: S.adet === 2 ? (l1 !== l2 ? 'Kız + Erkek' : (l1 === 'kiz' ? '2 Kız' : '2 Erkek')) : '1 Adet · ' + (kiz ? 'Kız' : 'Erkek'), cdAy: cdAy, cdAria: cdAria, discs: discs, proj: proj, discName: DISCS[S.disc].n,
      odalar: odalar, odaKay: odaKay, shop: shop, shopCount: PR.length, kayGeri: KAY(-1), kayIleri: KAY(1), galGeri: GALOK(-1), galIleri: GALOK(1), faq: faq,
      urs: URS
    };
  }
}"""

# Diğer ürün sayfaları (luna_usb.py) bu dosyadaki CSS ve parçaları içe aktarır; yazma yalnız doğrudan çalıştırınca
# Sihirli Özellikler bloğu: masaüstünde galerinin altına geçer (ortak.urun_ust)
def sihirli(h):
    i = h.index('<p class="ust-yazi" style="margin-top: 22px; margin-bottom: 0">Sihirli özellikler</p>')
    return h[i:h.index('\n    </div>', h.index('<div class="sih">', i)) + len('\n    </div>')]


if __name__ == '__main__':
    open(OUT, 'w', encoding='utf-8').write(HEAD.format(title='LunaDream · E', css=CSS + SERIT_OK_CSS) + urun_ust(HTML, '<section class="sahne"') + TAIL.format(h=int(os.environ.get('E_H', 7647)), js=masa_bayrak(JS)))
    print('yazıldı:', os.path.abspath(OUT))
