from django.apps import AppConfig


class AdsConfig(AppConfig):
    """
    Конфигурация приложения рекламных кампаний.

    Attributes:
        default_auto_field (str): Тип автоматически
        генерируемого первичного ключа.
        name (str): Путь к приложению на Python.
    """

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "apps.ads"
