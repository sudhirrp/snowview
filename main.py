import graphene
from fastapi import FastAPI

from custom_graphql import CustomGraphQLApp
from db_conf import db_session

db = db_session.session_factory()

app = FastAPI()


app.add_route("/graphql", CustomGraphQLApp(schema=graphene.Schema(query=None, mutation=None)))
