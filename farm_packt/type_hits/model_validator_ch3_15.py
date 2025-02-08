from pydantic import BaseModel, EmailStr, ValidationError, model_validator
from typing import Any, Self


class UserModelV(BaseModel):
    id: int
    username: str
    email: EmailStr
    password1: str
    password2: str

    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        pw1 = self.password1
        pw2 = self.password2
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        return self
    
    @model_validator(mode='before')
    @classmethod
    def check_private_data(cls, data:Any) -> Any:
        if isinstance(data, dict):
            # the assert method will rais error if the statment is true with the message next to
            # ...it after the comma
            assert (
                'private_data' not in data
            ), 'Private data should not be included'
            return data
        

user_data = {
    'id': 1,
    'username':'john',
    'email':'john@email.com',
    'password1':'strongp',
    'password2':'strongp3',
    'private_data':'secret',
}


try:
    user = UserModelV.model_validate(user_data)
    print(user)
except ValidationError as e:
    print(e)