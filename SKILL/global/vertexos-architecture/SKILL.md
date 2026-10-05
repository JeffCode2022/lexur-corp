---
name: vertexos-architecture
description: Principios de arquitectura en capas para todos los proyectos VertexOS. Actívalo cuando el usuario quiera estructurar un proyecto, definir la arquitectura, organizar carpetas, decidir cómo separar responsabilidades, o cuando se mencione: arquitectura, capas, clean architecture, separación de responsabilidades, patrón de repositorio, o cómo organizar el código en cualquier proyecto VertexOS.
---

# VertexOS — Arquitectura en Capas

Todo proyecto VertexOS sigue la arquitectura en capas inspirada en Clean Architecture, adaptada para ser pragmática y no sobreingeniería.

---

## 🏛️ Principio YAGNI Aplicado (Ponytail Method)

Antes de añadir cualquier capa, clase o abstracción, pregunta:

1. **¿Necesito esto ahora?** — Si no, no lo construyas
2. **¿Ya existe en el proyecto?** — Reutiliza antes de crear
3. **¿Lo provee el framework/SDK?** — Úsalo directamente
4. **¿Puede ser una sola función?** — Prefiere simplicidad
5. **¿Qué pasa si no lo hago?** — Si nada, no lo hagas

---

## 📐 Arquitectura Estándar VertexOS

### Para Apps Móviles/Desktop (Flutter + Kotlin)

```
Presentation Layer   → UI, Widgets, BLoC/Cubit, ViewModels
     ↓ (solo hacia abajo)
Domain Layer         → Use Cases, Entities, Repository Interfaces
     ↓ (solo hacia abajo)
Data Layer           → Repositories, DataSources, Models, APIs
     ↓
Infrastructure       → Base de datos, Red, Hardware, Sistema OS
```

### Para Web Apps / Backends (Next.js / Electron)

```
UI Layer             → Pages, Components, Hooks
     ↓
Application Layer    → Services, Store (Zustand/Redux)
     ↓
Data Layer           → API calls, Local DB, Cache
     ↓
Infrastructure       → SQLite, File System, External APIs
```

---

## 📂 Estructura de Carpetas Universal

```
{proyecto}/
├── src/
│   ├── core/              # Código compartido entre features
│   │   ├── theme/         # Design tokens, ThemeData
│   │   ├── widgets/       # Widgets/components reutilizables
│   │   ├── utils/         # Utilidades puras (sin side effects)
│   │   ├── errors/        # Tipos de error y manejo
│   │   └── constants/     # Constantes globales
│   ├── features/          # Features del dominio de negocio
│   │   └── {feature}/
│   │       ├── data/      # Implementaciones concretas
│   │       ├── domain/    # Lógica de negocio pura
│   │       └── presentation/  # UI y gestión de estado
│   └── app/               # Punto de entrada, routing, DI
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/
├── PROYECTO.md
└── .security-audit.md
```

---

## 🔄 Gestión de Estado: Patrón BLoC

Todos los proyectos Flutter usan BLoC. Reglas:

```dart
// ✅ CORRECTO: Un estado por condición
sealed class ProjectState {}
class ProjectLoading extends ProjectState {}
class ProjectLoaded extends ProjectState {
  final List<Project> projects;
  ProjectLoaded(this.projects);
}
class ProjectError extends ProjectState {
  final String message;
  ProjectError(this.message);
}
class ProjectEmpty extends ProjectState {}

// ❌ INCORRECTO: Estado con bool isLoading
class ProjectState {
  bool isLoading;     // Ambiguo
  String? error;      // Puede ser null pero isLoading también true
  List? data;         // Sin tipado fuerte
}
```

---

## 🧩 Inyección de Dependencias

### Dart/Flutter — GetIt

```dart
// lib/app/di/injection.dart
final getIt = GetIt.instance;

void setupDependencies() {
  // Core
  getIt.registerSingleton<VXAiRouter>(VXAiRouter());
  
  // Features
  getIt.registerFactory<VoiceBloc>(
    () => VoiceBloc(processor: getIt<VoiceCommandProcessor>()),
  );
}
```

### Node.js — Constructor injection simple

```typescript
// No usar frameworks de DI complejos para proyectos pequeños
// Pasar dependencias por constructor directamente
class ProjectService {
  constructor(
    private readonly db: Database,
    private readonly ai: AIRouter,
  ) {}
}
```

---

## 📏 Métricas de Calidad de Código

| Métrica | Límite |
|---------|--------|
| Líneas por archivo | ≤ 300 |
| Líneas por función/método | ≤ 40 |
| Parámetros por función | ≤ 4 |
| Nivel de anidamiento | ≤ 4 |
| Complejidad ciclomática | ≤ 10 |
| Cobertura de tests | ≥ 70% |

Si un archivo supera estos límites → refactorizar antes de continuar.

---

## 🔌 Comunicación entre Capas

### Dart/Flutter
```
Widget → BLoC (via events)
BLoC → UseCase (via call)
UseCase → Repository Interface
Repository Impl → DataSource
DataSource → API/DB/Hardware
```

### Node.js/Next.js
```
Component → Hook → Service → Repository → DB
```

**Regla de oro**: Las capas superiores NUNCA conocen las implementaciones de las inferiores. Solo interfaces/contratos.

---

## 📋 Referencias

- Clean Architecture: https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
- BLoC Pattern: https://bloclibrary.dev
- YAGNI: https://martinfowler.com/bliki/Yagni.html
