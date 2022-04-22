import os

PYTEST_RUNNING_GITHUB = os.getenv('PYTEST_RUNNING_GITHUB')

INSTALLED_APPS = [
    'users',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST') if not (
            PYTEST_RUNNING_GITHUB
        ) else 'localhost',
        'PORT': os.environ.get('POSTGRES_PORT'),
        'CONN_MAX_AGE': 300,
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
