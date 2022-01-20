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


class Tables(Base):
    __tablename__ = "TABLES"

    # row_id = Column(String, primary_key=True, server_default=text("uuid.uuid4()"))
    table_catalog = Column(String)
    table_schema = Column(String)
    table_name = Column(String)
    table_owner = Column(String)
    table_type = Column(String)
    is_transient = Column(String)
    clustering_key = Column(String)
    row_count = Column(Numeric(38, 0, 0, False))
    bytes = Column(Numeric(38, 0, 0, False))
    retention_time = Column(Numeric(9, 0, 0, False))
    self_referencing_column_name = Column(String)
    reference_generation = Column(String)
    user_defined_type_catalog = Column(String)
    user_defined_type_schema = Column(String)
    user_defined_type_name = Column(String)
    is_insertable_into = Column(String)
    is_typed = Column(String)
    commit_action = Column(String)
    created = Column(TIMESTAMP(timezone=True))
    last_altered = Column(TIMESTAMP(timezone=True))
    auto_clustering_on = Column(String)
    comment = Column(String)
    PrimaryKeyConstraint(table_schema, table_name, name="tables_pk")


class Views(Base):
    __tablename__ = "VIEWS"

    table_catalog = Column(String)
    table_schema = Column(String)
    table_name = Column(String)
    table_owner = Column(String)
    view_definition = Column(String)
    check_option = Column(String)
    is_updatable = Column(String)
    insertable_into = Column(String)
    is_secure = Column(String)
    created = Column(TIMESTAMP(timezone=True))
    last_altered = Column(TIMESTAMP(timezone=True))
    comment = Column(String)
    PrimaryKeyConstraint(table_schema, table_name, name="views_pk")
