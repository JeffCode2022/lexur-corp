#!/usr/bin/env node
// LEXUR — Verificador de contraste WCAG 2.2 para los tokens de color.
// Uso: node check-contrast.mjs [ruta/tokens.json]
// Sale con codigo 1 si algun par no cumple el minimo definido en contrastPairs.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const src = process.argv[2] ?? path.join(here, '..', 'resources', 'tokens.json');
const tokens = JSON.parse(fs.readFileSync(src, 'utf8').replace(/^\uFEFF/, ''));

function channel(c) {
  const s = c / 255;
  return s <= 0.04045 ? s / 12.92 : ((s + 0.055) / 1.055) ** 2.4;
}

function luminance(hex) {
  const h = hex.replace('#', '');
  if (h.length !== 6) throw new Error(`Solo HEX solido de 6 digitos: ${hex}`);
  const [r, g, b] = [0, 2, 4].map((i) => parseInt(h.slice(i, i + 2), 16));
  return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b);
}

function ratio(a, b) {
  const [l1, l2] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (l1 + 0.05) / (l2 + 0.05);
}

let failures = 0;
for (const [theme, colors] of Object.entries(tokens.color)) {
  console.log(`\n== Tema: ${theme} ==`);
  for (const [fg, bg, min] of tokens.contrastPairs) {
    const r = ratio(colors[fg], colors[bg]);
    const ok = r >= min;
    if (!ok) failures++;
    console.log(
      `${ok ? 'OK  ' : 'FAIL'}  ${fg.padEnd(22)} sobre ${bg.padEnd(22)} ${r.toFixed(2).padStart(5)}:1  (min ${min})`,
    );
  }
}

console.log(failures ? `\n${failures} par(es) fallan WCAG.` : '\nTodos los pares cumplen WCAG 2.2 AA.');
process.exit(failures ? 1 : 0);
