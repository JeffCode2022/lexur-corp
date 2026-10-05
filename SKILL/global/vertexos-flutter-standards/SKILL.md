---
name: vertexos-flutter-standards
description: Estandares de codigo Flutter para todos los proyectos VertexOS con interfaz movil o desktop. Activalo cuando el usuario quiera crear pantallas, widgets, componentes UI, o cuando se trabaje con Flutter en cualquier proyecto VertexOS. Incluye el sistema de diseno VertexOS (blanco/gris/acentos oscuros), gestion de estados loading/error/empty/success, estructura de carpetas, y convenciones de codigo.
---

# VertexOS — Estandares Flutter

Todos los proyectos Flutter dentro de VertexOS siguen estas convenciones. El objetivo: codigo limpio, consistente y una UI que nunca parezca generica.

---

## Design Tokens (lib/core/theme/vertexos_tokens.dart)

```dart
class VXTokens {
  // Colores
  static const Color white        = Color(0xFFFFFFFF);
  static const Color grey50       = Color(0xFFF9FAFB);
  static const Color grey100      = Color(0xFFF3F4F6);
  static const Color grey200      = Color(0xFFE5E7EB);
  static const Color grey400      = Color(0xFF9CA3AF);
  static const Color grey600      = Color(0xFF4B5563);
  static const Color grey800      = Color(0xFF1F2937);
  static const Color grey900      = Color(0xFF111827);
  static const Color accent       = Color(0xFF1F2937);
  static const Color success      = Color(0xFF10B981);
  static const Color error        = Color(0xFFEF4444);
  static const Color warning      = Color(0xFFF59E0B);

  // Espaciado
  static const double space4  = 4.0;
  static const double space8  = 8.0;
  static const double space12 = 12.0;
  static const double space16 = 16.0;
  static const double space24 = 24.0;
  static const double space32 = 32.0;

  // Radios
  static const double radiusSm = 6.0;
  static const double radiusMd = 10.0;
  static const double radiusLg = 16.0;

  // Fuente
  static const String fontFamily = 'Inter';
}
```

---

## Estructura de Carpetas

```
lib/
├── core/
│   ├── theme/
│   │   ├── vertexos_tokens.dart
│   │   └── vertexos_theme.dart
│   ├── widgets/
│   │   ├── vx_loading.dart
│   │   ├── vx_error.dart
│   │   ├── vx_empty.dart
│   │   └── vx_button.dart
│   └── utils/
│       └── extensions.dart
├── features/
│   └── {nombre_feature}/
│       ├── data/
│       ├── domain/
│       └── presentation/
│           ├── bloc/
│           ├── pages/
│           └── widgets/
└── main.dart
```

---

## Los 4 Estados UI Obligatorios

### 1. Loading
```dart
class VXLoading extends StatelessWidget {
  final String? message;
  const VXLoading({super.key, this.message});
  @override
  Widget build(BuildContext context) => Center(
    child: Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        const CircularProgressIndicator(strokeWidth: 2, color: VXTokens.accent),
        if (message != null) ...[
          const SizedBox(height: VXTokens.space16),
          Text(message!, style: const TextStyle(color: VXTokens.grey400, fontSize: 14)),
        ],
      ],
    ),
  );
}
```

### 2. Error
```dart
class VXError extends StatelessWidget {
  final String message;
  final VoidCallback? onRetry;
  const VXError({super.key, required this.message, this.onRetry});
  @override
  Widget build(BuildContext context) => Center(
    child: Padding(
      padding: const EdgeInsets.all(VXTokens.space24),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          const Icon(Icons.error_outline, size: 48, color: VXTokens.error),
          const SizedBox(height: VXTokens.space16),
          Text(message, textAlign: TextAlign.center,
            style: const TextStyle(color: VXTokens.grey600, fontSize: 14)),
          if (onRetry != null) ...[
            const SizedBox(height: VXTokens.space24),
            OutlinedButton(onPressed: onRetry, child: const Text('Reintentar')),
          ],
        ],
      ),
    ),
  );
}
```

### 3. Empty State
```dart
class VXEmpty extends StatelessWidget {
  final String title;
  final String? subtitle;
  final IconData icon;
  final Widget? action;
  const VXEmpty({super.key, required this.title, this.subtitle,
    this.icon = Icons.inbox_outlined, this.action});
  @override
  Widget build(BuildContext context) => Center(
    child: Padding(
      padding: const EdgeInsets.all(VXTokens.space32),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, size: 64, color: VXTokens.grey200),
          const SizedBox(height: VXTokens.space16),
          Text(title, style: const TextStyle(fontSize: 16,
            fontWeight: FontWeight.w600, color: VXTokens.grey800)),
          if (subtitle != null) ...[
            const SizedBox(height: VXTokens.space8),
            Text(subtitle!, textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 14, color: VXTokens.grey400)),
          ],
          if (action != null) ...[
            const SizedBox(height: VXTokens.space24),
            action!,
          ],
        ],
      ),
    ),
  );
}
```

### 4. Patron de Uso con BLoC
```dart
BlocBuilder<MyBloc, MyState>(
  builder: (context, state) => switch (state) {
    MyLoadingState() => const VXLoading(message: 'Cargando...'),
    MyErrorState(:final message) => VXError(
        message: message,
        onRetry: () => context.read<MyBloc>().add(RetryEvent()),
      ),
    MyEmptyState() => const VXEmpty(
        title: 'Sin resultados',
        subtitle: 'Aun no hay datos disponibles',
      ),
    MySuccessState(:final data) => _buildContent(data),
  },
);
```

---

## Convenciones

- Archivos: snake_case.dart
- Clases: PascalCase
- Variables/funciones: camelCase
- Widgets VertexOS: prefijo VX (VXButton, VXCard, VXLoading)
- Max 300 lineas por archivo
- Max 40 lineas por metodo/widget build
- Usar const siempre que sea posible
- Sin logica de negocio en widgets

---

## Gestion de Estado

- Usar BLoC + Cubit (flutter_bloc)
- Un BLoC por feature
- States inmutables con Equatable
- Eventos claros y descriptivos

---

## Referencias

- Flutter BLoC: https://bloclibrary.dev
- Flutter pub: https://pub.dev
- Mix styling: https://pub.dev/packages/mix
