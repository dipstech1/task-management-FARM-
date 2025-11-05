from fastapi import HTTPException
from app.schemas.user_schema import SignupRequestSchema,SingupResponseSchema

class UserService:

    def __init__(self) -> None:
        """Used when you want to store per-instance resources like DB connections."""
        # self.repository = user_repository

    def sign_up(self,user_data:SignupRequestSchema) -> SingupResponseSchema:
        self.validate_user_input(user_data)
        return SingupResponseSchema(data=None, message="User created successfully")
    
    @staticmethod
    def validate_user_input(user_data: SignupRequestSchema):
        if not user_data.first_name.isalpha() :
            raise HTTPException(status_code=400, detail="Weak password")

    # @classmethod
    # def with_default_repo(cls):
    #     """Factory method that wires up default repo dependencies."""
    #     from app.repositories import user_repository
    #     return cls(repository=user_repository)
