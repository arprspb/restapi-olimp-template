from uvicorn import run
from fastapi import FastAPI
from routers import *

app = FastAPI()


app.include_router(first_router)
app.include_router(second_router)

if __name__ == '__main__':
    run('main:app', host='0.0.0.0', port=8000, reload=True)