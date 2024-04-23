from fastapi import APIRouter, status, Body
from .models import SuccessResponseModel, ErrorResponseModel
from .schemas import Signup
from .service import create_user

router = APIRouter()


@router.post(
    "/signup",
    response_description="User signup",
    response_model=SuccessResponseModel | ErrorResponseModel,
    response_model_by_alias=False,
    status_code=status.HTTP_201_CREATED
)
async def signup(signup_form: Signup = Body(...)):
    """
       Create a new user record.
    """
    result = await create_user(signup_form)
    return result
