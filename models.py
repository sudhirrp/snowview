import uuid
from xmlrpc.client import Boolean

from sqlalchemy import (
    TIMESTAMP,
    Boolean,
    Column,
    DateTime,
    Integer,
    Numeric,
    PrimaryKeyConstraint,
    Sequence,
    String,
    text,
)
from sqlalchemy.sql import func

from db_conf import Base

TABLE_ID = Sequence("table_id_seq", start=1)


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, TABLE_ID, primary_key=True, server_default=TABLE_ID.next_value())
    title = Column(String)
    author = Column(String)
    content = Column(String)
    time_created = Column(TIMESTAMP(timezone=True), server_default=func.timestamp())


class Board(Base):
    __tablename__ = "TENANT_BOARD"

    tenant_id = Column(String, primary_key=True)
    tenant_name = Column(String)
    city = Column(String)
    zip = Column(Integer)
    created_date = Column(TIMESTAMP(timezone=True), server_default=func.timestamp())
    updated_date = Column(TIMESTAMP(timezone=True), server_default=func.timestamp())
