from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    Конфигурация приложения "Продукты".

    Attributes:
        default_auto_field (str): Тип автоматически
        генерируемого первичного ключа.
        name (str): Путь к приложению.
    """

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "apps.products"
