"""
Django settings for quotes project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import environ
from mongoengine import connect
import certifi

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['db.aleksvoit.com', 'localhost', '127.0.0.1', '0.0.0.0', 'kind-sibbie-aleks-gmbh-38417f5e.koyeb.app']


CSRF_TRUSTED_ORIGINS = [
    'https://localhost',
    'http://127.0.0.1:8000',
    'https://kind-sibbie-aleks-gmbh-38417f5e.koyeb.app'
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'quoteapp',
    'users',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "quotes.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "quotes.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# if os.getenv('PG_HOST') is None:
#     raise RuntimeError('Failed to load DB HOST name')

if DEBUG is True:
    DATABASES = {
        "default": {
            # "ENGINE": "django.db.backends.postgresql_psycopg2",
            # "NAME": env('PG_DB'),
            # 'USER': env('PG_USER'),
            # 'PASSWORD': env('PG_PASSWORD'),
            # 'HOST': env('PG_HOST'),
            # # 'HOST': 'db',
            # 'PORT': env('PG_PORT'),

            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": env('DATABASE_NAME'),
            'USER': env('DATABASE_USER'),
            'PASSWORD': env('DATABASE_PASSWORD'),
            'HOST': env('DATABASE_HOST'),
            # 'PORT': 5432,
            'OPTIONS': {'sslmode': 'require'},
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": env('DATABASE_NAME'),
            'USER': env('DATABASE_USER'),
            'PASSWORD': env('DATABASE_PASSWORD'),
            'HOST': env('DATABASE_HOST'),
            # 'PORT': 5432,
            'OPTIONS': {'sslmode': 'require'},

        }
    }

user = env('MG_USER')
password = env('MG_PASS')
cluster = env('MG_CLUSTER')
domain = env('MG_DOMAIN')
db_name = env('MG_DB')

connect(
    db=db_name,
    host=f'mongodb+srv://{user}:{password}@{cluster}.{domain}/',
    tlsCAFile=certifi.where()
)
# mongodb+srv://oleksandrvoitushenko:<db_password>@clusterhw8.gaxzbkd.mongodb.net/

# host=f'mongodb+srv://{user}:{password}@{cluster}.{domain}/?retryWrites=true&w=majority,'

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field


# def my_ssl_context(self):
#     return ssl.create_default_context(cafile=certifi.where())
#
#
# EmailBackend.ssl_context = my_ssl_context

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_STARTTLS = env('EMAIL_STARTTLS')

EMAIL_USE_SSL = True
EMAIL_USE_TLS = False

EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# ssl_context = ssl.create_default_context(cafile=certifi.where())
#
# connection = get_connection(
#     use_ssl=True,
#     ssl_context=ssl_context,
#     host=os.getenv('EMAIL_HOST'),
#     port=465,
#     username=os.getenv('EMAIL_HOST_USER'),
#     password=os.getenv('EMAIL_HOST_PASSWORD'),
# )
