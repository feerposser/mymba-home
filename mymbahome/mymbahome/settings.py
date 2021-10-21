from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# to generate a new secret key: from django.core.management.utils import get_random_secret_key
# get secret key by Dockerfile or a dev secret key by default
SECRET_KEY = os.getenv("SECRET_KEY", "-mo8xvm!c#8gqv^7ap_-rfo_k%^me(@=2%#0!=*y18^pjx2@)o")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv("DEBUG", False)
DEBUG = bool(int(os.getenv("DEBUG", 1)))

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "home.apps.HomeConfig",
    "projects.apps.ProjectsConfig",
    "feeder.apps.FeederConfig"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mymbahome.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "home", "templates"),
            os.path.join(BASE_DIR, "feeder", "templates")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'mymbahome.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if not DEBUG:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("MYSQL_DATABASE", "mymbahomedb"),
        "USER": os.getenv("MYSQL_USER", "admin"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD", "abc123321"),
        "HOST": os.getenv("DATABASE_HOST", "localhost"),
        "PORT": os.getenv("DATABASE_PORT", "3306")
    }
}
else:
    print("DEBUG -->", DEBUG)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# cache config - https://docs.djangoproject.com/en/3.1/topics/cache/
# used to temporary cache IN DATABASE the mumber of helped animals by the project without using
# third parties packages for create database views.
# run 'python manage.py createcachetable' to create the cache table
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cache_table",
        "TIMEOUT": 604800  # 1 week
    }
}


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static_files")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# MEDIA FILES
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
