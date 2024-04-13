from fastapi import Request

import constants
from components.fast_api import app, GetGamesFilters, UpdateGame
from components.jwt_helpers import JWT
from repository.GamesRepo import GamesRepo


@app.get("/games/")
@JWT.validate_token_and_role(roles=[constants.ADMIN_USER_ROLE])
async def get_games(request: Request, filters: GetGamesFilters):
    return GamesRepo.get_games(filters)


@app.put("/games/{title}")
@JWT.validate_token_and_role(roles=[constants.ADMIN_USER_ROLE])
async def update_games(request: Request, title, update_data: UpdateGame):
    GamesRepo.update_game(title, update_data.update_data)


@app.get("/games/recommendations/")
@JWT.validate_token_and_role(roles=[constants.ADMIN_USER_ROLE, constants.EDITOR_USER_ROLE])
async def get_recommendations(request: Request, filters: GetGamesFilters):
    user = JWT.get_user_by_request(request)
    return GamesRepo.get_recommendations(user, filters)

