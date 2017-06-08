# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_project',
        'USER': 'docker',
        'PASSWORD': 'secret',
        'HOST': 'db',
        'PORT': 5432,
        'CONN_MAX_AGE': 900
    }
}
