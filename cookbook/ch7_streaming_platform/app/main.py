from contextlib import asynccontextmanager
from bson import ObjectId
from pydantic import BaseModel

from fastapi import FastAPI, Body, Depends, HTTPException, status
from fastapi.encoders import ENCODERS_BY_TYPE
from app.db_connection import ping_mongo_db_server
from app.database import mongo_database


ENCODERS_BY_TYPE[ObjectId] = str


@asynccontextmanager
async def lifespan(app: FastAPI):
    await ping_mongo_db_server()
    yield


app = FastAPI(lifespan=lifespan)


class Playlist(BaseModel):
    name: str
    songs: list[str] = []


@app.post('/songs')
async def add_song(
    song: dict = Body(
        example={
            'title': 'My song',
            'artist': 'The greate artist',
            'genre': 'favorite genre',
        },
    ),
    db=Depends(mongo_database)
):
    await db.songs.insert_one(song)
    return {'message': 'Song added successfully', 'id': song['_id']}


@app.get('/songs')
async def get_songs(db=Depends(mongo_database)):
    songs = await db.songs.find().to_list()
    return songs


@app.get('/song/{song_id}')
async def get_song(song_id: str, db=Depends(mongo_database)):
    song = await db.songs.find_one({
        '_id': ObjectId(song_id)
        if ObjectId.is_valid(song_id)
        else None
    })
    if not song:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Song not found'
        )
    return song


@app.put('/song/{song_id}')
async def update_song(song_id: str, updated_song: dict, db=Depends(mongo_database)):
    result = await db.songs.update_one(
        {
            '_id': ObjectId(song_id)
            if ObjectId.is_valid(song_id)
            else None
        },
        {
            '$set': updated_song
        }
    )
    if result.modified_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Song not found'
        )
    return {'message': 'Song updated successfully'}


@app.delete('/song/{song_id}')
async def delete_song(song_id: str, db=Depends(mongo_database)):
    result = await db.songs.delete_one(
        {
            '_id': ObjectId(song_id)
            if ObjectId.is_valid(song_id)
            else None
        }
    )
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Song not found'
        )
    return {'message': 'Song deleted successfully'}


@app.post('/playlist')
async def create_playlist(
    playlist: Playlist = Body(
        example={
            'name': 'My playlist',
            'songs': ['song_id',],
        }
    ),
    db=Depends(mongo_database)
):
    result = await db.playlists.insert_one(playlist.model_dump())
    return {'message': 'Playlist created successfully', 'id': str(result.inserted_id)}


@app.get('/playlist/{playlist_id}')
async def get_playlist(playlist_id: str, db=Depends(mongo_database)):
    playlist = await db.playlists.find_one(
        {
            '_id': ObjectId(playlist_id)
            if ObjectId.is_valid(playlist_id)
            else None
        }
    )
    if not playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Playlist not found'
        )
    songs = await db.songs.find({
        '_id': {
            '$in': [ObjectId(song_id) for song_id in playlist['songs']]
        }
    }).to_list(None)
    return {
        'name': playlist['name'],
        'songs': songs
    }
