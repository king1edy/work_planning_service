from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

class Shift(Base):
    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("workers.id"))
    start_time = Column(String, nullable=False)  # "0-8", "8-16", "16-24"

    worker = relationship("Worker", back_populates="shifts")

Worker.shifts = relationship("Shift", back_populates="worker", cascade="all, delete")
