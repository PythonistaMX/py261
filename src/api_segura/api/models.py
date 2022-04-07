from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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

class User(Base):
    '''Modelo de usuarios'''
    class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
