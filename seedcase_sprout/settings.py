"""Django settings for seedcase_sprout project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-rc4eh2e#kjc!o=yn!9k@)hcgnlb(fvn9--pcjv4v0qs34c^p0l",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "") != "False"

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Fly.io deployment settings
APP_NAME = os.environ.get("FLY_APP_NAME")
if APP_NAME:
    ALLOWED_HOSTS.append(f"{APP_NAME}.fly.dev")

    # We trust our own url
    CSRF_TRUSTED_ORIGINS = [f"https://{APP_NAME}.fly.dev"]


# Application definition
INSTALLED_APPS = [
    "app",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "seedcase_sprout.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "seedcase_sprout.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
sqlite_url = "sqlite:///db.sqlite3"
database_url = os.environ.get("DATABASE_URL", sqlite_url)

DATABASES = {"default": dj_database_url.parse(database_url, conn_max_age=600)}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

"""
Static files (CSS, JavaScript, Images)
Serving static files are handled differently depending on the DEBUG-flag:

- DEBUG=True. The development server automatically serves static assets
  located in "static" folders. E.g "app/static" and "admin/static"

- DEBUG=False. The static assets are not handled automatically. We need
  to do three things:
  - Configure STATIC_ROOT which is the central location for static assets
  - Before running the application run `python manage.py collectstatic` to copy all
    static assets to STATIC_ROOT
  - Install whitenoise. Whitenoise will serve the static assets from the Django app.
    The other alternatives seems more complicated:
"""

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
