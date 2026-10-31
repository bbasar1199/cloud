const {chromium}=require('playwright');
const LCSS=`
.ay-kok .pk-liste{gap:14px!important}
.ay-kok .pk-liste>div{position:relative;background:#EDF6FF!important;border:2px solid #D3E6F8!important;border-radius:18px!important;box-shadow:none!important;overflow:visible}
.ay-kok .pk-liste>div.on{background:#fff!important;border-color:#E4AB63!important;box-shadow:0 8px 22px rgba(228,171,99,.30)!important}
.ay-kok .pk-liste .sat{min-height:96px!important;padding:10px 14px 10px 10px!important;gap:12px!important}
.ay-kok .pk-liste .tl{width:76px!important;height:76px!important;border-radius:14px!important;background:#fff!important;box-shadow:inset 0 0 0 1px #E3EEF9}
.ay-kok .pk-liste .tl img{height:64px!important;bottom:6px!important}
.ay-kok .pk-liste .tl.cift{width:84px!important}.ay-kok .pk-liste .tl.cift img{height:56px!important}
.ay-kok .pk-liste .tl.cift img:nth-child(1){left:32%!important}.ay-kok .pk-liste .tl.cift img:nth-child(2){left:68%!important}
.ay-kok .pk-liste .ad{font-size:18px!important;font-weight:800!important;color:#10182B!important}
.ay-kok .pk-liste .fiyat{font-size:18px!important;font-weight:800!important;color:#10182B!important}
.ay-kok .pk-liste .alt{color:#2E6FB0!important;font-weight:600!important}
.ay-kok .pk-liste .kurdele{background:#E4AB63!important;color:#fff!important;font-weight:800!important;border-radius:999px!important;padding:4px 12px!important;right:14px!important;top:-12px!important;box-shadow:0 3px 8px rgba(228,171,99,.4)}
.pk-hed{display:flex;align-items:center;gap:8px;margin:0 -2px -2px;padding:9px 14px;border-radius:0 0 18px 18px;background:#B3DAFF;color:#10182B;font-size:13.5px;font-weight:700}
.pk-liste>div.on .pk-hed{background:#E4AB63;color:#fff}
.pk-hed svg{width:16px;height:16px;flex:none}
`;
(async()=>{
const b=await chromium.launch({args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:2});
await p.route(/(\/cart\/(add|change|update|clear))|facebook|tiktok|google-analytics|googletagmanager|clarity|hotjar/, r=>r.abort());
await p.goto('https://ayluna.shop/products/lunadream-gece-lambasi?_cb='+Date.now(),{waitUntil:'domcontentloaded'});
await p.waitForTimeout(8000);
const ins=async(sel)=>p.evaluate(([css])=>{
  const s=document.createElement('style');s.textContent=css;document.head.appendChild(s);
  const go=()=>{document.querySelectorAll('.ay-kok .pk-liste>div').forEach((d,i)=>{if(d.querySelector('.pk-hed'))return;const h=document.createElement('div');h.className='pk-hed';h.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="2.5"/></svg>'+(i?'+ 12 masal diski hediye (kutu başı 6)':'+ 6 masal diski hediye');const k=d.querySelector('.ek');d.insertBefore(h,k||null);d.querySelector('.kurdele')&&(d.querySelector('.kurdele').textContent='En Çok Tercih Edilen')})};
  go();new MutationObserver(go).observe(document.body,{subtree:true,childList:true});
},[LCSS]);
await ins();
const sc=async(name,click)=>{await p.evaluate(()=>{const e=document.querySelector('.pk-liste');window.scrollTo(0,window.scrollY+e.getBoundingClientRect().top-90)});await p.waitForTimeout(700);await p.screenshot({path:name,clip:{x:0,y:40,width:390,height:420}});};
await sc('L1.png');
await p.click('.pk-liste>div:nth-child(2) .sat');await p.waitForTimeout(900);
await sc('L2.png');
await b.close();})();
