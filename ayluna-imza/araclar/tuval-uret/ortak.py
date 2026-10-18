# Fikir panoları için ortak başlık ve CSS (LunaDreamV2 ile aynı dil)
HEAD = '''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Young+Serif&amp;family=Onest:wght@400;500;600;700&amp;display=swap">
<style>
body{{margin:0;background:#F6F1E9}}
a{{color:#1A2142}}a:hover{{color:#2B3463}}
.pg{{width:390px;background:#F6F1E9;color:#1A2142;font-family:"Onest",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;font-size:16px;line-height:1.5;-webkit-font-smoothing:antialiased;overflow:hidden;position:relative}}
.pg *{{box-sizing:border-box}}
.ser{{font-family:"Young Serif",Georgia,"Times New Roman",serif;font-weight:400;letter-spacing:-.01em}}
.px{{padding-left:16px;padding-right:16px}}
.mut{{color:#5C6078}}
.h2{{font-family:"Young Serif",Georgia,serif;font-weight:400;font-size:30px;line-height:1.06;letter-spacing:-.02em;margin:0;text-wrap:balance}}
.ico{{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;flex:none}}
.btn{{display:flex;align-items:center;justify-content:center;gap:10px;width:100%;min-height:58px;border:0;border-radius:16px;background:#1A2142;color:#FFFDF9;font:inherit;font-size:17px;font-weight:600;cursor:pointer;text-decoration:none;transition:transform .15s cubic-bezier(.2,.7,.2,1)}}
.btn:active{{transform:scale(.985)}}
.etiket{{display:flex;justify-content:space-between;align-items:baseline;font-size:12px;font-weight:600;letter-spacing:.02em;color:#1A2142}}
.etiket>span:first-child{{text-transform:uppercase;letter-spacing:.12em;font-size:12px;color:#766B5B}}
.rozet{{display:inline-block;padding:2px 7px;border-radius:999px;font-size:12px;font-weight:700;letter-spacing:.02em;line-height:1.3;white-space:nowrap}}
.odeme{{display:flex;flex-direction:column;justify-content:center;height:62px;padding:0 12px;border-radius:14px;border:1.5px solid;font:inherit;color:#1A2142;text-align:left;cursor:pointer;transition:border-color .25s,background .25s,transform .2s cubic-bezier(.2,.7,.2,1)}}
.odeme:active{{transform:scale(.98)}}
.not{{margin:0 0 6px;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#766B5B}}
{css}
@media (prefers-reduced-motion:reduce){{.pg *{{transition:none!important;animation:none!important}}}}
</style>
</helmet>
'''
TAIL = '''</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":390,"height":{h}}}}}'>
{js}
</script>
</body>
</html>
'''
TL_JS = "function TL(n, kurus) { var s = (kurus ? n.toFixed(2) : String(Math.round(n))).split('.'); return '₺' + s[0].replace(/\\B(?=(\\d{3})+(?!\\d))/g, '.') + (kurus ? ',' + s[1] : ''); }"
# Aynı gün kargo (kullanıcı, 18 Eki: "bugün 16'ya kadar verilen siparişler aynı gün kargoda"). İstanbul saatiyle iş günü
# (Pzt–Cum) 16.00'dan önce verilen sipariş bugün kargoda, sonrası bir sonraki iş günü. Resmî tatiller canlıda tema ayarı.
KARGO_JS = """function KARGO(ms) {
      var ist = new Date(new Date(ms).toLocaleString('en-US', { timeZone: 'Europe/Istanbul' }));
      var isg = function (d) { return d.getDay() !== 0 && d.getDay() !== 6; }, IKI = function (n) { return n < 10 ? '0' + n : String(n); };
      var gun0 = new Date(ist.getFullYear(), ist.getMonth(), ist.getDate()), kalan = gun0.getTime() + 16 * 3600000 - ist.getTime();
      var bugun = isg(ist) && kalan > 0, gun = new Date(gun0);
      if (!bugun) do { gun.setDate(gun.getDate() + 1); } while (!isg(gun));
      var fark = Math.round((gun - gun0) / 86400000), GUN = ['Pazar', 'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi'];
      var hh = Math.floor(kalan / 3600000), mi = Math.floor(kalan / 60000) % 60, ss = Math.floor(kalan / 1000) % 60;
      return { bugun: bugun, gun: gun, sayac: bugun ? IKI(hh) + ':' + IKI(mi) + ':' + IKI(ss) : '',
        metin: bugun ? 'Bugün 16.00’ya kadar verilen siparişler aynı gün kargoda' : 'Bugün verilen siparişler ' + (fark === 1 ? 'yarın' : GUN[gun.getDay()]) + ' kargoda',
        aria: bugun ? 'Aynı gün kargo için ' + hh + ' saat ' + mi + ' dakika kaldı' : '' };
    }"""
