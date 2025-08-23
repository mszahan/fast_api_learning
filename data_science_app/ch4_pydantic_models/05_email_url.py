from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError


class User(BaseModel):
    email: EmailStr
    website: HttpUrl


user = User(email='jdoe@example.com', website='https://www.example.com')
print(user)
