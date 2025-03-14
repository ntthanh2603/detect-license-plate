from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/driver/{cid_id}", response_model=schemas.Driver)
def read_user(cid_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_driver(db, cid_id=cid_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Không thấy tài khoản")
    return db_user

@app.post("/drive/", response_model=schemas.Driver)
def create_user_for_drive(driver : schemas.Driver, db : Session = Depends(get_db)):
    db_driver = crud.get_driver_by_cid(db, cid_id=driver.cid)
    if db_driver is None:
        raise HTTPException(status_code=400, detail="Tài khoản tài xế đã tồn tại")
    return crud.create_driver(db=db, driver=driver)



# if __name__ == "__main__":
# 	import uvicorn

# 	# Run the FastAPI application using Uvicorn
# 	uvicorn.run(app, host="127.0.0.1", port=8000)
