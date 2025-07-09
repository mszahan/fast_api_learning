from bson import ObjectId
from fastapi import APIRouter, Body, Depends, HTTPException, Request, Response
from fastapi.responses import JSONResponse

from authentication import AuthHandler
from models import UserModel, LoginModel, CurrentUserModel

router = APIRouter()
auth_handler = AuthHandler()


@router.post('/register', response_description='Register new user')
async def register(request: Request, new_user: LoginModel = Body(...)) -> UserModel:
    users = request.app.db['users']

    # hash the password before inserting to mongodb
    new_user.password = auth_handler.get_password_hash(new_user.password)
    new_user = new_user.model_dump()
    if (existing_user := await users.find_one({'username': new_user['username']})) is not None:
        raise HTTPException(status_code=409, detail='Username is taken')
    new_user = await users.insert_one(new_user)
    created_user = await users.find_one({'_id': new_user.inserted_id})
    return created_user


@router.post('/login', response_description='Login user')
async def login(request: Request, login_user: LoginModel = Body(...)):
    users = request.app.db['users']
    user = await users.find_one({'username': login_user.username})
    if (user is None) or (not auth_handler.verify_password(login_user.password, user['password'])):
        raise HTTPException(
            status_code=401, detail='Invalid username or password')
    token = auth_handler.encode_token(str(user['_id']), user['username'])
    response = JSONResponse({'token': token, 'username': user['username']})
    return response


@router.get('/me', response_description='Get current user', response_model=CurrentUserModel)
async def me(request: Request, response: Response, user_data=Depends(auth_handler.auth_wrapper)):
    users = request.app.db['users']
    current_user = await users.find_one({'_id': ObjectId(user_data['user_id'])})
    return current_user
