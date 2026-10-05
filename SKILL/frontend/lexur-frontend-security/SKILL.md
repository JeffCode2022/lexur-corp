---
name: lexur-frontend-security
description: Estandares de ciberseguridad defensiva y blindaje para el frontend (Web, Desktop y Mobile) en LEXUR. Activalo al configurar politicas CSP (Content Security Policy), sanitizacion de entradas (XSS / DOMPurify), almacenamiento seguro de credenciales (Keyring, Keystore, Keychain, EncryptedSharedPreferences), proteccion contra CSRF/Clickjacking, aislamiento de IPC en Electron/Tauri, o prevencion de filtracion de secretos y datos sensibles.
---

# LEXUR — Frontend Security Engineering

El frontend es la primera linea de contacto con el usuario y la superficie de ataque mas expuesta. En LEXUR, la seguridad es activa: cada input se desconfia, cada comunicacion se aísla y los secretos nunca tocan el cliente.

---

## 1. Reglas Inviolables de Seguridad

1. **CERO SECRETOS EN EL CLIENTE**:
   - NUNCA incluir API keys privadas, service accounts, certificados privados ni tokens maestros en el codigo de cliente (Web, App o Desktop).
   - En Next.js: Solo variables con prefijo `NEXT_PUBLIC_` llegan al navegador, y solo deben ser valores publicos (ej: URLs base de APIs publicas).
2. **AUDITORIA PREVIA DE DEPENDENCIAS**:
   - Obligatorio auditar con `vertexos-security-audit` o `npm audit` antes de instalar cualquier libreria nueva.
   - Rechazo inmediato ante CVEs criticos o paquetes con scripts `postinstall` no justificados.
3. **PROHIBIDO `dangerouslySetInnerHTML` SIN SANITIZACION**:
   - Todo HTML inyectado dinamicamente DEBE ser sanitizado estrictamente con `DOMPurify`.
4. **ALMACENAMIENTO SEGURO DE SESIONES**:
   - NUNCA guardar tokens JWT o contraseñas en `localStorage` o `sessionStorage` en aplicaciones web (vulnerables a robo por XSS).
   - Usar cookies `httpOnly`, `Secure`, `SameSite=Strict`.

---

## 2. Content Security Policy (CSP) Estricto

En aplicaciones Web y capas web de Electron/Tauri, implementar cabeceras HTTP de seguridad rigurosas en `next.config.js` o middleware:

```typescript
// middleware.ts o next.config.mjs
const cspHeader = `
  default-src 'self';
  script-src 'self' 'strict-dynamic';
  style-src 'self' 'unsafe-inline';
  img-src 'self' blob: data:;
  font-src 'self';
  object-src 'none';
  base-uri 'self';
  form-action 'self';
  frame-ancestors 'none';
  block-all-mixed-content;
  upgrade-insecure-requests;
`.replace(/\s{2,}/g, ' ').trim();

export const securityHeaders = [
  { key: 'Content-Security-Policy', value: cspHeader },
  { key: 'X-Frame-Options', value: 'DENY' },
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
  { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=(), browsing-topics=()' },
];
```

---

## 3. Almacenamiento Seguro por Plataforma

| Plataforma | Datos No Sensibles (Preferencias de UI) | Credenciales / Tokens de Acceso |
|---|---|---|
| **Web** | `localStorage` / IndexedDB | Cookies de sesion `httpOnly` seguras |
| **Electron** | `electron-store` (sin cifrar) | `keytar` (acceso a Keychain de macOS, Credential Manager de Windows, Secret Service de Linux) |
| **Tauri v2** | `tauri-plugin-store` | `tauri-plugin-stronghold` (boveda criptografica cifrada con Argon2 + XChaCha20-Poly1305) |
| **Flutter** | `shared_preferences` | `flutter_secure_storage` (Keychain en iOS, Keystore + EncryptedSharedPreferences en Android) |
| **Android Compose** | DataStore Preferences | Jetpack Security (`EncryptedSharedPreferences` / `MasterKeys`) |
| **iOS SwiftUI** | `@AppStorage` (UserDefaults) | Keychain Services (`SecItemAdd`, `SecItemCopyMatching`) |

---

## 4. Sanitizacion Anti-XSS (Patron de Inyeccion Segura)

```typescript
// src/lib/sanitize.ts
import DOMPurify from 'isomorphic-dompurify';

export function sanitizeHtml(dirty: string): string {
  return DOMPurify.sanitize(dirty, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a', 'p', 'code', 'pre', 'ul', 'ol', 'li'],
    ALLOWED_ATTR: ['href', 'target', 'rel'],
  });
}
```

---

## 5. Blindaje de Comunicacion IPC (Electron y Tauri)

1. **Electron**:
   - `nodeIntegration: false`, `contextIsolation: true`, `sandbox: true`.
   - Validar argumentos en los handlers del proceso principal: nunca confiar en lo que envia el renderer.
   - Prohibido ejecutar comandos de shell dinamicos con `child_process.exec(userString)`.
2. **Tauri v2**:
   - Usar el sistema de permisos granular de Tauri v2 (`capabilities/*.json`).
   - Otorgar unicamente acceso a las APIs nativas indispensables para la vista activa.

---

## 6. Lista de Comprobacion de Seguridad Antes de Publicar

- [ ] Escaneo de dependencias ejecutado: `npm audit` / `cargo audit` / `flutter pub outdated`.
- [ ] No hay archivos `.env` ni claves privadas commiteadas en el repositorio Git.
- [ ] El CSP bloquea la carga de scripts externos no autorizados.
- [ ] Todas las cookies sensibles tienen los atributos `Secure; HttpOnly; SameSite=Strict`.
- [ ] La app no es vulnerable a Clickjacking (`X-Frame-Options: DENY` o `frame-ancestors 'none'`).
- [ ] Los tokens de autenticacion en plataformas nativas se guardan en el Keychain/Keystore del sistema.
