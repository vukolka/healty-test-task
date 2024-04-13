from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Credentials(BaseModel):
    username: str
    password: str


class User(BaseModel):
    username: str
    password: str = None
    email: str
    role: str
    genres: list[str] = None


class UpdateUser(BaseModel):
    username: str
    password: str = None
    email: str = None
    role: str = None
    genres: list[str] = []


class GenreList(BaseModel):
    genres: list[str]


class YearsFilter(BaseModel):
    start: str = None
    end: str = None


class GetGamesFilters(BaseModel):
    genres: list[str] = []
    years: YearsFilter = None
    devs: list[str] = []
    rating: str = None


class UpdateGame(BaseModel):
    update_data: dict[str, str]
