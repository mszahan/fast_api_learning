from motor.motor_asyncio import AsyncIOMotorClient
import logging

mongo_client = AsyncIOMotorClient(
    'mongodb://192.168.0.244:27017'
)

logger = logging.getLogger('uvicorn.error')

# to ping the mongodb


async def ping_mongo_db_server():
    try:
        await mongo_client.admin.command('ping')
        logger.info('Connected to MongoDB')
    except Exception as e:
        logger.error(f'Error connecting the MongoDB: {e}')
        raise e
