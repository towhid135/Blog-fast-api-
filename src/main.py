import os
from fastapi import FastAPI
from user.blogs.router import router as blogs_router
from authentication.router import router as auth_router
import uvicorn

app = FastAPI()

app.include_router(auth_router)
app.include_router(blogs_router, prefix="/user")

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=3000, reload=True)
