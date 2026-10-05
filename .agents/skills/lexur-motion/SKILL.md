---
name: lexur-motion
description: Sistema de movimiento y microinteracciones LEXUR para web, desktop y movil. Activalo cuando se implementen animaciones, transiciones de pagina o navegacion, microinteracciones, hover/press feedback, gestos, haptics, skeletons, loaders, o cuando el usuario pida que algo se sienta mas fluido, premium o "tipo Apple/Tesla".
---

# LEXUR — Motion

El movimiento explica (de donde viene, a donde va, que cambio). Nunca decora.
Referente: la fisica sobria de iOS y la UI de Tesla — rapida, precisa, sin rebotes exagerados.

## Tokens

| Token | ms | Uso |
|-------|----|-----|
| instant | 80 | Cambios de color/opacity en hover, press |
| fast | 150 | Toggles, checkbox, tooltips, menus pequenos |
| base | 220 | Popovers, dropdowns, cambios de layout local |
| slow | 320 | Sheets, drawers, modales |
| deliberate | 480 | Transiciones de pagina/hero, onboarding (maximo) |

| Easing | Curva | Uso |
|--------|-------|-----|
| standard | cubic-bezier(0.2, 0, 0, 1) | Movimiento dentro de pantalla |
| enter | cubic-bezier(0.05, 0.7, 0.1, 1) | Elementos que entran |
| exit | cubic-bezier(0.3, 0, 0.8, 0.15) | Elementos que salen (salidas ~20% mas cortas) |
| spring | dampingRatio 0.86, response 0.35s | Movil: gestos, sheets, arrastre |

## Reglas

1. Anima solo `transform` y `opacity` (web: nunca width/height/top/left; usa FLIP/layout animations).
2. Entradas: opacity 0->1 + translateY 8px->0 (o scale 0.98->1). Nada de rebotes ni rotaciones.
3. Press feedback: scale 0.97-0.98 + cambio de superficie en `instant`. Sin ripple Material (ver skills de plataforma).
4. Listas: stagger maximo 30ms por item y maximo 6 items animados; el resto aparece sin animacion.
5. Skeletons: bloques `surface2` estaticos o pulso de opacidad 0.6<->1 a 1.2s. **Nunca shimmer con gradiente.**
6. Loaders: spinner lineal de 1.5px o barra de progreso fina en `accent.default`. Determinado cuando se conozca el progreso.
7. Reduce Motion: reemplaza desplazamientos por fade de `fast` o elimina; nunca autoplay de video/parallax.
8. Haptics (movil): solo en confirmaciones (exito, toggle, seleccion en picker), nunca en scroll ni en cada tap.
9. 60/120 fps obligatorios: si una animacion produce jank, se simplifica o se elimina.

## Implementacion por plataforma

### Web / Electron / Tauri
```css
.lx-enter { animation: lx-in var(--lx-duration-base) var(--ease-enter) both; }
@keyframes lx-in { from { opacity: 0; transform: translateY(8px); } }
.lx-press { transition: transform var(--lx-duration-instant) var(--ease-standard),
                        background-color var(--lx-duration-instant) var(--ease-standard); }
.lx-press:active { transform: scale(0.98); }
```
- Libreria (si hace falta orquestacion/layout/gestos): **Motion** (`motion/react`). Auditar antes de instalar.
- Respeta `useReducedMotion()` de Motion o la media query (ya incluida en `lexur-tokens.css`).
- Transiciones entre rutas: View Transitions API con fade + 8px; fallback sin animacion.

### Flutter
- `LxDuration.*` + `LxEasing.*` desde `lexur_tokens.dart`. `AnimatedContainer`, `AnimatedSwitcher`, `TweenAnimationBuilder`.
- Reduce motion: `MediaQuery.of(context).disableAnimations`.
- Page transitions: `FadeForwardsPageTransitionsBuilder` o custom fade+slide 8px; en iOS respetar back-swipe (Cupertino).
- Haptics: `HapticFeedback.selectionClick()` / `lightImpact()`.

### Jetpack Compose
- `tween(LxMotion.BaseMs, easing = LxMotion.Standard)`, `spring(dampingRatio = LxMotion.SpringDampingRatio)`.
- `AnimatedVisibility(enter = fadeIn() + slideInVertically { it / 12 })`, `animateContentSize()`.
- Reduce motion: leer `Settings.Global.ANIMATOR_DURATION_SCALE` (0 = desactivado).
- Haptics: `LocalHapticFeedback.current.performHapticFeedback(HapticFeedbackType.Confirm)` (o `LongPress` en versiones previas).

### SwiftUI
- `LxMotion.standard()`, `LxMotion.spring`, o `.snappy` / `.smooth` del sistema.
- Reduce motion: `@Environment(\.accessibilityReduceMotion)`.
- Haptics: `.sensoryFeedback(.success, trigger: value)`.
- `matchedGeometryEffect` para transiciones heroe (lista -> detalle), estilo App Store.

## Verificacion
- Grabar la interaccion a 60fps (DevTools Performance / Flutter DevTools / Android Studio profiler / Instruments) sin frames perdidos.
- Probar con Reduce Motion activado.
