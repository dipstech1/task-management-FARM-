from fastapi import Request,FastAPI
from app.core.middleware import (
    request_middelware,
    response_middleware
)
# from app.core.middleware.auth_middleware import JWTAuthMiddleware

def register_middleware(app: FastAPI):

    # app.add_middleware(JWTAuthMiddleware)

    @app.middleware("http")
    async def combined_middleware(request:Request, call_next):
        await request_middelware.handle_request(request=request)
        return await response_middleware.wrap_response(request, call_next)
