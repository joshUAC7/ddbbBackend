
"""
Django settings for core project.
Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/
For the full list of settings and their values, see https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
# Don't forget to import dj-database-url at the beginning of the file
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-_510t&_)(ry1*#q475p21tyf-n6vsw&4yg2a@_j)307j#=r=h!'
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG=True
DEBUG = 'RENDER' not in os.environ

# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # third party
    "rest_framework",
    'rest_framework.authtoken',
    "corsheaders",
    'django.contrib.sites',

    # authentication
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # local
    'drfauth.apps.DrfauthConfig',
    'logic.apps.LogicConfig'

]


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
         'APP': {
            'client_id': '479391179314-jhm77qhqi43pvqug5j3ijjbuuus8f428.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        },
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        # "VERIFIED_EMAIL": True,

        # 'OAUTH_PKCE_ENABLED': True,
        # 'APP': {
        #     'client_id': '479391179314-jhm77qhqi43pvqug5j3ijjbuuus8f428.apps.googleusercontent.com',
        #     'secret': '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',
        #     'key': ''
        # }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# we are turning off email verification for now

# SOCIALACCOUNT_AUTO_SIGNUP=False
# SOCIALACCOUNT_EMAIL_REQUIRED = True
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_VERIFICATION='none'
SITE_ID = 1  # https://dj-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional
REST_USE_JWT = True # use JSON Web Tokens


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = '020200295a@gmail.com'
# EMAIL_HOST_PASSWORD = 'Richarddawkings7'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# ACCOUNT_EMAIL_REQUIRED = True

AUTH_USER_MODEL = "drfauth.CustomUserModel"
# We need to specify the exact serializer as well for dj-rest-auth, otherwise it will end up shooting itself
# in the foot and me in the head
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'drfauth.serializers.CustomUserModelSerializer'
}
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "drfauth.serializers.CustomRegisterSerializer",
}

# set up the authentication classes
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),

    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        'rest_framework.authentication.TokenAuthentication',
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
}
REST_AUTH = {
    'USE_JWT': True,
    "REGISTER_SERIALIZER": "drfauth.serializers.CustomRegisterSerializer",
}

ROOT_URLCONF = 'core.urls'


from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True, 
    'UPDATE_LAST_LOGIN': True,
    "USER_ID_FIELD": "userId",  # for the custom user model
    "USER_ID_CLAIM": "user_id",
    "SIGNING_KEY": SECRET_KEY
}

CORS_ORIGIN_ALLOW_ALL = True # only for dev environment!, this should be changed before you push to production

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME':'django_mysql',
#         'USER':'josue',
#         'PASSWORD':'Admin123',
#         'HOST':'mysql-131525-0.cloudclusters.net',
#         'PORT':'19407',
#         # 'OPTIONS':{
#         #     'driver':'ODBC Driver 17 for SQL Server',y
#         #     'extra_params': "Encrypt=no"
#         #     }
#     }
# }

DATABASES = {
        'default':dj_database_url.config(default="mysql://josue:Admin123@mysql-131525-0.cloudclusters.net:19407/django_mysql", conn_max_age=600),
        }
# DATABASE_CONNECTION_POOLING = False

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = "static/"
# STATIC_ROOT = 'staticfiles'
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]


STATIC_URL = '/static/'

# Following settings only make sense on production and may break development environments.
if not DEBUG:
    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
