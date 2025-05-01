from sqlalchemy.orm import Session

from service_a.db import models
from service_a.schemas import UserBase


def create_user(db: Session, user_data: UserBase) -> models.Users:
    db_user = models.Users(name=user_data.name, surname=user_data.surname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()


def get_users(db: Session) -> list:
    return db.query(models.Users).all()


def delete_user(db: Session, user_id: int) -> None:
    user = get_user(db=db, user_id=user_id)
    db.delete(user)
    db.commit()

