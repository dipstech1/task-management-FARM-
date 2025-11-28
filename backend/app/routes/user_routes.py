from typing import List
from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from app.helpers.get_current_user import get_current_user
from app.helpers.ger_user_role import check_role
from app.services.user_service import UserService
from app.schemas.user_schema import UserDetailSchema
from app.models.user_model import Roles


user_routes = APIRouter(prefix="/user", tags=["User"])

user_service = UserService()

@user_routes.get("/user-details", response_model=UserDetailSchema)
async def get_user_details(user_id = Depends(get_current_user)):
    return await user_service.get_user_details(user_id)

@user_routes.get("/all", response_model=List[UserDetailSchema])
@cache(expire=60)
async def get_all_users(user_id = Depends(check_role(role=Roles.ADMIN.value))):
    return await user_service.get_all_users()