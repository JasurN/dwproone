from .base import *

ALLOWED_HOSTS = ['localhost', '0.0.0.0']
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dwprooneprod',
        'USER': 'dwproone',
        'PASSWORD': os.environ['db_password'],
        'HOST': 'localhost',
        'PORT': ''
    }
}
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
