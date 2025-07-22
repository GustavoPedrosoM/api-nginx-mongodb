from fastapi import APIRouter
from .alunos import router as alunos_router
from .turmas import router as turmas_router

router = APIRouter()

router.include_router(alunos_router, prefix="/alunos", tags=["Alunos"])
router.include_router(turmas_router, prefix="/turmas", tags=["Turmas"])
