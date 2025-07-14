from fastapi import APIRouter, HTTPException
from app.schemas.turma_schema import TurmaCreate, TurmaUpdate, TurmaDB
from app.services.turma_service import *

router = APIRouter(prefix="/turmas", tags=["Turmas"])

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

@router.put("/{id}", response_model=TurmaDB)
async def atualizar(id: str, data: TurmaUpdate):
    return await atualizar_turma(id, data.dict(exclude_none=True))

@router.delete("/{id}")
async def remover(id: str):
    sucesso = await deletar_turma(id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    return {"msg": "Turma removida"}
