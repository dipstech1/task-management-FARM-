from beanie import PydanticObjectId
from app.dal.user_dal import UserDAL
from app.core.error_handler.custom_errors import UserNotFoundException
from app.schemas.user_schema import UserDetailSchema
class UserService:

    def __init__(self) -> None:
        self.userDAL = UserDAL()

    async def get_user_details(self,user_id:PydanticObjectId | None):

        if not user_id:
            raise UserNotFoundException()
        
        response = await self.userDAL.get_user_by_id(user_id)
        if response:
            user_data = response.model_dump(exclude={'password'})
            return UserDetailSchema(**user_data)
        else:
            return {
                "data" : "No user found"
            }