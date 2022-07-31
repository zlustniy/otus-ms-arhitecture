import json
import os

from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from otus_service import constants
from otus_service.models.db_user import User as UserORM

app = FastAPI()

config = {
    'DATABASE_URI': constants.DATABASE_URI,
    'MIGRATION_DATABASE_URI': constants.MIGRATION_DATABASE_URI,
    'HOSTNAME': os.environ.get('HOSTNAME', ''),
    'GREETING': os.environ.get('GREETING', 'Hello'),
}


@app.get("/health/")
async def health():
    return {"status": "OK"}


@app.get("/config/")
async def configuration():
    return json.dumps(config)


engine = create_engine(
    constants.DATABASE_URI,
)

session_cls = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


async def get_db():
    session = session_cls()
    try:
        yield session
        session.commit()
    finally:
        session.close()


class UserCreate(BaseModel):
    username: str
    firstName: str
    lastName: str
    email: str
    phone: str


class User(UserCreate):
    id: int

    class Config:
        orm_mode = True


router = SQLAlchemyCRUDRouter(
    schema=User,
    create_schema=UserCreate,
    db_model=UserORM,
    db=get_db,
    prefix='user'
)
app.include_router(router)
