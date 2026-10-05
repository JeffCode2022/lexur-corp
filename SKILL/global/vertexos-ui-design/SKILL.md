---
name: vertexos-ui-design
description: Sistema de diseno y estandares de UI/UX para todos los proyectos VertexOS. Activalo cuando el usuario quiera disenar pantallas, crear componentes visuales, implementar un sistema de diseno, trabajar en la apariencia de una app, o cuando mencione UI, UX, diseno, pantallas, componentes, tema, colores, o tipografia en cualquier proyecto VertexOS.
---

# VertexOS — Sistema de Diseno

Filosofia: Impeccable over Generic. Cada interfaz debe sentirse intencionada, profesional y nunca como una plantilla de IA generica.

---

## Filosofia de Diseno VertexOS

Basado en principios de Impeccable (impeccable.style):

1. Intencionado — Cada elemento tiene razon de existir
2. Consistente — Design tokens aplicados rigurosamente
3. Funcional — La UI sirve a la funcion, no al reves
4. Legible — Jerarquia visual clara, espaciado generoso
5. Sin artificios — Sin gradientes innecesarios, sombras excesivas

---

## Paleta de Colores

```
Fondo principal:    #FFFFFF  (blanco puro)
Fondo alternativo:  #F9FAFB  (gris muy claro)
Bordes:             #E5E7EB  (gris claro)
Texto secundario:   #9CA3AF  (gris medio)
Texto principal:    #111827  (casi negro)
Acento principal:   #1F2937  (gris oscuro corporativo)
Error:              #EF4444  (rojo)
Exito:              #10B981  (verde)
Advertencia:        #F59E0B  (ambar)
```

---

## Tipografia

```
Fuente:       Inter (Google Fonts, sin costo)
H1:           24px / Bold
H2:           20px / SemiBold
H3:           18px / SemiBold
Body Large:   16px / Regular
Body:         14px / Regular
Caption:      12px / Regular
Label:        13px / Medium
```

---

## Espaciado (Sistema 4pt)

```
XS:   4px
SM:   8px
MD:   12px
LG:   16px
XL:   24px
XXL:  32px
Huge: 48px
```

---

## Componentes Base

### Botones
```
Primary:    fondo #1F2937 / texto #FFFFFF / radio 10px
Secondary:  fondo #FFFFFF / borde #E5E7EB / texto #111827
Ghost:      fondo transparente / texto #374151
Altura: 44px (tap target movil)
Padding: 12px vertical / 20px horizontal
```

### Cards
```
Fondo: #FFFFFF
Borde: 1px solid #E5E7EB
Radio: 10px
Padding: 16px
Sin sombra (flat design)
```

### Inputs
```
Fondo: #F9FAFB
Borde normal:  1px solid #E5E7EB
Borde focused: 2px solid #1F2937
Borde error:   2px solid #EF4444
Radio: 8px
Altura: 44px
```

---

## Anti-Patrones (NUNCA hacer)

```
X Gradientes de colores vivos en fondos
X Sombras exageradas
X Animaciones de mas de 300ms sin proposito
X Texto menor a 12px en elementos interactivos
X Botones sin estado hover/pressed visible
X Forms sin labels visibles (solo placeholder)
X Empty states con solo texto — siempre con icono
X Loading spinner sin texto para esperas mayores a 2 segundos
X Modales sin forma de cerrarse
```

---

## Accesibilidad (Obligatorio)

- Contraste minimo texto/fondo: 4.5:1 (WCAG AA)
- Tap targets minimo: 44x44px en movil
- Todo elemento interactivo con estado focus visible
- Formularios con labels explicitos (no solo placeholders)

---

## Layout Movil

```
Margen lateral: 16px
Gap entre elementos: 12px
AppBar: 56px de altura
NavBar: 56px de altura, maximo 5 items
Content: ScrollView con padding 16px
```

## Layout Desktop

```
Sidebar: 240px fijo
Header: 48px de altura
Content area: flex-1, maximo 1280px centrado
Gap entre secciones: 24px
```

---

## Referencias

- Impeccable (anti-AI-slop): https://impeccable.style
- shadcn/ui (referencia): https://ui.shadcn.com
- Inter font: https://fonts.google.com/specimen/Inter
- WCAG: https://www.w3.org/WAI/WCAG22/quickref/
