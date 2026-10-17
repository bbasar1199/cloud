import {bundle} from '@remotion/bundler';
import {renderMedia, renderStill, selectComposition} from '@remotion/renderer';
import path from 'path';
const mod = process.argv[2] || 'kare'; // kare | video
const yalniz = process.argv[3];
const out = process.argv[4] || 'cikti';
const be = '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell';
const serveUrl = await bundle({entryPoint: path.resolve('src/index.ts')});
const ids = ['m1-isik', 'm2-disk', 'm3-kiz', 'm3-erkek', 'm4-tavan', 'm5-kiz', 'm5-erkek'].filter(i => !yalniz || yalniz === 'hepsi' || yalniz.split(',').includes(i));
for (const id of ids) {
  const c = await selectComposition({serveUrl, id, browserExecutable: be});
  if (mod === 'kare') {
    for (const fr of [0, Math.floor(c.durationInFrames * .3), Math.floor(c.durationInFrames * .5), Math.floor(c.durationInFrames * .75)]) {
      await renderStill({composition: c, serveUrl, frame: fr, output: `${out}/${id}-${fr}.jpg`, imageFormat: 'jpeg', browserExecutable: be});
    }
  } else {
    await renderMedia({composition: c, serveUrl, codec: 'h264', crf: Number(process.env.CRF || 26), x264Preset: 'slow', pixelFormat: 'yuv420p', muted: true, outputLocation: `${out}/${id}.mp4`, browserExecutable: be, concurrency: 2});
    await renderStill({composition: c, serveUrl, frame: 0, output: `${out}/${id}.jpg`, imageFormat: 'jpeg', jpegQuality: 78, browserExecutable: be});
  }
  console.log('tamam', id);
}
