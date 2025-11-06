from fastapi import HTTPException
from app.schemas.user_schema import SignupRequestSchema,SingupResponseSchema
from app.models.user_model import UserModel
from app.core.config import settings
from app.dal.user_dal import UserDAL

class UserService:

    def __init__(self) -> None:
        """Used when you want to store per-instance resources like DB connections."""
        # self.user = UserModel
        self.user_dal = UserDAL()

    async def sign_up(self,user_data:SignupRequestSchema) -> SingupResponseSchema:
        try:
            self.validate_user_input(user_data)
            new_user = UserModel(first_name=user_data.first_name, last_name=user_data.last_name,email=user_data.email,role=user_data.role,password=user_data.password)
            new_user_data = await self.user_dal.add_user(new_user)
            return SingupResponseSchema(data=new_user_data, message="User created successfully")
        except Exception as e:
            print(e)
            return SingupResponseSchema(data=None, message="Something went wrong")
    
    @staticmethod
    def validate_user_input(user_data: SignupRequestSchema):
        if not user_data.first_name.isalpha() :
            raise HTTPException(status_code=400, detail="Weak password")

    # @classmethod
    # def with_default_repo(cls):
    #     """Factory method that wires up default repo dependencies."""
    #     from app.repositories import user_repository
    #     return cls(repository=user_repository)
