from fastapi import APIRouter
from app.api.v1.routes.alunos import router as alunos_router
from app.api.v1.routes.turmas import router as turmas_router

router = APIRouter()
router.include_router(alunos_router)
router.include_router(turmas_router)
