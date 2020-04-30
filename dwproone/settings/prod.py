from .base import *

ALLOWED_HOSTS = ['localhost', '46.101.192.185']
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
