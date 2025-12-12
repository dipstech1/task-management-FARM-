from pydantic import BaseModel,Field,EmailStr
from beanie import PydanticObjectId
from enum import Enum
from typing import Any, TypedDict
from app.schemas.base_schema import BaseResponseSchema

class Roles(Enum):
    ADMIN = 'ADMIN'
    MANAGER = 'MANAGER'
    EMPLOYEE = 'EMPLOYEE'

class SignupRequestSchema(BaseModel):
    first_name:str = Field(title="First name")
    last_name:str = Field(title="Last name")
    email:EmailStr = Field(title="Email")
    password:str = Field(title="Password", min_length=5)
    role:Roles = Field(title="User role", default=Roles.EMPLOYEE)

class SignInRequestSchema(BaseModel):
    email : EmailStr = Field(...,title='User email')
    password : str = Field(...,title='User email')

class SingupResponseSchema(BaseResponseSchema):
    data:Any | None = Field(default=None)
    message:str = Field(title="Message")

class UserDetailSchema(BaseModel):
    id:PydanticObjectId = Field(title="Id")
    first_name:str = Field(title="First name")
    last_name:str = Field(title="Last name")
    email:EmailStr = Field(title="Email")
    role:Roles = Field(title="User role", default=Roles.EMPLOYEE)

class SigninResponse(BaseResponseSchema):
    pass


class UserPayload(TypedDict):
    user_id : str | None
    role : str