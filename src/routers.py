from fastapi import APIRouter
from avant_microservices.views import avant_microservices_router


router = APIRouter()


router.include_router(
    avant_microservices_router,
    prefix='/avant-microservices',
    tags=['avant-microservices'],
)
