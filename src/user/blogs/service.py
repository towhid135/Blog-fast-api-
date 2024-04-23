from .schemas import Blog
from .models import SuccessResponseModel, ErrorResponseModel
from fastapi import HTTPException
from utilities.db import blog_collection
from utilities.datetime_function import create_timestamps


async def save_blog_on_db(blog: Blog) -> SuccessResponseModel | ErrorResponseModel:
    try:
        blog.created_at = create_timestamps()
        await blog_collection.insert_one(
            blog.model_dump(by_alias=True, exclude=["id"])
        )
        success_response_object = SuccessResponseModel(
            status=True,
            data=blog
        )
        return success_response_object
    except HTTPException as e:
        error_object = ErrorResponseModel(
            status=False,
            status_code=e.status_code,
            message=e.detail
        )
        return error_object


def search_blog_with_id(blog_id: int):
    return {"id": 12, "name": "towhid"}
