from fastapi import APIRouter
from database import db_second_router_function

second_router = APIRouter()


@second_router.get('/kek')
def some_func():
    db_second_router_function()
    return {'key': 'value'}