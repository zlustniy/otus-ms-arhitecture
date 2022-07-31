from sqlalchemy import Column, String, Integer

from .meta import Base

__all__ = ['User']


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(128), unique=True, nullable=False)
    firstName = Column(String(128))
    lastName = Column(String(128))
    email = Column(String(128))
    phone = Column(String(12))
