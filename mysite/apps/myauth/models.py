from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Модель пользователя с расширенными полями.
    """

    class Meta:
        """
        Метаданные модели.

        Attributes:
            verbose_name (str): Название модели в единственном числе.
            verbose_name_plural (str): Название модели
            во множественном числе.
        """

        verbose_name: str = "Пользователь"
        verbose_name_plural: str = "Пользователи"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Имя пользователя.
        """
        return str(self.username)
