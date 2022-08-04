from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base

class Alumno(Base):
    '''Modelo de alumnos.'''
    __tablename__ = 'alumnos'
    cuenta = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    primer_apellido = Column(String(50))
    segundo_apellido = Column(String(50))
    carrera = Column(String(50))
    semestre = Column(Integer)
    promedio = Column(Float)
    al_corriente = Column(Boolean)