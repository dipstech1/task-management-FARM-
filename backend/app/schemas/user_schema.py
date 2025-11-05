from pydantic import BaseModel,Field,EmailStr
from enum import Enum
from typing import Any

class Roles(Enum):
    ADMIN = 1
    MANAGER = 2
    EMPLOYEE = 3

class SignupRequestSchema(BaseModel):
    first_name:str = Field(title="First name")
    last_name:str = Field(title="Last name")
    email:EmailStr = Field(title="Email")
    password:str = Field(title="Password", min_length=5)
    role:Roles = Field(title="User role", default=Roles.EMPLOYEE)

class SingupResponseSchema(BaseModel):
    data:Any | None = Field(default=None)
    message:str = Field(title="Message")