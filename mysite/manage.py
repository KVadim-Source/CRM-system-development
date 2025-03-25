#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import psycopg2


def create_db_and_user():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="VoSkReSeNsK",
        host="localhost"
    )
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'crm_system'")

    if not cursor.fetchone():
        cursor.execute("CREATE DATABASE crm_system")

    cursor.close()
    conn.close()


def create_superuser():
    """Создание суперпользователя, если его нет."""
    from django.contrib.auth.models import User

    try:
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='admin',
                email='',
                password='admin'
            )
    except Exception as e:
        print(f"Ошибка при создании суперпользователя: {e}")


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.prod')

    create_db_and_user()
    try:
        from django.core.management import execute_from_command_line

        execute_from_command_line(['manage.py', 'migrate'])
        create_superuser()
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


if __name__ == '__main__':
    main()
