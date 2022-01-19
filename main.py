from fastapi import FastAPI

from db_conf import db_session

db = db_session.session_factory()

app = FastAPI()
