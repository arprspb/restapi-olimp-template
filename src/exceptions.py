from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

class UserAlreadyExists(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="User already exists",
        )