from django.db import models

from apps.ads.models import Advertisement


class Lead(models.Model):
    """
    Модель потенциального клиента.

    Attributes:
        first_name (str): Имя потенциального клиента.
        last_name (str): Фамилия потенциального клиента.
        phone (str): Телефон потенциального клиента.
        email (str): Email потенциального клиента.
        advertisement (Advertisement | None): Рекламная
        кампания, связанная с потенциальным клиентом.
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
            permissions (list[tuple]): Кастомные разрешения для модели.
        """

        verbose_name: str = "Потенциальный клиент"
        verbose_name_plural: str = "Потенциальные клиенты"
        permissions: list[tuple[str, str]] = [
            ("can_view_lead", "Может просматривать потен-ых клиентов"),
            ("can_add_lead", "Может добавлять потен-ых клиентов"),
            ("can_change_lead", "Может изменять потен-ых клиентов"),
            ("can_delete_lead", "Может удалять потен-ых клиентов"),
        ]

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Фамилия и имя потенциального клиента.
        """
        return f"{self.last_name} {self.first_name}"
