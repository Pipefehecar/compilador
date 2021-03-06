"""
Django settings for DJango_comProject project.

Generated by 'django-admin startproject' using Django 1.11.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.core.urlresolvers import reverse_lazy


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7$6*z%a3#mix$--+3=jj!&z=q6dp%x%$6v@9ma^h&85vqhfj)i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# from unipath import path
# RUTA_PROYECTO = path(__file__).ancestor(2)



ALLOWED_HOSTS = []


# Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     # 'django.contrib.sites',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'apps.login',
#     'apps.registro',
#     'SOCIAL.apps.django.app.default',
# ]

DJANGO_APPS =[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    #'social.apps.django_app.default',
    'social_django',
]

LOCAL_APPS =[
    'apps.login',
    # 'apps.registro',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# from django.core.urlresolvers import reverse_lazy
# LOGIN_URL = reverse_lazy('login')
# LOGIN_REDIRECT_URL = reverse_lazy('login') # aqui redireccionamos a la url del compilador
# LOGOUT_URL = reverse_lazy('logout')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DJango_comProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'DJango_comProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME':'compilador.db',
    #     # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'dcompiler',
        'USER' : 'djangoadmin',
        'PASSWORD' : 'pipeadmin',
        'HOST' : 'localhost',
        'PORT' : '5432',
        }
    }


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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTHENTICATION_BACKENDS = (
    # 'social.backends.facebook.FacebookAppOAuth2',
    # 'social.backends.facebook.FacebookOAuth2',
    # 'social.backends.facebook.google.GoogleOpenId',
    # 'social.backends.facebook.google.GoogleOAuth2',
    # 'social.backends.facebook.googleGoogleOAuth',
    'django.contrib.auth.backends.ModelBackend',
    )

# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
# SOCIAL_AUTH_LOGIN_URL = '/error/'



# SOCIAL_AUTH_USER_MODEL = 'login.usuario'

# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']


 # Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
#Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '313768165072-a7af6m5l6r23p18g823k0g0o7qus8u6t.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'uzgMoCw3g0UBoGC4glzNKhCF'


#facebook
# SOCIAL_AUTH_FACEBOOK_KEY = 170382586947841
# SOCIAL_AUTH_FACEBOOK_SECRET = 4b714638e8ac480f2f93f5dd76dc5825

# LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('usuario:home') # aqui redireccionamos a la url del compilador
LOGOUT_URL = reverse_lazy('logout')

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'luisfehecar14@gmail.com'
EMAIL_HOST_PASSWORD = '108303320655'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
