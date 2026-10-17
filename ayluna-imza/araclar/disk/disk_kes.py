# Mağazadaki "Tek lamba, farklı temalar" afişinden (1024px) diskleri tek tek keser ve 512px'e yükseltir.
# Disk desenine dokunulmaz (yeniden çizim yok). Varsa Real-ESRGAN (çizim modeli, x4) ile netleştirir; yoksa Lanczos + keskinleştirme.
# Unicorn ve 2025 diskleri kutuda olmadığı için alınmaz.
# Kullanım:
#   python3 disk_kes.py <afis.png> <cikis-klasoru>                      (Lanczos)
#   <torch'lu python> disk_kes.py <afis.png> <cikis> --sr <RealESRGAN_x4plus_anime_6B.pth>
import sys, os
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

# afişteki yaklaşık merkezler (1024px)
DISKLER = {
    'okyanus': (75, 218), 'dogum-gunu': (207, 215), 'kis-gecesi': (337, 215), 'masal': (540, 213),
    'denizanasi': (676, 213), 'tasitlar': (813, 213), 'hayvanlar': (950, 213),
    'sato': (205, 357), 'ay-yildiz': (340, 357), 'deniz-kizi': (75, 497), 'uzay': (340, 497),
}
S = 512


def zemin_mi(a, lum, x, y):
    # afiş zemini kahverengi: R > G > B, sıcak, orta-koyu
    R, G, B = a[y, x]
    return R - B > 18 and R >= G >= B and 35 < lum[y, x] < 140


def yaricap(a, lum, cx, cy, ang):
    h, w = lum.shape
    for r in range(55, 85):
        ok = True
        for k in range(2):
            x = int(round(cx + (r + k) * np.cos(ang))); y = int(round(cy + (r + k) * np.sin(ang)))
            if 0 <= x < w and 0 <= y < h and not zemin_mi(a, lum, x, y):
                ok = False; break
        if ok:
            return r
    return None


def daire(a, lum, cx, cy):
    # merkezi dört yöndeki kenar mesafelerine göre ortala, yarıçap = 16 yönün medyanı
    for _ in range(2):
        rx1, rx2 = yaricap(a, lum, cx, cy, 0), yaricap(a, lum, cx, cy, np.pi)
        ry1, ry2 = yaricap(a, lum, cx, cy, np.pi / 2), yaricap(a, lum, cx, cy, -np.pi / 2)
        if rx1 and rx2: cx = cx + (rx1 - rx2) / 2
        if ry1 and ry2: cy = cy + (ry1 - ry2) / 2
    rs = [r for r in (yaricap(a, lum, cx, cy, t) for t in np.linspace(0, 2 * np.pi, 16, endpoint=False)) if r]
    return cx, cy, (float(np.median(rs)) if rs else 62.0) - 1.5


def sr_model(yol):
    import torch
    from torch import nn
    import torch.nn.functional as F

    class RDB(nn.Module):
        def __init__(s, nf=64, gc=32):
            super().__init__()
            s.conv1 = nn.Conv2d(nf, gc, 3, 1, 1); s.conv2 = nn.Conv2d(nf + gc, gc, 3, 1, 1)
            s.conv3 = nn.Conv2d(nf + 2 * gc, gc, 3, 1, 1); s.conv4 = nn.Conv2d(nf + 3 * gc, gc, 3, 1, 1)
            s.conv5 = nn.Conv2d(nf + 4 * gc, nf, 3, 1, 1); s.lrelu = nn.LeakyReLU(0.2, True)

        def forward(s, x):
            x1 = s.lrelu(s.conv1(x)); x2 = s.lrelu(s.conv2(torch.cat((x, x1), 1)))
            x3 = s.lrelu(s.conv3(torch.cat((x, x1, x2), 1))); x4 = s.lrelu(s.conv4(torch.cat((x, x1, x2, x3), 1)))
            return s.conv5(torch.cat((x, x1, x2, x3, x4), 1)) * 0.2 + x

    class RRDB(nn.Module):
        def __init__(s, nf=64, gc=32):
            super().__init__(); s.rdb1 = RDB(nf, gc); s.rdb2 = RDB(nf, gc); s.rdb3 = RDB(nf, gc)

        def forward(s, x):
            return s.rdb3(s.rdb2(s.rdb1(x))) * 0.2 + x

    class RRDBNet(nn.Module):
        def __init__(s, nb=6, nf=64, gc=32):
            super().__init__()
            s.conv_first = nn.Conv2d(3, nf, 3, 1, 1); s.body = nn.Sequential(*[RRDB(nf, gc) for _ in range(nb)])
            s.conv_body = nn.Conv2d(nf, nf, 3, 1, 1); s.conv_up1 = nn.Conv2d(nf, nf, 3, 1, 1); s.conv_up2 = nn.Conv2d(nf, nf, 3, 1, 1)
            s.conv_hr = nn.Conv2d(nf, nf, 3, 1, 1); s.conv_last = nn.Conv2d(nf, 3, 3, 1, 1); s.lrelu = nn.LeakyReLU(0.2, True)

        def forward(s, x):
            f = s.conv_first(x); f = f + s.conv_body(s.body(f))
            f = s.lrelu(s.conv_up1(F.interpolate(f, scale_factor=2, mode='nearest')))
            f = s.lrelu(s.conv_up2(F.interpolate(f, scale_factor=2, mode='nearest')))
            return s.conv_last(s.lrelu(s.conv_hr(f)))

    net = RRDBNet()
    sd = torch.load(yol, map_location='cpu')
    net.load_state_dict(sd.get('params_ema', sd.get('params', sd)), strict=True)
    net.eval()

    def calistir(img):
        t = torch.from_numpy(np.asarray(img, dtype=np.float32) / 255.).permute(2, 0, 1)[None]
        with torch.no_grad():
            o = net(t).clamp(0, 1)[0].permute(1, 2, 0).numpy()
        return Image.fromarray((o * 255 + .5).astype(np.uint8))
    return calistir


def main():
    src, out = sys.argv[1], sys.argv[2]
    sr = sr_model(sys.argv[sys.argv.index('--sr') + 1]) if '--sr' in sys.argv else None
    os.makedirs(out, exist_ok=True)
    im = Image.open(src).convert('RGB'); a = np.asarray(im).astype(np.int32)
    lum = (a[..., 0] * 299 + a[..., 1] * 587 + a[..., 2] * 114) // 1000
    for ad, (cx, cy) in DISKLER.items():
        cx, cy, r = daire(a, lum, cx, cy)
        if sr:
            # kenardan 6px pay bırakarak kes, x4 netleştir, sonra daireye kırp
            p = 6
            kes = im.crop((int(cx - r - p), int(cy - r - p), int(cx + r + p), int(cy + r + p)))
            buyuk = sr(kes)
            k = buyuk.width / kes.width
            buyuk = buyuk.crop((int(p * k), int(p * k), int(buyuk.width - p * k), int(buyuk.height - p * k)))
            buy = buyuk.resize((S, S), Image.LANCZOS)
        else:
            kes = im.crop((int(round(cx - r)), int(round(cy - r)), int(round(cx + r)), int(round(cy + r))))
            buy = kes.resize((S, S), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=2))
        # daire dışı siyah (sayfada border-radius:50% ile zaten kırpılır)
        maske = Image.new('L', (S * 4, S * 4), 0); ImageDraw.Draw(maske).ellipse((6, 6, S * 4 - 6, S * 4 - 6), fill=255)
        maske = maske.resize((S, S), Image.LANCZOS)
        son = Image.composite(buy, Image.new('RGB', (S, S), (8, 8, 12)), maske)
        son.save(os.path.join(out, f'disk-{ad}.jpg'), quality=92, optimize=True, progressive=True)
        print(ad, round(r, 1), 'sr' if sr else 'lanczos')


if __name__ == '__main__':
    main()
