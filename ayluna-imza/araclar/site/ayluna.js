/* Ayluna site önizlemesi · ortak çalışma zamanı (18 Eki)
   1) Tuval sayfalarının (.dc.html) şablonunu çalıştırır: {{delik}}, sc-for, sc-if, onClick; her çizimde DOM'u yerinde yamar
      (öğeler korunur: kaydırma, geçiş ve animasyonlar bozulmaz; açılan <details> açık kalır).
   2) Sepet deposu (localStorage), sepet çekmecesi, kapıda ödeme formu (EasySell yerine), menü, arama, yönlendirme.
   Shopify'da bu işlerin karşılığı: sepet = /cart.js + /cart/add.js, kapıda ödeme = EasySell, ödeme = Shopify checkout. */
(function () {
  'use strict';
  var V = window.AYLUNA_VERI || { urun: {}, sira: [] };
  var TL = function (n) { var s = (Math.round(n * 100) / 100).toFixed(2).split('.'); return '₺' + s[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.') + ',' + s[1]; };
  var HTMLNS = 'http://www.w3.org/1999/xhtml';
  // Tek dosya kipi (site-tek/index.html): bütün sayfalar tek dosyada, adres #sayfa ile değişir
  var TEK = !!window.AYLUNA_TEK;
  function gorsel(u) { return String(u || '').replace(/\/_blob\/([0-9a-f]{32})/g, function (m, i) { return (V.blob && V.blob[i]) || m; }); }

  /* ---------- 1. Şablon motoru ---------- */
  var kok = null, sablon = null, C = null, planli = false, ilk = true;
  function DCLogic(p) { this.props = p || {}; this.state = {}; }
  DCLogic.prototype.setState = function (o) { Object.assign(this.state, typeof o === 'function' ? o(this.state) : o); planla(); };
  window.DCLogic = DCLogic;

  function yol(sc, p) { return String(p).split('.').reduce(function (o, k) { return o == null ? o : o[k]; }, sc); }
  var DELIK = /\{\{\s*([^}]+?)\s*\}\}/g;
  function doldur(s, sc) { return s.replace(DELIK, function (m, p) { var v = yol(sc, p); return v == null ? '' : String(v); }); }
  function tek(s) { var m = s && s.match(/^\s*\{\{\s*([^}]+?)\s*\}\}\s*$/); return m ? m[1] : null; }

  function vyap(n, sc, out) {
    if (n.nodeType === 3) { out.push({ t: '#', v: doldur(n.nodeValue, sc) }); return; }
    if (n.nodeType !== 1) return;
    var tag = n.localName;
    if (tag === 'sc-for') {
      var l = yol(sc, tek(n.getAttribute('list')) || '') || [], as = n.getAttribute('as');
      for (var i = 0; i < l.length; i++) { var s2 = Object.create(sc); s2[as] = l[i]; for (var c = n.firstChild; c; c = c.nextSibling) vyap(c, s2, out); }
      return;
    }
    if (tag === 'sc-if') { var v = yol(sc, tek(n.getAttribute('value')) || ''); if (v && v !== 'false') for (var c2 = n.firstChild; c2; c2 = c2.nextSibling) vyap(c2, sc, out); return; }
    var d = { t: tag, ns: n.namespaceURI, a: {}, h: {}, c: [] };
    for (var k = 0; k < n.attributes.length; k++) {
      var at = n.attributes[k], nm = at.name;
      if (nm.indexOf('hint-') === 0) continue;
      if (/^on[a-z]+$/i.test(nm) && tek(at.value)) { var f = yol(sc, tek(at.value)); if (typeof f === 'function') d.h[nm.slice(2).toLowerCase()] = f; continue; }
      var deger = doldur(at.value, sc);
      if (deger.indexOf('/_blob/') >= 0) deger = deger.replace(/\/_blob\/([0-9a-f]{32})/g, function (m, i) { return (V.blob && V.blob[i]) || m; });
      d.a[nm] = deger;
    }
    var kaynak = tag === 'template' ? n.content : n;
    for (var c3 = kaynak.firstChild; c3; c3 = c3.nextSibling) vyap(c3, sc, d.c);
    out.push(d);
  }
  function dinle(el, h) {
    el.__h = h;
    if (!el.__d) el.__d = {};
    for (var t in h) if (!el.__d[t]) { el.__d[t] = 1; el.addEventListener(t, function (e) { var f = this.__h && this.__h[e.type]; if (f) f.call(this, e); }); }
  }
  function olustur(v) {
    if (v.t === '#') return document.createTextNode(v.v);
    var el = v.ns && v.ns !== HTMLNS ? document.createElementNS(v.ns, v.t) : document.createElement(v.t);
    for (var k in v.a) try { el.setAttribute(k, v.a[k]); } catch (e) {}
    dinle(el, v.h);
    for (var i = 0; i < v.c.length; i++) el.appendChild(olustur(v.c[i]));
    return el;
  }
  function koru(el, nm) { return (nm === 'open' && el.localName === 'details') || nm.indexOf('data-ay-') === 0; }
  function yama(el, v) {
    for (var i = el.attributes.length - 1; i >= 0; i--) { var nm = el.attributes[i].name; if (!(nm in v.a) && !koru(el, nm)) el.removeAttribute(nm); }
    for (var k in v.a) if (el.getAttribute(k) !== v.a[k]) try { el.setAttribute(k, v.a[k]); } catch (e) {}
    dinle(el, v.h);
    cocuklar(el, v.c);
  }
  function cocuklar(el, vc) {
    var ec = el.childNodes, i;
    for (i = 0; i < vc.length; i++) {
      var v = vc[i], n = ec[i];
      if (!n) { el.appendChild(olustur(v)); continue; }
      if (v.t === '#') { if (n.nodeType === 3) { if (n.nodeValue !== v.v) n.nodeValue = v.v; } else el.replaceChild(olustur(v), n); continue; }
      if (n.nodeType === 1 && n.localName === v.t && (n.namespaceURI === (v.ns || HTMLNS))) yama(n, v); else el.replaceChild(olustur(v), n);
    }
    while (ec.length > vc.length) el.removeChild(el.lastChild);
  }
  function ciz() {
    planli = false;
    var vals = C.renderVals(), out = [];
    for (var c = sablon.firstChild; c; c = c.nextSibling) vyap(c, vals, out);
    cocuklar(kok, out);
    suslen();
    if (ilk) { ilk = false; if (C.componentDidMount) C.componentDidMount(); }
    else if (C.componentDidUpdate) C.componentDidUpdate();
  }
  function planla() { if (planli || !C) return; planli = true; (window.requestAnimationFrame || setTimeout)(ciz); }

  /* ---------- 2. Sepet deposu ---------- */
  var ANAHTAR = 'ayluna-sepet-v1';
  var EKLER = V.ekler || [];
  var HIZLI = 79.99, KAPIDA = 80;
  function oku() { try { var s = JSON.parse(localStorage.getItem(ANAHTAR)); if (s && s.satirlar) return s; } catch (e) {} return { satirlar: [], ekler: {}, hizli: false }; }
  function yaz(s) { try { localStorage.setItem(ANAHTAR, JSON.stringify(s)); } catch (e) {} haber(); }
  function haber() { try { window.dispatchEvent(new CustomEvent('ayluna-sepet')); } catch (e) {} suslen(); if (C) planla(); }
  var Sepet = {
    oku: oku,
    ekle: function (sat) {
      var s = oku(), id = sat.h + '|' + (sat.varyant || '') + '|' + (sat.paket || 1);
      var var_ = s.satirlar.filter(function (x) { return x.id === id; })[0];
      if (var_) var_.adet += sat.adet || 1; else s.satirlar.push(Object.assign({ id: id, adet: 1 }, sat, { id: id }));
      yaz(s); return s;
    },
    // Ürün sayfasındaki satın alma butonları: o ürünün satırı seçili hâliyle tek kalır (kartla dene → geri dön → kapıda: ×2 olmaz)
    koy: function (sat) {
      var s = oku(), id = sat.h + '|' + (sat.varyant || '') + '|' + (sat.paket || 1);
      s.satirlar = s.satirlar.filter(function (x) { return x.h !== sat.h; });
      s.satirlar.push(Object.assign({ adet: 1 }, sat, { id: id })); yaz(s); return s;
    },
    adet: function (id, n) { var s = oku(); s.satirlar.forEach(function (x) { if (x.id === id) x.adet = Math.max(1, Math.min(9, n)); }); yaz(s); },
    sil: function (id) { var s = oku(); s.satirlar = s.satirlar.filter(function (x) { return x.id !== id; }); if (!s.satirlar.length) s.ekler = {}; yaz(s); },
    ek: function (k, on) { var s = oku(); s.ekler = s.ekler || {}; s.ekler[k] = on === undefined ? !s.ekler[k] : !!on; yaz(s); },
    hizli: function (on) { var s = oku(); s.hizli = !!on; yaz(s); },
    temizle: function () { yaz({ satirlar: [], ekler: {}, hizli: false }); },
    sayi: function () { var s = oku(); return s.satirlar.reduce(function (a, x) { return a + x.adet; }, 0) + EKLER.filter(function (e) { return s.ekler && s.ekler[e.k]; }).length; },
    // kart: %5 indirim; kapıda: +₺80, indirim yok
    toplam: function (yolu) {
      var s = oku(), urun = s.satirlar.reduce(function (a, x) { return a + x.birim * x.adet; }, 0);
      var ek = EKLER.reduce(function (a, e) { return a + (s.ekler && s.ekler[e.k] ? e.p : 0); }, 0);
      var kargo = s.hizli ? HIZLI : 0, ind = yolu === 'kapida' ? 0 : Math.round((urun + ek) * 0.05 * 100) / 100, kp = yolu === 'kapida' ? KAPIDA : 0;
      return { urun: urun, ek: ek, kargo: kargo, indirim: ind, kapida: kp, toplam: Math.round((urun + ek - ind + kargo + kp) * 100) / 100 };
    },
    EKLER: EKLER, HIZLI: HIZLI, KAPIDA: KAPIDA, TL: TL
  };
  window.AylunaSepet = Sepet;
  window.addEventListener('storage', function (e) { if (e.key === ANAHTAR) haber(); });

  /* Ürün sayfasındaki seçimi sepet satırına çevir (paket, model, seçenek) */
  function satir(h) {
    var U = V.urun[h]; if (!U) return null;
    var S = (C && C.state) || {}, n = S.adet || S.pk || 1;
    var pk = (U.paket || []).filter(function (b) { return b.n === n; })[0];
    // Paket ve çoklu adette üstü çizili "2 × eski fiyat" yok (TASARIM-BILGISI §7 kural 2)
    var birim = pk ? pk.p : U.p * n, eski = n === 1 ? (pk && pk.c ? pk.c : U.c || null) : null, varyant = [];
    varyant.push(n > 1 ? n + ' adet' : '1 adet');
    if (h === 'lunadream-gece-lambasi') { var M = { kiz: 'Kız (Tavşanlı)', erkek: 'Erkek (Robot)' }; varyant.push(n === 2 ? M[S.model || 'kiz'] + ' + ' + M[S.l2 || S.model || 'kiz'] : M[S.model || 'kiz']); }
    else if (U.secenek && U.secenek.length) varyant.push(U.secenek[S.sec || 0]);
    return { h: h, ad: U.ad, varyant: varyant.join(' · '), paket: n, birim: birim, eski: eski, img: U.img, adet: 1 };
  }

  /* ---------- 3. Arayüz katmanları ---------- */
  function kokP() { var w = window; try { while (w.parent && w.parent !== w && w.parent.Ayluna && w.parent.document) w = w.parent; } catch (e) {} return w; }
  function ust() { var w = kokP(); return w !== window ? w : null; }
  function el(html) { var d = document.createElement('div'); d.innerHTML = html.trim(); return d.firstChild; }
  function kilit(on) { document.documentElement.classList.toggle('ay-kilit', !!on); }
  var tost = null;
  function bildir(m) {
    if (!tost) { tost = el('<div class="ay-tost" role="status" aria-live="polite"></div>'); document.body.appendChild(tost); }
    tost.textContent = m; tost.classList.add('on'); clearTimeout(tost.__z); tost.__z = setTimeout(function () { tost.classList.remove('on'); }, 2600);
  }
  Sepet.bildir = bildir;

  // Menü
  var MENU = [['Ana sayfa', './'], ['Tüm ürünler', 'tum-urunler.html'], ['LunaDream Gece Lambası', 'lunadream-gece-lambasi.html'], ['Galaxy USB Projektör', 'galayx-usb-projektor.html'],
    ['Ayluna AyFeneri', 'lamba.html'], ['Galaksi Night Projektör', 'ayluna-galaksi-night-projektor.html'], ['Kargo takip', 'kargo-takip.html'], ['İade ve değişim', 'iade.html'], ['İletişim', 'iletisim.html']];
  var menu = null;
  function menuAc() {
    if (!menu) {
      menu = el('<div class="ay-katman ay-menu" role="dialog" aria-modal="true" aria-label="Menü"><div class="ay-perde" data-kapat></div><nav class="ay-panel sol">' +
        '<div class="ay-p-ust"><b>Ayluna</b><button type="button" class="ay-x" data-kapat aria-label="Menüyü kapat"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"></path></svg></button></div>' +
        '<ul>' + MENU.map(function (m) { return '<li><a href="' + m[1] + '">' + m[0] + '<svg viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"></path></svg></a></li>'; }).join('') + '</ul>' +
        '<a class="ay-wa" href="' + (V.wa || '#') + '" data-wa>WhatsApp destek · ortalama 2 saatte yanıt</a></nav></div>');
      document.body.appendChild(menu);
      menu.addEventListener('click', function (e) {
        if (e.target.closest('[data-kapat]')) { menuKapat(); return; }
        var a = e.target.closest('a[href]'); if (!a) return;
        e.preventDefault();
        if (a.hasAttribute('data-wa')) { bildir('WhatsApp numarası: [teyit]. Canlıda wa.me bağlantısı açılır.'); return; }
        menuKapat(); git(a.getAttribute('href'));
      });
    }
    menu.classList.add('on'); kilit(1);
    setTimeout(function () { var a = menu.querySelector('a'); if (a) a.focus(); }, 60);
  }
  function menuKapat() { if (menu) menu.classList.remove('on'); kilit(0); }

  /* Masaüstü (kullanıcı, 19 Eki: "mağazanın masaüstü görünüşünü de yapmak lazım"): 1024px ve üstünde ortak üst menü.
     Sayfaların telefon başlıkları o genişlikte gizlenir (ayluna.css); bağlantı ve düğmeler genel yönlendirmeden geçer. */
  var MASA = [['Tüm ürünler', 'tum-urunler.html', 'koleksiyon'], ['LunaDream', 'lunadream-gece-lambasi.html', 'lunadream-gece-lambasi'], ['Galaxy USB', 'galayx-usb-projektor.html', 'galayx-usb-projektor'],
    ['AyFeneri', 'lamba.html', 'lamba'], ['Galaksi Night', 'ayluna-galaksi-night-projektor.html', 'ayluna-galaksi-night-projektor'], ['Kargo takip', 'kargo-takip.html', 'kargo-takip'], ['İletişim', 'iletisim.html', 'iletisim']];
  var IC = function (d) { return '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true">' + d + '</svg>'; };
  var masa = null;
  // Masaüstü sınırı geçilince (pencere boyu) yeniden çiz: özellik kartları telefonda satın alma kutusunda, masaüstünde galerinin altında
  if (window.matchMedia) { var mq = matchMedia('(min-width: 1024px)'); if (mq.addEventListener) mq.addEventListener('change', planla); else if (mq.addListener) mq.addListener(planla); }
  function masaUst() {
    document.documentElement.setAttribute('data-ay-tur', SAYFA);
    if (!masa) {
      masa = el('<header class="ay-masa"><div class="ay-masa-ic"><a class="ay-logo" href="./" aria-label="Ayluna ana sayfa"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="rgba(255,255,255,.6)" stroke-width="1.6"></circle><path d="M12 2a10 10 0 0 1 0 20a7 10 0 0 0 0-20Z" fill="#F2A65A"></path></svg><b>Ayluna</b></a>' +
        '<nav aria-label="Ana menü">' + MASA.map(function (m) { return '<a href="' + m[1] + '" data-k="' + m[2] + '">' + m[0] + '</a>'; }).join('') + '</nav>' +
        '<div class="ay-masa-sag"><a href="arama.html" aria-label="Ara">' + IC('<circle cx="11" cy="11" r="6.5"></circle><path d="M20 20l-4.2-4.2"></path>') + '</a>' +
        '<a href="hesap.html" aria-label="Hesap">' + IC('<circle cx="12" cy="8.5" r="3.6"></circle><path d="M4.5 20a7.5 7.5 0 0 1 15 0"></path>') + '</a>' +
        '<button type="button" aria-label="Sepet">' + IC('<path d="M6 8h12l-1 12H7z"></path><path d="M9 8a3 3 0 0 1 6 0"></path>') + '</button></div></div></header>');
      document.body.insertBefore(masa, document.body.firstChild);
    }
    var k = SAYFA === 'urun' ? URUN : SAYFA, l = masa.querySelectorAll('nav a');
    for (var i = 0; i < l.length; i++) { if (l[i].getAttribute('data-k') === k) l[i].setAttribute('aria-current', 'page'); else l[i].removeAttribute('aria-current'); }
  }

  // Masaüstü yapışkan satın alma çubuğu (eleştirmen önerisi, kullanıcı seçti 19 Eki): sayfanın satın alma butonu
  // ekranın üstünden çıkınca menünün altından iner. Ürün, seçim, kartla al butonu (sayfadaki etiketin aynısı) ve fiyatsız Kapıda bağlantısı.
  // Yalnız transform/opacity; sayaç yok; telefonda görünmez (oradaki yapışkan çubuk sayfanın kendisinde).
  var cubuk = null, cubukIO = null;
  function anaBtn() { return document.querySelector('#kok .urun-ust .btn-on, #kok .urun-ust .btn1'); }
  function cubukYaz() {
    if (!cubuk) return;
    var b = anaBtn(), s = satir(URUN);
    cubuk.querySelector('[data-l]').textContent = b ? (b.querySelector('.b-ic>span') || b).textContent.trim() : 'Güvenli Ödeme ile Al';
    cubuk.querySelector('[data-v]').textContent = s ? s.varyant : '';
  }
  function cubukKur() {
    if (cubukIO) { cubukIO.disconnect(); cubukIO = null; }
    if (cubuk) cubuk.classList.remove('on');
    var U = V.urun[URUN], b = anaBtn();
    if (SAYFA !== 'urun' || !U || U.stok === false || !b || !window.IntersectionObserver) return;
    if (!cubuk) {
      cubuk = el('<div class="ay-al" role="region" aria-label="Hızlı satın alma"><div class="ay-al-ic"><img alt=""><span class="ay-al-y"><b></b><small data-v></small></span>' +
        '<button type="button" class="ay-al-kp" data-kp>Kapıda ödeme</button><button type="button" class="ay-al-btn" data-al><span data-l></span></button></div></div>');
      document.body.appendChild(cubuk);
      cubuk.addEventListener('click', function (e) {
        if (e.target.closest('[data-al]')) sepeteAt(URUN, 'kart'); else if (e.target.closest('[data-kp]')) sepeteAt(URUN, 'kapida');
      });
    }
    cubuk.querySelector('img').src = gorsel(U.img); cubuk.querySelector('b').textContent = U.ad;
    cubukIO = new IntersectionObserver(function (g) {
      var x = g[0], ac = !x.isIntersecting && x.boundingClientRect.top < 0;
      if (ac) cubukYaz(); cubuk.classList.toggle('on', ac);
    });
    cubukIO.observe(b);
  }

  // Sepet çekmecesi: sepet.html sayfası iframe'de (aynı sepet bileşeni)
  var cek = null;
  function cekmeceAc() {
    if (TEK) { git('sepet.html'); return; }
    var u_ = ust(); if (u_) { u_.Ayluna.cekmeceAc(); return; }
    if (!cek) {
      cek = el('<div class="ay-katman ay-cek" role="dialog" aria-modal="true" aria-label="Sepet"><div class="ay-perde" data-kapat></div><div class="ay-panel sag"><iframe title="Sepet" src="sepet.html"></iframe></div></div>');
      document.body.appendChild(cek);
      cek.addEventListener('click', function (e) { if (e.target.closest('[data-kapat]')) cekmeceKapat(); });
    } else { try { cek.querySelector('iframe').contentWindow.location.reload(); } catch (e) {} }
    cek.classList.add('on'); kilit(1);
    setTimeout(function () { var ok = false; try { var d = cek.querySelector('iframe').contentWindow.document; ok = !!(d.getElementById('kok') && d.getElementById('kok').childElementCount); } catch (e) {} if (!ok && cek.classList.contains('on')) { cekmeceKapat(); git('sepet.html'); } }, 2500);
  }
  function cekmeceKapat() { var u_ = ust(); if (u_) { u_.Ayluna.cekmeceKapat(); return; } if (cek) cek.classList.remove('on'); kilit(0); }

  // Kapıda ödeme formu (canlıda EasySell; burada aynı alanlar, ₺80 ücret, siparişe özel teklifler, "Bekle!" kartla %5)
  var kf = null;
  var ILLER = 'Adana,Adıyaman,Afyonkarahisar,Ağrı,Aksaray,Amasya,Ankara,Antalya,Ardahan,Artvin,Aydın,Balıkesir,Bartın,Batman,Bayburt,Bilecik,Bingöl,Bitlis,Bolu,Burdur,Bursa,Çanakkale,Çankırı,Çorum,Denizli,Diyarbakır,Düzce,Edirne,Elazığ,Erzincan,Erzurum,Eskişehir,Gaziantep,Giresun,Gümüşhane,Hakkari,Hatay,Iğdır,Isparta,İstanbul,İzmir,Kahramanmaraş,Karabük,Karaman,Kars,Kastamonu,Kayseri,Kilis,Kırıkkale,Kırklareli,Kırşehir,Kocaeli,Konya,Kütahya,Malatya,Manisa,Mardin,Mersin,Muğla,Muş,Nevşehir,Niğde,Ordu,Osmaniye,Rize,Sakarya,Samsun,Şanlıurfa,Siirt,Sinop,Şırnak,Sivas,Tekirdağ,Tokat,Trabzon,Tunceli,Uşak,Van,Yalova,Yozgat,Zonguldak'.split(',');
  function kapidaAc() {
    var u_ = ust(); if (u_) { u_.Ayluna.kapidaAc(); return; }
    cekmeceKapat();
    if (!Sepet.oku().satirlar.length) { bildir('Sepetin boş'); return; }
    if (!kf) {
      kf = el('<div class="ay-katman ay-kf" role="dialog" aria-modal="true" aria-labelledby="kf-b"><div class="ay-perde"></div><form class="ay-panel alt" novalidate>' +
        '<div class="ay-p-ust"><b id="kf-b">Kapıda ödeme</b><button type="button" class="ay-x" data-vazgec aria-label="Formu kapat"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"></path></svg></button></div>' +
        '<div class="kf-ic"><div class="kf-ozet"></div>' +
        '<label>Ad soyad<input name="ad" autocomplete="name" required></label>' +
        '<label>Telefon<input name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="05xx xxx xx xx" required></label>' +
        '<div class="kf-iki"><label>İl<select name="il" required><option value="">Seç</option>' + ILLER.map(function (i) { return '<option>' + i + '</option>'; }).join('') + '</select></label>' +
        '<label>İlçe<input name="ilce" required></label></div>' +
        '<label>Açık adres<textarea name="adres" rows="2" placeholder="Mahalle, sokak, no, daire" required></textarea></label>' +
        '<div class="kf-ek"></div><div class="kf-top"></div>' +
        '<p class="kf-hata" role="alert"></p>' +
        '<button class="ay-btn" type="submit">Siparişi tamamla</button>' +
        '<p class="kf-not">Ödemeyi ürün kapına geldiğinde nakit ya da kartla yaparsın. Siparişin WhatsApp\'tan onaylanır.</p></div></form>' +
        '<div class="kf-bekle" hidden><div><b>Bekle!</b><p>Kartla ödersen %5 indirim kazanırsın, kapıda ödeme ücreti de olmaz.</p>' +
        '<button type="button" class="ay-btn" data-karta>Kartla öde, %5 kazan</button><button type="button" class="ay-btn2" data-devam>Kapıda ödemeye devam</button><button type="button" class="ay-lnk" data-kapat>Vazgeç</button></div></div></div>');
      document.body.appendChild(kf);
      var f = kf.querySelector('form');
      kf.addEventListener('click', function (e) {
        var t = e.target;
        if (t.closest('[data-vazgec]') || t.classList.contains('ay-perde')) { kf.querySelector('.kf-bekle').hidden = false; return; }
        if (t.closest('[data-devam]')) { kf.querySelector('.kf-bekle').hidden = true; return; }
        if (t.closest('[data-karta]')) { kapidaKapat(); git('odeme.html'); return; }
        if (t.closest('[data-kapat]')) { kapidaKapat(); return; }
        var ek = t.closest('[data-ek]'); if (ek) { Sepet.ek(ek.getAttribute('data-ek')); kfDoldur(); }
      });
      f.addEventListener('submit', function (e) {
        e.preventDefault();
        var d = {}; ['ad', 'tel', 'il', 'ilce', 'adres'].forEach(function (k) { d[k] = (f.elements[k].value || '').trim(); });
        var hata = !d.ad ? 'Adını yaz.' : !/^0?5\d{9}$/.test(d.tel.replace(/\D/g, '')) ? 'Telefonu 05xx xxx xx xx biçiminde yaz.' : !d.il ? 'İl seç.' : !d.ilce ? 'İlçeyi yaz.' : d.adres.length < 10 ? 'Açık adresi yaz.' : '';
        kf.querySelector('.kf-hata').textContent = hata;
        if (hata) return;
        siparisVer('kapida', d);
      });
    }
    kfDoldur(); kf.querySelector('.kf-bekle').hidden = true; kf.classList.add('on'); kilit(1);
    setTimeout(function () { kf.querySelector('input[name=ad]').focus(); }, 80);
  }
  function kfDoldur() {
    var s = Sepet.oku(), t = Sepet.toplam('kapida');
    kf.querySelector('.kf-ozet').innerHTML = s.satirlar.map(function (x) { return '<div class="kf-s"><img src="' + gorsel(x.img) + '" alt=""><span><b>' + x.ad + '</b><small>' + x.varyant + (x.adet > 1 ? ' · ×' + x.adet : '') + '</small></span><em>' + TL(x.birim * x.adet) + '</em></div>'; }).join('');
    kf.querySelector('.kf-ek').innerHTML = '<p class="kf-ek-b">Siparişine ekle</p>' + EKLER.map(function (e) { var on = s.ekler && s.ekler[e.k]; return '<button type="button" class="kf-ekb' + (on ? ' on' : '') + '" data-ek="' + e.k + '" aria-pressed="' + !!on + '"><i></i><span>' + e.n + '</span><em>' + TL(e.p) + '</em></button>'; }).join('') +
      '<button type="button" class="kf-ekb' + (s.hizli ? ' on' : '') + '" data-ek="__hizli" aria-pressed="' + !!s.hizli + '"><i></i><span>Hızlı Kargo · öncelikli hazırlanır</span><em>' + TL(HIZLI) + '</em></button>';
    kf.querySelector('.kf-top').innerHTML = '<p><span>Ürünler</span><b>' + TL(t.urun + t.ek) + '</b></p><p><span>Kargo</span><b>' + (t.kargo ? TL(t.kargo) : 'Ücretsiz') + '</b></p><p><span>Kapıda ödeme ücreti</span><b>' + TL(t.kapida) + '</b></p><p class="kf-t"><span>Kapıda ödenecek</span><b>' + TL(t.toplam) + '</b></p>';
  }
  var _ek = Sepet.ek; Sepet.ek = function (k, on) { if (k === '__hizli') return Sepet.hizli(!Sepet.oku().hizli); return _ek(k, on); };
  function kapidaKapat() { if (kf) kf.classList.remove('on'); kilit(0); }

  // Sipariş: önizlemede sipariş localStorage'a yazılır, teşekkür sayfasında gösterilir
  function siparisVer(yolu, adres) {
    var s = Sepet.oku(), t = Sepet.toplam(yolu);
    var no = '#' + (1000 + Math.floor(Math.random() * 9000));
    try { localStorage.setItem('ayluna-son-siparis', JSON.stringify({ no: no, yol: yolu, adres: adres, sepet: s, toplam: t, ekler: EKLER, tarih: Date.now() })); } catch (e) {}
    Sepet.temizle(); git('siparis-alindi.html');
  }

  /* ---------- 4. Yönlendirme ---------- */
  function tekHash(u) { if (!u || u === './' || u === 'index.html') return '#'; var m = String(u).match(/^([\w-]+)\.html(\?.*)?$/); return m ? '#' + m[1] + (m[2] || '') : u; }
  function git(u) { if (TEK) { var h = tekHash(u); if (location.hash === h || (h === '#' && !location.hash)) rota(); else location.hash = h; return; } kokP().location.href = u; }
  function geri() { if (TEK) { if (history.length > 1) history.back(); else git('./'); return; } git(document.referrer && document.referrer.indexOf(location.host) >= 0 ? document.referrer : './'); }
  function norm(s) { return (s || '').toLocaleLowerCase('tr').replace(/\s+/g, ' ').trim(); }
  var ADLAR = [];
  Object.keys(V.urun).forEach(function (h) { (V.urun[h].adlar || [V.urun[h].ad]).forEach(function (a) { ADLAR.push([norm(a), h]); }); });
  ADLAR.sort(function (a, b) { return b[0].length - a[0].length; });
  function urunBul(metin) { var m = norm(metin); for (var i = 0; i < ADLAR.length; i++) if (m.indexOf(ADLAR[i][0]) >= 0) return ADLAR[i][1]; return null; }
  var YON = [[/whatsapp|iade için yaz/, 'wa'], [/ana sayfa/, './'], [/tüm ürünler|tümünü gör|ürünlere (bak|dön)|alışverişe devam/, 'tum-urunler.html'],
    [/kargo takip|siparişin nerede/, 'kargo-takip.html'], [/kargo politikası/, 'kargo.html'], [/iade/, 'iade.html'], [/gizlilik|kvkk|aydınlatma/, 'kvkk.html'],
    [/mesafeli/, 'mesafeli-satis.html'], [/ön bilgilendirme/, 'on-bilgilendirme.html'], [/hizmet şartları/, 'hizmet-sartlari.html'], [/iletişim/, 'iletisim.html'],
    [/hesabına giriş|giriş yap/, 'hesap.html']];
  function metinYonu(m) { m = norm(m); for (var i = 0; i < YON.length; i++) if (YON[i][0].test(m)) return YON[i][1]; return null; }

  var KOKEL = document.getElementById('kok') || document.body;
  var SAYFA = KOKEL.getAttribute('data-sayfa') || '', URUN = KOKEL.getAttribute('data-urun') || '';
  function sepeteAt(h, yolu) {
    var V2 = V.urun[h]; if (!V2) return;
    if (V2.stok === false) { bildir('Bu ürün şu an tükendi'); return; }
    var s = satir(h); if (!s) return;
    if (h !== URUN) { s.paket = 1; s.birim = V2.p; s.eski = V2.c; s.varyant = '1 adet' + (V2.secenek && V2.secenek.length ? ' · ' + V2.secenek[0] : ''); }
    if (h === URUN) Sepet.koy(s); else Sepet.ekle(s);
    if (yolu === 'kapida') kapidaAc(); else { cekmeceAc(); }
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest('a,button'); if (!a || a.closest('.ay-katman')) return;
    if (a.__h && a.__h.click) return;                      // bileşenin kendi işi (sekme, paket, ileri/geri…)
    var al = a.getAttribute('aria-label') || '', m = a.textContent || '';
    var href = a.getAttribute('href');
    if (sepetDugmesi(al)) { e.preventDefault(); if (SAYFA !== 'sepet') cekmeceAc(); return; }
    if (al === 'Menü') { e.preventDefault(); menuAc(); return; }
    if (al === 'Ara') { e.preventDefault(); git('arama.html'); return; }
    if (al === 'Yukarı çık') { e.preventDefault(); window.scrollTo({ top: 0, behavior: 'smooth' }); return; }
    if (a.classList.contains('marka') || al === 'Ayluna ana sayfa') { e.preventDefault(); git('./'); return; }
    var du = a.getAttribute('data-url'); if (du) { e.preventDefault(); git(du); return; }
    if (a.hasAttribute('data-wa') || /whatsapp/i.test(m) && href === '#') { e.preventDefault(); bildir('WhatsApp numarası: [teyit]. Canlıda wa.me bağlantısı açılır.'); return; }
    // Ürün sayfası: satın alma butonları
    if (a.tagName === 'BUTTON' && URUN && SAYFA === 'urun') {
      if (a.disabled) return;
      if (a.matches('.btn2,.btn-kp')) { e.preventDefault(); if (/haber ver/i.test(m)) { bildir('Gelince haber vereceğiz (önizleme)'); return; } sepeteAt(URUN, 'kapida'); return; }
      if (a.matches('.btn1,.btn-on')) { e.preventDefault(); sepeteAt(URUN, 'kart'); return; }
    }
    // Koleksiyon / kartlardaki "Sepete ekle"
    if (a.tagName === 'BUTTON' && /sepete ekle/i.test(m)) { var kart = a.closest('.uk,.kart'); var hh = kart && urunBul(kart.textContent); if (hh) { e.preventDefault(); sepeteAt(hh, 'kart'); } return; }
    if (a.tagName !== 'A') return;
    if (href && href !== '#' && href.charAt(0) === '#') { if (TEK) { e.preventDefault(); var hed = document.getElementById(href.slice(1)); if (hed) hed.scrollIntoView({ behavior: 'smooth', block: 'start' }); } return; }  // sayfa içi çapa
    e.preventDefault();
    var h2 = urunBul(m) || urunBul(a.getAttribute('aria-label'));
    var y = metinYonu(m);
    if (y === 'wa') { bildir('WhatsApp numarası: [teyit]. Canlıda wa.me bağlantısı açılır.'); return; }
    if (/^(gece lambası|projektör|nemlendirici|lunadream)$/i.test(norm(m))) { git('arama.html?q=' + encodeURIComponent(m.trim())); return; }
    if (h2 && !y) { git(h2 + '.html'); return; }
    if (y) { git(y); return; }
    if (h2) { git(h2 + '.html'); return; }
    if (href && href !== '#') git(href);
  }, true);
  // Kart div'leri (koleksiyon ızgarası): karta dokununca ürüne git
  document.addEventListener('click', function (e) {
    if (e.defaultPrevented) return;
    var k = e.target.closest('.uk'); if (!k || e.target.closest('button,a')) return;
    var h = urunBul(k.textContent); if (h) git(h + '.html');
  });
  // Formlar: önizlemede gönderim yerine onay
  document.addEventListener('submit', function (e) {
    var f = e.target; if (f.closest('.ay-katman') || f.hasAttribute('data-kendi')) return;
    e.preventDefault();
    var bos = Array.prototype.filter.call(f.querySelectorAll('input[type=email],input[type=text],input[type=tel],textarea'), function (i) { return !i.value.trim(); });
    if (bos.length) { bildir('Lütfen alanları doldur'); bos[0].focus(); return; }
    var msj = SAYFA === 'kargo-takip' ? 'Canlıda Track123 sonucu burada görünür (önizleme)' : SAYFA === 'iletisim' ? 'Mesajın alındı; en geç 2 saat içinde dönüyoruz (önizleme)' : SAYFA === 'hesap' ? 'Giriş kodu e-postana gönderildi (önizleme)' : 'Kaydın alındı, %5 kodun e-postana gelecek (önizleme)';
    bildir(msj); f.reset();
  }, true);
  window.addEventListener('message', function (e) { var d = e.data || {}; if (d.ayluna === 'kapat') cekmeceKapat(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { menuKapat(); cekmeceKapat(); if (kf && kf.classList.contains('on')) kf.querySelector('.kf-bekle').hidden = false; } });

  /* Her çizimden sonra: sepet rozeti */
  // Başlıktaki sepet düğmesi: "Sepet" ya da "Sepet, 0 ürün" (çekmecedeki "Sepeti kapat" değil)
  function sepetDugmesi(al) { return al === 'Sepet' || al.indexOf('Sepet,') === 0; }
  function suslen() {
    var n = Sepet.sayi();
    var b = document.querySelectorAll('[aria-label^="Sepet"]');
    for (var i = 0; i < b.length; i++) { if (b[i].closest('.ay-katman') || !sepetDugmesi(b[i].getAttribute('aria-label'))) continue; if (b[i].getAttribute('data-ay-adet') !== String(n)) b[i].setAttribute('data-ay-adet', String(n)); }
    document.documentElement.classList.toggle('ay-asagi', (window.scrollY || 0) > 400);
  }
  window.addEventListener('scroll', function () { document.documentElement.classList.toggle('ay-asagi', (window.scrollY || 0) > 400); }, { passive: true });

  function rota() {
    var h = location.hash.slice(1), ad = decodeURIComponent(h.split('?')[0] || 'index'), T = window.AYLUNA_SAYFALAR || {};
    var P = T[ad] || T['404'];
    if (C && C.componentWillUnmount) try { C.componentWillUnmount(); } catch (e) {}
    menuKapat(); kapidaKapat();
    document.getElementById('sayfa-css').textContent = P.css;
    document.documentElement.style.setProperty('--ay-zemin', P.zemin);
    document.body.style.setProperty('--ay-zemin', P.zemin);
    document.title = P.title;
    kok = document.getElementById('kok'); kok.setAttribute('data-sayfa', P.tur); kok.setAttribute('data-urun', P.urun || '');
    SAYFA = P.tur; URUN = P.urun || '';
    sablon = document.getElementById('T-' + (T[ad] ? ad : '404')).content;
    while (kok.firstChild) kok.removeChild(kok.firstChild);
    masaUst();
    ilk = true; planli = false; C = new (P.js())({}); window.scrollTo(0, 0); ciz(); cubukKur();
  }

  window.Ayluna = {
    tek: TEK, geri: geri, gorsel: gorsel, baslatTek: function () { window.addEventListener('hashchange', rota); rota(); },
    baslat: function (Comp) {
      kok = document.getElementById('kok'); sablon = document.getElementById('T').content;
      masaUst(); C = new Comp({}); ciz(); cubukKur();
    },
    cekmeceAc: cekmeceAc, cekmeceKapat: cekmeceKapat, cekmecede: function () { return !!ust(); }, kapidaAc: kapidaAc, kapidaKapat: kapidaKapat, menuAc: menuAc, git: git, siparisVer: siparisVer, bildir: bildir, TL: TL, satir: satir, urunBul: urunBul,
    odemeyeGec: function () { if (!Sepet.oku().satirlar.length) { bildir('Sepetin boş'); return; } git('odeme.html'); }
  };
  document.addEventListener('DOMContentLoaded', suslen);
})();
