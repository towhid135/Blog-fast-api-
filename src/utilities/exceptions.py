from fastapi import HTTPException,status


def data_not_found(details: str):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=details)


def data_already_exists(details: str):
    return HTTPException(status_code=status.HTTP_409_CONFLICT,detail=details)