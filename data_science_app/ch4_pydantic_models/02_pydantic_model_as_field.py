from datetime import date
from enum import Enum
from pydantic import BaseModel


class Gender(str, Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    NON_BINARY = 'Non Binary'


class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: list[str]
    address: Address


person = Person(
    first_name='John',
    last_name='Snow',
    gender=Gender.MALE,
    birthdate='1991-01-01',
    interests=['travel', 'coding'],
    address={
        'street_address': '12 Squirell Street',
        'postal_code': '434343',
        'city': 'Woodtown',
        'country': 'Uk'
    }


)
print(person)
