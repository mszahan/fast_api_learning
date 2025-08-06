from app.db_connection import mongo_client

# the last part afater . is database name
database = mongo_client.beat_streaming


def mongo_database():
    return database
