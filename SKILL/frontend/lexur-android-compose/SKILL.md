---
name: lexur-android-compose
description: Estandares de interfaz Android nativa con Jetpack Compose y Kotlin para el ecosistema LEXUR. Activalo al programar pantallas, componentes, temas (Theme.kt), ViewModels, navegacion (Navigation Compose) o integracion de hardware en Android. Bloquea estrictamente Material You (Dynamic Color) para mantener la identidad de marca, prohibe gradientes y blur (RenderEffect), y asegura soporte de Edge-to-Edge nativo y los 4 estados UI.
---

# LEXUR — Android Native UI (Jetpack Compose)

Desarrollo nativo Android con Kotlin y Jetpack Compose orientado a rendimiento maximo, arquitectura limpia y fidelidad estricta al lenguaje visual LEXUR "Precision Dark".

---

## 1. Reglas Criticas en Android / Compose

1. **PROHIBIDO Dynamic Color (Material You)**:
   - Los colores dinamicos extraidos del fondo de pantalla del usuario destruyen la identidad corporativa.
   - En `Theme.kt`, `dynamicColor` DEBE ser `false` siempre.
2. **PROHIBIDO `Brush.linearGradient` o cualquier gradiente**:
   - Superficies solidas con colores de tokens (`LxDarkColors` / `LxLightColors`).
3. **PROHIBIDO `RenderEffect.createBlurEffect` o `Modifier.blur`**:
   - Prohibido desenfocar el fondo para efectos de vidrio.
4. **Soporte Edge-to-Edge obligatorio**:
   - Todo layout utiliza `enableEdgeToEdge()` de `androidx.activity` y consume `WindowInsets` seguros (`safeDrawingPadding` o `statusBarsPadding`).

---

## 2. Configuracion del Tema LEXUR (`LexurTheme.kt`)

Usa los tokens generados en `LexurTokens.kt` (`LxColors`, `LxSpace`, `LxRadius`, `LxType`, `LxMotion`):

```kotlin
// app/src/main/java/com/lexur/design/theme/LexurTheme.kt
package com.lexur.design.theme

import android.app.Activity
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Typography
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.ReadOnlyComposable
import androidx.compose.runtime.SideEffect
import androidx.compose.runtime.staticCompositionLocalOf
import androidx.compose.ui.graphics.toArgb
import androidx.compose.ui.platform.LocalView
import androidx.core.view.WindowCompat
import com.lexur.design.tokens.*

val LocalLexurColors = staticCompositionLocalOf { LxDarkColors }

object LexurTheme {
    val colors: LxColors
        @Composable
        @ReadOnlyComposable
        get() = LocalLexurColors.current

    val space: LxSpace = LxSpace
    val radius: LxRadius = LxRadius
    val type: LxType = LxType
}

@Composable
fun LexurTheme(
    darkTheme: Boolean = isSystemInDarkTheme(), // O controlado por preferencia del usuario
    content: @Composable () -> Unit
) {
    val colors = if (darkTheme) LxDarkColors else LxLightColors

    val view = LocalView.current
    if (!view.isInEditMode) {
        SideEffect {
            val window = (view.context as Activity).window
            window.statusBarColor = colors.bgCanvas.toArgb()
            window.navigationBarColor = colors.bgCanvas.toArgb()
            val controller = WindowCompat.getInsetsController(window, view)
            controller.isAppearanceLightStatusBars = !darkTheme
            controller.isAppearanceLightNavigationBars = !darkTheme
        }
    }

    CompositionLocalProvider(
        LocalLexurColors provides colors
    ) {
        // Envolvemos en MaterialTheme base para interoperabilidad pero sin DynamicColor
        MaterialTheme(
            content = content
        )
    }
}
```

---

## 3. Componente de Referencia: Boton Solido Compose

```kotlin
// app/src/main/java/com/lexur/design/components/LxButton.kt
package com.lexur.design.components

import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.tween
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.interaction.collectIsPressedAsState
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import com.lexur.design.theme.LexurTheme
import com.lexur.design.tokens.LxMotion

enum class LxButtonVariant { Primary, Secondary, Ghost, Danger }
enum class LxButtonSize { Sm, Md, Lg }

@Composable
fun LxButton(
    text: String,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    variant: LxButtonVariant = LxButtonVariant.Primary,
    size: LxButtonSize = LxButtonSize.Md,
    enabled: Boolean = true,
    loading: Boolean = false,
    leadingIcon: (@Composable () -> Unit)? = null
) {
    val colors = LexurTheme.colors
    val interactionSource = remember { MutableInteractionSource() }
    val isPressed by interactionSource.collectIsPressedAsState()

    // Microinteraccion de escala fisica sobria (0.98 al presionar)
    val scale by animateFloatAsState(
        targetValue = if (isPressed && enabled && !loading) 0.98f else 1f,
        animationSpec = tween(LxMotion.InstantMs),
        label = "button_scale"
    )

    val (bgColor, contentColor, border) = when (variant) {
        LxButtonVariant.Primary -> Triple(colors.bgInverse, colors.textInverse, null)
        LxButtonVariant.Secondary -> Triple(colors.bgSurface2, colors.textPrimary, BorderStroke(1.dp, colors.borderDefault))
        LxButtonVariant.Ghost -> Triple(Color.Transparent, colors.textPrimary, null)
        LxButtonVariant.Danger -> Triple(colors.statusDanger, colors.textInverse, null)
    }

    val height = when (size) {
        LxButtonSize.Sm -> LexurTheme.space.s32
        LxButtonSize.Md -> LexurTheme.space.s40
        LxButtonSize.Lg -> LexurTheme.space.s48
    }

    val radius = when (size) {
        LxButtonSize.Sm -> LexurTheme.radius.sm
        else -> LexurTheme.radius.md
    }

    Surface(
        onClick = onClick,
        modifier = modifier
            .height(height)
            .scale(scale),
        enabled = enabled && !loading,
        shape = RoundedCornerShape(radius),
        color = if (!enabled) colors.bgSurface2 else bgColor,
        contentColor = if (!enabled) colors.textDisabled else contentColor,
        border = if (enabled) border else null,
        interactionSource = interactionSource
    ) {
        Row(
            modifier = Modifier.padding(horizontal = 16.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.Center
        ) {
            if (loading) {
                CircularProgressIndicator(
                    modifier = Modifier.size(16.dp),
                    strokeWidth = 2.dp,
                    color = contentColor
                )
            } else {
                if (leadingIcon != null) {
                    leadingIcon()
                    Spacer(modifier = Modifier.width(LexurTheme.space.s8))
                }
                Text(
                    text = text,
                    style = LexurTheme.type.label,
                    color = if (!enabled) colors.textDisabled else contentColor
                )
            }
        }
    }
}
```

---

## 4. Los 4 Estados UI Obligatorios en Compose

Mapeo formal con `sealed interface UiState<out T>`:

```kotlin
sealed interface TelemetryUiState {
    data object Loading : TelemetryUiState
    data class Error(val message: String) : TelemetryUiState
    data object Empty : TelemetryUiState
    data class Success(val data: TelemetryReport) : TelemetryUiState
}

@Composable
fun TelemetryScreen(
    state: TelemetryUiState,
    onRetry: () -> Unit,
    onStartSensors: () -> Unit
) {
    when (state) {
        is TelemetryUiState.Loading -> LxLoadingView(message = "Recuperando telemetría...")
        is TelemetryUiState.Error -> LxErrorView(
            message = state.message,
            onRetry = onRetry
        )
        is TelemetryUiState.Empty -> LxEmptyView(
            title = "Sin métricas registradas",
            description = "Conecta el hardware para iniciar la recopilación de datos.",
            actionLabel = "Iniciar conexión",
            onAction = onStartSensors
        )
        is TelemetryUiState.Success -> TelemetryContent(report = state.data)
    }
}
```

---

## 5. Pruebas y Verificacion Android

1. Validar que ninguna actividad use `dynamicColor = true`.
2. Ejecutar escaner de estilos prohibidos:
   `node <lexur-ui-review>/scripts/scan-forbidden-styles.mjs app/src/`
3. Probar en Compose Layout Inspector con tema oscuro y claro.
4. Validar navegacion por accesibilidad con TalkBack activo.
