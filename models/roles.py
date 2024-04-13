from components.db_common import get_db

db = get_db()


class RoleModel(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.TEXT, nullable=False)
