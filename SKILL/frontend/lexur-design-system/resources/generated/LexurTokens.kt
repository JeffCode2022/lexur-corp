// AUTO-GENERADO por lexur-design-system/scripts/generate-tokens.mjs (v1.0.0). NO EDITAR A MANO.
package com.lexur.design.tokens

import androidx.compose.animation.core.CubicBezierEasing
import androidx.compose.runtime.Immutable
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.em
import androidx.compose.ui.unit.sp

@Immutable
data class LxColors(
    val bgCanvas: Color,
    val bgSurface1: Color,
    val bgSurface2: Color,
    val bgSurface3: Color,
    val bgInverse: Color,
    val borderSubtle: Color,
    val borderDefault: Color,
    val borderStrong: Color,
    val borderControl: Color,
    val textPrimary: Color,
    val textSecondary: Color,
    val textTertiary: Color,
    val textDisabled: Color,
    val textInverse: Color,
    val textOnAccent: Color,
    val accentDefault: Color,
    val accentHover: Color,
    val accentPressed: Color,
    val accentSubtle: Color,
    val accentText: Color,
    val statusSuccess: Color,
    val statusSuccessSubtle: Color,
    val statusWarning: Color,
    val statusWarningSubtle: Color,
    val statusDanger: Color,
    val statusDangerSubtle: Color,
    val focusRing: Color,
    val overlayScrim: Color,
)

val LxDarkColors = LxColors(
    bgCanvas = Color(0xFF000000),
    bgSurface1 = Color(0xFF0A0A0A),
    bgSurface2 = Color(0xFF141414),
    bgSurface3 = Color(0xFF1F1F1F),
    bgInverse = Color(0xFFFAFAFA),
    borderSubtle = Color(0xFF1A1A1A),
    borderDefault = Color(0xFF2A2A2A),
    borderStrong = Color(0xFF404040),
    borderControl = Color(0xFF5E5E5E),
    textPrimary = Color(0xFFF5F5F5),
    textSecondary = Color(0xFFA3A3A3),
    textTertiary = Color(0xFF808080),
    textDisabled = Color(0xFF4D4D4D),
    textInverse = Color(0xFF0A0A0A),
    textOnAccent = Color(0xFFFFFFFF),
    accentDefault = Color(0xFF2E6BFF),
    accentHover = Color(0xFF4A80FF),
    accentPressed = Color(0xFF2457D6),
    accentSubtle = Color(0xFF0B1A3D),
    accentText = Color(0xFF6B9BFF),
    statusSuccess = Color(0xFF32D74B),
    statusSuccessSubtle = Color(0xFF0B2611),
    statusWarning = Color(0xFFFFD60A),
    statusWarningSubtle = Color(0xFF2B2402),
    statusDanger = Color(0xFFFF453A),
    statusDangerSubtle = Color(0xFF2E0E0C),
    focusRing = Color(0xFF2E6BFF),
    overlayScrim = Color(0xB8000000),
)

val LxLightColors = LxColors(
    bgCanvas = Color(0xFFFFFFFF),
    bgSurface1 = Color(0xFFFAFAFA),
    bgSurface2 = Color(0xFFF2F2F2),
    bgSurface3 = Color(0xFFE8E8E8),
    bgInverse = Color(0xFF0A0A0A),
    borderSubtle = Color(0xFFEFEFEF),
    borderDefault = Color(0xFFE0E0E0),
    borderStrong = Color(0xFFC2C2C2),
    borderControl = Color(0xFF8F8F8F),
    textPrimary = Color(0xFF0A0A0A),
    textSecondary = Color(0xFF525252),
    textTertiary = Color(0xFF6E6E6E),
    textDisabled = Color(0xFFB3B3B3),
    textInverse = Color(0xFFFAFAFA),
    textOnAccent = Color(0xFFFFFFFF),
    accentDefault = Color(0xFF0A5CFF),
    accentHover = Color(0xFF0050E6),
    accentPressed = Color(0xFF0042BF),
    accentSubtle = Color(0xFFEAF0FF),
    accentText = Color(0xFF0A5CFF),
    statusSuccess = Color(0xFF1E7E34),
    statusSuccessSubtle = Color(0xFFE8F5EB),
    statusWarning = Color(0xFFA15C00),
    statusWarningSubtle = Color(0xFFFFF4E0),
    statusDanger = Color(0xFFD70015),
    statusDangerSubtle = Color(0xFFFFEBEC),
    focusRing = Color(0xFF0A5CFF),
    overlayScrim = Color(0x7A000000),
)

object LxSpace {
    val s0 = 0.dp
    val s2 = 2.dp
    val s4 = 4.dp
    val s8 = 8.dp
    val s12 = 12.dp
    val s16 = 16.dp
    val s20 = 20.dp
    val s24 = 24.dp
    val s32 = 32.dp
    val s40 = 40.dp
    val s48 = 48.dp
    val s64 = 64.dp
    val s80 = 80.dp
    val s96 = 96.dp
    val s128 = 128.dp
}

object LxRadius {
    val none = 0.dp
    val xs = 4.dp
    val sm = 6.dp
    val md = 10.dp
    val lg = 14.dp
    val xl = 20.dp
    val full = 999.dp
}

object LxControl {
    val sm = 32.dp
    val md = 40.dp
    val lg = 48.dp
    val touchMinIos = 44.dp
    val touchMinAndroid = 48.dp
}

/** fontFamily se aplica en LexurTheme (Geist desde res/font). */
object LxType {
    val displayXl = TextStyle(fontSize = 72.sp, lineHeight = 76.sp, letterSpacing = (-0.04).em, fontWeight = FontWeight.W600)
    val display = TextStyle(fontSize = 56.sp, lineHeight = 60.sp, letterSpacing = (-0.03).em, fontWeight = FontWeight.W600)
    val h1 = TextStyle(fontSize = 40.sp, lineHeight = 44.sp, letterSpacing = (-0.025).em, fontWeight = FontWeight.W600)
    val h2 = TextStyle(fontSize = 32.sp, lineHeight = 38.sp, letterSpacing = (-0.02).em, fontWeight = FontWeight.W600)
    val h3 = TextStyle(fontSize = 24.sp, lineHeight = 30.sp, letterSpacing = (-0.015).em, fontWeight = FontWeight.W600)
    val h4 = TextStyle(fontSize = 20.sp, lineHeight = 26.sp, letterSpacing = (-0.01).em, fontWeight = FontWeight.W600)
    val bodyLg = TextStyle(fontSize = 17.sp, lineHeight = 26.sp, letterSpacing = (0).em, fontWeight = FontWeight.W400)
    val body = TextStyle(fontSize = 15.sp, lineHeight = 22.sp, letterSpacing = (0).em, fontWeight = FontWeight.W400)
    val bodySm = TextStyle(fontSize = 13.sp, lineHeight = 18.sp, letterSpacing = (0).em, fontWeight = FontWeight.W400)
    val label = TextStyle(fontSize = 14.sp, lineHeight = 20.sp, letterSpacing = (0).em, fontWeight = FontWeight.W500)
    val caption = TextStyle(fontSize = 12.sp, lineHeight = 16.sp, letterSpacing = (0.01).em, fontWeight = FontWeight.W500)
    val overline = TextStyle(fontSize = 11.sp, lineHeight = 14.sp, letterSpacing = (0.08).em, fontWeight = FontWeight.W600)
    val metric = TextStyle(fontSize = 48.sp, lineHeight = 52.sp, letterSpacing = (-0.02).em, fontWeight = FontWeight.W500)
}

object LxMotion {
    const val InstantMs = 80
    const val FastMs = 150
    const val BaseMs = 220
    const val SlowMs = 320
    const val DeliberateMs = 480
    val Standard = CubicBezierEasing(0.2f, 0f, 0f, 1f)
    val Enter = CubicBezierEasing(0.05f, 0.7f, 0.1f, 1f)
    val Exit = CubicBezierEasing(0.3f, 0f, 0.8f, 0.15f)
    const val SpringDampingRatio = 0.86f
}
