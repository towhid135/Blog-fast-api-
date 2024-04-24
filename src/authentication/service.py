from fastapi import HTTPException
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
import os
from utilities.db import user_collection
from .schemas import Signup
from .models import SuccessResponseModel, ErrorResponseModel
from utilities import exceptions
from utilities.datetime_function import create_timestamps
from .utils import get_password_hash

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")


async def get_user_by_email(email: str):
    user = await user_collection.find_one({
        "email": email
    })
    if user:
        return user
    else:
        return False


async def create_user(signup_data: Signup) -> SuccessResponseModel | ErrorResponseModel:
    try:
        user = await get_user_by_email(signup_data.email)
        if user:
            raise exceptions.data_already_exists("Already have an account!")
        else:
            pass
            signup_data.created_at = create_timestamps()
            signup_data.password = get_password_hash(signup_data.password)
            user_collection.insert_one(
                signup_data.model_dump(by_alias=True, exclude=["id"])
            )
            success_response_object = SuccessResponseModel(status=True, data=signup_data)
            return success_response_object
    except HTTPException as e:
        error_object = ErrorResponseModel(
            status=False,
            status_code=e.status_code,
            message=e.detail
        )
        return error_object


def create_access_token():
    jwt_payload = {}
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    jwt_payload.update({"exp": expire})
    encoded_jwt = jwt.encode(jwt_payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_jwt(access_token):
    decoded_jwt = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
    return decoded_jwt
