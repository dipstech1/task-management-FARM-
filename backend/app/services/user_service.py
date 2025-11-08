from fastapi import HTTPException
from app.schemas.user_schema import SignupRequestSchema,SingupResponseSchema
from app.models.user_model import UserModel
from app.dal.user_dal import UserDAL
from app.helpers.error_handler.custom_errors import ExistingUserException
class UserService:

    def __init__(self) -> None:
        """Used when you want to store per-instance resources like DB connections."""
        # self.user = UserModel
        self.USER_DAL = UserDAL()

    async def sign_up(self,user_data:SignupRequestSchema) -> SingupResponseSchema:
            self.validate_user_input(user_data)
            new_user = UserModel(first_name=user_data.first_name, last_name=user_data.last_name,email=user_data.email,role=user_data.role,password=user_data.password)
            is_new_user = await self.USER_DAL.get_user_details(new_user.email)
            if not is_new_user:
                new_user_data = await self.USER_DAL.add_user(new_user)
                return SingupResponseSchema(data=new_user_data, message="User created successfully")
            else:
                raise ExistingUserException(f"{new_user.email} already exist") 
        
    
    @staticmethod
    def validate_user_input(user_data: SignupRequestSchema):
        if not user_data.first_name.isalpha() :
            raise HTTPException(status_code=400, detail="Weak password")

    # @classmethod
    # def with_default_repo(cls):
    #     """Factory method that wires up default repo dependencies."""
    #     from app.repositories import user_repository
    #     return cls(repository=user_repository)
