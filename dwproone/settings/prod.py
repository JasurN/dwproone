from .base import *

ALLOWED_HOSTS = ['localhost', 'dwproone.uz', 'www.dwproone.uz']
SECRET_KEY = os.environ['SECRET_KEY']  # gets from gunicorn service
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dwprooneprod',
        'USER': 'dwproone',
        'PASSWORD': os.environ['db_password'],  # gets from gunicorn service
        'HOST': 'localhost',
        'PORT': ''
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
