from pydantic import BaseModel
from typing import Optional

class TurmaBase(BaseModel):
    nome: str
    ano: int
    turno: str

class TurmaCreate(TurmaBase):
    pass

class TurmaUpdate(BaseModel):
    nome: Optional[str] = None
    ano: Optional[int] = None
    turno: Optional[str] = None

class TurmaDB(TurmaBase):
    id: str
