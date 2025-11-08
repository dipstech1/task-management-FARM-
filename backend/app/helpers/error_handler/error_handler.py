from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from typing import  Any, Callable, TypedDict
from app.helpers.error_handler.custom_errors import APIError
from datetime import datetime, timezone

app = FastAPI()

class HttpExceptionData(TypedDict):
    message: str
    error_code : str
    timestamp : str


def register_all_errors(app: FastAPI):
    @app.exception_handler(APIError)
    async def handle_custom_exception(request:Request, exe:APIError):
                print("handle_custom_exception")
                return JSONResponse(
                    status_code = exe.status_code,
                    content={
                        "headers" : exe.headers["X-Error-Code"] if exe.headers else '',
                        "detail" : exe.detail,
                        "timestamp" : datetime.now(timezone.utc).isoformat()
                    }
                )

    @app.exception_handler(HTTPException)
    async def handle_http_error(request:Request,status_code:int, exe:HttpExceptionData):
                        return JSONResponse(
                            status_code=status_code,
                            content={
                                "detail" : exe['message'],
                                "error_code" : exe["error_code"]
                            }
                        )

    @app.exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR)
    async def handle_internal_server_error(request:Request, exe:HttpExceptionData):
                        return JSONResponse(
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={
                                "detail" : "Something went wrong",
                                "error_code" : "Internal server error"
                            }
                        )
  
   