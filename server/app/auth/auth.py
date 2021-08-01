from sqlalchemy.orm import Session

from app import crud
from app.auth import password_hashing


def authenticate_user(db: Session, username: str, password: str):
    user = crud.get_user_by_username(db, username)
    if not user:
        return False
    if not password_hashing.verify_password(password, user.hashed_password):
        return False
    return user
