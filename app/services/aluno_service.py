from app.core.database import aluno_collection
from app.models.aluno_model import aluno_helper
from bson import ObjectId

async def criar_aluno(data: dict) -> dict:
    aluno = await aluno_collection.insert_one(data)
    novo_aluno = await aluno_collection.find_one({"_id": aluno.inserted_id})
    return aluno_helper(novo_aluno)

async def listar_alunos():
    alunos = []
    async for aluno in aluno_collection.find():
        alunos.append(aluno_helper(aluno))
    return alunos

async def buscar_aluno(id: str):
    aluno = await aluno_collection.find_one({"_id": ObjectId(id)})
    return aluno_helper(aluno) if aluno else None

async def atualizar_aluno(id: str, data: dict):
    await aluno_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    aluno = await aluno_collection.find_one({"_id": ObjectId(id)})
    return aluno_helper(aluno)

async def deletar_aluno(id: str):
    resultado = await aluno_collection.delete_one({"_id": ObjectId(id)})
    return resultado.deleted_count > 0
