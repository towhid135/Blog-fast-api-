import os
import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.get_database("BlogDB")

blog_collection = db.get_collection("blogs")
user_collection = db.get_collection("users")
