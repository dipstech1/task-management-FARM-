from pydantic import BaseModel,Field
from typing import Any

class BaseResponseSchema(BaseModel):
    data : Any | None = Field(default=None)
    success : bool = Field(default=False)
