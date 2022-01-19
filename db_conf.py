import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.dialects import registry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# registry.register("snowflake", "snowflake.sqlalchemy", "dialect")
registry.register("snowflake", "snowflake.sqlalchemy", "dialect")

load_dotenv(".env")

SF_DB_URL = f'{os.environ["DATABASE_URL"]}'.format(
    SF_USER=f'{os.environ["SF_USER"]}',
    SF_PASSWORD=f'{os.environ["SF_PASSWORD"]}',
    SF_ACCOUNT=f'{os.environ["SF_ACCOUNT"]}',
    SF_DATABASE=f'{os.environ["SF_DATABASE"]}',
    SF_SCHEMA=f'{os.environ["SF_SCHEMA"]}',
    SF_WAREHOUSE=f'{os.environ["SF_WAREHOUSE"]}',
    SF_ROLE=f'{os.environ["SF_ROLE"]}',
)


SQLALCHEMY_DATABASE_URL = SF_DB_URL
print(f"SQLALCHEMY_DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
