from motor.motor_asyncio import AsyncIOMotorClient
# from elasticsearch import AsyncElasticsearch, TransportError
import logging

mongo_client = AsyncIOMotorClient(
    'mongodb://192.168.0.244:27017'
)

# es_client = AsyncElasticsearch(
#     hosts='http://192.168.0.244:9200')

logger = logging.getLogger('uvicorn.error')

# to ping the mongodb


async def ping_mongo_db_server():
    try:
        await mongo_client.admin.command('ping')
        logger.info('Connected to MongoDB')
    except Exception as e:
        logger.error(f'Error connecting the MongoDB: {e}')
        raise e


# async def ping_elastisearch():
#     try:
#         await es_client.info()
#         logger.inof('Connected to ElasticSearch')
#     except TransportError as e:
#         logger.error(f'Elasticsearch connection failed: {e}')
#         raise e
