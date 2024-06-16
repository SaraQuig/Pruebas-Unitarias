from fastapi import APIRouter
from app.api.endpoints import clientes

api_router = APIRouter()
api_router.include_router(clientes.router, prefix="/api", tags=["clientes"])
