from fastapi import APIRouter
from app.schemas.user_schema import SignupRequestSchema,SingupResponseSchema, SignInRequestSchema,SigninResponse
from app.services.auth_service import AuthService

user_service = AuthService()

route = APIRouter(prefix="/auth", tags=["Auth"])

@route.post("/signup", response_model=SingupResponseSchema)
async def sign_up(signupRequest:SignupRequestSchema):
    return await user_service.sign_up(signupRequest)
    
@route.post("/login", response_model=SigninResponse)
async def login(login_request :SignInRequestSchema ):
    try:
        return await user_service.login(login_data=login_request)
    except Exception:
        # Re-raise the exception so the registered exception handlers handle it
        raise