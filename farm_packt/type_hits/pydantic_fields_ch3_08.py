from typing import Literal
from pydantic import BaseModel, Field


class UserModelFields(BaseModel):
    # the three dots mean the field is reequired (mandatory)
    id: int = Field(...)
    username: str = Field(...)
    email: str = Field(...)
    account: Literal['personal', 'business'] | None = Field(default=None)
    nickname: str | None = Field(default=None)
