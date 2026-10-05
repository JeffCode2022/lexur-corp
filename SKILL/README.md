# LEXUR CORP — Ecosistema Empresarial de Skills

Skills de desarrollo e ingenieria para los proyectos de LEXUR CORP y VertexOS.

---

## 🎨 Suite Frontend LEXUR ("Precision Dark" — Apple, Tesla, X, Meta)

Diseñada para construir interfaces de grado profesional para Web, Desktop y Mobile con estetica futurista, superficies solidas, y **tolerancia cero a gradientes, glassmorphism, liquid glass o desenfoques artificiales**.

| Skill | Proposito | Cuando activar |
|---|---|---|
| **`lexur-design-system`** | Lenguaje visual "Precision Dark" y tokens unificados | Al diseñar cualquier pantalla, definir tokens de color, tipografia o espaciado |
| **`lexur-components`** | Especificaciones y anatomia de componentes UI (`Lx*`) | Al construir botones, inputs, modales, tablas, navegación o estados |
| **`lexur-motion`** | Fisicas, easings y microinteracciones fluidas | Al implementar animaciones, transiciones, loaders y feedback háptico |
| **`lexur-ui-review`** | Puerta de calidad visual y escaner de código | Antes de entregar, hacer merge o publicar cualquier pantalla o componente |
| **`lexur-web-nextjs`** | Web con Next.js (App Router), React, TS y Tailwind v4 | Al construir sitios, landings, dashboards web o capas web de desktop |
| **`lexur-desktop-apps`** | Apps de escritorio nativas con Tauri v2 y Electron | Al crear herramientas desktop, ventanas sólidas, comandos IPC y SQLite |
| **`lexur-flutter-ui`** | Flutter multiplataforma (iOS, Android, Web, Desktop) | Al programar con Flutter, extensiones de tema, BLoC y estados UI |
| **`lexur-android-compose`**| Android nativo con Kotlin y Jetpack Compose | Al programar interfaces Android nativas sin Dynamic Color (Material You) |
| **`lexur-ios-swiftui`** | iOS y macOS nativo con SwiftUI y SF Pro | Al programar para Apple sin Liquid Glass (`.sharedBackgroundVisibility(.hidden)`) |
| **`lexur-accessibility`** | Accesibilidad universal WCAG 2.2 nivel AA | Al auditar foco por teclado, lectores de pantalla y soporte de texto grande |
| **`lexur-performance`** | Optimizacion de Core Web Vitals y 60/120 FPS | Al optimizar LCP (< 1.8s), INP (< 100ms), CLS (< 0.05) y eliminar jank frames |
| **`lexur-frontend-security`**| Ciberseguridad frontend, CSP y blindaje de datos | Al configurar CSP, sanitizacion anti-XSS y almacenamiento en Keychain/Keystore |
| **`lexur-frontend-testing`** | Estrategia de pruebas automatizadas y piramide | Al escribir pruebas unitarias, de widgets, E2E con Playwright y regresion visual |

---

## 🛠️ Herramientas Ejecutables Incluidas en LEXUR

1. **Validador de Contraste WCAG 2.2 AA**:
   `node F:\LEXUR CORP\SKILL\frontend\lexur-design-system\scripts\check-contrast.mjs [tokens.json]`
2. **Generador Multiplataforma de Tokens** (CSS, Flutter, Compose, SwiftUI):
   `node F:\LEXUR CORP\SKILL\frontend\lexur-design-system\scripts\generate-tokens.mjs [tokens.json] [salida]`
3. **Escáner Automatizado Anti-Glass / Anti-Degradados**:
   `node F:\LEXUR CORP\SKILL\frontend\lexur-ui-review\scripts\scan-forbidden-styles.mjs <directorio_codigo>`

---

## 🏛️ Skills Globales de Plataforma (Ecosistema VertexOS)

| Skill | Descripcion | Cuando activar |
|---|---|---|
| `vertexos-master` | Orquestador principal | Siempre al inicio de sesion o nuevo proyecto |
| `vertexos-security-audit` | Auditoria de seguridad | Antes de instalar CUALQUIER dependencia |
| `vertexos-architecture` | Arquitectura en capas | Al estructurar un proyecto |
| `vertexos-flutter-standards` | Estandares Flutter + estados UI | Al trabajar en Flutter |
| `vertexos-kotlin-android` | Kotlin, root, ADB, accessibility | Al trabajar con Android nativo |
| `vertexos-ai-integration` | Gemini + Ollama dual IA | Al integrar IA en cualquier proyecto |
| `vertexos-ui-design` | Sistema de diseno VertexOS base | Al disenar pantallas base de VertexOS |

---

## 📱 Skills Especificos por Proyecto

| Skill | Proyecto | Cuando activar |
|---|---|---|
| `vertexos-mobile-voice` | VertexOS Mobile | Al implementar comandos de voz |
| `vertexos-desktop-electron` | VertexOS Desktop | Al trabajar en el gestor desktop |
| `vertexos-pentest-lab` | Laboratorio de Seguridad | Al integrar herramientas de pentesting |

---

## 🛡️ Principios Inviolables LEXUR CORP

1. **Seguridad Primero** — Auditar antes de instalar cualquier dependencia.
2. **Precision sobre Decoracion** — Cero degradados, cero glassmorphism, cero liquid glass.
3. **Consistencia Multiplataforma** — Los tokens en `tokens.json` alimentan Web, Desktop y Mobile sin divergencias.
4. **Estados Explicitos** — Todo componente con datos maneja: Loading, Error, Empty, Success.
5. **Accesibilidad y Rendimiento** — WCAG 2.2 AA y 60/120 FPS sin excepciones.
