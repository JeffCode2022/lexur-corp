---
name: lexur-components
description: Especificaciones de componentes UI LEXUR (anatomia, variantes, tamanos y estados) validas para web, desktop y movil. Activalo al crear o modificar botones, inputs, formularios, cards, navegacion (sidebar, tab bar, navbar), modales, sheets, drawers, menus, toasts, tablas, listas, badges, avatars, tabs, toggles, skeletons, estados vacios/error/carga, o al montar una libreria de componentes propia.
---

# LEXUR — Componentes

Cada componente se construye UNA vez por plataforma en `core/ui` (o `components/ui`) y se reutiliza.
Prefijo de componentes: `Lx` (`LxButton`, `LxInput`...). Todos usan solo tokens de `lexur-design-system`.

## Estados universales (todos los interactivos)

| Estado | Tratamiento |
|--------|-------------|
| default | Segun variante |
| hover (puntero) | Superficie +1 escalon (o `accent.hover`), `instant` |
| pressed | Superficie +2 / `accent.pressed` + scale 0.98 |
| focus-visible | Anillo 2px `focus.ring` con offset 2px (nunca eliminar outline sin reemplazo) |
| disabled | `text.disabled`, sin hover, cursor not-allowed, `aria-disabled`; no bajar opacidad de todo el bloque |
| loading | Spinner 16px en lugar del icono, label se mantiene, ancho no cambia, bloquea doble envio |
| selected | `surface2` + texto primario + indicador (check o barra 2px) — no solo color |

## Button

| Variante | Fondo | Texto | Borde | Uso |
|----------|-------|-------|-------|-----|
| primary | bg.inverse | text.inverse | — | Accion principal (1 por vista) |
| accent | accent.default | text.onAccent | — | Conversion puntual (comprar, suscribirse) |
| secondary | bg.surface2 | text.primary | border.default | Acciones secundarias |
| ghost | transparente | text.primary | — | Toolbars, acciones terciarias |
| danger | status.danger (solido) | dark: text.inverse (6.2:1) · light: text.onAccent (5.4:1) | — | Destructivas (siempre con confirmacion) |
| link | — | accent.text | — | Navegacion inline, subrayado en hover |

Tamanos: sm 32 (radio sm, label 13), md 40 (radio md, label 14), lg 48 (radio md, label 15). Padding horizontal 12/16/20.
Icono 16 (sm/md) o 20 (lg), gap 8. Boton solo-icono: cuadrado + `aria-label`/`accessibilityLabel` obligatorio.
Movil: altura minima 44pt (iOS) / 48dp (Android); botones de ancho completo en formularios.

## Input / TextField

- Label SIEMPRE visible arriba (`label`, `text.secondary`). Placeholder opcional, nunca reemplaza al label.
- Campo: alto 40 (desktop) / 48 (movil), fondo `surface1`, borde `border.control`, radio md, texto `body`.
- Focus: borde `focus.ring` 1px + anillo 2px. Error: borde `status.danger` + mensaje debajo con icono (`caption`), `aria-invalid` + `aria-describedby`.
- Helper text debajo en `text.tertiary`. Contador de caracteres a la derecha si hay limite.
- Variantes: text, password (toggle mostrar), search (icono, Esc limpia), textarea (autosize), select, combobox, OTP (segmentos 48x56 mono).
- Validacion: al perder foco y al enviar, no en cada tecla (salvo reglas de formato).

## Card / Panel
`surface1` + `border.subtle` 1px + radio lg + padding 16/24. Sin sombra. Hover solo si es clickeable (`surface2`).
Header: overline o h4 + acciones ghost a la derecha. Toda la card clickeable = un solo elemento enlace (no anidar botones).

## Navegacion

- **Top navbar (web)**: 56px, `bg.canvas` solido, hairline inferior al hacer scroll, links `label` `text.secondary` -> activo `text.primary`.
- **Sidebar (desktop/web app)**: 248/64px, `surface1`, items 36px radio md, activo `surface2`, secciones con overline, colapsable con tooltip en modo 64.
- **Tab bar (movil)**: 4-5 destinos, fondo `bg.canvas` solido + hairline superior, iconos 24 outline->filled, label `caption` opcional, area segura inferior.
- **Tabs (in-page)**: subrayado 2px `text.primary` en activo, sin pills de color.
- **Breadcrumb**: `bodySm` `text.tertiary`, separador `/` o chevron 12.
- **Command palette (Ctrl/Cmd+K)**: obligatoria en apps desktop/web complejas.

## Overlays (todos solidos, nunca translucidos ni con blur)

| Componente | Spec |
|-----------|------|
| Modal/Dialog | max 480 (confirm) / 640 (form); `surface1`, borde `border.default`, radio xl, scrim `overlay.scrim`; foco atrapado, Esc cierra, foco vuelve al disparador; titulo + descripcion + acciones a la derecha (primaria al final) |
| Sheet (movil) | Desde abajo, radio xl superior, handle 36x4 `border.strong`, detents medio/completo, swipe para cerrar + boton cerrar |
| Drawer (desktop) | Lateral derecho 400-560, para detalles con contexto |
| Popover/Menu | `surface3` + `border.strong`, radio md, items 32-36, separadores hairline, navegacion por flechas |
| Tooltip | `bg.inverse` + `text.inverse`, `caption`, delay 500ms, nunca contiene info critica |
| Toast | Abajo-centro (movil) / abajo-derecha (desktop), `surface3` + borde, icono de status + texto + accion opcional, 4-6s, pausa en hover, `role=status` |

## Datos

- **Tabla**: header `caption` `text.tertiary` mayusculas opcionales; filas 44 (compacta 36); divisores `border.subtle`; numeros a la derecha tabulares; hover `surface2`; seleccion con checkbox; sticky header solido; paginacion o virtualizacion > 100 filas; estado vacio dentro de la tabla.
- **Lista**: items 56-72 movil, avatar 40, titulo `body` w500, subtitulo `bodySm` `text.secondary`, metadata derecha `caption`.
- **Badge**: alto 20, radio full, `caption`, fondo `*Subtle` + texto status; neutro `surface2` + `text.secondary`.
- **Avatar**: circular, tamanos 24/32/40/56/96, fallback iniciales sobre `surface3`.
- **KPI / Metric**: overline + `metric` mono + delta con icono flecha y color status.

## Seleccion
Checkbox/Radio 18-20 con borde `border.control`, marcado `bg.inverse` (o acento). Toggle/Switch 44x24 (iOS 51x31 nativo), activo `accent.default`.
Segmented control: contenedor `surface2`, segmento activo `surface3`/`bg.inverse`.

## Estados de vista (obligatorios)

| Estado | Componente | Contenido |
|--------|-----------|-----------|
| Loading | `LxSkeleton` (layout real) | > 300ms skeleton; > 2s agregar texto; > 10s ofrecer cancelar |
| Empty | `LxEmptyState` | Icono 40 `text.tertiary` + titulo h4 + descripcion + accion primaria |
| Error | `LxErrorState` | Icono + que paso en lenguaje humano + accion (Reintentar) + detalle tecnico colapsable |
| Offline | Banner `warningSubtle` | "Sin conexion. Mostrando datos guardados." |
| Success | Contenido | Toast de confirmacion solo para acciones del usuario |

## Verificacion
- Story/preview de cada componente con TODAS las variantes y estados, en dark y light
  (Storybook/Ladle en web, `@Preview` en Compose, `#Preview` en SwiftUI, widget previews/golden tests en Flutter).
- Pasar `lexur-ui-review`.
