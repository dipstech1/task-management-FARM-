from beanie import Document
from pydantic import Field,EmailStr
from app.schemas.user_schema import Roles

class UserModel(Document):
    first_name:str = Field(title="First name")
    last_name:str = Field(title="Last name")
    email:EmailStr = Field(title="Email")
    password:str = Field(title="Password", min_length=5)
    role:Roles = Field(title="User role", default=Roles.EMPLOYEE)

    class Setting:
        name = "users"