from fastapi_users.models import BaseUser, BaseUserCreate, BaseUserUpdate, BaseUserDB
from sqlalchemy import Column, Integer, String, Float, Boolean
from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()

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

class User(BaseUser):
    pass


class UserCreate(BaseUserCreate):
    pass


class UserUpdate(BaseUserUpdate):
    pass


class UserDB(User, BaseUserDB):
    pass

class UserTable(Base, SQLAlchemyBaseUserTable):
    pass