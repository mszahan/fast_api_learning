from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_url: str = Field(default='')
    secret_key: str = Field(default='')

    #this will read api_url and secret key from env file
    class Config:
        env_file = '.env'
    

print(Settings().model_dump())
