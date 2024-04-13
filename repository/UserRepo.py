from fastapi import HTTPException

import constants
from components.db_common import db_commit
from components.logger import logger
from models.db_manager import session
from models.genres import GenreModel
from models.roles import RoleModel
from models.users import UserModel


class UserRepo:
    @staticmethod
    def _get_role_by_name(role_name):
        return session.query(RoleModel).filter_by(name=role_name).one_or_none()

    @staticmethod
    def _get_genre_by_name(genre_name):
        return session.query(GenreModel).filter_by(name=genre_name).one_or_none()

    @staticmethod
    def get_user_by_username(username):
        return session.query(UserModel).filter_by(username=username).one_or_none()

    @staticmethod
    def get_user_by_username_and_password(username, password):
        return session.query(UserModel).filter_by(username=username, password=password).one_or_none()

    @classmethod
    def add_genres_to_user(cls, user: UserModel, genres: list) -> None:
        for genre in genres:
            genre_instance = cls._get_genre_by_name(genre)
            if genre_instance:
                user.genres.append(genre_instance)
            else:
                logger.info(f'Genre not found {genre}, skipping...')
        db_commit()

    @classmethod
    def add_user(cls, username, password, email, role_name, genres):
        role = cls._get_role_by_name(role_name)
        if not role:
            raise HTTPException(status_code=400, detail='Role not found')
        if role.name == constants.ADMIN_USER_ROLE:
            raise HTTPException(status_code=400, detail='Cannot add admin user')
        try:
            user = UserModel(username=username, password=password, email=email, role_id=role.id)
            session.add(user)
            db_commit()
        except Exception as e:
            raise HTTPException(status_code=400, detail='Wrong user data')
        if genres:
            cls.add_genres_to_user(user, genres)
        return user

    @classmethod
    def update_user(cls, username: str, password: str, role_name: str, genres, user: UserModel):
        user_to_update = cls.get_user_by_username(username)
        if user.role.name == constants.ADMIN_USER_ROLE:
            for genre in genres:
                user_to_update.genres.append(cls._get_genre_by_name(genre))
        if user.role.name == constants.ADMIN_USER_ROLE and user.username != username:
            if password:
                user_to_update.password = password
            if role_name:
                role = cls._get_role_by_name(role_name)
                user_to_update.role.id = role.id
        elif user.username == user_to_update.username:
            if password:
                user_to_update.password = password
        db_commit()
        return user_to_update

    @classmethod
    def delete_user(cls, username, user):
        if user.username == username:
            raise HTTPException(status_code=400, detail='User cannot delete himself')
        user_to_delete = cls.get_user_by_username(username)
        if not user_to_delete:
            raise HTTPException(status_code=400, detail='User not found')
        if user_to_delete.role.name == constants.ADMIN_USER_ROLE:
            raise HTTPException(status_code=400, detail='Cannot delete admin user')
        if user_to_delete:
            session.delete(user_to_delete)
        db_commit()
