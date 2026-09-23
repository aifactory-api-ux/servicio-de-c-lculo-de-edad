"""
Servicio de cálculo de edad
"""
from datetime import date

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Age Calculator API",
    version="1.0.0"
)


class AgeRequest(BaseModel):
    """Modelo de solicitud para el cálculo de edad."""
    birthdate: date


class AgeResponse(BaseModel):
    """Modelo de respuesta con la edad calculada."""
    age: int


@app.post("/calculate-age", response_model=AgeResponse)
def calculate_age(request: AgeRequest) -> AgeResponse:
    """
    Calcula la edad actual a partir de la fecha de nacimiento.

    Args:
        request: Objeto con la fecha de nacimiento en formato YYYY-MM-DD

    Returns:
        Objeto con la edad calculada en años
    """
    today = date.today()
    birth_date = request.birthdate

    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return AgeResponse(age=age)
