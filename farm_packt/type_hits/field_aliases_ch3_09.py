from pydantic import BaseModel, Field
from typing import Literal

external_api_data = {
    "user_id": 234,
    "name": "Marko",
    "email":"marko@email.com",
    "account_type":"personal",
    "nick": "freethrow",
}

# This updated model provides aliases for all the fields that have different names, so it is possible to 
# validate your external data
class UserModelFields(BaseModel):
    id: int = Field(alias='user_id')
    username: str = Field(alias='name')
    email: str = Field()
    account: Literal['personal', 'business'] | None = Field(default=None, alias='account_type')
    nickname: str | None = Field(default=None, alias='nick')

user = UserModelFields.model_validate(external_api_data)

print(user)