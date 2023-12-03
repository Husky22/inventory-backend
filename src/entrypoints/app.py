from fastapi import FastAPI
from .item import item_router
from ..db_setup import create_db

create_db()

app = FastAPI()


app.include_router(item_router)

