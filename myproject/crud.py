from sqlalchemy.orm import Session

import models
import schemas
import auth


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.Namen).filter(models.Namen.id == user_id).first()

def get_user_by_name(db:Session, user:str):
    return db.query(models.Namen).filter(models.Namen.voornaam == user).first()
"""
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
"""

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Namen).offset(skip).limit(limit).all()


def create_persoon(db: Session, naam: schemas.NamenCreate):
    hashed_achternaam = auth.get_password_hash(naam.achternaam)
    db_user = models.Namen(voornaam=naam.voornaam, achternaam=hashed_achternaam)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Beroep).offset(skip).limit(limit).all()


def create_beroep(db: Session, beroep: schemas.BeroepCreate, user_id: int):
    db_item = models.Beroep(**beroep.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_werkgever(db: Session, werkgever : schemas.WerkgeverCreate ):
    hashed_werkgever = auth.get_password_hash(werkgever.werkgever)
    db_item = models.Werkgever(hashed_werkgever=hashed_werkgever,stad=werkgever.stad)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_persoon(db : Session, user_id : int):
    db.query(models.Namen).filter(models.Namen.id == user_id).delete()
    db.commit()

def delete_beroep_van_persoon(db : Session , user_id : int):
    db.query(models.Beroep).filter(models.Beroep.owner_id == user_id).delete()
    db.commit()

def update_beroep(db : Session , user_id : int , update : schemas.UpdateberoepenBase):
    beroep_info = db.query(models.Beroep).filter(models.Beroep.owner_id== user_id).first()

    if beroep_info is None:
        return None
    db.query(models.Beroep).filter(models.Beroep.owner_id== user_id).update(vars(update))
    db.commit()

    return db.query(models.Beroep).filter(models.Beroep.owner_id== user_id).first()