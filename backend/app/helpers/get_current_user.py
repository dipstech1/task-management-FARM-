
from fastapi import Request
from app.core.error_handler.custom_errors import AuthenticationException
from app.core.security import decode_jwt

def get_current_user_deatils(request:Request):
    token = getattr(request.state, "user_id", None)
    if not token:
        raise AuthenticationException()
    
    user_id_decoded = decode_jwt(token)
    request.state.user_id = user_id_decoded["id"]
    
    return request.state.user_id