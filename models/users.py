import config
from sqlalchemy_utils.types.encrypted.encrypted_type import StringEncryptedType

from components.db_common import get_db
from models.genres import GenresAssociationTable
from models.roles import RoleModel

db = get_db()


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)

    username = db.Column(db.TEXT, unique=True, nullable=False)
    email = db.Column(db.TEXT, unique=True, nullable=False)
    password = db.Column(StringEncryptedType(db.TEXT, config.DB_ENCRYPTION_KEY), nullable=False)
    role_id = db.Column(db.INTEGER, db.ForeignKey('roles.id'), nullable=False)

    role = db.relationship('RoleModel')
    genres = db.relationship('GenreModel', secondary='genres_associations', lazy='subquery')
