```markdown
# SPEC.md

## 1. TECHNOLOGY STACK

- **Language**: Python 3.11+
- **Framework**: FastAPI (single-file, no external dependencies beyond fastapi and uvicorn)
- **Server**: Uvicorn (ASGI server, imported as dependency)

## 2. DATA CONTRACTS

### Request Model

```json
{
  "birthdate": "YYYY-MM-DD"
}
```

### Response Model

```json
{
  "age": 30
}
```

Field `birthdate` accepts ISO 8601 date string. Field `age` returns integer years calculated from birthdate to current date.

## 3. API ENDPOINTS

| Method | Path | Description |
|--------|------|-------------|
| POST | `/calculate-age` | Receives birthdate, returns calculated age |

## 4. FILE STRUCTURE

```
main.py
requirements.txt
```

**main.py** — Single file containing FastAPI application instance, Pydantic request model, response model, and `/calculate-age` route handler.

**requirements.txt** — Contains only `fastapi` and `uvicorn[standard]`.

## 5. ENVIRONMENT VARIABLES

`None`

## 6. IMPORT CONTRACTS

From `fastapi`:
- `FastAPI`
- `BaseModel`

From `main.py`:
- Application instance: `app`

## 10. FUNCTIONAL REQUIREMENTS COVERAGE

| # | Literal Requirement Phrase | Implementation Location |
|---|----------------------------|-------------------------|
| 1 | "Crear un endpoint que reciba una fecha de nacimiento y calcule la edad actual" | `main.py` — POST `/calculate-age` route with birthdate input and age calculation |
| 2 | "solo local en mi maquina" | `main.py` — Run via `uvicorn main:app --reload --host 127.0.0.1 --port 8000` |
| 3 | "nignuna" (ninguna dependencia externa adicional) | `requirements.txt` contains only fastapi and uvicorn; no database, cache, auth, or infrastructure |
```