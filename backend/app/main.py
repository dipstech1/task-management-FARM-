from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.error_handler.error_handler import register_all_errors
from app.core.middleware.http_middleware  import register_middleware

from app.routes.auth_routes import route as authRoute
from app.routes.user_routes import user_routes
from app.routes.task_routes import task_router
from app.routes.project_routes import project_routes

from app.core.db import init_mongodb, close_mongo_connection
from fastapi_cache import FastAPICache
from app.core.cache import LRUBackend


@asynccontextmanager
async def life_span(app:FastAPI):
    await init_mongodb()
    FastAPICache.init(LRUBackend(capacity=1000), prefix="fastapi-cache")
    yield
    await close_mongo_connection()

app = FastAPI(lifespan=life_span)

register_all_errors(app)

register_middleware(app)



app.include_router(authRoute,prefix="/api" )
app.include_router(user_routes, prefix="/api")
app.include_router(task_router, prefix="/api")
app.include_router(project_routes, prefix="/api")


@app.get("/health")
def health_check():
    return {
        "status" : "OK"
    }