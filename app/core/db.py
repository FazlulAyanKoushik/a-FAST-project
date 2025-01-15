from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = None


async def init_db():
    global client
    client = AsyncIOMotorClient(settings.MONGO_URI)


def get_db():
    return client[settings.MONGO_DB]
