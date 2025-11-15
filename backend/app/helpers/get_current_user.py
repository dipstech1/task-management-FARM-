
from fastapi import Request
from app.core.error_handler.custom_errors import AuthenticationException

def get_current_user_deatils(request:Request):
    if not getattr(request.state, "user_id", None):
        raise AuthenticationException()
    
    return request.state.user_id