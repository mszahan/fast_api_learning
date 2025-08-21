from datetime import datetime
import time
from pydantic import BaseModel


class UserProfile(BaseModel):
    nickname: str
    location: str | None = None
    subscribed: bool = True


class Model(BaseModel):
    # Don't do this.
    # this is example shos why it doesn't work
    d: datetime = datetime.now()


o1 = Model()
print(o1.d)

time.sleep(1)

o2 = Model()
print(o2.d)
