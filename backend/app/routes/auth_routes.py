from fastapi import APIRouter
from app.schemas.user_schema import SignupRequestSchema,SingupResponseSchema
from app.services.user_service import UserService

user_service = UserService()

route = APIRouter(prefix="/auth", tags=["Auth"])

@route.post("/signup", response_model=SingupResponseSchema)
def sign_up(signupRequest:SignupRequestSchema):
    return user_service.sign_up(signupRequest)