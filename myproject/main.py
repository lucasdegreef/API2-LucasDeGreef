from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/persoon/", response_model=schemas.Naam)
def create_user(user: schemas.NamenCreate, db: Session = Depends(get_db)):
    return crud.create_persoon(db=db, naam=user)

#alle mensen in met voornaam en achternaam laten zien met hun beroep en geslacht
@app.get("/persoon/", response_model=list[schemas.Naam])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/persoon/{user_id}", response_model=schemas.Naam)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

#mensen linken aan een beroep.
@app.post("/persoon/{user_id}/beroep/", response_model=schemas.Beroep)
def create_item_for_user(
    user_id: int, beroep: schemas.BeroepCreate, db: Session = Depends(get_db)
):
    return crud.create_beroep(db=db, beroep=beroep, user_id=user_id)


@app.post("/persoon/werkgever",response_model=schemas.Werkgver)
def create_werkgever(werkgever : schemas.WerkgeverCreate , db : Session = Depends(get_db) ):
    return crud.create_werkgever(db=db , werkgever=werkgever)

#alle beroepen mensen hun beroepen.
@app.get("/beroepen/", response_model=list[schemas.Beroep])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.delete("/delete/{user_id}/")
def delete_user(user_id : int , db:Session = Depends(get_db)):
    details = crud.get_user_by_id(db, user_id=user_id )
    if details is None:
        raise HTTPException(status_code=400, detail="geen persoon gevonden om te verwijderen")
    crud.delete_persoon(db=db,user_id=user_id)
    crud.delete_beroep_van_persoon(db=db,user_id=user_id)
    return {"delete persoon" : "succes"}

@app.put("/update/beroep/{user_id}",response_model=schemas.Beroep)
def update_beroep(user_id : int, update: schemas.UpdateberoepenBase , db:Session = Depends(get_db)):
    details = crud.get_user_by_id(db=db, user_id=user_id)
    if details is None:
        raise HTTPException(status_code=400, detail="geen persoon gevonden")
    return crud.update_beroep(db=db,user_id=user_id,update=update)