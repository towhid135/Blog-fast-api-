from pydantic import BaseModel
from .schemas import Signup


class SuccessResponseModel(BaseModel):
    status: bool
    data: Signup


class ErrorResponseModel(BaseModel):
    status: bool
    status_code: int | str
    message: str
