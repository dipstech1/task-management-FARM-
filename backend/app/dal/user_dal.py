from dataclasses import dataclass
from app.models.user_model import UserModel
from app.models.collection import COLLECTION

@dataclass
class UserDAL:
    collection = COLLECTION.USER_COLLECTION

    async def add_user(self,user_data : UserModel ):
        new_user = await user_data.save()
        return new_user