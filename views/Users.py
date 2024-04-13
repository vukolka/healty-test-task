from fastapi import Request, HTTPException

import constants
from components.fast_api import app, User, UpdateUser
from components.jwt_helpers import JWT
from repository.UserRepo import UserRepo


@app.get("/user/")
@JWT.validate_token_and_role(roles=[constants.ADMIN_USER_ROLE])
async def get_user(request: Request, username: str):
    user = UserRepo.get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/user/")
@JWT.validate_token_and_role(roles=[constants.ADMIN_USER_ROLE, constants.EDITOR_USER_ROLE])
async def update_user(request: Request, user: UpdateUser):
    return UserRepo.update_user(user.username, user.password, user.role, user.genres, JWT.get_user_by_request(request))


@app.post("/user/")
@JWT.validate_token_and_role(roles=[constants.ADMIN_USER_ROLE])
async def create_user(request: Request, user: User):
    return UserRepo.add_user(user.username, user.password, user.email, user.role, user.genres)


@app.delete("/user/")
@JWT.validate_token_and_role(roles=[constants.ADMIN_USER_ROLE])
async def delete_user(request: Request, username: str):
    user = JWT.get_user_by_request(request)
    UserRepo.delete_user(username, user)
    return {"message": "User deleted"}
