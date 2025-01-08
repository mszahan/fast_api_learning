from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    dob: datetime

pu = User(id=1, username='mszahan', email='mszahan@email.com', dob=(1996, 6, 28))

## you can provide default and nullable data
class AnotherUser(BaseModel):
    id: int = 2
    username: str
    email: str
    dob: datetime
    fav_colors: list[str] | None = ['red', 'blue']