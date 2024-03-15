from fastapi import APIRouter

from database import db_first_router_function

router = APIRouter()


@router.get('/lol')
def some_func():
    db_first_router_function()
    return {'key': 'value'}