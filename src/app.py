from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from common.exceptions import CommonExceptions
from common.sentry import capture_exception
from routers import router
from django.apps import apps
from django.conf import settings
from orm import (
    async_request_started,
    async_request_finished
)

apps.populate(settings.INSTALLED_APPS)

app = FastAPI(
    title='Avant Microservices',
    description='Avant Microservices',
    version='0.0.1',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware('http')
async def asgi_django_orm_manager(request: Request, call_next):
    try:
        await async_request_started()
        response = await call_next(request)
    except Exception as ex:
        response = ex
    finally:
        await async_request_finished()
        return response


# sentry_sdk.init(
#     dsn=os.getenv('SENTRY_DSN'),
#     environment=os.getenv('ENVIRONMENT'),
# )


app.include_router(router)


@app.exception_handler(CommonExceptions)
async def handle_mystique_exception(
    request: Request,
    error: CommonExceptions
):
    return JSONResponse(
        error.to_dict(),
        error.status_code
    )


@app.exception_handler(Exception)
async def all_exceptions_handler(request: Request, error: Exception):
    capture_exception(error)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content='Internal server error',
    )
