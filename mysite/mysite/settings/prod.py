from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "crm_system",
        "USER": "postgres",
        "PASSWORD": "VoSkReSeNsK",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

STATIC_ROOT = BASE_DIR / "staticfiles"
