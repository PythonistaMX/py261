
from pydantic import BaseModel, Field, PositiveInt
from typing import Optional, Literal
from .data import CARRERAS


class SchemaAlumno(BaseModel):
    cuenta: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str = ''
    carrera: Literal[tuple(CARRERAS)]
    semestre: PositiveInt
    promedio: float = Field(ge=0, le=10)
    al_corriente: bool
        
    class Config:
        orm_mode = True
        

class SchemaAlumnoIn(BaseModel):
    nombre: str
    primer_apellido: str
    segundo_apellido: str = ''
    carrera: Literal[tuple(CARRERAS)]
    semestre: PositiveInt
    promedio: float = Field(ge=0, le=10)
    al_corriente: bool
        
    class Config:
        orm_mode = True