from fastapi import FastAPI, Path
from enum import Enum

app = FastAPI()


class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"


@app.get("/")
async def hello_world():
    return {"hello": "world"}


@app.get("/users/{user_type}/{id_user}")
async def get_user_by_type(user_type: UserType, id_user: int):
    return {"id": id_user, "type": user_type}


@app.get("/users/{id_user}")
async def get_user(id_user: int = Path(..., ge=1)):
    return {"id": id_user}


@app.get("/license-plates/{lic}")
async def get_license_plate(lic: str = Path(..., min_length=9, max_length=9,
                                            regex=r"^\w{2}-\d{3}-\w{2}$")):
    return {"license": lic}


@app.get("/users")
async def get_user(page: int = 1, size: int = 10):
    return {"page": page, "size": size}