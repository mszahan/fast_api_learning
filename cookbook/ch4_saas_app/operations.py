from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def add_user(session: Session,
             username: str,
             email: str,
             password: str) -> User | None:
    hashed_password = pwd_context.hash(password)
    db_user = User(username=username,
                   email=email,
                   hashed_password=hashed_password)
    session.add(db_user)
    try:
        session.commit()
        session.refresh(db_user)
    except IntegrityError:
        session.rollback()
        return
    return db_user
