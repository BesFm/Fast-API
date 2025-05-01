from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from service_a.db import crud, models, database
from service_a.schemas import User, UserCreate

controller = APIRouter(
    prefix='/users',
    tags=['Users'],
    responses={404: {'description': 'not_found'}}
)


def get_db() -> None:
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@controller.post('/create', response_model=User)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)) -> models.Users:
    return crud.create_user(db=db, user_data=user_data)


@controller.get('/{user_id}', response_model=User)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user:
        return db_user
    raise HTTPException(404, detail=f'User with id={user_id} not found')


@controller.get('/', response_model=list[User])
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)


@controller.delete('/{user_id}', response_model=User)
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db=db, user_id=user_id)
    crud.delete_user(db=db, user_id=user_id)
    return user
