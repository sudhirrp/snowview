import graphene
from fastapi import FastAPI

from custom_graphql import CustomGraphQLApp
from db_conf import db_session
from mutations import PostMutations
from queries import Query

db = db_session.session_factory()

app = FastAPI()


app.add_route("/graphql", CustomGraphQLApp(schema=graphene.Schema(query=Query, mutation=PostMutations)))
