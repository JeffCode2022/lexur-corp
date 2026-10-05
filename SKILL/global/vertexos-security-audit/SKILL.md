---
name: vertexos-security-audit
description: Auditoria de seguridad obligatoria antes de instalar dependencias en cualquier proyecto VertexOS. Activalo cuando el usuario quiera instalar un paquete, npm install, pub add, pip install, o agregar una dependencia. Tambien activalo ante vulnerabilidades, CVE, seguridad, filtracion de datos, o antes de hacer deploy. Este skill NUNCA se omite.
---

# VertexOS — Auditoria de Seguridad

REGLA CRITICA: Este skill se ejecuta ANTES de instalar cualquier dependencia en cualquier proyecto VertexOS. Sin excepciones.

---

## Protocolo de Auditoria de Dependencias

### Paso 1 — Verificacion de CVEs

```bash
# Para Node.js / npm
npm audit --audit-level=moderate

# Para Dart / Flutter
flutter pub outdated
dart pub deps --style=list

# Para Python
pip-audit --requirement requirements.txt

# Busqueda de CVEs: https://osv.dev/
# Score de salud del paquete: https://snyk.io/advisor/
```

### Paso 2 — Checklist de Evaluacion

| Criterio | Umbral minimo | Accion si falla |
|---------|---------------|-----------------|
| CVEs criticos conocidos | 0 criticos | RECHAZAR el paquete |
| CVEs altos conocidos | max 1 con fix disponible | Evaluar alternativa |
| Mantenimiento activo | ultimo commit < 12 meses | Buscar alternativa |
| Descargas semanales npm | >1,000/semana | Evaluar si vale |
| Licencia compatible | MIT, Apache 2.0, BSD | RECHAZAR licencias GPL en app propietaria |
| Permisos solicitados | Minimos para la tarea | RECHAZAR si pide mas de lo necesario |

### Paso 3 — Banderas Rojas (bloquean instalacion)

- El paquete hace requests a URLs externas sin documentarlo
- El paquete lee variables de entorno no relacionadas con su funcion
- El paquete tiene scripts postinstall que ejecutan codigo remoto
- El nombre es muy similar a uno popular (typosquatting)
- Publicado hace menos de 30 dias con muchas descargas repentinas

### Paso 4 — Documentar en .security-audit.md

```markdown
## Auditoria [FECHA]

### Paquete: {nombre}@{version}
- CVEs encontrados: Ninguno / Lista
- Licencia: MIT / Apache 2.0 / etc.
- Ultima actualizacion: YYYY-MM-DD
- Decision: APROBADO / RECHAZADO / APROBADO CON RESERVAS
- Razon: {explicacion}
```

---

## Reglas de Secretos y Credenciales

### NUNCA en codigo:
```
const API_KEY = "AIzaSyXXXXXXXXXXX";   <- MALO
String password = "miPassword123";       <- MALO
```

### SI debes hacer:
```
# .env (en .gitignore SIEMPRE)
GEMINI_API_KEY=tu_clave_aqui

# En codigo
const apiKey = process.env.GEMINI_API_KEY;
```

### .gitignore minimo requerido:
```
.env
.env.local
.env.*.local
*.key
*.pem
*.p12
secrets/
credentials/
```

---

## Checklist por Nivel de Seguridad

### Basico (todo proyecto)
- Sin secrets en codigo
- .gitignore configurado
- Dependencias auditadas
- HTTPS obligatorio para todas las APIs

### Alto (datos de usuario, sistemas empresariales)
- Autenticacion implementada y testeada
- Validacion de inputs en frontend Y backend
- Logs sin datos personales
- Cifrado en reposo para datos sensibles

### Critico (root, hardware, pentesting)
- Autenticacion biometrica para acciones sensibles
- Audit log de todas las acciones privilegiadas
- Principio de minimo privilegio aplicado
- Comunicaciones cifradas end-to-end
- Analisis de trafico de red realizado

---

## Referencias

- CVEs: https://osv.dev/
- Analisis npm: https://snyk.io/advisor/
- OWASP Mobile: https://owasp.org/www-project-mobile-security/
- Android Security: https://developer.android.com/topic/security/best-practices
