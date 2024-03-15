from uvicorn import run
from fastapi import FastAPI

from routers.first_router import first_router
from routers.second_router import second_router

app = FastAPI()


app.include_router(first_router)
app.include_router(second_router)

if __name__ == '__main__':
    run('main:app', host='0.0.0.0', port=8000, reload=True)