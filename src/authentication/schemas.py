from pydantic import BaseModel, ConfigDict, Field, constr, EmailStr
from datetime import datetime,timezone
from typing import Optional
from utilities.py_object_id import PyObjectId


class Signup(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    first_name: str = constr(strip_whitespace=True, max_length=15)
    last_name: str = constr(strip_whitespace=True, max_length=15)
    email: EmailStr
    password: str = constr(pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
    created_at: datetime
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class Signin(BaseModel):
    email: EmailStr
    password: str = constr(pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')


class Claims(BaseModel):
    iss: str = Field(default="blog_app")
    sub: PyObjectId  # user_id
    exp: datetime
    iat: datetime