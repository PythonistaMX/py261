from sqlalchemy.orm import Session

from . import models
from . import schemas


def consulta_alumnos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Alumno).offset(skip).limit(limit).all()


def consulta_alumno(db: Session, cuenta: int):
    return db.query(models.Alumno).filter(models.Alumno.cuenta == cuenta).first()


def alta_alumno(db: Session, cuenta: int, candidato: schemas.SchemaAlumnoIn):
    alumno = models.Alumno(cuenta=cuenta, **dict(candidato))
    db.add(alumno)
    db.commit()
    db.refresh(alumno)
    return alumno


def baja_alumno(db: Session, alumno: models.Alumno):
    db.delete(alumno)
    db.commit()
    return True
