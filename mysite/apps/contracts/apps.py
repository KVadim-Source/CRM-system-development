from django.apps import AppConfig


class ContractsConfig(AppConfig):
    """
    Конфигурация приложения "Контракты".

    Attributes:
        default_auto_field (str): Тип автоматически
        генерируемого первичного ключа.
        name (str): Путь к приложению.
        verbose_name (str): Название приложения
        для отображения в админке.
    """

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "apps.contracts"
    verbose_name: str = "Контракты"

    def ready(self) -> None:
        """
        Метод для выполнения кода при готовности приложения.

        Returns:
            None
        """
        pass
