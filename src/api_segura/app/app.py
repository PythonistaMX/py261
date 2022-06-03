from typing import List
from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from app import crud
from app import models
from app import schemas
from app.db import create_db_and_tables, get_db
from app.users import auth_backend, current_active_user, fastapi_users


app = FastAPI()

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
async def delete_alumno(cuenta, user: models.UserDB = Depends(current_active_user), db: Session = Depends(get_db)):
    alumno = crud.consulta_alumno(db=db, cuenta=cuenta)
    if alumno:
        crud.baja_alumno(db=db, alumno=alumno)
        return {}
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

AUTH_PATH ='/auth'

app.include_router(fastapi_users.get_auth_router(auth_backend), 
prefix=f"{AUTH_PATH}/jwt", 
tags=["auth"])
app.include_router(fastapi_users.get_register_router(), 
prefix=f"{AUTH_PATH}", 
tags=["auth"])
app.include_router(fastapi_users.get_reset_password_router(),
prefix=f"{AUTH_PATH}",
tags=["auth"],)
app.include_router(fastapi_users.get_verify_router(),
prefix=f"{AUTH_PATH}",
tags=["auth"],)
app.include_router(fastapi_users.get_users_router(), 
prefix="/users", 
tags=["users"])

@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()