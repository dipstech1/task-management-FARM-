from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from beanie import init_beanie

from app.models import user_model
from app.core.config import settings

models = [user_model.UserModel]

client: AsyncIOMotorClient | None = None
database = None

class Database:
    client: AsyncIOMotorClient | None = None
    db: AsyncIOMotorDatabase | None = None

db_instance = Database()

async def init_mongodb():
    # Create Motor client

    db_instance.client = AsyncIOMotorClient("mongodb://localhost:27017")

    # Choose database
    db_instance.db = db_instance.client[settings.DB_NAME]
    try:
        await init_beanie(database=db_instance.db, document_models=models)  # type: ignore
        print("Connected to MongoDB!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")


async def close_mongo_connection():
    """Closes the MongoDB connection pool during application shutdown."""
    if db_instance.client:
        db_instance.client.close()
        print("MongoDB connection closed.")