from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
import os

# URL de conexão MongoDB (pode usar .env no futuro)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = "escola_db"

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]

# Coleção de alunos
aluno_collection = db("alunos")
turma_collection = db["turmas"]


# Indexes (opcional, útil se quiser garantir matrícula única no futuro)
# await aluno_collection.create_index([("matricula", ASCENDING)], unique=True)
