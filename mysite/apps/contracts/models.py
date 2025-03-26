from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils import timezone
from dateutil.relativedelta import relativedelta

from apps.products.models import Product


def one_month_from_today():
    return timezone.now().date() + relativedelta(months=1)


class Contract(models.Model):
    """
    Модель контракта.

    Attributes:
        name (str): Название контракта.
        product (Product): Предоставляемая услуга.
        document (FileField): Файл с документом.
        start_date (date): Дата начала контракта.
        end_date (date): Дата окончания контракта.
        price (Decimal): Сумма контракта.
    """

    name: str = models.CharField(max_length=200, verbose_name="Название")
    product: Product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        verbose_name="Услуга",
        related_name="contracts",
    )
    start_date: models.DateField = models.DateField(
        verbose_name="Дата начала", default=now
    )
    end_date: models.DateField = models.DateField(
        verbose_name="Дата окончания", default=one_month_from_today
    )
    price: models.DecimalField = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Сумма контракта", default=0.0
    )
    document: models.FileField | None = models.FileField(
        upload_to="media",
        verbose_name="Документ",
        null=True,
        blank=True
    )

    def get_absolute_url(self) -> str:
        """
        Возвращает абсолютный URL-адрес для экземпляра Contract.

        Returns:
            str: URL для просмотра деталей контракта.
        """
        return reverse("contracts:contract_detail", args=[str(self.id)])

    class Meta:
        """
        Метаданные модели.

        Attributes:
            verbose_name (str): Название модели в единственном числе.
            verbose_name_plural (str): Название модели во множественном числе.
            permissions (list[tuple]): Кастомные разрешения для модели.
        """

        verbose_name: str = "Контракт"
        verbose_name_plural: str = "Контракты"
        permissions: list[tuple[str, str]] = [
            ("can_view_contract", "Может просматривать контракты"),
            ("can_add_contract", "Может добавлять контракты"),
            ("can_change_contract", "Может изменять контракты"),
            ("can_delete_contract", "Может удалять контракты"),
        ]

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Название контракта.
        """
        return str(self.name)

    @property
    def cost(self) -> float:
        """
        Возвращает стоимость контракта.

        Returns:
            float: Цена контракта в виде числа с плавающей точкой.
        """
        return float(self.price)
