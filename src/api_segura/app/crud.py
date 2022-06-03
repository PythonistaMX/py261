from sqlalchemy.orm import Session

from app.models import Alumno
from app import schemas


def consulta_alumnos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Alumno).offset(skip).limit(limit).all()


def consulta_alumno(db: Session, cuenta: int):
    return db.query(Alumno).filter(Alumno.cuenta == cuenta).first()


def alta_alumno(db: Session, cuenta: int, candidato: schemas.SchemaAlumnoIn):
    alumno = Alumno(cuenta=cuenta, **dict(candidato))
    db.add(alumno)
    db.commit()
    db.refresh(alumno)
    return alumno


def baja_alumno(db: Session, alumno: Alumno):
    db.delete(alumno)
    db.commit()
    return True
