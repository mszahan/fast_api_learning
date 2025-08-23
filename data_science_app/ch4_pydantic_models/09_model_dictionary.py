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

    def name_dict(self):
        return self.model_dump(include={'first_name', 'last_name'})


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
person_dict = person.model_dump()
print(person_dict['first_name'])
print(person_dict['address']['street_address'])

person_include = person.model_dump(include={'first_name', })
print(person_include)

person_exclude = person.model_dump(
    exclude={'first_name': True, 'address': {'country': True}})
# person_exclude = person.model_dump(
#     exclude={'first_name':..., 'address': {'country'}})
print(person_exclude)
