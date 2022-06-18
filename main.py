from fastapi import FastAPI, Path, Query
from enum import Enum

app = FastAPI()


class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"


class UsersFormat(str, Enum):
    SHORT = "short"
    FULL = "full"

@app.get("/")
async def hello_world():
    return {"hello": "world"}


@app.get("/users/{user_type}/{id_user}")
async def get_user_by_type(user_type: UserType, id_user: int):
    return {"id": id_user, "type": user_type}


@app.get("/users/{id_user}")
async def get_user_by_id(id_user: int = Path(..., ge=1)):
    return {"id": id_user}


@app.get("/license-plates/{lic}")
async def get_license_plate(lic: str = Path(..., min_length=9, max_length=9,
                                            regex=r"^\w{2}-\d{3}-\w{2}$")):
    return {"license": lic}


@app.get("/users-pages")
async def get_users(page: int = Query(1, gt=0), size: int = Query(10, le=100)):
    return {"page": page, "size": size}


@app.get("/all-users")
async def get_all_user(user_format: UsersFormat):
    return {"format": user_format}
