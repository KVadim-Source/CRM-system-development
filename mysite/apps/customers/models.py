from django.db import models

from apps.contracts.models import Contract
from apps.leads.models import Lead


class Customer(models.Model):
    """
    Модель клиента.

    Attributes:
        lead (Lead): Потенциальный клиент, связанный с
        активным клиентом (OneToOneField).
        contract (Contract): Контракт, связанный с клиентом.
    """

    lead: Lead = models.OneToOneField(
        "leads.Lead",
        on_delete=models.CASCADE,
        verbose_name="Потенциальный клиент",
        related_name="customer_leads",
    )
    contract: Contract = models.ForeignKey(
        "contracts.Contract",
        on_delete=models.CASCADE,
        verbose_name="Контракт",
        related_name="customer_contract",
        null=True,
        blank=True
    )

    class Meta:
        """
        Метаданные модели.

        Attributes:
            verbose_name (str): Название модели в единственном числе.
            verbose_name_plural (str): Название модели во множественном числе.
            permissions (list[tuple]): Кастомные разрешения для модели.
        """

        verbose_name: str = "Активный клиент"
        verbose_name_plural: str = "Активные клиенты"
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
            str: Фамилия и имя потенциального клиента, связанного с клиентом.
        """
        return f"{self.lead.last_name} {self.lead.first_name}"
