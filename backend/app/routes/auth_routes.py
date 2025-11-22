from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user_schema import SignupRequestSchema,SingupResponseSchema, SignInRequestSchema,SigninResponse
from app.services.auth_service import AuthService
from app.helpers.get_current_user import get_current_user

user_service = AuthService()

route = APIRouter(prefix="/auth", tags=["Auth"])

@route.post("/signup", response_model=SingupResponseSchema)
async def sign_up(signupRequest:SignupRequestSchema):
    return await user_service.sign_up(signupRequest)
    
@route.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    try:
        login_request = SignInRequestSchema(email=form_data.username, password=form_data.password)
        response = await user_service.login(login_data=login_request)
        return {
            "access_token": response.data,
            "token_type": "bearer"
        }
    except Exception:
        # Re-raise the exception so the registered exception handlers handle it
        raise


@route.post("/private")
async def private_route(user_id = Depends(get_current_user)):
    return {"message" : f"User id is ${user_id}"}