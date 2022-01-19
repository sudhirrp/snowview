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
