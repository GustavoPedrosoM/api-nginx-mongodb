from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Lê as variáveis
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "escola_db")

# Conecta ao MongoDB
client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]

# Coleções
aluno_collection = db.get_collection("alunos")
turma_collection = db.get_collection("turmas")

# Exemplo (se for usar em algum ponto futuro):
# await aluno_collection.create_index([("matricula", ASCENDING)], unique=True)
