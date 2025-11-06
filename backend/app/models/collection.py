from dataclasses import dataclass
from typing import List,ClassVar


@dataclass
class CollectionData:
    USER_COLLECTION = "users"
    PROJECT_COLLECTION = "projects"
    TASK_COLLECTION = "tasks"

    MODEL_COLLECTION:ClassVar[List] = []

    @staticmethod
    def add_model(model):
        if model not in CollectionData.MODEL_COLLECTION:
            CollectionData.MODEL_COLLECTION.append(model)

    def get_all_collections(self) -> List[str] :
        return CollectionData.MODEL_COLLECTION

COLLECTION = CollectionData() 