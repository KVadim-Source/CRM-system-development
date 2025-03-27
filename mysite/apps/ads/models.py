from decimal import Decimal

from django.db import models
from django.db.models import Case, Count, DecimalField, F, Sum, When
from django.db.models.functions import Round
from django.urls import reverse

from apps.products.models import Product


class AdvertisementQuerySet(models.QuerySet):
    """
    Кастомный QuerySet для модели Advertisement.
    """

    def with_stats(self):
        """
        Возвращает QuerySet с дополнительными статистическими данными.

        Returns:
            AdvertisementQuerySet: QuerySet с аннотированными данными.
        """
        return self.annotate(
            leads_count=Count("leads", distinct=True),
            customers_count=Count("leads__customer_leads", distinct=True),
            contracts_sum=Sum(
                "leads__customer_leads__contract__price",
                output_field=models.DecimalField(max_digits=10, decimal_places=2),
            ),
            profit=Round(
                Case(
                    When(budget=0, then=Decimal("0")),
                    default=F("contracts_sum") / F("budget"),
                    output_field=DecimalField(max_digits=10, decimal_places=2),
                ),
                2,
            ),
        )


class AdvertisementManager(models.Manager):
    """
    Кастомный менеджер для модели Advertisement.
    """

    def get_queryset(self):
        """
        Возвращает QuerySet для модели Advertisement.

        Returns:
            AdvertisementQuerySet: QuerySet для модели Advertisement.
        """
        return AdvertisementQuerySet(self.model, using=self._db)

    def with_stats(self):
        """
        Возвращает QuerySet с дополнительными статистическими данными.

        Returns:
            AdvertisementQuerySet: QuerySet с аннотированными данными.
        """
        return self.get_queryset().with_stats()


class Advertisement(models.Model):
    """
    Модель рекламной кампании.

    Attributes:
        name (str): Название кампании.
        product (Product): Продукт, связанный с кампанией.
        channel (str): Канал продвижения.
        budget (Decimal): Бюджет кампании.
    """

    name: str = models.CharField(max_length=200, verbose_name="Название")
    product: Product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        verbose_name="Услуга",
        related_name="advertisements",
    )
    channel: str = models.CharField(max_length=100, verbose_name="Канал продвижения")
    budget: Decimal = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Бюджет"
    )

    objects = AdvertisementManager()

    def get_absolute_url(self) -> str:
        """
        Возвращает абсолютный URL-адрес для экземпляра Advertisement.

        Returns:
            str: URL-адрес для детальной страницы кампании.
        """
        return reverse("ads:advertisement_detail", args=[str(self.id)])

    class Meta:
        """
        Метаданные модели.

        Attributes:
            verbose_name (str): Название модели в единственном числе.
            verbose_name_plural (str): Название модели во множественном числе.
        """

        verbose_name: str = "Рекламная кампания"
        verbose_name_plural: str = "Рекламные кампании"

    def __str__(self) -> str:
        """
        Возвращает название кампании.

        Returns:
            str: Название кампании.
        """
        return str(self.name)
