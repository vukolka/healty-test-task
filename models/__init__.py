import builtins

if not hasattr(builtins, 'db'):
    import models.db_manager as db
    builtins.db = db