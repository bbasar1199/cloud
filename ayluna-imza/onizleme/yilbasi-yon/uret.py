# Yılbaşı Ağacı Projektör Lamba · 3 yön taslağı (28 Eki). Telefon 390 px. Fiyat bilinmiyor: [fiyat].
import os
D = os.path.dirname(os.path.abspath(__file__))

ORTAK = """
*{box-sizing:border-box}body{margin:0;background:var(--zemin);color:var(--yazi);font-family:var(--fg),system-ui,sans-serif;font-size:15px;line-height:1.5;-webkit-font-smoothing:antialiased}
.pg{width:390px;margin:0 auto;overflow:hidden}
.bant{display:flex;justify-content:center;gap:6px;padding:8px 12px;background:var(--lac);color:#F5F3EF;font-size:12px;font-weight:600}
.ust{display:flex;align-items:center;justify-content:space-between;height:52px;padding:0 16px;background:var(--zemin);border-bottom:1px solid var(--cizgi)}
.ust b{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:21px;color:var(--lac)}
.ust i{width:22px;height:2px;background:var(--lac);box-shadow:0 6px 0 var(--lac),0 -6px 0 var(--lac)}
.bas{font-family:var(--fb);font-weight:var(--bk);letter-spacing:var(--bls);margin:0;line-height:1}
.fiyat{display:flex;align-items:baseline;gap:10px;margin:14px 0 0;font-variant-numeric:tabular-nums}
.fiyat b{font-size:24px}.fiyat s{color:var(--soluk);font-size:14px}
.btn{display:flex;align-items:center;justify-content:center;gap:10px;width:100%;min-height:52px;margin-top:14px;border:0;border-radius:14px;background:var(--btn);color:#fff;font:inherit;font-size:16px;font-weight:700}
.btn small{display:block;font-size:12px;font-weight:600;opacity:.8}
.yb{display:grid;grid-template-columns:auto 1fr;gap:12px;align-items:center;margin:14px 0 0;padding:12px 14px;border-radius:14px;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi);font-size:13px}
.yb .g{display:grid;place-items:center;width:48px;height:48px;border-radius:12px;background:var(--vurgu);color:#fff;font-weight:800;font-size:18px;line-height:1;text-align:center}
.yb .g small{display:block;font-size:10px;font-weight:700;letter-spacing:.02em}
.yb b{display:block;font-size:14px}
.guv{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:14px 0 0;font-size:12px;color:var(--soluk);text-align:center}
.guv span{padding:10px 4px;border-radius:12px;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi)}
.etk{display:inline-block;padding:3px 10px;border-radius:999px;background:var(--vurgu);color:#fff;font-size:12px;font-weight:700}
.blk{padding:28px 16px 0}
.blk h2{margin:0 0 6px;font-family:var(--fb);font-weight:var(--bk);letter-spacing:var(--bls);font-size:30px;line-height:1.05}
.blk p.alt{margin:0 0 14px;color:var(--soluk)}
"""

TESLIM = """<div class="yb"><span class="g" id="gun">--<small>GÜN</small></span><span><b>Yılbaşından önce kapında</b>Yılbaşına <span id="gk">--</span> gün var. Yılbaşından önce teslim için son sipariş <b style="display:inline" id="son">--</b>.</span></div>"""
TESLIM_JS = """
(function(){var n=new Date(),y=new Date(n.getFullYear(),11,31),gun=Math.ceil((y-n)/864e5);
// son sipariş: 1 iş gününde kargo + en geç 7 gün; 31 Aralık'tan geriye
var s=new Date(n.getFullYear(),11,31-7-1);while(s.getDay()===0||s.getDay()===6)s.setDate(s.getDate()-1);
var AY=['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık'];
document.querySelectorAll('#gun').forEach(function(e){e.firstChild.nodeValue=gun});document.querySelectorAll('#gk').forEach(function(e){e.textContent=gun});
document.querySelectorAll('#son').forEach(function(e){e.textContent=s.getDate()+' '+AY[s.getMonth()]});})();
"""

def sayfa(ad, kok, css, govde, js=''):
    html = ('<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?%s&family=Young+Serif&display=swap"><style>:root{%s}%s%s</style></head>'
            '<body><div class="pg">%s</div><script>%s%s</script></body></html>') % (kok['font'], ';'.join('--%s:%s' % kv for kv in kok['v'].items()), ORTAK, css, govde, TESLIM_JS, js)
    open(os.path.join(D, ad), 'w', encoding='utf-8').write(html)

# ---------- A · Hediye kutusu ----------
A_KOK = dict(font='family=Instrument+Serif:ital@0;1&family=Figtree:wght@400;500;600;700;800',
             v={'zemin': '#F6F0E7', 'kart': '#FFFCF7', 'cizgi': '#E6DACA', 'yazi': '#1A2142', 'soluk': '#5E6070', 'lac': '#1F4D36', 'btn': '#1F4D36',
                'vurgu': '#B23A2E', 'fb': '"Instrument Serif"', 'fg': '"Figtree"', 'bk': '400', 'bls': '-.01em'})
NOKTA = [('Hediye kutusu', 'Yılbaşı baskılı, kağıt dolgulu', 52, 18), ('Altın abajur', 'Desenli çıkartmayı giydirirsin', 36, 43),
         ('Desenli çıkartma', 'Abajura sarılır', 77, 48), ('İnci çıkartmalar', 'Kırmızı ve altın, kendinden yapışkanlı', 60, 60),
         ('Tüylü çubuklar', 'Kabloya sarılıp ağaç olur', 83, 77), ('Projektör ve diskler', 'USB kablolu, lensli; değiştirilebilir desenler', 36, 85),
         ('"Merry Christmas" çıkartması', 'Ağacın süsü', 63, 70), ('Montaj kartı', 'QR kodunda montaj videosu', 22, 52)]
A_CSS = """
.hero{position:relative}
.hero img{display:block;width:100%;aspect-ratio:3/4;object-fit:cover}
.hero .yz{position:absolute;left:0;right:0;bottom:0;padding:90px 16px 18px;background:linear-gradient(to top,rgba(20,24,20,.82),rgba(20,24,20,0));color:#fff}
.hero .bas{font-size:44px;line-height:.98}.hero .bas em{font-style:italic;color:#F2C46B}
.hero p{margin:8px 0 0;font-size:15px;color:#EDE6DA}
.al{padding:16px}
.al h1{margin:0;font-family:var(--fg);font-size:18px;font-weight:700;color:var(--yazi)}
.kut{position:relative;border-radius:18px;overflow:hidden}
.kut img{display:block;width:100%}
.kut button{position:absolute;width:30px;height:30px;margin:-15px 0 0 -15px;border:0;border-radius:50%;background:#fff;box-shadow:0 0 0 3px rgba(178,58,46,.9),0 4px 10px rgba(0,0,0,.25);color:var(--vurgu);font:800 13px var(--fg)}
.kut button.on{background:var(--vurgu);color:#fff;transform:scale(1.15)}
.kut button::after{content:"";position:absolute;inset:-9px}
.kl{margin:12px 0 0;padding:12px 14px;border-radius:14px;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi)}
.kl b{display:block;font-size:15px}.kl span{color:var(--soluk);font-size:13px}
.say{margin:8px 0 0;font-size:12px;color:var(--soluk)}
"""
A_GOV = ('<p class="bant">Ücretsiz kargo · 30 gün iade · Kapıda ödeme</p><div class="ust"><b>Ayluna</b><i></i></div>'
         '<div class="hero"><img src="g/kutu-tam.jpg" alt="Kutu içeriği"><div class="yz"><p class="etk" style="margin:0 0 10px">Yılbaşı hediyesi</p>'
         '<h2 class="bas">Açması da kurması da <em>hediye.</em></h2><p>Kutudan bir yılbaşı ağacı çıkıyor; sen süslüyorsun, tavana yılbaşı yansıtıyor.</p></div></div>'
         '<div class="al"><h1>Yılbaşı Ağacı Projektör Lamba</h1><p class="fiyat"><b>₺[fiyat]</b><s>₺[eski]</s></p>'
         '<button class="btn"><span>Güvenli Ödeme ile Al</span></button>' + TESLIM +
         '<div class="guv"><span>Hediye kutusunda</span><span>USB ile çalışır</span><span>30 gün iade</span></div></div>'
         '<section class="blk"><h2>Kutuda ne var?</h2><p class="alt">Fotoğraftaki numaralara dokun.</p><div class="kut"><img src="g/kutu-tam.jpg" alt="">'
         + ''.join('<button style="left:%d%%;top:%d%%" data-i="%d"%s>%d</button>' % (x, y, i, ' class="on"' if i == 1 else '', i + 1) for i, (_, _, x, y) in enumerate(NOKTA)) +
         '</div><div class="kl" id="kl"><b>%s</b><span>%s</span></div><p class="say">8 parça · USB adaptör kutuda yok</p></section><div style="height:28px"></div>' % NOKTA[1][:2])
A_JS = "var N=%s;document.querySelectorAll('.kut button').forEach(function(b){b.onclick=function(){document.querySelectorAll('.kut button').forEach(function(x){x.classList.remove('on')});b.classList.add('on');var n=N[+b.dataset.i];document.getElementById('kl').innerHTML='<b>'+n[0]+'</b><span>'+n[1]+'</span>';}});" % [list(n[:2]) for n in NOKTA]
sayfa('A-hediye-kutusu.html', A_KOK, A_CSS, A_GOV, A_JS)

# ---------- B · Tavan ----------
B_KOK = dict(font='family=Sora:wght@500;600;700&family=Manrope:wght@400;500;600;700;800',
             v={'zemin': '#0E1220', 'kart': '#161B2E', 'cizgi': '#262D47', 'yazi': '#F3F1EC', 'soluk': '#A9AEC6', 'lac': '#1A2142', 'btn': '#C8342B',
                'vurgu': '#2E8B57', 'fb': '"Sora"', 'fg': '"Manrope"', 'bk': '700', 'bls': '-.03em'})
DISK = [('klasik', 'Klasik yılbaşı'), ('mesaj', 'Yeni yıl mesajı'), ('kar', 'Kar taneleri'), ('geyik', 'Ren geyikleri'), ('kardan', 'Kardan adam'), ('can', 'Çanlar')]
B_CSS = """
.ust{background:var(--zemin)}.ust b{color:#F3F1EC}.ust i{background:#F3F1EC;box-shadow:0 6px 0 #F3F1EC,0 -6px 0 #F3F1EC}
.bant{background:#C8342B}
.hero{position:relative;height:560px;overflow:hidden}
.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero .yz{position:absolute;left:16px;right:16px;top:22px}
.hero .bas{font-size:40px;text-shadow:0 2px 18px rgba(0,0,0,.6)}
.hero .anahtar{position:absolute;left:16px;bottom:18px;display:flex;align-items:center;gap:10px;padding:8px 14px 8px 8px;border-radius:999px;background:rgba(14,18,32,.72);color:#fff;font-weight:700;font-size:14px;border:0}
.hero .anahtar i{width:40px;height:24px;border-radius:999px;background:#2E8B57;position:relative}.hero .anahtar i::after{content:"";position:absolute;right:3px;top:3px;width:18px;height:18px;border-radius:50%;background:#fff}
.al{padding:16px}.al h1{margin:0;font-size:18px;font-weight:700}
.tav{position:relative;width:300px;height:300px;margin:0 auto;border-radius:50%;overflow:hidden;box-shadow:0 0 0 6px #161B2E,0 0 60px rgba(242,180,90,.25)}
.tav img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .45s cubic-bezier(.2,.7,.2,1),transform .6s cubic-bezier(.2,.7,.2,1)}
.tav img.gizli{opacity:0;transform:rotate(-12deg) scale(1.08)}
.dk{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:18px 0 0}
.dk button{display:flex;flex-direction:column;align-items:center;gap:6px;padding:8px 4px;border:0;border-radius:14px;background:var(--kart);color:var(--yazi);font:600 12px var(--fg);box-shadow:inset 0 0 0 1px var(--cizgi)}
.dk button img{width:52px;height:52px;border-radius:50%;object-fit:cover}
.dk button.on{box-shadow:inset 0 0 0 2px #F2B45A}
.not{margin:12px 0 0;font-size:12px;color:var(--soluk);text-align:center}
"""
B_GOV = ('<p class="bant">Yılbaşı koleksiyonu · Ücretsiz kargo · Kapıda ödeme</p><div class="ust"><b>Ayluna</b><i></i></div>'
         '<div class="hero"><img src="g/tavan-dik.jpg" alt="Tavanda yılbaşı desenleri"><div class="yz"><h2 class="bas">Işığı kapat.<br>Yılbaşı tavanda.</h2></div>'
         '<button class="anahtar"><i></i>Işık kapalı · desen açık</button></div>'
         '<div class="al"><h1>Yılbaşı Ağacı Projektör Lamba</h1><p class="fiyat"><b>₺[fiyat]</b><s>₺[eski]</s></p>'
         '<button class="btn">Güvenli Ödeme ile Al</button>' + TESLIM + '<div class="guv"><span>6 yılbaşı deseni</span><span>USB ile çalışır</span><span>30 gün iade</span></div></div>'
         '<section class="blk"><h2>Bu gece hangisi?</h2><p class="alt">Diski değiştir, tavan değişsin.</p><div class="tav">'
         + ''.join('<img src="g/%s.jpg" alt="%s" data-k="%s"%s>' % (k, a, k, '' if i == 0 else ' class="gizli"') for i, (k, a) in enumerate(DISK)) +
         '</div><div class="dk">' + ''.join('<button data-k="%s"%s><img src="g/%s.jpg" alt="">%s</button>' % (k, ' class="on"' if i == 0 else '', k, a) for i, (k, a) in enumerate(DISK)) +
         '</div><p class="not">Disk değiştirmek: fişi çek, abajuru kaldır, diski değiştir, abajuru tak.</p></section><div style="height:28px"></div>')
B_JS = "document.querySelectorAll('.dk button').forEach(function(b){b.onclick=function(){document.querySelectorAll('.dk button').forEach(function(x){x.classList.toggle('on',x===b)});document.querySelectorAll('.tav img').forEach(function(i){i.classList.toggle('gizli',i.dataset.k!==b.dataset.k)})}});"
sayfa('B-tavan.html', B_KOK, B_CSS, B_GOV, B_JS)

# ---------- C · Birlikte yap ----------
C_KOK = dict(font='family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;500;600;700;800',
             v={'zemin': '#FFFFFF', 'kart': '#F6F7F4', 'cizgi': '#E4E7E1', 'yazi': '#14231B', 'soluk': '#5B6660', 'lac': '#1E5B3A', 'btn': '#1E5B3A',
                'vurgu': '#C8342B', 'fb': '"Bricolage Grotesque"', 'fg': '"Figtree"', 'bk': '800', 'bls': '-.035em'})
ADIM = [('adim40', 'Sar', 'Tüylü çubukları USB kablonun etrafına sar.'), ('adim68', 'Şekil ver', 'Kabloyu bükerek ağacın gövdesini kur.'),
        ('adim95', 'Giydir', 'Desenli çıkartmayı altın abajura yapıştır.'), ('adim102', 'Tak ve yak', 'Abajuru tak, USB’ye bağla, tavana çevir.')]
C_CSS = """
.hero{padding:18px 16px 0}
.hero .bas{font-size:46px;color:var(--lac)}.hero .bas span{color:var(--vurgu)}
.hero p{margin:10px 0 0;color:var(--soluk)}
.ikili{display:grid;grid-template-columns:1.25fr 1fr;gap:8px;margin:16px 0 0}
.ikili img{display:block;width:100%;height:240px;object-fit:cover;border-radius:16px}
.ikili figure{margin:0;position:relative}.ikili figcaption{position:absolute;left:8px;bottom:8px;padding:3px 9px;border-radius:999px;background:#fff;font-size:12px;font-weight:700}
.al{padding:0 16px}.al h1{margin:16px 0 0;font-size:18px;font-weight:700}
.adm{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;padding:0 16px 4px;scrollbar-width:none}
.adm figure{flex:0 0 230px;margin:0;scroll-snap-align:start;border-radius:16px;background:var(--kart);box-shadow:inset 0 0 0 1px var(--cizgi);overflow:hidden}
.adm img{display:block;width:100%;aspect-ratio:1;object-fit:cover}
.adm figcaption{padding:10px 12px 12px;font-size:13px;color:var(--soluk)}
.adm figcaption b{display:flex;align-items:center;gap:8px;font-size:16px;color:var(--yazi)}
.adm figcaption b i{display:grid;place-items:center;width:24px;height:24px;border-radius:50%;background:var(--lac);color:#fff;font-style:normal;font-size:12px}
.qr{margin:14px 16px 0;padding:12px 14px;border-radius:14px;background:#FFF5F3;color:#7A2A22;font-size:13px}
"""
C_GOV = ('<p class="bant">Ücretsiz kargo · 30 gün iade · Kapıda ödeme</p><div class="ust"><b>Ayluna</b><i></i></div>'
         '<div class="hero"><h2 class="bas">Birlikte yap,<br><span>birlikte yak.</span></h2><p>Kutudan çıkanlarla minik bir yılbaşı ağacı kurarsınız; USB’ye takınca tavana yılbaşı yansır.</p>'
         '<div class="ikili"><figure><img src="g/adim68.jpg" alt=""><figcaption>Yaparken</figcaption></figure><figure><img src="g/klasik.jpg" alt=""><figcaption>Yanınca</figcaption></figure></div></div>'
         '<div class="al"><h1>Yılbaşı Ağacı Projektör Lamba</h1><p class="fiyat"><b>₺[fiyat]</b><s>₺[eski]</s></p><button class="btn">Güvenli Ödeme ile Al</button>' + TESLIM +
         '<div class="guv"><span>Aile etkinliği</span><span>USB ile çalışır</span><span>30 gün iade</span></div></div>'
         '<section class="blk" style="padding-left:0;padding-right:0"><h2 style="padding:0 16px">4 adımda ağaç</h2><p class="alt" style="padding:0 16px">Videodaki gibi; kaydır.</p><div class="adm">'
         + ''.join('<figure><img src="g/%s.jpg" alt=""><figcaption><b><i>%d</i>%s</b>%s</figcaption></figure>' % (f, i + 1, t, a) for i, (f, t, a) in enumerate(ADIM)) +
         '</div><p class="qr">Kutudaki montaj kartının QR kodunda video var. İnci çıkartmalar küçük parça: küçük çocuklar bir yetişkinle yapsın.</p></section><div style="height:28px"></div>')
sayfa('C-birlikte-yap.html', C_KOK, C_CSS, C_GOV)
print('tamam')
