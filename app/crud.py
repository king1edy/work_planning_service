from sqlalchemy.orm import Session
from . import models, schemas

def create_worker(db: Session, worker: schemas.WorkerCreate):
    db_worker = models.Worker(name=worker.name)
    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)
    return db_worker

def get_workers(db: Session):
    return db.query(models.Worker).all()

def create_shift(db: Session, shift: schemas.ShiftCreate):
    worker = db.query(models.Worker).filter(models.Worker.id == shift.worker_id).first()
    
    if not worker:
        raise ValueError("Worker not found")
    
    existing_shift = db.query(models.Shift).filter(models.Shift.worker_id == shift.worker_id).first()
    
    if existing_shift:
        raise ValueError("Worker already has a shift for the day")

    db_shift = models.Shift(worker_id=shift.worker_id, start_time=shift.start_time)
    db.add(db_shift)
    db.commit()
    db.refresh(db_shift)
    return db_shift
