// In-page voice benchmark for aistudio.google.com/generate-speech.
// Paste into javascript_tool once per page load, then:
//   __bench([{voice:'Enzo', style:STYLE, text:TEXT, tag:'x'}, ...])   // starts in background
//   JSON.stringify(__results)                                      // poll (each JS call times out at ~45 s)
// Every case spends one generation from the daily quota (~26/day observed).

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const waitFor = async (sel, ms = 5000) => {
  for (let t = 0; t < ms; t += 200) {
    const el = document.querySelector(sel);
    if (el) return el;
    await sleep(200);
  }
  return null;
};

window.__setVal = (el, value) => {
  const proto = el instanceof HTMLInputElement ? HTMLInputElement.prototype : HTMLTextAreaElement.prototype;
  Object.getOwnPropertyDescriptor(proto, "value").set.call(el, value);
  ["input", "change", "blur"].forEach((t) => el.dispatchEvent(new Event(t, { bubbles: true })));
};

// Autocorrelation F0 over the finished WAV in <audio>; same algorithm as scripts/ref_pitch_acf.py.
window.__analyzeTTS = async (words) => {
  const src = document.querySelector("audio").src;
  const ab = await new OfflineAudioContext(1, 1, 16000).decodeAudioData(await (await fetch(src)).arrayBuffer());
  const step = Math.round(ab.sampleRate / 16000) || 1;
  const raw = ab.getChannelData(0);
  const x = step > 1 ? Float32Array.from({ length: Math.floor(raw.length / step) }, (_, i) => raw[i * step]) : raw;
  const fs = ab.sampleRate / step;
  const win = Math.round(fs * 0.04), hop = Math.round(fs * 0.01);
  const minL = Math.floor(fs / 400), maxL = Math.ceil(fs / 65);
  const f0 = [], rms = [];
  for (let s = 0; s + win + maxL < x.length; s += hop) {
    let e = 0;
    for (let i = 0; i < win; i++) e += x[s + i] * x[s + i];
    rms.push(Math.sqrt(e / win));
    let best = 0, bl = 0;
    for (let L = minL; L <= maxL; L++) {
      let c = 0, n2 = 0;
      for (let i = 0; i < win; i++) { c += x[s + i] * x[s + i + L]; n2 += x[s + i + L] * x[s + i + L]; }
      const r = c / Math.sqrt(e * n2 + 1e-12);
      if (r > best) { best = r; bl = L; }
    }
    f0.push(best > 0.6 && e / win > 1e-5 ? fs / bl : 0);
  }
  const v = f0.filter((f) => f > 0).sort((a, b) => a - b);
  const q = (p) => v[Math.floor(p * (v.length - 1))];
  const med = q(0.5);
  const st = v.map((f) => 12 * Math.log2(f / med));
  const mean = st.reduce((a, b) => a + b, 0) / st.length;
  const sd = Math.sqrt(st.reduce((a, b) => a + (b - mean) ** 2, 0) / st.length);
  const thr = Math.max(...rms) * 0.03;
  let cur = 0, tot = 0;
  for (const r of rms) { if (r < thr) cur++; else { if (cur >= 25) tot += cur; cur = 0; } }
  const dur = x.length / fs;
  return {
    dur: +dur.toFixed(1), f0_med: Math.round(med), p10_p90: [Math.round(q(0.1)), Math.round(q(0.9))],
    pitch_var_st: +sd.toFixed(2), wpm: words ? Math.round((words / dur) * 60) : null, pause_ratio: +(tot / 100 / dur).toFixed(3),
  };
};

window.__pickVoice = async (name) => {
  if ((document.querySelector("button.voice-chip")?.innerText || "").includes(" - " + name)) return true;
  (document.querySelector("button.active-voice-card-trigger") || document.querySelector("button.voice-chip")).click();
  const inp = await waitFor('input[aria-label="Search voices"]');
  if (!inp) return false;
  __setVal(inp, name);
  let card = null;
  for (let t = 0; t < 6000 && !card; t += 300) {
    await sleep(300);
    card = [...document.querySelectorAll(".cdk-overlay-pane button.voice-card-content")].find((b) => b.getAttribute("aria-label") === name);
  }
  if (card) { card.click(); await sleep(700); }
  document.querySelector('.cdk-overlay-pane button[aria-label="Close panel"]')?.click();
  await sleep(600);
  return !!card;
};

window.__setStyle = async (style) => {
  document.querySelector("button.attribute-chip").click();
  const t = await waitFor("textarea.daikon-custom-style-textarea");
  __setVal(t, style);
  await sleep(300);
  document.querySelector(".cdk-overlay-backdrop")?.click();
  await sleep(600);
};

// Audio streams in small chunks and autoplays; the full WAV lands in <audio> only after playback ends.
// After a fresh page load Chrome may block autoplay (stuck at 0:00): click Play once with a real click.
const waitFull = async (prevLen) => {
  for (let i = 0; i < 300; i++) {
    await sleep(1000);
    const a = document.querySelector("audio");
    const footer = document.querySelector("ms-audio-footer")?.innerText || "";
    if (a && a.src.length > 200000 && a.src.length !== prevLen && a.duration > 3 && footer.includes("play_circle")) return true;
  }
  return false;
};

const runCase = async ({ voice, style, text, tag }) => {
  if (style) await __setStyle(style);
  if (text) __setVal(document.querySelector('textarea[aria-label="Speech block text"]'), text);
  const body = text ?? document.querySelector('textarea[aria-label="Speech block text"]').value;
  const words = body.replace(/<[^>]+>/g, "").split(/\s+/).filter(Boolean).length;
  if (!(await __pickVoice(voice))) return { voice, tag, error: "voice not found" };
  const prevLen = document.querySelector("audio")?.src.length;
  document.querySelector("button.ctrl-enter-submits").click();
  await sleep(2000);
  if (!(await waitFull(prevLen))) return { voice, tag, error: "timeout (quota or render failure)" };
  return { voice, tag, ...(await __analyzeTTS(words)) };
};

window.__results = window.__results || [];
window.__bench = async (cases) => {
  window.__busy = true;
  for (const c of cases) {
    try { __results.push(await runCase(c)); }
    catch (e) { __results.push({ voice: c.voice, tag: c.tag, error: String(e) }); }
  }
  window.__busy = false;
};
