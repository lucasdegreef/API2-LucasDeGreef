from sqlalchemy import Column, ForeignKey, Integer, String,CHAR
from sqlalchemy.orm import relationship

from database import Base


class Namen(Base):
    __tablename__ = "Namen"

    id = Column(Integer, primary_key=True, index=True)
    voornaam = Column(String, index=True)
    achternaam = Column(String, index=True)

    items = relationship("Beroep", back_populates="beroep_id")


class Beroep(Base):
    __tablename__ = "Beroepen"

    id = Column(Integer, primary_key=True, index=True)
    beroep = Column(String, index=True)
    geslacht = Column(CHAR, index=True)
    owner_id = Column(Integer, ForeignKey("Namen.id"))

    beroep_id = relationship("Namen", back_populates="items")


class Werkgever(Base):
    __tablename__ = "Werkgever"

    id = Column(Integer, primary_key=True, index=True)
    hashed_werkgever = Column(String)
    stad = Column(String, index=True)
