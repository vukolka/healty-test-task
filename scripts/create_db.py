from components.db_common import db_commit
from models.db_manager import metadata, session
from models import roles
from models import genres
from models import users

metadata.create_all()
from models.users import UserModel
from models.roles import RoleModel
from models.genres import GenreModel
session.add(RoleModel(name='admin'))
session.add(RoleModel(name='editor'))
session.add(GenreModel(name='Adventure'))
session.add(GenreModel(name='RPG'))
session.add(UserModel(
    username='admin',
    email='vukolov.kolya@gmail.com',
    password='supersecretpassword',
    role_id=1
))
db_commit()