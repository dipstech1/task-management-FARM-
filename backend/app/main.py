from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.error_handler.error_handler import register_all_errors
from app.core.middleware.http_middleware  import register_middleware

from app.routes.auth_routes import route as authRoute

from app.core.db import init_mongodb, close_mongo_connection


@asynccontextmanager
async def life_span(app:FastAPI):
    await init_mongodb()
    yield
    await close_mongo_connection()

app = FastAPI(lifespan=life_span)

register_all_errors(app)

register_middleware(app)



app.include_router(authRoute )


@app.get("/health")
def health_check():
    return {
        "status" : "OK"
    }