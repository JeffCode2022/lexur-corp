---
name: lexur-ios-swiftui
description: Estandares de interfaz nativa iOS y macOS con SwiftUI para el ecosistema LEXUR. Activalo al programar pantallas, componentes, navegacion (NavigationStack), modales o integraciones de sistema en Swift/SwiftUI. Prohibe estrictamente el uso de Liquid Glass y materiales translucidos (.ultraThinMaterial, .glassEffect, UIVisualEffectView), optando por fondos solidos controlados con .sharedBackgroundVisibility(.hidden), SF Pro nativo con Dynamic Type y respuesta haptica sutil.
---

# LEXUR — iOS & macOS UI (SwiftUI)

Desarrollo nativo para el ecosistema Apple combinando la sobriedad fisica de Tesla/X con la precision tipografica y la excelencia ergonomica de Apple, eliminando cualquier estetica de "vidrio liquido" (Liquid Glass) o degradados ornamentales.

---

## 1. Reglas Criticas de Diseno en iOS / SwiftUI

1. **PROHIBIDO Liquid Glass y Materiales Translucidos**:
   - NUNCA usar `.ultraThinMaterial`, `.thinMaterial`, `.regularMaterial`, `.thickMaterial`.
   - NUNCA usar `.glassEffect()`, `.glassProminent`, ni contenedores de vidrio en barras o fondos.
   - En toolbars y barras de navegacion, anular las capsulas de vidrio usando:
     `.sharedBackgroundVisibility(.hidden)`
   - Fondos solidos mediante `Color.lxBgCanvas`, `Color.lxBgSurface1`, etc.
2. **PROHIBIDO Gradientes**:
   - Cero `LinearGradient`, `RadialGradient`, `AngularGradient` o `.gradient`.
3. **Tipografia Nativa SF Pro + Dynamic Type**:
   - Usar la fuente del sistema (`Font.system(...)`) o el empaquetado de Geist, asegurando escalado accesible con Dynamic Type.
4. **Respuesta Haptica Sutil (Sensory Feedback)**:
   - Solo en acciones confirmadas o estados de exito/error con `.sensoryFeedback()`.

---

## 2. Consumo de Tokens LEXUR en SwiftUI

Usa `LexurTokens.swift` (generado desde `tokens.json`), el cual expone colores dinamicos solidos que responden a `.dark` y `.light`:

```swift
import SwiftUI

struct LexurCardPreview: View {
    var body: some View {
        VStack(alignment: .leading, spacing: LxSpace.s12) {
            Text("TELEMETRÍA EN TIEMPO REAL")
                .font(.system(size: 11, weight: .semibold))
                .tracking(0.8)
                .foregroundStyle(Color.lxTextSecondary)
            
            Text("1,420 RPM")
                .font(.system(size: 40, weight: .semibold, design: .monospaced))
                .foregroundStyle(Color.lxTextPrimary)
        }
        .padding(LxSpace.s16)
        .background(Color.lxBgSurface1) // Solido sin material ni blur
        .clipShape(RoundedRectangle(cornerRadius: LxRadius.lg, style: .continuous))
        .overlay(
            RoundedRectangle(cornerRadius: LxRadius.lg, style: .continuous)
                .stroke(Color.lxBorderSubtle, lineWidth: 1)
        )
    }
}
```

---

## 3. Barras de Navegacion y Toolbars Solidas (Sin Glass)

En iOS moderno, SwiftUI envuelve los elementos de toolbar en capsulas de vidrio por defecto. Para asegurar el diseno solido LEXUR:

```swift
import SwiftUI

struct LexurNavigationContainer<Content: View>: View {
    @ViewBuilder let content: Content

    var body: some View {
        NavigationStack {
            content
                .background(Color.lxBgCanvas.ignoresSafeArea())
                .toolbarBackground(Color.lxBgCanvas, for: .navigationBar)
                .toolbarBackground(.visible, for: .navigationBar)
                .toolbar {
                    ToolbarItem(placement: .topBarTrailing) {
                        Button(action: { /* Accion */ }) {
                            Image(systemName: "slider.horizontal.3")
                                .foregroundStyle(Color.lxTextPrimary)
                        }
                        // Oculta el contenedor de capsula de vidrio:
                        .sharedBackgroundVisibility(.hidden)
                    }
                }
        }
        .preferredColorScheme(.dark) // Dark-first por defecto
    }
}
```

---

## 4. Componente de Referencia: Boton Nativo LEXUR (`LxButton`)

```swift
import SwiftUI

public enum LxButtonVariant {
    case primary
    case secondary
    case ghost
    case danger
}

public enum LxButtonSize {
    case sm
    case md
    case lg

    var height: CGFloat {
        switch self {
        case .sm: return LxControl.sm
        case .md: return LxControl.md
        case .lg: return LxControl.lg
        }
    }

    var font: Font {
        switch self {
        case .sm: return .system(size: 13, weight: .medium)
        case .md: return .system(size: 14, weight: .medium)
        case .lg: return .system(size: 16, weight: .medium)
        }
    }
}

public struct LxButton: View {
    private let title: String
    private let variant: LxButtonVariant
    private let size: LxButtonSize
    private let isLoading: Bool
    private let action: () -> Void

    public init(
        _ title: String,
        variant: LxButtonVariant = .primary,
        size: LxButtonSize = .md,
        isLoading: Bool = false,
        action: @escaping () -> Void
    ) {
        self.title = title
        self.variant = variant
        self.size = size
        self.isLoading = isLoading
        self.action = action
    }

    public var body: some View {
        Button(action: action) {
            HStack(spacing: LxSpace.s8) {
                if isLoading {
                    ProgressView()
                        .tint(foregroundColor)
                        .scaleEffect(0.8)
                }
                Text(title)
                    .font(size.font)
                    .foregroundStyle(foregroundColor)
            }
            .frame(height: size.height)
            .padding(.horizontal, LxSpace.s16)
            .background(backgroundColor)
            .clipShape(RoundedRectangle(cornerRadius: LxRadius.md, style: .continuous))
            .overlay(
                RoundedRectangle(cornerRadius: LxRadius.md, style: .continuous)
                    .stroke(borderColor, lineWidth: 1)
            )
        }
        .buttonStyle(LxPressableButtonStyle())
        .disabled(isLoading)
        .sensoryFeedback(.selection, trigger: isLoading)
    }

    private var backgroundColor: Color {
        switch variant {
        case .primary: return Color.lxBgInverse
        case .secondary: return Color.lxBgSurface2
        case .ghost: return Color.clear
        case .danger: return Color.lxStatusDanger
        }
    }

    private var foregroundColor: Color {
        switch variant {
        case .primary: return Color.lxTextInverse
        case .secondary, .ghost: return Color.lxTextPrimary
        case .danger: return Color.lxTextInverse
        }
    }

    private var borderColor: Color {
        switch variant {
        case .secondary: return Color.lxBorderDefault
        default: return Color.clear
        }
    }
}

// Microinteraccion fisica: escala 0.98 al presionar
struct LxPressableButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? 0.98 : 1.0)
            .animation(LxMotion.fast(), value: configuration.isPressed)
    }
}
```

---

## 5. Los 4 Estados UI en SwiftUI

Estructura de patron con enum exhaustivo:

```swift
enum ViewState<T> {
    case loading(String?)
    case error(String, retry: () -> Void)
    case empty(title: String, subtitle: String, actionTitle: String?, onAction: (() -> Void)?)
    case success(T)
}

struct TelemetryView: View {
    @StateObject private var viewModel = TelemetryViewModel()

    var body: some View {
        ZStack {
            Color.lxBgCanvas.ignoresSafeArea()

            switch viewModel.state {
            case .loading(let msg):
                LxLoadingView(message: msg ?? "Cargando...")
            case .error(let msg, let retry):
                LxErrorView(message: msg, onRetry: retry)
            case .empty(let title, let subtitle, let actionTitle, let onAction):
                LxEmptyView(title: title, subtitle: subtitle, actionTitle: actionTitle, onAction: onAction)
            case .success(let data):
                TelemetryDashboardContent(data: data)
            }
        }
    }
}
```

---

## 6. Verificacion y Validacion SwiftUI

1. Ejecutar escaner de estilos prohibidos:
   `node <lexur-ui-review>/scripts/scan-forbidden-styles.mjs <AppFolder>`
2. Verificar en simulador con modo Dark y Light.
3. Verificar con Dynamic Type en tamano maximo de accesibilidad.
4. Comprobar que VoiceOver lea etiquetas semanticas correctas con `.accessibilityLabel()`.
