from pathlib import Path
from decouple import config

USE_TZ = True
USE_I18N = True
LANGUAGE_CODE = "en-us"
LOGIN_URL = "/auth/login/"
ROOT_URLCONF = "config.urls"
AUTH_USER_MODEL = "accounts.User"
WSGI_APPLICATION = "config.wsgi.application"
TIME_ZONE = config("TIME_ZONE", default="UTC")
DEBUG = config("DEBUG", cast=bool, default=True)
BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SECRET_KEY = config(
    "SECRET_KEY",
    default="secret-key-!!!",
)
ALLOWED_HOSTS = (
    ["*"]
    if DEBUG
    else config(
        "ALLOWED_HOSTS", cast=lambda hosts: [h.strip() for h in hosts.split(",") if h]
    )
)
AUTHENTICATION_BACKENDS = [
    "apps.accounts.backend.ModelBackend",
]

# Applications

INSTALLED_APPS = [
    # default
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third-party
    "rest_framework",
    "storages",
    "django_celery_beat",
    # my apps
    "apps.core",
    "apps.accounts",
    "apps.home",
    "apps.order",
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

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.order.context_processors.cart",
            ],
        },
    },
]

# Password validation

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

# serving

STATIC_URL = "assets/"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Mode Handling:

if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / "assets"]

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
            "LOCATION": BASE_DIR / "tmp/cache",
        }
    }

    # EMAIL_USE_TLS = False
    # EMAIL_HOST = "localhost"
    # EMAIL_PORT = 25
    # EMAIL_HOST_USER = ""
    # EMAIL_HOST_PASSWORD = ""
    # DEFAULT_FROM_EMAIL = "shahabkabiri@maktab.dev"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = "shakabiri69@gmail.com"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_PASSWORD = "ofus rkqo zwyc daea"
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


else:
    REDIS_URL = f"redis://{config('REDIS_HOST')}:{config('REDIS_PORT')}"

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config("DB_NAME"),
            "USER": config("DB_USER"),
            "PASSWORD": config("DB_PASSWORD"),
            "HOST": config("DB_HOST"),
            "PORT": config("DB_PORT"),
        }
    }

    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": REDIS_URL,
        }
    }

    EMAIL_USE_TLS = config("EMAIL_USE_TLS")
    EMAIL_USE_SSL = config("EMAIL_USE_SSL")
    EMAIL_HOST = config("EMAIL_HOST")
    EMAIL_PORT = config("EMAIL_PORT")
    EMAIL_HOST_USER = config("EMAIL_USER")
    EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD")
    DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
#
# CELERY_TIMEZONE = TIME_ZONE
# CELERY_BROKER_URL = "redis://localhost:6379/0"
# CELERY_BROKER_BACKEND = "redis://localhost:6379/1"
# CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
# CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
