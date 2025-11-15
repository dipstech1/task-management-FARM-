# app/middleware/request_middleware.py
from fastapi import Request
from app.core.logger import log_info

async def handle_request(request: Request):
    """
    Add any request preprocessing, logging, validation, etc.
    This is optional—add logic as needed.
    """
    # Example: log or modify request
    print("Incoming request:", log_info(request.url.path))
    return request
