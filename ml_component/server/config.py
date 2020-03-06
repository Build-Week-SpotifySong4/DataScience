# ml_component/server/config.py
import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://postgres:@localhost/'
database_name = 'spotify_suggester'


class DevelopmentConfig:
    """Development configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class ProductionConfig:
    """Production configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = 'postgresql:///' + database_name
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] 
