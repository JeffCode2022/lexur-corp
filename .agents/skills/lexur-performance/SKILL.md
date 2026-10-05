---
name: lexur-performance
description: Estandares y optimizaciones de rendimiento frontend para web, desktop y movil en LEXUR. Activalo al auditar o mejorar Core Web Vitals (LCP, INP, CLS), tiempos de inicio (Cold Start / TTI), optimizacion de bundles, virtualizacion de listas masivas, perfiles de tasa de refresco a 60/120 FPS sin jank en Flutter/Compose/SwiftUI, o reduccion de consumo de memoria y CPU.
---

# LEXUR — Performance Engineering

En LEXUR, una experiencia "futurista y profesional" se define por la velocidad instantanea de respuesta. Una interfaz bella que tiene micro-parones o tarda en cargar pierde toda credibilidad.

---

## 1. Metricas Objetivas y Limites Inviolables

| Plataforma | Metrica | Umbral Maximo LEXUR | Como se mide |
|---|---|---|---|
| **Web** | Largest Contentful Paint (LCP) | **< 1.8 segundos** | Chrome DevTools / Lighthouse |
| **Web** | Interaction to Next Paint (INP) | **< 100 ms** (ideal < 50ms) | Web Vitals extension |
| **Web** | Cumulative Layout Shift (CLS) | **< 0.05** (ideal 0.0) | PerformanceObserver |
| **Web** | Tamano de Bundle JS inicial | **< 150 KB** (gzipped) | `@next/bundle-analyzer` |
| **Desktop / Movil** | Tasa de refresco en animaciones | **60 FPS sostenidos** (120 FPS en displays ProMotion) | Flutter DevTools / Android Profiler / Instruments |
| **Desktop** | Inicio en frio (Cold Start) | **< 800 ms** | Medido en ejecutable de produccion |
| **Desktop** | Memoria base en reposo | **< 50 MB** (Tauri) / **< 180 MB** (Electron) | Administrador de tareas del OS |

---

## 2. Optimizacion Web y Core Web Vitals (Next.js)

### 2.1. LCP (Largest Contentful Paint) < 1.8s
1. **Prioridad de la imagen Hero**:
   - Toda imagen principal en el viewport DEBE llevar `priority={true}` en `next/image` y formatos modernos (AVIF, WebP).
2. **Cero bloqueo por fuentes de terceros**:
   - Usar `next/font` con fuentes empaquetadas localmente (`geist`). NUNCA peticiones remotas a Google Fonts en tiempo de ejecucion.
3. **Server Components por defecto**:
   - Enviar HTML prerenderizado al cliente; evitar que el usuario vea una pantalla blanca mientras descarga JavaScript.

### 2.2. INP (Interaction to Next Paint) < 100ms
1. **Evitar tareas largas en el hilo principal (> 50ms)**:
   - Procesamiento pesado de datos (filtrado de miles de filas, calculos criptograficos) debe trasladarse a un Web Worker.
2. **`useTransition` y `startTransition`**:
   - Marcar actualizaciones no urgentes (como filtrado de listas o busqueda en vivo) con `startTransition` para mantener los inputs fluidos.
3. **Virtualizacion de listas**:
   - Cualquier lista o tabla con mas de 50 elementos DEBE utilizar virtualizacion (`@tanstack/react-virtual`).

### 2.3. CLS (Cumulative Layout Shift) < 0.05
1. Reservar siempre espacio explicito para imagenes (`width` y `height` definidos o `aspect-ratio`).
2. Skeletons con las dimensiones exactas del contenido final para evitar saltos cuando los datos lleguen.
3. Cero inyecciones de banners o modales que empujen el contenido hacia abajo.

---

## 3. Optimizacion en Flutter (60/120 FPS)

1. **Uso riguroso de `const`**:
   - Todo widget inmutable DEBE marcarse con `const` para evitar reconstrucciones en el arbol de elementos.
2. **Repaint Boundaries**:
   - Envolver widgets que se animan con frecuencia (ej: contadores, barras de progreso) en un `RepaintBoundary` para evitar repintar toda la pantalla.
3. **`ListView.builder` / `CustomScrollView`**:
   - Prohibido renderizar listas con `Column(children: [...])`. Usar builders perezosos para renderizar solo lo visible.
4. **Inspeccion en DevTools**:
   - Cero "jank frames" (marcos rojos/amarillos) en el perfilador de Flutter.

---

## 4. Optimizacion en Android (Jetpack Compose)

1. **Estabilidad de Recomposiciones**:
   - Usar modelos de datos inmutables marcados con `@Immutable` o listas de `kotlinx.collections.immutable` (`ImmutableList`).
   - Evitar lambdas inestables que provoquen recomposicion innecesaria de toda la vista.
2. **`LazyColumn` / `LazyRow` con `key` explicita**:
   - Asignar siempre `key = { item.id }` para que Compose recicle los elementos sin redibujar toda la lista.
3. **Derivacion de estado**:
   - Usar `derivedStateOf { ... }` para calculos basados en estados frecuentes (como la posicion del scroll).

---

## 5. Optimizacion en iOS (SwiftUI)

1. **Evitar `@State` innecesario**:
   - Mantener el arbol de vistas lo mas puro posible; los cambios de estado deben ser quirurgicos.
2. **`LazyVStack` y `Identifiable`**:
   - Listas largas siempre con `LazyVStack` o `List` nativa para reutilizacion de celdas.
3. **Animaciones de aceleracion por GPU**:
   - Animar unicamente atributos soportados por Core Animation (`opacity`, `transform` via `.offset` o `.scaleEffect`).

---

## 6. Auditoria de Rendimiento (Comando de Verificacion)

Para proyectos web, ejecutar auditoria antes de liberar a produccion:
```bash
pnpm build && pnpm exec lighthouse http://localhost:3000 --output html --output-path ./reports/lighthouse.html --chrome-flags="--headless"
```
Requisito de aprobacion LEXUR: Puntuacion >= 90 en todas las categorias.
