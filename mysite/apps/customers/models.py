from django.db import models

from apps.contracts.models import Contract
from apps.leads.models import Lead


class Customer(models.Model):
    """
    Модель клиента.

    Attributes:
        lead (Lead): Лид, связанный с
        активным клиентом (OneToOneField).
        contract (Contract): Контракт, связанный с клиентом.
    """

    lead: Lead = models.OneToOneField(
        "leads.Lead",
        on_delete=models.CASCADE,
        verbose_name="Лид",
        related_name="customer_leads",
    )
    contract: Contract = models.ForeignKey(
        "contracts.Contract",
        on_delete=models.CASCADE,
        verbose_name="Контракт",
        related_name="customer_contract",
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

        verbose_name: str = "Активный клиент"
        verbose_name_plural: str = "Активные клиенты"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Фамилия и имя лида, связанного с клиентом.
        """
        return f"{self.lead.last_name} {self.lead.first_name}"
