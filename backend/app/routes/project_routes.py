from fastapi import APIRouter, Depends
from app.helpers.get_current_user import get_current_user
from app.schemas.project_schema import ProjectSchema

project_routes = APIRouter(prefix="/project", tags=["Project"], dependencies=[Depends(get_current_user)])

@project_routes.post("/")
def create_task(project_data:ProjectSchema):
    print(project_data)
    return {
        'data' : project_data
    }





# @project_routes.get("/me", response_model=User)
# async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
#     # 'current_user' is available here because of the function dependency
#     return current_user