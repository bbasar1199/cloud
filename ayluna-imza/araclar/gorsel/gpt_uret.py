# LunaDream premium fotoğraf seti · OpenAI görsel API'siyle üretim (22 Eki).
# Kullanıcı: "Girip yap direkt GPT'den." Bu oturumda anahtar yoktu; anahtar ortam ayarına eklenince yeni oturumda:
#   python3 araclar/gorsel/gpt_uret.py --dene          # yalnız planı gösterir (istem, ekler, boyut), API'ye gitmez
#   python3 araclar/gorsel/gpt_uret.py                 # 11 kareyi üretir → canvas/p-gorsel/<Dosya>
#   python3 araclar/gorsel/gpt_uret.py p-kiz-gunduz    # yalnız adı verilen kareler
# İstemler ve ekler: ogrenme/chatgpt-istemleri-lunadream.txt (ChatGPT'ye elle yapıştırılan dosyanın aynısı).
# Anahtar yalnız OPENAI_API_KEY ortam değişkeninden okunur; ekrana ya da dosyaya yazılmaz. Ücret OpenAI hesabına yansır.
# Üretilen her kare büyütülüp gerçek ürünle karşılaştırılır (tavşan sayısı, kubbe kıvrımı, robotun yüzü, el/parmak, yazı);
# farklıysa kullanılmaz, yeniden üretilir. Higgsfield kullanılmaz.
import os, re, sys, json, base64, subprocess, tempfile

KOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
ISTEM = os.path.join(KOK, 'ogrenme', 'chatgpt-istemleri-lunadream.txt')
CIKIS = os.path.join(KOK, 'canvas', 'p-gorsel')
# Referans paketindeki adlar → depodaki dosyalar (paket bu dosyalardan kuruldu)
REF = {'01-m-kiz.jpg': 'canvas/magaza/m-kiz.jpg', '02-m-erkek.jpg': 'canvas/magaza/m-erkek.jpg',
       '03-c-kiz-gece.jpg': 'canvas/c-gorsel/c-kiz-gece.jpg', '04-c-erkek-gece.jpg': 'canvas/c-gorsel/c-erkek-gece.jpg',
       '05-disk-ay-yildiz.jpg': 'canvas/diskler/disk-ay-yildiz.jpg', '06-disk-uzay.jpg': 'canvas/diskler/disk-uzay.jpg',
       '07-c-elde.jpg': 'canvas/c-gorsel/c-elde.jpg', '08-disk-masal.jpg': 'canvas/diskler/disk-masal.jpg',
       '09-disk-okyanus.jpg': 'canvas/diskler/disk-okyanus.jpg', '10-disk-sato.jpg': 'canvas/diskler/disk-sato.jpg',
       '11-disk-deniz-kizi.jpg': 'canvas/diskler/disk-deniz-kizi.jpg', '12-disk-hayvanlar.jpg': 'canvas/diskler/disk-hayvanlar.jpg',
       '13-c-an-disk.jpg': 'canvas/c-gorsel/c-an-disk.jpg'}
BOYUT = {'kare': '1024x1024', 'dikey': '1024x1536'}


def kareler():
    """İstem dosyasındaki blokları sırayla döndürür: dosya, ekler, boyut, istem."""
    metin = open(ISTEM, encoding='utf-8').read()
    bas = list(re.finditer(r'^\d+\) Dosya: (\S+)\s+·\s+Ekler: (.+?)\s+·\s+Oran: (\S+).*\n-+\n', metin, re.M))
    for i, m in enumerate(bas):
        son = bas[i + 1].start() if i + 1 < len(bas) else len(metin)
        istem = ' '.join(metin[m.end():son].split())
        ekler = [e.strip() for e in m.group(2).split(',')]
        yield {'dosya': m.group(1), 'ekler': ekler, 'boyut': BOYUT['dikey' if m.group(3).startswith('dikey') else 'kare'], 'istem': istem}


def uret(k, anahtar):
    """Ekli referanslarla tek kare üretir (images/edits, gpt-image-1); PNG'yi canvas/p-gorsel'e yazar."""
    with tempfile.NamedTemporaryFile('w', suffix='.cfg', delete=False) as c:   # anahtar komut satırında görünmesin
        c.write('header = "Authorization: Bearer %s"\n' % anahtar)
        cfg = c.name
    try:
        komut = ['curl', '-sS', '-m', '600', '-K', cfg, 'https://api.openai.com/v1/images/edits',
                 '-F', 'model=gpt-image-1', '-F', 'prompt=' + k['istem'], '-F', 'size=' + k['boyut'], '-F', 'quality=high', '-F', 'n=1']
        for e in k['ekler']:
            komut += ['-F', 'image[]=@' + os.path.join(KOK, REF[e])]
        cevap = subprocess.run(komut, capture_output=True, text=True).stdout
    finally:
        os.unlink(cfg)
    try:
        veri = json.loads(cevap)
        b64 = veri['data'][0]['b64_json']
    except Exception:
        raise SystemExit('%s: API cevabı beklenmedik: %s' % (k['dosya'], cevap[:400]))
    os.makedirs(CIKIS, exist_ok=True)
    yol = os.path.join(CIKIS, k['dosya'])
    open(yol, 'wb').write(base64.b64decode(b64))
    return yol


if __name__ == '__main__':
    arg = [a for a in sys.argv[1:] if not a.startswith('--')]
    hepsi = list(kareler())
    secili = [k for k in hepsi if not arg or any(k['dosya'].startswith(a) for a in arg)]
    eksik = sorted({e for k in secili for e in k['ekler'] if e not in REF or not os.path.exists(os.path.join(KOK, REF[e]))})
    if eksik:
        raise SystemExit('referans bulunamadı: ' + ', '.join(eksik))
    if '--dene' in sys.argv:
        for k in secili:
            print('%-20s %-9s ekler: %s\n    %s…' % (k['dosya'], k['boyut'], ', '.join(k['ekler']), k['istem'][:110]))
        print('%d kare; API çağrılmadı.' % len(secili))
        sys.exit(0)
    anahtar = os.environ.get('OPENAI_API_KEY')
    if not anahtar:
        raise SystemExit('OPENAI_API_KEY yok: ortam ayarlarına eklenmeli (sohbete yapıştırılmaz).')
    for k in secili:
        print('üretiliyor:', k['dosya'], flush=True)
        print('  →', uret(k, anahtar), flush=True)
