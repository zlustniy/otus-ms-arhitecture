from __future__ import annotations

from alembic import context
from sqlalchemy import MetaData, create_engine, pool

from otus_service import constants
from otus_service.models.meta import (
    METADATA,
)


def include_object(object, name, type_, reflected, compare_to):
    if type_ == "table" and object.schema != constants.DB_SCHEMA:
        return False
    else:
        return True


def run_migrations_offline(meta_object, dbms_url):
    # type: (MetaData, DbUrlText) -> None
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context_kwargs = {}

    context.configure(
        url=dbms_url,
        target_metadata=meta_object,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_schemas=True,
        include_object=include_object,
        **context_kwargs
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online(meta_object, dbms_url):
    # type: (MetaData, DbUrlText) -> None
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_engine(dbms_url, poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context_kwargs = {}

        if constants.DB_SCHEMA:
            context_kwargs['version_table_schema'] = constants.DB_SCHEMA

        context.configure(
            connection=connection,
            target_metadata=meta_object,
            include_schemas=True,
            include_object=include_object,
            **context_kwargs
        )

        with context.begin_transaction():
            context.run_migrations()


def run_migrations(meta_object):
    # type: (MetaData) -> None
    dbms_url = constants.MIGRATION_DATABASE_URI
    if context.is_offline_mode():
        run_migrations_offline(meta_object, dbms_url)
    else:
        run_migrations_online(meta_object, dbms_url)


run_migrations(METADATA)
