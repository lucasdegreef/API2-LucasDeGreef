from pydantic import BaseModel


class BeroepBase(BaseModel):
    beroep: str
    geslacht: str


class BeroepCreate(BeroepBase):
    pass


class Beroep(BeroepBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class NamenBase(BaseModel):
    voornaam: str
    achternaam: str


class NamenCreate(NamenBase):
    pass


class Naam(NamenBase):
    id: int
    items: list[Beroep] = []

    class Config:
        orm_mode = True




class WerkgeverBase(BaseModel):
    stad: str


class WerkgeverCreate(WerkgeverBase):
    werkgever : str


class Werkgver(WerkgeverBase):
    id: int

    class Config:
        orm_mode = True


class UpdateberoepenBase(BaseModel):
    beroep: str
    geslacht: str
