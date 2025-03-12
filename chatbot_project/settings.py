"""
Django settings for chatbot_project project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# import dj_database_url

# DATABASES = {
#     "default": dj_database_url.config(default=os.getenv("DATABASE_URL"))
# }

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

from dotenv import load_dotenv

load_dotenv()

# AWS S3 Configuration
AWS_ACCESS_KEY_ID = os.getenv("CHAT_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.getenv("CHAT_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.getenv("CHAT_S3_BUCKET", "")
AWS_S3_REGION_NAME = os.getenv("CHAT_region", "") 

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

# Static Files
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"

STATIC_ROOT = '/static/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-lb@zq)p(ounyri)#nmz0z)9gqmo%1bhqj^1%)ai3jwr^$7w=0z"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []

# DB user details

# DB_NAME='chatbot_db'
# DB_SERVER = 'chatbot-db-cluster.cluster-cb4koygccrv8.us-east-1.rds.amazonaws.com'
# DB_USER_NAME = 'chatbot_admin'
# DB_PASSWORD = 'SridharPuppala147P'

OPEN_AI_KEY = "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"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",
    "chatbot_app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "chatbot_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = "chatbot_project.wsgi.application"

ALLOWED_HOSTS = ["ulfs.azurewebsites.net", "*"]
CSRF_TRUSTED_ORIGINS = ['https://*.azurewebsites.net','https://*.127.0.0.1']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", ""),  # Use your RDS database name
        "USER": os.getenv("DB_USER", ""),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),  # Store in env vars for security
        "HOST": os.getenv("DB_SERVER", ""),  # Your RDS Writer Endpoint
        "PORT": os.getenv("DB_PORT", ""),
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_URL = "static/"

# Static files (CSS, JavaScript, Images)
# STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'carrs2024ist@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'qpxh vdeg pusk ttgt'  # Your Gmail App Password