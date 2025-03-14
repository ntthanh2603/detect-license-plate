from sqlalchemy.orm import Session
import models
import schemas
from .models import Driver


def get_driver(db: Session, cid_id: int):
    return db.query(models.Driver).filter(models.Driver.cid == cid_id).first()

def get_driver_by_cid(db : Session, cid_id : str):
    return db.query(models.Driver).filter(models.Driver.cid == cid_id).first()

def get_drivers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Driver).offset(skip).limit(limit).all()

def create_driver(db: Session, driver : schemas.Driver):
    db.add(db)
    db.commit()
    db.refresh(db)
    return 