from pydantic import BaseModel
from typing import List

class WorkerCreate(BaseModel):
    name: str

class WorkerResponse(WorkerCreate):
    id: int

    class Config:
        from_attributes = True

class ShiftCreate(BaseModel):
    worker_id: int
    start_time: str  # "0-8", "8-16", "16-24"

class ShiftResponse(ShiftCreate):
    id: int

    class Config:
        from_attributes = True
