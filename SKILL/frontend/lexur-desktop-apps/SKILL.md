---
name: lexur-desktop-apps
description: Estandares de desarrollo para aplicaciones desktop profesionales LEXUR con Electron o Tauri (v2). Activalo cuando se cree o modifique una app de escritorio para Windows, macOS o Linux; al configurar ventanas nativas, IPC seguro (contextBridge / IPC commands), almacenamiento local (SQLite/Store), bandeja del sistema (tray), atajos de teclado globales (Cmd/Ctrl+K), auto-updater, o al decidir entre Electron y Tauri. PROHIBE terminantemente efectos translucidos como Mica, Acrylic o Vibrancy.
---

# LEXUR — Desktop Apps (Electron & Tauri v2)

Apps de escritorio de alto rendimiento con estetica minimalista, solida e industrial inspirada en Tesla, X y herramientas profesionales como Linear y Slack.

## 1. Criterio de seleccion: Electron vs Tauri v2

| Criterio | Tauri v2 (Recomendado por defecto) | Electron |
|---|---|---|
| **Tamano del instalador** | Ultraligero (< 15 MB) | Pesado (> 80 MB) |
| **Consumo de memoria** | Bajo (~30-50 MB RAM base) | Moderado-alto (~150-250 MB RAM base) |
| **Backend / Core** | Rust (seguridad de memoria, velocidad nativa) | Node.js (ecosistema npm existente) |
| **Uso ideal** | Dashboards, utilidades de sistema, herramientas de telemetria, apps de alta velocidad | Apps que requieren librerias npm con bindings C++ nativos muy especificos sin equivalente en Rust |

---

## 2. Regla Inviolable: Prohibicion de Glass / Mica / Acrylic / Vibrancy

En coherencia con el lenguaje de diseno LEXUR:
- **NO habilitar `vibrancy`** en macOS (`NSVisualEffectView`).
- **NO habilitar `backgroundMaterial: 'mica' | 'acrylic' | 'tabbed'`** en Windows.
- **NO habilitar ventanas transparentes** para simular vidrio o efecto borroso de fondo.
- **Las ventanas deben tener fondo solido**:
  - En modo Dark: `#000000` (`bg.canvas`) o `#0A0A0A` (`bg.surface1`).
  - En modo Light: `#FFFFFF` (`bg.canvas`).
- Bordes de ventana definidos por un hairline fino (`#2A2A2A` en dark / `#E0E0E0` en light) o la decoracion solida nativa del sistema.

---

## 3. Electron — Arquitectura y Seguridad Inquebrantable

### 3.1. Configuracion segura de BrowserWindow

```typescript
// electron/main.ts
import { app, BrowserWindow, shell } from 'electron';
import path from 'path';

function createWindow(): BrowserWindow {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    minWidth: 960,
    minHeight: 600,
    backgroundColor: '#000000', // Solido: NUNCA transparente ni mica
    titleBarStyle: 'hiddenInset', // macOS: semaforos nativos integrados sin blur
    autoHideMenuBar: true,       // Windows/Linux: barra limpia
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,       // OBLIGATORIO: aísla el contexto de la web
      nodeIntegration: false,      // OBLIGATORIO: nunca exponer Node directamente a la UI
      sandbox: true,               // OBLIGATORIO: habilita sandbox de Chromium
      webSecurity: true,           // OBLIGATORIO: nunca desactivar CORS ni politicas web
      allowRunningInsecureContent: false,
    },
  });

  // Prevenir navegacion no autorizada y abrir links en navegador externo del sistema
  win.webContents.setWindowOpenHandler(({ url }) => {
    if (url.startsWith('https:')) shell.openExternal(url);
    return { action: 'deny' };
  });

  return win;
}
```

### 3.2. Puente IPC seguro (Preload y ContextBridge)

Nunca expongas `ipcRenderer` crudo al renderizador. Declara interfaces tipadas:

```typescript
// electron/preload.ts
import { contextBridge, ipcRenderer } from 'electron';

export interface LexurDesktopAPI {
  ping: () => Promise<string>;
  getAppVersion: () => Promise<string>;
  openSystemDialog: (options: DialogOptions) => Promise<string[] | null>;
  onThemeChanged: (callback: (isDark: boolean) => void) => () => void;
}

const api: LexurDesktopAPI = {
  ping: () => ipcRenderer.invoke('lexur:ping'),
  getAppVersion: () => ipcRenderer.invoke('lexur:get-version'),
  openSystemDialog: (opts) => ipcRenderer.invoke('lexur:dialog:open', opts),
  onThemeChanged: (callback) => {
    const handler = (_: any, isDark: boolean) => callback(isDark);
    ipcRenderer.on('lexur:theme-changed', handler);
    return () => ipcRenderer.removeListener('lexur:theme-changed', handler);
  },
};

contextBridge.exposeInMainWorld('lexurBridge', api);
```

---

## 4. Tauri v2 — Estandares y Rendimiento

### 4.1. Configuracion de ventana solida (`tauri.conf.json`)

```json
{
  "$schema": "https://raw.githubusercontent.com/tauri-apps/tauri/dev/crates/tauri-cli/schemas/tauri.conf.json",
  "productName": "lexur-desktop",
  "app": {
    "windows": [
      {
        "title": "LEXUR Workstation",
        "width": 1280,
        "height": 840,
        "minWidth": 960,
        "minHeight": 600,
        "resizable": true,
        "fullscreen": false,
        "transparent": false,
        "theme": "Dark",
        "decorations": true
      }
    ],
    "security": {
      "csp": "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: asset:;"
    }
  }
}
```
*Nota: NUNCA agregar el bloque `"windowEffects"` en `tauri.conf.json`.*

### 4.2. Comandos seguros en Rust

```rust
// src-tauri/src/main.rs
use tauri::Manager;

#[tauri::command]
fn get_system_telemetry() -> Result<TelemetryData, String> {
    // Lectura protegida de hardware o datos locales sin shell injection
    Ok(TelemetryData {
        cpu_usage: 14.2,
        memory_mb: 240,
        status: "optimal".into(),
    })
}

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .invoke_handler(tauri::generate_handler![get_system_telemetry])
        .run(tauri::generate_context!())
        .expect("error running lexur desktop application");
}
```

---

## 5. Experiencia de Usuario Desktop (Patrones Clave)

1. **Command Palette Global (`Cmd/Ctrl + K`)**:
   - Acceso instantaneo a cualquier accion o navegacion sin despegar las manos del teclado.
2. **Atajos de teclado universales**:
   - `Cmd/Ctrl + ,`: Preferencias / Configuracion.
   - `Cmd/Ctrl + R`: Recarga deshabilitada en produccion.
   - `Cmd/Ctrl + Shift + L`: Alternar tema (Dark / Light).
3. **Manejo de estado offline y SQLite local**:
   - Electron: `better-sqlite3` con sentencias preparadas.
   - Tauri: `tauri-plugin-sql` o `rusqlite` en Rust.
   - Cero spinners infinitos: datos locales cargan en < 50ms.
4. **Bandeja del sistema (System Tray)**:
   - Icono monocromatico de 16x16 / 22x22 en blanco puro o negro solido segun el OS.
   - Menu contextual simple con acciones directas ("Abrir", "Estado", "Salir").

---

## 6. Verificacion y Auditoria

- [ ] Escaneo de estilos prohibidos ejecutado: `node <lexur-ui-review>/scripts/scan-forbidden-styles.mjs <src>`
- [ ] Sin uso de `nodeIntegration: true` o `contextIsolation: false` en Electron.
- [ ] CSP activo y estricto configurado en la ventana.
- [ ] No existen dependencias con scripts maliciosos de `postinstall`.
- [ ] El ejecutable compila en binario firmado (Codesign / Notarization en macOS, Authenticode en Windows).
