from fastapi import APIRouter

from database import db_first_router_function

first_router = APIRouter()


@first_router.get('/lol')
def some_func():
    db_first_router_function()
    return {'key': 'value'}