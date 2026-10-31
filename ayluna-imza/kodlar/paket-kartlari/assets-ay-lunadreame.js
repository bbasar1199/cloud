/* Ayluna · LunaDreamE bileşeni (araclar/tema/tema_uret.py). Her bölüm bu dosyayı yükler; bileşen bir kez kurulur. */
(window.AYLUNA_KUYRUK = window.AYLUNA_KUYRUK || []).push(function () {

class Component extends DCLogic {
  constructor(p) { super(p); this.state = { g: 0, model: 'kiz', adet: null, l2: null, topic: 'Tümü', disc: 1, oda: 0, dn: 0, dnT: 0, now: Date.now() }; }
  componentDidMount() {
    var self = this;
    // Büyük görünüm Esc ile kapanır
    this.esc = function (e) { if (e.key === 'Escape' && self.state.buyuk) self.setState({ buyuk: null }); };
    document.addEventListener('keydown', this.esc);
    // Azaltılmış hareket (ör. Windows'ta animasyon efektleri kapalı): galeri yine 5 sn'de geçer ama kaymadan, anında (galGit)
    var azH = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    // Neler yapabiliyor?: ekrana girince dört kelime bir kez oynar, "Tak."ta durur; azaltılmış harekette tur yok
    (function (k) { var el = document.querySelector('[data-tur="' + k + '"]'); if (!el || azH || typeof IntersectionObserver === 'undefined') return;
      var s = {}; s[k + 'On'] = false; self.setState(s); var ic = false;
      self[k + 'Io'] = new IntersectionObserver(function (es) { var g = es[0].isIntersecting && es[0].intersectionRatio >= .5;
        if (g && !ic && !self[k + 'Elle'] && !self[k + 'Kos']) self[k + 'Oyna'](); ic = g; }, { threshold: [0, .5] });
      self[k + 'Io'].observe(el); })('dk');
    // Tek saat: sayaçlar + galeri 5 sn'de bir sonraki fotoğrafa kayar (elle kaydırılınca durur) + dönen satır (hediye 4 sn, kargo 6 sn)
    this.tik = 0; this.iv = setInterval(function () { self.tik++; var S = self.state, o = { now: Date.now() };
      if (S.gOto !== false && self.tik % 5 === 0) self.galGit((S.g + 1) % Math.max(1, document.querySelectorAll('.kf').length));
      if (!azH && self.tik - S.dnT >= (S.dn ? 6 : 4)) { o.dn = 1 - S.dn; o.dnT = self.tik; }
      if (!azH) { var tkd = self.tik - (S.tkT === undefined ? 3 : S.tkT);
        if (S.tk === 4 && tkd >= 1) { o.tk = 0; o.tkT = self.tik - 1; o.tkAn = true; }
        else if (tkd >= 3) { o.tk = (S.tk || 0) + 1; o.tkT = self.tik; o.tkAn = false; } }
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
  dkAt(ms, f) { (this.dkT = this.dkT || []).push(setTimeout(f, ms)); }
  dkDur() { (this.dkT || []).forEach(clearTimeout); this.dkT = []; }
  dkGit(i) { var self = this; this.setState({ dkB: i, dkP: (this.state.dkP || 0) + 1, dkI: 0, dkOn: true });
    if (i === 2) { this.dkAt(900, function () { self.setState({ dkI: 1 }); }); this.dkAt(1800, function () { self.setState({ dkI: 2 }); }); } }
  dkOyna() { var self = this; this.dkDur(); this.dkKos = true; this.dkGit(0);
    [1, 2, 3].forEach(function (i) { self.dkAt(i * 3400, function () { self.dkGit(i); }); });
    this.dkAt(13600, function () { self.dkGit(0); }); this.dkAt(16200, function () { self.dkKos = false; }); }
  dkDokun(i) { this.dkDur(); this.dkKos = false; this.dkElle = true; this.dkGit(i); }
  galGit(i) { var el = document.querySelector('.kare-foto'); if (el && el.scrollTo && el.clientWidth) { this.otoKay = Date.now(); el.scrollTo({ left: i * el.clientWidth, behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); } else this.setState({ g: i }); }
  componentWillUnmount() { clearInterval(this.iv); this.dkDur(); if (this.dkIo) this.dkIo.disconnect();  if (this.esc) document.removeEventListener('keydown', this.esc); if (this.yolio) this.yolio.disconnect(); }
  renderVals() {
    var self = this, S = this.state, B = '/_blob/';
    function TL(n, kurus) { var s = (kurus ? n.toFixed(2) : String(Math.round(n))).split('.'); return '₺' + s[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.') + (kurus ? ',' + s[1] : ''); }
    // Galeri Shopify'daki gibi (kullanıcı, 19 Eki): canlı mağazanın görselleri, aynı sıra, kare (ogrenme/galeri-canli.json).
    // Çıkarılanlar: 'Temalar' afişi (kutuda olmayan diskler), 'Elif K.' kartı ve yorum kolajı (uydurma yorum).
    // Shopify'da galeri ürünün kendi görsellerinden (28 Eki); yoksa tasarım galerisi
    var MEDYA = (window.Ayluna && Ayluna.medya) ? Ayluna.medya() : null, G = MEDYA ? MEDYA.map(function (m) { return { src: m.src, n: m.alt }; }) : [{'id': '756460fee1769304a455ca478fcee1af', 'n': 'LunaDream Kız gece odasında yanıyor, tavanda ay ve yıldızlar: tavanı masala çeviren lamba'}, {'id': '447d1a0fd314f411baa1860180e51105', 'n': 'Alıcı yorumları: Abdülkerim T., Mehmet C. ve Handan B.'}, {'id': '992615e38254c615df3e40a553e54032', 'n': 'Her gece başka bir masal: LunaDream ve 6 masal diski'}, {'id': '3c0683cd0453bc9c12a7d20eae71116b', 'n': 'LunaDream Erkek modeli Uzay Kaşifi gece odasında, duvarda yıldızlar'}, {'id': '1bf394a66814e821fa3313725f076f0c', 'n': 'Kutudan ne çıkıyor: lamba, 6 masal diski, 6 hediye disk ve USB şarj kablosu; ücretsiz kargo, 30 gün iade, kartla %5 indirim'}];
    // Ay göstergesi: i. fotoğrafın evresi (i+1)/N; geçilenler ve o anki yanar, son fotoğrafta dolunay
    function AYE(f) { var r = 9, c = 12, rx = Math.abs(1 - 2 * f) * r; return f >= 1 ? 'M12 3a9 9 0 1 1 0 18a9 9 0 1 1 0-18Z' : 'M' + c + ' ' + (c - r) + 'A' + r + ' ' + r + ' 0 0 1 ' + c + ' ' + (c + r) + 'A' + rx.toFixed(2) + ' ' + r + ' 0 0 ' + (f < .5 ? 0 : 1) + ' ' + c + ' ' + (c - r) + 'Z'; }
    var gal = G.map(function (g, i) { var on = i === S.g; return { src: g.src || B + g.id, n: g.n, pos: '50% 50%', top: 56, h: 390, ay: AYE((i + 1) / G.length), acls: i < S.g ? 'lit' : (on ? 'lit on' : '') }; });
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
    ].map(function (b) { var on = S.adet === b.n; return { src1: b.n === 2 ? SRC(l1) : SRC(S.model), src2: SRC(l2), tlCls: b.n === 2 ? 'tl cift' : 'tl', t: b.t, p: b.p, old: b.old, hasOld: !!b.old, unit: b.unit, sub: b.sub, rib: b.rib, two: b.n === 2, hed: b.n === 2 ? '+ 12 masal diski hediye · kutu başı 6' : '+ 6 masal diski hediye',
      on: on ? 'true' : 'false', ac: on && b.n === 2, cls: on ? 'kt on' : 'kt', pick: function () { self.setState({ adet: b.n }); } }; });
    var total = S.adet === 2 ? P2 : P1, online = Math.round(total * 0.95 * 100) / 100, kapida = total + 80;
    var AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
    function KARGO(ms) {
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
    }
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
    // Videolar (28 Eki, kullanıcı: "videolar açılmıyor"): Shopify'da ürünün medyasındaki ya da bloğa seçilen videolar oynar; video yoksa tasarımdaki fotoğraflar kalır.
    // Önizlemede tasarımdaki kapaklar.
    var VID = (window.Ayluna && Ayluna.videolar) ? Ayluna.videolar() : null;
    var vids = VID && VID.length ? VID.map(function (v) { return { t: v.alt || 'LunaDream videosu', k: 'Dokun, sesli izle', al: (v.alt || 'LunaDream videosu') + ': videoyu oynat', src: v.poster || '', vsrc: v.src, pos: '50% 50%', gercek: true, kapak: false }; })
      : [
      { t: 'Işık kapanınca tavanda masal', al: 'Işık kapanınca tavanda masal', k: 'Kız modeli', src: B + '5ce96d9e6f38e8d571ac1cb9e529ec22', pos: '50% 40%', gercek: false, kapak: true },
      { t: 'Bir müşterimizin akşamı', al: 'Bir müşterimizin akşamı', k: 'Müşteri videosu', src: B + '7ad3cbbe71680f4ed3027dbd056e391f', pos: '50% 40%', gercek: false, kapak: true },
      { t: 'Uzay Kaşifi tavanda', al: 'Uzay Kaşifi tavanda', k: 'Erkek modeli', src: B + 'b2c8d9b92ad3541b532e3aa108a74735', pos: '50% 45%', gercek: false, kapak: true },
      { t: 'Disk nasıl takılır', al: 'Disk nasıl takılır', k: 'Kurulum', src: B + '5b284c77c252b08a2974bde8e43de126', pos: '50% 50%', gercek: false, kapak: true }
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
function KAY(y) { return function (e) { var t = e && (e.currentTarget || e.target), r = t && t.closest && t.closest('.serit-ok'), s = null;
      while (r && !s && r.tagName !== 'SECTION') { var n = r.nextElementSibling; if (n && n.classList.contains('noscroll')) s = n; r = r.parentElement; }
      if (!s) { var b = t && t.closest && t.closest('section'); s = b && b.querySelector('.noscroll'); }
      if (s) s.scrollBy({ left: y * Math.max(220, s.clientWidth * .8), behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); }; }
function GALOK(y) { return function (e) { var t = e && (e.currentTarget || e.target), k = t && t.closest && t.closest('.sahne, .hero, .gal, .slayt'), s = k && k.querySelector('.kare-foto, .h-iz, .g-iz, .s-iz');
      if (!s || !s.clientWidth) return; var m = Math.max(1, Math.round(s.scrollWidth / s.clientWidth)), n = (Math.round(s.scrollLeft / s.clientWidth) + y + m) % m;
      s.scrollTo({ left: n * s.clientWidth, behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); }; }
    var PR = [
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
    var OEV = ['M12 3A9 9 0 0 1 12 21A4.50 9 0 0 0 12 3Z', 'M12 3A9 9 0 0 1 12 21A0.00 9 0 0 1 12 3Z', 'M12 3A9 9 0 0 1 12 21A4.50 9 0 0 1 12 3Z', 'M12 3A9 9 0 0 1 12 21A9.00 9 0 0 1 12 3Z'], oi = S.oda || 0;
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
      { q: 'Nasıl ödeyebilirim?', a: 'Tüm kredi ve banka kartlarıyla ödeyebilirsin; kartla öderken %5 indirim alırsın, kart bilgin bize gelmez.' },
      { q: 'Beğenmezsem iade edebilir miyim?', a: '30 gün içinde iade edebilirsin. Sana iade kodunu göndeririz, kargosu ücretsizdir. İlk 14 gün yasal cayma hakkındır.' }
    ];
    var dB = S.dkB || 0, dP = S.dkP || 0;
    var dkV = { dkCls: 'dg b' + dB + ' x-' + ['tak', 'cal', 'kis', 'sarj'][dB] + ' i' + (S.dkI || 0) + ((S.model === 'erkek') ? ' erkek' : '') + (dP ? (dP % 2 ? ' oa' : ' ob') : '') + (S.dkOn === false ? ' bek' : S.dkOn ? ' gir' : ''),
      dkUrunG: function () { self.dkDokun(dB); } };
    [0, 1, 2, 3].forEach(function (i) { dkV['dkz' + i] = 'dg-z z' + i + (i <= dB ? ' on' : ''); dkV['dkw' + i] = i === dB ? 'on' : i < dB ? 'ust' : ''; dkV['dkc' + i] = i === dB ? 'on' : '';
      dkV['dkb' + i] = i === dB ? 'on' : ''; dkV['dkg' + i] = function () { self.dkDokun(i); }; });
    var MASA = !!(window.Ayluna && window.matchMedia && matchMedia('(min-width: 1024px)').matches);  // yalnız sitede; tuval hep telefon
    return { masa: MASA, tel: !MASA, ...dkV,
      gal: gal, gNo: S.g + 1, gCount: G.length, gKay: gKay, gPrev: function () { self.setState({ g: (S.g + G.length - 1) % G.length }); }, gNext: function () { self.setState({ g: (S.g + 1) % G.length }); }, models: models, modelName: kiz ? 'Kız · tavşanlı' : 'Erkek · Uzay Kaşifi', modelSrc: kiz ? KES_K : KES_E,
      kiz: kiz, erkek: !kiz, paket: paket, ikinci: ikinci, modelEtiket: S.adet === 2 ? '1. lamba' : 'Model', adetName: S.adet === 2 ? (l1 !== l2 ? 'Kız + Erkek' : (l1 === 'kiz' ? '2 Kız' : '2 Erkek')) : '1 Adet',
      onLabel: 'Güvenli Ödeme ile Al', onPrice: TL(online, true),  // düğmede fiyat yok (kullanıcı, 19 Eki)
      p1: TL(P1, true), c1: TL(C1, true), pct: Math.round((1 - P1 / C1) * 100),
      onNote: 'Kartla %5 indirimli · ' + TL(total - online, true) + ' daha az',
      kargo: KG.bugun ? 'Bugün' : kd.getDate() + ' ' + AY[kd.getMonth()], teslim: teslim,
      kgMetin: KG.metin, kgBugun: KG.bugun, kgSayac: KG.sayac, kgAria: KG.aria,
      tkY: -24 * (S.tk || 0), tkCls: 'dsr-iz' + (S.tkAn ? ' anlik' : ''), tkC0: 'dsr-s' + ((S.tk || 0) === 0 && !(0 === 0 && S.tkAn) ? ' on' : ''), tkC1: 'dsr-s' + ((S.tk || 0) === 1 && !(1 === 0 && S.tkAn) ? ' on' : ''), tkC2: 'dsr-s' + ((S.tk || 0) === 2 && !(2 === 0 && S.tkAn) ? ' on' : ''), tkC3: 'dsr-s' + ((S.tk || 0) === 3 && !(3 === 0 && S.tkAn) ? ' on' : ''), tkC4: 'dsr-s' + ((S.tk || 0) === 4 && !(4 === 0 && S.tkAn) ? ' on' : ''),
      dnA: 'dn-s' + (S.dn === 0 ? ' on' : self.tik - S.dnT < 1 ? ' ust' : ''), dnB: 'dn-s' + (S.dn === 1 ? ' on' : self.tik - S.dnT < 1 ? ' ust' : ''),
      // Puan ve sayı canlıda Loox'tan (teyit bekliyor)
      rating: '4,7', reviews: 62, starPct: 94,
      yolCls: S.yolAc ? 'yol on' : 'yol', sihKiz: S.model !== 'erkek', sihErkek: S.model === 'erkek', stokCls: S.stokAc ? 'stok-kd on' : 'stok-kd', vids: vids, vidCls: 'bolum gir', mfoto: mfoto, mesajlar: mesajlar,
      oneQ: oneQ, revRest: revRest, fsira: fsira,
      buyuk: S.buyuk || '', buyukAd: S.buyukAd || '', buyukVar: !!S.buyuk, buyukKapat: function () { self.setState({ buyuk: null }); }, cdLine: cdLine, cdShort: cdShort, cdTiny: cdTiny, cubukAlt: S.adet === 2 ? (l1 !== l2 ? 'Kız + Erkek' : (l1 === 'kiz' ? '2 Kız' : '2 Erkek')) : '1 Adet · ' + (kiz ? 'Kız' : 'Erkek'), cdAy: cdAy, cdAria: cdAria, discs: discs, proj: proj, discName: DISCS[S.disc].n,
      odalar: odalar, odaKay: odaKay, shop: shop, shopCount: PR.length, kayGeri: KAY(-1), kayIleri: KAY(1), galGeri: GALOK(-1), galIleri: GALOK(1), faq: faq,
      urs: URS
    };
  }
}

Ayluna.baslat(Component);
});
