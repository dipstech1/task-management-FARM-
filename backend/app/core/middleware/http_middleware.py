from fastapi import Request,FastAPI
from app.core.middleware import (
    request_middelware,
    response_middleware
)


def register_middleware(app: FastAPI):
    @app.middleware("http")
    async def combined_middleware(request:Request, call_next):
        await request_middelware.handle_request(request=request)
        return await response_middleware.wrap_response(request, call_next)
