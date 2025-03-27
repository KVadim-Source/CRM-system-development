from django.db import models

from apps.ads.models import Advertisement


class Lead(models.Model):
    """
    Модель лида.

    Attributes:
        first_name (str): Имя лида.
        last_name (str): Фамилия лида.
        phone (str): Телефон лида.
        email (str): Email лида.
        advertisement (Advertisement | None): Рекламная
        кампания, связанная с лидом.
    """

    first_name: str = models.CharField(max_length=100, verbose_name="Имя")
    last_name: str = models.CharField(max_length=100, verbose_name="Фамилия")
    phone: str = models.CharField(max_length=20, verbose_name="Телефон")
    email: str = models.EmailField(verbose_name="Email")
    advertisement: Advertisement | None = models.ForeignKey(
        "ads.Advertisement",
        on_delete=models.CASCADE,
        related_name="leads",
        verbose_name="Рекламная кампания",
        null=True,
        blank=True,
    )

    class Meta:
        """
        Метаданные модели.

        Attributes:
            verbose_name (str): Название модели в единственном числе.
            verbose_name_plural (str): Название модели во множественном числе.
        """

        verbose_name: str = "Лид"
        verbose_name_plural: str = "Лиды"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Фамилия и имя лида.
        """
        return f"{self.last_name} {self.first_name}"
