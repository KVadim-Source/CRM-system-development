import psycopg2
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.core.management import call_command
from mysite.settings.prod import (
    USER,
    PASSWORD,
    USERNAME_ADMIN,
    EMAIL_ADMIN,
    PASSWORD_ADMIN,
)

User = get_user_model()


class Command(BaseCommand):
    """
    Команда для инициализации базы данных и создания суперпользователя.

    Эта команда выполняет следующие действия:
    - Создает базу данных PostgreSQL, если она не существует.
    - Применяет миграции Django для создания таблиц в базе данных.
    - Создает суперпользователя Django, если его нет.

    Attributes:
        help (str): Краткое описание команды.
    """
    help = 'Initialize database and create superuser'

    def handle(self, *args, **options):
        self.create_db_and_user()
        self.apply_migrations()
        self.create_superuser()

    @staticmethod
    def create_db_and_user():
        """
        Создает базу данных и пользователя, если они не существуют.

        Использует подключение к PostgreSQL для проверки существования базы данных `crm_system`.
        Если база данных отсутствует, она создается.

        Raises:
            psycopg2.Error: Если возникает ошибка при подключении или выполнении SQL-запросов.
        """
        conn = psycopg2.connect(
            dbname="postgres", user=USER, password=PASSWORD, host="localhost"
        )
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'crm_system'")
        if not cursor.fetchone():
            cursor.execute("CREATE DATABASE crm_system")

        cursor.close()
        conn.close()

    @staticmethod
    def apply_migrations():
        """
        Выполняет миграции Django для создания таблиц в базе данных.
        """
        call_command('migrate')

    def create_superuser(self):
        """
        Создает суперпользователя Django, если его нет.

        Использует встроенную модель `User` для проверки существования суперпользователя.
        Если суперпользователь отсутствует, он создается с заданными учетными данными.

        Raises:
            Exception: Если возникает ошибка при создании суперпользователя.
        """
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username=USERNAME_ADMIN, email=EMAIL_ADMIN, password=PASSWORD_ADMIN
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
