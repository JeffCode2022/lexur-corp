---
name: vertexos-ai-integration
description: Integracion de motores de IA en proyectos VertexOS. Activalo cuando el usuario quiera integrar inteligencia artificial, comandos de voz, procesamiento de lenguaje natural, analisis automatico, o cuando mencione Gemini, Ollama, IA local, offline AI, reconocimiento de voz, o asistente inteligente en cualquier proyecto VertexOS.
---

# VertexOS — Integracion de IA

Ecosistema de IA dual: Gemini (online, alta capacidad) + Ollama (offline, privacidad total). Fallback automatico para garantizar disponibilidad.

---

## Arquitectura de IA Dual

```
VX AI Router
├── Online: Gemini API     → Alta capacidad, requiere internet
└── Offline: Ollama/Whisper → Privacidad total, sin internet

Regla: Datos sensibles (root, credenciales) → SIEMPRE usar Ollama local
```

---

## Gemini API (Online) — Flutter/Dart

```dart
// pubspec.yaml — AUDITAR CVEs antes: https://osv.dev/
// google_generative_ai: ^0.4.0

class VXGeminiService {
  static VXGeminiService? _instance;
  late final GenerativeModel _model;

  factory VXGeminiService() => _instance ??= VXGeminiService._init();

  VXGeminiService._init() {
    // API key desde variable de entorno — NUNCA hardcodeada
    final apiKey = const String.fromEnvironment('GEMINI_API_KEY');
    if (apiKey.isEmpty) throw Exception('GEMINI_API_KEY no configurada');
    _model = GenerativeModel(model: 'gemini-2.0-flash-exp', apiKey: apiKey);
  }

  Future<String> chat(String message) async {
    final response = await _model.generateContent([Content.text(message)]);
    return response.text ?? 'Sin respuesta';
  }

  Stream<String> chatStream(String message) async* {
    final stream = _model.generateContentStream([Content.text(message)]);
    await for (final chunk in stream) {
      yield chunk.text ?? '';
    }
  }
}
```

---

## Ollama (Offline / Privacidad) — Flutter/Dart

```bash
# Instalar en PC de desarrollo/servidor propio
# Modelos recomendados para espanol:
# ollama pull qwen2.5:3b    (2.3GB — excelente multilingue)
# ollama pull phi3:mini     (2.3GB — rapido, bueno para comandos)
```

```dart
class VXOllamaService {
  final String baseUrl;
  final String model;

  VXOllamaService({
    this.baseUrl = 'http://localhost:11434',
    this.model = 'qwen2.5:3b',
  });

  Future<bool> isAvailable() async {
    try {
      final response = await http.get(Uri.parse('$baseUrl/api/tags'))
          .timeout(const Duration(seconds: 2));
      return response.statusCode == 200;
    } catch (_) {
      return false;
    }
  }

  Future<String> chat(String message) async {
    final response = await http.post(
      Uri.parse('$baseUrl/api/generate'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'model': model, 'prompt': message, 'stream': false}),
    );
    if (response.statusCode == 200) {
      return (jsonDecode(response.body) as Map)['response'] as String;
    }
    throw Exception('Error Ollama: ${response.statusCode}');
  }
}
```

---

## Router con Fallback Automatico

```dart
class VXAiRouter {
  final VXGeminiService _gemini;
  final VXOllamaService _ollama;

  Future<String> chat(String message, {bool forceLocal = false}) async {
    if (forceLocal) return await _ollama.chat(message);

    try {
      return await _gemini.chat(message);
    } on Exception {
      if (await _ollama.isAvailable()) return await _ollama.chat(message);
      throw Exception('No hay conexion a IA disponible');
    }
  }
}
```

---

## Procesamiento de Comandos de Voz

```dart
class VoiceCommandProcessor {
  final VXAiRouter _ai;

  static const String _systemPrompt = '''
Eres el asistente de control del dispositivo Android en VertexOS.
Interpreta el comando y devuelve JSON:
{
  "action": "open_app|close_app|hardware_control|system_info|shell_command",
  "target": "objetivo",
  "params": {}
}
Si no es claro o es peligroso: {"action": "clarify", "message": "..."}
NO ejecutes comandos destructivos sin confirmacion explicita.
''';

  Future<VXCommand?> processCommand(String voiceInput) async {
    try {
      // Comandos sensibles siempre offline
      final isSensitive = voiceInput.contains('root') || voiceInput.contains('sistema');
      final response = await _ai.chat(
        '$_systemPrompt\n\nComando: $voiceInput',
        forceLocal: isSensitive,
      );
      return VXCommand.fromJson(jsonDecode(response));
    } catch (e) {
      return null;
    }
  }
}
```

---

## Reconocimiento de Voz

```dart
// speech_to_text — AUDITAR CVEs antes de instalar
class VXSpeechRecognizer {
  final SpeechToText _speech = SpeechToText();

  Future<bool> initialize() => _speech.initialize();

  Future<void> startListening({
    required void Function(String text) onResult,
    required void Function(String error) onError,
    String localeId = 'es_ES',
  }) async {
    await _speech.listen(
      onResult: (result) {
        if (result.finalResult) onResult(result.recognizedWords);
      },
      localeId: localeId,
    );
  }

  Future<void> stopListening() => _speech.stop();
}
```

---

## Seguridad en IA

1. API Keys: NUNCA en codigo — usar String.fromEnvironment o flutter_secure_storage
2. Datos sensibles: Siempre Ollama local — NUNCA enviar comandos root a Gemini
3. Rate limiting: Debounce de 500ms en voz
4. Prompt injection: Sanitizar inputs de usuario antes de enviar a IA
5. Logging: NUNCA logear mensajes completos del usuario

---

## Referencias

- Gemini SDK: https://ai.google.dev/gemini-api/docs
- Ollama API: https://github.com/ollama/ollama/blob/main/docs/api.md
- Vosk offline: https://alphacephei.com/vosk/
- speech_to_text: https://pub.dev/packages/speech_to_text
