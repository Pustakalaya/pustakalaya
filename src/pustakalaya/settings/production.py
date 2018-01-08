from .base import *  # NOQA

DEBUG = False

try:
    db_name = config["DATABASE"]["NAME"]
    db_user = config["DATABASE"]["USER"]
    db_password = config["DATABASE"]["PASSWORD"]
    db_host = config["DATABASE"]["HOST"]
    db_port = config["DATABASE"]["PORT"]
except KeyError:
    raise ImproperlyConfigured("Improperly configured database settings.")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': db_port,
    }
}
