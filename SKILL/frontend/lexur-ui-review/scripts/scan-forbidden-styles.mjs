#!/usr/bin/env node
// LEXUR — Escaner de estilos prohibidos (gradientes, glass, liquid glass, blur, colores hardcodeados).
// Uso: node scan-forbidden-styles.mjs [carpeta=.] [--strict]
//   --strict  -> las advertencias tambien hacen fallar (exit 1).
// Excepcion puntual: agregar el comentario  lexur-allow: <motivo>  en la misma linea.
import fs from 'node:fs';
import path from 'node:path';

const args = process.argv.slice(2);
const strict = args.includes('--strict');
const root = path.resolve(args.find((a) => !a.startsWith('--')) ?? '.');

const IGNORED_DIRS = new Set([
  'node_modules', '.git', '.next', 'out', 'dist', 'build', '.dart_tool', '.gradle', 'Pods',
  'DerivedData', 'target', '.turbo', 'coverage', '.vercel', 'generated', '.idea', '.vscode',
]);
const WEB = ['.css', '.scss', '.sass', '.less', '.ts', '.tsx', '.js', '.jsx', '.mjs', '.cjs', '.html', '.vue', '.svelte', '.astro'];
const DART = ['.dart'];
const KOTLIN = ['.kt', '.kts'];
const SWIFT = ['.swift'];

/** @type {{id:string, level:'error'|'warn', exts:string[], re:RegExp, msg:string, skipTokenFiles?:boolean}[]} */
const RULES = [
  // ---- Gradientes ----
  { id: 'css-gradient', level: 'error', exts: WEB, re: /\b(repeating-)?(linear|radial|conic)-gradient\s*\(/, msg: 'Gradiente CSS prohibido. Usa superficies solidas.' },
  { id: 'tw-gradient', level: 'error', exts: WEB, re: /\bbg-(gradient|linear|radial|conic)-/, msg: 'Utilidad de gradiente Tailwind prohibida.' },
  { id: 'gradient-text', level: 'error', exts: WEB, re: /\bbg-clip-text\b|background-clip\s*:\s*text/, msg: 'Texto con degradado prohibido.' },
  { id: 'dart-gradient', level: 'error', exts: DART, re: /\b(LinearGradient|RadialGradient|SweepGradient)\s*\(/, msg: 'Gradiente Flutter prohibido.' },
  { id: 'compose-gradient', level: 'error', exts: KOTLIN, re: /Brush\.(linearGradient|radialGradient|verticalGradient|horizontalGradient|sweepGradient)/, msg: 'Gradiente Compose prohibido.' },
  { id: 'swift-gradient', level: 'error', exts: SWIFT, re: /\b(LinearGradient|RadialGradient|AngularGradient|EllipticalGradient|MeshGradient)\b|\.gradient\b/, msg: 'Gradiente SwiftUI prohibido.' },

  // ---- Glass / Liquid Glass / Blur ----
  { id: 'css-backdrop', level: 'error', exts: WEB, re: /backdrop-filter|backdropFilter|\bbackdrop-(blur|saturate|brightness|contrast|opacity|filter)/, msg: 'Glassmorphism (backdrop-filter) prohibido.' },
  { id: 'css-blur', level: 'warn', exts: WEB, re: /filter\s*:\s*[^;]*blur\(|\bblur-(none|xs|sm|md|lg|xl|2xl|3xl|\[)/, msg: 'Blur detectado. Solo permitido para placeholders de imagen (justificar con lexur-allow).' },
  { id: 'electron-vibrancy', level: 'error', exts: WEB, re: /\bvibrancy\s*:|backgroundMaterial\s*:\s*['"](mica|acrylic|tabbed|auto)['"]|visualEffectState/, msg: 'Vibrancy/Mica/Acrylic de ventana prohibidos (efecto glass).' },
  { id: 'dart-blur', level: 'error', exts: DART, re: /\bBackdropFilter\s*\(|ImageFilter\.blur/, msg: 'Blur/glass Flutter prohibido.' },
  { id: 'dart-cupertino-bar', level: 'warn', exts: DART, re: /\bCupertino(NavigationBar|SliverNavigationBar|TabBar)\s*\(/, msg: 'Las barras Cupertino aplican blur si el fondo es translucido. Asigna backgroundColor solido de tokens.' },
  { id: 'compose-blur', level: 'error', exts: KOTLIN, re: /RenderEffect\.createBlurEffect|Modifier\s*\.\s*blur\s*\(|\.blur\s*\(\s*\d/, msg: 'Blur Compose prohibido.' },
  { id: 'compose-dynamic-color', level: 'error', exts: KOTLIN, re: /dynamic(Dark|Light)ColorScheme|dynamicColor\s*:\s*Boolean\s*=\s*true|dynamicColor\s*=\s*true/, msg: 'Material You (dynamic color) rompe la marca. Desactivalo.' },
  { id: 'swift-material', level: 'error', exts: SWIFT, re: /\.(ultraThinMaterial|thinMaterial|regularMaterial|thickMaterial|ultraThickMaterial)\b|\.glassEffect\s*\(|GlassEffectContainer|UIVisualEffectView|UIBlurEffect|\.glassProminent|\.buttonStyle\(\s*\.glass/, msg: 'Material/Liquid Glass prohibido en superficies propias.' },
  { id: 'swift-blur', level: 'warn', exts: SWIFT, re: /\.blur\s*\(\s*radius/, msg: 'Blur detectado. Justificar con lexur-allow.' },

  // ---- Colores fuera de tokens ----
  { id: 'hardcoded-hex', level: 'warn', exts: WEB, re: /#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?\b(?![\w-])/, msg: 'Color HEX hardcodeado. Usa tokens (bg-canvas, text-fg, var(--lx-*)).', skipTokenFiles: true },
  { id: 'tw-default-palette', level: 'warn', exts: WEB, re: /\b(bg|text|border|ring|fill|stroke)-(slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-\d{2,3}\b/, msg: 'Paleta por defecto de Tailwind. Usa colores semanticos LEXUR.' },
  { id: 'dart-hardcoded-color', level: 'warn', exts: DART, re: /\bColor\(0x[0-9a-fA-F]{8}\)|Colors\.(?!transparent\b)\w+/, msg: 'Color hardcodeado en Flutter. Usa LxColorTokens via Theme.', skipTokenFiles: true },
  { id: 'compose-hardcoded-color', level: 'warn', exts: KOTLIN, re: /\bColor\(0x[0-9a-fA-F]{8}\)|Color\.(Red|Blue|Green|Yellow|Cyan|Magenta|Gray|LightGray|DarkGray)\b/, msg: 'Color hardcodeado en Compose. Usa LexurTheme.colors.', skipTokenFiles: true },
  { id: 'swift-hardcoded-color', level: 'warn', exts: SWIFT, re: /Color\(\s*red:|Color\(\s*\.sRGB|Color\.(red|blue|green|yellow|orange|purple|pink|cyan|mint|teal|indigo)\b/, msg: 'Color hardcodeado en SwiftUI. Usa Color.lx*.', skipTokenFiles: true },
];

const TAURI_RULES = [
  { id: 'tauri-window-effects', level: 'error', re: /"windowEffects"/, msg: 'windowEffects (Mica/Acrylic/vibrancy) prohibido en Tauri.' },
  { id: 'tauri-transparent', level: 'warn', re: /"transparent"\s*:\s*true/, msg: 'Ventana transparente: verifica que no se use para efectos glass.' },
];

const findings = [];

function isTokenFile(file) {
  return /tokens?|theme[\\/]+generated|lexur_tokens|LexurTokens|scan-forbidden-styles|check-contrast/i.test(path.basename(file));
}

function scanFile(file) {
  if (isTokenFile(file)) return;
  const ext = path.extname(file);
  const base = path.basename(file);
  let rules;
  if (/^tauri(\.\w+)?\.conf\.json$/.test(base)) rules = TAURI_RULES;
  else rules = RULES.filter((r) => r.exts.includes(ext));
  if (!rules.length) return;

  const lines = fs.readFileSync(file, 'utf8').split(/\r?\n/);
  lines.forEach((line, i) => {
    if (line.includes('lexur-allow')) return;
    for (const r of rules) {
      if (r.re.test(line)) {
        findings.push({ file: path.relative(root, file), line: i + 1, ...r, snippet: line.trim().slice(0, 140) });
      }
    }
  });
}

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      if (!IGNORED_DIRS.has(entry.name) && !entry.name.startsWith('.')) walk(path.join(dir, entry.name));
    } else if (entry.isFile()) {
      scanFile(path.join(dir, entry.name));
    }
  }
}

if (!fs.existsSync(root)) {
  console.error(`No existe: ${root}`);
  process.exit(2);
}
fs.statSync(root).isDirectory() ? walk(root) : scanFile(root);

const errors = findings.filter((f) => f.level === 'error');
const warns = findings.filter((f) => f.level === 'warn');
for (const f of [...errors, ...warns]) {
  console.log(`${f.level === 'error' ? 'ERROR' : 'WARN '} ${f.file}:${f.line} [${f.id}] ${f.msg}\n       ${f.snippet}`);
}
console.log(`\nLEXUR scan: ${errors.length} error(es), ${warns.length} advertencia(s) en ${root}`);
process.exit(errors.length || (strict && warns.length) ? 1 : 0);
