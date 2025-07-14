from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class AlunoBase(BaseModel):
    nome: str
    idade: int
    matricula: str

class AlunoCreate(AlunoBase):
    pass

class AlunoUpdate(BaseModel):
    nome: Optional[str]
    idade: Optional[int]
    matricula: Optional[str]

class AlunoDB(AlunoBase):
    id: str

    class Config:
        orm_mode = True
