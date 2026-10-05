#!/usr/bin/env node
// LEXUR — Generador multiplataforma de design tokens.
// Uso: node generate-tokens.mjs [tokens.json] [carpetaSalida] [paqueteKotlin]
// Genera: lexur-tokens.css (Web/Electron/Tauri + Tailwind v4), lexur_tokens.dart (Flutter),
//         LexurTokens.kt (Jetpack Compose), LexurTokens.swift (SwiftUI).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const src = process.argv[2] ?? path.join(here, '..', 'resources', 'tokens.json');
const outDir = process.argv[3] ?? path.join(here, '..', 'resources', 'generated');
const kotlinPackage = process.argv[4] ?? 'com.lexur.design.tokens';
const t = JSON.parse(fs.readFileSync(src, 'utf8').replace(/^\uFEFF/, ''));
const HEADER = `AUTO-GENERADO por lexur-design-system/scripts/generate-tokens.mjs (v${t.meta.version}). NO EDITAR A MANO.`;

const kebab = (k) => k.replace(/\./g, '-').replace(/([a-z])([A-Z0-9])/g, '$1-$2').toLowerCase();
const camel = (k) =>
  k.split('.').map((p, i) => (i ? p[0].toUpperCase() + p.slice(1) : p)).join('');
const argb = (hex) => {
  const h = hex.replace('#', '').toUpperCase();
  return h.length === 6 ? `FF${h}` : `${h.slice(6)}${h.slice(0, 6)}`;
};
const rgbaParts = (hex) => {
  const h = hex.replace('#', '');
  const [r, g, b] = [0, 2, 4].map((i) => parseInt(h.slice(i, i + 2), 16));
  const a = h.length === 8 ? parseInt(h.slice(6, 8), 16) / 255 : 1;
  return { r, g, b, a: Math.round(a * 1000) / 1000 };
};
const colorKeys = Object.keys(t.color.dark);
const typeEntries = Object.entries(t.type);
const swiftWeight = { 400: '.regular', 500: '.medium', 600: '.semibold', 700: '.bold' };
const round = (n) => Math.round(n * 1000) / 1000;

// ---------- CSS + Tailwind v4 ----------
function css() {
  const vars = (theme) => colorKeys.map((k) => `  --lx-${kebab(k)}: ${t.color[theme][k]};`).join('\n');
  const twColors = colorKeys
    .map((k) => `  --color-${t.tailwindNames[k]}: var(--lx-${kebab(k)});`)
    .join('\n');
  const space = Object.entries(t.space).map(([k, v]) => `  --lx-space-${k.slice(1)}: ${v}px;`).join('\n');
  const radius = Object.entries(t.radius).map(([k, v]) => `  --radius-${k}: ${v}px;`).join('\n');
  const text = typeEntries
    .map(([k, s]) => {
      const n = kebab(k);
      return [
        `  --text-${n}: ${s.size / 16}rem;`,
        `  --text-${n}--line-height: ${s.line / 16}rem;`,
        `  --text-${n}--letter-spacing: ${s.tracking}em;`,
        `  --text-${n}--font-weight: ${s.weight};`,
      ].join('\n');
    })
    .join('\n');
  const dur = Object.entries(t.motion.duration).map(([k, v]) => `  --lx-duration-${k}: ${v}ms;`).join('\n');
  const ease = Object.entries(t.motion.easing)
    .map(([k, v]) => `  --ease-${k}: cubic-bezier(${v.join(', ')});`)
    .join('\n');
  const z = Object.entries(t.z).map(([k, v]) => `  --lx-z-${k}: ${v};`).join('\n');
  const layout = Object.entries(t.layout).map(([k, v]) => `  --lx-layout-${kebab(k)}: ${v}px;`).join('\n');
  const bp = Object.entries(t.breakpoint).map(([k, v]) => `  --breakpoint-${k === 'xxl' ? '2xl' : k}: ${v / 16}rem;`).join('\n');

  return `/* ${HEADER}
 * Uso (Tailwind v4): en globals.css ->  @import "tailwindcss";  @import "./lexur-tokens.css";
 * Tema: <html data-theme="dark|light|system">. Dark es el default (dark-first).
 */

:root,
[data-theme="dark"] {
  color-scheme: dark;
${vars('dark')}
}

[data-theme="light"] {
  color-scheme: light;
${vars('light')}
}

@media (prefers-color-scheme: light) {
  [data-theme="system"] {
    color-scheme: light;
${vars('light').replace(/^ {2}/gm, '    ')}
  }
}

:root {
${space}
${dur}
${z}
${layout}
}

/* Bloquea la paleta y escala por defecto de Tailwind: SOLO tokens LEXUR. */
@theme {
  --color-*: initial;
  --text-*: initial;
  --radius-*: initial;
  --font-sans: "${t.font.sans}", ${t.font.sansFallback};
  --font-mono: "${t.font.mono}", ${t.font.monoFallback};
${radius}
${text}
${ease}
${bp}
}

@theme inline {
${twColors}
}

@layer base {
  html {
    background-color: var(--lx-bg-canvas);
    color: var(--lx-text-primary);
    font-family: var(--font-sans);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-rendering: optimizeLegibility;
  }
  ::selection {
    background-color: var(--lx-accent-subtle);
    color: var(--lx-text-primary);
  }
  :focus-visible {
    outline: 2px solid var(--lx-focus-ring);
    outline-offset: 2px;
  }
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
      scroll-behavior: auto !important;
    }
  }
}

@utility numeric {
  font-variant-numeric: tabular-nums;
  font-feature-settings: "tnum" 1;
}

@utility hairline-b {
  border-bottom: 1px solid var(--lx-border-default);
}
`;
}

// ---------- Flutter ----------
function dart() {
  const fields = colorKeys.map((k) => `  final Color ${camel(k)};`).join('\n');
  const ctor = colorKeys.map((k) => `    required this.${camel(k)},`).join('\n');
  const inst = (theme) =>
    colorKeys.map((k) => `    ${camel(k)}: Color(0x${argb(t.color[theme][k])}),`).join('\n');
  const space = Object.entries(t.space).map(([k, v]) => `  static const double ${k} = ${v};`).join('\n');
  const radius = Object.entries(t.radius).map(([k, v]) => `  static const double ${k} = ${v};`).join('\n');
  const type = typeEntries
    .map(
      ([k, s]) =>
        `  static const TextStyle ${k} = TextStyle(fontFamily: fontSans, fontSize: ${s.size}, height: ${round(s.line / s.size)}, letterSpacing: ${round(s.tracking * s.size)}, fontWeight: FontWeight.w${s.weight});`,
    )
    .join('\n');
  const dur = Object.entries(t.motion.duration)
    .map(([k, v]) => `  static const Duration ${k} = Duration(milliseconds: ${v});`)
    .join('\n');
  const ease = Object.entries(t.motion.easing)
    .map(([k, v]) => `  static const Cubic ${k} = Cubic(${v.join(', ')});`)
    .join('\n');
  const control = Object.entries(t.control).map(([k, v]) => `  static const double ${k} = ${v};`).join('\n');
  const layout = Object.entries(t.layout).map(([k, v]) => `  static const double ${k} = ${v};`).join('\n');
  const bp = Object.entries(t.breakpoint).map(([k, v]) => `  static const double ${k} = ${v};`).join('\n');

  return `// ${HEADER}
// ignore_for_file: public_member_api_docs
import 'package:flutter/widgets.dart';

@immutable
class LxColorTokens {
  const LxColorTokens({
${ctor}
  });

${fields}

  static const LxColorTokens dark = LxColorTokens(
${inst('dark')}
  );

  static const LxColorTokens light = LxColorTokens(
${inst('light')}
  );
}

abstract final class LxSpace {
${space}
}

abstract final class LxRadius {
${radius}
}

abstract final class LxControl {
${control}
}

abstract final class LxLayout {
${layout}
}

abstract final class LxBreakpoint {
${bp}
}

abstract final class LxType {
  static const String fontSans = '${t.font.sans}';
  static const String fontMono = '${t.font.mono}';
${type}
}

abstract final class LxDuration {
${dur}
}

abstract final class LxEasing {
${ease}
}
`;
}

// ---------- Jetpack Compose ----------
function kotlin() {
  const fields = colorKeys.map((k) => `    val ${camel(k)}: Color,`).join('\n');
  const inst = (theme) =>
    colorKeys.map((k) => `    ${camel(k)} = Color(0x${argb(t.color[theme][k])}),`).join('\n');
  const space = Object.entries(t.space).map(([k, v]) => `    val ${k} = ${v}.dp`).join('\n');
  const radius = Object.entries(t.radius)
    .map(([k, v]) => `    val ${k} = ${k === 'full' ? 999 : v}.dp`)
    .join('\n');
  const type = typeEntries
    .map(
      ([k, s]) =>
        `    val ${k} = TextStyle(fontSize = ${s.size}.sp, lineHeight = ${s.line}.sp, letterSpacing = (${s.tracking}).em, fontWeight = FontWeight.W${s.weight})`,
    )
    .join('\n');
  const dur = Object.entries(t.motion.duration)
    .map(([k, v]) => `    const val ${k[0].toUpperCase() + k.slice(1)}Ms = ${v}`)
    .join('\n');
  const ease = Object.entries(t.motion.easing)
    .map(([k, v]) => `    val ${k[0].toUpperCase() + k.slice(1)} = CubicBezierEasing(${v.map((n) => `${n}f`).join(', ')})`)
    .join('\n');
  const control = Object.entries(t.control).map(([k, v]) => `    val ${k} = ${v}.dp`).join('\n');

  return `// ${HEADER}
package ${kotlinPackage}

import androidx.compose.animation.core.CubicBezierEasing
import androidx.compose.runtime.Immutable
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.em
import androidx.compose.ui.unit.sp

@Immutable
data class LxColors(
${fields}
)

val LxDarkColors = LxColors(
${inst('dark')}
)

val LxLightColors = LxColors(
${inst('light')}
)

object LxSpace {
${space}
}

object LxRadius {
${radius}
}

object LxControl {
${control}
}

/** fontFamily se aplica en LexurTheme (Geist desde res/font). */
object LxType {
${type}
}

object LxMotion {
${dur}
${ease}
    const val SpringDampingRatio = ${t.motion.spring.dampingRatio}f
}
`;
}

// ---------- SwiftUI ----------
function swift() {
  const fields = colorKeys.map((k) => `    public let ${camel(k)}: Color`).join('\n');
  const inst = (theme) =>
    colorKeys
      .map((k) => {
        const { r, g, b, a } = rgbaParts(t.color[theme][k]);
        return `        ${camel(k)}: Color(.sRGB, red: ${round(r / 255)}, green: ${round(g / 255)}, blue: ${round(b / 255)}, opacity: ${a})`;
      })
      .join(',\n');
  const dyn = colorKeys
    .map((k) => {
      const d = rgbaParts(t.color.dark[k]);
      const l = rgbaParts(t.color.light[k]);
      const ui = (c) =>
        `UIColor(red: ${round(c.r / 255)}, green: ${round(c.g / 255)}, blue: ${round(c.b / 255)}, alpha: ${c.a})`;
      const name = 'lx' + camel(k)[0].toUpperCase() + camel(k).slice(1);
      return `    static let ${name} = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? ${ui(l)} : ${ui(d)} })`;
    })
    .join('\n');
  const space = Object.entries(t.space).map(([k, v]) => `    public static let ${k}: CGFloat = ${v}`).join('\n');
  const radius = Object.entries(t.radius).map(([k, v]) => `    public static let ${k}: CGFloat = ${v}`).join('\n');
  const type = typeEntries
    .map(
      ([k, s]) =>
        `    public static let ${k} = LxTextToken(size: ${s.size}, lineHeight: ${s.line}, tracking: ${round(s.tracking * s.size)}, weight: ${swiftWeight[s.weight]})`,
    )
    .join('\n');
  const dur = Object.entries(t.motion.duration)
    .map(([k, v]) => `    public static let ${k}: Double = ${v / 1000}`)
    .join('\n');
  const ease = Object.entries(t.motion.easing)
    .map(
      ([k, v]) =>
        `    public static func ${k}(_ duration: Double = LxMotion.base) -> Animation { .timingCurve(${v.join(', ')}, duration: duration) }`,
    )
    .join('\n');

  return `// ${HEADER}
import SwiftUI
#if canImport(UIKit)
import UIKit
#endif

public struct LxColorSet {
${fields}
}

public enum LxPalette {
    public static let dark = LxColorSet(
${inst('dark')}
    )
    public static let light = LxColorSet(
${inst('light')}
    )
}

#if canImport(UIKit)
/// Colores dinamicos: siguen el ColorScheme activo. Dark es el default (todo lo que no sea .light).
public extension Color {
${dyn}
}
#endif

public enum LxSpace {
${space}
}

public enum LxRadius {
${radius}
}

public struct LxTextToken {
    public let size: CGFloat
    public let lineHeight: CGFloat
    public let tracking: CGFloat
    public let weight: Font.Weight
}

/// En iOS/macOS se usa la fuente del sistema (SF Pro). Ver lexur-ios-swiftui.
public enum LxType {
${type}
}

public enum LxMotion {
${dur}
${ease}
    public static let spring = Animation.spring(response: ${t.motion.spring.responseSeconds}, dampingFraction: ${t.motion.spring.dampingRatio})
}
`;
}

fs.mkdirSync(outDir, { recursive: true });
const files = {
  'lexur-tokens.css': css(),
  'lexur_tokens.dart': dart(),
  'LexurTokens.kt': kotlin(),
  'LexurTokens.swift': swift(),
};
for (const [name, content] of Object.entries(files)) {
  fs.writeFileSync(path.join(outDir, name), content, 'utf8');
  console.log(`Generado: ${path.join(outDir, name)}`);
}
