
from fastapi import  HTTPException, status
from typing import Optional

class APIError(HTTPException):
     def __init__(self, status_code: int, message: str, error_code: str):
        super().__init__(
            status_code=status_code,
            detail=message,
            headers={"X-Error-Code": error_code}
        )

class UserNotFoundException(APIError):
    def __init__(self, usr_message:Optional[str] = ''):
        super().__init__(
            status_code= status.HTTP_404_NOT_FOUND,
            message= "User not found" if not usr_message else usr_message,
            error_code="NOT_FOUND"
        )

class ExistingUserException(APIError):
    def __init__(self, usr_message:Optional[str] = ''):
        super().__init__(
            status_code= status.HTTP_226_IM_USED,
            message= "User already exist" if not usr_message else usr_message,
            error_code="NOT_FOUND"
        )

class InvalidPasswordException(APIError):
    def __init__(self, usr_message:Optional[str] = ''):
        super().__init__(
            status_code= status.HTTP_226_IM_USED,
            message= usr_message or '',
            error_code="INVALID"
        )