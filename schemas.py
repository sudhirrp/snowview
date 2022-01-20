from itertools import count

from graphene_sqlalchemy import SQLAlchemyObjectType
from pydantic import BaseModel

from models import Board, Post, Tables, Views


class PostSchema(BaseModel):
    title: str
    content: str


class PostModel(SQLAlchemyObjectType):
    class Meta:
        model = Post


class BoardSchema(BaseModel):
    tenant_id: str
    tenant_name: str
    city: str
    zip: int


class BoardModel(SQLAlchemyObjectType):
    class Meta:
        model = Board


class ViewsSchema(BaseModel):
    table_catalog = str
    table_schema = str
    table_name = str
    table_owner = str
    view_definition = str
    check_option = str
    is_updatable = str
    insertable_into = str
    is_secure = str
    created = str
    last_altered = str
    comment = str


class ViewsModel(SQLAlchemyObjectType):
    class Meta:
        model = Views


class TablesSchema(BaseModel):
    table_catalog = str
    table_schema = str
    table_name = str
    table_owner = str
    table_type = str
    is_transient = str
    clustering_key = str
    row_count = str
    bytes = str
    retention_time = str
    self_referencing_column_name = str
    reference_generation = str
    user_defined_type_catalog = str
    user_defined_type_schema = str
    user_defined_type_name = str
    is_insertable_into = str
    is_typed = str
    commit_action = str
    created = str
    last_altered = str
    auto_clustering_on = str
    comment = str


class TablesModel(SQLAlchemyObjectType):
    class Meta:
        model = Tables
