---
name: lexur-frontend-testing
description: Estrategia de pruebas automatizadas y piramide de testing para frontend en LEXUR (Web, Desktop y Mobile). Activalo al disenar o escribir pruebas unitarias de logica y reducers (Vitest), pruebas de componentes con accesibilidad (React Testing Library, Flutter WidgetTester, Compose TestRule, SwiftUI ViewInspector), pruebas end-to-end con Playwright y pruebas de regresion visual sin falsos positivos.
---

# LEXUR — Frontend Testing Strategy

En LEXUR, el software profesional no se entrega basado en "parece que funciona". Cada componente, flujo critico y transicion de estado esta respaldado por pruebas automatizadas reproducibles.

---

## 1. La Piramide de Pruebas LEXUR

```
             /\
            /  \     End-to-End (E2E) — Playwright (Flujos de negocio criticos + a11y)
           /----\
          /      \   Pruebas de Componentes / Widget Tests (Interacciones, teclado, estados)
         /--------\
        /          \ Pruebas Unitarias — Vitest / Flutter Test / JUnit (Logica pura, schemas, reducers)
       /------------\
```

---

## 2. Pruebas Unitarias y de Componentes (Web / Next.js)

### 2.1. Configuracion con Vitest + Testing Library

```typescript
// src/components/ui/__tests__/lx-button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { LxButton } from '../lx-button';

describe('LxButton — Componente LEXUR', () => {
  it('renderiza la etiqueta y maneja clics', () => {
    const handleClick = vi.fn();
    render(<LxButton label="Confirmar acción" onClick={handleClick} />);

    const button = screen.getByRole('button', { name: /confirmar acción/i });
    expect(button).toBeInTheDocument();

    fireEvent.click(button);
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('bloquea interacciones y muestra indicador en estado loading', () => {
    const handleClick = vi.fn();
    render(<LxButton label="Guardando" loading onClick={handleClick} />);

    const button = screen.getByRole('button');
    expect(button).toBeDisabled();
    expect(button).toHaveAttribute('aria-busy', 'true');

    fireEvent.click(button);
    expect(handleClick).not.toHaveBeenCalled();
  });
});
```

---

## 3. Pruebas de Widgets en Flutter (`WidgetTester`)

Toda interfaz Flutter debe comprobar los 4 estados UI obligatorios:

```dart
// test/features/telemetry/presentation/telemetry_screen_test.dart
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:lexur_app/features/telemetry/presentation/telemetry_screen.dart';

void main() {
  testWidgets('Debe mostrar estado de error y permitir reintentar', (tester) async {
    bool retried = false;

    await tester.pumpWidget(
      MaterialApp(
        home: TelemetryErrorView(
          message: 'Error de conexión con el sensor',
          onRetry: () => retried = true,
        ),
      ),
    );

    // Verificar que el mensaje es visible
    expect(find.text('Error de conexión con el sensor'), findsOneWidget);

    // Tocar el botón de reintentar
    await tester.tap(find.text('Reintentar'));
    await tester.pump();

    expect(retried, isTrue);
  });
}
```

---

## 4. Pruebas E2E y Regresion Visual con Playwright

Playwright es el estandar para validar flujos completos y evitar regresiones visuales en Web y Desktop (Electron/Tauri):

```typescript
// tests/e2e/login-flow.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Flujo de Autenticación', () => {
  test('Inicio de sesión exitoso y renderizado del dashboard', async ({ page }) => {
    await page.goto('/login');

    // Llenar formulario respetando etiquetas accesibles
    await page.getByLabel(/correo electrónico/i).fill('admin@lexur.corp');
    await page.getByLabel(/contraseña/i).fill('PasswordSegura123!');
    await page.getByRole('button', { name: /iniciar sesión/i }).click();

    // Esperar al dashboard y validar titulo
    await expect(page.getByRole('heading', { name: /centro de control/i })).toBeVisible();

    // Captura de regresion visual en modo oscuro
    await expect(page).toHaveScreenshot('dashboard-dark.png', {
      maxDiffPixelRatio: 0.01, // Tolerancia minima
    });
  });
});
```

---

## 5. Pruebas en Jetpack Compose (Android)

```kotlin
// app/src/androidTest/java/com/lexur/design/LxButtonTest.kt
package com.lexur.design

import androidx.compose.ui.test.*
import androidx.compose.ui.test.junit4.createComposeRule
import com.lexur.design.components.LxButton
import org.junit.Rule
import org.junit.Test

class LxButtonTest {
    @get:Rule
    val composeTestRule = createComposeRule()

    @Test
    fun buttonClickExecutesLambda() {
        var clicked = false
        composeTestRule.setContent {
            LxButton(text = "Ejecutar", onClick = { clicked = true })
        }

        composeTestRule.onNodeWithText("Ejecutar").performClick()
        assert(clicked)
    }
}
```

---

## 6. Checklist de Aprobacion de Testing (QA Gate)

- [ ] Cobertura de pruebas unitarias sobre logica de negocio >= 80%.
- [ ] Todos los componentes base tienen pruebas de renderizado en variantes primaria, secundaria, disabled y loading.
- [ ] No existen pruebas "flaky" (intermitentes) que dependan de tiempos de red arbitrarios (`sleep` o retardos ciegos).
- [ ] Las pruebas de accesibilidad con `axe-playwright` pasan con 0 violaciones.
- [ ] La suite completa corre en CI/CD antes de autorizar cualquier pull request a la rama `main`.
