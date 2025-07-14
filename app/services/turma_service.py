# app/services/turma_service.py

from app.core.database import turma_collection
from app.models.turma_model import turma_helper
from bson import ObjectId

async def criar_turma(data: dict) -> dict:
    turma = await turma_collection.insert_one(data)
    nova_turma = await turma_collection.find_one({"_id": turma.inserted_id})
    return turma_helper(nova_turma)

async def listar_turmas():
    turmas = []
    async for turma in turma_collection.find():
        turmas.append(turma_helper(turma))
    return turmas

async def buscar_turma(id: str):
    turma = await turma_collection.find_one({"_id": ObjectId(id)})
    return turma_helper(turma) if turma else None

async def atualizar_turma(id: str, data: dict):
    await turma_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    turma = await turma_collection.find_one({"_id": ObjectId(id)})
    return turma_helper(turma)

async def deletar_turma(id: str):
    resultado = await turma_collection.delete_one({"_id": ObjectId(id)})
    return resultado.deleted_count > 0
