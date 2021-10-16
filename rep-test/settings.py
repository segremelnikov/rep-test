"""
Django settings for rep-test project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


CURRENT_DIR = os.path.dirname(__file__)

TEMPLATE_DIRS = (
    os.path.join(CURRENT_DIR, 'templates'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5e-)wv)#fz)xop#)popso#*ogt#$7h_=s!z-7(_u#^78@a3-@5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['rep-test.ru', 'localhost']

LLOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'large': {
            'format': '%(asctime)s  %(levelname)s  %(process)d  %(pathname)s  %(funcName)s  %(lineno)d  %(message)s  '
        },
        'tiny': {
            'format': '%(asctime)s  %(message)s  '
        }
    },
    'handlers': {
        'errors_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'filename': 'logs/ErrorLoggers.log',
            'formatter': 'large',
        },
        'info_file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'filename': 'logs/InfoLoggers.log',
            'formatter': 'large',
        },
    },
    'loggers': {
        'error_logger': {
            'handlers': ['errors_file'],
            'level': 'WARNING',
            'propagate': False,
        },
        'info_logger': {
            'handlers': ['info_file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social_django',
    "crispy_forms",
    
    'regandauth', 
    'main',
    'addpeople',
    'estpeople',
    'results',
    'sandbox'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'main.middleware.AuthRequiredMiddleware',
    
]

ROOT_URLCONF = 'rep-test.urls'

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
                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'rep-test.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'HOST': 'localhost',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '[имя]',
        'USER': '[пользователь]',
        'PASSWORD': '[пароль]',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

#STATIC_ROOT = 'static/'

STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'static'), '/static/', )





CRISPY_TEMPLATE_PACK = "bootstrap4"


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kellyreptest@gmail.com'
EMAIL_HOST_PASSWORD = '[пароль]'
EMAIL_PORT = 587

AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',          
    'django.contrib.auth.backends.ModelBackend', 
)

SOCIAL_AUTH_VK_OAUTH2_KEY = '[KEY]'
SOCIAL_AUTH_VK_OAUTH2_SECRET = '[SECRET]'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = "/"

ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False

AUTH_PASSWORD_VALIDATORS = []