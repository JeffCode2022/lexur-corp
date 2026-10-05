// AUTO-GENERADO por lexur-design-system/scripts/generate-tokens.mjs (v1.0.0). NO EDITAR A MANO.
import SwiftUI
#if canImport(UIKit)
import UIKit
#endif

public struct LxColorSet {
    public let bgCanvas: Color
    public let bgSurface1: Color
    public let bgSurface2: Color
    public let bgSurface3: Color
    public let bgInverse: Color
    public let borderSubtle: Color
    public let borderDefault: Color
    public let borderStrong: Color
    public let borderControl: Color
    public let textPrimary: Color
    public let textSecondary: Color
    public let textTertiary: Color
    public let textDisabled: Color
    public let textInverse: Color
    public let textOnAccent: Color
    public let accentDefault: Color
    public let accentHover: Color
    public let accentPressed: Color
    public let accentSubtle: Color
    public let accentText: Color
    public let statusSuccess: Color
    public let statusSuccessSubtle: Color
    public let statusWarning: Color
    public let statusWarningSubtle: Color
    public let statusDanger: Color
    public let statusDangerSubtle: Color
    public let focusRing: Color
    public let overlayScrim: Color
}

public enum LxPalette {
    public static let dark = LxColorSet(
        bgCanvas: Color(.sRGB, red: 0, green: 0, blue: 0, opacity: 1),
        bgSurface1: Color(.sRGB, red: 0.039, green: 0.039, blue: 0.039, opacity: 1),
        bgSurface2: Color(.sRGB, red: 0.078, green: 0.078, blue: 0.078, opacity: 1),
        bgSurface3: Color(.sRGB, red: 0.122, green: 0.122, blue: 0.122, opacity: 1),
        bgInverse: Color(.sRGB, red: 0.98, green: 0.98, blue: 0.98, opacity: 1),
        borderSubtle: Color(.sRGB, red: 0.102, green: 0.102, blue: 0.102, opacity: 1),
        borderDefault: Color(.sRGB, red: 0.165, green: 0.165, blue: 0.165, opacity: 1),
        borderStrong: Color(.sRGB, red: 0.251, green: 0.251, blue: 0.251, opacity: 1),
        borderControl: Color(.sRGB, red: 0.369, green: 0.369, blue: 0.369, opacity: 1),
        textPrimary: Color(.sRGB, red: 0.961, green: 0.961, blue: 0.961, opacity: 1),
        textSecondary: Color(.sRGB, red: 0.639, green: 0.639, blue: 0.639, opacity: 1),
        textTertiary: Color(.sRGB, red: 0.502, green: 0.502, blue: 0.502, opacity: 1),
        textDisabled: Color(.sRGB, red: 0.302, green: 0.302, blue: 0.302, opacity: 1),
        textInverse: Color(.sRGB, red: 0.039, green: 0.039, blue: 0.039, opacity: 1),
        textOnAccent: Color(.sRGB, red: 1, green: 1, blue: 1, opacity: 1),
        accentDefault: Color(.sRGB, red: 0.18, green: 0.42, blue: 1, opacity: 1),
        accentHover: Color(.sRGB, red: 0.29, green: 0.502, blue: 1, opacity: 1),
        accentPressed: Color(.sRGB, red: 0.141, green: 0.341, blue: 0.839, opacity: 1),
        accentSubtle: Color(.sRGB, red: 0.043, green: 0.102, blue: 0.239, opacity: 1),
        accentText: Color(.sRGB, red: 0.42, green: 0.608, blue: 1, opacity: 1),
        statusSuccess: Color(.sRGB, red: 0.196, green: 0.843, blue: 0.294, opacity: 1),
        statusSuccessSubtle: Color(.sRGB, red: 0.043, green: 0.149, blue: 0.067, opacity: 1),
        statusWarning: Color(.sRGB, red: 1, green: 0.839, blue: 0.039, opacity: 1),
        statusWarningSubtle: Color(.sRGB, red: 0.169, green: 0.141, blue: 0.008, opacity: 1),
        statusDanger: Color(.sRGB, red: 1, green: 0.271, blue: 0.227, opacity: 1),
        statusDangerSubtle: Color(.sRGB, red: 0.18, green: 0.055, blue: 0.047, opacity: 1),
        focusRing: Color(.sRGB, red: 0.18, green: 0.42, blue: 1, opacity: 1),
        overlayScrim: Color(.sRGB, red: 0, green: 0, blue: 0, opacity: 0.722)
    )
    public static let light = LxColorSet(
        bgCanvas: Color(.sRGB, red: 1, green: 1, blue: 1, opacity: 1),
        bgSurface1: Color(.sRGB, red: 0.98, green: 0.98, blue: 0.98, opacity: 1),
        bgSurface2: Color(.sRGB, red: 0.949, green: 0.949, blue: 0.949, opacity: 1),
        bgSurface3: Color(.sRGB, red: 0.91, green: 0.91, blue: 0.91, opacity: 1),
        bgInverse: Color(.sRGB, red: 0.039, green: 0.039, blue: 0.039, opacity: 1),
        borderSubtle: Color(.sRGB, red: 0.937, green: 0.937, blue: 0.937, opacity: 1),
        borderDefault: Color(.sRGB, red: 0.878, green: 0.878, blue: 0.878, opacity: 1),
        borderStrong: Color(.sRGB, red: 0.761, green: 0.761, blue: 0.761, opacity: 1),
        borderControl: Color(.sRGB, red: 0.561, green: 0.561, blue: 0.561, opacity: 1),
        textPrimary: Color(.sRGB, red: 0.039, green: 0.039, blue: 0.039, opacity: 1),
        textSecondary: Color(.sRGB, red: 0.322, green: 0.322, blue: 0.322, opacity: 1),
        textTertiary: Color(.sRGB, red: 0.431, green: 0.431, blue: 0.431, opacity: 1),
        textDisabled: Color(.sRGB, red: 0.702, green: 0.702, blue: 0.702, opacity: 1),
        textInverse: Color(.sRGB, red: 0.98, green: 0.98, blue: 0.98, opacity: 1),
        textOnAccent: Color(.sRGB, red: 1, green: 1, blue: 1, opacity: 1),
        accentDefault: Color(.sRGB, red: 0.039, green: 0.361, blue: 1, opacity: 1),
        accentHover: Color(.sRGB, red: 0, green: 0.314, blue: 0.902, opacity: 1),
        accentPressed: Color(.sRGB, red: 0, green: 0.259, blue: 0.749, opacity: 1),
        accentSubtle: Color(.sRGB, red: 0.918, green: 0.941, blue: 1, opacity: 1),
        accentText: Color(.sRGB, red: 0.039, green: 0.361, blue: 1, opacity: 1),
        statusSuccess: Color(.sRGB, red: 0.118, green: 0.494, blue: 0.204, opacity: 1),
        statusSuccessSubtle: Color(.sRGB, red: 0.91, green: 0.961, blue: 0.922, opacity: 1),
        statusWarning: Color(.sRGB, red: 0.631, green: 0.361, blue: 0, opacity: 1),
        statusWarningSubtle: Color(.sRGB, red: 1, green: 0.957, blue: 0.878, opacity: 1),
        statusDanger: Color(.sRGB, red: 0.843, green: 0, blue: 0.082, opacity: 1),
        statusDangerSubtle: Color(.sRGB, red: 1, green: 0.922, blue: 0.925, opacity: 1),
        focusRing: Color(.sRGB, red: 0.039, green: 0.361, blue: 1, opacity: 1),
        overlayScrim: Color(.sRGB, red: 0, green: 0, blue: 0, opacity: 0.478)
    )
}

#if canImport(UIKit)
/// Colores dinamicos: siguen el ColorScheme activo. Dark es el default (todo lo que no sea .light).
public extension Color {
    static let lxBgCanvas = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 1, green: 1, blue: 1, alpha: 1) : UIColor(red: 0, green: 0, blue: 0, alpha: 1) })
    static let lxBgSurface1 = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.98, green: 0.98, blue: 0.98, alpha: 1) : UIColor(red: 0.039, green: 0.039, blue: 0.039, alpha: 1) })
    static let lxBgSurface2 = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.949, green: 0.949, blue: 0.949, alpha: 1) : UIColor(red: 0.078, green: 0.078, blue: 0.078, alpha: 1) })
    static let lxBgSurface3 = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.91, green: 0.91, blue: 0.91, alpha: 1) : UIColor(red: 0.122, green: 0.122, blue: 0.122, alpha: 1) })
    static let lxBgInverse = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.039, green: 0.039, blue: 0.039, alpha: 1) : UIColor(red: 0.98, green: 0.98, blue: 0.98, alpha: 1) })
    static let lxBorderSubtle = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.937, green: 0.937, blue: 0.937, alpha: 1) : UIColor(red: 0.102, green: 0.102, blue: 0.102, alpha: 1) })
    static let lxBorderDefault = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.878, green: 0.878, blue: 0.878, alpha: 1) : UIColor(red: 0.165, green: 0.165, blue: 0.165, alpha: 1) })
    static let lxBorderStrong = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.761, green: 0.761, blue: 0.761, alpha: 1) : UIColor(red: 0.251, green: 0.251, blue: 0.251, alpha: 1) })
    static let lxBorderControl = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.561, green: 0.561, blue: 0.561, alpha: 1) : UIColor(red: 0.369, green: 0.369, blue: 0.369, alpha: 1) })
    static let lxTextPrimary = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.039, green: 0.039, blue: 0.039, alpha: 1) : UIColor(red: 0.961, green: 0.961, blue: 0.961, alpha: 1) })
    static let lxTextSecondary = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.322, green: 0.322, blue: 0.322, alpha: 1) : UIColor(red: 0.639, green: 0.639, blue: 0.639, alpha: 1) })
    static let lxTextTertiary = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.431, green: 0.431, blue: 0.431, alpha: 1) : UIColor(red: 0.502, green: 0.502, blue: 0.502, alpha: 1) })
    static let lxTextDisabled = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.702, green: 0.702, blue: 0.702, alpha: 1) : UIColor(red: 0.302, green: 0.302, blue: 0.302, alpha: 1) })
    static let lxTextInverse = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.98, green: 0.98, blue: 0.98, alpha: 1) : UIColor(red: 0.039, green: 0.039, blue: 0.039, alpha: 1) })
    static let lxTextOnAccent = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 1, green: 1, blue: 1, alpha: 1) : UIColor(red: 1, green: 1, blue: 1, alpha: 1) })
    static let lxAccentDefault = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.039, green: 0.361, blue: 1, alpha: 1) : UIColor(red: 0.18, green: 0.42, blue: 1, alpha: 1) })
    static let lxAccentHover = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0, green: 0.314, blue: 0.902, alpha: 1) : UIColor(red: 0.29, green: 0.502, blue: 1, alpha: 1) })
    static let lxAccentPressed = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0, green: 0.259, blue: 0.749, alpha: 1) : UIColor(red: 0.141, green: 0.341, blue: 0.839, alpha: 1) })
    static let lxAccentSubtle = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.918, green: 0.941, blue: 1, alpha: 1) : UIColor(red: 0.043, green: 0.102, blue: 0.239, alpha: 1) })
    static let lxAccentText = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.039, green: 0.361, blue: 1, alpha: 1) : UIColor(red: 0.42, green: 0.608, blue: 1, alpha: 1) })
    static let lxStatusSuccess = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.118, green: 0.494, blue: 0.204, alpha: 1) : UIColor(red: 0.196, green: 0.843, blue: 0.294, alpha: 1) })
    static let lxStatusSuccessSubtle = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.91, green: 0.961, blue: 0.922, alpha: 1) : UIColor(red: 0.043, green: 0.149, blue: 0.067, alpha: 1) })
    static let lxStatusWarning = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.631, green: 0.361, blue: 0, alpha: 1) : UIColor(red: 1, green: 0.839, blue: 0.039, alpha: 1) })
    static let lxStatusWarningSubtle = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 1, green: 0.957, blue: 0.878, alpha: 1) : UIColor(red: 0.169, green: 0.141, blue: 0.008, alpha: 1) })
    static let lxStatusDanger = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.843, green: 0, blue: 0.082, alpha: 1) : UIColor(red: 1, green: 0.271, blue: 0.227, alpha: 1) })
    static let lxStatusDangerSubtle = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 1, green: 0.922, blue: 0.925, alpha: 1) : UIColor(red: 0.18, green: 0.055, blue: 0.047, alpha: 1) })
    static let lxFocusRing = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0.039, green: 0.361, blue: 1, alpha: 1) : UIColor(red: 0.18, green: 0.42, blue: 1, alpha: 1) })
    static let lxOverlayScrim = Color(uiColor: UIColor { $0.userInterfaceStyle == .light ? UIColor(red: 0, green: 0, blue: 0, alpha: 0.478) : UIColor(red: 0, green: 0, blue: 0, alpha: 0.722) })
}
#endif

public enum LxSpace {
    public static let s0: CGFloat = 0
    public static let s2: CGFloat = 2
    public static let s4: CGFloat = 4
    public static let s8: CGFloat = 8
    public static let s12: CGFloat = 12
    public static let s16: CGFloat = 16
    public static let s20: CGFloat = 20
    public static let s24: CGFloat = 24
    public static let s32: CGFloat = 32
    public static let s40: CGFloat = 40
    public static let s48: CGFloat = 48
    public static let s64: CGFloat = 64
    public static let s80: CGFloat = 80
    public static let s96: CGFloat = 96
    public static let s128: CGFloat = 128
}

public enum LxRadius {
    public static let none: CGFloat = 0
    public static let xs: CGFloat = 4
    public static let sm: CGFloat = 6
    public static let md: CGFloat = 10
    public static let lg: CGFloat = 14
    public static let xl: CGFloat = 20
    public static let full: CGFloat = 9999
}

public struct LxTextToken {
    public let size: CGFloat
    public let lineHeight: CGFloat
    public let tracking: CGFloat
    public let weight: Font.Weight
}

/// En iOS/macOS se usa la fuente del sistema (SF Pro). Ver lexur-ios-swiftui.
public enum LxType {
    public static let displayXl = LxTextToken(size: 72, lineHeight: 76, tracking: -2.88, weight: .semibold)
    public static let display = LxTextToken(size: 56, lineHeight: 60, tracking: -1.68, weight: .semibold)
    public static let h1 = LxTextToken(size: 40, lineHeight: 44, tracking: -1, weight: .semibold)
    public static let h2 = LxTextToken(size: 32, lineHeight: 38, tracking: -0.64, weight: .semibold)
    public static let h3 = LxTextToken(size: 24, lineHeight: 30, tracking: -0.36, weight: .semibold)
    public static let h4 = LxTextToken(size: 20, lineHeight: 26, tracking: -0.2, weight: .semibold)
    public static let bodyLg = LxTextToken(size: 17, lineHeight: 26, tracking: 0, weight: .regular)
    public static let body = LxTextToken(size: 15, lineHeight: 22, tracking: 0, weight: .regular)
    public static let bodySm = LxTextToken(size: 13, lineHeight: 18, tracking: 0, weight: .regular)
    public static let label = LxTextToken(size: 14, lineHeight: 20, tracking: 0, weight: .medium)
    public static let caption = LxTextToken(size: 12, lineHeight: 16, tracking: 0.12, weight: .medium)
    public static let overline = LxTextToken(size: 11, lineHeight: 14, tracking: 0.88, weight: .semibold)
    public static let metric = LxTextToken(size: 48, lineHeight: 52, tracking: -0.96, weight: .medium)
}

public enum LxMotion {
    public static let instant: Double = 0.08
    public static let fast: Double = 0.15
    public static let base: Double = 0.22
    public static let slow: Double = 0.32
    public static let deliberate: Double = 0.48
    public static func standard(_ duration: Double = LxMotion.base) -> Animation { .timingCurve(0.2, 0, 0, 1, duration: duration) }
    public static func enter(_ duration: Double = LxMotion.base) -> Animation { .timingCurve(0.05, 0.7, 0.1, 1, duration: duration) }
    public static func exit(_ duration: Double = LxMotion.base) -> Animation { .timingCurve(0.3, 0, 0.8, 0.15, duration: duration) }
    public static let spring = Animation.spring(response: 0.35, dampingFraction: 0.86)
}
