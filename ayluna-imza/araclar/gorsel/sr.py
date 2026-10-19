# Real-ESRGAN x4plus (yerel, CPU, ücretsiz) ile 4x büyütme: python sr.py girdi.png çıktı.png [geçiş]
# Kurulum (bir kez): python3 -m venv /tmp/sr-env && /tmp/sr-env/bin/pip install --index-url https://download.pytorch.org/whl/cpu torch torchvision
#   && /tmp/sr-env/bin/pip install spandrel pillow numpy
#   && curl -L -o /tmp/sr-model/RealESRGAN_x4plus.pth https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
# Çalıştır: /tmp/sr-env/bin/python araclar/gorsel/sr.py girdi.png çıktı.png
import sys, torch, numpy as np
from PIL import Image
from spandrel import ModelLoader
m = ModelLoader().load_from_file('/tmp/sr-model/RealESRGAN_x4plus.pth').model.eval()
torch.set_num_threads(4)
def sr(im):
    a = torch.from_numpy(np.asarray(im.convert('RGB')).astype(np.float32) / 255).permute(2, 0, 1)[None]
    with torch.no_grad(): o = m(a)
    return Image.fromarray((o[0].permute(1, 2, 0).clamp(0, 1).numpy() * 255).round().astype(np.uint8))
im = Image.open(sys.argv[1]); n = int(sys.argv[3]) if len(sys.argv) > 3 else 1
for _ in range(n): im = sr(im)
im.save(sys.argv[2])
