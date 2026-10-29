/* Ayluna site önizlemesi · ortak çalışma zamanı (18 Eki)
   1) Tuval sayfalarının (.dc.html) şablonunu çalıştırır: {{delik}}, sc-for, sc-if, onClick; her çizimde DOM'u yerinde yamar
      (öğeler korunur: kaydırma, geçiş ve animasyonlar bozulmaz; açılan <details> açık kalır).
   2) Sepet deposu (localStorage), sepet çekmecesi, kapıda ödeme formu (EasySell yerine), menü, arama, yönlendirme.
   Shopify'da bu işlerin karşılığı: sepet = /cart.js + /cart/add.js, kapıda ödeme = EasySell, ödeme = Shopify checkout.
   3) Shopify kipi (window.AYLUNA_SHOPIFY, tema: araclar/tema/tema_uret.py): sepet Shopify sepeti, adresler mağaza adresleri,
      fiyat ve stok canlı ürünlerden (AYLUNA_CANLI), görseller tema dosyalarından (AYLUNA_GORSEL), kapıda ödeme EasySell. */
(function () {
  'use strict';
  var V = window.AYLUNA_VERI || { urun: {}, sira: [] };
  var SHOP = !!window.AYLUNA_SHOPIFY, AYAR = window.AYLUNA_AYAR || {};
  if (SHOP) document.documentElement.classList.add('ay-shop');  // Shopify'da tasarımdaki Kapıda düğmeleri gizli (ayluna.css)
  // Shopify: görseller tema dosyalarından; fiyat, stok ve varyantlar mağazanın kendisinden (panoya yazılı fiyat yalnız ilk değer)
  var TUVAL_FIYAT = {};
  if (SHOP) {
    if (window.AYLUNA_GORSEL) V.blob = window.AYLUNA_GORSEL;
    var CANLI = window.AYLUNA_CANLI || {};
    Object.keys(V.urun).forEach(function (h) {
      var u = V.urun[h], c = CANLI[h]; TUVAL_FIYAT[h] = u.p;
      if (!c) { u.yok = true; return; }
      u.p = c.p / 100; u.c = c.c > c.p ? c.c / 100 : null; u.stok = !!c.stok; u.vid = c.vid; u.vs = c.v || []; u.url = c.url; u.dun = c.dun; u.kd = c.kd;
    });
    // Ürün kartı görselleri (28 Eki): tasarımdaki kart görseli (V.kart: görsel kimliği → ürün) Shopify'daki ürünün ana görseliyle değişir
    // (tema ayarı "Ürün görselleri Shopify'dan"; kapalıysa CANLI'da img yok, tasarım görseli kalır)
    if (V.kart) Object.keys(V.kart).forEach(function (id) { var c = CANLI[V.kart[id]]; if (c && c.img) { V.blob = V.blob || {}; V.blob[id] = c.img; } });
  }
  var TL = function (n) { var s = (Math.round(n * 100) / 100).toFixed(2).split('.'); return '₺' + s[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.') + ',' + s[1]; };
  var HTMLNS = 'http://www.w3.org/1999/xhtml';
  // Tek dosya kipi (site-tek/index.html): bütün sayfalar tek dosyada, adres #sayfa ile değişir
  var TEK = !!window.AYLUNA_TEK;
  // Blok içi görsel seçicileri (28 Eki, kullanıcı: "odası böyle görünecekteki görselleri de değiştirmek istiyorum ama sabit"): her blok
  // seçilen görselleri <script class="ay-gorsel-esle"> içinde verir (tasarımdaki görselin kimliği → Shopify görseli); tasarım görselinin yerine geçer.
  var BLOB0 = V.blob ? Object.assign({}, V.blob) : null;  // seçim temizlenirse tasarım görseline dönmek için
  function gorselEsle() {
    if (!SHOP) return;
    if (BLOB0) V.blob = Object.assign({}, BLOB0);
    var e = document.querySelectorAll('script.ay-gorsel-esle');
    for (var i = 0; i < e.length; i++) {
      try { var m = JSON.parse(e[i].textContent); Object.keys(m).forEach(function (k) { if (/^[0-9a-f]{32}$/.test(k) && m[k]) { V.blob = V.blob || {}; V.blob[k] = m[k]; } }); } catch (x) {}
    }
  }
  gorselEsle();
  function gorsel(u) { return String(u || '').replace(/\/_blob\/([0-9a-f]{32})/g, function (m, i) { return (V.blob && V.blob[i]) || m; }); }

  /* ---------- 1. Şablon motoru ---------- */
  var kok = null, sablon = null, C = null, planli = false, ilk = true;
  // Shopify bölümleri (28 Eki, kullanıcı: "sectionları tek tek bölümler kısmında görüp düzenleyebileceğim hale getir"): her bölüm
  // kendi parçasını taşır (template.ay-parca + hemen ardından .ay-kok); hepsi tek bileşenle, aynı durumla çizilir
  var parcalar = null;
  function parcaTopla() {
    var t = document.querySelectorAll('template.ay-parca'), l = [];
    for (var i = 0; i < t.length; i++) { var k = t[i].nextElementSibling; if (k && k.classList.contains('ay-kok')) l.push({ s: t[i].content, k: k }); }
    return l.length ? l : null;
  }
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
    if (el.hasAttribute('data-ay-dis') || el.hasAttribute('data-ay-dolu')) return;  // uygulama yuvası (EasySell düğmesi, uygulama blokları) ve dolan yorum kutusu: içi bizim değil
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
    if (parcalar) parcalar.forEach(function (p) { var o = []; for (var c2 = p.s.firstChild; c2; c2 = c2.nextSibling) vyap(c2, vals, o); cocuklar(p.k, o); });
    else { for (var c = sablon.firstChild; c; c = c.nextSibling) vyap(c, vals, out); cocuklar(kok, out); }
    // Süsleme (rozet, EasySell işareti, gizli form) hata verse de sayfanın hareketleri (galeri, kaydırma) başlasın
    try { suslen(); } catch (e) { if (window.console) console.warn('Ayluna: süsleme', e); }
    if (ilk) { ilk = false; if (C.componentDidMount) C.componentDidMount(); }
    else if (C.componentDidUpdate) C.componentDidUpdate();
  }
  function planla() { if (planli || !C) return; planli = true; (window.requestAnimationFrame || setTimeout)(ciz); }

  /* ---------- 2. Sepet deposu ---------- */
  var ANAHTAR = 'ayluna-sepet-v1';
  var EKLER = V.ekler || [];
  var HIZLI = 79.99, KAPIDA = 80;
  function oku() {
    if (SHOP) return SC;
    try { var s = JSON.parse(localStorage.getItem(ANAHTAR)); if (s && s.satirlar) return s; } catch (e) {} return { satirlar: [], ekler: {}, hizli: false };
  }
  /* Shopify sepeti: /cart.js ↔ bileşenlerin beklediği biçim. Siparişe özel teklifler "_ek" özelliğiyle ayrı tutulur. */
  function scCevir(c) {
    var s = { satirlar: [], ekler: {}, hizli: false, adetS: 0, ham: c };
    ((c && c.items) || []).forEach(function (it) {
      var p = it.properties || {};
      if (p._ek) { s.ekler[p._ek] = it.key; s.adetS += it.quantity; return; }
      var vt = it.variant_title && it.variant_title !== 'Default Title' ? it.variant_title : '';
      s.satirlar.push({ id: it.key, key: it.key, vid: it.variant_id, h: it.handle, ad: it.product_title, varyant: p._secim || vt || '1 adet', paket: +(p._paket || 1),
        birim: it.final_line_price / 100 / it.quantity, eski: it.original_line_price > it.final_line_price ? it.original_line_price / 100 / it.quantity : null,
        img: it.image || (V.urun[it.handle] && V.urun[it.handle].img) || '', adet: it.quantity });
      s.adetS += it.quantity;
    });
    return s;
  }
  var SC = scCevir(window.AYLUNA_SEPET);
  // Sepete ekleme: kalemler zaten Kaching özelliğini taşır; kaching_bundles=true Kaching'in isteği kendi seçimiyle değiştirmesini önler
  // (yoksa 2'li pakette Kız + Erkek iki aynı modele dönebilir)
  function scIstek(yol, govde) {
    if (yol === '/cart/add.js') yol += '?kaching_bundles=true';
    return fetch(yol, govde ? { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(govde) } : { headers: { Accept: 'application/json' } })
      .then(function (r) { return r.json().then(function (j) { if (!r.ok) throw new Error(j.description || j.message || 'Sepet hatası'); return j; }); });
  }
  function scYukle() { return scIstek('/cart.js').then(function (c) { SC = scCevir(c); haber(); return SC; }); }
  function scHata(e) { bildir(e && e.message ? e.message : 'Sepet güncellenemedi'); scYukle(); }
  // Seçimi Shopify kalemlerine çevir: LunaDream'de model = varyant (Kız/Erkek), paket = adet
  function kalemler(sat) {
    var U = V.urun[sat.h] || {}, n = sat.paket || 1, vs = U.vs || [], ozellik = { _secim: sat.varyant, _paket: String(n) };
    var kb = SHOP && sat.h === URUN ? kachingOzellik(n) : null; if (kb) ozellik.__kaching_bundles = kb;  // paket indirimi (Kaching)
    function vBul(anahtar) { for (var i = 0; i < vs.length; i++) if (vs[i].t.toLocaleLowerCase('tr').indexOf(anahtar) >= 0) return vs[i].id; return U.vid; }
    if (sat.h === 'lunadream-gece-lambasi' && sat.modeller) {
      var say = {}; sat.modeller.forEach(function (m) { var id = vBul(m === 'erkek' ? 'erkek' : 'kız'); say[id] = (say[id] || 0) + 1; });
      return Object.keys(say).map(function (id) { return { id: +id, quantity: say[id], properties: ozellik }; });
    }
    if (U.secenek && U.secenek.length && sat.secIndex != null && vs[sat.secIndex]) return [{ id: vs[sat.secIndex].id, quantity: n, properties: ozellik }];
    return [{ id: U.vid, quantity: n, properties: ozellik }];
  }
  function yaz(s) { try { localStorage.setItem(ANAHTAR, JSON.stringify(s)); } catch (e) {} haber(); }
  function haber() { try { window.dispatchEvent(new CustomEvent('ayluna-sepet')); } catch (e) {} suslen(); if (C) planla(); }
  var Sepet = SHOP ? {
    oku: oku,
    ekle: function (sat) { return scIstek('/cart/add.js', { items: kalemler(sat) }).then(scYukle).catch(scHata); },
    koy: function (sat) {
      var sil = {}; SC.satirlar.forEach(function (x) { if (x.h === sat.h) sil[x.key] = 0; });
      var once = Object.keys(sil).length ? scIstek('/cart/update.js', { updates: sil }) : Promise.resolve();
      return once.then(function () { return scIstek('/cart/add.js', { items: kalemler(sat) }); }).then(scYukle).catch(scHata);
    },
    adet: function (id, n) { return scIstek('/cart/change.js', { id: id, quantity: Math.max(1, Math.min(9, n)) }).then(function (c) { SC = scCevir(c); haber(); }).catch(scHata); },
    sil: function (id) { return scIstek('/cart/change.js', { id: id, quantity: 0 }).then(function (c) { SC = scCevir(c); haber(); }).catch(scHata); },
    ek: function (k) {
      var e = EKLER.filter(function (x) { return x.k === k; })[0], U = e && V.urun[e.h]; if (!e) return;
      if (SC.ekler[k]) return scIstek('/cart/change.js', { id: SC.ekler[k], quantity: 0 }).then(function (c) { SC = scCevir(c); haber(); }).catch(scHata);
      if (!U || !U.vid || U.stok === false) { bildir('Bu ürün şu an eklenemiyor'); return; }
      return scIstek('/cart/add.js', { items: [{ id: U.vid, quantity: 1, properties: { _ek: k } }] }).then(scYukle).catch(scHata);
    },
    hizli: function () {},
    temizle: function () { return scIstek('/cart/clear.js', {}).then(scYukle); },
    sayi: function () { return SC.adetS; },
    toplam: function (yolu) {
      var urun = SC.ham ? SC.ham.total_price / 100 : 0, ind = 0, kp = yolu === 'kapida' ? KAPIDA : 0;
      return { urun: urun, ek: 0, kargo: 0, indirim: ind, kapida: kp, toplam: Math.round((urun - ind + kp) * 100) / 100 };
    },
    yukle: scYukle, EKLER: EKLER, HIZLI: HIZLI, KAPIDA: KAPIDA, TL: TL
  } : {
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
      var kargo = s.hizli ? HIZLI : 0, ind = 0, kp = yolu === 'kapida' ? KAPIDA : 0;
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
    var modeller = null, secIndex = null;
    if (h === 'lunadream-gece-lambasi') { var M = { kiz: 'Kız (Tavşanlı)', erkek: 'Erkek (Robot)' }; modeller = n === 2 ? [S.model || 'kiz', S.l2 || S.model || 'kiz'] : [S.model || 'kiz']; varyant.push(modeller.map(function (m) { return M[m]; }).join(' + ')); }
    else if (U.secenek && U.secenek.length) { secIndex = S.sec || 0; varyant.push(U.secenek[secIndex]); }
    return { h: h, ad: U.ad, varyant: varyant.join(' · '), paket: n, birim: birim, eski: eski, img: U.img, adet: 1, modeller: modeller, secIndex: secIndex };
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

  // Menü (29 Eki, kullanıcı: Yılbaşı Projektör ana menüye; mevsim ürünü, ürünlerin başında)
  var MENU = [['Ana sayfa', './'], ['Ara', 'arama.html'], ['Tüm ürünler', 'tum-urunler.html'], ['Yılbaşı Projektör', 'yilbasi-agaci-projektor-lamba.html'], ['LunaDream Gece Lambası', 'lunadream-gece-lambasi.html'], ['Galaxy USB Projektör', 'galayx-usb-projektor.html'],
    ['Ayluna AyFeneri', 'lamba.html'], ['Galaksi Night Projektör', 'ayluna-galaksi-night-projektor.html'], ['Kargo takip', 'kargo-takip.html'], ['İade ve değişim', 'iade.html'], ['İletişim', 'iletisim.html']];
  var menu = null;
  function menuAc() {
    if (!menu) {
      menu = el('<div class="ay-katman ay-menu" role="dialog" aria-modal="true" aria-label="Menü"><div class="ay-perde" data-kapat></div><nav class="ay-panel sol">' +
        '<div class="ay-p-ust"><b>Ayluna</b><button type="button" class="ay-x" data-kapat aria-label="Menüyü kapat"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"></path></svg></button></div>' +
        '<ul>' + MENU.map(function (m) { return '<li><a href="' + adres(m[1]) + '">' + m[0] + '<svg viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"></path></svg></a></li>'; }).join('') + '</ul></nav></div>');
      document.body.appendChild(menu);
      menu.addEventListener('click', function (e) {
        if (e.target.closest('[data-kapat]')) { menuKapat(); return; }
        var a = e.target.closest('a[href]'); if (!a) return;
        e.preventDefault();
        menuKapat(); git(a.getAttribute('href'));
      });
    }
    menu.classList.add('on'); kilit(1);
    setTimeout(function () { var a = menu.querySelector('a'); if (a) a.focus(); }, 60);
  }
  function menuKapat() { if (menu) menu.classList.remove('on'); kilit(0); }

  /* Masaüstü (kullanıcı, 19 Eki: "mağazanın masaüstü görünüşünü de yapmak lazım"): 1024px ve üstünde ortak üst menü.
     Sayfaların telefon başlıkları o genişlikte gizlenir (ayluna.css); bağlantı ve düğmeler genel yönlendirmeden geçer. */
  var MASA = [['Tüm ürünler', 'tum-urunler.html', 'koleksiyon'], ['Yılbaşı Projektör', 'yilbasi-agaci-projektor-lamba.html', 'yilbasi-agaci-projektor-lamba'], ['LunaDream', 'lunadream-gece-lambasi.html', 'lunadream-gece-lambasi'], ['Galaxy USB', 'galayx-usb-projektor.html', 'galayx-usb-projektor'],
    ['AyFeneri', 'lamba.html', 'lamba'], ['Galaksi Night', 'ayluna-galaksi-night-projektor.html', 'ayluna-galaksi-night-projektor'], ['Kargo takip', 'kargo-takip.html', 'kargo-takip'], ['İletişim', 'iletisim.html', 'iletisim']];
  var IC = function (d) { return '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true">' + d + '</svg>'; };
  var masa = null;
  // Masaüstü sınırı geçilince (pencere boyu) yeniden çiz: özellik kartları telefonda satın alma kutusunda, masaüstünde galerinin altında
  if (window.matchMedia) { var mq = matchMedia('(min-width: 1024px)'); if (mq.addEventListener) mq.addEventListener('change', planla); else if (mq.addListener) mq.addListener(planla); }
  function masaUst() {
    document.documentElement.setAttribute('data-ay-tur', SAYFA);
    if (!masa) {
      masa = el('<header class="ay-masa"><div class="ay-masa-ic"><a class="ay-logo" href="' + adres('./') + '" aria-label="Ayluna ana sayfa"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="rgba(255,255,255,.6)" stroke-width="1.6"></circle><path d="M12 2a10 10 0 0 1 0 20a7 10 0 0 0 0-20Z" fill="#F2A65A"></path></svg><b>Ayluna</b></a>' +
        '<nav aria-label="Ana menü">' + MASA.map(function (m) { return '<a href="' + adres(m[1]) + '" data-k="' + m[2] + '">' + m[0] + '</a>'; }).join('') + '</nav>' +
        '<div class="ay-masa-sag"><a href="' + adres('arama.html') + '" aria-label="Ara">' + IC('<circle cx="11" cy="11" r="6.5"></circle><path d="M20 20l-4.2-4.2"></path>') + '</a>' +
        '<a href="' + adres('hesap.html') + '" aria-label="Hesap">' + IC('<circle cx="12" cy="8.5" r="3.6"></circle><path d="M4.5 20a7.5 7.5 0 0 1 15 0"></path>') + '</a>' +
        '<button type="button" aria-label="Sepet">' + IC('<path d="M6 8h12l-1 12H7z"></path><path d="M9 8a3 3 0 0 1 6 0"></path>') + '</button></div></div></header>');
      document.body.insertBefore(masa, document.body.firstChild);
    }
    var k = SAYFA === 'urun' ? URUN : SAYFA, l = masa.querySelectorAll('nav a');
    for (var i = 0; i < l.length; i++) { if (l[i].getAttribute('data-k') === k) l[i].setAttribute('aria-current', 'page'); else l[i].removeAttribute('aria-current'); }
    // Üst blok renk döngüsü (kullanıcı, 25 Eki): beyaz ↔ lacivert, yalnız opacity. Bütün lacivert katmanlar (sayfadaki .gk ve buradaki kopya)
    // aynı saate bağlı: 16 sn'lik döngüde aynı an. Masaüstü başlığının lacivert kopyası dokunulmaz, ekran okuyucu görmez.
    document.documentElement.style.setProperty('--rd-t', (-(Date.now() % 16000) / 1000).toFixed(2) + 's');
    var g = masa.querySelector('.gk'); if (g) masa.removeChild(g);
    g = document.createElement('div'); g.className = 'gk'; g.setAttribute('aria-hidden', 'true'); g.setAttribute('inert', '');
    g.appendChild(masa.querySelector('.ay-masa-ic').cloneNode(true));
    [].forEach.call(g.querySelectorAll('a,button'), function (x) { if (sepetDugmesi(x.getAttribute('aria-label') || '')) x.classList.add('gk-sepet'); x.removeAttribute('href'); x.removeAttribute('aria-label'); x.setAttribute('tabindex', '-1'); });
    masa.appendChild(g);
  }

  // Masaüstü yapışkan satın alma çubuğu (eleştirmen önerisi, kullanıcı seçti 19 Eki): sayfanın satın alma butonu
  // ekranın üstünden çıkınca menünün altından iner. Ürün, seçim ve kartla al butonu (sayfadaki etiketin aynısı).
  // Yalnız transform/opacity; sayaç yok; telefonda görünmez (oradaki yapışkan çubuk sayfanın kendisinde).
  var cubuk = null, cubukIO = null, cubukKay = false;
  function anaBtn() { return document.querySelector('.ay-kok .urun-ust .btn-on, .ay-kok .urun-ust .btn1'); }
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
        '<button type="button" class="ay-al-btn" data-al><span data-l></span></button></div></div>');  // kapıda ödeme kaldırıldı (27 Eki)
      document.body.appendChild(cubuk);
      cubuk.addEventListener('click', function (e) {
        if (e.target.closest('[data-al]')) sepeteAt(URUN, 'kart');
      });
    }
    cubuk.querySelector('img').src = gorsel(U.img); cubuk.querySelector('b').textContent = U.ad;
    cubukIO = new IntersectionObserver(function (g) {
      var x = g[0], ac = !x.isIntersecting && x.boundingClientRect.top < 0;
      if (ac) cubukYaz(); cubuk.classList.toggle('on', ac);
    });
    cubukIO.observe(b);
    // Buton ilk ekranın altındaysa (23 Eki: özellik kartları satın alma kutusuna geçti) hızlı kaydırmada ya da bağlantıyla atlamada
    // buton ekrana hiç girmeden geçer, gözlemci tetiklenmez; kaydırmada butonun yerine de bakılır (kare başına bir kez)
    if (!cubukKay) { cubukKay = true; var bekle = false;
      window.addEventListener('scroll', function () { if (bekle) return; bekle = true; (window.requestAnimationFrame || setTimeout)(function () { bekle = false; cubukBak(); }); }, { passive: true }); }
    cubukBak();
  }
  function cubukBak() {
    var b = anaBtn(); if (!cubuk || !cubukIO || !b) return;
    var ac = b.getBoundingClientRect().bottom < 0;
    if (ac !== cubuk.classList.contains('on')) { if (ac) cubukYaz(); cubuk.classList.toggle('on', ac); }
  }

  // Sepet çekmecesi: sepet.html sayfası iframe'de (aynı sepet bileşeni)
  var cek = null;
  function cekmeceAc() {
    if (TEK || SHOP) { git('sepet.html'); return; }
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
  // Shopify: EasySell formu kendi düğme seçicisiyle açılır ([data-ay-kapida], EasySell ayarı). Uygulama yoksa sepete yönlendirilir.
  function easySell() { return !!(window.EASYSELL_CONFIG || window.EasySell || window.easysell || document.querySelector('[class*="es-form"],[id*="easysell"],[class*="easysell"]')); }
  function kapidaAc() {
    if (SHOP) { if (!easySell()) { bildir('Kapıda ödeme formu yüklenemedi; sepetten devam edebilirsin'); git('sepet.html'); } return; }
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
        '<p class="kf-not">Ödemeyi ürün kapına geldiğinde nakit ya da kartla yaparsın.</p></div></form>' +
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
  var ADRES = { './': '/', 'index.html': '/', 'tum-urunler.html': '/collections/all', 'sepet.html': '/cart', 'odeme.html': '/checkout', 'arama.html': '/search',
    'hesap.html': '/account', 'kargo-takip.html': AYAR.takip || '/apps/track123', 'iletisim.html': '/pages/contact', 'iade.html': '/policies/refund-policy', 'kargo.html': '/policies/shipping-policy',
    'kvkk.html': '/policies/privacy-policy', 'mesafeli-satis.html': '/policies/terms-of-service', 'on-bilgilendirme.html': '/policies/terms-of-service', 'hizmet-sartlari.html': '/policies/terms-of-service', 'siparis-alindi.html': '/' };
  function adres(u) {
    if (!SHOP) return u;
    var m = String(u || './').match(/^([^?#]*)([?#].*)?$/), y = m[1] || './', q = m[2] || '';
    if (ADRES[y]) return ADRES[y] + (y === 'arama.html' || y === 'tum-urunler.html' ? q : '');
    var h = y.match(/^([\w-]+)\.html$/);
    if (h && V.urun[h[1]]) return (V.urun[h[1]].url || '/products/' + h[1]) + q;
    return u;
  }
  function git(u) { if (SHOP) { window.location.href = adres(u); return; } if (TEK) { var h = tekHash(u); if (location.hash === h || (h === '#' && !location.hash)) rota(); else location.hash = h; return; } kokP().location.href = u; }
  function geri() { if (SHOP) { if (history.length > 1 && document.referrer.indexOf(location.host) >= 0) history.back(); else git('./'); return; } if (TEK) { if (history.length > 1) history.back(); else git('./'); return; } git(document.referrer && document.referrer.indexOf(location.host) >= 0 ? document.referrer : './'); }
  function norm(s) { return (s || '').toLocaleLowerCase('tr').replace(/\s+/g, ' ').trim(); }
  var ADLAR = [];
  Object.keys(V.urun).forEach(function (h) { (V.urun[h].adlar || [V.urun[h].ad]).forEach(function (a) { ADLAR.push([norm(a), h]); }); });
  ADLAR.sort(function (a, b) { return b[0].length - a[0].length; });
  function urunBul(metin) { var m = norm(metin); for (var i = 0; i < ADLAR.length; i++) if (m.indexOf(ADLAR[i][0]) >= 0) return ADLAR[i][1]; return null; }
  var YON = [[/bize yaz|iade için yaz/, 'iletisim.html'], [/ana sayfa/, './'], [/tüm ürünler|tümünü gör|ürünlere (bak|dön)|alışverişe devam/, 'tum-urunler.html'],
    [/kargo takip|siparişin nerede/, 'kargo-takip.html'], [/kargo politikası/, 'kargo.html'], [/iade/, 'iade.html'], [/gizlilik|kvkk|aydınlatma/, 'kvkk.html'],
    [/mesafeli/, 'mesafeli-satis.html'], [/ön bilgilendirme/, 'on-bilgilendirme.html'], [/hizmet şartları/, 'hizmet-sartlari.html'], [/iletişim/, 'iletisim.html'],
    [/hesabına giriş|giriş yap/, 'hesap.html']];
  function metinYonu(m) { m = norm(m); for (var i = 0; i < YON.length; i++) if (YON[i][0].test(m)) return YON[i][1]; return null; }

  var KOKEL = document.querySelector('.ay-kok');  // Shopify'da betik <head>'de yüklenir; sayfa türü baslat'ta okunur
  var SAYFA = KOKEL ? KOKEL.getAttribute('data-sayfa') || '' : '', URUN = KOKEL ? KOKEL.getAttribute('data-urun') || '' : '';
  function sepeteAt(h, yolu) {
    var V2 = V.urun[h]; if (!V2) return;
    if (V2.stok === false) { bildir('Bu ürün şu an tükendi'); return; }
    var s = satir(h); if (!s) return;
    if (h !== URUN) { s.paket = 1; s.birim = V2.p; s.eski = V2.c; s.varyant = '1 adet' + (V2.secenek && V2.secenek.length ? ' · ' + V2.secenek[0] : ''); }
    if (SHOP) {
      if (!V2.vid) { bildir('Bu ürün mağazada bulunamadı'); return; }
      var is_ = h === URUN ? Sepet.koy(s) : Sepet.ekle(s);
      if (yolu === 'kart') is_.then(function () { if (SC.satirlar.length) git('sepet.html'); });
      else if (h !== URUN) is_.then(function () { bildir('Sepete eklendi'); });
      return;
    }
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
    // Ürün sayfası: satın alma butonları
    if (a.tagName === 'BUTTON' && URUN && SAYFA === 'urun') {
      if (a.disabled) return;
      if (a.matches('.btn2,.btn-kp')) {
        if (/haber ver/i.test(m)) { e.preventDefault(); bildir(SHOP ? 'Stok gelince haber vermek için İletişim sayfasından yaz' : 'Gelince haber vereceğiz (önizleme)'); return; }
        if (SHOP) { formEsitle(); if (!easySell()) { e.preventDefault(); sepeteAt(URUN, 'kart'); } return; }
        e.preventDefault(); sepeteAt(URUN, 'kapida'); return;
      }
      if (a.matches('.btn1,.btn-on')) { e.preventDefault(); sepeteAt(URUN, 'kart'); return; }
    }
    // Koleksiyon / kartlardaki "Sepete ekle"
    if (a.tagName === 'BUTTON' && /sepete ekle/i.test(m)) { var kart = a.closest('.uk,.kart'); var hh = kart && urunBul(kart.textContent); if (hh) { e.preventDefault(); sepeteAt(hh, 'kart'); } return; }
    if (a.tagName !== 'A') return;
    if (href && href !== '#' && href.charAt(0) === '#') { if (TEK) { e.preventDefault(); var hed = document.getElementById(href.slice(1)); if (hed) hed.scrollIntoView({ behavior: 'smooth', block: 'start' }); } return; }  // sayfa içi çapa
    e.preventDefault();
    // Gerçek adresi olan bağlantı (menü, kart) adresine gider (28 Eki, kullanıcı: "LunaDream'e basınca direkt LunaDream'in kendi sayfasına
    // yönlendir, ürün arama kısmına değil"); metinden yön bulma yalnız adressiz (#) tasarım bağlantıları için
    if (href && href !== '#') { git(href); return; }
    var h2 = urunBul(m) || urunBul(a.getAttribute('aria-label'));
    var y = metinYonu(m);
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
  function formGonder(f) {
    var d = new FormData(), al = function (sec) { var i = f.querySelector(sec); return i ? i.value.trim() : ''; };
    var ep = al('input[type=email]'), tel = al('input[type=tel]'), ad = al('input[type=text],input:not([type])'), msj = al('textarea');
    d.append('utf8', '✓'); d.append('form_type', SAYFA === 'iletisim' ? 'contact' : 'customer');
    if (SAYFA === 'iletisim') { d.append('contact[name]', ad); d.append('contact[email]', ep); d.append('contact[phone]', tel); d.append('contact[body]', msj); }
    else { d.append('contact[email]', ep); d.append('contact[tags]', 'newsletter'); }
    return fetch('/contact', { method: 'POST', body: d, credentials: 'same-origin' });
  }
  document.addEventListener('submit', function (e) {
    var f = e.target; if (f.closest('.ay-katman') || f.hasAttribute('data-kendi')) return;
    if (SHOP && f.closest('[data-ay-shopify]')) return;  // tema formları (ürün formu vb.) kendi yolunu izler
    e.preventDefault();
    var bos = Array.prototype.filter.call(f.querySelectorAll('input[type=email],input[type=text],input[type=tel],textarea'), function (i) { return !i.value.trim(); });
    if (bos.length) { bildir('Lütfen alanları doldur'); bos[0].focus(); return; }
    if (SHOP) {
      if (SAYFA === 'kargo-takip') { git('kargo-takip.html'); return; }
      if (SAYFA === 'hesap') { git('hesap.html'); return; }
      formGonder(f).then(function () { bildir(SAYFA === 'iletisim' ? 'Mesajın alındı; en geç 2 saat içinde dönüyoruz' : 'Kaydın alındı'); f.reset(); }).catch(function () { bildir('Gönderilemedi, birazdan tekrar dene'); });
      return;
    }
    var msj = SAYFA === 'kargo-takip' ? 'Canlıda Track123 sonucu burada görünür (önizleme)' : SAYFA === 'iletisim' ? 'Mesajın alındı; en geç 2 saat içinde dönüyoruz (önizleme)' : SAYFA === 'hesap' ? 'Giriş kodu e-postana gönderildi (önizleme)' : 'Kaydın alındı, %5 kodun e-postana gelecek (önizleme)';
    bildir(msj); f.reset();
  }, true);
  window.addEventListener('message', function (e) { var d = e.data || {}; if (d.ayluna === 'kapat') cekmeceKapat(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { menuKapat(); cekmeceKapat(); if (kf && kf.classList.contains('on')) kf.querySelector('.kf-bekle').hidden = false; } });

  /* Her çizimden sonra: sepet rozeti */
  // Başlıktaki sepet düğmesi: "Sepet" ya da "Sepet, 0 ürün" (çekmecedeki "Sepeti kapat" değil)
  function sepetDugmesi(al) { return al === 'Sepet' || al.indexOf('Sepet,') === 0; }
  // Shopify: Kapıda düğmeleri EasySell seçicisiyle işaretlenir; ana sayfa kartlarında canlı fiyat; gizli ürün formu seçime eşit
  /* Kaching arkada (kullanıcı, 19 Eki: "bizim kartlar, arkada Kaching"). Temadaki gizli <kaching-bundle> kutusu:
     tasarımdaki paket kartı seçilince Kaching'de aynı adetli paket seçilir. Kapıda formu (EasySell) paketi ve indirimi bu kutudan okur;
     kartla ödemede satırlara Kaching'in __kaching_bundles özelliği yazılır, indirim bununla uygulanır. Paket seçilmediyse Kaching'e dokunulmaz
     (açılışta seçili paket yok, eski temadaki gibi; seçimsiz alım 1 adet). */
  var KB_AYAR = null;
  function kaching() { var k = document.querySelector('kaching-bundle kaching-bundles-block'); return k && k.$$c ? k : null; }
  function kachingBar(n) {
    if (!KB_AYAR) {
      var ana = document.querySelector('script.kaching-bundles-product[data-main]'), pid = ana && ana.getAttribute('data-product-id');
      var sc = (pid && document.querySelector('script.kaching-bundles-deal-block-settings[data-product-id="' + pid + '"]')) || document.querySelector('script.kaching-bundles-deal-block-settings');
      try { KB_AYAR = sc ? JSON.parse(sc.textContent) : null; } catch (e) { KB_AYAR = null; }
      if (!KB_AYAR) return null;
    }
    var b = (KB_AYAR.dealBars || []).filter(function (x) { return x.quantity === n; })[0]; return b ? b.id : null;
  }
  function kachingEsitle() {
    if (!SHOP || SAYFA !== 'urun' || !C) return;
    var k = kaching(), S = C.state || {}, n = S.adet || S.pk; if (!k || !n) return;
    var id = kachingBar(n), r = id && k.querySelector('input[type="radio"][value="' + id + '"]');
    if (r && !r.checked) r.click();
  }
  function kachingOzellik(n) {
    var k = kaching(); if (!k) return null;
    try {
      var sv = k.$$c.selectedVariants() || [], top = 0; sv.forEach(function (v) { top += v.quantity; });
      var p = sv[0] && sv[0].properties; return top === n && p && p.__kaching_bundles ? p.__kaching_bundles : null;
    } catch (e) { return null; }
  }
  // Uygulama yuvası (tasarımda satın al düğmesinin altı): EasySell düğmesi (easysell-form kancasının yanına kendisi koyar) ve
  // tema düzenleyicide ürün bölümüne eklenen uygulama blokları
  function yuvaDoldur() {
    var y = document.querySelector('.ay-kok [data-ay-dis]'); if (!y) return;
    // EasySell sayfa düğmesi yuvadan önce kurulursa gizli ürün formunun içine düşer ve görünmez; yuvaya taşınır
    var eb = document.querySelector('form[data-ay-urun-formu] .es-popup-button'); if (eb) y.appendChild(eb);
    if (y.__dolu) return; y.__dolu = 1;
    y.insertBefore(document.createElement('easysell-form'), y.firstChild);
    // Yorum uygulaması (Loox) satın alma yuvasına değil, sayfadaki yorum kutusuna (data-ay-yorum); kutu Loox gelince görünür (ayluna.css)
    var yk = document.querySelector('.ay-kok [data-ay-yorum]'), ub = document.querySelector('.ay-uygulama-bloklari');
    if (ub) while (ub.firstChild) {
      var b = ub.firstChild;
      if (yk && b.nodeType === 1 && /loox/i.test(b.innerHTML)) { if (!yk.hasAttribute('data-ay-dolu')) { yk.textContent = ''; yk.setAttribute('data-ay-dolu', ''); } yk.appendChild(b); }
      else y.appendChild(b);
    }
  }
  // Dün satırı ve stok kurdelesi: sayı ürünün ayluna.dun_satis / ayluna.stok_kurdele alanından (elle girilir, KURULUM).
  // Alan boşsa tasarımdaki sayı kalır, 0 ise satır gizlenir.
  function elleSayi() {
    var u = V.urun[URUN]; if (!u) return;
    sayiYaz('.dun', u.dun, /\d+(?= kişi)/g); sayiYaz('.stok-kd', u.kd, /\d+(?= adet)/g);
  }
  function sayiYaz(sec, n, re) {
    if (n === null || n === undefined || n === '') return;
    var el = document.querySelectorAll('.ay-kok ' + sec);
    for (var i = 0; i < el.length; i++) {
      if (!(+n > 0)) { if (!el[i].hasAttribute('data-ay-gizli')) el[i].setAttribute('data-ay-gizli', ''); continue; }
      var w = document.createTreeWalker(el[i], NodeFilter.SHOW_TEXT), t;
      while ((t = w.nextNode())) { var s = t.nodeValue.replace(re, String(Math.round(+n))); if (s !== t.nodeValue) t.nodeValue = s; }
    }
  }
  // Teyitsiz yer tutucular ([N], [foto], [teyit], [garanti]…) canlı mağazada görünmez: bulunduğu soru, madde ya da satır gizlenir
  // (28 Eki, kullanıcı: "gerçek bir shopify mağazası yapacaksın"). Uygulama yuvası ve Loox kutusu dokunulmaz.
  var YER_TUTUCU = /\[[^\]\n]{1,60}\]/;
  function yerTutucuGizle() {
    var k = document.querySelectorAll('.ay-kok');
    for (var i = 0; i < k.length; i++) {
      var w = document.createTreeWalker(k[i], NodeFilter.SHOW_TEXT), t;
      while ((t = w.nextNode())) {
        if (!YER_TUTUCU.test(t.nodeValue)) continue;
        var e = t.parentElement; if (!e || e.closest('.yer,[data-ay-dis],[data-ay-dolu],[data-ay-yorum],script,style')) continue;
        var h = e.closest('details,li,.stok,.alici,.ozet3>div') || e;
        if (!h.hasAttribute('data-ay-gizli')) h.setAttribute('data-ay-gizli', '');
      }
    }
  }
  function shopSusle() {
    yerTutucuGizle();
    var k = document.querySelectorAll('.ay-kok .btn2, .ay-kok .btn-kp');
    for (var i = 0; i < k.length; i++) if (/kapıda/i.test(k[i].textContent) && !k[i].hasAttribute('data-ay-kapida')) k[i].setAttribute('data-ay-kapida', '');
    // Sepetteki "Kapıda ödemede ₺80…" notu Kapıda düğmesiyle birlikte gizlenir (kapıda ödeme EasySell'de)
    var sn = document.querySelectorAll('.ay-kok .s-not'); for (var z = 0; z < sn.length; z++) if (/kapıda ödeme ücreti/i.test(sn[z].textContent) && !sn[z].hasAttribute('data-ay-kapida')) sn[z].setAttribute('data-ay-kapida', '');
    var kart = document.querySelectorAll('.ay-kok .uk[data-h]');
    for (var j = 0; j < kart.length; j++) {
      var u = V.urun[kart[j].getAttribute('data-h')]; if (!u || u.yok) continue;
      var st = kart[j].querySelector('.f strong'), es = kart[j].querySelector('.f s'), rz = kart[j].querySelector('em');
      if (st && st.textContent !== TL(u.p)) st.textContent = TL(u.p);
      if (es) { var et = u.c ? TL(u.c) : ''; if (es.textContent !== et) es.textContent = et; }
      if (rz && !rz.classList.contains('tukendi')) { var rt = u.c ? '%' + Math.round((1 - u.p / u.c) * 100) : ''; if (rz.textContent !== rt) rz.textContent = rt; rz.hidden = !rt; }
    }
    if (SAYFA === 'urun') { formEsitle(); kachingEsitle(); yuvaDoldur(); elleSayi(); }
  }
  // Varyant görseli (28 Eki, kullanıcı: "Erkek seçilince varyasyondaki seçtiğim ürün gelmeli"): seçilen varyantın Shopify'daki görseli
  // galeride varsa galeri ona kayar; varyantın görseli yoksa ilk görsele döner. Açılışta galeri yerinde kalır.
  var sonVar = null;
  function varyantGorsel(vid) {
    if (sonVar === null || vid === sonVar) { sonVar = vid; return; }
    sonVar = vid;
    var U = V.urun[URUN], v = U && (U.vs || []).filter(function (x) { return x.id === vid; })[0]; if (!v) return;
    var yol = function (s) { return String(s || '').split('?')[0].replace(/^https?:/, ''); };
    var resimler = document.querySelectorAll('.ay-kok .urun-ust img');
    var im = v.i ? [].filter.call(resimler, function (x) { return yol(x.getAttribute('src')) === yol(v.i); })[0] : null;
    if (v.i && !im) return;  // varyantın görseli galeride yok (galeri tasarım görselleriyle)
    var hedef = im || resimler[0];
    for (var el = hedef && hedef.parentElement; el && el !== document.body; el = el.parentElement) {
      if (el.scrollWidth > el.clientWidth + 4 && /auto|scroll/.test(getComputedStyle(el).overflowX)) {
        var sl = hedef; while (sl.parentElement !== el) sl = sl.parentElement;
        var x = im ? el.scrollLeft + sl.getBoundingClientRect().left - el.getBoundingClientRect().left : 0;
        el.scrollTo({ left: x, behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
        return;
      }
    }
  }
  function formEsitle() {
    var f = document.querySelector('form[data-ay-urun-formu]'), s = satir(URUN); if (!f || !s) return;
    var ks = kalemler(s), k = ks[0]; if (!k) return;
    varyantGorsel(k.id);
    // Kapıda ödeme (EasySell) siparişi bu listeden kurar: sepeti boşaltıp yalnız sayfadaki seçimi ekler (EasySell'in paket uygulaması kancası).
    // Yoksa önceki model sepette kalıyor, karışık 2'li pakette (Erkek + Kız) iki aynı model gidiyordu (28 Eki, kullanıcı: "varyasyon seçince
    // kapıda ödemede doğru görünmüyor").
    window.pmpr_cart_item = ks.map(function (x) { return { id: x.id, quantity: x.quantity, properties: x.properties }; });
    var ad = { id: k.id, quantity: k.quantity, 'properties[_secim]': s.varyant, 'properties[_paket]': String(s.paket || 1) };
    Object.keys(ad).forEach(function (n) { var i = f.querySelector('[name="' + n + '"]'); if (!i) { i = document.createElement('input'); i.type = 'hidden'; i.name = n; f.appendChild(i); } if (i.value !== String(ad[n])) i.value = ad[n]; });
  }
  function suslen() {
    if (SHOP) shopSusle();
    var n = Sepet.sayi();
    var b = document.querySelectorAll('[aria-label^="Sepet"]');
    for (var i = 0; i < b.length; i++) { if (b[i].closest('.ay-katman') || !sepetDugmesi(b[i].getAttribute('aria-label'))) continue; if (b[i].getAttribute('data-ay-adet') !== String(n)) b[i].setAttribute('data-ay-adet', String(n)); }
    var gs = document.querySelectorAll('.gk-sepet'); for (var j = 0; j < gs.length; j++) if (gs[j].getAttribute('data-ay-adet') !== String(n)) gs[j].setAttribute('data-ay-adet', String(n));
    document.documentElement.classList.toggle('ay-asagi', (window.scrollY || 0) > 400);
    yapisBak();
  }
  // Telefondaki yapışkan çubuk (28 Eki, kullanıcı: "çok fazla alan kaplıyor"; eleştirmenin önerisi): paketler ve ana satın al düğmesi
  // ekrandayken çubuk aşağı çekilir (data-ay-cekil; yalnız transform/opacity), ekrandan çıkınca geri gelir. Aynı anda iki düğme görünmez.
  function yapisBak() {
    var y = document.querySelectorAll('.ay-kok .yapis'); if (!y.length) return;
    // EasySell'in kendi yapışkan düğmesi açıksa bizim çubuk gizlenir; ikisi üst üste binmesin (28 Eki)
    var es = !!document.getElementById('es-sticky'); if (es !== document.documentElement.classList.contains('ay-es-yapis')) document.documentElement.classList.toggle('ay-es-yapis', es);
    var b = anaBtn(), p = document.querySelector('.ay-kok .urun-ust .pk-liste, .ay-kok .urun-ust .pk'), cek = false;
    if (b) { var ust = (p || b).getBoundingClientRect().top, alt = b.getBoundingClientRect().bottom; cek = ust < window.innerHeight - 60 && alt > 0; }
    for (var i = 0; i < y.length; i++) if (cek !== y[i].hasAttribute('data-ay-cekil')) { if (cek) y[i].setAttribute('data-ay-cekil', ''); else y[i].removeAttribute('data-ay-cekil'); }
  }
  var yapisKare = false;
  window.addEventListener('scroll', function () {
    document.documentElement.classList.toggle('ay-asagi', (window.scrollY || 0) > 400);
    if (!yapisKare) { yapisKare = true; (window.requestAnimationFrame || setTimeout)(function () { yapisKare = false; yapisBak(); }); }
  }, { passive: true });

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
      if (C) return;  // her bölüm panonun betiğini yükler; bileşen bir kez kurulur
      parcalar = parcaTopla();
      if (parcalar) { kok = parcalar[0].k; document.documentElement.classList.add('ay-coklu'); }
      else { kok = document.getElementById('kok'); sablon = document.getElementById('T').content; }
      SAYFA = kok.getAttribute('data-sayfa') || ''; URUN = kok.getAttribute('data-urun') || '';
      masaUst(); C = new Comp({}); ciz(); cubukKur(); videoKur();
      // Tema düzenleyici: bölüm eklenince, değişince, silinince ya da yeri değişince parçalar yeniden toplanır ve çizilir
      if (parcalar) ['shopify:section:load', 'shopify:section:unload', 'shopify:section:reorder'].forEach(function (ad) {
        document.addEventListener(ad, function () { setTimeout(function () { gorselEsle(); var p = parcaTopla(); if (p) { parcalar = p; kok = p[0].k; planla(); setTimeout(function () { cubukKur(); videoKur(); }, 60); } }, 0); });
      });
      // Shopify: sayfadaki tasarım fiyatı mağaza fiyatından farklıysa uyar (yalnız tema düzenleyicide ve konsolda)
      if (SHOP && SAYFA === 'urun' && V.urun[URUN] && Math.abs((TUVAL_FIYAT[URUN] || 0) - V.urun[URUN].p) > 0.009) {
        console.warn('Ayluna: tasarımdaki fiyat', TUVAL_FIYAT[URUN], 'mağaza fiyatı', V.urun[URUN].p);
        if (window.Shopify && window.Shopify.designMode) bildir('Uyarı: bu sayfadaki fiyat mağaza fiyatından farklı; temayı güncelle');
      }
    },
    fiyat: function (l) {
      // Koleksiyon/arama listeleri: Shopify'da fiyat ve stok canlı
      if (!SHOP) return l;
      return l.map(function (x) { var u = V.urun[x.h]; if (!u || u.yok) return x; var c = u.c && u.c > u.p ? u.c : null; return Object.assign({}, x, { p: u.p, c: c, var: !!u.stok }); });
    },
    shopify: SHOP, adres: adres, medya: medya, videolar: videolar,
    cekmeceAc: cekmeceAc, cekmeceKapat: cekmeceKapat, cekmecede: function () { return !!ust(); }, kapidaAc: kapidaAc, kapidaKapat: kapidaKapat, menuAc: menuAc, git: git, siparisVer: siparisVer, bildir: bildir, TL: TL, satir: satir, urunBul: urunBul,
    odemeyeGec: function () { if (!Sepet.oku().satirlar.length) { bildir('Sepetin boş'); return; } git('odeme.html'); }
  };
  document.addEventListener('DOMContentLoaded', suslen);
  // Ürün galerisi (28 Eki, kullanıcı: "görsel olarak senin içine koyduklarını çekiyor"): Shopify'da ürünün kendi görselleri
  // (layout'taki #ay-medya; tema ayarından kapatılabilir). Boşsa panodaki tasarım galerisi kalır.
  function medyaOku() {
    if (!SHOP) return null;
    var e = document.getElementById('ay-medya'); if (!e) return null;
    try { var l = JSON.parse(e.textContent); return Array.isArray(l) ? { g: l, v: [] } : l; } catch (x) { return null; }
  }
  function medya() { var m = medyaOku(); return m && m.g && m.g.length ? m.g : null; }
  // Ürün videoları (28 Eki): ürünün Shopify medyasındaki videolar. Shopify'da video yoksa boş liste (video bölümü görünmez);
  // önizlemede null (tasarımdaki kapaklar kalır)
  function videolar() {
    if (!SHOP) return null;
    // Önce video bloğunun ayarında seçilen videolar (.ay-vid-veri), yoksa ürünün medyasındaki videolar
    var b = [], e = document.querySelectorAll('.ay-vid-veri');
    for (var i = 0; i < e.length; i++) { try { b = b.concat(JSON.parse(e[i].textContent) || []); } catch (x) {} }
    b = b.filter(function (v) { return v && v.src; });
    if (b.length) return b;
    var m = medyaOku(); return m ? (m.v || []).filter(function (v) { return v && v.src; }) : [];
  }
  // Videolar (28 Eki, kullanıcı: "videolar açılmıyor"): bölüm bloklarındaki Shopify videoları. Ekrandayken sessiz döner,
  // dokununca sesli ve tam ekran. Hareket azaltılmışsa kendiliğinden dönmez.
  var vidIO = null;
  function videoKur() {
    var v = document.querySelectorAll('.ay-vid video'); if (!v.length) return;
    var az = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (vidIO) vidIO.disconnect();
    if (!az && window.IntersectionObserver) {
      vidIO = new IntersectionObserver(function (g) { g.forEach(function (x) { var t = x.target; if (!t.muted) return; if (x.isIntersecting) { var p = t.play(); if (p && p.catch) p.catch(function () {}); } else t.pause(); }); }, { threshold: .4 });
      for (var i = 0; i < v.length; i++) vidIO.observe(v[i]);
    }
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('.ay-vid'); if (!b) return;
    var v = b.querySelector('video'); if (!v) return;
    v.muted = false; v.currentTime = 0; v.setAttribute('data-ay-oynuyor', ''); var p = v.play(); if (p && p.catch) p.catch(function () {});
    var f = v.requestFullscreen || v.webkitRequestFullscreen || v.webkitEnterFullscreen; if (f) try { f.call(v); } catch (x) {}
  });
  // Shopify temasında betik defer ile yüklenir; panolar kendilerini kuyruğa koyar (window.AYLUNA_KUYRUK), burada çalışır
  var kuyruk = window.AYLUNA_KUYRUK || [];
  window.AYLUNA_KUYRUK = { push: function (f) { f(); } };
  kuyruk.forEach(function (f) { f(); });
})();
/* Loox yorumları kısa başlar; "Tüm yorumları gör" ile açılır (28 Eki) */
(function () {
  function kur() {
    var l = document.getElementById('looxReviews'), k = l && l.parentElement;
    if (!k || k.__kisa) return; k.__kisa = 1; k.classList.add('ay-loox-kisa');
    var b = document.createElement('button'); b.type = 'button'; b.className = 'ay-loox-ac'; b.textContent = 'Tüm yorumları gör';
    b.addEventListener('click', function () { k.classList.remove('ay-loox-kisa'); b.remove(); });
    k.appendChild(b);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', kur); else kur();
  setTimeout(kur, 2000);
})();

/* Politika sayfaları (28 Eki): marka başlığı, güven şeridi, "Bize yaz" kartı ve diğer politikalar */
(function () {
  var c = document.querySelector('.shopify-policy__container'); if (!c || c.__ay) return; c.__ay = 1;
  var f = document.createElement('link'); f.rel = 'stylesheet'; f.href = 'https://fonts.googleapis.com/css2?family=Figtree:wght@400;600;700&family=Young+Serif&display=swap'; document.head.appendChild(f);
  var ust = document.createElement('header'); ust.className = 'ay-pol-ust';
  ust.innerHTML = '<a href="/" aria-label="Ayluna ana sayfa"><svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="#F3B562" stroke-width="2"/><path d="M12 3a9 9 0 0 0 0 18a6 9 0 0 1 0-18z" fill="#F3B562"/></svg><b>Ayluna</b></a><a class="ay-pol-geri" href="/collections/all">Mağazaya dön</a>';
  c.parentNode.insertBefore(ust, c);
  var y = location.pathname, P = [['/policies/refund-policy', 'İade ve değişim'], ['/policies/shipping-policy', 'Kargo'], ['/policies/privacy-policy', 'Gizlilik ve KVKK'], ['/policies/terms-of-service', 'Hizmet şartları ve satış sözleşmesi']];
  var alt = document.createElement('div'); alt.className = 'ay-pol-alt';
  alt.innerHTML = '<div class="ay-pol-serit"><span>30 gün iade</span><span>Ücretsiz kargo</span><span>Kapıda ödeme</span><span>Kartla %5 indirim</span></div>' +
    '<a class="ay-pol-kart" href="/pages/contact"><span><b>Sorunun mu var?</b><small>Sipariş numaranı yaz, hemen dönelim.</small></span><i aria-hidden="true">→</i></a>' +
    '<nav class="ay-pol-diger" aria-label="Diğer politikalar">' + P.filter(function (x) { return x[0] !== y; }).map(function (x) { return '<a href="' + x[0] + '">' + x[1] + '</a>'; }).join('') + '<a href="/pages/contact">İletişim</a></nav>';
  c.parentNode.insertBefore(alt, c.nextSibling);
})();

/* Sepet baskısı (28 Eki, C2): "Ekim fiyatı 3 gün 5 sa sonra bitiyor" (İstanbul saatiyle ay sonu; mağaza fiyatı her ay yükseliyor)
   + sepetteki ürünün stok sayısı: ürün alanı ayluna.stok_kurdele; alan boşsa ürün sayfasındaki kurdeleyle aynı sayı (LunaDream 18), 0 ise kurdele yok
   (29 Eki, kullanıcı: "stok zımbırtısı görünmüyor"; canlıda alan boş olduğundan kurdele hiç çıkmıyordu) */
(function () {
  var AY = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
  var IK = '<svg viewBox="0 0 22 22" aria-hidden="true"><circle cx="11" cy="11" r="9" fill="none" stroke="#1A2142" stroke-width="1.6"/><path d="M11 2A9 9 0 0 1 11 20Z" fill="#F3B562"/></svg>';
  function kalan() {
    var ist = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/Istanbul' })), s = Math.max(0, Math.floor((new Date(ist.getFullYear(), ist.getMonth() + 1, 1) - ist) / 60000));
    var g = Math.floor(s / 1440), sa = Math.floor(s / 60) % 24, dk = s % 60;
    return { ay: AY[ist.getMonth()], t: g ? g + ' gün ' + sa + ' sa' : sa ? sa + ' sa ' + dk + ' dk' : dk + ' dk' };
  }
  var STOK0 = { 'lunadream-gece-lambasi': 18, 'yilbasi-agaci-projektor-lamba': 12 };  // ürün sayfasındaki kurdelenin tasarım sayısı (luna_e.py STOK)
  function stok() {
    var C = window.AYLUNA_CANLI || {}, S = window.AylunaSepet && window.AylunaSepet.oku ? window.AylunaSepet.oku() : null, en = null;
    ((S && S.satirlar) || []).forEach(function (x) { var c = C[x.h], k = c && c.kd, n = k === null || k === undefined || k === '' ? STOK0[x.h] : +k; if (n > 0 && (!en || n < en.n)) en = { n: n, ad: x.ad.split(' ')[0] }; });
    return en;
  }
  function ciz() {
    var el = document.querySelectorAll('.ay-bsk'); if (!el.length) return; var k = kalan(), s = stok();
    var html = '<p class="fg">' + IK + '<span>' + k.ay + ' fiyatı <b>' + k.t + '</b> sonra bitiyor</span></p>' + (s ? '<span class="kd"><i></i>' + s.ad + ': son ' + s.n + ' adet</span>' : '');
    for (var i = 0; i < el.length; i++) if (el[i].__h !== html || !el[i].firstChild) { el[i].__h = html; el[i].innerHTML = html; }
  }
  ciz(); setInterval(ciz, 30000); window.addEventListener('ayluna-sepet', function () { setTimeout(ciz, 50); });
  new MutationObserver(function () { if (document.querySelector('.ay-bsk:empty')) ciz(); }).observe(document.documentElement, { childList: true, subtree: true });
})();
