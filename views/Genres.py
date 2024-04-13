from fastapi import Request

import constants
from components.fast_api import app, GenreList
from components.jwt_helpers import JWT
from repository.GenreRepo import GenreRepo


@app.post("/genres/")
@JWT.validate_token_and_role(roles=[constants.ADMIN_USER_ROLE, constants.EDITOR_USER_ROLE])
async def add_genrges(request: Request, genres: GenreList):
    GenreRepo.add_genres(genres.genres)
    return {'message': 'Genres added'}


@app.delete("/genres/")
@JWT.validate_token_and_role(roles=[constants.ADMIN_USER_ROLE, constants.EDITOR_USER_ROLE])
async def remove_genres(request: Request, genres: GenreList):
    GenreRepo.remove_genres(genres.genres)
    return {"message": "Genres removed"}


@app.get("/genres/")
@JWT.validate_token_and_role(roles=[constants.ADMIN_USER_ROLE, constants.EDITOR_USER_ROLE])
async def get_genres(request: Request):
    return GenreRepo.get_genres()
