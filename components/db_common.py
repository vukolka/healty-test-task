import builtins


def get_db():
    return builtins.db


def db_commit(db=None):
    if not db:
        db = get_db()
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
