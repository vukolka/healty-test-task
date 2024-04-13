from fastapi import HTTPException

from components.db_common import db_commit
from components.logger import logger
from models.db_manager import session
from models.genres import GenreModel


class GenreRepo:
    @staticmethod
    def add_genre(genre):
        try:
            session.add(GenreModel(name=genre))
            db_commit()
        except Exception:
            raise HTTPException(status_code=400, detail='Genre already exists')

    @classmethod
    def add_genres(cls, genres):
        for genre in genres:
            try:
                cls.add_genre(genre)
            except Exception:
                logger.warning('Genre already exists, skipping...')

    @classmethod
    def remove_genres(cls, genres):
        session.query(GenreModel).filter(GenreModel.name.in_(genres)).delete()

    @staticmethod
    def get_genres():
        return session.query(GenreModel).all()