import React from 'react';
import {AbsoluteFill, Composition, Img, staticFile, useCurrentFrame, useVideoConfig, interpolate, Easing} from 'remotion';

const W = 720, H = 1280, FPS = 30;
const e = Easing.bezier(.2, .7, .2, 1);
const ease = (f: number, a: number[], b: number[]) => interpolate(f, a, b, {easing: e, extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
/* 0→1→0 döngü: ilk kare ile son kare aynı, dikiş görünmez */
const gidip = (t: number) => (1 - Math.cos(2 * Math.PI * t)) / 2;
const zemin: React.CSSProperties = {backgroundColor: '#0C1027'};
const kapla: React.CSSProperties = {position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover'};

/* Sıcak ışık halesi: ürünün üstüne değil, çevresindeki havaya */
const Hale: React.FC<{x: string; y: string; r: number; o: number}> = ({x, y, r, o}) => (
  <AbsoluteFill style={{opacity: o, mixBlendMode: 'screen', background: `radial-gradient(circle ${r}px at ${x} ${y}, rgba(242,166,90,.55), rgba(242,166,90,.18) 45%, rgba(242,166,90,0) 100%)`}} />
);

/* 1 · 20:00 Işığı yak — elde lamba; ortada ışık söner, yeniden yanar */
const IsigiYak: React.FC = () => {
  const f = useCurrentFrame(); const {durationInFrames: d} = useVideoConfig();
  const t = f / d;
  const karanlik = f < 84 ? ease(f, [66, 84], [0, .62]) : ease(f, [96, 128], [.62, 0]);
  const s = 1.0 + .05 * gidip(t);
  return (
    <AbsoluteFill style={zemin}>
      <Img src={staticFile('elde.jpg')} style={{...kapla, objectPosition: '45% 30%', transform: `scale(${s}) translateY(${1.2 * gidip(t)}%)`, transformOrigin: '50% 40%'}} />
      <AbsoluteFill style={{backgroundColor: '#0C1027', opacity: karanlik}} />
      <Hale x="50%" y="34%" r={520} o={(1 - karanlik / .62) * (.75 + .25 * gidip(t * 2))} />
    </AbsoluteFill>
  );
};

/* 2 · 20:30 Diski seç — açık kubbe yakın plan + yavaşça dönen diskler */
const DiskiSec: React.FC = () => {
  const f = useCurrentFrame(); const {durationInFrames: d} = useVideoConfig();
  const t = f / d, p = gidip(t);
  const disk = (n: number, x: number, y: number, r: number, don: number, faz: number) => (
    <div style={{position: 'absolute', left: x - r / 2, top: y - r / 2, width: r, height: r, borderRadius: '50%', overflow: 'hidden', boxShadow: '0 30px 50px -20px rgba(0,0,0,.8)', transform: `translateY(${Math.sin(2 * Math.PI * (t + faz)) * 10}px) rotate(${don}deg)`}}>
      <Img src={staticFile(`disk${n}.jpg`)} style={{width: '100%', height: '100%', objectFit: 'cover', transform: 'scale(1.06)'}} />
    </div>
  );
  return (
    <AbsoluteFill style={{backgroundColor: '#141A36'}}>
      <div style={{position: 'absolute', left: 0, top: 370, width: W, height: 640, overflow: 'hidden'}}>
        <Img src={staticFile('yuva.jpg')} style={{...kapla, objectPosition: '82% 50%', transform: `scale(${1.04 + .05 * p}) translateX(${-1.5 * p}%)`, transformOrigin: '78% 45%'}} />
        <AbsoluteFill style={{background: 'linear-gradient(180deg,#141A36 0%,rgba(20,26,54,0) 14%,rgba(20,26,54,0) 70%,#141A36 100%)'}} />
      </div>
      {disk(1, 360, 300, 230, 360 * t, 0)}
      {disk(5, 120, 360, 140, -12 + 24 * p, .3)}
      {disk(3, 600, 340, 150, 10 - 20 * p, .6)}
    </AbsoluteFill>
  );
};

/* 3 · 20:45 Kendi dünyasında — yavaş yakınlaşma, nefes alan sıcak hale */
const Dunya: React.FC<{src: string}> = ({src}) => {
  const f = useCurrentFrame(); const {durationInFrames: d} = useVideoConfig();
  const p = gidip(f / d);
  return (
    <AbsoluteFill style={zemin}>
      <Img src={staticFile(src)} style={{...kapla, objectPosition: '50% 50%', transform: `scale(${1.02 + .07 * p}) translateY(${-1.2 * p}%)`, transformOrigin: '50% 58%'}} />
      <Hale x="50%" y="56%" r={420} o={.25 + .3 * p} />
    </AbsoluteFill>
  );
};

/* 4 · 21:00 Tavanda masal — yansıma yavaşça döner ve kayar */
const Tavan: React.FC = () => {
  const f = useCurrentFrame(); const {durationInFrames: d} = useVideoConfig();
  const p = gidip(f / d);
  return (
    <AbsoluteFill style={zemin}>
      <Img src={staticFile('tavan.jpg')} style={{...kapla, objectPosition: `${30 + 40 * p}% 50%`, transform: `scale(1.2) rotate(${-3 + 6 * p}deg)`, transformOrigin: '50% 40%'}} />
    </AbsoluteFill>
  );
};

/* 5 · 21:15 Gözler kapanır — gece ile başlar, kısa bir gündüz, yeniden gece (ilk kare = son kare) */
const Gece: React.FC<{gunduz: string; gece: string}> = ({gunduz, gece}) => {
  const f = useCurrentFrame(); const {durationInFrames: d} = useVideoConfig();
  const p = gidip(f / d);
  const geceO = f < 90 ? ease(f, [60, 84], [1, 0]) : ease(f, [100, 160], [0, 1]);
  const st: React.CSSProperties = {...kapla, objectPosition: '50% 62%', transform: `scale(${1.03 + .04 * p})`, transformOrigin: '50% 70%'};
  return (
    <AbsoluteFill style={zemin}>
      <Img src={staticFile(gunduz)} style={st} />
      <Img src={staticFile(gece)} style={{...st, opacity: geceO}} />
    </AbsoluteFill>
  );
};

export const Root: React.FC = () => (
  <>
    <Composition id="m1-isik" component={IsigiYak} durationInFrames={5 * FPS} fps={FPS} width={W} height={H} />
    <Composition id="m2-disk" component={DiskiSec} durationInFrames={6 * FPS} fps={FPS} width={W} height={H} />
    <Composition id="m3-kiz" component={() => <Dunya src="kiz-dunya.jpg" />} durationInFrames={5 * FPS} fps={FPS} width={W} height={H} />
    <Composition id="m3-erkek" component={() => <Dunya src="erkek-dunya.jpg" />} durationInFrames={5 * FPS} fps={FPS} width={W} height={H} />
    <Composition id="m4-tavan" component={Tavan} durationInFrames={6 * FPS} fps={FPS} width={W} height={H} />
    <Composition id="m5-kiz" component={() => <Gece gunduz="kiz-gunduz.jpg" gece="kiz-gece.jpg" />} durationInFrames={6 * FPS} fps={FPS} width={W} height={H} />
    <Composition id="m5-erkek" component={() => <Gece gunduz="erkek-gunduz.jpg" gece="erkek-gece.jpg" />} durationInFrames={6 * FPS} fps={FPS} width={W} height={H} />
  </>
);
