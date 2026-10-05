---
name: vertexos-kotlin-android
description: Guia de implementacion Kotlin para Android en proyectos VertexOS con acceso privilegiado al sistema. Activalo cuando el usuario quiera implementar Accessibility Service, control root, ADB over WiFi, biometria, APIs del sistema Android, control de hardware (WiFi, Bluetooth, camara, sensores), o cualquier funcionalidad que requiera acceso de bajo nivel al sistema Android.
---

# VertexOS — Kotlin Android

Nucleo de sistema de la app VertexOS Mobile. Arquitectura de privilegios en capas con enfoque en seguridad.

---

## Arquitectura de Privilegios en Capas

```
Nivel 3: Root (Magisk/KernelSU)  — Kernel, particiones, sistema completo
Nivel 2: ADB over WiFi            — Debug bridge, shell, install APKs
Nivel 1: Accessibility Service    — Navegacion UI, automatizacion de apps
Nivel 0: Permisos normales        — Camara, microfono, ubicacion, sensores
```

Principio: Usar siempre el nivel minimo necesario. Acciones Nivel 2+ requieren autenticacion biometrica.

---

## Accessibility Service

```kotlin
// AndroidManifest.xml
// <service android:name=".accessibility.VXAccessibilityService"
//     android:exported="true"
//     android:permission="android.permission.BIND_ACCESSIBILITY_SERVICE">
//   <intent-filter>
//     <action android:name="android.accessibilityservice.AccessibilityService" />
//   </intent-filter>
//   <meta-data android:name="android.accessibilityservice"
//     android:resource="@xml/accessibility_service_config" />
// </service>

class VXAccessibilityService : AccessibilityService() {
    override fun onAccessibilityEvent(event: AccessibilityEvent?) {
        event ?: return
        // Procesar eventos del sistema
    }

    fun launchApp(packageName: String) {
        val intent = packageManager.getLaunchIntentForPackage(packageName)
        intent?.let {
            it.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
            startActivity(it)
        }
    }

    fun performBack() = performGlobalAction(GLOBAL_ACTION_BACK)
    fun openNotifications() = performGlobalAction(GLOBAL_ACTION_NOTIFICATIONS)
    override fun onInterrupt() {}
}
```

---

## Root con Libsu

```kotlin
// build.gradle.kts — AUDITAR CVEs antes de agregar
// implementation("com.github.topjohnwu.libsu:core:5.2.2")

object VXRootManager {
    fun hasRootAccess(): Boolean = Shell.isAppGrantedRoot() == true

    // SIEMPRE verificar biometria antes de ejecutar comandos root
    fun executeRootCommand(
        command: String,
        onSuccess: (List<String>) -> Unit,
        onError: (String) -> Unit
    ) {
        Shell.cmd(command).submit { result ->
            if (result.isSuccess) onSuccess(result.out)
            else onError(result.err.joinToString())
        }
    }
}
```

---

## ADB over WiFi

```kotlin
object VXAdbManager {
    fun isAdbWifiEnabled(context: Context): Boolean {
        val adbEnabled = Settings.Global.getInt(
            context.contentResolver, Settings.Global.ADB_ENABLED, 0
        )
        return adbEnabled == 1
    }

    // Requiere root
    fun enableAdbOverTcp(port: Int = 5555) {
        VXRootManager.executeRootCommand(
            command = "setprop service.adb.tcp.port $port && stop adbd && start adbd",
            onSuccess = { /* ADB TCP habilitado */ },
            onError = { error -> /* Manejar error */ }
        )
    }
}
```

---

## Autenticacion Biometrica

```kotlin
class VXBiometricAuth(private val activity: FragmentActivity) {
    fun authenticate(
        title: String = "VertexOS",
        subtitle: String = "Confirma tu identidad",
        onSuccess: () -> Unit,
        onError: (String) -> Unit,
        onFail: () -> Unit,
    ) {
        val biometricPrompt = BiometricPrompt(activity,
            object : BiometricPrompt.AuthenticationCallback() {
                override fun onAuthenticationSucceeded(result: BiometricPrompt.AuthenticationResult) = onSuccess()
                override fun onAuthenticationError(errorCode: Int, errString: CharSequence) = onError(errString.toString())
                override fun onAuthenticationFailed() = onFail()
            }
        )
        val promptInfo = BiometricPrompt.PromptInfo.Builder()
            .setTitle(title)
            .setSubtitle(subtitle)
            .setNegativeButtonText("Cancelar")
            .build()
        biometricPrompt.authenticate(promptInfo)
    }
}
```

---

## Method Channel (Flutter <-> Kotlin)

```kotlin
class MainActivity : FlutterActivity() {
    private val CHANNEL = "com.vertexos.mobile/system"

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL)
            .setMethodCallHandler { call, result ->
                when (call.method) {
                    "hasRoot" -> result.success(VXRootManager.hasRootAccess())
                    "executeCommand" -> {
                        val cmd = call.argument<String>("command") ?: ""
                        VXRootManager.executeRootCommand(
                            command = cmd,
                            onSuccess = { output -> result.success(output.joinToString("\n")) },
                            onError = { error -> result.error("ROOT_ERROR", error, null) }
                        )
                    }
                    "enableAdbWifi" -> {
                        VXAdbManager.enableAdbOverTcp()
                        result.success(true)
                    }
                    else -> result.notImplemented()
                }
            }
    }
}
```

---

## Permisos AndroidManifest.xml

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<uses-permission android:name="android.permission.USE_BIOMETRIC" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.WRITE_SECURE_SETTINGS" />
```

---

## Referencias

- libsu (Root): https://github.com/topjohnwu/libsu
- Android Accessibility: https://developer.android.com/guide/topics/ui/accessibility/service
- BiometricPrompt: https://developer.android.com/training/sign-in/biometric-auth
- Shizuku (alternativa sin root): https://shizuku.rikka.app/
