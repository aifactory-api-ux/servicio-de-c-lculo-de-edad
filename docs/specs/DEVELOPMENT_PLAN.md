# DEVELOPMENT PLAN: Servicio de cálculo de edad

## 1. ARCHITECTURE OVERVIEW
Servicio FastAPI minimalista que expone un único endpoint POST `/calculate-age`. Recibe una fecha de nacimiento en formato ISO 8601 y retorna la edad calculada en años. Arquitectura single-file sin dependencias externas adicionales a las del framework.

## 2. ACCEPTANCE CRITERIA
1. Endpoint POST `/calculate-age` acepta body JSON con campo `birthdate` (YYYY-MM-DD) y retorna `{ "age": <integer> }`
2. La edad se calcula como la diferencia entre la fecha actual y la fecha de nacimiento
3. Archivos generados: `main.py` y `requirements.txt` únicamente

## TEAM SCOPE (MANDATORY — PARSED BY THE PIPELINE)
- **Role:** backend_developer (`role-be`)

---

## 3. EXECUTABLE ITEMS

### ITEM 1: Implementar endpoint de cálculo de edad

**Goal:** Crear endpoint POST `/calculate-age` que reciba birthdate y retorne age

**Files to create:**
- `main.py` — Aplicación FastAPI con modelo Request, modelo Response, y route handler
- `requirements.txt` — Dependencias: fastapi y uvicorn[standard]

**Dependencies:** Ninguna adicional (solo fastapi, uvicorn)

**Validation:**
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
uvicorn main:app --reload --host 127.0.0.1 --port 8000

# Probar endpoint
curl -X POST "http://127.0.0.1:8000/calculate-age" \
  -H "Content-Type: application/json" \
  -d '{"birthdate": "1990-01-15"}'

# Respuesta esperada: {"age": 35} (o la edad calculada según fecha actual)
```

**Role:** role-be (backend_developer)