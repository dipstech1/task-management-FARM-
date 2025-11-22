from typing import List
from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from app.helpers.get_current_user import get_current_user
from app.services.user_service import UserService
from app.schemas.user_schema import UserDetailSchema

user_routes = APIRouter(prefix="/user", tags=["User"])

user_service = UserService()

@user_routes.get("/user-details", response_model=UserDetailSchema)
async def get_user_details(user_id = Depends(get_current_user)):
    return await user_service.get_user_details(user_id)

@user_routes.get("/all", response_model=List[UserDetailSchema])
@cache(expire=60)
async def get_all_users(user_id = Depends(get_current_user)):
    return await user_service.get_all_users()