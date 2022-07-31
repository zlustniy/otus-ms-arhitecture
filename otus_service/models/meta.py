from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

from otus_service import constants

__all__ = (
    'METADATA',
    'Base',
)

METADATA = MetaData(schema=constants.DB_SCHEMA)
""" Контейнер для декларирования ОРМ моделей """

Base = declarative_base(metadata=METADATA)
