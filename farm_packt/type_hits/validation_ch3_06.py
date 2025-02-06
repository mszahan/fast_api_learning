from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str


user = User.model_validate({
    'id':1,
    'username':'john',
    'email':'john@email.com',
    'password':'strongpassword'
})

print(user)
print(user.id)