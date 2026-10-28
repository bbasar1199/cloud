# Yılbaşı Ağacı Projektör Lamba · imza ürün sayfası (28 Eki). Çalıştır: python3 yilbasi_sayfa.py
# Kullanıcı: "LunaDream için yaptığımız gibi profesyonel ve satışa hazır bir site yap." Üç yön (onizleme/yilbasi-yon) → eleştirmen
# birleşimi: Main sistemi (beyaz zemin, lacivert, amber; Young Serif + Onest), A'nın "Kutuda ne var?" noktalı fotoğrafı,
# B'nin disk seçicisi yalnız bir gece bandında, C'nin "Yaparken / Yanınca" ikilisi, 3 adımda kurulum.
# Satın alma çekirdeği AyFeneri / Galaksi Night ile aynı (ozel_sayfa.py): galeri, ad + fiyat, özellikler, paket, stok (elle), Güvenli Ödeme,
# EasySell yeri, teslim çizgisi, 4 soru, SSS, 30 gün iade, mesajlar, öneri şeridi, alt bilgi, yapışkan çubuk.
# Gerçek aciliyet: yılbaşından önce teslim için son sipariş günü (1 iş gününde kargo + en geç 7 gün; 31 Aralık'tan geriye). Sahte sayaç yok.
# Teyitsiz: fiyat (geçici; canlıda Shopify), disk sayısı (afişte "6+"), parça sayısı. Yorum yok (yeni ürün): Loox yıldız satırı ve yorum bölümü konmadı.
# Görseller: kullanıcının kutu fotoğrafı ve montaj videosu kareleri; tavan ve disk görselleri satıcı afişinin yazısız kısmı (canvas/ozel/yb-*).
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ortak import UST_CSS, TAIL, TL_JS, KARGO_JS, tk_css, tk_adim, TK_DEGER, TK_IKON, canli_galeri, urun_ust, masa_bayrak, mesaj_js, MESAJ_CSS, SERIT_OK_CSS, KAY_JS, GAL_OK
import luna_usb as U
import ozel_yon as O
import ozel_sayfa as OS
import urun_soru as US
CANVAS = os.path.join(HERE, '..', '..', 'canvas')
B = '/_blob/'
I = OS.I
H = 'yilbasi-agaci-projektor-lamba'
AD = 'Yılbaşı Ağacı Projektör Lamba'
P1 = 999.0   # GEÇİCİ: ürün Shopify'da yok (28 Eki); canlıda fiyat Shopify'dan gelir (ayluna.js)
C1 = None

# 2. tur (28 Eki, kullanıcı: "çok sade ve sıkıcı olmuş"): çam yeşili + altın bantlar, dört imza anı (Ağacı yak, dergi kapağı, dönen tavan, takvim yaprağı)
# 4. tur (28 Eki, kullanıcı: "hem yılbaşı hem ürünle mükemmel uyumlu"): renkler ürünün kendi kutusundan (pudra pembesi zemin, altın yaldız,
# çam yeşili, kırmızı kozalak); ışık dizisi ayraçları (kutudaki "A little light, a lot of joy" ışıkları), galeri göstergesi minik ağaçlar.
TEMA = dict(v='#E3B65A', v2='#8C5E10', zemin='#FFFFFF', cizgi='#ECE7E1', koyu='#0D261C', koyu2='#173828',
            fb='"Young Serif"', fg='"Onest"', bk=400, bls='-.02em',
            font='family=Young+Serif&family=Onest:wght@400;500;600;700;800')

# Kutu fotoğrafındaki parçalar (montaj kartındaki "Kit contents" + fotoğraf); konum % (sol, üst)
PARCA = [('Hediye kutusu', 'Yılbaşı baskılı, kağıt dolgulu.', 52, 18), ('Altın abajur', 'Desenli çıkartmayı giydirirsin.', 36, 43),
         ('Desenli çıkartma', 'Abajurun etrafına sarılır.', 77, 48), ('İnci çıkartmalar', 'Kırmızı ve altın; kendinden yapışkanlı.', 60, 60),
         ('"Merry Christmas" çıkartması', 'Ağacın tepesine süs.', 63, 70), ('Tüylü süs çubukları', 'Kabloya sarılır, ağaç olur.', 83, 77),
         ('Projektör ve desen diskleri', 'USB kablolu, lensli modül; diskler değişir.', 36, 85), ('Montaj kartı', 'QR kodunda montaj videosu.', 22, 52)]
DISK = [('Klasik yılbaşı', 'yb-d-klasik'), ('Yeni yıl mesajı', 'yb-d-mesaj'), ('Kar taneleri', 'yb-d-kar'),
        ('Ren geyikleri', 'yb-d-geyik'), ('Kardan adam', 'yb-d-kardan'), ('Çanlar', 'yb-d-can')]
ADIM = [('yb-adim1', 'Sar', 'Tüylü çubukları USB kablonun etrafına sar, bükerek ağaç şekli ver.'),
        ('yb-adim3', 'Giydir', 'Desenli çıkartmayı altın abajura yapıştır; istersen inci çıkartmalarla süsle.'),
        ('yb-adim4', 'Tak, tavana çevir', 'Abajuru tak, USB’ye bağla, ışığı kapat.')]

USB_IK = '<svg viewBox="0 0 28 28"><rect x="9" y="3" width="10" height="9" rx="1.5"></rect><path d="M11 6h2M15 6h2"></path><path d="M14 12v8"></path><path d="M14 20c-4 0-6 2-6 5M14 20c4 0 6 2 6 5"></path></svg>'
HEDIYE_IK = '<svg viewBox="0 0 28 28"><rect x="4" y="11" width="20" height="14" rx="2"></rect><path d="M3 11h22M14 11v14"></path><path d="M14 11c-2-5-8-6-8-2 0 2 4 2 8 2zM14 11c2-5 8-6 8-2 0 2-4 2-8 2z"></path></svg>'
AGAC_IK = '<svg viewBox="0 0 28 28"><path d="M14 3l6 8h-3l5 7h-4l4 5H6l4-5H6l5-7H8z"></path><path d="M14 23v3"></path></svg>'

CSS = r"""
.al h1{font-size:24px;line-height:1.15}
.fiyat b{font-size:22px}
.dsk-y{display:flex}.dsk-y img{width:26px;height:26px;border-radius:50%;object-fit:cover;margin-left:-9px;box-shadow:0 0 0 2px #fff}.dsk-y img:first-child{margin-left:0}
/* Yılbaşından önce kapında: gerçek tarih (1 iş gününde kargo + en geç 7 gün) */
.yb-k{display:grid;grid-template-columns:52px minmax(0,1fr);gap:12px;align-items:center;margin:14px 0 0;padding:12px 14px;border-radius:16px;background:#F3F7F4;box-shadow:inset 0 0 0 1px #D7E6DC;color:var(--lac)}
.yb-k .gk{display:grid;place-items:center;align-content:center;width:52px;height:52px;border-radius:14px;background:#2E6B4F;color:#fff;font-weight:800;font-size:19px;line-height:1;font-variant-numeric:tabular-nums}
.yb-k .gk small{display:block;margin-top:3px;font-size:12px;font-weight:700}
.yb-k b{display:block;font-size:15px;line-height:1.3}
.yb-k span.t{display:block;margin-top:2px;font-size:13px;color:var(--soluk)}
.yb-k.gecti{background:#FFF6EC;box-shadow:inset 0 0 0 1px #F1DEC6}.yb-k.gecti .gk{background:var(--v2)}
.adapt{display:flex;gap:8px;align-items:flex-start;margin:10px 0 0;font-size:13px;color:var(--soluk)}
.adapt svg{flex:none;width:18px;height:18px;margin-top:1px;fill:none;stroke:var(--lac);stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
/* Yaparken / Yanınca */
.ikili{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:8px;margin-top:16px}
.ikili figure{position:relative;margin:0;border-radius:18px;overflow:hidden;aspect-ratio:4/5;background:#0D261C}
.ikili img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ikili figcaption{position:absolute;left:10px;bottom:10px;padding:4px 10px;border-radius:999px;background:#fff;color:var(--lac);font-size:12px;font-weight:700}
.ikili-w .ok{position:absolute;left:50%;top:50%;z-index:1;display:grid;place-items:center;width:36px;height:36px;margin:-18px 0 0 -18px;border-radius:50%;background:var(--v);box-shadow:0 0 0 4px #fff}
.ikili-w .ok svg{width:16px;height:16px;fill:none;stroke:var(--lac);stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.ikili-w{position:relative}
/* Kutuda ne var? */
.kut{position:relative;margin-top:16px;border-radius:20px;overflow:hidden;background:#EFE6D8}
.kut img{display:block;width:100%;height:auto}
.kut button{position:absolute;width:30px;height:30px;margin:-15px 0 0 -15px;padding:0;border:0;border-radius:50%;background:#fff;color:var(--lac);font:800 13px var(--fg);box-shadow:0 0 0 2px var(--lac),0 4px 10px rgba(0,0,0,.25);transition:transform .25s var(--ease),background-color .25s var(--ease)}
.kut button::after{content:"";position:absolute;inset:-9px}
.kut button.on{background:var(--lac);color:#fff;transform:scale(1.18)}
.kl{display:grid;grid-template-columns:28px minmax(0,1fr);gap:10px;align-items:center;margin-top:12px;padding:12px 14px;border-radius:14px;background:#F6F7F9;color:var(--lac)}
.kl em{display:grid;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--lac);color:#fff;font-style:normal;font-weight:800;font-size:13px}
.kl b{display:block;font-size:15px}.kl span{display:block;font-size:13px;color:var(--soluk)}
.kliste{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:6px 12px;margin:14px 0 0;padding:0;font-size:13px;color:var(--lac)}
.kliste li{display:flex;gap:6px}.kliste li::before{content:"";flex:none;width:6px;height:6px;margin-top:7px;border-radius:50%;background:var(--v)}
.kyok{margin:12px 0 0;padding:10px 12px;border-radius:12px;background:#FFF6EC;color:#6B3D0B;font-size:13px}
/* Bu gece hangisi? (tek gece bandı) */
.tav{position:relative;width:260px;height:260px;margin:18px auto 0;border-radius:50%;overflow:hidden;box-shadow:0 0 0 6px rgba(255,255,255,.06),0 0 70px rgba(242,166,90,.22)}
.tav img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:rotate(-5deg) scale(1.06);transition:opacity .5s var(--ease),transform .7s var(--ease)}
.tav img.on{opacity:1;transform:none}
.tav-ad{display:block;margin-top:12px;text-align:center;font-weight:700;color:#fff}
.dk{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:16px}
.dk button{display:flex;flex-direction:column;align-items:center;gap:6px;min-height:48px;padding:8px 4px;border:0;border-radius:14px;background:rgba(255,255,255,.06);color:#F4E7C8;font:600 12px var(--fg);box-shadow:inset 0 0 0 1px rgba(255,255,255,.12)}
.dk button img{width:46px;height:46px;border-radius:50%;object-fit:cover}
.dk button.on{box-shadow:inset 0 0 0 2px var(--v);color:#fff}
.koyu .alt-not{margin:14px 0 0;font-size:12px;color:#C9D6CE;text-align:center}
/* 3 adım */
.adm{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:16px;padding:16px 16px 4px}
.adm figure{flex:0 0 240px;margin:0;scroll-snap-align:start;border-radius:18px;background:#F6F7F9;overflow:hidden}
.adm img{display:block;width:100%;aspect-ratio:1/1;object-fit:cover}
.adm figcaption{padding:12px 14px 14px;font-size:13px;color:var(--soluk)}
.adm figcaption b{display:flex;align-items:center;gap:8px;margin-bottom:2px;font-size:16px;color:var(--lac)}
.adm figcaption b i{display:grid;place-items:center;width:24px;height:24px;border-radius:50%;background:var(--lac);color:#fff;font-style:normal;font-size:12px}
.qr{margin:12px 16px 0;padding:12px 14px;border-radius:14px;background:#F6F7F9;color:var(--lac);font-size:13px}
.pg{--lac:#123A2A;--kirmizi:#8E2A22}
.vid{position:relative;flex:0 0 172px;height:306px;scroll-snap-align:start;padding:0;border:0;border-radius:20px;overflow:hidden;background:#0D261C;cursor:pointer;color:#fff;text-align:left;font:inherit}
.vid img,.vid video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.vid::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(8,24,17,.88) 0,rgba(8,24,17,0) 52%)}
.vid-oyna{position:absolute;left:50%;top:42%;z-index:1;width:56px;height:56px;margin:-28px 0 0 -28px;border-radius:50%;display:grid;place-items:center;background:rgba(255,253,251,.94);box-shadow:0 6px 16px rgba(8,24,17,.35)}
.vid-oyna svg{width:22px;height:22px;fill:#123A2A;margin-left:3px}
.vid-alt{position:absolute;left:12px;right:12px;bottom:12px;z-index:1;display:flex;flex-direction:column;gap:2px;line-height:1.25}
.vid-alt b{font-size:14px}.vid-alt span{font-size:13px;color:#E9DDBF}
/* Özellik kartları (29 Eki, kullanıcı: "emoji benefit LunaDream gibi düzgün ve iyi animasyonlarla olsun"): LunaDream "Sihirli özellikler"
   ile aynı kurgu. Her kartta 28 px'lik iki parçalı gösterge: ürünün ikonu + yanında çalışan küçük arayüz (adım çubukları, disk dizisi,
   fiş → akış → yanan ağaç, açılan kutu). 6 sn'lik tek döngü, kartlar 0,6 sn arayla; yalnız transform/opacity; başlık + iki satır. */
.ozb{margin:22px 0 0;font-size:13px;font-weight:700;color:#123A2A}
.yo{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-top:10px}
.yo-k{display:flex;flex-direction:column;gap:10px;padding:12px;border-radius:14px;background:#fff;border:1px solid #E4E6EB;color:#123A2A;text-decoration:none;transition:transform .2s cubic-bezier(.2,.7,.2,1)}
a.yo-k:active{transform:scale(.985)}
.yo-k:nth-child(2){--gec:.6s}.yo-k:nth-child(3){--gec:1.2s}.yo-k:nth-child(4){--gec:1.8s}
.yo-k b{display:block;font-size:14px;font-weight:600;line-height:1.25}
.yo-k .t{display:block;margin-top:2px;font-size:13px;line-height:1.4;color:#5C6078}
.yo-k u{color:#123A2A;text-underline-offset:3px;text-decoration-thickness:1px;white-space:nowrap}
.yg{display:flex;align-items:center;gap:8px;height:28px}
.yg svg{flex:none;height:28px;width:auto;overflow:visible;fill:none;stroke:#123A2A;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.yg *{animation-duration:6s;animation-iteration-count:infinite;animation-timing-function:cubic-bezier(.2,.7,.2,1);animation-fill-mode:both}
/* 1 · Kendin kur: dört adım çubuğu sırayla dolar (Sar, Süsle, Tak, Yansıt); ağaca süs sarılır, sonda tepe yıldızı yanar */
.yg-agac .s{stroke:#C99A3A;stroke-width:1.8;opacity:0}
.yg-agac .s1{animation-name:yga1}.yg-agac .s2{animation-name:yga2}.yg-agac .s3{animation-name:yga3}
@keyframes yga1{0%,10%{opacity:0}16%,92%{opacity:1}100%{opacity:0}}
@keyframes yga2{0%,30%{opacity:0}36%,92%{opacity:1}100%{opacity:0}}
@keyframes yga3{0%,50%{opacity:0}56%,92%{opacity:1}100%{opacity:0}}
.yg-agac .yz{fill:#E3B65A;stroke:none;transform-box:fill-box;transform-origin:center;animation-name:ygyz}
@keyframes ygyz{0%,66%{opacity:.2;transform:scale(.5)}72%,92%{opacity:1;transform:none}100%{opacity:.2;transform:scale(.5)}}
.adm{display:flex;gap:3px}
.adm i{width:9px;height:4px;border-radius:2px;background:#123A2A;opacity:.14}
.adm i:nth-child(1){animation-name:ygm1}.adm i:nth-child(2){animation-name:ygm2}.adm i:nth-child(3){animation-name:ygm3}.adm i:nth-child(4){animation-name:ygm4;background:#E3B65A}
@keyframes ygm1{0%,10%{opacity:.14}16%,92%{opacity:1}100%{opacity:.14}}
@keyframes ygm2{0%,30%{opacity:.14}36%,92%{opacity:1}100%{opacity:.14}}
@keyframes ygm3{0%,50%{opacity:.14}56%,92%{opacity:1}100%{opacity:.14}}
@keyframes ygm4{0%,66%{opacity:.14}72%,92%{opacity:1}100%{opacity:.14}}
/* 2 · Değişen desenler: disk dizisi; sıradaki disk öne gelir ve döner (LunaDream disk kartının dili) */
.yg-disk{gap:0}
.yg-disk span{position:relative;display:block;width:28px;height:28px;margin-left:-7px;border-radius:50%;overflow:hidden;box-shadow:0 0 0 2px #fff;transform:scale(.82);opacity:.55}
.yg-disk span:first-child{margin-left:0}
.yg-disk img{display:block;width:100%;height:100%;object-fit:cover}
.yg-disk span:nth-child(1){animation-name:ygd1;z-index:3}.yg-disk span:nth-child(2){animation-name:ygd2;z-index:2}.yg-disk span:nth-child(3){animation-name:ygd3;z-index:1}
.yg-disk span:nth-child(1) img{animation-name:ygdr1}.yg-disk span:nth-child(2) img{animation-name:ygdr2}.yg-disk span:nth-child(3) img{animation-name:ygdr3}
@keyframes ygd1{0%,30%{transform:none;opacity:1}36%,94%{transform:scale(.82);opacity:.55}100%{transform:none;opacity:1}}
@keyframes ygd2{0%,30%{transform:scale(.82);opacity:.55}36%,63%{transform:none;opacity:1}69%,100%{transform:scale(.82);opacity:.55}}
@keyframes ygd3{0%,63%{transform:scale(.82);opacity:.55}69%,94%{transform:none;opacity:1}100%{transform:scale(.82);opacity:.55}}
@keyframes ygdr1{0%{transform:none}33%,100%{transform:rotate(-120deg)}}
@keyframes ygdr2{0%,33%{transform:none}66%,100%{transform:rotate(-120deg)}}
@keyframes ygdr3{0%,66%{transform:none}97%,100%{transform:rotate(-120deg)}}
/* 3 · USB ile yanar: fiş girer → üç nokta akar → ağaç yanar, hale açılır (LunaDream telefon → lamba kartının dili) */
.yg-usb .fis{animation-name:ygf}
@keyframes ygf{0%,6%{transform:translateX(-5px);opacity:.5}18%,92%{transform:none;opacity:1}100%{transform:translateX(-5px);opacity:.5}}
.akis2{position:relative;width:24px;height:6px}
.akis2 i{position:absolute;left:0;top:1px;width:4px;height:4px;border-radius:50%;background:#C99A3A;opacity:0;animation-name:ygak}
.akis2 i:nth-child(2){animation-delay:.2s}.akis2 i:nth-child(3){animation-delay:.4s}
@keyframes ygak{0%,18%{transform:none;opacity:0}21%{opacity:1}34%{transform:translateX(20px);opacity:0}100%{transform:translateX(20px);opacity:0}}
.yg-usb .ag{animation-name:ygag}
@keyframes ygag{0%,36%{opacity:.35}42%,92%{opacity:1}100%{opacity:.35}}
.yg-usb .dol{fill:#F6DFA6;stroke:none;opacity:0;animation-name:ygic}
.yg-usb .ic{fill:#E3B65A;stroke:none;opacity:0;animation-name:ygic}
@keyframes ygic{0%,36%{opacity:0}42%,92%{opacity:1}100%{opacity:0}}
.yg-usb .hal{fill:none;stroke:#E3B65A;stroke-width:1.5;opacity:0;transform-box:fill-box;transform-origin:center;animation-name:yghl}
@keyframes yghl{0%,40%{opacity:0;transform:scale(.6)}48%{opacity:.9}66%,100%{opacity:0;transform:scale(1.25)}}
/* 4 · Hediye kutusunda: kapak kalkar, içinden yıldız, disk ve süs çubuğu sırayla yükselir */
.yg-kutu .kap{transform-box:fill-box;transform-origin:0% 100%;animation-name:ygkp}
@keyframes ygkp{0%,12%{transform:none}22%,80%{transform:translateY(-3px) rotate(-14deg)}90%,100%{transform:none}}
.cik{display:flex;align-items:flex-end;gap:5px;height:24px}
.cik i{display:block;opacity:0;transform:translateY(8px)}
.cik i:nth-child(1){animation-name:ygc1}.cik i:nth-child(2){animation-name:ygc2}.cik i:nth-child(3){animation-name:ygc3}
.cik .c-y{width:10px;height:10px;background:#E3B65A;clip-path:polygon(50% 0,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%)}
.cik .c-d{width:12px;height:12px;border-radius:50%;border:1.5px solid #123A2A;box-shadow:inset 0 0 0 2.5px #FFFFFF;background:#8E2A22}
.cik .c-c{width:4px;height:18px;border-radius:2px;background:#2F6B45}
@keyframes ygc1{0%,22%{opacity:0;transform:translateY(8px)}30%,80%{opacity:1;transform:none}88%,100%{opacity:0;transform:translateY(8px)}}
@keyframes ygc2{0%,32%{opacity:0;transform:translateY(8px)}40%,80%{opacity:1;transform:none}88%,100%{opacity:0;transform:translateY(8px)}}
@keyframes ygc3{0%,42%{opacity:0;transform:translateY(8px)}50%,80%{opacity:1;transform:none}88%,100%{opacity:0;transform:translateY(8px)}}
.yg *{animation-delay:var(--gec,0s)}
.akis2 i:nth-child(2){animation-delay:calc(var(--gec,0s) + .2s)}.akis2 i:nth-child(3){animation-delay:calc(var(--gec,0s) + .4s)}
/* Duran kare (hareket azaltılmış): dolu adımlar, öndeki disk, yanan ağaç, açık kutu */
@media (prefers-reduced-motion:reduce){.yg *{animation:none!important}.yg-agac .s,.adm i,.yg-usb .ic,.cik i{opacity:1;transform:none}.yg-disk span:first-child{opacity:1;transform:none}.yg-usb .ag,.yg-usb .dol{opacity:1}}
/* Canlı fiyat, paket eski fiyatı, kargo şeridi, teslim kartı, yapışkan sayaç (29 Eki, canlı denetim; LunaDream'deki karşılıkları) */
.fiyat{display:flex;align-items:baseline;flex-wrap:wrap;gap:4px 10px}
.fiyat .rozet{align-self:center;background:#8E2A22;color:#fff}
.pk-f{display:flex;flex-direction:column;align-items:flex-end;line-height:1.2}
.pk-f s{margin-top:2px;font-size:12px;font-weight:500;color:var(--soluk)}
.donen{position:relative;display:grid;margin:12px 0 0;padding:10px 14px;border-radius:14px;background:#123A2A;font-size:14px;font-weight:700;color:#fff;overflow:hidden}
.dn-s{grid-area:1/1;display:flex;align-items:center;gap:8px;min-height:24px;opacity:0;transform:translateY(80%);transition:opacity .36s cubic-bezier(.2,.7,.2,1),transform .36s cubic-bezier(.2,.7,.2,1)}
.dn-s.on{opacity:1;transform:none}.dn-s.ust{transform:translateY(-80%)}
.dn-s svg{width:16px;height:16px;flex:none;fill:#E3B65A}
.dn-s svg.dn-kt{fill:none;stroke:#E3B65A;stroke-width:1.6;stroke-linejoin:round}
.dn-m{flex:1;min-width:0;font-size:13px;line-height:1.3}
.dn-sy{flex:none;padding:3px 8px;border-radius:999px;background:rgba(255,255,255,.14);color:#fff;font-size:14px;font-variant-numeric:tabular-nums;letter-spacing:.02em}
.dn-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
@media (prefers-reduced-motion:reduce){.donen{row-gap:8px}.dn-s{grid-area:auto;opacity:1;transform:none;transition:none}}
.al .teslim{margin-top:20px;padding:16px 8px 12px;border:1px solid var(--cizgi);border-radius:20px}
.al .teslim .yol{margin-top:0}
.y-yazi .sayac-ay{width:12px;height:12px;margin:0 3px 0 0;vertical-align:-1px}
.y-yazi .sayac-ay circle{fill:none;stroke:rgba(255,255,255,.6);stroke-width:2}.y-yazi .sayac-ay path{fill:#E3B65A}
.teslim::before,.teslim .yd{background:#EEF2EF}
.teslim .yol-iz em::before{box-shadow:0 0 0 2px #EEF2EF,0 0 0 3.5px var(--lac)}
.pk-k .nokta{margin-left:4px}.pk-k.on .nokta{box-shadow:inset 0 0 0 1.6px #123A2A}.pk-k.on .nokta i{opacity:1;transform:none;background:#123A2A}
.fy-rozet{background:#123A2A;color:#fff}
/* Ay sonu fiyatı: küçük, paket başlığının sağında (LunaDream "Kampanya · 1–31 Ekim" yeri) */
.pk-bas{display:flex;align-items:center;justify-content:space-between;gap:10px}
.pk-bas .ays-k{display:inline-flex;align-items:center;gap:5px;font-size:12px;font-weight:700;color:#8E2A22;font-variant-numeric:tabular-nums;white-space:nowrap}
.pk-bas .ays-k svg{width:14px;height:14px;fill:none;stroke:#C9A27A;stroke-width:1.6}.pk-bas .ays-k path{fill:#E3B65A;stroke:none}
/* Videolar (Shopify'da ürünün videoları; tasarımda kurulum videosu karesi) */
.vd{position:relative;display:block;margin-top:14px;border-radius:20px;overflow:hidden;aspect-ratio:9/12;background:#0D261C}
.vd img{width:100%;height:100%;object-fit:cover;opacity:.85}
.vd .oy{position:absolute;left:50%;top:50%;display:grid;place-items:center;width:64px;height:64px;margin:-32px 0 0 -32px;border-radius:50%;background:rgba(255,253,251,.92)}
.vd .oy svg{width:22px;height:22px;margin-left:3px;fill:#123A2A}
.vd figcaption{position:absolute;left:14px;right:14px;bottom:12px;color:#fff;font-size:14px;font-weight:600}
@media (prefers-reduced-motion:reduce){.yg *{animation:none!important;opacity:1}}

.gv-l{list-style:none;margin:14px 0 0;padding:0;border-top:1px solid #ECE7E1}.gv-l li{display:grid;grid-template-columns:120px minmax(0,1fr);gap:12px;padding:14px 0;border-bottom:1px solid #ECE7E1}.gv-l b{font-family:var(--fb);font-weight:400;font-size:17px;color:#123A2A}.gv-l span{font-size:13px;color:#6B5246}
/* Fotoğraflı üç kart (ikon yok) */
.fk{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin:16px 0 0}
.fk figure{margin:0;border-radius:16px;overflow:hidden;background:#F6F3EE}
.fk img{display:block;width:100%;aspect-ratio:3/4;object-fit:cover}
.fk figcaption{padding:8px 10px 10px}
.fk b{display:block;font-family:var(--fb);font-weight:400;font-size:15px;line-height:1.1;color:#123A2A}
.fk span{display:block;margin-top:3px;font-size:12px;line-height:1.35;color:#6B5246}
/* Dönen güven şeridi */
.ser{margin:12px 0 0;font-size:13px;font-weight:600;color:#123A2A}
.ser-pen{display:block;height:24px;overflow:hidden;-webkit-mask-image:linear-gradient(#0000,#000 3px,#000 21px,#0000);mask-image:linear-gradient(#0000,#000 3px,#000 21px,#0000)}
.ser-iz{display:flex;flex-direction:column;transition:transform .5s var(--ease)}.ser-iz.anlik{transition:none}
.ser-s{display:flex;align-items:center;gap:8px;height:24px;white-space:nowrap}
.ser-s::before{content:"";flex:none;width:7px;height:7px;border-radius:50%;background:#8E2A22;box-shadow:0 0 0 3px rgba(142,42,34,.15)}
/* Ay sonu fiyat kartı */
.ays{display:grid;grid-template-columns:34px minmax(0,1fr) auto;gap:10px;align-items:center;margin:12px 0 0;padding:12px 14px;border-radius:16px;background:#123A2A;color:#fff}
.ays-ay svg{width:30px;height:30px;fill:none;stroke:rgba(244,231,200,.5);stroke-width:1.4}.ays-ay path{fill:#F3C978;stroke:none}
.ays b{display:block;font-size:14px;line-height:1.3}.ays .t{display:block;font-size:12px;color:#C9D6CE}
.ays-s{display:flex;align-items:baseline;gap:2px;font-variant-numeric:tabular-nums}
.ays-s b{display:inline-grid;place-items:center;min-width:34px;height:34px;border-radius:9px;background:#F3C978;color:#123A2A;font-size:17px}
.ays-s small{margin:0 4px 0 2px;font-size:12px;color:#E9DDBF}
/* Stok kurdelesi butonun üst kenarına yarı biner */
.al-on{position:relative;margin-top:16px}.al-on .btn1{margin-top:0}
.stk{position:absolute;left:16px;top:-12px;z-index:1;display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 10px 0 8px;border-radius:999px;background:#8E2A22;color:#fff;font-size:12px;font-weight:700;box-shadow:0 0 0 3px #fff}
.stk i{width:7px;height:7px;border-radius:50%;background:#F3C978}

.pg .otuz{background:#F6F3EE;color:#123A2A}.pg .otuz b,.pg .otuz>span:last-child span{color:#123A2A}
.pg .mesaj-bol img{border-radius:14px;box-shadow:0 0 0 6px #fff,0 0 0 7px #ECE7E1}
.pg .koyu{background:radial-gradient(120% 70% at 50% 0%,#1B4433 0%,#0D261C 70%)}
.pg .h2 .n,.pg .bas-y .n{color:var(--v2)}.pg .koyu .n,.pg footer .n,.pg .yak .n{color:var(--v)}
.pg .al h1{color:#123A2A}
/* Ağacı yak: oda karanlık; dokununca ışık alttan (lambadan) tavana yayılır. 2 sn kapalı → 7 sn açık; dokununca durur */
.yak{position:relative;border-radius:24px;overflow:hidden;background:#05100B;color:#fff}
.yak-g{position:relative;height:420px;overflow:hidden}
.pg .al{padding-bottom:8px}.pg #yak{padding-top:20px}
.yak-g img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 20%}
.yak .k0{filter:brightness(.42) saturate(.55)}
.yak .k1{clip-path:circle(0% at 50% 100%);transition:clip-path 1.8s var(--ease) .1s}
.yak.on .k1{clip-path:circle(150% at 50% 100%)}
.yak .kor{position:absolute;left:50%;bottom:22px;width:14px;height:14px;margin-left:-7px;border-radius:50%;background:var(--v);box-shadow:0 0 18px 6px rgba(227,182,90,.55);transition:opacity .6s var(--ease)}
.yak.on .kor{opacity:0}
.yak-y{position:absolute;left:18px;right:18px;top:20px}
.yak-y .bas-y{margin:0;font-size:40px;line-height:1;color:#fff;text-shadow:0 2px 20px rgba(0,0,0,.5)}
.yak-alt{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px 16px;background:#0D261C}
.yak-alt span{font-size:14px;color:#D9E3DC}
.anah{display:inline-flex;align-items:center;gap:10px;min-height:48px;padding:0 6px 0 14px;border:0;border-radius:999px;background:rgba(255,255,255,.08);color:#fff;font:700 14px var(--fg)}
.anah i{position:relative;width:46px;height:28px;border-radius:999px;background:#33473E;transition:background-color .3s var(--ease)}
.anah i::after{content:"";position:absolute;left:3px;top:3px;width:22px;height:22px;border-radius:50%;background:#fff;transition:transform .3s var(--ease)}
.yak.on .anah i{background:var(--v)}.yak.on .anah i::after{transform:translateX(18px)}
/* Dergi kapağı: dev tek kelime, arkasında o adımın karesi; 2,6 sn'de bir değişir, dokununca durur */
.dg{position:relative;height:520px;margin-top:16px;border-radius:24px;overflow:hidden;background:#0D261C}
.dg img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(1.06);transition:opacity .6s var(--ease),transform 2.6s var(--ease)}
.dg img.on{opacity:.92;transform:none}
.dg::after{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(8,24,17,.92) 0%,rgba(8,24,17,.15) 55%,rgba(8,24,17,0) 70%);pointer-events:none}
.dg-k{position:absolute;left:16px;right:16px;bottom:72px;z-index:1;margin:0;font-family:var(--fb);font-weight:400;font-size:96px;line-height:.9;letter-spacing:-.04em;color:#fff}
.dg-k span{display:inline-block;animation:dgk .55s var(--ease) both}
.dg-k em{font-style:normal;color:var(--v)}
@keyframes dgk{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
.dg-t{position:absolute;left:16px;right:16px;bottom:22px;z-index:1;margin:0;font-size:15px;color:#E4ECE6}
.dg-s{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px;margin-top:10px}
.dg-s button{min-height:48px;border:0;border-radius:12px;background:#F2EEE5;color:var(--lac);font:700 14px var(--fg);box-shadow:inset 0 -3px 0 transparent}
.dg-s button.on{background:var(--lac);color:#fff;box-shadow:inset 0 -3px 0 var(--v)}
/* Dönen tavan: seçili desen tavanda ağır ağır döner */
.tav-d{position:absolute;inset:0;animation:tavd 90s linear infinite}
@keyframes tavd{to{transform:rotate(360deg)}}
/* Kime hediye? */
.hd{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:16px;padding:16px 16px 4px}
.hd-k{flex:0 0 220px;scroll-snap-align:start;padding:18px 16px;border-radius:20px;color:#fff;min-height:200px;display:flex;flex-direction:column}
.hd-k svg{width:34px;height:34px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.hd-k b{display:block;margin-top:auto;font-family:var(--fb);font-weight:400;font-size:24px;line-height:1.05}
.hd-k span{display:block;margin-top:6px;font-size:13px;line-height:1.4;opacity:.88}
.hd-k.y{background:#163828}.hd-k.k{background:#8E2A22}.hd-k.a{background:#E9D3A4;color:#3B2A0E}.hd-k.l{background:#9A6A3A}
/* Takvim yaprağı: yılbaşından önce teslim için son sipariş günü (gerçek hesap) */
.tkv{display:grid;grid-template-columns:120px minmax(0,1fr);gap:16px;align-items:center}
.tkv-y{position:relative;border-radius:16px;overflow:hidden;background:#fff;box-shadow:0 10px 30px rgba(0,0,0,.25);text-align:center;transform:rotate(-3deg)}
.tkv-y b{display:block;padding:6px 0;background:var(--kirmizi);color:#fff;font-size:13px;letter-spacing:.08em}
.tkv-y strong{display:block;padding:6px 0 2px;font-family:var(--fb);font-weight:400;font-size:62px;line-height:1;color:var(--lac)}
.tkv-y small{display:block;padding-bottom:10px;font-size:12px;color:#7A5A48}
.tkv-y::before{content:"";position:absolute;left:0;right:0;top:30px;height:6px;background:radial-gradient(circle,#fff 2px,transparent 2.5px) 0 0/12px 6px}
.tkv-m{text-align:left}.tkv-m b{display:block;font-family:var(--fb);font-weight:400;font-size:22px;line-height:1.1;color:#fff}
.tkv-m span{display:block;margin-top:6px;font-size:14px;color:#D9E3DC}
.tkv-m .btn1{width:100%;margin-top:14px;background:var(--v);justify-content:center}.pg .tkv-m .btn1,.pg .tkv-m .btn1 .b-ic>span{color:#14231B}.pg .tkv-m .btn1 svg{stroke:#14231B}
/* 4. tur: kutunun dünyası */
.pg .serit{background:#123A2A;color:#F4E7C8}.pg .serit .sy b{background:#1F4A33}
.pg .duyuru.ua-s>.gk{background:#0D261C;color:#E9DDBF}.pg .duyuru.ua-s>.gk b{color:#F3C978}.pg header.ua-b>.gk{background:#123A2A}
.dizi .hale{fill:#F3C978;opacity:.22}
.pg .koyu,.pg footer.alt-bilgi{background:radial-gradient(120% 70% at 50% 0%,#1F4A33 0%,#0D261C 72%)}
/* Işık dizisi ayracı: sarkan tel + yanıp sönen ampuller (yalnız opacity) */
.dizi{position:relative;height:34px;margin:6px 0 -6px;overflow:hidden}
.dizi svg{position:absolute;left:0;top:0;width:100%;height:34px}
.dizi .tel{fill:none;stroke:#2C5A41;stroke-width:1.4}
.dizi .amp{animation:amp 2.4s ease-in-out infinite}
.dizi .amp:nth-child(4n){animation-delay:.8s}.dizi .amp:nth-child(4n+2){animation-delay:1.6s}
@keyframes amp{0%,100%{opacity:1}50%{opacity:.35}}
/* Galeri göstergesi: minik ağaçlar; geçilenler altın yanar */
.pg .d-iz{gap:7px}
.pg .d-iz i{width:11px;height:14px;border-radius:0;background:rgba(255,253,249,.45);clip-path:polygon(50% 0,72% 34%,62% 34%,86% 68%,70% 68%,100% 100%,0 100%,30% 68%,14% 68%,38% 34%,28% 34%)}
.pg .d-iz .lit{background:#F3C978}
.pg .d-iz .on{transform:scale(1.25);transform-origin:50% 100%}
/* Başlık noktaları altın yıldız; kartlar kutunun pudra tonunda */
.pg .al .ozler .oz{background:#F6F3EE}
.pg .pk-k{background:#FFFFFF}
.pg .kl,.pg .adm figure{background:#F6F3EE}
.kut{background:#F4F0EA;box-shadow:0 0 0 6px #fff,0 0 0 7px #ECE7E1}
.yil-c{background:linear-gradient(90deg,#123A2A,#1F4A33)}
.pg .yb-k{background:#123A2A url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 20'%3E%3Cpath d='M0 4q10 8 20 0t20 0' fill='none' stroke='%232C5A41'/%3E%3Ccircle cx='10' cy='8' r='2' fill='%23F3C978'/%3E%3Ccircle cx='30' cy='8' r='2' fill='%23E06A55'/%3E%3C/svg%3E") top/40px 20px repeat-x;padding-top:18px}
/* 3. tur (eleştirmen 6,5 → ilk ekran): satın alma kutusu yeni dile bağlanır */
.pg .yb-k{background:#123A2A;box-shadow:none;color:#fff}.pg .yb-k .gk{background:var(--v);color:#123A2A}.pg .yb-k span.t{color:#C9D6CE}
.pg .al .ozler{gap:6px;border:0;box-shadow:none;background:none}
.pg .al .ozler .oz{border:0;border-radius:14px;background:#F6F3EE;box-shadow:none}
.yil-c{display:inline-flex;align-items:center;gap:6px;margin:0 0 8px;padding:4px 10px;border-radius:999px;background:#123A2A;color:var(--v);font-size:12px;font-weight:700}
.yil-c svg{width:14px;height:14px;fill:var(--v)}
.pg .yapis{background:#0D261C}
.yak-ic{position:absolute;right:14px;bottom:14px;width:84px;height:84px;border-radius:16px;overflow:hidden;box-shadow:0 0 0 3px rgba(255,255,255,.85);opacity:0;transform:translateY(8px);transition:opacity .5s var(--ease) .9s,transform .5s var(--ease) .9s}
.yak-ic img{width:100%;height:100%;object-fit:cover}
.yak-ic small{position:absolute;left:0;right:0;bottom:0;padding:2px 0;background:rgba(13,38,28,.82);color:#fff;font-size:12px;text-align:center}
.yak.on .yak-ic{opacity:1;transform:none}
.hd-k{padding:0;overflow:hidden}
.hd-k .hd-g{height:118px;background-size:cover;background-position:center}
.hd-k .hd-y{display:flex;flex-direction:column;flex:1;padding:12px 14px 16px}
.hd-k .hd-y b{margin-top:0}
.hd-k.k{background:#7A2E24}
@media (prefers-reduced-motion:reduce){.tav img,.kut button,.yak .k1,.dg img,.anah i,.anah i::after,.kor,.yak-ic{transition:none}.tav-d,.dg-k span{animation:none}}
"""


def tl(x): return O.tl(x)


def ozler():
    # 29 Eki (kullanıcı: "emoji benefit LunaDream gibi düzgün ve iyi animasyonlarla olsun"): luna_e.kart_k kurgusu — ürün ikonu +
    # yanında çalışan küçük arayüz; başlık + iki satır, kartlar eşit boy.
    agac = ('<svg viewBox="0 0 24 28"><path d="M12 4 L21 24 H3 Z"></path><path d="M12 24v3"></path>'
            '<path class="s s1" d="M9.5 11.5 Q12 13.5 14.8 10.8"></path><path class="s s2" d="M7.5 16.5 Q12 19.5 16.8 15.6"></path>'
            '<path class="s s3" d="M5.4 21.4 Q12 24.4 18.8 20.6"></path><circle class="yz" cx="12" cy="3.4" r="2.6"></circle></svg>'
            '<span class="adm"><i></i><i></i><i></i><i></i></span>')
    disk = ''.join('<span><img src="%s" alt=""></span>' % I(k) for _, k in DISK[:3])
    usb = ('<svg viewBox="0 0 18 28"><g class="fis"><rect x="1" y="10" width="11" height="8" rx="1.5"></rect><path d="M12 12h4.5v4H12"></path></g></svg>'
           '<span class="akis2"><i></i><i></i><i></i></span>'
           '<svg viewBox="0 0 24 28"><circle class="hal" cx="12" cy="15" r="11"></circle><path class="dol" d="M12 4 L21 24 H3 Z"></path><g class="ag"><path d="M12 4 L21 24 H3 Z"></path><path d="M12 24v3"></path></g>'
           '<circle class="ic" cx="10" cy="14" r="1.6"></circle><circle class="ic" cx="14.5" cy="18.5" r="1.6"></circle><circle class="ic" cx="8" cy="20.5" r="1.6"></circle><circle class="ic" cx="12" cy="9" r="1.4"></circle></svg>')
    kutu = ('<svg viewBox="0 0 28 28"><rect x="5" y="13" width="18" height="13" rx="1.5"></rect><path d="M14 13v13"></path>'
            '<g class="kap"><rect x="3" y="9" width="22" height="4.5" rx="1.2"></rect><path d="M14 9c-2-4-6.5-4.6-5.6-1M14 9c2-4 6.5-4.6 5.6-1"></path></g></svg>'
            '<span class="cik"><i class="c-y"></i><i class="c-d"></i><i class="c-c"></i></span>')
    k = [('agac', agac, 'Kendin kur', 'Çubukları sar, ağacını sen şekillendir.', ''),
         ('disk', disk, 'Değişen desenler', 'Diski değiştir, tavan değişsin.', ' <u>Desenleri gör</u>'),
         ('usb', usb, 'USB ile yanar', 'Şarj başlığı ya da powerbank yeter.', ''),
         ('kutu', kutu, 'Hediye kutusunda', 'Baskılı kutusu ve süsleriyle gelir.', '')]
    kart = ''.join(('<a class="yo-k" href="#diskler">%s</a>' if a == 'disk' else '<div class="yo-k">%s</div>')
                   % ('<span class="yg yg-%s" aria-hidden="true">%s</span><span><b>%s</b><span class="t">%s%s</span></span>' % (a, g, b, t, u)) for a, g, b, t, u in k)
    return '<p class="ozb">Yılbaşı ağacının özellikleri</p><div class="yo">' + kart + '</div>'


def hero():
    gost = '<span class="d-iz" aria-hidden="true"><sc-for list="{{gal}}" as="f" hint-placeholder-count="4"><i class="{{f.dcls}}"></i></sc-for></span>'
    return ("""
  <!-- Galeri: Shopify'da ürünün kendi görselleri; kaydırılır, 5 sn'de kendiliğinden geçer -->
  <section class="hero kare" aria-label="%s fotoğrafları">
    <div class="h-iz noscroll" onScroll="{{gKay}}"><sc-for list="{{gal}}" as="f" hint-placeholder-count="2"><div class="{{f.cls}}"><img src="{{f.src}}" alt="{{f.n}}" style="object-position: {{f.pos}}"></div></sc-for></div>%s
    <div class="h-alt">%s<span style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%%); white-space: nowrap" aria-live="polite">Fotoğraf {{gNo}} / {{gCount}}</span></div>
  </section>
""" % (AD, GAL_OK, gost))


def al():
    # 29 Eki (kullanıcı: "ürün bilgileri kısmında diğerlerine göre çok eksik var, ana iskeleti koruyacağız"): Galaxy USB / LunaDream
    # satın alma iskeleti birebir: ad, fiyat satırı (canlı fiyat; karşılaştırma fiyatı varsa çizili eski fiyat + rozet, LunaDream animasyonu),
    # tek satır açıklama, dönen güven satırı (Dün N yalnız ürün alanı doluysa), özellik kartları, paket, kargo şeridi, stok, butonlar, teslim, 4 soru.
    dsr_ik = lambda ik: '<svg viewBox="0 0 24 24">' + ik + '</svg>'
    HED = '<rect x="4" y="10" width="16" height="10" rx="1.5"></rect><path d="M3 7.5h18v3H3zM12 7.5V20M12 7.5c-1.6-3.4-5.6-4-4.8-.6M12 7.5c1.6-3.4 5.6-4 4.8-.6"></path>'
    sat = [('<i class="dsr-nokta"></i>', '{{tk0a}}<b>{{tk0b}}</b>{{tk0c}}'), (dsr_ik(TK_IKON['kargo']), '<b>Ücretsiz kargo</b> ile kapına'),
           (dsr_ik(TK_IKON['iade']), '<b>30 gün</b> iade hakkı'), (dsr_ik(HED), '<b>Hediye kutusunda</b>, süsleriyle')]
    bir = lambda i, ik, t: '<span class="{{tkC%d}}">' % i + ik + '<span>' + t + '</span></span>'
    dsr = ('    <p class="dun dsr"><span class="dsr-sr">{{tkSr}}</span><span class="dsr-pen" aria-hidden="true"><span class="{{tkCls}}" style="transform: translateY({{tkY}}px)">'
           + ''.join(bir(i, *x) for i, x in enumerate(sat)) + bir(4, *sat[0]) + '</span></span></p>\n')
    return (("""
  <section class="al" id="siparis">
    <h1 class="bas-y">%s</h1>
    <p class="fiyat-satir"><span class="sr-m">{{fySr}}</span><b class="fy-yeni" aria-hidden="true">{{fyP}}</b><sc-if value="{{fyInd}}" hint-placeholder-val="{{false}}"><span class="fy-yuva" aria-hidden="true"><s class="fy-eski">{{fyC}}</s><span class="rozet fy-rozet">%%{{fyPct}} indirim</span></span></sc-if></p>
    <p class="alt-b">Kendin süsle, USB’ye tak; tavan yılbaşı olsun.</p>
""" + dsr + """    %s
    <div class="pk-bas"><span>Paket</span><span class="ays-k" aria-label="{{aysAria}}"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="{{aysYol}}"></path></svg>{{aysAy}} fiyatı · {{aysG}} gün {{aysS}} sa</span></div>
    <div class="pk"><sc-for list="{{paket}}" as="b" hint-placeholder-count="2">
      <button class="{{b.cls}}" onClick="{{b.pick}}" aria-pressed="{{b.on}}"><sc-if value="{{b.rib}}" hint-placeholder-val="{{false}}"><span class="kurdele">Hediye için</span></sc-if><span class="pk-g"><img src="%s" alt=""><sc-if value="{{b.two}}" hint-placeholder-val="{{false}}"><span class="x2">×2</span></sc-if></span><span class="pk-o"><b>{{b.t}}</b><span>{{b.sub}}</span></span><span class="pk-f"><b>{{b.p}}</b><sc-if value="{{b.hasOld}}" hint-placeholder-val="{{false}}"><s>{{b.old}}</s></sc-if></span><span class="nokta"><i></i></span></button>
    </sc-for></div>
    <!-- Dönen kargo şeridi (29 Eki, LunaDream'deki gibi): hediye kutusu 4 sn ↔ 16.00 aynı gün kargo + sayaç 6 sn -->
    <p class="donen"><span class="dn-sr">Yılbaşı baskılı hediye kutusunda. {{kgMetin}}.</span><span class="{{dnA}}" aria-hidden="true"><svg viewBox="0 0 16 16"><path d="M8 1l2 4.2 4.6.6-3.4 3.2.9 4.6L8 11.4 3.9 13.6l.9-4.6L1.4 5.8 6 5.2z"></path></svg>Yılbaşı baskılı hediye kutusunda</span><span class="{{dnB}}" aria-hidden="true"><svg viewBox="0 0 24 24" class="dn-kt"><rect x="3" y="7" width="13" height="10" rx="1.5"></rect><path d="M16 10h3l2 3v4h-5"></path><circle cx="7" cy="18" r="1.6"></circle><circle cx="18" cy="18" r="1.6"></circle></svg><span class="dn-m">{{kgMetin}}</span><sc-if value="{{kgBugun}}" hint-placeholder-val="{{true}}"><b class="dn-sy">{{kgSayac}}</b></sc-if></span></p>
    <!-- Stok kurdelesi: sayı ürün alanı ayluna.stok_kurdele'den (canlı); boşsa ya da 0 ise kurdele yok -->
    <div class="al-on"><sc-if value="{{stokVar}}" hint-placeholder-val="{{false}}"><span class="stk"><i aria-hidden="true"></i>Bu yılbaşı için son {{stokN}} adet</span></sc-if>
    <button class="btn1" type="button"><span class="b-ic"><span>{{onLabel}}</span></span>%s</button></div>
    <div class="ay-dis" data-ay-dis></div>
    <div class="teslim"><ol class="yol" aria-label="Siparişten teslime"><span class="yol-iz" aria-hidden="true"><i></i><i></i><em></em></span><li class="y1"><span class="yd"></span><b>Bugün</b><span>Sipariş verildi</span></li><li class="y2"><span class="yd"></span><b>{{kargo}}</b><span>Kargoda</span></li><li class="y3"><span class="yd"></span><b>{{teslim}}</b><span>Kapında</span></li></ol></div>
    %s
  </section>
""") % (AD, ozler(), I('yb-kare'), U.OK, US.urs_html(US.sorular(OS.ICERIK[H])[0])))


YANINCA = """
  <!-- Yaparken / Yanınca: kurulum karesi (kullanıcının videosu) ve tavandaki desen -->
  <section class="bolum px">
    <h2 class="bas-y h2">Kutudan çıkar,<br>tavana yansıt<span class="n">.</span></h2>
    <p class="alt-b">Bir akşam birlikte kurarsınız; ışığı kapatınca tavan yılbaşı olur.</p>
    <div class="ikili-w"><div class="ikili">
      <figure><img src="@@yb-adim2@@" alt="Tüylü çubuklar kabloya sarılırken"><figcaption>Yaparken</figcaption></figure>
      <figure><img src="@@yb-tavan@@" alt="Tavanda yılbaşı desenleri" style="object-position: 50% 30%"><figcaption>Yanınca</figcaption></figure>
    </div><span class="ok" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"></path></svg></span></div>
  </section>
"""


def kutuda():
    nok = ''.join('<button style="left: %d%%; top: %d%%" class="{{nk%d}}" type="button" onClick="{{nkSec%d}}" aria-label="%s" aria-pressed="{{nkOn%d}}">%d</button>'
                  % (x, y, i, i, n, i, i + 1) for i, (n, _, x, y) in enumerate(PARCA))
    liste = ''.join('<li>%s</li>' % n for n, _, _, _ in PARCA)
    return ("""
  <!-- Kutuda ne var? (eleştirmen 1. fikir): gerçek kutu fotoğrafında numaralı noktalar; dokununca parça adı. Altta düz liste. -->
  <section class="bolum px" id="kutu">
    <h2 class="bas-y h2">Kutuda<br>ne var<span class="n">?</span></h2>
    <p class="alt-b">Fotoğraftaki numaralara dokun.</p>
    <div class="kut"><img src="@@yb-kutu@@" alt="Kutudan çıkan parçalar">""" + nok + """</div>
    <div class="kl"><em>{{nkNo}}</em><span><b>{{nkAd}}</b><span>{{nkAlt}}</span></span></div>
    <ul class="kliste">""" + liste + """</ul>
    <p class="kyok">USB adaptör kutuda yok: evdeki telefon şarj başlığı, powerbank ya da bilgisayar yeter.</p>
  </section>
""")


def gece():
    return ("""
  <!-- Bu gece hangisi? (eleştirmen 2. fikir): sayfadaki tek koyu bant; 4 sn'de kendiliğinden geçer, dokununca durur -->
  <section class="koyu bolum" id="diskler">
    <div class="px"><h2 class="bas-y h2" style="color: #fff">Bu gece<br>hangisi<span class="n">?</span></h2><p class="alt-b" style="color: #C9D6CE">Diski değiştir; desen tavanda ağır ağır dönsün.</p>
    <div class="tav" aria-hidden="true"><div class="tav-d"><sc-for list="{{disk}}" as="d" hint-placeholder-count="2"><img class="{{d.cls}}" src="{{d.src}}" alt=""></sc-for></div></div>
    <span class="tav-ad" aria-live="polite">{{dAd}}</span>
    <div class="dk"><sc-for list="{{disk}}" as="d" hint-placeholder-count="6"><button class="{{d.bcls}}" type="button" onClick="{{d.pick}}" aria-pressed="{{d.on}}"><img src="{{d.src}}" alt="">{{d.n}}</button></sc-for></div>
    <p class="alt-not">Disk değiştirmek: fişi çek, abajuru kaldır, diski değiştir, abajuru tak. Desen görselleri ürün afişinden; tavanda daha yumuşak görünür.</p></div>
  </section>
""")


def adimlar():
    k = ''.join('<figure><img src="@@%s@@" alt="%s"><figcaption><b><i>%d</i>%s</b>%s</figcaption></figure>' % (f, t, i + 1, t, a) for i, (f, t, a) in enumerate(ADIM))
    return ("""
  <!-- 3 adımda ağaç: kullanıcının montaj videosundan kareler -->
  <section class="bolum" id="kurulum">
    <div class="px"><h2 class="bas-y h2">Üç adımda<br>ağaç<span class="n">.</span></h2><p class="alt-b">Videodaki gibi; kaydır.</p></div>
    <div class="adm noscroll">""" + k + """<span aria-hidden="true" style="flex: 0 0 6px"></span></div>
    <p class="qr">Montaj kartının QR kodunda video var. USB ucunu ve projektör lensini kapatma. İnci çıkartmalar küçük parça: küçük çocuklar bir yetişkinle yapsın.</p>
  </section>
""")


def gerisi():
    g = OS.gerisi('af')
    # 29 Eki (kullanıcı: "yorum kısmı eklememişsin onu ekle"): AyFeneri'deki Loox yorum bölümü kalır; tema Loox kutusunu buraya koyar
    # Bölüm değil div: temada önceki bloğun içine girer, blok sayısı ve product.json değişmez (kurulu temada editör ayarları korunur)
    Y0 = '<section class="px" id="yorumlar" style="padding-bottom: 44px">'
    assert Y0 in g
    i = g.index(Y0); j = g.index('</section>', i)
    g = g[:i] + '<div class="px" id="yorumlar" style="padding-top: 44px; padding-bottom: 44px">' + g[i + len(Y0):j] + '</div>' + g[j + len('</section>'):]
    g = g.replace('Bu gece duvarında <br>ay olsun', 'Bu yılbaşı<br>tavana bak').replace('@@af-ay-yakin@@', '@@yb-kare@@').replace('<b>AyFeneri</b>', '<b>Yılbaşı Ağacı</b>')
    g = g.replace('<small style="color: var(--koyu)">Kartla %5 indirim dahil</small>', '')
    Y = '<b>Yılbaşı Ağacı</b><span>{{adetName}}</span>'
    assert Y in g
    g = g.replace(Y, '<b>Yılbaşı Ağacı</b><span>{{adetName}} · <svg class="sayac-ay" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="{{cdAy}}"></path></svg>{{cdTiny}}</span>')
    # 5. tur: ikonlu güven kartları yerine ikonsuz liste (kullanıcı: "emoji benefit kısımlarını beğenmedim")
    assert U.GUVEN in g
    g = g.replace(U.GUVEN, '<ul class="gv-l"><li><b>Ücretsiz kargo</b><span>1 iş gününde kargoda, adım adım takip.</span></li>'
                  '<li><b>Güvenli ödeme</b><span>Kart bilgin bize gelmez; kapıda ödeme de var.</span></li></ul>')
    M1 = 'Sizden gelen<br>mesajlar'; M2 = 'LunaDream siparişlerinden; müşterilerimizin izniyle paylaşılan gerçek sohbetler.'
    assert M1 in g and M2 in g
    g = g.replace(M1, 'Ayluna’dan alanlar<br>yazıyor').replace(M2, 'Diğer lambalarımızı alan müşterilerimizden, izinleriyle.')
    assert 'yb-kare' in g and 'Yılbaşı Ağacı' in g
    return g


YAK = """
  <!-- Ağacı yak (imza anı, AyFeneri'ndeki "Feneri yak" gibi): oda karanlık; ışık lambadan (alttan) tavana yayılır -->
  <section class="bolum px" id="yak">
    <div class="{{yakCls}}">
      <div class="yak-g"><img class="k0" src="@@yb-tavan@@" alt=""><img class="k1" src="@@yb-tavan@@" alt="Tavana yansıyan yılbaşı desenleri"><span class="kor" aria-hidden="true"></span><span class="yak-ic"><img src="@@yb-adim4@@" alt="Kurulan yılbaşı ağacı lambası"><small>Kutudan çıkan</small></span>
        <div class="yak-y"><p class="bas-y">{{yakYazi}}</p></div></div>
      <div class="yak-alt"><span>{{yakAlt}}</span><button class="anah" type="button" onClick="{{yakSw}}" aria-pressed="{{yakOn}}">{{yakEt}}<i></i></button></div>
    </div>
  </section>
"""

DERGI = """
  <!-- Dergi kapağı (LunaDream "Neler yapabiliyor?" dili, kullanıcı 22 Eki seçti): dev tek kelime, arkada o adımın gerçek karesi -->
  <section class="bolum px" id="nasil">
    <h2 class="bas-y h2">Dört kelimede<br>yılbaşı<span class="n">.</span></h2>
    <div class="dg"><sc-for list="{{dg}}" as="d" hint-placeholder-count="2"><img class="{{d.cls}}" src="{{d.src}}" alt=""></sc-for>
      <p class="dg-k" aria-live="polite"><span>{{dgK}}<em>.</em></span></p><p class="dg-t">{{dgT}}</p></div>
    <div class="dg-s" role="tablist"><sc-for list="{{dg}}" as="d" hint-placeholder-count="4"><button class="{{d.bcls}}" type="button" role="tab" aria-selected="{{d.on}}" onClick="{{d.pick}}">{{d.k}}</button></sc-for></div>
    <p class="alt-b" style="margin-top: 12px; font-size: 13px">Kurulum videosu kutudaki QR kodda.</p>
  </section>
"""

HEDIYE = """
  <!-- Kime hediye? (hediye rehberi; ürün bilgisine dayalı, iddia yok) -->
  <section class="bolum" id="hediye">
    <div class="px"><h2 class="bas-y h2">Kime<br>hediye<span class="n">?</span></h2><p class="alt-b">Kutusuyla hazır; açması da kurması da hediye.</p></div>
    <div class="hd noscroll">
      <div class="hd-k y"><span class="hd-g" style="background-image: url(@@yb-d-kar@@)" aria-hidden="true"></span><span class="hd-y"><b>Çocuğuna</b><span>Ağacı birlikte kurun; yatmadan tavana kar taneleri.</span></span></div>
      <div class="hd-k k"><span class="hd-g" style="background-image: url(@@yb-d-mesaj@@)" aria-hidden="true"></span><span class="hd-y"><b>Sevdiğine</b><span>Yeni yıl mesajlı diskle tavana "Merry Christmas".</span></span></div>
      <div class="hd-k a"><span class="hd-g" style="background-image: url(@@yb-adim3@@)" aria-hidden="true"></span><span class="hd-y"><b>Anneannene</b><span>Torunla bir akşam etkinliği; sonra komodinde süs.</span></span></div>
      <div class="hd-k l"><span class="hd-g" style="background-image: url(@@yb-kare@@)" aria-hidden="true"></span><span class="hd-y"><b>Kendine</b><span>Masanda minik ağaç; USB’ye tak, oda yılbaşı olsun.</span></span></div>
      <span aria-hidden="true" style="flex: 0 0 6px"></span>
    </div>
  </section>
"""

TAKVIM = """
  <!-- Takvim yaprağı: yılbaşından önce teslim için son sipariş günü (1 iş gününde kargo + en geç 7 gün; sayaç değil) -->
  <section class="koyu bolum px" id="takvim">
    <div class="tkv"><div class="tkv-y" aria-hidden="true"><b>{{tkAy}}</b><strong>{{tkGun}}</strong><small>{{tkHafta}}</small></div>
      <div class="tkv-m"><b>{{tkBas}}</b><span>{{tkAlt}}</span><button class="btn1" type="button" onClick="{{alaGit}}"><span class="b-ic"><span>Şimdi sipariş ver</span></span>""" + U.OK + """</button></div></div>
  </section>
"""


DIZI = '''<div class="dizi" aria-hidden="true"><svg viewBox="0 0 390 34" preserveAspectRatio="none"><path class="tel" d="M0 6 Q48 26 97 8 T195 8 T292 8 T390 6"></path><circle class="hale" cx="24" cy="15" r="8"></circle><circle class="amp" cx="24" cy="15" r="4" fill="#F3C978"></circle><circle class="hale" cx="58" cy="19" r="8"></circle><circle class="amp" cx="58" cy="19" r="4" fill="#FFE2A8"></circle><circle class="hale" cx="97" cy="10" r="8"></circle><circle class="amp" cx="97" cy="10" r="4" fill="#F3C978"></circle><circle class="hale" cx="136" cy="16" r="8"></circle><circle class="amp" cx="136" cy="16" r="4" fill="#F3C978"></circle><circle class="hale" cx="175" cy="11" r="8"></circle><circle class="amp" cx="175" cy="11" r="4" fill="#FFE2A8"></circle><circle class="hale" cx="214" cy="11" r="8"></circle><circle class="amp" cx="214" cy="11" r="4" fill="#F3C978"></circle><circle class="hale" cx="253" cy="16" r="8"></circle><circle class="amp" cx="253" cy="16" r="4" fill="#F3C978"></circle><circle class="hale" cx="292" cy="10" r="8"></circle><circle class="amp" cx="292" cy="10" r="4" fill="#FFE2A8"></circle><circle class="hale" cx="331" cy="16" r="8"></circle><circle class="amp" cx="331" cy="16" r="4" fill="#F3C978"></circle><circle class="hale" cx="366" cy="12" r="8"></circle><circle class="amp" cx="366" cy="12" r="4" fill="#F3C978"></circle></svg></div>'''


VIDEO = """
  <!-- Videolar (28 Eki, kullanıcı: "ürün videolarını da koyalım, videosuz güven unsuru azalıyor"): LunaDream'deki video şeridi.
       Temada ayrı bölüm (ay-videolar): her kartın video seçicisi var; video seçilmemişse kapak fotoğrafı görünür (bölüm hep görünür).
       Ürünün Shopify videoları da buraya gelir. Ekrandayken sessiz döner; dokununca sesli, tam ekran. -->
  <section class="bolum" id="videolar">
    <div class="px"><h2 class="bas-y h2">Kutudan tavana<br>nasıl görünüyor<span class="n">?</span></h2><p class="alt-b">Kurulumu da ışığı da kendi gözünle gör.</p></div>
    <div class="noscroll" style="display: flex; gap: 10px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-left: 16px; padding: 16px 16px 0">
      <sc-for list="{{vids}}" as="v" hint-placeholder-count="4"><button class="vid ay-vid" type="button" aria-label="{{v.al}}"><sc-if value="{{v.gercek}}" hint-placeholder-val="{{false}}"><video src="{{v.vsrc}}" poster="{{v.src}}" muted loop playsinline preload="metadata"></video></sc-if><sc-if value="{{v.kapak}}" hint-placeholder-val="{{true}}"><img src="{{v.src}}" alt="" style="object-position: {{v.pos}}"></sc-if><span class="vid-oyna" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l11-6.5z"></path></svg></span><span class="vid-alt"><b>{{v.t}}</b><span>{{v.k}}</span></span></button></sc-for>
      <span aria-hidden="true" style="flex: 0 0 6px"></span>
    </div>
  </section>
"""


def govde():
    h = ('<div class="pg">\n  ' + U.SERIT + hero() + al() + YAK + gece() + kutuda() + VIDEO + DIZI + DERGI + HEDIYE + gerisi() + '</div>\n')
    return re.sub(r'@@([\w-]+)@@', lambda m: I(m.group(1)), h)


def faq():
    return [{'q': q, 'a': a} for q, a in US.sorular(OS.ICERIK[H])[1]]


def js():
    gal = [[B + i, '%s görseli %d' % (AD, k + 1), '50% 50%'] for k, i in enumerate(canli_galeri(H))]
    disk = [[n, I(k)] for n, k in DISK]
    parca = [[n, a] for n, a, _, _ in PARCA]
    dg = [['Sar', 'Tüylü çubukları USB kablonun etrafına sar.', I('yb-adim1')], ['Süsle', 'Desenli çıkartmayı altın abajura giydir; inciler senden.', I('yb-adim3')],
          ['Tak', 'Abajuru tak, USB’ye bağla.', I('yb-adim4')], ['Yansıt', 'Işığı kapat: tavan yılbaşı olur.', I('yb-tavan')]]
    BA = OS.BA
    PR = [('lunadream-gece-lambasi', 'LunaDream Gece Lambası', 1699.99, 1999), ('galayx-usb-projektor', 'Galaxy USB Projektör', 1599, 1999),
          ('lamba', 'Ayluna AyFeneri', 1649.99, 2499), ('ayluna-galaksi-night-projektor', 'Ayluna Galaksi Night Projektör', 2199, 2999),
          ('galaksiambiyanisigi', 'Galaksi Ambiyans Işığı', 1499, 2898), ('ask-saati', 'Ayluna Kum Saati Lamba', 799, 999)]
    shop = [[n, p, c, B + BA['u-%s.jpg' % h]] for h, n, p, c in PR]
    nk = ''.join("nk%d: S.nk === %d ? 'on' : '', nkOn%d: S.nk === %d ? 'true' : 'false', nkSec%d: function () { self.setState({ nk: %d }); },\n      " % (i, i, i, i, i, i) for i in range(len(PARCA)))
    return """class Component extends DCLogic {
  constructor(p) { super(p); this.state = { ser: 0, g: 0, gOto: true, adet: null, disk: 0, dOto: true, nk: 1, yak: true, yOto: true, yBas: 0, dg: 0, dgOto: true, t: 0, dn: 0, dnT: 0, now: Date.now() }; }
  componentDidMount() {
    var self = this;
    this.azHareket = !!(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches);
    if (this.azHareket) this.setState({ dOto: false, yOto: false, yak: true, dgOto: false });
    // Tek saat: şerit sayacı, galeri (5 sn), disk (4 sn)
    this.iv = setInterval(function () {
      var S = self.state, t = S.t + 1, o = { now: Date.now(), t: t };
      if (S.gOto && t % 5 === 0) self.galGit((S.g + 1) % (self.galN || """ + str(len(gal)) + """));
      if (S.dOto && t % 4 === 0) o.disk = (S.disk + 1) % """ + str(len(DISK)) + """;
      if (S.yOto && t - S.yBas >= (S.yak ? 7 : 2)) { o.yak = !S.yak; o.yBas = t; }
      if (S.dgOto && t % 3 === 0) o.dg = (S.dg + 1) % 4;
      if (!self.azHareket && t % 3 === 0) o.ser = S.ser + 1;
      if (!self.azHareket && t - S.dnT >= (S.dn ? 6 : 4)) { o.dn = 1 - S.dn; o.dnT = t; }
      var azH = self.azHareket;
""" + tk_adim('t', 1) + """
      self.setState(o);
    }, 1000);
  }
  galGit(i) { var el = document.querySelector('.h-iz'); if (el && el.scrollTo && el.clientWidth) { this.otoKay = Date.now(); el.scrollTo({ left: i * el.clientWidth, behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); } else this.setState({ g: i }); }
  componentDidUpdate() { var el = document.querySelector('.h-iz'); if (el && el.clientWidth && Math.abs(el.scrollLeft - this.state.g * el.clientWidth) > el.clientWidth / 2) { this.otoKay = Date.now(); el.scrollLeft = this.state.g * el.clientWidth; } }
  componentWillUnmount() { clearInterval(this.iv); }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    """ + TL_JS + """
    var MEDYA = (window.Ayluna && Ayluna.medya) ? Ayluna.medya() : null, GAL = MEDYA ? MEDYA.map(function (m) { return [m.src, m.alt, '50% 50%']; }) : """ + json.dumps(gal, ensure_ascii=False) + """;
    self.galN = GAL.length;
    var gal = GAL.map(function (g, i) { var on = i === S.g; return { src: g[0], n: g[1], pos: g[2], cls: 'hs' + (on ? ' on' : ''), dcls: i < S.g ? 'lit' : (on ? 'lit on' : '') }; });
    function gKay(e) { var el = e && (e.currentTarget || e.target); if (!el || !el.clientWidth) return; var i = Math.round(el.scrollLeft / el.clientWidth), o = {};
      if (i !== self.state.g) o.g = i; if (self.state.gOto && Date.now() - (self.otoKay || 0) > 900) o.gOto = false; if (o.g !== undefined || o.gOto === false) self.setState(o); }
    // Fiyat: Shopify'da canlı fiyat (V.urun), tuvalde geçici fiyat. 2 adette indirim tanımlı değil: tasarruf yazılmaz.
    var VU = ((window.AYLUNA_VERI || {}).urun || {})[""" + json.dumps(H) + """] || {}, P1 = VU.p || """ + str(P1) + """;
    var C1v = VU.c > P1 ? VU.c : null, fyPct = C1v ? Math.round((1 - P1 / C1v) * 100) : 0;
    var paket = [
      { n: 1, t: '1 Adet', p: TL(P1, true), old: C1v ? TL(C1v, true) : '', sub: C1v ? '%' + fyPct + ' indirim' : 'Kendine ya da evine', rib: false },
      { n: 2, t: '2 Adet', p: TL(2 * P1, true), old: C1v ? TL(2 * C1v, true) : '', sub: 'Biri sana, biri hediye', rib: false }
    ].map(function (b) { var on = S.adet === b.n; return { t: b.t, p: b.p, old: b.old, hasOld: !!b.old, sub: b.sub, rib: b.rib, two: b.n === 2, on: on ? 'true' : 'false', cls: on ? 'pk-k on' : 'pk-k', pick: function () { self.setState({ adet: b.n }); } }; });
    var DISK = """ + json.dumps(disk, ensure_ascii=False) + """;
    var disk = DISK.map(function (d, i) { var on = i === S.disk; return { n: d[0], src: d[1], on: on ? 'true' : 'false', cls: on ? 'on' : '', bcls: on ? 'on' : '', pick: function () { self.setState({ disk: i, dOto: false }); } }; });
    var VID = (window.Ayluna && Ayluna.videolar) ? Ayluna.videolar() : null;
    var vids = VID && VID.length ? VID.map(function (v) { return { t: v.alt || 'Yılbaşı Ağacı videosu', k: 'Dokun, sesli izle', al: (v.alt || 'Yılbaşı Ağacı videosu') + ': videoyu oynat', src: v.poster || '', vsrc: v.src, pos: '50% 50%', gercek: true, kapak: false }; }) : [
      { t: 'Kutudan çıkanlar', al: 'Kutudan çıkanlar', k: 'Kutu açılışı', src: B + '""" + OS.BL['yb-kutu'] + """', pos: '50% 40%', gercek: false, kapak: true },
      { t: 'Ağacı sarmak', al: 'Ağacı sarmak', k: 'Kurulum', src: B + '""" + OS.BL['yb-adim1'] + """', pos: '50% 50%', gercek: false, kapak: true },
      { t: 'Abajuru giydirmek', al: 'Abajuru giydirmek', k: 'Süsleme', src: B + '""" + OS.BL['yb-adim3'] + """', pos: '50% 50%', gercek: false, kapak: true },
      { t: 'Işık kapanınca tavan', al: 'Işık kapanınca tavan', k: 'Tavanda yılbaşı', src: B + '""" + OS.BL['yb-tavan'] + """', pos: '50% 30%', gercek: false, kapak: true }];
    var PARCA = """ + json.dumps(parca, ensure_ascii=False) + """;
    var DG = """ + json.dumps(dg, ensure_ascii=False) + """, GUNA = ['Pazar', 'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi'];
    var AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'], AYU = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
    var now = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    """ + KARGO_JS + """
    var KG = KARGO(S.now || Date.now()), kd = new Date(KG.gun);
    var t1 = new Date(kd); t1.setDate(t1.getDate() + 3); var t2 = new Date(kd); t2.setDate(t2.getDate() + 7);
    var teslim = t1.getMonth() === t2.getMonth() ? t1.getDate() + '–' + t2.getDate() + ' ' + AY[t2.getMonth()] : t1.getDate() + ' ' + AY[t1.getMonth()] + '–' + t2.getDate() + ' ' + AY[t2.getMonth()];
    // Yılbaşından önce teslim için son sipariş: 31 Aralık'tan 7 gün teslim + 1 iş günü kargo geriye; hafta sonu atlanır
    var g0 = new Date(now.getFullYear(), now.getMonth(), now.getDate()), yil = now.getMonth() === 0 && now.getDate() < 7 ? null : new Date(now.getFullYear(), 11, 31);
    var son = yil ? new Date(yil.getFullYear(), 11, 23) : null; if (son) while (son.getDay() === 0 || son.getDay() === 6) son.setDate(son.getDate() - 1);
    var gunYil = yil ? Math.round((yil - g0) / 864e5) : 0, yetisir = son && g0 <= son;
    var ybCls = yetisir ? 'yb-k' : 'yb-k gecti', ybGun = yetisir ? String(gunYil) : '', ybGunEt = yetisir ? 'gün' : '';
    var ybBas = yetisir ? 'Yılbaşından önce kapında' : 'Yılbaşına yetişmeyebilir', ybAlt = yetisir ? ('Yılbaşına ' + gunYil + ' gün var. Yılbaşından önce teslim için son sipariş: ' + son.getDate() + ' ' + AYU[son.getMonth()] + '.') : ('Tahmini teslim: ' + teslim + '.');
    function IKI(n) { return n < 10 ? '0' + n : String(n); }
    // Ay sonu (İstanbul saatiyle) ve gerçek ürün alanları (Shopify: AYLUNA_CANLI; tuvalde yok → satır yok)
    var aySon = new Date(now.getFullYear(), now.getMonth() + 1, 1), ayBas = new Date(now.getFullYear(), now.getMonth(), 1), istS = new Date(new Date(S.now || Date.now()).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kalanDk = Math.max(0, Math.floor((aySon - istS) / 60000)), aysGun = Math.floor(kalanDk / 1440), aysSa = Math.floor(kalanDk / 60) % 24, aysOran = Math.min(1, (istS - ayBas) / (aySon - ayBas));
    var CN = (window.AYLUNA_CANLI || {})[""" + json.dumps(H) + """] || {}, stokN = +CN.kd > 0 ? +CN.kd : 0, dunN = +CN.dun > 0 ? +CN.dun : 0;
    var SER = (dunN ? ['Dün ' + dunN + ' kişi satın aldı'] : []).concat(['Ücretsiz kargo, 1 iş gününde kargoda', '30 gün iade hakkı', 'Kapıda ödeme de var', 'Yılbaşı baskılı hediye kutusunda']);
    var serI = S.ser % (SER.length + 1); if (serI === SER.length && !self.serSifir) { self.serSifir = setTimeout(function () { self.serSifir = null; self.setState({ ser: 0 }); }, 520); }
    var ist = new Date(new Date(S.now || Date.now()).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
    var kalan = Math.max(0, new Date(ist.getFullYear(), ist.getMonth(), ist.getDate(), 23, 59, 59, 999).getTime() - ist.getTime());
    var hh = Math.floor(kalan / 3600000), mi = Math.floor(kalan / 60000) % 60, ss = Math.floor(kalan / 1000) % 60;
    function AYY(f) { var r = 9, c = 12, rx = Math.abs(1 - 2 * f) * r; return 'M' + c + ' ' + (c - r) + 'A' + r + ' ' + r + ' 0 0 1 ' + c + ' ' + (c + r) + 'A' + rx.toFixed(2) + ' ' + r + ' 0 0 ' + (f < .5 ? 0 : 1) + ' ' + c + ' ' + (c - r) + 'Z'; }
    function alaGit() { var h = document.getElementById('siparis'); if (h && h.scrollIntoView) h.scrollIntoView({ behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' }); }
""" + KAY_JS + """    var PR = """ + json.dumps(shop, ensure_ascii=False) + """;
    var shop = PR.map(function (x) { var d = x[2] > x[1]; return { n: x[0], src: x[3], price: TL(x[1], true), old: d ? TL(x[2], true) : '', pct: d ? '%' + Math.round((1 - x[1] / x[2]) * 100) : '' }; });
    return {
      gal: gal, gNo: S.g + 1, gCount: GAL.length, gKay: gKay, paket: paket, adetName: S.adet === 2 ? '2 Adet' : '1 Adet',
      """ + TK_DEGER + """
      tk0a: dunN ? 'Dün ' : '', tk0b: dunN ? dunN + ' kişi' : 'Kapıda ödeme', tk0c: dunN ? ' satın aldı' : ' de var',
      tkSr: (dunN ? 'Dün ' + dunN + ' kişi satın aldı. ' : 'Kapıda ödeme de var. ') + 'Ücretsiz kargo ile kapına. 30 gün iade hakkı. Hediye kutusunda, süsleriyle.',
      fySr: 'Fiyat ' + TL(P1, true) + (C1v ? ', önceki fiyat ' + TL(C1v, true) + ', %' + fyPct + ' indirim' : ''),
      onLabel: 'Güvenli Ödeme ile Al', fyP: TL(P1, true), fyInd: !!C1v, fyC: C1v ? TL(C1v, true) : '', fyPct: fyPct,
      kgMetin: KG.metin, kgBugun: KG.bugun, kgSayac: KG.sayac, cdTiny: IKI(hh) + ' sa ' + IKI(mi) + ' dk kaldı',
      dnA: 'dn-s' + (S.dn === 0 ? ' on' : S.t - S.dnT < 1 ? ' ust' : ''), dnB: 'dn-s' + (S.dn === 1 ? ' on' : S.t - S.dnT < 1 ? ' ust' : ''), kargo: kd.getDate() + ' ' + AY[kd.getMonth()], teslim: teslim,
      ybCls: ybCls, ybGun: ybGun, ybGunEt: ybGunEt, ybBas: ybBas, ybAlt: ybAlt,
      hh: IKI(hh), mm: IKI(mi), ss: IKI(ss), snCls: ss % 2 ? 'sn tA' : 'sn tB', cdAria: 'Bugünkü fiyat garantisinin bitmesine ' + hh + ' saat ' + mi + ' dakika', cdAy: AYY(Math.round(kalan / 864000) / 100),
      disk: disk, dAd: DISK[S.disk][0],
      yakCls: S.yak ? 'yak on' : 'yak', yakOn: S.yak ? 'true' : 'false', yakEt: S.yak ? 'Açık' : 'Kapalı', yakYazi: S.yak ? 'Tavan yılbaşı oldu.' : 'Işığı kapat, ağacı yak.',
      yakAlt: S.yak ? 'Desenler tavanda; diski değiştirince değişir.' : 'Lamba kapalı. Dokun, yansısın.', yakSw: function () { self.setState({ yak: !self.state.yak, yOto: false }); },
      dg: DG.map(function (d, i) { var on = i === S.dg; return { k: d[0], src: d[2], cls: on ? 'on' : '', bcls: on ? 'on' : '', on: on ? 'true' : 'false', pick: function () { self.setState({ dg: i, dgOto: false }); } }; }),
      dgK: DG[S.dg][0], dgT: DG[S.dg][1],
      tkAy: son ? AYU[son.getMonth()].toLocaleUpperCase('tr') : AYU[t2.getMonth()].toLocaleUpperCase('tr'), tkGun: son ? String(son.getDate()) : String(t2.getDate()), tkHafta: son ? GUNA[son.getDay()] : 'tahmini teslim',
      tkBas: yetisir ? 'Yılbaşından önce kapında olması için son sipariş günü.' : 'Bu yıl yılbaşına yetişmeyebilir.', tkAlt: yetisir ? ('Yılbaşına ' + gunYil + ' gün var. Bugün verirsen ' + kd.getDate() + ' ' + AYU[kd.getMonth()] + ' kargoda.') : ('Tahmini teslim: ' + teslim + '.'),
      ser: SER.concat([SER[0]]).map(function (t) { return { t: t }; }), serY: -24 * serI, serCls: serI === 0 ? 'ser-iz anlik' : 'ser-iz',
      aysYol: AYY(1 - aysOran), aysBas: AYU[now.getMonth()] + ' fiyatı bitiyor', aysAlt: 'Fiyatlar her ay güncelleniyor; bu fiyat ay sonuna kadar.', aysG: String(aysGun), aysS: String(aysSa), aysAria: AYU[now.getMonth()] + ' fiyatının bitmesine ' + aysGun + ' gün ' + aysSa + ' saat',
      vids: vids, aysAy: AYU[now.getMonth()], stokVar: stokN > 0, stokN: stokN,
      nkNo: S.nk + 1, nkAd: PARCA[S.nk][0], nkAlt: PARCA[S.nk][1],
      """ + nk + """alaGit: alaGit, faq: """ + json.dumps(faq(), ensure_ascii=False) + """, kayGeri: KAY(-1), kayIleri: KAY(1), shop: shop, shopCount: PR.length
    };
  }
}"""


DOSYA = 'YilbasiAgaci.dc.html'


def sayfa():
    css = O.tema_css(dict(TEMA, ek='')) + U.CSS + O.CSS + '\n' + OS.CSS + CSS + US.URS_CSS + SERIT_OK_CSS + MESAJ_CSS + tk_css('#123A2A', '#2F6B45', '#2E9E62', '1.2s') + UST_CSS
    return U.head(AD, css, TEMA['font']) + govde()


if __name__ == '__main__':
    h = int(os.environ.get('S_H', 6200))
    open(os.path.join(CANVAS, DOSYA), 'w', encoding='utf-8').write(urun_ust(sayfa(), '<section class="hero kare"') + TAIL.format(h=h, js=masa_bayrak(mesaj_js(js()))))
    print('yazıldı:', DOSYA, h)
