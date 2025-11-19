from dataclasses import dataclass

from beanie import PydanticObjectId
from app.models.user_model import UserModel
from app.models.collection import COLLECTION

@dataclass
class UserDAL:
    collection = COLLECTION.USER_COLLECTION

    async def add_user(self,user_data : UserModel ):
        new_user = await user_data.save()
        return new_user

    async def get_user_details(self, email:str):
        data:UserModel | None = await UserModel.find_one(UserModel.email == email )
        return data
    
    async def get_user_by_id(self, id:PydanticObjectId):
        print("DOC IDDDDDDDD ", id)
        data : UserModel | None = await UserModel.get(id)
        return data