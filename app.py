from components.fast_api import app


def register_routes():
    import views.Users
    import views.Auth
    import views.Genres
    import views.Games


def create_app():
    register_routes()
    return app

fastapi_app = create_app()