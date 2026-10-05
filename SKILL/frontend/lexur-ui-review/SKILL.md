---
name: lexur-ui-review
description: Revision de calidad visual y QA de diseno LEXUR antes de entregar, hacer merge o publicar cualquier interfaz. Activalo cuando el usuario pida revisar, auditar o pulir una UI, hacer code review de frontend, verificar que se cumple el design system, o antes de cerrar cualquier tarea que haya creado o modificado pantallas/componentes (web, desktop o movil). Incluye un escaner automatico de gradientes, glass, blur y colores hardcodeados.
---

# LEXUR — UI Review (puerta de calidad)

Ninguna tarea de UI se considera terminada sin pasar esta revision.

## Paso 1 — Escaneo automatico (obligatorio)

```bash
node <ruta-skill>/scripts/scan-forbidden-styles.mjs <carpeta-src>            # errores bloquean
node <ruta-skill>/scripts/scan-forbidden-styles.mjs <carpeta-src> --strict   # antes de release
```
Detecta en Web/Electron/Tauri/Flutter/Compose/SwiftUI: gradientes, backdrop-filter/glass,
Liquid Glass (`.glassEffect`, materials), vibrancy/Mica/Acrylic, Material You dinamico,
blur y colores fuera de tokens. Exit 0 = OK.
Excepcion justificada: comentario `lexur-allow: <motivo>` en la misma linea (registrar en `DESIGN.md`).

Y el contraste de tokens del proyecto:
```bash
node <lexur-design-system>/scripts/check-contrast.mjs design/tokens.json
```

## Paso 2 — Revision visual (capturas en dark Y light)

Toma capturas (Playwright, emulador, simulador o `generate_image` solo para mockups) y verifica:

### Sistema
- [ ] Solo tokens: colores, spacing (multiplos de 4), radios, tipografia de la escala.
- [ ] Maximo 3 tamanos de texto por vista; titulares con tracking negativo.
- [ ] Un solo acento; boton primario invertido; acento solo en links/foco/seleccion/CTA puntual.
- [ ] Jerarquia por superficies + hairlines; cero sombras en dark.
- [ ] Iconos de un solo set, mismo stroke y tamano consistente.

### Estados (cada vista/componente con datos)
- [ ] Loading (skeleton si > 300ms, texto si > 2s), Empty (icono + mensaje + accion), Error (mensaje humano + reintentar), Success.
- [ ] Hover, pressed, focus-visible, disabled, selected visibles en todos los interactivos.
- [ ] Estados de formulario: validacion inline, error con texto (no solo color), submit con loading.

### Layout y responsive
- [ ] Web: 360, 768, 1024, 1440, 1920 px sin overflow horizontal.
- [ ] Movil: pantalla pequena (iPhone SE / 360dp) y grande; safe areas; teclado abierto.
- [ ] Desktop: ventana minima (ej. 960x600) y maximizada.
- [ ] Fuente al 200% / Dynamic Type XXXL sin cortes.

### Movimiento
- [ ] Duraciones/easings de tokens; nada > 480ms salvo transiciones de pagina hero.
- [ ] `prefers-reduced-motion` / Reduce Motion respetado.

### Senales de "AI slop" (rechazo inmediato)
Degradados, blobs/orbes, glass, glow neon, emojis como iconos, todo centrado,
cards con sombra grande, lorem ipsum, paleta Tailwind por defecto, espaciados irregulares.

## Paso 3 — Revision cruzada
Ejecuta tambien las checklists de: `lexur-accessibility`, `lexur-performance`, `lexur-frontend-security`
y confirma que los tests de `lexur-frontend-testing` pasan (incluida regresion visual si existe).

## Paso 4 — Reporte
Entrega al usuario un resumen corto:
```
UI Review — <feature>
Scan: 0 errores / N advertencias (justificadas: ...)
Contraste: OK
Estados: OK | faltan: ...
Responsive: OK | problemas: ...
A11y / Perf / Seguridad: OK | hallazgos: ...
Veredicto: APROBADO | CAMBIOS REQUERIDOS
```
