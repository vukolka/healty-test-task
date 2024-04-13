import base64
from datetime import datetime, timezone, timedelta
from functools import wraps

import jwt
from fastapi import Request, HTTPException

import config
from models.db_manager import session
from models.users import UserModel


class JWT:

    @staticmethod
    def generate_token(user: UserModel):
        now = datetime.now(timezone.utc)
        exp = now + timedelta(days=5)
        payload = {
            'username': user.username,
            'role': user.role.name,
            'iat': now.timestamp(),
            'exp': exp.timestamp()
        }
        token = jwt.encode(payload, config.JWT_KEY, algorithm="HS256")
        return base64.b64encode(token.encode())

    @classmethod
    def get_user_by_username(cls, username: str) -> UserModel:
        return session.query(UserModel).filter_by(username=username).one_or_none()

    @classmethod
    def validate_token(cls, token: str):
        try:
            token = base64.b64decode(token)
            return jwt.decode(token, config.JWT_KEY, algorithms=['HS256'])
        except Exception:
            raise HTTPException(status_code=401, detail='Invalid token')

    @classmethod
    def get_user_by_request(cls, request: Request) -> UserModel:
        token = request.headers.get('token')
        claims = cls.validate_token(token)
        return cls.get_user_by_username(claims['username'])

    @classmethod
    def validate_token_and_role(cls, roles):
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, request: Request, **kwargs):
                token = request.headers.get('token')
                claims = cls.validate_token(token)
                if claims['role'] not in roles:
                    raise HTTPException(status_code=401, detail='Invalid user role')
                return await func(*args, request, **kwargs)

            return wrapper
        return decorator
