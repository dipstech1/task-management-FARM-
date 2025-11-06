from fastapi import HTTPException
from app.schemas.user_schema import SignupRequestSchema,SingupResponseSchema
from app.models.user_model import UserModel
from app.core.config import settings

class UserService:

    def __init__(self) -> None:
        """Used when you want to store per-instance resources like DB connections."""
        # self.user = UserModel

    def sign_up(self,user_data:SignupRequestSchema) -> SingupResponseSchema:
        self.validate_user_input(user_data)
        new_user = UserModel(**user_data.model_dump())
        print("settings ", settings.model_dump())
        new_user.insert()
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
