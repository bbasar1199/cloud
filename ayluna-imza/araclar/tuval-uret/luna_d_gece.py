# D · "Bir gece, beş an" kaydırma sırası panosu: aynı sahne 5 kez, her biri bir an (tuvalde kaydırma olmadığı için).
# Sahnenin CSS'i ve işaretlemesi luna_d.py'den alınır; tek kaynak orası. Çalıştır: python3 luna_d_gece.py (önce luna_d.py)
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamD.dc.html'), encoding='utf-8').read()
OUT = os.path.join(HERE, '..', '..', 'canvas', 'LunaDreamD-BirGece.dc.html')
head = src.split('</helmet>')[0] + '</helmet>\n'
head = head.replace('<title>LunaDream · D Oda ve Tavan</title>', '<title>D · Bir gece, beş an (kaydırma sırası)</title>')
a = src.index('<div class="{{geceCls}}">'); b = src.index('<div class="gece-adimlar"')
sahne = src[a:b].rstrip()
sahne = sahne.replace('<div class="{{geceCls}}">', '<div class="gece-cerceve an{{k.i}}">', 1)
js_kaynak = src.split('data-dc-script')[1]
m = re.search(r"var M = \[(.*?)\n    \];", js_kaynak, re.S)
HTML = '''<div class="pg" style="width: 2046px; background: #FFF8F0; overflow: visible">
  <div style="display: flex; gap: 24px; align-items: flex-start">
    <sc-for list="{{kareler}}" as="k" hint-placeholder-count="5">
      <div style="width: 390px; flex: none">
        <p style="margin: 0 0 8px; font-size: 13px; font-weight: 700; color: #9A561B">{{k.etiket}}</p>
        ''' + sahne + '''
      </div>
    </sc-for>
  </div>
</div>
'''
JS = '''class Component extends DCLogic {
  renderVals() {
    var B = '/_blob/', kiz = true, self = this;
    var M = [''' + m.group(1) + '''
    ];
    var moments = M.map(function (a, i) { return { i: i, t: a.t, title: a.title, text: a.text, src: B + a.id, alt: a.alt, pos: a.pos, on: 'false', gizli: 'false', cls: 'g-an' + (a.koyu ? ' koyu' : ''), pick: function () {} }; });
    var kareler = M.map(function (a, i) { return { i: i, etiket: 'Kaydırma ' + (i + 1) + '/5 · ' + a.t }; });
    return { moments: moments, kareler: kareler };
  }
}'''
open(OUT, 'w', encoding='utf-8').write(head + HTML + '</x-dc>\n<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":2046,"height":610}}\'>\n' + JS + '\n</script>\n</body>\n</html>\n')
print('yazıldı:', os.path.abspath(OUT))
