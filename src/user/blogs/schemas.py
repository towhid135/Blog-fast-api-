from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from utilities.py_object_id import PyObjectId

class Blog(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    background_image: str = Field(...)
    title: str = Field(...)
    description: str = Field(...)
    created_at: datetime = datetime.now()
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )
