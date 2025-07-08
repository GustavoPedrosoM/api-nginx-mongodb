from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def hello_world():
    return {"message": "Olá, Gustavo! Sua API base está no ar 🚀"}
