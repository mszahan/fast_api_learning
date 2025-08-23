from datetime import date
from pydantic import BaseModel, field_validator, ValidationError


class Person(BaseModel):
    first_name: str
    last_name: str
    birthdate: date

    @field_validator('birthdate')
    def valid_birthdate(cls, v: date):
        delta = date.today() - v
        age = delta.days / 365
        if age > 120:
            raise ValueError('You seem a bit too old')
        return v


try:
    Person(first_name='John', last_name='Doe', birthdate='1990-01-01')
    print('valid date of birth and other info')
except ValidationError as e:
    print(str(e))
