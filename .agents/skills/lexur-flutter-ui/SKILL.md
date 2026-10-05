---
name: lexur-flutter-ui
description: Estandares de interfaz y arquitectura Flutter para proyectos multiplataforma LEXUR (iOS, Android, Web, Desktop). Activalo cuando se construyan pantallas, widgets, componentes visuales, navegacion (GoRouter), gestion de estado (BLoC / Cubit) o temas en Flutter. Aplica rigurosamente el sistema de diseno LEXUR "Precision Dark", los 4 estados UI obligatorios (Loading, Error, Empty, Success), y prohibe fondos con degradados, blur (BackdropFilter) y estilos genéricos.
---

# LEXUR — Flutter UI Standards

Flutter permite renderizado pixel-perfect en movil, desktop y web con 60/120 FPS. En LEXUR, la interfaz se construye con precision industrial, superficies solidas y ausencia total de adornos artificiales o desenfoques innecesarios.

---

## 1. Tokens de Diseno Flutter

Copia el archivo generado por el design system a tu proyecto:
`lib/core/theme/tokens/lexur_tokens.dart` (generado desde `tokens.json`).

### 1.1. Extension de Tema (`ThemeExtension`)

Para consumir los tokens respetando el modo claro/oscuro del sistema y del usuario:

```dart
// lib/core/theme/lexur_theme_extension.dart
import 'package:flutter/material.dart';
import 'tokens/lexur_tokens.dart';

@immutable
class LexurTheme extends ThemeExtension<LexurTheme> {
  final LxColorTokens colors;

  const LexurTheme({required this.colors});

  static final LexurTheme dark = LexurTheme(colors: LxColorTokens.dark);
  static final LexurTheme light = LexurTheme(colors: LxColorTokens.light);

  @override
  ThemeExtension<LexurTheme> copyWith({LxColorTokens? colors}) {
    return LexurTheme(colors: colors ?? this.colors);
  }

  @override
  ThemeExtension<LexurTheme> lerp(ThemeExtension<LexurTheme>? other, double t) {
    if (other is! LexurTheme) return this;
    return this; // Sin interpolaciones de degradado entre temas; cambio limpio
  }
}

extension LexurThemeContext on BuildContext {
  LexurTheme get lx => Theme.of(this).extension<LexurTheme>() ?? LexurTheme.dark;
  LxColorTokens get lxColors => lx.colors;
}
```

### 1.2. Configuracion de `ThemeData` solido

```dart
// lib/core/theme/theme_factory.dart
import 'package:flutter/material.dart';
import 'tokens/lexur_tokens.dart';
import 'lexur_theme_extension.dart';

class LexurThemeFactory {
  static ThemeData buildDarkTheme() {
    final colors = LxColorTokens.dark;
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.dark,
      scaffoldBackgroundColor: colors.bgCanvas,
      canvasColor: colors.bgCanvas,
      splashFactory: NoSplash.splashFactory, // Sin ondas ripple Material excesivas
      highlightColor: Colors.transparent,
      fontFamily: LxType.fontSans,
      dividerTheme: DividerThemeData(
        color: colors.borderDefault,
        thickness: 1.0,
        space: 1.0,
      ),
      appBarTheme: AppBarTheme(
        backgroundColor: colors.bgCanvas,
        surfaceTintColor: Colors.transparent, // NUNCA tintes de Material You
        elevation: 0,
        scrolledUnderElevation: 0,
        centerTitle: false,
        titleTextStyle: LxType.h4.copyWith(color: colors.textPrimary),
      ),
      extensions: [LexurTheme.dark],
    );
  }

  static ThemeData buildLightTheme() {
    final colors = LxColorTokens.light;
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.light,
      scaffoldBackgroundColor: colors.bgCanvas,
      canvasColor: colors.bgCanvas,
      splashFactory: NoSplash.splashFactory,
      highlightColor: Colors.transparent,
      fontFamily: LxType.fontSans,
      dividerTheme: DividerThemeData(
        color: colors.borderDefault,
        thickness: 1.0,
        space: 1.0,
      ),
      appBarTheme: AppBarTheme(
        backgroundColor: colors.bgCanvas,
        surfaceTintColor: Colors.transparent,
        elevation: 0,
        scrolledUnderElevation: 0,
        centerTitle: false,
        titleTextStyle: LxType.h4.copyWith(color: colors.textPrimary),
      ),
      extensions: [LexurTheme.light],
    );
  }
}
```

---

## 2. Reglas Inviolables en Flutter

1. **PROHIBIDO `BackdropFilter` o `ImageFilter.blur`**:
   - Todo dialog, modal, drawer o header es solido con borde hairline.
2. **PROHIBIDO `LinearGradient`, `RadialGradient` o `SweepGradient`**:
   - Fondos solidos con escala de superficies (`bgCanvas`, `bgSurface1`, `bgSurface2`, `bgSurface3`).
3. **Cero tintes de elevacion de Material You (`surfaceTintColor: Colors.transparent`)**:
   - Material 3 por defecto mezcla un color primario en superficies elevadas. Debe anularse a `Colors.transparent`.
4. **Barras de navegacion e iOS (Cupertino)**:
   - Al usar widgets de estilo iOS, asignar `backgroundColor` solido sin transparencia para evitar el efecto de vidrio nativo.

---

## 3. Los 4 Estados UI Obligatorios

Toda vista o widget que consulte datos DEBE implementar explicitamente:
1. `LxLoadingView` (Skeleton solido o spinner 1.5px si dura > 300ms)
2. `LxErrorView` (Icono, mensaje claro, boton Reintentar)
3. `LxEmptyView` (Icono sutil, explicacion amigable, CTA de creacion)
4. `LxSuccessView` (Contenido final estructurado)

### Implementacion con BLoC Pattern

```dart
// Ejemplo de consumo en UI
BlocBuilder<TelemetryBloc, TelemetryState>(
  builder: (context, state) => switch (state) {
    TelemetryLoading() => const LxLoading(message: 'Sincronizando telemetría...'),
    TelemetryError(:final message) => LxError(
        message: message,
        onRetry: () => context.read<TelemetryBloc>().add(RefreshTelemetry()),
      ),
    TelemetryEmpty() => LxEmpty(
        icon: Icons.speed_outlined,
        title: 'Sin métricas activas',
        subtitle: 'Inicia el motor para comenzar a registrar datos en tiempo real.',
        actionTitle: 'Conectar sensores',
        onAction: () => context.read<TelemetryBloc>().add(ConnectSensors()),
      ),
    TelemetrySuccess(:final metrics) => TelemetryDashboard(metrics: metrics),
  },
);
```

---

## 4. Componente de Referencia: Boton Solido LEXUR (`LxButton`)

```dart
// lib/core/widgets/lx_button.dart
import 'package:flutter/material.dart';
import '../theme/tokens/lexur_tokens.dart';
import '../theme/lexur_theme_extension.dart';

enum LxButtonVariant { primary, secondary, ghost, danger }
enum LxButtonSize { sm, md, lg }

class LxButton extends StatelessWidget {
  final String label;
  final VoidCallback? onPressed;
  final LxButtonVariant variant;
  final LxButtonSize size;
  final Widget? icon;
  final bool isLoading;

  const LxButton({
    super.key,
    required this.label,
    this.onPressed,
    this.variant = LxButtonVariant.primary,
    this.size = LxButtonSize.md,
    this.icon,
    this.isLoading = false,
  });

  @override
  Widget build(BuildContext context) {
    final colors = context.lxColors;

    final (bgColor, fgColor, borderSide) = switch (variant) {
      LxButtonVariant.primary => (colors.bgInverse, colors.textInverse, BorderSide.none),
      LxButtonVariant.secondary => (colors.bgSurface2, colors.textPrimary, BorderSide(color: colors.borderDefault)),
      LxButtonVariant.ghost => (Colors.transparent, colors.textPrimary, BorderSide.none),
      LxButtonVariant.danger => (colors.statusDanger, colors.textInverse, BorderSide.none),
    };

    final (height, padding, textStyle, radius) = switch (size) {
      LxButtonSize.sm => (LxControl.sm, const EdgeInsets.symmetric(horizontal: 12), LxType.bodySm, LxRadius.sm),
      LxButtonSize.md => (LxControl.md, const EdgeInsets.symmetric(horizontal: 16), LxType.label, LxRadius.md),
      LxButtonSize.lg => (LxControl.lg, const EdgeInsets.symmetric(horizontal: 20), LxType.body, LxRadius.md),
    };

    return SizedBox(
      height: height,
      child: OutlinedButton(
        style: OutlinedButton.styleFrom(
          backgroundColor: bgColor,
          foregroundColor: fgColor,
          side: borderSide,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(radius)),
          padding: padding,
          elevation: 0,
        ),
        onPressed: isLoading ? null : onPressed,
        child: isLoading
            ? SizedBox(
                width: 16,
                height: 16,
                child: CircularProgressIndicator(strokeWidth: 2, color: fgColor),
              )
            : Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  if (icon != null) ...[icon!, const SizedBox(width: LxSpace.s8)],
                  Text(label, style: textStyle.copyWith(color: fgColor)),
                ],
              ),
      ),
    );
  }
}
```

---

## 5. Verificacion de Rendimiento y Calidad

- Ejecutar `flutter analyze` sin advertencias.
- Ejecutar escaner de estilos prohibidos:
  `node <lexur-ui-review>/scripts/scan-forbidden-styles.mjs lib/`
- Validar tasa de refresco a 60/120 FPS sin frames rojos en Flutter DevTools Performance.
- Probar con escalado de texto de accesibilidad (Large Text al 200%) asegurando que ningun texto quede cortado ni cause `RenderFlex overflow`.
