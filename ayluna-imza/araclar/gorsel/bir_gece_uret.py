# "Bir gece, beş an" görsellerini gerçek ürün fotoğrafından üretir (FLUX.1 Kontext, Hugging Face).
# Kural: ürün sıfırdan çizilmez; girdi gerçek ürün fotoğrafıdır, model yalnız sahneyi kurar. Görselde yazı yok.
# Gerekli: ortam değişkeni HF_TOKEN (Hugging Face, okuma yetkisi yeter). Kurulum: pip install gradio_client pillow
# Kullanım: python3 bir_gece_uret.py <çıkış-klasörü> [an-adı ...]
import os, sys, shutil
from PIL import Image
from gradio_client import Client, handle_file

KOK = os.path.dirname(os.path.abspath(__file__))
MAG = os.path.join(KOK, '..', '..', 'canvas', 'magaza')
KORU = ('Keep the lamp exactly as in the input: same shape, same colors, same figures, same buttons, same proportions. '
        'Do not add text, letters or logos. Photorealistic interior photography, natural soft light, vertical composition.')
ANLAR = {
    '2000-oda':   ('m-kiz', "Place this lamp on a white wooden nightstand beside a child's bed in a cozy, tidy children's bedroom at 8 pm. "
                            "The lamp is switched on and glows warm. In the background a parent's hand draws soft linen curtains. A teddy bear sits on the bed."),
    '2045-kiz':   ('m-kiz', "A mother and a little girl lie in bed together, relaxed, listening to a lullaby. This lamp glows warm on the nightstand next to them, "
                            "a phone lies beside it. Cozy dim bedroom, evening."),
    '2045-erkek': ('m-erkek', "This robot lamp stands on a nightstand in a dark boy's bedroom at night and projects soft stars and planets onto the ceiling. "
                              "A little boy lies in bed looking up at the ceiling in wonder."),
    '2100-uyku':  ('m-kiz', "Dark children's bedroom at night. A little girl is asleep in bed. This lamp glows softly on the nightstand and gently projects "
                            "a moon and stars onto the ceiling and wall."),
    '0730-sabah': ('m-kiz', "Morning daylight in a children's bedroom, sunlight through linen curtains. This lamp is switched off and stands on the nightstand, "
                            "connected to a thin white USB charging cable."),
}

def dikey(ad, hedef):
    # kare ürün fotoğrafını 2:3 dikey tuvale yerleştir (çıktı da dikey olsun)
    im = Image.open(os.path.join(MAG, ad + '.jpg')).convert('RGB').resize((640, 640), Image.LANCZOS)
    c = Image.new('RGB', (640, 960), im.getpixel((470, 60)))
    c.paste(im.crop((0, 0, 640, 40)).resize((640, 360)), (0, 0)); c.paste(im, (0, 320))
    c.save(hedef, quality=92)

def main():
    if not os.environ.get('HF_TOKEN'):
        sys.exit('HF_TOKEN yok. Ortam ayarlarına Hugging Face okuma anahtarı HF_TOKEN olarak eklenmeli.')
    cik = sys.argv[1]; os.makedirs(cik, exist_ok=True)
    secili = sys.argv[2:] or list(ANLAR)
    c = Client('black-forest-labs/FLUX.1-Kontext-Dev', hf_token=os.environ['HF_TOKEN'], verbose=False)
    for an in secili:
        ref, istem = ANLAR[an]
        gir = os.path.join(cik, ref + '-dikey.jpg')
        if not os.path.exists(gir): dikey(ref, gir)
        for seed in (7, 21):
            res = c.predict(input_image=handle_file(gir), prompt=istem + ' ' + KORU, seed=seed, randomize_seed=False,
                            guidance_scale=2.5, steps=28, api_name='/infer')
            yol = res[0]['path'] if isinstance(res[0], dict) else res[0]
            hedef = os.path.join(cik, f'{an}-{seed}.jpg')
            Image.open(yol).convert('RGB').save(hedef, quality=92)
            print('ok', hedef)

if __name__ == '__main__':
    main()
