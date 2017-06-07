# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'km^(2@8l*w$_+^a!%d6&2s^g$18!c35=fcr(^+*!ltuad1=l)z'

ALLOWED_HOSTS = ['127.0.0.1']

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

X_FRAME_OPTIONS = 'DENY'
