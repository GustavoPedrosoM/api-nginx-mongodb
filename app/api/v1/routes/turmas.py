from fastapi import APIRouter, HTTPException
from app.schemas.turma_schema import TurmaCreate, TurmaUpdate, TurmaDB
from app.services.turma_service import *
from app.core.database import aluno_collection
from app.models.aluno_model import aluno_helper
from app.schemas.aluno_schema import AlunoDB


router = APIRouter()

@router.post("/", response_model=TurmaDB)
async def criar(data: TurmaCreate):
    return await criar_turma(data.dict())

@router.get("/", response_model=list[TurmaDB])
async def listar():
    return await listar_turmas()

@router.get("/{id}", response_model=TurmaDB)
async def obter(id: str):
    turma = await buscar_turma(id)
    if not turma:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    return turma

@router.get("/{turma_id}/alunos", response_model=list[AlunoDB])
async def listar_alunos_por_turma(turma_id: str):
    alunos = []
    async for aluno in aluno_collection.find({"turma_id": ObjectId(turma_id)}):
        alunos.append(aluno_helper(aluno))
    return alunos

@router.put("/{id}", response_model=TurmaDB)
async def atualizar(id: str, data: TurmaUpdate):
    return await atualizar_turma(id, data.dict(exclude_none=True))

@router.delete("/{id}")
async def remover(id: str):
    sucesso = await deletar_turma(id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    return {"msg": "Turma removida"}
