---
name: vertexos-mobile-voice
description: Implementación de comandos de voz para la app móvil VertexOS Mobile. Actívalo cuando el usuario trabaje en la app móvil Android y quiera implementar el sistema de comandos de voz, reconocimiento de voz en español, procesamiento de intención de comandos, o la integración de voz con el sistema de control del dispositivo.
---

# VertexOS Mobile — Sistema de Comandos de Voz

Implementación del sistema de control por voz del dispositivo Android. Integra reconocimiento de voz → procesamiento de IA → ejecución de acción de sistema.

---

## 🎤 Flujo de Comando de Voz

```
Usuario habla
    ↓
VXSpeechRecognizer (escucha)
    ↓
Texto transcrito
    ↓
VXAiRouter (procesa intención)
    ↓
VXCommand (acción parseada)
    ↓
VXCommandExecutor (ejecuta según nivel)
    ↓
Respuesta de voz (TTS)
```

---

## 📱 Comandos de Voz Soportados

### Nivel 0 — Sin privilegios especiales

```
"Abre [nombre de app]"          → launchApp(packageName)
"Cierra [nombre de app]"        → closeApp()
"Sube el volumen"               → volumeControl(+)
"Baja el volumen"               → volumeControl(-)
"Prende la linterna"            → flashlight(on)
"Apaga la linterna"             → flashlight(off)
"¿Qué hora es?"                 → systemInfo(time)
"¿Cuánta batería tengo?"        → systemInfo(battery)
```

### Nivel 1 — Accessibility Service

```
"Vuelve atrás"                  → performGlobalAction(BACK)
"Ve al inicio"                  → performGlobalAction(HOME)
"Muéstrame las notificaciones"  → performGlobalAction(NOTIFICATIONS)
"Captura de pantalla"           → performGlobalAction(SCREENSHOT)
```

### Nivel 2 — ADB over WiFi

```
"Lista las apps instaladas"     → adb shell pm list packages
"Instala [app]"                 → adb install
"Ejecuta comando [cmd]"         → adb shell [cmd] (biometría primero)
```

### Nivel 3 — Root (siempre con biometría)

```
"Dame info del sistema"         → cat /proc/cpuinfo
"Reinicia [servicio]"           → root shell (biometría obligatoria)
```

---

## 🔊 Text-to-Speech (Respuestas de voz)

```dart
// lib/features/voice/data/vx_tts_service.dart
class VXTtsService {
  final FlutterTts _tts = FlutterTts();

  Future<void> initialize() async {
    await _tts.setLanguage('es-ES');
    await _tts.setSpeechRate(0.9);
    await _tts.setVolume(1.0);
    await _tts.setPitch(1.0);
  }

  Future<void> speak(String text) => _tts.speak(text);
  Future<void> stop() => _tts.stop();
}
```

---

## 🧠 Procesamiento de Comandos

```dart
// Comandos predefinidos (rápidos, sin IA)
class VXCommandParser {
  static VXCommand? parseQuick(String input) {
    final lower = input.toLowerCase().trim();
    
    if (lower.startsWith('abre ')) {
      final appName = lower.replaceFirst('abre ', '');
      return VXCommand(action: 'open_app', target: appName);
    }
    
    if (lower.contains('batería') || lower.contains('bateria')) {
      return VXCommand(action: 'system_info', target: 'battery');
    }
    
    if (lower.contains('linterna')) {
      final state = lower.contains('prende') || lower.contains('enciende');
      return VXCommand(action: 'flashlight', target: state ? 'on' : 'off');
    }
    
    // Si no es comando predefinido → enviar a IA para interpretar
    return null;
  }
}
```

---

## 🎙️ Widget de Activación de Voz

```dart
// Botón de micrófono en la UI
class VXVoiceButton extends StatefulWidget {
  final VoidCallback onCommandReceived;
  
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onLongPressStart: (_) => _startListening(),
      onLongPressEnd: (_) => _stopListening(),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        width: 72,
        height: 72,
        decoration: BoxDecoration(
          color: _isListening ? VXTokens.error : VXTokens.accent,
          shape: BoxShape.circle,
        ),
        child: Icon(
          _isListening ? Icons.mic : Icons.mic_none,
          color: Colors.white,
          size: 28,
        ),
      ),
    );
  }
}
```

---

## 📋 Referencias

- speech_to_text: https://pub.dev/packages/speech_to_text
- flutter_tts: https://pub.dev/packages/flutter_tts
- Vosk offline: https://github.com/alphacep/vosk-flutter
