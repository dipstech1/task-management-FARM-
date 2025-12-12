from pydantic import BaseModel, Field
from typing import List

#: name, description, created_by, members

class ProjectSchema(BaseModel):
    name : str = Field(..., description="Project name")
    description:str = Field(default='')
    created_by : str = Field(..., description='Id of creator')
    members : List[str] = Field(..., description='List of members id')