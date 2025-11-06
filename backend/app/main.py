from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.routes.auth_routes import route as authRoute

from app.core.db import init_mongodb, close_mongo_connection


@asynccontextmanager
async def life_span(app:FastAPI):
    await init_mongodb()
    yield
    await close_mongo_connection()

app = FastAPI(lifespan=life_span)

app.include_router(authRoute )

@app.get("/health")
def health_check():
    return {
        "status" : "OK"
    }