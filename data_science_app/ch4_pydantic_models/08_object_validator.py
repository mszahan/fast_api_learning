from pydantic import BaseModel, EmailStr, ValidationError, model_validator


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str

    @model_validator(mode='after')
    def passwords_match(self):
        if self.password != self.password_confirmation:
            raise ValueError('Password do not match')
        return self


try:
    UserRegistration(email='hola@hola.com', password='password',
                     password_confirmation='password')
    print('Password mathed and valid email address')
except ValidationError as e:
    print(str(e))
