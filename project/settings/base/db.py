# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_blog',
        'USER': 'django_blog',
        'PASSWORD': 'secret',
        'HOST': 'db',
        'PORT': 5432,
        'CONN_MAX_AGE': 900
    }
}
