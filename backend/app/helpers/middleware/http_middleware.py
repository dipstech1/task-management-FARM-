from datetime import datetime, timezone
from fastapi import Request,FastAPI,HTTPException
from fastapi.responses import JSONResponse
from app.helpers.error_handler.custom_errors import APIError


def register_middleware(app: FastAPI):
    @app.middleware("http")
    async def custom_response_wrapper(request: Request, call_next):
        try:
            response = await call_next(request)
            # handle normal responses
            return response
        except APIError as exc:
            # handle your custom APIError gracefully
            return JSONResponse(
                status_code=exc.status_code,
                content={
                    "message": exc.detail,
                    "error_code": exc.headers.get("X-Error-Code", ""), # type: ignore
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                },
            )
        except HTTPException as exc:
        # ✅ Handle general HTTP exceptions
            return JSONResponse(
                status_code=exc.status_code,
                content={
                    "message": exc.detail,
                    "error_code": getattr(exc, "headers", {}).get("X-Error-Code", "HTTP_ERROR"),
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                },
        )
        except Exception as e:
            # fallback for unhandled exceptions
            raise e
   
