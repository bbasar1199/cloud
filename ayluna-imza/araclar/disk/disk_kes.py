# Mağazadaki "Tek lamba, farklı temalar" afişinden (1024px) diskleri tek tek keser, daire içini netleştirir, 384px JPEG yazar.
# Disk desenine dokunulmaz (yeniden çizim yok); yalnız büyütme + hafif keskinleştirme. Unicorn ve 2025 kutuda olmadığı için alınmaz.
# Kullanım: python3 disk_kes.py <afis.png> <cikis-klasoru>
import sys, os
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
im = Image.open(src).convert('RGB'); a = np.asarray(im).astype(np.int32)
lum = (a[..., 0] * 299 + a[..., 1] * 587 + a[..., 2] * 114) // 1000
# afişteki yaklaşık merkezler (1024px)
DISKLER = {
  'okyanus': (75, 218), 'dogum-gunu': (207, 215), 'kis-gecesi': (337, 215), 'masal': (540, 213),
  'denizanasi': (676, 213), 'tasitlar': (813, 213), 'hayvanlar': (950, 213),
  'sato': (205, 357), 'ay-yildiz': (340, 357), 'deniz-kizi': (75, 497), 'uzay': (340, 497),
}
def kenar(cx, cy):
    # merkezden 8 yöne, koyu disk zemininin bittiği yarıçap; medyan
    rs = []
    for ang in np.linspace(0, 2 * np.pi, 16, endpoint=False):
        r_bul = None
        def zemin(r):
            x = int(round(cx + r * np.cos(ang))); y = int(round(cy + r * np.sin(ang)))
            if not (0 <= x < im.width and 0 <= y < im.height): return True
            R, G, B = a[y, x]
            # afiş zemini kahverengi: R > G > B, sıcak, orta-koyu
            return R - B > 18 and R >= G >= B and 35 < lum[y, x] < 140
        for r in range(55, 85):
            # arka arkaya 4 piksel zemin ise disk bitti (desendeki turuncu lekeler yanıltmasın)
            if all(zemin(r + k) for k in range(2)):
                r_bul = r; break
        if r_bul: rs.append(r_bul)
    return float(np.median(rs)) if rs else 62.0
def yaricap(cx, cy, ang):
    for r in range(55, 85):
        ok = True
        for k in range(2):
            x = int(round(cx + (r + k) * np.cos(ang))); y = int(round(cy + (r + k) * np.sin(ang)))
            if 0 <= x < im.width and 0 <= y < im.height:
                R, G, B = a[y, x]
                if not (R - B > 18 and R >= G >= B and 35 < lum[y, x] < 140): ok = False; break
        if ok: return r
    return None
def merkez(cx, cy):
    # dört yöndeki kenar mesafelerine göre merkezi ortala
    rx1, rx2 = yaricap(cx, cy, 0), yaricap(cx, cy, np.pi)
    ry1, ry2 = yaricap(cx, cy, np.pi / 2), yaricap(cx, cy, -np.pi / 2)
    if rx1 and rx2: cx = cx + (rx1 - rx2) / 2
    if ry1 and ry2: cy = cy + (ry1 - ry2) / 2
    return cx, cy
for ad, (cx, cy) in DISKLER.items():
    # merkezi düzelt: koyu piksellerin ağırlık merkezi
    r0 = 58
    ys, xs = np.mgrid[cy - r0:cy + r0, cx - r0:cx + r0]
    m = ((xs - cx) ** 2 + (ys - cy) ** 2 < r0 ** 2)
    for _ in range(2):
        cx, cy = merkez(cx, cy)
    r = kenar(cx, cy) - 1.5
    box = (cx - r, cy - r, cx + r, cy + r)
    kes = im.crop(tuple(int(round(v)) for v in box))
    S = 384
    buy = kes.resize((S, S), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=2))
    # daire dışı siyah (sayfada zaten border-radius:50% ile kırpılıyor)
    maske = Image.new('L', (S * 4, S * 4), 0); ImageDraw.Draw(maske).ellipse((6, 6, S * 4 - 6, S * 4 - 6), fill=255)
    maske = maske.resize((S, S), Image.LANCZOS)
    zemin = Image.new('RGB', (S, S), (8, 8, 12))
    son = Image.composite(buy, zemin, maske)
    son.save(os.path.join(out, f'disk-{ad}.jpg'), quality=90, optimize=True, progressive=True)
    print(ad, round(r, 1))
