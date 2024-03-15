from fastapi import APIRouter
from database import db_second_router_function

router = APIRouter()


@router.get('/kek')
def some_func():
    db_second_router_function()
    return {'key': 'value'}