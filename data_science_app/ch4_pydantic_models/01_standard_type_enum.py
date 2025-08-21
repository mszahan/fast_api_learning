from datetime import date
from enum import Enum

from pydantic import BaseModel, ValidationError


class Gender(str, Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    NON_BINARY = 'Non Binary'


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: list[str]


# invalid gender
try:
    Person(
        first_name='John',
        last_name='Snow',
        gender='Invalid value',
        birthdate='1996-12-31',
        interests=['travel', 'coding']
    )
except ValidationError as e:
    print(str(e))
