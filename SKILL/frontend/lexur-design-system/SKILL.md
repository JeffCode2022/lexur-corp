---
name: lexur-design-system
description: Lenguaje visual oficial LEXUR ("Precision Dark") y design tokens multiplataforma. Activalo SIEMPRE que se disene o implemente cualquier interfaz (web, desktop, movil), pantalla, componente, tema, colores, tipografia, espaciado, iconos, modo oscuro/claro, branding, landing page o dashboard en un proyecto LEXUR. Estilo futurista profesional inspirado en Apple, Tesla, X, Meta e Instagram. PROHIBE gradientes, glassmorphism, liquid glass, blur y neumorfismo.
---

# LEXUR — Design System "Precision Dark"

Filosofia: **precision sobre decoracion**. La interfaz se siente cara por su tipografia,
su espaciado y su contencion, no por efectos. Si un elemento no comunica, se elimina.

## 1. Reglas inviolables

| # | Regla |
|---|-------|
| 1 | **Cero gradientes**: ni `linear/radial/conic-gradient`, ni `LinearGradient`, ni `Brush.*Gradient`, ni texto con degradado. |
| 2 | **Cero glass / liquid glass / blur**: ni `backdrop-filter`, ni `BackdropFilter`, ni `.ultraThinMaterial`, ni `.glassEffect`, ni Mica/Acrylic/vibrancy. |
| 3 | **Superficies solidas**: jerarquia por escalones de superficie + bordes hairline de 1px, no por sombras. |
| 4 | **Un solo acento** por producto. Todo lo demas es escala monocromatica. |
| 5 | **Solo tokens**: prohibido escribir un HEX, px de spacing o duracion "a mano" fuera de los archivos de tokens. |
| 6 | **Dark-first**: el tema por defecto es dark (negro puro). Light es completo y de primera clase. Opciones de usuario: Dark / Light / Sistema. |
| 7 | **WCAG 2.2 AA**: texto >= 4.5:1, UI no textual >= 3:1. Verificado con script, no a ojo. |
| 8 | Sin neumorfismo, sin sombras de color, sin bordes de neon/glow, sin emojis como iconos, sin ilustraciones genericas 3D "AI". |

## 2. ADN de las referencias (que tomamos de cada una)

- **Apple**: jerarquia tipografica extrema (titulares grandes y apretados), aire generoso, producto/contenido como heroe, esquinas continuas.
- **Tesla**: negro puro, cromado minimo, numeros grandes tipo telemetria, overlines en mayusculas espaciadas, UI que desaparece.
- **X**: negro verdadero, divisores hairline, listas densas pero legibles, boton primario invertido (blanco sobre negro).
- **Meta / Instagram**: contenido primero, navegacion por gestos, feedback inmediato, estados vacios cuidados.

Detalle y ejemplos de layout: [references/brand-language.md](references/brand-language.md).

## 3. Tokens — fuente unica de verdad

- Fuente: [resources/tokens.json](resources/tokens.json)
- Generados (copiar al proyecto, nunca editar a mano):
  - Web / Electron / Tauri (Tailwind v4): [lexur-tokens.css](resources/generated/lexur-tokens.css)
  - Flutter: [lexur_tokens.dart](resources/generated/lexur_tokens.dart)
  - Jetpack Compose: [LexurTokens.kt](resources/generated/LexurTokens.kt)
  - SwiftUI: [LexurTokens.swift](resources/generated/LexurTokens.swift)

### Flujo para un proyecto nuevo
1. Copia `resources/tokens.json` al repo del proyecto en `design/tokens.json`.
2. Si el producto tiene acento propio, cambia SOLO `accent.*` (y `focus.ring`) en ambos temas.
3. Valida contraste (debe salir con codigo 0):
   `node <skill>/scripts/check-contrast.mjs design/tokens.json`
4. Genera los archivos de plataforma:
   `node <skill>/scripts/generate-tokens.mjs design/tokens.json <carpeta-salida> [paquete.kotlin]`
5. Registra el acento y cualquier decision en `DESIGN.md` del proyecto.

## 4. Resumen de tokens (dark / light)

| Token | Dark | Light | Uso |
|-------|------|-------|-----|
| bg.canvas | #000000 | #FFFFFF | Fondo de app |
| bg.surface1/2/3 | #0A0A0A / #141414 / #1F1F1F | #FAFAFA / #F2F2F2 / #E8E8E8 | Cards, inputs, hover, popovers (cada nivel = +1 escalon) |
| border.subtle/default/strong | #1A1A1A / #2A2A2A / #404040 | #EFEFEF / #E0E0E0 / #C2C2C2 | Divisores y contornos decorativos |
| border.control | #5E5E5E | #8F8F8F | Contorno de inputs/checkbox (>= 3:1) |
| text.primary/secondary/tertiary | #F5F5F5 / #A3A3A3 / #808080 | #0A0A0A / #525252 / #6E6E6E | Jerarquia de texto |
| accent.default | #2E6BFF | #0A5CFF | Relleno de accion acentuada, seleccion, indicadores |
| accent.text | #6B9BFF | #0A5CFF | Links e iconos acentuados sobre superficies |
| status.success/warning/danger | #32D74B / #FFD60A / #FF453A | #1E7E34 / #A15C00 / #D70015 | Estados (+ variantes `*Subtle` solidas de fondo) |
| overlay.scrim | #000 al 72% | #000 al 48% | Unico color con alpha: fondo de modales (SIN blur) |

**Boton primario = invertido** (`bg.inverse` + `text.inverse`), estilo Apple/Tesla/X.
El acento se reserva para: links, foco, seleccion, toggles activos, progreso y CTA de conversion puntual.

## 5. Tipografia

- Web, Electron, Tauri, Flutter, Android: **Geist** (UI) + **Geist Mono** (datos, codigo, metricas). Licencia SIL OFL. Fallback: Inter, system-ui.
- iOS / macOS nativo: **SF Pro** (fuente del sistema) para sentirse nativo.
- Fuentes **empaquetadas localmente** (nunca cargadas en runtime desde CDN de terceros: privacidad + offline).
- Escala (px / line-height / tracking): displayXl 72/76/-4%, display 56/60/-3%, h1 40/44/-2.5%, h2 32/38/-2%,
  h3 24/30/-1.5%, h4 20/26/-1%, bodyLg 17/26, body 15/22, bodySm 13/18, label 14/20 w500,
  caption 12/16 w500, overline 11/14 w600 +8% MAYUSCULAS, metric 48/52 mono tabular.
- Titulares: peso 600 y tracking negativo. Nunca mas de 3 tamanos distintos en una misma vista.
- Numeros que cambian (precios, contadores, telemetria): `tabular-nums` / mono.
- Movil: maximo `display` 40px; respetar Dynamic Type / escala de fuente del sistema hasta 200%.

## 6. Espacio, forma y layout

- Grilla de 4pt. Escala: 0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128.
- Radios: xs 4, sm 6, md 10 (default controles), lg 14 (cards), xl 20 (sheets/modales), full (pills/avatars).
  Usar esquinas continuas (squircle) donde la plataforma lo soporte.
- Controles: sm 32 / md 40 / lg 48. Tap target minimo 44pt iOS, 48dp Android, 24px web (ideal 40+).
- Layout desktop: sidebar 248 (colapsado 64), header 56, contenido max 1200, lectura max 680.
- Gutters: 16 movil, 32 desktop. Secciones de landing separadas por 96-128.

## 7. Elevacion y profundidad (sin sombras, sin blur)

```
Nivel 0  canvas                     -> fondo
Nivel 1  surface1 + border.subtle   -> cards, paneles
Nivel 2  surface2 + border.default  -> inputs, hover, items seleccionados
Nivel 3  surface3 + border.strong   -> popovers, menus, tooltips
Modal    surface1 + border.default sobre overlay.scrim (solido, sin blur)
```
Light: se permite UNA sombra neutra muy sutil solo en popovers/modales
(`0 8px 24px rgba(0,0,0,0.08)`), siempre acompanada del borde. Dark: nunca sombras.
Headers sticky: fondo `bg.canvas` solido + `border-bottom` hairline. Nunca translucido.

## 8. Iconografia e imagen

- Web/Electron/Tauri/Flutter: **Lucide** (stroke 1.5, tamanos 16/20/24). iOS: **SF Symbols**. Android: **Material Symbols Outlined** peso 300.
- Iconos monocromaticos con `currentColor`. Nunca iconos multicolor ni emojis en UI.
- Fotografia/renders: alto contraste, fondos negros o neutros, sin overlays de degradado.
  Para legibilidad sobre imagen usar un bloque solido o el scrim, no un gradiente.
- Graficos/data-viz: lineas 1.5px, escala de grises + acento para la serie principal, rellenos solidos con opacidad baja permitidos solo bajo lineas (sin degradado), grid hairline `border.subtle`.

## 9. Validacion obligatoria antes de entregar UI

1. `node scripts/check-contrast.mjs <tokens.json>` -> codigo 0.
2. Escaneo de estilos prohibidos (skill `lexur-ui-review`): `node <lexur-ui-review>/scripts/scan-forbidden-styles.mjs <src>` -> codigo 0.
3. Revisar ambos temas (dark y light) y tamano de fuente al 200%.

## Skills relacionados
`lexur-components` (anatomia y estados) · `lexur-motion` (animacion) · `lexur-accessibility` ·
`lexur-web-nextjs` · `lexur-desktop-apps` · `lexur-flutter-ui` · `lexur-android-compose` · `lexur-ios-swiftui` · `lexur-ui-review`
