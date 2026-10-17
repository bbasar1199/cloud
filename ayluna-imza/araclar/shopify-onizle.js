// Shopify bölümlerini liquidjs ile sahte verilerle çizer; tek bir HTML sayfası üretir.
// Kullanım: npm i liquidjs@10.16.1 && node ayluna-imza/araclar/shopify-onizle.js /tmp/shopify.html
const fs=require('fs'); const path=require('path'); const {Liquid}=require('liquidjs');
const KOK=path.resolve(__dirname,'..'); const ON='file://'+KOK+'/onizleme/';
const modelOverride=process.argv[3]||'';
const L=new Liquid({jsTruthy:false});
const img=(f,w,h)=>({src:ON+'g/'+f,width:w,height:h,alt:f});
L.registerFilter('image_url',v=>v&&v.src?v.src:'');
L.registerFilter('asset_url',v=>ON+'f/'+v);
L.registerFilter('placeholder_svg_tag',()=>'<svg width="100%" height="100%"></svg>');
L.registerFilter('money_without_trailing_zeros',c=>{const x=(c/100).toFixed(2).split('.');return '₺'+x[0].replace(/\B(?=(\d{3})+(?!\d))/g,'.')+(x[1]==='00'?'':','+x[1]);});
L.registerFilter('divided_by',(a,b)=>Number.isInteger(+a)&&Number.isInteger(+b)?Math.floor(a/b):a/b);
L.registerFilter('money',c=>{const x=(c/100).toFixed(2).split('.');return '₺'+x[0].replace(/\B(?=(\d{3})+(?!\d))/g,'.')+','+x[1];});
L.registerTag('schema',{parse(t,r){this.tpl=[];const s=this.liquid.parser.parseStream(r);s.on('tag:endschema',()=>s.stop()).on('template',x=>{}).on('end',()=>{throw new Error('schema kapanmadı')});s.start();},*render(){return '';}});
L.registerTag('style',{parse(t,r){this.tpl=[];const s=this.liquid.parser.parseStream(r);s.on('tag:endstyle',()=>s.stop()).on('template',x=>this.tpl.push(x)).on('end',()=>{throw new Error('style')});s.start();},*render(ctx,em){em.write('<style>');yield this.liquid.renderer.renderTemplates(this.tpl,ctx,em);em.write('</style>');}});
L.registerTag('form',{parse(t,r){this.args=t.args;this.tpl=[];const s=this.liquid.parser.parseStream(r);s.on('tag:endform',()=>s.stop()).on('template',x=>this.tpl.push(x)).on('end',()=>{throw new Error('form')});s.start();},*render(ctx,em){em.write('<form class="ay-gizli-form" style="display:none">');yield this.liquid.renderer.renderTemplates(this.tpl,ctx,em);em.write('</form>');}});

const M=['Tavşanlı','Uzay Kaşifi'], P=[['1 lamba',169999,199900],['2 lamba',274999,399800]];
let id=1; const variants=[]; for(const m of M) for(const p of P) variants.push({id:id++,options:[m,p[0]],price:p[1],compare_at_price:p[2],available:true,title:m+' / '+p[0]});
const product={title:'LunaDream',variants,selected_or_first_available_variant:variants[0],metafields:{loox:{}},url:'#'};
const urun=(t,f,p,c)=>({title:t,url:'#',price:p,compare_at_price:c,price_varies:false,featured_image:img(f,600,600)});
const video=(n)=>({sources:[{mime_type:'video/mp4',width:720,url:ON+'v/'+n+'.mp4'}],preview_image:{src:ON+'v/'+n+'.jpg'}});
const OV={
 'ayluna-sahne':{kiz_gunduz:img('kiz-gunduz.jpg',1080,1446),kiz_gece:img('kiz-gece.jpg',1080,1446),kiz_dunya:img('kiz-dunya.jpg',731,980),kiz_elde:img('elde.jpg',470,622),erkek_gunduz:img('erkek-gunduz.jpg',731,980),erkek_gece:img('erkek-gece.jpg',731,980),erkek_dunya:img('erkek-dunya.jpg',731,980),erkek_elde:img('erkek-gunduz.jpg',731,980),tavan:img('tavan.jpg',522,355)},
 'ayluna-siparis':{ek_urun:{title:'Yıldız Işığı Nemlendirici',featured_image:img('u-yildiz.jpg',600,600),selected_or_first_available_variant:{id:99,price:84999}}},
 'ayluna-kutu':{lamba_kiz:img('elde.jpg',470,622),lamba_erkek:img('erkek-gunduz.jpg',731,980)},
 'ayluna-dunya':{resim_kiz:img('kiz-dunya.jpg',731,980),resim_erkek:img('erkek-dunya.jpg',731,980)},
 'ayluna-diski-tak':{kiz_gunduz:img('kiz-gunduz.jpg',1080,1446),kiz_gece:img('kiz-gece.jpg',1080,1446),erkek_gunduz:img('erkek-gunduz.jpg',731,980),erkek_gece:img('erkek-gece.jpg',731,980)},
 'ayluna-kardes':{kiz_gunduz:img('kiz-gunduz.jpg',1080,1446),kiz_gece:img('kiz-gece.jpg',1080,1446),erkek_gunduz:img('erkek-gunduz.jpg',731,980),erkek_gece:img('erkek-gece.jpg',731,980)},
 'ayluna-diger-isiklar':{urunler:[urun('Yıldız Işığı Nemlendirici','u-yildiz.jpg',84999,0),urun('Galaksi Night Projektör','u-galaksi.jpg',219900,0),urun('Astronot Oda Nemlendirici','u-astronot.jpg',79900,0),urun('Ayluna AyFeneri','u-ayfeneri.jpg',164999,0),urun('Sunset Lamba','u-sunset.jpg',69900,0)]},
 'ayluna-alt-bilgi':{menu:{links:['Gece lambaları','Projektörler','Nemlendiriciler','Mesafeli Satış Sözleşmesi','KVKK','İade','İletişim'].map(t=>({title:t,url:'#'}))}}
};
const BLOK={
 'ayluna-siparis':(b,i)=>({kart_resim:i===0?img('kiz-oda.jpg',731,980):img('erkek-gunduz.jpg',731,980),bento_resim:i===0?img('kiz-dunya.jpg',731,980):img('erkek-dunya.jpg',731,980)}),
 'ayluna-yorumlar':(b,i)=>b.type==='foto'?{resim:img(['ugc2.jpg','ugc1k.jpg','ugc5.jpg','ugc3.jpg','ugc4.jpg'][i/2|0],400,600)}:{},
 'ayluna-kutu':(b,i)=>({resim:img('disk'+(i+1)+'.jpg',188,188)}),
 'ayluna-dunya':(b,i)=>({resim:img(['disk2.jpg','disk4.jpg','disk3.jpg','disk6.jpg'][i],188,188)}),
 'ayluna-diski-tak':(b,i)=>({resim:img('disk'+(i+1)+'.jpg',188,188)}),
 'ayluna-bir-gece':(b,i)=>({video_kiz:video(['m1-isik','m2-disk','m3-kiz','m4-tavan','m5-kiz'][i]),video_erkek:i===2?video('m3-erkek'):i===4?video('m5-erkek'):null})
};
const SIRA=['ayluna-duyuru','ayluna-sahne','ayluna-siparis','ayluna-fayda','ayluna-yorumlar','ayluna-kutu','ayluna-dunya','ayluna-diski-tak','ayluna-bir-gece','ayluna-sss','ayluna-kardes','ayluna-diger-isiklar','ayluna-kapanis','ayluna-alt-bilgi'];
(async()=>{
  let govde='';
  for(const ad of SIRA){
    const src=fs.readFileSync(path.join(KOK,'shopify',ad+'.txt'),'utf8');
    const sch=JSON.parse(src.match(/{%\s*schema\s*%}([\s\S]*?){%\s*endschema\s*%}/)[1]);
    const ayar={}; for(const x of sch.settings||[]) if(x.id) ayar[x.id]=x.default!==undefined?x.default:(x.type==='checkbox'?false:null);
    Object.assign(ayar,OV[ad]||{});
    const pre=(sch.presets&&sch.presets[0].blocks)||[];
    const blocks=pre.map((pb,i)=>{const tip=sch.blocks.find(t=>t.type===pb.type);const st={};for(const x of tip.settings) if(x.id) st[x.id]=x.default!==undefined?x.default:null;Object.assign(st,pb.settings||{});const tipIndex=pre.slice(0,i).filter(q=>q.type===pb.type).length;Object.assign(st,BLOK[ad]?BLOK[ad](pb,pb.type==='foto'?i:tipIndex):{});return {id:'b'+i,type:pb.type,settings:st,shopify_attributes:''};});
    const html=await L.parseAndRender(src,{section:{id:ad.replace('ayluna-','s-'),settings:ayar,blocks},product,shop:{money_format:'₺{{amount_with_comma_separator}}'},routes:{root_url:'/',cart_url:'/cart',collections_url:'/collections'}});
    govde+='<div id="shopify-section-'+ad+'">'+html+'</div>\n';
  }
  fs.writeFileSync(process.argv[2],'<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Shopify bölüm testi</title><style>body{margin:0;background:#0C1027}</style></head><body>'+govde+'</body></html>');
  console.log('yazıldı');
})().catch(e=>{console.error('HATA',e.message);process.exit(1);});
