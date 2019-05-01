from pathlib import Path

from dj_database_url import parse as parse_db_url
from prettyconf import config
from corsheaders.defaults import default_headers


# Project Structure
PROJECT_NAME = "piririm"

# Debug & Development
DEBUG = config("DEBUG", default=False, cast=config.boolean)
LOG_LEVEL = config("LOG_LEVEL", default='WARNING')

# Database
DATABASES = {
    'default': config('DATABASE_URL', cast=parse_db_url),
}

# always connected:
DATABASES['default']['CONN_MAX_AGE'] = config("CONN_MAX_AGE", cast=config.eval, default="None")
DATABASES['default']['TEST'] = {'NAME': config('TEST_DATABASE_NAME', default=None)}

assert DATABASES['default']['TEST']['NAME'] != DATABASES['default']['NAME']

# Security & Signup/Signin
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*", cast=config.list)
SECRET_KEY = config("SECRET_KEY")


# i18n & l10n
TIME_ZONE = "UTC"
USE_I18N = False
USE_L10N = False
USE_TZ = False
LANGUAGE_CODE = "en-us"

# Miscelaneous
ROOT_URLCONF = "{}.urls".format(PROJECT_NAME)
WSGI_APPLICATION = "{}.wsgi.application".format(PROJECT_NAME)
LOG_REQUEST_ID_HEADER = "HTTP_X_REQUEST_ID"

# Application
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]

INSTALLED_APPS = (
    'django.contrib.postgres',

    'raven.contrib.django.raven_compat',

    'corsheaders',

    'apps.bills',
    'apps.records',
)

CACHES = {
    'default': {
        'BACKEND': config('CACHE_BACKEND', default='django.core.cache.backends.dummy.DummyCache')
    }
}

# CORS:
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = default_headers + (
    'x-username', 'x-password',
)

RAVEN_CONFIG = {
    'dsn': config('RAVEN_DSN', default=''),
    'release': '0',
}
