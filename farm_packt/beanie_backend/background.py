from time import sleep
import resend
from config import BaseConfig

settings = BaseConfig()


def delayed_task(username: str) -> None:
    sleep(5)
    print(f"Task completed for user: {username}")
