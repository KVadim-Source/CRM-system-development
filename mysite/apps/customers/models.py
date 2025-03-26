from django.db import models
from apps.leads.models import Lead
from apps.ads.models import Advertisement


class Customer(models.Model):
    """
    Модель клиента.

    Attributes:
        lead (Lead): Потенциальный клиент, связанный с активным клиентом (OneToOneField).
        advertisement (Advertisement): Рекламная кампания,
        связанная с клиентом.
        created_at (datetime): Дата создания клиента.
    """
    lead: Lead = models.OneToOneField(
        'leads.Lead',
        on_delete=models.CASCADE,
        verbose_name='Лид'
    )
    advertisement: Advertisement = models.ForeignKey(
        'ads.Advertisement',
        on_delete=models.CASCADE,
        related_name='customers',
        verbose_name='Рекламная кампания'
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        """
        Метаданные модели.

        Attributes:
            verbose_name (str): Название модели в единственном числе.
            verbose_name_plural (str): Название модели во множественном числе.
            permissions (list[tuple]): Кастомные разрешения для модели.
        """
        verbose_name: str = 'Активный клиент'
        verbose_name_plural: str = 'Активные клиенты'
        permissions: list[tuple[str, str]] = [
            ("can_view_customer", "Может просматривать клиентов"),
            ("can_add_customer", "Может добавлять клиентов"),
            ("can_change_customer", "Может изменять клиентов"),
            ("can_delete_customer", "Может удалять клиентов"),
        ]

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Фамилия и имя лида, связанного с клиентом.
        """
        return f'{self.lead.last_name} {self.lead.first_name}'
