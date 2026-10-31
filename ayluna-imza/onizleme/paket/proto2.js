const {chromium}=require('playwright');
const Y1='https://cdn.shopify.com/s/files/1/0792/3571/1204/files/generated-1793448152312.png?width=300';
const Y2='https://cdn.shopify.com/s/files/1/0792/3571/1204/files/generated-1793448172535.png?width=300';
const YCSS=`
.pg .pk{gap:14px!important;display:flex;flex-direction:column}
.pg .pk-k{position:relative;flex-wrap:wrap;background:#F1F7F3!important;border:2px solid #D2E3D9!important;border-radius:18px!important;min-height:96px!important;padding:10px 14px 0 10px!important;box-shadow:none!important;overflow:visible!important}
.pg .pk-k.on{background:#fff!important;border-color:#B3362B!important;box-shadow:0 8px 22px rgba(179,54,43,.22)!important}
.pg .pk-g{width:76px!important;height:76px!important;border-radius:14px!important;background:#fff!important;box-shadow:inset 0 0 0 1px #E2ECE6}
.pg .pk-g img{position:absolute;inset:4px;width:calc(100% - 8px)!important;height:calc(100% - 8px)!important;object-fit:contain!important;margin:0!important;transform:none!important}
.pg .pk-g .x2{display:none!important}
.pg .pk-o b,.pg .pk-f b{font-size:18px!important;font-weight:800!important;color:#123A2A!important}
.pg .pk-o span{color:#B3362B!important;font-weight:600!important}
.pg .pk-k .kurdele{background:#B3362B!important;color:#fff!important;font-weight:800!important;border-radius:999px!important;padding:4px 12px!important;top:-12px!important;right:14px!important;left:auto!important}
.pk-hed{flex-basis:calc(100% + 24px);display:flex;align-items:center;gap:8px;margin:10px -14px 0 -10px;padding:9px 14px;border-radius:0 0 16px 16px;background:#DDEBE2;color:#123A2A;font-size:13.5px;font-weight:700}
.pk-k.on .pk-hed{background:#123A2A;color:#fff}
.pk-hed svg{width:16px;height:16px;flex:none}
`;
(async()=>{
const b=await chromium.launch({args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:2});
await p.route(/(\/cart\/(add|change|update|clear))|facebook|tiktok|google-analytics|googletagmanager|clarity|hotjar/, r=>r.abort());
await p.goto('https://ayluna.shop/products/yilbasi-agaci-projektor-lamba?_cb='+Date.now(),{waitUntil:'domcontentloaded'});
await p.waitForTimeout(8000);
await p.evaluate(([css,y1,y2])=>{
  const s=document.createElement('style');s.textContent=css;document.head.appendChild(s);
  const go=()=>{document.querySelectorAll('.pg .pk-k').forEach((d,i)=>{const im=d.querySelector('.pk-g img');if(im&&im.dataset.y!=='1'){im.src=i?y2:y1;im.dataset.y='1'}if(d.querySelector('.pk-hed'))return;const h=document.createElement('span');h.className='pk-hed';h.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="8" width="18" height="13" rx="2"/><path d="M12 8v13M3 12h18M12 8c-2-4-6-4-6-1s6 1 6 1 6 2 6-1-4-3-6 1"/></svg>'+(i?'2 hediye kutusunda gelir':'Hediye kutusunda gelir');d.appendChild(h)})};
  go();new MutationObserver(go).observe(document.body,{subtree:true,childList:true});
},[YCSS,Y1,Y2]);
const sc=async(name)=>{await p.evaluate(()=>{const e=document.querySelector('.pg .pk');window.scrollTo(0,window.scrollY+e.getBoundingClientRect().top-90)});await p.waitForTimeout(900);await p.screenshot({path:name,clip:{x:0,y:40,width:390,height:330}});};
await sc('Y1.png');
await p.click('.pg .pk-k:nth-child(2)');await p.waitForTimeout(900);
await sc('Y2.png');
await b.close();})();
