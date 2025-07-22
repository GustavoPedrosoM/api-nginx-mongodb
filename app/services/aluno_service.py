from app.core.database import aluno_collection
from app.models.aluno_model import aluno_helper
from app.core.database import turma_collection
from bson import ObjectId

async def criar_aluno(data: dict) -> dict:
    if "turma_id" in data and data["turma_id"]:
        data["turma_id"] = ObjectId(data["turma_id"])
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
    if not aluno:
        return None

    turma = None
    if "turma_id" in aluno:
        turma = await turma_collection.find_one({"_id": ObjectId(aluno["turma_id"])})

    return aluno_helper(aluno, turma)

async def atualizar_aluno(id: str, data: dict):
    if "turma_id" in data:
        data["turma_id"] = ObjectId(data["turma_id"])
    await aluno_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    aluno = await aluno_collection.find_one({"_id": ObjectId(id)})
    return aluno_helper(aluno)

async def deletar_aluno(id: str):
    resultado = await aluno_collection.delete_one({"_id": ObjectId(id)})
    return resultado.deleted_count > 0
