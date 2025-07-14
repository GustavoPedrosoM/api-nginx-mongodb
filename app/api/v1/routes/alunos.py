from fastapi import APIRouter, HTTPException
from app.schemas.aluno_schema import AlunoCreate, AlunoUpdate, AlunoDB
from app.services.aluno_service import *

router = APIRouter(prefix="/alunos", tags=["Alunos"])

@router.post("/", response_model=AlunoDB)
async def criar(data: AlunoCreate):
    return await criar_aluno(data.dict())

@router.get("/", response_model=list[AlunoDB])
async def listar():
    return await listar_alunos()

@router.get("/{id}", response_model=AlunoDB)
async def obter(id: str):
    aluno = await buscar_aluno(id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@router.put("/{id}", response_model=AlunoDB)
async def atualizar(id: str, data: AlunoUpdate):
    return await atualizar_aluno(id, data.dict(exclude_none=True))

@router.delete("/{id}")
async def remover(id: str):
    sucesso = await deletar_aluno(id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"msg": "Aluno removido"}
