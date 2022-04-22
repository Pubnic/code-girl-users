from fastapi import APIRouter
from .serializers import StatusOKSerializer


avant_microservices_router = APIRouter()


@avant_microservices_router.get(
    '/status',
    summary='Status da API',
    description='Retorna se o status da API é OK.',
    response_model=StatusOKSerializer,
)
async def status():
    return StatusOKSerializer()
