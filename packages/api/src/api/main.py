from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.core.di import settings
from packages.common.src.common.logger import configure_logging

configure_logging()


@asynccontextmanager
async def lifespan(_: FastAPI):
    yield


def build_routes(app: FastAPI):
    from api.features.health.router import router as health_router
    from api.features.search.router import router as status_router

    app.include_router(health_router)
    app.include_router(status_router)


def create_app() -> FastAPI:
    _app = FastAPI(
        lifespan=lifespan,
        version=settings.app_version,
        title=settings.app_name,
    )
    build_routes(_app)

    return _app


app = create_app()
