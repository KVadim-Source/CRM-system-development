from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Введите свои данные пользователя PostgreSQL
USER = "postgres"
PASSWORD = "VoSkReSeNsK"

# Введите желаемые данные для суперпользователя (администратора)
USERNAME_ADMIN = "admin"
EMAIL_ADMIN = "admin@example.com"
PASSWORD_ADMIN = "admin"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "crm_system",
        "USER": USER,
        "PASSWORD": PASSWORD,
        "HOST": "localhost",
        "PORT": "5432",
    }
}

STATIC_ROOT = BASE_DIR / "staticfiles"
