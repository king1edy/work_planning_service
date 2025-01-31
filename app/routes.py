from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from . import crud, schemas

router = APIRouter()

@router.post("/workers/", response_model=schemas.WorkerResponse)
def create_worker(worker: schemas.WorkerCreate, db: Session = Depends(get_db)):
    return crud.create_worker(db, worker)

@router.get("/workers/", response_model=list[schemas.WorkerResponse])
def get_workers(db: Session = Depends(get_db)):
    return crud.get_workers(db)

@router.post("/shifts/", response_model=schemas.ShiftResponse)
def create_shift(shift: schemas.ShiftCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_shift(db, shift)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
