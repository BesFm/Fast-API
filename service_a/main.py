from fastapi import FastAPI

from service_a.controllers import controller_users
from service_a.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=controller_users.controller)
