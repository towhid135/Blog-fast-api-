from fastapi import APIRouter, Body, status
from .schemas import Blog
from .models import SuccessResponseModel, ErrorResponseModel
from .service import save_blog_on_db, search_blog_with_id

router = APIRouter()


@router.post(
    "/blogs",
    response_description="Add new blog",
    response_model=SuccessResponseModel | ErrorResponseModel,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False
)
async def create_blog(blog: Blog = Body(...)):
    """
       Insert a new blog record.
       A unique `id` will be created and provided in the response.
    """
    result = await save_blog_on_db(blog)
    return result


@router.get("/blogs/{blog_id}")
async def get_blog(blog_id: int) -> Blog:
    return search_blog_with_id(blog_id)
