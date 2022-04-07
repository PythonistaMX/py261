from fastapi import APIRouter
from typing import List
from data import CARRERAS

router = APIRouter()

@router.get("/carreras")
def consulta_carreras():
    return {'carreras': CARRERAS}