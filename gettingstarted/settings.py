"""
Django settings for gettingstarted project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import django_heroku
from rest_framework import serializers

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
# breakpoint()
STATIC_DIR = os.path.join(BASE_DIR,'static')
MEDIA_DIR = os.path.join(BASE_DIR,'media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "CHANGE_ME!!!! (P.S. the SECRET_KEY environment variable will be used, if set, instead)."

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # "django_adminlte",
    "sales",
    "adminlte3",
    # "django_adminlte_theme",
    "adminlte3_theme",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admindocs",
    "hello",
    "food",
    # "address",
    "api",
    "product",
    "food_delivery",
    "restaurant",
    # "sales",
    "store_follower",
    "rest_framework",
  # "rest_framework_api_key",
    'rest_framework.authtoken',
    # 'django_extensions',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    # 'django_google_maps',
    "promocode",
    "Location",
    "review",
    "commission",
    "tax",
    "dispute",
    "djstripe",

]
STRIPE_LIVE_SECRET_KEY = os.environ.get("STRIPE_LIVE_SECRET_KEY", "sk_live_IXZa5jTxiyiOglwAue5Y5JFW")
STRIPE_TEST_PUBLIC_KEY = os.environ.get("STRIPE_TEST_PUBLIC_KEY", "pk_test_hRyI3DFnQ9SdUXHf5LVh7kzi")
STRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "sk_test_Gtm8AHI0FVaVXmBIsKUSNB4E")
STRIPE_LIVE_MODE = False  # Change to True in production
DJSTRIPE_WEBHOOK_SECRET = "whsec_az1UrBkiB2tBBJhq9qh1wPrBq4DGAWbi"  # Get it from the section in the Stripe dashboard where you added the webhook endpoint



# GOOGLE_API_KEY = 'AIzaSyCXTmnpb48jkPSW_BZxS2_mEM_kjZnewBE'
GOOGLE_MAPS_API_KEY = 'AIzaSyDD4BVDPaXBoj87tuQviOckH4HauJWGhyU'


# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         # 'rest_framework.permissions.IsAuthenticated',
#         'rest_framework.permissions.IsAdminUser',
#     ]
# }

# REST_AUTH_SERIALIZERS = {
#     'LOGIN_SERIALIZER': 'path.to.custom.LoginSerializer',
#     # 'LOGIN_SERIALIZER': 'path.to.custom.LoginSerializer',
# }
REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'api.serializers.LoginSerializer',
    'TOKEN_SERIALIZER': 'api.serializers.CustomTokenSerializer',
}
REST_AUTH_REGISTER_SERIALIZERS = {
    # 'TOKEN_SERIALIZER': 'api.serializers.CustomTokenSerializer',
    # 'REGISTER_SERIALIZER': 'rest_auth.registration.serializers.RegisterSerializer',
    'REGISTER_SERIALIZER': 'api.serializers.RegisterSerializer',
    }

# For permission

# REST_FRAMEWORK = {
#     "DEFAULT_PERMISSION_CLASSES": [
#         "rest_framework_api_key.permissions.HasAPIKey",
#     ]
# }

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.SessionAuthentication',
#         # 'rest_framework.authentication.TokenAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#    )
# }


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_VERIFICATION = 'none'
#
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False
#
# SITE_ID = 1

# AUTH_USER_MODEL = 'api.CustomUser'

# AUTHENTICATION_BACKENDS = (
#     # Needed to login by username in Django admin, regardless of `allauth`
#     "django.contrib.auth.backends.ModelBackend",
#
#     # `allauth` specific authentication methods, such as login by e-mail
#     "allauth.account.auth_backends.AuthenticationBackend",
# )

OLD_PASSWORD_FIELD_ENABLED = True
REST_SESSION_LOGIN = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = 'username|email'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
# ACCOUNT_EMAIL_VERIFICATION = 'optional'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    # 'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S.%f%z",
    'DATETIME_FORMAT': "%Y-%m-%d",
}





MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
  'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # 'food.middleware.CurrentUserMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
ROOT_URLCONF = "gettingstarted.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [TEMPLATE_DIR],
        # 'DIRS': [],
        #  'DIRS': [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.media',
            ]
        },
    }
]

WSGI_APPLICATION = "gettingstarted.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE" : "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3")
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        'OPTIONS': {
            'min_length': 6,
        }
     },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "/static/"
STATICFILES_DIRS = [STATIC_DIR,]

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

# LOGIN_URL = '/food_delivery/user_login/'


django_heroku.settings(locals())

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
