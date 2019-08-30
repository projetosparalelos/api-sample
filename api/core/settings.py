"""
Django settings.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import datetime
import os

from decouple import Csv, config

VERSION = '0.1.0'

ENV = config('ENV')

DEBUG = config('DEBUG', cast=bool)

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

DJANGO_ADMIN = config('DJANGO_ADMIN', cast=bool)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
    'django_filters',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',
    'accounts',
    'legal',
    'todo',
]

if DEBUG or DJANGO_ADMIN:
    # Conditionally enables the Django admin and its dependencies.
    index = INSTALLED_APPS.index('django.contrib.auth')
    INSTALLED_APPS.insert(index, 'django.contrib.admin')
    INSTALLED_APPS.insert(index, 'suit')
    INSTALLED_APPS.insert(index, 'ckeditor')

MIDDLEWARE = [
    'bugsnag.django.middleware.BugsnagMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'core.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['core/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': config('DB_NAME')
    }
}


# Authentication
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-user-model
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'accounts.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 6}
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = config('LANGUAGE_CODE')

LANGUAGES = [
    ('en-US', "English (US)"),
    ('es-ES', "Español (España)"),
    ('pt-BR', "Português (Brasil)"),
]

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]

STATIC_ROOT = os.path.join(BASE_PARENT_DIR, 'resources/static/')

STATIC_URL = '/static/'


# User uploaded files.
# https://docs.djangoproject.com/en/2.1/ref/settings/#media-root

MEDIA_ROOT = os.path.join(BASE_PARENT_DIR, 'resources/media/')

MEDIA_URL = '/media/'


# Emails
# https://docs.djangoproject.com/en/2.1/ref/settings/#default-from-email

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

EMAIL_HOST = config('EMAIL_HOST')

EMAIL_PORT = config('EMAIL_PORT', cast=int)

EMAIL_HOST_USER = config('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)

EMAIL_USE_SSL = config('EMAIL_USE_SSL', cast=bool)


# Django REST Framework
# http://www.django-rest-framework.org

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'core.drf_authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '2000/day'
    },
    'EXCEPTION_HANDLER': 'core.drf_exception_handler.custom_exception_handler',
}

# Django REST Framework JWT
# http://getblimp.github.io/django-rest-framework-jwt/#additional-settings

JWT_AUTH = {
    'JWT_PAYLOAD_HANDLER': 'core.drf_jwt.jwt_payload_handler',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'core.drf_jwt.jwt_response_payload_handler',
    'JWT_GET_USER_SECRET_KEY': 'core.drf_jwt.jwt_get_user_secret_key',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=180),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}


# CORS
# https://github.com/zestedesavoir/django-cors-middleware

CORS_ORIGIN_ALLOW_ALL = DEBUG

CORS_ORIGIN_WHITELIST = config('CORS_ORIGIN_WHITELIST', cast=Csv())


# Celery
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

CELERY_BROKER_URL = config('CELERY_BROKER_URL')

CELERY_TASK_DEFAULT_QUEUE = config('CELERY_TASK_DEFAULT_QUEUE')

CELERY_TASK_DEFAULT_EXCHANGE = config('CELERY_TASK_DEFAULT_EXCHANGE')

CELERY_TASK_DEFAULT_ROUTING_KEY = config('CELERY_TASK_DEFAULT_ROUTING_KEY')

CELERY_ACCEPT_CONTENT = ['application/json']

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'

CELERY_TIMEZONE = TIME_ZONE


# Bugsnag

BUGSNAG = {
    'api_key': config('BUGSNAG_API_KEY'),
    'project_root': BASE_DIR,
    'notify_release_stages': ['prd', 'hlg'],
    'release_stage': ENV
}


# Django Suit
# http://django-suit.readthedocs.io/en/develop/configuration.html#full-example

SUIT_CONFIG = {
    'ADMIN_NAME': 'Todo List API',
    'SEARCH_URL': '',

    'MENU': (
        {
            'app': 'accounts',
            'icon': 'icon-user',
            'models': ('user',)
        },
        {
            'app': 'legal',
            'icon': 'icon-briefcase',
            'models': ('legal',)
        },
        {
            'app': 'todo',
            'icon': 'icon-list',
            'models': ('list', 'task')
        },
    )
}


# Django CKEditor
# https://github.com/django-ckeditor/django-ckeditor

CKEDITOR_CONFIGS = {
    'default': {
        'width': 580,
        'colorButton_colors': 'FFE9C6,FFFFFF,555555',
        'colorButton_enableMore': True,
        'colorButton_enableAutomatic': False,
        'toolbar': [
            ['PasteText', '-', 'Undo', 'Redo'], ['RemoveFormat'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'SpecialChar'],
            ['Link', 'Unlink'],
            ['TextColor', 'BGColor'],
            ['Format'],
            ['NumberedList', 'BulletedList', 'Blockquote', '-', 'Outdent', 'Indent', '-',
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Maximize', 'Print'],
            ['ShowBlocks', 'Source']
        ],
    }
}
