from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from typing import TypedDict
from app.helpers.error_handler.custom_errors import APIError
from datetime import datetime, timezone
from app.core.logger import log_error


class HttpExceptionData(TypedDict):
    message: str
    error_code: str
    timestamp: str


def register_all_errors(app):
    @app.exception_handler(APIError)
    async def handle_custom_exception(request: Request, exe: APIError):
        log_error(str(exe.detail))
        return JSONResponse(
            status_code=exe.status_code,
            content={
                "headers": exe.headers.get("X-Error-Code", "") if exe.headers else "",
                "detail": exe.detail,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            },
        )

    @app.exception_handler(HTTPException)
    async def handle_http_error(request: Request, exe: HTTPException):
        # HTTPException has attributes: status_code, detail, headers
        log_error(str(exe.detail))
        headers = getattr(exe, "headers", None)
        error_code = headers.get("X-Error-Code", "") if isinstance(headers, dict) else ""
        return JSONResponse(
            status_code=exe.status_code,
            content={"detail": exe.detail, "error_code": error_code},
        )

    @app.exception_handler(RequestValidationError)
    async def handle_request_validation_error(request: Request, exe: RequestValidationError):
        log_error(str(exe))
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": exe.errors() if hasattr(exe, "errors") else str(exe), "error_code": "validation_error"},
        )

    @app.exception_handler(ResponseValidationError)
    async def handle_response_validation_error(request: Request, exe: ResponseValidationError):
        log_error(str(exe))
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Response validation error", "error_code": "response_validation_error"},
        )

    @app.exception_handler(Exception)
    async def handle_internal_server_error(request: Request, exe: Exception):
        log_error(str(exe))
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Something went wrong", "error_code": "internal_server_error"},
        )
  
   