from components.db_common import get_db

db = get_db()

GenresAssociationTable = db.Table(
    "genres_associations",
    db.Model.metadata,
    db.Column("user_id", db.ForeignKey("users.id")),
    db.Column("genre_id", db.ForeignKey("genres.id")),
)


class GenreModel(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.TEXT, nullable=False)
