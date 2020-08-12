from .base import *

ALLOWED_HOSTS = ['localhost', 'dwproone.uz', 'www.dwproone.uz']
ADMINS = [('Jasurbek', '97jasur@gmail.com'), ]
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
