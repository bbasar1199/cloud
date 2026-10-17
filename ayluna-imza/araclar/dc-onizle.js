// Basit .dc.html önizleyici: sc-for / sc-if / {{yol}} + onClick
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [src, out, stateJson, clipFrom, clipH] = process.argv.slice(2);
const P = path.dirname(src), MAG = fs.existsSync(path.join(P, 'magaza')) ? path.resolve(P, 'magaza') : path.resolve(P, '../magaza');
const F = path.resolve(__dirname, '../onizleme/f') + '/';
const blobMap = { e02351b3be4a1c555c5d760d0bbda723:'m-kiz', '0033dfea6282c5bc479c385213661c00':'m-erkek', '211acb76d908e8ed6d4f5fcddc987893':'ld0','652e1893a0ae33a24ee0e3d53edab757':'ld1',ec0a99ef7b8839a12ab7e6aa4282f7da:'ld2','35f6b0090fd4e65b22f48d111fe61905':'ld3',a08890007843d79d94bfffc397a3d0ac:'ld4',d4efe7e83c74524ece75e962161f7fff:'ld5',fd0a28089115b8aa3de9bcb92a65a8e2:'ld6','3ddd8b8b95f040d436d5d0ea350924b8':'ld7','98db755893dbcebe192c69e73ae5afff':'ld8'};
let html = fs.readFileSync(src, 'utf8');
const css = (html.match(/<style>([\s\S]*?)<\/style>/) || [])[1];
const body = html.split('</helmet>')[1].split('</x-dc>')[0];
const script = html.match(/data-dc-script[^>]*>([\s\S]*?)<\/script>/)[1];
const fonts = `@font-face{font-family:"Young Serif";src:url(file://${F}young-serif-latin-ext-400-normal.woff2)}@font-face{font-family:"Young Serif";src:url(file://${F}young-serif-latin-400-normal.woff2)}` + [400,500,600,700].map(w=>`@font-face{font-family:Onest;font-weight:${w};src:url(file://${F}onest-latin-${w}-normal.woff2)}@font-face{font-family:Onest;font-weight:${w};src:url(file://${F}onest-latin-ext-${w}-normal.woff2);unicode-range:U+0100-024F}`).join('');
const page = `<!doctype html><html><head><meta charset=utf-8><style>${fonts}${css}</style></head><body><template id=T>${body}</template><div id=root></div>
<script>class DCLogic{constructor(p){this.props=p;this.state={}}setState(o){Object.assign(this.state,o);R()}}
${script}
const BM=${JSON.stringify(blobMap)};
const C=new Component({});Object.assign(C.state,${stateJson||'{}'});
function get(sc,p){return p.split('.').reduce((o,k)=>o==null?o:o[k],sc)}
function sub(s,sc){return s.replace(/\\{\\{\\s*([^}]+?)\\s*\\}\\}/g,(m,p)=>{const v=get(sc,p);return v==null?'':String(v)})}
function walk(n,sc,parent){
 if(n.nodeType===3){parent.appendChild(document.createTextNode(sub(n.textContent,sc)));return}
 if(n.nodeType!==1)return;
 const tag=n.tagName.toLowerCase();
 if(tag==='sc-for'){const l=get(sc,n.getAttribute('list').replace(/[{}]/g,'').trim())||[];const as=n.getAttribute('as');l.forEach(it=>{const s2=Object.create(sc);s2[as]=it;n.childNodes.forEach(c=>walk(c,s2,parent))});return}
 if(tag==='sc-if'){const v=get(sc,n.getAttribute('value').replace(/[{}]/g,'').trim());if(v&&v!=='false')n.childNodes.forEach(c=>walk(c,sc,parent));return}
 const el=document.createElementNS(n.namespaceURI,n.tagName.toLowerCase()==n.tagName?n.tagName:tag);
 for(const a of n.attributes){const m=a.value.match(/^\\{\\{\\s*([^}]+?)\\s*\\}\\}$/);
  if(/^on[A-Z]/.test(a.name)||/^on[a-z]+$/.test(a.name)&&m){const f=m&&get(sc,m[1]);if(typeof f==='function')el.addEventListener(a.name.slice(2).toLowerCase(),f);continue}
  let v=sub(a.value,sc);if(a.name==='src'&&v.startsWith('/_blob/')){const id=v.slice(7);v=BM[id]?'file://${MAG}/'+BM[id]+'.jpg':'data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22/>'}
  try{el.setAttribute(a.name,v)}catch(e){}}
 if(el.tagName==='IMG'&&!el.getAttribute('src').startsWith('file'))el.style.background='#C9BFAE';
 n.childNodes.forEach(c=>walk(c,sc,el));parent.appendChild(el)}
function R(){const v=C.renderVals();const r=document.getElementById('root');r.innerHTML='';const t=document.getElementById('T').content;t.childNodes.forEach(c=>walk(c,v,r))}
R();</script></body></html>`;
const PH = path.join(require('os').tmpdir(), 'ayluna-dc-onizle.html');
fs.writeFileSync(PH, page);
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:2});
pg.on('pageerror',e=>console.log('ERR',e.message));
await pg.goto('file://'+PH);await pg.waitForTimeout(800);
const y=await pg.evaluate(()=>{const e=document.getElementById('siparis');return e?e.getBoundingClientRect().top+scrollY:0});
await pg.screenshot({path:out,clip:{x:0,y:y+Number(clipFrom||0),width:390,height:Number(clipH||1000)},fullPage:true});
console.log('levha y',y);await b.close()})();
