from decouple import config
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-t&*dt)9m)=s(8rhdkd%$kilnf)o2mpaq86@!dgvt=c1suk%k0$')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=['127.0.0.1', 'localhost'], cast=lambda v: [s.strip() for s in v.split(',')])

# CORS Headers
CORS_ALLOW_ALL_ORIGINS = config('CORS_ALLOW_ALL_ORIGINS', default=False, cast=bool)
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='', cast=lambda v: [s.strip() for s in v.split(',')])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'corsheaders',  
    'rest_framework',
    'mpesa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  
]
ROOT_URLCONF = 'project1.urls'

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

WSGI_APPLICATION = 'project1.wsgi.application'
# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DATABASE_NAME', default='db_name'),
        'USER': config('DATABASE_USER', default='db_user'),
        'PASSWORD': config('DATABASE_PASSWORD', default='db_password'),
        'HOST': config('DATABASE_HOST', default='localhost'),
        'PORT': config('DATABASE_PORT', default='3306', cast=int),
    }
}


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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MPESA_CONFIG = {
    'CONSUMER_KEY': config('MPESA_CONSUMER_KEY'),
    'CONSUMER_SECRET': config('MPESA_CONSUMER_SECRET'),
    'HOST_NAME': config('MPESA_HOST_NAME'),
    'PASS_KEY': config('MPESA_PASS_KEY'),
    'SAFARICOM_API': config('MPESA_SAFARICOM_API'),
    'AUTH_URL': config('MPESA_AUTH_URL'),
    'TRANSACTION_TYPE': config('MPESA_TRANSACTION_TYPE'),
    'TILL_NUMBER': config('MPESA_TILL_NUMBER'),
    'SHORT_CODE': config('MPESA_SHORT_CODE'),
}