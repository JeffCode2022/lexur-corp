# lexur-corp

> **LEXUR CORP** — Enterprise Software Solutions, Multiplatform Design System & Autonomous Engineering Architecture.

---

## 🏛️ Acerca de LEXUR CORP

LEXUR CORP es una corporación de ingeniería de software enfocada en diseñar y construir arquitecturas digitales de alto impacto, plataformas distribuidas en la nube y sistemas de misión crítica para fintech, salud, logística, retail y energía.

Este repositorio consolida:
1. **Landing Page Oficial de LEXUR**: Interfaz web de alta fidelidad, inspirada en los estándares de precisión de Apple, Tesla, X y Meta.
2. **Suite Multiplataforma de Design System ("Precision Dark / Precision Light")**: Tokens unificados para Web, Flutter, Jetpack Compose y SwiftUI.
3. **Ecosistema de Skills para Agentes Autónomos**: Reglas rigurosas de accesibilidad (WCAG 2.2 AA), ciberseguridad defensiva, rendimiento extremo (60/120 FPS) y tolerancia cero a efectos decorativos no funcionales.

---

## 📂 Estructura del Repositorio

```text
lexur-corp/
├── .agents/
│   └── skills/                         # Skills para agentes inteligentes (Antigravity / Gemini CLI)
│       ├── lexur-accessibility/        # WCAG 2.2 AA universal
│       ├── lexur-android-compose/      # Jetpack Compose nativo
│       ├── lexur-components/           # Especificación de componentes Lx*
│       ├── lexur-design-system/        # Tokens (CSS, Dart, Kotlin, Swift) y generador
│       ├── lexur-desktop-apps/         # Tauri v2 y Electron
│       ├── lexur-flutter-ui/           # Flutter multiplataforma & BLoC
│       ├── lexur-frontend-security/    # Blindaje XSS, CSP & Keystore/Keychain
│       ├── lexur-frontend-testing/     # Pirámide de pruebas & Playwright
│       ├── lexur-ios-swiftui/          # iOS/macOS SwiftUI nativo
│       ├── lexur-motion/               # Físicas, easings y microinteracciones
│       ├── lexur-performance/          # Core Web Vitals (<1.8s LCP) & 60/120 FPS
│       ├── lexur-ui-review/            # Escáner automatizado de calidad visual
│       └── lexur-web-nextjs/           # Next.js App Router + Tailwind v4
│
├── landing-page/                       # Sitio web principal de LEXUR
│   ├── index.html                      # Landing page de producción (Light Apple/Tesla Precision)
│   ├── index_dark.html                 # Versión Dark Theme de alta fidelidad
│   ├── assets/                         # Identidad visual, tipografías vectoriales e iconografía
│   └── build_landing*.py               # Generadores modulares y scripts de compilación
│
└── SKILL/                              # Catálogo empresarial de skills organizados
    ├── frontend/                       # Suite frontend LEXUR
    ├── global/                         # Skills globales de plataforma (VertexOS)
    ├── specific/                       # Skills específicos por proyecto
    └── README.md                       # Documentación técnica del catálogo
```

---

## 🎨 Suite Frontend & Design Tokens

Los tokens de diseño (`tokens.json`) actúan como la única fuente de la verdad para todas las plataformas:

- **Web / Next.js**: `lexur-tokens.css` (Tailwind CSS v4)
- **Flutter**: `lexur_tokens.dart`
- **Android**: `LexurTokens.kt` (Jetpack Compose)
- **iOS / macOS**: `LexurTokens.swift` (SwiftUI)

### Herramientas Ejecutables:
- **Generador de Tokens**:
  ```bash
  node .agents/skills/lexur-design-system/scripts/generate-tokens.mjs
  ```
- **Auditor de Contraste WCAG 2.2**:
  ```bash
  node .agents/skills/lexur-design-system/scripts/check-contrast.mjs
  ```
- **Escáner Anti-Glass / Anti-Degradados**:
  ```bash
  node .agents/skills/lexur-ui-review/scripts/scan-forbidden-styles.mjs <directorio>
  ```

---

## 🚀 Despliegue de la Landing Page

Para visualizar o servir la landing page localmente:

```bash
# Con Python
cd landing-page
python -m http.server 8000
```

Visita `http://localhost:8000` en tu navegador.

---

## 🛡️ Principios Inviolables LEXUR

1. **Seguridad Primero**: Auditoría estricta antes de integrar dependencias externas.
2. **Precisión sobre Decoración**: Superficies sólidas, legibilidad máxima y cero degradados o desenfoques artificiales.
3. **Consistencia Multiplataforma**: La misma jerarquía visual en Web, Desktop y Mobile.
4. **Manejo Explícito de Estados**: Loading, Error, Empty y Success obligatorios.
5. **Accesibilidad y Rendimiento**: WCAG 2.2 AA y 60/120 FPS sin excepciones.

---

## 📄 Licencia

© 2026 LEXUR Software Solutions Corp. Todos los derechos reservados.
