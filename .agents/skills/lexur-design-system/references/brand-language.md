# LEXUR — Lenguaje de marca y patrones de layout

Referencia extendida de `lexur-design-system`. Leer cuando se disene una pantalla completa,
una landing, un dashboard o una app movil desde cero.

## Principios de composicion

1. **Un heroe por vista.** Cada pantalla tiene un unico foco (un numero, un producto, una accion). Todo lo demas es secundario.
2. **Contraste por escala, no por color.** Diferencia jerarquia con tamano/peso/espacio. El color es la ultima herramienta.
3. **Alineacion estricta.** Todo se alinea a la grilla de 4pt y a columnas (12 web, 8 tablet, 4 movil).
4. **Densidad intencional.** Marketing = aire (secciones 96-128px). Herramientas/dashboards = densos pero con ritmo de 8px.
5. **Texto real.** Nunca lorem ipsum en entregables. Microcopy corto, directo, en segunda persona, sin signos de exclamacion.
6. **Silencio visual.** Si dudas entre poner o quitar un borde, icono o etiqueta: quitalo.

## Patrones por tipo de producto

### Landing / sitio corporativo (estilo Apple / Tesla)
- Hero a pantalla completa sobre `bg.canvas`: overline (11px, +8%, mayusculas, `text.secondary`) -> titular `displayXl` -> subtitulo `bodyLg` `text.secondary` (max 560px) -> 1 CTA primario invertido + 1 CTA ghost.
- Media del producto grande, centrada o a sangre; sin marcos de dispositivo salvo que se pida.
- Secciones alternas canvas / surface1, separadas por hairline o solo por espacio.
- Bloques de especificaciones tipo Tesla: numero `metric` mono + caption debajo, en fila de 3-4.
- Navegacion superior: 56px, fondo solido, logo izquierda, 4-6 links `label`, CTA derecha.
- Footer denso en `text.tertiary`, columnas de links, hairline superior.

### Dashboard / herramienta interna (estilo X / Linear / Tesla console)
- Sidebar 248px `bg.surface1` + hairline derecho; items 32-36px, icono 16-20 + label; activo = `bg.surface2` + texto primario (no acento de fondo).
- Header 56px con breadcrumb, busqueda/command palette (Ctrl/Cmd+K) y avatar.
- KPIs arriba: cards `surface1` con overline + `metric` + delta (success/danger, con icono, nunca solo color).
- Tablas: filas 44px, divisores `border.subtle`, encabezado `caption` `text.tertiary`, numeros alineados a la derecha y tabulares, hover `surface2`.
- Paneles de detalle como drawer lateral solido, no modal, cuando el usuario necesita contexto.

### App movil consumer (estilo Instagram / X / Meta)
- Contenido a sangre, cromado minimo. Tab bar de 4-5 destinos, iconos outline -> filled al activarse, sin labels si los iconos son universales (con accessibilityLabel siempre).
- Feeds: separadores hairline o espacio de 8px, nunca cards con sombra.
- Acciones primarias por gesto + boton visible (gesto nunca es la unica via).
- Sheets inferiores (radio xl arriba) solidos sobre scrim. Haptics sutiles en acciones confirmadas.
- Skeletons con `surface2` estatico o pulso de opacidad (nunca shimmer con gradiente).

### App movil de control / telemetria (estilo Tesla app)
- Numero heroe enorme (`display`/`metric`) centrado, estado en overline.
- Controles grandes (>= 56) en grilla, iconos 24, label debajo.
- Estados del dispositivo con color de status + texto + icono.

## Voz y microcopy

| Evitar | Preferir |
|--------|----------|
| "¡Ups! Algo salio mal :(" | "No pudimos cargar tus proyectos. Reintentar" |
| "Haz clic aqui" | "Ver informe" |
| "Enviar" (generico) | Verbo + objeto: "Crear proyecto", "Guardar cambios" |
| "No hay datos" | "Aun no tienes proyectos. Crea el primero para empezar." + accion |

## Senales de "AI slop" (rechazar en revision)

- Fondos con degradados morado/azul, blobs, orbes difuminados, mallas de color.
- Tarjetas con sombra grande + radio enorme + borde de color.
- Todo centrado, iconos-emoji, titulos con degradado, "glow" de neon.
- Mas de un color de acento, badges de colores aleatorios.
- Espaciados irregulares (13px, 18px, 27px), mas de 3 tamanos de texto por vista.
- Ilustraciones 3D genericas, stock photos de gente sonriendo a una laptop.
