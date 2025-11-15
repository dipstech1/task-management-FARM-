# app/middleware/response_middleware.py
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime, timezone
from typing import Callable
from fastapi import Request

from app.helpers.error_handler.custom_errors import APIError


async def wrap_response(request: Request, call_next: Callable):
    try:
        response = await call_next(request)
        return response

    except APIError as exc:   # custom app error
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "message": exc.detail,
                "error_code": exc.headers.get("X-Error-Code", ""),  # type: ignore
                "timestamp": datetime.now(timezone.utc).isoformat(),
            },
        )

    except HTTPException as exc:  # FastAPI errors
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "message": exc.detail,
                "error_code": getattr(exc, "headers", {}).get("X-Error-Code", "HTTP_ERROR"),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            },
        )

    except Exception as e:
        # Allow FastAPI’s global exception handler to catch it
        raise e
