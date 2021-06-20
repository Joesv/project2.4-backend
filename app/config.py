from os import getenv, path
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import timedelta


class Config:
    load_dotenv()

    PORT = getenv('PORT')
    DEBUG = True

    dev = getenv('IS_DEV', False)

    DB_USER = getenv('DB_USER')
    DB_PASSWORD = getenv('DB_PASSWORD')
    DB_HOST = getenv('DB_HOST')
    DB_PORT = getenv('DB_PORT')
    DB_NAME = getenv('DB_NAME')

    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{password}@{host}:{port}/{name}'.format(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        name=DB_NAME
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)

    BASE_DIR = path.abspath(dirname(__file__))

    # application threads
    THREADS_PER_PAGE = getenv('THREADS_PER_PAGE', 2)

    # protection against CSRF
    CSRF_ENABLED = getenv('CSRF_ENABLED', True)
    CSRF_SESSION_KEY = getenv('CSRF_SESSION_KEY', 'secret')  # TODO: secret key for signing data

    # secret key for signing cookies
    SECRET_KEY = getenv('SECRET_KEY')

    # Key for API JWT tokens
    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=1)

    # Openweather api key and wether or not to fetch the data
    OPENWEATHERAPIKEY = getenv('OPENWEATHERMAP_API')
    ENABLEWEATHERAPI = getenv('ENABLEWEATHERAPI') == 'true'  # we're using expensive API calls, in case autoreload is enabled you might reach your limit
