from sqlalchemy import Column, Integer, String

from service_a.db.database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String, index=True)
