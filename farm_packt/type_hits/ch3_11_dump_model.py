from pydantic import BaseModel, Field, EmailStr

class UserModel(BaseModel):
    id: int = Field()
    username: str = Field(min_length=5, max_length=20)
    email: EmailStr = Field()
    password: str = Field(min_length=5, max_length=20, pattern='^[a-zA-Z0-9]+$')


user = UserModel(id=1, username='freethrow', email='mark@email.com', password='strongpassword')

# dump data as dictionary
print(user.model_dump())

# dump data as json
#password ommit doen't work for some reason
print(user.model_dump_json(exclude=set("password")))

