"""
Django settings for choban project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os, environ

env = environ.Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env.read_env(os.path.join(BASE_DIR, '.env'))

URL = env('URL') or 'https://choban.app'
PACKAGES_URL = URL+'/packages'

FORCE_SCRIPT_NAME = env('FORCE_SCRIPT_NAME', default=None)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY') or os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(env('DEBUG', default=True)) or os.environ.get('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS').replace(' ', '').split(',') if env(
    'ALLOWED_HOSTS') else ['choban.herokuapp.com', 'localhost:8000']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'rest_framework',
    'api',
    'packages',
    'rest_framework.authtoken',
    'django_gravatar',
    'django_filters',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware'
]

ROOT_URLCONF = env('ROOT_URLCONF', default='choban.urls')

CORS_ORIGIN_ALLOW_ALL = env('CORS_ORIGIN_ALLOW_ALL', default=False) or os.environ.get('CORS_ORIGIN_ALLOW_ALL')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'choban', 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = env('WSGI_APPLICATION', default='choban.wsgi.application')

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASE_HOST = env('DATABASE_HOST') or os.environ.get('DATABASE_HOST')
DATABASE_NAME = env('DATABASE_NAME') or os.environ.get('DATABASE_NAME')
DATABASE_PASSWORD = env('DATABASE_PASSWORD') or os.environ.get('DATABASE_PASSWORD')
DATABASE_USER = env('DATABASE_USER') or os.environ.get('DATABASE_USER')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': 5432,
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcached:11211',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = env('STATICFILES_DIR', default=os.path.join(BASE_DIR, 'staticfiles')) or os.environ.get('STATICFILES_DIR')

MEDIA_URL = '/media/'
MEDIA_ROOT = env('MEDIAFILES_DIR', default=os.path.join(BASE_DIR, 'media')) or os.environ.get('MEDIAFILES_DIR')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "packages", "static")
]
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination'
}
LOGIN_REDIRECT_URL = '/packages'
