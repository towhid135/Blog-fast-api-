from .schemas import Blog
from pydantic import BaseModel


class SuccessResponseModel(BaseModel):
    status: bool
    data: Blog


class ErrorResponseModel(BaseModel):
    status: bool
    status_code: int | str
    message: str
