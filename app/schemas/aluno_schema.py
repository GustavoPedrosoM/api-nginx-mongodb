from pydantic import BaseModel
from typing import Optional

class TurmaResumo(BaseModel):
    id: str
    nome: str

class AlunoBase(BaseModel):
    nome: str
    idade: int
    matricula: str
    turma_id: Optional[str] = None

class AlunoCreate(AlunoBase):
    pass

class AlunoUpdate(BaseModel):
    nome: Optional[str]
    idade: Optional[int]
    matricula: Optional[str]
    turma_id: Optional[str] = None

class AlunoDB(AlunoBase):
    id: str
    turma: Optional[TurmaResumo] = None  

    class Config:
        from_attributes = True
