---
name: lexur-web-nextjs
description: Estandares de frontend web LEXUR con Next.js (App Router) + React + TypeScript + Tailwind CSS v4. Activalo al crear o modificar sitios web, landing pages, dashboards, web apps o la UI web que corre dentro de Electron/Tauri; al configurar Tailwind, temas dark/light, fuentes, formularios, data fetching, estado, rutas o estructura de carpetas en React/Next.js.
---

# LEXUR — Web (Next.js + React + TS + Tailwind v4)

Usa siempre la ultima version estable de Next.js/React/Tailwind (verifica en la doc oficial antes de iniciar;
no asumas APIs de versiones viejas). Toda dependencia nueva pasa por la auditoria de `lexur-frontend-security`.

## Stack estandar

| Necesidad | Eleccion | Nota |
|-----------|----------|------|
| Framework | Next.js App Router, TS `strict` | RSC por defecto; `"use client"` solo en hojas interactivas |
| Estilos | Tailwind v4 + `lexur-tokens.css` | Paleta por defecto bloqueada: solo tokens |
| Primitivas a11y | Radix UI / shadcn/ui (copiado y re-estilizado) | Eliminar sombras, blur y colores por defecto |
| Iconos | lucide-react | `strokeWidth={1.5}` |
| Tema | next-themes | `attribute="data-theme" defaultTheme="dark" enableSystem` |
| Fuentes | paquete `geist` (self-hosted via next/font) | Nunca fuentes desde CDN de terceros en runtime |
| Formularios | react-hook-form + zod | El mismo schema zod valida en servidor |
| Estado servidor | RSC fetch / Server Actions; TanStack Query en cliente | |
| Estado cliente | Zustand (minimo) | Primero URL state (searchParams) |
| Animacion | Motion (`motion/react`) | Ver `lexur-motion` |
| i18n | next-intl | es/en desde el dia 1 si hay clientes externos |
| Tests | Vitest + Testing Library + Playwright + axe | Ver `lexur-frontend-testing` |
| Calidad | ESLint + Prettier + prettier-plugin-tailwindcss | `pnpm` + lockfile commiteado |

## Estructura

```
src/
├── app/                      # Rutas (solo composicion, sin logica de negocio)
│   ├── (marketing)/          # Grupo: landing, pricing...
│   ├── (app)/                # Grupo: zona autenticada
│   ├── layout.tsx            # <html data-theme> + fuentes + providers
│   └── globals.css
├── components/
│   ├── ui/                   # Primitivas Lx* (button, input, dialog...) — ver lexur-components
│   └── layout/               # Navbar, Sidebar, Footer
├── features/<feature>/       # components/, actions.ts, queries.ts, schema.ts, types.ts
├── lib/                      # cn.ts, env.ts (validado con zod), utils puros
└── styles/lexur-tokens.css   # GENERADO desde design/tokens.json
design/tokens.json            # copia del design system (fuente de verdad del proyecto)
```

## Setup paso a paso

1. Genera tokens (ver `lexur-design-system`) y copia `lexur-tokens.css` a `src/styles/`.
2. `globals.css`:
   ```css
   @import "tailwindcss";
   @import "../styles/lexur-tokens.css";
   /* next/font expone variables con nombre hasheado: re-mapear las familias */
   @theme inline {
     --font-sans: var(--font-geist-sans), Inter, ui-sans-serif, system-ui, sans-serif;
     --font-mono: var(--font-geist-mono), ui-monospace, monospace;
   }
   ```
3. `layout.tsx`: ver [examples/layout.tsx](examples/layout.tsx) (fuentes, `suppressHydrationWarning`, ThemeProvider dark por defecto).
4. `lib/cn.ts` con `tailwind-merge` **configurado con la escala LEXUR** — sin esto, `text-h1` y `text-fg`
   se consideran conflicto y uno se elimina: [examples/cn.ts](examples/cn.ts).
5. Primitivas: [examples/lx-button.tsx](examples/lx-button.tsx) como patron para el resto de `components/ui`.
6. Headers de seguridad y CSP: `lexur-frontend-security` (obligatorio antes del primer deploy).

## Clases semanticas (las unicas permitidas para color)

`bg-canvas bg-surface-1 bg-surface-2 bg-surface-3 bg-inverse` · `text-fg text-fg-muted text-fg-subtle text-fg-disabled text-fg-inverse text-on-accent text-accent-fg` ·
`border-line-subtle border-line border-line-strong border-line-control` · `bg-accent bg-accent-hover bg-accent-pressed bg-accent-subtle` ·
`text-success|warning|danger` + `bg-*-subtle` · `outline-focus` · `bg-scrim`.
Tipografia: `text-display-xl text-display text-h1..h4 text-body-lg text-body text-body-sm text-label text-caption text-overline text-metric` + `numeric`.
Radios: `rounded-xs|sm|md|lg|xl|full`. Easing: `ease-standard|enter|exit`.

## Reglas

- Componentes de servidor por defecto; datos sensibles y llamadas a APIs privadas solo en servidor (`import "server-only"`).
- Toda ruta con datos tiene `loading.tsx` (skeleton), `error.tsx` (con reset) y estado vacio explicito; `not-found.tsx` global.
- Imagenes con `next/image` (AVIF/WebP, `sizes` correcto, `priority` solo en el LCP).
- Links internos con `next/link`; nada de `<a onClick>`.
- Metadata (`generateMetadata`), Open Graph y `viewport` con `themeColor` = `bg.canvas` por tema.
- Variables de entorno validadas con zod en `lib/env.ts`; solo `NEXT_PUBLIC_*` llega al cliente y NUNCA contiene secretos.
- Maximo 300 lineas por archivo, 40 por componente/funcion (alineado con `vertexos-architecture` si existe).
- `dangerouslySetInnerHTML` prohibido salvo HTML sanitizado (DOMPurify) y revisado.

## Verificacion
```bash
pnpm lint && pnpm tsc --noEmit && pnpm test && pnpm build
node <lexur-ui-review>/scripts/scan-forbidden-styles.mjs src
pnpm exec playwright test        # e2e + axe + screenshots dark/light
```
Lighthouse (movil) >= 90 en Performance, Accessibility, Best Practices y SEO (ver `lexur-performance`).
