from typing import Awaitable, Callable
from fastapi import Request, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response, JSONResponse
from jose import JWTError
from app.core.security import decode_jwt

from app.core.logger import log_info

class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        authorization = request.headers.get("Authorization")

        if authorization:
            try:
                scheme, token = authorization.split()
                if scheme.lower() != 'bearer':
                    raise ValueError("Invalid auth scheme")
                payload = decode_jwt(token)
                log_info(f"PAYLOAD IS ${payload}")
                request.state.user_id = token
            except (ValueError, JWTError) as e:
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content= {
                        "detail" : f"Invalid token ${e}"
                    }
                )
        else:
            request.state.user_id = None
                

        return await call_next(request)