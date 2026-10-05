---
name: vertexos-desktop-electron
description: Desarrollo del Gestor de Proyectos VertexOS Desktop usando Electron + Next.js. Actívalo cuando el usuario trabaje en la aplicación desktop del gestor de proyectos VertexOS, quiera crear ventanas, módulos del gestor, integración con el sistema de archivos, base de datos local SQLite, o la interfaz web del gestor.
---

# VertexOS Desktop — Electron + Next.js

Gestor central de proyectos VertexOS. App desktop multiplataforma con web UI moderna.

---

## 🏗️ Stack Tecnológico

```
Electron (shell)          → Ventana nativa, IPC, acceso al sistema
Next.js 14 (App Router)   → UI web moderna, SSR/CSR
Tailwind CSS              → Estilos con tokens VertexOS
SQLite (better-sqlite3)   → Base de datos local, sin servidor
Fastify                   → API local dentro de Electron
PocketBase                → Sync opcional a servidor propio
```

---

## 📂 Estructura del Proyecto

```
vertexos-desktop/
├── electron/
│   ├── main.ts           # Proceso principal Electron
│   ├── preload.ts        # Bridge seguro UI ↔ Sistema
│   ├── ipc/              # Handlers de IPC por módulo
│   └── database/         # Acceso SQLite
├── src/
│   ├── app/              # Next.js App Router
│   │   ├── dashboard/    # Módulo Dashboard
│   │   ├── projects/     # Módulo Proyectos
│   │   ├── bugs/         # Módulo Bug Tracker
│   │   ├── logs/         # Módulo Logs
│   │   ├── timeline/     # Módulo Timeline
│   │   ├── security/     # Módulo Seguridad
│   │   └── ai/           # Módulo Agente IA
│   ├── components/       # Componentes UI reutilizables
│   └── lib/              # Utilidades y servicios
├── package.json
└── electron-builder.yml  # Configuración de build
```

---

## ⚡ IPC Seguro (Electron ↔ Next.js)

```typescript
// electron/preload.ts
contextBridge.exposeInMainWorld('vertexos', {
  // Proyectos
  getProjects: () => ipcRenderer.invoke('projects:getAll'),
  createProject: (data: ProjectInput) => ipcRenderer.invoke('projects:create', data),
  
  // Logs
  getLogs: (projectId: string) => ipcRenderer.invoke('logs:get', projectId),
  addLog: (log: LogEntry) => ipcRenderer.invoke('logs:add', log),
  
  // IA
  askAI: (question: string) => ipcRenderer.invoke('ai:chat', question),
  
  // Seguridad
  auditDependency: (pkg: string) => ipcRenderer.invoke('security:audit', pkg),
});
```

---

## 🗄️ Base de Datos SQLite

```typescript
// electron/database/schema.ts
const SCHEMA = `
  CREATE TABLE IF NOT EXISTS projects (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    status TEXT DEFAULT 'active',
    description TEXT,
    stack TEXT,           -- JSON array
    skills TEXT,          -- JSON array  
    created_at TEXT,
    updated_at TEXT
  );

  CREATE TABLE IF NOT EXISTS logs (
    id TEXT PRIMARY KEY,
    project_id TEXT REFERENCES projects(id),
    level TEXT NOT NULL,  -- info|warning|error|debug
    message TEXT NOT NULL,
    metadata TEXT,        -- JSON
    timestamp TEXT NOT NULL
  );

  CREATE TABLE IF NOT EXISTS bugs (
    id TEXT PRIMARY KEY,
    project_id TEXT REFERENCES projects(id),
    title TEXT NOT NULL,
    description TEXT,
    severity TEXT,        -- critical|high|medium|low
    status TEXT DEFAULT 'open',
    created_at TEXT,
    resolved_at TEXT
  );

  CREATE TABLE IF NOT EXISTS security_audits (
    id TEXT PRIMARY KEY,
    project_id TEXT REFERENCES projects(id),
    package_name TEXT NOT NULL,
    version TEXT,
    cves_found TEXT,      -- JSON array
    decision TEXT,        -- approved|rejected|approved_with_caveats
    notes TEXT,
    audited_at TEXT
  );
`;
```

---

## 🎨 Componentes UI (Next.js + Tailwind)

Los componentes siguen los tokens del sistema de diseño VertexOS adaptados a Tailwind:

```typescript
// Colores en tailwind.config.ts
colors: {
  vx: {
    white: '#FFFFFF',
    grey: {
      50: '#F9FAFB',
      100: '#F3F4F6',
      200: '#E5E7EB',
      400: '#9CA3AF',
      600: '#4B5563',
      800: '#1F2937',
      900: '#111827',
    },
    accent: '#1F2937',
    error: '#EF4444',
    success: '#10B981',
  }
}
```

---

## 📋 Referencias

- Electron: https://www.electronjs.org/docs/latest
- Next.js: https://nextjs.org/docs
- better-sqlite3: https://github.com/WiseLibs/better-sqlite3
- PocketBase: https://pocketbase.io/docs/
