from fastapi import Depends
from app.helpers.get_current_user import get_current_user
from app.schemas.user_schema import UserPayload
from app.core.error_handler.custom_errors import PermissionError

def check_role(role:str):

    def get_user_role(user : UserPayload = Depends(get_current_user)):
        if role != user['role']:
            raise PermissionError(f"{user['role']} is not permitted")

        return user
    
    return get_user_role
    