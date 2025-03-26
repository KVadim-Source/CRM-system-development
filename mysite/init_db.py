import os

import psycopg2
from django.core.management import execute_from_command_line

from apps.myauth.models import User


def create_db_and_user() -> None:
    """
    Создает базу данных и пользователя, если они не существуют.

    Использует подключение к PostgreSQL для
    проверки существования базы данных `crm_system`.
    Если база данных отсутствует, она создается.

    Raises:
        psycopg2.Error: Если возникает ошибка
        при подключении или выполнении SQL-запросов.
    """
    conn = psycopg2.connect(
        dbname="postgres", user="postgres", password="VoSkReSeNsK", host="localhost"
    )
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'crm_system'")

    if not cursor.fetchone():
        cursor.execute("CREATE DATABASE crm_system")

    cursor.close()
    conn.close()


def create_superuser() -> None:
    """
    Создает суперпользователя Django, если его нет.

    Использует встроенную модель `User`
    для проверки существования суперпользователя.
    Если суперпользователь отсутствует,
    он создается с заданными учетными данными.

    Raises:
        Exception: Если возникает ошибка при создании суперпользователя.
    """
    try:
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username="admin", email="admin@example.com", password="admin"
            )
            print("Суперпользователь успешно создан")
    except Exception as e:
        print(f"Ошибка при создании суперпользователя: {e}")


def init_db() -> None:
    """
    Инициализирует базу данных и создает суперпользователя.

    Выполняет миграции и создает базу данных, если она не существует.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.prod")
    create_db_and_user()
    execute_from_command_line(["manage.py", "migrate"])
    create_superuser()


if __name__ == "__main__":
    init_db()
