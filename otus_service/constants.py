import os

from dotenv import load_dotenv

load_dotenv()

DB_SCHEMA = None
DATABASE_URI = os.environ['DATABASE_URI']
MIGRATION_DATABASE_URI = DATABASE_URI.replace('postgresql+asyncpg', 'postgresql')
