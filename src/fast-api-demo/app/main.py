from typing import List
from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from . import crud
from . import models
from . import schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/", response_model=List[schemas.SchemaAlumno])
def vuelca_base(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    alumnos = crud.consulta_alumnos(db, skip=skip, limit=limit)
    return alumnos


@app.get("/api/{cuenta}", response_model=schemas.SchemaAlumno)
def get_alumno(cuenta, db: Session = Depends(get_db)):
    alumno = crud.consulta_alumno(db=db, cuenta=cuenta)
    if alumno:
        return alumno
    else:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

        
@app.delete("/api/{cuenta}")
def delete_alumno(cuenta, db: Session = Depends(get_db)):
    alumno = crud.consulta_alumno(db=db, cuenta=cuenta)
    if alumno:
        crud.baja_alumno(db=db, alumno=alumno)
        return {status_code:201, detail:"OK"}
    else:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

        
@app.post("/api/{cuenta}", response_model=schemas.SchemaAlumno)
def post_alumno(cuenta, candidato: schemas.SchemaAlumnoIn, db: Session = Depends(get_db)):
    alumno = crud.consulta_alumno(db=db, cuenta=cuenta)
    if alumno:
        raise HTTPException(status_code=409, detail="Recurso existente")
    return crud.alta_alumno(db=db, cuenta=cuenta, candidato=candidato)        
        
        
@app.put("/api/{cuenta}", response_model=schemas.SchemaAlumno)
def put_alumno(cuenta, candidato: schemas.SchemaAlumnoIn, db: Session = Depends(get_db)):
    alumno = crud.consulta_alumno(db=db, cuenta=cuenta)
    if alumno:
        crud.baja_alumno(db=db, alumno=alumno)
        return crud.alta_alumno(db=db, cuenta=cuenta, candidato=candidato)
    else:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")
    
    