from fastapi import APIRouter, Depends, HTTPException, Body, BackgroundTasks
from fastapi.responses import JSONResponse

from authentication import AuthHandler
from models import CurrentUser, LoginUser, RegisterUser, User

from background import delayed_task


auth_handler = AuthHandler()
router = APIRouter()


@router.post('/register', response_description='Register user', response_model=CurrentUser)
async def register(newUser: RegisterUser = Body(...), response_model=User):
    newUser.password = auth_handler.get_password_hash(newUser.password)
    query = {"$or": [
        {"username": newUser.username},
        {"email": newUser.email}

    ]}
    existing_user = await User.find_one(query)
    if existing_user is not None:
        raise HTTPException(
            status_code=409, detail='username or password already exists')
    user = await User(**newUser.model_dump()).save()
    return user


@router.post('/login', response_description='Login user and return token')
async def login(bacground_tasks: BackgroundTasks, loginUser: LoginUser = Body(...)):
    user = await User.find_one(User.username == loginUser.username)
    if user and auth_handler.verify_password(loginUser.password, user.password):
        token = auth_handler.encode_token(str(user.id), user.username)
        bacground_tasks.add_task(delayed_task, user.username)
        return JSONResponse(content={"token": token, 'username': user.username})
    raise HTTPException(status_code=401, detail='Invalid username or password')


@router.get('/me', response_description='Logged in user data', response_model=CurrentUser)
async def me(user_data=Depends(auth_handler.auth_wrapper)):
    current_user = await User.get(user_data['user_id'])
    return current_user
