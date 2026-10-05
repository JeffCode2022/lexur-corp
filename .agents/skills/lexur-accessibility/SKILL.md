---
name: lexur-accessibility
description: Estandares de accesibilidad universal WCAG 2.2 nivel AA para todas las aplicaciones web, desktop y moviles de LEXUR. Activalo al disenar o auditar la navegabilidad por teclado, gestion del foco, compatibilidad con lectores de pantalla (VoiceOver, TalkBack, NVDA), ratios de contraste de color, roles y atributos ARIA, soporte de texto grande / Dynamic Type, o al realizar pruebas automatizadas con axe-core y Playwright a11y.
---

# LEXUR — Accessibility (WCAG 2.2 AA)

La verdadera ingenieria de software de clase mundial no excluye a nadie. En LEXUR, la accesibilidad es parte integral de la arquitectura y la construccion de componentes, no un parche posterior.

---

## 1. Principios Fundamentales WCAG 2.2 AA

1. **Perceptible**:
   - Todo elemento que transmita informacion debe tener alternativa textual o auditiva.
   - Contraste minimo 4.5:1 para texto normal, 3:1 para texto grande (>= 18pt o >= 14pt negrita) y componentes de interfaz (bordes de control, estados de foco).
   - NUNCA transmitir informacion valiosa UNICAMENTE mediante color (ej: un error debe tener icono y texto, no solo borde rojo).
2. **Operable**:
   - Todo lo accionable mediante mouse/touch DEBE ser accionable exclusivamente mediante teclado.
   - Trampas de foco prohibidas: el foco debe poder entrar y salir de cualquier componente.
   - Indicador de foco visible OBLIGATORIO (`focus-visible` con anillo de 2px `focus.ring` y offset de 2px). NUNCA `outline: none` sin sustituto.
   - Tap targets minimos: 44x44 pt en iOS, 48x48 dp en Android, 24x24 px (ideal 40px) en Web/Desktop.
3. **Comprensible**:
   - Mensajes de error claros, en contexto y con sugerencia de recuperacion.
   - Formularios con etiquetas (`<label>`) explicitas asociadas mediante `id` / `for`.
4. **Robusto**:
   - HTML semantico puro antes que ARIA (`<button>`, `<nav>`, `<main>`, `<dialog>`).
   - Si se usa ARIA, seguir estrictamente los patrones WAI-ARIA Authoring Practices (APG).

---

## 2. Gestion de Foco y Teclado

### 2.1. Orden natural y navegacion
- Seguir el flujo logico de lectura (de arriba a abajo, de izquierda a derecha).
- Prohibido `tabIndex > 0`. Solo usar `tabIndex={0}` para hacer enfocable un elemento personalizado o `tabIndex={-1}` para recibir foco programatico.

### 2.2. Modales y Overlays (Focus Trap y Restauracion)
Cuando se abre un modal, sheet o dialog:
1. El foco debe trasladarse automaticamente al primer elemento interactivo o al titulo del modal.
2. La tecla `Tab` debe ciclar unicamente dentro del modal.
3. La tecla `Escape` debe cerrar el modal de inmediato.
4. Al cerrarse, el foco DEBE retornar exactamente al boton o elemento que lo abrio.

---

## 3. Semantica y Lectores de Pantalla

### 3.1. Botones solo-icono
Todo boton sin texto visible DEBE tener una descripcion clara:
- **Web**: `<button aria-label="Cerrar modal"> <XIcon aria-hidden="true" /> </button>`
- **Flutter**: `IconButton(icon: Icon(Icons.close), tooltip: 'Cerrar ventana')` o `Semantics(label: 'Cerrar ventana', child: ...)`
- **Compose**: `IconButton(onClick = ..., modifier = Modifier.semantics { contentDescription = "Cerrar ventana" })`
- **SwiftUI**: `Button(...) { Image(...) }.accessibilityLabel("Cerrar ventana")`

### 3.2. Regiones en vivo (`aria-live` / Announcements)
Para notificar cambios dinamicos (ej: resultados de busqueda, toasts de exito/error):
- `role="status"` o `aria-live="polite"`: para notificaciones informativas que esperan a que el lector termine de hablar.
- `role="alert"` o `aria-live="assertive"`: unicamente para errores criticos que requieren atencion inmediata.

---

## 4. Auditoria Automatizada con axe-core y Playwright

En proyectos web y desktop (Electron/Tauri), incluir pruebas de accesibilidad en los tests e2e:

```typescript
// tests/e2e/accessibility.spec.ts
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.describe('Auditoría de Accesibilidad LEXUR', () => {
  test('La página principal no debe tener violaciones WCAG 2.2 AA', async ({ page }) => {
    await page.goto('/');

    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag22aa'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });
});
```

---

## 5. Checklist Obligatoria de Entrega (A11y Gate)

- [ ] Contraste verificado con `check-contrast.mjs` (todos los pares pasan).
- [ ] La app se puede navegar y operar al 100% solo con teclado (Tab, Shift+Tab, Enter, Espacio, Esc).
- [ ] Ningun interactivo tiene `outline: none` sin un foco alternativo de alto contraste.
- [ ] Las imagenes decorativas tienen `alt=""` / `aria-hidden="true"`; las imagenes informativas tienen descripcion precisa.
- [ ] No hay textos con fuentes menores a 12px.
- [ ] Al escalar la fuente del sistema al 200% (Dynamic Type / Zoom del navegador), ningun texto se trunca ni se superpone.
- [ ] Lectores de pantalla (VoiceOver / TalkBack / NVDA) anuncian correctamente roles y estados (abierto/cerrado, seleccionado, cargando).
