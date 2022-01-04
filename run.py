from project.config import DevelopmentConfig
from project.dao.models import User
from project.dao.models import Movie
from project.dao.models import Director
from project.dao.models import Genre
from project.app import create_app, db

app = create_app(DevelopmentConfig)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie": Movie,
        "User": User
    }
