from fastapi import HTTPException
from app.schemas.user_schema import SignupRequestSchema,SingupResponseSchema, SignInRequestSchema,SigninResponse
from app.models.user_model import UserModel
from app.dal.user_dal import UserDAL
from app.helpers.error_handler.custom_errors import ExistingUserException,UserNotFoundException,InvalidPasswordException
from app.core.security import hash_data, decode_data, create_jwt

class AuthService:

    def __init__(self) -> None:
        """Used when you want to store per-instance resources like DB connections."""
        # self.user = UserModel
        self.USER_DAL = UserDAL()

    async def sign_up(self,user_data:SignupRequestSchema) -> SingupResponseSchema:
            self.validate_user_input(user_data)
            new_user = UserModel(first_name=user_data.first_name, last_name=user_data.last_name,email=user_data.email,role=user_data.role,password=hash_data(user_data.password))
            is_new_user = await self.USER_DAL.get_user_details(new_user.email)
            if not is_new_user:
                new_user_data = await self.USER_DAL.add_user(new_user)
                return SingupResponseSchema(data=new_user_data, message="User created successfully", success=True)
            else:
                raise ExistingUserException(f"{new_user.email} already exist") 
            
    async def login(self, login_data:SignInRequestSchema) -> SigninResponse :
         user_exist : UserModel | None = await self.USER_DAL.get_user_details(login_data.email)

         if not user_exist:
              raise UserNotFoundException(usr_message="Invalid credentials6")
         else:
            is_password_same = decode_data(user_exist.password, login_data.password)

            if not is_password_same:
                 raise InvalidPasswordException(usr_message="Invalid credentials")
            
            print("user_exist ", user_exist)
            
            user_token_data = {
                 "email" : user_exist.email,
            }
            token = create_jwt(user_token_data)

            print("token , ", token) 

            return SigninResponse(data=token, success=True)
    
    @staticmethod
    def validate_user_input(user_data: SignupRequestSchema):
        if not user_data.first_name.isalpha() :
            raise HTTPException(status_code=400, detail="Weak password")

    # @classmethod
    # def with_default_repo(cls):
    #     """Factory method that wires up default repo dependencies."""
    #     from app.repositories import user_repository
    #     return cls(repository=user_repository)
