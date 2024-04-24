from fastapi import APIRouter, status, Body
from .models import SuccessResponseModel, ErrorResponseModel
from .schemas import Signup, Signin
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

# @router.get(
#     "/signin",
#     response_description="User signin",
#     response_model= SuccessResponseModel | ErrorResponseModel,
#     response_model_by_alias=False,
#     status_code=status.HTTP_200_OK
# )
# async def Signin(signin_form:Signin):
#     result = get_user(signin_form)
#     return result
