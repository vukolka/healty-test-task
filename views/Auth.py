from fastapi import HTTPException

from components.fast_api import app, Credentials
from components.jwt_helpers import JWT
from repository.UserRepo import UserRepo


@app.post("/auth/")
def authenticate(credentials: Credentials):
    user = UserRepo.get_user_by_username_and_password(credentials.username, credentials.password)
    if user:
        return {'token': JWT.generate_token(user)}
    else:
        raise HTTPException(status_code=400, detail='Invalid username or password')
