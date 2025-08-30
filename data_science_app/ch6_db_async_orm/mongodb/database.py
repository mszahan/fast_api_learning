from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

# connection to the whole server
motor_client = AsyncIOMotorClient('mongodb://192.168.0.244:27017')

# single database whole server
database = motor_client['datascience']


def get_database() -> AsyncIOMotorDatabase:
    return database
